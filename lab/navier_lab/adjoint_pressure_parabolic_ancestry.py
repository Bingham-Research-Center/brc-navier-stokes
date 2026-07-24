"""Parabolic coefficient-tail ancestry ledger.

The reviewed coefficient-tail theorem forces a physical payment

    sigma * h**(-3)

above the fixed-parabolic cutoff

    Lambda = kappa * h**(-1/2) / sigma.

This module records the exact consequence of identifying that cutoff with
the reciprocal next event scale.  It also gives the sharp power-law
survivor ``sigma=h**q`` for every ``q>3``.

The survivor is a scale and nonnegative dissipation ledger.  The companion
proof note upgrades it to a smooth divergence-free coefficient path, but
neither object solves Navier--Stokes.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
import math
from typing import List


SEVEN_SIXTHS = 7.0 / 6.0


def _validate(h: float, q: float, kappa: float) -> None:
    if not 0.0 < h < 1.0:
        raise ValueError("h must lie strictly between zero and one")
    if q <= 3.0:
        raise ValueError("q must exceed the inverse-cubic threshold three")
    if kappa < 1.0:
        raise ValueError("kappa must be at least one")


@dataclass(frozen=True)
class ParabolicAncestryNode:
    """One exact power-law event node."""

    h: float
    q: float
    kappa: float
    sigma: float
    normalised_cutoff: float
    physical_cutoff: float
    physical_tail_mass: float
    physical_time: float
    log_scale: float


def ancestry_node(
    h: float,
    *,
    q: float = 4.0,
    kappa: float = 1.0,
) -> ParabolicAncestryNode:
    """Return the node with ``sigma=h**q``."""
    h = float(h)
    q = float(q)
    kappa = float(kappa)
    _validate(h, q, kappa)

    sigma = h**q
    cutoff = kappa * h ** (-0.5)
    return ParabolicAncestryNode(
        h=h,
        q=q,
        kappa=kappa,
        sigma=sigma,
        normalised_cutoff=cutoff,
        physical_cutoff=cutoff / sigma,
        physical_tail_mass=sigma * h ** (-3.0),
        physical_time=sigma * sigma * h,
        log_scale=math.log(1.0 / sigma),
    )


def next_h(
    h: float,
    *,
    q: float = 4.0,
    kappa: float = 1.0,
) -> float:
    """Solve ``sigma_next=sigma/(kappa*h**(-1/2))`` exactly."""
    h = float(h)
    q = float(q)
    kappa = float(kappa)
    _validate(h, q, kappa)
    return kappa ** (-1.0 / q) * h ** (1.0 + 1.0 / (2.0 * q))


def ancestry_sequence(
    h_start: float,
    count: int,
    *,
    q: float = 4.0,
    kappa: float = 1.0,
) -> List[ParabolicAncestryNode]:
    """Generate a finite exact next-cutoff/next-event sequence."""
    if count < 1:
        raise ValueError("count must be positive")
    nodes: List[ParabolicAncestryNode] = []
    h = float(h_start)
    for index in range(count):
        nodes.append(ancestry_node(h, q=q, kappa=kappa))
        if index + 1 < count:
            h = next_h(h, q=q, kappa=kappa)
    return nodes


def ancestry_residual(
    current: ParabolicAncestryNode,
    following: ParabolicAncestryNode,
) -> float:
    """Return ``log(sigma_next*V_current/sigma_current)``."""
    return math.log(
        following.sigma
        * current.normalised_cutoff
        / current.sigma
    )


def cutoff_residual(
    current: ParabolicAncestryNode,
    following: ParabolicAncestryNode,
) -> float:
    """Return ``log(Lambda_current*sigma_next)``."""
    return math.log(current.physical_cutoff * following.sigma)


def distortion_mass(
    current: ParabolicAncestryNode,
    following: ParabolicAncestryNode,
) -> float:
    """Return the seventh-over-sixth scale distortion mass."""
    return current.sigma**7 / following.sigma**6


def log_scale_ratio(
    current: ParabolicAncestryNode,
    following: ParabolicAncestryNode,
) -> float:
    """Return ``log(1/sigma_next)/log(1/sigma_current)``."""
    return following.log_scale / current.log_scale


def tail_increments(
    nodes: List[ParabolicAncestryNode],
) -> List[float]:
    """Return positive annular masses with the final tail closed at zero."""
    if not nodes:
        raise ValueError("nodes must be nonempty")
    tails = [node.physical_tail_mass for node in nodes]
    return [
        tails[index]
        - (tails[index + 1] if index + 1 < len(tails) else 0.0)
        for index in range(len(tails))
    ]


def minimum_carrier_frequency(
    *,
    tail_increment: float,
    time_width: float,
    cutoff: float,
    weak_l3_bound: float = 1.0,
    bump_constant: float = 1.0,
) -> float:
    """Frequency sufficient for one normalised-gradient burst.

    A time bump with squared integral ``tail_increment`` on an interval of
    width ``time_width`` has amplitude at most

        bump_constant*sqrt(tail_increment/time_width).

    The packet ``w_K(x)=K**(1/2)w(Kx)`` has unit gradient norm and weak-L3
    norm proportional to ``K**(-1/2)``.  The returned frequency therefore
    keeps the burst below ``weak_l3_bound`` while placing it wholly beyond
    the requested cutoff.
    """
    if tail_increment <= 0.0:
        raise ValueError("tail_increment must be positive")
    if time_width <= 0.0:
        raise ValueError("time_width must be positive")
    if cutoff <= 0.0:
        raise ValueError("cutoff must be positive")
    if weak_l3_bound <= 0.0:
        raise ValueError("weak_l3_bound must be positive")
    if bump_constant <= 0.0:
        raise ValueError("bump_constant must be positive")
    amplitude_squared = (
        bump_constant * bump_constant * tail_increment / time_width
    )
    return max(cutoff, amplitude_squared / (weak_l3_bound**2))


def certificate(
    h_start: float = 1.0e-4,
    count: int = 5,
    *,
    q: float = 4.0,
    kappa: float = 1.0,
) -> dict[str, float | int]:
    """Return a compact numerical ledger."""
    nodes = ancestry_sequence(
        h_start,
        count,
        q=q,
        kappa=kappa,
    )
    ratios = [
        log_scale_ratio(current, following)
        for current, following in zip(nodes, nodes[1:])
    ]
    residuals = [
        abs(cutoff_residual(current, following))
        for current, following in zip(nodes, nodes[1:])
    ]
    return {
        "count": count,
        "q": q,
        "kappa": kappa,
        "largest_cutoff_residual": max(residuals, default=0.0),
        "largest_log_scale_ratio": max(ratios, default=1.0),
        "seven_sixths": SEVEN_SIXTHS,
        "last_tail_mass": nodes[-1].physical_tail_mass,
    }


def main() -> None:
    print(json.dumps(certificate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
