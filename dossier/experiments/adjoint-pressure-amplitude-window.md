# A compact relative-amplitude observable retains balanced pressure charge

- **Experiment:** EXP-ADJOINT-PRESSURE-AMPLITUDE-WINDOW-001
- **Route:** ROUTE-R3B
- **Status:** conditional analytic reduction;
  [adversarially recomputed valid after scope repair](../review-ledger.md)
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** adversarially recomputed
  [first-hitting polar-vacuum theorem](adjoint-pressure-polar-vacuum.md)
  and, for the strong profile conclusion, the norm-gated
  [balanced Kato-polar compactness theorem](adjoint-pressure-balanced-polar.md)

The balanced first-hitting branch previously had two named defects:
linear-growth amplitude concentration and a moving pressure trace. This
note separates them.

For \(L\ge1\), soften the regularised polar from scale
\(\varepsilon_h\) to \(L\varepsilon_h\):

\[
\zeta_h^{(L)}
:=
\frac{a_h}{\sqrt{|a_h|^2+(L\varepsilon_h)^2}}.
\tag{1}
\]

The first-hitting mass, band limitation, and moving-grid pressure capture
give the quantitative tail

\[
\boxed{
\left|
\int_0^h\!\!\int
\zeta_h^{(L)}\cdot H_h
\right|
\le
C L^{-1/11}.
}
\tag{2}
\]

The constant is uniform in \(h\) on every balanced subsequence

\[
0<\theta_-
\le
\theta_h:=\frac{\varepsilon_h}{h^9}
\le\theta_+<\infty.
\tag{3}
\]

Subtracting (1) from the original charged polar and then applying a fixed
smooth cutoff leaves a compactly supported smooth test of the net signed
amplitude observable with positive pairing. Its support lies where

\[
0<\frac{r_-}{2}
\le \frac{|a_h|}{\varepsilon_h}
\le2r_+<\infty.
\tag{4}
\]

Thus neither the vacuum \(a_h/\varepsilon_h\to0\) nor concentration at
\(|a_h|/\varepsilon_h\to\infty\) can be the sole carrier of the
finite-band charge in this signed-observable, vague-amplitude sense. This
does not prove decay of absolute pressure mass at large amplitude or
positivity of the raw indicator-truncated polar on one interval. On the
norm-gated path, the windowed observable is a smooth function of the
already compact full-time, local-in-space polar profile. At this stage,
the remaining failure to pass its positive pairing to a limit was the
moving pressure-trace defect. The subsequent
[bulk-participation theorem](adjoint-pressure-trace-participation.md)
excludes its source-volume-vanishing realisation but leaves conditional
identification of the signed pressure-root time open.

This is not global compactness of \(a_h/\varepsilon_h\). Uncharged
amplitude concentration may remain and may still obstruct closure of the
full Oseen products.

## 1. Exact balanced first-hitting input

Retain the notation of the two input theorems:

\[
\rho_\varepsilon(z)
:=
\sqrt{|z|^2+\varepsilon^2}-\varepsilon,
\qquad
\zeta_h^{(1)}
:=
\frac{a_h}{\sqrt{|a_h|^2+\varepsilon_h^2}},
\tag{5}
\]

\[
K=\kappa h^{-1/2},
\qquad
\ell=K^{-1},
\qquad
H_h=P_{>K}\mathcal T(r^{\rm lo},b^{\rm lo}).
\tag{6}
\]

First hitting gives, uniformly for \(0\le\tau\le h\),

\[
\boxed{
\int_{\mathbb R^3}
\rho_{\varepsilon_h}(a_h(\tau))\,dx
\le M_\rho.
}
\tag{7}
\]

The charged finite-band child supplies

\[
\boxed{
-\int_0^h\!\!\int
\zeta_h^{(1)}\cdot H_h
\ge p_{\rm pol}>0,
}
\tag{8}
\]

\[
p_{\rm pol}
\le
Z_h
:=
\int_0^h\!\!\int|H_h|
\le C_{\rm pol}.
\tag{9}
\]

To justify (8) without changing the reviewed construction, let \(Q_K\)
be its real even multiplier. Its symbol is one on the Fourier support of
\(H_h\), so

\[
Q_KH_h=H_h,
\qquad
\int Q_Kf\cdot H_h=\int f\cdot H_h.
\tag{10}
\]

Finally, a measurable time-dependent union of at most \(N_*\)
descendant \(\ell\)-cubes obeys the reviewed moving-grid capture estimate

\[
\boxed{
\int_0^h\int_{U(\tau)}|H_h|
\le
C_{\rm mov}h^{7/4}N_*^{1/6}.
}
\tag{11}
\]

The tail theorem below uses only (3) and (5)--(11). The stronger
norm-gated hypothesis is needed only when the result is combined with
the spacetime compactness theorem in Section 6.

## 2. Softened polar volume gains one power of \(L^{-1}\)

Put

\[
r:=\frac{|a_h|}{\varepsilon_h},
\qquad
\Phi(r):=\sqrt{1+r^2}-1.
\tag{12}
\]

Pointwise,

\[
|\zeta_h^{(L)}|^2
=
\frac{r^2}{r^2+L^2}.
\tag{13}
\]

Since

\[
\frac{
L|\zeta_h^{(L)}|^2
}{
\Phi(r)
}
=
\frac{L(\sqrt{1+r^2}+1)}{r^2+L^2}
\le2,
\tag{14}
\]

with the continuous interpretation at \(r=0\), we have

\[
\boxed{
|\zeta_h^{(L)}|^2
\le
\frac2L\Phi(r).
}
\tag{15}
\]

For completeness, write \(x=\sqrt{1+r^2}\ge1\). The derivative of

\[
x\longmapsto
\frac{L(x+1)}{x^2+L^2-1}
\tag{16}
\]

has the sign of \(L^2-(x+1)^2\). If \(1\le L\le2\), the maximum is
\(2/L\le2\) at \(x=1\). If \(L\ge2\), the interior maximum is
\(L/[2(L-1)]\le1\). This proves (14).

Because

\[
\rho_{\varepsilon_h}(a_h)
=
\varepsilon_h\Phi(r),
\tag{17}
\]

equations (7) and (15) yield

\[
\boxed{
\|\zeta_h^{(L)}(\tau)\|_2^2
\le
\frac{2M_\rho}{L\varepsilon_h}
\qquad(0\le\tau\le h).
}
\tag{18}
\]

The new factor \(L^{-1}\) is the source of the pairing decay.

## 3. Bernstein balls count the large projected polar set

Let

\[
f_{h,L}(\tau):=Q_K\zeta_h^{(L)}(\tau).
\tag{19}
\]

If \(q_K(x)=K^3q(Kx)\) is the kernel of \(Q_K\), then

\[
\|f_{h,L}(\tau)\|_\infty\le C_Q,
\qquad
\|\nabla f_{h,L}(\tau)\|_\infty\le C_{\nabla Q}K,
\tag{20}
\]

and \(Q_K\) is bounded on \(L^2\). Fix \(0<\alpha\le1\), and let

\[
G_{h,L,\alpha}(\tau)
:=
\{x:|f_{h,L}(\tau,x)|\ge\alpha\}.
\tag{21}
\]

Cover this set by all descendant grid cubes meeting it. For each active
cube choose one point \(x_m\) in (21). The Lipschitz bound in (20) gives

\[
|f_{h,L}(\tau,y)|\ge\frac\alpha2
\quad\hbox{on}\quad
B_{c_Q\alpha/K}(x_m),
\tag{22}
\]

where \(c_Q>0\) is fixed and may be reduced so that the radius is at most
\(\ell/4\).

Colour the grid indices modulo three in each coordinate. Within each of
the resulting \(27\) classes the balls in (22) are disjoint. Therefore
each active cube costs at least

\[
c_Q\alpha^2(\alpha/K)^3
=c_Q\alpha^5K^{-3}
\tag{23}
\]

of the \(L^2\) mass of \(f_{h,L}\), up to the fixed number of colours.
Equation (18) gives the time-uniform count

\[
\boxed{
N_{h,L,\alpha}(\tau)
\le
\frac{C_QK^3}
{L\varepsilon_h\alpha^5}
\qquad\hbox{for a.e. }\tau.
}
\tag{24}
\]

The count first applies to finite spatial truncations. Monotone
convergence removes the truncation. As in the input moving-grid theorem,
membership is Borel in \(\tau\) because the smooth threshold function is
maximised on each closed cube.

## 4. The softened pairing has an \(L^{-1/11}\) tail

By (10),

\[
\int\zeta_h^{(L)}\cdot H_h
=
\int f_{h,L}\cdot H_h.
\tag{25}
\]

On the complement of (21), the absolute pairing is at most
\(\alpha Z_h\). On (21), use
\(\|f_{h,L}\|_\infty\le C_Q\), cover it by the active cubes from (24),
and apply (11). This gives

\[
\begin{aligned}
\left|
\int_0^h\!\!\int
\zeta_h^{(L)}\cdot H_h
\right|
&\le
C_{\rm pol}\alpha
+
C h^{7/4}
\left(
\frac{K^3}
{L\varepsilon_h\alpha^5}
\right)^{1/6}\\
&=
C_{\rm pol}\alpha
+
C\theta_h^{-1/6}
L^{-1/6}\alpha^{-5/6}.
\end{aligned}
\tag{26}
\]

The last equality uses \(K=\kappa h^{-1/2}\) and
\(\varepsilon_h=\theta_hh^9\):

\[
h^{7/4}K^{1/2}\varepsilon_h^{-1/6}
\asymp
h^{7/4-1/4-3/2}\theta_h^{-1/6}
=\theta_h^{-1/6}.
\tag{27}
\]

On the balanced branch, choose

\[
\alpha=L^{-1/11}.
\tag{28}
\]

Both terms in (26) then have the same power:

\[
L^{-1/6}\alpha^{-5/6}
=
L^{-1/6+5/66}
=L^{-1/11}.
\tag{29}
\]

Thus

\[
\boxed{
\sup_h
\left|
\int_0^h\!\!\int
\zeta_h^{(L)}\cdot H_h
\right|
\le
C(\theta_-,\kappa,M_\rho,Q,C_{\rm mov},C_{\rm pol})
L^{-1/11}.
}
\tag{30}
\]

This is the claimed large-softening tail. No limiting profile or
pressure trace is used.

## 5. A fixed compact relative-amplitude window retains charge

Define the soft window

\[
\beta_h^{(L)}
:=
\zeta_h^{(1)}-\zeta_h^{(L)}.
\tag{31}
\]

Choose one fixed \(L_0\ge1\), independent of \(h\), sufficiently large
that the right side of (30) is at most \(p_{\rm pol}/4\). Equations (8)
and (30) give

\[
\boxed{
-\int_0^h\!\!\int
\beta_h^{(L_0)}\cdot H_h
\ge
\frac{3p_{\rm pol}}4.
}
\tag{32}
\]

This soft window already vanishes at both ends of the relative-amplitude
axis. Indeed, with \(r=|a_h|/\varepsilon_h\),

\[
|\beta_h^{(L)}|
=
\frac r{\sqrt{r^2+1}}
-
\frac r{\sqrt{r^2+L^2}},
\tag{33}
\]

so

\[
|\beta_h^{(L)}|\le r
\quad(r\ge0),
\tag{34}
\]

and

\[
|\beta_h^{(L)}|
\le
\frac{L^2-1}{2r^2}
\quad(r>0).
\tag{35}
\]

For (35), rationalise the difference in (33) and bound its denominator
below by \(2r^3\).

Choose fixed \(0<r_-<r_+<\infty\) so that

\[
C_{\rm pol}r_-\le\frac{p_{\rm pol}}{16},
\qquad
C_{\rm pol}
\frac{L_0^2-1}{2r_+^2}
\le\frac{p_{\rm pol}}{16}.
\tag{36}
\]

Let \(\chi\in C^\infty([0,\infty))\) satisfy

\[
0\le\chi\le1,
\qquad
\chi=1\ \hbox{on }[r_-,r_+],
\qquad
\operatorname{supp}\chi
\subset[r_-/2,2r_+].
\tag{37}
\]

The part removed by \(\chi\) is contained in
\(\{r<r_-\}\cup\{r>r_+\}\). Equations (9), (34), (35), and (36) show
that its absolute pairing is at most \(p_{\rm pol}/8\). Hence the hard
window

\[
W_h
:=
\chi\!\left(\frac{|a_h|}{\varepsilon_h}\right)
\beta_h^{(L_0)}
\tag{38}
\]

satisfies

\[
\boxed{
-\int_0^h\!\!\int W_h\cdot H_h
\ge
\frac{5p_{\rm pol}}8
\ge\frac{p_{\rm pol}}2.
}
\tag{39}
\]

The constants \(L_0,r_-,r_+\) depend only on the uniform branch
constants, not on \(h\). Equation (39) is the precise sense in which a
fixed finite relative-amplitude window retains positive charge.

## 6. The charged window is a smooth function of the compact polar

Let

\[
\mathsf Z_h
:=
\frac{A_h}{\sqrt{1+|A_h|^2}},
\qquad
A_h:=\frac{a_h}{\varepsilon_h}.
\tag{40}
\]

Solving algebraically for the softened polar gives

\[
\zeta_h^{(L)}
=
\frac{\mathsf Z_h}
{\sqrt{
|\mathsf Z_h|^2
+L^2(1-|\mathsf Z_h|^2)
}}.
\tag{41}
\]

Thus

\[
\beta_h^{(L)}
=
\mathcal B_L(\mathsf Z_h),
\tag{42}
\]

where, on the closed unit ball,

\[
\boxed{
\mathcal B_L(z)
:=
z\left(
1-
\frac1{
\sqrt{|z|^2+L^2(1-|z|^2)}
}
\right).
}
\tag{43}
\]

The denominator in (43) is at least one.
\(\mathcal B_L(0)=0\), and
\(\mathcal B_L(z)=0\) when \(|z|=1\). The hard cutoff in (38) also
vanishes in neighbourhoods of \(z=0\) and \(|z|=1\). Consequently (38)
can be written

\[
W_h=\mathcal W(\mathsf Z_h)
\tag{44}
\]

for one fixed smooth, hence Lipschitz, map
\(\mathcal W:\overline{B_1(0)}\to\mathbb R^3\).

Equivalently, in the relative-amplitude variable,

\[
\boxed{
W_h
=
\chi(r)m_{L_0}(r)\zeta_h^{(1)},
\qquad
m_L(r)
:=
1-
\frac{\sqrt{r^2+1}}{\sqrt{r^2+L^2}}.
}
\tag{44a}
\]

For \(L>1\), \(m_L(r)\) is positive but nonconstant. Thus (39)
localises a weighted net signed amplitude observable. It does not assert
positive pairing for the raw field
\(\mathbf1_{\{r_-\le r\le r_+\}}\zeta_h^{(1)}\).

On the norm-gated balanced path, the previous theorem makes the rooted
laws of \(\mathsf Z_h\) tight on strong

\[
L^2_{\rm loc}((0,1)\times\mathbb R^3).
\tag{45}
\]

The Lipschitz composition in (44) therefore makes the rooted laws of the
charged finite-amplitude window \(W_h\) tight on the same strong
topology. Infinite-amplitude concentration cannot be the sole carrier of
the positive signed observable in (39).

This still does not justify passage to the pressure-weighted trace.
The pressure measure and \(W_h\) may move together through a thin time
layer exactly as in the moving-bump countermodel from the preceding
theorem. Strong bulk convergence of \(W_h\) is insufficient to identify

\[
\lim_h\int W_h\cdot H_h.
\tag{46}
\]

## 7. Exact dyadic amplitude resolution

There is also a pointwise same-sign telescope:

\[
\zeta_\varepsilon
=
\sum_{k=0}^{N-1}
\left(
\zeta_{2^k\varepsilon}
-
\zeta_{2^{k+1}\varepsilon}
\right)
+
\zeta_{2^N\varepsilon}.
\tag{47}
\]

Letting \(N\to\infty\) gives

\[
\boxed{
\zeta_\varepsilon
=
\sum_{k=0}^{\infty}
\left(
\zeta_{2^k\varepsilon}
-
\zeta_{2^{k+1}\varepsilon}
\right),
\qquad
\sum_{k=0}^{\infty}
\left|
\zeta_{2^k\varepsilon}
-
\zeta_{2^{k+1}\varepsilon}
\right|
=|\zeta_\varepsilon|.
}
\tag{48}
\]

All terms are parallel to \(a\) and have nonnegative scalar
coefficients, so there is no absolute-value loss. Equation (30) says
that the aggregate pairing of the softened remainder in (47) vanishes
quantitatively. This is an amplitude resolution of one event, not an
event-index telescope and not a finite same-trajectory depth budget.

## 8. Exact consequence and remaining gate

Conditional on the balanced first-hitting charged finite-band branch:

1. the pairing of the \(L\varepsilon_h\)-softened polar is
   \(O(L^{-1/11})\), uniformly in \(h\);
2. one fixed smooth window
   \(r_-/2\le|a_h|/\varepsilon_h\le2r_+\) carries a positive fraction of
   the pressure charge as the weighted net signed observable (44a);
3. neither relative-amplitude vacuum nor infinite-amplitude
   concentration can be the sole carrier of that signed observable;
4. on the norm-gated path, the charged window is a smooth function of
   the strongly tight full-time, local-in-space polar profile.

This removes **linear-growth amplitude concentration as the sole carrier
of the positive finite-band mark in the signed-observable,
vague-amplitude sense**. It does not prove:

- global weak or strong compactness of \(a_h/\varepsilon_h\);
- decay of absolute pressure mass at large relative amplitude;
- positive pairing for a raw indicator-truncated polar on one amplitude
  interval;
- absence of uncharged amplitude concentration in the Oseen equation;
- convergence of the full pressure or drift products;
- conditional identification of the pressure-weighted trace with the
  limiting profile;
- a finite charge for the strict sub-\(h^9\) cascade;
- an event-index telescope or finite same-trajectory budget;
- regularity, breakdown, or any Clay alternative A--D.

The subsequent
[bulk-participation theorem](adjoint-pressure-trace-participation.md)
uses annular reproduction and the moving-grid theorem to exclude
concentration of fixed charge on every source-volume-vanishing set. It
also forces fixed positive probability of a nonzero full-time
compact-window profile. Thus the pure zero-profile moving thin layer is
no longer live.

The remaining norm-gated balanced-branch question is:

> Can the Oseen pressure structure identify the signed pressure-root
> time with the surviving nonzero compact-window profile law, and then
> close any remaining uncharged concentration in the full Oseen
> products?

The strict sub-\(h^9\) amplitude cascade remains the other finite-band
branch.

## Reproduce

```bash
make adjoint-pressure-amplitude-window
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_amplitude_window -v
make check
git diff --check
```
