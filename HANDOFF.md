# Handoff: current Navier--Stokes moonshot gate

**Updated:** 2026-07-24

**Clay status:** unsolved

**Checkpoint:** `EXP-ADJOINT-PRESSURE-STAGGERED-ENTRANCE-ANCESTRY-001`

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
+C\mathfrak F_n(T;r_\bullet)
+C\mathfrak D_n^{\rm stag}(T;r_\bullet)
+o_n(1).
\]

Here:

- \(\mathfrak F_n\) is adjoint-weighted positive nonlinear work into
  spatially cut-off high-pass velocity on the current window;
- \(\mathfrak D_n^{\rm stag}\) is the nested physical action
  \[
  \sum_{\rho_nR_k\le r_\bullet}
  \left(\frac{\delta_{n,k}}{\rho_nR_k}\right)^{1/2},
  \]
  with \(\delta_{n,k}\) the physical dissipation on a common-endpoint
  staggered ancestry interval.

The new
[staggered-ancestry theorem](dossier/experiments/adjoint-pressure-staggered-entrance-ancestry.md)
uses \(\gamma(j+1)\) heat times on the \(j\)-th inward shell.  The physical
lookbacks remain uniformly bounded because
\((j+1)L^{-2j}\) is bounded, while inherited high frequencies decay
exponentially in \(j\).  Entrance high-pass energy is therefore no longer an
independent payer.

The remaining zero-data response has exact nonnegative auxiliary work and the
same-trajectory ceiling

\[
\Psi_{n,k}\lesssim \frac{M^2}{\nu}\Delta_{n,k}.
\]

This is forced-heat bookkeeping, not a new NSE flux sign.  After physical
pullback it yields \(\mathfrak D_n^{\rm stag}\).  A terminal dissipation
modulus \(s^\alpha\) controls this action for every \(\alpha>1/2\).  A
triangular scalar family survives at \(\alpha=1/2\), so the power boundary is
sharp for scalar histories; it is not a one-trajectory NSE counterexample or
a classification of critical logarithmic moduli.

Adversarial same-system recomputation accepted the theorem after correcting
the nesting calculation and threshold scope.  External mathematical review
is pending.

## Exact live fork

### A. Uniform adjoint-cost budget

Obtain at least one genuinely NSE-specific estimate:

1. bound \(\mathfrak F_n\) through source coherence, an active-block law, or a
   signed spatial transfer;
2. bound \(\mathfrak D_n^{\rm stag}\) at the critical \(s^{1/2}\) endpoint,
   perhaps with a logarithmic gain or non-reuse of nested intervals; or
3. convert divergence of either aggregate into individually fresh event
   charges paid by one finite same-trajectory budget.

Do not reintroduce entrance energy, remote linear inheritance, macroscopic
shells, or diffusion-boundary leakage as separate branches; those are
summed or re-expressed by the current chain.

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
- No finite current-work budget, critical nested-action bound, fresh payer
  index, or event-index sum is known.

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

1. Test whether spatial localisation of the staggered source controls
   \(\mathfrak F_n\) or creates bounded overlap with
   \(\mathfrak D_n^{\rm stag}\).
2. Analyse critical and logarithmically improved terminal dissipation moduli
   using actual NSE structure, not another free scalar ledger.
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
