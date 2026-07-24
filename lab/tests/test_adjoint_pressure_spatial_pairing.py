import math
import unittest

from navier_lab.adjoint_pressure_spatial_pairing import (
    beltrami_current_ledger,
    paired_coefficient_budget,
    pressure_history_from_gradient,
    reciprocal_amplitudes,
)


class AdjointPressureSpatialPairingTests(unittest.TestCase):
    def test_reciprocal_amplitudes_have_constant_product(self):
        for time in (0.0, 0.1, 0.7):
            alpha, beta = reciprocal_amplitudes(
                time,
                viscosity=0.6,
                frequency=4.0,
                primal_amplitude=2.5,
                adjoint_amplitude=1.7,
            )
            self.assertAlmostEqual(alpha * beta, 2.5 * 1.7)

    def test_viscous_wronskian_vanishes_exactly(self):
        ledger = beltrami_current_ledger(
            0.4,
            viscosity=0.8,
            frequency=2.0,
            primal_amplitude=3.0,
            adjoint_amplitude=5.0,
        )
        self.assertEqual(ledger.viscous_wronskian, 0.0)

    def test_displayed_gauge_pressure_flux_cancels_transport_pointwise(self):
        for time in (0.0, 0.2, 0.9):
            ledger = beltrami_current_ledger(
                time,
                viscosity=0.4,
                frequency=1.5,
                primal_amplitude=2.0,
                adjoint_amplitude=3.0,
            )
            self.assertAlmostEqual(
                ledger.adjoint_pressure + ledger.primal_pressure,
                -ledger.transport,
            )
            self.assertAlmostEqual(ledger.total_w_u, 0.0)

    def test_each_pressure_flux_is_half_the_cancelled_transport(self):
        ledger = beltrami_current_ledger(
            0.3,
            viscosity=1.0,
            frequency=2.0,
            primal_amplitude=-2.0,
            adjoint_amplitude=3.0,
        )
        self.assertAlmostEqual(
            ledger.adjoint_pressure,
            -0.5 * ledger.transport,
        )
        self.assertAlmostEqual(
            ledger.primal_pressure,
            -0.5 * ledger.transport,
        )

    def test_pressure_history_is_positive_while_current_is_zero(self):
        ledger = beltrami_current_ledger(
            0.2,
            viscosity=1.0,
            frequency=3.0,
            primal_amplitude=2.0,
            adjoint_amplitude=5.0,
        )
        history = pressure_history_from_gradient(
            0.5,
            32.0 * math.pi * 3.0,
            primal_amplitude=2.0,
            adjoint_amplitude=5.0,
        )
        self.assertEqual(ledger.total_w_u, 0.0)
        self.assertGreater(history, 0.0)

    def test_paired_budget_diverges_with_frequency_index(self):
        budgets = [
            paired_coefficient_budget(
                index,
                0.01,
                viscosity=0.2,
                primal_amplitude=1.0,
            )
            for index in (1, 5, 10)
        ]
        energies = [budget[0] for budget in budgets]
        dissipations = [budget[1] for budget in budgets]
        self.assertTrue(
            all(
                energies[index] < energies[index + 1]
                for index in range(len(energies) - 1)
            )
        )
        self.assertTrue(
            all(
                dissipations[index] < dissipations[index + 1]
                for index in range(len(dissipations) - 1)
            )
        )

    def test_paired_budget_has_exact_zero_horizon_limit(self):
        energy, dissipation = paired_coefficient_budget(
            2,
            1.0e-12,
            viscosity=0.7,
            primal_amplitude=1.3,
        )
        expected_energy = 2.0 * (2.0 * math.pi) ** 3 * 1.3**2
        self.assertAlmostEqual(energy, expected_energy, places=7)
        self.assertGreaterEqual(dissipation, 0.0)

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            reciprocal_amplitudes(
                -1.0,
                viscosity=1.0,
                frequency=1.0,
                primal_amplitude=1.0,
                adjoint_amplitude=1.0,
            )
        with self.assertRaises(ValueError):
            reciprocal_amplitudes(
                0.0,
                viscosity=0.0,
                frequency=1.0,
                primal_amplitude=1.0,
                adjoint_amplitude=1.0,
            )
        with self.assertRaises(ValueError):
            pressure_history_from_gradient(0.0, 1.0)
        with self.assertRaises(ValueError):
            pressure_history_from_gradient(1.0, 0.0)
        with self.assertRaises(ValueError):
            paired_coefficient_budget(0, 1.0)


if __name__ == "__main__":
    unittest.main()
