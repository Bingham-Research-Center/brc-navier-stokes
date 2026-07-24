"""Exact ledgers for one prescribed multistage Oseen itinerary."""

from __future__ import annotations

from fractions import Fraction
from math import factorial
import json

from navier_lab.adjoint_pressure_one_return import (
    one_return_prefactor_power,
    one_return_stretched_exponent,
)


def _positive(value: Fraction, name: str) -> Fraction:
    value = Fraction(value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return value


def ratio_product(frequencies: tuple[Fraction, ...]) -> Fraction:
    """Product of successive input/output ratios, equal to R0/Rm."""
    if not frequencies:
        raise ValueError("frequencies must be nonempty")
    scales = tuple(
        _positive(value, "frequency") for value in frequencies
    )
    product = Fraction(1)
    for source, target in zip(scales, scales[1:]):
        product *= source / target
    return product


def path_prefactor(
    initial_frequency: Fraction,
    output_frequency: Fraction,
    action: Fraction,
    transitions_after_first_return: int,
) -> Fraction:
    """A^(m+1) S/R0 in the uniform-constant path bound."""
    initial = _positive(initial_frequency, "initial_frequency")
    output = _positive(output_frequency, "output_frequency")
    interaction = _positive(action, "action")
    if transitions_after_first_return < 0:
        raise ValueError(
            "transitions_after_first_return must be nonnegative"
        )
    return (
        interaction ** (transitions_after_first_return + 1)
        * output
        / initial
    )


def simplex_clock_bound(
    horizon: Fraction,
    rates: tuple[Fraction, ...],
) -> Fraction:
    """Simplex ceiling for P(sum of independent exponentials <= h)."""
    h = _positive(horizon, "horizon")
    if not rates:
        raise ValueError("rates must be nonempty")
    rate_product = Fraction(1)
    for rate in rates:
        rate_product *= _positive(rate, "rate")
    ceiling = h ** len(rates) * rate_product / factorial(len(rates))
    return min(Fraction(1), ceiling)


def dyadic_square_product_exponent(
    transitions_after_first_return: int,
) -> int:
    """Power of 2 in prod R_j^2/R_0^(2(m+1)) for R_j=2^-j R0."""
    m = transitions_after_first_return
    if m < 0:
        raise ValueError(
            "transitions_after_first_return must be nonnegative"
        )
    return -m * (m + 1)


def slow_dyadic_clock_ceiling(clock_count: int) -> Fraction:
    """Ceiling 2^-n(n-1)/n! for n consecutive slow dyadic clocks."""
    if clock_count <= 0:
        raise ValueError("clock_count must be positive")
    n = clock_count
    return Fraction(1, 2 ** (n * (n - 1)) * factorial(n))


def log_depth_stretched_exponent(
    frequency_exponent: Fraction,
    interaction_loss: Fraction,
) -> Fraction:
    """Forced exponent after a polynomial loss from logarithmic depth.

    The loss must be smaller than the bare scale-clock prefactor power.
    That strict condition makes every non-logarithmic source term vanish.
    """
    beta = _positive(frequency_exponent, "frequency_exponent")
    loss = Fraction(interaction_loss)
    if loss < 0:
        raise ValueError("interaction_loss must be nonnegative")
    if loss >= one_return_prefactor_power(beta):
        raise ValueError(
            "interaction_loss must be smaller than the "
            "one-return prefactor power"
        )
    return one_return_stretched_exponent(beta) - loss


def main() -> None:
    frequencies = (
        Fraction(64),
        Fraction(32),
        Fraction(8),
        Fraction(2),
    )
    payload = {
        "experiment": "one prescribed multistage Oseen itinerary",
        "frequency_ratio_product": str(ratio_product(frequencies)),
        "endpoint_ratio": str(frequencies[0] / frequencies[-1]),
        "zero_extra_transition_prefactor": str(
            path_prefactor(
                Fraction(64),
                Fraction(1),
                Fraction(3, 2),
                0,
            )
        ),
        "three_extra_transition_prefactor": str(
            path_prefactor(
                Fraction(64),
                Fraction(1),
                Fraction(3, 2),
                3,
            )
        ),
        "dyadic_square_product_exponent_m3": (
            dyadic_square_product_exponent(3)
        ),
        "four_slow_dyadic_clock_ceiling": str(
            slow_dyadic_clock_ceiling(4)
        ),
        "parabolic_log_depth_exponent_loss_one_quarter": str(
            log_depth_stretched_exponent(
                Fraction(1, 2),
                Fraction(1, 4),
            )
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
