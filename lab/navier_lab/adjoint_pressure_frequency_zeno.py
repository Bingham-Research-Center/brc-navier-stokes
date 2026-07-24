"""Exact ledgers for a dyadic Zeno-frequency pressure path.

The scalar path uses dyadic frequencies R_i=2^i and heat rates
lambda_i=R_i^2.  Its i-th upward transition kernel has total mass
R_(i-1)/R_i=1/2.  With R_0=1, a terminal high-to-low pressure
observation has product weight R_m R_0=2^m, exactly cancelling the
path mass.
"""

from __future__ import annotations

import json
from fractions import Fraction
from typing import TypeAlias


Vector: TypeAlias = tuple[Fraction, Fraction, Fraction]


def _order(value: int, name: str = "order") -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return value


def _fraction(value: int | Fraction, name: str) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise ValueError(f"{name} must be an integer or Fraction")
    return Fraction(value)


def _vector(
    first: int | Fraction,
    second: int | Fraction,
    third: int | Fraction,
) -> Vector:
    return (Fraction(first), Fraction(second), Fraction(third))


def vector_add(left: Vector, right: Vector) -> Vector:
    """Return the exact componentwise vector sum."""
    return tuple(a + b for a, b in zip(left, right, strict=True))  # type: ignore[return-value]


def vector_subtract(left: Vector, right: Vector) -> Vector:
    """Return the exact componentwise vector difference."""
    return tuple(a - b for a, b in zip(left, right, strict=True))  # type: ignore[return-value]


def vector_dot(left: Vector, right: Vector) -> Fraction:
    """Return the exact Euclidean dot product."""
    return sum(
        (a * b for a, b in zip(left, right, strict=True)),
        Fraction(0),
    )


def vector_squared_norm(vector: Vector) -> Fraction:
    """Return the exact squared Euclidean norm."""
    return vector_dot(vector, vector)


def leray_projection(vector: Vector, frequency: Vector) -> Vector:
    """Project a vector orthogonally to a nonzero Fourier frequency."""
    denominator = vector_squared_norm(frequency)
    if denominator == 0:
        raise ValueError("frequency must be nonzero")
    coefficient = vector_dot(vector, frequency) / denominator
    return tuple(  # type: ignore[return-value]
        component - coefficient * wave
        for component, wave in zip(vector, frequency, strict=True)
    )


def hodge_gradient_projection(vector: Vector, frequency: Vector) -> Vector:
    """Project a vector onto a nonzero Fourier frequency."""
    denominator = vector_squared_norm(frequency)
    if denominator == 0:
        raise ValueError("frequency must be nonzero")
    coefficient = vector_dot(vector, frequency) / denominator
    return tuple(  # type: ignore[return-value]
        coefficient * wave for wave in frequency
    )


def dyadic_frequency(level: int) -> Fraction:
    """Return R_i=2^i."""
    index = _order(level, "level")
    return Fraction(2**index)


def state_frequency(level: int) -> Vector:
    """Return xi_i, alternating between the first two coordinate axes."""
    index = _order(level, "level")
    frequency = dyadic_frequency(index)
    if index % 2 == 0:
        return _vector(frequency, 0, 0)
    return _vector(0, frequency, 0)


def state_polarisation() -> Vector:
    """Return the common state polarisation e_3."""
    return _vector(0, 0, 1)


def upward_drift_frequency(level: int) -> Vector:
    """Return eta_i=xi_i-xi_(i-1) for one upward Fourier link."""
    if _order(level, "level") < 1:
        raise ValueError("level must be at least one")
    return vector_subtract(
        state_frequency(level),
        state_frequency(level - 1),
    )


def upward_drift_polarisation(level: int) -> Vector:
    """Return beta_i, divergence-free at eta_i with sharp transport."""
    index = _order(level, "level")
    if index < 1:
        raise ValueError("level must be at least one")
    frequency = dyadic_frequency(index)
    if index % 2 == 1:
        return _vector(frequency, frequency / 2, 0)
    return _vector(frequency / 2, frequency, 0)


def upward_transport_coefficient(level: int) -> Fraction:
    """Return beta_i dot xi_(i-1)=R_i R_(i-1)."""
    if _order(level, "level") < 1:
        raise ValueError("level must be at least one")
    return vector_dot(
        upward_drift_polarisation(level),
        state_frequency(level - 1),
    )


def terminal_output_frequency() -> Vector:
    """Return the fixed low output frequency kappa=e_3."""
    return _vector(0, 0, 1)


def terminal_drift_frequency(level: int) -> Vector:
    """Return zeta_i=kappa-xi_i for the terminal pressure return."""
    index = _order(level, "level")
    return vector_subtract(
        terminal_output_frequency(),
        state_frequency(index),
    )


def terminal_drift_polarisation(level: int) -> Vector:
    """Return gamma_i, divergence-free at zeta_i."""
    index = _order(level, "level")
    frequency = dyadic_frequency(index)
    if index % 2 == 0:
        return _vector(1, 0, frequency)
    return _vector(0, 1, frequency)


def terminal_transport_coefficient(level: int) -> Fraction:
    """Return gamma_i dot xi_i=R_i."""
    index = _order(level, "level")
    return vector_dot(
        terminal_drift_polarisation(index),
        state_frequency(index),
    )


def heat_rate(level: int) -> Fraction:
    """Return lambda_i=R_i^2=4^i."""
    frequency = dyadic_frequency(level)
    return frequency * frequency


def heat_clock(level: int) -> Fraction:
    """Return the mean heat waiting time lambda_i^-1."""
    if _order(level, "level") < 1:
        raise ValueError("level must be at least one")
    return 1 / heat_rate(level)


def upward_transition_mass(level: int) -> Fraction:
    """Return (R_(i-1) R_i)/lambda_i=R_(i-1)/R_i."""
    if _order(level, "level") < 1:
        raise ValueError("level must be at least one")
    return (
        dyadic_frequency(level - 1)
        * dyadic_frequency(level)
        / heat_rate(level)
    )


def path_mass(depth: int) -> Fraction:
    """Return the product of all upward transition masses."""
    steps = _order(depth, "depth")
    result = Fraction(1)
    for level in range(1, steps + 1):
        result *= upward_transition_mass(level)
    return result


def terminal_pressure_weight(depth: int) -> Fraction:
    """Return R_m R_0 for the final high-high-to-low observation."""
    steps = _order(depth, "depth")
    return dyadic_frequency(steps) * dyadic_frequency(0)


def observed_total_mass(depth: int) -> Fraction:
    """Return terminal weight times path mass, identically one."""
    return terminal_pressure_weight(depth) * path_mass(depth)


def mean_zeno_clock(depth: int) -> Fraction:
    """Return E S_m=sum_{i=1}^m 4^-i."""
    steps = _order(depth, "depth")
    return sum(
        (heat_clock(level) for level in range(1, steps + 1)),
        Fraction(0),
    )


def mean_zeno_clock_closed(depth: int) -> Fraction:
    """Return (1-4^-m)/3."""
    steps = _order(depth, "depth")
    return (1 - Fraction(1, 4**steps)) / 3


def infinite_mean_zeno_clock() -> Fraction:
    """Return sum_{i>=1}4^-i=1/3."""
    return Fraction(1, 3)


def pressure_cost_lower_bound(
    depth: int,
    trace_order: int,
    horizon: int | Fraction = 1,
) -> Fraction:
    """Return Jensen's exact lower bound for the integrated cost.

    With q_eta(t)=t^eta and independent X_i~Exp(4^i), the terminally
    weighted depth-m output is E[(t-S_m)_+^eta].  Integrating to T and
    using convexity gives

        cost >= (T-E S_m)^(eta+1)/(eta+1).
    """
    steps = _order(depth, "depth")
    eta = _order(trace_order, "trace_order")
    time = _fraction(horizon, "horizon")
    if time < 0:
        raise ValueError("horizon must be nonnegative")
    remainder = max(Fraction(0), time - mean_zeno_clock(steps))
    return remainder ** (eta + 1) / (eta + 1)


def uniform_pressure_cost_floor(
    trace_order: int,
    horizon: int | Fraction = 1,
) -> Fraction:
    """Return the depth-uniform floor using E S_infinity=1/3."""
    eta = _order(trace_order, "trace_order")
    time = _fraction(horizon, "horizon")
    if time < 0:
        raise ValueError("horizon must be nonnegative")
    remainder = max(Fraction(0), time - infinite_mean_zeno_clock())
    return remainder ** (eta + 1) / (eta + 1)


def output_trace_power(depth: int, trace_order: int) -> int:
    """Return the small-time power eta+m of the m-fold output."""
    return _order(depth, "depth") + _order(trace_order, "trace_order")


def packet_amplitude(level: int) -> Fraction:
    """Return the scale-critical packet amplitude B_i=R_i."""
    if _order(level, "level") < 1:
        raise ValueError("level must be at least one")
    return dyadic_frequency(level)


def packet_volume(level: int) -> Fraction:
    """Return V_i=R_i^-3."""
    frequency = packet_amplitude(level)
    return 1 / frequency**3


def packet_energy(level: int) -> Fraction:
    """Return B_i^2 V_i=R_i^-1."""
    amplitude = packet_amplitude(level)
    return amplitude**2 * packet_volume(level)


def packet_enstrophy_rate(level: int) -> Fraction:
    """Return (B_i R_i)^2 V_i=R_i."""
    amplitude = packet_amplitude(level)
    frequency = dyadic_frequency(level)
    return (amplitude * frequency) ** 2 * packet_volume(level)


def packet_dissipation(level: int) -> Fraction:
    """Return enstrophy rate times the heat clock, equal to R_i^-1."""
    return packet_enstrophy_rate(level) * heat_clock(level)


def finite_energy_or_dissipation(depth: int) -> Fraction:
    """Return sum_{i=1}^m2^-i=1-2^-m."""
    steps = _order(depth, "depth")
    return sum(
        (packet_energy(level) for level in range(1, steps + 1)),
        Fraction(0),
    )


def weak_l3_tail_charge(level: int) -> Fraction:
    """Return R_j^3 sum_{i=j}^infinity V_i=8/7."""
    if _order(level, "level") < 1:
        raise ValueError("level must be at least one")
    frequency = dyadic_frequency(level)
    volume_tail = packet_volume(level) / (1 - Fraction(1, 8))
    return frequency**3 * volume_tail


def main() -> None:
    payload = {
        "experiment": "dyadic Zeno-frequency pressure path",
        "infinite_mean_clock": str(infinite_mean_zeno_clock()),
        "depths": {
            str(depth): {
                "path_mass": str(path_mass(depth)),
                "terminal_pressure_weight": str(
                    terminal_pressure_weight(depth)
                ),
                "observed_total_mass": str(observed_total_mass(depth)),
                "mean_clock": str(mean_zeno_clock(depth)),
                "linear_trace_cost_lower_bound": str(
                    pressure_cost_lower_bound(depth, 1)
                ),
                "energy_sum": str(
                    finite_energy_or_dissipation(depth)
                ),
            }
            for depth in (1, 2, 4, 8, 16)
        },
        "uniform_cost_floors": {
            str(trace_order): str(
                uniform_pressure_cost_floor(trace_order)
            )
            for trace_order in range(5)
        },
        "weak_l3_tail_charge": str(weak_l3_tail_charge(10)),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
