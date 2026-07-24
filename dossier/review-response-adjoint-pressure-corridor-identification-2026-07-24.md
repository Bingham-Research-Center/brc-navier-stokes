# Independent review response: smooth-layer corridor identification

**Date:** 2026-07-24

**Reviewed packet:**
[`review-letter-adjoint-pressure-corridor-identification-2026-07-24.md`](review-letter-adjoint-pressure-corridor-identification-2026-07-24.md)

**Primary theorem:**
[`experiments/adjoint-pressure-corridor-identification.md`](experiments/adjoint-pressure-corridor-identification.md)

**Verdict:** valid in the stated conditional scope after one
smooth-layer source repair

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found no fatal defect after the note
made the layerwise Sobolev hypothesis for the infinite starting-source
sum explicit.  The accepted result is a smooth-layer topology and
capture theorem for one specified separated-return Oseen block.

It does not prove that this block participates in the complete feedback
pressure, control histories with no separated return, convert LP capture
escape into an instantaneous energy tail, pass the layerwise smooth
constants to the rough hull, or prove any Clay alternative A--D.

## Accepted chain

1. The heat--Leray \(L^2\) estimate gives the exact fractional Volterra
   majorant
   \[
   \|T_b^mw\|_{C_tL^2_x}
   \le
   \|w\|_{C_tL^2_x}
   \frac{(a\Gamma(1/2)\sqrt h)^m}
        {\Gamma(m/2+1)}.
   \]
   Its Mittag--Leffler series converges without a smallness assumption.
2. Strong homogeneous Littlewood--Paley convergence in \(L^2\), uniform
   on the compact range of a \(C_tL^2_x\)-valued function, gives
   convergence of every fixed truncated iterate.  There is no
   polynomial-remainder issue in \(L^2\).
3. The reviewed fixed low-output pressure operator is continuous from
   \(C_tL^2_x\) to spacetime \(L^1\).  It therefore identifies the
   truncated mild pressure exactly with the absolutely convergent
   corridor path series.
4. Subtracting the full and low-insertion mild equations gives the
   exact first-high-insertion identity
   \[
   d_U=T_bd_U+\mathsf H_UT_bv_U.
   \]
   This is an LP--Dyson grouping, not an instantaneous Fourier-energy
   statement.
5. For all separated starting bands \(F_*\le F\le U\),
   \[
   \frac SF(c_0\nu F^2h)\mathcal B(h,F)
   =
   c_0\nu ShF
   [\mathcal B_0(h)+h^6F^{-2}].
   \]
   The two dyadic sums are bounded by \(2U\) and \(2/F_*\).
   At \(U\le\kappa h^{-1/2}\), the complete multi-start aggregate is
   therefore bounded by
   \[
   C_\kappa Sh^{1/2}\mathcal B_0(h)
   +C_\kappa(S/F_*)h^7.
   \]
6. A fixed floor for that parabolic aggregate forces
   \[
   \log_+\!\bigl(D_b(h)h^3\bigr)
   \gtrsim h^{-9/4},
   \qquad
   D_b(h)\ge h^{-3}e^{c h^{-9/4}}.
   \]
7. The repaired explicit hypothesis
   \(r\in L^\infty_tH^s_x\), \(s>0\), gives
   \[
   \|w_F\|_{C_tL^2_x}
   \lesssim
   B_\infty\nu^{-1}
   \|r\|_{L^\infty H^s}F^{-s-1}.
   \]
   Hence the infinite separated-return source converges on each fixed
   smooth layer.
8. The two-term fixed-depth decomposition in equation (40a), followed
   by the uniform Gamma tail, proves \(V_U\to V_\infty\).  Pressure
   continuity makes the finite capture ceiling well-defined.
9. After subsequence extraction, either one uniformly parabolic ceiling
   captures half the separated-return continuation pressure, or no such
   ceiling does and the minimum capture frequency is
   superparabolic.  The first branch pays the \(9/4\) cost; the second
   is exactly LP--Dyson capture escape.

## Repair made during review

The first draft invoked convergence of
\(W_\infty=\sum_Fw_F\) from smoothness without listing the needed state
regularity among its assumptions.  The final note now states the
layerwise hypothesis \(r\in L^\infty_tH^s_x\), proves the
\(F^{-s-1}\) source bound, and writes the two-term convergence argument
for \(V_U\to V_\infty\).  These constants remain deliberately
non-uniform along the genealogy.

The note also records the PDE sign convention, avoids double-counting
the depth-zero return, distinguishes an oriented Oseen block from any
additional stretching orientation, and describes the escape branch
only as failure of parabolic LP capture.

The reviewer edited no files.

## Exact remaining boundary

The next theorem must supply at least one genuinely new PDE statement:

1. a fixed participation floor for the separated-return continuation;
2. a charge for histories which reach the detector without a separated
   return;
3. uniform parabolic spectral tightness; or
4. a same-trajectory dissipation charge for superparabolic LP capture
   escape.

None follows from the current layerwise topology theorem.

## Validation

- Targeted tests: 8 passed.
- Full suite at review time: 751 tests passed.
- Records, links, mathematical markup, and diff checks passed.
