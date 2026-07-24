"""Exact ledgers for the no-chargeable-return parabolic corridor."""

from __future__ import annotations

from fractions import Fraction
from math import factorial
import json


DIRECT_SOURCE_TIME_POWER = Fraction(3, 4)


def _positive(value: Fraction, name: str) -> Fraction:
    value = Fraction(value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return value


def direct_source_integrated_power() -> Fraction:
    """Integrating the reviewed t^(3/4) source adds one time power."""
    return DIRECT_SOURCE_TIME_POWER + 1


def dyadic_heat_budget(top_rate: Fraction) -> Fraction:
    """Sum all dyadic heat rates Q^2 below a top output band."""
    rate = _positive(top_rate, "top_rate")
    return Fraction(4, 3) * rate


def direct_source_frequency_telescope(
    initial_frequency: Fraction,
    continuation_frequencies: tuple[Fraction, ...],
    pressure_frequency: Fraction,
) -> Fraction:
    """Telescope source, transition, and final-pressure frequencies.

    The normalised direct source contributes 1/F.  Each continuation
    contributes R_previous/R_next, and the pressure contributes S R_last.
    """
    initial = _positive(initial_frequency, "initial_frequency")
    pressure = _positive(pressure_frequency, "pressure_frequency")
    factor = Fraction(1, 1) / initial
    previous = initial
    for index, frequency in enumerate(continuation_frequencies):
        current = _positive(frequency, f"continuation_frequencies[{index}]")
        factor *= previous / current
        previous = current
    return factor * pressure * previous


def aggregate_depth_term(
    action: Fraction,
    heat_budget: Fraction,
    depth: int,
) -> Fraction:
    """The all-band clock sum at continuation depth m."""
    action_value = _positive(action, "action")
    budget = _positive(heat_budget, "heat_budget")
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    clocks = depth + 1
    return (action_value * budget) ** clocks / factorial(clocks)


def aggregate_depth_ratio(
    action: Fraction,
    heat_budget: Fraction,
    depth: int,
) -> Fraction:
    """Ratio of consecutive all-band clock terms."""
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    action_value = _positive(action, "action")
    budget = _positive(heat_budget, "heat_budget")
    return action_value * budget / (depth + 2)


def parabolic_no_return_pressure_power() -> Fraction:
    """Power left after all frequencies below h^-1/2 are summed."""
    return direct_source_integrated_power()


def main() -> None:
    action = Fraction(3, 2)
    budget = Fraction(2, 5)
    payload = {
        "experiment": "no-chargeable-return parabolic corridor",
        "direct_source_integrated_power": str(
            direct_source_integrated_power()
        ),
        "dyadic_heat_budget_for_unit_top_rate": str(
            dyadic_heat_budget(Fraction(1))
        ),
        "frequency_telescope": str(
            direct_source_frequency_telescope(
                Fraction(64),
                (Fraction(16), Fraction(32), Fraction(4)),
                Fraction(1),
            )
        ),
        "depth_four_aggregate_term": str(
            aggregate_depth_term(action, budget, 4)
        ),
        "depth_four_successive_ratio": str(
            aggregate_depth_ratio(action, budget, 4)
        ),
        "parabolic_pressure_power": str(
            parabolic_no_return_pressure_power()
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
