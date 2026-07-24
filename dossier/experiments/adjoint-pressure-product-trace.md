# Uniform source roots identify the compact-window pressure trace

- **Experiment:** EXP-ADJOINT-PRESSURE-PRODUCT-TRACE-001
- **Route:** ROUTE-R3B
- **Status:** conditional analytic reduction;
  [independently reviewed valid after Polish-space and vector-variation repairs](../review-response-adjoint-pressure-product-trace-2026-07-24.md)
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** independently reviewed
  [balanced Kato-polar compactness theorem](adjoint-pressure-balanced-polar.md),
  [finite-amplitude window theorem](adjoint-pressure-amplitude-window.md),
  and [bulk-participation theorem](adjoint-pressure-trace-participation.md)

> **Successor boundary.** The later reviewed
> [intermediate-localisation theorem](adjoint-pressure-intermediate-localization.md)
> eliminates the source-localised ancestor of this finite-band chain.
> The theorem below remains correct conditionally, but its antecedent is
> empty within the reviewed feedback branch tree.

The preceding theorem gives the finite-band pressure a uniform
source-volume modulus. With

\[
K=\kappa h^{-1/2},
\qquad
\ell=K^{-1},
\qquad
R=h^{-3},
\qquad
\Omega_h=B_{BR},
\tag{1}
\]

every measurable
\(F\subset(0,h)\times\Omega_h\) obeys

\[
\boxed{
\int_F|H_h|
\le
C_B
\left(
\frac{|F|}{hR^3}
\right)^{1/7}
}
\tag{2}
\]

when the relative volume is at most one, with the global \(L^1\) bound
used above one.

This note uses (2) to close the remaining **conditional moving-trace
defect** for the fixed compact amplitude window. Root profiles uniformly
in \(x\in\Omega_h\), independently root the scaled time
\(s=t/h\), and let

\[
\mathsf Z_{h,x}(s,y)
:=
\frac{
a_h(hs,x+\ell y)/\varepsilon_h
}{
\sqrt{
1+|a_h(hs,x+\ell y)/\varepsilon_h|^2
}
}.
\tag{3}
\]

The three reviewed global balanced budgets imply that the
uniform-spatial-root laws of \(\mathsf Z_{h,x}\) are tight in strong
full-time, local-in-space \(L^2\). The uniform source-cylinder law then
pushes forward **exactly** to

\[
ds\otimes\rho_h(dz),
\tag{4}
\]

where \(\rho_h\) is the uniform-spatial-root profile law. In contrast,
the vector pressure measure pushes forward to a measure
\(\boldsymbol\nu_h\) satisfying

\[
\boxed{
|\boldsymbol\nu_h|(A)
\le
C\bigl(ds\otimes\rho_h\bigr)(A)^{1/7}.
}
\tag{5}
\]

Every limit therefore has the form

\[
d\boldsymbol\nu(s,z)
=
\boldsymbol f(s,z)\,ds\,d\rho(z),
\qquad
\boldsymbol f\in
L^{7/6,\infty}(ds\,d\rho).
\tag{6}
\]

The pressure-selected time can no longer lie on a moving graph
\(s=r(z)\): such a graph has zero product measure and hence zero
\(\boldsymbol\nu\)-mass.

Spatial band limitation makes the remaining evaluation exact. If
\(Q_K\) is the reviewed real even reproducing multiplier and \(q\) is
its fixed descendant-scale Schwartz kernel, define

\[
\mathscr E(z)(s)
:=
\int_{\mathbb R^3}
q(y)\mathcal W(z(s,y))\,dy.
\tag{7}
\]

Then the compact-window signed mark passes to the product law:

\[
\boxed{
-
\int_0^1\int_{\mathcal X}
\mathscr E(z)(s)\cdot\boldsymbol f(s,z)
\,d\rho(z)\,ds
\ge p_{\rm win}>0.
}
\tag{8}
\]

Thus the signed finite-band mark is represented by an actual
full-layer time of the limiting compact-window profile, after the exact
spatial reproduction already present in the prelimit pairing.

This closes the conditional moving-trace defect for the compact window.
It does not close concentration in the unwindowed amplitude, drift, or
pressure products and does not yet construct an amplitude-normalised
Oseen solution.

## 1. Reviewed balanced budgets and rooted variables

On the norm-gated balanced branch,

\[
0<\theta_-
\le
\frac{\varepsilon_h}{h^9}
\le\theta_+<\infty.
\tag{9}
\]

For a spatial root \(x\), retain the reviewed actions

\[
\mathfrak O_{h,x}^D
:=
\int_0^1\int_{B_D}
\Phi(A_{h,x}),
\tag{10}
\]

\[
\mathfrak K_{h,x}^D
:=
\int_0^1\int_{B_D}
\mathcal K_\Phi(A_{h,x}),
\tag{11}
\]

\[
\mathfrak P_{h,x}^D
:=
\int_0^1\int_{B_D}
|\nabla_y\Pi_{h,x}|.
\tag{12}
\]

Their physical conversions are

\[
\mathfrak O_{h,x}^D
=
\frac1{\varepsilon_hh\ell^3}
\int_0^h\int_{B_{D\ell}(x)}
\rho_{\varepsilon_h}(a_h),
\tag{13}
\]

\[
\mathfrak K_{h,x}^D
=
\frac1{\varepsilon_hh\ell}
\int_0^h\int_{B_{D\ell}(x)}
\mathcal K_{\varepsilon_h}(a_h),
\tag{14}
\]

\[
\mathfrak P_{h,x}^D
=
\frac1{\varepsilon_h\ell^3}
\int_0^h\int_{B_{D\ell}(x)}
|\nabla\pi_h^*|.
\tag{15}
\]

The reviewed global estimates are

\[
\int_0^h\int\rho_{\varepsilon_h}(a_h)\le C h,
\qquad
\int_0^h\int\mathcal K_{\varepsilon_h}(a_h)\le C,
\qquad
\int_0^h\int|\nabla\pi_h^*|\le C.
\tag{16}
\]

The transformed equation gives, rootwise,

\[
\|\mathsf Z_{h,x}\|_{L^2(0,1;H^1(B_D))}^2
\le
C_D\left(1+\mathfrak K_{h,x}^{D+1}\right),
\tag{17}
\]

\[
\begin{aligned}
\|\partial_s\mathsf Z_{h,x}\|_
{L^1(0,1;W^{-1,6/5}(B_D))}
\le C_D\big[
&(1+\kappa^2M)
(\mathfrak K_{h,x}^{D+1})^{1/2}\\
&+\mathfrak K_{h,x}^{D+1}
+\mathfrak P_{h,x}^{D+1}
\big].
\end{aligned}
\tag{17a}
\]

The modular action is additionally retained to keep limiting profiles
inside the regularised-polar state space. Only boundedness of the three
actions is used below.

The window is

\[
W_h
=
\mathcal W\left(
\frac{a_h}{\sqrt{|a_h|^2+\varepsilon_h^2}}
\right)
=
\mathcal W(\mathsf Z_h),
\qquad
\|W_h\|_\infty\le C_W,
\tag{18}
\]

with fixed smooth \(\mathcal W\), and

\[
-\int_0^h\int_{\mathbb R^3}W_h\cdot H_h
\ge p_{\rm win}>0.
\tag{19}
\]

The pressure has

\[
\int_0^h\int_{\mathbb R^3}|H_h|
\le C_{\rm pol},
\tag{20}
\]

and, for every fixed \(B>32\),

\[
\int_0^h\int_{\Omega_h^c}|H_h|
\longrightarrow0.
\tag{21}
\]

## 2. Uniform spatial roots have scale-free action means

Let

\[
d\lambda_h(x)
:=
\frac{\mathbf1_{\Omega_h}(x)}{|\Omega_h|}\,dx.
\tag{22}
\]

For fixed \(z\), the roots \(x\) for which
\(z\in B_{D\ell}(x)\) have volume at most \(C_D\ell^3\).
Fubini, (13), and the first estimate in (16) give

\[
\begin{aligned}
\int_{\Omega_h}
\mathfrak O_{h,x}^D\,d\lambda_h(x)
&\le
\frac{C_D}
{R^3\varepsilon_hh}
\int_0^h\int
\rho_{\varepsilon_h}(a_h)\\
&\le
\frac{C_D}{R^3\varepsilon_h}
\le C_D.
\end{aligned}
\tag{23}
\]

Similarly, (14)--(16) give

\[
\int_{\Omega_h}
\mathfrak K_{h,x}^D\,d\lambda_h(x)
\le
\frac{C_D\ell^2}
{R^3\varepsilon_hh}
\le C_D,
\tag{24}
\]

\[
\int_{\Omega_h}
\mathfrak P_{h,x}^D\,d\lambda_h(x)
\le
\frac{C_D}{R^3\varepsilon_h}
\le C_D.
\tag{25}
\]

The cancellations are

\[
R^3\varepsilon_h\asymp1,
\qquad
\frac{\ell^2}{R^3\varepsilon_hh}
\asymp1.
\tag{26}
\]

Markov's inequality, (17), and the same countable buffered-ball
Aubin--Lions argument as in the reviewed pressure-root theorem show that
the laws

\[
\rho_h
:=
(x\mapsto\mathsf Z_{h,x})_\#\lambda_h
\tag{27}
\]

are tight on the closed profile space

\[
\mathcal X_1
:=
\left\{
z\in
L^2\!\left((0,1);L^2_{\rm loc}(\mathbb R^3)\right):
|z|\le1\ {\rm a.e.}
\right\},
\tag{28}
\]

with the strong full-time, local-in-space projective topology.
The ambient projective \(L^2_{\rm loc}\) space is separable and complete,
and the constraint \(|z|\le1\) is closed under strong local \(L^2\)
convergence.  Thus \(\mathcal X_1\) is Polish.  For each prelimit \(h\),
translation continuity in local \(L^2\) makes
\(x\mapsto\mathsf Z_{h,x}\) Borel (indeed continuous), so the
pushforward in (27) is well defined.

After extraction,

\[
\rho_h\Rightarrow\rho
\qquad\hbox{on }\mathcal X_1.
\tag{29}
\]

## 3. The uniform cylinder becomes an exact product law

Define the uniform source-cylinder probability

\[
dm_h(t,x)
:=
\frac{
\mathbf1_{(0,h)\times\Omega_h}(t,x)
}{
h|\Omega_h|
}\,dt\,dx
\tag{30}
\]

and the decorated-root map

\[
\Theta_h(t,x)
:=
\left(
\frac th,
\mathsf Z_{h,x}
\right)
\in
\mathcal Y:=[0,1]\times\mathcal X_1.
\tag{31}
\]

The product space \(\mathcal Y\) is Polish.

The profile depends on \(x\), not on the independently selected root
time \(t\). Therefore

\[
\boxed{
\overline m_h
:=
(\Theta_h)_\#m_h
=
ds\otimes\rho_h.
}
\tag{32}
\]

In particular,

\[
\overline m_h
\Rightarrow
\overline m
:=
ds\otimes\rho.
\tag{33}
\]

Define the finite vector measure \(\boldsymbol\nu_h\) on
\(\mathcal Y\) by

\[
\int_{\mathcal Y}\varphi\,d\boldsymbol\nu_h
:=
\int_0^h\int_{\Omega_h}
\varphi\!\left(\frac th,\mathsf Z_{h,x}\right)
H_h(t,x)\,dx\,dt
\tag{34}
\]

for bounded Borel scalar \(\varphi\). For every Borel
\(A\subset\mathcal Y\), let

\[
F_A:=\Theta_h^{-1}(A).
\tag{35}
\]

Total variation cannot increase under pushforward. Equations (2),
(30), and \(|\Omega_h|\asymp R^3\) give

\[
\begin{aligned}
|\boldsymbol\nu_h|(A)
&\le
\int_{F_A}|H_h|\\
&\le
C
\left(
\frac{|F_A|}{hR^3}
\right)^{1/7}\\
&\le
C_B\overline m_h(A)^{1/7}
\end{aligned}
\tag{36}
\]

whenever \(\overline m_h(A)\le c_B\), while (20) supplies the global
bound. Enlarging the constant gives (5) for every \(A\).

This is the step unavailable before the bulk-participation theorem.
The pressure-root law is now uniformly absolutely continuous with
respect to a base law in which time and profile are independent.

## 4. The limiting pressure has a product-law density

The product probabilities \(\overline m_h\) are tight. Equation (5)
makes \(\boldsymbol\nu_h\) tight as finite vector measures: a set with
small \(\overline m_h\)-complement has small
\(|\boldsymbol\nu_h|\)-complement. Extract again so that

\[
\boldsymbol\nu_h
\stackrel{*}{\rightharpoonup}
\boldsymbol\nu.
\tag{37}
\]

The modulus passes to the limit. One convenient proof tests against
\(0\le\phi\le1\). Layer cake and (5) give

\[
\int\phi\,d|\boldsymbol\nu_h|
\le
C
\int_0^1
\overline m_h\{\phi>r\}^{1/7}\,dr
\le
C
\left(
\int\phi\,d\overline m_h
\right)^{1/7}.
\tag{38}
\]

No convergence of the total variations is needed.  For every continuous
\(0\le\phi\le1\) and every continuous vector test \(g\) with
\(|g|\le\phi\), (38) gives

\[
\left|\int g\cdot d\boldsymbol\nu_h\right|
\le
\int\phi\,d|\boldsymbol\nu_h|
\le
C
\left(
\int\phi\,d\overline m_h
\right)^{1/7}.
\tag{38a}
\]

Passing by (33) and (37), and then using the continuous-vector dual
description of total variation, yields

\[
\int\phi\,d|\boldsymbol\nu|
\le
C
\left(
\int\phi\,d\overline m
\right)^{1/7}.
\tag{38b}
\]

Regular approximation on the Polish space \(\mathcal Y\) extends this
inequality from continuous functions to Borel indicators and recovers the
same set modulus for the limit. Hence

\[
\boldsymbol\nu\ll\overline m
=ds\otimes\rho.
\tag{39}
\]

Writing its vector Radon--Nikodym density as \(\boldsymbol f\),

\[
d\boldsymbol\nu(s,z)
=
\boldsymbol f(s,z)\,ds\,d\rho(z).
\tag{40}
\]

The set modulus with exponent \(1/7\) is equivalent, up to constants,
to

\[
\boxed{
\boldsymbol f
\in
L^{7/6,\infty}
\bigl([0,1]\times\mathcal X_1,ds\,d\rho\bigr).
}
\tag{41}
\]

In particular, every graph

\[
\{(s,z):s=r(z)\}
\tag{42}
\]

of a measurable profile-dependent time has
\((ds\otimes\rho)\)-measure zero and therefore
\(|\boldsymbol\nu|\)-measure zero. The abstract moving bump from the
balanced compactness theorem cannot be the limiting pressure law.

## 5. Spatial reproduction turns the window into an \(L^2\) time observable

Let \(Q_K\) be the fixed-shape real even multiplier from the reviewed
amplitude-window theorem. Its symbol is one on
\(\operatorname{supp}\widehat H_h\), so

\[
Q_KH_h=H_h,
\qquad
\int_{\mathbb R^3}W_h\cdot H_h
=
\int_{\mathbb R^3}Q_KW_h\cdot H_h.
\tag{43}
\]

Write its convolution kernel as

\[
Q_Kf(x)
=
\int_{\mathbb R^3}
K^3q(K(x-z))f(z)\,dz,
\qquad
q\in\mathcal S(\mathbb R^3),
\quad q(-y)=q(y).
\tag{44}
\]

Changing variables \(z=x+\ell y\) gives the exact rooted identity

\[
Q_KW_h(hs,x)
=
\int_{\mathbb R^3}
q(y)\mathcal W(\mathsf Z_{h,x}(s,y))\,dy
=
\mathscr E(\mathsf Z_{h,x})(s),
\tag{45}
\]

where \(\mathscr E\) is (7).

The map

\[
\mathscr E:
\mathcal X_1
\longrightarrow
L^2(0,1;\mathbb R^3)
\tag{46}
\]

is continuous. Indeed, on \(|y|\le D\), smoothness of
\(\mathcal W\) and Cauchy--Schwarz control the difference by the strong
\(L^2((0,1)\times B_D)\) profile distance. On \(|y|>D\), it is at most

\[
2C_W\|q\|_{L^1(|y|>D)}
\longrightarrow0
\tag{47}
\]

uniformly in the profiles. Moreover,

\[
\|\mathscr E(z)\|_{L^\infty(0,1)}
\le
C_W\|q\|_1
=:M_{\mathscr E}.
\tag{48}
\]

As a continuous map into the separable space
\(L^2(0,1;\mathbb R^3)\), \(\mathscr E\) has a jointly Borel
representative \((s,z)\mapsto\mathscr E(z)(s)\).  All product-law
pairings below use this representative; changing it on a
\((ds\otimes\rho)\)-null set does not change the conclusion.

By (21), the exterior contributions of both \(W_h\) and \(Q_KW_h\)
against \(H_h\) tend to zero. Equations (19), (43), and (45) therefore
give

\[
\boxed{
-
\int_{\mathcal Y}
\mathscr E(z)(s)\cdot
d\boldsymbol\nu_h(s,z)
\ge
p_{\rm win}-o(1).
}
\tag{49}
\]

## 6. Full-time compactness makes the evaluation stable

The integrand in (49) is not continuous on
\(\mathcal Y\), because an \(L^2\) function cannot be evaluated
continuously at one time. The product structure and modulus (5) repair
exactly this issue.

Let \(J_\delta\) be a smooth time mollifier on \((0,1)\), after a fixed
bounded extension to the real line, and put

\[
G_\delta(s,z)
:=
\left(J_\delta\mathscr E(z)\right)(s).
\tag{50}
\]

For fixed \(\delta>0\), (46) makes \(G_\delta\) bounded and continuous
on \(\mathcal Y\).

Tightness of \(\rho_h\) gives, for every \(\eta>0\), a compact
\(\mathcal C_\eta\subset\mathcal X_1\) with

\[
\inf_h\rho_h(\mathcal C_\eta)\ge1-\eta
\tag{51}
\]

along the extracted tail. The image
\(\mathscr E(\mathcal C_\eta)\) is compact in \(L^2(0,1)\), so time
mollification converges uniformly on it. Using (32) and (48),

\[
\boxed{
\lim_{\delta\downarrow0}
\limsup_{h\downarrow0}
\int_{\mathcal Y}
|\mathscr E(z)(s)-G_\delta(s,z)|^2
\,d\overline m_h(s,z)
=0.
}
\tag{52}
\]

Put

\[
\mathcal R_\delta(s,z)
:=
|\mathscr E(z)(s)-G_\delta(s,z)|
\le2M_{\mathscr E}.
\tag{53}
\]

For every \(0<\gamma<2M_{\mathscr E}\), split at
\(\mathcal R_\delta=\gamma\). Equations (5) and Chebyshev give

\[
\begin{aligned}
\int\mathcal R_\delta\,d|\boldsymbol\nu_h|
&\le
\gamma|\boldsymbol\nu_h|(\mathcal Y)
+
2M_{\mathscr E}
|\boldsymbol\nu_h|
\{\mathcal R_\delta>\gamma\}\\
&\le
C\gamma
+
C M_{\mathscr E}
\left(
\frac{
\|\mathcal R_\delta\|_{L^2(\overline m_h)}^2
}{\gamma^2}
\right)^{1/7}.
\end{aligned}
\tag{54}
\]

For fixed \(\gamma\), first use (52); then let
\(\gamma\downarrow0\). This proves

\[
\lim_{\delta\downarrow0}
\limsup_{h\downarrow0}
\int\mathcal R_\delta\,d|\boldsymbol\nu_h|
=0.
\tag{55}
\]

The same argument applies to
\((\overline m,\boldsymbol\nu)\). For fixed \(\delta\), weak convergence
in (37) passes the bounded continuous \(G_\delta\). Letting
\(\delta\downarrow0\) in (55) consequently gives

\[
\boxed{
\int_{\mathcal Y}
\mathscr E(z)(s)\cdot d\boldsymbol\nu_h
\longrightarrow
\int_{\mathcal Y}
\mathscr E(z)(s)\cdot d\boldsymbol\nu.
}
\tag{56}
\]

This is the trace-identification step. It uses full-time profile
compactness, exact product rooting, and the source-volume pressure
modulus together; none of the three alone suffices.

## 7. The signed mark belongs to the limiting profile

Combine (40), (49), and (56):

\[
\boxed{
-
\int_0^1
\int_{\mathcal X_1}
\mathscr E(z)(s)
\cdot
\boldsymbol f(s,z)
\,d\rho(z)\,ds
\ge
p_{\rm win}>0.
}
\tag{57}
\]

This is an actual product-law pairing. The variable \(s\) is Lebesgue
time on the whole scaled layer, \(z\) is a strong full-time
compact-window profile, and \(\boldsymbol f\) is a genuine
weak-\(L^{7/6}\) density rather than a graph-supported trace.

The spatial convolution in \(\mathscr E\) is not a loss: (43) says it
is exactly invisible to the finite-band pressure pairing. Equation (57)
therefore identifies the complete reviewed compact-window signed mark.

## 8. Exact consequence and remaining gate

On every norm-gated balanced first-hitting charged finite-band
subsequence:

1. uniform source roots have scale-free mean modular, Kato, and pressure
   actions;
2. their regularised-polar profile laws are tight in strong full-time,
   local-in-space \(L^2\);
3. uniform time and uniform spatial rooting give the exact product law
   \(ds\otimes\rho_h\);
4. finite-band pressure is uniformly absolutely continuous with
   exponent \(1/7\) relative to that product law;
5. every limiting pressure has a density
   \(\boldsymbol f\in L^{7/6,\infty}(ds\,d\rho)\);
6. spatial reproduction and temporal mollification pass the complete
   compact-window signed pairing to the limit;
7. the limiting product-law pairing remains strictly positive.

This excludes both:

- disappearance of the charged window into a source-volume-vanishing
  layer; and
- conditional concentration of pressure time on a moving graph over
  the profile law.

It does not prove:

- compactness of the unwindowed amplitude
  \(A_h=a_h/\varepsilon_h\);
- convergence of the drift, diffusion, or pressure products in the
  amplitude-normalised Oseen equation;
- that \(\boldsymbol f\) is the pressure generated by a limiting
  amplitude and drift;
- a nonzero amplitude-normalised Oseen solution or an Oseen rigidity
  contradiction;
- a finite charge for the strict sub-\(h^9\) branch;
- an event telescope, finite same-trajectory budget, regularity theorem,
  breakdown theorem, or Clay alternative A--D.

The exact balanced question is now:

> Can the unwindowed amplitude, drift, and pressure products be closed
> around the nonzero compact-window product-law mark, producing an
> honest amplitude-normalised Oseen limit to which rigidity applies?

## Reproduce

```bash
make adjoint-pressure-product-trace
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_product_trace -v
make check
git diff --check
```
