from stonewave.sql.udtfs.logger import logger
from stonewave.sql.udtfs.base_function import BaseFunction
from datetime import datetime, timezone


class GenerateUnionFunction(BaseFunction):
    data_types = [
        ("null", lambda i: None),
        ("int", lambda i: i),
        ("float", lambda i: float(i)),
        ("bool", lambda i: bool(i)),
        ("string", lambda i: str(i)),
        ("timestamp", lambda i: datetime.fromtimestamp(i / 1e6, timezone.utc)),
        ("list<string>", lambda i: [str(i)]),
    ]

    def __init__(self):
        pass

    def get_name(self):
        return "generate_union"

    def process(self, row_writer, row_idx, args):
        rng = range(0, args[0])
        types = [i.strip() for i in args[1].split(",")]
        array = []
        for idx, data_type in enumerate(GenerateUnionFunction.data_types):
            parsed_indices = []
            for idx_ts, type_str in enumerate(types):
                if type_str == data_type[0]:
                    array.extend([data_type[1](i) for i in rng])
                    parsed_indices.append(idx_ts)
            for i in reversed(parsed_indices):
                types.pop(i)
        record_batch_builder = row_writer.record_batch_builder
        col_name = "generate_union"
        record_batch_builder.add_column(col_name)
        record_batch_builder.extend(col_name, array)
        row_count = len(array)
        record_batch_builder.increase_row_count(row_count)
        logger.debug(
            "rows generated via generate_union",
            row_count=row_count,
            builder_row_count=record_batch_builder.row_count(),
        )
