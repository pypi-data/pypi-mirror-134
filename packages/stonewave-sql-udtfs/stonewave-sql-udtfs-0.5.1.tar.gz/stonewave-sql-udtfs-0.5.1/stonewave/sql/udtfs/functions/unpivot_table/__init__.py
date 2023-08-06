from stonewave.sql.udtfs.base_function import BaseFunction
import pyarrow as pa


class UnpivotTableFunction(BaseFunction):
    def __init__(self):
        self.tables = []
        self.x_field = None
        self.y_name_field = None
        self.y_data_field = None

    def get_name(self):
        return "unpivot_table"

    def process(self, row_writer, row_idx, args):
        if self.x_field == None and len(args) < 4:
            raise Exception(
                "Table function 'unpivot_table' parameter invalid: "
                "parameter should be (data_set_name, index_field, "
                "column_name, column_value_name)"
            )
        batch = args[0]
        if batch is not None:
            self.x_field = args[1]
            self.y_name_field = args[2]
            self.y_data_field = args[3]
            table = pa.Table.from_batches([batch])
            # FIXME: the current implementation caches all batches, which is not necessary
            self.tables.append(table)
        else:
            self.unpivot(row_writer)

    def unpivot(self, row_writer):
        if self.tables:
            table = pa.concat_tables(self.tables, promote=True)
            df = table.to_pandas()
            unpvt = df.melt(
                id_vars=self.x_field,
                var_name=self.y_name_field,
                value_name=self.y_data_field,
            )
            unpvt_table = pa.Table.from_pandas(unpvt, preserve_index=False)
            batches = unpvt_table.to_batches()
            row_writer.batch_iterator = iter(batches)
        else:
            return
