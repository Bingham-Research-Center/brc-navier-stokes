# Agent router

Read `HANDOFF.md`, then only its named proof note and route record. Follow
another link only to discharge the live obligation.

## Other entry points

- Records/status work: `dossier/records/README.md` → one JSON record → artefact.
- 2607 audit: `dossier/papers/2607.08866-audit.md` →
  `dossier/records/paper-2607-obligations.json` → proof map.
- Exact 2607 source: `make fetch-2607`; read only
  `lab/cache/arxiv/2607.08866v2/source/chaos_sphere.tex`.
- Executable certificate: `lab/README.md` → one module/test.
- Clay tree: `dossier/clay-target.md` → `dossier/possibility-tree.md`.
- Breakdown/HWY: `dossier/papers/2509.25116-bridge-note.md`.
- Human orientation: `README.md`.

## Rules

- The Clay problem is unsolved. Match any resolution to exact alternative A--D.
- The repaired 2607 result is conditional; its geometry is not known for
  arbitrary Clay data.
- Distinguish theorem, conditional theorem, source claim, computation, and
  heuristic. Same-system review is not external confirmation.
- `dossier/records/` is canonical; one proof note owns each derivation.
  Routine work changes only that pair and replace-not-append `HANDOFF.md`.
- Preserve source versions/anchors. Keep source and PDF caches ignored.
- Do not seek deleted review correspondence; use `dossier/review-ledger.md`.
  Keep superseded chronology in Git, not live context. Add code only for a
  nontrivial falsifiable finite claim.
- Every commit batch includes a new self-contained
  `dossier/rounds/YYYY-MM-DD-<slug>.tex` report: formal statements/proofs,
  conjectures, robust novel findings subject to review, and open obligations.
  Compile it warning-free into ignored `lab/cache/rounds/` before committing.
- Commit every trackable round change with a terse, detailed message, John’s
  configured identity, and `Co-authored-by: Codex <codex@openai.com>`.
  Ensure the Bingham Research Center repository and both remotes are public;
  push `main` to `brc` and `origin`, then verify their exact SHA each time.
- Progress closes an obligation or possibility node, not a prose quota.
- Before reporting or committing: `make check` and `git diff --check`.
