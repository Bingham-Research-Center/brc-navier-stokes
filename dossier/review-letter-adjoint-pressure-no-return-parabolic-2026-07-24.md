# Independent review request: no-return parabolic exclusion

**Date:** 2026-07-24

**Route:** ROUTE-R3B

**Clay status:** unsolved

**Primary candidate theorem:**
[`experiments/adjoint-pressure-no-return-parabolic.md`](experiments/adjoint-pressure-no-return-parabolic.md)

**Reviewed inputs:**

- [`experiments/adjoint-pressure-second-interaction.md`](experiments/adjoint-pressure-second-interaction.md)
- [`experiments/adjoint-pressure-corridor-sum.md`](experiments/adjoint-pressure-corridor-sum.md)
- [`experiments/adjoint-pressure-corridor-identification.md`](experiments/adjoint-pressure-corridor-identification.md)
- [`experiments/adjoint-pressure-last-return-renewal.md`](experiments/adjoint-pressure-last-return-renewal.md)

**Executable ledgers:**

- `lab/navier_lab/adjoint_pressure_no_return.py`
- `lab/tests/test_adjoint_pressure_no_return.py`

Please treat every implication as untrusted and recompute the candidate
chain.  In particular:

1. Verify the use of the reviewed estimate
   \(\|q(t)\|_{L^{3/2,1}}\lesssim t^{3/4}\) and the annular
   heat--Leray \(L^1\) bound for \(g_F=\Delta_FT_bq\).
2. Check the normalisation
   \[
   Fe^{-c_0\nu F^2\tau}
   =(c_0\nu F)^{-1}
   \lambda_Fe^{-\lambda_F\tau}
   \]
   and all viscosity and frequency factors.
3. Recompute the path telescope
   \[
   F^{-1}
   (R_0/R_1)\cdots(R_{m-1}/R_m)
   SR_m=S,
   \]
   including the depth-zero case and the retained tensor orientation.
4. Verify that a depth-\(m\) path has exactly \(m+1\) exponential heat
   clocks, and that integrating the earlier \(s^{3/4}\) source gives
   \(I_q(h)=4h^{7/4}/7\).
5. Check the infinite starting-band and continuation-band sum:
   \[
   \sum_{\boldsymbol R\in\mathscr N_m(U)}
   \Theta_{\boldsymbol R}(h)
   \le
   H_U^{m+1}/(m+1)!.
   \]
   There is no infrared cutoff, so any hidden unweighted band count is
   fatal.
6. Audit the complementary filters.  They must preserve annular input
   support, cost only \(C_{\rm LP}\) per continuation depth, and create
   no extra frequency entropy.
7. Verify exact identification of the absolutely convergent path
   pressure with
   \(r_{{\rm no},U}=(I-\mathsf A_{b,U})^{-1}g_U\), including the
   homogeneous infrared limits and the uniform Gamma tail.
8. Check that every fixed layer has a finite capture ceiling and that a
   parabolic subsequence contradicts the captured \(p_0/4\) floor by
   \(C_\kappa Sh^{7/4}\to0\).
9. Recompute the combination with the last-return renewal theorem:
   the claimed exhaustive result is superparabolic LP--Dyson capture
   escape or the \(9/4\) coefficient cost, not a physical
   high-frequency theorem.

A valid result is only a smooth-layer conditional parabolic-exclusion
theorem.  It does not turn capture escape into physical dissipation,
stop the physical zoom, produce a singular solution, prove regularity
or breakdown, or establish a Clay alternative A--D.
