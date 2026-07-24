import unittest
from fractions import Fraction

from navier_lab.adjoint_pressure_critical_volterra import (
    barker_constructed_delta,
    barker_oseen_time_margin,
    barker_serrin_excess,
    cumulative_variable_space_margin,
    gradient_time_exponent,
    hardy_iterate_value,
    hardy_step_ratio,
    interpolated_serrin_index,
    oseen_kernel_exponent,
    oseen_time_margin,
    packet_gradient_radius_power,
    serrin_index,
    sobolev_space_exponent,
    telescoped_variable_space_margin,
)


class AdjointPressureCriticalVolterraTests(unittest.TestCase):
    def test_half_integrability_is_the_exact_threshold(self):
        delta = Fraction(1, 2)
        self.assertEqual(gradient_time_exponent(delta), Fraction(5, 2))
        self.assertEqual(sobolev_space_exponent(delta), Fraction(15))
        self.assertEqual(serrin_index(delta), Fraction(1))
        self.assertEqual(oseen_kernel_exponent(delta), Fraction(3, 5))
        self.assertEqual(oseen_time_margin(delta), Fraction(0))
        self.assertEqual(packet_gradient_radius_power(delta), Fraction(0))

    def test_energy_and_subcritical_examples_have_exact_indices(self):
        self.assertEqual(gradient_time_exponent(0), Fraction(2))
        self.assertEqual(sobolev_space_exponent(0), Fraction(6))
        self.assertEqual(serrin_index(0), Fraction(3, 2))
        self.assertEqual(oseen_kernel_exponent(0), Fraction(3, 4))
        self.assertEqual(oseen_time_margin(0), Fraction(-1, 4))
        self.assertEqual(packet_gradient_radius_power(0), Fraction(1))

        delta = Fraction(3, 4)
        self.assertEqual(sobolev_space_exponent(delta), Fraction(33))
        self.assertEqual(serrin_index(delta), Fraction(9, 11))
        self.assertEqual(oseen_time_margin(delta), Fraction(1, 11))
        self.assertEqual(packet_gradient_radius_power(delta), Fraction(-1, 2))

    def test_barker_constructed_exponent_is_strictly_below_half(self):
        for bound, constant in ((1, 1), (10, 3), (100, 7)):
            delta = barker_constructed_delta(bound, constant)
            self.assertGreater(delta, 0)
            self.assertLess(delta, Fraction(1, 2))
            self.assertEqual(
                serrin_index(delta) - 1,
                barker_serrin_excess(bound, constant),
            )
            self.assertEqual(
                oseen_time_margin(delta),
                barker_oseen_time_margin(bound, constant),
            )
            self.assertLess(barker_oseen_time_margin(bound, constant), 0)

    def test_weak_l3_interpolation_never_crosses_the_serrin_line(self):
        delta = Fraction(3, 46)
        for mixing in (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(1)):
            index = interpolated_serrin_index(delta, mixing)
            self.assertGreaterEqual(index, 1)
            if mixing > 0:
                self.assertGreater(index, 1)

    def test_variable_lebesgue_staircase_telescopes_exactly(self):
        inverse_exponents = [
            Fraction(1, 3),
            Fraction(1, 4),
            Fraction(1, 2),
            Fraction(1, 5),
            Fraction(1, 6),
        ]
        for delta in (Fraction(0), Fraction(1, 3), Fraction(3, 4)):
            self.assertEqual(
                cumulative_variable_space_margin(delta, inverse_exponents),
                telescoped_variable_space_margin(delta, inverse_exponents),
            )

    def test_supercritical_staircase_has_negative_linear_drift(self):
        delta = Fraction(1, 3)
        for steps in (4, 20, 100):
            inverse_exponents = [Fraction(1, 3)] * (steps + 1)
            total = cumulative_variable_space_margin(delta, inverse_exponents)
            self.assertEqual(total, steps * oseen_time_margin(delta))
            self.assertLess(total, 0)

    def test_critical_hardy_operator_keeps_constant_at_every_depth(self):
        for gamma in (0.1, 0.4, 0.8):
            for order in (0, 1, 2, 10, 100):
                self.assertEqual(
                    hardy_iterate_value(gamma, 0.0, order),
                    1.0,
                )

    def test_positive_hardy_gain_forces_step_ratios_to_zero(self):
        gamma = 0.4
        epsilon = 0.1
        ratios = [
            hardy_step_ratio(gamma, epsilon, order)
            for order in (1, 2, 4, 8, 16, 32, 64)
        ]
        for previous, current in zip(ratios, ratios[1:]):
            self.assertGreater(previous, current)
        self.assertLess(ratios[-1], ratios[0])
        values = [
            hardy_iterate_value(gamma, epsilon, order)
            for order in (1, 4, 16, 64)
        ]
        for previous, current in zip(values, values[1:]):
            self.assertGreater(previous, current)

    def test_invalid_inputs_are_rejected(self):
        for delta in (Fraction(-1, 10), Fraction(1), True, 0.1):
            with self.assertRaises(ValueError):
                serrin_index(delta)
        with self.assertRaises(ValueError):
            barker_constructed_delta(0, 1)
        with self.assertRaises(ValueError):
            interpolated_serrin_index(Fraction(1, 4), Fraction(2))
        with self.assertRaises(ValueError):
            cumulative_variable_space_margin(Fraction(1, 4), [Fraction(1, 3)])
        with self.assertRaises(ValueError):
            hardy_iterate_value(0.0, 0.1, 1)
        with self.assertRaises(ValueError):
            hardy_iterate_value(0.4, -0.1, 1)
        with self.assertRaises(ValueError):
            hardy_step_ratio(0.4, 0.1, 0)


if __name__ == "__main__":
    unittest.main()
