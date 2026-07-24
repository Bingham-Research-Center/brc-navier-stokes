# Adversarial review request: divergent causal interaction depth

**Date:** 2026-07-24
**Route:** ROUTE-R3B
**Clay status:** unsolved

Please audit the proposed
[interaction-depth theorem](experiments/adjoint-pressure-divergent-interaction-depth.md).
The first claim is that every fixed finite Stokes--Duhamel feedback
iterate has vanishing complete adjoint-pressure cost.  The quantitative
sharpening tracks the constants and radius threshold exponentially in
the order and concludes that the reviewed packet remains after
\(c\log(1/h)\) interactions.

## Exact setup

The reviewed zero-data remainder solves

\[
\partial_t r-\nu\Delta r-\mathbb P(b\cdot\nabla r)
=\mathbb P(b\cdot\nabla q),
\qquad r(0)=0,
\]

with a fixed pressure floor.  Define

\[
(T_bz)(t)
=
\int_0^t e^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}(z\otimes b)(s)\,ds,
\qquad
u_0=q,\quad u_m=T_b^mq.
\]

For fixed \(N\), put

\[
R_{N+1}=r-\sum_{m=1}^Nu_m.
\]

The proposed conclusions are

\[
\int_0^h\|\mathcal T(u_m,b)\|_1\,dt=o_m(1)
\quad\text{for every fixed }m,
\]

and

\[
\partial_tR_{N+1}-\nu\Delta R_{N+1}
-\mathbb P(b\cdot\nabla R_{N+1})
=\mathbb P(b\cdot\nabla u_N),
\]

with at least half the fixed pressure floor for all sufficiently small
\(h\) depending on \(N\).

## New induction

The global time exponents are

\[
A_m=\frac74-\frac32\,3^{-m},
\qquad
B_m=\frac54-\frac12\,3^{-m},
\]

where

\[
\|u_m(t)\|_1\lesssim_m t^{A_m},
\quad
\|u_m(t)\|_2\lesssim_m t,
\quad
\|u_m(t)\|_{L^{3/2,1}}\lesssim_m t^{B_m}.
\]

For \(m\ge1\), set

\[
\beta_m=\frac{11}{2}-3^{-(m-1)}.
\]

The proposed simultaneous exterior induction is

\[
\int_0^h\|u_m\|_{L^2(|x|>R)}^2dt
\lesssim_m
h^{\beta_m}R^{-5}
+h^4R^{-7}
+h^{5/2}R^{-15},
\]

and

\[
\int_0^h
\left(
\|\nabla u_m\|_{L^2(|x|>R)}^2
+\|u_m\|_{L^{6,2}(|x|>R)}^2
\right)dt
\lesssim_m
h^3R^{-7}+h^{3/2}R^{-15}.
\]

At the intermediate radius \(L=h^{-1/10}\), the five pressure powers
are

\[
\frac{29}{20},\quad
\frac{41}{20},\quad
\frac{\beta_m}{2}-\frac54,\quad
\frac{17}{20},\quad
\frac12.
\]

The third is minimal at \(m=1\), where it equals \(1\).  Exterior
coefficient shells give

\[
h^{\beta_m/2+6}+h^{11}+h^{89/4}.
\]

## Quantitative sharpening after the first review pass

The first independent pass accepted the fixed-\(m\) induction, requested
only that the near-pressure citation use the global \(L^2\) estimate,
and asked that the repeated radius-halving threshold be explicit.  Both
repairs are now made.

The sharpened proof records constants \(C_0>0\) and \(\Lambda\ge2\)
such that global norm coefficients are at most
\(C_0\Lambda^m\), squared-tail coefficients are at most
\(C_0^2\Lambda^{2m}\), and the tail estimates apply for
\(R\ge C_\nu4^m\).  The \(4^m\) records two nested radius halvings per
full induction order, correcting the \(2^m\) threshold rejected in the
second review pass.  In particular,

\[
\int_0^h\|\mathcal T(u_m,b)\|_1\,dt
\le C_0\Lambda^mh^{11/8}
\]

after optimising the intermediate split at
\(\alpha=1/4\), where the five pressure powers are
\(11/8,17/8,\beta_m/2-7/8,11/8,13/8\).
When \(h^{-1/4}\ge C_\nu4^m\), choose

\[
N(h)=\left\lfloor c_{\rm dep}\log\frac1h\right\rfloor,
\qquad
c_{\rm dep}\le
\min\left\{
\frac{11}{32\log\Lambda},
\frac{1}{16\log2}
\right\},
\]

gives

\[
\sum_{m=1}^{N(h)}
\int_0^h\|\mathcal T(u_m,b)\|_1\,dt
\lesssim h^{33/32}\to0.
\]

Hence \(R_{N(h)+1}\) retains at least half the pressure floor.

## Questions requiring an explicit verdict

1. Is the energy induction
   \(\sup\|u_m\|_2^2+\int\|\nabla u_m\|_2^2\lesssim_m t^2\)
   valid from only the uniform weak-\(L^3\) drift
   ceiling and Lorentz--Sobolev?
2. Does
   \(L^1\cap L^2\hookrightarrow L^{3/2,1}\) have the stated
   multiplicative exponents, and are the recurrences for \(A_m,B_m\)
   exact?
3. Does the kernel of
   \(e^{\nu\theta\Delta}\mathbb P\operatorname{div}\) satisfy the
   differentiated off-diagonal \(L^2\) bound \(CR^{-7/2}\) uniformly in
   the required region?
4. Is the spatial inner/outer source split exact despite the Leray
   projection, with no cutoff derivative or omitted nonlocal term?
5. Does the outer-source zero-data Stokes energy estimate propagate the
   gradient tail, and does time--space Young convolution add exactly one
   power of \(h\) to the squared \(L^2\) tail?
6. Does the cutoff Lorentz--Sobolev inequality close the simultaneous
   \(L^2\), gradient, and \(L^{6,2}\) induction without circularity?
7. Are \(\beta_m\), all three exterior-tail powers, and all five
   intermediate pressure powers exact?
8. Can the reviewed Bogovskii and dyadic coefficient-shell arguments be
   reused at every fixed \(m\) with constants independent of \(h\)?
9. Is the Dyson remainder equation exact, including indexing and signs,
   and does pressure bilinearity transfer the floor after a finite
   truncation?
10. Do the displayed coefficient recurrences genuinely give at most
    exponential growth uniformly in \(m\), including interpolation,
    beta factors, both radius halvings, source squaring, Bogovskii, and shell
    summation?
11. Does the simultaneous restriction
    \(\Lambda^m h^{11/8}\to0\) and \(4^m\ll h^{-1/4}\) justify the stated
    \(N(h)=\lfloor c\log(1/h)\rfloor\) truncation and its
    \(O(h^{33/32})\) pressure sum?  Is \(\alpha=1/4\) genuinely the
    maximiser of the minimum pressure power?
12. Does any step silently require convergence of the infinite Dyson
    series, a strong \(L^3\) drift, an endpoint adjoint on the rough
    profile, or finite propagation?
13. Is “requires logarithmically divergent causal interaction depth”
    accurate when formulated as persistence in the Dyson remainder
    \(R_{N(h)+1}\), without attributing the pressure to one positive
    iterate?
14. Is the conclusion correctly bounded away from feedback exclusion,
    the inverse-\(15/4\) direct branch, and any Clay alternative A--D?

Please be especially suspicious of the simultaneous exterior induction:
look for an unrecognised annular cutoff term, use of the current
iterate's \(L^{6,2}\) tail before it is proved, or a Stokes maximal
regularity estimate that is unavailable for the restricted source.

## Executable checks

```bash
make adjoint-pressure-interaction-depth
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_interaction_depth -v
make records
make links
make markup
git diff --check
```
