from stonewave.sql.udtfs.table_row_writer import TableRowWriter
from stonewave.sql.udtfs.protocol.fsm.apply import _lateral_join, _get_row


def _equal_length_apply(func, left_table, column_name_qualifier, func_params):
    # this can only be used with outer apply
    # only table function writing results row by row with a batch builder can correctly function here
    right_table_writer = TableRowWriter()
    func.initialize(right_table_writer)

    right_table = None
    for i in range(0, left_table.num_rows):
        row = _get_row(left_table, i, func_params)
        try:
            func.process(right_table_writer, i, row)
            if right_table_writer.builder_row_count() <= i:
                right_table_writer.record_batch_builder.append_null_row()
        except Exception as e:
            right_table_writer.record_batch_builder.append_null_row()
    right_table = right_table_writer.flush(forced=True)
    joined_table = _lateral_join(left_table, right_table, column_name_qualifier)
    return joined_table
