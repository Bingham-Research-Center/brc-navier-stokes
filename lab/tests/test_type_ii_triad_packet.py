from fractions import Fraction
import unittest

from navier_lab.type_ii_triad_packet import (
    ZERO,
    band_energy_pairing,
    closed_triad_flux,
    convolution_triad_flux,
    dyadic_heat_band_multipliers,
    is_divergence_free,
    packet_radius_powers,
    packet_scaling,
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
