import math
import unittest

from navier_lab.adjoint_pressure_intermediate_localization import (
    admissible_alpha,
    admissible_interval,
    localization_powers,
    pressure_ceiling,
)


class AdjointPressureIntermediateLocalizationTests(unittest.TestCase):
    def test_sharp_admissible_interval(self):
        lower, upper = admissible_interval()
        self.assertTrue(math.isclose(lower, 1.0 / 30.0))
        self.assertTrue(math.isclose(upper, 3.0))
        self.assertFalse(admissible_alpha(lower))
        self.assertTrue(admissible_alpha(0.1))
        self.assertFalse(admissible_alpha(upper))

    def test_one_tenth_gives_the_displayed_pressure_powers(self):
        powers = localization_powers(0.1)
        self.assertTrue(
            math.isclose(powers["near_local_energy"], 29.0 / 20.0)
        )
        self.assertTrue(
            math.isclose(powers["near_cutoff"], 41.0 / 20.0)
        )
        self.assertTrue(
            math.isclose(powers["first_feedback_tail"], 3.0 / 10.0)
        )
        self.assertTrue(
            math.isclose(powers["second_feedback_tail"], 1.0 / 2.0)
        )
        self.assertTrue(
            math.isclose(powers["source_radius_gap"], 29.0 / 10.0)
        )

    def test_intermediate_ball_is_strictly_inside_source_cutoff(self):
        powers = localization_powers(0.1)
        self.assertGreater(powers["source_radius_gap"], 0.0)

    def test_pressure_ceiling_vanishes_monotonically(self):
        previous = pressure_ceiling(1.0, 0.1)
        for h in (1.0e-2, 1.0e-4, 1.0e-8):
            current = pressure_ceiling(h, 0.1)
            self.assertLess(current, previous)
            previous = current

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            localization_powers(0.0)
        with self.assertRaises(ValueError):
            pressure_ceiling(0.0)
        with self.assertRaises(ValueError):
            pressure_ceiling(0.1, alpha=0.01)


if __name__ == "__main__":
    unittest.main()
