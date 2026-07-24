PYTHON ?= python
PYTHONPATH := lab

.PHONY: check context records links markup test scaling log-chain multicore anisotropic covering-entropy perimeter-packing packet-lifetime mixed-lorentz vanishing-tail critical-localization truncated-direction ancient-compactness commutator-bubbles commutator-dust natural-frequency same-solution-granularity projective-alignment vacuum-orientation polar-tensor polar-entropy tensor-adjoint adjoint-kato shear-adjoint trace-adjoint trace-band-flux trace-boundary-flux trace-projective projective-interface trace-excess trace-temporal alignment-excess carrier-microbubble microbubble-decoration strain-jet forcing-jet moving-band tree-budget band-increment fresh-detector frequency-energy scale-defect two-scale-sync fixed-shell-clock continuation-clock fixed-shell-local singular-clock-centering terminal-satellite-tower terminal-satellite-compactness terminal-besov-ancestry terminal-outer-profile terminal-distance-profile terminal-satellite-packing terminal-cluster-packing terminal-logscale-survivor scale-hull-balance parabolic-scale-hull defect-event-suspension adjoint-pressure-history adjoint-pressure-packets adjoint-pressure-initial-layer adjoint-pressure-bandlimit adjoint-pressure-enstrophy adjoint-pressure-cubic adjoint-pressure-direct adjoint-pressure-feedback adjoint-pressure-feedback-shells adjoint-pressure-feedback-frequency adjoint-pressure-feedback-dust adjoint-pressure-temporal adjoint-pressure-polar-vacuum adjoint-pressure-balanced-polar adjoint-pressure-amplitude-window adjoint-pressure-trace-participation adjoint-pressure-product-trace adjoint-pressure-intermediate-localization adjoint-pressure-stretched-history adjoint-pressure-second-interaction adjoint-pressure-interaction-depth adjoint-pressure-critical-volterra adjoint-pressure-skew-compression adjoint-pressure-frequency-colligation adjoint-pressure-frequency-zeno defect-event-hull strain fetch-2607 compile-2607
.PHONY: adjoint-pressure-terminal-return adjoint-pressure-ancestry-survivor adjoint-pressure-spatial-frequency adjoint-pressure-amplified-ancestry adjoint-pressure-one-return adjoint-pressure-multistage-path adjoint-pressure-corridor-sum adjoint-pressure-corridor-identification adjoint-pressure-last-return adjoint-pressure-no-return adjoint-pressure-parabolic-coefficient-tail adjoint-pressure-parabolic-ancestry adjoint-pressure-parabolic-flux adjoint-pressure-inherited-ancestry adjoint-pressure-flux-decrement adjoint-pressure-spectral-pairing adjoint-pressure-spatial-pairing

check: context records links markup test

context:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.context_budget

records:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.records

links:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.links

markup:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.math_markup

test:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m unittest discover -s lab/tests -v

scaling:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.scaling

log-chain:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.log_chain

multicore:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.multicore

anisotropic:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.anisotropic

covering-entropy:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.covering_entropy

perimeter-packing:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.perimeter_packing

packet-lifetime:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.packet_lifetime

mixed-lorentz:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.mixed_lorentz

vanishing-tail:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.vanishing_tail

critical-localization:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.critical_localization

truncated-direction:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.truncated_direction

ancient-compactness:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.ancient_compactness

commutator-bubbles:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.commutator_bubbles

commutator-dust:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.commutator_dust

natural-frequency:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.natural_frequency

same-solution-granularity:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.same_solution_granularity

projective-alignment:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.alignment_defect

vacuum-orientation:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.vacuum_orientation

polar-tensor:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.polar_tensor_evolution

polar-entropy:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.polar_entropy_barrier

tensor-adjoint:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.tensor_adjoint_closure

adjoint-kato:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_kato

shear-adjoint:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.shear_adjoint

trace-adjoint:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.trace_adjoint

trace-band-flux:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.trace_band_flux

trace-boundary-flux:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.trace_boundary_flux

trace-projective:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.trace_projective_domination

projective-interface:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.projective_zero_interface

trace-excess:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.terminal_trace_excess

trace-temporal:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.trace_temporal_modulus

alignment-excess:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.terminal_alignment_excess

carrier-microbubble:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.terminal_carrier_microbubble

microbubble-decoration:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.microbubble_decoration

strain-jet:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.strain_jet_freezing

forcing-jet:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.forcing_jet_decoupling

moving-band:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.moving_band_coupling

tree-budget:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.tree_budget

band-increment:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.band_increment

fresh-detector:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.fresh_detector

frequency-energy:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.frequency_energy

scale-defect:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.scale_defect

two-scale-sync:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.two_scale_synchronization

fixed-shell-clock:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.fixed_shell_clock

continuation-clock:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.continuation_clock

fixed-shell-local:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.fixed_shell_localization

singular-clock-centering:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.singular_clock_centering

terminal-satellite-tower:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.terminal_satellite_tower

terminal-satellite-compactness:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.terminal_satellite_compactness

terminal-besov-ancestry:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.terminal_besov_ancestry

terminal-outer-profile:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.terminal_outer_profile

terminal-distance-profile:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.terminal_distance_profile

terminal-satellite-packing:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.terminal_satellite_packing

terminal-cluster-packing:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.terminal_cluster_packing

terminal-logscale-survivor:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.terminal_logscale_survivor

scale-hull-balance:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.scale_hull_balance

parabolic-scale-hull:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.parabolic_scale_hull

defect-event-suspension:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.defect_event_suspension

adjoint-pressure-history:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_history

adjoint-pressure-packets:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_packets

adjoint-pressure-initial-layer:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_initial_layer

adjoint-pressure-bandlimit:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_bandlimit

adjoint-pressure-enstrophy:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_enstrophy

adjoint-pressure-cubic:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_cubic

adjoint-pressure-direct:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_direct

adjoint-pressure-feedback:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_feedback

adjoint-pressure-feedback-shells:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_feedback_shells

adjoint-pressure-feedback-frequency:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_feedback_frequency

adjoint-pressure-feedback-dust:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_feedback_dust

adjoint-pressure-temporal:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_temporal

adjoint-pressure-polar-vacuum:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_polar_vacuum

adjoint-pressure-balanced-polar:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_balanced_polar

adjoint-pressure-amplitude-window:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_amplitude_window

adjoint-pressure-trace-participation:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_trace_participation

adjoint-pressure-product-trace:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_product_trace

adjoint-pressure-intermediate-localization:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_intermediate_localization

adjoint-pressure-stretched-history:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_stretched_history

adjoint-pressure-second-interaction:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_second_interaction

adjoint-pressure-interaction-depth:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_interaction_depth

adjoint-pressure-critical-volterra:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_critical_volterra

adjoint-pressure-skew-compression:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_skew_compression

adjoint-pressure-frequency-colligation:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_frequency_colligation

adjoint-pressure-frequency-zeno:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_frequency_zeno

adjoint-pressure-terminal-return:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_terminal_return

adjoint-pressure-ancestry-survivor:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_ancestry_survivor

adjoint-pressure-spatial-frequency:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_spatial_frequency

adjoint-pressure-amplified-ancestry:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_amplified_ancestry

adjoint-pressure-one-return:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_one_return

adjoint-pressure-multistage-path:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_multistage_path

adjoint-pressure-corridor-sum:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_corridor_sum

adjoint-pressure-corridor-identification:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_corridor_identification

adjoint-pressure-last-return:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_last_return

adjoint-pressure-no-return:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_no_return

adjoint-pressure-parabolic-coefficient-tail:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_parabolic_coefficient_tail

adjoint-pressure-parabolic-ancestry:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_parabolic_ancestry

adjoint-pressure-parabolic-flux:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_parabolic_flux

adjoint-pressure-inherited-ancestry:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_inherited_ancestry

adjoint-pressure-flux-decrement:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_flux_decrement

adjoint-pressure-spectral-pairing:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_spectral_pairing

adjoint-pressure-spatial-pairing:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_pressure_spatial_pairing

defect-event-hull: defect-event-suspension

strain:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.strain

fetch-2607:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.source_cache 2607.08866 --version v2

compile-2607: fetch-2607
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.paper_build 2607.08866 --version v2 --main chaos_sphere.tex
