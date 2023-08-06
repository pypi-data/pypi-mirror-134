from enum import Enum
from typing import Dict, Optional, Tuple, Union

import pydantic

from classiq_interface.generator.function_params import FunctionParams
from classiq_interface.generator.preferences.optimization import (
    StatePrepOptimizationMethod,
)
from classiq_interface.generator.range_types import NonNegativeFloatRange
from classiq_interface.helpers.custom_pydantic_types import pydanticProbabilityFloat


class Metrics(str, Enum):
    KL = "KL"
    L2 = "L2"
    L1 = "L1"
    MAX_PROBABILITY = "MAX_PROBABILITY"


def is_power_of_two(pmf):
    n = len(pmf)
    is_power_of_two = (n != 0) and (n & (n - 1) == 0)
    if not is_power_of_two:
        raise ValueError("Probabilities length must be power of 2")
    return pmf


class PMF(pydantic.BaseModel):
    pmf: Tuple[pydanticProbabilityFloat, ...]

    @pydantic.validator("pmf")
    def is_sum_to_one(cls, pmf):
        # n = len(pmf)
        # is_power_of_two = (n != 0) and (n & (n - 1) == 0)
        # if not is_power_of_two:
        #     raise ValueError("Probabilities length must be power of 2")
        if round(sum(pmf), 8) != 1:
            raise ValueError("Probabilities do not sum to 1")
        return pmf

    _is_pmf_valid = pydantic.validator("pmf", allow_reuse=True)(is_power_of_two)


class GaussianMoments(pydantic.BaseModel):
    mu: float
    sigma: pydantic.PositiveFloat


class GaussianMixture(pydantic.BaseModel):
    gaussian_moment_list: Tuple[GaussianMoments, ...]


class StatePreparation(FunctionParams):
    probabilities: Union[PMF, GaussianMixture]
    depth_range: Optional[NonNegativeFloatRange] = NonNegativeFloatRange(
        lower_bound=0, upper_bound=1e100
    )
    cnot_count_range: Optional[NonNegativeFloatRange] = NonNegativeFloatRange(
        lower_bound=0, upper_bound=1e100
    )
    error_metric: Optional[Dict[Metrics, NonNegativeFloatRange]] = pydantic.Field(
        default_factory=lambda: {
            Metrics.KL: NonNegativeFloatRange(lower_bound=0, upper_bound=1e100)
        }
    )
    optimization_method: Optional[
        StatePrepOptimizationMethod
    ] = StatePrepOptimizationMethod.KL
    num_qubits: Optional[int] = None
    is_uniform_start: bool = True

    @pydantic.validator("is_uniform_start")
    def is_uniform_start_validator(cls, is_uniform_start, values):
        if is_uniform_start:
            return is_uniform_start

        if Metrics.KL in values.get("error_metric", dict()):
            raise ValueError("Error Metric for non-uniform start can be L1 ans L2")
        if StatePrepOptimizationMethod.KL == values.get("optimization_method"):
            raise ValueError(
                "Optimization method for non-uniform start can be L1 ans L2"
            )
        return is_uniform_start

    @pydantic.root_validator()
    def validate_num_qubits(cls, values):
        num_qubits = values.get("num_qubits")
        probabilities = values.get("probabilities")
        if isinstance(probabilities, GaussianMixture) and num_qubits is None:
            raise ValueError("num_qubits must be set when using gaussian mixture")

        return values

    class Config:
        extra = "forbid"
