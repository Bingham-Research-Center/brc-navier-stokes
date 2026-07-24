"""Exact next-event survivor for the adjoint-pressure tail ledger.

This module works in the stretched coordinate ``x = h^(-7/4)`` and in
logarithmic variables.  That avoids numerical underflow in the regime in
which the reviewed logarithmic interaction-depth constant is small.

The certificate is deliberately a scalar time-frequency dissipation
ledger.  It is not a coefficient field or a Navier--Stokes solution.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, ROUND_FLOOR, localcontext
import json
from typing import Iterable, List


P = Decimal(7) / Decimal(4)
LN2 = Decimal(
    "0.693147180559945309417232121458176568075500134360255254120"
    "680009493393621969694715605863326996418687"
)


def _decimal(value: Decimal | float | int | str) -> Decimal:
    if isinstance(value, Decimal):
        return value
    return Decimal(str(value))


def _validate(
    x: Decimal,
    c: Decimal,
    acceleration: Decimal,
    c_dep: Decimal,
    tail_constant: Decimal,
) -> None:
    if x <= 1:
        raise ValueError("x=h^(-7/4) must exceed one")
    if c <= 0:
        raise ValueError("c must be positive")
    if acceleration <= 1:
        raise ValueError("acceleration must exceed one")
    if c_dep <= 0:
        raise ValueError("c_dep must be positive")
    if tail_constant <= 0:
        raise ValueError("tail_constant must be positive")


@dataclass(frozen=True)
class AncestryNode:
    """One event in logarithmic coordinates."""

    x: Decimal
    h: Decimal
    interaction_order: int
    top_frequency: Decimal
    log_top_frequency: Decimal
    log_zoom: Decimal
    log_total_mass: Decimal
    log_tail_mass: Decimal
    log_physical_time: Decimal

    @property
    def log_tail_fraction(self) -> Decimal:
        with localcontext() as context:
            context.prec = 100
            return +(self.log_tail_mass - self.log_total_mass)

    @property
    def log_kill_frequency(self) -> Decimal:
        """Log of h^(3/2)/sqrt(sigma).

        For the accelerated zoom this is exactly ``a*c*x/2``.  It is the
        frequency at which the terminal-return physical charge becomes
        order one.
        """
        with localcontext() as context:
            context.prec = 100
            log_h = self.h.ln()
            return +(Decimal("1.5") * log_h - self.log_zoom / 2)


@dataclass(frozen=True)
class FrequencySlab:
    """Mass placed on one terminal time annulus.

    ``high_mass`` is placed at ``exp(log_high_frequency)``.  ``bulk_mass``
    may be placed below every selected tail threshold.
    """

    bulk_mass: Decimal
    high_mass: Decimal
    log_high_frequency: Decimal


def ancestry_node(
    x: Decimal | float | int | str,
    *,
    c: Decimal | float | int | str = "1",
    acceleration: Decimal | float | int | str = "2",
    c_dep: Decimal | float | int | str = "0.05",
    tail_constant: Decimal | float | int | str = "1",
    precision: int = 100,
) -> AncestryNode:
    """Return one exact-form ledger node from ``x=h^(-7/4)``."""
    x_d = _decimal(x)
    c_d = _decimal(c)
    acceleration_d = _decimal(acceleration)
    c_dep_d = _decimal(c_dep)
    tail_constant_d = _decimal(tail_constant)
    _validate(x_d, c_d, acceleration_d, c_dep_d, tail_constant_d)

    with localcontext() as context:
        context.prec = precision
        log_x = x_d.ln()
        log_h = -log_x / P
        h = log_h.exp()
        raw_order = c_dep_d * (-log_h)
        order = int(raw_order.to_integral_value(rounding=ROUND_FLOOR))
        log_top = Decimal(order) * LN2
        top = Decimal(2) ** order
        stretched_depth = c_d * x_d
        log_zoom = Decimal(3) * log_h - acceleration_d * stretched_depth
        log_total = -(acceleration_d - 1) * stretched_depth
        log_tail = (
            tail_constant_d.ln()
            - acceleration_d * stretched_depth
            + Decimal(2) * log_top
        )
        log_time = Decimal(2) * log_zoom + log_h
        return AncestryNode(
            x=+x_d,
            h=+h,
            interaction_order=order,
            top_frequency=+top,
            log_top_frequency=+log_top,
            log_zoom=+log_zoom,
            log_total_mass=+log_total,
            log_tail_mass=+log_tail,
            log_physical_time=+log_time,
        )


def next_depth(
    x: Decimal | float | int | str,
    *,
    c: Decimal | float | int | str = "1",
    acceleration: Decimal | float | int | str = "2",
    c_dep: Decimal | float | int | str = "0.05",
    precision: int = 100,
) -> Decimal:
    """Solve the exact next-event identity sigma_next=sigma/L.

    In the stretched coordinate the unique positive increment ``d`` solves

        a*c*d + (3/p)*log(1+d/x) = log L(x).
    """
    x_d = _decimal(x)
    c_d = _decimal(c)
    acceleration_d = _decimal(acceleration)
    c_dep_d = _decimal(c_dep)
    node = ancestry_node(
        x_d,
        c=c_d,
        acceleration=acceleration_d,
        c_dep=c_dep_d,
        precision=precision,
    )
    if node.interaction_order < 1:
        raise ValueError("start far enough down the genealogy that L>1")

    with localcontext() as context:
        context.prec = precision
        coefficient = acceleration_d * c_d
        low = Decimal(0)
        high = node.log_top_frequency / coefficient

        def residual(increment: Decimal) -> Decimal:
            return (
                coefficient * increment
                + (Decimal(3) / P)
                * (Decimal(1) + increment / x_d).ln()
                - node.log_top_frequency
            )

        # The residual is strictly increasing, negative at zero, and
        # positive at this upper endpoint.
        for _ in range(4 * precision):
            middle = (low + high) / 2
            if residual(middle) < 0:
                low = middle
            else:
                high = middle
        result = x_d + (low + high) / 2
        if result <= x_d:
            raise ArithmeticError("working precision cannot resolve the next depth")
        return +result


def ancestry_sequence(
    x_start: Decimal | float | int | str,
    count: int,
    *,
    c: Decimal | float | int | str = "1",
    acceleration: Decimal | float | int | str = "2",
    c_dep: Decimal | float | int | str = "0.05",
    tail_constant: Decimal | float | int | str = "1",
    precision: int = 100,
) -> List[AncestryNode]:
    """Generate nodes satisfying exact dyadic next-event ancestry."""
    if count < 1:
        raise ValueError("count must be positive")
    x = _decimal(x_start)
    nodes: List[AncestryNode] = []
    for index in range(count):
        nodes.append(
            ancestry_node(
                x,
                c=c,
                acceleration=acceleration,
                c_dep=c_dep,
                tail_constant=tail_constant,
                precision=precision,
            )
        )
        if index + 1 < count:
            x = next_depth(
                x,
                c=c,
                acceleration=acceleration,
                c_dep=c_dep,
                precision=precision,
            )
    return nodes


def ancestry_residual(current: AncestryNode, following: AncestryNode) -> Decimal:
    """Return log(sigma_next L_current / sigma_current)."""
    with localcontext() as context:
        context.prec = 100
        return +(
            following.log_zoom
            + current.log_top_frequency
            - current.log_zoom
        )


def next_event_charge_log(
    x: Decimal | float | int | str,
    x_next: Decimal | float | int | str,
    *,
    c: Decimal | float | int | str = "1",
    acceleration: Decimal | float | int | str = "2",
    precision: int = 100,
) -> Decimal:
    """Log of sigma*(sigma/sigma_next)^2*h^-3.

    This is the terminal-return physical charge when the current
    normalised top frequency is exactly ``sigma/sigma_next``.
    """
    x_d = _decimal(x)
    x_next_d = _decimal(x_next)
    c_d = _decimal(c)
    acceleration_d = _decimal(acceleration)
    if x_d <= 1 or x_next_d <= x_d:
        raise ValueError("require 1 < x < x_next")
    if c_d <= 0 or acceleration_d <= 1:
        raise ValueError("require c>0 and acceleration>1")
    with localcontext() as context:
        context.prec = precision
        return +(
            (Decimal(6) / P) * (x_next_d / x_d).ln()
            + acceleration_d
            * c_d
            * (Decimal(2) * x_next_d - Decimal(3) * x_d)
        )


def frequency_certificate(nodes: Iterable[AncestryNode]) -> List[FrequencySlab]:
    """Split one finite nested history into bulk and required tail masses.

    The input must begin sufficiently far down the genealogy that both the
    prescribed tail masses and the remaining bulk masses decrease.  The
    returned final slab is the unresolved terminal core of the finite
    certificate.  Summing slabs from index ``j`` onwards recovers exactly
    the cumulative masses at event ``j``.
    """
    values = list(nodes)
    if not values:
        raise ValueError("at least one node is required")

    with localcontext() as context:
        context.prec = 100
        totals = [node.log_total_mass.exp() for node in values]
        tails = [node.log_tail_mass.exp() for node in values]
        bulks = [total - tail for total, tail in zip(totals, tails)]
    if any(bulk <= 0 for bulk in bulks):
        raise ValueError("the tail charge exceeds the total history mass")
    if any(
        tails[index + 1] >= tails[index]
        or bulks[index + 1] >= bulks[index]
        for index in range(len(values) - 1)
    ):
        raise ValueError("start deeper so both cumulative components decrease")

    with localcontext() as context:
        context.prec = 100
        slabs: List[FrequencySlab] = []
        for index in range(len(values) - 1):
            slabs.append(
                FrequencySlab(
                    bulk_mass=+(bulks[index] - bulks[index + 1]),
                    high_mass=+(tails[index] - tails[index + 1]),
                    log_high_frequency=-values[index + 1].log_zoom,
                )
            )
        last = values[-1]
        slabs.append(
            FrequencySlab(
                bulk_mass=bulks[-1],
                high_mass=tails[-1],
                log_high_frequency=+(
                    last.log_top_frequency - last.log_zoom
                ),
            )
        )
    return slabs


def cumulative_slab_masses(
    slabs: Iterable[FrequencySlab],
    start: int,
) -> tuple[Decimal, Decimal]:
    """Return bulk and high mass in the nested terminal interval."""
    values = list(slabs)
    if start < 0 or start >= len(values):
        raise ValueError("start must index a slab")
    with localcontext() as context:
        context.prec = 100
        return (
            +sum((slab.bulk_mass for slab in values[start:]), Decimal(0)),
            +sum((slab.high_mass for slab in values[start:]), Decimal(0)),
        )


def main() -> None:
    nodes = ancestry_sequence(
        "10000",
        4,
        c="0.001",
        acceleration="2",
        c_dep="1",
        tail_constant="0.01",
        precision=100,
    )
    slabs = frequency_certificate(nodes)
    payload = {
        "experiment": "exact dyadic next-event ancestry survivor",
        "nodes": [
            {
                "x": str(node.x),
                "interaction_order": node.interaction_order,
                "top_frequency": str(node.top_frequency),
                "log_zoom": str(node.log_zoom),
                "log_tail_fraction": str(node.log_tail_fraction),
                "ancestry_residual": (
                    None
                    if index + 1 == len(nodes)
                    else str(ancestry_residual(node, nodes[index + 1]))
                ),
            }
            for index, node in enumerate(nodes)
        ],
        "slab_count": len(slabs),
        "all_slab_masses_positive": all(
            slab.bulk_mass > 0 and slab.high_mass > 0 for slab in slabs
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
