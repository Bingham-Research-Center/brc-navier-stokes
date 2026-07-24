from fractions import Fraction
import unittest

from navier_lab.adjoint_pressure_one_return import (
    PARABOLIC_FREQUENCY_EXPONENT,
    direct_high_state_exponent,
    heat_clock_gain_power,
    one_return_prefactor_power,
    one_return_pressure_power,
    one_return_stretched_exponent,
    physical_zoom_prefactor_exponent,
)


class AdjointPressureOneReturnTests(unittest.TestCase):
    def test_subparabolic_clock_has_positive_gain(self):
        self.assertEqual(
            heat_clock_gain_power(Fraction(1, 16)),
            Fraction(7, 8),
        )

    def test_superparabolic_clock_is_saturated(self):
        self.assertEqual(
            heat_clock_gain_power(Fraction(3, 4)),
            0,
        )

    def test_prefactor_is_piecewise_exact(self):
        self.assertEqual(
            one_return_prefactor_power(Fraction(1, 4)),
            Fraction(3, 4),
        )
        self.assertEqual(
            one_return_prefactor_power(Fraction(3, 4)),
            Fraction(3, 4),
        )

    def test_one_sixteenth_return_forces_forty_three_sixteenths(self):
        self.assertEqual(
            one_return_stretched_exponent(Fraction(1, 16)),
            Fraction(43, 16),
        )

    def test_parabolic_return_has_nine_quarters_exponent(self):
        self.assertEqual(
            one_return_stretched_exponent(
                PARABOLIC_FREQUENCY_EXPONENT
            ),
            Fraction(9, 4),
        )

    def test_piecewise_exponent_is_symmetric_about_one_half(self):
        self.assertEqual(
            one_return_stretched_exponent(Fraction(1, 4)),
            one_return_stretched_exponent(Fraction(3, 4)),
        )
        self.assertEqual(
            one_return_stretched_exponent(Fraction(1, 4)),
            Fraction(5, 2),
        )

    def test_nine_quarters_is_the_global_piecewise_minimum(self):
        samples = (
            Fraction(1, 100),
            Fraction(1, 4),
            Fraction(1, 2),
            Fraction(3, 4),
            Fraction(2, 1),
        )
        values = [one_return_stretched_exponent(x) for x in samples]
        self.assertEqual(min(values), Fraction(9, 4))

    def test_forced_exponent_is_exact_pressure_boundary(self):
        for beta in (
            Fraction(1, 16),
            Fraction(1, 2),
            Fraction(3, 4),
        ):
            gamma = one_return_stretched_exponent(beta)
            self.assertEqual(
                one_return_pressure_power(beta, gamma),
                0,
            )

    def test_direct_floor_is_insufficient_below_parabolic_frequency(self):
        beta = Fraction(1, 16)
        self.assertEqual(
            one_return_pressure_power(
                beta,
                direct_high_state_exponent(beta),
            ),
            Fraction(7, 8),
        )

    def test_direct_and_return_exponents_agree_above_parabolic(self):
        beta = Fraction(3, 4)
        self.assertEqual(
            one_return_stretched_exponent(beta),
            direct_high_state_exponent(beta),
        )

    def test_physical_zoom_keeps_cubic_prefactor(self):
        self.assertEqual(physical_zoom_prefactor_exponent(), 3)

    def test_invalid_exponents_are_rejected(self):
        with self.assertRaises(ValueError):
            one_return_stretched_exponent(Fraction(0))
        with self.assertRaises(ValueError):
            one_return_pressure_power(
                Fraction(1, 2),
                Fraction(-1, 2),
            )


if __name__ == "__main__":
    unittest.main()
