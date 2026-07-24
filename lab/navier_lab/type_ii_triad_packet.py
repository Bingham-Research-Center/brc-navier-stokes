"""Exact triad and scaling ledgers for a critical Type-II packet."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import sqrt


WaveVector = tuple[int, int, int]


@dataclass(frozen=True)
class RationalComplex:
    """A minimal exact complex number with rational components."""

    real: Fraction = Fraction(0)
    imag: Fraction = Fraction(0)

    def __add__(self, other: RationalComplex) -> RationalComplex:
        return RationalComplex(
            self.real + other.real,
            self.imag + other.imag,
        )

    def __mul__(self, other: RationalComplex) -> RationalComplex:
        return RationalComplex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real,
        )

    def scale(self, factor: Fraction) -> RationalComplex:
        return RationalComplex(factor * self.real, factor * self.imag)

    def squared_modulus(self) -> Fraction:
        return self.real**2 + self.imag**2


ZERO = RationalComplex()


def dyadic_heat_band_multipliers() -> dict[int, Fraction]:
    """Return the exact Gaussian-band multipliers at squared modes 1, 4, 5.

    The heat-scale endpoints are ``log(2)`` and ``2 log(2)``, so the
    multiplier at squared frequency ``n`` is ``2**(-n)-4**(-n)``.
    """
    return {
        squared_frequency: (
            Fraction(1, 2**squared_frequency)
            - Fraction(1, 4**squared_frequency)
        )
        for squared_frequency in (1, 4, 5)
    }


def triad_fourier_modes() -> dict[
    WaveVector,
    tuple[RationalComplex, RationalComplex, RationalComplex],
]:
    """Return Fourier coefficients of the explicit divergence-free triad.

    The stream function is
    ``cos(x) + cos(2y) + cos(x+2y)`` and
    ``u=(partial_y phi,-partial_x phi,0)``.
    """
    modes: dict[
        WaveVector,
        tuple[RationalComplex, RationalComplex, RationalComplex],
    ] = {}
    for wave in ((1, 0, 0), (0, 2, 0), (1, 2, 0)):
        for sign in (-1, 1):
            signed_wave = tuple(sign * entry for entry in wave)
            k_x, k_y, _ = signed_wave
            half = Fraction(1, 2)
            modes[signed_wave] = (
                RationalComplex(imag=half * k_y),
                RationalComplex(imag=-half * k_x),
                ZERO,
            )
    return modes


def is_divergence_free(
    wave: WaveVector,
    coefficient: tuple[RationalComplex, RationalComplex, RationalComplex],
) -> bool:
    """Check ``wave dot coefficient = 0`` exactly."""
    total = ZERO
    for component, entry in zip(wave, coefficient, strict=True):
        total = total + entry.scale(Fraction(component))
    return total == ZERO


def convolution_triad_flux(
    multipliers: dict[int, Fraction],
) -> Fraction:
    """Compute the normalized mean of ``u tensor u : grad(Su)`` exactly."""
    modes = triad_fourier_modes()
    total = ZERO
    for wave_a, wave_b, wave_c in product(modes, repeat=3):
        if any(
            wave_a[index] + wave_b[index] + wave_c[index]
            for index in range(3)
        ):
            continue
        squared_frequency = sum(entry * entry for entry in wave_c)
        multiplier = multipliers[squared_frequency]
        vector_a = modes[wave_a]
        vector_b = modes[wave_b]
        vector_c = modes[wave_c]
        for first_index in range(3):
            for derivative_index in range(3):
                derivative = RationalComplex(
                    imag=Fraction(wave_c[derivative_index])
                )
                term = (
                    vector_a[first_index]
                    * vector_b[derivative_index]
                    * derivative
                    * vector_c[first_index]
                ).scale(multiplier)
                total = total + term
    if total.imag != 0:
        raise ArithmeticError("real triad flux acquired an imaginary part")
    return total.real


def closed_triad_flux(
    multipliers: dict[int, Fraction],
) -> Fraction:
    """Return the closed three-mode flux formula."""
    return (
        -Fraction(1, 2) * multipliers[1]
        + 2 * multipliers[4]
        - Fraction(3, 2) * multipliers[5]
    )


def band_energy_pairing(
    multipliers: dict[int, Fraction],
) -> Fraction:
    """Return the normalized positive pairing ``<u,Su>``."""
    total = Fraction(0)
    for wave, vector in triad_fourier_modes().items():
        squared_frequency = sum(entry * entry for entry in wave)
        total += multipliers[squared_frequency] * sum(
            component.squared_modulus() for component in vector
        )
    return total


def packet_radius_powers() -> dict[str, Fraction]:
    """Return the fixed-energy packet powers in its physical radius."""
    return {
        "velocity_amplitude": Fraction(-3, 2),
        "weak_l3": Fraction(-1, 2),
        "turnover_time": Fraction(5, 2),
        "nonlinear_work_rate": Fraction(-5, 2),
        "enstrophy": Fraction(-2),
        "integrated_nonlinear_work": Fraction(0),
        "viscous_dissipation": Fraction(1, 2),
        "effective_viscosity": Fraction(1, 2),
        "weak_l3_fourth_power_occupation": Fraction(1, 2),
    }


def packet_scaling(
    radius: float,
    amplitude: float,
    viscosity: float,
) -> dict[str, float]:
    """Evaluate the exact monomial packet ledger."""
    if radius <= 0 or amplitude <= 0 or viscosity <= 0:
        raise ValueError("radius, amplitude, and viscosity must be positive")
    weak_l3 = amplitude * radius ** (-0.5)
    turnover_time = radius**2.5 / amplitude
    nonlinear_rate = amplitude**3 * radius ** (-2.5)
    enstrophy = amplitude**2 * radius ** (-2)
    return {
        "weak_l3": weak_l3,
        "turnover_time": turnover_time,
        "nonlinear_rate": nonlinear_rate,
        "enstrophy": enstrophy,
        "integrated_nonlinear_work": nonlinear_rate * turnover_time,
        "viscous_dissipation": (
            viscosity * enstrophy * turnover_time
        ),
        "effective_viscosity": viscosity * sqrt(radius) / amplitude,
        "weak_l3_fourth_power_occupation": (
            weak_l3**4 * turnover_time
        ),
    }


def report() -> str:
    multipliers = dyadic_heat_band_multipliers()
    flux = convolution_triad_flux(multipliers)
    scaling = packet_scaling(
        radius=2.0**-10,
        amplitude=1.0,
        viscosity=1.0,
    )
    return "\n".join(
        [
            "Type-II triad packet certificate",
            f"multipliers: {multipliers}",
            f"exact normalized triad flux: {flux}",
            f"positive band pairing: {band_energy_pairing(multipliers)}",
            f"radius powers: {packet_radius_powers()}",
            (
                "sample fixed nonlinear work: "
                f"{scaling['integrated_nonlinear_work']}"
            ),
            (
                "sample square-root dissipation: "
                f"{scaling['viscous_dissipation']}"
            ),
        ]
    )


if __name__ == "__main__":
    print(report())
