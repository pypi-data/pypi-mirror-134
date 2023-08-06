from dataclasses import dataclass
from typing import Iterable, Optional

import pandas as pd
from atoti_core import (
    BASE_SCENARIO_NAME,
    QUERY_DOC,
    BaseCondition,
    BaseCube,
    BaseLevel,
    BaseMeasure,
    doc,
    generate_mdx,
    get_query_args_doc,
    keyword_only_dataclass,
)
from typeguard import typechecked, typeguard_ignore
from typing_extensions import Literal

from ._execute_gaq import ExecuteGaq
from ._query_mdx import QueryMdx
from ._widget_conversion_details import WidgetConversionDetails
from .query_hierarchies import QueryHierarchies
from .query_levels import QueryLevels
from .query_measures import QueryMeasures


@keyword_only_dataclass
@typeguard_ignore
@dataclass(frozen=True)
class QueryCube(BaseCube[QueryHierarchies, QueryLevels, QueryMeasures]):
    """Query cube."""

    _hierarchies: QueryHierarchies
    _measures: QueryMeasures
    _execute_gaq: Optional[ExecuteGaq]
    _query_mdx: QueryMdx

    @property
    def levels(self) -> QueryLevels:
        """Levels of the cube."""
        return QueryLevels(self.hierarchies)

    @doc(QUERY_DOC, args=get_query_args_doc(is_query_session=True))
    @typechecked
    def query(
        self,
        *measures: BaseMeasure,
        condition: Optional[BaseCondition] = None,
        include_totals: bool = False,
        levels: Iterable[BaseLevel] = (),
        mode: Literal["pretty", "raw"] = "pretty",
        scenario: str = BASE_SCENARIO_NAME,
        timeout: int = 30
    ) -> pd.DataFrame:
        if mode == "raw" and self._execute_gaq:
            return self._execute_gaq(
                cube_name=self.name,
                measures=measures,
                levels=levels,
                condition=condition,
                include_totals=include_totals,
                scenario=scenario,
                timeout=timeout,
            )

        mdx = generate_mdx(
            cube_name=self.name,
            condition=condition,
            hierarchies=self.hierarchies,
            include_totals=include_totals,
            levels=levels,
            measures=measures,
            scenario=scenario,
        )

        query_result = self._query_mdx(
            mdx, keep_totals=include_totals, mode=mode, timeout=timeout
        )

        # Always use an MDX including totals because ActiveUI 5 then relies on context values to show/hide totals.
        if not include_totals and query_result._atoti_widget_conversion_details:
            query_result._atoti_widget_conversion_details = WidgetConversionDetails(
                mdx=generate_mdx(
                    cube_name=self.name,
                    condition=condition,
                    hierarchies=self.hierarchies,
                    include_totals=True,
                    levels=levels,
                    measures=measures,
                    scenario=scenario,
                ),
                session_id=query_result._atoti_widget_conversion_details.session_id,
                widget_creation_code=query_result._atoti_widget_conversion_details.widget_creation_code,
            )

        return query_result
