"""Exact ledgers for the last-separated-return renewal decomposition."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
import json


BASE_SHELL_EXPONENT = Fraction(7, 4)
PARABOLIC_AGGREGATE_POWER = Fraction(1, 2)


def _nonnegative(value: Fraction, name: str) -> Fraction:
    value = Fraction(value)
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")
    return value


def full_word_weight(
    no_return_weight: Fraction,
    return_weight: Fraction,
    depth: int,
) -> Fraction:
    """Total weight of all A/B words of a fixed depth."""
    a = _nonnegative(no_return_weight, "no_return_weight")
    b = _nonnegative(return_weight, "return_weight")
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    return (a + b) ** depth


def no_return_word_weight(
    no_return_weight: Fraction,
    depth: int,
) -> Fraction:
    """Weight of the unique all-A word."""
    a = _nonnegative(no_return_weight, "no_return_weight")
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    return a**depth


def operator_words_by_leftmost_return(
    depth: int,
) -> tuple[str, tuple[tuple[str, ...], ...]]:
    """Partition A/B operator words by the leftmost B.

    Symbols are written in composition order, so the leftmost B is the
    last B chronologically.  The first return value is the all-A word;
    group k contains exactly the words whose leftmost B has index k.
    """
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    words = tuple(
        "".join(symbols)
        for symbols in product(("A", "B"), repeat=depth)
    )
    no_return = "A" * depth
    groups = tuple(
        tuple(word for word in words if word.find("B") == index)
        for index in range(depth)
    )
    return no_return, groups


def last_return_word_weight(
    no_return_weight: Fraction,
    return_weight: Fraction,
    depth: int,
) -> Fraction:
    """Group every word containing B by its last chronological B."""
    a = _nonnegative(no_return_weight, "no_return_weight")
    b = _nonnegative(return_weight, "return_weight")
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    if depth == 0:
        return Fraction(0)
    return sum(
        (
            a**after
            * b
            * (a + b) ** (depth - 1 - after)
            for after in range(depth)
        ),
        Fraction(0),
    )


def full_resolvent(
    source: Fraction,
    no_return_weight: Fraction,
    return_weight: Fraction,
) -> Fraction:
    """Scalar analogue of (I-A-B)^-1 g."""
    g = _nonnegative(source, "source")
    a = _nonnegative(no_return_weight, "no_return_weight")
    b = _nonnegative(return_weight, "return_weight")
    if a + b >= 1:
        raise ValueError("resolvent weights must sum to less than one")
    return g / (1 - a - b)


def no_return_resolvent(
    source: Fraction,
    no_return_weight: Fraction,
) -> Fraction:
    """Scalar analogue of (I-A)^-1 g."""
    g = _nonnegative(source, "source")
    a = _nonnegative(no_return_weight, "no_return_weight")
    if a >= 1:
        raise ValueError("no_return_weight must be less than one")
    return g / (1 - a)


def last_return_resolvent(
    source: Fraction,
    no_return_weight: Fraction,
    return_weight: Fraction,
) -> Fraction:
    """Scalar analogue of (I-A)^-1 B (I-A-B)^-1 g."""
    a = _nonnegative(no_return_weight, "no_return_weight")
    b = _nonnegative(return_weight, "return_weight")
    full = full_resolvent(source, a, b)
    return b * full / (1 - a)


def separated_output_heat_rate_sum(
    input_heat_rate: Fraction,
    separation_steps: int = 6,
) -> Fraction:
    """Sum output Q^2 rates for Q <= 2^-steps R."""
    rate = _nonnegative(input_heat_rate, "input_heat_rate")
    if rate == 0:
        raise ValueError("input_heat_rate must be positive")
    if separation_steps <= 0:
        raise ValueError("separation_steps must be positive")
    top_output_rate = rate / 4**separation_steps
    return Fraction(4, 3) * top_output_rate


def high_output_tail_inverse_square_sum(
    base_inverse_square: Fraction,
) -> Fraction:
    """Sum Q^-2 over dyadic Q strictly above the base output U."""
    base = _nonnegative(base_inverse_square, "base_inverse_square")
    if base == 0:
        raise ValueError("base_inverse_square must be positive")
    return base * Fraction(1, 3)


def parabolic_stretched_exponent() -> Fraction:
    """The all-starting-band last-return cost exponent."""
    return BASE_SHELL_EXPONENT + PARABOLIC_AGGREGATE_POWER


def main() -> None:
    a = Fraction(1, 4)
    b = Fraction(1, 3)
    source = Fraction(2, 5)
    payload = {
        "experiment": "last separated return renewal",
        "depth_six_full_weight": str(full_word_weight(a, b, 6)),
        "depth_six_no_return_weight": str(
            no_return_word_weight(a, 6)
        ),
        "depth_six_last_return_weight": str(
            last_return_word_weight(a, b, 6)
        ),
        "depth_six_last_return_word_count": sum(
            len(group)
            for group in operator_words_by_leftmost_return(6)[1]
        ),
        "full_resolvent": str(full_resolvent(source, a, b)),
        "no_return_resolvent": str(
            no_return_resolvent(source, a)
        ),
        "last_return_resolvent": str(
            last_return_resolvent(source, a, b)
        ),
        "six_step_heat_rate_entropy": str(
            separated_output_heat_rate_sum(Fraction(1), 6)
        ),
        "high_output_tail_inverse_square_sum": str(
            high_output_tail_inverse_square_sum(Fraction(1))
        ),
        "parabolic_stretched_exponent": str(
            parabolic_stretched_exponent()
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
