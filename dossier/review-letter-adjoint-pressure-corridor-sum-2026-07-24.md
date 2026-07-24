# Independent review request: the full subparabolic frequency corridor

**Date:** 2026-07-24

**Route:** ROUTE-R3B

**Clay status claimed by author:** unsolved

Please review
[`experiments/adjoint-pressure-corridor-sum.md`](experiments/adjoint-pressure-corridor-sum.md)
adversarially.  The proposed theorem starts with the reviewed
high-to-\(F\) return, inserts one fixed dyadic Littlewood--Paley
resolution after every later interaction, and sums every prescribed
path satisfying only \(R_j\le U\), where \(U\ge F\).  Arbitrary dyadic upcrossings
and downcrossings are allowed; there is no lower-frequency cutoff or
finite-branching assumption.

Put

\[
L_F=c_0\nu F^2h,
\qquad
H_U
=
h\sum_{\substack{Q\in2^{\mathbb Z}\\Q\le U}}
c_0\nu Q^2.
\]

The central claim is that the simplex clock products sum over the
infinite dyadic entropy:

\[
\sum_{\boldsymbol R\in\mathscr C_m}
\frac{h^{m+1}}{(m+1)!}
\prod_{j=0}^m\lambda_j
=
\frac{L_FH_U^m}{(m+1)!},
\]

and hence

\[
\int_0^h
\|\mathcal P^{\rm corr}_{S,F}(t)\|_1\,dt
\le
C_{\rm src}\frac SF
L_F\frac{e^{AH_U}-1}{H_U}
\mathcal B(h,F).
\]

For \(F\asymp h^{-\beta}\), \(0<\beta\le1/2\), and
\(F\le U\lesssim h^{-1/2}\), a fixed aggregate floor then forces

\[
D_b(h)
\ge
h^{-3}\exp\!\left(c h^{-(11/4-\beta)}\right),
\]

with minimum exponent \(9/4\) at \(\beta=1/2\).

Please try to falsify, in particular:

1. the exact finite-truncation expansion
   \[
   (P_KT_b)^mw_F
   =
   \sum_{R_1,\ldots,R_m\in\mathcal D_K(F)}
   w_{(F,R_1,\ldots,R_m)};
   \]
2. the note's refusal to infer the untruncated identity without an
   additional topology in which multiplication by \(b\) and \(T_b\)
   are continuous;
3. whether the individually defined path components still satisfy the
   reviewed path estimate uniformly;
4. the dyadic entropy identity
   \[
   \sum_{Q\le U}c_0\nu Q^2
   \le(4/3)c_0\nu U^2;
   \]
5. the number of clocks: \(m\) post-return interactions but \(m+1\)
   exponential clocks;
6. the Tonelli factorisation of the full depth-\(m\) weighted path sum;
7. the exact generating-series indexing
   \[
   \sum_{m\ge0}
   A^{m+1}\frac{L_FH_U^m}{(m+1)!}
   =
   L_F\frac{e^{AH_U}-1}{H_U};
   \]
8. whether finite total \(L^1_{t,x}\) norms prove unconditional
   convergence of the countable recombined pressure series;
9. whether arbitrary jumps inside the ceiling really are included;
10. the subparabolic reduction
    \[
    (S/F)L_F\asymp SFh\asymp Sh^{1-\beta};
    \]
11. the forced exponent \(11/4-\beta\) and its parabolic minimum;
12. uniformity when \(U/F\) grows, provided
    \(U\lesssim h^{-1/2}\), and dependence on \(M,\nu\) and the fixed
    cutoffs; and
13. the scope boundary: identification with the complete Dyson
    remainder, paths exiting above \(U\), and a participation
    floor all remain unproved.

Please classify the disposition as:

- valid in the exact stated conditional scope;
- repairable, with precise corrections; or
- invalid, identifying the first fatal implication.

The executable certificate is:

```bash
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_corridor_sum -v
PYTHONPATH=lab python -m \
  navier_lab.adjoint_pressure_corridor_sum
```
