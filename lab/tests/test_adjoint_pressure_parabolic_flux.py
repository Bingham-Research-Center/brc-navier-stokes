from fractions import Fraction
import unittest

from navier_lab.adjoint_pressure_parabolic_flux import (
    ANNULUS_BRANCH,
    FLUX_BRANCH,
    INHERITED_BRANCH,
    geometric_shell_cascade,
    near_lossless_retention,
    physical_cutoff,
    physical_interval_length,
    physical_tail_floor,
    sharp_tail_floor,
    signed_high_pass_input,
    tail_flux_alternative,
    zeno_heat_time,
)


class AdjointPressureParabolicFluxTests(unittest.TestCase):
    def test_smooth_multiplier_floor_converts_to_sharp_tail(self):
        self.assertEqual(sharp_tail_floor(18.0, 3.0), 2.0)

    def test_high_pass_energy_identity_has_the_signed_input_convention(self):
        self.assertEqual(
            signed_high_pass_input(
                viscosity=2.0,
                dissipation=5.0,
                incoming_energy=7.0,
                outgoing_energy=3.0,
            ),
            8.0,
        )

    def test_each_tail_flux_branch_is_exhaustive(self):
        common = {
            "smooth_tail_floor": 4.0,
            "multiplier_bound": 1.0,
            "viscosity": 2.0,
        }
        annulus = tail_flux_alternative(
            **common,
            annular_dissipation=2.0,
            far_dissipation=2.0,
            incoming_energy=0.0,
            outgoing_energy=0.0,
        )
        inherited = tail_flux_alternative(
            **common,
            annular_dissipation=1.0,
            far_dissipation=3.0,
            incoming_energy=4.0,
            outgoing_energy=0.0,
        )
        flux = tail_flux_alternative(
            **common,
            annular_dissipation=1.0,
            far_dissipation=3.0,
            incoming_energy=3.0,
            outgoing_energy=0.0,
        )
        self.assertEqual(annulus.branch, ANNULUS_BRANCH)
        self.assertEqual(inherited.branch, INHERITED_BRANCH)
        self.assertEqual(flux.branch, FLUX_BRANCH)
        self.assertGreaterEqual(
            flux.signed_flux,
            flux.signed_flux_threshold,
        )

    def test_flux_floor_is_one_quarter_of_viscous_sharp_floor(self):
        result = tail_flux_alternative(
            smooth_tail_floor=16.0,
            multiplier_bound=2.0,
            annular_dissipation=1.9,
            far_dissipation=2.1,
            incoming_energy=2.9,
            outgoing_energy=0.0,
            viscosity=1.5,
        )
        self.assertEqual(result.branch, FLUX_BRANCH)
        self.assertAlmostEqual(result.sharp_floor, 4.0)
        self.assertAlmostEqual(result.signed_flux_threshold, 1.5)
        self.assertGreater(result.signed_flux, 1.5)

    def test_physical_parabolic_phase_is_exact(self):
        sigma = 2.0e-5
        h = 3.0e-4
        kappa = 1.7
        cutoff = physical_cutoff(
            sigma=sigma,
            h=h,
            kappa=kappa,
        )
        duration = physical_interval_length(sigma=sigma, h=h)
        self.assertAlmostEqual(cutoff * cutoff * duration, kappa**2)
        self.assertAlmostEqual(
            physical_tail_floor(
                sigma=sigma,
                h=h,
                coefficient=2.5,
            ),
            2.5 * sigma * h ** (-3.0),
        )

    def test_shell_cascade_satisfies_every_energy_balance_exactly(self):
        ledger = geometric_shell_cascade(
            9,
            input_flux=Fraction(7, 5),
            retention=Fraction(4, 5),
        )
        self.assertTrue(
            all(
                residual == 0
                for residual in ledger.shell_balance_residuals()
            )
        )
        self.assertTrue(
            all(
                residual == 0
                for residual in ledger.cumulative_residuals()
            )
        )
        self.assertEqual(
            sum(ledger.viscous_costs, start=Fraction(0)),
            ledger.input_flux,
        )
        self.assertEqual(
            sum(ledger.energy_changes, start=Fraction(0)) / 2
            + sum(ledger.viscous_costs, start=Fraction(0)),
            0,
        )

    def test_each_boundary_flux_is_the_same_cumulative_tail_payment(self):
        ledger = geometric_shell_cascade(
            7,
            input_flux=Fraction(11, 13),
            retention=Fraction(9, 10),
        )
        for boundary, flux in enumerate(ledger.boundary_fluxes):
            self.assertEqual(
                ledger.cumulative_tail_cost(boundary),
                flux,
            )

    def test_near_lossless_arbitrary_depth_concentrates_at_the_top(self):
        fractions = []
        intermediate_losses = []
        for depth in (10, 100, 1000):
            ledger = geometric_shell_cascade(
                depth,
                retention=near_lossless_retention(depth),
            )
            top_fraction = float(
                ledger.viscous_costs[-1] / ledger.input_flux
            )
            fractions.append(top_fraction)
            intermediate_losses.append(1.0 - top_fraction)
        self.assertTrue(
            all(
                fractions[index + 1] > fractions[index]
                for index in range(len(fractions) - 1)
            )
        )
        self.assertLess(intermediate_losses[-1], 0.0011)
        self.assertGreater(fractions[-1], 0.9989)

    def test_dyadic_zeno_clocks_fit_inside_unit_viscosity_event(self):
        sigma = 3.0e-6
        h = 2.0e-5
        kappa = 1.25
        cutoff = physical_cutoff(
            sigma=sigma,
            h=h,
            kappa=kappa,
        )
        duration = physical_interval_length(sigma=sigma, h=h)
        infinite_time = zeno_heat_time(base_frequency=cutoff)
        finite_time = zeno_heat_time(
            base_frequency=cutoff,
            depth=12,
        )
        self.assertAlmostEqual(
            infinite_time / duration,
            1.0 / (3.0 * kappa**2),
        )
        self.assertLess(finite_time, infinite_time)
        self.assertLess(infinite_time, duration)

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            sharp_tail_floor(0.0)
        with self.assertRaises(ValueError):
            signed_high_pass_input(
                viscosity=1.0,
                dissipation=-1.0,
                incoming_energy=0.0,
                outgoing_energy=0.0,
            )
        with self.assertRaises(ValueError):
            tail_flux_alternative(
                smooth_tail_floor=2.0,
                multiplier_bound=1.0,
                annular_dissipation=0.2,
                far_dissipation=0.3,
                incoming_energy=0.0,
                outgoing_energy=0.0,
                viscosity=1.0,
            )
        with self.assertRaises(ValueError):
            geometric_shell_cascade(0)
        with self.assertRaises(ValueError):
            geometric_shell_cascade(2, retention=Fraction(1))
        with self.assertRaises(ValueError):
            near_lossless_retention(1)
        with self.assertRaises(ValueError):
            zeno_heat_time(base_frequency=1.0, ratio=1.0)
        with self.assertRaises(ValueError):
            zeno_heat_time(base_frequency=1.0, depth=0)


if __name__ == "__main__":
    unittest.main()
