"""Exact exponent ledger for fixed causal feedback interaction depth."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from typing import Dict


def _validate_order(order: int, *, allow_zero: bool = True) -> None:
    lower = 0 if allow_zero else 1
    if isinstance(order, bool) or not isinstance(order, int) or order < lower:
        relation = "nonnegative" if allow_zero else "positive"
        raise ValueError(f"order must be a {relation} integer")


def l1_exponent(order: int) -> Fraction:
    """Return A_m for the m-th iterate, with u_0=q."""
    _validate_order(order)
    return Fraction(7, 4) - Fraction(3, 2) * Fraction(1, 3**order)


def lorentz_exponent(order: int) -> Fraction:
    """Return B_m for the L^(3/2,1) time bound."""
    _validate_order(order)
    return Fraction(5, 4) - Fraction(1, 2) * Fraction(1, 3**order)


def inner_tail_time_exponent(order: int) -> Fraction:
    """Return beta_m in the squared exterior L2 tail for m >= 1."""
    _validate_order(order, allow_zero=False)
    return Fraction(11, 2) - Fraction(1, 3 ** (order - 1))


def recurrence_residual(order: int) -> Fraction:
    """Check A_m - A_(m-1)/3 - 7/6 exactly."""
    _validate_order(order, allow_zero=False)
    return l1_exponent(order) - l1_exponent(order - 1) / 3 - Fraction(7, 6)


def intermediate_pressure_powers(
    order: int,
    alpha: Fraction = Fraction(1, 10),
) -> Dict[str, Fraction]:
    """Return all h powers after intermediate coefficient localisation."""
    _validate_order(order, allow_zero=False)
    if not isinstance(alpha, Fraction):
        alpha = Fraction(alpha)
    if alpha <= 0:
        raise ValueError("alpha must be positive")
    beta = inner_tail_time_exponent(order)
    return {
        "near_local_energy": Fraction(3, 2) - alpha / 2,
        "near_cutoff": Fraction(2, 1) + alpha / 2,
        "far_inner_source": beta / 2 - Fraction(3, 2) + 5 * alpha / 2,
        "far_stable_first": Fraction(1, 2) + 7 * alpha / 2,
        "far_stable_second": -Fraction(1, 4) + 15 * alpha / 2,
        "source_radius_gap": Fraction(3, 1) - alpha,
    }


def exterior_shell_powers(order: int) -> Dict[str, Fraction]:
    """Return h powers after dyadic summation from R_src=h^-3."""
    _validate_order(order, allow_zero=False)
    beta = inner_tail_time_exponent(order)
    return {
        "inner_source": beta / 2 + 6,
        "stable_first": Fraction(11, 1),
        "stable_second": Fraction(89, 4),
    }


def fixed_order_pressure_ceiling(
    h: float,
    order: int,
    alpha: Fraction = Fraction(1, 10),
) -> float:
    """Dimensionless exponent-only pressure ceiling at one fixed order."""
    if not 0.0 < h <= 1.0:
        raise ValueError("h must lie in (0, 1]")
    powers = intermediate_pressure_powers(order, alpha)
    shell_powers = exterior_shell_powers(order)
    active = [value for key, value in powers.items() if key != "source_radius_gap"]
    if powers["source_radius_gap"] <= 0 or any(value <= 0 for value in active):
        raise ValueError("alpha is outside the admissible range")
    return sum(h ** float(power) for power in active) + sum(
        h ** float(power) for power in shell_powers.values()
    )


def uniform_pressure_power(alpha: Fraction) -> Fraction:
    """Worst h power over all interaction orders at one split exponent."""
    if not isinstance(alpha, Fraction):
        alpha = Fraction(alpha)
    if not Fraction(1, 30) < alpha < 3:
        raise ValueError("alpha must lie in (1/30, 3)")
    first_order = intermediate_pressure_powers(1, alpha)
    return min(
        value
        for key, value in first_order.items()
        if key != "source_radius_gap"
    )


def logarithmic_depth(
    h: float,
    growth_base: float,
    alpha: Fraction = Fraction(1, 4),
) -> int:
    """A conservative depth satisfying both constant and radius ledgers."""
    if not 0.0 < h < 1.0:
        raise ValueError("h must lie in (0, 1)")
    if not math.isfinite(growth_base) or growth_base < 2.0:
        raise ValueError("growth_base must be finite and at least 2")
    if not isinstance(alpha, Fraction):
        alpha = Fraction(alpha)
    if alpha <= 0:
        raise ValueError("alpha must be positive")
    pressure_power = uniform_pressure_power(alpha)
    depth_rate = min(
        float(pressure_power) / (4.0 * math.log(growth_base)),
        float(alpha) / (2.0 * math.log(4.0)),
    )
    return math.floor(depth_rate * math.log(1.0 / h))


def logarithmic_partial_sum_envelope(
    h: float,
    growth_base: float,
    alpha: Fraction = Fraction(1, 4),
) -> float:
    """Geometric pressure envelope through the conservative depth."""
    depth = logarithmic_depth(h, growth_base, alpha)
    if depth == 0:
        return 0.0
    pressure_power = uniform_pressure_power(alpha)
    return h ** float(pressure_power) * sum(
        growth_base**order for order in range(1, depth + 1)
    )


def main() -> None:
    orders = range(1, 7)
    payload = {
        "experiment": "logarithmically divergent causal feedback depth",
        "orders": {
            str(order): {
                "A_m": str(l1_exponent(order)),
                "B_m": str(lorentz_exponent(order)),
                "beta_m": str(inner_tail_time_exponent(order)),
                "intermediate_pressure_powers": {
                    key: str(value)
                    for key, value in intermediate_pressure_powers(order).items()
                },
                "exterior_shell_powers": {
                    key: str(value)
                    for key, value in exterior_shell_powers(order).items()
                },
                "ceiling_at_1e-8": fixed_order_pressure_ceiling(
                    1.0e-8,
                    order,
                ),
            }
            for order in orders
        },
        "logarithmic_depth_example": {
            "growth_base": 8.0,
            "h": 1.0e-80,
            "depth": logarithmic_depth(1.0e-80, 8.0),
            "partial_sum_envelope": logarithmic_partial_sum_envelope(
                1.0e-80,
                8.0,
            ),
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
