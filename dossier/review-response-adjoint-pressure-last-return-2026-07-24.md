# Independent review response: last-separated-return renewal

**Date:** 2026-07-24

**Reviewed packet:**
[`review-letter-adjoint-pressure-last-return-2026-07-24.md`](review-letter-adjoint-pressure-last-return-2026-07-24.md)

**Primary theorem:**
[`experiments/adjoint-pressure-last-return-renewal.md`](experiments/adjoint-pressure-last-return-renewal.md)

**Verdict:** valid as a smooth-layer conditional reduction after
filter-topology, source-scope, and quantifier repairs

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found no fatal defect after the note
replaced a disjoint-block interpretation by an exact complementary
filter partition, proved an inverse-linear high-output operator tail,
charged the complementary filters in the per-depth path constant, and
made the inherited one-return source hypotheses explicit.

The accepted result removes a former participation **assumption** only
by replacing it with an exhaustive alternative.  It does not exclude
the no-chargeable-feedback-return component, exclude superparabolic
LP--Dyson capture escape, pass a spectral charge to the rough hull, or
prove any Clay alternative A--D.

## Accepted chain

1. Output band by output band,
   \[
   \mathsf J_Q+
   \mathbf 1_{\{Q\ge F_*\}}P_{>64Q}=I.
   \]
   Hence \(\mathsf A_b+\mathsf B_b=T_b\) exactly despite smooth LP
   overlap.  This is a filter identity, not a positivity or
   disjoint-support statement.
2. Expanding the nested high-pass tails by input band gives
   \[
   \sum_{F\ge F_*}
   F^2e^{-c\nu F^2\tau}\|P_{>64F}z\|_2^2
   \lesssim
   \frac1{\nu\tau}\|z\|_2^2.
   \]
   Both complementary operators therefore have the reviewed
   fractional Volterra kernel and convergent Gamma-series inverse
   without a smallness assumption.
3. Each band-\(Q\) output obeys
   \[
   \|\mathsf C_{b,Q}z\|_{X_h}
   \lesssim
   \frac{B_\infty}{\nu Q}\|z\|_{X_h}.
   \]
   Almost orthogonality and
   \(\sum_{Q>U}Q^{-2}\lesssim U^{-2}\) give
   \[
   \left\|\sum_{Q>U}\mathsf C_{b,Q}\right\|_{X_h\to X_h}
   \lesssim\frac{B_\infty}{\nu U}.
   \]
   Only this ultraviolet tail is asserted in operator norm; the
   homogeneous infrared end is taken strongly in \(L^2\).
4. From \((I-\mathsf A_b)r=g+\mathsf B_br\),
   \[
   r=(I-\mathsf A_b)^{-1}g
     +(I-\mathsf A_b)^{-1}\mathsf B_br.
   \]
   The second term selects the leftmost operator \(\mathsf B_b\),
   hence the last \(\mathsf B_b\) chronologically.  Every non-all-
   \(\mathsf A_b\) word occurs exactly once.
5. The exact source identity
   \[
   \mathsf B_br=\sum_{F\ge F_*}w_F
   \]
   holds strongly without an added Sobolev hypothesis.  The operator
   tails and uniform Gamma majorants give
   \(r_{{\rm last},U}\to r_{\rm last}\) in \(C_tL^2_x\), and the fixed
   pressure observation converges in spacetime \(L^1\).
6. Each complementary filter preserves the preceding annular support
   and has a uniform \(L^1\) multiplier norm.  At depth \(m\) it costs
   \(C_{\rm LP}^m\), correctly absorbed into
   \(A_{\rm filt}^{m+1}\).  There is no extra input-band entropy or
   hidden dependence on \(U\).
7. The reviewed all-starting-band corridor sum therefore remains
   \[
   \|\mathscr P_{S,b}r_{{\rm last},U}\|_{L^1_{t,x}}
   \le
   C_\kappa Sh^{1/2}\mathcal B_0(h)
   +C_\kappa(S/F_*)h^7
   \quad(U\le\kappa h^{-1/2}).
   \]
8. A complete feedback pressure floor \(p_0\) forces either a
   \(p_0/2\) no-chargeable-return floor or a \(p_0/2\) last-return
   floor.  In the latter case a finite ceiling captures a
   \(p_0/4\) fraction.  Subsequences then have either superparabolic
   capture escape or a uniformly parabolic ceiling, and the latter
   forces, for sufficiently small \(h\),
   \[
   D_b(h)\ge h^{-3}\exp(c h^{-9/4}).
   \]

## Repairs made during review

The first candidate described \(\mathsf A_b\)-paths as a literal
subfamily of disjoint LP paths.  The accepted note instead defines
the complementary input filter separately for each output band.  Its
uniform \(L^1\) cost is placed in the per-depth exponential constant.

The candidate's qualitative high-output convergence argument was
replaced by the explicit \(O(U^{-1})\) \(X_h\)-operator tail.  The note
also distinguishes that ultraviolet estimate from strong homogeneous
convergence at frequency zero and records
\[
\mathsf A_{b,U}
=\mathsf L_UT_b-\sum_{F_*\le Q\le U}\mathsf B_{b,Q}.
\]

Finally, the note now defines \(D_b(h)\), states that Sections 5--6
inherit the full reviewed one-return source ledger, renames the
filtered exponential factor, and writes the superparabolic and
sufficiently-small-\(h\) quantifiers explicitly.

The reviewer edited no files.

## Exact remaining boundary

Along the selected feedback sequence, one of three things remains:

1. pressure survives in the no-chargeable-feedback-return component;
2. the last-return pressure requires superparabolic LP--Dyson capture;
3. the coefficient pays the \(9/4\) stretched-exponential
   dissipation cost.

The participation antecedent is gone, but the first two branches need
a genuinely new PDE theorem.

## Validation

- Targeted executable tests after the final repairs: 10 passed.
- Full suite after canonical synchronisation: 761 tests passed.
- Record validation: 102 experiments.
- Local-link validation: 779 targets.
- Mathematical markup and diff checks passed at review close.
