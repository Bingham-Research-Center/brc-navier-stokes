# Independent review request: dyadic Zeno-frequency pressure path

**Date:** 2026-07-24

**Primary note:**
[`experiments/adjoint-pressure-frequency-zeno.md`](experiments/adjoint-pressure-frequency-zeno.md)

**Executable certificate:**
[`../lab/navier_lab/adjoint_pressure_frequency_zeno.py`](../lab/navier_lab/adjoint_pressure_frequency_zeno.py)

**Tests:**
[`../lab/tests/test_adjoint_pressure_frequency_zeno.py`](../lab/tests/test_adjoint_pressure_frequency_zeno.py)

**Clay status:** unsolved

## Requested verdict

Please decide whether the note gives an exact countermodel to the
**positive cross-band norm majorant**, without implying an actual Oseen
or Navier--Stokes counterexample.

The intended conclusion is:

> Weak-\(L^3\) cross-band scale factors, exponential heat clocks,
> arbitrary fixed algebraic strong zero trace, and finite critical
> energy/dissipation ledgers do not alone force multiscale
> pressure-depth decay.

## 1. Cross-band scale

Please verify that annular \(L^1\) output localisation and the same
Lorentz--Bernstein estimate as in the reviewed fixed-band theorem give

\[
\|\Delta_Se^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}(z_R\otimes b)\|_1
\lesssim
MRS e^{-c\nu S^2(t-s)}\|z_R\|_1.
\]

After fixed-constant normalisation, does the scalar kernel

\[
k_{S,R}(t)=RS e^{-S^2t}
\]

have total mass \(R/S\)?

Please also check that the band-resolved pressure majorant from input
\(R\) to output \(S\) has instantaneous scale \(MRS\).

## 2. Probability representation

For \(R_i=2^i\), verify

\[
k_i(t)
=
\frac12\,4^i e^{-4^it},
\qquad
K_m:=k_m*\cdots*k_1
=
2^{-m}f_{S_m},
\]

where \(S_m\) is the sum of independent exponential variables with
rates \(4^i\).

Please also check the single sequence-space formulation

\[
(\mathfrak Tz)_i=k_i*z_{i-1},
\qquad
\mathfrak Cz=\sum_{i\ge0}2^iz_i:
\]

for band-zero input, \(\mathfrak T^m q\) occupies only band \(m\), so
the observation is not chosen anew with \(m\).

For \(q_\eta(t)=t^\eta\), please recompute

\[
u_{m,\eta}(t)
=
2^{-m}\mathbb E[(t-S_m)_+^\eta]
\]

and the small-time order \(O(t^{m+\eta})\).
For \(\eta=0\), the current note defines
\((x)_+^0=\mathbf1_{\{x>0\}}\); please check that every positive-depth
output then has the claimed zero trace.

## 3. Terminal pressure and finite horizon

Please verify that the terminal observation weight \(2^m\) is the
normalised product \(R_mR_0\) cross-band pressure factor, with
\(R_0=1\), and that

\[
\mathcal P_{m,\eta}(T)
=
\frac1{\eta+1}
\mathbb E[(T-S_m)_+^{\eta+1}].
\]

Check

\[
\mathbb ES_m=\frac{1-4^{-m}}3
\]

and the Jensen floor

\[
\mathcal P_{m,\eta}(1)
\ge
\frac{(2/3)^{\eta+1}}{\eta+1}.
\]

Is the convexity assertion valid also for \(\eta=0\)?

## 4. Packet ledger

For \(B_i=R_i\), \(V_i=R_i^{-3}\), and
\(\tau_i=R_i^{-2}\), please check:

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

Please assess whether the note is sufficiently explicit that this is
only a kinematic scaling ledger, not one simultaneously realised
interacting field.

## 5. Exact finite-depth Fourier/Leray supplement

After the scalar packet passed its first audit, an exact algebraic
supplement was added.  Please verify it independently.

With \(R_i=2^i\), define

\[
\xi_i=
\begin{cases}
R_i e_1,&i\text{ even},\\
R_i e_2,&i\text{ odd},
\end{cases}
\qquad a=e_3,
\qquad \eta_i=\xi_i-\xi_{i-1},
\]

and

\[
\beta_i=
\begin{cases}
R_i(e_1+\tfrac12e_2),&i\text{ odd},\\
R_i(\tfrac12e_1+e_2),&i\text{ even}.
\end{cases}
\]

Please check

\[
\beta_i\cdot\eta_i=0,
\qquad
\beta_i\cdot\xi_{i-1}=R_iR_{i-1},
\qquad
\mathbb P_{\xi_i}e_3=e_3.
\]

Thus one divergence-free complex drift mode maps the selected state
mode from \(\xi_{i-1}\) to \(\xi_i\) with exactly the numerator of the
scalar kernel.

For the terminal return, let \(\kappa=e_3\).  Writing
\(\xi_i=R_i e_{\alpha_i}\), define

\[
\zeta_i=\kappa-\xi_i,
\qquad
\gamma_i=e_{\alpha_i}+R_i e_3.
\]

Please check

\[
\gamma_i\cdot\zeta_i=0,
\qquad
\gamma_i\cdot\xi_i=R_i,
\qquad
\mathbb Q_\kappa e_3=e_3.
\]

This should give the exact terminal factor \(R_iR_0=R_i\), while

\[
|\beta_i|^2=\frac54R_i^2,
\qquad
|\gamma_i|^2=1+R_i^2.
\]

The intended conclusion is only that elementary finite-depth Fourier
phase and Leray-polarisation compatibility is not an obstruction.
Please reject any wording that promotes these global complex torus
modes to one uniformly weak-\(L^3\), spatially localised
\(\mathbb R^3\) drift, controls the unwanted cross-interactions of a
mode sum, or claims an Oseen or Navier--Stokes solution.

## 6. Scope

Reject or require repair if the note implies any of:

- equality with the vector cross-band Oseen operator rather than its
  positive majorant;
- one uniformly weak-\(L^3\) drift realising every transition;
- one uniformly weak-\(L^3\) localised drift with compatible packet
  overlap and controlled cross-interactions;
- a Navier--Stokes trajectory, feedback solution, regularity failure, or
  Clay alternative A--D.

## Reproduce

```bash
make adjoint-pressure-frequency-zeno
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_frequency_zeno -v
make check
```
