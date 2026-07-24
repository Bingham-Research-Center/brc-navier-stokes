PYTHON ?= python
PYTHONPATH := lab
RUN_MODULE = PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.

# Ordinary proof-lab modules acquire a make target automatically by replacing
# underscores with hyphens.  Keep only genuinely semantic aliases below.
INTERNAL_MODULES := __init__ context_budget intervals links math_markup \
	paper_build records source_cache
LAB_MODULES := $(basename $(notdir $(wildcard lab/navier_lab/*.py)))
LAB_MODULES := $(filter-out $(INTERNAL_MODULES),$(LAB_MODULES))
LAB_TARGETS := $(subst _,-,$(LAB_MODULES))
ALIASES := context markup projective-alignment polar-tensor polar-entropy \
	tensor-adjoint trace-projective projective-interface trace-excess \
	trace-temporal alignment-excess carrier-microbubble strain-jet forcing-jet \
	moving-band two-scale-sync fixed-shell-local defect-event-hull

.PHONY: check context records links markup test $(LAB_TARGETS) $(ALIASES) \
	fetch-2607 compile-2607

check: context records links markup test

context:
	$(RUN_MODULE)context_budget

records:
	$(RUN_MODULE)records

links:
	$(RUN_MODULE)links

markup:
	$(RUN_MODULE)math_markup

test:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m unittest discover -s lab/tests -v

$(LAB_TARGETS):
	$(RUN_MODULE)$(subst -,_,$@)

projective-alignment:
	$(RUN_MODULE)alignment_defect

polar-tensor:
	$(RUN_MODULE)polar_tensor_evolution

polar-entropy:
	$(RUN_MODULE)polar_entropy_barrier

tensor-adjoint:
	$(RUN_MODULE)tensor_adjoint_closure

trace-projective:
	$(RUN_MODULE)trace_projective_domination

projective-interface:
	$(RUN_MODULE)projective_zero_interface

trace-excess:
	$(RUN_MODULE)terminal_trace_excess

trace-temporal:
	$(RUN_MODULE)trace_temporal_modulus

alignment-excess:
	$(RUN_MODULE)terminal_alignment_excess

carrier-microbubble:
	$(RUN_MODULE)terminal_carrier_microbubble

strain-jet:
	$(RUN_MODULE)strain_jet_freezing

forcing-jet:
	$(RUN_MODULE)forcing_jet_decoupling

moving-band:
	$(RUN_MODULE)moving_band_coupling

two-scale-sync:
	$(RUN_MODULE)two_scale_synchronization

fixed-shell-local:
	$(RUN_MODULE)fixed_shell_localization

defect-event-hull: defect-event-suspension

fetch-2607:
	$(RUN_MODULE)source_cache 2607.08866 --version v2

compile-2607: fetch-2607
	$(RUN_MODULE)paper_build 2607.08866 --version v2 --main chaos_sphere.tex
