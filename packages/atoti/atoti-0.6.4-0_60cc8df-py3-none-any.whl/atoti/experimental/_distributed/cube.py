from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Iterable

from atoti_core import JavaType, LevelCoordinates
from typeguard import typeguard_ignore

from ..._local_cube import LocalCube
from ...aggregates_cache import AggregatesCache
from .hierarchies import DistributedHierarchies
from .levels import DistributedLevels
from .measures import DistributedMeasures

if TYPE_CHECKING:
    from ..._java_api import JavaApi
    from .session import DistributedSession


class DistributedCube(
    LocalCube[DistributedHierarchies, DistributedLevels, DistributedMeasures]
):
    """Cube of a distributed session."""

    @typeguard_ignore
    def __init__(self, name: str, *, java_api: JavaApi, session: DistributedSession):
        """Init."""
        super().__init__(
            name=name,
            java_api=java_api,
            session=session,
            hierarchies=DistributedHierarchies(_java_api=java_api, _cube=self),
            level_function=lambda hierarchies: DistributedLevels(hierarchies),
            measures=DistributedMeasures(_java_api=java_api, _cube_name=name),
            agg_cache=AggregatesCache(
                _cube_name=name,
                _set_capacity=java_api.set_aggregates_cache_capacity,
                _get_capacity=java_api.get_aggregates_cache_capacity,
            ),
        )

    def _get_level_java_types(  # pylint: disable=no-self-use
        self, levels_coordinates: Iterable[LevelCoordinates]
    ) -> Dict[LevelCoordinates, JavaType]:
        return {level_coordinates: "Object" for level_coordinates in levels_coordinates}
