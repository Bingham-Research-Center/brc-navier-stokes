from fractions import Fraction
import unittest

from navier_lab.adjoint_pressure_multistage_path import (
    dyadic_square_product_exponent,
    log_depth_stretched_exponent,
    path_prefactor,
    ratio_product,
    simplex_clock_bound,
    slow_dyadic_clock_ceiling,
)


class AdjointPressureMultistagePathTests(unittest.TestCase):
    def test_successive_frequency_ratios_telescope(self):
        frequencies = (
            Fraction(81, 2),
            Fraction(27, 5),
            Fraction(9, 7),
            Fraction(3, 11),
        )
        self.assertEqual(
            ratio_product(frequencies),
            frequencies[0] / frequencies[-1],
        )

    def test_single_frequency_has_empty_ratio_product(self):
        self.assertEqual(ratio_product((Fraction(7),)), 1)

    def test_path_prefactor_includes_final_observation(self):
        self.assertEqual(
            path_prefactor(
                Fraction(64),
                Fraction(2),
                Fraction(3, 2),
                0,
            ),
            Fraction(3, 64),
        )
        self.assertEqual(
            path_prefactor(
                Fraction(64),
                Fraction(2),
                Fraction(3, 2),
                2,
            ),
            Fraction(27, 256),
        )

    def test_simplex_clock_bound_is_exact_rational_ceiling(self):
        self.assertEqual(
            simplex_clock_bound(
                Fraction(1, 10),
                (Fraction(2), Fraction(3), Fraction(5)),
            ),
            Fraction(1, 200),
        )

    def test_simplex_clock_bound_is_capped_at_one(self):
        self.assertEqual(
            simplex_clock_bound(
                Fraction(2),
                (Fraction(3), Fraction(5)),
            ),
            1,
        )

    def test_dyadic_rate_product_exponent(self):
        self.assertEqual(dyadic_square_product_exponent(0), 0)
        self.assertEqual(dyadic_square_product_exponent(3), -12)
        self.assertEqual(dyadic_square_product_exponent(8), -72)

    def test_slow_dyadic_clock_ceiling(self):
        self.assertEqual(slow_dyadic_clock_ceiling(1), 1)
        self.assertEqual(slow_dyadic_clock_ceiling(2), Fraction(1, 8))
        self.assertEqual(
            slow_dyadic_clock_ceiling(4),
            Fraction(1, 98304),
        )
        self.assertEqual(
            slow_dyadic_clock_ceiling(4),
            simplex_clock_bound(
                Fraction(1),
                (
                    Fraction(1),
                    Fraction(1, 4),
                    Fraction(1, 16),
                    Fraction(1, 64),
                ),
            ),
        )

    def test_fixed_depth_has_no_stretched_exponent_loss(self):
        self.assertEqual(
            log_depth_stretched_exponent(
                Fraction(1, 2),
                Fraction(0),
            ),
            Fraction(9, 4),
        )

    def test_logarithmic_depth_subtracts_explicit_loss(self):
        self.assertEqual(
            log_depth_stretched_exponent(
                Fraction(1, 2),
                Fraction(1, 4),
            ),
            Fraction(2),
        )
        self.assertEqual(
            log_depth_stretched_exponent(
                Fraction(1, 4),
                Fraction(1, 2),
            ),
            Fraction(2),
        )

    def test_interaction_loss_must_leave_constant_term_vanishing(self):
        with self.assertRaises(ValueError):
            log_depth_stretched_exponent(
                Fraction(1, 2),
                Fraction(1, 2),
            )
        with self.assertRaises(ValueError):
            log_depth_stretched_exponent(
                Fraction(1, 4),
                Fraction(3, 4),
            )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            ratio_product(())
        with self.assertRaises(ValueError):
            ratio_product((Fraction(1), Fraction(0)))
        with self.assertRaises(ValueError):
            path_prefactor(
                Fraction(1),
                Fraction(1),
                Fraction(1),
                -1,
            )
        with self.assertRaises(ValueError):
            simplex_clock_bound(Fraction(1), ())
        with self.assertRaises(ValueError):
            dyadic_square_product_exponent(-1)
        with self.assertRaises(ValueError):
            slow_dyadic_clock_ceiling(0)
        with self.assertRaises(ValueError):
            log_depth_stretched_exponent(
                Fraction(1, 2),
                Fraction(-1, 4),
            )


if __name__ == "__main__":
    unittest.main()
