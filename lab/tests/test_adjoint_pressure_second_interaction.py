import math
import unittest

from navier_lab.adjoint_pressure_second_interaction import (
    admissible_alpha,
    exterior_shell_powers,
    first_interaction_tail_powers,
    intermediate_pressure_powers,
    pressure_ceiling,
)


class AdjointPressureSecondInteractionTests(unittest.TestCase):
    def test_squared_tail_powers_are_exact(self):
        powers = first_interaction_tail_powers()
        self.assertEqual(powers["inner_source"], (9.0 / 2.0, 5.0))
        self.assertEqual(powers["first_q_tail"], (4.0, 7.0))
        self.assertEqual(powers["second_q_tail"], (5.0 / 2.0, 15.0))

    def test_one_tenth_gives_all_displayed_intermediate_powers(self):
        powers = intermediate_pressure_powers(0.1)
        expected = {
            "near_local_energy": 29.0 / 20.0,
            "near_cutoff": 41.0 / 20.0,
            "far_inner_source": 1.0,
            "far_first_q_tail": 17.0 / 20.0,
            "far_second_q_tail": 1.0 / 2.0,
            "source_radius_gap": 29.0 / 10.0,
        }
        for key, value in expected.items():
            self.assertTrue(math.isclose(powers[key], value))

    def test_admissible_interval_retains_one_thirtieth_to_three(self):
        self.assertFalse(admissible_alpha(1.0 / 30.0))
        self.assertTrue(admissible_alpha(0.1))
        self.assertFalse(admissible_alpha(3.0))

    def test_exterior_shell_sum_has_large_positive_powers(self):
        powers = exterior_shell_powers()
        self.assertTrue(math.isclose(powers["inner_source"], 33.0 / 4.0))
        self.assertTrue(math.isclose(powers["first_q_tail"], 11.0))
        self.assertTrue(math.isclose(powers["second_q_tail"], 89.0 / 4.0))

    def test_pressure_ceiling_vanishes(self):
        previous = pressure_ceiling(1.0)
        for h in (1.0e-2, 1.0e-4, 1.0e-8):
            current = pressure_ceiling(h)
            self.assertLess(current, previous)
            previous = current

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            intermediate_pressure_powers(0.0)
        with self.assertRaises(ValueError):
            exterior_shell_powers(0.0)
        with self.assertRaises(ValueError):
            pressure_ceiling(0.0)
        with self.assertRaises(ValueError):
            pressure_ceiling(0.5, alpha=0.01)


if __name__ == "__main__":
    unittest.main()
