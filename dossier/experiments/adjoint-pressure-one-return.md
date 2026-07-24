# One separated Oseen return preserves spatial--frequency amplification

- **Experiment:** EXP-ADJOINT-PRESSURE-ONE-RETURN-001
- **Route:** ROUTE-R3B
- **Status:** adversarially recomputed conditional analytic reduction
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** adversarially recomputed
  [spatial--frequency amplification theorem](adjoint-pressure-spatial-frequency.md),
  [terminal-return theorem](adjoint-pressure-terminal-return.md), and
  [feedback-shell theorem](adjoint-pressure-feedback-shells.md)
- **Review:** [valid in the stated conditional scope](../review-ledger.md)

The spatial--frequency theorem charges pressure observed while the
zero-data Oseen state is still above a growing frequency \(F\).  Its
unresolved complement consists of histories which visit high frequency
and return low before the terminal pressure observation.

This note closes the first nontrivial member of that complement.

> If the state tail above \(64F\) makes one heat-mediated Oseen return
> to the annulus \(F\), and that returned state then generates pressure
> in a fixed band \(S\ll F\), the return does not erase the inverse
> frequency gain.  Its exact extra heat clock is
> \(\min\{h,F^{-2}\}\).

For the one-return pressure functional defined below,

\[
\boxed{
\begin{aligned}
\mathfrak R^{(1)}_{S,F}(h)
\le
C_\nu M\frac SF
\min\{1,F^2h\}
\bigg\{
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
\tag{1}
\]

Consequently, if \(F=h^{-\beta}\) and a fixed positive pressure
fraction is carried by this one-return component, then

\[
\boxed{
D_b(h)
\ge
h^{-3}
\exp\!\left(
c h^{-\gamma_1(\beta)}
\right),
\qquad
\gamma_1(\beta)
:=
\frac74+\beta+(1-2\beta)_+.
}
\tag{2}
\]

Equivalently,

\[
\boxed{
\gamma_1(\beta)
=
\begin{cases}
\displaystyle\frac{11}{4}-\beta,
&0<\beta\le\frac12,\\[5pt]
\displaystyle\frac74+\beta,
&\beta\ge\frac12.
\end{cases}
\qquad
\gamma_1(\beta)\ge\frac94.
}
\tag{3}
\]

Thus one separated return costs at least the \(9/4\) stretched
exponent.  Below the parabolic frequency it costs more than a direct
terminal high-state observation because the return has too little time
to use its full heat clock.

The pressure floor for this particular component is an additional
antecedent.  The theorem does not prove that every returned-low history
contains such a single separated final return.  A gradual descent
through several comparable bands remains open.

## 1. Reviewed state and spatial ledgers

Retain the selected zero-data feedback remainder \(r\) and drift \(b\)
on \((0,h)\).  The reviewed bounds are

\[
\sup_{0<t<h}\|b(t)\|_{L^{3,\infty}}\le M,
\tag{4}
\]

\[
\int_0^h\|r(t)\|_2^2\,dt\le C_rh^3,
\tag{5}
\]

and, for \(L\ge2\),

\[
\int_0^h
\|r(t)\|_{L^2(|x|>2L)}^2\,dt
\le
C_T
\left(
h^{7/2}L^{-1}
+h^{5/2}L^{-15}
\right).
\tag{6}
\]

Put \(R_0=h^{-3}\).  Use the reviewed source cutoff
\(c_{\rm in}=\chi_{R_0}b\), and decompose the exterior drift into
fixed-shape annuli

\[
b=c_{\rm in}+\sum_{k\ge0}c_k,
\qquad
L_k=2^kR_0.
\tag{7}
\]

If

\[
X_k
:=
\left(
\int_0^h
\|r(t)\|_{L^2(|x|>cL_k)}^2\,dt
\right)^{1/2},
\qquad
Y_k
:=
\left(
\int_0^h\|\nabla c_k(t)\|_2^2\,dt
\right)^{1/2},
\tag{8}
\]

the reviewed shell calculation gives

\[
\boxed{
\begin{aligned}
\sum_{k\ge0}X_kY_k
\le C\bigg[
&h^{7/4}
\left(
1+\log_+\!\bigl(D_b(h)h^3\bigr)
\right)\\
&+h^{21/4}
+h^{89/4}
+h^{103/4}
\bigg].
\end{aligned}}
\tag{9}
\]

The inner drift obeys

\[
\int_0^h\|\nabla c_{\rm in}(t)\|_2^2\,dt
\le C_{\rm in}h^{-3}.
\tag{10}
\]

These are the only spatial inputs used below.

## 2. Annular heat--Leray return

Let \(\Delta_F\) be a fixed smooth annular multiplier supported in

\[
\left\{\frac F2\le|\xi|\le2F\right\},
\tag{11}
\]

and retain the smooth high pass

\[
P_{>64F}:=\sum_{K>64F}\Delta_K.
\tag{12}
\]

For the state interaction use the Oseen tensor convention

\[
(z\boxtimes c)_{ik}:=z_i c_k.
\tag{13}
\]

When \(c\) is solenoidal,

\[
\operatorname{div}(z\boxtimes c)=c\cdot\nabla z.
\tag{14}
\]

In general,

\[
\operatorname{div}(z\boxtimes c)
=c\cdot\nabla z+z\,\operatorname{div}c.
\tag{14a}
\]

The cutoff pieces in (7) need not be solenoidal: all estimates below
are applied directly to the complete tensor divergence in (13), so the
second term in (14a) is not dropped.  These terms cancel only when the
exact coefficient partition is summed back to the solenoidal drift
\(b\).

For \(0<s<t<h\), define

\[
\mathcal V_F(z,c;t,s)
:=
\Delta_F e^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}
\left(
(P_{>64F}z(s))\boxtimes c(s)
\right).
\tag{15}
\]

### Lemma 1: local annular return

Suppose \(c\in H^1(\mathbb R^3)\) is supported in a fixed-shape
annulus \(A_L\), and choose nested fixed-shape enlargements

\[
A_L\Subset A_L^+\Subset A_L^{++}
\tag{16}
\]

with gaps comparable to \(L\).  If \(FL\ge1\), then

\[
\boxed{
\begin{aligned}
\|\mathcal V_F(z,c;t,s)\|_1
\le
Ce^{-c_\nu F^2(t-s)}
\bigg[
&\|z(s)\|_{L^2(A_L^{++})}\\
&+(FL)^{-2}\|z(s)\|_2
\bigg]
\|\nabla c(s)\|_2.
\end{aligned}}
\tag{17}
\]

For an unrestricted \(c\in H^1\), the global version is

\[
\boxed{
\|\mathcal V_F(z,c;t,s)\|_1
\le
Ce^{-c_\nu F^2(t-s)}
\|z(s)\|_2\|\nabla c(s)\|_2.
}
\tag{18}
\]

### Proof

The annular heat--Leray multiplier in (15) has an integrable tensor
kernel with

\[
\left\|
\Delta_F e^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}
\right\|_{L^1\to L^1}
\le
CF e^{-c_\nu F^2(t-s)}.
\tag{19}
\]

If the state input has frequency \(K>64F\) and the output lies in
(11), Fourier support forces the coefficient frequency to be
comparable to \(K\).  Annular Bernstein therefore supplies \(K^{-1}\)
on the coefficient:

\[
\|\widetilde\Delta_Kc\|_2
\le
CK^{-1}\|\widetilde\Delta_K\nabla c\|_2.
\tag{20}
\]

The exact support sum, Cauchy--Schwarz over dyadic \(K\), and finite
overlap give

\[
F
\sum_{K>64F}
K^{-1}
\|\Delta_Kz\|_2
\|\widetilde\Delta_K\nabla c\|_2
\le
C\|z\|_2\|\nabla c\|_2.
\tag{21}
\]

This proves (18).  For (17), split the product across \(A_L^+\) and
use the same two off-diagonal Schwartz-kernel estimates as in the
reviewed spatial--frequency lemma:

\[
\|\Delta_Kz\|_{L^2(A_L^+)}
\le
C\left[
\|z\|_{L^2(A_L^{++})}
+(KL)^{-2}\|z\|_2
\right],
\tag{22}
\]

\[
\|\widetilde\Delta_Kc\|_{L^2((A_L^+)^c)}
\le
CK^{-1}(KL)^{-2}\|\nabla c\|_2.
\tag{23}
\]

Since \(K>64F\), the resulting dyadic sums are bounded by the
right-hand side of (17).  Tensor transposition changes neither Fourier
support nor any tensor norm used here.  This proves the lemma.

## 3. The one-return state

Define the annular state obtained after one separated high-to-\(F\)
Oseen interaction:

\[
\boxed{
w_F(t)
:=
\int_0^t
\Delta_F e^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}
\left(
(P_{>64F}r(s))\boxtimes b(s)
\right)\,ds.
}
\tag{24}
\]

The Leray projection makes \(w_F\) solenoidal, and its Fourier support
is contained in (11).

Apply (18) to \(c_{\rm in}\), (17) to every \(c_k\), and integrate in
the source time \(s\).  Equations (5), (9), and (10), together with
the reviewed off-diagonal sum, give a nonnegative function \(G_F\)
such that

\[
\|w_F(t)\|_1
\le
C\int_0^t
e^{-c_\nu F^2(t-s)}G_F(s)\,ds
\tag{25}
\]

and

\[
\boxed{
\begin{aligned}
\int_0^hG_F(s)\,ds
\le C\bigg\{
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
\tag{26}
\]

For clarity, the constant term in (26) is the inner product of the
two reviewed square-function budgets:

\[
\left(
\int_0^h\|r(s)\|_2^2\,ds
\right)^{1/2}
\left(
\int_0^h\|\nabla c_{\rm in}(s)\|_2^2\,ds
\right)^{1/2}
\lesssim
h^{3/2}h^{-3/2}=1.
\tag{27}
\]

The last term in (26) is the same two-moment shell leakage as in the
spatial--frequency theorem; replacing its separation frequency by
\(64F\) changes only a fixed constant.

Fubini's theorem and (25) now expose the exact extra heat clock:

\[
\boxed{
\begin{aligned}
\int_0^h\|w_F(t)\|_1\,dt
&\le
C
\min\{h,F^{-2}\}
\int_0^hG_F(s)\,ds.
\end{aligned}}
\tag{28}
\]

The viscosity dependence is absorbed into \(C_\nu\).

## 4. Final low-pressure observation

Let

\[
\Pi_S:=S_S\mathbb Q\operatorname{div},
\qquad
F\ge16S,
\tag{29}
\]

with the same fixed low-output multiplier as in the terminal-return
theorem.  Define the one-return pressure cost

\[
\boxed{
\mathfrak R^{(1)}_{S,F}(h)
:=
\int_0^h
\left\|
\Pi_S\bigl(w_F(t)\otimes b(t)\bigr)
\right\|_1\,dt.
}
\tag{30}
\]

The tensor orientation in (30) is immaterial for the pressure gradient
when \(w_F\) and \(b\) are solenoidal.

The low-output pressure multiplier has \(L^1\) tensor-kernel norm
\(O(S)\).  Lorentz Hölder and annular Lorentz--Bernstein give

\[
\begin{aligned}
\|\Pi_S(w_F\otimes b)\|_1
&\le
CS\|w_F\|_{L^{3/2,1}}
\|b\|_{L^{3,\infty}}\\
&\le
CMSF\|w_F\|_1.
\end{aligned}
\tag{31}
\]

Combining (26), (28), and (31) proves

\[
\begin{aligned}
\mathfrak R^{(1)}_{S,F}(h)
&\le
C_\nu MSF
\min\{h,F^{-2}\}
\int_0^hG_F(s)\,ds\\
&=
C_\nu M\frac SF
\min\{1,F^2h\}
\int_0^hG_F(s)\,ds,
\end{aligned}
\tag{32}
\]

which is exactly (1).

The estimate contains both clock regimes:

\[
\frac SF\min\{1,F^2h\}
=
\begin{cases}
SFh,&F^2h\le1,\\
S/F,&F^2h\ge1.
\end{cases}
\tag{33}
\]

Thus a subparabolic return has an additional small factor \(F^2h\);
a superparabolic return can use its full heat clock but still retains
the terminal \(S/F\) loss.

## 5. Inverting a fixed one-return floor

Fix \(S>0\), \(M<\infty\), and \(\beta>0\).  Along a selected sequence
\(h\downarrow0\), take \(F(h)\asymp h^{-\beta}\) and assume

\[
\boxed{
\mathfrak R^{(1)}_{S,F(h)}(h)
\ge p_1>0.
}
\tag{34}
\]

This is an additional participation antecedent.  It is not inferred
from the pressure floor for the complete feedback state.

The outer factor in (1) has the exact power

\[
\frac S{F(h)}
\min\{1,F(h)^2h\}
\asymp
h^{\eta_1(\beta)},
\tag{35}
\]

where

\[
\boxed{
\eta_1(\beta)
:=
\beta+(1-2\beta)_+
=
\begin{cases}
1-\beta,&0<\beta\le1/2,\\
\beta,&\beta\ge1/2.
\end{cases}}
\tag{36}
\]

The constant and algebraic-error terms in (1) therefore vanish.
Equations (1) and (34) force

\[
\log\!\bigl(D_b(h)h^3\bigr)
\ge
c h^{-(7/4+\eta_1(\beta))}.
\tag{37}
\]

Since

\[
\gamma_1(\beta)
=\frac74+\eta_1(\beta)
=\frac94+\left|\beta-\frac12\right|,
\tag{38}
\]

equations (2)--(3) follow.  The parabolic return
\(\beta=1/2\) is the least expensive one, and even it forces

\[
\boxed{
D_b(h)
\ge
h^{-3}\exp(c h^{-9/4}).
}
\tag{39}
\]

## 6. Physical scaling and exact surviving boundary

On one physical trajectory at zoom \(\sigma_h\), absolute continuity
of dissipation gives

\[
\sigma_hD_b(h)\longrightarrow0.
\tag{40}
\]

Under the one-return floor (34), equations (2) and (40) require

\[
\boxed{
\sigma_h
=
o\!\left[
h^3
\exp\!\left(
-c h^{-\gamma_1(\beta)}
\right)
\right].
}
\tag{41}
\]

This remains a necessary cost, not a contradiction.  The reviewed
amplified-ancestry scalar history can accelerate its zoom beyond any
one prescribed stretched coordinate.

The theorem closes only the following returned-low child:

> A pressure-bearing state tail can evade spatial--frequency
> amplification by making one separated high-to-annular Oseen return
> immediately before the final low-pressure observation.

It cannot.  A surviving returned-low itinerary must instead use at
least one additional state interaction after the separated return, or
descend through a sequence of comparable bands so that no single final
return is separated by the factor used in (12).  At the stage of this
theorem, summing those multistage descents, proving non-reuse on the
physical trajectory, and forcing the participation floor (34) remained
open.

The later reviewed corridor and
[last-separated-return renewal](adjoint-pressure-last-return-renewal.md)
theorems now sum every post-return path below a parabolic ceiling and
replace the participation antecedent by an exact trichotomy.  The live
branches are the no-chargeable-feedback-return block and
superparabolic LP--Dyson capture; the \(9/4\) cost remains a necessary
same-trajectory expense rather than a contradiction.

No regularity theorem, breakdown theorem, coefficient construction,
Oseen singularity, Navier--Stokes singularity, or Clay alternative
A--D follows.

## Reproduce

```bash
make adjoint-pressure-one-return
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_one_return -v
make check
```
