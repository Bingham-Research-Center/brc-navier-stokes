import unittest
from fractions import Fraction

from navier_lab.adjoint_pressure_interaction_depth import (
    exterior_shell_powers,
    fixed_order_pressure_ceiling,
    inner_tail_time_exponent,
    intermediate_pressure_powers,
    l1_exponent,
    logarithmic_depth,
    logarithmic_partial_sum_envelope,
    lorentz_exponent,
    recurrence_residual,
    uniform_pressure_power,
)


class AdjointPressureInteractionDepthTests(unittest.TestCase):
    def test_l1_recurrence_and_closed_form_are_exact(self):
        self.assertEqual(l1_exponent(0), Fraction(1, 4))
        for order in range(1, 12):
            self.assertEqual(recurrence_residual(order), 0)
        self.assertEqual(l1_exponent(1), Fraction(5, 4))
        self.assertLess(l1_exponent(20), Fraction(7, 4))

    def test_lorentz_closed_form_is_exact(self):
        self.assertEqual(lorentz_exponent(0), Fraction(3, 4))
        self.assertEqual(lorentz_exponent(1), Fraction(13, 12))
        self.assertLess(lorentz_exponent(20), Fraction(5, 4))

    def test_inner_tail_power_improves_monotonically(self):
        self.assertEqual(inner_tail_time_exponent(1), Fraction(9, 2))
        previous = inner_tail_time_exponent(1)
        for order in range(2, 12):
            current = inner_tail_time_exponent(order)
            self.assertGreater(current, previous)
            self.assertLess(current, Fraction(11, 2))
            previous = current

    def test_one_tenth_pressure_powers_have_first_order_minimum(self):
        first = intermediate_pressure_powers(1)
        self.assertEqual(
            first,
            {
                "near_local_energy": Fraction(29, 20),
                "near_cutoff": Fraction(41, 20),
                "far_inner_source": Fraction(1, 1),
                "far_stable_first": Fraction(17, 20),
                "far_stable_second": Fraction(1, 2),
                "source_radius_gap": Fraction(29, 10),
            },
        )
        for order in range(2, 12):
            powers = intermediate_pressure_powers(order)
            self.assertGreater(powers["far_inner_source"], first["far_inner_source"])
            for key, value in powers.items():
                self.assertGreater(value, 0, key)

    def test_exterior_shell_powers_have_first_order_minimum(self):
        first = exterior_shell_powers(1)
        self.assertEqual(first["inner_source"], Fraction(33, 4))
        self.assertEqual(first["stable_first"], Fraction(11, 1))
        self.assertEqual(first["stable_second"], Fraction(89, 4))
        for order in range(2, 12):
            self.assertGreater(
                exterior_shell_powers(order)["inner_source"],
                first["inner_source"],
            )

    def test_each_fixed_order_ceiling_vanishes(self):
        for order in (1, 2, 5, 20):
            previous = fixed_order_pressure_ceiling(1.0, order)
            for h in (1.0e-2, 1.0e-4, 1.0e-8):
                current = fixed_order_pressure_ceiling(h, order)
                self.assertLess(current, previous)
                previous = current

    def test_logarithmic_depth_respects_both_growth_ledgers(self):
        growth_base = 8.0
        alpha = Fraction(1, 4)
        pressure_power = Fraction(11, 8)
        for h in (1.0e-40, 1.0e-80, 1.0e-160):
            depth = logarithmic_depth(h, growth_base, alpha)
            self.assertGreater(depth, 0)
            self.assertLessEqual(
                growth_base**depth,
                h ** (-float(pressure_power) / 4.0),
            )
            self.assertLessEqual(4.0**depth, h ** (-float(alpha) / 2.0))

    def test_one_quarter_optimises_the_uniform_pressure_power(self):
        optimum = uniform_pressure_power(Fraction(1, 4))
        self.assertEqual(optimum, Fraction(11, 8))
        for alpha in (
            Fraction(1, 20),
            Fraction(3, 16),
            Fraction(1, 5),
            Fraction(3, 10),
            Fraction(1, 2),
            Fraction(2, 1),
        ):
            self.assertLess(uniform_pressure_power(alpha), optimum)

    def test_logarithmic_partial_sum_envelope_vanishes(self):
        growth_base = 8.0
        hs = (1.0e-40, 1.0e-80, 1.0e-160)
        values = [
            logarithmic_partial_sum_envelope(h, growth_base) for h in hs
        ]
        self.assertGreater(values[0], values[1])
        self.assertGreater(values[1], values[2])
        for h, value in zip(hs, values):
            self.assertLessEqual(
                value,
                growth_base / (growth_base - 1.0) * h ** (33.0 / 32.0),
            )

    def test_invalid_inputs_are_rejected(self):
        for order in (-1, True, 1.5):
            with self.assertRaises(ValueError):
                l1_exponent(order)
        with self.assertRaises(ValueError):
            inner_tail_time_exponent(0)
        with self.assertRaises(ValueError):
            intermediate_pressure_powers(1, Fraction(0, 1))
        with self.assertRaises(ValueError):
            fixed_order_pressure_ceiling(0.0, 1)
        with self.assertRaises(ValueError):
            fixed_order_pressure_ceiling(0.5, 1, Fraction(1, 100))
        with self.assertRaises(ValueError):
            fixed_order_pressure_ceiling(0.5, 1, Fraction(3, 1))
        with self.assertRaises(ValueError):
            logarithmic_depth(1.0, 8.0)
        with self.assertRaises(ValueError):
            logarithmic_depth(0.5, 1.5)
        with self.assertRaises(ValueError):
            logarithmic_depth(0.5, float("inf"))
        with self.assertRaises(ValueError):
            logarithmic_depth(0.5, 8.0, Fraction(0, 1))
        with self.assertRaises(ValueError):
            uniform_pressure_power(Fraction(1, 30))
        with self.assertRaises(ValueError):
            uniform_pressure_power(Fraction(3, 1))


if __name__ == "__main__":
    unittest.main()
