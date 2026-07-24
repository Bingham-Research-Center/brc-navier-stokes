"""Spatial primal-adjoint conservation and exact Beltrami cancellation.

The local density ``q=a dot b`` obeys a pointwise conservation law whose
current contains both adjoint and primal pressure fluxes.  For reciprocal
heat amplitudes of one periodic Beltrami eigenfield, those pressure fluxes
cancel the transport flux pointwise and the viscous Wronskian vanishes.
In the displayed pressure gauges the total local current is therefore
zero although the adjoint-pressure gradient is nonzero.  In any pressure
gauge, the current divergence and every cutoff-gradient pairing vanish.

This is a certificate for a structural no-go on the bare spatial pairing
ledger.  It is not an R3 finite-energy trajectory or a Clay conclusion.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
import math


@dataclass(frozen=True)
class BeltramiCurrentLedger:
    """Scalar coefficients of the local current for one Beltrami field.

    The viscous coefficient multiplies

        sum_i U_i grad U_i.

    The other three coefficients multiply ``w U``, where
    ``w=|U|^2/2``.
    """

    primal_amplitude: float
    adjoint_amplitude: float
    pairing_product: float
    viscous_wronskian: float
    transport: float
    adjoint_pressure: float
    primal_pressure: float
    total_w_u: float


def reciprocal_amplitudes(
    time: float,
    *,
    viscosity: float,
    frequency: float,
    primal_amplitude: float,
    adjoint_amplitude: float,
) -> tuple[float, float]:
    """Return the reversed-primal and forward-adjoint amplitudes."""
    if time < 0.0:
        raise ValueError("time must be nonnegative")
    if viscosity <= 0.0:
        raise ValueError("viscosity must be positive")
    if frequency <= 0.0:
        raise ValueError("frequency must be positive")
    phase = float(viscosity) * float(frequency) ** 2 * float(time)
    return (
        float(primal_amplitude) * math.exp(phase),
        float(adjoint_amplitude) * math.exp(-phase),
    )


def beltrami_current_ledger(
    time: float,
    *,
    viscosity: float = 1.0,
    frequency: float = 1.0,
    primal_amplitude: float = 1.0,
    adjoint_amplitude: float = 1.0,
) -> BeltramiCurrentLedger:
    """Return the exact scalar ledger of the local conservation current."""
    alpha, beta = reciprocal_amplitudes(
        time,
        viscosity=viscosity,
        frequency=frequency,
        primal_amplitude=primal_amplitude,
        adjoint_amplitude=adjoint_amplitude,
    )
    product = alpha * beta
    viscous = viscosity * (beta * alpha - alpha * beta)
    transport = -2.0 * alpha * alpha * beta
    adjoint_pressure = alpha * alpha * beta
    primal_pressure = alpha * alpha * beta
    total = transport + adjoint_pressure + primal_pressure
    return BeltramiCurrentLedger(
        primal_amplitude=alpha,
        adjoint_amplitude=beta,
        pairing_product=product,
        viscous_wronskian=viscous,
        transport=transport,
        adjoint_pressure=adjoint_pressure,
        primal_pressure=primal_pressure,
        total_w_u=total,
    )


def pressure_history_from_gradient(
    horizon: float,
    gradient_l1: float,
    *,
    primal_amplitude: float = 1.0,
    adjoint_amplitude: float = 1.0,
) -> float:
    """Return ``|AB| T ||grad w||_1`` for the Beltrami adjoint pressure."""
    if horizon <= 0.0:
        raise ValueError("horizon must be positive")
    if gradient_l1 <= 0.0:
        raise ValueError("gradient_l1 must be positive")
    return (
        abs(float(primal_amplitude) * float(adjoint_amplitude))
        * float(horizon)
        * float(gradient_l1)
    )


def paired_coefficient_budget(
    index: int,
    horizon: float,
    *,
    viscosity: float = 1.0,
    primal_amplitude: float = 1.0,
) -> tuple[float, float]:
    """Return terminal energy and viscosity-weighted dissipation.

    For the paired field ``W_n`` on ``[0,2 pi]^3``,
    ``||W_n||_2^2=2(2 pi)^3`` and
    ``R_n^2=2n^2+2n+1``.
    """
    if not isinstance(index, int) or index < 1:
        raise ValueError("index must be a positive integer")
    if horizon <= 0.0:
        raise ValueError("horizon must be positive")
    if viscosity <= 0.0:
        raise ValueError("viscosity must be positive")
    radius_squared = 2 * index * index + 2 * index + 1
    volume = (2.0 * math.pi) ** 3
    growth = math.exp(
        2.0 * float(viscosity) * radius_squared * float(horizon)
    )
    amplitude_squared = float(primal_amplitude) ** 2
    terminal_energy = 2.0 * volume * amplitude_squared * growth
    viscous_dissipation = volume * amplitude_squared * (growth - 1.0)
    return terminal_energy, viscous_dissipation


def certificate() -> dict[str, float | str]:
    ledger = beltrami_current_ledger(
        0.25,
        viscosity=0.7,
        frequency=3.0,
        primal_amplitude=2.0,
        adjoint_amplitude=5.0,
    )
    pressure_history = pressure_history_from_gradient(
        0.5,
        32.0 * math.pi * 3.0,
        primal_amplitude=2.0,
        adjoint_amplitude=5.0,
    )
    return {
        "experiment": "spatial primal-adjoint current cancellation",
        "pairing_product": ledger.pairing_product,
        "pressure_flux_sum": (
            ledger.adjoint_pressure + ledger.primal_pressure
        ),
        "transport_flux": ledger.transport,
        "total_current_coefficient": ledger.total_w_u,
        "pressure_history_lower_bound": pressure_history,
    }


def main() -> None:
    print(json.dumps(certificate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
