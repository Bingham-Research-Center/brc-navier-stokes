"""Exact heat-rate entropy ledgers for a full frequency corridor."""

from __future__ import annotations

from fractions import Fraction
from math import exp, factorial
import json


BASE_SHELL_EXPONENT = Fraction(7, 4)
PARABOLIC_PREFACTOR_POWER = Fraction(1, 2)


def _positive(value: Fraction, name: str) -> Fraction:
    value = Fraction(value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return value


def finite_dyadic_heat_sum(
    top_heat_rate: Fraction,
    band_count: int,
) -> Fraction:
    """Sum top_rate * sum_{k=0}^{n-1} 4^-k exactly."""
    top = _positive(top_heat_rate, "top_heat_rate")
    if band_count <= 0:
        raise ValueError("band_count must be positive")
    return top * sum(
        (Fraction(1, 4**index) for index in range(band_count)),
        Fraction(0),
    )


def infinite_dyadic_heat_sum(
    top_heat_rate: Fraction,
) -> Fraction:
    """Infinite dyadic heat-rate entropy, equal to 4/3 of the top."""
    top = _positive(top_heat_rate, "top_heat_rate")
    return Fraction(4, 3) * top


def weighted_path_clock_sum(
    initial_heat_budget: Fraction,
    corridor_heat_budget: Fraction,
    depth: int,
) -> Fraction:
    """Sum of simplex clock products over every depth-m corridor path."""
    initial = _positive(initial_heat_budget, "initial_heat_budget")
    corridor = _positive(
        corridor_heat_budget,
        "corridor_heat_budget",
    )
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    return initial * corridor**depth / factorial(depth + 1)


def aggregate_depth_term(
    action: Fraction,
    initial_heat_budget: Fraction,
    corridor_heat_budget: Fraction,
    depth: int,
) -> Fraction:
    """A^(m+1) L H^m/(m+1)! for the full corridor."""
    interaction = _positive(action, "action")
    return (
        interaction ** (depth + 1)
        * weighted_path_clock_sum(
            initial_heat_budget,
            corridor_heat_budget,
            depth,
        )
    )


def aggregate_partial_sum(
    action: Fraction,
    initial_heat_budget: Fraction,
    corridor_heat_budget: Fraction,
    maximum_depth: int,
) -> Fraction:
    """Exact rational partial sum of the full-corridor series."""
    if maximum_depth < 0:
        raise ValueError("maximum_depth must be nonnegative")
    return sum(
        (
            aggregate_depth_term(
                action,
                initial_heat_budget,
                corridor_heat_budget,
                depth,
            )
            for depth in range(maximum_depth + 1)
        ),
        Fraction(0),
    )


def aggregate_closed_form(
    action: Fraction,
    initial_heat_budget: Fraction,
    corridor_heat_budget: Fraction,
) -> float:
    """Closed sum L*(exp(A H)-1)/H."""
    interaction = float(_positive(action, "action"))
    initial = float(
        _positive(initial_heat_budget, "initial_heat_budget")
    )
    corridor = float(
        _positive(corridor_heat_budget, "corridor_heat_budget")
    )
    return initial * (exp(interaction * corridor) - 1) / corridor


def depth_term_ratio(
    action: Fraction,
    corridor_heat_budget: Fraction,
    depth: int,
) -> Fraction:
    """Ratio of the depth-(m+1) term to the depth-m term."""
    interaction = _positive(action, "action")
    corridor = _positive(
        corridor_heat_budget,
        "corridor_heat_budget",
    )
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    return interaction * corridor / (depth + 2)


def parabolic_prefactor_power() -> Fraction:
    """Power of h in S/F when F is parabolic."""
    return PARABOLIC_PREFACTOR_POWER


def corridor_prefactor_power(
    frequency_exponent: Fraction,
) -> Fraction:
    """Power 1-beta for a subparabolic corridor F=h^-beta."""
    beta = _positive(frequency_exponent, "frequency_exponent")
    if beta > Fraction(1, 2):
        raise ValueError(
            "frequency_exponent must be at most one half"
        )
    return 1 - beta


def corridor_stretched_exponent(
    frequency_exponent: Fraction,
) -> Fraction:
    """Forced exponent 11/4-beta for a subparabolic corridor."""
    return (
        BASE_SHELL_EXPONENT
        + corridor_prefactor_power(frequency_exponent)
    )


def parabolic_stretched_exponent() -> Fraction:
    """Dissipation logarithm exponent forced by a corridor floor."""
    return BASE_SHELL_EXPONENT + parabolic_prefactor_power()


def corridor_pressure_power(
    dissipation_log_exponent: Fraction,
) -> Fraction:
    """Power of h in the leading logarithmic parabolic ceiling."""
    exponent = _positive(
        dissipation_log_exponent,
        "dissipation_log_exponent",
    )
    return parabolic_stretched_exponent() - exponent


def main() -> None:
    action = Fraction(3, 2)
    initial_heat_budget = Fraction(2, 3)
    corridor_heat_budget = Fraction(2, 3)
    payload = {
        "experiment": "full subparabolic frequency corridor",
        "finite_eight_band_heat_sum": str(
            finite_dyadic_heat_sum(Fraction(1), 8)
        ),
        "infinite_dyadic_heat_sum": str(
            infinite_dyadic_heat_sum(Fraction(1))
        ),
        "depth_zero_term": str(
            aggregate_depth_term(
                action,
                initial_heat_budget,
                corridor_heat_budget,
                0,
            )
        ),
        "depth_four_term": str(
            aggregate_depth_term(
                action,
                initial_heat_budget,
                corridor_heat_budget,
                4,
            )
        ),
        "closed_series": aggregate_closed_form(
            action,
            initial_heat_budget,
            corridor_heat_budget,
        ),
        "one_quarter_corridor_stretched_exponent": str(
            corridor_stretched_exponent(Fraction(1, 4))
        ),
        "parabolic_stretched_exponent": str(
            parabolic_stretched_exponent()
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
