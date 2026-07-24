# Handoff: current Navier--Stokes moonshot gate

**Updated:** 2026-07-24

**Clay status:** unsolved

**Checkpoint:** `EXP-ADJOINT-PRESSURE-TERMINAL-DISSIPATION-COLLAPSE-001`

**Live route:** ROUTE-R3B, conditional weak-\(L^3\) Type-I regularity

This is replace-not-append current state.  Use
[`dossier/status.md`](dossier/status.md) for durable results,
[`dossier/records/`](dossier/records/README.md) for canonical metadata, and
one linked experiment for proof detail.  Pre-slim chronology is recoverable
with `git show a7ae140:HANDOFF.md`.

## State in one minute

No Clay alternative A--D is proved.  R3B starts from a smooth finite-energy
trajectory before a candidate first singular time, a uniform terminal
weak-\(L^3\) bound, and the conditional Besov-event genealogy.  Its structural
chain yields a nonzero coherent ancient suitable weak-\(L^3\) distance
profile with two terminal singular points and recurring positive Besov
defect.  Even a complete R3B exclusion would leave Type II in ROUTE-R3C.

Every selected event forces a positive finite-window adjoint-pressure cost.
The current upper audit now gives, for every sufficiently small fixed physical
cutoff \(r_\bullet\),

\[
P_n(T)
\le
C
+C\widehat{\mathfrak D}_n(T;r_\bullet)
+o_n(1).
\]

\[
\widehat{\mathfrak D}_n
=
\sum_{\rho_nR_k\le r_\bullet}
\left(
\frac{\widehat\delta_{n,k}}{\rho_nR_k}
\right)^{1/2},
\]

where \(\widehat\delta_{n,k}\) is global physical dissipation on nested
common-endpoint intervals extending from the staggered prehistory through the
current window.

The
[terminal-dissipation theorem](dossier/experiments/adjoint-pressure-terminal-dissipation-collapse.md)
rewrites current spatially cut-off nonlinear work as an exact projected
gradient pairing.  Weak-\(L^3\) interpolation bounds it by coefficient
dissipation; the signed local filtered-energy identity absorbs the otherwise
unknown local high-pass dissipation.  Exact physical scaling then merges
current work and staggered entrance ancestry into the single action above.

Thus entrance energy, current nonlinear work, remote inheritance,
macroscopic shells, and diffusion-boundary leakage are no longer independent
upper-audit branches.  A terminal modulus \(s^\alpha\) controls the action
for every \(\alpha>1/2\).  A triangular scalar family survives at
\(\alpha=1/2\), so the power boundary is sharp only for scalar histories;
critical logarithmic moduli and one-trajectory NSE non-reuse remain open.
Adversarial same-system recomputation accepted the theorem.  External
mathematical review is pending.

## Exact live fork

### A. Uniform adjoint-cost budget

Obtain at least one genuinely NSE-specific estimate:

1. bound \(\widehat{\mathfrak D}_n\) at the critical \(s^{1/2}\) endpoint
   through a logarithmic/Dini gain or non-reuse of nested intervals;
2. compare it with the already forced lower-band decrement; or
3. convert its divergence into individually fresh event
   charges paid by one finite same-trajectory budget.

Do not reintroduce current nonlinear work or the earlier payer branches; all
are absorbed into \(\widehat{\mathfrak D}_n\).

### B. Event-index freshness

Use the already forced terminal flux and lower-band decrement to prove:

- bounded time-frequency overlap;
- a scale-zero event floor;
- a non-Zeno/intervening-event law; or
- a pressure-visible cross-event telescope.

The current decrement excludes a near-lossless distinct-shell cascade but
still permits overlapping geometrically decaying events.

## Standing assumptions

- The weak-\(L^3\) Type-I hypothesis is not derived for arbitrary Clay data.
- The Albritton--Barker critical-amplitude repair awaits external
  confirmation.
- The Besov-event and feedback-pressure genealogy is conditional.
- No critical nested-action bound, fresh payer index, or event-index sum is
  known.

## Closed shortcuts

| Do not retry unchanged | Obstruction |
|---|---|
| Raw energy, absolute continuity, or terminal nesting | Scalar nested histories retain divergent critical action. |
| Natural heat time per scale | Geometric scales have a Zeno clock. |
| Adjoint \(L^2\) energy | It stops at the square-root secondary-index law. |
| Positive cumulative flux | One reservoir can pay many nested boundaries. |
| Bare local high-pass identity | Diffuse endpoint-weighted arrays have no charged block. |
| Bare spectral or spatial primal--adjoint telescope | The former is pressure-blind; the latter can cancel in every gauge. |

## Next actions

1. Classify the exact critical logarithmic/Dini modulus required to sum
   \(\widehat{\mathfrak D}_n\).
2. Test that condition against the weak-\(L^3\) lower-band decrement and
   local higher-integrability theorem on the actual trajectory.
3. If neither closes a payer, consolidate for fresh-context external review
   before another long theorem chain.

Other routes: [2607 audit](dossier/papers/2607.08866-audit.md),
[possibility tree](dossier/possibility-tree.md), and
[HWY bridge](dossier/papers/2509.25116-bridge-note.md).

## Control rules

- Same-system review is adversarial recomputation, not independent external
  review.
- Tests certify only the algebra and finite bookkeeping they exercise.
- Progress closes an obligation or possibility node; prose volume is not
  progress.
- Before reporting or committing: `make check` and `git diff --check`.
