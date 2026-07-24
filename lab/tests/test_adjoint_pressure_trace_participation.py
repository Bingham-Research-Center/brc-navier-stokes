import math
import unittest

from navier_lab.adjoint_pressure_trace_participation import (
    balanced_scales,
    bulk_participation_floor,
    cell_layer_units,
    charged_window_volume_floor,
    density_split_capture_modulus,
    finite_band_l2_squared_ceiling,
    mean_source_duty_time,
    modular_window_volume_ceiling,
    moving_high_density_capture,
    optimal_density_threshold,
    optimised_capture_modulus,
    rejected_moving_tube_ledger,
    source_participation_fraction,
)


class AdjointPressureTraceParticipationTests(unittest.TestCase):
    def test_finite_band_l2_squared_is_linear_in_layer_time(self):
        first = finite_band_l2_squared_ceiling(1.0e-3)
        second = finite_band_l2_squared_ceiling(1.0e-6)
        self.assertTrue(math.isclose(second, first * 1.0e-3))

    def test_balanced_source_and_cell_powers_are_exact(self):
        h = 1.0e-4
        scales = balanced_scales(h)
        self.assertTrue(
            math.isclose(scales["source_cells"], h ** (-21.0 / 2.0))
        )
        self.assertTrue(
            math.isclose(scales["source_cylinder_volume"], h**-8)
        )
        self.assertTrue(
            math.isclose(scales["cell_layer_volume"], h ** (5.0 / 2.0))
        )

    def test_window_volume_lies_between_inverse_one_and_inverse_eight(self):
        for h in (1.0e-2, 1.0e-4, 1.0e-6):
            lower = charged_window_volume_floor(
                signed_charge=1.0,
                window_ceiling=1.0,
                pressure_l2_squared=h,
            )
            upper = modular_window_volume_ceiling(
                layer_time=h,
                regularisation=h**9,
                regularised_mass=1.0,
                modular_floor=1.0,
            )
            self.assertTrue(math.isclose(lower, h**-1))
            self.assertTrue(math.isclose(upper, h**-8))

    def test_l2_preliminary_participation_has_old_h7_power(self):
        h = 1.0e-4
        scales = balanced_scales(h)
        volume = h**-1
        self.assertTrue(
            math.isclose(
                source_participation_fraction(
                    volume,
                    h,
                    scales["source_radius"],
                ),
                h**7,
            )
        )
        self.assertTrue(
            math.isclose(
                mean_source_duty_time(
                    volume,
                    scales["source_radius"],
                ),
                h**8,
            )
        )
        self.assertTrue(
            math.isclose(
                cell_layer_units(
                    volume,
                    h,
                    scales["descendant_length"],
                ),
                h ** (-7.0 / 2.0),
            )
        )

    def test_variable_count_capture_cancels_every_layer_time_power(self):
        for h in (1.0e-2, 1.0e-4, 1.0e-6):
            scales = balanced_scales(h)
            participation = h**3
            threshold = h
            direct = (
                h ** (3.0 / 2.0)
                * (
                    scales["wavenumber"]
                    * h
                    * (
                        participation
                        * scales["source_cells"]
                        / threshold
                    ) ** (1.0 / 3.0)
                ) ** 0.5
            )
            reduced = moving_high_density_capture(
                participation,
                threshold,
            )
            self.assertTrue(math.isclose(direct, reduced))

    def test_density_split_optimises_to_one_seventh_modulus(self):
        for participation in (1.0e-7, 1.0e-14, 1.0e-28):
            threshold = optimal_density_threshold(participation)
            self.assertTrue(
                math.isclose(threshold, participation ** (1.0 / 7.0))
            )
            self.assertTrue(
                math.isclose(
                    density_split_capture_modulus(
                        participation,
                        threshold,
                    ),
                    2.0 * participation ** (1.0 / 7.0),
                )
            )
            self.assertTrue(
                math.isclose(
                    optimised_capture_modulus(participation),
                    2.0 * participation ** (1.0 / 7.0),
                )
            )

    def test_fixed_charge_forces_fixed_source_participation(self):
        floor = bulk_participation_floor(
            signed_charge=0.25,
            window_ceiling=2.0,
            capture_modulus_constant=4.0,
        )
        self.assertTrue(math.isclose(floor, (0.25 / 8.0) ** 7))

    def test_rejected_moving_tube_keeps_scalar_ledgers(self):
        for h in (1.0e-2, 1.0e-4, 1.0e-6):
            ledger = rejected_moving_tube_ledger(h)
            self.assertTrue(
                math.isclose(ledger["duty_fraction"], h**7)
            )
            self.assertTrue(
                math.isclose(ledger["physical_duty_time"], h**8)
            )
            self.assertTrue(
                math.isclose(ledger["pressure_amplitude_scale"], h)
            )
            self.assertTrue(
                math.isclose(ledger["total_pressure_mass"], 1.0)
            )
            self.assertTrue(
                math.isclose(
                    ledger["total_pressure_l2_squared"],
                    (4.0 / 3.0) * h,
                )
            )
            self.assertTrue(
                math.isclose(ledger["window_spacetime_volume"], h**-1)
            )
            self.assertTrue(
                math.isclose(
                    ledger["cell_layer_participation"],
                    h ** (-7.0 / 2.0),
                )
            )

    def test_moving_selector_rejects_the_old_tube(self):
        previous_ratio = 0.0
        for h in (1.0e-2, 1.0e-4, 1.0e-6):
            ledger = rejected_moving_tube_ledger(h)
            self.assertTrue(
                math.isclose(
                    ledger["active_cells_each_time"],
                    h ** (-7.0 / 2.0),
                )
            )
            self.assertTrue(
                math.isclose(
                    ledger["moving_selector_capture_ceiling"],
                    h ** (7.0 / 6.0),
                )
            )
            self.assertGreater(
                ledger["total_pressure_mass"],
                ledger["moving_selector_capture_ceiling"],
            )
            self.assertGreater(
                ledger["capture_violation_ratio"],
                previous_ratio,
            )
            previous_ratio = ledger["capture_violation_ratio"]

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            balanced_scales(0.0)
        with self.assertRaises(ValueError):
            finite_band_l2_squared_ceiling(-1.0)
        with self.assertRaises(ValueError):
            charged_window_volume_floor(1.0, 0.0, 1.0)
        with self.assertRaises(ValueError):
            modular_window_volume_ceiling(1.0, 0.0, 1.0, 1.0)
        with self.assertRaises(ValueError):
            source_participation_fraction(1.0, 1.0, 0.0)
        with self.assertRaises(ValueError):
            moving_high_density_capture(1.0, 2.0)
        with self.assertRaises(ValueError):
            density_split_capture_modulus(0.0, 0.5)
        with self.assertRaises(ValueError):
            bulk_participation_floor(1.0, 1.0, 0.0)


if __name__ == "__main__":
    unittest.main()
