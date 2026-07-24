"""Ledgers for smooth-layer LP--Dyson corridor identification.

The analytic theorem is in
``dossier/experiments/adjoint-pressure-corridor-identification.md``.
This module checks only its exact scalar coefficients and frequency
power bookkeeping.
"""

from __future__ import annotations

from fractions import Fraction
from math import gamma
import json


BASE_SHELL_EXPONENT = Fraction(7, 4)
PARABOLIC_CAPTURE_POWER = Fraction(1, 2)


def _nonnegative(value: Fraction, name: str) -> Fraction:
    value = Fraction(value)
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")
    return value


def fractional_volterra_coefficient(
    size: Fraction,
    depth: int,
) -> float:
    """Return x^m/Gamma(m/2+1), the C_t L2 Dyson majorant."""
    x = _nonnegative(size, "size")
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    return float(x**depth) / gamma(Fraction(depth, 2) + 1)


def fractional_volterra_partial_sum(
    size: Fraction,
    maximum_depth: int,
) -> float:
    """Partial Mittag--Leffler sum for the fractional Volterra bound."""
    if maximum_depth < 0:
        raise ValueError("maximum_depth must be nonnegative")
    return sum(
        fractional_volterra_coefficient(size, depth)
        for depth in range(maximum_depth + 1)
    )


def corridor_word_weight(
    low_weight: Fraction,
    depth: int,
) -> Fraction:
    """Weight of the unique all-low binary word at depth m."""
    low = _nonnegative(low_weight, "low_weight")
    if low > 1:
        raise ValueError("low_weight must be at most one")
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    return low**depth


def exit_word_weight(
    low_weight: Fraction,
    depth: int,
) -> Fraction:
    """Total weight of depth-m words containing at least one exit."""
    low = _nonnegative(low_weight, "low_weight")
    if low > 1:
        raise ValueError("low_weight must be at most one")
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    return 1 - low**depth


def first_exit_word_weight(
    low_weight: Fraction,
    depth: int,
) -> Fraction:
    """Sum q(1+p+...+p^(m-1)) for the first-exit location."""
    low = _nonnegative(low_weight, "low_weight")
    if low > 1:
        raise ValueError("low_weight must be at most one")
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    if depth == 0:
        return Fraction(0)
    high = 1 - low
    return high * sum(
        (low**index for index in range(depth)),
        Fraction(0),
    )


def finite_initial_band_sum(
    lowest_frequency: Fraction,
    highest_frequency: Fraction,
) -> Fraction:
    """Sum dyadic F from F_* through U, inclusive."""
    lowest = _nonnegative(lowest_frequency, "lowest_frequency")
    highest = _nonnegative(highest_frequency, "highest_frequency")
    if lowest == 0 or highest == 0:
        raise ValueError("frequencies must be positive")
    if highest < lowest:
        raise ValueError(
            "highest_frequency must be at least lowest_frequency"
        )
    ratio = highest / lowest
    if ratio.denominator != 1:
        raise ValueError("frequency ratio must be an integer power of two")
    integer_ratio = ratio.numerator
    if integer_ratio & (integer_ratio - 1):
        raise ValueError("frequency ratio must be an integer power of two")
    band_count = integer_ratio.bit_length()
    return lowest * (2**band_count - 1)


def finite_inverse_initial_band_sum(
    lowest_frequency: Fraction,
    highest_frequency: Fraction,
) -> Fraction:
    """Sum F^-1 over the same finite dyadic interval."""
    lowest = _nonnegative(lowest_frequency, "lowest_frequency")
    highest = _nonnegative(highest_frequency, "highest_frequency")
    if lowest == 0 or highest == 0:
        raise ValueError("frequencies must be positive")
    if highest < lowest:
        raise ValueError(
            "highest_frequency must be at least lowest_frequency"
        )
    ratio = highest / lowest
    if ratio.denominator != 1:
        raise ValueError("frequency ratio must be an integer power of two")
    integer_ratio = ratio.numerator
    if integer_ratio & (integer_ratio - 1):
        raise ValueError("frequency ratio must be an integer power of two")
    band_count = integer_ratio.bit_length()
    return sum(
        (
            Fraction(1, lowest * 2**index)
            for index in range(band_count)
        ),
        Fraction(0),
    )


def aggregate_initial_band_power(
    ceiling_exponent: Fraction,
) -> Fraction:
    """Power of h in h U when U=h^-alpha."""
    alpha = _nonnegative(ceiling_exponent, "ceiling_exponent")
    return 1 - alpha


def forced_stretched_exponent(
    ceiling_exponent: Fraction,
) -> Fraction:
    """Shell exponent plus the aggregate h U prefactor power."""
    return (
        BASE_SHELL_EXPONENT
        + aggregate_initial_band_power(ceiling_exponent)
    )


def parabolic_forced_stretched_exponent() -> Fraction:
    """The parabolic capture endpoint, equal to 9/4."""
    return BASE_SHELL_EXPONENT + PARABOLIC_CAPTURE_POWER


def main() -> None:
    payload = {
        "experiment": "smooth-layer corridor identification",
        "fractional_sum_x_1_depth_20": (
            fractional_volterra_partial_sum(Fraction(1), 20)
        ),
        "depth_six_corridor_weight_p_3_4": str(
            corridor_word_weight(Fraction(3, 4), 6)
        ),
        "depth_six_exit_weight_p_3_4": str(
            exit_word_weight(Fraction(3, 4), 6)
        ),
        "depth_six_first_exit_weight_p_3_4": str(
            first_exit_word_weight(Fraction(3, 4), 6)
        ),
        "initial_band_sum_16_to_1024": str(
            finite_initial_band_sum(Fraction(16), Fraction(1024))
        ),
        "parabolic_capture_power": str(
            aggregate_initial_band_power(Fraction(1, 2))
        ),
        "parabolic_stretched_exponent": str(
            parabolic_forced_stretched_exponent()
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
