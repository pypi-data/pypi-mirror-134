import pandas as pd
from typing_extensions import Literal, Protocol


class QueryMdx(Protocol):
    def __call__(
        self,
        mdx: str,
        *,
        keep_totals: bool = False,
        timeout: int = 30,
        mode: Literal["pretty", "raw"] = "pretty",
    ) -> pd.DataFrame:
        ...
