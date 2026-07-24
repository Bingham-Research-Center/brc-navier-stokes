"""Sharp high-pass energy ledger for the parabolic coefficient tail.

The reviewed adjoint-pressure theorem gives a *smooth-multiplier*
dissipation floor above a physical cutoff ``Lambda``.  Plancherel turns
that into a sharp high-pass floor.  The exact Navier--Stokes high-pass
energy identity then gives an exhaustive alternative:

* comparable dissipation in ``Lambda < |xi| <= R Lambda``;
* enough energy already present above ``R Lambda``; or
* positive signed nonlinear input into frequencies above ``R Lambda``.

The geometric shell ledger at the end is deliberately weaker than a PDE
construction.  It records that cumulative signed flux and the integrated
energy balances alone permit one almost lossless cascade to cross
arbitrarily many boundaries.  It is not a Navier--Stokes solution.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import json
import math


ANNULUS_BRANCH = "comparable_annulus"
INHERITED_BRANCH = "inherited_high_energy"
FLUX_BRANCH = "positive_signed_flux"


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


def sharp_tail_floor(
    smooth_tail_floor: float,
    multiplier_bound: float = 1.0,
) -> float:
    """Convert ``D_tail^chi >= P`` into ``D_tail^sharp >= P/C_chi^2``."""
    smooth_tail_floor = _positive(
        smooth_tail_floor,
        "smooth_tail_floor",
    )
    multiplier_bound = _positive(multiplier_bound, "multiplier_bound")
    return smooth_tail_floor / multiplier_bound**2


def signed_high_pass_input(
    *,
    viscosity: float,
    dissipation: float,
    incoming_energy: float,
    outgoing_energy: float,
) -> float:
    """Return the exact integrated nonlinear input into a sharp tail.

    For ``E_K(t)=||Q_{>K}v(t)||_2^2`` and
    ``D_K=integral ||grad Q_{>K}v||_2^2``, the convention is

        Phi_K = (E_K(b)-E_K(a))/2 + nu D_K.

    Positive ``Phi_K`` is nonlinear input into the high-pass region.
    """
    viscosity = _positive(viscosity, "viscosity")
    dissipation = _nonnegative(dissipation, "dissipation")
    incoming_energy = _nonnegative(incoming_energy, "incoming_energy")
    outgoing_energy = _nonnegative(outgoing_energy, "outgoing_energy")
    return (
        0.5 * (outgoing_energy - incoming_energy)
        + viscosity * dissipation
    )


@dataclass(frozen=True)
class TailFluxAlternative:
    """Numerical certificate for the exhaustive sharp-tail alternative."""

    branch: str
    sharp_floor: float
    annular_dissipation: float
    far_dissipation: float
    incoming_energy: float
    outgoing_energy: float
    signed_flux: float
    annular_threshold: float
    inherited_energy_threshold: float
    signed_flux_threshold: float


def tail_flux_alternative(
    *,
    smooth_tail_floor: float,
    multiplier_bound: float,
    annular_dissipation: float,
    far_dissipation: float,
    incoming_energy: float,
    outgoing_energy: float,
    viscosity: float,
) -> TailFluxAlternative:
    """Classify one exact annulus/energy/flux trichotomy.

    ``annular_dissipation + far_dissipation`` is the sharp dissipation
    above the lower cutoff.  It must dominate the converted sharp floor.
    """
    sharp_floor = sharp_tail_floor(
        smooth_tail_floor,
        multiplier_bound,
    )
    annular_dissipation = _nonnegative(
        annular_dissipation,
        "annular_dissipation",
    )
    far_dissipation = _nonnegative(
        far_dissipation,
        "far_dissipation",
    )
    incoming_energy = _nonnegative(incoming_energy, "incoming_energy")
    outgoing_energy = _nonnegative(outgoing_energy, "outgoing_energy")
    viscosity = _positive(viscosity, "viscosity")

    if annular_dissipation + far_dissipation < sharp_floor:
        raise ValueError("the sharp dissipation does not meet its floor")

    annular_threshold = 0.5 * sharp_floor
    inherited_threshold = 0.5 * viscosity * sharp_floor
    flux_threshold = 0.25 * viscosity * sharp_floor
    signed_flux = signed_high_pass_input(
        viscosity=viscosity,
        dissipation=far_dissipation,
        incoming_energy=incoming_energy,
        outgoing_energy=outgoing_energy,
    )

    if annular_dissipation >= annular_threshold:
        branch = ANNULUS_BRANCH
    elif incoming_energy >= inherited_threshold:
        branch = INHERITED_BRANCH
    else:
        branch = FLUX_BRANCH
        if signed_flux < flux_threshold:
            raise AssertionError("the exact energy identity lost its flux floor")

    return TailFluxAlternative(
        branch=branch,
        sharp_floor=sharp_floor,
        annular_dissipation=annular_dissipation,
        far_dissipation=far_dissipation,
        incoming_energy=incoming_energy,
        outgoing_energy=outgoing_energy,
        signed_flux=signed_flux,
        annular_threshold=annular_threshold,
        inherited_energy_threshold=inherited_threshold,
        signed_flux_threshold=flux_threshold,
    )


def physical_tail_floor(
    *,
    sigma: float,
    h: float,
    coefficient: float = 1.0,
) -> float:
    """Return the reviewed fixed-parabolic physical floor ``c sigma h^-3``."""
    sigma = _positive(sigma, "sigma")
    h = _positive(h, "h")
    coefficient = _positive(coefficient, "coefficient")
    return coefficient * sigma * h ** (-3.0)


def physical_cutoff(
    *,
    sigma: float,
    h: float,
    kappa: float = 1.0,
) -> float:
    """Return ``Lambda=kappa/(sigma sqrt(h))``."""
    sigma = _positive(sigma, "sigma")
    h = _positive(h, "h")
    kappa = _positive(kappa, "kappa")
    return kappa / (sigma * math.sqrt(h))


def physical_interval_length(*, sigma: float, h: float) -> float:
    """Return the physical event duration ``delta=sigma^2 h``."""
    sigma = _positive(sigma, "sigma")
    h = _positive(h, "h")
    return sigma * sigma * h


@dataclass(frozen=True)
class ShellCascadeLedger:
    """Exact integrated conservative shell-energy ledger.

    Shells are indexed ``0,...,depth``.  Boundary ``n`` separates
    shells ``0,...,n`` from ``n+1,...,depth``.  Positive boundary flux
    moves energy towards the higher shells.
    """

    depth: int
    input_flux: Fraction
    retention: Fraction
    boundary_fluxes: tuple[Fraction, ...]
    viscous_costs: tuple[Fraction, ...]
    energy_changes: tuple[Fraction, ...]

    def shell_balance_residuals(self) -> tuple[Fraction, ...]:
        """Return every integrated shell-energy balance residual."""
        residuals = [
            self.energy_changes[0] / 2
            + self.viscous_costs[0]
            + self.boundary_fluxes[0]
        ]
        for shell in range(1, self.depth):
            residuals.append(
                self.energy_changes[shell] / 2
                + self.viscous_costs[shell]
                - self.boundary_fluxes[shell - 1]
                + self.boundary_fluxes[shell]
            )
        residuals.append(
            self.energy_changes[self.depth] / 2
            + self.viscous_costs[self.depth]
            - self.boundary_fluxes[self.depth - 1]
        )
        return tuple(residuals)

    def cumulative_tail_cost(self, boundary: int) -> Fraction:
        """Return viscous cost in shells strictly above ``boundary``."""
        if not 0 <= boundary < self.depth:
            raise ValueError("boundary must lie between zero and depth-1")
        return sum(
            self.viscous_costs[boundary + 1 :],
            start=Fraction(0),
        )

    def cumulative_residuals(self) -> tuple[Fraction, ...]:
        """Return ``tail viscous cost - boundary flux`` at every boundary."""
        return tuple(
            self.cumulative_tail_cost(boundary)
            - self.boundary_fluxes[boundary]
            for boundary in range(self.depth)
        )


def geometric_shell_cascade(
    depth: int,
    *,
    input_flux: Fraction = Fraction(1),
    retention: Fraction = Fraction(1, 2),
) -> ShellCascadeLedger:
    """Build an exact depth-``m`` cascade with ``F_n=P r^n``.

    Intermediate shells dissipate the flux decrement and the top shell
    dissipates the surviving flux.  Only the low reservoir changes energy.
    """
    if not isinstance(depth, int) or depth < 1:
        raise ValueError("depth must be a positive integer")
    input_flux = Fraction(input_flux)
    retention = Fraction(retention)
    if input_flux <= 0:
        raise ValueError("input_flux must be positive")
    if not 0 < retention < 1:
        raise ValueError("retention must lie strictly between zero and one")

    fluxes = tuple(
        input_flux * retention**boundary
        for boundary in range(depth)
    )
    costs = [Fraction(0)]
    costs.extend(
        fluxes[shell - 1] - fluxes[shell]
        for shell in range(1, depth)
    )
    costs.append(fluxes[-1])
    changes = (-2 * input_flux,) + (Fraction(0),) * depth
    return ShellCascadeLedger(
        depth=depth,
        input_flux=input_flux,
        retention=retention,
        boundary_fluxes=fluxes,
        viscous_costs=tuple(costs),
        energy_changes=changes,
    )


def near_lossless_retention(depth: int) -> Fraction:
    """Return ``1-1/depth^2``, whose depth survival tends to one."""
    if not isinstance(depth, int) or depth < 2:
        raise ValueError("depth must be an integer at least two")
    return Fraction(depth * depth - 1, depth * depth)


def zeno_heat_time(
    *,
    base_frequency: float,
    depth: int | None = None,
    ratio: float = 2.0,
    viscosity: float = 1.0,
) -> float:
    """Sum natural heat clocks above ``base_frequency``.

    The first visited frequency is ``ratio*base_frequency``.  ``depth=None``
    returns the infinite geometric sum.
    """
    base_frequency = _positive(base_frequency, "base_frequency")
    ratio = _positive(ratio, "ratio")
    viscosity = _positive(viscosity, "viscosity")
    if ratio <= 1.0:
        raise ValueError("ratio must exceed one")
    if depth is not None and (
        not isinstance(depth, int) or depth < 1
    ):
        raise ValueError("depth must be positive or None")

    first = 1.0 / (
        viscosity * base_frequency**2 * ratio**2
    )
    quotient = ratio ** (-2.0)
    if depth is None:
        return first / (1.0 - quotient)
    return first * (1.0 - quotient**depth) / (1.0 - quotient)


def certificate() -> dict[str, float | int | str]:
    """Return a compact numerical certificate."""
    depth = 20
    retention = near_lossless_retention(depth)
    ledger = geometric_shell_cascade(
        depth,
        retention=retention,
    )
    sigma = 1.0e-5
    h = 1.0e-4
    cutoff = physical_cutoff(sigma=sigma, h=h, kappa=1.0)
    duration = physical_interval_length(sigma=sigma, h=h)
    return {
        "experiment": "parabolic tail to signed high-pass flux",
        "depth": depth,
        "largest_shell_residual": float(
            max(map(abs, ledger.shell_balance_residuals()))
        ),
        "largest_tail_residual": float(
            max(map(abs, ledger.cumulative_residuals()))
        ),
        "top_dissipation_fraction": float(
            ledger.viscous_costs[-1] / ledger.input_flux
        ),
        "dyadic_zeno_fraction_of_event": (
            zeno_heat_time(base_frequency=cutoff) / duration
        ),
    }


def main() -> None:
    print(json.dumps(certificate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
