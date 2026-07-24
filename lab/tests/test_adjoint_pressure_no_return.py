from fractions import Fraction
import unittest

from navier_lab.adjoint_pressure_no_return import (
    aggregate_depth_ratio,
    aggregate_depth_term,
    direct_source_frequency_telescope,
    direct_source_integrated_power,
    dyadic_heat_budget,
    parabolic_no_return_pressure_power,
)


class AdjointPressureNoReturnTests(unittest.TestCase):
    def test_direct_source_integrates_to_seven_quarters(self):
        self.assertEqual(
            direct_source_integrated_power(),
            Fraction(7, 4),
        )

    def test_infinite_lower_band_heat_budget_is_geometric(self):
        self.assertEqual(
            dyadic_heat_budget(Fraction(1)),
            Fraction(4, 3),
        )

    def test_all_frequency_ratios_telescope_to_pressure_scale(self):
        for path in (
            (),
            (Fraction(8),),
            (Fraction(8), Fraction(32), Fraction(2)),
            (Fraction(256), Fraction(4), Fraction(64), Fraction(1)),
        ):
            self.assertEqual(
                direct_source_frequency_telescope(
                    Fraction(16),
                    path,
                    Fraction(3, 5),
                ),
                Fraction(3, 5),
            )

    def test_depth_zero_has_one_starting_heat_clock(self):
        action = Fraction(2, 3)
        budget = Fraction(5, 7)
        self.assertEqual(
            aggregate_depth_term(action, budget, 0),
            action * budget,
        )

    def test_aggregate_depth_ratio_has_factorial_decay(self):
        action = Fraction(7, 5)
        budget = Fraction(3, 8)
        for depth in range(8):
            current = aggregate_depth_term(action, budget, depth)
            following = aggregate_depth_term(
                action,
                budget,
                depth + 1,
            )
            self.assertEqual(
                following / current,
                aggregate_depth_ratio(action, budget, depth),
            )

    def test_parabolic_sum_retains_seven_quarters_power(self):
        self.assertEqual(
            parabolic_no_return_pressure_power(),
            Fraction(7, 4),
        )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            dyadic_heat_budget(Fraction(0))
        with self.assertRaises(ValueError):
            direct_source_frequency_telescope(
                Fraction(0),
                (),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            direct_source_frequency_telescope(
                Fraction(1),
                (Fraction(-1),),
                Fraction(1),
            )
        with self.assertRaises(ValueError):
            aggregate_depth_term(Fraction(1), Fraction(1), -1)
        with self.assertRaises(ValueError):
            aggregate_depth_ratio(Fraction(0), Fraction(1), 0)


if __name__ == "__main__":
    unittest.main()
