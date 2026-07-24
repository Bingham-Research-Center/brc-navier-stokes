# Annular pressure remainder localises to one heat time and scale zero

- **Experiment:** EXP-ADJOINT-PRESSURE-PARABOLIC-REGENERATION-001
- **Route:** ROUTE-R3B
- **Status:** conditional same-genealogy analytic reduction
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** [nonlinear regeneration](adjoint-pressure-nonlinear-regeneration.md),
  [annular pressure cost](adjoint-pressure-annular-cost.md), and
  [adjoint-pressure history](adjoint-pressure-history.md)
- **External review:** pending
- **Adversarial recomputation:** analytic core accepted after the scope and
  quantifier repairs recorded below

The preceding theorem showed that a non-summable annular
adjoint-pressure action cannot be a passive low-frequency cloud or a
direct remote linear inheritance. Its remaining nonlinear Duhamel
field, however, used one common look-back horizon for every spatial
shell. The present reduction replaces that horizon by one shell heat
time and removes every aggregate shell range staying at positive
physical radius.

Let \(R_k=L^kR_0\), \(L\ge16\), and retain the endpoint exterior-adjoint
tail

\[
\mathcal A_{n,k}(T)
:=
\left(
\int_0^T
\|a_{n,\psi}(\tau)\|_{L^2(|x|>2R_k)}^2\,d\tau
\right)^{1/2}
\le A_*R_k^{-1/2}.
\tag{1}
\]

For a radius \(R_k\), use exactly one heat time

\[
\ell_k:=\frac{R_k^2}{\nu}
\tag{2}
\]

and define the one-heat-time nonlinear Duhamel field

\[
\mathcal Q_{n,k}(\tau)
:=
-
\mathsf S_{>R_k^{-1}}
\int_0^{\ell_k}
e^{\nu s\Delta}
\mathbb P\operatorname{div}
\bigl(
b_n(\tau+s)\otimes b_n(\tau+s)
\bigr)\,ds.
\tag{3}
\]

Suppose the physical genealogy has zoom radii \(\rho_n\to0\) and

\[
\rho_n^2H_n\longrightarrow h_*>0.
\tag{4}
\]

Fix any physical cutoff \(r_\bullet\) satisfying

\[
0<r_\bullet<\sqrt{\nu h_*}.
\tag{5}
\]

For all large \(n\), every index with
\(\rho_nR_k\le r_\bullet\) admits the exact look-back (2).  Define

\[
\mathfrak Q_n(T;r_\bullet)
:=
\sum_{\rho_nR_k\le r_\bullet}
\mathcal A_{n,k}(T)
\left(
\int_0^T
\|\nabla\mathcal Q_{n,k}(\tau)\|_{L^2(\mathcal C_k)}^2\,d\tau
\right)^{1/2}.
\tag{6}
\]

Then the annular pressure history obeys

\[
\boxed{
\int_0^T
\|\nabla\pi^*_{n,\psi}(\tau)\|_1\,d\tau
\le
C_{\psi,M,A_*,\nu,T,R_0,L}
+
C\mathfrak Q_n(T;r_\bullet)
+
\varepsilon_n(r_\bullet),
}
\tag{7}
\]

Here \(\varepsilon_n(r_\bullet)\to0\) as \(n\to\infty\) for every
fixed \(r_\bullet>0\). It is the entire macroscopic annular remainder,
including both the coefficient-gradient and coefficient-cutoff actions
from shells whose base physical radius is at least \(r_\bullet\), up to
fixed annular constants.

Recall the fixed-window genealogy cost

\[
\mathfrak p^\mathcal G_{\psi,T}
:=
\liminf_{\substack{n\to\infty\\H_n\ge T}}
\frac1{\sqrt{\nu T}}
\int_0^T
\|\nabla\pi^*_{n,\psi}(\tau)\|_1\,d\tau.
\tag{7a}
\]

Consequently

\[
\liminf_{n\to\infty}\mathfrak Q_n(T;r_\bullet)<\infty
\quad\Longrightarrow\quad
\mathfrak p^\mathcal G_{\psi,T}<\infty.
\tag{8}
\]

The exact converse quantifier is: for every fixed admissible cutoff,

\[
\boxed{
\forall r_\bullet\in(0,\sqrt{\nu h_*}),\qquad
P_{n_j}(T)\longrightarrow\infty
\ \Longrightarrow\
\mathfrak Q_{n_j}(T;r_\bullet)\longrightarrow\infty,
}
\tag{8a}
\]

where

\[
P_n(T):=
\int_0^T\|\nabla\pi^*_{n,\psi}(\tau)\|_1\,d\tau.
\tag{8b}
\]

For any countable
\(r_m\in(0,\sqrt{\nu h_*})\) with \(r_m\downarrow0\), a further
subsequence can therefore choose \(n_{j_m}\uparrow\infty\) with
\(\mathfrak Q_{n_{j_m}}(T;r_m)\ge m\). This is an aggregate scale-zero
localisation of the upper-audit remainder. It is not an individual-shell
lower bound, a prescribed joint limit \(r_n\), or a cross-shell cascade.

The field (3) samples only one heat-time Duhamel integral. Earlier
history can still determine the coefficient fields inside that integral;
no causal independence from remote ancestry is proved. Nor does the
result bound (6), localise its nonlinear source spatially, give its sign,
separate event indices, exclude Zeno reuse, or prove any Clay
alternative.

## 1. Annular estimate and physical genealogy

Let

\[
\mathcal G=\{(u_n,H_n)\}_{n\ge1}
\tag{9}
\]

be the smooth finite-energy physical genealogy and put

\[
b_n(\tau)=u_n(-\tau),
\qquad
0\le\tau\le H_n.
\tag{10}
\]

Assume

\[
\sup_n\sup_{0\le\tau\le H_n}
\|b_n(\tau)\|_{L^{3,\infty}}
\le M.
\tag{11}
\]

The tail estimate (1) is assumed uniformly on the selected genealogy
diagonal. Any finitely many initial radii outside the asymptotic tail
range can be absorbed into \(A_*\) using adjoint \(L^2\) energy.

The annular theorem supplies enlarged coefficient annuli

\[
\mathcal C_k
\subset
B_{8R_{k+1}}\setminus B_{4R_k}
\tag{12}
\]

with bounded overlap and

\[
\begin{aligned}
\int_0^T\|\nabla\pi^*_{n,\psi}\|_1\,d\tau
\le{}&
C_{\rm in}\\
&+
C\sum_{k\ge0}
\mathcal A_{n,k}(T)
\bigg[
\left(
\int_0^T
\|\nabla b_n\|_{L^2(\mathcal C_k)}^2\,d\tau
\right)^{1/2}\\
&\hspace{41mm}
+M\left(\frac{T}{R_k}\right)^{1/2}
\bigg].
\end{aligned}
\tag{13}
\]

The cutoff part is already summable under (1):

\[
\sum_{k\ge0}
\mathcal A_{n,k}(T)
M\left(\frac{T}{R_k}\right)^{1/2}
\le
A_*M\sqrt T
\sum_{k\ge0}R_k^{-1}
<\infty.
\tag{14}
\]

Only the coefficient-gradient action remains.

For completeness, the physical outer profiles have the form

\[
V_n(y,s)
=
\frac{\rho_n}{\nu_{\rm phys}}
v\left(
x_n+\rho_ny,
T^*+\frac{\rho_n^2}{\nu_{\rm phys}}s
\right),
\tag{15}
\]

and the genealogy uses

\[
u_n(s)=V_n(s-\varepsilon_n),
\qquad
\varepsilon_n\longrightarrow0,
\qquad
H_n=\frac{\nu_{\rm phys}T^*}{2\rho_n^2}.
\tag{16}
\]

Thus (4) holds with

\[
h_*=\frac{\nu_{\rm phys}T^*}{2}.
\tag{17}
\]

The proof below uses only (4), the exact dissipation scaling in (15),
and absolute continuity of the original Leray dissipation.

## 2. One-heat-time inheritance is summable

Fix a smooth Littlewood--Paley low-pass
\(\mathsf S_{\le\kappa}\), with complementary multiplier
\(\mathsf S_{>\kappa}\) supported away from zero.  If

\[
\ell_k=\frac{R_k^2}{\nu}
\tag{18}
\]

and \(\tau+\ell_k\le H_n\), the exact forward Navier--Stokes mild
formula gives

\[
\boxed{
\mathsf S_{>R_k^{-1}}b_n(\tau)
=
\mathcal J_{n,k}(\tau)
+
\mathcal Q_{n,k}(\tau),
}
\tag{19}
\]

where

\[
\mathcal J_{n,k}(\tau)
:=
\mathsf S_{>R_k^{-1}}
e^{R_k^2\Delta}
b_n(\tau+\ell_k).
\tag{20}
\]

The multiplier in
\(\nabla\mathsf S_{>R_k^{-1}}e^{R_k^2\Delta}\) has a convolution
kernel with \(L^1\) norm \(CR_k^{-1}\).  Indeed, after the change
\(\zeta=R_k\xi\), its kernel is \(R_k^{-4}K(x/R_k)\) for one fixed
Schwartz function \(K\).  Lorentz multiplier boundedness and (11)
therefore give

\[
\|\nabla\mathcal J_{n,k}(\tau)\|_{L^{3,\infty}}
\le
CMR_k^{-1}.
\tag{21}
\]

Since \(|\mathcal C_k|\le C_LR_k^3\), finite-volume Lorentz embedding
gives

\[
\|\nabla\mathcal J_{n,k}(\tau)\|_{L^2(\mathcal C_k)}
\le
CMR_k^{-1/2}.
\tag{22}
\]

After time integration and multiplication by (1),

\[
\boxed{
\begin{aligned}
\sum_k
\mathcal A_{n,k}(T)
\left(
\int_0^T
\|\nabla\mathcal J_{n,k}\|_{L^2(\mathcal C_k)}^2\,d\tau
\right)^{1/2}
&\le
CA_*M\sqrt T
\sum_kR_k^{-1}\\
&<\infty,
\end{aligned}
}
\tag{23}
\]

for every collection of indices on which (18) is admissible.  Unlike
the remote-horizon estimate, this uses no global \(L^2\) energy.  One
local heat time is enough to turn the endpoint half-power into a
summable reciprocal-radius action.

The low-frequency field obeys the same bound.  Bernstein and
finite-volume Lorentz embedding give

\[
\|\nabla\mathsf S_{\le R_k^{-1}}b_n(\tau)\|_{L^2(\mathcal C_k)}
\le
CMR_k^{-1/2},
\tag{24}
\]

so its weighted shell sum is again bounded by the right side of (23).

## 3. Every sub-cutoff shell admits the one-heat-time formula

Fix \(r_\bullet\) as in (5).  From (4),

\[
\rho_n^2(H_n-T)\longrightarrow h_*.
\tag{25}
\]

Hence, for all sufficiently large \(n\),

\[
\frac{r_\bullet^2}{\nu}
<
\rho_n^2(H_n-T).
\tag{26}
\]

If \(\rho_nR_k\le r_\bullet\), then

\[
\ell_k
=
\frac{R_k^2}{\nu}
\le
\frac{r_\bullet^2}{\nu\rho_n^2}
<
H_n-T.
\tag{27}
\]

Thus \(\tau+\ell_k\le H_n\) for every \(0\le\tau\le T\), and (19)
holds simultaneously for every shell in (6).

In physical variables, (18) has duration

\[
\frac{\rho_n^2}{\nu_{\rm phys}}\ell_k
=
\frac{(\rho_nR_k)^2}{\nu\nu_{\rm phys}}.
\tag{28}
\]

The actual genealogy is unit-viscosity, so \(\nu=1\) there and this is
the natural physical heat time
\((\rho_nR_k)^2/\nu_{\rm phys}\).

## 4. Every fixed macroscopic shell range vanishes

Let

\[
D_{n,k}(T)
:=
\int_0^T
\|\nabla b_n(\tau)\|_{L^2(\mathcal C_k)}^2\,d\tau.
\tag{29}
\]

The interval \(0\le\tau\le T\) pulls back under (15)--(16) to

\[
I_n(T)
=
\left[
T^*-\frac{\rho_n^2}{\nu_{\rm phys}}(T+\varepsilon_n),
\,
T^*-\frac{\rho_n^2}{\nu_{\rm phys}}\varepsilon_n
\right],
\tag{30}
\]

whose length tends to zero.  Put

\[
\delta_{n,k}
:=
\int_{I_n(T)}
\int_{x_n+\rho_n\mathcal C_k}
|\nabla v(x,t)|^2\,dx\,dt.
\tag{31}
\]

The exact physical scaling is

\[
\boxed{
D_{n,k}(T)
=
\frac{1}{\nu_{\rm phys}\rho_n}
\delta_{n,k}.
}
\tag{32}
\]

Set \(r_{n,k}:=\rho_nR_k\).  Equations (1) and (32) give the critical
cancellation

\[
\mathcal A_{n,k}(T)D_{n,k}(T)^{1/2}
\le
\frac{A_*}{\sqrt{\nu_{\rm phys}}}
r_{n,k}^{-1/2}\delta_{n,k}^{1/2}.
\tag{33}
\]

The physical annuli \(x_n+\rho_n\mathcal C_k\) have overlap bounded
only by \(L\).  Therefore, for every fixed \(r_\bullet>0\),
Cauchy--Schwarz in shell index gives

\[
\begin{aligned}
&\sum_{r_{n,k}>r_\bullet}
\mathcal A_{n,k}(T)D_{n,k}(T)^{1/2}\\
&\qquad\le
\frac{CA_*}{\sqrt{\nu_{\rm phys}}}
\left(
\sum_{r_{n,k}>r_\bullet}r_{n,k}^{-1}
\right)^{1/2}
\left(
\int_{I_n(T)}
\|\nabla v(t)\|_2^2\,dt
\right)^{1/2}\\
&\qquad\le
\frac{CA_*}{\sqrt{\nu_{\rm phys}r_\bullet}}
\left(
\int_{I_n(T)}
\|\nabla v(t)\|_2^2\,dt
\right)^{1/2}.
\end{aligned}
\tag{34}
\]

Here

\[
\sum_{r_{n,k}>r_\bullet}r_{n,k}^{-1}
\le
\frac{1}{r_\bullet(1-L^{-1})}.
\tag{35}
\]

The original Leray energy inequality gives

\[
\|\nabla v\|_2^2\in L^1(0,T^*).
\tag{36}
\]

Because \(|I_n(T)|\to0\), absolute continuity of this fixed physical
integral gives

\[
\boxed{
\sum_{r_{n,k}>r_\bullet}
\mathcal A_{n,k}(T)D_{n,k}(T)^{1/2}
\longrightarrow0
}
\tag{37}
\]

for every fixed \(r_\bullet>0\).  This is stronger than merely
discarding shells beyond the genealogy horizon: every shell range that
stays at a positive physical radius disappears from the pressure audit.

The coefficient-cutoff term vanishes there as well:

\[
\begin{aligned}
\sum_{r_{n,k}>r_\bullet}
\mathcal A_{n,k}(T)
M\left(\frac{T}{R_k}\right)^{1/2}
&\le
A_*M\sqrt T
\sum_{r_{n,k}>r_\bullet}R_k^{-1}\\
&=
A_*M\sqrt T\,\rho_n
\sum_{r_{n,k}>r_\bullet}r_{n,k}^{-1}\\
&\le
\frac{CA_*M\sqrt T}{r_\bullet}\rho_n
\longrightarrow0.
\end{aligned}
\tag{37a}
\]

## 5. Proof of the aggregate scale-zero reduction

Split the coefficient-gradient sum in (13) according to

\[
\rho_nR_k\le r_\bullet
\quad\hbox{or}\quad
\rho_nR_k>r_\bullet.
\tag{38}
\]

The second part is \(o(1)\) by (37) and (37a).  On the first part, equations
(19) and (24) decompose

\[
b_n
=
\mathsf S_{\le R_k^{-1}}b_n
+
\mathcal J_{n,k}
+
\mathcal Q_{n,k}.
\tag{39}
\]

The weighted low-frequency and one-heat-time inherited actions are
uniformly finite by (23)--(24).  The coefficient-cutoff action is
uniformly finite by (14), and the compact inner coefficient is contained
in \(C_{\rm in}\).  The only remaining term is (6), proving (7).

If the lower limit of (6) is finite, take a subsequence realising it in
(7) to obtain (8).  If instead the left side of (7) tends to infinity
along a subsequence, every other term stays bounded or vanishes, so
\(\mathfrak Q_n(T;r_\bullet)\to\infty\) there.

Because \(r_\bullet\) can be any fixed number satisfying (5), such a
divergence survives after every fixed positive physical shell range is
removed. The diagonal following (8a) gives an aggregate scale-zero
witness. It supplies neither one distinguished shell nor directed
transfer between shells.

## 6. Exact route consequence

This theorem closes:

1. the need to use one common remote look-back horizon for all shells;
2. every full annular shell range staying at a positive
   physical radius;
3. direct one-heat-time linear inheritance as a non-summable
   high-frequency action, without global energy;
4. the possibility that the endpoint annular obstruction is merely a
   macroscopic far-field cloud; and
5. a precise one-heat-time aggregate criterion for finite genealogy
   pressure cost.

It does not prove:

1. finiteness of the one-heat-time action (6);
2. an individual shell or block carrying a fixed charge;
3. cross-shell transfer or a directed cascade;
4. causal independence from history before the displayed heat time;
5. spatial localisation of the nonlinear source in (3);
6. a positive sign, flux charge, or event-index freshness;
7. a non-Zeno speed bound or exclusion of the coherent ancient profile;
8. regularity, breakdown, or any Clay alternative A--D.

The next target has now been resolved as an exact reduction in
[spatial high-pass payer](adjoint-pressure-spatial-highpass-payer.md).
Its local filtered-energy identity leaves divergent entrance-energy or
positive-work square-root aggregates.  Its abstract endpoint-weighted
scalar arrays show that bare physical quadratic budgets still permit
diffuse blocks; they are not NSE or adjoint realisations.  The remaining
target is therefore an NSE-specific non-diffusion, active-block,
coherence, ancestry, or cross-event telescoping theorem.

The horizon, reciprocal-shell, physical scaling, and macroscopic
Cauchy--Schwarz ledgers are checked in
`lab/navier_lab/adjoint_pressure_parabolic_regeneration.py` and
`lab/tests/test_adjoint_pressure_parabolic_regeneration.py`.
