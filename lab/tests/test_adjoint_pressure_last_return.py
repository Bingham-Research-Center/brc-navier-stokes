from fractions import Fraction
import unittest

from navier_lab.adjoint_pressure_last_return import (
    full_resolvent,
    full_word_weight,
    high_output_tail_inverse_square_sum,
    last_return_resolvent,
    last_return_word_weight,
    no_return_resolvent,
    no_return_word_weight,
    operator_words_by_leftmost_return,
    parabolic_stretched_exponent,
    separated_output_heat_rate_sum,
)


class AdjointPressureLastReturnTests(unittest.TestCase):
    def test_words_partition_by_absence_or_last_return(self):
        a = Fraction(2, 5)
        b = Fraction(1, 7)
        for depth in range(12):
            self.assertEqual(
                full_word_weight(a, b, depth),
                no_return_word_weight(a, depth)
                + last_return_word_weight(a, b, depth),
            )

    def test_depth_zero_has_no_return_event(self):
        self.assertEqual(
            last_return_word_weight(Fraction(1), Fraction(1), 0),
            0,
        )

    def test_last_return_position_sum_has_correct_orientation(self):
        a = Fraction(1, 2)
        b = Fraction(1, 3)
        self.assertEqual(
            last_return_word_weight(a, b, 2),
            b * (a + b) + a * b,
        )

    def test_noncommutative_words_group_by_leftmost_b(self):
        for depth in range(8):
            no_return, groups = operator_words_by_leftmost_return(depth)
            grouped = {no_return}
            for index, group in enumerate(groups):
                self.assertTrue(group)
                self.assertTrue(
                    all(word.find("B") == index for word in group)
                )
                self.assertTrue(grouped.isdisjoint(group))
                grouped.update(group)
            self.assertEqual(len(grouped), 2**depth)

    def test_resolvent_renewal_identity_is_exact(self):
        source = Fraction(3, 8)
        a = Fraction(1, 5)
        b = Fraction(1, 4)
        self.assertEqual(
            full_resolvent(source, a, b),
            no_return_resolvent(source, a)
            + last_return_resolvent(source, a, b),
        )

    def test_six_step_downcross_heat_entropy_is_tiny(self):
        self.assertEqual(
            separated_output_heat_rate_sum(Fraction(1), 6),
            Fraction(1, 3072),
        )

    def test_separation_entropy_has_quadratic_scale_power(self):
        for steps in range(1, 9):
            current = separated_output_heat_rate_sum(
                Fraction(1),
                steps,
            )
            following = separated_output_heat_rate_sum(
                Fraction(1),
                steps + 1,
            )
            self.assertEqual(following / current, Fraction(1, 4))

    def test_high_output_operator_tail_is_inverse_linear(self):
        self.assertEqual(
            high_output_tail_inverse_square_sum(Fraction(1)),
            Fraction(1, 3),
        )
        for scale_steps in range(6):
            base = Fraction(1, 4**scale_steps)
            following = base / 4
            self.assertEqual(
                high_output_tail_inverse_square_sum(following)
                / high_output_tail_inverse_square_sum(base),
                Fraction(1, 4),
            )

    def test_parabolic_cost_is_nine_quarters(self):
        self.assertEqual(
            parabolic_stretched_exponent(),
            Fraction(9, 4),
        )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            full_word_weight(Fraction(-1), Fraction(1), 1)
        with self.assertRaises(ValueError):
            no_return_word_weight(Fraction(1), -1)
        with self.assertRaises(ValueError):
            last_return_word_weight(Fraction(1), Fraction(1), -1)
        with self.assertRaises(ValueError):
            full_resolvent(
                Fraction(1),
                Fraction(1, 2),
                Fraction(1, 2),
            )
        with self.assertRaises(ValueError):
            no_return_resolvent(Fraction(1), Fraction(1))
        with self.assertRaises(ValueError):
            separated_output_heat_rate_sum(Fraction(0), 6)
        with self.assertRaises(ValueError):
            separated_output_heat_rate_sum(Fraction(1), 0)
        with self.assertRaises(ValueError):
            high_output_tail_inverse_square_sum(Fraction(0))
        with self.assertRaises(ValueError):
            operator_words_by_leftmost_return(-1)


if __name__ == "__main__":
    unittest.main()
