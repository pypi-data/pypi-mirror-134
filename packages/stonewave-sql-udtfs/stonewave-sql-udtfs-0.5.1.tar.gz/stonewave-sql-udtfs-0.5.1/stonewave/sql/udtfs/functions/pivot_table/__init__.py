from stonewave.sql.udtfs.base_function import BaseFunction
import pyarrow as pa
import pandas as pd


class PivotTableFunction(BaseFunction):
    def __init__(self):
        self.tables = []
        self.x_field = None
        self.y_name_field = None
        self.y_data_fields = None

    def get_name(self):
        return "pivot_table"

    def process(self, row_writer, row_idx, args):
        if self.x_field == None and len(args) < 4:
            raise Exception(
                "Table function 'pivot_table' parameter invalid: "
                "parameter should be (data_set_name, index_field, "
                "column_name, column_values)"
            )
        batch = args[0]
        if batch is not None:
            self.x_field = args[1]
            self.y_name_field = args[2]
            self.y_data_fields = list(map(str.strip, args[3].split(",")))
            table = pa.Table.from_batches([batch])
            self.tables.append(table)
        else:
            self.pivot(row_writer)

    def pivot(self, row_writer):
        if self.tables:
            table = pa.concat_tables(self.tables, promote=True)
            df = table.to_pandas()
            pvt = pd.pivot_table(
                df,
                values=self.y_data_fields,
                index=self.x_field,
                columns=self.y_name_field,
            )
            pvt.columns = ["{}${}".format(x[0], x[1]) for x in pvt.columns]
            pvt = pvt.reset_index()
            table = pa.Table.from_pandas(pvt, preserve_index=False)
            batches = table.to_batches()
            row_writer.batch_iterator = iter(batches)
        else:
            return
