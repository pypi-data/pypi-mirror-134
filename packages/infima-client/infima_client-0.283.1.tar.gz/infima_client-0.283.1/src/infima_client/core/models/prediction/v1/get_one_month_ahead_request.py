from typing import (
    Any,
    BinaryIO,
    Dict,
    List,
    Optional,
    TextIO,
    Tuple,
    Type,
    TypeVar,
    Union,
    cast,
)

from attr import define, field

from infima_client.core.models.core.factor_date_range import CoreFactorDateRange
from infima_client.core.types import UNSET, Unset

T = TypeVar("T", bound="PredictionV1GetOneMonthAheadRequest")


@define(auto_attribs=True)
class PredictionV1GetOneMonthAheadRequest:
    """
    Attributes:
        symbols (List[str]): Pool and cohort names to fetch historical prepayment predictions. Example: 31417EUD1.
        factor_date_range (Union[Unset, CoreFactorDateRange]):
    """

    symbols: List[str]
    factor_date_range: Union[Unset, CoreFactorDateRange] = UNSET
    additional_properties: Dict[str, Any] = field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        symbols = self.symbols

        factor_date_range: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.factor_date_range, Unset):
            factor_date_range = self.factor_date_range.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbols": symbols,
            }
        )
        if factor_date_range is not UNSET:
            field_dict["factorDateRange"] = factor_date_range

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        symbols = cast(List[str], d.pop("symbols"))

        _factor_date_range = d.pop("factorDateRange", UNSET)
        factor_date_range: Union[Unset, CoreFactorDateRange]
        if isinstance(_factor_date_range, Unset):
            factor_date_range = UNSET
        else:
            factor_date_range = CoreFactorDateRange.from_dict(_factor_date_range)

        prediction_v1_get_one_month_ahead_request = cls(
            symbols=symbols,
            factor_date_range=factor_date_range,
        )

        prediction_v1_get_one_month_ahead_request.additional_properties = d
        return prediction_v1_get_one_month_ahead_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
