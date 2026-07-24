# Independent review request: spatial primal--adjoint current cancellation

**Date:** 2026-07-24

**Clay status:** unsolved

**Primary note:**
[`experiments/adjoint-pressure-spatial-pairing.md`](experiments/adjoint-pressure-spatial-pairing.md)

**Relevant reviewed inputs:**

- [`experiments/adjoint-pressure-history.md`](experiments/adjoint-pressure-history.md)
- [`experiments/adjoint-pressure-skew-compression.md`](experiments/adjoint-pressure-skew-compression.md)
- [`experiments/adjoint-pressure-parabolic-flux.md`](experiments/adjoint-pressure-parabolic-flux.md)
- [`experiments/adjoint-pressure-spectral-pairing.md`](experiments/adjoint-pressure-spectral-pairing.md)

## Requested disposition

Please classify the note as one of:

1. valid in its stated local-identity and periodic-counterexample scope;
2. repairable, with exact repairs;
3. fatal analytic gap; or
4. correct but duplicative of a recorded result.

Do not assess it as a Clay solution.

## Claim A: re-derivation of the recorded pointwise conservation law

For

\[
\partial_\tau b+\nu\Delta b-b\cdot\nabla b+\nabla p_b=0,
\qquad
\nabla\cdot b=0,
\]

\[
\partial_\tau a-\nu\Delta a-b\cdot\nabla a+\nabla\pi_a=0,
\qquad
\nabla\cdot a=0,
\]

the note sets \(q=a\cdot b\) and claims

\[
\partial_\tau q+\nabla\cdot\mathcal J=0,
\]

\[
\mathcal J
=
\nu\sum_i(a_i\nabla b_i-b_i\nabla a_i)
-q\,b+\pi_ab+p_ba.
\]

Please check:

1. both reversed-time signs;
2. the viscous Wronskian sign;
3. the transport sign and use of the same coefficient \(b\);
4. both pressure-flux signs;
5. gauge invariance under time-dependent pressure constants; and
6. validity on \(\mathbb R^3\) and \(\mathbb T^3\) under the stated
   smoothness assumptions.

This identity was already recorded as equation (42) of the reviewed
skew-compression note.  The present note does not claim it as new; it
re-derives it to audit the coercivity of its total current.

## Claim B: cutoff identity and telescope

For every fixed smooth cutoff \(\eta\), the note claims

\[
\frac d{d\tau}\int\eta\,a\cdot b
=
\int\nabla\eta\cdot\mathcal J.
\]

It also claims that nested cutoff pairings telescope but expose only
the signed total current, not the adjoint-pressure component separately.

Please check the integration-by-parts sign and whether the stated
structural conclusion is at the right strength.

## Claim C: generic reciprocal Beltrami cancellation

Let

\[
\nabla\cdot U=0,\qquad
\nabla\times U=RU,\qquad
\Delta U=-R^2U,
\qquad
w=\frac{|U|^2}{2}.
\]

For nonzero constants \(A,B\), put

\[
b=Ae^{\nu R^2\tau}U,
\qquad
a=Be^{-\nu R^2\tau}U.
\]

The note claims these solve the reversed primal and forward adjoint
equations with

\[
p_b=A^2e^{2\nu R^2\tau}w,
\qquad
\pi_a=ABw.
\]

In the displayed pressure gauges, it then claims

\[
\nu\sum_i(a_i\nabla b_i-b_i\nabla a_i)=0,
\]

\[
-q\,b=-2A^2Be^{\nu R^2\tau}wU,
\]

\[
\pi_ab+p_ba=2A^2Be^{\nu R^2\tau}wU,
\]

and hence, in those gauges,

\[
\mathcal J\equiv0
\]

pointwise, even when

\[
\int_0^T\|\nabla\pi_a\|_1\,d\tau
=|AB|T\|\nabla w\|_1>0.
\]

Please recompute every coefficient and sign, and check that the physical
trajectory has

\[
u(t)=Ae^{-\nu R^2t}U,
\qquad
p_u(t)=-A^2e^{-2\nu R^2t}w.
\]

Under arbitrary time-dependent pressure gauges, the requested invariant
claim is only

\[
\nabla\cdot\mathcal J=0,
\qquad
\int\nabla\eta\cdot\mathcal J=0
\]

for every fixed smooth cutoff \(\eta\).

## Claim D: one-radius and fixed-low examples

For the one-radius field

\[
U_N=(-\sin Ny,\cos Nx,-\sin Nx+\cos Ny),
\qquad N\in\mathbb N,
\]

the note imports the checked floor

\[
\int_0^T\|\nabla\pi_{a,N}\|_1\,d\tau
\ge32\pi|AB|NT
\]

while \(\mathcal J_N\equiv0\) in the displayed gauges and every cutoff
flux vanishes in all gauges.

For the paired equal-radius field at

\[
k_n=(n,-n-1,0),\qquad
\ell_n=(n+1,-n,0),
\qquad n\in\mathbb N,\ n\ge1,
\]

it imports the fixed-low floor

\[
\int_0^T
\|P_{\le K}\nabla\widetilde\pi_n\|_1\,d\tau
\ge
16\pi^2|AB|
\left(1-\frac1{2R_n^2}\right)T
\]

for \(\sqrt2<K<R_n\), while again
\(\mathcal J_n\equiv0\) in the displayed gauges and every cutoff flux
vanishes in all gauges.

Please check that the generic cancellation applies unchanged to both
families and that the spectral floor is not being confused with a
spatially projected current.

## Claim E: scope and nonuniform budget

For fixed \(A\ne0\) and \(T>0\), the note states

\[
\sup_{\tau\le T}\|\widetilde b_n(\tau)\|_2^2
+\nu\int_0^T\|\nabla\widetilde b_n\|_2^2\,d\tau
\longrightarrow\infty.
\]

Thus the examples do not contradict the reviewed finite-energy
terminal-return toll.  The claimed no-go is only:

> The bare spatial primal--adjoint conservation current does not itself
> coerce the adjoint-pressure history through its gauge-invariant signed
> cutoff-current telescope.  In the displayed gauges pressure cancels
> the other current terms pointwise; in all gauges every cutoff flux
> vanishes.

The note does not claim to exclude:

- a pressure-polar or pressure-component functional;
- a new sign or transversality theorem controlling cancellation;
- a norm or other functional of a canonically gauge-fixed current;
- a controlled divergence-defect functional;
- direct event ancestry;
- a finite-energy \(\mathbb R^3\) counterexample;
- a Besov-event genealogy, singularity, or Clay alternative.

Please identify any wording that exceeds this scope and whether the
new **pointwise same-trajectory cancellation of the already known
current** duplicates an earlier counterexample rather than closing a
genuinely distinct spatial-current coercivity candidate.

## Executable checks

The certificate currently has eight targeted tests for:

1. reciprocal heat amplitudes;
2. the zero viscous Wronskian;
3. pointwise pressure--transport cancellation;
4. the two equal pressure-flux contributions;
5. positive pressure history with zero total current;
6. the paired-family nonuniform budget; and
7. invalid inputs.

Please treat those tests as algebraic checks only, not as proof of the
PDE identity.
