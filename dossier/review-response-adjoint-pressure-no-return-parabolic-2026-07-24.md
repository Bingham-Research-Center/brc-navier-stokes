# Independent review response: no-return parabolic exclusion

**Date:** 2026-07-24

**Reviewed packet:**
`review-letter-adjoint-pressure-no-return-parabolic-2026-07-24.md` (archived in Git at `c277792`)

**Primary theorem:**
[`experiments/adjoint-pressure-no-return-parabolic.md`](experiments/adjoint-pressure-no-return-parabolic.md)

**Verdict:** valid in the stated smooth-layer conditional scope

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found no fatal defect.  The accepted
result proves that the exact no-chargeable-feedback-return block cannot
carry a fixed pressure floor under any uniformly parabolic LP--Dyson
capture ceiling.

Combined with the preceding last-return renewal theorem, the complete
feedback frequency alternative is reduced to superparabolic capture
escape or the reviewed \(9/4\) stretched-exponential coefficient cost.
This is not yet a physical high-frequency dissipation theorem and does
not prove any Clay alternative A--D.

## Accepted chain

1. The reviewed direct-response bounds interpolate to
   \[
   \|q(t)\|_{L^{3/2,1}}
   \lesssim
   \|q(t)\|_1^{1/3}\|q(t)\|_2^{2/3}
   \lesssim t^{3/4}.
   \]
2. The band-\(F\) first feedback source obeys
   \[
   \|g_F(t)\|_1
   \lesssim
   MF\int_0^t e^{-\lambda_F(t-s)}s^{3/4}\,ds
   =
   \frac{M}{c_0\nu F}
   \int_0^t\lambda_Fe^{-\lambda_F(t-s)}s^{3/4}\,ds.
   \]
   It therefore supplies one normalised heat clock and one
   \(F^{-1}\) factor.
3. With \(m\) later complementary interactions there are exactly
   \(m+1\) heat clocks.  Every frequency factor telescopes:
   \[
   F^{-1}
   \prod_{j=1}^m\frac{R_{j-1}}{R_j}
   SR_m=S.
   \]
   The depth-zero case is the same identity \(F^{-1}SF=S\).
4. The time-ordered convolution is
   \[
   \int_0^h
   s^{3/4}
   \mathbb P(X_0+\cdots+X_m\le h-s)\,ds.
   \]
   It is bounded by
   \((4/7)h^{7/4}\Theta_{\boldsymbol R}(h)\).
5. Summing the starting band and every continuation band below \(U\)
   gives
   \[
   \sum_{\boldsymbol R\in\mathscr N_m(U)}
   \Theta_{\boldsymbol R}(h)
   \le
   \frac{H_U^{m+1}}{(m+1)!}.
   \]
   The infinite infrared band count is harmless because the dyadic
   \(Q^2\) heat rates are summable.
6. The complementary input filters preserve the preceding annular
   support.  Their uniform \(L^1\) multiplier cost is paid once per
   continuation depth and absorbed into \(A_{\rm no}\); it introduces
   neither unweighted band entropy nor \(U\)-dependence.
7. Consequently the entire pressure path series is absolutely
   summable:
   \[
   \|\mathscr P_{S,b}r_{{\rm no},U}\|_{L^1_{t,x}}
   \le
   CSh^{7/4}\left(e^{A_{\rm no}H_U}-1\right).
   \]
   At \(U\le\kappa h^{-1/2}\), this is \(O(h^{7/4})\).
8. Finite infrared cutoffs give exact algebraic path expansions.
   Strong homogeneous \(L^2\) convergence, the ultraviolet operator
   tail, uniform Gamma majorants, and pressure continuity identify
   their limit with
   \((I-\mathsf A_{b,U})^{-1}g_U\), and then with \(r_{\rm no}\) as
   \(U\to\infty\).
9. Every fixed smooth layer therefore has a finite no-return capture
   ceiling.  A bounded subsequence of
   \(U_{\rm no}(h)\sqrt h\) would put the captured \(p_0/4\) floor below
   \(C_\kappa h^{7/4}\to0\), a contradiction.
10. The complete renewal split now leaves only:
    superparabolic capture of a pressure-bearing renewal block, or
    \[
    D_b(h)\ge h^{-3}e^{c h^{-9/4}}
    \]
    along the parabolically captured last-return branch.

## Precision additions made at review close

The final note states explicitly why transposing the solenoidal tensor
orientation gives the same scalar pressure source.  It also names the
finite infrared objects
\(g_{U,K}\), \(\mathsf A_{b,U,K}\), and
\(r_{{\rm no},U,K}\) before passing to the homogeneous limit.

The reviewer edited no files.

## Exact remaining boundary

The frequency itinerary is now reduced to one common escape:
no uniformly parabolic LP--Dyson ceiling captures the pressure-bearing
renewal component.  The next theorem must turn that operator-series
escape into a same-trajectory physical charge, or use the
\(9/4\) coefficient cost to stop the physical zoom.

The current result does not itself give an instantaneous Fourier tail,
physical high-frequency dissipation, spatial concentration, a theorem
on the rough hull, a singular solution, regularity, breakdown, or any
Clay alternative.

## Validation

- Targeted executable tests: 7 passed.
- Full suite at review time: 768 tests passed.
- Record, link, mathematical-markup, and diff checks passed.
