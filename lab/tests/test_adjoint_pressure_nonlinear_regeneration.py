import unittest

from navier_lab.adjoint_pressure_nonlinear_regeneration import (
    heat_erasure_horizon_power,
    inherited_budget_ceiling,
    inherited_shell_sum_power,
    low_frequency_shell_sum,
    physical_erasure_rho_power,
)


class AdjointPressureNonlinearRegenerationTests(unittest.TestCase):
    def test_reciprocal_frequency_cost_is_geometric(self):
        self.assertEqual(
            low_frequency_shell_sum(
                base_radius=1.0,
                shell_ratio=16.0,
                coefficient=15.0,
            ),
            16.0,
        )

    def test_endpoint_tail_adds_one_quarter_horizon_power(self):
        self.assertEqual(
            inherited_shell_sum_power(tail_exponent=0.5),
            0.25,
        )
        self.assertEqual(
            heat_erasure_horizon_power(tail_exponent=0.5),
            0.75,
        )

    def test_physical_genealogy_inherited_budget_vanishes_linearly(self):
        self.assertEqual(
            physical_erasure_rho_power(
                energy_blowup_power=0.5,
                horizon_growth_power=2.0,
                tail_exponent=0.5,
            ),
            1.0,
        )

    def test_inherited_budget_has_energy_times_horizon_minus_three_quarters(self):
        self.assertEqual(
            inherited_budget_ceiling(
                energy_ceiling=8.0,
                horizon=16.0,
                duration=4.0,
                tail_constant=3.0,
                tail_exponent=0.5,
                heat_constant=2.0,
            ),
            12.0,
        )

    def test_any_positive_tail_improves_heat_erasure(self):
        weak_tail = heat_erasure_horizon_power(
            tail_exponent=0.25,
        )
        endpoint = heat_erasure_horizon_power(
            tail_exponent=0.5,
        )
        strong_tail = heat_erasure_horizon_power(
            tail_exponent=0.75,
        )
        self.assertLess(weak_tail, endpoint)
        self.assertLess(endpoint, strong_tail)

    def test_invalid_ledgers_are_rejected(self):
        with self.assertRaises(ValueError):
            low_frequency_shell_sum(
                base_radius=1.0,
                shell_ratio=1.0,
            )
        with self.assertRaises(ValueError):
            inherited_budget_ceiling(
                energy_ceiling=1.0,
                horizon=0.0,
                duration=1.0,
                tail_constant=1.0,
            )
        with self.assertRaises(ValueError):
            physical_erasure_rho_power(
                energy_blowup_power=-1.0,
            )


if __name__ == "__main__":
    unittest.main()
