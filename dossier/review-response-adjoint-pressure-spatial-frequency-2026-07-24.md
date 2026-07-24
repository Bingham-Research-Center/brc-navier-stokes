# Independent review response: spatial-shell/frequency-tail amplification

**Date:** 2026-07-24

**Reviewed packet:**
[`review-letter-adjoint-pressure-spatial-frequency-2026-07-24.md`](review-letter-adjoint-pressure-spatial-frequency-2026-07-24.md)

**Primary theorem:**
[`experiments/adjoint-pressure-spatial-frequency.md`](experiments/adjoint-pressure-spatial-frequency.md)

**Verdict:** accepted after six precision repairs

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI re-derived the annular
Littlewood--Paley support identity, both separated-support estimates,
the dyadic \(F^{-1}\) summation, the inner cutoff budget, the shell
leakage, the inversion, and the physical scaling.  It found no fatal
implication.  The theorem was accepted after the following repairs:

1. \(c\in H^1\) and three nested fixed-shape annuli with gaps comparable
   to \(L\) are now explicit.
2. The exact support sum is over \(K>4F\); only the subsequent upper
   bound is enlarged to \(K\ge2F\).
3. The tensor convention is explicit and gives
   \(\operatorname{div}(z\otimes c)=(z\cdot\nabla)c\) for solenoidal
   \(z\), without requiring the cutoff pieces \(c_k\) to be solenoidal.
4. Weak \(L^3\) finite-annulus control and the cutoff product rule now
   verify \(c_k\in H^1\).
5. The inversion fixes \(S>0\).
6. The fixed high-state pressure floor is explicitly an additional
   antecedent, not a consequence of the full pressure floor, exterior
   shell survival, or causal interaction depth.

No reviewer edits were made.

## Accepted theorem

For \(F\ge16S\), the selected low-output pressure from the state tail
above \(4F\) satisfies

\[
\boxed{
\begin{aligned}
\mathfrak P_{S,F}(h)
\le
C\frac SF\bigg\{
1
&+h^{7/4}
\left[
1+\log_+\!\bigl(D_b(h)h^3\bigr)
\right]\\
&+h^{21/4}
+h^{89/4}
+h^{103/4}
+h^6F^{-2}
\bigg\}.
\end{aligned}}
\]

The reviewer confirmed that the off-diagonal shell error inside braces
is \(h^6F^{-2}\), and that dyadic Cauchy--Schwarz gives a full
\(F^{-1}\), not \(F^{-1/2}\).

Consequently, for fixed \(S>0\), the additional antecedent

\[
\mathfrak P_{S,F(h)}(h)\ge p_{\rm sf}>0,
\qquad
F(h)\to\infty,
\]

forces

\[
\boxed{
D_b(h)
\ge
h^{-3}
\exp\!\left(
c_{\rm sf}\frac{F(h)}S h^{-7/4}
\right).
}
\]

If \(F(h)=h^{-\beta}\), this becomes

\[
D_b(h)
\ge
h^{-3}\exp\!\left(c h^{-(7/4+\beta)}\right).
\]

At the hypothetical dyadic causal top,
\(\beta=c_{\rm dep}\log2\), the exponent is
\(7/4+c_{\rm dep}\log2\).

## Exact accepted frontier

On one common physical trajectory, absolute continuity of dissipation
then requires

\[
\sigma_h
=
o\!\left[
h^3
\exp\!\left(
-c_{\rm sf}\frac{F(h)}S h^{-7/4}
\right)
\right].
\]

This is a frequency-dependent necessary cost, not a contradiction.  No
reviewed theorem currently infers a fixed high-state pressure fraction
above a growing \(F\) from logarithmic interaction depth.  The live
branch is therefore an exhaustive frequency-itinerary or pressure
recombination theorem: prove that the persistent complete feedback
packet must enter this high-state alternative, or control the
complementary returned-low-frequency histories.

## Validation

- Targeted exact tests: 10 passed.
- Executable exponent audit: passed.
- Reviewer full suite: 700 tests passed.
- `make check`: passed.
- `git diff --check`: passed.
