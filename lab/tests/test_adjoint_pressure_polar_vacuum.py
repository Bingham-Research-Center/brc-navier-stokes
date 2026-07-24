import math
import unittest

from navier_lab.adjoint_pressure_polar_vacuum import (
    artificial_mark_capture,
    balanced_orlicz_tail,
    descendant_frequency,
    inverse_ninth_regularization_ceiling,
    moving_grid_capture,
    moving_grid_integral_capture,
    normalized_pressure_mass_per_source_cell,
    polar_cell_ceiling,
    polar_volume_ceiling,
    pressure_cell_floor,
    quadratic_vacuum_bad_mass,
    source_volume_ledger,
)


class AdjointPressurePolarVacuumTests(unittest.TestCase):
    def test_descendant_frequency_has_parabolic_power(self):
        h = 1.0e-6
        kappa = 0.3
        self.assertTrue(
            math.isclose(
                descendant_frequency(h, kappa),
                kappa * h**-0.5,
            )
        )

    def test_moving_grid_forms_agree_for_constant_count(self):
        h = 1.0e-5
        cells = 4.0e7
        kappa = 0.4
        direct = moving_grid_capture(h, cells, kappa)
        integral = moving_grid_integral_capture(
            h,
            h * cells ** (1.0 / 3.0),
            kappa,
        )
        self.assertTrue(math.isclose(direct, integral))

    def test_polar_volume_is_inverse_regularization(self):
        epsilon = 2.0e-8
        mass = 3.0
        self.assertTrue(
            math.isclose(
                polar_volume_ceiling(epsilon, mass),
                2.0 * mass / epsilon,
            )
        )

    def test_pressure_cloud_has_inverse_twenty_one_halves_cells(self):
        h = 1.0e-4
        floor = pressure_cell_floor(h)
        self.assertTrue(math.isclose(floor, h ** (-21.0 / 2.0)))

    def test_polar_cell_comparison_forces_inverse_ninth_scale(self):
        h = 1.0e-4
        ceiling = inverse_ninth_regularization_ceiling(h)
        self.assertTrue(math.isclose(ceiling, h**9))
        self.assertTrue(
            math.isclose(
                polar_cell_ceiling(
                    h,
                    ceiling,
                    regularized_mass_ceiling=0.5,
                ),
                h ** (-21.0 / 2.0),
            )
        )

    def test_quadratic_vacuum_bad_mass_has_seven_sixths_power(self):
        h = 1.0e-5
        first = quadratic_vacuum_bad_mass(h, 0.25)
        second = quadratic_vacuum_bad_mass(2.0 * h, 0.25)
        self.assertTrue(
            math.isclose(second, 2.0 ** (7.0 / 6.0) * first)
        )

    def test_balanced_amplitude_has_orlicz_tail_and_unit_cell_mass(self):
        h = 1.0e-4
        first = balanced_orlicz_tail(1.0, 64.0)
        second = balanced_orlicz_tail(1.0, 64.0 * 2.0**6)
        self.assertTrue(math.isclose(second, first / 2.0))
        self.assertTrue(
            math.isclose(
                normalized_pressure_mass_per_source_cell(
                    h,
                    h**9,
                ),
                1.0,
            )
        )
        self.assertTrue(
            math.isclose(
                normalized_pressure_mass_per_source_cell(
                    h,
                    0.25 * h**9,
                ),
                4.0,
            )
        )

    def test_source_volume_model_saturates_every_new_power(self):
        h = 1.0e-4
        ledger = source_volume_ledger(h)
        self.assertTrue(math.isclose(ledger["source_radius"], h**-3))
        self.assertTrue(math.isclose(ledger["volume"], h**-9))
        self.assertTrue(math.isclose(ledger["amplitude"], h**9))
        self.assertTrue(math.isclose(ledger["regularization"], h**9))
        self.assertTrue(math.isclose(ledger["regularized_mass"], 1.0))
        self.assertTrue(math.isclose(ledger["l2_squared"], h**9))
        self.assertTrue(
            math.isclose(ledger["spatial_gradient_squared"], h**8)
        )
        self.assertTrue(
            math.isclose(ledger["spacetime_gradient_squared"], h**9)
        )
        self.assertTrue(math.isclose(ledger["polar_l2_squared"], h**-9))
        self.assertTrue(math.isclose(ledger["kato_dissipation"], 1.0))
        self.assertTrue(
            math.isclose(
                ledger["descendant_cells"],
                h ** (-21.0 / 2.0),
            )
        )
        self.assertTrue(
            math.isclose(ledger["pressure_amplitude"], h**8)
        )
        self.assertTrue(
            math.isclose(ledger["pressure_l1_spacetime"], 1.0)
        )
        self.assertTrue(
            math.isclose(
                ledger["pressure_mass_per_cell"],
                h ** (21.0 / 2.0),
            )
        )

    def test_artificial_mark_obeys_capture_power(self):
        h = 1.0e-4
        total_cells = source_volume_ledger(h)["descendant_cells"]
        for fraction in (1.0e-6, 1.0e-3, 0.25, 1.0):
            cells = fraction * total_cells
            captured = artificial_mark_capture(h, cells)
            bound = moving_grid_capture(h, cells)
            self.assertLessEqual(captured, bound * (1.0 + 1.0e-12))

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            descendant_frequency(0.0)
        with self.assertRaises(ValueError):
            moving_grid_capture(1.0, 0.0)
        with self.assertRaises(ValueError):
            moving_grid_integral_capture(1.0, -1.0)
        with self.assertRaises(ValueError):
            polar_volume_ceiling(0.0)
        with self.assertRaises(ValueError):
            polar_cell_ceiling(1.0, 1.0, kappa=0.0)
        with self.assertRaises(ValueError):
            pressure_cell_floor(1.0, pressure_mass=0.0)
        with self.assertRaises(ValueError):
            inverse_ninth_regularization_ceiling(
                1.0,
                polar_cell_constant=0.0,
            )
        with self.assertRaises(ValueError):
            quadratic_vacuum_bad_mass(1.0, 0.0)
        with self.assertRaises(ValueError):
            balanced_orlicz_tail(0.0, 1.0)
        with self.assertRaises(ValueError):
            normalized_pressure_mass_per_source_cell(1.0, -1.0)
        with self.assertRaises(ValueError):
            source_volume_ledger(-1.0)
        with self.assertRaises(ValueError):
            artificial_mark_capture(1.0, 0.0)


if __name__ == "__main__":
    unittest.main()
