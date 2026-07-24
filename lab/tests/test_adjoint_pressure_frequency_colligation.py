import math
import unittest
from fractions import Fraction

from navier_lab.adjoint_pressure_frequency_colligation import (
    alternating_frequency_family,
    alternating_linear_leakage,
    band_action,
    critical_step_action,
    dyson_iterate_bound,
    effective_parabolic_time,
    heat_weighted_alternating_leakage,
    logarithmic_depth_log_tail,
    one_sided_ray_ledgers,
    pressure_depth_bound,
    pressure_tail_majorant,
    required_drift_to_critical_ratio,
)


class AdjointPressureFrequencyColligationTests(unittest.TestCase):
    def test_band_action_is_scale_zero_on_a_parabolic_window(self):
        for frequency in (1, 2, 10, 1000):
            self.assertEqual(
                band_action(3, frequency, Fraction(5, frequency**2), 2),
                30,
            )

    def test_fixed_band_dyson_iterates_have_factorial_depth(self):
        action = Fraction(3, 2)
        for order in range(12):
            self.assertEqual(
                dyson_iterate_bound(order + 1, action)
                / dyson_iterate_bound(order, action),
                action / (order + 1),
            )
            self.assertEqual(
                pressure_depth_bound(order, action),
                dyson_iterate_bound(order + 1, action),
            )

    def test_exact_pressure_tail_majorant_dominates_long_partial_tail(self):
        action = Fraction(3, 2)
        first_order = 8
        majorant = pressure_tail_majorant(first_order, action)
        partial_tail = sum(
            (
                pressure_depth_bound(order, action)
                for order in range(first_order, 80)
            ),
            Fraction(0),
        )
        self.assertGreaterEqual(majorant, partial_tail)
        self.assertLess(
            pressure_tail_majorant(30, action),
            Fraction(1, 10**20),
        )

    def test_logarithmic_depth_beats_every_fixed_polynomial_input_loss(self):
        logs = [
            logarithmic_depth_log_tail(
                log_inverse_h,
                depth_constant=1.0,
                action=6.0,
                input_power=2.0,
            )
            for log_inverse_h in (100, 1000, 10000)
        ]
        self.assertTrue(all(right < left for left, right in zip(
            logs, logs[1:]
        )))
        self.assertLess(logs[-1], -40000)

    def test_integer_frequency_family_has_exact_leray_angles(self):
        for parameter in (3, 4, 10, 100):
            family = alternating_frequency_family(parameter)
            xi_minus = family["xi_minus"]
            xi_plus = family["xi_plus"]
            shift = family["shift"]
            radius = family["radius"]
            cosine = family["cosine"]
            sine = family["sine"]
            self.assertEqual(
                tuple(left + delta for left, delta in zip(xi_minus, shift)),
                xi_plus,
            )
            self.assertEqual(sum(value * value for value in xi_minus), radius**2)
            self.assertEqual(sum(value * value for value in xi_plus), radius**2)
            self.assertEqual(cosine * cosine + sine * sine, 1)
            self.assertGreater(cosine, 0)
            self.assertGreater(sine, 0)

    def test_alternating_linear_leakage_is_exact_and_unbounded(self):
        for parameter in (3, 10, 100, 1000):
            self.assertEqual(
                alternating_linear_leakage(parameter),
                Fraction(parameter**2 - 1, 2 * parameter),
            )
        self.assertGreater(alternating_linear_leakage(1000), 499)

    def test_one_sided_ray_has_finite_linear_angular_budget(self):
        for parameter in (3, 10, 100):
            previous_leakage = 0.0
            for steps in (1, 10, 100, 1000):
                leakage, variation = one_sided_ray_ledgers(parameter, steps)
                self.assertGreaterEqual(leakage, previous_leakage)
                self.assertLessEqual(leakage, variation + 1e-12)
                self.assertLess(variation, math.pi)
                previous_leakage = leakage

    def test_heat_weighted_backtracking_still_has_linear_growth(self):
        previous = Fraction(0)
        for parameter in (10, 100, 1000):
            leakage = heat_weighted_alternating_leakage(parameter)
            self.assertGreater(leakage, previous)
            previous = leakage
        self.assertTrue(
            math.isclose(
                float(heat_weighted_alternating_leakage(1000)) / 1000,
                0.25,
                rel_tol=2e-5,
            )
        )

    def test_backtracking_lives_for_one_parabolic_time(self):
        for parameter in (100, 1000, 10000):
            self.assertTrue(
                math.isclose(
                    effective_parabolic_time(parameter),
                    0.5,
                    rel_tol=2e-3,
                )
            )

    def test_unit_step_backtracking_requires_supercritical_drift(self):
        ratios = [
            required_drift_to_critical_ratio(parameter)
            for parameter in (10, 100, 1000)
        ]
        self.assertTrue(all(right > left for left, right in zip(
            ratios, ratios[1:]
        )))
        self.assertTrue(
            math.isclose(
                float(ratios[-1]) / 1000**2,
                0.125,
                rel_tol=2e-5,
            )
        )
        for parameter in (3, 10, 100, 1000):
            self.assertEqual(
                required_drift_to_critical_ratio(parameter)
                * critical_step_action(parameter),
                1,
            )

    def test_critical_drift_gives_quadratically_small_microstep_action(self):
        for parameter in (100, 1000, 10000):
            self.assertTrue(
                math.isclose(
                    parameter**2 * critical_step_action(parameter),
                    8.0,
                    rel_tol=3e-3,
                )
            )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            band_action(-1, 1, 1)
        with self.assertRaises(ValueError):
            dyson_iterate_bound(-1, 1)
        with self.assertRaises(ValueError):
            dyson_iterate_bound(True, 1)
        with self.assertRaises(ValueError):
            pressure_tail_majorant(0, 2)
        with self.assertRaises(ValueError):
            logarithmic_depth_log_tail(-1, 1, 1, 1)
        with self.assertRaises(ValueError):
            alternating_frequency_family(2)
        with self.assertRaises(ValueError):
            alternating_frequency_family(True)
        with self.assertRaises(ValueError):
            critical_step_action(10, Fraction(-1))


if __name__ == "__main__":
    unittest.main()
