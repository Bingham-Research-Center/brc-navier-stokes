"""Ledgers for parabolic scale-zero adjoint-pressure regeneration.

The analytic theorem uses two cancellations:

* one heat time at shell radius ``R`` turns the endpoint adjoint weight
  ``R^-1/2`` and the inherited local gradient ``R^-1/2`` into the
  summable cost ``R^-1``;
* after physical pullback, the rescaling factors cancel and a shell
  costs ``r^-1/2 * sqrt(physical_dissipation)``.

This module checks only those powers and their geometric sums.  It does
not mechanise the Duhamel identity, Lorentz multiplier estimate, annular
CLMS bound, or Leray dissipation absolute continuity.
"""

from __future__ import annotations

import json
import math


def _positive(value: float, name: str) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be finite and positive")
    return value


def _nonnegative(value: float, name: str) -> float:
    value = float(value)
    if not math.isfinite(value) or value < 0.0:
        raise ValueError(f"{name} must be finite and nonnegative")
    return value


def one_heat_time(*, radius: float, viscosity: float) -> float:
    """Return the parabolic look-back ``R^2 / nu``."""
    radius = _positive(radius, "radius")
    viscosity = _positive(viscosity, "viscosity")
    return radius**2 / viscosity


def inherited_shell_cost(
    *,
    radius: float,
    adjoint_constant: float = 1.0,
    coefficient_constant: float = 1.0,
) -> float:
    """Return the endpoint one-heat-time shell cost ``C / R``."""
    radius = _positive(radius, "radius")
    adjoint_constant = _positive(
        adjoint_constant,
        "adjoint_constant",
    )
    coefficient_constant = _positive(
        coefficient_constant,
        "coefficient_constant",
    )
    return adjoint_constant * coefficient_constant / radius


def inherited_shell_sum(
    *,
    base_radius: float,
    shell_ratio: float,
    adjoint_constant: float = 1.0,
    coefficient_constant: float = 1.0,
) -> float:
    """Sum all endpoint inherited shell costs."""
    base_radius = _positive(base_radius, "base_radius")
    shell_ratio = _positive(shell_ratio, "shell_ratio")
    if shell_ratio <= 1.0:
        raise ValueError("shell_ratio must exceed one")
    first = inherited_shell_cost(
        radius=base_radius,
        adjoint_constant=adjoint_constant,
        coefficient_constant=coefficient_constant,
    )
    return first / (1.0 - shell_ratio**-1.0)


def physical_shell_action(
    *,
    rescaled_radius: float,
    zoom_radius: float,
    physical_dissipation: float,
    physical_viscosity: float,
    adjoint_constant: float = 1.0,
) -> float:
    """Return the pulled-back endpoint shell action.

    The direct expression retains the rescaled factors so that tests can
    verify their exact cancellation:

    ``A R^-1/2 * sqrt(delta / (nu_phys * rho))``.
    """
    rescaled_radius = _positive(
        rescaled_radius,
        "rescaled_radius",
    )
    zoom_radius = _positive(zoom_radius, "zoom_radius")
    physical_dissipation = _nonnegative(
        physical_dissipation,
        "physical_dissipation",
    )
    physical_viscosity = _positive(
        physical_viscosity,
        "physical_viscosity",
    )
    adjoint_constant = _positive(
        adjoint_constant,
        "adjoint_constant",
    )
    adjoint_tail = adjoint_constant * rescaled_radius**-0.5
    rescaled_dissipation = (
        physical_dissipation
        / (physical_viscosity * zoom_radius)
    )
    return adjoint_tail * math.sqrt(rescaled_dissipation)


def physical_shell_action_reduced(
    *,
    physical_radius: float,
    physical_dissipation: float,
    physical_viscosity: float,
    adjoint_constant: float = 1.0,
) -> float:
    """Return ``A sqrt(delta / (nu_phys * r))``."""
    physical_radius = _positive(
        physical_radius,
        "physical_radius",
    )
    physical_dissipation = _nonnegative(
        physical_dissipation,
        "physical_dissipation",
    )
    physical_viscosity = _positive(
        physical_viscosity,
        "physical_viscosity",
    )
    adjoint_constant = _positive(
        adjoint_constant,
        "adjoint_constant",
    )
    return (
        adjoint_constant
        * math.sqrt(
            physical_dissipation
            / (physical_viscosity * physical_radius)
        )
    )


def outer_action_ceiling(
    *,
    minimum_physical_radius: float,
    shell_ratio: float,
    total_physical_dissipation: float,
    physical_viscosity: float,
    overlap: float = 1.0,
    adjoint_constant: float = 1.0,
) -> float:
    """Return the macroscopic-shell Cauchy--Schwarz ceiling."""
    minimum_physical_radius = _positive(
        minimum_physical_radius,
        "minimum_physical_radius",
    )
    shell_ratio = _positive(shell_ratio, "shell_ratio")
    total_physical_dissipation = _nonnegative(
        total_physical_dissipation,
        "total_physical_dissipation",
    )
    physical_viscosity = _positive(
        physical_viscosity,
        "physical_viscosity",
    )
    overlap = _positive(overlap, "overlap")
    adjoint_constant = _positive(
        adjoint_constant,
        "adjoint_constant",
    )
    if shell_ratio <= 1.0:
        raise ValueError("shell_ratio must exceed one")
    reciprocal_radius_sum = (
        1.0
        / minimum_physical_radius
        / (1.0 - shell_ratio**-1.0)
    )
    return (
        adjoint_constant
        / math.sqrt(physical_viscosity)
        * math.sqrt(reciprocal_radius_sum)
        * math.sqrt(overlap * total_physical_dissipation)
    )


def scale_zero_lookback_is_admissible(
    *,
    physical_cutoff: float,
    viscosity: float,
    horizon_constant: float,
) -> bool:
    """Test ``r_cut^2 / nu < lim rho^2 H``."""
    physical_cutoff = _positive(
        physical_cutoff,
        "physical_cutoff",
    )
    viscosity = _positive(viscosity, "viscosity")
    horizon_constant = _positive(
        horizon_constant,
        "horizon_constant",
    )
    return physical_cutoff**2 / viscosity < horizon_constant


def main() -> None:
    """Print the endpoint parabolic-regeneration ledger."""
    payload = {
        "one_heat_time_R4_nu2": one_heat_time(
            radius=4.0,
            viscosity=2.0,
        ),
        "reciprocal_shell_sum_L16": inherited_shell_sum(
            base_radius=1.0,
            shell_ratio=16.0,
        ),
        "scale_zero_cutoff_admissible": (
            scale_zero_lookback_is_admissible(
                physical_cutoff=0.5,
                viscosity=1.0,
                horizon_constant=1.0,
            )
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
