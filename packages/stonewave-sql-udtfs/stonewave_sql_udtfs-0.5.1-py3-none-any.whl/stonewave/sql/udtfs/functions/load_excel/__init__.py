import pyarrow as pa
import pandas as pd
from stonewave.sql.udtfs.logger import logger
from stonewave.sql.udtfs.base_function import BaseFunction
from stonewave.sql.udtfs.base_dataloader import BaseDataloader


class LoadExcelFunction(BaseFunction, BaseDataloader):
    def __init__(self):
        BaseDataloader.__init__(self)

    def get_name(self):
        return "load_excel"

    def process(self, row_writer, row_idx, args):
        excel_file = args[0]
        sheet_name = [c.strip() for c in args[1].split(",")] if len(args) > 1 and args[1] != "" else None
        logger.debug(
            "executing load_excel table function",
            excel_file=excel_file,
            sheet_name=sheet_name,
        )
        try:
            self.set_path(excel_file)
            excel_file_path = self.get_path()

            excel_data = pd.read_excel(
                excel_file_path,
                sheet_name=sheet_name,
                engine="openpyxl",
                dtype=str,
            )

            sheets = []
            for sheet_name, df in excel_data.items():
                # trim spaces in column names
                df.columns = df.columns.str.strip()
                table = pa.Table.from_pandas(df, preserve_index=False)
                batches = table.to_batches()
                if batches:
                    sheets.append(batches[0])
            row_writer.batch_iterator = iter(sheets)
        except Exception as e:
            logger.error("failed to load excel file", error=str(e))
