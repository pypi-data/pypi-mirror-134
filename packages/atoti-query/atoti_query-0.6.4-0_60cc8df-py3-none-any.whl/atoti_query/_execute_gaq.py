from typing import Iterable, Optional

import pandas as pd
from atoti_core import BaseCondition, BaseLevel, BaseMeasure
from typing_extensions import Protocol


class ExecuteGaq(Protocol):
    def __call__(
        self,
        *,
        cube_name: str,
        measures: Iterable[BaseMeasure],
        levels: Iterable[BaseLevel],
        condition: Optional[BaseCondition] = None,
        include_totals: bool,
        scenario: str,
        timeout: int,
    ) -> pd.DataFrame:
        ...
