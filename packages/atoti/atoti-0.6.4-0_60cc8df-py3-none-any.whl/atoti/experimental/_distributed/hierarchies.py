from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Dict, Mapping, Tuple, Union

from atoti_core import HierarchyKey, keyword_only_dataclass
from atoti_query import QueryHierarchy, QueryLevel
from typeguard import typechecked, typeguard_ignore

from ..._local_hierarchies import LocalHierarchies
from ...hierarchy import Hierarchy
from ...level import Level

if TYPE_CHECKING:
    from ...column import Column
    from .cube import DistributedCube

    LevelOrColumn = Union[Level, Column]


def _cube_hierarchy_to_query_hierarchy(hierarchy: Hierarchy) -> QueryHierarchy:
    """Convert a cube hierarchy into a query hierarchy."""
    return QueryHierarchy(
        _name=hierarchy.name,
        _dimension=hierarchy.dimension,
        _levels=to_query_levels(hierarchy.levels),
        _slicing=hierarchy.slicing,
    )


def _cube_level_to_query_level(level: Level) -> QueryLevel:
    """Convert a cube level into a query level."""
    return QueryLevel(
        _name=level.name, _dimension=level.dimension, _hierarchy=level.hierarchy
    )


def to_query_levels(levels: Mapping[str, Level]) -> Mapping[str, QueryLevel]:
    """Convert a dict of cube levels into a dict of query levels."""
    return {
        levelName: _cube_level_to_query_level(levels[levelName])
        for levelName in levels
        if levelName != "ALL"
    }


@keyword_only_dataclass
@typeguard_ignore
@dataclass(frozen=True)
class DistributedHierarchies(
    LocalHierarchies[QueryHierarchy],
):
    """Manage the hierarchies."""

    _cube: DistributedCube = field(repr=False)

    def _get_underlying(self) -> Dict[Tuple[str, str], QueryHierarchy]:
        hierarchies = self._retrieve_hierarchies(self._java_api, self._cube)
        return {
            hierarchyCoordinate: _cube_hierarchy_to_query_hierarchy(
                hierarchies[hierarchyCoordinate]
            )
            for hierarchyCoordinate in hierarchies
        }

    @typechecked
    def __getitem__(self, key: HierarchyKey) -> QueryHierarchy:
        (dimension_name, hierarchy_name) = self._convert_key(key)
        cube_hierarchies = self._java_api.retrieve_hierarchy(
            hierarchy_name,
            cube_name=self._cube.name,
            dimension=dimension_name,
            convert_to_python_hierarchies=self._cube._convert_to_python_hierarchies,
        )
        hierarchies = [_cube_hierarchy_to_query_hierarchy(h) for h in cube_hierarchies]
        if len(hierarchies) == 0:
            raise KeyError(f"Unknown hierarchy: {key}")
        if len(hierarchies) == 1:
            return hierarchies[0]
        raise self._multiple_hierarchies_error(key, hierarchies)
