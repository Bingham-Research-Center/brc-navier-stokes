"""Ledgers for the uniform-source product-law pressure trace."""

from __future__ import annotations

import math


def _positive(name: str, value: float) -> None:
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be positive and finite")


def uniform_root_scales(
    layer_time: float,
    amplitude_ratio: float = 1.0,
    wavenumber_factor: float = 1.0,
) -> dict[str, float]:
    """Return the three uniform-root mean-action scale factors."""

    _positive("layer_time", layer_time)
    _positive("amplitude_ratio", amplitude_ratio)
    _positive("wavenumber_factor", wavenumber_factor)
    regularisation = amplitude_ratio * layer_time**9
    source_radius = layer_time**-3
    descendant_length = (
        layer_time**0.5 / wavenumber_factor
    )
    source_volume = source_radius**3
    orlicz_mean_factor = 1.0 / (
        source_volume * regularisation
    )
    kato_mean_factor = (
        descendant_length**2
        / (
            source_volume
            * regularisation
            * layer_time
        )
    )
    pressure_mean_factor = orlicz_mean_factor
    return {
        "regularisation": regularisation,
        "source_radius": source_radius,
        "source_volume": source_volume,
        "descendant_length": descendant_length,
        "orlicz_mean_factor": orlicz_mean_factor,
        "kato_mean_factor": kato_mean_factor,
        "pressure_mean_factor": pressure_mean_factor,
    }


def density_modulus_exponent(
    moving_capture_power: float = 1.0 / 6.0,
) -> float:
    """Optimise lambda + (D/lambda)^beta."""

    _positive("moving_capture_power", moving_capture_power)
    return moving_capture_power / (1.0 + moving_capture_power)


def lorentz_density_exponent(
    absolute_continuity_power: float,
) -> float:
    """Return p from 1-1/p=alpha."""

    _positive(
        "absolute_continuity_power",
        absolute_continuity_power,
    )
    if absolute_continuity_power >= 1.0:
        raise ValueError(
            "absolute_continuity_power must be below one"
        )
    return 1.0 / (1.0 - absolute_continuity_power)


def product_base_mass(
    time_fraction: float,
    profile_fraction: float,
) -> float:
    """Return the mass of a product event."""

    _positive("time_fraction", time_fraction)
    _positive("profile_fraction", profile_fraction)
    if time_fraction > 1.0 or profile_fraction > 1.0:
        raise ValueError("fractions must not exceed one")
    return time_fraction * profile_fraction


def graph_neighbourhood_pressure_ceiling(
    time_width: float,
    absolute_continuity_power: float = 1.0 / 7.0,
    constant: float = 1.0,
) -> float:
    """Bound pressure on a graph neighbourhood of product mass width."""

    _positive("time_width", time_width)
    _positive(
        "absolute_continuity_power",
        absolute_continuity_power,
    )
    _positive("constant", constant)
    if time_width > 1.0:
        raise ValueError("time_width must not exceed one")
    return constant * time_width**absolute_continuity_power


def trace_approximation_error_bound(
    l2_error_squared: float,
    split_threshold: float,
    observable_ceiling: float,
    absolute_continuity_power: float = 1.0 / 7.0,
    modulus_constant: float = 1.0,
    total_variation_ceiling: float = 1.0,
) -> float:
    """Return the low/high error split used for temporal mollification."""

    _positive("l2_error_squared", l2_error_squared)
    _positive("split_threshold", split_threshold)
    _positive("observable_ceiling", observable_ceiling)
    _positive(
        "absolute_continuity_power",
        absolute_continuity_power,
    )
    _positive("modulus_constant", modulus_constant)
    _positive(
        "total_variation_ceiling",
        total_variation_ceiling,
    )
    return (
        split_threshold * total_variation_ceiling
        + 2.0
        * observable_ceiling
        * modulus_constant
        * (
            l2_error_squared / split_threshold**2
        ) ** absolute_continuity_power
    )


def report(layer_time: float = 1.0e-4) -> dict[str, float | str]:
    """Return the critical product-trace exponent ledger."""

    scales = uniform_root_scales(layer_time)
    alpha = density_modulus_exponent()
    delta = layer_time
    return {
        "experiment": "uniform-source product-law pressure trace",
        "layer_time": layer_time,
        "orlicz_mean_factor": scales["orlicz_mean_factor"],
        "kato_mean_factor": scales["kato_mean_factor"],
        "pressure_mean_factor": scales["pressure_mean_factor"],
        "absolute_continuity_power": alpha,
        "limiting_lorentz_exponent": (
            lorentz_density_exponent(alpha)
        ),
        "graph_neighbourhood_ceiling": (
            graph_neighbourhood_pressure_ceiling(delta, alpha)
        ),
        "balanced_trace_error_bound": (
            trace_approximation_error_bound(
                l2_error_squared=delta**9,
                split_threshold=delta,
                observable_ceiling=1.0,
                absolute_continuity_power=alpha,
            )
        ),
    }


def main() -> None:
    import json

    print(json.dumps(report(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
