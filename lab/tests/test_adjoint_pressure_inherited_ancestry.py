import unittest

from navier_lab.adjoint_pressure_inherited_ancestry import (
    farther_parabolic_cutoff,
    fixed_time_tail_upper,
    historical_flux_from_last_hitting,
    inherited_ancestry_certificate,
    parabolic_sharp_floor,
    squeezed_terminal_flux_floor,
    threshold_frequency_product,
)


class AdjointPressureInheritedAncestryTests(unittest.TestCase):
    def test_fixed_time_tail_is_the_h1_plancherel_bound(self):
        self.assertEqual(
            fixed_time_tail_upper(enstrophy=45.0, cutoff=3.0),
            5.0,
        )

    def test_parabolic_floor_and_farther_cutoff_have_exact_scaling(self):
        sigma = 2.0e-5
        h = 4.0e-4
        coefficient = 3.0
        multiplier_bound = 2.0
        kappa = 1.5
        farther_factor = 2.5
        self.assertAlmostEqual(
            parabolic_sharp_floor(
                sigma=sigma,
                h=h,
                coefficient=coefficient,
                multiplier_bound=multiplier_bound,
            ),
            coefficient * sigma * h ** (-3.0)
            / multiplier_bound**2,
        )
        self.assertAlmostEqual(
            farther_parabolic_cutoff(
                sigma=sigma,
                h=h,
                kappa=kappa,
                farther_factor=farther_factor,
            ),
            farther_factor * kappa / (sigma * h**0.5),
        )

    def test_threshold_frequency_product_is_exact(self):
        sigma = 7.0e-6
        h = 3.0e-4
        coefficient = 2.0
        multiplier_bound = 5.0
        kappa = 1.25
        farther_factor = 3.0
        value = threshold_frequency_product(
            sigma=sigma,
            h=h,
            coefficient=coefficient,
            multiplier_bound=multiplier_bound,
            kappa=kappa,
            farther_factor=farther_factor,
        )
        expected = (
            coefficient
            * kappa**2
            * farther_factor**2
            / multiplier_bound**2
            * sigma ** (-1.0)
            * h ** (-4.0)
        )
        self.assertAlmostEqual(value / expected, 1.0)

    def test_vanishing_tail_floor_still_overwhelms_fixed_h1_tail(self):
        ratios = []
        floors = []
        for exponent in (2, 3, 4, 5):
            h = 10.0 ** (-exponent)
            sigma = h**4
            result = inherited_ancestry_certificate(
                sigma=sigma,
                h=h,
                viscosity=1.0,
                fixed_time_enstrophy=100.0,
                coefficient=1.0,
                multiplier_bound=1.0,
                kappa=1.0,
                farther_factor=2.0,
            )
            floors.append(result.sharp_floor)
            ratios.append(
                result.half_threshold
                / result.fixed_time_tail_upper
            )
        self.assertTrue(
            all(
                floors[index + 1] < floors[index]
                for index in range(len(floors) - 1)
            )
        )
        self.assertTrue(
            all(
                ratios[index + 1] > ratios[index]
                for index in range(len(ratios) - 1)
            )
        )
        self.assertGreater(ratios[-1], 1.0)

    def test_last_hitting_gives_one_quarter_of_entrance_threshold(self):
        self.assertEqual(
            historical_flux_from_last_hitting(
                entrance_threshold=8.0,
            ),
            2.0,
        )
        self.assertEqual(
            historical_flux_from_last_hitting(
                entrance_threshold=8.0,
                dissipation=3.0,
            ),
            5.0,
        )

    def test_application_constants_are_nu_T_over_eight(self):
        result = inherited_ancestry_certificate(
            sigma=1.0e-10,
            h=1.0e-3,
            viscosity=2.0,
            fixed_time_enstrophy=5.0,
            coefficient=0.5,
            multiplier_bound=2.0,
            kappa=1.0,
            farther_factor=2.0,
        )
        self.assertEqual(
            result.inherited_threshold,
            2.0 * result.sharp_floor / 2.0,
        )
        self.assertEqual(
            result.historical_flux_floor,
            2.0 * result.sharp_floor / 8.0,
        )
        self.assertTrue(result.fixed_time_inheritance_excluded)

    def test_squeezed_annulus_gives_nu_T_over_four(self):
        self.assertEqual(
            squeezed_terminal_flux_floor(
                viscosity=3.0,
                sharp_floor=8.0,
            ),
            6.0,
        )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            fixed_time_tail_upper(enstrophy=-1.0, cutoff=1.0)
        with self.assertRaises(ValueError):
            fixed_time_tail_upper(enstrophy=1.0, cutoff=0.0)
        with self.assertRaises(ValueError):
            farther_parabolic_cutoff(
                sigma=1.0,
                h=1.0,
                farther_factor=1.0,
            )
        with self.assertRaises(ValueError):
            historical_flux_from_last_hitting(
                entrance_threshold=0.0,
            )
        with self.assertRaises(ValueError):
            squeezed_terminal_flux_floor(
                viscosity=1.0,
                sharp_floor=0.0,
            )
        with self.assertRaises(ValueError):
            inherited_ancestry_certificate(
                sigma=1.0,
                h=1.0,
                viscosity=0.0,
                fixed_time_enstrophy=1.0,
            )


if __name__ == "__main__":
    unittest.main()
