# Review response: intermediate feedback localisation

**Date:** 2026-07-24
**Route:** ROUTE-R3B
**Verdict:** valid in the stated conditional scope
**Clay status:** unsolved

The independent adversarial reviewer audited
[the theorem](experiments/adjoint-pressure-intermediate-localization.md)
against
[the review request](review-letter-adjoint-pressure-intermediate-localization-2026-07-24.md).
No invalid implication remains.

## Accepted theorem

The reviewer accepted that the source-localised payer in the reviewed
feedback-shell alternative is empty. If

\[
c_h=b_h^{\rm in}
=\chi_{h^{-3}}b_h,
\qquad
\int_0^h\|\nabla c_h\|_2^2\,d\tau\lesssim h^{-3},
\]

then, at every intermediate radius
\(L=h^{-\alpha}\) with \(1/30<\alpha<3\),

\[
\begin{aligned}
\int_0^h\|\mathcal T(r_h,c_h)\|_1\,d\tau
\lesssim{}&
h^{3/2}L^{1/2}
+h^2L^{-1/2}\\
&+h^{1/4}L^{-1/2}
+h^{-1/4}L^{-15/2}.
\end{aligned}
\]

All four terms vanish. At \(\alpha=1/10\), their powers are

\[
\frac{29}{20},
\qquad
\frac{41}{20},
\qquad
\frac3{10},
\qquad
\frac12.
\]

This contradicts a fixed source-localised pressure floor.

## Referee checks

The reviewer independently confirmed:

1. \(8L<4R_{\rm src}\) makes the source-cutoff coefficient equal the
   original coefficient throughout the near ball;
2. centre-uniform local energy and the weak-\(L^3\) cutoff term give
   the near gradient cost \(L+hL^{-1}\);
3. every component of
   \(\nabla[(1-\chi_L)c_h]\), including the distant source-cutoff
   transition, lies where the Bogovskii-corrected exterior remainder
   equals \(r_h\);
4. the far coefficient gradient costs at most \(Ch^{-3}\);
5. CLMS gives the displayed powers with no missing pressure or cutoff
   term;
6. the simultaneous exponent interval is exactly
   \(1/30<\alpha<3\); and
7. the feedback-shell alternative is exhaustive, so vanishing of the
   local payer forces its exterior pressure fraction and hence the
   stretched-exponential bound
   \[
   D_b(h)
   \ge
   h^{-3}\exp(c_{\rm sh}h^{-7/4}).
   \]

## Exact retained boundary

The conclusion applies only to the selected zero-data drift-feedback
branch. It eliminates its inverse-cubic source-localised child and all
conditional descendants of that child. It does not sum the
stretched-exponential cost along one trajectory, lower-bound the
physical zoom, exclude the direct-response or signed late-annulus
branches, or prove any Clay alternative A--D.

## Validation

The reviewer ran:

- the focused executable and 5 focused tests;
- all 604 repository tests;
- records, links, and mathematical-markup validation;
- `git diff --check`.

All passed.
