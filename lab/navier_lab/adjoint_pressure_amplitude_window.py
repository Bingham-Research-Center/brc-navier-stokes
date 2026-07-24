"""Exact ledgers for the balanced finite-amplitude polar window."""

from __future__ import annotations

import math
from collections.abc import Sequence


def _positive(name: str, value: float) -> None:
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be positive and finite")


def _at_least_one(name: str, value: float) -> None:
    if not math.isfinite(value) or value < 1.0:
        raise ValueError(f"{name} must be finite and at least one")


def _vector3(name: str, value: Sequence[float]) -> tuple[float, float, float]:
    if len(value) != 3:
        raise ValueError(f"{name} must have three components")
    result = tuple(float(component) for component in value)
    if not all(math.isfinite(component) for component in result):
        raise ValueError(f"{name} must be finite")
    return result  # type: ignore[return-value]


def modular(relative_amplitude: float) -> float:
    """Return Phi(r)=sqrt(1+r^2)-1 for r >= 0."""

    if not math.isfinite(relative_amplitude) or relative_amplitude < 0.0:
        raise ValueError("relative_amplitude must be nonnegative and finite")
    scale = math.hypot(1.0, relative_amplitude)
    return relative_amplitude * relative_amplitude / (scale + 1.0)


def softened_polar_magnitude(
    relative_amplitude: float,
    softening_factor: float,
) -> float:
    """Return r/sqrt(r^2+L^2), the magnitude of zeta_(L epsilon)."""

    if not math.isfinite(relative_amplitude) or relative_amplitude < 0.0:
        raise ValueError("relative_amplitude must be nonnegative and finite")
    _at_least_one("softening_factor", softening_factor)
    return relative_amplitude / math.hypot(
        relative_amplitude,
        softening_factor,
    )


def modular_domination_ratio(
    relative_amplitude: float,
    softening_factor: float,
) -> float:
    """Return L |zeta_L|^2/Phi(r), with its continuous value at r=0."""

    if not math.isfinite(relative_amplitude) or relative_amplitude < 0.0:
        raise ValueError("relative_amplitude must be nonnegative and finite")
    _at_least_one("softening_factor", softening_factor)
    if relative_amplitude == 0.0:
        return 2.0 / softening_factor
    polar = softened_polar_magnitude(
        relative_amplitude,
        softening_factor,
    )
    return (
        softening_factor
        * polar
        * polar
        / modular(relative_amplitude)
    )


def softened_polar_l2_ceiling(
    regularised_mass: float,
    regularisation: float,
    softening_factor: float,
) -> float:
    """Return 2 M/(L epsilon) from the first-hitting mass bound."""

    _positive("regularised_mass", regularised_mass)
    _positive("regularisation", regularisation)
    _at_least_one("softening_factor", softening_factor)
    return 2.0 * regularised_mass / (
        softening_factor * regularisation
    )


def active_cell_ceiling(
    regularised_mass: float,
    regularisation: float,
    wavenumber: float,
    softening_factor: float,
    threshold: float,
    geometric_constant: float = 1.0,
) -> float:
    """Return the alpha-high descendant-cell ceiling.

    The Bernstein-ball argument gives

        N <= C K^3 M/(L epsilon alpha^5).
    """

    _positive("regularised_mass", regularised_mass)
    _positive("regularisation", regularisation)
    _positive("wavenumber", wavenumber)
    _at_least_one("softening_factor", softening_factor)
    _positive("threshold", threshold)
    _positive("geometric_constant", geometric_constant)
    return (
        geometric_constant
        * regularised_mass
        * wavenumber**3
        / (
            softening_factor
            * regularisation
            * threshold**5
        )
    )


def moving_capture_ceiling(
    layer_time: float,
    active_cells: float,
    capture_constant: float = 1.0,
) -> float:
    """Return C h^(7/4) N^(1/6)."""

    _positive("layer_time", layer_time)
    _positive("active_cells", active_cells)
    _positive("capture_constant", capture_constant)
    return (
        capture_constant
        * layer_time ** (7.0 / 4.0)
        * active_cells ** (1.0 / 6.0)
    )


def physical_pairing_tail(
    layer_time: float,
    regularisation: float,
    softening_factor: float,
    threshold: float,
    pressure_mass: float = 1.0,
    wavenumber_factor: float = 1.0,
    high_set_constant: float = 1.0,
) -> float:
    """Return the low-set plus moving-capture pairing ceiling."""

    _positive("layer_time", layer_time)
    _positive("regularisation", regularisation)
    _at_least_one("softening_factor", softening_factor)
    _positive("threshold", threshold)
    _positive("pressure_mass", pressure_mass)
    _positive("wavenumber_factor", wavenumber_factor)
    _positive("high_set_constant", high_set_constant)
    wavenumber = wavenumber_factor / math.sqrt(layer_time)
    cells = active_cell_ceiling(
        regularised_mass=1.0,
        regularisation=regularisation,
        wavenumber=wavenumber,
        softening_factor=softening_factor,
        threshold=threshold,
        geometric_constant=high_set_constant**6,
    )
    return (
        pressure_mass * threshold
        + moving_capture_ceiling(layer_time, cells)
    )


def balanced_pairing_tail(
    amplitude_ratio: float,
    softening_factor: float,
    threshold: float,
    pressure_mass: float = 1.0,
    high_set_constant: float = 1.0,
) -> float:
    """Return alpha Z + C theta^(-1/6)L^(-1/6)alpha^(-5/6)."""

    _positive("amplitude_ratio", amplitude_ratio)
    _at_least_one("softening_factor", softening_factor)
    _positive("threshold", threshold)
    _positive("pressure_mass", pressure_mass)
    _positive("high_set_constant", high_set_constant)
    return (
        pressure_mass * threshold
        + high_set_constant
        * amplitude_ratio ** (-1.0 / 6.0)
        * softening_factor ** (-1.0 / 6.0)
        * threshold ** (-5.0 / 6.0)
    )


def power_balanced_threshold(softening_factor: float) -> float:
    """Return L^(-1/11), which balances the two tail powers."""

    _at_least_one("softening_factor", softening_factor)
    return softening_factor ** (-1.0 / 11.0)


def optimized_pairing_tail(
    amplitude_ratio: float,
    softening_factor: float,
    pressure_mass: float = 1.0,
    high_set_constant: float = 1.0,
) -> float:
    """Evaluate the pairing bound at alpha=L^(-1/11)."""

    return balanced_pairing_tail(
        amplitude_ratio=amplitude_ratio,
        softening_factor=softening_factor,
        threshold=power_balanced_threshold(softening_factor),
        pressure_mass=pressure_mass,
        high_set_constant=high_set_constant,
    )


def soft_window_magnitude(
    relative_amplitude: float,
    softening_factor: float,
) -> float:
    """Return |zeta_epsilon-zeta_(L epsilon)|."""

    return (
        softened_polar_magnitude(relative_amplitude, 1.0)
        - softened_polar_magnitude(
            relative_amplitude,
            softening_factor,
        )
    )


def large_amplitude_window_ceiling(
    relative_amplitude: float,
    softening_factor: float,
) -> float:
    """Return (L^2-1)/(2r^2), valid as a soft-window ceiling."""

    _positive("relative_amplitude", relative_amplitude)
    _at_least_one("softening_factor", softening_factor)
    return (
        softening_factor * softening_factor - 1.0
    ) / (2.0 * relative_amplitude * relative_amplitude)


def window_map(
    polar: Sequence[float],
    softening_factor: float,
) -> tuple[float, float, float]:
    """Return B_L(z)=z-z/sqrt(|z|^2+L^2(1-|z|^2))."""

    z = _vector3("polar", polar)
    _at_least_one("softening_factor", softening_factor)
    z2 = sum(component * component for component in z)
    if z2 > 1.0 + 1.0e-12:
        raise ValueError("polar must lie in the closed unit ball")
    z2 = min(z2, 1.0)
    denominator = math.sqrt(
        z2 + softening_factor**2 * (1.0 - z2)
    )
    factor = 1.0 - 1.0 / denominator
    return tuple(factor * component for component in z)


def relative_amplitude_from_polar(polar: Sequence[float]) -> float:
    """Invert z=A/sqrt(1+|A|^2), allowing infinity on the unit sphere."""

    z = _vector3("polar", polar)
    z2 = sum(component * component for component in z)
    if z2 > 1.0 + 1.0e-12:
        raise ValueError("polar must lie in the closed unit ball")
    if z2 >= 1.0:
        return math.inf
    return math.sqrt(z2 / (1.0 - z2))


def _smooth_step(value: float) -> float:
    if value <= 0.0:
        return 0.0
    if value >= 1.0:
        return 1.0
    left = math.exp(-1.0 / value)
    right = math.exp(-1.0 / (1.0 - value))
    return left / (left + right)


def hard_window_cutoff(
    relative_amplitude: float,
    lower_amplitude: float,
    upper_amplitude: float,
) -> float:
    """Return a smooth cutoff equal to one on [lower, upper].

    It vanishes outside [lower/2, 2 upper].
    """

    if (
        not math.isfinite(relative_amplitude)
        or relative_amplitude < 0.0
    ):
        if math.isinf(relative_amplitude) and relative_amplitude > 0.0:
            return 0.0
        raise ValueError("relative_amplitude must be nonnegative")
    _positive("lower_amplitude", lower_amplitude)
    _positive("upper_amplitude", upper_amplitude)
    if upper_amplitude <= lower_amplitude:
        raise ValueError("upper_amplitude must exceed lower_amplitude")
    low = _smooth_step(
        (relative_amplitude - lower_amplitude / 2.0)
        / (lower_amplitude / 2.0)
    )
    high = 1.0 - _smooth_step(
        (relative_amplitude - upper_amplitude) / upper_amplitude
    )
    return low * high


def hard_window_map(
    polar: Sequence[float],
    softening_factor: float,
    lower_amplitude: float,
    upper_amplitude: float,
) -> tuple[float, float, float]:
    """Return the smooth compact-amplitude-window map of the polar."""

    z = _vector3("polar", polar)
    relative_amplitude = relative_amplitude_from_polar(z)
    cutoff = hard_window_cutoff(
        relative_amplitude,
        lower_amplitude,
        upper_amplitude,
    )
    return tuple(
        cutoff * component
        for component in window_map(z, softening_factor)
    )


def dyadic_window_telescope(
    relative_amplitude: float,
    levels: int,
) -> dict[str, float | list[float]]:
    """Return the exact finite dyadic polar telescope and its remainder."""

    if not math.isfinite(relative_amplitude) or relative_amplitude < 0.0:
        raise ValueError("relative_amplitude must be nonnegative and finite")
    if not isinstance(levels, int) or levels < 0:
        raise ValueError("levels must be a nonnegative integer")
    bands = [
        soft_window_magnitude(relative_amplitude, 2.0)
        if level == 0
        else (
            softened_polar_magnitude(relative_amplitude, 2.0**level)
            - softened_polar_magnitude(
                relative_amplitude,
                2.0 ** (level + 1),
            )
        )
        for level in range(levels)
    ]
    remainder = softened_polar_magnitude(
        relative_amplitude,
        2.0**levels,
    )
    return {
        "bands": bands,
        "remainder": remainder,
        "total": sum(bands) + remainder,
    }


def report(
    layer_time: float = 1.0e-4,
    amplitude_ratio: float = 1.0,
    softening_factor: float = 2.0**11,
) -> dict[str, float | str]:
    """Return a compact machine-readable amplitude-window ledger."""

    _positive("layer_time", layer_time)
    _positive("amplitude_ratio", amplitude_ratio)
    _at_least_one("softening_factor", softening_factor)
    regularisation = amplitude_ratio * layer_time**9
    threshold = power_balanced_threshold(softening_factor)
    cells = active_cell_ceiling(
        regularised_mass=1.0,
        regularisation=regularisation,
        wavenumber=layer_time**-0.5,
        softening_factor=softening_factor,
        threshold=threshold,
    )
    return {
        "experiment": "balanced finite-amplitude polar window",
        "layer_time": layer_time,
        "amplitude_ratio": amplitude_ratio,
        "softening_factor": softening_factor,
        "threshold": threshold,
        "active_cells": cells,
        "captured_high_mass": moving_capture_ceiling(
            layer_time,
            cells,
        ),
        "optimized_pairing_tail": optimized_pairing_tail(
            amplitude_ratio,
            softening_factor,
        ),
        "active_cell_h_power": -21.0 / 2.0,
        "pairing_tail_L_power": -1.0 / 11.0,
    }


def main() -> None:
    import json

    print(json.dumps(report(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
