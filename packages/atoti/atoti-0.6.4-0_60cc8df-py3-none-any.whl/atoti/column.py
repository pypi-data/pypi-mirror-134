from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Dict, Tuple, Union

from atoti_core import BitwiseOperatorsOnly, Identity, keyword_only_dataclass
from typeguard import typeguard_ignore

from ._operation import ColumnOperation, ConditionOperation, Operation
from .type import DataType

if TYPE_CHECKING:
    from .table import Table

# Type for table rows
Row = Union[Tuple[Any, ...], Dict[str, Any]]


@keyword_only_dataclass
@typeguard_ignore
@dataclass(frozen=True, eq=False)
class Column(BitwiseOperatorsOnly):
    """Column of a Table."""

    name: str
    """The name of the column."""

    data_type: DataType
    """The type of the elements in the column."""

    _table: Table = field(repr=False)

    def __mul__(self, other: Any) -> Operation:
        """Multiplication operator."""
        return ColumnOperation(self) * other  # type: ignore[no-any-return]

    def __rmul__(self, other: Any) -> Operation:
        """Multiplication operator."""
        return other * ColumnOperation(self)  # type: ignore[no-any-return]

    def __truediv__(self, other: Any) -> Operation:
        """Division operator."""
        return ColumnOperation(self) / other  # type: ignore[no-any-return]

    def __rtruediv__(self, other: Any) -> Operation:
        """Division operator."""
        return other / ColumnOperation(self)  # type: ignore[no-any-return]

    def __add__(self, other: Any) -> Operation:
        """Addition operator."""
        return ColumnOperation(self) + other  # type: ignore[no-any-return]

    def __radd__(self, other: Any) -> Operation:
        """Addition operator."""
        return other + ColumnOperation(self)  # type: ignore[no-any-return]

    def __sub__(self, other: Any) -> Operation:
        """Subtraction operator."""
        return ColumnOperation(self) - other  # type: ignore[no-any-return]

    def __rsub__(self, other: Any) -> Operation:
        """Subtraction operator."""
        return other - ColumnOperation(self)  # type: ignore[no-any-return]

    def __eq__(  # type: ignore[override]
        self,
        other: Any,
    ) -> ConditionOperation:
        """Equal operator."""
        return ColumnOperation(self) == other  # type: ignore[no-any-return]

    def __ne__(  # type: ignore[override]
        self,
        other: Any,
    ) -> ConditionOperation:
        """Not equal operator."""
        return ColumnOperation(self) != other  # type: ignore[no-any-return]

    def __lt__(self, other: Any) -> ConditionOperation:
        """Lower than operator."""
        return ColumnOperation(self) < other  # type: ignore[no-any-return]

    def __gt__(self, other: Any) -> ConditionOperation:
        """Greater than operator."""
        return ColumnOperation(self) > other  # type: ignore[no-any-return]

    def __le__(self, other: Any) -> ConditionOperation:
        """Lower than or equal operator."""
        return ColumnOperation(self) <= other  # type: ignore[no-any-return]

    def __ge__(self, other: Any) -> ConditionOperation:
        """Greater than or equal operator."""
        return ColumnOperation(self) >= other  # type: ignore[no-any-return]

    def _identity(self) -> Identity:
        return (self.name,) + self._table._identity()
