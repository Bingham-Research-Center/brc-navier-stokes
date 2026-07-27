# Agent router

Read `HANDOFF.md`, then only its named proof note, record, and course move; follow another link only for the live obligation.

## Other entry points

- Records/status work: `dossier/records/README.md` → one JSON record → artefact.
- Milestones: `dossier/milestones.md` (ranked results, external-review state).
- 2607 audit: `dossier/papers/2607.08866-audit.md` →
  `dossier/records/paper-2607-obligations.json`; exact source: `make fetch-2607`,
  then only `lab/cache/arxiv/2607.08866v2/source/chaos_sphere.tex`.
- Executable certificate: `lab/README.md` → one module/test.
- Clay tree: `dossier/clay-target.md` → `dossier/possibility-tree.md`.
- Breakdown/HWY: `dossier/papers/2509.25116-bridge-note.md`.
- Campaign choice: `dossier/moonshot-course.md`; human map: `README.md`.
- Audit record: `dossier/reviews/2026-07-27-fable-audit.md`.

## Rules

- The Clay problem is unsolved. Match any resolution to exact alternative A--D.
- The repaired 2607 result is conditional; its geometry is not known for arbitrary
  Clay data.
- Distinguish theorem, conditional theorem, source claim, computation, and
  heuristic. Same-system review is not external confirmation.
- Label a representative-schedule exponent schedule-conditional in the same
  sentence; a route-level barrier needs a schedule-free proof.
- After three budget/countermodel cycles with no velocity-field-realizable
  obstruction, freeze the route in `HANDOFF.md` and
  return to `dossier/possibility-tree.md`; the handoff owns the live count.
- A new budget cycle must break cascade averaging (Tao 2016) via local
  energy, pressure, or exact triad phase/geometry.
- Update `dossier/milestones.md` with each schedule-independent result.
- Read any signed external review file at the repository root and log its
  disposition in `dossier/review-ledger.md` before deleting it; do not
  seek already-deleted correspondence.
- `dossier/records/` is canonical; one proof note owns each derivation.
  Routine work changes only that pair and replace-not-append `HANDOFF.md`.
- Preserve source versions/anchors. Keep source and PDF caches ignored. Keep
  superseded chronology in Git, not live context. Add code only for a
  nontrivial falsifiable finite claim.
- Every commit batch includes a new self-contained
  `dossier/rounds/YYYY-MM-DD-<slug>.tex` report: formal statements/proofs,
  conjectures, robust novel findings subject to review, and open obligations.
  Compile it warning-free into ignored `lab/cache/rounds/` before committing.
- Commit each trackable round with John's configured identity, a terse detailed
  message, and `Co-authored-by: Codex <codex@openai.com>`. Keep the Bingham
  Research Center repository and both remotes public; push `main` to `brc` and
  `origin`, then verify their exact SHA.
- Progress closes an obligation or possibility node, not a prose quota. Before
  reporting or committing: `make check` and `git diff --check`.
