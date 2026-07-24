import math
import unittest

from navier_lab.adjoint_pressure_amplitude_window import (
    active_cell_ceiling,
    balanced_pairing_tail,
    dyadic_window_telescope,
    hard_window_cutoff,
    hard_window_map,
    large_amplitude_window_ceiling,
    modular_domination_ratio,
    optimized_pairing_tail,
    physical_pairing_tail,
    power_balanced_threshold,
    soft_window_magnitude,
    softened_polar_l2_ceiling,
    softened_polar_magnitude,
    window_map,
)


class AdjointPressureAmplitudeWindowTests(unittest.TestCase):
    def test_softened_polar_is_pointwise_dominated_by_modular(self):
        for softening in (1.0, 2.0, 10.0, 1000.0):
            for amplitude in (
                0.0,
                1.0e-9,
                0.1,
                1.0,
                10.0,
                1.0e4,
            ):
                self.assertLessEqual(
                    modular_domination_ratio(amplitude, softening),
                    2.0 + 1.0e-12,
                )

    def test_l2_ceiling_has_inverse_softening_and_regularisation(self):
        first = softened_polar_l2_ceiling(3.0, 0.25, 2.0)
        second = softened_polar_l2_ceiling(3.0, 0.125, 8.0)
        self.assertTrue(math.isclose(first, 12.0))
        self.assertTrue(math.isclose(second, 6.0))

    def test_active_cell_count_has_twenty_one_halves_power(self):
        alpha = 0.2
        softening = 8.0
        theta = 3.0
        for h in (1.0e-2, 1.0e-4, 1.0e-6):
            cells = active_cell_ceiling(
                regularised_mass=1.0,
                regularisation=theta * h**9,
                wavenumber=h**-0.5,
                softening_factor=softening,
                threshold=alpha,
            )
            normalised = (
                cells
                * theta
                * softening
                * alpha**5
                * h ** (21.0 / 2.0)
            )
            self.assertTrue(math.isclose(normalised, 1.0))

    def test_moving_capture_cancels_every_layer_time_power(self):
        theta = 2.0
        softening = 32.0
        alpha = 0.25
        expected = balanced_pairing_tail(
            amplitude_ratio=theta,
            softening_factor=softening,
            threshold=alpha,
        )
        for h in (1.0e-2, 1.0e-4, 1.0e-6):
            actual = physical_pairing_tail(
                layer_time=h,
                regularisation=theta * h**9,
                softening_factor=softening,
                threshold=alpha,
            )
            self.assertTrue(math.isclose(actual, expected))

    def test_power_balancing_gives_inverse_eleventh_tail(self):
        first_l = 7.0
        second_l = first_l * 2.0**11
        self.assertTrue(
            math.isclose(
                power_balanced_threshold(second_l),
                power_balanced_threshold(first_l) / 2.0,
            )
        )
        self.assertTrue(
            math.isclose(
                optimized_pairing_tail(1.0, second_l),
                optimized_pairing_tail(1.0, first_l) / 2.0,
            )
        )

    def test_window_map_matches_difference_of_the_two_polars(self):
        amplitude = (2.0, -3.0, 6.0)
        amplitude_norm = math.sqrt(sum(value * value for value in amplitude))
        polar = tuple(
            value / math.sqrt(1.0 + amplitude_norm**2)
            for value in amplitude
        )
        softening = 5.0
        expected_factor = (
            1.0 / math.sqrt(amplitude_norm**2 + 1.0)
            - 1.0 / math.sqrt(amplitude_norm**2 + softening**2)
        )
        expected = tuple(expected_factor * value for value in amplitude)
        actual = window_map(polar, softening)
        for left, right in zip(actual, expected):
            self.assertTrue(math.isclose(left, right))

    def test_soft_window_vanishes_at_zero_and_infinite_amplitude(self):
        softening = 10.0
        self.assertEqual(soft_window_magnitude(0.0, softening), 0.0)
        self.assertEqual(window_map((0.0, 0.0, 0.0), softening), (0.0,) * 3)
        self.assertEqual(window_map((1.0, 0.0, 0.0), softening), (0.0,) * 3)
        for amplitude in (10.0, 100.0, 1000.0):
            self.assertLessEqual(
                soft_window_magnitude(amplitude, softening),
                large_amplitude_window_ceiling(amplitude, softening)
                + 1.0e-12,
            )

    def test_hard_window_has_compact_relative_amplitude_support(self):
        lower = 0.5
        upper = 8.0
        self.assertEqual(hard_window_cutoff(0.2, lower, upper), 0.0)
        self.assertEqual(hard_window_cutoff(lower, lower, upper), 1.0)
        self.assertEqual(hard_window_cutoff(upper, lower, upper), 1.0)
        self.assertEqual(hard_window_cutoff(20.0, lower, upper), 0.0)
        self.assertEqual(
            hard_window_map((1.0, 0.0, 0.0), 4.0, lower, upper),
            (0.0, 0.0, 0.0),
        )

    def test_dyadic_windows_telescope_without_absolute_loss(self):
        target = softened_polar_magnitude(3.0, 1.0)
        for levels in (0, 1, 4, 20):
            result = dyadic_window_telescope(3.0, levels)
            self.assertTrue(math.isclose(result["total"], target))
            self.assertTrue(
                all(value >= 0.0 for value in result["bands"])
            )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            modular_domination_ratio(-1.0, 2.0)
        with self.assertRaises(ValueError):
            softened_polar_magnitude(1.0, 0.5)
        with self.assertRaises(ValueError):
            active_cell_ceiling(1.0, 1.0, 1.0, 1.0, 0.0)
        with self.assertRaises(ValueError):
            balanced_pairing_tail(0.0, 1.0, 1.0)
        with self.assertRaises(ValueError):
            window_map((2.0, 0.0, 0.0), 2.0)
        with self.assertRaises(ValueError):
            hard_window_cutoff(1.0, 2.0, 1.0)
        with self.assertRaises(ValueError):
            dyadic_window_telescope(1.0, -1)


if __name__ == "__main__":
    unittest.main()
