# Every path inside a subparabolic frequency corridor is summable

- **Experiment:** EXP-ADJOINT-PRESSURE-CORRIDOR-SUM-001
- **Route:** ROUTE-R3B
- **Status:** independently reviewed conditional analytic reduction
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** independently reviewed
  [one-return theorem](adjoint-pressure-one-return.md),
  [prescribed multistage-path theorem](adjoint-pressure-multistage-path.md),
  and [fixed-band factorial theorem](adjoint-pressure-frequency-colligation.md)
- **Review:** [valid after topology and scope repairs](../review-response-adjoint-pressure-corridor-sum-2026-07-24.md)

The prescribed-path theorem shows that intermediate cross-band scale
ratios telescope, but it does not sum the number of paths.  The
remaining entropy looks infinite because a state band may jump to
infinitely many lower dyadic bands.

The heat clocks supply exactly the missing weight.  Start with the
reviewed high-to-\(F\) return \(w_F\), insert one fixed dyadic
Littlewood--Paley resolution after every later Oseen interaction, and
retain **every** path satisfying only

\[
R_j\le U,
\qquad
U\ge F.
\tag{1}
\]

No comparability or lower-frequency cutoff is imposed.  Put

\[
L_F:=c_0\nu F^2h,
\qquad
H_U
:=
h\sum_{\substack{Q\in2^{\mathbb Z}\\Q\le U}}
c_0\nu Q^2.
\tag{2}
\]

The dyadic heat-rate entropy is finite:

\[
H_U
\le
\frac43c_0\nu U^2h.
\tag{3}
\]

At depth \(m\), summing the ordered-simplex clock product over all
frequency choices produces \(L_FH_U^m/(m+1)!\).  Therefore

\[
\boxed{
\sum_{m=0}^{\infty}
A^{m+1}
\frac{L_FH_U^m}{(m+1)!}
=
L_F
\frac{e^{AH_U}-1}{H_U}.
}
\tag{4}
\]

For the recombined corridor pressure defined below, this gives

\[
\boxed{
\int_0^h
\|\mathcal P^{\rm corr}_{S,F}(t)\|_1\,dt
\le
C_{\rm src}
\frac SF
L_F
\frac{e^{AH_U}-1}{H_U}
\mathcal B(h,F).
}
\tag{5}
\]

More generally, if \(F(h)\asymp h^{-\beta}\) with
\(0<\beta\le1/2\), and

\[
F(h)\le U(h)\lesssim h^{-1/2},
\tag{5a}
\]

then

\[
\boxed{
\int_0^h
\|\mathcal P^{\rm corr}_{S,F}(t)\|_1\,dt
\le
C_{\rm corr}S h^{1-\beta}
\mathcal B(h,F).
}
\tag{6}
\]

Thus arbitrary interaction depth and all pressure recombination inside
every subparabolic or parabolic corridor preserve the
one-return scale--clock factor.  A fixed positive floor for this entire
aggregate forces

\[
\boxed{
D_b(h)
\ge
h^{-3}
\exp\!\left(
c h^{-(11/4-\beta)}
\right).
}
\tag{6a}
\]

The least expensive case is the parabolic endpoint \(\beta=1/2\),
where the exponent is \(9/4\).

The theorem allows arbitrary upcrossings and downcrossings through every
band up to \(U\), and therefore through every band up to the parabolic
scale when \(U\asymp h^{-1/2}\).  It does not control a path which ever
exceeds \(U\), and it does not prove that the complete returned-low
pressure places a fixed fraction in the corridor.

## 1. Reviewed source and path estimate

Fix \(h,\nu,S>0\), dyadic scales \(F,U\in2^{\mathbb Z}\) with
\(U\ge F\), and \(M<\infty\).  Let \(b\) be the smooth divergence-free
drift with

\[
\sup_{0<t<h}\|b(t)\|_{L^{3,\infty}}\le M.
\tag{7}
\]

Use the fixed dyadic partition

\[
\sum_{R\in2^{\mathbb Z}}\Delta_R=I
\tag{8}
\]

on nonzero frequencies, with every \(\Delta_R\) obtained by dilating
one smooth annular symbol.  Finite sums of these multipliers may be
inserted algebraically after every interaction.  Passing to the
homogeneous infinite sum requires the additional continuity topology
explicitly withheld below (21); the zero Fourier mode alone does not
justify that passage.

Let

\[
w_F(t)
:=
\int_0^t
\Delta_Fe^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}
\left(
(P_{>64F}r(s))\boxtimes b(s)
\right)\,ds
\tag{9}
\]

be the reviewed one-return state.  Here

\[
(z\boxtimes b)_{ik}:=z_ib_k.
\tag{10}
\]

There is a nonnegative source \(G_F\) such that

\[
\|w_F(t)\|_1
\le
C_{\rm src}
\int_0^t
e^{-c_0\nu F^2(t-s)}G_F(s)\,ds
\tag{11}
\]

and

\[
\int_0^hG_F(s)\,ds
\le
\mathcal B(h,F),
\tag{12}
\]

where

\[
\boxed{
\begin{aligned}
\mathcal B(h,F)
:=
1
&+h^{7/4}
\left[
1+\log_+\!\bigl(D_b(h)h^3\bigr)
\right]\\
&+h^{21/4}
+h^{89/4}
+h^{103/4}
+h^6F^{-2}.
\end{aligned}}
\tag{13}
\]

For an annular state \(z_R\), define the output-\(Q\) Oseen block

\[
(\mathcal V_{Q,b}z_R)(t)
:=
\int_0^t
\Delta_Qe^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}
\left(
z_R(s)\boxtimes b(s)
\right)\,ds.
\tag{14}
\]

The reviewed cross-band estimate is

\[
\|\mathcal V_{Q,b}z_R(t)\|_1
\le
C_xMRQ
\int_0^t
e^{-c_0\nu Q^2(t-s)}
\|z_R(s)\|_1\,ds.
\tag{15}
\]

The fixed low-output pressure operator obeys

\[
\left\|
\Pi_S(z_R\boxtimes b)
\right\|_1
\le
C_pMSR\|z_R\|_1.
\tag{16}
\]

Put

\[
A_x:=\frac{C_xM}{c_0\nu},
\qquad
A_p:=\frac{C_pM}{c_0\nu},
\qquad
A:=\max\{A_x,A_p\}.
\tag{17}
\]

If \(M=0\), every pressure field below is zero.  In the fixed-floor
discussion take \(M>0\).

## 2. Exact Littlewood--Paley path expansion

For a finite frequency path

\[
\boldsymbol R=(R_0,\ldots,R_m),
\qquad
R_0:=F,
\tag{18}
\]

define

\[
w_{\boldsymbol R}
:=
\begin{cases}
w_F,&m=0,\\
\mathcal V_{R_m,b}
w_{(R_0,\ldots,R_{m-1})},&m\ge1.
\end{cases}
\tag{19}
\]

Let the unprojected Volterra Oseen operator be

\[
(T_bz)(t)
:=
\int_0^t
e^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}
\left(
z(s)\boxtimes b(s)
\right)\,ds.
\tag{20}
\]

For \(K\ge1\), put

\[
\mathcal D_K(F)
:=
\left\{
R\in2^{\mathbb Z}:
2^{-K}F\le R\le2^KF
\right\},
\qquad
P_K:=\sum_{R\in\mathcal D_K(F)}\Delta_R.
\tag{20a}
\]

This is a finite sum.  Repeated linearity therefore gives the exact
finite identity

\[
\boxed{
(P_KT_b)^mw_F
=
\sum_{R_1,\ldots,R_m\in\mathcal D_K(F)}
w_{(F,R_1,\ldots,R_m)}.
}
\tag{21}
\]

Passing from (21) to an identity for \(T_b^mw_F\) would additionally
require \(P_KT_b\)-iterates to converge in a topology in which
multiplication by \(b\) and \(T_b\) are continuous.  Smoothness and the
weak-\(L^3\) ceiling alone are not used here to assert that endpoint
continuity.  The theorem below needs only the individually defined path
components (19); it proves their corridor pressure series absolutely
convergent in \(L^1_{t,x}\).

Define the full corridor paths

\[
\boxed{
\mathscr C_m(F;U)
:=
\bigl\{
(F,R_1,\ldots,R_m):
R_j\in2^{\mathbb Z},\
R_j\le U
\quad(1\le j\le m)
\bigr\}.
\tag{22}
\]

For \(m=0\), this set contains the single path \((F)\).  For \(m\ge1\)
it is countably infinite because there is no lower-frequency cutoff.
The relevant entropy is not its cardinality.  With

\[
\lambda(Q):=c_0\nu Q^2,
\tag{23}
\]

the weighted one-step entropy is the convergent geometric series

\[
\boxed{
\sum_{\substack{Q\in2^{\mathbb Z}\\Q\le U}}
\lambda(Q)
\le
\frac43c_0\nu U^2.
}
\tag{23a}
\]

Indeed, if \(Q_*\) is the largest dyadic number not exceeding \(U\),
then the left side is
\(c_0\nu Q_*^2\sum_{k\ge0}4^{-k}\).  This proves (3).

## 3. Heat-rate entropy and aggregate summation

For
\(\boldsymbol R\in\mathscr C_m(F;U)\), let

\[
\lambda_j:=c_0\nu R_j^2,
\qquad
X_j\sim{\rm Exp}(\lambda_j)
\tag{24}
\]

independently.  The prescribed-path theorem gives

\[
\boxed{
\begin{aligned}
\mathfrak R_{\boldsymbol R}(h)
&:=
\int_0^h
\left\|
\Pi_S
\left(w_{\boldsymbol R}(t)\boxtimes b(t)\right)
\right\|_1\,dt\\
&\le
C_{\rm src}
A^{m+1}
\frac SF
\Theta_{\boldsymbol R}(h)
\mathcal B(h,F),
\end{aligned}}
\tag{25}
\]

where

\[
\Theta_{\boldsymbol R}(h)
:=
\mathbb P(X_0+\cdots+X_m\le h).
\tag{26}
\]

The exact ordered-simplex bound is

\[
\Theta_{\boldsymbol R}(h)
\le
\frac{h^{m+1}}{(m+1)!}
\prod_{j=0}^m\lambda_j.
\tag{27}
\]

Sum this nonnegative ceiling over every path in (22).  Since
\(R_0=F\), Tonelli's theorem and the product structure give

\[
\boxed{
\begin{aligned}
&\sum_{\boldsymbol R\in\mathscr C_m(F;U)}
\frac{h^{m+1}}{(m+1)!}
\prod_{j=0}^m\lambda_j\\
&\qquad=
\frac{L_FH_U^{m}}{(m+1)!}.
\end{aligned}}
\tag{28}
\]

Combining (25) and (28) yields

\[
\boxed{
\begin{aligned}
\sum_{\boldsymbol R\in\mathscr C_m(F;U)}
\mathfrak R_{\boldsymbol R}(h)
&\le
C_{\rm src}
\frac SF
\mathcal B(h,F)
A^{m+1}
\frac{L_FH_U^{m}}{(m+1)!}.
\end{aligned}}
\tag{29}
\]

The exponential generating function is exactly

\[
\boxed{
\begin{aligned}
\sum_{m=0}^{\infty}
A^{m+1}
\frac{L_FH_U^{m}}{(m+1)!}
&=
AL_F
\sum_{m=0}^{\infty}
\frac{(AH_U)^m}{(m+1)!}\\
&=
L_F
\frac{e^{AH_U}-1}{H_U}.
\end{aligned}}
\tag{30}
\]

This proves (4).

The collection of all finite corridor paths is countable.  Equations
(29)--(30) show that the sum of the spacetime \(L^1\) norms of their
pressure fields is finite.  Hence that pressure series converges
unconditionally in
\(L^1((0,h)\times\mathbb R^3)\).  Define

\[
\boxed{
\mathcal P^{\rm corr}_{S,F}
:=
\sum_{m=0}^{\infty}
\sum_{\boldsymbol R\in\mathscr C_m(F;U)}
\Pi_S
\left(
w_{\boldsymbol R}\boxtimes b
\right).
}
\tag{31}
\]

Equivalently, one may first restrict every band to
\(2^{-K}F\le R_j\le U\), sum to depth \(N\), and let
\(K,N\to\infty\) in either order.  Absolute convergence makes the limit
independent of that enumeration.

The triangle inequality and (30) give

\[
\begin{aligned}
\int_0^h
\|\mathcal P^{\rm corr}_{S,F}(t)\|_1\,dt
&\le
\sum_{m=0}^{\infty}
\sum_{\boldsymbol R\in\mathscr C_m(F;U)}
\mathfrak R_{\boldsymbol R}(h)\\
&\le
C_{\rm src}
\frac SF
L_F
\frac{e^{AH_U}-1}{H_U}
\mathcal B(h,F),
\end{aligned}
\tag{32}
\]

which proves (5).  Thus arbitrary reinforcement under pressure
recombination is controlled; cancellation would only make the left side
smaller.

## 4. Subparabolic and parabolic corridors

First take

\[
F(h)\asymp h^{-\beta},
\qquad
0<\beta\le\frac12,
\qquad
F(h)\le U(h)\lesssim h^{-1/2}.
\tag{32a}
\]

Then

\[
L_F\asymp h^{1-2\beta},
\qquad
L_F\le H_U\le C.
\tag{32b}
\]

On a fixed bounded interval of \(H>0\),

\[
\frac{e^{AH}-1}{H}
\le
C_A.
\tag{32c}
\]

Since \(S/F\asymp Sh^\beta\), equation (32) gives

\[
\boxed{
\int_0^h
\|\mathcal P^{\rm corr}_{S,F}(t)\|_1\,dt
\le
C_{\rm corr}S h^{1-\beta}
\mathcal B(h,F).
}
\tag{32d}
\]

Here \(C_{\rm corr}\) depends on \(M,\nu\), the fixed cutoff constants,
the comparison constants in \(F\asymp h^{-\beta}\), and the uniform
bound on \(Uh^{1/2}\), but not on the possibly divergent ratio \(U/F\).

If this aggregate has a fixed positive floor, the constant and all
explicit positive-power terms vanish after multiplication by
\(h^{1-\beta}\).  The logarithmic term must satisfy

\[
\log_+\!\bigl(D_b(h)h^3\bigr)
\ge
c h^{-(11/4-\beta)}.
\tag{32e}
\]

This proves (6)--(6a).  The exponent is strictly decreasing on
\((0,1/2]\), so its minimum is \(9/4\) at the parabolic endpoint.

For completeness, specialise that endpoint directly.  Fix
\(S,M,\nu>0\).  Along a sequence \(h\downarrow0\), choose dyadic
\(F(h)\le U(h)\) with

\[
0<\mu_-\le F(h)h^{1/2}\le\mu_+<\infty,
\qquad
U(h)h^{1/2}\le\upsilon_+<\infty.
\tag{34}
\]

Then both heat budgets obey

\[
L_F\le c_0\nu\mu_+^2,
\qquad
H_U
\le\frac43c_0\nu\upsilon_+^2,
\tag{35}
\]

so the exponential factor in (32) is independent of \(h\).  Moreover,

\[
\frac SF\asymp Sh^{1/2},
\qquad
h^6F^{-2}=O(h^7).
\tag{36}
\]

Equation (32) now becomes

\[
\boxed{
\int_0^h
\|\mathcal P^{\rm corr}_{S,F}(t)\|_1\,dt
\le
C_{\rm corr}Sh^{1/2}
\left\{
1+h^{7/4}
\left[
1+\log_+\!\bigl(D_b(h)h^3\bigr)
\right]
+o(h^{7/4})
\right\}.
}
\tag{37}
\]

Assume this complete corridor aggregate carries a fixed floor:

\[
\int_0^h
\|\mathcal P^{\rm corr}_{S,F}(t)\|_1\,dt
\ge\eta>0.
\tag{38}
\]

The constant and explicit positive-power terms in braces, after
multiplication by \(h^{1/2}\), tend to zero.  Equations (37)--(38)
therefore force

\[
\log_+\!\bigl(D_b(h)h^3\bigr)
\ge
c h^{-9/4}.
\tag{39}
\]

This is the \(\beta=1/2\) case of (6a).  The floor (38) remains an
additional antecedent.

## 5. Exact advance and remaining boundary

The theorem closes the following infinite-depth branch:

> After one high-to-subparabolic-or-parabolic return, a pressure packet
> survives by wandering for arbitrarily many interactions and arbitrary
> dyadic jumps below a parabolic ceiling \(U\).

It cannot do so cheaply.  The complete corridor pressure series is
absolutely summable, all path reinforcement is controlled, and a fixed
aggregate floor pays exponent \(11/4-\beta\ge9/4\), with equality only
for a parabolic return.

The full returned-low pressure is not yet identified with (31).
Every omitted path has a first corridor exit
\(R_j>U\).  The next theorem must charge or sum those excursions,
or prove that a fixed fraction of the complete pressure lies in the
reviewed high-state, one-return, or full-corridor components.  This note
does not prove such participation, a singular Oseen or Navier--Stokes
solution, or any Clay alternative.

The subsequent independently reviewed
[smooth-layer identification theorem](adjoint-pressure-corridor-identification.md)
closes the qualitative topology issue for the specified
separated-return block and sums every separated starting band.  It does
not retroactively supply global participation, control histories with
no separated return, or charge superparabolic LP--Dyson capture escape.
The later independently reviewed
[last-separated-return renewal theorem](adjoint-pressure-last-return-renewal.md)
then removes global participation as an antecedent by partitioning the
complete feedback pressure into the exact no-chargeable-return block or
a finitely capturable last-return block.  It still does not charge the
former or a superparabolic capture escape.

## 6. Executable certificate

The dyadic heat-rate entropy, exact factorial term, exponential
generating series, and subparabolic exponent ledger are checked by

```bash
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_corridor_sum -v
PYTHONPATH=lab python -m \
  navier_lab.adjoint_pressure_corridor_sum
```
