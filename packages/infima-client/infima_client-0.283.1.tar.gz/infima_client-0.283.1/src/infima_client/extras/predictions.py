from typing import TYPE_CHECKING, List, Optional, Union, cast

import pandas as pd

from infima_client.core.types import Unset

if TYPE_CHECKING:
    from infima_client.client import InfimaClient

from .utils import (
    DateT,
    ResponseMapping,
    frame_chunker,
    handle_date,
    response_mapping_to_frame,
)


@frame_chunker("symbols")
def get_predictions(
    *,
    client: "InfimaClient",
    symbols: List[str],
    as_of: Optional[DateT] = None,
    col: Optional[str] = "cpr",
    wide: bool = True,
) -> Optional[pd.DataFrame]:
    resp = client.api.prediction_v1.get(
        symbols=symbols,
        as_of=handle_date(as_of) if as_of is not None else None,
    )

    mapping = cast(Union[ResponseMapping, Unset], resp.predictions)
    if isinstance(mapping, Unset):
        return None
    else:
        record_path = ["values"]
        meta = ["asOf", "symbol"]
        index_cols = ["as_of", "symbol", "factor_date"]
        wide_on = "factor_date" if wide else None

        return response_mapping_to_frame(
            mapping, record_path, meta, index_cols, col=col, wide_on=wide_on
        )
