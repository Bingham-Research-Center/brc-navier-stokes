import unittest
from fractions import Fraction

from navier_lab.adjoint_pressure_frequency_zeno import (
    dyadic_frequency,
    finite_energy_or_dissipation,
    heat_clock,
    heat_rate,
    hodge_gradient_projection,
    infinite_mean_zeno_clock,
    leray_projection,
    mean_zeno_clock,
    mean_zeno_clock_closed,
    observed_total_mass,
    output_trace_power,
    packet_dissipation,
    packet_energy,
    packet_enstrophy_rate,
    packet_volume,
    path_mass,
    pressure_cost_lower_bound,
    state_frequency,
    state_polarisation,
    terminal_drift_frequency,
    terminal_drift_polarisation,
    terminal_output_frequency,
    terminal_pressure_weight,
    terminal_transport_coefficient,
    uniform_pressure_cost_floor,
    upward_drift_frequency,
    upward_drift_polarisation,
    upward_transition_mass,
    upward_transport_coefficient,
    vector_add,
    vector_dot,
    vector_squared_norm,
    weak_l3_tail_charge,
)


class AdjointPressureFrequencyZenoTests(unittest.TestCase):
    def test_dyadic_heat_scales_are_exact(self):
        for level in range(1, 20):
            self.assertEqual(dyadic_frequency(level), 2**level)
            self.assertEqual(heat_rate(level), 4**level)
            self.assertEqual(heat_clock(level), Fraction(1, 4**level))

    def test_every_upward_transition_has_half_mass(self):
        for level in range(1, 20):
            self.assertEqual(upward_transition_mass(level), Fraction(1, 2))

    def test_terminal_pressure_exactly_cancels_path_mass(self):
        for depth in range(40):
            self.assertEqual(path_mass(depth), Fraction(1, 2**depth))
            self.assertEqual(terminal_pressure_weight(depth), 2**depth)
            self.assertEqual(observed_total_mass(depth), 1)

    def test_heat_clocks_form_a_finite_zeno_sum(self):
        for depth in range(40):
            self.assertEqual(
                mean_zeno_clock(depth),
                mean_zeno_clock_closed(depth),
            )
            self.assertLess(mean_zeno_clock(depth), Fraction(1, 3))
        self.assertEqual(infinite_mean_zeno_clock(), Fraction(1, 3))

    def test_constant_and_strong_trace_costs_persist_at_every_depth(self):
        for depth in range(1, 40):
            self.assertGreaterEqual(
                pressure_cost_lower_bound(depth, 0),
                Fraction(2, 3),
            )
            self.assertGreaterEqual(
                pressure_cost_lower_bound(depth, 1),
                Fraction(2, 9),
            )

    def test_every_fixed_algebraic_trace_order_has_a_positive_floor(self):
        for trace_order in range(12):
            floor = (
                Fraction(2, 3) ** (trace_order + 1)
                / (trace_order + 1)
            )
            self.assertEqual(
                uniform_pressure_cost_floor(trace_order),
                floor,
            )
            for depth in (1, 2, 5, 20):
                self.assertGreaterEqual(
                    pressure_cost_lower_bound(depth, trace_order),
                    floor,
                )

    def test_each_iterate_has_increasing_strong_zero_trace_order(self):
        for trace_order in range(8):
            for depth in range(20):
                self.assertEqual(
                    output_trace_power(depth, trace_order),
                    depth + trace_order,
                )

    def test_exact_upward_fourier_leray_links(self):
        state_vector = state_polarisation()
        for level in range(1, 30):
            drift_frequency = upward_drift_frequency(level)
            drift_vector = upward_drift_polarisation(level)
            previous_frequency = state_frequency(level - 1)
            output_frequency = state_frequency(level)

            self.assertEqual(
                vector_add(previous_frequency, drift_frequency),
                output_frequency,
            )
            self.assertEqual(vector_dot(drift_vector, drift_frequency), 0)
            self.assertEqual(vector_dot(state_vector, output_frequency), 0)
            self.assertEqual(
                upward_transport_coefficient(level),
                dyadic_frequency(level) * dyadic_frequency(level - 1),
            )
            self.assertEqual(
                leray_projection(state_vector, output_frequency),
                state_vector,
            )
            self.assertEqual(
                vector_squared_norm(drift_vector),
                Fraction(5, 4) * dyadic_frequency(level) ** 2,
            )

    def test_exact_terminal_fourier_hodge_return(self):
        state_vector = state_polarisation()
        output_frequency = terminal_output_frequency()
        for level in range(30):
            drift_frequency = terminal_drift_frequency(level)
            drift_vector = terminal_drift_polarisation(level)
            input_frequency = state_frequency(level)

            self.assertEqual(
                vector_add(input_frequency, drift_frequency),
                output_frequency,
            )
            self.assertEqual(vector_dot(drift_vector, drift_frequency), 0)
            self.assertEqual(
                terminal_transport_coefficient(level),
                dyadic_frequency(level),
            )
            self.assertEqual(
                hodge_gradient_projection(state_vector, output_frequency),
                state_vector,
            )
            self.assertEqual(
                vector_squared_norm(drift_vector),
                1 + dyadic_frequency(level) ** 2,
            )

    def test_critical_packet_tower_has_bounded_weak_l3_charge(self):
        for level in range(1, 30):
            self.assertEqual(weak_l3_tail_charge(level), Fraction(8, 7))

    def test_packet_energy_and_time_integrated_dissipation_are_summable(self):
        for level in range(1, 20):
            self.assertEqual(packet_volume(level), Fraction(1, 8**level))
            self.assertEqual(packet_energy(level), Fraction(1, 2**level))
            self.assertEqual(packet_enstrophy_rate(level), 2**level)
            self.assertEqual(packet_dissipation(level), Fraction(1, 2**level))
        for depth in range(30):
            total = 1 - Fraction(1, 2**depth)
            self.assertEqual(finite_energy_or_dissipation(depth), total)
            self.assertLessEqual(total, 1)

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            dyadic_frequency(-1)
        with self.assertRaises(ValueError):
            heat_clock(0)
        with self.assertRaises(ValueError):
            pressure_cost_lower_bound(1, -1)
        with self.assertRaises(ValueError):
            pressure_cost_lower_bound(1, 1, Fraction(-1))
        with self.assertRaises(ValueError):
            weak_l3_tail_charge(0)
        with self.assertRaises(ValueError):
            path_mass(True)
        with self.assertRaises(ValueError):
            upward_drift_frequency(0)
        with self.assertRaises(ValueError):
            leray_projection(
                state_polarisation(),
                (Fraction(0), Fraction(0), Fraction(0)),
            )


if __name__ == "__main__":
    unittest.main()
