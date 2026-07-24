"""Exact scalar ledger for stretched-exponential feedback history."""

from __future__ import annotations

import json
import math
from typing import Dict, Iterable, List, Tuple


P = 7.0 / 4.0


def _validate_parameters(h: float, c: float, acceleration: float) -> None:
    if not 0.0 < h <= 1.0:
        raise ValueError("h must lie in (0, 1]")
    if c <= 0.0:
        raise ValueError("c must be positive")
    if acceleration <= 1.0:
        raise ValueError("acceleration must exceed one")


def log_ledger(
    h: float,
    c: float = 1.0,
    acceleration: float = 2.0,
) -> Dict[str, float]:
    """Return all ledger quantities in logarithmic coordinates."""
    _validate_parameters(h, c, acceleration)
    depth = c * h ** (-P)
    log_h = math.log(h)
    return {
        "h": log_h,
        "forced_dissipation": -3.0 * log_h + depth,
        "zoom": 3.0 * log_h - acceleration * depth,
        "interaction_scale": -acceleration * depth,
        "dissipation_scale": -(acceleration - 1.0) * depth,
        "physical_time": 7.0 * log_h - 2.0 * acceleration * depth,
        "logarithmic_depth": depth,
        "interaction_clock": 7.0 * log_h,
        "dissipation_clock": 7.0 * log_h - 2.0 * depth,
    }


def physical_nodes(
    h_values: Iterable[float],
    c: float = 1.0,
    acceleration: float = 2.0,
) -> List[Tuple[float, float]]:
    """Return decreasing (physical time, physical dissipation) nodes."""
    values = list(h_values)
    if not values:
        raise ValueError("at least one h value is required")
    if any(values[index + 1] >= values[index] for index in range(len(values) - 1)):
        raise ValueError("h values must be strictly decreasing")

    nodes: List[Tuple[float, float]] = []
    for h in values:
        ledger = log_ledger(h, c, acceleration)
        delta = math.exp(ledger["physical_time"])
        rho = math.exp(ledger["dissipation_scale"])
        if delta == 0.0 or rho == 0.0:
            raise ValueError("nodes underflow; use logarithmic coordinates")
        nodes.append((delta, rho))

    if any(
        nodes[index + 1][0] >= nodes[index][0]
        or nodes[index + 1][1] >= nodes[index][1]
        for index in range(len(nodes) - 1)
    ):
        raise AssertionError("physical nodes must decrease")
    return nodes


def piecewise_history_segments(
    h_values: Iterable[float],
    c: float = 1.0,
    acceleration: float = 2.0,
) -> List[Tuple[float, float, float]]:
    """Build a finite positive piecewise-affine history certificate.

    Each tuple is ``(left, right, slope)``. Integrating the slopes from
    zero to any selected physical-time node recovers its prescribed
    physical dissipation exactly, up to floating-point arithmetic.
    """
    nodes = physical_nodes(h_values, c, acceleration)
    segments: List[Tuple[float, float, float]] = []

    inner_delta, inner_rho = nodes[-1]
    segments.append((0.0, inner_delta, inner_rho / inner_delta))

    for index in range(len(nodes) - 2, -1, -1):
        right_delta, right_rho = nodes[index]
        left_delta, left_rho = nodes[index + 1]
        slope = (right_rho - left_rho) / (right_delta - left_delta)
        if slope <= 0.0:
            raise AssertionError("history slope must be positive")
        segments.append((left_delta, right_delta, slope))

    return segments


def integrated_history(
    endpoint: float,
    segments: Iterable[Tuple[float, float, float]],
) -> float:
    """Integrate a piecewise-constant history density to an endpoint."""
    if endpoint < 0.0:
        raise ValueError("endpoint must be nonnegative")
    total = 0.0
    for left, right, slope in segments:
        if endpoint <= left:
            continue
        total += slope * (min(endpoint, right) - left)
    return total


def main() -> None:
    h_values = [0.8, 0.7, 0.6, 0.5]
    nodes = physical_nodes(h_values, c=0.2, acceleration=2.0)
    segments = piecewise_history_segments(
        h_values,
        c=0.2,
        acceleration=2.0,
    )
    payload = {
        "experiment": "stretched feedback history ledger",
        "h_values": h_values,
        "nodes": nodes,
        "segment_count": len(segments),
        "total_history": integrated_history(nodes[0][0], segments),
        "outer_mass": nodes[0][1],
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
