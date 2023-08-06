from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from atoti_core import LevelCoordinates, get_java_coordinates

from ..measure_description import MeasureDescription

if TYPE_CHECKING:
    from .._java_api import JavaApi


@dataclass(eq=False)  # pylint: disable=keyword-only-dataclass
class LevelMeasure(MeasureDescription):
    """Measure based on a cube level."""

    _level_coordinates: LevelCoordinates

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        distilled_name = java_api.create_measure(
            cube_name,
            measure_name,
            "LEVEL",
            get_java_coordinates(self._level_coordinates),
        )
        return distilled_name
