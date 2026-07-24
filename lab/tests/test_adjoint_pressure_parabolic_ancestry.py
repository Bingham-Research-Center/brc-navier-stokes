import math
import unittest

from navier_lab.adjoint_pressure_parabolic_ancestry import (
    SEVEN_SIXTHS,
    ancestry_node,
    ancestry_residual,
    ancestry_sequence,
    cutoff_residual,
    distortion_mass,
    log_scale_ratio,
    minimum_carrier_frequency,
    next_h,
    tail_increments,
)


class AdjointPressureParabolicAncestryTests(unittest.TestCase):
    def test_next_node_matches_cutoff_and_next_event_exactly(self):
        nodes = ancestry_sequence(1.0e-3, 6, q=4.0, kappa=1.25)
        for current, following in zip(nodes, nodes[1:]):
            self.assertAlmostEqual(
                ancestry_residual(current, following),
                0.0,
                places=12,
            )
            self.assertAlmostEqual(
                cutoff_residual(current, following),
                0.0,
                places=12,
            )
            self.assertAlmostEqual(
                current.physical_cutoff,
                1.0 / following.sigma,
                delta=1.0e-12 * current.physical_cutoff,
            )

    def test_inverse_cubic_physical_tail_vanishes_for_q_above_three(self):
        nodes = ancestry_sequence(1.0e-2, 7, q=3.25)
        tails = [node.physical_tail_mass for node in nodes]
        self.assertTrue(
            all(
                tails[index + 1] < tails[index]
                for index in range(len(tails) - 1)
            )
        )
        self.assertLess(tails[-1], tails[0] * 0.25)

    def test_distortion_mass_is_kappa_six_times_tail_mass(self):
        nodes = ancestry_sequence(1.0e-3, 5, q=4.0, kappa=1.7)
        for current, following in zip(nodes, nodes[1:]):
            expected = current.kappa**6 * current.physical_tail_mass
            self.assertAlmostEqual(
                distortion_mass(current, following),
                expected,
                delta=1.0e-12 * expected,
            )

    def test_log_scale_ratio_stays_below_seven_sixths(self):
        nodes = ancestry_sequence(1.0e-4, 5, q=3.1, kappa=1.0)
        expected = 1.0 + 1.0 / (2.0 * 3.1)
        for current, following in zip(nodes, nodes[1:]):
            ratio = log_scale_ratio(current, following)
            self.assertAlmostEqual(ratio, expected, places=12)
            self.assertLess(ratio, SEVEN_SIXTHS)

    def test_seven_sixths_is_the_sharp_power_limit(self):
        ratios = [1.0 + 1.0 / (2.0 * q) for q in (4.0, 3.1, 3.01)]
        self.assertTrue(
            all(
                ratios[index + 1] > ratios[index]
                for index in range(len(ratios) - 1)
            )
        )
        self.assertLess(ratios[-1], SEVEN_SIXTHS)
        self.assertLess(SEVEN_SIXTHS - ratios[-1], 0.001)

    def test_event_roof_mean_diverges_in_the_survivor(self):
        nodes = ancestry_sequence(1.0e-4, 14, q=4.0, kappa=1.0)
        mean_roofs = [
            (nodes[index].log_scale - nodes[0].log_scale) / index
            for index in range(1, len(nodes))
        ]
        self.assertTrue(
            all(
                mean_roofs[index + 1] > mean_roofs[index]
                for index in range(len(mean_roofs) - 1)
            )
        )
        self.assertGreater(mean_roofs[-1], 2.0 * mean_roofs[0])

    def test_tail_increments_are_positive_and_telescope(self):
        nodes = ancestry_sequence(1.0e-3, 7, q=4.0)
        increments = tail_increments(nodes)
        self.assertTrue(all(increment > 0.0 for increment in increments))
        self.assertAlmostEqual(
            sum(increments),
            nodes[0].physical_tail_mass,
            places=14,
        )
        for index in range(len(nodes)):
            self.assertAlmostEqual(
                sum(increments[index:]),
                nodes[index].physical_tail_mass,
                places=14,
            )

    def test_carrier_frequency_enforces_cutoff_and_weak_l3_bound(self):
        mass = 2.0e-5
        width = 3.0e-12
        cutoff = 4.0e8
        weak_bound = 2.5
        bump_constant = 1.7
        frequency = minimum_carrier_frequency(
            tail_increment=mass,
            time_width=width,
            cutoff=cutoff,
            weak_l3_bound=weak_bound,
            bump_constant=bump_constant,
        )
        amplitude = bump_constant * math.sqrt(mass / width)
        self.assertGreaterEqual(frequency, cutoff)
        self.assertLessEqual(
            amplitude / math.sqrt(frequency),
            weak_bound * (1.0 + 1.0e-12),
        )

    def test_physical_intervals_and_scales_strictly_shrink(self):
        nodes = ancestry_sequence(1.0e-3, 6, q=4.0)
        for current, following in zip(nodes, nodes[1:]):
            self.assertLess(following.h, current.h)
            self.assertLess(following.sigma, current.sigma)
            self.assertLess(following.physical_time, current.physical_time)
            self.assertGreater(
                following.physical_cutoff,
                current.physical_cutoff,
            )

    def test_invalid_inputs_are_rejected(self):
        for invalid_h in (0.0, 1.0, -0.1):
            with self.assertRaises(ValueError):
                ancestry_node(invalid_h)
        with self.assertRaises(ValueError):
            ancestry_node(0.1, q=3.0)
        with self.assertRaises(ValueError):
            next_h(0.1, kappa=0.5)
        with self.assertRaises(ValueError):
            ancestry_sequence(0.1, 0)
        with self.assertRaises(ValueError):
            tail_increments([])
        with self.assertRaises(ValueError):
            minimum_carrier_frequency(
                tail_increment=0.0,
                time_width=1.0,
                cutoff=1.0,
            )


if __name__ == "__main__":
    unittest.main()
