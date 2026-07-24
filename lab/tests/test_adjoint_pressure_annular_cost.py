import unittest

from navier_lab.adjoint_pressure_annular_cost import (
    annular_pressure_weight,
    critical_tail_partial_sum,
    gradient_rescaling_exponent,
    local_energy_restart_ceiling,
    shell_lp_radius_exponent,
    static_cell_ledger,
    summable_tail_ceiling,
)


class AdjointPressureAnnularCostTests(unittest.TestCase):
    def test_restart_ceiling_has_large_and_small_radius_terms(self):
        self.assertEqual(
            local_energy_restart_ceiling(
                radius=4.0,
                duration=8.0,
                viscosity=2.0,
                restart_constant=3.0,
            ),
            24.0,
        )

    def test_annular_weight_adds_dissipation_and_cutoff_terms(self):
        self.assertAlmostEqual(
            annular_pressure_weight(
                radius=4.0,
                duration=4.0,
                weak_l3_bound=3.0,
                viscosity=1.0,
                restart_constant=1.0,
            ),
            5.0**0.5 + 3.0,
        )

    def test_endpoint_half_tail_spends_one_unit_per_shell(self):
        for depth in (1, 4, 11):
            self.assertEqual(
                critical_tail_partial_sum(
                    base_radius=2.0,
                    shell_ratio=16.0,
                    tail_constant=3.0,
                    tail_exponent=0.5,
                    shell_count=depth,
                ),
                3.0 * depth,
            )

    def test_any_positive_tail_gain_is_geometrically_summable(self):
        partial = critical_tail_partial_sum(
            base_radius=4.0,
            shell_ratio=16.0,
            tail_constant=2.0,
            tail_exponent=0.75,
            shell_count=20,
        )
        ceiling = summable_tail_ceiling(
            base_radius=4.0,
            shell_ratio=16.0,
            tail_constant=2.0,
            tail_exponent=0.75,
        )
        self.assertLess(partial, ceiling)
        self.assertAlmostEqual(ceiling, 2.0 * 2.0**0.5)

    def test_five_halves_is_the_physical_scaling_threshold(self):
        self.assertAlmostEqual(shell_lp_radius_exponent(2.5), -0.2)
        self.assertEqual(gradient_rescaling_exponent(2.5), 0.0)
        self.assertLess(gradient_rescaling_exponent(2.49), 0.0)
        self.assertGreater(gradient_rescaling_exponent(2.51), 0.0)

    def test_static_cell_cloud_saturates_all_endpoint_powers(self):
        result = static_cell_ledger(radius=16.0)
        self.assertEqual(result.cell_count, 16.0**3)
        self.assertAlmostEqual(result.weak_l3_proxy, 1.0)
        self.assertEqual(result.adjoint_l2, 16.0**-0.5)
        self.assertEqual(
            result.coefficient_gradient_l2,
            16.0**0.5,
        )
        self.assertEqual(result.bilinear_l1_proxy, 1.0)

    def test_invalid_ledgers_are_rejected(self):
        with self.assertRaises(ValueError):
            local_energy_restart_ceiling(
                radius=0.0,
                duration=1.0,
            )
        with self.assertRaises(ValueError):
            critical_tail_partial_sum(
                base_radius=1.0,
                shell_ratio=1.0,
                tail_constant=1.0,
                tail_exponent=0.5,
                shell_count=2,
            )
        with self.assertRaises(ValueError):
            summable_tail_ceiling(
                base_radius=1.0,
                shell_ratio=2.0,
                tail_constant=1.0,
                tail_exponent=0.5,
            )
        with self.assertRaises(ValueError):
            shell_lp_radius_exponent(3.0)


if __name__ == "__main__":
    unittest.main()
