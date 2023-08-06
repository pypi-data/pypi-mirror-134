from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Dict, Mapping, Tuple, TypeVar, Union

from atoti_core import (
    BaseHierarchies,
    BaseHierarchy,
    HierarchyKey,
    keyword_only_dataclass,
)

from ._delegate_mutable_mapping import DelegateMutableMapping
from .level import Level

if TYPE_CHECKING:
    from ._java_api import JavaApi
    from ._local_cube import LocalCube
    from .column import Column
    from .hierarchy import Hierarchy

    LevelOrColumn = Union[Level, Column]

_BaseHierarchy = TypeVar("_BaseHierarchy", bound=BaseHierarchy[Any])


@keyword_only_dataclass
# See https://github.com/python/mypy/issues/5374.
@dataclass(frozen=True)  # type: ignore[misc]
class LocalHierarchies(
    DelegateMutableMapping[Tuple[str, str], _BaseHierarchy],
    BaseHierarchies[_BaseHierarchy],
):
    """Local hierarchies class."""

    _java_api: JavaApi = field(repr=False)

    @abstractmethod
    def _get_underlying(self) -> Dict[Tuple[str, str], _BaseHierarchy]:
        """Fetch the hierarchies from the JVM each time they are needed."""

    def _update(self, other: Mapping[Tuple[str, str], _BaseHierarchy]) -> None:
        raise AttributeError(f"{self._get_name()} cube hierarchies cannot be changed.")

    def __delitem__(self, key: HierarchyKey) -> None:
        """Delete the hierarchy.

        Args:
            key: The name of the hierarchy to delete.
        """
        raise AttributeError(f"{self._get_name()} cube hierarchies cannot be changed")

    def _get_name(self) -> str:
        return self.__class__.__name__.replace("Hierarchies", "")

    @staticmethod
    def _retrieve_hierarchies(
        java_api: JavaApi, cube: LocalCube[Any, Any, Any]
    ) -> Dict[Tuple[str, str], Hierarchy]:
        """Retrieve the hierarchies from the cube."""
        return java_api.retrieve_hierarchies(
            cube_name=cube.name,
            convert_to_python_hierarchies=cube._convert_to_python_hierarchies,
        )
