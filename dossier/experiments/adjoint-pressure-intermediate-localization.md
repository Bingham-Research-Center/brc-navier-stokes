# Intermediate localisation eliminates the source-localised feedback payer

- **Experiment:** EXP-ADJOINT-PRESSURE-INTERMEDIATE-LOCALIZATION-001
- **Route:** ROUTE-R3B
- **Status:** conditional analytic reduction;
  [adversarially recomputed valid in scope](../review-ledger.md)
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** adversarially recomputed
  [feedback-tail theorem](adjoint-pressure-feedback-tail.md) and
  [feedback-shell theorem](adjoint-pressure-feedback-shells.md)

The reviewed feedback-shell theorem gives the exhaustive alternative

\[
\boxed{
\begin{array}{ll}
\text{source-localised payer:}
&
\displaystyle
\int_0^h
\|\mathcal T(r_h,b_h^{\rm in})(\tau)\|_1\,d\tau
\ge p_{\rm in}>0,
\\[5pt]
\text{exterior escape:}
&
\displaystyle
D_b(h)
\ge
h^{-3}\exp(c_{\rm sh}h^{-7/4}),
\end{array}}
\tag{1}
\]

where

\[
b_h^{\rm in}
=
\chi_{h^{-3}}b_h,
\qquad
\int_0^h
\|\nabla b_h^{\rm in}(\tau)\|_2^2\,d\tau
\le C_{\rm in}h^{-3}.
\tag{2}
\]

The first alternative is impossible. The missing observation is that
the reviewed exterior \(L^2\) tail of the zero-data remainder may be
used a second time, now after the coefficient has already been cut to
\(b_h^{\rm in}\). At an intermediate radius

\[
L_h=h^{-\alpha},
\qquad
\frac1{30}<\alpha<3,
\tag{3}
\]

the inner coefficient costs only \(O(L_h)\) local energy, whereas the
outer coefficient meets only the vanishing tail of \(r_h\). Both pieces
of \(\mathcal T(r_h,b_h^{\rm in})\) vanish.

For the concrete choice \(\alpha=1/10\),

\[
\boxed{
\int_0^h
\|\mathcal T(r_h,b_h^{\rm in})(\tau)\|_1\,d\tau
\le
C\left(
h^{29/20}
+
h^{41/20}
+
h^{3/10}
+
h^{1/2}
\right)
\longrightarrow0.
}
\tag{4}
\]

Thus the source-localised payer in (1) is empty. Every selected
zero-data drift-feedback sequence must take the stretched-exponential
exterior branch. This closes a genuine possibility-tree child, but the
stretched-exponential branch is not itself excluded and Clay remains
unsolved.

## 1. Reviewed zero-data tail and source cutoff

Retain the feedback equation

\[
\partial_\tau r_h
-\nu\Delta r_h
-\mathbb P(b_h\cdot\nabla r_h)
=
\mathbb P(b_h\cdot\nabla q_h),
\qquad
r_h(0)=0.
\tag{5}
\]

The arbitrary-terminal-time energy estimate gives

\[
\boxed{
\int_0^h\|r_h(\tau)\|_2^2\,d\tau
\le C_rh^3.
}
\tag{6}
\]

The adversarially recomputed feedback-tail theorem gives, for every
\(L\ge2\),

\[
\boxed{
\int_0^h
\|r_h(\tau)\|_{L^2(|x|>2L)}^2\,d\tau
\le
C_T
\left(
h^{7/2}L^{-1}
+
h^{5/2}L^{-15}
\right).
}
\tag{7}
\]

Let

\[
R_{\rm src}:=h^{-3}.
\tag{8}
\]

Choose the reviewed fixed-shape source cutoff so that

\[
\chi_{R_{\rm src}}=1
\quad\hbox{on }B_{4R_{\rm src}},
\qquad
\operatorname{supp}\chi_{R_{\rm src}}
\subset B_{8R_{\rm src}},
\tag{9}
\]

and put

\[
c_h:=b_h^{\rm in}:=\chi_{R_{\rm src}}b_h.
\tag{10}
\]

On the source-localised branch,

\[
\boxed{
\int_0^h\|\nabla c_h(\tau)\|_2^2\,d\tau
\le C_{\rm in}h^{-3}.
}
\tag{11}
\]

This is the crucial improvement over applying the feedback-tail master
estimate to the uncut coefficient \(b_h\), whose global dissipation can
be much larger.

The pressure operator is

\[
\mathcal T(z,c)
:=
\nabla\Delta^{-1}\operatorname{div}
\bigl((z\cdot\nabla)c\bigr).
\tag{12}
\]

For solenoidal \(z\), the reviewed CLMS estimate is

\[
\boxed{
\|\mathcal T(z,c)\|_1
\le
C_{\rm dH}\|z\|_2\|\nabla c\|_2.
}
\tag{13}
\]

Only the first factor must be divergence free.

## 2. Split the already localised coefficient at an intermediate radius

Choose a radial cutoff \(\chi_L\) satisfying

\[
\chi_L=1\quad\hbox{on }B_{4L},
\qquad
\chi_L=0\quad\hbox{outside }B_{8L},
\qquad
|\nabla\chi_L|\le CL^{-1},
\tag{14}
\]

and split

\[
c_h=c_{h,L}^{\rm near}+c_{h,L}^{\rm far},
\qquad
c_{h,L}^{\rm near}:=\chi_Lc_h,
\qquad
c_{h,L}^{\rm far}:=(1-\chi_L)c_h.
\tag{15}
\]

We will take \(L=h^{-\alpha}\) with \(\alpha<3\). Hence
\(8L<4R_{\rm src}\) for all sufficiently small \(h\), and
\(c_h=b_h\) throughout \(B_{8L}\). The centre and cutoff in the local
energy estimate are therefore exactly compatible with the source
cutoff.

The centre-uniform local-energy estimate and weak-\(L^3\) finite-volume
bound give

\[
\int_0^h
\|\nabla c_{h,L}^{\rm near}\|_2^2\,d\tau
\le
C\left(
L+hL^{-1}
\right).
\tag{16}
\]

Indeed, the first term is the actual coefficient dissipation in
\(B_{8L}\), and the cutoff term is

\[
L^{-2}
\int_0^h\|b_h(\tau)\|_{L^2(B_{8L})}^2\,d\tau
\le
CM^2hL^{-1}.
\tag{17}
\]

Equations (6), (13), and (16) imply

\[
\boxed{
\begin{aligned}
\int_0^h
\|\mathcal T(r_h,c_{h,L}^{\rm near})(\tau)\|_1\,d\tau
\le
C\left(
h^{3/2}L^{1/2}
+
h^2L^{-1/2}
\right).
\end{aligned}
}
\tag{18}
\]

## 3. The far coefficient meets only a solenoidal exterior remainder

A raw exterior cutoff of \(r_h\) is not divergence free. Apply the
reviewed scaled-annulus Bogovskii construction at radius \(L\). It
produces a solenoidal field \(\widetilde r_{h,L}\) satisfying

\[
\widetilde r_{h,L}=r_h
\quad\hbox{on }\operatorname{supp}
\nabla c_{h,L}^{\rm far},
\tag{19}
\]

and

\[
\|\widetilde r_{h,L}(\tau)\|_2
\le
C
\|r_h(\tau)\|_{L^2(|x|>2L)}.
\tag{20}
\]

Consequently,

\[
(r_h\cdot\nabla)c_{h,L}^{\rm far}
=
(\widetilde r_{h,L}\cdot\nabla)c_{h,L}^{\rm far}.
\tag{21}
\]

The global source-cutoff budget (11), the intermediate cutoff cost, and
\(hL^{-1}\ll h^{-3}\) give

\[
\int_0^h
\|\nabla c_{h,L}^{\rm far}\|_2^2\,d\tau
\le
C\left(h^{-3}+hL^{-1}\right)
\le Ch^{-3}.
\tag{22}
\]

Now apply (7), (13), and (19)--(22). Spacetime
Cauchy--Schwarz gives

\[
\boxed{
\begin{aligned}
\int_0^h
\|\mathcal T(r_h,c_{h,L}^{\rm far})(\tau)\|_1\,d\tau
\le
C\left(
h^{1/4}L^{-1/2}
+
h^{-1/4}L^{-15/2}
\right).
\end{aligned}
}
\tag{23}
\]

The two powers are exactly

\[
\left(h^{7/2}L^{-1}\right)^{1/2}
\left(h^{-3}\right)^{1/2}
=
h^{1/4}L^{-1/2},
\tag{24}
\]

\[
\left(h^{5/2}L^{-15}\right)^{1/2}
\left(h^{-3}\right)^{1/2}
=
h^{-1/4}L^{-15/2}.
\tag{25}
\]

No pressure kernel localisation, finite propagation, or moving-cube
estimate is used.

## 4. The exponent window closes the local payer

By linearity of \(\mathcal T\), equations (15), (18), and (23) give

\[
\boxed{
\begin{aligned}
P_{\rm src}(h)
:={}&
\int_0^h
\|\mathcal T(r_h,b_h^{\rm in})(\tau)\|_1\,d\tau\\
\le{}&
C\left(
h^{3/2}L^{1/2}
+
h^2L^{-1/2}
+
h^{1/4}L^{-1/2}
+
h^{-1/4}L^{-15/2}
\right).
\end{aligned}
}
\tag{26}
\]

Set

\[
L=L_h:=h^{-\alpha}.
\tag{27}
\]

The four powers of \(h\) in (26) are

\[
\frac32-\frac\alpha2,
\qquad
2+\frac\alpha2,
\qquad
\frac14+\frac\alpha2,
\qquad
-\frac14+\frac{15\alpha}{2}.
\tag{28}
\]

All are positive exactly when

\[
\boxed{\frac1{30}<\alpha<3.}
\tag{29}
\]

The requirements \(L\ge2\), the local-energy clock condition
\(\nu h\le\delta_{\rm LE}L^2\), and
\(8L<4R_{\rm src}\) also hold throughout this interval for all
sufficiently small \(h\).

Taking \(\alpha=1/10\) yields, in the order displayed in (26),

\[
\frac{29}{20},
\qquad
\frac{41}{20},
\qquad
\frac3{10},
\qquad
\frac12.
\tag{30}
\]

This proves (4), contradicting the fixed source-localised pressure floor
in the first line of (1).

## 5. Exact route consequence

The source-localised branch of the reviewed feedback-shell alternative
is empty. Therefore every selected zero-data drift-feedback sequence
must obey

\[
\boxed{
D_b(h)
\ge
h^{-3}\exp(c_{\rm sh}h^{-7/4}).
}
\tag{31}
\]

All later finite-frequency and high-coefficient descendants were
conditional refinements of the now-excluded source-localised payer.
Their theorems remain correct as conditional statements, but those
antecedents are empty within this reviewed branch tree.

Equation (31) is a major narrowing, not a contradiction. On one common
physical trajectory the zoom factor may shrink quickly enough that the
physical dissipation

\[
\sigma_hD_b(h)
\tag{32}
\]

still tends to zero. Nothing here:

- sums the stretched-exponential cost over event index;
- gives a lower bound on the physical zoom \(\sigma_h\);
- excludes the direct-response or signed late-annulus branches;
- closes finite-horizon or eternal parent candidates; or
- proves regularity, breakdown, or any Clay alternative A--D.

The live feedback gate is now:

> Can one-trajectory clock or genealogy geometry prevent
> \(\sigma_h\) from outrunning the stretched-exponential lower bound in
> (31), or convert that bound into a summable physical-history cost?

## Reproduce

```bash
make adjoint-pressure-intermediate-localization
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_intermediate_localization -v
make check
git diff --check
```
