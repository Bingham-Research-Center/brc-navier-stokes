"""Exponent ledger for the spatial-shell/frequency-tail amplification."""

from __future__ import annotations

from fractions import Fraction
import json


BASE_SHELL_EXPONENT = Fraction(7, 4)
SOURCE_RADIUS_EXPONENT = Fraction(3, 1)
OFF_DIAGONAL_TIME_EXPONENT = Fraction(6, 1)


def _nonnegative(value: Fraction, name: str) -> Fraction:
    value = Fraction(value)
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")
    return value


def amplified_stretched_exponent(
    frequency_exponent: Fraction,
) -> Fraction:
    """Return gamma forced by F=h^(-beta).

    The shell-frequency estimate is

        P_hi <= (S/F) h^(7/4) log(D h^3).

    Thus an order-one high-tail packet forces
    ``log(D h^3)`` at exponent ``7/4+beta``.
    """
    beta = _nonnegative(frequency_exponent, "frequency_exponent")
    return BASE_SHELL_EXPONENT + beta


def high_tail_pressure_power(
    frequency_exponent: Fraction,
    dissipation_log_exponent: Fraction,
) -> Fraction:
    """Power of h in the leading high-tail pressure ceiling."""
    beta = _nonnegative(frequency_exponent, "frequency_exponent")
    gamma = _nonnegative(
        dissipation_log_exponent,
        "dissipation_log_exponent",
    )
    return BASE_SHELL_EXPONENT + beta - gamma


def inner_high_tail_power(frequency_exponent: Fraction) -> Fraction:
    """Power of the source-cutoff high-tail contribution S/F."""
    return _nonnegative(frequency_exponent, "frequency_exponent")


def off_diagonal_error_power(frequency_exponent: Fraction) -> Fraction:
    """Power after choosing two off-diagonal kernel moments.

    Before the outer S/F factor, the error is h^6 F^-2.  For
    F=h^-beta the complete power is 6+3 beta.
    """
    beta = _nonnegative(frequency_exponent, "frequency_exponent")
    return OFF_DIAGONAL_TIME_EXPONENT + 3 * beta


def quadratic_terminal_toll_exponent(
    frequency_exponent: Fraction,
) -> Fraction:
    """Power d in the polynomial floor D >= h^(-d)."""
    beta = _nonnegative(frequency_exponent, "frequency_exponent")
    return SOURCE_RADIUS_EXPONENT + 2 * beta


def physical_zoom_prefactor_exponent() -> Fraction:
    """Polynomial prefactor in sigma=o(h^3 exp(-c h^-gamma))."""
    return SOURCE_RADIUS_EXPONENT


def main() -> None:
    beta = Fraction(1, 16)
    gamma = amplified_stretched_exponent(beta)
    payload = {
        "experiment": "spatial shell and frequency tail amplification",
        "frequency_exponent": str(beta),
        "amplified_stretched_exponent": str(gamma),
        "critical_pressure_power": str(
            high_tail_pressure_power(beta, gamma)
        ),
        "subcritical_pressure_power": str(
            high_tail_pressure_power(beta, BASE_SHELL_EXPONENT)
        ),
        "inner_high_tail_power": str(inner_high_tail_power(beta)),
        "off_diagonal_error_power": str(off_diagonal_error_power(beta)),
        "quadratic_terminal_toll_exponent": str(
            quadratic_terminal_toll_exponent(beta)
        ),
        "physical_zoom_prefactor_exponent": str(
            physical_zoom_prefactor_exponent()
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
