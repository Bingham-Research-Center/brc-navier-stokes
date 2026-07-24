# First-hitting Kato mass forces an inverse-ninth vacuum polar scale

- **Experiment:** EXP-ADJOINT-PRESSURE-POLAR-VACUUM-001
- **Route:** ROUTE-R3B
- **Status:** conditional analytic reduction;
  [adversarially recomputed valid after repair](../review-ledger.md)
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** adversarially recomputed
  [Kato-polar signed aggregate](adjoint-pressure-signed-aggregate.md) and
  [temporal-disintegration reduction](adjoint-pressure-temporal-disintegration.md)

The preceding temporal theorem left three possible ways to relate the
finite-band pressure slices: time compactness of the effective polar,
a limiting Oseen balance, or a same-trajectory telescope. This note closes
the most direct version of the second possibility.

The terminal mass-gain stopping can be made canonical. Stop the selected
regularisation at its **first** fixed positive mass gain. On the whole
resulting layer,

\[
L_{\varepsilon_h}(a_h(\tau))
\le
\|\varphi\|_1+\gamma_*.
\]

Consequently its regularised polar

\[
\zeta_h
:=
\frac{a_h}{\sqrt{|a_h|^2+\varepsilon_h^2}}
\]

has the uniform spatial-volume bound

\[
\|\zeta_h(\tau)\|_2^2
\lesssim
\varepsilon_h^{-1}.
\]

The finite-band pressure capture estimate also admits a moving-grid form:
if \(\mathcal F(\tau)\) is a measurable family of descendant cubes, then

\[
\int_0^h\int_{U_{\mathcal F(\tau)}}|H_h|
\lesssim
h^{3/2}
\left(
K\int_0^h|\mathcal F(\tau)|^{1/3}\,d\tau
\right)^{1/2}.
\]

Positive effective-polar work can occur only on cubes where a local
\(L^2\) amount of \(\zeta_h\) is present. The first-hitting bound permits
at most \(C\varepsilon_h^{-1}K^3\) such cubes at any time. Combining these
facts with \(K=\kappa h^{-1/2}\) forces

\[
\boxed{\varepsilon_h\lesssim h^9.}
\]

This is much smaller than the earlier \(O(h^2)\) ceiling. The exponent is
the exact point at which an order-one polar can fill the
\(h^{-21/2}\) descendant cells required by the finite-band pressure cloud
while its regularised mass remains bounded.

There is a parallel state-level conclusion. At points sampled by the
finite-band pressure law, the rooted field

\[
y\longmapsto h^{-2}
\bigl(a_h(\tau,x+K^{-1}y)-\varphi(x+K^{-1}y)\bigr)
\]

converges to zero in local \(L^2\), in probability. The fixed detector also
vanishes at those roots. Yet the effective polar mark has positive limiting
alignment. Thus the surviving decoration is a **vacuum polarisation**:
it is not the polar of a nonzero \(h^2\)-normalised Oseen profile.

This does not exclude the finite-band branch. It replaces a prospective
quadratic-scale Oseen profile by a sharper amplitude-scale question:
compactify the adjoint at its selected scale \(\varepsilon_h\), prove that
\(\varepsilon_h\) cannot descend far below \(h^9\), or find a
same-trajectory functional which does not require continuity of the polar
map at zero.

## 1. Canonical first-hitting terminal layers

Retain the smooth reversed Oseen system

\[
\partial_\tau a-\nu\Delta a
-b\cdot\nabla a+\nabla\pi^*=0,
\qquad
\nabla\cdot a=\nabla\cdot b=0,
\qquad
a(0)=\varphi,
\tag{1}
\]

and write

\[
\rho_\varepsilon(z)
:=
\sqrt{|z|^2+\varepsilon^2}-\varepsilon,
\qquad
L_\varepsilon(f)
:=
\int_{\mathbb R^3}\rho_\varepsilon(f)\,dx.
\tag{2}
\]

For fixed \(\varepsilon>0\), put

\[
\Delta_\varepsilon(\tau)
:=
L_\varepsilon(a(\tau))-L_\varepsilon(\varphi).
\tag{3}
\]

The temporal-disintegration theorem supplies a terminal sequence with

\[
h_j^{(0)}\longrightarrow0,
\qquad
\Delta_{\varepsilon_j}(h_j^{(0)})\ge\gamma,
\tag{4}
\]

where \(\gamma>0\) is independent of \(j\). Set

\[
\gamma_*:=\frac{\gamma}{2}.
\tag{5}
\]

The map in (3) is continuous. Indeed, for \(z,z'\in\mathbb R^3\),

\[
\left|
\rho_\varepsilon(z)-\rho_\varepsilon(z')
\right|
\le
\frac{(|z|+|z'|)|z-z'|}{2\varepsilon}.
\tag{6}
\]

The smooth Oseen solution is continuous in \(L^2\), so (6) and
Cauchy--Schwarz give continuity of \(L_\varepsilon(a(\tau))\).

Define the first hitting time

\[
h_j
:=
\inf
\left\{
0\le\tau\le h_j^{(0)}:
\Delta_{\varepsilon_j}(\tau)=\gamma_*
\right\}.
\tag{7}
\]

Equations (3)--(6) imply

\[
0<h_j\le h_j^{(0)},
\qquad
h_j\longrightarrow0,
\tag{8}
\]

\[
\boxed{
\Delta_{\varepsilon_j}(h_j)=\gamma_*,
\qquad
\Delta_{\varepsilon_j}(\tau)<\gamma_*
\quad(0\le\tau<h_j).
}
\tag{9}
\]

The exact Kato-polar identity is

\[
-\int_0^s\!\!\int
\zeta_\varepsilon(a)\cdot\nabla\pi^*
=
\Delta_\varepsilon(s)
+\nu\int_0^s\mathcal K_\varepsilon(a),
\qquad
\mathcal K_\varepsilon(a)\ge0.
\tag{10}
\]

At the new stopping time,

\[
\boxed{
-\int_0^{h_j}\!\!\int
\zeta_{\varepsilon_j}(a_j)\cdot\nabla\pi_j^*
\ge\gamma_*.
}
\tag{11}
\]

Thus the whole reviewed signed pressure decomposition may be rerun on
\([0,h_j]\), with smaller fixed constants and unchanged powers. The branch
tree may select a different child after this refinement. In the remainder
of this note, assume that a subsequence reaches the charged finite-band
child.

Abbreviate that subsequence by

\[
h:=h_j,
\qquad
\varepsilon_h:=\varepsilon_j,
\qquad
a_h:=a_j,
\qquad
\zeta_h:=\zeta_{\varepsilon_h}(a_h).
\tag{12}
\]

Equation (9) gives the uniform-in-time regularised mass bound

\[
\boxed{
L_{\varepsilon_h}(a_h(\tau))
\le
L_{\varepsilon_h}(\varphi)+\gamma_*
\le
\|\varphi\|_1+\gamma_*
=:
M_\rho
\quad(0\le\tau\le h).
}
\tag{13}
\]

This is the extra information which was absent from an arbitrary
near-maximising stopping time.

## 2. First hitting bounds the spatial polar volume

For \(t=|z|/\varepsilon\),

\[
\frac{\rho_\varepsilon(z)}{\varepsilon}
=
\sqrt{1+t^2}-1
=
\frac{t^2}{\sqrt{1+t^2}+1},
\tag{14}
\]

whereas

\[
\left|
\frac{z}{\sqrt{|z|^2+\varepsilon^2}}
\right|^2
=
\frac{t^2}{1+t^2}.
\tag{15}
\]

Since

\[
\frac{\sqrt{1+t^2}+1}{1+t^2}\le2,
\tag{16}
\]

equations (14)--(15) give the pointwise inequality

\[
\boxed{
|\zeta_\varepsilon(z)|^2
\le
\frac{2}{\varepsilon}\rho_\varepsilon(z).
}
\tag{17}
\]

Combining (13) and (17) yields

\[
\boxed{
\|\zeta_h(\tau)\|_2^2
\le
\frac{2M_\rho}{\varepsilon_h}
\quad(0\le\tau\le h).
}
\tag{18}
\]

This is not a derivative estimate. It says that an order-one polar field
can occupy at most \(O(\varepsilon_h^{-1})\) spatial volume while the
first-hitting mass is bounded.

## 3. The finite-band capture estimate follows moving grids

Retain the finite-band notation

\[
K=\kappa h^{-1/2},
\qquad
\ell=K^{-1},
\tag{19}
\]

\[
H_h
:=
P_{>K}\mathcal T(r^{\rm lo},b^{\rm lo}),
\tag{20}
\]

and the physical grid

\[
Q_m:=\ell(m+[0,1)^3),
\qquad
m\in\mathbb Z^3.
\tag{21}
\]

Let \(\tau\mapsto\mathcal F(\tau)\subset\mathbb Z^3\) be a measurable
family of finite index sets. Put

\[
U(\tau)
:=
\bigcup_{m\in\mathcal F(\tau)}Q_m,
\qquad
N(\tau):=|\mathcal F(\tau)|.
\tag{22}
\]

The convolution kernel \(L_K\) of \(H_h\) defines

\[
w_\tau(y)
:=
\int_{U(\tau)}|L_K(x-y)|\,dx.
\tag{23}
\]

The same kernel calculation as for a fixed grid union is pointwise in
time:

\[
\|w_\tau\|_\infty\le C_A,
\qquad
\|w_\tau\|_{L^{3,1}}
\le
C_A N(\tau)^{1/3}\ell.
\tag{24}
\]

Therefore

\[
\begin{aligned}
\int_0^h\int_{U(\tau)}|H_h|
&\le
C_A
\left(
\int_0^h\int|r^{\rm lo}|^2w_\tau
\right)^{1/2}\\
&\quad\times
\left(
\int_0^h\int|\nabla b^{\rm lo}|^2w_\tau
\right)^{1/2}.
\end{aligned}
\tag{25}
\]

The arbitrary-terminal-time feedback estimate gives

\[
\|r(\tau)\|_2^2\le C_r\tau^2.
\tag{26}
\]

Consequently the first factor squared in (25) is at most

\[
C\int_0^h\tau^2\,d\tau
\le Ch^3.
\tag{27}
\]

At each time, Lorentz--Bernstein and (24) give

\[
\begin{aligned}
\int|\nabla b^{\rm lo}|^2w_\tau
&\le
C
\|\nabla b^{\rm lo}\|_{L^{3,\infty}}^2
\|w_\tau\|_{L^{3,1}}\\
&\le
C K^2N(\tau)^{1/3}\ell\\
&=
C K N(\tau)^{1/3}.
\end{aligned}
\tag{28}
\]

Equations (25)--(28) prove the moving-grid capture law

\[
\boxed{
\int_0^h\int_{U(\tau)}|H_h|
\le
C_{\rm mov}h^{3/2}
\left(
K\int_0^hN(\tau)^{1/3}\,d\tau
\right)^{1/2}.
}
\tag{29}
\]

In particular, if \(N(\tau)\le N_*\) almost everywhere, then

\[
\boxed{
\int_0^h\int_{U(\tau)}|H_h|
\le
C_{\rm mov}h^{7/4}N_*^{1/6}.
}
\tag{30}
\]

This is the fixed-grid estimate with no penalty for moving the selected
set of cells in time. If a family is initially countable, truncate it in
space, use (29), and pass by monotone convergence. For every threshold
family below, define membership of \(m\) by taking the supremum of the
relevant continuous threshold function over the closed cube
\(\overline{Q_m}\). Smoothness of \(a_h\) makes each membership set Borel
in time; overcounting common cube boundaries is harmless. This applies to
the projected-polar set in Section 4, the rooted \(L^2\) set in Section 5,
and the rooted Orlicz set in Section 6.

## 4. Positive polar work forces \(\varepsilon_h\lesssim h^9\)

Choose the real even multiplier \(Q_K\) from the signed-aggregate theorem:
its symbol is one on the Fourier support of \(H_h\). Hence

\[
Q_KH_h=H_h,
\qquad
-\int_0^h\!\!\int
Q_K\zeta_h\cdot H_h
\ge p_{\rm pol}>0.
\tag{31}
\]

Also,

\[
p_{\rm pol}
\le
Z_h
:=
\int_0^h\int|H_h|
\le
C_{\rm pol}.
\tag{32}
\]

Let \(q_K(x)=K^3q(Kx)\) be the Schwartz kernel of \(Q_K\), and put

\[
C_Q:=\|q\|_1.
\tag{33}
\]

Since \(|\zeta_h|\le1\),

\[
\|Q_K\zeta_h\|_\infty\le C_Q.
\tag{34}
\]

Define

\[
\alpha_*:=\frac{p_{\rm pol}}{2C_{\rm pol}},
\qquad
G_h(\tau)
:=
\left\{
x:
|Q_K\zeta_h(\tau,x)|\ge\alpha_*
\right\}.
\tag{35}
\]

On the complement of \(G_h\), the absolute contribution to (31) is at
most \(\alpha_*Z_h\le p_{\rm pol}/2\). It follows from (31) and (34) that

\[
\boxed{
\int_0^h\int_{G_h(\tau)}|H_h|
\ge
\frac{p_{\rm pol}}{2C_Q}
=:
p_*.
}
\tag{36}
\]

Choose a fixed \(D\) so large that

\[
\int_{|y|>D}|q(y)|\,dy
\le\frac{\alpha_*}{2}.
\tag{37}
\]

If \(x\in G_h(\tau)\), the local part of the convolution satisfies

\[
\frac{\alpha_*}{2}
\le
\left|
\int_{|x-y|\le D\ell}
q_K(x-y)\zeta_h(\tau,y)\,dy
\right|.
\tag{38}
\]

Cauchy--Schwarz and
\(\|q_K\|_2=K^{3/2}\|q\|_2\) imply

\[
\boxed{
\int_{B_{D\ell}(x)}
|\zeta_h(\tau,y)|^2\,dy
\ge
c_{Q,D}\ell^3.
}
\tag{39}
\]

For each \(\tau\), let \(\mathcal F_\zeta(\tau)\) be the set of grid cubes
meeting \(G_h(\tau)\). Enlarge the neighbouring cube stencil by the fixed
amount required in (39). The enlarged stencils have bounded overlap, so
(18) and (39) give

\[
\boxed{
N_\zeta(\tau)
:=
|\mathcal F_\zeta(\tau)|
\le
C_{Q,D}K^3\|\zeta_h(\tau)\|_2^2
\le
\frac{C_{Q,D,\rho}K^3}{\varepsilon_h}.
}
\tag{40}
\]

Apply (29) to the moving union which covers \(G_h(\tau)\). Equations
(19), (36), and (40) yield

\[
\begin{aligned}
p_*
&\le
C h^{3/2}
\left(
K\int_0^h
\left(
\frac{K^3}{\varepsilon_h}
\right)^{1/3}
d\tau
\right)^{1/2}\\
&=
C h^{3/2}
\left(
hK^2\varepsilon_h^{-1/3}
\right)^{1/2}\\
&=
C h^2K\varepsilon_h^{-1/6}\\
&=
C_{\kappa}h^{3/2}\varepsilon_h^{-1/6}.
\end{aligned}
\tag{41}
\]

Therefore

\[
\boxed{
\varepsilon_h
\le
C_{\rm vac}h^9.
}
\tag{42}
\]

The same argument records the geometry behind the exponent. From (30)
and (36),

\[
\operatorname*{ess\,sup}_{0<\tau<h}N_\zeta(\tau)
\ge
c h^{-21/2}.
\tag{43}
\]

The upper bound in (40) can accommodate this only when

\[
\varepsilon_h^{-1}h^{-3/2}
\gtrsim
h^{-21/2},
\tag{44}
\]

which is exactly (42). Thus the charged polar must occupy, at some times,
the full descendant-cell power already forced by the finite-band pressure
cloud.

Equation (42) is an upper bound, not a matching lower bound. The selected
regularisation may still satisfy
\(\varepsilon_h/h^9\to0\).

## 5. The quadratic-scale rooted Oseen state is vacuum

The preceding conclusion can be seen directly at the state level. Put

\[
w_h:=a_h-\varphi.
\tag{45}
\]

The reviewed zero-data estimate gives

\[
\|w_h(\tau)\|_2\le F_\varphi\tau.
\tag{46}
\]

For a pressure-weighted point \((\tau,x)\), define the
quadratic-amplitude descendant-rooted state

\[
\mathsf W_{h,\tau,x}(y)
:=
h^{-2}w_h(\tau,x+\ell y).
\tag{47}
\]

Fix \(D>0\) and \(\delta>0\). At a fixed time, the number of grid cubes
which can meet

\[
\left\{
x:
\|\mathsf W_{h,\tau,x}\|_{L^2(B_D)}
>\delta
\right\}
\tag{48}
\]

is, by bounded overlap and (46), at most

\[
\begin{aligned}
N_{\delta,D}(\tau)
&\le
C_D
\frac{\|w_h(\tau)\|_2^2}
{\delta^2h^4\ell^3}\\
&\le
C_{\delta,D}
h^{-7/2}
\left(\frac{\tau}{h}\right)^2.
\end{aligned}
\tag{49}
\]

Apply the moving-grid estimate (29), retaining the time dependence in
(49). Since

\[
\int_0^hN_{\delta,D}(\tau)^{1/3}\,d\tau
\le
C_{\delta,D}h^{-1/6},
\tag{50}
\]

one obtains

\[
\boxed{
\frac1{Z_h}
\int_0^h\int
\mathbf1_{\{
\|\mathsf W_{h,\tau,x}\|_{L^2(B_D)}>\delta
\}}
|H_h(\tau,x)|\,dx\,d\tau
\le
C_{\delta,D}h^{7/6}.
}
\tag{51}
\]

Thus \(\mathsf W_{h,\tau,x}\to0\) in local \(L^2\), in probability under
the finite-band pressure law.

The fixed detector does not survive at these roots either. Let

\[
S_h:=h^{-2/3}.
\tag{52}
\]

The ball \(B_{S_h}\) meets at most \(Ch^{-7/2}\) descendant cubes.
The fixed-grid capture estimate gives

\[
\boxed{
\frac1{Z_h}
\int_0^h\int_{|x|\le S_h}|H_h|
\le Ch^{7/6}.
}
\tag{53}
\]

Outside \(B_{S_h}\), the Schwartz decay of \(\varphi\) gives, for every
fixed \(D\),

\[
\sup_{|x|>S_h}
\left\|
h^{-2}\varphi(x+\ell\,\cdot)
\right\|_{L^2(B_D)}
\longrightarrow0.
\tag{54}
\]

Combining (47), (51), (53), and (54) proves

\[
\boxed{
y\longmapsto h^{-2}a_h(\tau,x+\ell y)
\longrightarrow0
\quad\hbox{in local }L^2,
\quad\hbox{in finite-band pressure probability}.
}
\tag{55}
\]

By contrast, (31) says that the rooted effective polar

\[
\mathsf A_{h,\tau,x}(y)
:=
Q_K\zeta_h(\tau,x+\ell y)
\tag{56}
\]

has a positive limiting central alignment with the pressure direction.
Therefore (55) and (56) cannot pass to the limit through the ordinary
polar graph at quadratic amplitude. The nonzero mark lives at the vacuum
of the \(h^2\)-normalised Oseen state.

This does not rule out an Oseen balance after dividing \(a_h\) by the much
smaller selected amplitude \(\varepsilon_h\). It proves that such an
amplitude renormalisation is indispensable.

## 6. Balanced scale or strict amplitude cascade

Put

\[
\theta_h:=\frac{\varepsilon_h}{h^9}.
\tag{56a}
\]

Equation (42) gives \(\theta_h\le C\). The lower behaviour of
\(\theta_h\) now creates an exhaustive subsequence alternative.

To identify the balanced branch, define the dimensionless convex
integrand

\[
\Phi(z):=\sqrt{1+|z|^2}-1.
\tag{56b}
\]

Equation (13) is equivalent to

\[
\int_{\mathbb R^3}
\Phi\!\left(\frac{a_h(\tau,x)}{\varepsilon_h}\right)dx
\le
\frac{M_\rho}{\varepsilon_h}
\quad(0\le\tau\le h).
\tag{56c}
\]

For a fixed rooted radius \(D\), put

\[
\mathfrak O_{h,\tau,x}^{D}
:=
\int_{B_D}
\Phi\!\left(
\frac{a_h(\tau,x+\ell y)}{\varepsilon_h}
\right)dy.
\tag{56d}
\]

At each time, bounded overlap and (56c) show that the set where
\(\mathfrak O_{h,\tau,x}^{D}>L\) meets at most

\[
N_{L,D}(\tau)
\le
\frac{C_DK^3}{L\varepsilon_h}
\tag{56e}
\]

descendant cubes. Applying (30) and dividing by \(Z_h\ge p_{\rm pol}\)
gives

\[
\boxed{
\Gamma_h^{\rm fb}
\left\{
\mathfrak O_{h,\tau,x}^{D}>L
\right\}
\le
C_Dh^{3/2}\varepsilon_h^{-1/6}L^{-1/6}
=
C_D(\theta_hL)^{-1/6}.
}
\tag{56f}
\]

Consequently, if

\[
\liminf_{h\to0}\theta_h>0,
\tag{56g}
\]

the rooted Orlicz mass of \(a_h/\varepsilon_h\) is tight in finite-band
pressure probability. This is a boundedness statement, not strong
compactness.

The same normalisation is exactly the descendant Oseen normalisation.
For one root \(x\), set

\[
A_{h,x}(s,y)
:=
\frac{a_h(hs,x+\ell y)}{\varepsilon_h},
\qquad
B_{h,x}(s,y)
:=
\frac{h}{\ell}b_h(hs,x+\ell y),
\tag{56h}
\]

\[
\Pi_{h,x}(s,y)
:=
\frac{h}{\varepsilon_h\ell}
\pi_h^*(hs,x+\ell y).
\tag{56i}
\]

Then (1) becomes

\[
\boxed{
\partial_sA_{h,x}
-\nu\kappa^2\Delta_yA_{h,x}
-B_{h,x}\cdot\nabla_yA_{h,x}
+\nabla_y\Pi_{h,x}
=0.
}
\tag{56j}
\]

The drift remains critical:

\[
\|B_{h,x}(s)\|_{L^{3,\infty}_y}
\le
\frac{h}{\ell^2}M
=
\kappa^2M.
\tag{56k}
\]

A physical pressure-gradient component \(H_h\) appears in (56j) as

\[
\mathcal H_{h,x}(s,y)
:=
\frac{h}{\varepsilon_h}
H_h(hs,x+\ell y).
\tag{56l}
\]

Globally in descendant coordinates,

\[
\int_0^1\int_{\mathbb R^3}
|\mathcal H_{h,0}(s,y)|\,dy\,ds
=
\frac{Z_h}{\varepsilon_h\ell^3}.
\tag{56m}
\]

The inverse-cubic source ball contains

\[
N_{\rm src}
\asymp
\frac{h^{-9}}{\ell^3}
\asymp
h^{-21/2}
\tag{56m'}
\]

descendant cells. Since \(Z_h\asymp1\), the normalised pressure mass in
(56m), divided by \(N_{\rm src}\), is of order

\[
\frac{h^9}{\varepsilon_h}
=
\theta_h^{-1}.
\tag{56m''}
\]

Thus \(\theta_h\asymp1\) is precisely the scale at which the
amplitude-normalised Oseen pressure has order-one mass per source cell on
average. This does not assert cellwise equidistribution. After subsequence
selection, the finite-band branch has the exact fork

\[
\boxed{
\begin{array}{ll}
\liminf\theta_h>0:
&
\text{balanced amplitude and pressure-probability Orlicz tightness};
\\[2mm]
\theta_h\to0:
&
\text{strict sub-}h^9\text{ amplitude cascade.}
\end{array}
}
\tag{56n}
\]

The first line still lacks gradient and time compactness. The second line
has a diverging amplitude-normalised pressure scale and loses the tail
control in (56f). Neither line is excluded here.

## 7. A sharp kinematic source-volume carrier

The inverse-ninth power and the full cell count are sharp for the ledgers
used above. Set

\[
R_h:=h^{-3},
\qquad
K_h:=\kappa h^{-1/2},
\qquad
\varepsilon_h^{\rm mod}:=h^9.
\tag{57}
\]

Choose
\(\eta\in C_c^\infty(\mathbb R^3)\) which equals one on a nonempty ball,
fix translations \(y_h\), and define the exact solenoidal field

\[
V_h
:=
K_h^{-1}
\nabla\times
\left[
\eta\!\left(\frac{x-y_h}{R_h}\right)
\bigl(\cos(K_hx_1)-\cos(K_hx_2)\bigr)e_3
\right].
\tag{58}
\]

On the corresponding scaled plateau, its leading part is

\[
\bigl(\sin(K_hx_2),\sin(K_hx_1),0\bigr),
\tag{58a}
\]

which is divergence free. On that bulk region and a time plateau
\(\sigma_h=\sigma\ne0\), the corresponding polar has

\[
\operatorname{div}
\left[
\frac{\sigma
(\sin(K_hx_2),\sin(K_hx_1),0)}
{\sqrt{
1+\sigma^2(
\sin^2(K_hx_1)+\sin^2(K_hx_2)
)
}}
\right]
=
-\sigma^3K_h
\frac{
\sin(K_hx_1)\sin(K_hx_2)
(\cos(K_hx_1)+\cos(K_hx_2))
}{
\left[
1+\sigma^2(
\sin^2(K_hx_1)+\sin^2(K_hx_2)
)
\right]^{3/2}
}.
\tag{58b}
\]

It therefore has a nonzero gradient projection at a fixed harmonic
comparable to \(K_h\). The envelope error is

\[
O((K_hR_h)^{-1})=O(h^{7/2}).
\tag{59}
\]

Let \(\sigma_h:[0,h]\to[-1,1]\) be smooth, vanish on
\([0,h/3]\), obey \(\sigma_h(h)=1\), and spend a fixed fraction of the
layer on plateaux where \(|\sigma_h|\ge c_\sigma>0\); explicitly, require

\[
\left|
\left\{
\tau\in[0,h]:
|\sigma_h(\tau)|\ge c_\sigma
\right\}
\right|
\ge c_\sigma' h
\tag{59a}
\]

for fixed \(c_\sigma,c_\sigma'>0\). Put

\[
w_h^{\rm mod}(\tau,x)
:=
h^9\sigma_h(\tau)V_h(x).
\tag{60}
\]

The exact powers are

\[
\|w_h^{\rm mod}(\tau)\|_2^2
\lesssim h^9
\quad\hbox{for every }\tau,
\qquad
\|w_h^{\rm mod}(\tau)\|_2^2
\asymp h^9
\quad\hbox{when }|\sigma_h(\tau)|\ge c_\sigma,
\tag{61}
\]

\[
\int_0^h
\|\nabla w_h^{\rm mod}(\tau)\|_2^2\,d\tau
\asymp
h\cdot h^{18}K_h^2R_h^3
\asymp
h^9,
\tag{62}
\]

and, when \(|\sigma_h|\) is bounded below,

\[
L_{\varepsilon_h^{\rm mod}}
(w_h^{\rm mod})
\asymp
\varepsilon_h^{\rm mod}R_h^3
\asymp1.
\tag{63}
\]

The polar field has order-one frequency-\(K_h\) content throughout
volume \(R_h^3=h^{-9}\). Its descendant-cell count is

\[
\boxed{
R_h^3K_h^3
\asymp
h^{-21/2}.
}
\tag{64}
\]

The pressure-capture power can be saturated by an artificial annular
gradient mark as well. Let \(P_{K_h}^{\rm ann}\) be a smooth multiplier
with a real even symbol supported in symmetric neighbourhoods of one
nonzero gradient harmonic and its negative from the polar in (58a), and
let
\(\mathbb Q_\nabla=\nabla\Delta^{-1}\operatorname{div}\) be the
orthogonal gradient projection. On the part of the layer where
\(|\sigma_h|\) is bounded below, put

\[
H_h^{\rm mod}
:=
-h^8
P_{K_h}^{\rm ann}\mathbb Q_\nabla P_{K_h}^{\rm ann}
\zeta_{\varepsilon_h^{\rm mod}}(w_h^{\rm mod}).
\tag{64a}
\]

Then

\[
\int_0^h\int|H_h^{\rm mod}|
\asymp
h^8hR_h^3
\asymp1.
\tag{64b}
\]

The explicit bulk divergence in (58b), the chosen annular harmonic, and
the fact that the plateau contains \(\asymp R_h^3\) periodic volume give

\[
\left\|
\mathbb Q_\nabla
P_{K_h}^{\rm ann}
\zeta_{\varepsilon_h^{\rm mod}}(w_h^{\rm mod})
\right\|_2^2
\asymp R_h^3
\tag{64b.1}
\]

on every fixed-amplitude time plateau. Hence self-adjointness gives

\[
-\int_0^h\int
\zeta_{\varepsilon_h^{\rm mod}}(w_h^{\rm mod})
\cdot H_h^{\rm mod}
=
h^8
\int_0^h
\left\|
\mathbb Q_\nabla
P_{K_h}^{\rm ann}
\zeta_{\varepsilon_h^{\rm mod}}(w_h^{\rm mod})
\right\|_2^2\,d\tau
\asymp1.
\tag{64b'}
\]

One descendant cell carries at most \(Ch^{21/2}\) of this spacetime
mass. Hence a union of \(N\) cells carries

\[
\min\{1,CNh^{21/2}\}
\le
C h^{7/4}N^{1/6},
\tag{64c}
\]

with equality of powers at \(N\asymp h^{-21/2}\).

Moreover, on every fixed fraction of the layer where
\(|\sigma_h|\) stays away from zero,

\[
\int_0^h
\mathcal K_{\varepsilon_h^{\rm mod}}
(w_h^{\rm mod})\,d\tau
\asymp
h^9K_h^2R_h^3h
\asymp1.
\tag{65}
\]

Because \(\|w_h^{\rm mod}\|_2\lesssim h^{9/2}\), the pointwise
\(O(\tau)\) difference bound is easily respected after the initial
zero interval. The function \(\sigma_h\) may make arbitrarily many
fixed-amplitude sign changes before its final first hit; neither
(61), (62), nor the bounded mass in (63) sees their number.

This model is kinematic. It is not asserted to solve the Oseen equation,
to arise from one Navier--Stokes trajectory, or to realise
\(H_h^{\rm mod}\) through the pressure factorisation
\(\mathcal T(r^{\rm lo},b^{\rm lo})\).
It proves that the powers \(h^9\) and \(h^{-21/2}\), and the absence of a
temporal modulus, cannot be improved from first-hitting Kato mass,
quadratic energy, spatial band limitation, and finite-band capture alone.

## 8. Exact consequence and remaining gate

On a first-hitting terminal sequence, rerun the reviewed branch tree.
If it reaches the charged finite-band child, then:

1. the selected Kato regularisation satisfies
   \[
   \varepsilon_h\lesssim h^9;
   \]
2. the order-one effective polar must occupy the complete
   \(h^{-21/2}\) source-volume cell power at some times;
3. the \(h^2\)-normalised rooted adjoint state converges to zero in
   pressure probability;
4. the nonzero effective-polar law is therefore a vacuum decoration, not
   the polar graph of a nonzero quadratic-scale Oseen profile;
5. the selected amplitude is either balanced,
   \(\varepsilon_h\asymp h^9\), with rooted Orlicz tightness for
   \(a_h/\varepsilon_h\), or it enters a strict sub-\(h^9\) cascade.

This closes the direct proposal to obtain limiting Oseen rigidity by
combining the old \(h^2\) regularisation ceiling with the descendant
parabolic scale. It does not close ROUTE-R3B. In particular, it does not
prove:

- a lower bound \(\varepsilon_h\gtrsim h^9\);
- compactness of \(a_h/\varepsilon_h\);
- time compactness or bounded variation of the effective polar;
- an additive event functional or finite same-trajectory budget;
- exclusion of the high-coefficient, direct inverse-\(15/4\), exterior
  stretched-exponential, or signed late-annulus branches;
- regularity, breakdown, or any Clay alternative A--D.

The exact finite-band gate is now:

> Either compactify the amplitude-normalised adjoint
> \(a_h/\varepsilon_h\) and its Oseen balance, prove that a strict
> sub-\(h^9\) amplitude cascade pays a finite same-trajectory quantity,
> or construct a telescope which uses the first-hitting Kato mass without
> requiring continuity of the polar graph at zero.

Run the exact exponent ledger with:

```bash
make adjoint-pressure-polar-vacuum
```
