# Independent review response: the full subparabolic frequency corridor

**Date:** 2026-07-24

**Route:** ROUTE-R3B

**Clay status:** unsolved

**Reviewed request:**
`review-letter-adjoint-pressure-corridor-sum-2026-07-24.md` (archived in Git at `c277792`)

**Reviewed note:**
[`experiments/adjoint-pressure-corridor-sum.md`](experiments/adjoint-pressure-corridor-sum.md)

## Verdict

**Valid in the exact stated conditional scope after one topology repair
and four scope precisions.**

The independent mathematical AI found no fatal analytic implication.
It re-derived the infinite dyadic heat-rate entropy, the full weighted
path sum, unconditional pressure convergence, and the subparabolic
inversion.

## Verified aggregate calculation

For a finite Littlewood--Paley truncation, the reviewer verified the
exact algebraic identity

\[
(P_KT_b)^mw_F
=
\sum_{R_1,\ldots,R_m\in\mathcal D_K(F)}
w_{(F,R_1,\ldots,R_m)}.
\]

It agreed that the untruncated homogeneous identity needs an additional
topology in which multiplication by \(b\) and \(T_b\) are continuous.
The accepted note now explicitly withholds that inference.  The
corridor theorem uses only the individually defined path components.

Every such component satisfies the reviewed multistage estimate
uniformly.  A depth-\(m\) path has \(m+1\) clocks: the initial return
clock and \(m\) later clocks.  With

\[
L_F=c_0\nu F^2h,
\qquad
H_U
=
h\sum_{\substack{Q\in2^{\mathbb Z}\\Q\le U}}c_0\nu Q^2,
\]

the reviewer recovered the exact Tonelli factorisation

\[
\sum_{\boldsymbol R\in\mathscr C_m(F;U)}
\frac{h^{m+1}}{(m+1)!}
\prod_{j=0}^m\lambda_j
=
\frac{L_FH_U^m}{(m+1)!}.
\]

The lower-band entropy is finite:

\[
\sum_{Q\le U}c_0\nu Q^2
=
\frac43c_0\nu Q_*^2
\le
\frac43c_0\nu U^2,
\]

where \(Q_*\) is the largest dyadic band below \(U\).  Thus the
unweighted countably infinite branching is harmless after weighting by
the heat clocks.

The reviewer also verified the generating series

\[
\sum_{m\ge0}
A^{m+1}\frac{L_FH_U^m}{(m+1)!}
=
L_F\frac{e^{AH_U}-1}{H_U}.
\]

The sum of the spacetime \(L^1\) norms of all path-pressure fields is
finite.  Their recombined pressure series therefore converges
unconditionally, independently of the depth and lower-band enumeration.
Every finite path with \(R_j\le U\) is included, with no comparability
or finite-branching assumption.

Finally, if

\[
F\asymp h^{-\beta},
\qquad
0<\beta\le\frac12,
\qquad
F\le U\lesssim h^{-1/2},
\]

then

\[
H_U=O(1),
\qquad
L_F\asymp h^{1-2\beta},
\qquad
\frac SF L_F\asymp Sh^{1-\beta}.
\]

A fixed aggregate floor consequently forces

\[
D_b(h)
\ge
h^{-3}
\exp\!\left(c h^{-(11/4-\beta)}\right).
\]

The least expensive case is \(\beta=1/2\), with exponent \(9/4\).

## Repairs adopted

The accepted note now:

1. states only the exact finite LP-truncation identity and explicitly
   withholds the untruncated LP--Dyson identification;
2. says arbitrary jumps are covered up to \(U\), and up to the
   parabolic scale only when \(U\asymp h^{-1/2}\);
3. allows \(U/F\) to diverge rather than calling \(U\) a fixed multiple
   of \(F\);
4. states the full forced exponent \(11/4-\beta\ge9/4\), with equality
   only at the parabolic endpoint; and
5. records that the aggregate constant is uniform in \(U/F\) when
   \(Uh^{1/2}\) is uniformly bounded.

## Scope boundary

The theorem proves absolute summability of the pressure fields attached
to every finite path below \(U\).  It does not identify that series with
the complete Dyson remainder, derive a fixed participation floor,
control paths exiting above \(U\), construct a singularity, or prove any
Clay alternative.
