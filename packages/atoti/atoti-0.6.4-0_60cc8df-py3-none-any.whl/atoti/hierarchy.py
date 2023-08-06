from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Callable, Mapping, Tuple

from atoti_core import BaseHierarchy, keyword_only_dataclass
from typeguard import typeguard_ignore

from ._hierarchy_isin_condition import HierarchyIsinCondition
from .level import Level

if TYPE_CHECKING:
    from ._java_api import JavaApi


@keyword_only_dataclass
@typeguard_ignore
@dataclass(eq=False)
class Hierarchy(BaseHierarchy[Level]):
    """Hierarchy of a :class:`~atoti.cube.Cube`.

    A hierarchy is a sub category of a :attr:`~dimension` and represents a precise type of data.

    For example, :guilabel:`Quarter` or :guilabel:`Week` could be hierarchies in the :guilabel:`Time` dimension.
    """

    _name: str
    _levels: Mapping[str, Level]
    _dimension: str
    _slicing: bool
    _cube_name: str
    _java_api: JavaApi = field(repr=False)
    _visible: bool
    _update_hierarchies: Callable[[Mapping[Tuple[str, str], Mapping[str, Level]]], None]

    @property
    def name(self) -> str:
        return self._name

    @property
    def levels(self) -> Mapping[str, Level]:
        return self._levels

    @levels.setter
    def levels(self, value: Mapping[str, Level]) -> None:
        """Levels setter."""
        self._levels = value
        self._update_hierarchies({(self._dimension, self.name): value})

    @property
    def dimension(self) -> str:
        return self._dimension

    @dimension.setter
    def dimension(self, value: str) -> None:
        """Dimension setter."""
        self._java_api.update_hierarchy_coordinate(
            cube_name=self._cube_name,
            hierarchy=self,
            new_dim=value,
            new_hier=self._name,
        )
        self._java_api.refresh()
        self._dimension = value

    @property
    def slicing(self) -> bool:
        return self._slicing

    @slicing.setter
    def slicing(self, value: bool) -> None:
        """Slicing setter."""
        self._java_api.update_hierarchy_slicing(self, value)
        self._java_api.refresh()
        self._slicing = value

    @property
    def visible(self) -> bool:
        """Whether the hierarchy is visible or not."""
        return self._visible

    @visible.setter
    def visible(self, value: bool) -> None:
        """Visibility setter."""
        self._java_api.set_hierarchy_visibility(
            cube_name=self._cube_name,
            dimension=self._dimension,
            name=self._name,
            visible=value,
        )
        self._java_api.refresh()
        self._visible = value

    def isin(self, *member_paths: Tuple[Any, ...]) -> HierarchyIsinCondition:
        return HierarchyIsinCondition(
            hierarchy_coordinates=(self.dimension, self.name),
            level_names=list(self.levels),
            member_paths=member_paths,
        )
