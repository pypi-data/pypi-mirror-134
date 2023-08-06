from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Dict

from atoti_core import keyword_only_dataclass
from typeguard import typeguard_ignore

from ._local_cubes import LocalCubes
from .cube import Cube

if TYPE_CHECKING:
    from .session import Session


@keyword_only_dataclass
@typeguard_ignore
@dataclass(frozen=True)
class Cubes(LocalCubes[Cube]):
    """Manage the cubes of the session."""

    _session: Session = field(repr=False)  # type: ignore[assignment]

    def __getitem__(self, key: str) -> Cube:
        """Get the cube with the given name."""
        return self._session._retrieve_cube(key)

    def _get_underlying(self) -> Dict[str, Cube]:
        return self._session._retrieve_cubes()
