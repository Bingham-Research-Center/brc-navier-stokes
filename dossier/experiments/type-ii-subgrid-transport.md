# Terminal Type-II trace defect has an exact signed subgrid ancestry

- **Experiment:** EXP-TYPE-II-SUBGRID-TRANSPORT-001
- **Route:** ROUTE-R3C
- **Status:** complete analytic reduction with sharp shell-ledger survivor
- **Clay status:** unsolved

This note continues the
[carrier-defect theorem](type-ii-carrier-defect-compactness.md). It treats
the energy-efficient branch in which the retained terminal layer survives as
a positive trace-defect measure. The coherent nonzero weak-trace branch and
the energy-vanishing branch remain separate.

## Verdict

A terminal trace defect is not merely an abstract failure of strong
\(L^2_{\mathrm{loc}}\) convergence. It is exactly the vanishing-filter limit
of a nonnegative subgrid-energy density. For every fixed backward carrier
time, the smooth Navier--Stokes local energy equality transports that density
by an exact signed identity.

After choosing a diagonal filter length \(\ell_j\downarrow0\), every positive
terminal trace defect has at least one of three ancestors:

1. positive subgrid energy already present one fixed carrier time earlier;
2. positive **signed** nonlinear energy transfer into the subgrid scales; or
3. positive spatial import of subgrid energy through the carrier cutoff.

The normalised viscous subgrid loss and its cutoff error vanish. Under the
exact carrier pullback, a fixed nonlinear-transfer or spatial-import term is
an order-\(b_j\asymp e_j\) physical energy transfer, not the vanishing
\(b_j\tau_j\) spacetime mass left by the previous theorem. Since
\(b_j\ge c>0\), this is a genuine fixed physical floor.

It is still not automatically a non-reusable charge. An exact dissipative
shell ledger below moves one surviving energy packet through infinitely many
increasing frequency boundaries on disjoint intervals. Every signed boundary
flux has a fixed lower bound, the total viscous loss is finite, and its
terminal tail tends to zero. The model is not an NSE solution, but it proves
that energy equality, signed flux, scale ordering, disjoint time intervals,
and terminal absolute continuity alone cannot sum the event floors. The next
theorem must use the actual NSE flux geometry to force residence, freshness,
or a return to a controlled critical class.

## 1. Carrier and filter notation

Let \(v_j\) be the energy-efficient carrier sequence, with

\[
\partial_sv_j+\nabla\!\cdot(v_j\otimes v_j)+\nabla q_j
=\varepsilon_j\Delta v_j,
\qquad
\nabla\!\cdot v_j=0,
\]

\[
\varepsilon_j\longrightarrow0,
\qquad
\sup_{j,s}\|v_j(s)\|_2^2\le M,
\qquad
b_j=a_j^2R_j^3\ge c_b>0.
\]

The exact one-trajectory pullback also gives the clock-uniform fact

\[
\varepsilon_j
\int_0^{H_j}\!\!\int|\nabla v_j|^2\,dy\,ds
\longrightarrow0,
\]

including when \(H_j\to\infty\). Thus none of the forward-clock cells can
hide a total normalised viscous loss after the selected time.

Fix a nonnegative even function

\[
G\in C_c^\infty(\mathbb R^3),
\qquad
\int_{\mathbb R^3}G\,dy=1,
\]

and write

\[
G_\ell(y):=\ell^{-3}G(y/\ell),
\qquad
\overline f_\ell:=G_\ell*f.
\]

For one smooth field \(v\), define the subgrid stress, energy, viscous
variance, and signed nonlinear flux by

\[
\tau_{\ell,ij}(v,v)
:=
\overline{v_iv_j}_\ell-\overline v_{\ell,i}\overline v_{\ell,j},
\]

\[
k_\ell[v]
:=
\frac12\operatorname{tr}\tau_\ell(v,v)
=
\frac12\left(
\overline{|v|^2}_\ell-|\overline v_\ell|^2
\right),
\]

\[
d_\ell[v]
:=
\overline{|\nabla v|^2}_\ell
-|\nabla\overline v_\ell|^2,
\]

\[
\Pi_\ell[v]
:=
-\tau_{\ell,ij}(v,v)
\partial_j\overline v_{\ell,i}.
\]

Jensen's inequality gives the pointwise signs

\[
k_\ell[v]\ge0,
\qquad
d_\ell[v]\ge0.
\]

Put

\[
E(v):=\frac12|v|^2,
\qquad
\overline E^{\,r}_\ell
:=
\frac12|\overline v_\ell|^2.
\]

The inviscid spatial subgrid-energy flux is the vector with components

\[
\mathcal J^0_{\ell,j}[v,q]
:=
\overline{(E(v)+q)v_j}_\ell
-
\bigl(\overline E^{\,r}_\ell+\overline q_\ell\bigr)
\overline v_{\ell,j}
-
\overline v_{\ell,i}\tau_{\ell,ij}(v,v).
\]

The superscript \(0\) records that the viscous diffusion
\(-\varepsilon\nabla k_\ell\) has not been folded into this spatial flux.

## 2. Exact subgrid-energy balance

### Theorem 1: local signed transport identity

Every smooth finite-energy Navier--Stokes solution with viscosity
\(\varepsilon>0\) satisfies

\[
\boxed{
\partial_s k_\ell
+\nabla\!\cdot\mathcal J^0_\ell
=
\Pi_\ell
-\varepsilon d_\ell
+\varepsilon\Delta k_\ell.
}
\]

Let \(0\le\chi\in C_c^\infty(\mathbb R^3)\), and set

\[
K_{\ell,\chi}(s)
:=
\int_{\mathbb R^3}\chi k_\ell(s)\,dy.
\]

For every \([s_1,s_2]\) in the smooth lifespan,

\[
\boxed{
\begin{aligned}
K_{\ell,\chi}(s_2)-K_{\ell,\chi}(s_1)
={}&
\int_{s_1}^{s_2}\!\!\int\chi\Pi_\ell\,dy\,ds\\
&+
\int_{s_1}^{s_2}\!\!\int
\mathcal J^0_\ell\cdot\nabla\chi\,dy\,ds\\
&-
\varepsilon
\int_{s_1}^{s_2}\!\!\int\chi d_\ell\,dy\,ds\\
&+
\varepsilon
\int_{s_1}^{s_2}\!\!\int k_\ell\Delta\chi\,dy\,ds.
\end{aligned}
}
\]

The first term is the signed transfer from resolved to subgrid scales inside
the cutoff. The second is signed spatial import through the cutoff region.
Neither has been replaced by its absolute value.

### Proof

The smooth local energy equality is

\[
\partial_sE(v)
+\nabla\!\cdot\bigl((E(v)+q)v\bigr)
=
\varepsilon\Delta E(v)
-\varepsilon|\nabla v|^2.
\]

Filtering gives

\[
\partial_s\overline{E(v)}_\ell
+\nabla\!\cdot\overline{(E(v)+q)v}_\ell
=
\varepsilon\Delta\overline{E(v)}_\ell
-\varepsilon\overline{|\nabla v|^2}_\ell.
\]

The filtered momentum equation is

\[
\partial_s\overline v_\ell
+\nabla\!\cdot
\bigl(\overline v_\ell\otimes\overline v_\ell+\tau_\ell\bigr)
+\nabla\overline q_\ell
=
\varepsilon\Delta\overline v_\ell.
\]

Taking its scalar product with \(\overline v_\ell\) yields

\[
\begin{aligned}
\partial_s\overline E^{\,r}_\ell
&+
\nabla\!\cdot
\left[
\bigl(\overline E^{\,r}_\ell+\overline q_\ell\bigr)
\overline v_\ell
+
\bigl(\overline v_{\ell,i}\tau_{\ell,ij}\bigr)_{j=1}^3
\right]\\
&=
-\Pi_\ell
+\varepsilon\Delta\overline E^{\,r}_\ell
-\varepsilon|\nabla\overline v_\ell|^2.
\end{aligned}
\]

Subtracting this identity from the filtered local energy equality gives the
pointwise subgrid balance. Multiplication by \(\chi\), integration in space
and time, and two integrations by parts give the cutoff identity.

## 3. The terminal trace defect is the zero-filter subgrid energy

At the selected time, recall

\[
v_j(0)\otimes v_j(0)\,dy
\stackrel{*}{\rightharpoonup}
V(0)\otimes V(0)\,dy+\mathcal R_0,
\qquad
\mathcal T_0:=\operatorname{tr}\mathcal R_0\ge0.
\]

### Theorem 2: exact recovery of the trace defect

For every fixed \(\ell>0\) and
\(\chi\in C_c^\infty(\mathbb R^3)\),

\[
\lim_{j\to\infty}
K_{j,\ell,\chi}(0)
=
\int\chi k_\ell^0\,dy,
\]

where

\[
k_\ell^0
:=
\frac12G_\ell*
\bigl(|V(0)|^2\,dy+\mathcal T_0\bigr)
-
\frac12|G_\ell*V(0)|^2.
\]

Moreover,

\[
\boxed{
\lim_{\ell\downarrow0}\lim_{j\to\infty}
K_{j,\ell,\chi}(0)
=
\frac12\int\chi\,d\mathcal T_0.
}
\]

Thus \(\mathcal T_0\) is exactly twice the iterated zero-filter limit of the
nonnegative terminal subgrid energy.

### Proof

For fixed \(\ell\), terminal weak \(L^2\) convergence gives

\[
G_\ell*v_j(0)\longrightarrow G_\ell*V(0)
\]

strongly on compact sets. Convolution of the terminal tensor-measure limit
and taking the trace gives

\[
G_\ell*|v_j(0)|^2
\longrightarrow
G_\ell*\bigl(|V(0)|^2\,dy+\mathcal T_0\bigr)
\]

against compactly supported tests. This proves the first limit.

As \(\ell\downarrow0\), the approximate-identity theorem gives

\[
G_\ell*V(0)\to V(0)\quad\hbox{in }L^2,
\]

\[
G_\ell*|V(0)|^2\to|V(0)|^2
\quad\hbox{in }L^1,
\]

while \(G_\ell*\mathcal T_0\,dy\) converges weakly as measures to
\(\mathcal T_0\). The coherent \(V(0)\) variance therefore vanishes and only
half the trace-defect measure remains.

## 4. Exact one-trajectory ancestry trichotomy

Assume

\[
\Delta_\chi
:=
\int\chi\,d\mathcal T_0>0.
\]

Theorem 2 and a diagonal extraction give
\(\ell_j\downarrow0\) such that

\[
K_{j,\ell_j,\chi}(0)
\longrightarrow
\frac{\Delta_\chi}{2}.
\]

Fix \(S>0\). The carrier past is arbitrarily long, so
\([-S,0]\subset I_j\) eventually. Define

\[
\mathsf K_j^-:=K_{j,\ell_j,\chi}(-S),
\]

\[
\mathsf P_j
:=
\int_{-S}^{0}\!\!\int
\chi\Pi_{\ell_j}[v_j]\,dy\,ds,
\]

\[
\mathsf X_j
:=
\int_{-S}^{0}\!\!\int
\mathcal J^0_{\ell_j}[v_j,q_j]\cdot\nabla\chi\,dy\,ds,
\]

\[
\mathsf D_j
:=
\varepsilon_j
\int_{-S}^{0}\!\!\int
\chi d_{\ell_j}[v_j]\,dy\,ds,
\]

\[
\mathsf C_j
:=
\varepsilon_j
\int_{-S}^{0}\!\!\int
k_{\ell_j}[v_j]\Delta\chi\,dy\,ds.
\]

### Theorem 3: persistence, signed cascade, or spatial import

The exact identity is

\[
\boxed{
\mathsf K_j^-
+\mathsf P_j
+\mathsf X_j
=
K_{j,\ell_j,\chi}(0)
+\mathsf D_j
-\mathsf C_j.
}
\]

Furthermore,

\[
\mathsf D_j\longrightarrow0,
\qquad
\mathsf C_j\longrightarrow0,
\]

and therefore

\[
\boxed{
\limsup_{j\to\infty}
\max\{\mathsf K_j^-,\mathsf P_j,\mathsf X_j\}
\ge
\frac{\Delta_\chi}{6}.
}
\]

After a subsequence, at least one of the following occurs:

1. **Inherited microstructure:** the nonnegative subgrid energy
   \(\mathsf K_j^-\) has a fixed lower bound one carrier time earlier.
2. **Positive signed cascade:** the net nonlinear transfer
   \(\mathsf P_j\), with its sign retained, has a fixed positive lower bound.
3. **Positive spatial import:** the net subgrid-energy flux
   \(\mathsf X_j\) through the support of \(\nabla\chi\) has a fixed positive
   lower bound. Backwards in time, the terminal carrier originated outside
   the smaller cutoff.

### Proof

The cutoff identity in Theorem 1 gives the displayed equality. Since
\(0\le\chi\le1\), Jensen's inequality and Fubini give

\[
0\le\mathsf D_j
\le
\varepsilon_j
\int_{-S}^{0}\!\!\int|\nabla v_j|^2\,dy\,ds
\longrightarrow0
\]

by terminal dissipation collapse.

Also

\[
\int_{\mathbb R^3}k_{\ell_j}[v_j(\cdot,s)]\,dy
\le
\frac12\|v_j(s)\|_2^2
\le\frac M2.
\]

Hence

\[
|\mathsf C_j|
\le
\frac12\varepsilon_jSM\|\Delta\chi\|_\infty
\longrightarrow0.
\]

The sum on the left consequently has lower limit at least
\(\Delta_\chi/2\). The maximum of three real numbers is at least one third
of their sum, which proves the trichotomy without taking absolute values of
either flux.

## 5. Exact pullback to the physical trajectory

Let

\[
r_j:=R_j\ell_j,
\qquad
\chi_j(x):=\chi\!\left(\frac{x-x_j}{R_j}\right).
\]

Use the same filter \(G\) at physical length \(r_j\). Under

\[
u(x,t)=a_jv_j(y,s),
\qquad
x=x_j+R_jy,
\qquad
t=t_j+\tau_js,
\]

the subgrid quantities obey

\[
k_{r_j}[u]=a_j^2k_{\ell_j}[v_j],
\qquad
\Pi_{r_j}[u]=\frac{a_j^3}{R_j}\Pi_{\ell_j}[v_j],
\]

\[
\mathcal J^0_{r_j}[u,p]
=a_j^3\mathcal J^0_{\ell_j}[v_j,q_j],
\qquad
d_{r_j}[u]
=\frac{a_j^2}{R_j^2}d_{\ell_j}[v_j].
\]

Because \(\tau_j=R_j/a_j\), every term in the integrated identity has the
same exact energy factor \(b_j=a_j^2R_j^3\):

\[
\int\chi_j k_{r_j}[u(\cdot,t_j)]\,dx
=
b_jK_{j,\ell_j,\chi}(0),
\]

\[
\int_{t_j-S\tau_j}^{t_j}\!\!\int
\chi_j\Pi_{r_j}[u]\,dx\,dt
=
b_j\mathsf P_j,
\]

\[
\int_{t_j-S\tau_j}^{t_j}\!\!\int
\mathcal J^0_{r_j}[u,p]\cdot\nabla\chi_j\,dx\,dt
=
b_j\mathsf X_j,
\]

with the same factor for the viscous subgrid loss and cutoff correction.

Since \(b_j\ge c_b\), either flux branch supplies the fixed physical floor

\[
\limsup_j
\max\{b_j\mathsf P_j,b_j\mathsf X_j\}
\ge
\frac{c_b\Delta_\chi}{6}
\]

unless the inherited-energy branch occurs. This transfer takes place on the
shrinking physical interval

\[
[t_j-S\tau_j,t_j].
\]

Because \(t_j-S\tau_j\to T^*\), these fixed-carrier-time intervals can be
made pairwise disjoint by a further subsequence. Disjointness in time,
however, does not make transfers across different filter scales additive.

## 6. Sharp non-reuse obstruction: one packet crosses every shell

The following exact scalar ledger tests precisely the remaining inference.
It is a dissipative frequency-shell model, not a Navier--Stokes solution.

Let

\[
\kappa_n:=2^n,
\qquad
\delta_n:=\nu^{-1}2^{-4n},
\qquad
T_n:=\sum_{m<n}\delta_m,
\qquad
T_\infty:=\sum_{m\ge1}\delta_m<\infty.
\]

Choose a smooth nondecreasing
\(\alpha:[0,1]\to[0,1]\), constant near both endpoints, with
\(\alpha(0)=0\) and \(\alpha(1)=1\).

At time \(T_n\), put energy \(M_n>0\) in shell \(n\). On
\(I_n=[T_n,T_{n+1}]\), set

\[
\theta:=\frac{t-T_n}{\delta_n},
\]

\[
E_n(t)
:=
M_n(1-\alpha(\theta))
e^{-2\nu\kappa_n^2(t-T_n)},
\]

\[
F_n(t)
:=
\frac{M_n}{\delta_n}\alpha'(\theta)
e^{-2\nu\kappa_n^2(t-T_n)}
\ge0,
\]

and let the next-shell energy solve

\[
\dot E_{n+1}
+2\nu\kappa_{n+1}^2E_{n+1}
=F_n,
\qquad
E_{n+1}(T_n)=0.
\]

Then

\[
\dot E_n+2\nu\kappa_n^2E_n=-F_n,
\]

so this is an exact adjacent-shell energy balance with positive signed
forward flux. Put

\[
M_{n+1}:=E_{n+1}(T_{n+1}).
\]

The two heat factors give

\[
M_{n+1}
\ge
M_n
\exp\left[
-2\nu(\kappa_n^2+\kappa_{n+1}^2)\delta_n
\right].
\]

But

\[
\sum_{n\ge1}
\nu(\kappa_n^2+\kappa_{n+1}^2)\delta_n
=
5\sum_{n\ge1}2^{-2n}
<\infty.
\]

Therefore

\[
\inf_nM_n=:M_\infty>0,
\]

and every boundary receives a fixed positive signed flux:

\[
\int_{I_n}F_n(t)\,dt
\ge
M_n e^{-2\nu\kappa_n^2\delta_n}
\ge c_\nu M_\infty>0.
\]

On the other hand, summing the exact two-shell energy balances gives

\[
\sum_{n\ge1}
2\nu\int_{I_n}
\left(
\kappa_n^2E_n+\kappa_{n+1}^2E_{n+1}
\right)\,dt
=
M_1-M_\infty
<\infty.
\]

The dissipation remaining after shell \(N\) is \(M_N-M_\infty\to0\).
Thus the ledger has all of the following simultaneously:

1. pairwise disjoint time intervals accumulating at \(T_\infty\);
2. strictly increasing adjacent frequency boundaries;
3. a uniform positive signed flux through every boundary;
4. finite total viscous dissipation and vanishing terminal dissipation tail;
5. positive energy \(M_\infty\) escaping to infinite shell index.

The same energy packet pays every flux floor. No estimate based only on the
listed ledgers can sum those floors against total energy or dissipation.

## 7. Route consequence

For the terminal-microstructure branch, the vague phrase “trace loss” has
now been replaced by an exact one-trajectory signed trichotomy and an exact
physical scaling:

\[
\boxed{
\text{inherited subgrid energy}
\quad\text{or}\quad
\text{fixed positive nonlinear transfer}
\quad\text{or}\quad
\text{fixed positive spatial import}.
}
\]

The shell survivor shows why this is not yet a contradiction. A closing
theorem must add at least one genuinely NSE-specific statement:

1. a residence theorem forcing a fixed fraction of transferred energy to
   remain at the new scale long enough to pay a nonsummable viscous action;
2. a freshness theorem assigning successive transfers to disjoint physical
   energy, pressure, or enstrophy reservoirs rather than merely disjoint
   times and filter boundaries;
3. a one-trajectory spatial-ancestry theorem preventing repeated import
   through moving carrier cutoffs; or
4. a critical-return theorem showing that an indefinitely accelerating
   subgrid cascade restores a controlled endpoint class.

The coherent \(V(0)\ne0\) branch still needs propagation and ancient-Euler
rigidity. The energy-vanishing nine cells still need a separate normalisation
or charge. No alternative A--D of the Clay problem is proved.
