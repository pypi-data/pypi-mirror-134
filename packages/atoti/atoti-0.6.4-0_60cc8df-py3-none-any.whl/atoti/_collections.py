from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Iterator, MutableSet, TypeVar

_Item = TypeVar("_Item")


# This class is a collection wrapper, it's fine to pass the wrapped collection positionally.

# See https://github.com/python/mypy/issues/5374.
@dataclass(frozen=True)  # type: ignore[misc] # pylint: disable=keyword-only-dataclass
class DelegateMutableSet(MutableSet[_Item]):

    """A set which calls a method each time its elements are changed."""

    _data: MutableSet[_Item] = field(repr=False)

    @abstractmethod
    def _on_change(self) -> None:
        """Hook called each time the data in the set changes."""

    def __contains__(self, value: object) -> bool:
        return value in self._data

    def add(self, value: _Item) -> None:
        self._data.add(value)
        self._on_change()

    def discard(self, value: _Item) -> None:
        self._data.discard(value)
        self._on_change()

    def __iter__(self) -> Iterator[_Item]:
        return iter(self._data)

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return repr(self._data)
