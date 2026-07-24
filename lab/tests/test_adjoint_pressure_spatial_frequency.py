from fractions import Fraction
import unittest

from navier_lab.adjoint_pressure_spatial_frequency import (
    BASE_SHELL_EXPONENT,
    amplified_stretched_exponent,
    high_tail_pressure_power,
    inner_high_tail_power,
    off_diagonal_error_power,
    physical_zoom_prefactor_exponent,
    quadratic_terminal_toll_exponent,
)


class AdjointPressureSpatialFrequencyTests(unittest.TestCase):
    def test_frequency_power_adds_to_the_shell_exponent(self):
        self.assertEqual(
            amplified_stretched_exponent(Fraction(1, 16)),
            Fraction(29, 16),
        )

    def test_amplified_exponent_is_the_exact_pressure_boundary(self):
        for beta in (
            Fraction(1, 100),
            Fraction(1, 16),
            Fraction(1, 2),
        ):
            gamma = amplified_stretched_exponent(beta)
            self.assertEqual(
                high_tail_pressure_power(beta, gamma),
                0,
            )

    def test_old_stretched_floor_makes_high_tail_vanish(self):
        beta = Fraction(1, 16)
        self.assertEqual(
            high_tail_pressure_power(beta, BASE_SHELL_EXPONENT),
            beta,
        )

    def test_weaker_log_floor_has_positive_vanishing_power(self):
        beta = Fraction(1, 10)
        gamma = Fraction(9, 5)
        self.assertGreater(high_tail_pressure_power(beta, gamma), 0)

    def test_stronger_log_floor_is_not_excluded_by_the_ceiling(self):
        beta = Fraction(1, 10)
        gamma = Fraction(2, 1)
        self.assertLess(high_tail_pressure_power(beta, gamma), 0)

    def test_inner_high_tail_decays_by_inverse_frequency(self):
        self.assertEqual(
            inner_high_tail_power(Fraction(3, 20)),
            Fraction(3, 20),
        )

    def test_two_moment_off_diagonal_error_is_strictly_higher_order(self):
        beta = Fraction(1, 16)
        self.assertEqual(
            off_diagonal_error_power(beta),
            Fraction(99, 16),
        )
        self.assertGreater(
            off_diagonal_error_power(beta),
            amplified_stretched_exponent(beta),
        )

    def test_quadratic_toll_remains_only_polynomial(self):
        self.assertEqual(
            quadratic_terminal_toll_exponent(Fraction(1, 16)),
            Fraction(25, 8),
        )

    def test_physical_zoom_keeps_the_cubic_prefactor(self):
        self.assertEqual(physical_zoom_prefactor_exponent(), 3)

    def test_invalid_frequency_and_log_exponents_are_rejected(self):
        with self.assertRaises(ValueError):
            amplified_stretched_exponent(Fraction(-1, 10))
        with self.assertRaises(ValueError):
            high_tail_pressure_power(
                Fraction(1, 10),
                Fraction(-1, 10),
            )


if __name__ == "__main__":
    unittest.main()
