from __future__ import annotations

from typing import TYPE_CHECKING

from .._path_utils import to_absolute_path
from . import DataSource

if TYPE_CHECKING:
    from .._java_api import JavaApi
    from ..table import Table


class ArrowDataSource(DataSource):
    def __init__(self, java_api: JavaApi):
        super().__init__(java_api, "ARROW")

    def load_arrow_into_table(
        self,
        *,
        table: Table,
        path: str,
    ) -> None:
        self.load_data_into_table(
            table.name,
            scenario_name=table.scenario,
            source_params={
                "absolutePath": to_absolute_path(path),
                "isTemporaryFile": True,
            },
        )
