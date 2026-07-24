# Handoff: current Navier--Stokes moonshot gate

**Updated:** 2026-07-24

**Clay status:** unsolved

**Checkpoint:** `EXP-ADJOINT-PRESSURE-FRESHNESS-WITHOUT-FLOOR-001`

**Transition:** freeze the R3B pressure subbranch for external review, then
open ROUTE-R3C

This is replace-not-append working memory.  Durable results live in
[`dossier/status.md`](dossier/status.md), exact metadata in
[`dossier/records/`](dossier/records/README.md), and derivations in their
named experiment notes.

## State in one minute

R3B assumes a smooth finite-energy trajectory before a candidate first
singular time, a uniform terminal weak-\(L^3\) bound, and the conditional
Besov-event genealogy.  None is derived for arbitrary Clay data; Type II is
the separate open ROUTE-R3C.

Every selected event has a positive finite-window adjoint-pressure cost.  The
[current theorem](dossier/experiments/adjoint-pressure-terminal-dissipation-collapse.md)
absorbs entrance energy, current nonlinear work, remote inheritance,
macroscopic shells, and diffusion-boundary leakage into one physical action:

\[
P_n(T)\le C+C\widehat{\mathfrak D}_n(T;r_\bullet)+o_n(1),
\qquad
\widehat{\mathfrak D}_n
=
\sum_{\rho_nR_k\le r_\bullet}
\sqrt{\frac{\widehat\delta_{n,k}}{\rho_nR_k}}.
\]

The [latest theorem](dossier/experiments/adjoint-pressure-logarithmic-heat-schedule.md)
reduces the linear lookback to the minimal logarithmic order certified by the
heat-kernel majorant.  If \(\mu(s)\le\sqrt{s}\,\omega(s)\), it gives the exact
sufficient condition

\[
\sum_j Q_j^{1/4}
\omega(CQ_jr_\bullet^2L^{-2j})^{1/2}<\infty,
\qquad Q_j\asymp1+\log(j+2).
\]

For the saturated log--log family with powers \((\beta,\eta)\), this holds
exactly when \(\beta>2\), or
\(\beta=2,\eta>5/2\).  One fixed scalar history saturates the boundary.
Disjoint solenoidal packets show that Barker's global
\(L^{2+\delta_B}_{t,x}\) gradient gain, even with the energy norm and weak-\(L^3\),
cannot imply it by norms alone; those packets are not NSE solutions.

The [freshness theorem](dossier/experiments/adjoint-pressure-freshness-without-floor.md)
shows that an infinite subsequence of the forced lower bands is automatically
frequency-disjoint; time overlap is harmless and its physical floors satisfy
\(\sum_mT_{j_m}<\infty\).  Even granting next-event scale matching gives only
bounded multiplicity and \(\sum_jT_j<\infty\).  The exact power ancestry
permits this with super-exponential decay.  Overlap alone is not the missing
theorem.

## Exact live fork

### A. Uniform adjoint-cost budget

Closing this conditional subbranch now requires one genuinely NSE-specific
major theorem:

1. the classified terminal Dini gain;
2. a nonsummable scale-zero floor or fixed unnormalised fresh charge;
3. rigidity excluding an infinite decaying signed-flux cascade; or
4. a pressure-visible telescope with an event increment not proportional to
   \(T_j\).

### B. Event-index freshness

Global higher integrability alone is now closed as a shortcut.  Do not reopen
older payer or overlap branches; the recorded theorems already absorb them.

## Next bounded cycle

1. Keep this R3B pressure subbranch frozen pending fresh external review.
2. Read the Clay target and possibility tree for ROUTE-R3C only.
3. Formulate the first exhaustive Type-II entrance alternative without
   importing the weak-\(L^3\) Type-I ceiling.

## Guardrails

- The Albritton--Barker critical-amplitude repair is proof-consistent but
  awaits external confirmation.
- Besov-event and feedback-pressure ancestry remain conditional.
- No critical nested-action bound, fresh payer index, event-index sum, or
  Clay alternative A--D is proved.
- Same-system review is adversarial recomputation, not independent external
  review.
- Tests certify only the finite algebra and bookkeeping they exercise.

## Do not retry unchanged

| Shortcut | Recorded obstruction |
|---|---|
| Energy, absolute continuity, or nesting alone | Finite scalar histories retain divergent critical action. |
| Barker global \(L^{2+\delta_B}\) gradient gain | Disjoint kinematic packets retain arbitrary critical terminal histories. |
| Bounded frequency overlap | It only sums the vanishing \(T_j\); exact event ancestry permits \(\sum_jT_j<\infty\). |
| One natural heat time per scale | Geometric frequencies have a Zeno clock. |
| Adjoint \(L^2\) energy | It stops at the square-root secondary-index law. |
| Positive cumulative flux | One reservoir may pay many nested boundaries. |
| Bare spectral/spatial primal--adjoint telescope | One is pressure-blind; the other can cancel in every gauge. |

Other routes: [2607 audit](dossier/papers/2607.08866-audit.md),
[possibility tree](dossier/possibility-tree.md), and
[HWY bridge](dossier/papers/2509.25116-bridge-note.md).

Before reporting or committing: `make check` and `git diff --check`.
