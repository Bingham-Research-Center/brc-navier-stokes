"""Fixed-time tail and last-hitting ledgers for inherited parabolic energy.

The parabolic tail-to-flux theorem has an ``inherited energy`` branch:
the sharp tail above ``K=R Lambda`` already carries energy ``nu*T/2`` at
the entrance to the selected event.  On one common smooth preterminal
Navier--Stokes trajectory this cannot be unexplained indefinitely.

At any fixed earlier smooth time ``t0``, Plancherel gives

    E_K(t0) <= ||grad v(t0)||_2^2 / K^2.

For the reviewed parabolic scales,

    T K^2 = (c_kappa*kappa^2/C_chi^2)
            R^2 sigma^(-1) h^(-4),

which diverges as ``sigma,h -> 0``.  Consequently the entrance threshold
eventually exceeds twice the fixed-time tail.  Continuity then supplies
a last time at which the tail energy equals half its entrance threshold,
and the exact high-pass energy identity forces positive nonlinear input
between that time and the event entrance.

For an event-adaptive factor ``R -> 1``, continuity of the finite sharp
Fourier-dissipation measure makes the intervening annular cost smaller
than ``T/4``.  Splitting at entrance energy ``nu*T`` then forces either
event or historical flux at least ``nu*T/4``.

This module checks only the exact scalar consequences.  It does not
mechanise continuity from above of a finite measure, make the resulting
flux intervals disjoint, or prove regularity.
"""

from __future__ import annotations

from dataclasses import dataclass
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


def fixed_time_tail_upper(*, enstrophy: float, cutoff: float) -> float:
    """Return the Plancherel upper bound ``E_K <= enstrophy/K^2``."""
    enstrophy = _nonnegative(enstrophy, "enstrophy")
    cutoff = _positive(cutoff, "cutoff")
    return enstrophy / cutoff**2


def parabolic_sharp_floor(
    *,
    sigma: float,
    h: float,
    coefficient: float = 1.0,
    multiplier_bound: float = 1.0,
) -> float:
    """Return ``T=(c_kappa/C_chi^2) sigma h^-3``."""
    sigma = _positive(sigma, "sigma")
    h = _positive(h, "h")
    coefficient = _positive(coefficient, "coefficient")
    multiplier_bound = _positive(multiplier_bound, "multiplier_bound")
    return (
        coefficient
        * sigma
        * h ** (-3.0)
        / multiplier_bound**2
    )


def farther_parabolic_cutoff(
    *,
    sigma: float,
    h: float,
    kappa: float = 1.0,
    farther_factor: float = 2.0,
) -> float:
    """Return ``K=R*kappa/(sigma*sqrt(h))``."""
    sigma = _positive(sigma, "sigma")
    h = _positive(h, "h")
    kappa = _positive(kappa, "kappa")
    farther_factor = _positive(farther_factor, "farther_factor")
    if farther_factor <= 1.0:
        raise ValueError("farther_factor must exceed one")
    return farther_factor * kappa / (sigma * math.sqrt(h))


def threshold_frequency_product(
    *,
    sigma: float,
    h: float,
    coefficient: float = 1.0,
    multiplier_bound: float = 1.0,
    kappa: float = 1.0,
    farther_factor: float = 2.0,
) -> float:
    """Return the exact product ``T*K^2`` at the reviewed scales."""
    floor = parabolic_sharp_floor(
        sigma=sigma,
        h=h,
        coefficient=coefficient,
        multiplier_bound=multiplier_bound,
    )
    cutoff = farther_parabolic_cutoff(
        sigma=sigma,
        h=h,
        kappa=kappa,
        farther_factor=farther_factor,
    )
    return floor * cutoff**2


def historical_flux_from_last_hitting(
    *,
    entrance_threshold: float,
    dissipation: float = 0.0,
) -> float:
    """Return the exact flux at the half-threshold last hitting.

    If ``E(a) >= theta`` and ``E(s)=theta/2``, the high-pass identity

        Phi([s,a]) = (E(a)-E(s))/2 + nu*D

    gives ``Phi >= theta/4``.  The returned value is the identity's
    right side at the smallest allowed terminal energy; ``dissipation``
    is understood to include the viscosity factor ``nu*D``.
    """
    entrance_threshold = _positive(
        entrance_threshold,
        "entrance_threshold",
    )
    dissipation = _nonnegative(dissipation, "dissipation")
    return entrance_threshold / 4.0 + dissipation


def squeezed_terminal_flux_floor(
    *,
    viscosity: float,
    sharp_floor: float,
) -> float:
    """Return the clean terminal-flux floor ``nu*T/4``.

    After choosing the annulus to cost less than ``T/4``, the farther
    dissipation exceeds ``3T/4``.  Splitting at entrance energy ``nu*T``
    gives ``nu*T/4`` in both the event-flux and last-hitting cases.
    """
    viscosity = _positive(viscosity, "viscosity")
    sharp_floor = _positive(sharp_floor, "sharp_floor")
    return viscosity * sharp_floor / 4.0


@dataclass(frozen=True)
class InheritedAncestryCertificate:
    """Numerical certificate for one inherited-state ancestry check."""

    sharp_floor: float
    cutoff: float
    inherited_threshold: float
    half_threshold: float
    fixed_time_tail_upper: float
    threshold_frequency_product: float
    historical_flux_floor: float
    fixed_time_inheritance_excluded: bool


def inherited_ancestry_certificate(
    *,
    sigma: float,
    h: float,
    viscosity: float,
    fixed_time_enstrophy: float,
    coefficient: float = 1.0,
    multiplier_bound: float = 1.0,
    kappa: float = 1.0,
    farther_factor: float = 2.0,
) -> InheritedAncestryCertificate:
    """Evaluate all constants in the late inherited-state theorem."""
    viscosity = _positive(viscosity, "viscosity")
    fixed_time_enstrophy = _nonnegative(
        fixed_time_enstrophy,
        "fixed_time_enstrophy",
    )
    floor = parabolic_sharp_floor(
        sigma=sigma,
        h=h,
        coefficient=coefficient,
        multiplier_bound=multiplier_bound,
    )
    cutoff = farther_parabolic_cutoff(
        sigma=sigma,
        h=h,
        kappa=kappa,
        farther_factor=farther_factor,
    )
    inherited_threshold = viscosity * floor / 2.0
    half_threshold = inherited_threshold / 2.0
    tail_upper = fixed_time_tail_upper(
        enstrophy=fixed_time_enstrophy,
        cutoff=cutoff,
    )
    return InheritedAncestryCertificate(
        sharp_floor=floor,
        cutoff=cutoff,
        inherited_threshold=inherited_threshold,
        half_threshold=half_threshold,
        fixed_time_tail_upper=tail_upper,
        threshold_frequency_product=floor * cutoff**2,
        historical_flux_floor=inherited_threshold / 4.0,
        fixed_time_inheritance_excluded=tail_upper < half_threshold,
    )


def certificate() -> dict[str, float | bool | str]:
    """Return a compact late-scale numerical certificate."""
    result = inherited_ancestry_certificate(
        sigma=1.0e-12,
        h=1.0e-3,
        viscosity=1.0,
        fixed_time_enstrophy=10.0,
        coefficient=0.2,
        multiplier_bound=1.5,
        kappa=1.25,
        farther_factor=2.0,
    )
    return {
        "experiment": "inherited state to historical signed flux",
        "threshold_frequency_product": (
            result.threshold_frequency_product
        ),
        "fixed_time_tail_upper": result.fixed_time_tail_upper,
        "half_threshold": result.half_threshold,
        "fixed_time_inheritance_excluded": (
            result.fixed_time_inheritance_excluded
        ),
        "historical_flux_floor": result.historical_flux_floor,
        "squeezed_terminal_flux_floor": squeezed_terminal_flux_floor(
            viscosity=1.0,
            sharp_floor=result.sharp_floor,
        ),
    }


def main() -> None:
    print(json.dumps(certificate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
