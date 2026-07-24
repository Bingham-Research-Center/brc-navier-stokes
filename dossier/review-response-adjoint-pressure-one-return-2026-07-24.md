# Independent review response: one separated returned-low Oseen step

**Date:** 2026-07-24

**Reviewed packet:**
`review-letter-adjoint-pressure-one-return-2026-07-24.md` (archived in Git at `c277792`)

**Primary theorem:**
[`experiments/adjoint-pressure-one-return.md`](experiments/adjoint-pressure-one-return.md)

**Verdict:** valid in the stated conditional scope

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI re-derived the annular heat--Leray
kernel, separated Fourier support, \(K^{-1}\) coefficient gain, dyadic
sum, spatial shell transfer, heat clock, final Lorentz estimate, and
piecewise inversion.  It found no mathematical defect in the stated
one-return theorem.

No reviewer edits or repairs were required.

## Accepted theorem

Let \(w_F\) be the state produced when the zero-data state tail above
\(64F\) makes one heat-mediated Oseen interaction into the annulus
\(F\).  If \(\mathfrak R^{(1)}_{S,F}(h)\) denotes the pressure which
that returned state generates in a fixed output band \(S\), then

\[
\boxed{
\begin{aligned}
\mathfrak R^{(1)}_{S,F}(h)
\le
C_\nu M\frac SF
\min\{1,F^2h\}
\bigg\{
1
&+h^{7/4}
\left[
1+\log_+\!\bigl(D_b(h)h^3\bigr)
\right]\\
&+h^{21/4}
+h^{89/4}
+h^{103/4}
+h^6F^{-2}
\bigg\}.
\end{aligned}}
\]

The reviewer confirmed every structural factor:

1. the annular heat--Leray kernel is
   \(O(F e^{-c_\nu F^2(t-s)})\);
2. high-to-\(F\) Fourier support forces the coefficient to the high
   input scale;
3. coefficient Bernstein supplies \(K^{-1}\), and the dyadic sum
   cancels the kernel's \(F\);
4. the inner and exterior spatial ledgers transfer without changing
   their powers;
5. Fubini gives precisely \(\min\{h,F^{-2}\}\); and
6. final Lorentz--Bernstein gives
   \(MSF\|w_F\|_1\).

For the nonsolenoidal spatial cutoff pieces,

\[
\operatorname{div}(z\boxtimes c)
=c\cdot\nabla z+z\,\operatorname{div}c.
\]

The proof estimates the complete tensor divergence and never discards
the second term.  Those cutoff-divergence terms cancel when the exact
coefficient partition is summed back to the solenoidal drift.

## Accepted inversion

For \(F(h)\asymp h^{-\beta}\), a fixed positive one-return pressure
fraction forces

\[
\boxed{
D_b(h)
\ge
h^{-3}
\exp\!\left(
c h^{-\gamma_1(\beta)}
\right),
}
\]

where

\[
\boxed{
\gamma_1(\beta)
=
\frac74+\beta+(1-2\beta)_+
=
\frac94+\left|\beta-\frac12\right|.
}
\]

Thus

\[
\gamma_1(\beta)\ge\frac94,
\]

with equality only at the parabolic return scale
\(F=h^{-1/2}\).  A subparabolic return is more expensive because its
available terminal window is shorter than one natural heat clock.

On one physical trajectory this requires

\[
\sigma_h
=
o\!\left[
h^3
\exp\!\left(
-c h^{-\gamma_1(\beta)}
\right)
\right].
\]

## Exact accepted frontier

The theorem charges one separated high-to-annular Oseen return
immediately before the low-pressure observation.  Its pressure floor
is an explicit additional antecedent.  It does not prove that the
complete feedback packet enters this component.

Consequently, a surviving returned-low itinerary must use at least one
additional state interaction after the separated return, or descend
through several comparable frequency bands so that no single final
return has the separation used by the theorem.  Summation of that
multistage descent is the live frequency-itinerary gate.

No regularity theorem, breakdown theorem, Oseen singularity,
Navier--Stokes singularity, or Clay alternative A--D follows.

## Validation

- Targeted exact tests: 12 passed.
- Executable certificate: passed.
- Reviewer `make check`: 724 tests passed.
- `git diff --check`: passed.
