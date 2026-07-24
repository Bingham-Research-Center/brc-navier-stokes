"""Exact power ledgers for the first-hitting polar-vacuum reduction."""

from __future__ import annotations

import math


def _positive(name: str, value: float) -> None:
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be positive and finite")


def descendant_frequency(
    layer_time: float,
    kappa: float = 1.0,
) -> float:
    """Return K=kappa h^(-1/2)."""

    _positive("layer_time", layer_time)
    _positive("kappa", kappa)
    return kappa / math.sqrt(layer_time)


def moving_grid_capture(
    layer_time: float,
    maximum_cells: float,
    kappa: float = 1.0,
    capture_constant: float = 1.0,
) -> float:
    """Return C h^(7/4) N_*^(1/6)."""

    _positive("layer_time", layer_time)
    _positive("maximum_cells", maximum_cells)
    _positive("kappa", kappa)
    _positive("capture_constant", capture_constant)
    return (
        capture_constant
        * math.sqrt(kappa)
        * layer_time ** (7.0 / 4.0)
        * maximum_cells ** (1.0 / 6.0)
    )


def moving_grid_integral_capture(
    layer_time: float,
    cell_count_third_integral: float,
    kappa: float = 1.0,
    capture_constant: float = 1.0,
) -> float:
    """Return C h^(3/2) (K int N(t)^(1/3) dt)^(1/2)."""

    _positive("layer_time", layer_time)
    _positive("cell_count_third_integral", cell_count_third_integral)
    _positive("kappa", kappa)
    _positive("capture_constant", capture_constant)
    frequency = descendant_frequency(layer_time, kappa)
    return (
        capture_constant
        * layer_time**1.5
        * math.sqrt(frequency * cell_count_third_integral)
    )


def polar_volume_ceiling(
    regularization: float,
    regularized_mass_ceiling: float = 1.0,
) -> float:
    """Return 2 M_rho / epsilon from |zeta|^2 <= 2 rho/epsilon."""

    _positive("regularization", regularization)
    _positive("regularized_mass_ceiling", regularized_mass_ceiling)
    return 2.0 * regularized_mass_ceiling / regularization


def polar_cell_ceiling(
    layer_time: float,
    regularization: float,
    regularized_mass_ceiling: float = 1.0,
    kappa: float = 1.0,
    localization_constant: float = 1.0,
) -> float:
    """Return C K^3 ||zeta||_2^2."""

    _positive("localization_constant", localization_constant)
    frequency = descendant_frequency(layer_time, kappa)
    volume = polar_volume_ceiling(
        regularization,
        regularized_mass_ceiling,
    )
    return localization_constant * frequency**3 * volume


def pressure_cell_floor(
    layer_time: float,
    pressure_mass: float = 1.0,
    kappa: float = 1.0,
    capture_constant: float = 1.0,
) -> float:
    """Invert p <= C sqrt(kappa) h^(7/4) N^(1/6)."""

    _positive("layer_time", layer_time)
    _positive("pressure_mass", pressure_mass)
    _positive("kappa", kappa)
    _positive("capture_constant", capture_constant)
    denominator = capture_constant * math.sqrt(kappa)
    return (
        pressure_mass
        / (denominator * layer_time ** (7.0 / 4.0))
    ) ** 6


def inverse_ninth_regularization_ceiling(
    layer_time: float,
    pressure_mass: float = 1.0,
    kappa: float = 1.0,
    capture_constant: float = 1.0,
    polar_cell_constant: float = 1.0,
) -> float:
    """Invert p <= C h^2 K epsilon^(-1/6)."""

    _positive("layer_time", layer_time)
    _positive("pressure_mass", pressure_mass)
    _positive("kappa", kappa)
    _positive("capture_constant", capture_constant)
    _positive("polar_cell_constant", polar_cell_constant)
    frequency = descendant_frequency(layer_time, kappa)
    numerator = (
        capture_constant
        * polar_cell_constant ** (1.0 / 6.0)
        * layer_time**2
        * frequency
    )
    return (numerator / pressure_mass) ** 6


def quadratic_vacuum_bad_mass(
    layer_time: float,
    rooted_l2_threshold: float,
    capture_constant: float = 1.0,
) -> float:
    """Return C delta^(-1/3) h^(7/6)."""

    _positive("layer_time", layer_time)
    _positive("rooted_l2_threshold", rooted_l2_threshold)
    _positive("capture_constant", capture_constant)
    return (
        capture_constant
        * rooted_l2_threshold ** (-1.0 / 3.0)
        * layer_time ** (7.0 / 6.0)
    )


def balanced_orlicz_tail(
    amplitude_ratio: float,
    rooted_orlicz_threshold: float,
    capture_constant: float = 1.0,
) -> float:
    """Return C (theta L)^(-1/6), where theta=epsilon/h^9."""

    _positive("amplitude_ratio", amplitude_ratio)
    _positive("rooted_orlicz_threshold", rooted_orlicz_threshold)
    _positive("capture_constant", capture_constant)
    return (
        capture_constant
        * (amplitude_ratio * rooted_orlicz_threshold)
        ** (-1.0 / 6.0)
    )


def normalized_pressure_mass_per_source_cell(
    layer_time: float,
    regularization: float,
    pressure_mass: float = 1.0,
) -> float:
    """Return Z h^9/epsilon, the descendant-normalized cell average."""

    _positive("layer_time", layer_time)
    _positive("regularization", regularization)
    _positive("pressure_mass", pressure_mass)
    return pressure_mass * layer_time**9 / regularization


def source_volume_ledger(
    layer_time: float,
    kappa: float = 1.0,
) -> dict[str, float]:
    """Return the powers of the inverse-ninth source-volume carrier."""

    _positive("layer_time", layer_time)
    _positive("kappa", kappa)
    frequency = descendant_frequency(layer_time, kappa)
    length = 1.0 / frequency
    source_radius = layer_time**-3
    volume = source_radius**3
    regularization = layer_time**9
    amplitude = regularization
    pressure_amplitude = layer_time**8
    cells = volume / length**3
    return {
        "frequency": frequency,
        "descendant_length": length,
        "source_radius": source_radius,
        "volume": volume,
        "amplitude": amplitude,
        "regularization": regularization,
        "regularized_mass": regularization * volume,
        "l2_squared": amplitude**2 * volume,
        "spatial_gradient_squared": (
            amplitude**2 * frequency**2 * volume
        ),
        "spacetime_gradient_squared": (
            layer_time * amplitude**2 * frequency**2 * volume
        ),
        "polar_l2_squared": volume,
        "kato_dissipation": (
            layer_time
            * regularization
            * frequency**2
            * volume
        ),
        "descendant_cells": cells,
        "pressure_amplitude": pressure_amplitude,
        "pressure_l1_spacetime": (
            pressure_amplitude * layer_time * volume
        ),
        "pressure_mass_per_cell": (
            pressure_amplitude * layer_time * length**3
        ),
    }


def artificial_mark_capture(
    layer_time: float,
    cells: float,
    kappa: float = 1.0,
) -> float:
    """Return min(total mass, cells times the model's per-cell mass)."""

    _positive("layer_time", layer_time)
    _positive("cells", cells)
    ledger = source_volume_ledger(layer_time, kappa)
    return min(
        ledger["pressure_l1_spacetime"],
        cells * ledger["pressure_mass_per_cell"],
    )


def report(layer_time: float = 1.0e-4) -> dict[str, float | str]:
    """Return a compact machine-readable polar-vacuum ledger."""

    kappa = 0.25
    ceiling = inverse_ninth_regularization_ceiling(
        layer_time,
        kappa=kappa,
    )
    cell_floor = pressure_cell_floor(
        layer_time,
        kappa=kappa,
    )
    return {
        "experiment": "adjoint-pressure first-hitting polar vacuum",
        "layer_time": layer_time,
        "inverse_ninth_regularization_ceiling": ceiling,
        "pressure_cell_floor": cell_floor,
        "polar_cells_at_ceiling": polar_cell_ceiling(
            layer_time,
            ceiling,
            kappa=kappa,
        ),
        "quadratic_vacuum_bad_mass": quadratic_vacuum_bad_mass(
            layer_time,
            rooted_l2_threshold=0.5,
        ),
        "balanced_orlicz_tail": balanced_orlicz_tail(
            amplitude_ratio=1.0,
            rooted_orlicz_threshold=10.0,
        ),
        "normalized_pressure_mass_per_source_cell": (
            normalized_pressure_mass_per_source_cell(
                layer_time,
                layer_time**9,
            )
        ),
        **{
            f"model_{key}": value
            for key, value in source_volume_ledger(
                layer_time,
                kappa,
            ).items()
        },
    }


def main() -> None:
    import json

    print(json.dumps(report(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
