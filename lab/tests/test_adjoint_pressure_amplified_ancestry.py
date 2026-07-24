from decimal import Decimal, localcontext
import unittest

from navier_lab.adjoint_pressure_amplified_ancestry import (
    BASE_EXPONENT,
    amplified_exponent,
    amplified_node,
    amplified_sequence,
    amplification_identity_residual,
    ancestry_residual,
    cost_identity_residual,
    cumulative_slab_masses,
    frequency_certificate,
    next_amplified_depth,
    next_event_charge_log,
)


class AdjointPressureAmplifiedAncestryTests(unittest.TestCase):
    PARAMS = {
        "beta": "0.0625",
        "c": "0.001",
        "acceleration": "2",
        "tail_constant": "0.01",
        "precision": 100,
    }

    def test_frequency_adds_to_the_reviewed_stretched_exponent(self):
        self.assertEqual(
            amplified_exponent(Decimal("0.0625")),
            Decimal(29) / Decimal(16),
        )

    def test_frequency_times_old_depth_is_the_new_coordinate(self):
        node = amplified_node("10000", **self.PARAMS)
        self.assertLess(
            abs(amplification_identity_residual(node)),
            Decimal("1e-90"),
        )

    def test_total_dissipation_saturates_the_amplified_cost(self):
        node = amplified_node("10000", **self.PARAMS)
        self.assertLess(
            abs(cost_identity_residual(node, c=self.PARAMS["c"])),
            Decimal("1e-90"),
        )

    def test_next_depth_solves_exact_ancestry(self):
        nodes = amplified_sequence("10000", 5, **self.PARAMS)
        for current, following in zip(nodes, nodes[1:]):
            self.assertLess(
                abs(ancestry_residual(current, following)),
                Decimal("1e-80"),
            )
            self.assertGreater(following.y, current.y)
            self.assertLess(following.h, current.h)

    def test_top_physical_frequency_is_next_reciprocal_scale(self):
        nodes = amplified_sequence("10000", 5, **self.PARAMS)
        for current, following in zip(nodes, nodes[1:]):
            with localcontext() as context:
                context.prec = 100
                residual = (
                    current.log_frequency
                    - current.log_zoom
                    + following.log_zoom
                )
            self.assertLess(abs(residual), Decimal("1e-80"))

    def test_increment_is_small_relative_to_amplified_depth(self):
        ratios = []
        for y in ("1000", "3000", "10000", "30000"):
            y_d = Decimal(y)
            following = next_amplified_depth(
                y_d,
                beta=self.PARAMS["beta"],
                c=self.PARAMS["c"],
                acceleration=self.PARAMS["acceleration"],
                precision=self.PARAMS["precision"],
            )
            ratios.append((following - y_d) / y_d)
        self.assertTrue(
            all(
                ratios[index + 1] < ratios[index]
                for index in range(len(ratios) - 1)
            )
        )

    def test_tail_charge_and_fraction_vanish(self):
        nodes = [
            amplified_node(y, **self.PARAMS)
            for y in ("1000", "3000", "10000", "30000")
        ]
        tail_logs = [node.log_tail_mass for node in nodes]
        fraction_logs = [node.log_tail_fraction for node in nodes]
        self.assertTrue(
            all(
                tail_logs[index + 1] < tail_logs[index]
                for index in range(len(tail_logs) - 1)
            )
        )
        self.assertTrue(
            all(
                fraction_logs[index + 1] < fraction_logs[index]
                for index in range(len(fraction_logs) - 1)
            )
        )
        self.assertLess(fraction_logs[-1], Decimal("-20"))

    def test_polynomial_frequency_remains_below_kill_frequency(self):
        nodes = [
            amplified_node(y, **self.PARAMS)
            for y in ("1000", "3000", "10000", "30000")
        ]
        gaps = [
            node.log_frequency - node.log_kill_frequency
            for node in nodes
        ]
        self.assertTrue(
            all(
                gaps[index + 1] < gaps[index]
                for index in range(len(gaps) - 1)
            )
        )
        self.assertLess(gaps[-1], Decimal("-20"))

    def test_one_nested_history_recovers_total_and_tail_masses(self):
        nodes = amplified_sequence("10000", 5, **self.PARAMS)
        slabs = frequency_certificate(nodes)
        self.assertTrue(
            all(
                slab.bulk_mass > 0 and slab.high_mass > 0
                for slab in slabs
            )
        )
        for index, node in enumerate(nodes):
            bulk, high = cumulative_slab_masses(slabs, index)
            with localcontext() as context:
                context.prec = 100
                total = node.log_total_mass.exp()
                tail = node.log_tail_mass.exp()
                recovered_total = bulk + high
            self.assertLess(abs(high - tail), Decimal("1e-90"))
            self.assertLess(abs(recovered_total - total), Decimal("1e-90"))

    def test_high_slab_frequencies_meet_every_nested_threshold(self):
        nodes = amplified_sequence("10000", 5, **self.PARAMS)
        slabs = frequency_certificate(nodes)
        self.assertTrue(
            all(
                slabs[index + 1].log_high_frequency
                >= slabs[index].log_high_frequency
                for index in range(len(slabs) - 1)
            )
        )
        for index, node in enumerate(nodes):
            with localcontext() as context:
                context.prec = 100
                threshold = node.log_frequency - node.log_zoom
                gaps = [
                    slab.log_high_frequency - threshold
                    for slab in slabs[index:]
                ]
            self.assertTrue(
                all(gap >= Decimal("-1e-80") for gap in gaps)
            )

    def test_three_halves_boundary_persists_in_new_coordinate(self):
        exponent = amplified_exponent(self.PARAMS["beta"])
        boundaries = []
        for y in (Decimal("1000"), Decimal("3000"), Decimal("10000")):
            boundaries.append(
                next_event_charge_log(
                    y,
                    Decimal("1.5") * y,
                    beta=self.PARAMS["beta"],
                    c=self.PARAMS["c"],
                    acceleration=self.PARAMS["acceleration"],
                )
            )
        with localcontext() as context:
            context.prec = 100
            expected = (Decimal(6) / exponent) * Decimal("1.5").ln()
        self.assertTrue(
            all(abs(value - expected) < Decimal("1e-90") for value in boundaries)
        )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            amplified_exponent(0)
        with self.assertRaises(ValueError):
            amplified_node("1", **self.PARAMS)
        with self.assertRaises(ValueError):
            amplified_node("10", beta="0", c="1", acceleration="2")
        with self.assertRaises(ValueError):
            amplified_node("10", beta="1", c="0", acceleration="2")
        with self.assertRaises(ValueError):
            amplified_node("10", beta="1", c="1", acceleration="1")
        with self.assertRaises(ValueError):
            amplified_sequence("10000", 0, **self.PARAMS)
        with self.assertRaises(ValueError):
            next_event_charge_log("10", "9")
        with self.assertRaises(ValueError):
            cumulative_slab_masses([], 0)


if __name__ == "__main__":
    unittest.main()
