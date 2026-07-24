# Agent router

Read `HANDOFF.md`, follow one linked route, and stop loading context when the
task has enough evidence.

## Routes

- Live R3B work: `HANDOFF.md` → one linked experiment.
- Claims, routes, or experiments:
  `dossier/records/README.md` → relevant JSON entry → named artefact.
- Closed 2607 audit:
  `dossier/papers/2607.08866-audit.md` →
  `dossier/records/paper-2607-obligations.json` →
  `dossier/papers/2607.08866-proof-map.md`.
- Exact 2607 source: run `make fetch-2607`; inspect only
  `lab/cache/arxiv/2607.08866v2/source/chaos_sphere.tex`.
- Executable certificate: `lab/README.md` → `Makefile` → one module/test.
- Clay or another route:
  `dossier/clay-target.md` → `dossier/possibility-tree.md`.
- Breakdown/HWY: `dossier/papers/2509.25116-bridge-note.md`.
- Human orientation: `README.md`.

## Context discipline

- `HANDOFF.md` is replace-not-append live state.
- `dossier/status.md` is the compact durable index; proof belongs in one
  experiment and exact metadata in `dossier/records/`.
- Link instead of repeating derivations.  Recover removed chronology from Git.
- Same-system review is “adversarial recomputation”, never external review.
- `make context` enforces active-file budgets.

## Non-negotiables

- The Clay problem is unsolved.  Match any claimed resolution to exact
  alternative A--D.
- R3B assumes a weak-\(L^3\) Type-I genealogy; closing it would not cover
  Type II.
- The 2607 chain is only a repaired projected-mild conditional theorem; its
  geometric hypotheses are not derived for arbitrary Clay data.
- Label theorem, conditional theorem, published claim, preprint claim,
  computation, and heuristic exactly.
- Progress closes an obligation or possibility node; prose volume is not
  progress.
- Change canonical records and narrative together.  Preserve source version
  and line anchors; keep downloaded sources and generated PDFs ignored.
- Before reporting or committing: `make check` and `git diff --check`.
