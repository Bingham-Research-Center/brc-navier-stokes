# Independent review request: last-separated-return renewal

**Date:** 2026-07-24

**Route:** ROUTE-R3B

**Clay status:** unsolved

**Primary candidate theorem:**
[`experiments/adjoint-pressure-last-return-renewal.md`](experiments/adjoint-pressure-last-return-renewal.md)

**Reviewed inputs:**

- [`experiments/adjoint-pressure-divergent-interaction-depth.md`](experiments/adjoint-pressure-divergent-interaction-depth.md)
- [`experiments/adjoint-pressure-one-return.md`](experiments/adjoint-pressure-one-return.md)
- [`experiments/adjoint-pressure-corridor-sum.md`](experiments/adjoint-pressure-corridor-sum.md)
- [`experiments/adjoint-pressure-corridor-identification.md`](experiments/adjoint-pressure-corridor-identification.md)

**Executable ledgers:**

- `lab/navier_lab/adjoint_pressure_last_return.py`
- `lab/tests/test_adjoint_pressure_last_return.py`

Please treat every implication as untrusted and recompute the analytic
chain.  In particular:

1. Verify that the output-band filters
   \(\mathsf A_{b,Q}\) and \(\mathsf B_{b,Q}\) form an exact
   complementary partition despite smooth LP overlap.
2. Check the nested-high-pass estimate by swapping input and output
   dyadic sums, and verify the fractional
   \((t-s)^{-1/2}\) Volterra kernel for both operators.
3. Check the stronger high-output estimate
   \[
   \left\|\sum_{Q>U}\mathsf C_{b,Q}\right\|_{X_h\to X_h}
   \lesssim B_\infty(\nu U)^{-1},
   \]
   including almost orthogonality, the time integral, and the separate
   treatment of the homogeneous low-frequency end.
4. Recompute the noncommutative renewal identity
   \[
   r=(I-\mathsf A_b)^{-1}g
     +(I-\mathsf A_b)^{-1}\mathsf B_br.
   \]
   Check that the second term groups by the leftmost operator
   \(\mathsf B_b\), hence the last \(\mathsf B_b\) chronologically,
   with no missing or duplicated word.
5. Verify the exact identity
   \(\mathsf B_br=\sum_{F\ge F_*}w_F\), the direct definition of
   \(\mathsf A_{b,U}\), and convergence of the truncated resolvents and
   their fixed low-output pressures.
6. Audit the filtered-corridor comparison.  In particular, verify that
   each complementary input filter is uniformly \(L^1\)-bounded and
   that its cost is absorbed in the per-depth constant
   \(A_{\rm filt}\), with no hidden \(U\)- or depth-dependent factor.
7. Recompute the all-starting-band aggregate and its parabolic ceiling:
   \[
   \|\mathscr P_{S,b}r_{{\rm last},U}\|_{L^1_{t,x}}
   \lesssim
   Sh^{1/2}\mathcal B_0(h)+(S/F_*)h^7.
   \]
8. Verify the \(p_0/2\) renewal split, the \(p_0/4\) captured floor,
   the subsequence exhaustion, and the resulting \(9/4\)
   stretched-exponential cost.
9. Enforce the scope boundary: \(g=T_bq\) already contains one
   interaction, the theorem concerns only the oriented feedback block,
   and superparabolic LP--Dyson capture is not yet a physical
   dissipation charge.

A valid result here only replaces the former separated-return
participation antecedent by an exhaustive three-way alternative on
fixed smooth layers.  It is not a rough-hull spectral theorem, a
singular solution, regularity, breakdown, or any Clay alternative A--D.
