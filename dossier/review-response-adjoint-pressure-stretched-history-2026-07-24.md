# Review response: stretched feedback history ledger

**Date:** 2026-07-24
**Route:** ROUTE-R3B
**Verdict:** valid as a scalar-ledger realisation
**Clay status:** unsolved

The independent adversarial reviewer audited
[the theorem](experiments/adjoint-pressure-stretched-history.md) against
`review-letter-adjoint-pressure-stretched-history-2026-07-24.md` (archived in Git at `c277792`).
No repair to the claimed result is required.

## Accepted result

For every \(c>0\), \(a>1\), and strictly decreasing
\(h_j\downarrow0\), the definitions

\[
\begin{aligned}
D_j&=h_j^{-3}e^{ch_j^{-7/4}},\\
\sigma_j&=h_j^3e^{-ach_j^{-7/4}},\\
\lambda_j&=e^{-ach_j^{-7/4}},\\
\rho_j&=e^{-(a-1)ch_j^{-7/4}},\\
\delta_j&=h_j^7e^{-2ach_j^{-7/4}}
\end{aligned}
\]

give decreasing nested physical-time and dissipation nodes. One
nonnegative \(e\in L^1(0,\delta_1)\) satisfies

\[
\int_0^{\delta_j}e(s)\,ds
=\rho_j
=\sigma_jD_j
\]

for every \(j\).

## Referee checks

The reviewer independently confirmed:

1. \(\delta(h)\) and \(\rho(h)\) are strictly increasing in \(h\), so
   decreasing \(h_j\) gives correctly ordered nested nodes;
2. the countable piecewise-affine interpolation is genuinely absolutely
   continuous at \(0\), its derivative is nonnegative and integrable,
   and its integral recovers the interpolation on partial as well as
   complete subintervals;
3. both scale ratios and both normalised clocks are exact;
4. the little-\(o\) quotient is exactly \(\rho_j\to0\);
5. fresh history increments telescope to \(\rho_1\), while the
   cumulative packets may all retain normalised value one because they
   are nested rather than disjoint; and
6. the theorem is consistently labelled as scalar-ledger compatibility
   and never promoted to a velocity, pressure, suitable solution, or
   Navier--Stokes construction.

The note now states \(s=-t\) explicitly and includes the
partial-interval proof of
\(F(s)=\int_0^s e\), as optional clarity requested by the reviewer.

## Exact retained boundary

Finite raw physical dissipation, absolute continuity, terminal nesting,
the exact physical scale map, and the stretched-exponential lower bound
do not contradict one another. A successful exclusion must use genuinely
PDE information, a non-reusable signed or vector charge, an actual
event-ancestry relation, or a causal interaction-order improvement.

This verdict does not show that any Navier--Stokes trajectory realises the
ledger, exclude the stretched-exponential feedback branch, prove
regularity or breakdown, or establish any Clay alternative A--D.

## Validation

The reviewer ran:

- the focused executable and all 6 focused tests;
- the full repository suite with 610 tests;
- records, links, and mathematical-markup validation; and
- `git diff --check`.

All passed.
