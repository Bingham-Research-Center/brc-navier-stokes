# Independent review response: parabolic coefficient-tail theorem

**Date:** 2026-07-24

**Reviewed request:**
[`review-letter-adjoint-pressure-parabolic-coefficient-tail-2026-07-24.md`](review-letter-adjoint-pressure-parabolic-coefficient-tail-2026-07-24.md)

**Primary theorem:**
[`experiments/adjoint-pressure-parabolic-coefficient-tail.md`](experiments/adjoint-pressure-parabolic-coefficient-tail.md)

**Verdict:** valid in the stated smooth-layer conditional scope

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found no fatal or repairable analytic
gap.  It recomputed the low-coefficient resolvent, the exact
last-high-coefficient identities, both endpoint Lorentz estimates, the
pressure comparison, the growing-cutoff exponent, and the physical
scaling.

The reviewer validated a theorem on each smooth finite-energy genealogy
layer.  It did not validate event-index summability, a contradiction
with finite physical dissipation, a rough-hull theorem, regularity,
breakdown, or any Clay alternative A--D.

## Accepted analytic chain

The reviewer independently checked:

1. Lorentz--Bernstein gives
   \[
   \|S_Vb\|_\infty\le CV\|b\|_{L^{3,\infty}}.
   \]
2. On
   \(Z_h=L^1_tL^{3/2,1}_x\), the Stokes kernel has the half-order
   time norm and
   \[
   \|T_c^m\|_{Z_h\to Z_h}
   \le
   \frac{(CMV\Gamma(1/2)\sqrt h)^m}
        {\Gamma(m/2+1)}.
   \]
3. The resulting Mittag--Leffler resolvent is bounded by
   \(Ce^{A\kappa^2}\) when \(V=\kappa h^{-1/2}\).  The extra initial
   factor \(\kappa\) in \(r_c=(I-T_c)^{-1}T_cq_c\) is absorbed by one
   enlargement of \(A\).
4. The auxiliary direct-response estimate uses only the solenoidal
   weak-\(L^3\) ceiling; \(c=S_Vb\) need not itself solve
   Navier--Stokes.
5. The identities
   \[
   q_b-q_c=T_d\varphi,
   \]
   \[
   r_b-r_c
   =
   (I-T_c)^{-1}
   \left[
   T_c(q_b-q_c)+T_d(q_b+r_b)
   \right],
   \]
   and
   \[
   \mathscr P_{S,b}r_b-\mathscr P_{S,c}r_c
   =
   \mathscr P_{S,c}(r_b-r_c)+\mathscr P_{S,d}r_b
   \]
   are exact.  They group the difference by the last chronological
   \(d=(I-S_V)b\) occurrence.
6. O'Neil's product law
   \[
   L^{6,2}\cdot L^2\longrightarrow L^{3/2,1}
   \]
   and the remaining half heat clock give
   \[
   \|q_b-q_c\|_{Z_h}\le ChE_d^{1/2},
   \]
   \[
   \|T_d(q_b+r_b)\|_{Z_h}\le Ch^{3/2}E_d^{1/2}.
   \]
   No \(L^\infty_t\dot H^1_x\) assumption or failed endpoint
   convolution is hidden here.
7. The low-output pressure kernel has \(L^1\) norm \(O(S)\).
   The apparent factor \(\kappa\) in \(T_c(q_b-q_c)\) cancels exactly
   against
   \[
   E_d^{1/2}
   \le
   V^{-1}D_{b,>V}^{\chi\,1/2}
   =
   h^{1/2}\kappa^{-1}D_{b,>V}^{\chi\,1/2}.
   \]
   Hence
   \[
   \|\mathscr P_{S,b}r_b-\mathscr P_{S,c}r_c\|_1
   \le
   Ce^{A\kappa^2}h^{3/2}
   D_{b,>V}^{\chi\,1/2}.
   \]
8. Inversion gives
   \[
   D_{b,>\kappa h^{-1/2}}^\chi
   \ge
   ce^{-2A\kappa^2}h^{-3}.
   \]
   With
   \[
   \kappa^2
   =
   \frac{\varepsilon}{2A}\log\frac1h,
   \]
   this becomes the superparabolic tail floor
   \[
   D_{b,>\kappa h^{-1/2}}^\chi
   \ge
   c_\varepsilon h^{-3+\varepsilon}.
   \]
9. The pullback identity
   \[
   \sigma_jD_{b_j,>V_j}^\chi
   =
   \int_{I_j}
   \|\nabla(I-S_{V_j/\sigma_j})v\|_2^2\,dt
   \]
   is exact.  Global physical Fourier-tail continuity yields only
   \(\sigma_jh_j^{-3+\varepsilon}\to0\), not a contradiction.

## Reviewer-requested precision additions

The final theorem now explicitly:

1. absorbs the depth-one factor
   \(\kappa\) into the final \(e^{A\kappa^2}\) constant; and
2. specifies that the logarithmic cutoff uses that same final enlarged
   \(A\).

These additions clarify the constant ledger without changing the
theorem.

## Additional audit observation

The reviewer also checked that the full-\(T_b\) Galerkin approximation
has exact first-high and last-high insertion identities.  The new
coefficient-split theorem is stronger for the present route: it follows
directly from the complete feedback pressure floor and avoids the
Galerkin endpoint weakness.

## Exact accepted frontier

Superparabolic LP--Dyson capture can no longer remain only an
operator-series label.  Every selected feedback packet creates an
actual high-frequency coefficient-dissipation tail, reaching the
superparabolic scale
\[
h^{-1/2}\sqrt{\log(1/h)}
\]
with size at least \(h^{-3+\varepsilon}\).

The next missing theorem is now event-index non-reuse: couple that
physical frequency to the next Besov event, or prove that the nested
physical Fourier-tail payments cannot all be charged to the same finer
dissipation.

## Validation

- Targeted ledger tests: 8 passed.
- Mathematical-markup validation: passed.
- Current canonical repository validation:
  105 experiments, 813 local-link targets, 31,722 mathematical
  delimiters, and 786 tests passed.
