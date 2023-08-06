from transitions import Machine
from stonewave.sql.udtfs.protocol import ipc
from stonewave.sql.udtfs.protocol.fsm.shared_record_batch_reader import read_record_batch
from stonewave.sql.udtfs.table_row_writer import TableRowWriter
from stonewave.sql.udtfs.constants import PROCESS_ERROR_MSG_TEMPLATE


class EvalFunctionWithTableParamFsm(object):
    states = ["start", "wait_for_next_table_batch", "wait_for_next", "end"]

    def __init__(self, func, batch_sender):
        self.func = func
        self._batch_sender = batch_sender
        self.machine = Machine(model=self, states=EvalFunctionWithTableParamFsm.states, initial="start")

        self.machine.add_transition(
            trigger="eval_with_table_param",
            source="start",
            dest="wait_for_next_table_batch",
            after="eval_params",
        )

        self.machine.add_transition(
            trigger="eval_with_table_param",
            source="wait_for_next_table_batch",
            dest="wait_for_next_table_batch",
            after="eval_params",
        )

        self.machine.add_transition(
            trigger="end_table_param",
            source="wait_for_next_table_batch",
            dest="wait_for_next",
            after="send_next_batch",
        )

        self.machine.add_transition(
            trigger="next",
            source="wait_for_next",
            dest="wait_for_next",
            after="send_next_batch",
        )

        self.machine.add_transition(trigger="end", source="wait_for_next", dest="end", before="end_evaluation")

        self.machine.add_transition(trigger="*", source="end", dest="end", before="end_evaluation")
        self._row_writer = TableRowWriter()
        self.func.initialize(self._row_writer)
        self._batches = []
        self._batch_idx = 0
        self._read_record_batch_func = read_record_batch

    @property
    def read_record_batch_func(self):
        return self._read_record_batch_func

    # a method used for injecting a different function for unit testing purpose
    @read_record_batch_func.setter
    def read_record_batch_func(self, value):
        self._read_record_batch_func = value

    def eval_params(self, params, respond):
        batch = self._read_record_batch_func(params[0])

        params[0] = batch
        try:
            func_name = self.func.get_name()
            if batch is not None:
                self.func.process(self._row_writer, 0, params)
                next_batch = self._row_writer.flush(forced=False)
                if next_batch:
                    self._batches.append(next_batch)
                respond("next_table_batch")
            else:
                self.func.process(self._row_writer, 0, params)
                self.end_table_param(params, respond)
        except Exception as e:
            raise Exception(PROCESS_ERROR_MSG_TEMPLATE.format(func_name, str(e)))

    def send_next_batch(self, params, respond):
        if self._batch_idx < len(self._batches):
            batch = self._batches[self._batch_idx]
            self._batch_idx += 1
            self._batch_sender.send(batch, respond)
            return
        batch = self._row_writer.flush()
        if batch is not None:
            self._batch_sender.send(batch, respond)
            return
        batch = self._row_writer.flush(forced=True)
        if batch is not None:
            self._batch_sender.send(batch, respond)
            return
        self.end(params, respond)

    def end_evaluation(self, params, respond):
        respond("finish")
