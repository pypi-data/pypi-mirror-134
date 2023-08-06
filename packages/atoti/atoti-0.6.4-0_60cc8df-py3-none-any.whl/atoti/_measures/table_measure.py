from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Iterable, Optional

from atoti_core import keyword_only_dataclass

from ..measure_description import MeasureDescription

if TYPE_CHECKING:
    from .._java_api import JavaApi
    from ..column import Column
    from ..level import Level
    from ..table import Table


@keyword_only_dataclass
@dataclass(eq=False)
class TableMeasure(MeasureDescription):
    """Measure based on the column of a table."""

    _column: Column
    _agg_fun: str
    _table: Table = field(repr=False)

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        return java_api.aggregated_measure(
            cube_name=cube_name,
            measure_name=measure_name,
            table_name=self._table.name,
            column_name=self._column.name,
            agg_function=self._agg_fun,
            required_levels=[],
        )


@keyword_only_dataclass
@dataclass(eq=False)
class SingleValueTableMeasure(MeasureDescription):
    """Single value aggregated measure based on the column of a table."""

    _column: Column
    _levels: Optional[Iterable[Level]] = None

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        table = self._column._table
        # levels = [] if self._levels is None else self._levels

        distilled_name = java_api.value_measure(
            cube_name=cube_name,
            measure_name=measure_name,
            table_name=table.name,
            column_name=self._column.name,
            column_type=self._column.data_type,
            required_levels=self._levels,
        )

        return distilled_name
