# Handoff: Type-II entrance

**Updated:** 2026-07-24

**Clay status:** unsolved

**Live route:** `ROUTE-R3C`

**Previous checkpoint:** `EXP-ADJOINT-PRESSURE-FRESHNESS-WITHOUT-FLOOR-001`

This is replace-not-append working memory. Durable results live in
[`dossier/status.md`](dossier/status.md), exact metadata in
[`dossier/records/`](dossier/records/README.md), and derivations in their
named experiment notes.

## Load only

- [Clay target](dossier/clay-target.md).
- [R3C in the possibility tree](dossier/possibility-tree.md#r3c-type-ii).
- [Canonical R3C record](dossier/records/routes.json).
- For overlap with prior work only:
  [natural-frequency cascade](dossier/experiments/natural-frequency-cascade.md),
  [packet lifetime](dossier/experiments/packet-lifetime.md), and
  [sparse-analyticity endgame](dossier/experiments/sparse-analyticity-endgame.md).

Do not load the R3B chain unless a new theorem or external review directly
reopens it. Its result, assumptions, gates, failed shortcuts, and proof links
are preserved in the
[durable R3B status](dossier/status.md#2-conditional-r3b-profile-reduction).

## Exact live question

Starting only from a smooth finite-energy solution before a putative first
singular time, give an exhaustive Type-II entrance alternative that survives
moving centres, multiple cores, changing scales, oscillation, and loss of
profile compactness. Do not import R3B's uniform weak-\(L^3\) bound or
conditional Besov genealogy.

## Checked starting ledger

Write \(m(t)=\|u(t)\|_{L^{3,\infty}}\) and \(E_0=\sup_t\|u(t)\|_2^2\).
Energy and Sobolev give

\[
m(t)^4\lesssim E_0\|\nabla u(t)\|_2^2,
\qquad
\int_0^{T^*}m(t)^4\,dt\lesssim E_0^2/\nu.
\]

Thus Type-II weak-\(L^3\) growth is permitted only on a finite
\(m^4\)-occupation budget; this is not regularity.

For a near-extremising dyadic amplitude layer with energy \(e(t)\), the scale
ledger is

\[
a\asymp m^3/e,\qquad R\asymp e/m^2,\qquad
\|\nabla u\|_2^2\gtrsim m^4/e.
\]

Along any \(m\to\infty\) sequence, the first candidate exhaustive split is:

1. \(E_0/e\) remains bounded: an energy-efficient coherent carrier;
2. \(E_0/e\to\infty\): a vanishing-energy carrier.

This split is a reduction to prove and stress-test, not yet a route closure.
The high-consequence unknown is whether actual NSE dynamics force enough
compactness or rigidity in either branch; scalar energy and clock budgets
alone allow Zeno concentration.

## Next bounded cycle

1. Prove the layer reduction with exact constants and quantifiers.
2. Test both branches against Type-II rates, moving/multiple centres,
   oscillatory scales, and compactness loss.
3. Record either one exhaustive entrance theorem or the sharp survivor that
   prevents it; then update R3C's canonical record and compact status.

## Frozen boundary

R3B remains a conditional weak-\(L^3\) Type-I branch pending independent
external review. No critical nested-action bound, fresh fixed event charge,
event-index contradiction, or Clay alternative A--D is proved. The
Albritton--Barker critical-amplitude repair also awaits external confirmation.

Before reporting or committing: `make check` and `git diff --check`.
