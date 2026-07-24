"""Exact exponent ledger for one separated returned-low Oseen step."""

from __future__ import annotations

from fractions import Fraction
import json


BASE_SHELL_EXPONENT = Fraction(7, 4)
PARABOLIC_FREQUENCY_EXPONENT = Fraction(1, 2)
SOURCE_RADIUS_EXPONENT = Fraction(3, 1)


def _positive(value: Fraction, name: str) -> Fraction:
    value = Fraction(value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return value


def heat_clock_gain_power(frequency_exponent: Fraction) -> Fraction:
    """Power from min(1,F^2 h) when F=h^-beta."""
    beta = _positive(frequency_exponent, "frequency_exponent")
    return max(Fraction(0), 1 - 2 * beta)


def one_return_prefactor_power(
    frequency_exponent: Fraction,
) -> Fraction:
    """Power of h in F^-1 min(1,F^2 h)."""
    beta = _positive(frequency_exponent, "frequency_exponent")
    return beta + heat_clock_gain_power(beta)


def one_return_stretched_exponent(
    frequency_exponent: Fraction,
) -> Fraction:
    """Exponent gamma forced by a fixed one-return pressure floor."""
    beta = _positive(frequency_exponent, "frequency_exponent")
    return BASE_SHELL_EXPONENT + one_return_prefactor_power(beta)


def direct_high_state_exponent(
    frequency_exponent: Fraction,
) -> Fraction:
    """Reviewed direct terminal high-state stretched exponent."""
    beta = _positive(frequency_exponent, "frequency_exponent")
    return BASE_SHELL_EXPONENT + beta


def one_return_pressure_power(
    frequency_exponent: Fraction,
    dissipation_log_exponent: Fraction,
) -> Fraction:
    """Power of h in the leading one-return pressure ceiling."""
    beta = _positive(frequency_exponent, "frequency_exponent")
    gamma = _positive(
        dissipation_log_exponent,
        "dissipation_log_exponent",
    )
    return (
        BASE_SHELL_EXPONENT
        + one_return_prefactor_power(beta)
        - gamma
    )


def physical_zoom_prefactor_exponent() -> Fraction:
    """Polynomial prefactor in the forced physical zoom ceiling."""
    return SOURCE_RADIUS_EXPONENT


def main() -> None:
    subparabolic = Fraction(1, 16)
    parabolic = PARABOLIC_FREQUENCY_EXPONENT
    payload = {
        "experiment": "one separated returned-low Oseen step",
        "subparabolic_frequency_exponent": str(subparabolic),
        "subparabolic_heat_clock_gain": str(
            heat_clock_gain_power(subparabolic)
        ),
        "subparabolic_stretched_exponent": str(
            one_return_stretched_exponent(subparabolic)
        ),
        "parabolic_frequency_exponent": str(parabolic),
        "parabolic_stretched_exponent": str(
            one_return_stretched_exponent(parabolic)
        ),
        "parabolic_minimum": str(Fraction(9, 4)),
        "physical_zoom_prefactor_exponent": str(
            physical_zoom_prefactor_exponent()
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
