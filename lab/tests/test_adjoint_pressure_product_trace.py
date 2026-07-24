import math
import unittest

from navier_lab.adjoint_pressure_product_trace import (
    density_modulus_exponent,
    graph_neighbourhood_pressure_ceiling,
    lorentz_density_exponent,
    product_base_mass,
    trace_approximation_error_bound,
    uniform_root_scales,
)


class AdjointPressureProductTraceTests(unittest.TestCase):
    def test_uniform_root_action_means_are_scale_free(self):
        for h in (1.0e-2, 1.0e-4, 1.0e-6):
            scales = uniform_root_scales(h)
            self.assertTrue(
                math.isclose(scales["orlicz_mean_factor"], 1.0)
            )
            self.assertTrue(
                math.isclose(scales["kato_mean_factor"], 1.0)
            )
            self.assertTrue(
                math.isclose(scales["pressure_mean_factor"], 1.0)
            )

    def test_one_sixth_capture_gives_one_seventh_modulus(self):
        alpha = density_modulus_exponent(1.0 / 6.0)
        self.assertTrue(math.isclose(alpha, 1.0 / 7.0))

    def test_one_seventh_modulus_gives_weak_seven_sixths_density(self):
        exponent = lorentz_density_exponent(1.0 / 7.0)
        self.assertTrue(math.isclose(exponent, 7.0 / 6.0))

    def test_uniform_time_and_profile_roots_form_a_product(self):
        self.assertTrue(
            math.isclose(
                product_base_mass(0.2, 0.35),
                0.07,
            )
        )

    def test_graph_neighbourhood_pressure_vanishes(self):
        previous = 1.0
        for width in (1.0e-7, 1.0e-14, 1.0e-28):
            ceiling = graph_neighbourhood_pressure_ceiling(width)
            self.assertTrue(
                math.isclose(ceiling, width ** (1.0 / 7.0))
            )
            self.assertLess(ceiling, previous)
            previous = ceiling

    def test_temporal_mollification_error_split_can_vanish(self):
        previous = 1.0
        for delta in (1.0e-2, 1.0e-4, 1.0e-6):
            bound = trace_approximation_error_bound(
                l2_error_squared=delta**9,
                split_threshold=delta,
                observable_ceiling=1.0,
            )
            self.assertTrue(math.isclose(bound, 3.0 * delta))
            self.assertLess(bound, previous)
            previous = bound

    def test_nonunit_amplitude_and_wavenumber_factors_are_explicit(self):
        scales = uniform_root_scales(
            1.0e-4,
            amplitude_ratio=2.0,
            wavenumber_factor=3.0,
        )
        self.assertTrue(
            math.isclose(scales["orlicz_mean_factor"], 0.5)
        )
        self.assertTrue(
            math.isclose(scales["pressure_mean_factor"], 0.5)
        )
        self.assertTrue(
            math.isclose(
                scales["kato_mean_factor"],
                1.0 / 18.0,
            )
        )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            uniform_root_scales(0.0)
        with self.assertRaises(ValueError):
            density_modulus_exponent(0.0)
        with self.assertRaises(ValueError):
            lorentz_density_exponent(1.0)
        with self.assertRaises(ValueError):
            product_base_mass(1.1, 0.5)
        with self.assertRaises(ValueError):
            graph_neighbourhood_pressure_ceiling(2.0)
        with self.assertRaises(ValueError):
            trace_approximation_error_bound(
                1.0,
                0.0,
                1.0,
            )


if __name__ == "__main__":
    unittest.main()
