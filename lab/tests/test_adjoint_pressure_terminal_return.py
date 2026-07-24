import unittest
from fractions import Fraction

from navier_lab.adjoint_pressure_terminal_return import (
    critical_drift_amplitude,
    critical_drift_gradient_l2_squared,
    critical_drift_l2_squared,
    critical_packet_volume,
    critical_pressure_squared,
    critical_tensor_l1_squared,
    energy_normalised_state_amplitude,
    energy_normalised_state_l2_squared,
    minimum_volume_for_l1_mass_and_l2_ceiling,
    physical_dissipation_charge,
    physical_tail_charge_power,
    pressure_ceiling_squared,
    required_band_dissipation,
    terminal_layer_physical_charge,
    terminal_layer_required_dissipation_exponent,
    zeno_state_l2_squared,
)


class AdjointPressureTerminalReturnTests(unittest.TestCase):
    def test_squared_pressure_ceiling_has_exact_scale_ratio(self):
        self.assertEqual(
            pressure_ceiling_squared(2, 32, 3, 5, 7),
            Fraction(525, 256),
        )

    def test_required_dissipation_exactly_inverts_the_ceiling(self):
        pressure = Fraction(3, 5)
        output = Fraction(2)
        input_floor = Fraction(32)
        horizon = Fraction(7, 3)
        state = Fraction(11, 4)
        constant = Fraction(5, 2)
        dissipation = required_band_dissipation(
            pressure,
            output,
            input_floor,
            horizon,
            state,
            constant,
        )
        self.assertEqual(
            pressure_ceiling_squared(
                output,
                input_floor,
                horizon,
                state,
                dissipation,
                constant,
            ),
            pressure**2,
        )

    def test_energy_normalised_state_packet_has_unit_l2_square(self):
        for frequency in (1, 2, 8, 64, 1024):
            self.assertEqual(
                energy_normalised_state_amplitude(frequency),
                frequency**3,
            )
            self.assertEqual(
                energy_normalised_state_l2_squared(frequency),
                1,
            )

    def test_critical_drift_packet_ledgers(self):
        for frequency in (1, 2, 8, 64, 1024):
            self.assertEqual(critical_packet_volume(frequency), Fraction(1, frequency**3))
            self.assertEqual(critical_drift_amplitude(frequency), frequency)
            self.assertEqual(
                critical_drift_l2_squared(frequency),
                Fraction(1, frequency),
            )
            self.assertEqual(
                critical_drift_gradient_l2_squared(frequency),
                frequency,
            )

    def test_critical_packet_saturates_the_frequency_power(self):
        for output in (1, 3, 9):
            for frequency in (2, 8, 32, 128):
                expected = Fraction(output**2, frequency)
                self.assertEqual(
                    critical_tensor_l1_squared(frequency),
                    Fraction(1, frequency),
                )
                self.assertEqual(
                    critical_pressure_squared(output, frequency),
                    expected,
                )
                self.assertEqual(
                    pressure_ceiling_squared(
                        output,
                        frequency,
                        1,
                        1,
                        frequency,
                    ),
                    expected,
                )

    def test_zeno_localisation_violates_uniform_state_energy(self):
        for frequency in (2, 4, 16, 256):
            self.assertEqual(zeno_state_l2_squared(frequency), frequency)
            self.assertEqual(
                minimum_volume_for_l1_mass_and_l2_ceiling(
                    Fraction(1, frequency),
                    1,
                ),
                Fraction(1, frequency**2),
            )
            self.assertGreater(
                Fraction(1, frequency**2),
                critical_packet_volume(frequency),
            )

    def test_unit_return_forces_quadratic_band_dissipation(self):
        for frequency in (2, 4, 16, 256):
            self.assertEqual(
                required_band_dissipation(
                    1,
                    1,
                    frequency,
                    1,
                    1,
                ),
                frequency**2,
            )

    def test_parabolic_pullback_multiplies_dissipation_by_event_scale(self):
        self.assertEqual(
            physical_dissipation_charge(Fraction(1, 32), 1024),
            32,
        )

    def test_terminal_layer_physical_charge_retains_every_factor(self):
        self.assertEqual(
            terminal_layer_physical_charge(
                Fraction(1, 64),
                8,
                Fraction(1, 4),
            ),
            64,
        )
        self.assertEqual(
            terminal_layer_physical_charge(
                Fraction(1, 64),
                8,
                Fraction(1, 4),
                pressure_floor=2,
                output_frequency=3,
                state_l2_constant=5,
                multiplier_constant=7,
            ),
            Fraction(256, 11025),
        )

    def test_terminal_layer_power_ledger(self):
        self.assertEqual(
            terminal_layer_required_dissipation_exponent(1, 1, 0),
            3,
        )
        self.assertEqual(
            terminal_layer_required_dissipation_exponent(
                1,
                1,
                Fraction(7, 4),
            ),
            Fraction(13, 2),
        )
        self.assertEqual(
            physical_tail_charge_power(
                Fraction(13, 2),
                1,
                1,
                Fraction(7, 4),
            ),
            0,
        )
        self.assertEqual(
            physical_tail_charge_power(
                7,
                1,
                1,
                Fraction(7, 4),
            ),
            Fraction(1, 2),
        )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            pressure_ceiling_squared(0, 2, 1, 1, 1)
        with self.assertRaises(ValueError):
            pressure_ceiling_squared(1, 2, -1, 1, 1)
        with self.assertRaises(ValueError):
            required_band_dissipation(1, 1, 2, 0, 1)
        with self.assertRaises(ValueError):
            critical_packet_volume(True)
        with self.assertRaises(ValueError):
            minimum_volume_for_l1_mass_and_l2_ceiling(1, 0)
        with self.assertRaises(ValueError):
            terminal_layer_physical_charge(1, 2, 0)


if __name__ == "__main__":
    unittest.main()
