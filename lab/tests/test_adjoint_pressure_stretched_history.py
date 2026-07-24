import math
import unittest

from navier_lab.adjoint_pressure_stretched_history import (
    P,
    integrated_history,
    log_ledger,
    physical_nodes,
    piecewise_history_segments,
)


class AdjointPressureStretchedHistoryTests(unittest.TestCase):
    def test_forced_stretched_exponential_floor_is_exact(self):
        h = 0.4
        c = 0.7
        ledger = log_ledger(h, c, acceleration=2.5)
        depth = c * h ** (-P)
        self.assertTrue(
            math.isclose(
                ledger["forced_dissipation"] + 3.0 * math.log(h),
                depth,
            )
        )

    def test_scale_ratios_and_logarithmic_depth_are_exact(self):
        h = 0.5
        ledger = log_ledger(h, c=0.3, acceleration=2.0)
        self.assertTrue(
            math.isclose(
                ledger["zoom"] - ledger["interaction_scale"],
                3.0 * math.log(h),
            )
        )
        self.assertTrue(
            math.isclose(
                ledger["interaction_scale"]
                - ledger["dissipation_scale"],
                -ledger["logarithmic_depth"],
            )
        )

    def test_both_physical_clocks_are_exact(self):
        h = 0.6
        ledger = log_ledger(h, c=0.4, acceleration=3.0)
        self.assertTrue(
            math.isclose(
                ledger["physical_time"]
                - 2.0 * ledger["interaction_scale"],
                ledger["interaction_clock"],
            )
        )
        self.assertTrue(
            math.isclose(
                ledger["physical_time"]
                - 2.0 * ledger["dissipation_scale"],
                ledger["dissipation_clock"],
            )
        )

    def test_zoom_outruns_reciprocal_stretched_exponential(self):
        c = 0.5
        acceleration = 2.25
        gaps = []
        for h in (0.8, 0.6, 0.4, 0.3):
            ledger = log_ledger(h, c, acceleration)
            reciprocal_floor = (
                3.0 * math.log(h) - c * h ** (-P)
            )
            gaps.append(ledger["zoom"] - reciprocal_floor)
        self.assertTrue(all(gap < 0.0 for gap in gaps))
        self.assertTrue(
            all(gaps[index + 1] < gaps[index] for index in range(len(gaps) - 1))
        )

    def test_one_positive_history_recovers_every_nested_mass(self):
        h_values = [0.8, 0.7, 0.6, 0.5]
        nodes = physical_nodes(h_values, c=0.2, acceleration=2.0)
        segments = piecewise_history_segments(
            h_values,
            c=0.2,
            acceleration=2.0,
        )
        self.assertTrue(all(slope > 0.0 for _, _, slope in segments))
        for delta, rho in nodes:
            self.assertTrue(
                math.isclose(
                    integrated_history(delta, segments),
                    rho,
                    rel_tol=1.0e-12,
                    abs_tol=1.0e-15,
                )
            )
        self.assertTrue(
            math.isclose(
                sum((right - left) * slope for left, right, slope in segments),
                nodes[0][1],
            )
        )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            log_ledger(0.0)
        with self.assertRaises(ValueError):
            log_ledger(0.5, c=0.0)
        with self.assertRaises(ValueError):
            log_ledger(0.5, acceleration=1.0)
        with self.assertRaises(ValueError):
            physical_nodes([])
        with self.assertRaises(ValueError):
            physical_nodes([0.4, 0.5])
        with self.assertRaises(ValueError):
            integrated_history(-1.0, [])


if __name__ == "__main__":
    unittest.main()
