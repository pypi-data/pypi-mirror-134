from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, Callable, Dict, Iterable, List, Optional, TypeVar

import pandas as pd
from atoti_core import (
    BASE_SCENARIO_NAME,
    QUERY_DOC,
    BaseCondition,
    BaseCube,
    BaseLevel,
    BaseMeasure,
    Identity,
    JavaType,
    LevelCoordinates,
    LevelsT,
    doc,
    generate_mdx,
    get_query_args_doc,
)
from typing_extensions import Literal

from ._condition import Condition
from ._docs_utils import EXPLAIN_QUERY_DOC
from ._java_api import JavaApi
from ._local_hierarchies import LocalHierarchies
from ._local_measures import LocalMeasures
from ._query_plan import QueryAnalysis
from ._runtime_type_checking_utils import typecheck
from .aggregates_cache import AggregatesCache
from .hierarchy import Hierarchy

if TYPE_CHECKING:
    from ._local_session import LocalSession

_LocalMeasures = TypeVar("_LocalMeasures", bound=LocalMeasures[Any])
_LocalHierarchies = TypeVar("_LocalHierarchies", bound=LocalHierarchies[Any])


@typecheck
class LocalCube(BaseCube[_LocalHierarchies, LevelsT, _LocalMeasures]):
    """Local cube class."""

    def __init__(
        self,
        name: str,
        *,
        java_api: JavaApi,
        session: LocalSession[Any],
        hierarchies: _LocalHierarchies,
        level_function: Callable[[_LocalHierarchies], LevelsT],
        measures: _LocalMeasures,
        agg_cache: AggregatesCache,
    ):
        """Init."""
        super().__init__(_name=name, _hierarchies=hierarchies, _measures=measures)
        self._session = session
        self._java_api = java_api
        self._levels: LevelsT = level_function(hierarchies)
        self._agg_cache = agg_cache

    @property
    def name(self) -> str:
        """Name of the cube."""
        return self._name

    @property
    def hierarchies(self) -> _LocalHierarchies:
        """Hierarchies of the cube."""
        return self._hierarchies

    @property
    def levels(self) -> LevelsT:
        """Levels of the cube."""
        return self._levels

    @property
    def measures(self) -> _LocalMeasures:
        """Measures of the cube."""
        return self._measures

    @property
    def aggregates_cache(self) -> AggregatesCache:
        """Aggregates cache of the cube."""
        return self._agg_cache

    @abstractmethod
    def _get_level_java_types(
        self, levels_coordinates: Iterable[LevelCoordinates]
    ) -> Dict[LevelCoordinates, JavaType]:
        ...

    @doc(QUERY_DOC, args=get_query_args_doc(is_query_session=False))
    def query(
        self,
        *measures: BaseMeasure,
        condition: Optional[BaseCondition] = None,
        include_totals: bool = False,
        levels: Iterable[BaseLevel] = (),
        mode: Literal["pretty", "raw"] = "pretty",
        scenario: str = BASE_SCENARIO_NAME,
        timeout: int = 30,
    ) -> pd.DataFrame:
        if mode == "pretty":
            mdx = generate_mdx(
                cube_name=self.name,
                hierarchies=self.hierarchies,
                condition=condition,
                include_totals=include_totals,
                levels=levels,
                measures=measures,
                scenario=scenario,
            )
            query_result = self._session.query_mdx(
                mdx, keep_totals=include_totals, mode=mode, timeout=timeout
            )
            return query_result

        # Execute the query without going through `QueryCube.query()` to avoid fetching the discovery.
        return self._session._create_query_session()._execute_gaq(
            cube_name=self.name,
            measures=measures,
            levels=levels,
            condition=condition,
            include_totals=include_totals,
            scenario=scenario,
            timeout=timeout,
        )

    @doc(EXPLAIN_QUERY_DOC, corresponding_method="query")
    def explain_query(
        self,
        *measures: BaseMeasure,
        condition: Optional[Condition] = None,
        include_totals: bool = False,
        levels: Iterable[BaseLevel] = (),
        scenario: str = BASE_SCENARIO_NAME,
        timeout: int = 30,
    ) -> QueryAnalysis:
        mdx = generate_mdx(
            cube_name=self.name,
            hierarchies=self.hierarchies,
            condition=condition,
            include_totals=include_totals,
            levels=levels,
            measures=measures,
            scenario=scenario,
        )
        return self._java_api.analyse_mdx(mdx, timeout)

    def _convert_to_python_hierarchies(
        self, java_hierarchies: Iterable[Any]
    ) -> List[Hierarchy]:
        hierarchies = []
        for java_hierarchy in java_hierarchies:
            hierarchy = Hierarchy(
                _name=java_hierarchy.getName(),
                _levels=JavaApi._convert_from_java_levels(java_hierarchy.getLevels()),
                _dimension=java_hierarchy.getDimensionName(),
                _slicing=java_hierarchy.getSlicing(),
                _cube_name=self.name,
                _java_api=self._java_api,
                _visible=java_hierarchy.getVisible(),
                _update_hierarchies=self.hierarchies.update,
            )
            for level in hierarchy.levels.values():
                level._hierarchy = hierarchy
            hierarchies.append(hierarchy)
        return hierarchies

    def _identity(self) -> Identity:
        return (
            self._name,
            self._session.name,
        )
