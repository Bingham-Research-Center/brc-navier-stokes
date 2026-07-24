import unittest
from fractions import Fraction

from navier_lab.adjoint_pressure_skew_compression import (
    compression_identity,
    critical_depth_state,
    feedback_residual_pressure,
    feedback_right_side,
    feedback_solution,
    matrix_product,
    norm_squared,
    pressure_depth_value,
    rational_rotation,
    real_coupling_norm_squared,
    real_coupling_solution,
    skew_generator,
    strong_trace_feedback_right_side,
    strong_trace_feedback_solution,
    strong_trace_hardy_factor,
    strong_trace_residual_pressure,
    strong_trace_skew_generator,
    transpose,
    unitary_leakage_ledgers,
    unitary_telescoped_squared_leakage,
)


class AdjointPressureSkewCompressionTests(unittest.TestCase):
    def test_full_generator_is_exactly_skew(self):
        generator = skew_generator()
        negative_generator = tuple(
            tuple(-value for value in row)
            for row in generator
        )
        self.assertEqual(transpose(generator), negative_generator)

    def test_skew_compression_has_exact_pressure_defect(self):
        for vector in ((1, 0), (0, 1), (1, 1), (2, -3)):
            full_side, split_side = compression_identity(vector)
            self.assertEqual(full_side, split_side)

    def test_critical_compression_rotates_without_depth_decay(self):
        expected = ((1, 0), (0, 1), (-1, 0), (0, -1))
        for order in range(16):
            self.assertEqual(
                critical_depth_state(order),
                tuple(Fraction(value) for value in expected[order % 4]),
            )
            self.assertEqual(abs(pressure_depth_value(order)), 1)

    def test_feedback_solution_and_every_residual_pressure_are_exact(self):
        self.assertEqual(feedback_right_side(), feedback_solution())
        for order in range(100):
            self.assertEqual(abs(feedback_residual_pressure(order)), 1)

    def test_linear_time_mode_has_strong_zero_trace_and_no_depth_decay(self):
        generator = strong_trace_skew_generator()
        negative_generator = tuple(
            tuple(-value for value in row)
            for row in generator
        )
        self.assertEqual(transpose(generator), negative_generator)
        self.assertEqual(strong_trace_hardy_factor(), Fraction(1, 2))
        self.assertEqual(strong_trace_feedback_solution(0), (0, 0))
        for time in (Fraction(0), Fraction(1, 10), Fraction(1), Fraction(7, 3)):
            self.assertEqual(
                strong_trace_feedback_right_side(time),
                strong_trace_feedback_solution(time),
            )
            for order in range(20):
                self.assertEqual(
                    abs(strong_trace_residual_pressure(order, time)),
                    time,
                )

    def test_real_coupling_is_energy_stable_despite_persistent_coefficients(self):
        for coupling in (
            Fraction(-10),
            Fraction(-1),
            Fraction(0),
            Fraction(1),
            Fraction(10),
        ):
            solution = real_coupling_solution(coupling)
            self.assertEqual(
                norm_squared(solution),
                real_coupling_norm_squared(coupling),
            )
            self.assertLessEqual(norm_squared(solution), Fraction(2))
        self.assertEqual(real_coupling_solution(1), feedback_solution())

    def test_rational_rotation_is_exactly_unitary(self):
        for n_value in (1, 2, 10, 100):
            cosine, sine = rational_rotation(n_value)
            rotation = (
                (cosine, -sine),
                (sine, cosine),
            )
            self.assertEqual(
                matrix_product(transpose(rotation), rotation),
                (
                    (Fraction(1), Fraction(0)),
                    (Fraction(0), Fraction(1)),
                ),
            )

    def test_squared_leakage_telescopes_but_linear_leakage_survives(self):
        previous_linear = Fraction(0)
        for n_value in (10, 100, 1000):
            linear, squared = unitary_leakage_ledgers(n_value)
            self.assertEqual(
                squared,
                unitary_telescoped_squared_leakage(n_value),
            )
            self.assertGreater(linear, previous_linear)
            self.assertLess(linear, Fraction(2))
            previous_linear = linear
        linear, squared = unitary_leakage_ledgers(1000)
        self.assertGreater(linear, Fraction(199, 100))
        self.assertLess(squared, Fraction(1, 200))

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            critical_depth_state(-1)
        with self.assertRaises(ValueError):
            critical_depth_state(1, (1, 2, 3))
        with self.assertRaises(ValueError):
            rational_rotation(0)
        with self.assertRaises(ValueError):
            rational_rotation(True)
        with self.assertRaises(ValueError):
            unitary_leakage_ledgers(10, -1)
        with self.assertRaises(ValueError):
            real_coupling_solution(0.5)
        with self.assertRaises(ValueError):
            strong_trace_feedback_solution(Fraction(-1))


if __name__ == "__main__":
    unittest.main()
