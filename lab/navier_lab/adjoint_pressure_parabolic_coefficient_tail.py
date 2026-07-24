"""Power ledger for the parabolic coefficient-tail theorem.

This module checks algebraic exponents only.  The analytic estimates are
proved in the accompanying dossier note.
"""

from __future__ import annotations

import math


def resolvent_factor(kappa: float, growth: float = 1.0) -> float:
    """Return the model half-order Volterra resolvent bound."""
    if kappa < 0 or growth <= 0:
        raise ValueError("kappa must be nonnegative and growth positive")
    return math.exp(growth * kappa * kappa)


def low_pressure_bound(
    h: float,
    kappa: float,
    *,
    growth: float = 1.0,
    constant: float = 1.0,
) -> float:
    """Model C exp(A kappa^2) h^(7/4) low-coefficient pressure."""
    if not 0 < h <= 1 or constant <= 0:
        raise ValueError("require 0 < h <= 1 and constant > 0")
    return constant * resolvent_factor(kappa, growth) * h ** (7.0 / 4.0)


def comparison_prefactor(
    h: float,
    kappa: float,
    *,
    growth: float = 1.0,
    constant: float = 1.0,
) -> float:
    """Coefficient multiplying sqrt(D_tail) in the comparison."""
    if not 0 < h <= 1 or constant <= 0:
        raise ValueError("require 0 < h <= 1 and constant > 0")
    return constant * resolvent_factor(kappa, growth) * h ** (3.0 / 2.0)


def tail_floor(
    h: float,
    kappa: float,
    pressure: float,
    *,
    growth: float = 1.0,
    constant: float = 1.0,
) -> float:
    """Invert the comparison after half the pressure floor remains."""
    if pressure <= 0:
        raise ValueError("pressure must be positive")
    prefactor = comparison_prefactor(
        h, kappa, growth=growth, constant=constant
    )
    return (pressure / (2.0 * prefactor)) ** 2


def logarithmic_kappa(h: float, epsilon: float, growth: float = 1.0) -> float:
    """Choose A kappa^2 = (epsilon/2) log(1/h)."""
    if not 0 < h < 1:
        raise ValueError("require 0 < h < 1")
    if not 0 < epsilon < 1 or growth <= 0:
        raise ValueError("require 0 < epsilon < 1 and growth > 0")
    return math.sqrt(epsilon * math.log(1.0 / h) / (2.0 * growth))


def superparabolic_cutoff(h: float, epsilon: float, growth: float = 1.0) -> float:
    """Return kappa_epsilon(h) h^(-1/2)."""
    return logarithmic_kappa(h, epsilon, growth) / math.sqrt(h)


def logarithmic_tail_power(epsilon: float) -> float:
    """Power p in the lower bound h^p after the logarithmic choice."""
    if not 0 < epsilon < 1:
        raise ValueError("require 0 < epsilon < 1")
    return -3.0 + epsilon


def main() -> None:
    h = 1.0e-8
    epsilon = 0.2
    growth = 1.5
    kappa = logarithmic_kappa(h, epsilon, growth)
    print(f"kappa={kappa:.6g}")
    print(f"cutoff/parabolic={kappa:.6g}")
    print(f"low-pressure power={7 / 4 - epsilon / 2:.6g}")
    print(f"tail power={logarithmic_tail_power(epsilon):.6g}")


if __name__ == "__main__":
    main()
