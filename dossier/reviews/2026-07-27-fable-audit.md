# External audit and curation record, 2026-07-27

**Reviewer:** Claude (Fable 5), an external system operated by John Lawson;
not the system that authored the research content.
**Scope:** whole repository at HEAD `1d9d02c` (121 commits, 2026-07-23 to
2026-07-25).
**Method:** three parallel read-only audit passes (git history and churn;
ledger-label honesty; rounds/LaTeX and lab assessment), then a curation
design whose file-level mechanics were verified against the live validators
(`make check` run green before and after every change).
**Clay status: unsolved.** Nothing in this report or in the curation pass
changes any mathematical claim.

This document is the durable record of the audit AND of the four-commit
curation intervention that followed it. It is written so that (a) another
agent can critique every judgment here with the evidence cited, and (b) the
resident research agent (Codex) can reconstruct exactly what was changed,
why, and how to challenge or revert it.

## 1. Verdict summary

1. The bookkeeping layer is structurally excellent: zero dangling
   references, duplicate IDs, orphaned files, or date anomalies across all
   five ledgers in [records](../records/README.md).
2. The epistemic discipline is real and improved since the 2026-07-24
   external audit: the self-review loop is now admitted in three surfaces,
   `CLM-ANCIENT-BESOV-LIOUVILLE-001` was downgraded to
   `repaired_source_theorem`, and the open n-uniform genealogy gap of the
   frozen R3B pressure endpoint is recorded in [status](../status.md).
3. The main problems are volume and drift, not dishonesty:
   - 53 experiment notes (median lifetime 1.45 hours between creation and
     last edit; 79 percent under 6 hours) were referenced by no durable
     document and are retired in commit 4 of this pass.
   - The active q4 line's signature scale `L = s^(-9/11) l^(2/11)` is
     schedule-conditional arithmetic, not equation-forced (section 4).
   - The final ~8 research rounds form a budget-versus-countermodel arms
     race whose countermodels are spectra, not velocity fields; they bound
     the method, not Navier-Stokes (section 4).
4. Two external review reports left untracked at the repository root on
   2026-07-24 were deleted without being read or logged (section 5). The
   router rules now require read-and-log before deletion.
5. Five results deserve not to be buried; they are now ranked in the
   [milestone registry](../milestones.md) (section 3).

## 2. What the audit checked and found

### Git history (121 commits, ~26 hours)

Twelve eras: scaffolding; Grujic audit (closed at `6f11282`); five short
exploratory routes (covering entropy, commutator, polar tensor, adjoint
Kato, microbubbles), each closed within hours; the durable ROUTE-R3B
satellite-tower/Besov-ancestry reduction (commits 55-67); adjoint-pressure
charging (68-94, ended frozen with no contradiction); pivot to
ROUTE-R3C/Type-II (95-109); q4 spectral genealogy (110-121, the live
frontier, currently blocked by its own countermodel in
[the handoff](../../HANDOFF.md)).

Codex already performed major trims: 54 `review-letter-*` files deleted at
`0ec2084`, 54 `review-response-*` at `a2dd57e`, HANDOFF/status slimming at
`5af52d2` (net -6033 lines). The rounds discipline (one reviewer-facing
`.tex` per commit batch) started at commit 102 (`b75b5c2`) and has been
followed 20-for-20; the first 101 commits, containing most of the R3B
mathematics, predate it and have no round reports.

### Ledger honesty

All five JSON ledgers validated clean. Claims: 40 total, of which 29
`established`; each was checked against its own statement text and audit
field. Two carried `established` for readings of proof internals rather
than displayed theorems; they are reclassified in commit 1 (section 6).
ROUTE-R3A carried the bare machine status `closed` on the strength of the
`conditional_preprint` claim `CLM-GRUJIC-001`; every prose surface already
scoped this closure as conditional, and the enum now does too
(`closed_conditional`). No Clay alternative is eliminated anywhere; the
[possibility tree](../possibility-tree.md) is consistent with the ledgers.

### Rounds and lab

The 20 files in `dossier/rounds/` classify as 7 substantive, 5 incremental,
8 negative/countermodel. The lab remains exactly what it advertises:
exact-rational arithmetic certificates (868 tests at audit time, zero
numerical PDE content, zero third-party numeric imports). Tonal overclaim
watch-list, none rising to a false statement: declarative theorem-style
titles over schedule-conditional bodies; a section titled "Slam-dunk
candidates" in `dossier/rounds/2026-07-24-type-ii-record-transport.tex`;
the non-verbatim Albritton-Barker amplitude reading load-bearing inside the
"Durable results" section of [status](../status.md) (it is flagged there,
but load-bearing).

## 3. Milestones (why these five)

See the [milestone registry](../milestones.md) for the rows. Ranking
rationale, most externally valuable first:

1. **arXiv:2607.08866 referee audit + line-anchored proof map**
   ([audit](../papers/2607.08866-audit.md),
   [proof map](../papers/2607.08866-proof-map.md)): the one artefact an
   outside mathematician would value today; 16 obligations, pinned source,
   a defensible repaired conditional theorem, and a concrete erratum
   candidate.
2. **Temporal five-power barrier**
   ([round](../rounds/2026-07-24-type-ii-temporal-five-barrier.tex)):
   schedule-independent statement resting on peer-reviewed
   Leslie-Shvydkoy; sharp endpoint; citable as a standalone lemma note.
3. **Energy-only carrier turnover clock**
   ([round](../rounds/2026-07-24-type-ii-compact-carrier-clock.tex)):
   reusable tool estimate, uniform over moving centres.
4. **Terminal-dimension pincer**
   ([round](../rounds/2026-07-25-type-ii-terminal-dimension-pincer.tex)):
   the most mathematician-facing conditional q4 result; three precision
   repairs already logged in the [review ledger](../review-ledger.md).
5. **Per-event adjoint-pressure cost note**
   ([reviewer note](../adjoint-pressure-cost-reviewer.tex)): the only
   fully self-contained write-up in the tree, with the honest open
   boundary (the event-sum/n-uniform genealogy budget) stated.

## 4. Drift diagnosis (the finding most worth contesting)

Claim: the q4 scale `L = s^(-9/11) l^(2/11)` is not forced by the
equations. Derivation of the claim, so it can be checked or refuted:

- The schedule is chosen, not derived: `m_j = 2^(2j)`, `a_j = 2^(6j)`,
  `R_j = 2^(-4j)`, `tau_j = 2^(-10j)`, `q_j = 4`, `nu = 1`, introduced as
  "the exact representative powers" (formerly in the experiment note
  `dossier/experiments/type-ii-cross-record-correlation.md`, retired in
  commit 4 of this pass, recoverable from Git).
- The record gap `Delta t_j ~ 2^(-11j)/j` follows from those choices; the
  "11" is 10 (from `tau_j`) plus 1 (from the band width), both chosen.
- Temporal integrability `s < 11/2` and the rearrangement exponents `2/11`
  and `9/11 = 1 - 2/11` are then pure arithmetic of 11/2. Viscosity is
  normalized away and no absolute constants are tracked.
- Genuine content nearby, to be fair: `R_j ~ m_j^(-2)` is honest critical
  weak-L3 scaling; the Leslie-Shvydkoy inputs are real published theorems;
  and the five-power barrier survives independently of the schedule.
- Decisive symptom: even inside its own schedule the strategy does not
  close. The [handoff](../../HANDOFF.md) records a smooth positive-flux
  shell that pays every current budget finitely and "is a spectral
  countermodel, not a velocity field". The last ~8 rounds each built a
  finer budget and then a finer countermodel that defeats it; every
  countermodel is explicitly not an NSE evolution. A negative result about
  the method is being produced at increasing precision.

Consequence drawn (judgment, not theorem): further exponent refinement
inside the fixed q4 schedule has low expected value; the schedule-robust
results (milestones 2-4) and the open charge question in the handoff are
the live mathematics. The new router rules make this operational: label
schedule-conditional exponents as such, and freeze a route after three
budget/countermodel cycles with no velocity-field-realizable obstruction.

## 5. The deleted external reviews (process failure, now guarded)

On 2026-07-24 an external audit wrote two untracked reports to the
repository root (`FABLE-REPORT-SO-FAR.md`, `FABLE-SECOND-ORDER-REVIEW.md`).
They were deleted with zero acknowledgment anywhere in history
(`git log --all -S FABLE` is empty), consistent with the then-current rule
"deleted review correspondence is not an input". Their standing
conclusions that remain relevant are preserved here: no false equations
were found in any red-teamed hub; literature citations checked faithful
against arXiv sources; the "adversarial review" loop is same-system (now
admitted in-tree); the adjoint-pressure cost bound is per-event with the
n-uniform genealogy sum open (now recorded in [status](../status.md)).
The router now requires reading and logging any signed external review
file in the [review ledger](../review-ledger.md) before deletion.

## 6. Curation intervention record (four commits, 2026-07-27)

No mathematics was touched. Everything is revertible per-commit; each
commit body carries its own rationale.

- **Commit 1 (`curate: scope conditional statuses...`).** Added
  `established_reading` (claims) and `closed_conditional` (routes) to both
  enum copies (`lab/schemas/research-ledgers.schema.json`,
  `lab/navier_lab/records.py`) with semantics in
  [records/README](../records/README.md). Reclassified ROUTE-R3A
  (`closed` to `closed_conditional`) and two claims
  (`CLM-LOCAL-WEAK-L3-SINGULAR-COUNT-001`,
  `CLM-ENERGY-MEASURE-NO-ATOMS-001`, `established` to
  `established_reading`), appending one audit sentence each. Nothing
  depends on the two claims; no prose document cites their IDs.
- **Commit 2 (`curate: add ranked milestone registry...`).** Added
  [milestones](../milestones.md), README/AGENTS links, four router rules
  (schedule-conditional labelling; three-cycle freeze; read-and-log before
  deleting external reviews; milestone-row maintenance), and registered
  both in `lab/navier_lab/context_budget.py` (AGENTS budget 40 to 55,
  milestones 60, required markers) so `make check` enforces them.
- **Commit 3 (this report).** Added this file and an external-review
  section in the [review ledger](../review-ledger.md).
- **Commit 4 (`curate: retire ...`).** Retired the experiment notes
  referenced by no durable document, their exclusive lab modules and
  tests, and the corresponding ledger entries. Retirement criterion, so it
  can be re-derived mechanically: a note is dead if and only if no
  markdown file outside `dossier/experiments/` links to it (resolved with
  the same regex and path rules as `lab/navier_lab/links.py`) and none of
  its ledger records appear in any 2607 obligation's evidence; a lab file
  is prunable if and only if it appears only in dead records' artifacts
  and is imported by no kept module. Durable roots include this report and
  the milestone registry, which deliberately resurrects
  `type-ii-compact-carrier-clock`. Recovery: any retired file is
  enumerable via `git log --diff-filter=D --name-only` and restorable via
  `git show <sha>:<path>` (recipe in [records/README](../records/README.md)).

## 7. Points most open to critique

Listed so a critic knows where this pass exercised judgment:

1. The dead-note criterion counts only direct links from durable
   documents, not transitive links between experiment notes. A chain of
   notes reachable only through a retired note is treated as dead. The
   counter-position (transitive closure) would have kept 133 of 138 notes
   and defeated the trim's purpose; but specific resurrections are cheap
   (`git show` + ledger re-entry) and invited.
2. `established_reading` is a new status; a critic may argue the two
   reclassified claims deserve full `established` (the readings are short
   and arguably routine) or, conversely, `preprint_claim` severity. The
   chosen semantics are in [records/README](../records/README.md).
3. The three-cycle freeze threshold in the router rules is a chosen
   constant. Two would have frozen q4 earlier; five would likely never
   bind. Adjust with evidence, not convenience.
4. The q4-numerology verdict (section 4) is a judgment about research
   value, not a mathematical refutation; nothing in the q4 chain was found
   false. If a finite angular/spatial/phase/genealogical charge for the
   broad shell is found, the verdict weakens materially.
5. Milestone ranking places external legibility above internal depth; the
   frozen R3B reduction (commits 55-67) is arguably deeper mathematics
   than milestones 3-5 but is not separately rowed because it lacks a
   self-contained write-up; it is reachable through milestone 5's
   dependencies.

## 8. Queued next steps (deferred, each needs its own deep session)

1. Verify and polish the 2607 audit into an erratum/comment note.
2. Deep-verify the five-power barrier; extract a standalone lemma note.
3. Verify the R^(5/2) carrier clock; short write-up.
4. Verify the dimension pincer and the adjoint-pressure cost note,
   including the Albritton-Barker amplitude reading against the published
   text.

External review of all mathematical content remains pending. Same-system
recomputation, and this audit, are not that review.
