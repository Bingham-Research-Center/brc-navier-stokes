# Agent router

Read `HANDOFF.md`, follow its smallest sufficient link set, and stop loading
context once the current obligation is decidable.

## Routes

- Live work: `HANDOFF.md` → its named route and proof note.
- Claim, route, experiment, or status:
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

## Discipline

- `HANDOFF.md` is replace-not-append live state; `dossier/status.md` is the
  compact durable index; `dossier/records/` is canonical.
- Default change: one proof note, one record update, and only the narrative
  sync needed to route the next decision. Link; do not copy derivations.
- Incorporate review corrections into canonical artefacts. Do not retain
  one-use correspondence; Git preserves superseded chronology.
- Add code only when it can falsify or certify a nontrivial finite claim.
- The Clay problem is unsolved. Match any resolution to exact alternative
  A--D; closing a conditional route is not a Clay resolution.
- The 2607 chain is only a repaired projected-mild conditional theorem; its
  geometric hypotheses are not derived for arbitrary Clay data.
- Label theorem, conditional theorem, source claim, computation, and heuristic
  exactly.  Same-system review is adversarial recomputation, not external
  review.
- Preserve source versions and line anchors; keep downloaded sources and
  generated PDFs ignored.
- Progress closes an obligation or possibility node, not a prose quota.
- Before reporting or committing: `make check` and `git diff --check`.
