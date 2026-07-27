# Milestone registry

**Updated:** 2026-07-27 · **Clay status:** unsolved

Ranked durable results nearest to a standalone external write-up. Any round
whose result is schedule-independent adds or updates its row in the same
commit. No entry resolves a Clay alternative; each is conditional exactly as
recorded in its ledger entries.

## Status vocabulary

- **candidate-standalone-note:** a self-contained write-up exists or is one
  bounded edit away; external review pending.
- **internal-durable:** schedule-independent and ledger-recorded; needs a
  self-contained write-up before circulation.

## Milestones

| # | Result | Artefacts | Status | External review | Depends on |
|---|---|---|---|---|---|
| 1 | Referee-grade audit and line-anchored proof map of arXiv:2607.08866v2 | [audit](papers/2607.08866-audit.md), [proof map](papers/2607.08866-proof-map.md) | candidate-standalone-note | pending | O2607-01..16; CLM-GRUJIC-001 (conditional_preprint) |
| 2 | Type-II temporal five-power barrier: Ls in time, weak-L3 in space with s > 5 plus the energy class excludes fixed-energy shrinking carriers at first blow-up; endpoint 5 sharp | [round](rounds/2026-07-24-type-ii-temporal-five-barrier.tex), [note](experiments/type-ii-temporal-five-barrier.md) | candidate-standalone-note | pending | ROUTE-R3C entry assumptions; CLM-ENERGY-MEASURE-NO-ATOMS-001 (established_reading) |
| 3 | Energy-only low-pass turnover clock: replacing a radius-R carrier by a sufficiently smaller one costs time at least c R^(5/2), uniform over moving centres | [round](rounds/2026-07-24-type-ii-compact-carrier-clock.tex), [note](experiments/type-ii-compact-carrier-clock.md) | candidate-standalone-note | pending | ROUTE-R3C entry assumptions |
| 4 | Conditional terminal-dimension pincer: 3/5 <= dim_H sigma <= 1 with H^1(sigma) = 0 for the anomalous defect | [round](rounds/2026-07-25-type-ii-terminal-dimension-pincer.tex), [note](experiments/type-ii-terminal-dimension-pincer.md) | candidate-standalone-note | pending; same-system recomputation logged in the review ledger | CLM-ENERGY-MEASURE-NO-ATOMS-001 (established_reading) |
| 5 | Per-event adjoint-pressure cost lower bound with the open n-uniform genealogy boundary stated | [reviewer note](adjoint-pressure-cost-reviewer.tex), [history note](experiments/adjoint-pressure-history.md) | candidate-standalone-note | pending | frozen ROUTE-R3B gates in [routes](records/routes.json) |

Retire a row only when its result is superseded, with the successor named
here and the superseded artefacts left to Git history.
