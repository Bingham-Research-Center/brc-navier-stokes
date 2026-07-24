"""Spectral primal-adjoint pairing and its pressure-blindness.

For the reversed Navier-Stokes coefficient ``b`` and its forward Oseen
adjoint ``a``, the global L2 pairing is conserved.  Localising both fields
with a fixed orthogonal componentwise Fourier-frequency projector gives
an exact commutator flux.  A projected pressure gradient need not vanish;
its contribution pairs to zero against the projected divergence-free
field.

The finite-dimensional routines below check that algebra.  The Beltrami
ledger records an exact periodic same-trajectory example in which the
coefficient and adjoint occupy radius ``N`` while their nonzero adjoint
pressure occupies radius ``sqrt(2) N``.  It is a torus counterexample to
pressure coercion by spectral L2 pairing, not an R3 Clay trajectory.
"""

from __future__ import annotations

from fractions import Fraction
import json
import math
from typing import Iterable


Scalar = Fraction
Vector = tuple[Scalar, ...]
Matrix = tuple[Vector, ...]


def _dot(left: Vector, right: Vector) -> Scalar:
    if len(left) != len(right):
        raise ValueError("vectors must have the same dimension")
    return sum(
        (left[index] * right[index] for index in range(len(left))),
        start=Fraction(0),
    )


def _matvec(matrix: Matrix, vector: Vector) -> Vector:
    if not matrix or len(matrix) != len(vector):
        raise ValueError("matrix and vector dimensions do not match")
    if any(len(row) != len(vector) for row in matrix):
        raise ValueError("matrix must be square")
    return tuple(_dot(row, vector) for row in matrix)


def _add(*vectors: Vector) -> Vector:
    if not vectors:
        raise ValueError("at least one vector is required")
    dimension = len(vectors[0])
    if any(len(vector) != dimension for vector in vectors):
        raise ValueError("vectors must have the same dimension")
    return tuple(
        sum(
            (vector[index] for vector in vectors),
            start=Fraction(0),
        )
        for index in range(dimension)
    )


def _scale(value: Scalar, vector: Vector) -> Vector:
    return tuple(value * component for component in vector)


def _subtract(left: Vector, right: Vector) -> Vector:
    return _add(left, _scale(Fraction(-1), right))


def localised_pairing_derivative(
    *,
    adjoint: Vector,
    coefficient: Vector,
    projector: Matrix,
    transport: Matrix,
    laplacian: Matrix,
    adjoint_pressure_gradient: Vector,
    primal_pressure_gradient: Vector,
    viscosity: Scalar,
) -> Scalar:
    """Return ``d <P a,P b>/dt`` from the two evolution equations.

    The abstract equations are

        a' = nu L a + B a - g_a,
        b' = -nu L b + B b - g_b.

    The intended hypotheses are: ``P`` is orthogonal, ``L`` is
    self-adjoint and commutes with ``P``, ``B`` is skew, and the projected
    pressure gradients are orthogonal to the corresponding projected
    divergence-free fields.  The pressure gradients need not lie in the
    kernel of ``P``.
    """
    if viscosity <= 0:
        raise ValueError("viscosity must be positive")
    projected_adjoint = _matvec(projector, adjoint)
    projected_coefficient = _matvec(projector, coefficient)
    adjoint_derivative = _add(
        _scale(viscosity, _matvec(laplacian, adjoint)),
        _matvec(transport, adjoint),
        _scale(Fraction(-1), adjoint_pressure_gradient),
    )
    coefficient_derivative = _add(
        _scale(-viscosity, _matvec(laplacian, coefficient)),
        _matvec(transport, coefficient),
        _scale(Fraction(-1), primal_pressure_gradient),
    )
    return (
        _dot(
            _matvec(projector, adjoint_derivative),
            projected_coefficient,
        )
        + _dot(
            projected_adjoint,
            _matvec(projector, coefficient_derivative),
        )
    )


def localised_pairing_commutator_flux(
    *,
    adjoint: Vector,
    coefficient: Vector,
    projector: Matrix,
    transport: Matrix,
) -> Scalar:
    """Return the exact cross-projector transport flux.

    Under the hypotheses in :func:`localised_pairing_derivative`, this is

        - <(I-P)a, B P b> + <P a, B(I-P)b>.
    """
    projected_adjoint = _matvec(projector, adjoint)
    projected_coefficient = _matvec(projector, coefficient)
    low_adjoint = _subtract(adjoint, projected_adjoint)
    low_coefficient = _subtract(coefficient, projected_coefficient)
    return (
        -_dot(
            low_adjoint,
            _matvec(transport, projected_coefficient),
        )
        + _dot(
            projected_adjoint,
            _matvec(transport, low_coefficient),
        )
    )


def telescoping_increment(values: Iterable[Scalar]) -> Scalar:
    """Return the sum of consecutive increments exactly."""
    sequence = tuple(values)
    if not sequence:
        raise ValueError("values must be nonempty")
    return sum(
        (
            sequence[index + 1] - sequence[index]
            for index in range(len(sequence) - 1)
        ),
        start=Fraction(0),
    )


def beltrami_velocity(x: float, y: float, *, frequency: int = 1) -> tuple[float, float, float]:
    """Return the explicit two-direction Beltrami eigenfield."""
    if not isinstance(frequency, int) or frequency < 1:
        raise ValueError("frequency must be a positive integer")
    nx = frequency * float(x)
    ny = frequency * float(y)
    return (
        -math.sin(ny),
        math.cos(nx),
        -math.sin(nx) + math.cos(ny),
    )


def beltrami_pressure_potential(
    x: float,
    y: float,
    *,
    frequency: int = 1,
) -> float:
    """Return ``|U_N|^2/2 = 1-sin(Nx)cos(Ny)``."""
    if not isinstance(frequency, int) or frequency < 1:
        raise ValueError("frequency must be a positive integer")
    return 1.0 - math.sin(frequency * x) * math.cos(frequency * y)


def beltrami_pressure_gradient(
    x: float,
    y: float,
    *,
    primal_amplitude: float = 1.0,
    adjoint_amplitude: float = 1.0,
    frequency: int = 1,
) -> tuple[float, float, float]:
    """Return the time-independent adjoint pressure gradient."""
    if not isinstance(frequency, int) or frequency < 1:
        raise ValueError("frequency must be a positive integer")
    product = float(primal_amplitude) * float(adjoint_amplitude)
    nx = frequency * float(x)
    ny = frequency * float(y)
    return (
        -product * frequency * math.cos(nx) * math.cos(ny),
        product * frequency * math.sin(nx) * math.sin(ny),
        0.0,
    )


def beltrami_amplitudes(
    time: float,
    *,
    viscosity: float = 1.0,
    frequency: int = 1,
    primal_amplitude: float = 1.0,
    adjoint_amplitude: float = 1.0,
) -> tuple[float, float]:
    """Return reversed-primal growth and forward-adjoint decay."""
    if viscosity <= 0.0:
        raise ValueError("viscosity must be positive")
    if not isinstance(frequency, int) or frequency < 1:
        raise ValueError("frequency must be a positive integer")
    if time < 0.0:
        raise ValueError("time must be nonnegative")
    phase = viscosity * frequency * frequency * float(time)
    return (
        float(primal_amplitude) * math.exp(phase),
        float(adjoint_amplitude) * math.exp(-phase),
    )


def pressure_history_l1_lower_bound(
    horizon: float,
    *,
    primal_amplitude: float = 1.0,
    adjoint_amplitude: float = 1.0,
    frequency: int = 1,
) -> float:
    """Lower-bound the torus pressure history by one gradient component.

    On ``[0,2 pi]^3``,

        integral |partial_x(1-sin(Nx)cos(Ny))| = 32 pi N.
    """
    if horizon <= 0.0:
        raise ValueError("horizon must be positive")
    if not isinstance(frequency, int) or frequency < 1:
        raise ValueError("frequency must be a positive integer")
    return (
        32.0
        * math.pi
        * float(horizon)
        * abs(float(primal_amplitude) * float(adjoint_amplitude))
        * frequency
    )


def radial_spectral_gap(
    cutoff: float,
    *,
    frequency: int = 1,
) -> tuple[bool, bool]:
    """Report high-pass occupancy of the solenoidal pair and pressure.

    The pair occupies radius ``N``.  The nonconstant pressure gradient
    occupies radius ``sqrt(2)N``.
    """
    if cutoff <= 0.0:
        raise ValueError("cutoff must be positive")
    if not isinstance(frequency, int) or frequency < 1:
        raise ValueError("frequency must be a positive integer")
    return (
        frequency > cutoff,
        math.sqrt(2.0) * frequency > cutoff,
    )


def paired_wavevectors(
    index: int,
) -> tuple[tuple[int, int, int], tuple[int, int, int], float]:
    """Return two integer wavevectors with equal, diverging radius.

    Their difference is always ``(1,1,0)`` up to sign:

        k=(n,-n-1,0), l=(n+1,-n,0).
    """
    if not isinstance(index, int) or index < 1:
        raise ValueError("index must be a positive integer")
    first = (index, -index - 1, 0)
    second = (index + 1, -index, 0)
    radius = math.sqrt(2 * index * index + 2 * index + 1)
    return first, second, radius


def helical_mode(
    wavevector: tuple[int, int, int],
    x: float,
    y: float,
) -> tuple[float, float, float]:
    """Return a positive-helicity mode for an xy-plane wavevector."""
    qx, qy, qz = wavevector
    if qz != 0 or (qx == 0 and qy == 0):
        raise ValueError("wavevector must be nonzero and lie in the xy plane")
    radius = math.sqrt(qx * qx + qy * qy)
    phase = qx * float(x) + qy * float(y)
    return (
        -qy / radius * math.sin(phase),
        qx / radius * math.sin(phase),
        math.cos(phase),
    )


def helical_invariant_residuals(
    wavevector: tuple[int, int, int],
) -> tuple[float, ...]:
    """Return exact-form residuals for divergence and positive helicity."""
    qx, qy, qz = wavevector
    if qz != 0 or (qx == 0 and qy == 0):
        raise ValueError("wavevector must be nonzero and lie in the xy plane")
    radius = math.sqrt(qx * qx + qy * qy)
    cosine = (0.0, 0.0, 1.0)
    sine = (-qy / radius, qx / radius, 0.0)

    def cross(
        left: tuple[float, float, float],
        right: tuple[float, float, float],
    ) -> tuple[float, float, float]:
        return (
            left[1] * right[2] - left[2] * right[1],
            left[2] * right[0] - left[0] * right[2],
            left[0] * right[1] - left[1] * right[0],
        )

    q = (float(qx), float(qy), 0.0)
    q_cross_sine = cross(q, sine)
    q_cross_cosine = cross(q, cosine)
    divergence = q[0] * sine[0] + q[1] * sine[1]
    cosine_residual = tuple(
        q_cross_sine[index] - radius * cosine[index]
        for index in range(3)
    )
    sine_residual = tuple(
        -q_cross_cosine[index] - radius * sine[index]
        for index in range(3)
    )
    return (divergence,) + cosine_residual + sine_residual


def paired_beltrami_velocity(
    index: int,
    x: float,
    y: float,
) -> tuple[float, float, float]:
    """Return the sum of the equal-radius helical pair."""
    first, second, _ = paired_wavevectors(index)
    left = helical_mode(first, x, y)
    right = helical_mode(second, x, y)
    return tuple(
        left[component] + right[component]
        for component in range(3)
    )  # type: ignore[return-value]


def paired_low_pressure_coefficient(index: int) -> float:
    """Return the fixed-low-mode coefficient ``1-1/(2 R_n^2)``."""
    _, _, radius = paired_wavevectors(index)
    return 1.0 - 1.0 / (2.0 * radius * radius)


def paired_beltrami_pressure_potential(
    index: int,
    x: float,
    y: float,
) -> float:
    """Return half the squared paired field with its two pressure modes."""
    first, second, radius = paired_wavevectors(index)
    alpha = first[0] * float(x) + first[1] * float(y)
    beta = second[0] * float(x) + second[1] * float(y)
    low = 1.0 - 1.0 / (2.0 * radius * radius)
    high = 1.0 / (2.0 * radius * radius)
    return (
        1.0
        + low * math.cos(alpha - beta)
        + high * math.cos(alpha + beta)
    )


def paired_lowpass_gap(
    cutoff: float,
    *,
    index: int,
) -> tuple[bool, bool]:
    """Report low-pass occupancy of the pair and fixed pressure return."""
    if cutoff <= 0.0:
        raise ValueError("cutoff must be positive")
    _, _, radius = paired_wavevectors(index)
    return (
        radius <= cutoff,
        math.sqrt(2.0) <= cutoff,
    )


def paired_low_pressure_history_l1_lower_bound(
    horizon: float,
    *,
    index: int,
    primal_amplitude: float = 1.0,
    adjoint_amplitude: float = 1.0,
) -> float:
    """Lower-bound the fixed-low pressure history by one component.

    The low pressure mode is

        c_n cos(x+y),  c_n=1-1/(2 R_n^2).

    One component of its gradient has torus L1 norm ``16 pi^2 c_n``.
    """
    if horizon <= 0.0:
        raise ValueError("horizon must be positive")
    coefficient = paired_low_pressure_coefficient(index)
    return (
        16.0
        * math.pi**2
        * float(horizon)
        * abs(float(primal_amplitude) * float(adjoint_amplitude))
        * coefficient
    )


def certificate() -> dict[str, float | bool | str]:
    cutoff = 2.0
    pair_low, pressure_low = paired_lowpass_gap(cutoff, index=20)
    primal, adjoint = beltrami_amplitudes(0.7)
    gradient = beltrami_pressure_gradient(0.0, 0.0)
    return {
        "experiment": "spectral primal-adjoint pressure blindness",
        "amplitude_product": primal * adjoint,
        "pressure_gradient_at_origin": abs(gradient[0]),
        "pair_below_fixed_low_cutoff": pair_low,
        "pressure_below_fixed_low_cutoff": pressure_low,
        "fixed_low_pressure_history_lower_bound": (
            paired_low_pressure_history_l1_lower_bound(
                1.0,
                index=20,
            )
        ),
    }


def main() -> None:
    print(json.dumps(certificate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
