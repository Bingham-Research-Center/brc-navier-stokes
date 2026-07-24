import math
import unittest

from navier_lab.adjoint_pressure_balanced_polar import (
    bad_cell_ceiling,
    balanced_action_tail,
    balanced_scales,
    captured_bad_mass,
    curvature_to_kato_ratio,
    hessian_quadratic,
    polar_time_derivative_budget,
    third_derivative_contraction,
    trace_defect_ledger,
)


class AdjointPressureBalancedPolarTests(unittest.TestCase):
    def test_all_balanced_cell_scales_have_twenty_one_halves_power(self):
        h = 1.0e-4
        scales = balanced_scales(h)
        self.assertTrue(
            math.isclose(scales["source_cells"], h ** (-21.0 / 2.0))
        )
        for key in (
            "kato_cell_scale",
            "pressure_cell_scale",
            "orlicz_cell_scale",
        ):
            self.assertTrue(
                math.isclose(scales[key], h ** (21.0 / 2.0))
            )

    def test_bad_cell_count_exactly_cancels_capture_power(self):
        for h in (1.0e-2, 1.0e-4, 1.0e-6):
            scales = balanced_scales(h)
            cells = bad_cell_ceiling(
                total_budget=1.0,
                rooted_threshold=64.0,
                cell_scale=scales["kato_cell_scale"],
            )
            self.assertTrue(
                math.isclose(
                    captured_bad_mass(h, cells),
                    64.0 ** (-1.0 / 6.0),
                )
            )

    def test_each_local_action_has_the_same_scale_free_tail(self):
        h = 1.0e-5
        for action in ("kato", "pressure", "orlicz"):
            first = balanced_action_tail(h, 1.0, action)
            second = balanced_action_tail(h, 2.0**6, action)
            self.assertTrue(math.isclose(second, first / 2.0))

    def test_amplitude_ratio_enters_with_inverse_sixth_power(self):
        h = 1.0e-5
        first = balanced_action_tail(
            h,
            rooted_threshold=1.0,
            action="kato",
            amplitude_ratio=1.0,
        )
        second = balanced_action_tail(
            h,
            rooted_threshold=1.0,
            action="kato",
            amplitude_ratio=2.0**6,
        )
        self.assertTrue(math.isclose(second, first / 2.0))

    def test_hessian_and_third_derivative_formulas_on_axes(self):
        self.assertTrue(
            math.isclose(
                hessian_quadratic((3.0, 0.0, 0.0), (1.0, 0.0, 0.0)),
                10.0 ** (-1.5),
            )
        )
        self.assertTrue(
            math.isclose(
                hessian_quadratic((3.0, 0.0, 0.0), (0.0, 1.0, 0.0)),
                10.0 ** (-0.5),
            )
        )
        third = third_derivative_contraction(
            (3.0, 0.0, 0.0),
            (1.0, 0.0, 0.0),
        )
        self.assertTrue(math.isclose(third[0], -9.0 / 10.0**2.5))
        self.assertTrue(math.isclose(third[1], 0.0))
        self.assertTrue(math.isclose(third[2], 0.0))

    def test_curvature_is_pointwise_controlled_by_kato_density(self):
        amplitudes = (
            (0.0, 0.0, 0.0),
            (0.1, -0.2, 0.3),
            (3.0, 0.0, 0.0),
            (100.0, -40.0, 2.0),
        )
        directions = (
            (1.0, 0.0, 0.0),
            (0.0, 1.0, 0.0),
            (1.0, -2.0, 3.0),
            (-4.0, 0.5, 2.0),
        )
        for amplitude in amplitudes:
            for direction in directions:
                self.assertLessEqual(
                    curvature_to_kato_ratio(amplitude, direction),
                    4.0 + 1.0e-12,
                )

    def test_time_derivative_budget_uses_sqrt_and_linear_actions(self):
        value = polar_time_derivative_budget(
            kato_action=4.0,
            pressure_action=3.0,
            drift_ceiling=5.0,
        )
        self.assertTrue(math.isclose(value, 19.0))

    def test_trace_model_is_compact_in_l2_but_keeps_pairing(self):
        first = trace_defect_ledger(100.0)
        second = trace_defect_ledger(10000.0)
        self.assertTrue(
            math.isclose(
                second["profile_l2_squared"],
                first["profile_l2_squared"] / 100.0,
            )
        )
        self.assertTrue(
            math.isclose(
                second["profile_variation"],
                first["profile_variation"],
            )
        )
        self.assertTrue(
            math.isclose(
                second["self_weighted_pairing"],
                first["self_weighted_pairing"],
            )
        )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            balanced_scales(0.0)
        with self.assertRaises(ValueError):
            bad_cell_ceiling(1.0, 0.0, 1.0)
        with self.assertRaises(ValueError):
            captured_bad_mass(1.0, -1.0)
        with self.assertRaises(ValueError):
            balanced_action_tail(1.0, 1.0, "unknown")
        with self.assertRaises(ValueError):
            hessian_quadratic((1.0, 2.0), (1.0, 2.0, 3.0))
        with self.assertRaises(ValueError):
            polar_time_derivative_budget(1.0, 1.0, 0.0)
        with self.assertRaises(ValueError):
            trace_defect_ledger(0.0)


if __name__ == "__main__":
    unittest.main()
