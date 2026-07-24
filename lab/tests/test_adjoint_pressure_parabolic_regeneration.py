import unittest

from navier_lab.adjoint_pressure_parabolic_regeneration import (
    inherited_shell_cost,
    inherited_shell_sum,
    one_heat_time,
    outer_action_ceiling,
    physical_shell_action,
    physical_shell_action_reduced,
    scale_zero_lookback_is_admissible,
)


class AdjointPressureParabolicRegenerationTests(unittest.TestCase):
    def test_one_heat_time_has_parabolic_radius_power(self):
        self.assertEqual(
            one_heat_time(radius=6.0, viscosity=3.0),
            12.0,
        )

    def test_endpoint_inherited_cost_is_reciprocal_radius(self):
        self.assertEqual(
            inherited_shell_cost(
                radius=8.0,
                adjoint_constant=2.0,
                coefficient_constant=4.0,
            ),
            1.0,
        )

    def test_inherited_shells_sum_geometrically(self):
        self.assertEqual(
            inherited_shell_sum(
                base_radius=1.0,
                shell_ratio=16.0,
                adjoint_constant=15.0,
            ),
            16.0,
        )

    def test_physical_pullback_cancels_zoom_radius(self):
        direct = physical_shell_action(
            rescaled_radius=20.0,
            zoom_radius=0.05,
            physical_dissipation=3.0,
            physical_viscosity=2.0,
            adjoint_constant=7.0,
        )
        reduced = physical_shell_action_reduced(
            physical_radius=1.0,
            physical_dissipation=3.0,
            physical_viscosity=2.0,
            adjoint_constant=7.0,
        )
        self.assertAlmostEqual(direct, reduced)

    def test_outer_ceiling_is_square_root_absolute_continuous(self):
        first = outer_action_ceiling(
            minimum_physical_radius=1.0,
            shell_ratio=4.0,
            total_physical_dissipation=0.04,
            physical_viscosity=1.0,
        )
        second = outer_action_ceiling(
            minimum_physical_radius=1.0,
            shell_ratio=4.0,
            total_physical_dissipation=0.01,
            physical_viscosity=1.0,
        )
        self.assertEqual(first, 2.0 * second)
        self.assertEqual(
            outer_action_ceiling(
                minimum_physical_radius=1.0,
                shell_ratio=4.0,
                total_physical_dissipation=0.0,
                physical_viscosity=1.0,
            ),
            0.0,
        )

    def test_scale_zero_cutoff_has_strict_horizon_margin(self):
        self.assertTrue(
            scale_zero_lookback_is_admissible(
                physical_cutoff=0.5,
                viscosity=1.0,
                horizon_constant=1.0,
            )
        )
        self.assertFalse(
            scale_zero_lookback_is_admissible(
                physical_cutoff=1.0,
                viscosity=1.0,
                horizon_constant=1.0,
            )
        )

    def test_invalid_ledgers_are_rejected(self):
        with self.assertRaises(ValueError):
            one_heat_time(radius=1.0, viscosity=0.0)
        with self.assertRaises(ValueError):
            inherited_shell_sum(
                base_radius=1.0,
                shell_ratio=1.0,
            )
        with self.assertRaises(ValueError):
            outer_action_ceiling(
                minimum_physical_radius=1.0,
                shell_ratio=2.0,
                total_physical_dissipation=-1.0,
                physical_viscosity=1.0,
            )


if __name__ == "__main__":
    unittest.main()
