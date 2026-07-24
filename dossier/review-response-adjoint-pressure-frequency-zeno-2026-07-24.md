# Independent review response: dyadic Zeno-frequency pressure path

**Date:** 2026-07-24

**Reviewed packet:**
[`review-letter-adjoint-pressure-frequency-zeno-2026-07-24.md`](review-letter-adjoint-pressure-frequency-zeno-2026-07-24.md)

**Primary countermodel:**
[`experiments/adjoint-pressure-frequency-zeno.md`](experiments/adjoint-pressure-frequency-zeno.md)

**Verdict:** accepted after four precision repairs

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI re-derived the cross-band multiplier
scale, kernel mass, probability representation, strong trace order,
terminal pressure factor, Jensen floor, and every critical packet
ledger.  It accepted the scalar positive-majorant countermodel after
three initial precision repairs:

1. the causal convention for \((x)_+^0\) and the restriction of the
   strong-zero-trace statement to positive depth were made explicit;
2. the sequence observation was extended to include band zero; and
3. the terminal factor was identified as the product \(R_mR_0\), not a
   general ratio.

The reviewer then accepted the exact finite-depth Fourier/Leray
supplement after one stale canonical-record sentence was repaired.  No
reviewer edits were made.

## Accepted scalar chain

The positive cross-band Oseen majorant has scale

\[
\|\Delta_Se^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}(z_R\otimes b)\|_1
\lesssim
MRS e^{-c\nu S^2(t-s)}\|z_R\|_1.
\]

After fixed-constant normalisation its kernel is

\[
k_{S,R}(t)=RS e^{-S^2t},
\qquad
\int_0^\infty k_{S,R}(t)\,dt=\frac RS.
\]

On the dyadic path \(R_i=2^i\),

\[
k_i(t)=\frac12\,4^ie^{-4^it},
\qquad
K_m=2^{-m}f_{S_m},
\qquad
\mathbb ES_m=\frac{1-4^{-m}}3.
\]

For \(q_\eta(t)=t^\eta\),

\[
u_{m,\eta}(t)
=
2^{-m}\mathbb E[(t-S_m)_+^\eta]
=O(t^{m+\eta})
\]

at every positive depth.  The single observation
\(\mathfrak Cz=\sum_{i\ge0}2^iz_i\) supplies the terminal product
\(R_mR_0=2^m\), so

\[
\mathcal P_{m,\eta}(1)
=
\frac1{\eta+1}
\mathbb E[(1-S_m)_+^{\eta+1}]
\ge
\frac{(2/3)^{\eta+1}}{\eta+1}.
\]

The reviewer confirmed that the hinge function is convex also for
\(\eta=0\).  For the linear strong-zero-trace input the floor is
\(\mathcal P_{m,1}(1)\ge2/9\).

## Accepted critical ledger

For \(B_i=R_i\), \(V_i=R_i^{-3}\), and
\(\tau_i=R_i^{-2}\), the reviewer recomputed

\[
R_j^3\sum_{i\ge j}V_i=\frac87,
\qquad
\sum_iB_i^2V_i=1,
\]

\[
\sum_i\tau_i(B_iR_i)^2V_i=1,
\qquad
\sum_i\tau_i=\frac13.
\]

These are kinematic scale identities, not one interacting field.

## Accepted Fourier/Leray supplement

For alternating state frequencies

\[
\xi_i=
\begin{cases}
R_ie_1,&i\text{ even},\\
R_ie_2,&i\text{ odd},
\end{cases}
\qquad a=e_3,
\]

the reviewer checked the exact divergence-free upward modes:

\[
\beta_i\cdot(\xi_i-\xi_{i-1})=0,
\qquad
\beta_i\cdot\xi_{i-1}=R_iR_{i-1},
\qquad
\mathbb P_{\xi_i}a=a.
\]

At the fixed terminal frequency \(\kappa=e_3\), it also checked

\[
\gamma_i\cdot(\kappa-\xi_i)=0,
\qquad
\gamma_i\cdot\xi_i=R_i,
\qquad
\mathbb Q_\kappa a=a.
\]

Thus selected finite-depth complex Fourier blocks realise the exact
upward numerator and terminal Hodge factor.  Their amplitudes satisfy

\[
|\beta_i|^2=\frac54R_i^2,
\qquad
|\gamma_i|^2=1+R_i^2.
\]

## Exact accepted frontier

The result proves:

> Weak-\(L^3\) cross-band norm estimates, exponential heat clocks,
> arbitrary fixed algebraic strong zero trace, and finite critical
> energy/dissipation ledgers do not by themselves make every multiscale
> pressure path summable.  Elementary Fourier/Leray compatibility does
> not repair that norm-only argument.

It does **not** construct one uniformly weak-\(L^3\), spatially
localised \(\mathbb R^3\) drift whose full mode sum realises the path,
control unwanted cross-interactions, solve the Oseen equation, realise
Navier--Stokes feedback, or establish any Clay alternative.

The live gate is now a same-trajectory theorem coupling spatial
localisation and overlap, all signed/vector cross-interactions, the
finite coefficient budget, and physical event ancestry.

## Validation

- Targeted exact tests: 12 passed.
- Reviewer full suite: 668 tests passed.
- `make check`: passed.
- `git diff --check`: passed.
