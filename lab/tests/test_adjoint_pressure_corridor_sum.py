from fractions import Fraction
import unittest

from navier_lab.adjoint_pressure_corridor_sum import (
    aggregate_closed_form,
    aggregate_depth_term,
    aggregate_partial_sum,
    corridor_prefactor_power,
    corridor_pressure_power,
    corridor_stretched_exponent,
    depth_term_ratio,
    finite_dyadic_heat_sum,
    infinite_dyadic_heat_sum,
    parabolic_prefactor_power,
    parabolic_stretched_exponent,
    weighted_path_clock_sum,
)


class AdjointPressureCorridorSumTests(unittest.TestCase):
    def test_infinite_lower_band_entropy_is_four_thirds(self):
        self.assertEqual(
            infinite_dyadic_heat_sum(Fraction(7, 5)),
            Fraction(28, 15),
        )
        finite = finite_dyadic_heat_sum(Fraction(1), 12)
        self.assertLess(finite, Fraction(4, 3))
        self.assertEqual(
            Fraction(4, 3) - finite,
            Fraction(1, 3 * 4**11),
        )

    def test_weighted_path_sum_has_m_plus_one_clocks(self):
        initial = Fraction(2, 3)
        corridor = Fraction(3, 5)
        self.assertEqual(
            weighted_path_clock_sum(initial, corridor, 0),
            initial,
        )
        self.assertEqual(
            weighted_path_clock_sum(initial, corridor, 2),
            Fraction(1, 25),
        )

    def test_aggregate_depth_term_has_correct_indexing(self):
        action = Fraction(3, 2)
        initial = Fraction(2, 3)
        corridor = Fraction(2, 3)
        self.assertEqual(
            aggregate_depth_term(action, initial, corridor, 0),
            1,
        )
        self.assertEqual(
            aggregate_depth_term(action, initial, corridor, 1),
            Fraction(1, 2),
        )
        self.assertEqual(
            aggregate_depth_term(action, initial, corridor, 4),
            Fraction(1, 120),
        )

    def test_successive_term_ratio_is_factorial(self):
        action = Fraction(3, 2)
        initial = Fraction(2, 3)
        corridor = Fraction(2, 3)
        for depth in range(8):
            current = aggregate_depth_term(
                action,
                initial,
                corridor,
                depth,
            )
            following = aggregate_depth_term(
                action,
                initial,
                corridor,
                depth + 1,
            )
            self.assertEqual(
                following / current,
                depth_term_ratio(action, corridor, depth),
            )

    def test_partial_sums_converge_to_closed_exponential_series(self):
        action = Fraction(1, 3)
        initial = Fraction(2, 5)
        corridor = Fraction(1, 2)
        partial = float(
            aggregate_partial_sum(
                action,
                initial,
                corridor,
                18,
            )
        )
        closed = aggregate_closed_form(
            action,
            initial,
            corridor,
        )
        self.assertAlmostEqual(partial, closed, places=14)

    def test_parabolic_corridor_forces_nine_quarters(self):
        self.assertEqual(parabolic_prefactor_power(), Fraction(1, 2))
        self.assertEqual(
            parabolic_stretched_exponent(),
            Fraction(9, 4),
        )
        self.assertEqual(
            corridor_pressure_power(Fraction(9, 4)),
            0,
        )

    def test_subparabolic_corridor_matches_one_return_exponent(self):
        self.assertEqual(
            corridor_prefactor_power(Fraction(1, 4)),
            Fraction(3, 4),
        )
        self.assertEqual(
            corridor_stretched_exponent(Fraction(1, 4)),
            Fraction(5, 2),
        )
        self.assertEqual(
            corridor_stretched_exponent(Fraction(1, 2)),
            Fraction(9, 4),
        )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            finite_dyadic_heat_sum(Fraction(1), 0)
        with self.assertRaises(ValueError):
            infinite_dyadic_heat_sum(Fraction(0))
        with self.assertRaises(ValueError):
            weighted_path_clock_sum(
                Fraction(1),
                Fraction(1),
                -1,
            )
        with self.assertRaises(ValueError):
            aggregate_partial_sum(
                Fraction(1),
                Fraction(1),
                Fraction(1),
                -1,
            )
        with self.assertRaises(ValueError):
            aggregate_closed_form(
                Fraction(-1),
                Fraction(1),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            depth_term_ratio(
                Fraction(1),
                Fraction(1),
                -1,
            )
        with self.assertRaises(ValueError):
            corridor_pressure_power(Fraction(0))
        with self.assertRaises(ValueError):
            corridor_prefactor_power(Fraction(3, 4))


if __name__ == "__main__":
    unittest.main()
