# Independent review request: one prescribed multistage Oseen itinerary

**Date:** 2026-07-24

**Route:** ROUTE-R3B

**Clay status claimed by author:** unsolved

Please review
[`experiments/adjoint-pressure-multistage-path.md`](experiments/adjoint-pressure-multistage-path.md)
adversarially.  The proposed theorem starts with the independently
reviewed high-to-annular state \(w_0\), applies \(m\) further actual
annular heat--Leray Oseen blocks along one prescribed frequency
itinerary, and then observes pressure below a fixed frequency \(S\).

The main claim is

\[
\mathfrak R_{\boldsymbol R}(h)
\le
C_{\rm src}A_pA_x^m
\frac{S}{R_0}
\Theta_{\boldsymbol R}(h)
\mathcal B(h,R_0),
\]

where

\[
\Theta_{\boldsymbol R}(h)
=
\mathbb P(X_0+\cdots+X_m\le h),
\qquad
X_j\sim{\rm Exp}(c_0\nu R_j^2)
\]

independently.  In particular, all intermediate frequency ratios are
claimed to telescope:

\[
\prod_{j=1}^m\frac{R_{j-1}}{R_j}
=
\frac{R_0}{R_m},
\]

and the initial heat mass, final pressure factor, and this product leave
exactly \(S/R_0\).

Please try to falsify, in particular:

1. the indexing: \(w_0\) already contains the first high-to-\(R_0\)
   return, while \(m\) counts only later state interactions;
2. the cross-band normalisation
   \[
   C_xMR_{j-1}R_je^{-c_0\nu R_j^2t}
   =
   A_x(R_{j-1}/R_j)e_j(t);
   \]
3. the initial factor
   \((c_0\nu R_0^2)^{-1}\) and final pressure factor
   \(C_pMSR_m\);
4. the exact telescoping to \(A_pA_x^mS/R_0\);
5. the use of positive scalar majorants and Tonelli without identifying
   them with the signed vector Oseen operator;
6. the convolution-CDF identity for \(m+1\) independent exponential
   clocks;
7. both clock ceilings
   \[
   \Theta\le\min(1,c_0\nu R_0^2h),
   \qquad
   \Theta\le
   \frac{h^{m+1}}{(m+1)!}\prod_{j=0}^m\lambda_j;
   \]
8. the subset-clock bound (28);
9. for \(R_j=2^{-j}R_0\), the rate-product factor
   \(2^{-m(m+1)}\);
10. the slow-clock corollary
    \[
    \Theta\le 2^{-n(n-1)}/n!;
    \]
11. the fixed-depth inversion, including that it reproduces
    \[
    \gamma_1(\beta)
    =
    9/4+|\beta-1/2|;
    \]
12. the logarithmic-depth correction: with interaction loss
    \(\delta=\kappa\log_+A\), the coarse inversion requires the stricter
    condition
    \(\delta<p(\beta)=\beta+(1-2\beta)_+\), because otherwise the
    constant term need not vanish;
13. whether \(A=\max(A_x,A_p)\) is adequate when \(A<1\); and
14. the scope boundary: this is one prescribed iterated component, not
    a path decomposition, entropy bound, recombination theorem,
    participation result, Oseen singularity, Navier--Stokes singularity,
    or Clay resolution.

Please also flag any missing hypothesis on the annular cutoffs,
frequency ordering, tensor orientation, \(M\), or viscosity.

Classify the disposition as:

- valid in the exact stated conditional scope;
- repairable, with precise corrections; or
- invalid, identifying the first fatal implication.

The executable certificate is:

```bash
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_multistage_path -v
PYTHONPATH=lab python -m \
  navier_lab.adjoint_pressure_multistage_path
```
