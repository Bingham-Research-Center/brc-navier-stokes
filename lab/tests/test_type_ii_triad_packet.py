from fractions import Fraction
import unittest

from navier_lab.type_ii_triad_packet import (
    ZERO,
    band_energy_pairing,
    closed_triad_flux,
    closed_pell_two_shell_flux,
    convolution_triad_flux,
    dyadic_heat_band_multipliers,
    is_divergence_free,
    packet_radius_powers,
    packet_scaling,
    pell_profile_limit_coefficient,
    pell_solutions,
    pell_two_shell_flux_coefficients,
    pell_two_shell_modes,
    shell_flux_coefficients,
    triad_fourier_modes,
)


class TypeIITriadPacketTests(unittest.TestCase):
    def test_all_six_fourier_modes_are_divergence_free(self) -> None:
        modes = triad_fourier_modes()
        self.assertEqual(len(modes), 6)
        for wave, coefficient in modes.items():
            self.assertTrue(is_divergence_free(wave, coefficient))
            self.assertNotEqual(coefficient, (ZERO, ZERO, ZERO))

    def test_dyadic_heat_band_multipliers_are_exact(self) -> None:
        self.assertEqual(
            dyadic_heat_band_multipliers(),
            {
                1: Fraction(1, 4),
                4: Fraction(15, 256),
                5: Fraction(31, 1024),
            },
        )

    def test_convolution_recovers_closed_triad_flux(self) -> None:
        multipliers = dyadic_heat_band_multipliers()
        self.assertEqual(
            convolution_triad_flux(multipliers),
            closed_triad_flux(multipliers),
        )

    def test_explicit_gaussian_band_flux_is_nonzero(self) -> None:
        flux = convolution_triad_flux(dyadic_heat_band_multipliers())
        self.assertEqual(flux, Fraction(-109, 2048))
        self.assertNotEqual(flux, 0)

    def test_gaussian_band_pairing_is_strictly_positive(self) -> None:
        pairing = band_energy_pairing(dyadic_heat_band_multipliers())
        self.assertEqual(pairing, Fraction(651, 2048))
        self.assertGreater(pairing, 0)

    def test_pell_recurrence_generates_adjacent_shells(self) -> None:
        self.assertEqual(
            pell_solutions(4),
            ((2, 1), (7, 4), (26, 15), (97, 56)),
        )
        for n, m in pell_solutions(4):
            self.assertEqual(n * n - 3 * m * m, 1)
            shells = {
                sum(entry * entry for entry in wave)
                for wave in pell_two_shell_modes(n, m)
            }
            self.assertEqual(shells, {4 * m * m, 4 * m * m + 1})

    def test_pell_modes_are_divergence_free(self) -> None:
        for n, m in pell_solutions(3):
            modes = pell_two_shell_modes(n, m)
            self.assertEqual(len(modes), 6)
            for wave, coefficient in modes.items():
                self.assertTrue(is_divergence_free(wave, coefficient))

    def test_pell_convolution_has_exact_two_shell_transfer(self) -> None:
        for n, m in pell_solutions(3):
            lower_shell = 4 * m * m
            upper_shell = lower_shell + 1
            expected = {
                lower_shell: Fraction(n * m, 2),
                upper_shell: -Fraction(n * m, 2),
            }
            self.assertEqual(
                pell_two_shell_flux_coefficients(n, m),
                expected,
            )
            self.assertEqual(
                shell_flux_coefficients(pell_two_shell_modes(n, m)),
                expected,
            )
            multipliers = {
                lower_shell: Fraction(7, 11),
                upper_shell: Fraction(2, 11),
            }
            self.assertEqual(
                sum(
                    coefficient * multipliers[shell]
                    for shell, coefficient in expected.items()
                ),
                closed_pell_two_shell_flux(multipliers, n, m),
            )

    def test_pell_heat_profile_is_positive_and_has_zero_total_mass(self) -> None:
        for n, m in pell_solutions(4):
            coefficients = pell_two_shell_flux_coefficients(n, m)
            self.assertEqual(sum(coefficients.values()), 0)
            first_shell_moment = sum(
                shell * coefficient
                for shell, coefficient in coefficients.items()
            )
            self.assertEqual(first_shell_moment, -Fraction(n * m, 2))
            lower_shell = 4 * m * m
            upper_shell = lower_shell + 1
            self.assertGreater(
                Fraction(1, 2**lower_shell)
                - Fraction(1, 2**upper_shell),
                0,
            )

    def test_pell_profiles_converge_to_shell_derivative_coefficient(self) -> None:
        coefficients = [
            float(pell_profile_limit_coefficient(n, m))
            for n, m in pell_solutions(5)
        ]
        target = 3.0**0.5 / 8.0
        errors = [abs(value - target) for value in coefficients]
        self.assertTrue(
            all(next_error < error for error, next_error in zip(errors, errors[1:]))
        )
        self.assertLess(errors[-1], 1.0e-5)

    def test_invalid_pell_inputs_are_rejected(self) -> None:
        for values in ((1, 1), (2, 0), (-2, -1)):
            with self.assertRaises(ValueError):
                pell_two_shell_modes(*values)
            with self.assertRaises(ValueError):
                closed_pell_two_shell_flux({}, *values)
            with self.assertRaises(ValueError):
                pell_profile_limit_coefficient(*values)
        with self.assertRaises(ValueError):
            pell_solutions(-1)

    def test_fixed_energy_packet_powers_are_critical(self) -> None:
        self.assertEqual(
            packet_radius_powers(),
            {
                "velocity_amplitude": Fraction(-3, 2),
                "weak_l3": Fraction(-1, 2),
                "turnover_time": Fraction(5, 2),
                "nonlinear_work_rate": Fraction(-5, 2),
                "enstrophy": Fraction(-2),
                "integrated_nonlinear_work": Fraction(0),
                "viscous_dissipation": Fraction(1, 2),
                "effective_viscosity": Fraction(1, 2),
                "weak_l3_fourth_power_occupation": Fraction(1, 2),
            },
        )

    def test_packet_ledger_keeps_work_fixed_and_dissipation_small(self) -> None:
        radius = 2.0**-12
        ledger = packet_scaling(
            radius=radius,
            amplitude=3.0,
            viscosity=2.0,
        )
        self.assertAlmostEqual(
            ledger["integrated_nonlinear_work"],
            9.0,
        )
        self.assertAlmostEqual(
            ledger["viscous_dissipation"],
            6.0 * radius**0.5,
        )
        self.assertAlmostEqual(
            ledger["effective_viscosity"],
            2.0 * radius**0.5 / 3.0,
        )
        self.assertAlmostEqual(
            ledger["weak_l3_fourth_power_occupation"],
            27.0 * radius**0.5,
        )

    def test_invalid_packet_inputs_are_rejected(self) -> None:
        for values in (
            (0.0, 1.0, 1.0),
            (1.0, 0.0, 1.0),
            (1.0, 1.0, 0.0),
        ):
            with self.assertRaises(ValueError):
                packet_scaling(*values)


if __name__ == "__main__":
    unittest.main()
