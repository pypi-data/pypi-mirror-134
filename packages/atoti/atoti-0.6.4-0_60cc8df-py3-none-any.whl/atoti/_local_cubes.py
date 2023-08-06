from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Mapping, TypeVar

from atoti_core import BaseCubes, keyword_only_dataclass

from ._delegate_mutable_mapping import DelegateMutableMapping
from ._local_cube import LocalCube

if TYPE_CHECKING:
    from ._local_session import LocalSession

_LocalCube = TypeVar("_LocalCube", bound="LocalCube[Any, Any, Any]", covariant=True)


@keyword_only_dataclass
# See https://github.com/python/mypy/issues/5374.
@dataclass(frozen=True)  # type: ignore[misc]
class LocalCubes(DelegateMutableMapping[str, _LocalCube], BaseCubes[_LocalCube]):
    """Local cubes class."""

    _session: LocalSession[LocalCubes[_LocalCube]] = field(repr=False)

    def _update(  # pylint: disable=no-self-use
        self, other: Mapping[str, _LocalCube]
    ) -> None:
        raise NotImplementedError("Use Session.create_cube() to create a cube.")

    def __delitem__(self, key: str) -> None:
        """Delete the cube with the given name."""
        try:
            self._session._java_api.delete_cube(key)
            self._session._java_api.refresh()
        except KeyError:
            raise Exception(f"No cube named {key}") from None
