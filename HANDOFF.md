# Handoff: current Navier--Stokes moonshot gate

**Updated:** 2026-07-24

**Clay status:** unsolved

**Mathematical checkpoint:** `EXP-ADJOINT-PRESSURE-SPATIAL-HIGHPASS-PAYER-001`

**Live route:** ROUTE-R3B, conditional weak-\(L^3\) Type-I regularity

This file is current state, not chronology. Canonical metadata lives in
[`dossier/records/`](dossier/records/README.md), proof detail in the linked
experiment notes, and the pre-slim narrative remains recoverable with

```bash
git show a7ae140:HANDOFF.md
git show a7ae140:dossier/status.md
```

## State in one minute

The project has not solved any Clay alternative. The active branch assumes a
smooth finite-energy trajectory before a candidate first singular time,
together with a uniform terminal weak-\(L^3\) bound and the conditional
Besov-event genealogy constructed in the R3B chain. Closing this branch would
be a substantial Type-I theorem, not a Clay solution; Type II remains in
ROUTE-R3C.

The structural reduction produces a nonzero coherent ancient suitable
weak-\(L^3\) distance profile with two locally finite terminal singular
points and a recurring positive Albritton--Barker quotient defect. The
shortest proof route is:

1. [terminal Besov ancestry](dossier/experiments/terminal-besov-ancestry.md);
2. [ancient outer profile](dossier/experiments/terminal-outer-profile.md);
3. [two-point distance profile](dossier/experiments/terminal-distance-profile.md);
4. [parabolic scale hull](dossier/experiments/parabolic-scale-hull.md);
5. [defect-event suspension](dossier/experiments/defect-event-suspension.md).

Every event forces a finite-window
[adjoint-pressure packet](dossier/experiments/adjoint-pressure-packets.md).
The exhaustive feedback analysis then forces a physical coefficient tail
above a superparabolic cutoff:

\[
D_{b,>\,h^{-1/2}\sqrt{\log(1/h)}}^\chi(h)
\gtrsim_\varepsilon h^{-3+\varepsilon}.
\]

The latest same-trajectory chain converts that tail into a sharper physical
statement:

- [tail-to-flux](dossier/experiments/adjoint-pressure-parabolic-flux.md)
  gives annular dissipation, inherited entrance energy, or positive signed
  high-pass input;
- [terminal flux ancestry](dossier/experiments/adjoint-pressure-inherited-ancestry.md)
  removes the first two bookkeeping alternatives at an adaptive boundary;
- [weak-\(L^3\) flux decrement](dossier/experiments/adjoint-pressure-flux-decrement.md)
  forces a fixed fractional loss in the lower comparable band.

For every sufficiently late event there are terminal intervals
\(\widetilde J_j\), cutoffs \(K_j/\Lambda_j\to1\), and floors \(T_j>0\)
such that

\[
\Phi_{K_j}(\widetilde J_j)\ge\frac{\nu T_j}{4},
\qquad
\nu\int_{\widetilde J_j}
\|\nabla Q_{\eta K_j<|\xi|\le K_j}v\|_2^2\,dt
\ge
c\left(\frac{\nu}{M}\right)^2
\Phi_{K_j}(\widetilde J_j).
\]

This excludes the near-lossless distinct-shell ledger. It does not make
different events fresh: the intervals and bands can overlap, \(T_j\to0\),
and an infinite geometrically decaying cascade may still have finite total
physical cost.

## Exact live fork

Do not enumerate another pressure mechanism before addressing one of these
two gates.

### A. Uniform adjoint-cost budget

For the physical genealogy \(\mathcal G=\{(u_n,H_n)\}\), determine whether

\[
\mathfrak p^\mathcal G_{\psi,T}
=
\liminf_{\substack{n\to\infty\\H_n\ge T}}
\frac1{\sqrt{\nu T}}
\int_0^T\|\nabla\pi^*_{n,\psi}\|_1\,dt
\]

has a finite upper bound for one nontrivial compact solenoidal test, uniformly
at the required event scales, or prove a sharp obstruction. The lower bound is
already established in
[adjoint-pressure history](dossier/experiments/adjoint-pressure-history.md).

The [conditional annular cost theorem](dossier/experiments/adjoint-pressure-annular-cost.md)
removes the nonuniform global-\(L^2\) factor and leaves an exact
\(R_k^{-1/2}\) exterior-adjoint endpoint. The subsequent
[nonlinear-regeneration theorem](dossier/experiments/adjoint-pressure-nonlinear-regeneration.md)
removes passive low frequencies and remote linear inheritance. The latest
[parabolic-regeneration theorem](dossier/experiments/adjoint-pressure-parabolic-regeneration.md)
replaces the common remote horizon by one shell heat time and removes every
aggregate shell range staying at positive physical radius. For any fixed
admissible \(r_\bullet>0\),

\[
\int_0^T\|\nabla\pi^*_{n,\psi}\|_1\,dt
\le C+C\mathfrak Q_n(T;r_\bullet)+o(1),
\]

where \(\mathfrak Q_n\) is the high-frequency nonlinear Duhamel action on
shells \(\rho_nR_k\le r_\bullet\), using only the preceding heat time
\(R_k^2/\nu\). Divergent pressure histories force this aggregate action to
diverge below every fixed admissible \(r_\bullet\); a further diagonal reaches
scale zero.

The new
[spatial high-pass payer theorem](dossier/experiments/adjoint-pressure-spatial-highpass-payer.md)
uses an exact local filtered-energy identity to prove

\[
\mathfrak Q_n\le C+C\mathfrak E_n+C\mathfrak F_n,
\]

where \(\mathfrak E_n\) is entrance high-pass energy and
\(\mathfrak F_n\) is positive spatially cut-off nonlinear work, both with
the endpoint adjoint square-root weights. Spatial diffusion-boundary leakage
is summable. Divergent pressure histories force
\(\mathfrak E_n+\mathfrak F_n\to\infty\) below every fixed physical cutoff.
An exact endpoint-weighted scalar array shows why finite physical quadratic
payer totals, proportional decrements, and natural heat clocks still yield
neither one charged block nor event freshness. The array is not an NSE,
Duhamel, or adjoint construction; source localisation, non-diffuse structure,
and external review remain open.

### B. Event-index freshness

Use the forced lower-band decrement to prove one of:

1. bounded time-frequency overlap;
2. a scale-zero event floor;
3. a non-Zeno cascade-speed bound;
4. an intervening selected Besov event; or
5. a genuinely pressure-visible cross-event telescope.

Bare spectral and spatial primal--adjoint telescopes are closed:
[spectral pairing](dossier/experiments/adjoint-pressure-spectral-pairing.md)
is pressure-blind, while the
[spatial current](dossier/experiments/adjoint-pressure-spatial-pairing.md)
can cancel in every gauge.

## Standing assumptions not yet derived

- The R3B branch begins inside a weak-\(L^3\) Type-I scenario.
- The proof-consistent critical-amplitude reading of Albritton--Barker
  Theorem 4.1 still needs external mathematical confirmation.
- The selected Besov-event and feedback-pressure genealogy is conditional.
- No finite payer index, non-diffuse block theorem, or event-index sum is known.

## Closed shortcuts: do not retry unchanged

| Shortcut | Exact obstruction |
|---|---|
| Raw energy, absolute continuity, or terminal nesting | Positive physical costs can be summable. |
| Positive cumulative flux | One reservoir can pay many nested boundaries. |
| Natural heat time per frequency step | Geometric frequencies have a Zeno clock. |
| Adjoint \(L^2\) energy | It stops at the missing Lorentz secondary index and square-root law. |
| Critical positive scalar majorants | Their Volterra spectral radius stays order one. |
| Source-localised feedback payer | [Intermediate localisation](dossier/experiments/adjoint-pressure-intermediate-localization.md) makes its antecedent empty. |
| Bare next-event cutoff matching | The sharp \(7/6\) log-scale ceiling still allows infinite mean. |
| Near-lossless shell cascade | The new lower-band decrement excludes it, but geometric decay survives. |
| Bare local high-pass payer identity | An abstract endpoint-weighted array has divergent square-root action but vanishing individual and total physical quadratic charges. |

The broader failure catalogue is indexed in
[`dossier/status.md`](dossier/status.md) and the canonical
[experiment ledger](dossier/records/experiments.json).

## Next actions

1. Seek an NSE-specific non-diffusion estimate, active-block bound, source
   coherence law, entrance ancestry, or signed cross-event telescope for
   \(\mathfrak E_n+\mathfrak F_n\).
2. If one yields fixed blocks, test whether their decrement packets embed
   additively; otherwise test the diffuse ledger against the regenerated
   endpoint profile.
3. Allow at most five new frontier attempts without a cost/freshness theorem,
   an unconditional NSE statement, or a decisive no-go; then consolidate.
4. Prepare fresh-context external review packets for the adjoint-cost theorem,
   the Albritton--Barker repair, and the terminal flux/decrement pair.
5. Revisit ROUTE-R3C explicitly before describing any R3B closure as movement
   close to Clay.

## Other routes, on demand

- Repaired 2607 conditional theorem:
  [audit](dossier/papers/2607.08866-audit.md) and
  [proof map](dossier/papers/2607.08866-proof-map.md).
- Full route tree: [possibility tree](dossier/possibility-tree.md).
- Breakdown/HWY bridge:
  [2509.25116 note](dossier/papers/2509.25116-bridge-note.md).

## Control rules

- Same-system agent review is adversarial recomputation, not independent
  external review.
- Tests certify only the exact algebra and bookkeeping they exercise.
- Replace stale handoff text; never append a research diary here.
- Before reporting or committing, run `make check` and `git diff --check`.
