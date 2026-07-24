"""Scalar ancestry survivor after spatial-frequency cost amplification.

If ``F(h)=h**(-beta)``, the reviewed spatial-frequency theorem changes
the stretched coordinate from ``h**(-7/4)`` to
``y=h**(-(7/4+beta))``.  This module checks that the stronger total-cost
ledger, exact next-event ancestry, and quadratic terminal tail still fit
inside one finite nonnegative nested history.

This is not a coefficient field, Oseen solution, or Navier--Stokes
trajectory.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, localcontext
import json
from typing import Iterable, List


BASE_EXPONENT = Decimal(7) / Decimal(4)


def _decimal(value: Decimal | float | int | str) -> Decimal:
    if isinstance(value, Decimal):
        return value
    return Decimal(str(value))


def amplified_exponent(beta: Decimal | float | int | str) -> Decimal:
    beta_d = _decimal(beta)
    if beta_d <= 0:
        raise ValueError("beta must be positive")
    return BASE_EXPONENT + beta_d


def _validate(
    y: Decimal,
    beta: Decimal,
    c: Decimal,
    acceleration: Decimal,
    tail_constant: Decimal,
) -> None:
    if y <= 1:
        raise ValueError("y=h^(-(7/4+beta)) must exceed one")
    if beta <= 0:
        raise ValueError("beta must be positive")
    if c <= 0:
        raise ValueError("c must be positive")
    if acceleration <= 1:
        raise ValueError("acceleration must exceed one")
    if tail_constant <= 0:
        raise ValueError("tail_constant must be positive")


@dataclass(frozen=True)
class AmplifiedNode:
    """One amplified-cost event in logarithmic coordinates."""

    y: Decimal
    h: Decimal
    beta: Decimal
    exponent: Decimal
    log_frequency: Decimal
    log_dissipation: Decimal
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
        with localcontext() as context:
            context.prec = 100
            return +(
                Decimal("1.5") * self.h.ln()
                - self.log_zoom / Decimal(2)
            )


@dataclass(frozen=True)
class AmplifiedSlab:
    """Fresh bulk and high-frequency mass on one terminal time annulus."""

    bulk_mass: Decimal
    high_mass: Decimal
    log_high_frequency: Decimal


def amplified_node(
    y: Decimal | float | int | str,
    *,
    beta: Decimal | float | int | str = "0.0625",
    c: Decimal | float | int | str = "1",
    acceleration: Decimal | float | int | str = "2",
    tail_constant: Decimal | float | int | str = "1",
    precision: int = 100,
) -> AmplifiedNode:
    """Return a node saturating the amplified total-cost exponent."""
    y_d = _decimal(y)
    beta_d = _decimal(beta)
    c_d = _decimal(c)
    acceleration_d = _decimal(acceleration)
    tail_constant_d = _decimal(tail_constant)
    _validate(y_d, beta_d, c_d, acceleration_d, tail_constant_d)
    exponent = amplified_exponent(beta_d)

    with localcontext() as context:
        context.prec = precision
        log_y = y_d.ln()
        log_h = -log_y / exponent
        h = log_h.exp()
        log_frequency = -beta_d * log_h
        stretched_cost = c_d * y_d
        log_dissipation = -Decimal(3) * log_h + stretched_cost
        log_zoom = Decimal(3) * log_h - acceleration_d * stretched_cost
        log_total = -(acceleration_d - 1) * stretched_cost
        log_tail = (
            tail_constant_d.ln()
            - acceleration_d * stretched_cost
            + Decimal(2) * log_frequency
        )
        log_time = Decimal(2) * log_zoom + log_h
        return AmplifiedNode(
            y=+y_d,
            h=+h,
            beta=+beta_d,
            exponent=+exponent,
            log_frequency=+log_frequency,
            log_dissipation=+log_dissipation,
            log_zoom=+log_zoom,
            log_total_mass=+log_total,
            log_tail_mass=+log_tail,
            log_physical_time=+log_time,
        )


def next_amplified_depth(
    y: Decimal | float | int | str,
    *,
    beta: Decimal | float | int | str = "0.0625",
    c: Decimal | float | int | str = "1",
    acceleration: Decimal | float | int | str = "2",
    precision: int = 100,
) -> Decimal:
    """Solve ``sigma_next=sigma/F`` for ``F(h)=h**(-beta)``."""
    y_d = _decimal(y)
    beta_d = _decimal(beta)
    c_d = _decimal(c)
    acceleration_d = _decimal(acceleration)
    node = amplified_node(
        y_d,
        beta=beta_d,
        c=c_d,
        acceleration=acceleration_d,
        precision=precision,
    )

    with localcontext() as context:
        context.prec = precision
        coefficient = acceleration_d * c_d
        target = node.log_frequency
        low = Decimal(0)
        high = target / coefficient

        def residual(increment: Decimal) -> Decimal:
            return (
                coefficient * increment
                + (Decimal(3) / node.exponent)
                * (Decimal(1) + increment / y_d).ln()
                - target
            )

        for _ in range(4 * precision):
            middle = (low + high) / Decimal(2)
            if residual(middle) < 0:
                low = middle
            else:
                high = middle
        result = y_d + (low + high) / Decimal(2)
        if result <= y_d:
            raise ArithmeticError("working precision cannot resolve next depth")
        return +result


def amplified_sequence(
    y_start: Decimal | float | int | str,
    count: int,
    *,
    beta: Decimal | float | int | str = "0.0625",
    c: Decimal | float | int | str = "1",
    acceleration: Decimal | float | int | str = "2",
    tail_constant: Decimal | float | int | str = "1",
    precision: int = 100,
) -> List[AmplifiedNode]:
    """Generate nodes satisfying exact polynomial-frequency ancestry."""
    if count < 1:
        raise ValueError("count must be positive")
    y = _decimal(y_start)
    nodes: List[AmplifiedNode] = []
    for index in range(count):
        nodes.append(
            amplified_node(
                y,
                beta=beta,
                c=c,
                acceleration=acceleration,
                tail_constant=tail_constant,
                precision=precision,
            )
        )
        if index + 1 < count:
            y = next_amplified_depth(
                y,
                beta=beta,
                c=c,
                acceleration=acceleration,
                precision=precision,
            )
    return nodes


def ancestry_residual(
    current: AmplifiedNode,
    following: AmplifiedNode,
) -> Decimal:
    """Return ``log(sigma_next*F_current/sigma_current)``."""
    with localcontext() as context:
        context.prec = 100
        return +(
            following.log_zoom
            + current.log_frequency
            - current.log_zoom
        )


def amplification_identity_residual(node: AmplifiedNode) -> Decimal:
    """Return ``log(F*h^-7/4)-log(y)``."""
    with localcontext() as context:
        context.prec = 100
        return +(
            node.log_frequency
            - BASE_EXPONENT * node.h.ln()
            - node.y.ln()
        )


def cost_identity_residual(
    node: AmplifiedNode,
    *,
    c: Decimal | float | int | str = "1",
) -> Decimal:
    """Return ``log(D*h^3)-c*F*h^-7/4``."""
    c_d = _decimal(c)
    with localcontext() as context:
        context.prec = 100
        return +(
            node.log_dissipation
            + Decimal(3) * node.h.ln()
            - c_d * node.y
        )


def next_event_charge_log(
    y: Decimal | float | int | str,
    y_next: Decimal | float | int | str,
    *,
    beta: Decimal | float | int | str = "0.0625",
    c: Decimal | float | int | str = "1",
    acceleration: Decimal | float | int | str = "2",
    precision: int = 100,
) -> Decimal:
    """Log of ``sigma*(sigma/sigma_next)^2*h^-3``."""
    y_d = _decimal(y)
    y_next_d = _decimal(y_next)
    beta_d = _decimal(beta)
    c_d = _decimal(c)
    acceleration_d = _decimal(acceleration)
    exponent = amplified_exponent(beta_d)
    if y_d <= 1 or y_next_d <= y_d:
        raise ValueError("require 1 < y < y_next")
    if c_d <= 0 or acceleration_d <= 1:
        raise ValueError("require c>0 and acceleration>1")
    with localcontext() as context:
        context.prec = precision
        return +(
            (Decimal(6) / exponent) * (y_next_d / y_d).ln()
            + acceleration_d
            * c_d
            * (Decimal(2) * y_next_d - Decimal(3) * y_d)
        )


def frequency_certificate(
    nodes: Iterable[AmplifiedNode],
) -> List[AmplifiedSlab]:
    """Split one finite nested history into fresh bulk and tail masses."""
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
        raise ValueError("start deeper so cumulative components decrease")

    with localcontext() as context:
        context.prec = 100
        slabs: List[AmplifiedSlab] = []
        for index in range(len(values) - 1):
            slabs.append(
                AmplifiedSlab(
                    bulk_mass=+(bulks[index] - bulks[index + 1]),
                    high_mass=+(tails[index] - tails[index + 1]),
                    log_high_frequency=-values[index + 1].log_zoom,
                )
            )
        last = values[-1]
        slabs.append(
            AmplifiedSlab(
                bulk_mass=bulks[-1],
                high_mass=tails[-1],
                log_high_frequency=+(
                    last.log_frequency - last.log_zoom
                ),
            )
        )
    return slabs


def cumulative_slab_masses(
    slabs: Iterable[AmplifiedSlab],
    start: int,
) -> tuple[Decimal, Decimal]:
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
    nodes = amplified_sequence(
        "10000",
        4,
        beta="0.0625",
        c="0.001",
        acceleration="2",
        tail_constant="0.01",
    )
    payload = {
        "experiment": "amplified spatial-frequency ancestry survivor",
        "base_exponent": str(BASE_EXPONENT),
        "frequency_exponent": str(nodes[0].beta),
        "amplified_exponent": str(nodes[0].exponent),
        "max_ancestry_residual": str(
            max(
                abs(ancestry_residual(current, following))
                for current, following in zip(nodes, nodes[1:])
            )
        ),
        "last_tail_fraction_log": str(nodes[-1].log_tail_fraction),
        "last_frequency_to_kill_log_gap": str(
            nodes[-1].log_frequency - nodes[-1].log_kill_frequency
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
