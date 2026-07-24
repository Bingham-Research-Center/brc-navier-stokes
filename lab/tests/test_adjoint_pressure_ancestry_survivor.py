from decimal import Decimal, localcontext
import unittest

from navier_lab.adjoint_pressure_ancestry_survivor import (
    LN2,
    P,
    ancestry_node,
    ancestry_residual,
    ancestry_sequence,
    cumulative_slab_masses,
    frequency_certificate,
    next_event_charge_log,
    next_depth,
)


class AdjointPressureAncestrySurvivorTests(unittest.TestCase):
    PARAMS = {
        "c": "0.001",
        "acceleration": "2",
        "c_dep": "1",
        "tail_constant": "0.01",
        "precision": 100,
    }

    def test_dyadic_frequency_has_the_reviewed_polynomial_size(self):
        node = ancestry_node("10000", **self.PARAMS)
        alpha = Decimal(self.PARAMS["c_dep"]) * LN2
        log_inverse_h = node.x.ln() / P
        gap = node.log_top_frequency - alpha * log_inverse_h
        self.assertLessEqual(gap, 0)
        self.assertGreaterEqual(gap, -LN2)

    def test_next_depth_solves_exact_ancestry_identity(self):
        nodes = ancestry_sequence("10000", 4, **self.PARAMS)
        for current, following in zip(nodes, nodes[1:]):
            self.assertLess(
                abs(ancestry_residual(current, following)),
                Decimal("1e-80"),
            )
            self.assertGreater(following.x, current.x)
            self.assertLess(following.h, current.h)

    def test_top_physical_frequency_is_the_next_reciprocal_scale(self):
        nodes = ancestry_sequence("10000", 4, **self.PARAMS)
        for current, following in zip(nodes, nodes[1:]):
            with localcontext() as context:
                context.prec = 100
                current_log_physical_frequency = (
                    current.log_top_frequency - current.log_zoom
                )
                residual = (
                    current_log_physical_frequency
                    + following.log_zoom
                )
            self.assertLess(
                abs(residual),
                Decimal("1e-80"),
            )

    def test_terminal_return_charge_vanishes_inside_total_mass(self):
        nodes = [
            ancestry_node(x, **self.PARAMS)
            for x in ("1000", "3000", "10000", "30000")
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

    def test_causal_frequency_is_far_below_the_kill_frequency(self):
        nodes = [
            ancestry_node(x, **self.PARAMS)
            for x in ("1000", "3000", "10000", "30000")
        ]
        gaps = [
            node.log_top_frequency - node.log_kill_frequency
            for node in nodes
        ]
        self.assertTrue(
            all(
                gaps[index + 1] < gaps[index]
                for index in range(len(gaps) - 1)
            )
        )
        self.assertLess(gaps[-1], Decimal("-20"))

    def test_one_history_splits_into_positive_bulk_and_tail_slabs(self):
        nodes = ancestry_sequence("10000", 5, **self.PARAMS)
        slabs = frequency_certificate(nodes)
        self.assertEqual(len(slabs), len(nodes))
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

    def test_high_slab_frequencies_are_nested(self):
        nodes = ancestry_sequence("10000", 5, **self.PARAMS)
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
                threshold = node.log_top_frequency - node.log_zoom
                differences = [
                    slab.log_high_frequency - threshold
                    for slab in slabs[index:]
                ]
            self.assertTrue(
                all(
                    difference >= Decimal("-1e-80")
                    for difference in differences
                )
            )

    def test_tail_normalisation_is_exact(self):
        node = ancestry_node("10000", **self.PARAMS)
        with localcontext() as context:
            context.prec = 100
            log_normalised_tail = node.log_tail_mass - node.log_zoom
            expected = (
                Decimal(self.PARAMS["tail_constant"]).ln()
                + Decimal(2) * node.log_top_frequency
                - Decimal(3) * node.h.ln()
            )
        self.assertLess(
            abs(log_normalised_tail - expected),
            Decimal("1e-90"),
        )

    def test_next_increment_is_small_relative_to_stretched_depth(self):
        ratios = []
        for x in ("1000", "3000", "10000", "30000"):
            x_d = Decimal(x)
            following = next_depth(
                x_d,
                c=self.PARAMS["c"],
                acceleration=self.PARAMS["acceleration"],
                c_dep=self.PARAMS["c_dep"],
                precision=self.PARAMS["precision"],
            )
            ratios.append((following - x_d) / x_d)
        self.assertTrue(
            all(
                ratios[index + 1] < ratios[index]
                for index in range(len(ratios) - 1)
            )
        )

    def test_three_halves_is_the_exact_next_event_charge_threshold(self):
        c = Decimal(self.PARAMS["c"])
        acceleration = Decimal(self.PARAMS["acceleration"])
        below = []
        boundary = []
        above = []
        for x in (Decimal("1000"), Decimal("3000"), Decimal("10000")):
            below.append(
                next_event_charge_log(
                    x,
                    Decimal("1.4") * x,
                    c=c,
                    acceleration=acceleration,
                )
            )
            boundary.append(
                next_event_charge_log(
                    x,
                    Decimal("1.5") * x,
                    c=c,
                    acceleration=acceleration,
                )
            )
            above.append(
                next_event_charge_log(
                    x,
                    Decimal("1.6") * x,
                    c=c,
                    acceleration=acceleration,
                )
            )
        self.assertTrue(
            all(
                below[index + 1] < below[index]
                for index in range(len(below) - 1)
            )
        )
        with localcontext() as context:
            context.prec = 100
            expected_boundary = (Decimal(6) / P) * Decimal("1.5").ln()
            boundary_errors = [
                abs(value - expected_boundary) for value in boundary
            ]
        self.assertTrue(
            all(
                error < Decimal("1e-90")
                for error in boundary_errors
            )
        )
        self.assertTrue(
            all(
                above[index + 1] > above[index]
                for index in range(len(above) - 1)
            )
        )
        self.assertLess(below[-1], 0)
        self.assertGreater(above[-1], 0)

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            ancestry_node("1", **self.PARAMS)
        with self.assertRaises(ValueError):
            ancestry_node("10", c="0", acceleration="2", c_dep="1")
        with self.assertRaises(ValueError):
            ancestry_node("10", c="1", acceleration="1", c_dep="1")
        with self.assertRaises(ValueError):
            ancestry_node("10", c="1", acceleration="2", c_dep="0")
        with self.assertRaises(ValueError):
            ancestry_sequence("10000", 0, **self.PARAMS)
        with self.assertRaises(ValueError):
            next_depth("2", c="1", acceleration="2", c_dep="0.01")
        with self.assertRaises(ValueError):
            next_event_charge_log("10", "9")
        with self.assertRaises(ValueError):
            cumulative_slab_masses([], 0)


if __name__ == "__main__":
    unittest.main()
