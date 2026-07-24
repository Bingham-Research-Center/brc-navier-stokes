import math
import unittest

from navier_lab.adjoint_pressure_parabolic_coefficient_tail import (
    comparison_prefactor,
    logarithmic_kappa,
    logarithmic_tail_power,
    low_pressure_bound,
    resolvent_factor,
    superparabolic_cutoff,
    tail_floor,
)


class AdjointPressureParabolicCoefficientTailTests(unittest.TestCase):
    def test_half_order_resolvent_has_quadratic_exponent(self) -> None:
        self.assertAlmostEqual(resolvent_factor(2.0, 1.5), math.exp(6.0))

    def test_low_pressure_has_seven_quarters_power(self) -> None:
        h = 0.25
        value = low_pressure_bound(h, 0.0)
        self.assertAlmostEqual(value, h ** (7.0 / 4.0))

    def test_comparison_has_three_halves_power(self) -> None:
        h = 0.25
        value = comparison_prefactor(h, 0.0)
        self.assertAlmostEqual(value, h ** (3.0 / 2.0))

    def test_tail_floor_inverts_the_comparison(self) -> None:
        h = 0.125
        kappa = 1.25
        pressure = 0.4
        prefactor = comparison_prefactor(h, kappa)
        floor = tail_floor(h, kappa, pressure)
        self.assertAlmostEqual(prefactor * math.sqrt(floor), pressure / 2.0)

    def test_logarithmic_choice_has_exact_resolvent_loss(self) -> None:
        h = 1.0e-10
        epsilon = 0.3
        growth = 1.7
        kappa = logarithmic_kappa(h, epsilon, growth)
        self.assertAlmostEqual(
            resolvent_factor(kappa, growth),
            h ** (-epsilon / 2.0),
            places=10,
        )

    def test_cutoff_is_superparabolic(self) -> None:
        epsilon = 0.2
        growth = 1.0
        ratios = [
            superparabolic_cutoff(h, epsilon, growth) * math.sqrt(h)
            for h in (1.0e-4, 1.0e-8, 1.0e-16)
        ]
        self.assertLess(ratios[0], ratios[1])
        self.assertLess(ratios[1], ratios[2])

    def test_logarithmic_tail_power_is_nearly_inverse_cubic(self) -> None:
        self.assertAlmostEqual(logarithmic_tail_power(0.1), -2.9)

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            logarithmic_kappa(1.0, 0.2)
        with self.assertRaises(ValueError):
            tail_floor(0.5, 1.0, 0.0)
        with self.assertRaises(ValueError):
            resolvent_factor(-1.0)


if __name__ == "__main__":
    unittest.main()
