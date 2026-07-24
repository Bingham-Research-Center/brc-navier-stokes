"""Ledgers for the annular nonlinear-regeneration reduction.

Reciprocal-frequency splitting makes the low-frequency part of every
far spatial shell summable.  Heat evolution from the remote end of a
long physical genealogy contributes at most

``tail * duration**(1/2) * energy * horizon**(-(1+beta)/2)``,

where ``R**(-beta)`` is the exterior adjoint tail.  At the proved
endpoint ``beta=1/2`` this is ``energy*horizon**(-3/4)``.

This module checks those powers only.  It does not mechanise the
Littlewood--Paley split, Duhamel formula, CLMS estimate, or the
Navier--Stokes nonlinear regeneration term.
"""

from __future__ import annotations

import json
import math


def _positive(value: float, name: str) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be finite and positive")
    return value


def low_frequency_shell_sum(
    *,
    base_radius: float,
    shell_ratio: float,
    coefficient: float = 1.0,
) -> float:
    """Sum the reciprocal-radius low-frequency shell costs."""
    base_radius = _positive(base_radius, "base_radius")
    shell_ratio = _positive(shell_ratio, "shell_ratio")
    coefficient = _positive(coefficient, "coefficient")
    if shell_ratio <= 1.0:
        raise ValueError("shell_ratio must exceed one")
    return (
        coefficient
        / base_radius
        / (1.0 - shell_ratio**-1.0)
    )


def heat_erasure_horizon_power(*, tail_exponent: float) -> float:
    """Return ``(1+beta)/2`` for an ``R^-beta`` adjoint tail."""
    tail_exponent = _positive(tail_exponent, "tail_exponent")
    return (1.0 + tail_exponent) / 2.0


def inherited_budget_ceiling(
    *,
    energy_ceiling: float,
    horizon: float,
    duration: float,
    tail_constant: float,
    tail_exponent: float = 0.5,
    heat_constant: float = 1.0,
) -> float:
    """Return the heat-erased inherited annular budget."""
    energy_ceiling = _positive(energy_ceiling, "energy_ceiling")
    horizon = _positive(horizon, "horizon")
    duration = _positive(duration, "duration")
    tail_constant = _positive(tail_constant, "tail_constant")
    heat_constant = _positive(heat_constant, "heat_constant")
    power = heat_erasure_horizon_power(
        tail_exponent=tail_exponent,
    )
    return (
        heat_constant
        * tail_constant
        * math.sqrt(duration)
        * energy_ceiling
        * horizon ** (-power)
    )


def physical_erasure_rho_power(
    *,
    energy_blowup_power: float = 0.5,
    horizon_growth_power: float = 2.0,
    tail_exponent: float = 0.5,
) -> float:
    """Return the positive rho power after heat erasure.

    If ``E_rho ~ rho^-e`` and ``H_rho ~ rho^-h``, the inherited
    budget has power ``-e + h*(1+beta)/2``.
    """
    energy_blowup_power = _positive(
        energy_blowup_power,
        "energy_blowup_power",
    )
    horizon_growth_power = _positive(
        horizon_growth_power,
        "horizon_growth_power",
    )
    power = heat_erasure_horizon_power(
        tail_exponent=tail_exponent,
    )
    return (
        -energy_blowup_power
        + horizon_growth_power * power
    )


def inherited_shell_sum_power(*, tail_exponent: float) -> float:
    """Return the dyadic heat-shell power ``horizon^-beta/2``."""
    tail_exponent = _positive(tail_exponent, "tail_exponent")
    return tail_exponent / 2.0


def main() -> None:
    """Print the endpoint physical-genealogy ledger."""
    payload = {
        "endpoint_horizon_power": heat_erasure_horizon_power(
            tail_exponent=0.5,
        ),
        "endpoint_shell_sum_power": inherited_shell_sum_power(
            tail_exponent=0.5,
        ),
        "physical_rho_power": physical_erasure_rho_power(),
        "reciprocal_shell_sum": low_frequency_shell_sum(
            base_radius=1.0,
            shell_ratio=16.0,
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
