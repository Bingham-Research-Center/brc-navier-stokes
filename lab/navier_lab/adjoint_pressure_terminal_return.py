"""Exact ledgers for the high-high-to-low adjoint-pressure return.

For low output S and high input floor L, the Littlewood--Paley
high-high estimate has the squared form

    P^2 <= C^2 (S/L)^2 Q^2 T D,

where Q is the L-infinity-in-time L2 norm of the transported state and
D is the coefficient dissipation in the resonant high-frequency tail.
The functions below keep the scale consequences exact over Fractions.
"""

from __future__ import annotations

import json
from fractions import Fraction


def _fraction(
    value: int | Fraction,
    name: str,
    *,
    positive: bool = False,
    nonnegative: bool = False,
) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise ValueError(f"{name} must be an integer or Fraction")
    result = Fraction(value)
    if positive and result <= 0:
        raise ValueError(f"{name} must be positive")
    if nonnegative and result < 0:
        raise ValueError(f"{name} must be nonnegative")
    return result


def pressure_ceiling_squared(
    output_frequency: int | Fraction,
    input_frequency_floor: int | Fraction,
    horizon: int | Fraction,
    state_l2_ceiling: int | Fraction,
    coefficient_band_dissipation: int | Fraction,
    multiplier_constant: int | Fraction = 1,
) -> Fraction:
    """Return C^2(S/L)^2 Q^2 T D."""
    output = _fraction(output_frequency, "output_frequency", positive=True)
    input_floor = _fraction(
        input_frequency_floor,
        "input_frequency_floor",
        positive=True,
    )
    time = _fraction(horizon, "horizon", nonnegative=True)
    state = _fraction(
        state_l2_ceiling,
        "state_l2_ceiling",
        nonnegative=True,
    )
    dissipation = _fraction(
        coefficient_band_dissipation,
        "coefficient_band_dissipation",
        nonnegative=True,
    )
    constant = _fraction(
        multiplier_constant,
        "multiplier_constant",
        positive=True,
    )
    return (
        constant**2
        * (output / input_floor) ** 2
        * state**2
        * time
        * dissipation
    )


def required_band_dissipation(
    pressure_floor: int | Fraction,
    output_frequency: int | Fraction,
    input_frequency_floor: int | Fraction,
    horizon: int | Fraction,
    state_l2_ceiling: int | Fraction,
    multiplier_constant: int | Fraction = 1,
) -> Fraction:
    """Invert the squared pressure ceiling for D."""
    pressure = _fraction(
        pressure_floor,
        "pressure_floor",
        nonnegative=True,
    )
    output = _fraction(output_frequency, "output_frequency", positive=True)
    input_floor = _fraction(
        input_frequency_floor,
        "input_frequency_floor",
        positive=True,
    )
    time = _fraction(horizon, "horizon", positive=True)
    state = _fraction(
        state_l2_ceiling,
        "state_l2_ceiling",
        positive=True,
    )
    constant = _fraction(
        multiplier_constant,
        "multiplier_constant",
        positive=True,
    )
    return (
        pressure**2
        * input_floor**2
        / (constant**2 * output**2 * state**2 * time)
    )


def critical_packet_volume(frequency: int | Fraction) -> Fraction:
    """Return the critical spatial volume R^-3."""
    scale = _fraction(frequency, "frequency", positive=True)
    return scale**-3


def energy_normalised_state_amplitude(
    frequency: int | Fraction,
) -> Fraction:
    """Return R^(3/2) squared, represented as the exact amplitude square."""
    scale = _fraction(frequency, "frequency", positive=True)
    return scale**3


def energy_normalised_state_l2_squared(
    frequency: int | Fraction,
) -> Fraction:
    """Return amplitude^2 times volume, identically one."""
    return (
        energy_normalised_state_amplitude(frequency)
        * critical_packet_volume(frequency)
    )


def critical_drift_amplitude(frequency: int | Fraction) -> Fraction:
    """Return the scale-critical drift amplitude R."""
    return _fraction(frequency, "frequency", positive=True)


def critical_drift_l2_squared(frequency: int | Fraction) -> Fraction:
    """Return R^2 R^-3=R^-1."""
    scale = critical_drift_amplitude(frequency)
    return scale**2 * critical_packet_volume(scale)


def critical_drift_gradient_l2_squared(
    frequency: int | Fraction,
) -> Fraction:
    """Return (R times amplitude)^2 R^-3=R."""
    scale = critical_drift_amplitude(frequency)
    return (scale * scale) ** 2 * critical_packet_volume(scale)


def critical_tensor_l1_squared(frequency: int | Fraction) -> Fraction:
    """Return the squared L1 product ledger, R^-1."""
    scale = _fraction(frequency, "frequency", positive=True)
    state_amplitude_squared = energy_normalised_state_amplitude(scale)
    drift_amplitude_squared = critical_drift_amplitude(scale) ** 2
    volume_squared = critical_packet_volume(scale) ** 2
    return (
        state_amplitude_squared
        * drift_amplitude_squared
        * volume_squared
    )


def critical_pressure_squared(
    output_frequency: int | Fraction,
    input_frequency: int | Fraction,
) -> Fraction:
    """Return S^2 times the critical tensor L1 square, S^2/R."""
    output = _fraction(output_frequency, "output_frequency", positive=True)
    scale = _fraction(input_frequency, "input_frequency", positive=True)
    return output**2 * critical_tensor_l1_squared(scale)


def zeno_state_l2_squared(
    input_frequency: int | Fraction,
) -> Fraction:
    """Return the L2 square of L1 mass R^-1 in volume R^-3: R."""
    scale = _fraction(input_frequency, "input_frequency", positive=True)
    l1_mass = 1 / scale
    return l1_mass**2 / critical_packet_volume(scale)


def minimum_volume_for_l1_mass_and_l2_ceiling(
    l1_mass: int | Fraction,
    state_l2_ceiling: int | Fraction,
) -> Fraction:
    """Return the Cauchy--Schwarz support floor (L1/L2)^2."""
    mass = _fraction(l1_mass, "l1_mass", nonnegative=True)
    state = _fraction(
        state_l2_ceiling,
        "state_l2_ceiling",
        positive=True,
    )
    return (mass / state) ** 2


def physical_dissipation_charge(
    physical_event_scale: int | Fraction,
    normalised_dissipation: int | Fraction,
) -> Fraction:
    """Return D_phys=sigma D_normalised under parabolic scaling."""
    scale = _fraction(
        physical_event_scale,
        "physical_event_scale",
        positive=True,
    )
    dissipation = _fraction(
        normalised_dissipation,
        "normalised_dissipation",
        nonnegative=True,
    )
    return scale * dissipation


def terminal_layer_physical_charge(
    physical_event_scale: int | Fraction,
    input_frequency_floor: int | Fraction,
    layer_time: int | Fraction,
    pressure_floor: int | Fraction = 1,
    output_frequency: int | Fraction = 1,
    state_l2_constant: int | Fraction = 1,
    multiplier_constant: int | Fraction = 1,
) -> Fraction:
    """Return the physical charge sigma p^2 L^2/(C^2 S^2 c_r^2 h^3)."""
    scale = _fraction(
        physical_event_scale,
        "physical_event_scale",
        positive=True,
    )
    frequency = _fraction(
        input_frequency_floor,
        "input_frequency_floor",
        positive=True,
    )
    time = _fraction(layer_time, "layer_time", positive=True)
    pressure = _fraction(
        pressure_floor,
        "pressure_floor",
        nonnegative=True,
    )
    output = _fraction(output_frequency, "output_frequency", positive=True)
    state_constant = _fraction(
        state_l2_constant,
        "state_l2_constant",
        positive=True,
    )
    constant = _fraction(
        multiplier_constant,
        "multiplier_constant",
        positive=True,
    )
    return (
        scale
        * pressure**2
        * frequency**2
        / (
            constant**2
            * output**2
            * state_constant**2
            * time**3
        )
    )


def terminal_layer_required_dissipation_exponent(
    state_l2_power: int | Fraction,
    horizon_power: int | Fraction,
    input_frequency_power: int | Fraction,
) -> Fraction:
    """Return d where Q=h^a, T=h^b, L=h^-c force D >= h^-d."""
    state_power = _fraction(state_l2_power, "state_l2_power")
    time_power = _fraction(horizon_power, "horizon_power")
    frequency_power = _fraction(
        input_frequency_power,
        "input_frequency_power",
    )
    return 2 * frequency_power + 2 * state_power + time_power


def physical_tail_charge_power(
    event_scale_power: int | Fraction,
    state_l2_power: int | Fraction,
    horizon_power: int | Fraction,
    input_frequency_power: int | Fraction,
) -> Fraction:
    """Return e where sigma=h^beta makes the physical charge h^e."""
    zoom_power = _fraction(event_scale_power, "event_scale_power")
    required_power = terminal_layer_required_dissipation_exponent(
        state_l2_power,
        horizon_power,
        input_frequency_power,
    )
    return zoom_power - required_power


def main() -> None:
    payload = {
        "experiment": "high-high-to-low pressure return toll",
        "dyadic_scales": {
            str(level): {
                "frequency": str(2**level),
                "critical_pressure_squared": str(
                    critical_pressure_squared(1, 2**level)
                ),
                "critical_drift_gradient_l2_squared": str(
                    critical_drift_gradient_l2_squared(2**level)
                ),
                "required_dissipation_for_unit_return": str(
                    required_band_dissipation(
                        1,
                        1,
                        2**level,
                        1,
                        1,
                    )
                ),
                "zeno_state_l2_squared": str(
                    zeno_state_l2_squared(2**level)
                ),
            }
            for level in (1, 2, 4, 8, 16)
        },
        "terminal_layer_dissipation_power_for_Q_h_and_T_h": str(
            terminal_layer_required_dissipation_exponent(1, 1, 0)
        ),
        "physical_tail_power_at_alpha_7_over_4_beta_7": str(
            physical_tail_charge_power(7, 1, 1, Fraction(7, 4))
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
