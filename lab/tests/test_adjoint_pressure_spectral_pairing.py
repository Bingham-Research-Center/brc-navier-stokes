from fractions import Fraction
import math
import unittest

from navier_lab.adjoint_pressure_spectral_pairing import (
    beltrami_amplitudes,
    beltrami_pressure_gradient,
    beltrami_pressure_potential,
    beltrami_velocity,
    helical_invariant_residuals,
    localised_pairing_commutator_flux,
    localised_pairing_derivative,
    paired_beltrami_pressure_potential,
    paired_beltrami_velocity,
    paired_low_pressure_coefficient,
    paired_low_pressure_history_l1_lower_bound,
    paired_lowpass_gap,
    paired_wavevectors,
    pressure_history_l1_lower_bound,
    radial_spectral_gap,
    telescoping_increment,
)


class AdjointPressureSpectralPairingTests(unittest.TestCase):
    def setUp(self):
        self.projector = (
            (Fraction(1), Fraction(0), Fraction(0)),
            (Fraction(0), Fraction(1), Fraction(0)),
            (Fraction(0), Fraction(0), Fraction(0)),
        )
        self.transport = (
            (Fraction(0), Fraction(-1), Fraction(2)),
            (Fraction(1), Fraction(0), Fraction(-3)),
            (Fraction(-2), Fraction(3), Fraction(0)),
        )
        self.laplacian = (
            (Fraction(-1), Fraction(0), Fraction(0)),
            (Fraction(0), Fraction(-2), Fraction(0)),
            (Fraction(0), Fraction(0), Fraction(-3)),
        )
        self.adjoint = (
            Fraction(2),
            Fraction(-1),
            Fraction(4),
        )
        self.coefficient = (
            Fraction(3),
            Fraction(5),
            Fraction(-2),
        )

    def test_localised_pairing_is_exactly_the_transport_commutator(self):
        derivative = localised_pairing_derivative(
            adjoint=self.adjoint,
            coefficient=self.coefficient,
            projector=self.projector,
            transport=self.transport,
            laplacian=self.laplacian,
            adjoint_pressure_gradient=(
                Fraction(5),
                Fraction(-3),
                Fraction(0),
            ),
            primal_pressure_gradient=(
                Fraction(1),
                Fraction(2),
                Fraction(0),
            ),
            viscosity=Fraction(5, 3),
        )
        flux = localised_pairing_commutator_flux(
            adjoint=self.adjoint,
            coefficient=self.coefficient,
            projector=self.projector,
            transport=self.transport,
        )
        self.assertEqual(derivative, flux)

    def test_nonzero_projected_pressure_has_zero_pairing_contribution(self):
        common = {
            "adjoint": self.adjoint,
            "coefficient": self.coefficient,
            "projector": self.projector,
            "transport": self.transport,
            "laplacian": self.laplacian,
            "viscosity": Fraction(1),
        }
        zero_pressure = localised_pairing_derivative(
            **common,
            adjoint_pressure_gradient=(
                Fraction(0),
                Fraction(0),
                Fraction(0),
            ),
            primal_pressure_gradient=(
                Fraction(0),
                Fraction(0),
                Fraction(0),
            ),
        )
        huge_pressure = localised_pairing_derivative(
            **common,
            adjoint_pressure_gradient=(
                Fraction(5 * 10**12),
                Fraction(-3 * 10**12),
                Fraction(0),
            ),
            primal_pressure_gradient=(
                Fraction(10**15),
                Fraction(2 * 10**15),
                Fraction(0),
            ),
        )
        self.assertEqual(huge_pressure, zero_pressure)

    def test_pairing_shell_increments_telescope_exactly(self):
        values = (
            Fraction(11, 7),
            Fraction(-3, 5),
            Fraction(2, 9),
            Fraction(17, 13),
        )
        self.assertEqual(
            telescoping_increment(values),
            values[-1] - values[0],
        )

    def test_beltrami_pressure_potential_is_half_velocity_square(self):
        for x, y in ((0.0, 0.0), (0.4, -0.7), (1.2, 2.1)):
            velocity = beltrami_velocity(x, y, frequency=3)
            half_square = 0.5 * sum(
                component * component
                for component in velocity
            )
            self.assertAlmostEqual(
                half_square,
                beltrami_pressure_potential(x, y, frequency=3),
            )

    def test_primal_and_adjoint_amplitudes_have_constant_product(self):
        for time in (0.0, 0.1, 0.7, 2.0):
            primal, adjoint = beltrami_amplitudes(
                time,
                viscosity=0.6,
                frequency=4,
                primal_amplitude=2.5,
                adjoint_amplitude=1.7,
            )
            self.assertAlmostEqual(primal * adjoint, 2.5 * 1.7)

    def test_adjoint_pressure_gradient_is_time_independent_and_nonzero(self):
        gradient = beltrami_pressure_gradient(
            0.0,
            0.0,
            primal_amplitude=2.0,
            adjoint_amplitude=3.0,
            frequency=5,
        )
        self.assertEqual(gradient, (-30.0, 0.0, 0.0))
        self.assertGreater(
            pressure_history_l1_lower_bound(
                0.4,
                primal_amplitude=2.0,
                adjoint_amplitude=3.0,
                frequency=5,
            ),
            0.0,
        )

    def test_pressure_occupies_a_gap_above_the_solenoidal_pair(self):
        frequency = 7
        cutoff = 1.2 * frequency
        pair_high, pressure_high = radial_spectral_gap(
            cutoff,
            frequency=frequency,
        )
        self.assertFalse(pair_high)
        self.assertTrue(pressure_high)
        self.assertLess(cutoff, math.sqrt(2.0) * frequency)

    def test_pressure_history_lower_bound_has_exact_scaling(self):
        value = pressure_history_l1_lower_bound(
            0.25,
            primal_amplitude=2.0,
            adjoint_amplitude=-3.0,
            frequency=4,
        )
        self.assertAlmostEqual(
            value,
            32.0 * math.pi * 0.25 * 6.0 * 4,
        )

    def test_paired_wavevectors_have_equal_radius_and_fixed_difference(self):
        for index in (1, 5, 50):
            first, second, radius = paired_wavevectors(index)
            self.assertEqual(
                tuple(
                    second[axis] - first[axis]
                    for axis in range(3)
                ),
                (1, 1, 0),
            )
            self.assertAlmostEqual(
                sum(component * component for component in first),
                radius * radius,
            )
            self.assertAlmostEqual(
                sum(component * component for component in second),
                radius * radius,
            )
            self.assertTrue(
                all(
                    abs(residual) < 1.0e-12
                    for residual in helical_invariant_residuals(first)
                )
            )
            self.assertTrue(
                all(
                    abs(residual) < 1.0e-12
                    for residual in helical_invariant_residuals(second)
                )
            )

    def test_paired_pressure_potential_is_half_velocity_square(self):
        for index in (1, 4, 17):
            for x, y in ((0.0, 0.0), (0.3, -0.8), (1.1, 2.2)):
                velocity = paired_beltrami_velocity(index, x, y)
                half_square = 0.5 * sum(
                    component * component
                    for component in velocity
                )
                self.assertAlmostEqual(
                    half_square,
                    paired_beltrami_pressure_potential(
                        index,
                        x,
                        y,
                    ),
                )

    def test_fixed_low_pressure_return_survives_arbitrarily_high_pair(self):
        coefficients = []
        for index in (2, 20, 200):
            _, _, radius = paired_wavevectors(index)
            cutoff = 2.0
            pair_low, pressure_low = paired_lowpass_gap(
                cutoff,
                index=index,
            )
            self.assertLess(math.sqrt(2.0), cutoff)
            self.assertLess(cutoff, radius)
            self.assertFalse(pair_low)
            self.assertTrue(pressure_low)
            coefficients.append(paired_low_pressure_coefficient(index))
        self.assertTrue(
            all(
                coefficients[position + 1] > coefficients[position]
                for position in range(len(coefficients) - 1)
            )
        )
        self.assertGreater(coefficients[-1], 0.99999)

    def test_fixed_low_pressure_history_has_uniform_positive_floor(self):
        values = [
            paired_low_pressure_history_l1_lower_bound(
                0.5,
                index=index,
                primal_amplitude=2.0,
                adjoint_amplitude=3.0,
            )
            for index in (1, 10, 100)
        ]
        self.assertTrue(all(value > 0.0 for value in values))
        self.assertGreater(values[0], 20.0 * math.pi**2)
        self.assertGreater(values[-1], values[0])

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            beltrami_velocity(0.0, 0.0, frequency=0)
        with self.assertRaises(ValueError):
            beltrami_amplitudes(-1.0)
        with self.assertRaises(ValueError):
            pressure_history_l1_lower_bound(0.0)
        with self.assertRaises(ValueError):
            radial_spectral_gap(0.0)
        with self.assertRaises(ValueError):
            paired_wavevectors(0)
        with self.assertRaises(ValueError):
            paired_lowpass_gap(0.0, index=1)
        with self.assertRaises(ValueError):
            paired_low_pressure_history_l1_lower_bound(
                0.0,
                index=1,
            )
        with self.assertRaises(ValueError):
            telescoping_increment(())
        with self.assertRaises(ValueError):
            localised_pairing_derivative(
                adjoint=self.adjoint,
                coefficient=self.coefficient,
                projector=self.projector,
                transport=self.transport,
                laplacian=self.laplacian,
                adjoint_pressure_gradient=(Fraction(0),) * 3,
                primal_pressure_gradient=(Fraction(0),) * 3,
                viscosity=Fraction(0),
            )


if __name__ == "__main__":
    unittest.main()
