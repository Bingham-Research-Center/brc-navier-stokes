# Proof lab

The lab performs small, auditable algebra, bookkeeping, and finite-model
checks.  It is not a theorem prover: passing tests do not certify analytic
estimates, compactness, Fourier support, or a Navier--Stokes theorem.

## Use

From the repository root:

```bash
make check
make scaling
make adjoint-pressure-flux-decrement
make fetch-2607
```

For an experiment's focused command, read its `lab/navier_lab/*.py` artefact
in [`dossier/records/experiments.json`](../dossier/records/experiments.json)
and replace underscores in the module name with hyphens.  The Makefile
discovers ordinary modules automatically; only short historical aliases and
the source-fetch/build commands are declared by hand.

`make check` runs:

- active-context budgets;
- canonical-record validation;
- local-link and mathematical-markup checks; and
- the complete unit-test suite.

`make fetch-2607` writes only beneath ignored `lab/cache/`.  Its manifest pins
the retrieval URL, UTC time, byte count, SHA-256 digest, and archive members.
Exact source remains untracked unless redistribution permission is verified.

## Layout

- `navier_lab/`: dependency-free checkers and finite models.
- `tests/`: executable assertions for those modules.
- `schemas/`: public record schemas.
- `cache/`: ignored downloaded sources, builds, and generated PDFs.

The experiment ledger is the only maintained catalogue of what each module
checks and, crucially, what it does not check.  This avoids a second
hand-written inventory drifting behind the mathematics.

## Certificate discipline

A genuine numerical certificate must separate:

1. candidate generation;
2. deterministic finite certificate data;
3. a small independent verifier; and
4. the analytic theorem turning verifier acceptance into the claimed result.

Use directed rounding or exact arithmetic where certification requires it.
Do not add a Python module merely to restate algebra that is clearer and fully
auditable in the proof note itself.

## Adding an experiment

Add the canonical record before implementation.  State the hypothesis,
invariants, success criterion, failure interpretation, and exact artefacts.
Add code only when it can falsify or mechanically certify something
nontrivial; an analytic proof does not need ceremonial executable scaffolding.
