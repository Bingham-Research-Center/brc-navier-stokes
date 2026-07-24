"""Exact ledgers for finite-band bulk pressure participation."""

from __future__ import annotations

import math


def _positive(name: str, value: float) -> None:
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be positive and finite")


def balanced_scales(
    layer_time: float,
    amplitude_ratio: float = 1.0,
    wavenumber_factor: float = 1.0,
) -> dict[str, float]:
    """Return the balanced pressure-source, cell, and volume scales."""

    _positive("layer_time", layer_time)
    _positive("amplitude_ratio", amplitude_ratio)
    _positive("wavenumber_factor", wavenumber_factor)
    regularisation = amplitude_ratio * layer_time**9
    wavenumber = wavenumber_factor * layer_time**-0.5
    descendant_length = 1.0 / wavenumber
    source_radius = layer_time**-3
    source_cells = (source_radius / descendant_length) ** 3
    return {
        "regularisation": regularisation,
        "wavenumber": wavenumber,
        "descendant_length": descendant_length,
        "source_radius": source_radius,
        "source_cells": source_cells,
        "source_cylinder_volume": layer_time * source_radius**3,
        "cell_layer_volume": layer_time * descendant_length**3,
    }


def finite_band_l2_squared_ceiling(
    layer_time: float,
    wavenumber_factor: float = 1.0,
    constant: float = 1.0,
) -> float:
    """Return C K^4 integral_0^h t^2 dt, with constants absorbed.

    For K=kappa h^(-1/2), this is C kappa^4 h.
    """

    _positive("layer_time", layer_time)
    _positive("wavenumber_factor", wavenumber_factor)
    _positive("constant", constant)
    return constant * wavenumber_factor**4 * layer_time


def charged_window_volume_floor(
    signed_charge: float,
    window_ceiling: float,
    pressure_l2_squared: float,
) -> float:
    """Return charge^2/(||W||_infinity^2 ||H||_2^2)."""

    _positive("signed_charge", signed_charge)
    _positive("window_ceiling", window_ceiling)
    _positive("pressure_l2_squared", pressure_l2_squared)
    return (
        signed_charge**2
        / (window_ceiling**2 * pressure_l2_squared)
    )


def modular_window_volume_ceiling(
    layer_time: float,
    regularisation: float,
    regularised_mass: float,
    modular_floor: float,
) -> float:
    """Return h M/(epsilon Phi(r_min)) for a compact amplitude window."""

    _positive("layer_time", layer_time)
    _positive("regularisation", regularisation)
    _positive("regularised_mass", regularised_mass)
    _positive("modular_floor", modular_floor)
    return (
        layer_time
        * regularised_mass
        / (regularisation * modular_floor)
    )


def source_participation_fraction(
    window_spacetime_volume: float,
    layer_time: float,
    source_radius: float,
) -> float:
    """Return |E|/(h R^3)."""

    _positive("window_spacetime_volume", window_spacetime_volume)
    _positive("layer_time", layer_time)
    _positive("source_radius", source_radius)
    return window_spacetime_volume / (
        layer_time * source_radius**3
    )


def cell_layer_units(
    window_spacetime_volume: float,
    layer_time: float,
    descendant_length: float,
) -> float:
    """Return the window volume in full descendant-cell layers."""

    _positive("window_spacetime_volume", window_spacetime_volume)
    _positive("layer_time", layer_time)
    _positive("descendant_length", descendant_length)
    return window_spacetime_volume / (
        layer_time * descendant_length**3
    )


def mean_source_duty_time(
    window_spacetime_volume: float,
    source_radius: float,
) -> float:
    """Return |E|/R^3, the source-volume mean physical duty time."""

    _positive("window_spacetime_volume", window_spacetime_volume)
    _positive("source_radius", source_radius)
    return window_spacetime_volume / source_radius**3


def capture_ceiling(
    layer_time: float,
    selected_cells: float,
    constant: float = 1.0,
) -> float:
    """Return C h^(7/4) N^(1/6)."""

    _positive("layer_time", layer_time)
    _positive("selected_cells", selected_cells)
    _positive("constant", constant)
    return (
        constant
        * layer_time ** (7.0 / 4.0)
        * selected_cells ** (1.0 / 6.0)
    )


def moving_high_density_capture(
    source_participation: float,
    density_threshold: float,
    constant: float = 1.0,
) -> float:
    """Return C (D/lambda)^(1/6) after the critical scale cancellation."""

    _positive("source_participation", source_participation)
    _positive("density_threshold", density_threshold)
    _positive("constant", constant)
    if density_threshold > 1.0:
        raise ValueError("density_threshold must not exceed one")
    return (
        constant
        * (source_participation / density_threshold) ** (1.0 / 6.0)
    )


def density_split_capture_modulus(
    source_participation: float,
    density_threshold: float,
    low_density_constant: float = 1.0,
    high_density_constant: float = 1.0,
) -> float:
    """Return C_low lambda + C_high (D/lambda)^(1/6)."""

    _positive("source_participation", source_participation)
    _positive("density_threshold", density_threshold)
    _positive("low_density_constant", low_density_constant)
    _positive("high_density_constant", high_density_constant)
    if density_threshold > 1.0:
        raise ValueError("density_threshold must not exceed one")
    return (
        low_density_constant * density_threshold
        + moving_high_density_capture(
            source_participation,
            density_threshold,
            high_density_constant,
        )
    )


def optimal_density_threshold(source_participation: float) -> float:
    """Return the exponent-balancing threshold lambda=D^(1/7)."""

    _positive("source_participation", source_participation)
    return min(1.0, source_participation ** (1.0 / 7.0))


def optimised_capture_modulus(
    source_participation: float,
) -> float:
    """Return the unit-constant optimised density-split modulus."""

    threshold = optimal_density_threshold(source_participation)
    if source_participation > 1.0:
        return 1.0
    return density_split_capture_modulus(
        source_participation,
        threshold,
    )


def bulk_participation_floor(
    signed_charge: float,
    window_ceiling: float,
    capture_modulus_constant: float,
) -> float:
    """Invert charge <= ||W||_infinity C D^(1/7)."""

    _positive("signed_charge", signed_charge)
    _positive("window_ceiling", window_ceiling)
    _positive("capture_modulus_constant", capture_modulus_constant)
    return (
        signed_charge
        / (window_ceiling * capture_modulus_constant)
    ) ** 7


def rejected_moving_tube_ledger(
    layer_time: float,
) -> dict[str, float]:
    """Return the rejected h^7-duty moving-tube exponent ledger.

    The idealised schedule uses every source cell for scaled duty h^7
    and amplitude 2 h s at the actual scaled time s. Its scalar L1 and
    L2 ledgers work, but the time-dependent active-cell selector violates
    moving capture by a factor h^(-7/6).
    """

    _positive("layer_time", layer_time)
    scales = balanced_scales(layer_time)
    duty_fraction = layer_time**7
    cells = scales["source_cells"]
    pressure_amplitude_scale = layer_time
    time_weight_l1 = 1.0
    time_weight_l2_squared = 4.0 / 3.0
    physical_duty_time = layer_time * duty_fraction
    active_cells_each_time = cells * duty_fraction
    mass_per_cell = (
        pressure_amplitude_scale
        * time_weight_l1
        * scales["descendant_length"] ** 3
        * physical_duty_time
    )
    l2_squared_per_cell = (
        pressure_amplitude_scale**2
        * time_weight_l2_squared
        * scales["descendant_length"] ** 3
        * physical_duty_time
    )
    window_volume_per_cell = (
        scales["descendant_length"] ** 3
        * physical_duty_time
    )
    total_mass = cells * mass_per_cell
    return {
        **scales,
        "duty_fraction": duty_fraction,
        "physical_duty_time": physical_duty_time,
        "source_cells_used": cells,
        "active_cells_each_time": active_cells_each_time,
        "pressure_amplitude_scale": pressure_amplitude_scale,
        "limiting_time_density_slope": 2.0,
        "time_weight_l2_squared": time_weight_l2_squared,
        "mass_per_cell": mass_per_cell,
        "total_pressure_mass": total_mass,
        "total_pressure_l2_squared": cells * l2_squared_per_cell,
        "window_spacetime_volume": cells * window_volume_per_cell,
        "cell_layer_participation": (
            cells * window_volume_per_cell
            / scales["cell_layer_volume"]
        ),
        "bulk_profile_l2_squared": duty_fraction,
        "self_weighted_profile_pairing": 1.0,
        "moving_selector_capture_ceiling": capture_ceiling(
            layer_time,
            active_cells_each_time,
        ),
        "capture_violation_ratio": (
            total_mass
            / capture_ceiling(layer_time, active_cells_each_time)
        ),
    }


def report(layer_time: float = 1.0e-4) -> dict[str, float | str]:
    """Return a compact machine-readable trace-participation ledger."""

    scales = balanced_scales(layer_time)
    pressure_l2 = finite_band_l2_squared_ceiling(layer_time)
    volume_floor = charged_window_volume_floor(
        signed_charge=1.0,
        window_ceiling=1.0,
        pressure_l2_squared=pressure_l2,
    )
    preliminary_participation = source_participation_fraction(
        volume_floor,
        layer_time,
        scales["source_radius"],
    )
    model = rejected_moving_tube_ledger(layer_time)
    return {
        "experiment": "finite-band bulk pressure participation",
        "layer_time": layer_time,
        "pressure_l2_squared_ceiling": pressure_l2,
        "preliminary_window_volume_floor": volume_floor,
        "preliminary_source_participation_floor": preliminary_participation,
        "preliminary_cell_layer_units_floor": cell_layer_units(
            volume_floor,
            layer_time,
            scales["descendant_length"],
        ),
        "preliminary_mean_source_duty_time_floor": mean_source_duty_time(
            volume_floor,
            scales["source_radius"],
        ),
        "optimised_capture_modulus_at_preliminary_floor": (
            optimised_capture_modulus(preliminary_participation)
        ),
        "rejected_model_total_mass": model["total_pressure_mass"],
        "rejected_model_l2_squared": model[
            "total_pressure_l2_squared"
        ],
        "rejected_model_moving_selector_ceiling": model[
            "moving_selector_capture_ceiling"
        ],
        "rejected_model_capture_violation_ratio": model[
            "capture_violation_ratio"
        ],
        "rejected_model_bulk_profile_l2_squared": model[
            "bulk_profile_l2_squared"
        ],
    }


def main() -> None:
    import json

    print(json.dumps(report(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
