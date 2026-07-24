# Agent router

Read `HANDOFF.md`, follow one linked route, and stop loading context once the
task has enough evidence.

## Routes

- Live R3B: `HANDOFF.md` → its one current proof note.
- Canonical claim, route, or experiment:
  `dossier/records/README.md` → one JSON entry → named artefact.
- Closed 2607 audit: `dossier/papers/2607.08866-audit.md` →
  `dossier/records/paper-2607-obligations.json` →
  `dossier/papers/2607.08866-proof-map.md`.
- Exact 2607 source: `make fetch-2607`, then only
  `lab/cache/arxiv/2607.08866v2/source/chaos_sphere.tex`.
- Executable certificate: `lab/README.md` → one module/test.
- Clay/other route: `dossier/clay-target.md` →
  `dossier/possibility-tree.md`.
- Breakdown/HWY: `dossier/papers/2509.25116-bridge-note.md`.
- Human orientation: `README.md`.

## Write discipline

- `HANDOFF.md` is replace-not-append live state; `dossier/status.md` is the
  compact durable index; `dossier/records/` is canonical.
- Default frontier unit: one proof note, one record update, and the smallest
  necessary status/handoff sync.  Link instead of repeating derivations.
- Do not commit one-use review correspondence.  Incorporate corrections into
  the proof; Git preserves superseded chronology.
- Add executable code only when it can falsify or certify a nontrivial finite
  claim.  `make context` enforces active-file budgets.

## Non-negotiables

- The Clay problem is unsolved.  Match any resolution claim to exact
  alternative A--D.
- R3B assumes weak-\(L^3\) Type I and would not cover Type II.
- The 2607 chain is only a repaired projected-mild conditional theorem; its
  geometric hypotheses are not derived for arbitrary Clay data.
- Label theorem, conditional theorem, source claim, computation, and heuristic
  exactly.  Same-system review is adversarial recomputation, not external
  review.
- Progress closes an obligation or possibility node; prose volume is not
  progress.
- Change records and narrative together.  Preserve source versions and line
  anchors; keep downloaded sources and generated PDFs ignored.
- Before reporting or committing: `make check` and `git diff --check`.
