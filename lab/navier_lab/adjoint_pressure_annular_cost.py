"""Ledgers for the annular adjoint-pressure localisation theorem.

The analytic theorem replaces the coefficient's global ``L2`` norm by
centre-uniform Navier--Stokes local energy and an exterior ``L2`` tail of
the Oseen adjoint.  This module checks only the resulting powers and
geometric sums.  It does not mechanise the Bogovskii construction, CLMS
div--curl estimate, or local-energy restart theorem.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
import math


def _positive(value: float, name: str) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be finite and positive")
    return value


def local_energy_restart_ceiling(
    *,
    radius: float,
    duration: float,
    viscosity: float = 1.0,
    restart_constant: float = 1.0,
) -> float:
    """Return ``C * (R + nu*T/R)`` for one enlarged annulus."""
    radius = _positive(radius, "radius")
    duration = _positive(duration, "duration")
    viscosity = _positive(viscosity, "viscosity")
    restart_constant = _positive(
        restart_constant,
        "restart_constant",
    )
    return restart_constant * (
        radius + viscosity * duration / radius
    )


def annular_pressure_weight(
    *,
    radius: float,
    duration: float,
    weak_l3_bound: float,
    viscosity: float = 1.0,
    restart_constant: float = 1.0,
) -> float:
    """Return the coefficient multiplying one exterior adjoint tail."""
    radius = _positive(radius, "radius")
    duration = _positive(duration, "duration")
    weak_l3_bound = _positive(
        weak_l3_bound,
        "weak_l3_bound",
    )
    local_energy = local_energy_restart_ceiling(
        radius=radius,
        duration=duration,
        viscosity=viscosity,
        restart_constant=restart_constant,
    )
    cutoff = weak_l3_bound * math.sqrt(duration / radius)
    return math.sqrt(local_energy) + cutoff


def critical_tail_partial_sum(
    *,
    base_radius: float,
    shell_ratio: float,
    tail_constant: float,
    tail_exponent: float,
    shell_count: int,
) -> float:
    """Sum ``C R_k^(1/2-beta)`` over finitely many shells."""
    base_radius = _positive(base_radius, "base_radius")
    shell_ratio = _positive(shell_ratio, "shell_ratio")
    tail_constant = _positive(tail_constant, "tail_constant")
    tail_exponent = _positive(tail_exponent, "tail_exponent")
    if shell_ratio <= 1.0:
        raise ValueError("shell_ratio must exceed one")
    if not isinstance(shell_count, int) or shell_count < 0:
        raise ValueError("shell_count must be a nonnegative integer")
    return sum(
        tail_constant
        * (base_radius * shell_ratio**index) ** (
            0.5 - tail_exponent
        )
        for index in range(shell_count)
    )


def summable_tail_ceiling(
    *,
    base_radius: float,
    shell_ratio: float,
    tail_constant: float,
    tail_exponent: float,
) -> float:
    """Return the infinite shell sum, requiring ``beta>1/2``."""
    base_radius = _positive(base_radius, "base_radius")
    shell_ratio = _positive(shell_ratio, "shell_ratio")
    tail_constant = _positive(tail_constant, "tail_constant")
    tail_exponent = _positive(tail_exponent, "tail_exponent")
    if shell_ratio <= 1.0:
        raise ValueError("shell_ratio must exceed one")
    if tail_exponent <= 0.5:
        raise ValueError("tail_exponent must exceed one half")
    ratio = shell_ratio ** (0.5 - tail_exponent)
    return (
        tail_constant
        * base_radius ** (0.5 - tail_exponent)
        / (1.0 - ratio)
    )


def shell_lp_radius_exponent(integrability: float) -> float:
    """Return ``1-3/p`` in the annular ``L^p`` estimate."""
    integrability = _positive(integrability, "integrability")
    if not 2.0 < integrability < 3.0:
        raise ValueError("integrability must lie strictly between 2 and 3")
    return 1.0 - 3.0 / integrability


def gradient_rescaling_exponent(integrability: float) -> float:
    """Return the Navier--Stokes spacetime power ``2p-5``."""
    integrability = _positive(integrability, "integrability")
    return 2.0 * integrability - 5.0


@dataclass(frozen=True)
class StaticCellLedger:
    """Norm powers for the critical annular cell cloud."""

    radius: float
    cell_count: float
    coefficient_amplitude: float
    adjoint_amplitude: float
    weak_l3_proxy: float
    adjoint_l2: float
    coefficient_gradient_l2: float
    bilinear_l1_proxy: float


def static_cell_ledger(*, radius: float) -> StaticCellLedger:
    """Return the endpoint cloud with unit internal cell scale.

    There are ``R^3`` cells, coefficient amplitude ``R^-1``, and
    adjoint amplitude ``R^-2``.  The weak-``L3`` proxy and bilinear
    ``L1`` action are scale zero, while the two ``L2`` factors have
    powers ``-1/2`` and ``+1/2``.
    """
    radius = _positive(radius, "radius")
    cells = radius**3
    coefficient = radius**-1
    adjoint = radius**-2
    return StaticCellLedger(
        radius=radius,
        cell_count=cells,
        coefficient_amplitude=coefficient,
        adjoint_amplitude=adjoint,
        weak_l3_proxy=coefficient * cells ** (1.0 / 3.0),
        adjoint_l2=adjoint * math.sqrt(cells),
        coefficient_gradient_l2=coefficient * math.sqrt(cells),
        bilinear_l1_proxy=adjoint * coefficient * cells,
    )


def main() -> None:
    """Print one representative endpoint ledger."""
    payload = {
        "critical_tail_four_shells": critical_tail_partial_sum(
            base_radius=1.0,
            shell_ratio=16.0,
            tail_constant=1.0,
            tail_exponent=0.5,
            shell_count=4,
        ),
        "p_five_halves_shell_exponent": shell_lp_radius_exponent(2.5),
        "p_five_halves_scaling_exponent": (
            gradient_rescaling_exponent(2.5)
        ),
        "static_cell_ledger": asdict(static_cell_ledger(radius=16.0)),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
