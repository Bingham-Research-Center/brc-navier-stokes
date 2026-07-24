# Independent review request: smooth-layer corridor identification

**Date:** 2026-07-24

**Route:** ROUTE-R3B

**Clay status:** unsolved

**Primary candidate theorem:**
[`experiments/adjoint-pressure-corridor-identification.md`](experiments/adjoint-pressure-corridor-identification.md)

**Reviewed inputs:**

- [`experiments/adjoint-pressure-one-return.md`](experiments/adjoint-pressure-one-return.md)
- [`experiments/adjoint-pressure-multistage-path.md`](experiments/adjoint-pressure-multistage-path.md)
- [`experiments/adjoint-pressure-corridor-sum.md`](experiments/adjoint-pressure-corridor-sum.md)

**Executable ledgers:**

- `lab/navier_lab/adjoint_pressure_corridor_identification.py`
- `lab/tests/test_adjoint_pressure_corridor_identification.py`

Please treat every implication as untrusted and recompute the analytic
chain.  In particular:

1. Verify the \(C_tL^2_x\) fractional Volterra estimate and the
   \(\Gamma(m/2+1)\) denominator, including continuity at \(t=0\) and
   convergence without a smallness assumption.
2. Check that the homogeneous low-frequency sums converge strongly in
   \(L^2\), that this convergence is uniform on the compact range of an
   \(X_h\)-valued continuous function, and that fixed iterates therefore
   converge.
3. Verify that the reviewed fixed low-output pressure operator, rather
   than a bare Riesz transform, is continuous
   \(C_tL^2_x\to L^1_{t,x}\) with the stated layerwise bound.
4. Check the exact equality between the pressure of
   \((\mathsf L_UT_b)^mw_F\) and the unconditional sum of every
   depth-\(m\) corridor path.
5. Recompute the first-high-insertion identity
   \(d=T_bd+\mathsf H_UT_bv_U\), including signs and the fact that the
   smooth LP multipliers need not be idempotent.
6. Verify the fixed-layer participation ceiling and distinguish it from
   any uniform genealogy-level frequency control.
7. Audit the all-starting-band sum:
   \[
   \sum_{F_*\le F\le U}
   \frac SF(c_0\nu F^2h)
   \frac{e^{AH_U}-1}{H_U}
   \bigl(\mathcal B_0+h^6F^{-2}\bigr),
   \]
   including both dyadic geometric sums and the resulting
   \(Sh^{1/2}\mathcal B_0\) parabolic bound.
8. Check the smooth-layer convergence of
   \(W_\infty=\sum_{F\ge F_*}w_F\) and
   \(V_U\to V_\infty\), with all constants allowed to depend on that
   one layer.
9. Verify that the sequence alternative is exhaustive and that branch
   (45) is described only as failure of parabolic LP--Dyson capture,
   not as an instantaneous Fourier-energy tail or a rough-hull theorem.
10. Audit the exact remaining boundary: participation of the specified
    separated-return block, gradual descents without a separated
    return, or a PDE charge for superparabolic capture.

A valid result here is only a conditional smooth-layer identification
and reduction.  It is not a singular solution, regularity, breakdown,
or any Clay alternative A--D.
