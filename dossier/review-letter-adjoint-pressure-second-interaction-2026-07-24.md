# Adversarial review request: second causal feedback interaction

**Date:** 2026-07-24
**Route:** ROUTE-R3B
**Clay status:** unsolved

Please audit
[the proposed theorem](experiments/adjoint-pressure-second-interaction.md).
The claim is that the first heat-mediated response inside the reviewed
zero-data Oseen feedback remainder has vanishing total adjoint-pressure
cost. Hence any fixed feedback packet must lie at causal drift depth at
least two.

## Exact decomposition

The reviewed feedback remainder solves

\[
\partial_\tau r-\nu\Delta r-\mathbb P(b\cdot\nabla r)
=
\mathbb P(b\cdot\nabla q),
\qquad r(0)=0,
\]

with a fixed pressure floor. Define

\[
r^{[1]}(\tau)
=
\int_0^\tau
e^{\nu(\tau-s)\Delta}
\mathbb P\operatorname{div}(q\otimes b)(s)\,ds,
\]

where
\((q\otimes b)_{ik}=q_i b_k\), and put
\(r^{[\ge2]}=r-r^{[1]}\).

The proposed theorem is

\[
\int_0^h
\|\nabla\pi^*_{[r^{[1]},b]}\|_1\,d\tau=o(1),
\]

and consequently

\[
\partial_\tau r^{[\ge2]}
-\nu\Delta r^{[\ge2]}
-\mathbb P(b\cdot\nabla r^{[\ge2]})
=
\mathbb P(b\cdot\nabla r^{[1]}),
\]

with a fixed remaining pressure floor.

## New analytic link

The reviewed cube and energy bounds imply

\[
\|q(t)\|_1\lesssim t^{1/4},
\qquad
\|q(t)\|_2\lesssim t,
\qquad
\|q(t)\|_{L^{3/2,1}}\lesssim t^{3/4}.
\]

For the kernel \(\mathcal K_\theta\) of
\(e^{\nu\theta\Delta}\mathbb P\operatorname{div}\), use

\[
|\mathcal K_\theta(x)|
\lesssim_\nu(|x|+\sqrt\theta)^{-4},
\quad
\|\mathcal K_\theta\|_1\lesssim_\nu\theta^{-1/2},
\quad
\|\mathbf1_{|x|>R}\mathcal K_\theta\|_2
\lesssim_\nu R^{-5/2}.
\]

Splitting \(q\otimes b\) at \(R/2\) gives

\[
\int_0^h
\|r^{[1]}(t)\|_{L^2(|x|>R)}^2\,dt
\lesssim
h^{9/2}R^{-5}
+h^4R^{-7}
+h^{5/2}R^{-15}.
\]

Intermediate localisation at \(L=h^{-1/10}\) gives the five inner
pressure powers

\[
\frac{29}{20},\quad
\frac{41}{20},\quad
1,\quad
\frac{17}{20},\quad
\frac12.
\]

Dyadic coefficient shells outside \(R_{\rm src}=h^{-3}\) give

\[
h^{33/4}+h^{11}+h^{89/4}.
\]

## Questions requiring an explicit verdict

1. Does the tensor convention in the Duhamel term reproduce
   \(b\cdot\nabla q\) with no missing term?
2. Does summing the reviewed cube bound genuinely give the stated
   \(L^1\) estimate, and does real interpolation give
   \(L^{3/2,1}\) with time power \(3/4\)?
3. Are the three nonstationary Stokes-kernel estimates valid for the
   projected divergence operator on \(\mathbb R^3\)?
4. Does the inner/outer source split control the full projected
   convolution, including its nonlocal pressure part?
5. Are the pointwise-time powers
   \(t^{7/4}R^{-5/2}\),
   \(t^{3/2}R^{-7/2}\), and
   \(t^{3/4}R^{-15/2}\), and hence all three squared spacetime-tail
   powers, exact?
6. Does the scale-invariant Bogovskii truncation cover every component
   of the far inverse-cubic coefficient-gradient support?
7. Does centre-uniform local energy give \(CR_k\) for every exterior
   dyadic coefficient piece, making the shell series genuinely
   summable without a hidden \(D_b(h)\) tail?
8. Is pressure linearity sufficient to transfer the fixed floor to
   \(r^{[\ge2]}\), and is its displayed equation exact?
9. Does any step silently assume a rough endpoint adjoint, global
   \(L^3\), finite propagation, or an unproved Oseen kernel bound?
10. Is the conclusion correctly limited to exclusion of the first
    feedback iterate, without claiming uniform control in interaction
    depth or a Clay result?

Please be especially suspicious of the off-diagonal Stokes estimate:
look for a lost near-boundary source, an invalid use of an \(L^1\)
kernel bound at \(\theta=0\), or a projection term with slower spatial
decay.

## Executable checks

```bash
make adjoint-pressure-second-interaction
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_second_interaction -v
make records
make links
make markup
git diff --check
```
