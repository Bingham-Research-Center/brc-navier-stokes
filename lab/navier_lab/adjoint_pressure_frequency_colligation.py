"""Exact ledgers for a fixed-band Oseen colligation.

The analytic estimate certified by this module is

    ||V_R^m q(t)||_1 <= ||q||_(L^infty_t L^1_x)
                         (K M R^2 t)^m / m!,

where every Oseen interaction is projected back to one smooth annulus.
The module also records an exact integer-frequency family showing why
Leray-angle geometry without the coefficient-time action is insufficient.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction


def _fraction(value: int | Fraction, name: str) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise ValueError(f"{name} must be an integer or Fraction")
    return Fraction(value)


def _nonnegative(value: int | Fraction, name: str) -> Fraction:
    result = _fraction(value, name)
    if result < 0:
        raise ValueError(f"{name} must be nonnegative")
    return result


def _positive_integer(value: int, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer")
    return value


def _order(value: int, name: str = "order") -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return value


def band_action(
    weak_l3_bound: int | Fraction,
    frequency: int | Fraction,
    horizon: int | Fraction,
    multiplier_constant: int | Fraction = 1,
) -> Fraction:
    """Return a=K M R^2 T, the dimensionless fixed-band action."""
    weak_bound = _nonnegative(weak_l3_bound, "weak_l3_bound")
    band = _nonnegative(frequency, "frequency")
    time = _nonnegative(horizon, "horizon")
    constant = _nonnegative(multiplier_constant, "multiplier_constant")
    return constant * weak_bound * band * band * time


def dyson_iterate_bound(
    order: int,
    action: int | Fraction,
    input_l1: int | Fraction = 1,
) -> Fraction:
    """Return Q a^m/m! for the m-th fixed-band Oseen iterate."""
    steps = _order(order)
    action_value = _nonnegative(action, "action")
    input_value = _nonnegative(input_l1, "input_l1")
    return input_value * action_value**steps / math.factorial(steps)


def pressure_depth_bound(
    order: int,
    action: int | Fraction,
    input_l1: int | Fraction = 1,
) -> Fraction:
    """Return Q a^(m+1)/(m+1)! for integrated pressure at depth m."""
    steps = _order(order) + 1
    action_value = _nonnegative(action, "action")
    input_value = _nonnegative(input_l1, "input_l1")
    return input_value * action_value**steps / math.factorial(steps)


def pressure_tail_majorant(
    first_order: int,
    action: int | Fraction,
    input_l1: int | Fraction = 1,
) -> Fraction:
    """Geometrically majorise the pressure tail from one depth onward.

    The pressure term at depth m is Q a^(m+1)/(m+1)!.  If
    a < first_order+2, every subsequent term ratio is at most
    a/(first_order+2), which gives this exact rational tail bound.
    """
    order = _order(first_order, "first_order")
    action_value = _nonnegative(action, "action")
    denominator = Fraction(order + 2) - action_value
    if denominator <= 0:
        raise ValueError("action must be smaller than first_order+2")
    first_term = pressure_depth_bound(order, action_value, input_l1)
    return first_term * Fraction(order + 2, 1) / denominator


def logarithmic_depth_log_tail(
    log_inverse_h: float,
    depth_constant: float,
    action: float,
    input_power: float,
) -> float:
    """Return the log of e^a h^-A a^(N+1)/(N+1)!.

    Here N=floor(c log(1/h)).  This standard exponential-tail majorant
    tends to minus infinity faster than any linear function of
    log(1/h), even after a fixed polynomial input loss h^-A.
    """
    values = {
        "log_inverse_h": log_inverse_h,
        "depth_constant": depth_constant,
        "action": action,
        "input_power": input_power,
    }
    for name, value in values.items():
        if (isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(value)
                or value < 0):
            raise ValueError(f"{name} must be finite and nonnegative")
    depth = math.floor(depth_constant * log_inverse_h)
    if action == 0:
        return -math.inf
    return (
        input_power * log_inverse_h
        + action
        + (depth + 1) * math.log(action)
        - math.lgamma(depth + 2)
    )


def alternating_frequency_family(
    parameter: int,
) -> dict[str, object]:
    """Return the exact two-frequency Leray geometry for n>=3.

    The two integer frequencies are

        xi_-=(n^2-1,-2n,0),  xi_+=(n^2-1,2n,0),

    and differ by k=(0,4n,0).  Their common length is n^2+1.
    """
    n_value = _positive_integer(parameter, "parameter")
    if n_value < 3:
        raise ValueError("parameter must be at least three")
    n = Fraction(n_value)
    radius = n * n + 1
    parallel = n * n - 1
    cosine = (n**4 - 6 * n * n + 1) / radius**2
    sine = 4 * n * parallel / radius**2
    return {
        "xi_minus": (parallel, -2 * n, Fraction(0)),
        "xi_plus": (parallel, 2 * n, Fraction(0)),
        "shift": (Fraction(0), 4 * n, Fraction(0)),
        "radius": radius,
        "transport_frequency": parallel,
        "cosine": cosine,
        "sine": sine,
    }


def alternating_linear_leakage(parameter: int) -> Fraction:
    """Return sum_{m>=0} sin(delta) cos(delta)^m exactly."""
    family = alternating_frequency_family(parameter)
    cosine = family["cosine"]
    sine = family["sine"]
    assert isinstance(cosine, Fraction)
    assert isinstance(sine, Fraction)
    return sine / (1 - cosine)


def heat_weighted_alternating_leakage(parameter: int) -> Fraction:
    """Return the leakage when each heat multiplier equals cos(delta).

    Every completed projected interaction receives the heat factor.  The
    current pressure observation does not, so the series is
    s*sum((c^2)^m)=1/s.
    """
    family = alternating_frequency_family(parameter)
    cosine = family["cosine"]
    sine = family["sine"]
    assert isinstance(cosine, Fraction)
    assert isinstance(sine, Fraction)
    return 1 / sine


def one_sided_ray_ledgers(
    parameter: int,
    steps: int,
) -> tuple[float, float]:
    """Return linear leakage and angular variation on the +k ray."""
    family = alternating_frequency_family(parameter)
    count = _order(steps, "steps")
    frequency = tuple(float(value) for value in family["xi_minus"][:2])
    shift = tuple(float(value) for value in family["shift"][:2])
    amplitude = 1.0
    leakage = 0.0
    variation = 0.0
    for _ in range(count):
        next_frequency = (
            frequency[0] + shift[0],
            frequency[1] + shift[1],
        )
        norm = math.hypot(*frequency)
        next_norm = math.hypot(*next_frequency)
        cosine = (
            frequency[0] * next_frequency[0]
            + frequency[1] * next_frequency[1]
        ) / (norm * next_norm)
        sine = abs(
            frequency[0] * next_frequency[1]
            - frequency[1] * next_frequency[0]
        ) / (norm * next_norm)
        cosine = max(-1.0, min(1.0, cosine))
        sine = max(0.0, min(1.0, sine))
        leakage += amplitude * sine
        variation += math.atan2(sine, cosine)
        amplitude *= abs(cosine)
        frequency = next_frequency
    return leakage, variation


def effective_parabolic_time(parameter: int) -> float:
    """Return R^2 times the effective geometric lifetime.

    One microstep has heat multiplier c=exp(-R^2 dt), hence
    dt=-log(c)/R^2.  The survival ratio is c^2 and its effective number
    of steps is 1/(1-c^2).  The returned product tends to 1/2.
    """
    family = alternating_frequency_family(parameter)
    cosine = float(family["cosine"])
    return -math.log(cosine) / (1 - cosine * cosine)


def required_drift_to_critical_ratio(parameter: int) -> Fraction:
    """Return the drift amplitude needed for unit Duhamel action / R.

    For viscosity one, integrating the target heat mode over a pulse with
    multiplier c gives action B*alpha*(1-c)/R^2.  Setting this to one
    yields the exact ratio returned here.
    """
    family = alternating_frequency_family(parameter)
    cosine = family["cosine"]
    radius = family["radius"]
    transport = family["transport_frequency"]
    assert isinstance(cosine, Fraction)
    assert isinstance(radius, Fraction)
    assert isinstance(transport, Fraction)
    return radius / (transport * (1 - cosine))


def critical_step_action(
    parameter: int,
    critical_amplitude_constant: int | Fraction = 1,
) -> Fraction:
    """Return the exact pulse action when B=M R is scale-critical."""
    amplitude = _nonnegative(
        critical_amplitude_constant,
        "critical_amplitude_constant",
    )
    family = alternating_frequency_family(parameter)
    cosine = family["cosine"]
    radius = family["radius"]
    transport = family["transport_frequency"]
    assert isinstance(cosine, Fraction)
    assert isinstance(radius, Fraction)
    assert isinstance(transport, Fraction)
    return amplitude * transport * (1 - cosine) / radius


def main() -> None:
    action = band_action(3, 100, Fraction(1, 10000), 2)
    payload = {
        "experiment": "fixed-band Oseen frequency colligation",
        "parabolic_action": str(action),
        "pressure_depth_bounds": {
            str(order): str(pressure_depth_bound(order, action))
            for order in range(8)
        },
        "pressure_tail_from_depth_12": str(
            pressure_tail_majorant(12, action)
        ),
        "logarithmic_depth_log_tail": {
            str(log_inverse_h): logarithmic_depth_log_tail(
                log_inverse_h, 1.0, float(action), 2.0
            )
            for log_inverse_h in (100, 1000, 10000)
        },
        "fourier_backtracking": {
            str(parameter): {
                "linear_leakage": str(
                    alternating_linear_leakage(parameter)
                ),
                "heat_weighted_leakage": str(
                    heat_weighted_alternating_leakage(parameter)
                ),
                "effective_parabolic_time": effective_parabolic_time(
                    parameter
                ),
                "required_drift_over_carrier": (
                    str(required_drift_to_critical_ratio(parameter))
                ),
                "critical_step_action": str(critical_step_action(parameter)),
            }
            for parameter in (10, 100, 1000)
        },
        "one_sided_ray": {
            str(parameter): {
                "linear_leakage_1000_steps": one_sided_ray_ledgers(
                    parameter, 1000
                )[0],
                "angular_variation_1000_steps": one_sided_ray_ledgers(
                    parameter, 1000
                )[1],
            }
            for parameter in (10, 100, 1000)
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
