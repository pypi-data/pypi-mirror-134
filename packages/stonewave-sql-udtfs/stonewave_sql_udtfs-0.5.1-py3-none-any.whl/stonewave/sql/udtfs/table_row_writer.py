from stonewave.sql.udtfs.record_batch_builder import RecordBatchBuilder


class TableRowWriter(object):
    """
    Use the row writer to write results produced from a table function. There are two major ways to write results:
    1) get `record_batch_builder` and write the produced rows row by row. See `RecordBatchBuilder`'s API for details.
    2) set `batch_iterator` that will produce a list of record batches.
    The `batch_iterator` MUST be a generator that calling its next method will return a pyarrow's RecordBatch
    """

    def __init__(self, flushing_batch_size=8 * 1024):
        self._flushing_batch_size = flushing_batch_size
        self._record_batch_builder = RecordBatchBuilder()
        self._batch_iterator = None
        self._current_builder_row_count = 0
        self._last_flushed_batch_size = 0
        self._new_rows_count = 0

    @property
    def record_batch_builder(self):
        return self._record_batch_builder

    @record_batch_builder.setter
    def record_batch_builder(self, value):
        self._record_batch_builder = value

    @property
    def batch_iterator(self):
        return self._batch_iterator

    @batch_iterator.setter
    def batch_iterator(self, value):
        self._batch_iterator = value

    def builder_row_count(self):
        return self.record_batch_builder.row_count()

    def is_not_empty(self):
        return self.batch_iterator or self.record_batch_builder.row_count() > 0

    def append_row(self, row):
        self._record_batch_builder.append_row(row)

    def append_rows(self, rows):
        for row in rows:
            self._record_batch_builder.append_row(row)

    def flush(self, forced=False):
        self._before_flush()
        flushed_batch = None
        if self.batch_iterator:
            batch = self.record_batch_builder.flush()
            if batch is not None:
                flushed_batch = batch
            else:
                try:
                    flushed_batch = next(self.batch_iterator)
                except StopIteration:
                    self.batch_iterator = None
                    return None
        elif self._is_over_flushing_size() or forced and self.record_batch_builder.row_count() > 0:
            flushed_batch = self.record_batch_builder.flush()

        self._last_flushed_batch_size = flushed_batch.num_rows if flushed_batch else 0
        self._after_flush()
        return flushed_batch

    ##################################################
    # APIs below are internal and is subject to change
    ##################################################
    @property
    def new_rows_count(self):
        """
        :return: the number of new rows after processing a new row or flushing results
        """
        return self._new_rows_count

    def _before_process(self):
        self._current_builder_row_count = self.record_batch_builder.row_count()

    def _after_process(self):
        self._new_rows_count = self.record_batch_builder.row_count() - self._current_builder_row_count

    def _before_flush(self):
        self._current_builder_row_count = self.record_batch_builder.row_count()

    def _after_flush(self):
        self._new_rows_count = (
            self.record_batch_builder.row_count() + self._last_flushed_batch_size - self._current_builder_row_count
        )

    def _is_over_flushing_size(self):
        return self.record_batch_builder.row_count() >= self._flushing_batch_size
