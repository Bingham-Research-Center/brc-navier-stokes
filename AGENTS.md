# Agent router

Start with `HANDOFF.md`. Load only its named proof note and canonical route;
follow another link only when the live obligation requires it.

## Lookup routes

- Claim, route, experiment, or source:
  `dossier/records/README.md` → one JSON entry → named artefact.
- Closed 2607 audit: `dossier/papers/2607.08866-audit.md` →
  `dossier/records/paper-2607-obligations.json` →
  `dossier/papers/2607.08866-proof-map.md`.
- Exact 2607 source: `make fetch-2607`, then only
  `lab/cache/arxiv/2607.08866v2/source/chaos_sphere.tex`.
- Executable certificate: `lab/README.md` → one module/test.
- Clay/other route: `dossier/clay-target.md` → `dossier/possibility-tree.md`.
- Breakdown/HWY: `dossier/papers/2509.25116-bridge-note.md`.
- Human orientation: `README.md`.

## Discipline

- The Clay problem is unsolved. Match any resolution to exact alternative
  A--D; closing a conditional route is not a Clay resolution.
- The 2607 chain is only a repaired projected-mild conditional theorem; its
  geometric hypotheses are not derived for arbitrary Clay data.
- Label theorem, conditional theorem, source claim, computation, and heuristic
  exactly.  Same-system review is adversarial recomputation, not external
  review.
- `dossier/records/` is canonical and one proof note owns each derivation.
  Routine work updates that pair and `HANDOFF.md`; change `status.md` or the
  possibility tree only when durable route state changes.
- `HANDOFF.md` is replace-not-append. Incorporate review corrections into
  canonical artefacts; leave one-use correspondence and superseded chronology
  to Git.
- Add code only when it can falsify or certify a nontrivial finite claim.
- Preserve source versions and line anchors; keep source/PDF caches ignored.
- Progress closes an obligation or possibility node, not a prose quota.
- Before reporting or committing: `make check` and `git diff --check`.
