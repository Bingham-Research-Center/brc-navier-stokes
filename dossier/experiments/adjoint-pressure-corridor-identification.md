# Smooth-layer LP--Dyson identification leaves only superparabolic capture

- **Experiment:** EXP-ADJOINT-PRESSURE-CORRIDOR-IDENTIFICATION-001
- **Route:** ROUTE-R3B
- **Status:** adversarially recomputed conditional analytic reduction
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** adversarially recomputed
  [one-return theorem](adjoint-pressure-one-return.md),
  [multistage-path theorem](adjoint-pressure-multistage-path.md), and
  [full-corridor theorem](adjoint-pressure-corridor-sum.md)
- **Review:** [valid after one smooth-layer source repair](../review-ledger.md)

The full-corridor theorem deliberately withheld the infinite
Littlewood--Paley identity.  The weak-\(L^3\) ceiling does not by itself
make multiplication by the drift continuous on a rough endpoint
space.  The physical argument, however, is evaluated first on each
member of the smooth finite-energy genealogy.  On one such fixed
layer there is a stronger topology available:

\[
X_h:=C([0,h];L^2_\sigma(\mathbb R^3)).
\tag{1}
\]

In this topology Volterra time ordering makes the complete Dyson series
convergent.  The convergence constants may depend on the smooth
layer's \(L^\infty_x\) norm and are not uniform along the genealogy.
That distinction is decisive.

The result below proves three things.

1. On every fixed smooth layer, the reviewed corridor pressure series
   is exactly the low-pressure observation of a spectrally truncated
   Oseen mild solution.
2. The complete smooth-layer continuation splits exactly into that
   corridor solution and a first-high-insertion remainder.
3. Every fixed layer has a finite frequency ceiling which captures any
   prescribed fraction of its nonzero continuation pressure.  Along a
   collapsing sequence, either such ceilings remain parabolic and the
   reviewed \(9/4\) cost applies, or the required ceilings escape
   superparabolically.

Within the separated-return branch under the participation antecedent
(42), the missing issue is no longer qualitative LP--Dyson
identification.  It is a **uniform spectral-tightness theorem** at the
parabolic frequency.  Globally, participation and histories with no
separated return remain open.  This note proves none of those missing
statements.

## 1. Smooth-layer operators

Fix \(h,\nu,S>0\).  Let \(b\) be one smooth divergence-free,
finite-energy genealogy member on \([0,h]\).  In particular \(b\) is
strongly measurable.  Retain the reviewed, genealogy-uniform endpoint
ceiling

\[
\sup_{0<t<h}\|b(t)\|_{L^{3,\infty}}\le M.
\tag{2a}
\]

The new smooth-layer norms are

\[
B_\infty
:=
\|b\|_{L^\infty((0,h)\times\mathbb R^3)}
<\infty,
\qquad
B_2
:=
\|b\|_{L^\infty(0,h;L^2)}
<\infty.
\tag{2}
\]

No uniform bound for \(B_\infty\) or \(B_2\) along the genealogy is
asserted.  The corridor estimate uses the uniform constant \(M\);
the topology argument uses only the finite layerwise constants in
(2).
Define

\[
(T_bz)(t)
:=
\int_0^t
e^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}
\bigl(z(s)\boxtimes b(s)\bigr)\,ds,
\tag{3}
\]

where \((z\boxtimes b)_{ik}=z_i b_k\).  Let
\(\{\Delta_R\}_{R\in2^{\mathbb Z}}\) be the fixed homogeneous
Littlewood--Paley resolution used in the corridor theorem.  For dyadic
\(U\), define the strong \(L^2\) multipliers

\[
\mathsf L_U
:=
\sum_{\substack{R\in2^{\mathbb Z}\\R\le U}}\Delta_R,
\qquad
\mathsf H_U:=I-\mathsf L_U.
\tag{4}
\]

The symbols overlap, so \(\mathsf L_U\) need not be an orthogonal
projection.  Only

\[
\mathsf L_U+\mathsf H_U=I,
\qquad
\sup_U
\bigl(
\|\mathsf L_U\|_{2\to2}
+\|\mathsf H_U\|_{2\to2}
\bigr)
\le C_{\rm LP}
\tag{5}
\]

is used.

For the fixed low-output pressure observation put

\[
(\mathscr P_{S,b}z)(t)
:=
\Pi_S\bigl(z(t)\boxtimes b(t)\bigr),
\qquad
Y_h:=L^1((0,h)\times\mathbb R^3).
\tag{6}
\]

The fixed-band pressure kernel and Cauchy--Schwarz give

\[
\boxed{
\|\mathscr P_{S,b}z\|_{Y_h}
\le
C_PS hB_2\|z\|_{X_h}.
}
\tag{7}
\]

This is a layerwise continuity statement.  It neither constructs an
adjoint on the rough limiting hull nor uses convergence of the
genealogy pressures.

Let \(w_F\) be the reviewed one-return state at a dyadic
\(F\le U\).  Smoothness of the selected layer gives

\[
w_F\in X_h,
\qquad
\operatorname{supp}\widehat w_F
\subset\{F/2\le|\xi|\le2F\}.
\tag{8}
\]

The signs below use the plus-sign mild convention inherited from the
reviewed feedback equation.  With the opposite PDE convention, replace
every \(T_b\) by \(\sigma T_b\), \(\sigma\in\{-1,1\}\), including in
the path components.  All norm estimates and conclusions are
unchanged.

## 2. Fractional Volterra convergence

The \(L^2\) heat--Leray estimate is

\[
\left\|
e^{\nu\tau\Delta}
\mathbb P\operatorname{div}G
\right\|_2
\le
C_H(\nu\tau)^{-1/2}\|G\|_2.
\tag{9}
\]

Consequently, with

\[
a:=\frac{C_HB_\infty}{\sqrt\nu},
\tag{10}
\]

one has

\[
\|T_bz(t)\|_2
\le
a\int_0^t
(t-s)^{-1/2}\|z(s)\|_2\,ds.
\tag{11}
\]

The \(m\)-fold convolution of \(t^{-1/2}\mathbf1_{t>0}\), followed by
one integration against the constant function, gives

\[
\boxed{
\|T_b^mw_F\|_{X_h}
\le
\|w_F\|_{X_h}
\frac{
\bigl(a\Gamma(1/2)\sqrt h\bigr)^m
}{
\Gamma(m/2+1)
}.
}
\tag{12}
\]

The same calculation with \(\mathsf L_UT_b\) gives

\[
\boxed{
\|(\mathsf L_UT_b)^mw_F\|_{X_h}
\le
\|w_F\|_{X_h}
\frac{
\bigl(C_{\rm LP}a\Gamma(1/2)\sqrt h\bigr)^m
}{
\Gamma(m/2+1)
}.
}
\tag{13}
\]

Both majorant series converge for every finite argument.  Hence

\[
v_F
:=
\sum_{m=0}^\infty T_b^mw_F,
\qquad
v_{F,U}
:=
\sum_{m=0}^\infty(\mathsf L_UT_b)^mw_F
\tag{14}
\]

converge absolutely in \(X_h\).  They are the unique mild solutions in
\(X_h\) of

\[
v_F=w_F+T_bv_F,
\qquad
v_{F,U}=w_F+\mathsf L_UT_bv_{F,U}.
\tag{15}
\]

This is qualitative layerwise convergence.  Since \(B_\infty\) can
grow without control along the genealogy, (12)--(13) do not supply the
uniform parabolic-frequency estimate sought in ROUTE-R3B.

The \(m=0\) term in (14) is \(w_F\) itself.  Thus \(v_F\) is the full
Dyson continuation of this one specified oriented Oseen block,
including its one-return source; that source must not be added again.
If the physical operator contains an additional tensor orientation or
stretching block, it requires its own path labels and estimates and is
not silently included here.

## 3. Identification with every corridor path

For an integer \(K\) large enough that \(2^{-K}F\le U\), put

\[
\mathsf L_{U,K}
:=
\sum_{\substack{R\in2^{\mathbb Z}\\
                  2^{-K}F\le R\le U}}
\Delta_R.
\tag{16}
\]

This is a finite sum.  Repeated linearity gives, for every fixed depth
\(m\),

\[
\boxed{
(\mathsf L_{U,K}T_b)^mw_F
=
\sum_{\substack{R_1,\ldots,R_m\in2^{\mathbb Z}\\
                  2^{-K}F\le R_j\le U}}
w_{(F,R_1,\ldots,R_m)}.
}
\tag{17}
\]

The multipliers \(\mathsf L_{U,K}\) converge strongly on \(L^2\) to
\(\mathsf L_U\).  If \(z\in X_h\), then \(z([0,h])\) is a compact
subset of \(L^2\).  Uniform boundedness of the multipliers upgrades
strong convergence to

\[
\sup_{0\le t\le h}
\|(\mathsf L_{U,K}-\mathsf L_U)z(t)\|_2
\longrightarrow0.
\tag{18}
\]

Since \(T_b:X_h\to X_h\) is continuous, induction in \(m\) gives

\[
(\mathsf L_{U,K}T_b)^mw_F
\longrightarrow
(\mathsf L_UT_b)^mw_F
\quad\hbox{in }X_h.
\tag{19}
\]

Apply the continuous map (7).  The full-corridor theorem independently
proves absolute \(Y_h\)-summability of the path pressures.  Therefore
the limit of the finite sums in (17) is their unconditional sum, and

\[
\boxed{
\mathscr P_{S,b}
\bigl((\mathsf L_UT_b)^mw_F\bigr)
=
\sum_{\boldsymbol R\in\mathscr C_m(F;U)}
\Pi_S\bigl(w_{\boldsymbol R}\boxtimes b\bigr)
\quad\hbox{in }Y_h.
}
\tag{20}
\]

Summing in \(m\), using (13), (7), and the already reviewed absolute
path estimate, yields the exact identification

\[
\boxed{
\mathscr P_{S,b}v_{F,U}
=
\mathcal P^{\rm corr}_{S,F;U}
\quad\hbox{in }Y_h.
}
\tag{21}
\]

Here the final index records the ceiling \(U\); this is the same
corridor series denoted by \(\mathcal P^{\rm corr}_{S,F}\) when the
ceiling was fixed in the preceding theorem.

Thus equation (31) of the corridor theorem is not merely a formally
defined pressure series on a smooth layer: it is the pressure of the
unique spectrally truncated mild continuation (15).

## 4. Exact first-high-insertion remainder

Put

\[
d_{F,U}:=v_F-v_{F,U}.
\tag{22}
\]

Subtracting the two equations in (15), and using
\(\mathsf H_U=I-\mathsf L_U\), gives

\[
\boxed{
d_{F,U}
=
T_bd_{F,U}
+\mathsf H_UT_bv_{F,U}.
}
\tag{23}
\]

Equivalently,

\[
d_{F,U}
=
\sum_{\ell=0}^\infty
T_b^\ell
\mathsf H_UT_bv_{F,U}
\quad\hbox{in }X_h.
\tag{24}
\]

This groups every binary LP word by its first
\(\mathsf H_U\)-insertion: before that insertion every interaction uses
\(\mathsf L_U\), and afterwards the full Oseen continuation is
retained.  The grouping is legitimate because (12)--(13), with the
factor \(2^m\) for all binary words at depth \(m\), still gives a
convergent fractional Volterra majorant.

The pressure decomposition is exact:

\[
\boxed{
\mathscr P_{S,b}v_F
=
\mathcal P^{\rm corr}_{S,F;U}
+\mathscr P_{S,b}d_{F,U}
\quad\hbox{in }Y_h.
}
\tag{25}
\]

No positivity or absence of cancellation is asserted.

## 5. The participation ceiling is finite on every smooth layer

As \(U\to\infty\) dyadically,
\(\mathsf L_U\to I\) strongly on \(L^2\).  At each fixed \(m\),

\[
(\mathsf L_UT_b)^mw_F
\longrightarrow
T_b^mw_F
\quad\hbox{in }X_h.
\tag{26}
\]

The majorant (13) is independent of \(U\), so dominated summation gives

\[
\boxed{
v_{F,U}\longrightarrow v_F
\quad\hbox{in }X_h,
\qquad
\mathscr P_{S,b}d_{F,U}\longrightarrow0
\quad\hbox{in }Y_h.
}
\tag{27}
\]

Suppose

\[
\|\mathscr P_{S,b}v_F\|_{Y_h}\ge p_0>0.
\tag{28}
\]

Define the half-participation ceiling

\[
\boxed{
U_{1/2}(h;b,w_F)
:=
\min\left\{
2^kF:k\ge0,\
\|\mathscr P_{S,b}d_{F,2^kF}\|_{Y_h}
\le\frac{p_0}{2}
\right\}.
}
\tag{29}
\]

Equation (27) proves that this dyadic minimum is finite.  The reverse
triangle inequality and (25) give

\[
\boxed{
\|\mathcal P^{\rm corr}_{S,F;U}\|_{Y_h}
\ge\frac{p_0}{2}
\quad\hbox{at }U=U_{1/2}(h;b,w_F).
}
\tag{30}
\]

This is a genuine participation statement, but only at a
layer-dependent finite ceiling.  Nothing above bounds that ceiling by
\(Ch^{-1/2}\).

## 6. Summing every separated return band

The starting-band entropy can also be removed.  Fix a dyadic
\(F_*\ge16S\) and, for \(F_*\le F\le U\), retain every reviewed
one-return source \(w_F\).  Define

\[
W_U:=\sum_{\substack{F\in2^{\mathbb Z}\\F_*\le F\le U}}w_F,
\qquad
V_U:=\sum_{m=0}^\infty(\mathsf L_UT_b)^mW_U.
\tag{31}
\]

The sum defining \(W_U\) is finite.  Linearity and (21) give

\[
\mathscr P_{S,b}V_U
=
\sum_{\substack{F\in2^{\mathbb Z}\\F_*\le F\le U}}
\mathcal P^{\rm corr}_{S,F;U}.
\tag{32}
\]

Write

\[
\begin{aligned}
\mathcal B_0(h)
:=
1
&+h^{7/4}
\left[
1+\log_+\!\bigl(D_b(h)h^3\bigr)
\right]\\
&+h^{21/4}+h^{89/4}+h^{103/4},
\end{aligned}
\tag{33}
\]

so the reviewed source ledger is
\(\mathcal B(h,F)=\mathcal B_0(h)+h^6F^{-2}\).
Put

\[
H_U
:=
h\sum_{Q\le U}c_0\nu Q^2,
\qquad
\Phi_A(H)
:=
\frac{e^{AH}-1}{H}.
\tag{34}
\]

Summing the reviewed corridor estimate over the finite starting-band
set gives

\[
\boxed{
\begin{aligned}
\|\mathscr P_{S,b}V_U\|_{Y_h}
\le{}&
C_{\rm src}c_0\nu Sh\Phi_A(H_U)\\
&{}\times
\left[
\mathcal B_0(h)
\sum_{F_*\le F\le U}F
+h^6
\sum_{F_*\le F\le U}F^{-1}
\right].
\end{aligned}
}
\tag{35}
\]

The dyadic sums obey

\[
\sum_{F_*\le F\le U}F<2U,
\qquad
\sum_{F_*\le F\le U}F^{-1}<\frac2{F_*}.
\tag{36}
\]

Hence, whenever \(U\le\kappa h^{-1/2}\),

\[
\boxed{
\|\mathscr P_{S,b}V_U\|_{Y_h}
\le
C_{\kappa}S h^{1/2}\mathcal B_0(h)
+C_{\kappa}\frac S{F_*}h^7.
}
\tag{37}
\]

A fixed positive floor for this complete multi-start aggregate therefore
forces

\[
\boxed{
D_b(h)
\ge
h^{-3}\exp\!\left(c h^{-9/4}\right).
}
\tag{38}
\]

Thus spreading pressure over all separated return bands below the
parabolic ceiling does not evade the \(9/4\) cost.

To pass from finite starting-band sums to the infinite source, add the
explicit layerwise hypothesis

\[
r\in L^\infty(0,h;H^s(\mathbb R^3))
\quad\hbox{for some }s>0.
\tag{38a}
\]

This holds on each fixed preterminal smooth genealogy layer, but its
norm is not asserted to be uniform along the genealogy.  Under (38a),
the infinite separated-return source

\[
W_\infty:=\sum_{F\ge F_*}w_F
\tag{39}
\]

converges in \(X_h\).  One direct verification is to use any finite
smooth-layer Sobolev ceiling
\(\sup_t\|r(t)\|_{H^s}<\infty\): the high-input tail contributes
\(F^{-s}\), while the band-\(F\) heat--divergence kernel has time mass
\(O(F^{-1})\).  Thus \(\|w_F\|_{X_h}\lesssim F^{-s-1}\), with a
layer-dependent constant, and the dyadic sum converges.  Define

\[
V_\infty:=\sum_{m=0}^\infty T_b^mW_\infty.
\tag{40}
\]

For each fixed \(m\), use the exact decomposition

\[
\begin{aligned}
(\mathsf L_UT_b)^mW_U-T_b^mW_\infty
={}&
(\mathsf L_UT_b)^m(W_U-W_\infty)\\
&+
\left[
(\mathsf L_UT_b)^m-T_b^m
\right]W_\infty.
\end{aligned}
\tag{40a}
\]

The first term tends to zero by \(W_U\to W_\infty\) and the uniform
fixed-depth operator bound.  The second tends to zero by the strong
LP argument in (26).  Finally, the Gamma majorant (13), together with
\(\sup_U\|W_U\|_{X_h}<\infty\), gives a summable tail uniform in \(U\).
Therefore

\[
V_U\longrightarrow V_\infty
\quad\hbox{in }X_h
\qquad(U\to\infty).
\tag{41}
\]

Therefore, if

\[
\|\mathscr P_{S,b}V_\infty\|_{Y_h}\ge p_0,
\tag{42}
\]

define the finite dyadic multi-start capture ceiling

\[
\boxed{
\mathcal U_{1/2}(h)
:=
\min\left\{
U\in2^{\mathbb Z}:U\ge F_*,\
\|\mathscr P_{S,b}(V_\infty-V_U)\|_{Y_h}
\le\frac{p_0}{2}
\right\}.
}
\tag{42a}
\]

Then

\[
\|\mathscr P_{S,b}V_{\mathcal U_{1/2}(h)}\|_{Y_h}
\ge\frac{p_0}{2}.
\tag{43}
\]

## 7. Exact parabolic-or-escape alternative

Consider a selected sequence \(h_j\downarrow0\) of smooth physical
layers satisfying the uniform floor (42), the uniform weak-\(L^3\)
ceiling (2a), and the same fixed cutoff conventions.  The exhaustive
alternative is:

1. for some fixed \(\kappa<\infty\) and a subsequence,

   \[
   \boxed{
   \mathcal U_{1/2}(h_j)
   \le\kappa h_j^{-1/2};
   }
   \tag{44}
   \]

2. or, after passing to a subsequence, for every
   \(\kappa<\infty\), eventually no dyadic
   \(F_*\le U\le\kappa h_j^{-1/2}\) satisfies the approximation in
   (42a).  Equivalently,

   \[
   \boxed{
   \mathcal U_{1/2}(h_j)\sqrt{h_j}
   \longrightarrow\infty.
   }
   \tag{45}
   \]

In branch 1, equations (37), (43) force the reviewed
stretched-exponential cost (38).  Branch (45) is a precise
**superparabolic spectral-capture escape**.  It is not a loose
``possibly high frequency'' remainder: no uniformly parabolic ceiling
captures even half of the separated-return continuation pressure.
It is a statement about LP insertions in this Dyson continuation, not
by itself an instantaneous Fourier-energy tail, spatial escape, or a
spectral theorem on the rough limiting hull.

The subsequent adversarially recomputed
[last-separated-return renewal theorem](adjoint-pressure-last-return-renewal.md)
removes item 3 as a standalone participation antecedent.  It partitions
the complete feedback pressure exactly into a no-chargeable-return
block and a last-return block.  The latter has the finite capture
ceiling proved here.  The subsequent adversarially recomputed
[no-return parabolic-exclusion theorem](adjoint-pressure-no-return-parabolic.md)
also proves that the exact complementary block is \(O(h^{7/4})\) below
every uniformly parabolic ceiling.  The current exhaustive frequency
boundary is therefore one common superparabolic LP--Dyson capture escape,
or the \(9/4\) stretched-exponential coefficient cost on the captured
last-return branch.

None of these theorems turns the common operator-series escape into an
instantaneous state-frequency tail or a same-trajectory physical charge.
They prove no singular solution, regularity theorem, breakdown theorem,
or Clay alternative A--D.

## 8. Executable ledger

The fractional Volterra coefficient, binary first-exit identity,
starting-band geometric sums, and \(9/4\) parabolic power are checked by

```bash
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_corridor_identification -v
PYTHONPATH=lab python -m \
  navier_lab.adjoint_pressure_corridor_identification
```
