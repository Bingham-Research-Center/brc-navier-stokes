# Handoff: current Navier--Stokes moonshot gate

**Updated:** 2026-07-24

**Clay status:** unsolved

**Checkpoint:** `EXP-ADJOINT-PRESSURE-TERMINAL-DISSIPATION-COLLAPSE-001`

**Live route:** ROUTE-R3B, conditional weak-\(L^3\) Type-I regularity

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

Here \(\widehat\delta_{n,k}\) is global physical dissipation on nested
common-endpoint intervals spanning the staggered prehistory and current
window.  A terminal modulus \(s^\alpha\) controls the action for
\(\alpha>1/2\).  Scalar nested histories still diverge at \(\alpha=1/2\);
that is a sharp scalar obstruction, not an NSE trajectory.

The separate actual-NSE flux theorem forces a positive terminal high-pass
flux and a fixed fractional lower-band dissipation decrement at every late
event.  It has not yet been coupled to the action above strongly enough to
prevent reuse of overlapping intervals and bands.

## Exact live fork

### A. Uniform adjoint-cost budget

Control \(\widehat{\mathfrak D}_n\) at the critical \(s^{1/2}\) endpoint by
one genuinely NSE-specific input:

1. a logarithmic/Dini terminal dissipation gain;
2. non-reuse or bounded overlap of the nested intervals;
3. the already forced lower-band decrement; or
4. fresh event charges paid by one finite same-trajectory budget.

Do not reopen the older payer branches; the current theorem already absorbs
them.

### B. Event-index freshness

Prove a scale-zero event floor, bounded time-frequency overlap,
non-Zeno/intervening-event law, or pressure-visible cross-event telescope.
The decrement excludes only a near-lossless distinct-shell cascade;
geometrically decaying overlapping events survive.

## Next bounded cycle

1. Replace the linear heat-lookback schedule by the smallest summable one and
   derive the exact critical Dini series.
2. Determine the sharp logarithmic threshold with one fixed scalar history.
3. Test whether the available weak-\(L^3\) higher-integrability or decrement
   implies that threshold on the actual trajectory.
4. If it does not, record the precise missing PDE estimate and stop this
   branch for fresh-context external review rather than generate another
   chain of equivalent ledgers.

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
| One natural heat time per scale | Geometric frequencies have a Zeno clock. |
| Adjoint \(L^2\) energy | It stops at the square-root secondary-index law. |
| Positive cumulative flux | One reservoir may pay many nested boundaries. |
| Bare spectral/spatial primal--adjoint telescope | One is pressure-blind; the other can cancel in every gauge. |

Other routes: [2607 audit](dossier/papers/2607.08866-audit.md),
[possibility tree](dossier/possibility-tree.md), and
[HWY bridge](dossier/papers/2509.25116-bridge-note.md).

Before reporting or committing: `make check` and `git diff --check`.
