"""Scalar ledgers for the weak-L3 lower-band flux decrement.

The analytic theorem decomposes sharp high-pass flux into far-low strain
and a remainder containing a comparable lower-band factor.  Choosing the
lower cutoff ratio so that the far-low strain is at most one twelfth of
viscosity forces a fixed lower-band dissipation fraction on both terminal
interval types.

This module checks constants only.  It does not mechanise the Fourier
support cancellation, Lorentz--Sobolev inequality, or Navier--Stokes
equation.
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


def admissible_lower_ratio(
    *,
    viscosity: float,
    weak_l3_bound: float,
    low_pass_constant: float = 1.0,
) -> float:
    """Return ``min(1/8, sqrt(nu/(12*C*M)))``."""
    viscosity = _positive(viscosity, "viscosity")
    weak_l3_bound = _positive(weak_l3_bound, "weak_l3_bound")
    low_pass_constant = _positive(
        low_pass_constant,
        "low_pass_constant",
    )
    return min(
        1.0 / 8.0,
        math.sqrt(
            viscosity
            / (12.0 * low_pass_constant * weak_l3_bound)
        ),
    )


def far_low_viscosity_fraction(
    *,
    lower_ratio: float,
    weak_l3_bound: float,
    viscosity: float,
    low_pass_constant: float = 1.0,
) -> float:
    """Return ``C*M*eta^2/nu`` for the far-low strain term."""
    lower_ratio = _positive(lower_ratio, "lower_ratio")
    weak_l3_bound = _positive(weak_l3_bound, "weak_l3_bound")
    viscosity = _positive(viscosity, "viscosity")
    low_pass_constant = _positive(
        low_pass_constant,
        "low_pass_constant",
    )
    return (
        low_pass_constant
        * weak_l3_bound
        * lower_ratio**2
        / viscosity
    )


def decrement_constant(*, remainder_constant: float = 1.0) -> float:
    """Return the common analytic constant ``3/(16*C0^2)``."""
    remainder_constant = _positive(
        remainder_constant,
        "remainder_constant",
    )
    return 3.0 / (16.0 * remainder_constant**2)


@dataclass(frozen=True)
class FluxDecrementCertificate:
    """Constant ledger for one terminal interval."""

    flux: float
    high_dissipation: float
    lower_band_dissipation_floor: float
    viscosity_weighted_decrement_floor: float
    relative_decrement: float


def low_entrance_certificate(
    *,
    viscosity: float,
    weak_l3_bound: float,
    tail_floor: float,
    high_dissipation: float,
    entrance_energy: float,
    terminal_energy: float = 0.0,
    remainder_constant: float = 1.0,
) -> FluxDecrementCertificate:
    """Check the low-entrance terminal interval.

    Required hypotheses are ``E_in < nu*T`` and ``D_h > 3*T/4``.
    The exact flux is ``(E_out-E_in)/2 + nu*D_h``.
    """
    viscosity = _positive(viscosity, "viscosity")
    weak_l3_bound = _positive(weak_l3_bound, "weak_l3_bound")
    tail_floor = _positive(tail_floor, "tail_floor")
    high_dissipation = _positive(
        high_dissipation,
        "high_dissipation",
    )
    entrance_energy = float(entrance_energy)
    terminal_energy = float(terminal_energy)
    if not math.isfinite(entrance_energy) or entrance_energy < 0.0:
        raise ValueError("entrance_energy must be finite and nonnegative")
    if not math.isfinite(terminal_energy) or terminal_energy < 0.0:
        raise ValueError("terminal_energy must be finite and nonnegative")
    if entrance_energy >= viscosity * tail_floor:
        raise ValueError("entrance_energy must be below nu*tail_floor")
    if high_dissipation <= 3.0 * tail_floor / 4.0:
        raise ValueError(
            "high_dissipation must exceed 3*tail_floor/4"
        )
    flux = (
        (terminal_energy - entrance_energy) / 2.0
        + viscosity * high_dissipation
    )
    if flux <= 0.0:
        raise ValueError("terminal hypotheses must force positive flux")
    constant = decrement_constant(
        remainder_constant=remainder_constant,
    )
    lower_floor = (
        constant
        * viscosity
        * flux
        / weak_l3_bound**2
    )
    weighted = viscosity * lower_floor
    return FluxDecrementCertificate(
        flux=flux,
        high_dissipation=high_dissipation,
        lower_band_dissipation_floor=lower_floor,
        viscosity_weighted_decrement_floor=weighted,
        relative_decrement=weighted / flux,
    )


def hitting_certificate(
    *,
    viscosity: float,
    weak_l3_bound: float,
    full_energy: float,
    high_dissipation: float,
    remainder_constant: float = 1.0,
) -> FluxDecrementCertificate:
    """Check a half-to-full high-pass energy hitting interval."""
    viscosity = _positive(viscosity, "viscosity")
    weak_l3_bound = _positive(weak_l3_bound, "weak_l3_bound")
    full_energy = _positive(full_energy, "full_energy")
    high_dissipation = _positive(
        high_dissipation,
        "high_dissipation",
    )
    flux = full_energy / 4.0 + viscosity * high_dissipation
    constant = decrement_constant(
        remainder_constant=remainder_constant,
    )
    lower_floor = (
        constant
        * viscosity
        * flux
        / weak_l3_bound**2
    )
    weighted = viscosity * lower_floor
    return FluxDecrementCertificate(
        flux=flux,
        high_dissipation=high_dissipation,
        lower_band_dissipation_floor=lower_floor,
        viscosity_weighted_decrement_floor=weighted,
        relative_decrement=weighted / flux,
    )


def pressure_tail_lower_band_floor(
    *,
    viscosity: float,
    weak_l3_bound: float,
    tail_floor: float,
    remainder_constant: float = 1.0,
) -> float:
    """Return the common corollary ``c*nu^2*T/M^2``.

    The common constant uses the low-entrance flux floor ``nu*T/4``.
    """
    viscosity = _positive(viscosity, "viscosity")
    weak_l3_bound = _positive(weak_l3_bound, "weak_l3_bound")
    tail_floor = _positive(tail_floor, "tail_floor")
    constant = decrement_constant(
        remainder_constant=remainder_constant,
    )
    return (
        constant
        * viscosity**2
        * tail_floor
        / (4.0 * weak_l3_bound**2)
    )


def retained_flux_after_depth(
    *,
    initial_flux: float,
    relative_decrement: float,
    depth: int,
) -> float:
    """Return the maximal retained flux after repeated decrements.

    If each comparable band dissipates at least ``delta`` times the
    outgoing flux, conservation gives ``F_next <= F/(1+delta)``.
    """
    initial_flux = _positive(initial_flux, "initial_flux")
    relative_decrement = _positive(
        relative_decrement,
        "relative_decrement",
    )
    if not isinstance(depth, int) or depth < 0:
        raise ValueError("depth must be a nonnegative integer")
    return initial_flux / (1.0 + relative_decrement) ** depth


def main() -> None:
    """Print one representative exact ledger."""
    viscosity = 1.0
    weak_l3_bound = 4.0
    tail_floor = 2.0
    ratio = admissible_lower_ratio(
        viscosity=viscosity,
        weak_l3_bound=weak_l3_bound,
    )
    certificate = low_entrance_certificate(
        viscosity=viscosity,
        weak_l3_bound=weak_l3_bound,
        tail_floor=tail_floor,
        high_dissipation=2.0,
        entrance_energy=1.0,
        terminal_energy=1.0,
    )
    payload = {
        "lower_ratio": ratio,
        "far_low_viscosity_fraction": far_low_viscosity_fraction(
            lower_ratio=ratio,
            weak_l3_bound=weak_l3_bound,
            viscosity=viscosity,
        ),
        "flux": certificate.flux,
        "lower_band_dissipation_floor": (
            certificate.lower_band_dissipation_floor
        ),
        "relative_decrement": certificate.relative_decrement,
        "ten_step_retained_flux": retained_flux_after_depth(
            initial_flux=certificate.flux,
            relative_decrement=certificate.relative_decrement,
            depth=10,
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
