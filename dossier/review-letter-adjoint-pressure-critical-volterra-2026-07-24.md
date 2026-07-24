# Adversarial review request: critical scalar Oseen--Volterra obstruction

**Date:** 2026-07-24
**Route:** ROUTE-R3B
**Clay status:** unsolved

Please audit the proposed
[critical Oseen--Volterra reduction](experiments/adjoint-pressure-critical-volterra.md).
The preceding reviewed theorem leaves a pressure packet beyond
\(c\log(1/h)\) heat-feedback interactions.  This note tests whether
critical causal time ordering or Barker's published higher-integrability
gain can sum the remaining interaction chain.

## Proposed conclusions

The proposed theorem has four deliberately separated parts.

1. The positive critical scalar operator
   \[
   (\mathsf H_\gamma f)(t)
   =
   B(\gamma,1-\gamma)^{-1}
   \int_0^t(t-s)^{\gamma-1}s^{-\gamma}f(s)\,ds
   \]
   obeys \(\mathsf H_\gamma^m1=1\) for every \(m\), and therefore is
   causal but not quasi-nilpotent.
2. Replacing \(s^{-\gamma}\) by
   \(s^{-\gamma+\varepsilon}\), \(\varepsilon>0\), gives
   \[
   \mathsf H_{\gamma,\varepsilon}^{\,m}1(t)
   =
   t^{m\varepsilon}
   \prod_{j=1}^m
   \frac{B(\gamma,1-\gamma+j\varepsilon)}
        {B(\gamma,1-\gamma)}
   \]
   and an \(O(C^m/(m!)^\gamma)\) operator-norm bound.
3. If \(\nabla b\in L^{2+\delta}_{x,t}\), homogeneous Sobolev gives
   \(b\in L^p_tL^q_x\) with
   \[
   p=2+\delta,\qquad
   q=\frac{3(2+\delta)}{1-\delta}.
   \]
   The same-space Oseen heat-kernel/Hölder margin is
   \[
   \varepsilon_{\rm O}
   =
   \frac{2\delta-1}{2(2+\delta)},
   \]
   positive exactly for \(\delta>1/2\).
4. Barker's proof constructs
   \[
   \delta_B
   =
   \frac{3C_{5,\rm univ}}{12M+6C_{5,\rm univ}}
   =
   \frac{C_{5,\rm univ}}{4M+2C_{5,\rm univ}}
   <\frac12,
   \]
   so its exact Oseen margin is
   \[
   -\frac{2M}{8M+5C_{5,\rm univ}}<0.
   \]

The note concludes only that a positive norm-only critical Volterra
majorant, Barker's present exponent, endpoint interpolation, and a
Lebesgue-exponent staircase do not close the infinite-depth causal gate.
It does not assert that the true Oseen operator fails to be
quasi-nilpotent.

## Primary-source anchor

The exact arXiv v2 source of Tobias Barker,
*Higher Integrability and the Number of Singular Points for the
Navier--Stokes Equations with a Scale-Invariant Bound*,
is cached under
`lab/cache/arxiv/2111.14776v2/source.tex`.

- Lines 529--535 choose \(q=2+C_{5,\rm univ}/M\) and state the resulting
  higher-integrability input.
- Lines 559--570 give the nonlinear maximal-regularity exponent
  \(2+3C_{5,\rm univ}/(12M+6C_{5,\rm univ})\).
- Lines 572--574 put the heat term in the same exponent away from the
  restart time and conclude the corollary.

The cached source remains ignored and is not a review artefact.

## Questions requiring an explicit verdict

1. Is the beta-integral identity exact, including its parameter range,
   and does positivity justify
   \(r(\mathsf H_\gamma)=1\)?
2. Is the subcritical iterate formula indexed correctly?
3. Does the gamma-ratio bound really imply the stated
   \(C^m/(m!)^\gamma\) operator-norm estimate and summability?
4. Is the scalar countermodel scoped narrowly enough, given that its
   coefficient is in weak rather than strong \(L^{1/\gamma}_t\)?
5. Does
   \(\nabla b\in L^{2+\delta}_{x,t}\), together with the inherited
   whole-space normalisation, rigorously give
   \(b\in L^{2+\delta}_tL^{3(2+\delta)/(1-\delta)}_x\)?
6. Is the projected differentiated heat-kernel exponent
   \[
   \vartheta=\frac12+\frac3{2q}
   =\frac3{2(2+\delta)}
   \]
   correct for same-space \(L^a\) iteration?
7. Does time Hölder give exactly
   \(1-\vartheta-1/p\), and is its positivity equivalent to both
   \(\delta>1/2\) and the strict Serrin inequality?
8. Is the finite-partition triangular-block proof of
   quasi-nilpotence valid when the margin is positive?
9. For varying exponents, is
   \[
   \sum_{m=1}^N\varepsilon_m
   =
   N\varepsilon_{\rm O}
   -\frac32(1/a_0-1/a_N)
   \]
   exact, and does it rule out an arbitrarily long all-positive
   Lebesgue-exponent staircase when \(\delta<1/2\)?
10. Does interpolation with \(L^\infty_tL^{3,\infty}_x\) retain a
    strictly super-Serrin index for every positive interpolation weight?
11. Is the exponent extracted from Barker's proof exactly (or at least
    no larger than) the displayed \(\delta_B\), and are the derived
    negative margin and positive packet radius power exact?
12. At \(\delta=1/2\), does homogeneous Sobolev give
    \(b\in L^{5/2}_tL^{15}_x\), placing the actual velocity on the
    classical Prodi--Serrin line?
13. Does any claim silently upgrade a scalar majorant into an Oseen
    counterexample, confuse strong and weak endpoint time spaces, or
    claim pressure-\(L^1\) summability from an \(L^a\) operator theorem?
14. Is the final open question correctly restricted to
    Oseen-specific cancellation, tensor sign, solenoidal projection,
    pressure cancellation, or same-trajectory ancestry?

Please look especially for a hidden endpoint Hardy inequality, an
incorrect use of homogeneous Sobolev on \(\mathbb R^3\), or an invalid
spectral argument for the triangular Volterra operator.

## Executable checks

```bash
make adjoint-pressure-critical-volterra
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_critical_volterra -v
make markup
git diff --check
```
