import math
import unittest

from navier_lab.adjoint_pressure_temporal import (
    capture_volume_floor,
    descendant_cell_floor,
    descendant_length,
    finite_band_time_space_capture,
    finite_band_weighted_time_space_capture,
    high_branch_time_capture,
    high_branch_weighted_time_capture,
    regularization_ceiling,
    saturation_ledger,
    weak_density_exponent,
)


class AdjointPressureTemporalTests(unittest.TestCase):
    def test_mass_gain_forces_quadratic_regularization_ceiling(self):
        h = 1.0e-5
        ceiling = regularization_ceiling(
            layer_time=h,
            difference_rate=3.0,
            regularized_mass=0.75,
        )
        self.assertTrue(math.isclose(ceiling, 6.0 * h**2))

    def test_capture_volume_has_inverse_square_power(self):
        h = 1.0e-6
        volume = capture_volume_floor(
            layer_time=h,
            difference_rate=2.0,
            captured_mass=0.5,
        )
        self.assertTrue(math.isclose(volume, h**-2 / 16.0))

    def test_descendant_cell_count_has_inverse_seven_halves_power(self):
        h = 1.0e-6
        kappa = 0.4
        cells = descendant_cell_floor(
            layer_time=h,
            difference_rate=2.0,
            captured_mass=0.5,
            kappa=kappa,
        )
        self.assertTrue(
            math.isclose(cells, kappa**3 * h**(-3.5) / 16.0)
        )
        self.assertTrue(
            math.isclose(descendant_length(h, kappa), math.sqrt(h) / kappa)
        )

    def test_high_branch_time_capture_is_square_root(self):
        mass_floor = 0.5
        constant = 1.7
        first = high_branch_time_capture(
            0.25,
            mass_floor,
            constant,
        )
        second = high_branch_time_capture(
            1.0,
            mass_floor,
            constant,
        )
        self.assertTrue(math.isclose(first, 0.5 * second))

    def test_high_branch_terminal_edge_has_three_halves_power(self):
        delta = 0.2
        first = high_branch_weighted_time_capture(
            delta**3 / 3.0,
            energy_fraction=1.0,
        )
        second = high_branch_weighted_time_capture(
            (2.0 * delta) ** 3 / 3.0,
            energy_fraction=1.0,
        )
        self.assertTrue(math.isclose(second, 2.0**1.5 * first))

    def test_finite_band_capture_is_linear_in_time_fraction(self):
        mass_floor = 0.4
        constant = 2.0
        volume = 64.0
        first = finite_band_time_space_capture(
            0.2,
            volume,
            mass_floor,
            constant,
        )
        second = finite_band_time_space_capture(
            0.4,
            volume,
            mass_floor,
            constant,
        )
        self.assertTrue(math.isclose(second, 2.0 * first))
        self.assertTrue(
            math.isclose(
                first,
                constant * 0.2 * 2.0 / mass_floor,
            )
        )

    def test_finite_band_terminal_edge_has_quadratic_power(self):
        delta = 0.2
        first = finite_band_weighted_time_space_capture(
            time_fraction=delta,
            time_second_moment=delta**3 / 3.0,
            macro_volume=1.0,
        )
        second = finite_band_weighted_time_space_capture(
            time_fraction=2.0 * delta,
            time_second_moment=(2.0 * delta) ** 3 / 3.0,
            macro_volume=1.0,
        )
        self.assertTrue(math.isclose(second, 4.0 * first))

    def test_capture_exponents_give_time_and_space_densities(self):
        self.assertTrue(math.isclose(weak_density_exponent(0.5), 2.0))
        self.assertTrue(
            math.isclose(
                weak_density_exponent(1.0 / 6.0),
                6.0 / 5.0,
            )
        )

    def test_kinematic_seed_saturates_every_power(self):
        h = 1.0e-4
        kappa = 0.3
        ledger = saturation_ledger(h, kappa)
        self.assertTrue(math.isclose(ledger["amplitude"], h**2))
        self.assertTrue(math.isclose(ledger["regularization"], h**2))
        self.assertTrue(math.isclose(ledger["volume"], h**-2))
        self.assertTrue(math.isclose(ledger["l1"], 1.0))
        self.assertTrue(math.isclose(ledger["l2_squared"], h**2))
        self.assertTrue(
            math.isclose(
                ledger["frequency"],
                kappa * h**-0.5,
            )
        )
        self.assertTrue(
            math.isclose(
                ledger["spatial_gradient_squared"],
                kappa**2 * h,
            )
        )
        self.assertTrue(
            math.isclose(
                ledger["spacetime_gradient_squared"],
                kappa**2 * h**2,
            )
        )
        self.assertTrue(
            math.isclose(
                ledger["descendant_cells"],
                kappa**3 * h**(-3.5),
            )
        )
        self.assertTrue(
            math.isclose(ledger["descendant_rooted_frequency"], 1.0)
        )
        self.assertTrue(
            math.isclose(ledger["naive_polar_modulus"], h**-1)
        )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            regularization_ceiling(0.0, 1.0, 1.0)
        with self.assertRaises(ValueError):
            capture_volume_floor(1.0, -1.0, 1.0)
        with self.assertRaises(ValueError):
            high_branch_time_capture(1.1)
        with self.assertRaises(ValueError):
            finite_band_time_space_capture(0.5, 0.0)
        with self.assertRaises(ValueError):
            high_branch_weighted_time_capture(-1.0, 0.5)
        with self.assertRaises(ValueError):
            high_branch_weighted_time_capture(1.0, 1.1)
        with self.assertRaises(ValueError):
            finite_band_weighted_time_space_capture(
                0.5,
                -1.0,
                1.0,
            )
        with self.assertRaises(ValueError):
            weak_density_exponent(1.0)
        with self.assertRaises(ValueError):
            saturation_ledger(1.0, 0.0)


if __name__ == "__main__":
    unittest.main()
