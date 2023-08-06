from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from .._py4j_utils import as_java_object
from ..measure_description import LiteralMeasureValue, MeasureDescription

if TYPE_CHECKING:
    from .._java_api import JavaApi


@dataclass(eq=False)  # pylint: disable=keyword-only-dataclass
class LiteralMeasure(MeasureDescription):
    """A measure equal to a literal value."""

    _value: LiteralMeasureValue

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        val = as_java_object(self._value, gateway=java_api.gateway)
        distilled_name = java_api.create_measure(
            cube_name, measure_name, "LITERAL", val
        )
        return distilled_name
