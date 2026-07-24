"""Exact ledgers for temporal disintegration of signed pressure laws."""

from __future__ import annotations

import math


def _positive(name: str, value: float) -> None:
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be positive and finite")


def _fraction(name: str, value: float) -> None:
    _positive(name, value)
    if value > 1:
        raise ValueError(f"{name} must be at most one")


def regularization_ceiling(
    layer_time: float,
    difference_rate: float,
    regularized_mass: float,
) -> float:
    """Invert mass <= ||w||_2^2/(2 epsilon), with ||w||_2 <= F h."""

    _positive("layer_time", layer_time)
    _positive("difference_rate", difference_rate)
    _positive("regularized_mass", regularized_mass)
    return (
        difference_rate**2
        * layer_time**2
        / (2.0 * regularized_mass)
    )


def capture_volume_floor(
    layer_time: float,
    difference_rate: float,
    captured_mass: float,
) -> float:
    """Invert captured_mass <= |E|^(1/2) F h."""

    _positive("layer_time", layer_time)
    _positive("difference_rate", difference_rate)
    _positive("captured_mass", captured_mass)
    return (
        captured_mass
        / (difference_rate * layer_time)
    ) ** 2


def descendant_length(layer_time: float, kappa: float = 1.0) -> float:
    """Return ell=kappa^-1 sqrt(h)."""

    _positive("layer_time", layer_time)
    _positive("kappa", kappa)
    return math.sqrt(layer_time) / kappa


def descendant_cell_floor(
    layer_time: float,
    difference_rate: float,
    captured_mass: float,
    kappa: float = 1.0,
) -> float:
    """Return the volume floor divided by one descendant-cell volume."""

    volume = capture_volume_floor(
        layer_time,
        difference_rate,
        captured_mass,
    )
    length = descendant_length(layer_time, kappa)
    return volume / length**3


def high_branch_time_capture(
    time_fraction: float,
    mass_floor: float = 1.0,
    capture_constant: float = 1.0,
) -> float:
    """Return C |A|^(1/2)/Z for the high-coefficient pressure law."""

    _fraction("time_fraction", time_fraction)
    _positive("mass_floor", mass_floor)
    _positive("capture_constant", capture_constant)
    return (
        capture_constant
        * math.sqrt(time_fraction)
        / mass_floor
    )


def high_branch_weighted_time_capture(
    time_second_moment: float,
    energy_fraction: float,
    mass_floor: float = 1.0,
    capture_constant: float = 1.0,
) -> float:
    """Return C (int_A s^2 ds * eta(A))^(1/2)/Z."""

    if not math.isfinite(time_second_moment) or time_second_moment < 0:
        raise ValueError(
            "time_second_moment must be nonnegative and finite"
        )
    if not math.isfinite(energy_fraction) or energy_fraction < 0:
        raise ValueError("energy_fraction must be nonnegative and finite")
    if energy_fraction > 1:
        raise ValueError("energy_fraction must be at most one")
    _positive("mass_floor", mass_floor)
    _positive("capture_constant", capture_constant)
    return (
        capture_constant
        * math.sqrt(time_second_moment * energy_fraction)
        / mass_floor
    )


def finite_band_time_space_capture(
    time_fraction: float,
    macro_volume: float,
    mass_floor: float = 1.0,
    capture_constant: float = 1.0,
) -> float:
    """Return C |A| |E|^(1/6)/Z for the finite-band pressure law."""

    _fraction("time_fraction", time_fraction)
    _positive("macro_volume", macro_volume)
    _positive("mass_floor", mass_floor)
    _positive("capture_constant", capture_constant)
    return (
        capture_constant
        * time_fraction
        * macro_volume ** (1.0 / 6.0)
        / mass_floor
    )


def finite_band_weighted_time_space_capture(
    time_fraction: float,
    time_second_moment: float,
    macro_volume: float,
    mass_floor: float = 1.0,
    capture_constant: float = 1.0,
) -> float:
    """Return C (|A| int_A s^2 ds)^(1/2) |E|^(1/6)/Z."""

    _fraction("time_fraction", time_fraction)
    if not math.isfinite(time_second_moment) or time_second_moment < 0:
        raise ValueError(
            "time_second_moment must be nonnegative and finite"
        )
    _positive("macro_volume", macro_volume)
    _positive("mass_floor", mass_floor)
    _positive("capture_constant", capture_constant)
    return (
        capture_constant
        * math.sqrt(time_fraction * time_second_moment)
        * macro_volume ** (1.0 / 6.0)
        / mass_floor
    )


def weak_density_exponent(capture_exponent: float) -> float:
    """Return p determined by 1-1/p=capture_exponent."""

    _positive("capture_exponent", capture_exponent)
    if capture_exponent >= 1:
        raise ValueError("capture_exponent must be smaller than one")
    return 1.0 / (1.0 - capture_exponent)


def saturation_ledger(
    layer_time: float,
    kappa: float = 1.0,
) -> dict[str, float]:
    """Return the exact powers of the quadratic-scale kinematic seed."""

    _positive("layer_time", layer_time)
    _positive("kappa", kappa)
    amplitude = layer_time**2
    volume = layer_time**-2
    length = descendant_length(layer_time, kappa)
    frequency = 1.0 / length
    spatial_gradient_squared = (
        amplitude**2 * frequency**2 * volume
    )
    return {
        "amplitude": amplitude,
        "regularization": amplitude,
        "volume": volume,
        "l1": amplitude * volume,
        "l2_squared": amplitude**2 * volume,
        "frequency": frequency,
        "spatial_gradient_squared": spatial_gradient_squared,
        "spacetime_gradient_squared": (
            layer_time * spatial_gradient_squared
        ),
        "descendant_length": length,
        "descendant_cells": volume / length**3,
        "descendant_rooted_frequency": frequency * length,
        "naive_polar_modulus": layer_time / amplitude,
    }


def report(layer_time: float = 1.0e-4) -> dict[str, float | str]:
    """Return a compact machine-readable temporal-disintegration ledger."""

    kappa = 0.25
    mass = 0.5
    rate = 2.0
    return {
        "experiment": "adjoint-pressure temporal disintegration",
        "layer_time": layer_time,
        "regularization_ceiling": regularization_ceiling(
            layer_time,
            rate,
            mass,
        ),
        "capture_volume_floor": capture_volume_floor(
            layer_time,
            rate,
            mass,
        ),
        "descendant_cell_floor": descendant_cell_floor(
            layer_time,
            rate,
            mass,
            kappa,
        ),
        "high_time_density_exponent": weak_density_exponent(0.5),
        "finite_band_space_density_exponent": (
            weak_density_exponent(1.0 / 6.0)
        ),
        "finite_band_time_capture": finite_band_time_space_capture(
            0.2,
            0.3,
            mass,
        ),
        "high_terminal_edge_capture": (
            high_branch_weighted_time_capture(
                0.2**3 / 3.0,
                1.0,
                mass,
            )
        ),
        "finite_band_terminal_edge_capture": (
            finite_band_weighted_time_space_capture(
                0.2,
                0.2**3 / 3.0,
                0.3,
                mass,
            )
        ),
        "naive_polar_modulus": saturation_ledger(
            layer_time,
            kappa,
        )["naive_polar_modulus"],
    }


def main() -> None:
    import json

    print(json.dumps(report(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
