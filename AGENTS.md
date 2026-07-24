# Agent router

Read `HANDOFF.md` first. It contains only the live gate; do not preload its
ancestry. Follow one route below and stop when that route has enough evidence.

## Routes

- Live ROUTE-R3B gate:
  `HANDOFF.md` → relevant link in `dossier/status.md` → one proof note.
- Canonical claims, routes, and experiments:
  `dossier/records/README.md` → relevant JSON record → named artefact.
- Closed 2607 audit:
  `dossier/papers/2607.08866-audit.md` →
  `dossier/records/paper-2607-obligations.json` →
  `dossier/papers/2607.08866-proof-map.md`.
- Exact 2607 source: run `make fetch-2607`; inspect only
  `lab/cache/arxiv/2607.08866v2/source/chaos_sphere.tex`.
- Executable ledger:
  `lab/README.md` → `Makefile` → one named module and test.
- Clay scope or another route:
  `dossier/clay-target.md` → `dossier/possibility-tree.md`.
- Breakdown/HWY:
  `dossier/papers/2509.25116-bridge-note.md`.
- Human-facing orientation: `README.md`.

## Context discipline

- `HANDOFF.md` is replace-not-append current state, not a research diary.
- `dossier/status.md` is a compact result/frontier index, not a proof.
- Put proof detail in one experiment note and exact metadata in
  `dossier/records/`; link instead of copying.
- Keep approximately 200 lines in `HANDOFF.md` and the possibility tree,
  and 500 in `dossier/status.md`; `make context` enforces hard limits.
- Recover pre-slim chronology with
  `git show a7ae140:HANDOFF.md` or
  `git show a7ae140:dossier/status.md`.
- Same-system agent review is “adversarial recomputation”, not independent
  external review.

## Non-negotiables

- The Clay problem is unsolved. Match any claimed resolution to exact
  alternative A--D.
- ROUTE-R3B assumes a weak-\(L^3\) Type-I genealogy; even closing it does not
  cover Type II.
- The 2607 chain is only a repaired projected-mild conditional theorem; its
  geometric hypotheses are not derived for arbitrary Clay data.
- Label theorem, conditional theorem, published theorem, preprint claim,
  computation, and heuristic exactly.
- Progress closes an obligation or possibility node; prose volume is not
  progress.
- `dossier/records/` is canonical. Change records and narrative together.
- Keep downloaded sources and generated PDFs in ignored `lab/cache/`; preserve
  source-version and line-anchor provenance.
- Before reporting or committing: `make check` and `git diff --check`.
