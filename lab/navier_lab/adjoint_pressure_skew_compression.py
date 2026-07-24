"""Exact ledgers for skew compression and critical pressure persistence."""

from __future__ import annotations

import json
from fractions import Fraction
from typing import Iterable

Vector = tuple[Fraction, ...]
Matrix = tuple[tuple[Fraction, ...], ...]


def _fraction(value: int | Fraction, name: str) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise ValueError(f"{name} must be an integer or Fraction")
    return Fraction(value)


def _order(value: int, name: str = "order") -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return value


def _vector(values: Iterable[int | Fraction], name: str = "vector") -> Vector:
    result = tuple(_fraction(value, name) for value in values)
    if not result:
        raise ValueError(f"{name} must be nonempty")
    return result


def transpose(matrix: Matrix) -> Matrix:
    """Return the exact transpose of a nonempty rectangular matrix."""
    if not matrix or not matrix[0]:
        raise ValueError("matrix must be nonempty")
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("matrix must be rectangular")
    return tuple(tuple(matrix[row][column] for row in range(len(matrix)))
                 for column in range(width))


def matrix_vector(matrix: Matrix, vector: Iterable[int | Fraction]) -> Vector:
    """Multiply an exact matrix and vector."""
    values = _vector(vector)
    if not matrix or any(len(row) != len(values) for row in matrix):
        raise ValueError("matrix and vector dimensions must agree")
    return tuple(sum((entry * value for entry, value in zip(row, values)),
                     Fraction(0))
                 for row in matrix)


def matrix_product(left: Matrix, right: Matrix) -> Matrix:
    """Multiply two exact matrices."""
    if not left or not right or not left[0] or not right[0]:
        raise ValueError("matrices must be nonempty")
    left_width = len(left[0])
    right_width = len(right[0])
    if any(len(row) != left_width for row in left):
        raise ValueError("left matrix must be rectangular")
    if any(len(row) != right_width for row in right):
        raise ValueError("right matrix must be rectangular")
    if left_width != len(right):
        raise ValueError("matrix dimensions must agree")
    right_columns = transpose(right)
    return tuple(
        tuple(
            sum((a * b for a, b in zip(row, column)), Fraction(0))
            for column in right_columns
        )
        for row in left
    )


def dot(left: Iterable[int | Fraction],
        right: Iterable[int | Fraction]) -> Fraction:
    """Return an exact Euclidean pairing."""
    left_values = _vector(left, "left")
    right_values = _vector(right, "right")
    if len(left_values) != len(right_values):
        raise ValueError("vector dimensions must agree")
    return sum((a * b for a, b in zip(left_values, right_values)),
               Fraction(0))


def norm_squared(vector: Iterable[int | Fraction]) -> Fraction:
    """Return an exact squared Euclidean norm."""
    values = _vector(vector)
    return dot(values, values)


def skew_generator() -> Matrix:
    """Return the three-dimensional skew block used by the countermodel."""
    return (
        (Fraction(0), Fraction(-1), Fraction(-1)),
        (Fraction(1), Fraction(0), Fraction(-1)),
        (Fraction(1), Fraction(1), Fraction(0)),
    )


def solenoidal_compression() -> Matrix:
    """Return A=PBP on the first two coordinates."""
    return (
        (Fraction(0), Fraction(-1)),
        (Fraction(1), Fraction(0)),
    )


def pressure_observation() -> Matrix:
    """Return C=QBP from the first two coordinates to the third."""
    return ((Fraction(1), Fraction(1)),)


def strong_trace_skew_generator() -> Matrix:
    """Return the gamma=1/2 skew block for the linear time mode."""
    return (
        (Fraction(0), Fraction(-2), Fraction(-1)),
        (Fraction(2), Fraction(0), Fraction(-1)),
        (Fraction(1), Fraction(1), Fraction(0)),
    )


def strong_trace_compression() -> Matrix:
    """Return A=2J, inverse to the Hardy factor on the time mode."""
    return (
        (Fraction(0), Fraction(-2)),
        (Fraction(2), Fraction(0)),
    )


def strong_trace_hardy_factor() -> Fraction:
    """Return H_(1/2)(t)/t=1/2."""
    return Fraction(1, 2)


def compression_identity(
    vector: Iterable[int | Fraction],
) -> tuple[Fraction, Fraction]:
    """Return both sides of ||Bz||^2=||Az||^2+||Cz||^2."""
    values = _vector(vector)
    if len(values) != 2:
        raise ValueError("vector must have dimension two")
    embedded = values + (Fraction(0),)
    full_side = norm_squared(matrix_vector(skew_generator(), embedded))
    projected = matrix_vector(solenoidal_compression(), values)
    pressure = matrix_vector(pressure_observation(), values)
    split_side = norm_squared(projected) + norm_squared(pressure)
    return full_side, split_side


def critical_depth_state(
    order: int,
    initial: Iterable[int | Fraction] = (1, 0),
) -> Vector:
    """Return A^order initial, the constant-time critical iterate."""
    steps = _order(order)
    state = _vector(initial, "initial")
    if len(state) != 2:
        raise ValueError("initial must have dimension two")
    compression = solenoidal_compression()
    for _ in range(steps):
        state = matrix_vector(compression, state)
    return state


def pressure_depth_value(order: int) -> Fraction:
    """Return C A^order e1; its absolute value is one at every depth."""
    return matrix_vector(
        pressure_observation(),
        critical_depth_state(order),
    )[0]


def feedback_source() -> Vector:
    """Return q for the exact critical feedback relation r=A(q+r)."""
    return (Fraction(-1), Fraction(-1))


def feedback_solution() -> Vector:
    """Return the exact constant feedback solution."""
    return (Fraction(1), Fraction(0))


def feedback_right_side() -> Vector:
    """Return A(q+r), equal to the exact feedback solution."""
    combined = tuple(
        source + solution
        for source, solution in zip(feedback_source(), feedback_solution())
    )
    return matrix_vector(solenoidal_compression(), combined)


def feedback_residual(order: int) -> Vector:
    """Return A^order r after removing the first order interactions."""
    return critical_depth_state(order, feedback_solution())


def feedback_residual_pressure(order: int) -> Fraction:
    """Return C A^order r, with unit absolute value for every order."""
    return matrix_vector(
        pressure_observation(),
        feedback_residual(order),
    )[0]


def strong_trace_depth_state(
    order: int,
    time: int | Fraction,
    initial: Iterable[int | Fraction] = (1, 0),
) -> Vector:
    """Return the strong-trace iterate t (mu A)^order initial."""
    time_value = _fraction(time, "time")
    if time_value < 0:
        raise ValueError("time must be nonnegative")
    state = critical_depth_state(order, initial)
    return tuple(time_value * value for value in state)


def strong_trace_feedback_source(time: int | Fraction) -> Vector:
    """Return q(t)=-t(e1+e2)."""
    time_value = _fraction(time, "time")
    if time_value < 0:
        raise ValueError("time must be nonnegative")
    return (-time_value, -time_value)


def strong_trace_feedback_solution(time: int | Fraction) -> Vector:
    """Return r(t)=t e1, which has a strong zero right trace."""
    time_value = _fraction(time, "time")
    if time_value < 0:
        raise ValueError("time must be nonnegative")
    return (time_value, Fraction(0))


def strong_trace_feedback_right_side(time: int | Fraction) -> Vector:
    """Return H_(1/2) A(q+r), equal to r on the linear time mode."""
    source = strong_trace_feedback_source(time)
    solution = strong_trace_feedback_solution(time)
    combined = tuple(
        source_value + solution_value
        for source_value, solution_value in zip(source, solution)
    )
    transported = matrix_vector(strong_trace_compression(), combined)
    factor = strong_trace_hardy_factor()
    return tuple(factor * value for value in transported)


def strong_trace_residual_pressure(
    order: int,
    time: int | Fraction,
) -> Fraction:
    """Return C T^order r(t), whose absolute value equals t."""
    return matrix_vector(
        pressure_observation(),
        strong_trace_depth_state(order, time),
    )[0]


def real_coupling_solution(coupling: int | Fraction) -> Vector:
    """Solve r_lambda=lambda A(q+r_lambda) exactly for real lambda."""
    value = _fraction(coupling, "coupling")
    denominator = 1 + value * value
    return (
        value * (1 + value) / denominator,
        value * (value - 1) / denominator,
    )


def real_coupling_norm_squared(coupling: int | Fraction) -> Fraction:
    """Return ||r_lambda||^2=2 lambda^2/(1+lambda^2)."""
    value = _fraction(coupling, "coupling")
    return 2 * value * value / (1 + value * value)


def rational_rotation(step_denominator: int) -> tuple[Fraction, Fraction]:
    """Return cosine and sine from the rational half-angle 1/n."""
    if (isinstance(step_denominator, bool)
            or not isinstance(step_denominator, int)
            or step_denominator < 1):
        raise ValueError("step_denominator must be a positive integer")
    n_value = Fraction(step_denominator)
    cosine = (n_value * n_value - 1) / (n_value * n_value + 1)
    sine = 2 * n_value / (n_value * n_value + 1)
    return cosine, sine


def unitary_leakage_ledgers(
    step_denominator: int,
    steps: int | None = None,
) -> tuple[Fraction, Fraction]:
    """Return the linear pressure sum and squared energy-defect sum."""
    if steps is None:
        steps = step_denominator
    count = _order(steps, "steps")
    cosine, sine = rational_rotation(step_denominator)
    linear = sum(
        (sine * cosine**order for order in range(count)),
        Fraction(0),
    )
    squared = sum(
        (sine * sine * cosine ** (2 * order) for order in range(count)),
        Fraction(0),
    )
    return linear, squared


def unitary_telescoped_squared_leakage(
    step_denominator: int,
    steps: int | None = None,
) -> Fraction:
    """Return 1-cosine^(2 steps), the exact unitary defect telescope."""
    if steps is None:
        steps = step_denominator
    count = _order(steps, "steps")
    cosine, _ = rational_rotation(step_denominator)
    return 1 - cosine ** (2 * count)


def main() -> None:
    payload = {
        "experiment": "skew compression and pressure persistence",
        "blocks": {
            "B": [[str(value) for value in row] for row in skew_generator()],
            "A": [
                [str(value) for value in row]
                for row in solenoidal_compression()
            ],
            "C": [
                [str(value) for value in row]
                for row in pressure_observation()
            ],
        },
        "feedback": {
            "q": [str(value) for value in feedback_source()],
            "r": [str(value) for value in feedback_solution()],
            "A(q+r)": [str(value) for value in feedback_right_side()],
            "depth_pressures": {
                str(order): str(feedback_residual_pressure(order))
                for order in range(8)
            },
        },
        "strong_zero_trace_feedback": {
            "gamma": "1/2",
            "hardy_factor_on_t": str(strong_trace_hardy_factor()),
            "A": [
                [str(value) for value in row]
                for row in strong_trace_compression()
            ],
            "r_at_zero": [
                str(value) for value in strong_trace_feedback_solution(0)
            ],
            "r_at_one": [
                str(value) for value in strong_trace_feedback_solution(1)
            ],
            "depth_pressures_at_t_equals_one": {
                str(order): str(strong_trace_residual_pressure(order, 1))
                for order in range(8)
            },
        },
        "unitary_small_step": {
            str(n_value): {
                "linear_leakage": float(unitary_leakage_ledgers(n_value)[0]),
                "squared_leakage": float(unitary_leakage_ledgers(n_value)[1]),
            }
            for n_value in (10, 100, 1000)
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
