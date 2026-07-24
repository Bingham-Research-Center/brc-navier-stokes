# Independent review request: spectral primal--adjoint pressure blindness

**Date:** 2026-07-24

**Clay status:** unsolved

**Primary note:**
[`experiments/adjoint-pressure-spectral-pairing.md`](experiments/adjoint-pressure-spectral-pairing.md)

**Relevant reviewed inputs:**

- [`experiments/adjoint-pressure-history.md`](experiments/adjoint-pressure-history.md)
- [`experiments/adjoint-pressure-skew-compression.md`](experiments/adjoint-pressure-skew-compression.md)
- [`experiments/adjoint-pressure-parabolic-flux.md`](experiments/adjoint-pressure-parabolic-flux.md)

## Requested disposition

Please classify the note as one of:

1. valid in its stated identity/periodic-counterexample scope;
2. repairable, with exact repairs;
3. fatal analytic gap; or
4. correct but duplicative of an earlier recorded result.

Do not assess it as a Clay solution.

## Claim A: exact frequency-localised pairing identity

For a reversed smooth Navier--Stokes coefficient and its forward Oseen
adjoint,

\[
\partial_\tau b+\nu\Delta b-b\cdot\nabla b+\nabla p_b=0,
\]

\[
\partial_\tau a-\nu\Delta a-b\cdot\nabla a+\nabla\pi_a=0,
\]

let \(P\) be a fixed orthogonal componentwise Fourier frequency
projector which commutes with derivatives and preserves solenoidality.
It is not the Leray projector onto the solenoidal range.  The note claims

\[
\frac d{d\tau}\langle Pa,Pb\rangle
=
-
\langle(I-P)a,b\cdot\nabla Pb\rangle
+
\langle Pa,b\cdot\nabla(I-P)b\rangle.
\]

Please check:

1. both reversed-time signs;
2. exact viscous cancellation;
3. exact cancellation of the two pressure gradients;
4. the transport integration by parts and commutator signs;
5. endpoint/regularity assumptions; and
6. validity for sharp high-pass and annular \(L^2\) projectors.

## Claim B: telescope but no pressure charge

For nested projectors \(P_n\), the localised pairings

\[
\mathcal C_n=\langle P_na,P_nb\rangle
\]

and their derivatives telescope exactly across shell index.  However,
the pressure terms vanish separately at every index.  The note concludes
that this exact solenoidal \(L^2\) telescope cannot, from these structural
hypotheses alone, bound the unweighted pressure history

\[
\int_0^T\|\nabla\pi_a\|_1\,d\tau.
\]

Please check whether this conclusion is stated at the right strength and
whether it is already fully contained in the reviewed global-pairing or
skew-compression notes.

## Claim C: exact same-trajectory Beltrami separation

For \(N\in\mathbb N\), on \([0,2\pi]^3\), define

\[
U_N
=
\left(
-\sin(Ny),\,
\cos(Nx),\,
-\sin(Nx)+\cos(Ny)
\right)
\]

and

\[
w_N
=
\frac{|U_N|^2}{2}
=
1-\sin(Nx)\cos(Ny).
\]

The note claims

\[
\nabla\cdot U_N=0,
\qquad
\nabla\times U_N=NU_N,
\qquad
\Delta U_N=-N^2U_N,
\]

\[
(U_N\cdot\nabla)U_N=\nabla w_N.
\]

For nonzero \(A,B\), set

\[
b(\tau)=Ae^{\nu N^2\tau}U_N,
\qquad
a(\tau)=Be^{-\nu N^2\tau}U_N.
\]

It claims these solve the reversed primal and forward adjoint equations
with

\[
p_b=A^2e^{2\nu N^2\tau}w_N,
\qquad
\pi_a=ABw_N.
\]

Please recompute all signs and amplitudes, including the assertion that
\(b\) is the reversal of one exact unforced physical NSE solution.

## Claim D: pressure history and spectral gap

The note derives

\[
\int_0^T\|\nabla\pi_a\|_{L^1(\mathbb T^3)}\,d\tau
\ge
32\pi|AB|NT
\]

from

\[
\partial_xw_N=-N\cos(Nx)\cos(Ny).
\]

It also claims \(a,b\) occupy Fourier radius \(N\), while
\(\nabla\pi_a\) occupies radius \(\sqrt2N\).  Hence, for

\[
N<K<\sqrt2N,
\]

\[
P_{>K}a=P_{>K}b=0,
\qquad
P_{>K}\nabla\pi_a=\nabla\pi_a\ne0.
\]

Please check the torus integral, strict cutoff conventions, all Fourier
supports, and whether this genuinely proves zero localised pairing flux
with positive pressure history above the same cutoff.

## Claim E: fixed-low high--high return

For \(n\in\mathbb N\), \(n\ge1\), the strengthened example uses

\[
k_n=(n,-n-1,0),
\qquad
\ell_n=(n+1,-n,0),
\]

with common radius

\[
R_n=\sqrt{2n^2+2n+1}\to\infty
\]

and fixed difference \(\ell_n-k_n=(1,1,0)\).  For an xy-plane
wavevector \(q\), define the positive-helicity mode

\[
H_q
=
\left(
-\frac{q_2}{|q|}\sin(q\cdot x),\,
\frac{q_1}{|q|}\sin(q\cdot x),\,
\cos(q\cdot x)
\right).
\]

The note puts \(W_n=H_{k_n}+H_{\ell_n}\) and claims

\[
\frac{|W_n|^2}{2}
=
1
+
\left(1-\frac1{2R_n^2}\right)\cos(x+y)
+
\frac1{2R_n^2}\cos((2n+1)(x-y)).
\]

Thus, for every

\[
\sqrt2<K<R_n,
\]

the sharp low pass obeys

\[
P_{\le K}W_n=0,
\]

while

\[
P_{\le K}\nabla\frac{|W_n|^2}{2}
=
\left(1-\frac1{2R_n^2}\right)\nabla\cos(x+y)
\ne0.
\]

With reciprocal reversed-primal and forward-adjoint heat amplitudes, the
note obtains the uniform low-pressure history floor

\[
\int_0^T
\|P_{\le K}\nabla\widetilde\pi_n\|_1\,d\tau
\ge
16\pi^2|AB|
\left(1-\frac1{2R_n^2}\right)T.
\]

Please check:

1. equal radii and helicity;
2. the exact trigonometric coefficients and signs;
3. the fixed-low and high Fourier supports;
4. the \(16\pi^2\) componentwise \(L^1\) constant; and
5. whether this legitimately sharpens the no-go to the
   high--high-to-fixed-low geometry without claiming an event genealogy.

For fixed \(A\ne0\) and every \(T>0\), this paired family has no
coefficient-energy or coefficient-dissipation budget uniform in \(n\).
It is therefore not asserted to contradict the reviewed terminal-return
toll or its finite-energy physical genealogy.

## Scope boundary to enforce

The note claims only:

> A solenoidal spectral \(L^2\) localisation of the conserved
> primal--adjoint pairing cannot itself charge the adjoint-pressure
> history: the projected pressure gradient may be nonzero, but its scalar
> contribution pairs to zero against the divergence-free projected field
> before the shell telescope is taken.  This does not exclude an
> additional pressure-sensitive coupling or genuinely mixed functional.

The periodic example is not claimed to:

- be finite-energy data on \(\mathbb R^3\);
- realise the Besov-event genealogy or coefficient-tail antecedent;
- construct an infinite cascade or singularity;
- defeat a spatially localised, pressure-polar, or divergence-defect
  functional; or
- prove any Clay alternative A--D.

Please identify any wording that exceeds this scope.
