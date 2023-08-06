import datetime
import math
import sys
from functools import partial, wraps
from typing import Any, Callable, Dict, List, Optional, TypeVar, Union, cast

if sys.version_info >= (3, 8):
    from typing import Protocol
else:  # for Python<3.8
    from typing_extensions import Protocol

import pandas as pd
import stringcase
import tqdm
from more_itertools import chunked

from infima_client.core.models import CoreDate, CoreFactorDate, CoreFactorDateRange
from infima_client.core.types import UNSET

# DateT = TypeVar("DateT", str, datetime.date, pd.Timestamp)
DateT = Union[str, datetime.date, pd.Timestamp]


KNOWN_DATE_COLUMNS = ["asOf", "factorDate", "issueDate", "maturityDate"]


class ResponseMapping(Protocol):
    """Mock class for helping type mapped attributes in Model objects."""

    additional_keys: List[str]

    def __getitem__(self, key: str) -> Any:
        pass


def handle_date(dt: DateT) -> CoreDate:
    """Convert date object to CoreDate."""
    _dt = pd.Timestamp(dt).date()
    return CoreDate(year=_dt.year, month=_dt.month, day=_dt.day)


def handle_factor_date(dt: DateT) -> CoreFactorDate:
    """Convert factor date object to CoreFactorDate."""
    _dt = pd.Timestamp(dt).date()
    if _dt.day != 1:
        raise ValueError("Factor dates are expected to have day=1")
    return CoreFactorDate(year=_dt.year, month=_dt.month)


def handle_factor_date_range(
    start: Optional[DateT], end: Optional[DateT]
) -> Optional[CoreFactorDateRange]:
    """Convert start and end factor date objects to CoreFactorDateRange."""
    if start is None and end is None:
        return None
    else:
        return CoreFactorDateRange(
            start=handle_factor_date(start) if start is not None else UNSET,
            end=handle_factor_date(end) if end is not None else UNSET,
        )


def maybe_parse_known_date_columns(df: pd.DataFrame) -> pd.DataFrame:
    for col in KNOWN_DATE_COLUMNS:
        df = maybe_parse_date_column(df, stringcase.snakecase(col))
        df = maybe_parse_date_column(df, col)
    return df


def maybe_parse_date_column(df: pd.DataFrame, col: str) -> pd.DataFrame:
    if col in df.columns:
        return _parse_nested_date(df, col)
    elif all([f"{col}.{attr}" in df.columns for attr in ["year", "month"]]):
        return _parse_exploded_date(df, col)
    return df


def _parse_nested_date(df: pd.DataFrame, col: str) -> pd.DataFrame:
    dt = df.pop(col)
    exploded = pd.json_normalize(dt)
    if "day" not in exploded.columns:
        exploded["day"] = 1
    df[stringcase.snakecase(col)] = pd.to_datetime(exploded).to_numpy()
    return df


def _parse_exploded_date(df: pd.DataFrame, col: str) -> pd.DataFrame:
    to_drop = []
    dt_args = {}
    for attr in ["year", "month"]:
        c = f"{col}.{attr}"
        to_drop.append(c)
        dt_args[attr] = df[c]

    c = f"{col}.day"
    if f"{col}.day" in df.columns:
        to_drop.append(c)
        dt_args["day"] = df[c]
    else:
        dt_args["day"] = 1

    df[stringcase.snakecase(col)] = pd.to_datetime(dt_args).to_numpy()
    return df.drop(to_drop, axis=1)


def maybe_get_column(df: pd.DataFrame, col: Optional[str] = None) -> pd.DataFrame:
    if col is None or col not in df.columns:
        return df
    return df[[col]]


def maybe_wide(df: pd.DataFrame, on: Optional[str] = None) -> pd.DataFrame:
    if on is None or on not in df.index.names:
        return df
    return df.unstack(on)


def model_to_frame(model: Any, record_path: List[str], meta: List[str]) -> pd.DataFrame:
    df = pd.json_normalize(model.to_dict(), record_path=record_path, meta=meta)
    if len(df) == 0:
        return df

    df = df.pipe(maybe_parse_known_date_columns).rename(columns=stringcase.snakecase)
    return df


def response_mapping_to_frame(
    mapping: ResponseMapping,
    record_path: List[str],
    meta: List[str],
    index_cols: List[str],
    col: Optional[str] = "cpr",
    wide_on: Optional[str] = None,
) -> Optional[pd.DataFrame]:
    frames = [
        model_to_frame(mapping[key], record_path, meta)
        for key in mapping.additional_keys
    ]
    if frames:
        out = pd.concat(frames, ignore_index=True)
        if out.empty:
            return out
        else:
            return (
                out.set_index(index_cols)
                .pipe(maybe_get_column, col=col)
                .pipe(maybe_wide, on=wide_on)
            )
    else:
        return None


def nested_dict_to_frame(
    data: Dict[str, Dict[str, Any]],
    path: str,
    set_index: bool = True,
) -> Optional[pd.DataFrame]:
    def _recurse(
        data: Dict[str, Dict[str, Any]], keys: List[str], meta: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        records = []
        key = keys[0]
        keys_remain = keys[1:]

        is_final = len(keys_remain) == 0  # on last level
        is_wild = "(*)" in key  # is a wildcard key
        key = key.replace("(*)", "")

        if is_wild:
            # wildcard keys mean the dict keys should become values in an index level
            for idx, val in data.items():
                meta[key] = idx  # update the meta data with the key value
                if is_final:
                    # objs from the last level should be records
                    val.update(meta)
                    records.append(val)
                else:
                    # keep recursing but with updated meta
                    records.extend(_recurse(val, keys_remain, meta))
        else:
            # regular keys should be recursed into
            records.extend(_recurse(data[key], keys_remain, meta))

        return records

    keys = path.split("->")
    recs = _recurse(data, keys, {})

    index_levels = [k.replace("(*)", "") for k in keys if "(*)" in k]

    if recs:
        df = (
            pd.DataFrame.from_records(recs)
            .pipe(maybe_parse_known_date_columns)
            .rename(columns=stringcase.snakecase)
        )
        if set_index:
            df = df.set_index(index_levels)
        return df
    else:
        return None


def simple_dict_to_frame(
    data: Dict[str, Any],
    index_name: str,
) -> Optional[pd.DataFrame]:
    if not data:
        return None
    df = (
        pd.DataFrame.from_dict(data, orient="index")
        .pipe(maybe_parse_known_date_columns)
        .rename(columns=stringcase.snakecase)
    )
    df.index = df.index.rename(index_name)
    return df


MAX_BATCH_SIZE = 5_000

T = TypeVar("T")
FChunker = Callable[..., T]


class Catter(Protocol):
    def __call__(self, vals: List[T]) -> T:
        ...


def chunker(
    col: str, catter: Catter, size: int = MAX_BATCH_SIZE
) -> Callable[[FChunker[T]], FChunker[T]]:
    assert size <= MAX_BATCH_SIZE

    def _deco(func: FChunker[T]) -> FChunker[T]:
        @wraps(func)
        def _chunked_func(*args: Any, **kwargs: Any) -> T:
            items = kwargs.pop(col)
            it = chunked(items, size)

            progress: bool = kwargs.pop("progress", False)
            if progress and len(items) > size:
                it = tqdm.tqdm(it, total=math.ceil(len(items) / size))

            coll: List[T] = []
            for chunk in it:
                kwargs[col] = chunk
                coll.append(func(*args, **kwargs))

            return catter(coll)

        return _chunked_func

    return _deco


frame_catter = cast(Catter, partial(pd.concat, ignore_index=False, axis=0))

frame_chunker = cast(
    Callable[..., Callable[[FChunker[T]], FChunker[T]]],
    partial(chunker, catter=frame_catter),
)
