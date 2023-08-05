from datetime import date
from textwrap import indent
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from infima_client.client import InfimaClient


def demo(client: "InfimaClient") -> None:  # 5,2021
    """
    Demo for pool and cohort predictions and realization functions
    """

    def _headline(msg: str) -> None:
        n = ((60 - len(msg)) // 2) - 2
        pre = post = " " + "=" * n + " "
        print("\n" + pre + msg + post + "\n")

    def _statement(msg: str) -> None:
        pre = ">>> "
        print(pre + msg)

    def _assignment(name: str, vals: Any) -> None:
        _statement(f"{name} = {vals}")

    def _output(msg: str) -> None:
        print("\n" + indent(msg, "    ") + "\n")

    as_of = date.fromisoformat("2021-10-28")
    pools = ["3133AE2D5", "3133AE2K9", "3133AE2U7", "3133AE3J1", "3133AE3S1"]
    cohorts = [
        "FNCL 1.5 2021",
        "FNCL 2.0 2021",
        "FNCL 2.5 2021",
        "FNCL 3.0 2021",
        "FNCL 3.5 2021",
    ]

    _headline("Demo of InfimaClient usage")
    _assignment("pools", pools)
    _assignment("cohorts", cohorts)
    _assignment("as_of", as_of)

    _headline("pool predictions")
    df = client.get_predictions(symbols=pools, as_of=as_of)
    _statement("df = client.get_predictions(symbols=pools, as_of=as_of)")

    if df is not None:
        _output(df.to_string())

    _headline("pool realizations")
    start = date.fromisoformat("2017-01-01")
    end = date.fromisoformat("2021-12-01")
    _assignment("start", start)
    _assignment("end", end)
    df = client.get_pool_actuals(cusips=pools, start=start, end=end)
    _statement("df = client.get_pool_actuals(cusips=pools, start=start, end=end)")

    if df is not None:
        _output(df.to_string())

    _headline("cohort predictions")
    df = client.get_predictions(symbols=cohorts, as_of=as_of)
    _statement("df = client.get_predictions(symbols=cohorts, as_of=as_of)")

    if df is not None:
        _output(df.to_string())

    _headline("cohort realizations")
    start = date.fromisoformat("2017-01-01")
    end = date.fromisoformat("2021-12-01")
    _assignment("start", start)
    _assignment("end", end)
    df = client.get_cohort_actuals(cohorts=cohorts, start=start, end=end)
    _statement("df = client.get_cohort_actuals(cohorts=cohorts, start=start, end=end)")

    if df is not None:
        _output(df.to_string())
