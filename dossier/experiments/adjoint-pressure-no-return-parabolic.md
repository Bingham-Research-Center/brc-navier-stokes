# No-chargeable-return pressure cannot stay below a parabolic ceiling

- **Experiment:** EXP-ADJOINT-PRESSURE-NO-RETURN-PARABOLIC-001
- **Route:** ROUTE-R3B
- **Status:** independently reviewed valid in the stated smooth-layer
  conditional scope
- **Review:** [accepted with no fatal flaw after two precision
  additions](../review-response-adjoint-pressure-no-return-parabolic-2026-07-24.md)
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** independently reviewed
  [first-feedback theorem](adjoint-pressure-second-interaction.md),
  [full-corridor theorem](adjoint-pressure-corridor-sum.md),
  [smooth-layer identification theorem](adjoint-pressure-corridor-identification.md),
  and [last-return renewal theorem](adjoint-pressure-last-return-renewal.md)

The last-return renewal theorem leaves an exact complementary pressure
block

\[
r_{\rm no}
:=
(I-\mathsf A_b)^{-1}g,
\qquad
g:=T_bq.
\tag{1}
\]

It contains every feedback Dyson word with no chargeable separated
return after the first feedback source \(g\).  This note proves that
this block cannot carry a fixed pressure floor while all of its
LP--Dyson outputs stay below a parabolic frequency ceiling.

The decisive input is the reviewed direct-response gain

\[
\|q(t)\|_{L^{3/2,1}}\le C_qt^{3/4}.
\tag{2}
\]

After resolving \(g\) into its output bands, the band \(F\) interaction
has the normalised heat form

\[
\|g_F(t)\|_1
\le
\frac{C_gM}{c_0\nu F}
\int_0^t
\lambda_F e^{-\lambda_F(t-s)}s^{3/4}\,ds,
\qquad
\lambda_F:=c_0\nu F^2.
\tag{3}
\]

The \(F^{-1}\) in (3), every later cross-band ratio, and the final
pressure frequency telescope exactly to the fixed detector frequency
\(S\).  The starting band supplies one heat clock, so it must be
summed together with all later output bands.  With

\[
H_U:=h\sum_{Q\le U}\lambda_Q
\le\frac43c_0\nu hU^2,
\tag{4}
\]

the complete filtered path sum obeys

\[
\boxed{
\|\mathscr P_{S,b}r_{{\rm no},U}\|_{L^1_{t,x}}
\le
C_gS h^{7/4}
\left(e^{A_{\rm no}H_U}-1\right).
}
\tag{5}
\]

Here \(r_{{\rm no},U}\) retains every starting band and every later
complementary output band at most \(U\).  Consequently,

\[
\boxed{
U\le\kappa h^{-1/2}
\quad\Longrightarrow\quad
\|\mathscr P_{S,b}r_{{\rm no},U}\|_{L^1_{t,x}}
\le C_\kappa S h^{7/4}\longrightarrow0.
}
\tag{6}
\]

Every fixed smooth layer still has a finite capture ceiling.  Hence, if
\(r_{\rm no}\) carries a fixed pressure floor along a collapsing
sequence, its minimum capture ceiling satisfies

\[
\boxed{
U_{\rm no}(h)\sqrt h\longrightarrow\infty.
}
\tag{7}
\]

Combining (7) with the last-return theorem sharpens the complete
feedback alternative.  After subsequence extraction, either

1. a pressure-bearing renewal block has superparabolic LP--Dyson
   capture escape; or
2. for all sufficiently small selected \(h\),
   \[
   \boxed{
   D_b(h)\ge h^{-3}\exp\!\left(ch^{-9/4}\right).
   }
   \tag{8}
   \]

Thus the exact no-chargeable-return branch is no longer a separate
unanalysed possibility: below every parabolic ceiling it vanishes.
The remaining frequency obstruction is one common superparabolic
capture escape, not yet an instantaneous Fourier-energy or physical
dissipation statement.

## 1. Reviewed smooth-layer data

Fix \(0<h\le1\), \(\nu,S>0\), and a dyadic \(F_*\ge16S\).  On one fixed smooth
finite-energy genealogy layer, retain

\[
b\in L^\infty(0,h;L^\infty\cap L^2),
\qquad
\nabla\cdot b=0,
\qquad
\sup_{0<t<h}\|b(t)\|_{L^{3,\infty}}\le M.
\tag{9}
\]

The weak-\(L^3\) constant \(M\) is uniform along the selected
genealogy.  Smooth norms may depend on this one layer.  The reviewed
direct response \(q\) satisfies (2), and

\[
(T_bz)(t)
:=
\int_0^t
e^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}
\bigl(z(s)\boxtimes b(s)\bigr)\,ds,
\qquad
(z\boxtimes b)_{ik}:=z_ib_k.
\tag{10}
\]

Put

\[
X_h:=C([0,h];L^2_\sigma(\mathbb R^3)),
\qquad
Y_h:=L^1((0,h)\times\mathbb R^3).
\tag{11}
\]

The last-return theorem defines the complementary output filters

\[
\mathsf J_Q
:=
\begin{cases}
I,&Q<F_*,\\
I-P_{>64Q},&Q\ge F_*,
\end{cases}
\tag{12}
\]

\[
(\mathsf A_{b,Q}z)(t)
:=
\int_0^t
\Delta_Qe^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}
\bigl((\mathsf J_Qz(s))\boxtimes b(s)\bigr)\,ds,
\tag{13}
\]

and

\[
\mathsf A_b:=\sum_Q\mathsf A_{b,Q},
\qquad
\mathsf A_{b,U}:=\sum_{Q\le U}\mathsf A_{b,Q}.
\tag{14}
\]

Their fractional Volterra series converge in \(X_h\), and

\[
\|\mathsf A_b-\mathsf A_{b,U}\|_{X_h\to X_h}
\le\frac{CB_\infty}{\nu U},
\qquad
B_\infty:=\|b\|_{L^\infty_{t,x}}.
\tag{15}
\]

For the fixed low-output pressure observation, put

\[
\Pi_S:=S_S\mathbb Q\operatorname{div},
\qquad
(\mathscr P_{S,b}z)(t)
:=
\Pi_S\bigl(z(t)\boxtimes b(t)\bigr).
\tag{16}
\]

The reviewed fixed-band kernel gives the continuous map
\(\mathscr P_{S,b}:X_h\to Y_h\).
Because \(b,q\), and every heat--Leray projected path state are
solenoidal, transposing \(z\boxtimes b\) gives the same scalar pressure
source after the two divergences.  Thus (16) has the reviewed physical
pressure orientation.

## 2. The first feedback source has a normalised starting clock

For every dyadic \(F\), define

\[
\boxed{
g_F(t)
:=
\int_0^t
\Delta_Fe^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}
\bigl(q(s)\boxtimes b(s)\bigr)\,ds.
}
\tag{17}
\]

The annular heat--Leray kernel satisfies

\[
\left\|
\Delta_Fe^{\nu\tau\Delta}
\mathbb P\operatorname{div}
\right\|_{L^1\to L^1}
\le
C_\nu Fe^{-c_0\nu F^2\tau}.
\tag{18}
\]

Lorentz Hölder and (2), (9) give

\[
\|q(s)\boxtimes b(s)\|_1
\le
C\|q(s)\|_{L^{3/2,1}}\|b(s)\|_{L^{3,\infty}}
\le C_qMs^{3/4}.
\tag{19}
\]

Equations (17)--(19) prove

\[
\|g_F(t)\|_1
\le
C_gMF
\int_0^t
e^{-\lambda_F(t-s)}s^{3/4}\,ds.
\tag{20}
\]

Since \(F=\lambda_F/(c_0\nu F)\), this is exactly (3).  Define

\[
I_q(h)
:=
\int_0^h s^{3/4}\,ds
=\frac47h^{7/4}.
\tag{21}
\]

The power \(7/4\) is source-time regularity, not the earlier
coefficient-dissipation logarithm.

## 3. Filtered paths and exact frequency telescope

For a finite path

\[
\boldsymbol R=(R_0,\ldots,R_m),
\qquad
R_0:=F,
\tag{22}
\]

define

\[
g_{\boldsymbol R}
:=
\begin{cases}
g_F,&m=0,\\
\mathsf A_{b,R_m}
g_{(R_0,\ldots,R_{m-1})},&m\ge1.
\end{cases}
\tag{23}
\]

Every state in (23) is annular at its last listed frequency.  Put

\[
C_{\rm LP}:=\sup_Q\|\mathsf J_Q\|_{L^1\to L^1}<\infty.
\tag{24}
\]

The reviewed cross-band estimate therefore gives, for annular \(z_R\),

\[
\|\mathsf A_{b,Q}z_R(t)\|_1
\le
C_xMC_{\rm LP}RQ
\int_0^t
e^{-\lambda_Q(t-s)}
\|z_R(s)\|_1\,ds.
\tag{25}
\]

After normalising the heat kernel, one continuation contributes the
frequency ratio

\[
\frac{C_xMC_{\rm LP}}{c_0\nu}\frac RQ.
\tag{26}
\]

The final fixed pressure observation obeys

\[
\|\Pi_S(z_R\boxtimes b)\|_1
\le C_pMSR\|z_R\|_1.
\tag{27}
\]

Thus all frequency factors along (22) telescope:

\[
\boxed{
\frac1F
\left(
\frac{R_0}{R_1}\cdots
\frac{R_{m-1}}{R_m}
\right)
SR_m
=S.
}
\tag{28}
\]

For \(m=0\), the empty product in (28) is one and the same identity is
\(F^{-1}SF=S\).

Let

\[
X_j\sim{\rm Exp}(\lambda_{R_j}),
\qquad
0\le j\le m,
\tag{29}
\]

be independent, and put

\[
\Theta_{\boldsymbol R}(h)
:=
\mathbb P(X_0+\cdots+X_m\le h).
\tag{30}
\]

Writing
\(k_R(\tau):=\lambda_R e^{-\lambda_R\tau}\mathbf1_{\{\tau>0\}}\),
the time-ordered integral is exactly

\[
\int_0^h
\bigl(k_{R_m}*\cdots*k_{R_0}*s_+^{3/4}\bigr)(t)\,dt
=
\int_0^h
s^{3/4}
\mathbb P(X_0+\cdots+X_m\le h-s)\,ds.
\tag{30a}
\]

Integrating the time-ordered convolution and using (21), (28) gives
one fixed \(A_{\rm no}\ge1\), depending only on the reviewed uniform
constants, such that

\[
\boxed{
\int_0^h
\left\|
\Pi_S(g_{\boldsymbol R}(t)\boxtimes b(t))
\right\|_1\,dt
\le
C_gS A_{\rm no}^{m+1}
\Theta_{\boldsymbol R}(h)I_q(h).
}
\tag{31}
\]

The probability in (30a) is at most
\(\Theta_{\boldsymbol R}(h)\); this proves (31).

## 4. Every starting band and every continuation path is summable

For dyadic \(U\ge F_*\), let

\[
\mathscr N_m(U)
:=
\left\{
(F,R_1,\ldots,R_m):
F,R_j\in2^{\mathbb Z},\
F\le U,\
R_j\le U
\right\}.
\tag{32}
\]

There is no lower-frequency cutoff.  With
\(\lambda(Q)=c_0\nu Q^2\),

\[
\sum_{Q\le U}\lambda(Q)
\le\frac43c_0\nu U^2.
\tag{33}
\]

The ordered-simplex estimate gives

\[
\Theta_{\boldsymbol R}(h)
\le
\frac{h^{m+1}}{(m+1)!}
\prod_{j=0}^m\lambda_{R_j}.
\tag{34}
\]

Tonelli and the product structure now sum the starting band and every
later output band at once:

\[
\boxed{
\sum_{\boldsymbol R\in\mathscr N_m(U)}
\Theta_{\boldsymbol R}(h)
\le
\frac{H_U^{m+1}}{(m+1)!}.
}
\tag{35}
\]

Combining (31), (35), and then summing over \(m\ge0\) gives the
absolutely convergent pressure series

\[
\begin{aligned}
&\sum_{m=0}^\infty
\sum_{\boldsymbol R\in\mathscr N_m(U)}
\int_0^h
\left\|
\Pi_S(g_{\boldsymbol R}(t)\boxtimes b(t))
\right\|_1\,dt\\
&\qquad\le
C_gSI_q(h)
\sum_{m=0}^\infty
\frac{(A_{\rm no}H_U)^{m+1}}{(m+1)!}\\
&\qquad=
C_gSI_q(h)
\left(e^{A_{\rm no}H_U}-1\right).
\end{aligned}
\tag{36}
\]

This proves the path-sum bound in (5).  In contrast with a termwise
mass bound, the starting-frequency entropy is finite because every
starting band carries its own heat rate \(\lambda_F\).

## 5. Identification with the truncated no-return mild solution

For \(K\ge1\), put

\[
\mathcal D_K(U)
:=
\left\{
Q\in2^{\mathbb Z}:2^{-K}U\le Q\le U
\right\},
\tag{36a}
\]

\[
g_{U,K}:=\sum_{F\in\mathcal D_K(U)}g_F,
\qquad
\mathsf A_{b,U,K}
:=
\sum_{Q\in\mathcal D_K(U)}\mathsf A_{b,Q},
\tag{36b}
\]

and

\[
r_{{\rm no},U,K}
:=
\sum_{m=0}^\infty
\mathsf A_{b,U,K}^mg_{U,K}.
\tag{36c}
\]

The band sets in (36a) are finite, so the pressure of (36c) expands
algebraically into exactly the corresponding paths (23), with no
homogeneous-limit issue.

Put

\[
g_U:=\sum_{\substack{F\in2^{\mathbb Z}\\F\le U}}g_F,
\qquad
r_{{\rm no},U}
:=
\sum_{m=0}^\infty
\mathsf A_{b,U}^mg_U.
\tag{37}
\]

As \(K\to\infty\), strong homogeneous LP convergence and the uniform
Gamma majorant give

\[
g_{U,K}\longrightarrow g_U,
\qquad
\mathsf A_{b,U,K}^mz\longrightarrow\mathsf A_{b,U}^mz,
\qquad
r_{{\rm no},U,K}\longrightarrow r_{{\rm no},U}
\quad\hbox{in }X_h.
\tag{37a}
\]

The first sum in (37) is the strong homogeneous LP output truncation
of \(g=T_bq\).  Since \(g\in X_h\),

\[
g_U\longrightarrow g
\quad\hbox{in }X_h.
\tag{38}
\]

For each fixed \(m\),

\[
\begin{aligned}
\mathsf A_{b,U}^mg_U-\mathsf A_b^mg
={}&
\mathsf A_{b,U}^m(g_U-g)\\
&+
\left(\mathsf A_{b,U}^m-\mathsf A_b^m\right)g
\longrightarrow0
\quad\hbox{in }X_h
\end{aligned}
\tag{39}
\]

by (15) and the fixed-depth Volterra bounds.  The Gamma majorant is
uniform in \(U\), so

\[
\boxed{
r_{{\rm no},U}\longrightarrow r_{\rm no}
\quad\hbox{in }X_h,
\qquad
\mathscr P_{S,b}r_{{\rm no},U}
\longrightarrow
\mathscr P_{S,b}r_{\rm no}
\quad\hbox{in }Y_h.
}
\tag{40}
\]

At the finite lower cutoff, linearity expands the pressure of (36c)
into the paths (23).  Strong \(X_h\) convergence in (37a), pressure
continuity, and absolute \(Y_h\)-summability in (36) let
\(K\to\infty\), and then (38)--(40) let \(U\to\infty\).
Thus (36) is the pressure bound for the actual truncated mild solution,
not merely a formal path majorant.  Equations (4), (21), and (36)
prove (5)--(6).

## 6. No-return pressure forces superparabolic capture

Assume along a selected sequence \(h_j\downarrow0\) that

\[
\|\mathscr P_{S,b}r_{\rm no}\|_{Y_h}
\ge\frac{p_0}{2}.
\tag{41}
\]

Define

\[
\boxed{
U_{\rm no}(h)
:=
\min\left\{
U\in2^{\mathbb Z}:U\ge F_*,\
\|\mathscr P_{S,b}
(r_{\rm no}-r_{{\rm no},U})\|_{Y_h}
\le\frac{p_0}{4}
\right\}.
}
\tag{42}
\]

It is finite by (40), and

\[
\|\mathscr P_{S,b}r_{{\rm no},U_{\rm no}(h)}\|_{Y_h}
\ge\frac{p_0}{4}.
\tag{43}
\]

If \(U_{\rm no}(h_j)\sqrt{h_j}\) failed to tend to infinity, there
would be a finite \(\kappa\) and a subsequence on which

\[
U_{\rm no}(h_j)\le\kappa h_j^{-1/2}.
\tag{44}
\]

Equations (6), (43) would then give

\[
\frac{p_0}{4}
\le C_\kappa S h_j^{7/4}\longrightarrow0,
\tag{45}
\]

a contradiction.  This proves (7).

## 7. Combined feedback dichotomy

Retain the complete selected feedback pressure floor

\[
\|\mathscr P_{S,b}r\|_{Y_h}\ge p_0.
\tag{46}
\]

The reviewed exact renewal split gives

\[
r=r_{\rm no}+r_{\rm last}.
\tag{47}
\]

After passing to a subsequence, either (41) holds throughout or

\[
\|\mathscr P_{S,b}r_{\rm last}\|_{Y_h}
\ge\frac{p_0}{2}
\tag{48}
\]

holds throughout.  In the first branch, (7) forces superparabolic
capture.  In the second, the last-return theorem gives either
superparabolic capture or the \(9/4\) cost (8).  The two alternatives
stated after (7) are therefore exhaustive.

Superparabolic capture means failure of every uniform
\(U\lesssim h^{-1/2}\) LP--Dyson approximation.  It does not yet imply
an instantaneous state-frequency tail, a lower bound for physical
high-frequency dissipation, spatial escape, or a theorem on the rough
limiting hull.  Equation (8) is a necessary coefficient cost; the
physical zoom may still outrun it.  No singular solution, regularity
theorem, breakdown theorem, or Clay alternative A--D is proved.

The subsequent independently reviewed
[parabolic coefficient-tail theorem](adjoint-pressure-parabolic-coefficient-tail.md)
now removes the first two qualifications for every selected complete
feedback packet: it forces an actual same-layer coefficient-dissipation
tail above \(h^{-1/2}\sqrt{\log(1/h)}\), with size at least
\(h^{-3+\varepsilon}\).  It still does not make different event-index
payments additive or prevent the physical zoom from outrunning their
weights.

## 8. Executable ledger

The direct-source time power, infinite lower-band heat entropy,
frequency telescope, factorial depth sum, and parabolic \(7/4\) power
are checked by

```bash
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_no_return -v
PYTHONPATH=lab python -m \
  navier_lab.adjoint_pressure_no_return
```
