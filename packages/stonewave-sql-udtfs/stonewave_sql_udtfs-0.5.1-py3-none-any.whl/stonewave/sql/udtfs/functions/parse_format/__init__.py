import pyarrow as pa
import parse
import json
from stonewave.sql.udtfs.base_function import BaseFunction, udtf


@udtf(is_parser=True)
class ParseFormatFunction(BaseFunction):
    def __init__(self):
        self.compiled_format_cache = {}

    def get_name(self):
        return "parse_format"

    def process(self, row_writer, row_idx, args):
        text = args[0]
        pattern_format = args[1]
        compiled_format = None
        if pattern_format in self.compiled_format_cache:
            compiled_format = self.compiled_format_cache[pattern_format]
        else:
            compiled_format = parse.compile(pattern_format)
            self.compiled_format_cache[pattern_format] = compiled_format
        extracted_values = compiled_format.parse(text)

        record_batch_builder = row_writer.record_batch_builder
        if extracted_values:
            for col_name in extracted_values.named:
                record_batch_builder.add_column(col_name, pa.utf8())
                val = extracted_values[col_name]
                if isinstance(val, dict):
                    val = json.dumps(val)
                record_batch_builder.append(col_name, val)

            i = 0
            for v in extracted_values:
                col_name = "a" + str(i)
                record_batch_builder.add_column(col_name, pa.utf8())
                i += 1
                record_batch_builder.append(col_name, v)
            record_batch_builder.increase_row_count()
