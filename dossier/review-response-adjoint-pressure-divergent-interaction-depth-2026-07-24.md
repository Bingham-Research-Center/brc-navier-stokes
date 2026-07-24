# Review response: logarithmically divergent causal interaction depth

**Date:** 2026-07-24
**Route:** ROUTE-R3B
**Verdict:** valid after geometric repair and quantitative sharpening
**Clay status:** unsolved

The independent adversarial reviewer audited
[the theorem](experiments/adjoint-pressure-divergent-interaction-depth.md)
against the
`review-letter-adjoint-pressure-divergent-interaction-depth-2026-07-24.md` (archived in Git at `c277792`)
in three passes.

## Accepted theorem

Let

\[
u_0=q,
\qquad
u_m=T_b^mq,
\qquad
(T_bz)(t)
=
\int_0^t e^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}(z\otimes b)(s)\,ds.
\]

Every fixed iterate has vanishing complete pressure.  More strongly,
there are constants \(c_{\rm dep}>0\) and \(h_0>0\) such that, with

\[
N(h)=\left\lfloor c_{\rm dep}\log\frac1h\right\rfloor,
\qquad
R_{N+1}=r-\sum_{m=1}^Nu_m=T_b^Nr,
\]

the selected feedback packet satisfies

\[
\int_0^h
\|\mathcal T(R_{N(h)+1},b)(t)\|_1\,dt
\ge\frac{p_r}{2}
\]

for every selected \(0<h<h_0\).

Thus the pressure persists in Dyson remainders of at least logarithmically
growing causal depth.  This does not sum the infinite Dyson expansion
or exclude feedback.

## First-pass findings

The reviewer accepted:

1. the global energy and \(L^1\)--\(L^{3/2,1}\) recurrences;
2. the differentiated projected Stokes-kernel estimate;
3. the noncircular exterior gradient, \(L^{6,2}\), and \(L^2\)
   induction at every fixed order;
4. all \(\beta_m\), intermediate, and exterior-shell exponents; and
5. the exact finite Dyson remainder equation and pressure-floor
   transfer.

One required textual repair was made: the near-pressure estimate uses
the global \(L^2\) estimate, not the gradient estimate.

## Required geometric repair

The first quantitative draft understated the radius threshold.  One
order uses \(R/2\) in the source split and \(R/2\) again in the cutoff
Lorentz--Sobolev step.  Hence a full order reaches the preceding
\(L^{6,2}\) tail at \(R/4\), not \(R/2\).  The corrected estimates use

\[
R_m^{\min}=C_\nu4^m
\]

and the worst full-step radius coefficient is

\[
4^{15}=2^{30}.
\]

The reviewer confirmed that this remains a fixed exponential loss and
does not alter the logarithmic-depth conclusion.

## Accepted optimisation and constant ledger

The exact global exponents are

\[
A_m=\frac74-\frac32\,3^{-m},
\qquad
B_m=\frac54-\frac12\,3^{-m},
\qquad
\beta_m=\frac{11}{2}-3^{-(m-1)}.
\]

All norm coefficients grow at most like \(C_0\Lambda^m\), and all
squared-tail coefficients grow at most like
\(C_0^2\Lambda^{2m}\), for one fixed \(\Lambda\ge2\).

Optimising the intermediate split at
\(\alpha=1/4\) gives the five pressure powers

\[
\frac{11}{8},
\qquad
\frac{17}{8},
\qquad
\frac{\beta_m}{2}-\frac78,
\qquad
\frac{11}{8},
\qquad
\frac{13}{8}.
\]

Their minimum is \(11/8\), attained at \(m=1\).  The reviewer confirmed
that \(\alpha=1/4\) globally maximises this minimum.  Therefore

\[
\int_0^h\|\mathcal T(u_m,b)(t)\|_1\,dt
\le C_0\Lambda^m h^{11/8}
\]

whenever \(h^{-1/4}\ge C_\nu4^m\).

Choosing

\[
c_{\rm dep}\le
\min\left\{
\frac{11}{32\log\Lambda},
\frac{1}{16\log2}
\right\}
\]

gives

\[
\Lambda^{N(h)}\le h^{-11/32},
\qquad
4^{N(h)}\le h^{-1/8}\ll h^{-1/4},
\]

and hence

\[
\sum_{m=1}^{N(h)}
\int_0^h\|\mathcal T(u_m,b)(t)\|_1\,dt
\le Ch^{33/32}\longrightarrow0.
\]

## Exact retained boundary

The theorem proves persistence beyond
\(c_{\rm dep}\log(1/h)\) causal feedback interactions.  It does not:

- improve the exponential interaction ledger to a summable one;
- prove quasi-nilpotence or convergence of the infinite Dyson series;
- identify a positive pressure contribution from one individual high
  iterate;
- exclude the full feedback or inverse-\(15/4\) direct branch; or
- prove regularity, breakdown, or any Clay alternative A--D.

The next gate is an Oseen time-ordering theorem stronger than the
present exponential ledger, or another genuinely PDE causal law
excluding pressure that persists at logarithmically divergent depth.

## Validation

The final reviewed state passed:

- the focused executable and all 10 focused tests;
- records validation with 34 sources, 29 claims, 23 routes,
  89 experiments, and 16 obligations;
- links and mathematical-markup validation;
- the full repository suite with 626 tests; and
- `git diff --check`.

The reviewer made no file edits.
