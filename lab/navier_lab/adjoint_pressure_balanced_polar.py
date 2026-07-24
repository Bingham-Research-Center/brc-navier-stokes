"""Exact ledgers for balanced first-hitting polar compactness."""

from __future__ import annotations

import math
from collections.abc import Sequence


def _positive(name: str, value: float) -> None:
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be positive and finite")


def _vector3(name: str, value: Sequence[float]) -> tuple[float, float, float]:
    if len(value) != 3:
        raise ValueError(f"{name} must have three components")
    result = tuple(float(component) for component in value)
    if not all(math.isfinite(component) for component in result):
        raise ValueError(f"{name} must be finite")
    return result  # type: ignore[return-value]


def balanced_scales(
    layer_time: float,
    amplitude_ratio: float = 1.0,
    kappa: float = 1.0,
) -> dict[str, float]:
    """Return the exact descendant scales for epsilon=theta h^9."""

    _positive("layer_time", layer_time)
    _positive("amplitude_ratio", amplitude_ratio)
    _positive("kappa", kappa)
    length = math.sqrt(layer_time) / kappa
    regularization = amplitude_ratio * layer_time**9
    return {
        "descendant_length": length,
        "regularization": regularization,
        "source_cells": layer_time**-9 / length**3,
        "kato_cell_scale": regularization * layer_time * length,
        "pressure_cell_scale": regularization * length**3,
        "orlicz_cell_scale": regularization * length**3,
    }


def bad_cell_ceiling(
    total_budget: float,
    rooted_threshold: float,
    cell_scale: float,
    overlap_constant: float = 1.0,
) -> float:
    """Return C budget/(L times the physical-to-rooted cell scale)."""

    _positive("total_budget", total_budget)
    _positive("rooted_threshold", rooted_threshold)
    _positive("cell_scale", cell_scale)
    _positive("overlap_constant", overlap_constant)
    return (
        overlap_constant
        * total_budget
        / (rooted_threshold * cell_scale)
    )


def captured_bad_mass(
    layer_time: float,
    bad_cells: float,
    capture_constant: float = 1.0,
) -> float:
    """Return the fixed-grid capture ceiling C h^(7/4) N^(1/6)."""

    _positive("layer_time", layer_time)
    _positive("bad_cells", bad_cells)
    _positive("capture_constant", capture_constant)
    return (
        capture_constant
        * layer_time ** (7.0 / 4.0)
        * bad_cells ** (1.0 / 6.0)
    )


def balanced_action_tail(
    layer_time: float,
    rooted_threshold: float,
    action: str,
    amplitude_ratio: float = 1.0,
    kappa: float = 1.0,
    total_budget: float = 1.0,
    capture_constant: float = 1.0,
) -> float:
    """Return the H-law tail produced by the balanced cell count.

    ``action`` is one of ``kato``, ``pressure``, or ``orlicz``.
    """

    scales = balanced_scales(layer_time, amplitude_ratio, kappa)
    key = {
        "kato": "kato_cell_scale",
        "pressure": "pressure_cell_scale",
        "orlicz": "orlicz_cell_scale",
    }.get(action)
    if key is None:
        raise ValueError("action must be kato, pressure, or orlicz")
    cells = bad_cell_ceiling(
        total_budget,
        rooted_threshold,
        scales[key],
    )
    return captured_bad_mass(
        layer_time,
        cells,
        capture_constant,
    )


def hessian_quadratic(
    amplitude: Sequence[float],
    direction: Sequence[float],
) -> float:
    """Return v.D^2 Phi(A).v for Phi(A)=sqrt(1+|A|^2)-1."""

    a = _vector3("amplitude", amplitude)
    v = _vector3("direction", direction)
    a2 = sum(component * component for component in a)
    v2 = sum(component * component for component in v)
    av = sum(left * right for left, right in zip(a, v))
    scale = math.sqrt(1.0 + a2)
    return v2 / scale - av * av / scale**3


def third_derivative_contraction(
    amplitude: Sequence[float],
    direction: Sequence[float],
) -> tuple[float, float, float]:
    """Return D^3 Phi(A)[v,v] as a three-vector."""

    a = _vector3("amplitude", amplitude)
    v = _vector3("direction", direction)
    a2 = sum(component * component for component in a)
    v2 = sum(component * component for component in v)
    av = sum(left * right for left, right in zip(a, v))
    scale = math.sqrt(1.0 + a2)
    return tuple(
        -(2.0 * av * v_i + v2 * a_i) / scale**3
        + 3.0 * av * av * a_i / scale**5
        for a_i, v_i in zip(a, v)
    )


def curvature_to_kato_ratio(
    amplitude: Sequence[float],
    direction: Sequence[float],
) -> float:
    """Return |D^3 Phi(A)[v,v]|/(v.D^2 Phi(A).v)."""

    quadratic = hessian_quadratic(amplitude, direction)
    if quadratic == 0.0:
        return 0.0
    third = third_derivative_contraction(amplitude, direction)
    return math.sqrt(sum(component * component for component in third)) / (
        quadratic
    )


def polar_time_derivative_budget(
    kato_action: float,
    pressure_action: float,
    drift_ceiling: float,
    constant: float = 1.0,
) -> float:
    """Return C[(1+M)sqrt(K)+K+P] for the local polar equation."""

    _positive("kato_action", kato_action)
    _positive("pressure_action", pressure_action)
    _positive("drift_ceiling", drift_ceiling)
    _positive("constant", constant)
    return constant * (
        (1.0 + drift_ceiling) * math.sqrt(kato_action)
        + kato_action
        + pressure_action
    )


def trace_defect_ledger(
    concentration: float,
    bump_l1: float = 1.0,
    bump_l2_squared: float = 1.0,
    bump_variation: float = 1.0,
) -> dict[str, float]:
    """Return the powers of the abstract moving-time trace defect.

    A bump of width 1/n has L2-squared size O(1/n), fixed variation,
    a uniform averaged time marginal, and a fixed self-weighted pairing.
    """

    _positive("concentration", concentration)
    _positive("bump_l1", bump_l1)
    _positive("bump_l2_squared", bump_l2_squared)
    _positive("bump_variation", bump_variation)
    return {
        "profile_l2_squared": bump_l2_squared / concentration,
        "profile_variation": bump_variation,
        "averaged_time_density": 1.0,
        "self_weighted_pairing": bump_l2_squared / bump_l1,
    }


def report(layer_time: float = 1.0e-4) -> dict[str, float | str]:
    """Return a compact machine-readable balanced-polar ledger."""

    scales = balanced_scales(layer_time)
    return {
        "experiment": "balanced first-hitting polar compactness",
        "layer_time": layer_time,
        **scales,
        "kato_tail_at_L64": balanced_action_tail(
            layer_time,
            rooted_threshold=64.0,
            action="kato",
        ),
        "pressure_tail_at_L64": balanced_action_tail(
            layer_time,
            rooted_threshold=64.0,
            action="pressure",
        ),
        "orlicz_tail_at_L64": balanced_action_tail(
            layer_time,
            rooted_threshold=64.0,
            action="orlicz",
        ),
        **{
            f"trace_{key}": value
            for key, value in trace_defect_ledger(1000.0).items()
        },
    }


def main() -> None:
    import json

    print(json.dumps(report(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
