import unittest

from navier_lab.adjoint_pressure_flux_decrement import (
    admissible_lower_ratio,
    decrement_constant,
    far_low_viscosity_fraction,
    hitting_certificate,
    low_entrance_certificate,
    pressure_tail_lower_band_floor,
    retained_flux_after_depth,
)


class AdjointPressureFluxDecrementTests(unittest.TestCase):
    def test_ratio_makes_far_low_term_at_most_one_twelfth(self):
        viscosity = 2.0
        weak_l3_bound = 7.0
        low_pass_constant = 3.0
        ratio = admissible_lower_ratio(
            viscosity=viscosity,
            weak_l3_bound=weak_l3_bound,
            low_pass_constant=low_pass_constant,
        )
        fraction = far_low_viscosity_fraction(
            lower_ratio=ratio,
            weak_l3_bound=weak_l3_bound,
            viscosity=viscosity,
            low_pass_constant=low_pass_constant,
        )
        self.assertLessEqual(fraction, 1.0 / 12.0)
        self.assertLessEqual(ratio, 1.0 / 8.0)

    def test_ratio_cap_also_respects_viscosity_fraction(self):
        ratio = admissible_lower_ratio(
            viscosity=10.0,
            weak_l3_bound=0.01,
            low_pass_constant=1.0,
        )
        self.assertEqual(ratio, 1.0 / 8.0)
        self.assertLessEqual(
            far_low_viscosity_fraction(
                lower_ratio=ratio,
                weak_l3_bound=0.01,
                viscosity=10.0,
            ),
            1.0 / 12.0,
        )

    def test_common_decrement_constant(self):
        self.assertEqual(
            decrement_constant(remainder_constant=3.0),
            1.0 / 48.0,
        )

    def test_low_entrance_identity_and_decrement(self):
        result = low_entrance_certificate(
            viscosity=2.0,
            weak_l3_bound=4.0,
            tail_floor=8.0,
            high_dissipation=7.0,
            entrance_energy=12.0,
            terminal_energy=4.0,
            remainder_constant=2.0,
        )
        self.assertEqual(result.flux, 10.0)
        expected_relative = (
            decrement_constant(remainder_constant=2.0)
            * 2.0**2
            / 4.0**2
        )
        self.assertEqual(result.relative_decrement, expected_relative)
        self.assertEqual(
            result.viscosity_weighted_decrement_floor,
            expected_relative * result.flux,
        )

    def test_low_entrance_extreme_endpoint_still_has_positive_flux(self):
        result = low_entrance_certificate(
            viscosity=1.0,
            weak_l3_bound=2.0,
            tail_floor=4.0,
            high_dissipation=3.1,
            entrance_energy=3.9,
            terminal_energy=0.0,
        )
        self.assertGreater(result.flux, 1.0)

    def test_half_to_full_hitting_flux_identity(self):
        result = hitting_certificate(
            viscosity=3.0,
            weak_l3_bound=5.0,
            full_energy=8.0,
            high_dissipation=4.0,
            remainder_constant=2.0,
        )
        self.assertEqual(result.flux, 14.0)
        self.assertEqual(
            result.relative_decrement,
            decrement_constant(remainder_constant=2.0)
            * 3.0**2
            / 5.0**2,
        )

    def test_pressure_tail_corollary_has_exact_powers(self):
        value = pressure_tail_lower_band_floor(
            viscosity=3.0,
            weak_l3_bound=2.0,
            tail_floor=8.0,
            remainder_constant=1.5,
        )
        expected = (
            decrement_constant(remainder_constant=1.5)
            * 3.0**2
            * 8.0
            / (4.0 * 2.0**2)
        )
        self.assertEqual(value, expected)

    def test_uniform_decrement_forces_geometric_retention(self):
        values = [
            retained_flux_after_depth(
                initial_flux=10.0,
                relative_decrement=0.25,
                depth=depth,
            )
            for depth in range(6)
        ]
        self.assertEqual(values[0], 10.0)
        self.assertTrue(
            all(
                values[index + 1] < values[index]
                for index in range(len(values) - 1)
            )
        )
        self.assertAlmostEqual(values[-1], 10.0 / 1.25**5)

    def test_invalid_ledgers_are_rejected(self):
        with self.assertRaises(ValueError):
            admissible_lower_ratio(
                viscosity=0.0,
                weak_l3_bound=1.0,
            )
        with self.assertRaises(ValueError):
            low_entrance_certificate(
                viscosity=1.0,
                weak_l3_bound=1.0,
                tail_floor=1.0,
                high_dissipation=1.0,
                entrance_energy=1.0,
            )
        with self.assertRaises(ValueError):
            low_entrance_certificate(
                viscosity=1.0,
                weak_l3_bound=1.0,
                tail_floor=1.0,
                high_dissipation=0.75,
                entrance_energy=0.5,
            )
        with self.assertRaises(ValueError):
            retained_flux_after_depth(
                initial_flux=1.0,
                relative_decrement=0.1,
                depth=-1,
            )


if __name__ == "__main__":
    unittest.main()
