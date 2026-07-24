from fractions import Fraction
import unittest

from navier_lab.adjoint_pressure_corridor_identification import (
    aggregate_initial_band_power,
    corridor_word_weight,
    exit_word_weight,
    finite_initial_band_sum,
    finite_inverse_initial_band_sum,
    first_exit_word_weight,
    forced_stretched_exponent,
    fractional_volterra_coefficient,
    fractional_volterra_partial_sum,
    parabolic_forced_stretched_exponent,
)


class AdjointPressureCorridorIdentificationTests(unittest.TestCase):
    def test_fractional_volterra_indexing(self):
        self.assertEqual(
            fractional_volterra_coefficient(Fraction(3), 0),
            1.0,
        )
        self.assertAlmostEqual(
            fractional_volterra_coefficient(Fraction(2), 2),
            4.0,
        )
        self.assertAlmostEqual(
            fractional_volterra_coefficient(Fraction(2), 4),
            8.0,
        )

    def test_fractional_volterra_series_converges_numerically(self):
        partial_20 = fractional_volterra_partial_sum(
            Fraction(1),
            20,
        )
        partial_40 = fractional_volterra_partial_sum(
            Fraction(1),
            40,
        )
        partial_80 = fractional_volterra_partial_sum(
            Fraction(1),
            80,
        )
        self.assertLess(partial_20, partial_40)
        self.assertAlmostEqual(partial_40, partial_80, places=12)

    def test_corridor_and_exit_words_partition_every_depth(self):
        for depth in range(10):
            corridor = corridor_word_weight(Fraction(3, 5), depth)
            exit_weight = exit_word_weight(Fraction(3, 5), depth)
            self.assertEqual(corridor + exit_weight, 1)

    def test_first_exit_grouping_equals_all_exit_words(self):
        for depth in range(12):
            self.assertEqual(
                first_exit_word_weight(Fraction(7, 9), depth),
                exit_word_weight(Fraction(7, 9), depth),
            )

    def test_finite_initial_band_entropy_is_geometric(self):
        self.assertEqual(
            finite_initial_band_sum(Fraction(16), Fraction(128)),
            240,
        )
        self.assertLess(
            finite_initial_band_sum(Fraction(16), Fraction(128)),
            2 * 128,
        )

    def test_inverse_initial_band_tail_is_lower_endpoint_dominated(self):
        value = finite_inverse_initial_band_sum(
            Fraction(16),
            Fraction(128),
        )
        self.assertEqual(value, Fraction(15, 128))
        self.assertLess(value, Fraction(1, 8))

    def test_parabolic_aggregate_forces_nine_quarters(self):
        self.assertEqual(
            aggregate_initial_band_power(Fraction(1, 2)),
            Fraction(1, 2),
        )
        self.assertEqual(
            forced_stretched_exponent(Fraction(1, 2)),
            Fraction(9, 4),
        )
        self.assertEqual(
            parabolic_forced_stretched_exponent(),
            Fraction(9, 4),
        )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            fractional_volterra_coefficient(Fraction(-1), 1)
        with self.assertRaises(ValueError):
            fractional_volterra_partial_sum(Fraction(1), -1)
        with self.assertRaises(ValueError):
            corridor_word_weight(Fraction(2), 1)
        with self.assertRaises(ValueError):
            exit_word_weight(Fraction(1, 2), -1)
        with self.assertRaises(ValueError):
            first_exit_word_weight(Fraction(2), 1)
        with self.assertRaises(ValueError):
            finite_initial_band_sum(Fraction(32), Fraction(16))
        with self.assertRaises(ValueError):
            finite_initial_band_sum(Fraction(3), Fraction(10))
        with self.assertRaises(ValueError):
            finite_inverse_initial_band_sum(
                Fraction(0),
                Fraction(16),
            )
        with self.assertRaises(ValueError):
            aggregate_initial_band_power(Fraction(-1, 2))


if __name__ == "__main__":
    unittest.main()
