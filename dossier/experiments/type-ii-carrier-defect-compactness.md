# Energy-efficient Type-II carriers lose viscosity before they gain compactness

- **Experiment:** EXP-TYPE-II-CARRIER-DEFECT-001
- **Route:** ROUTE-R3C
- **Status:** complete analytic reduction with exact equation-family survivor
- **Clay status:** unsolved

This note continues the
[Type-II entrance theorem](type-ii-inviscid-carrier-entrance.md) for the
unforced whole-space equation. It treats the energy-efficient carrier branch
and distinguishes deductions from one physical Navier--Stokes trajectory from
properties of arbitrary vanishing-viscosity equation families.

## Verdict

The actual carrier equation gives more compactness than a bare weak
space-time subsequence, but much less than strong \(L^2_{\mathrm{loc}}\).
Uniform global energy implies

\[
v_j\longrightarrow V
\quad\hbox{strongly in}\quad
C_{\mathrm{loc}}\bigl(H^{-r}_{\mathrm{loc}}\bigr)
\quad\hbox{for every }r>0,
\]

and the quadratic flux converges to an Euler--Reynolds object

\[
\partial_sV+
\mathbb P\nabla\!\cdot
\bigl(V\otimes V+\mathcal R\bigr)=0,
\qquad
\mathcal R\ge0.
\]

Here \(\mathcal R\) is a positive-semidefinite matrix-valued measure. Its
trace is exactly the local \(L^2\) compactness defect. At the selected time
there is a separate positive-semidefinite tensor defect \(\mathcal R_0\),
which may vanish. In every partial or tight carrier-geometry branch,

\[
\int_{B_K}|V(0)|^2\,dy
+\operatorname{tr}\mathcal R_0(B_K)>0
\]

for some fixed \(K\). Thus the selected carrier cannot disappear without
leaving either a nonzero weak trace or a positive trace defect.

There is also a favourable one-trajectory fact. In the energy-efficient
branch the normalised viscous dissipation on every fixed carrier-time
interval tends to zero. The physical interval shrinks to \(T^*\), while the
normalising layer energy stays bounded below, so terminal absolute
continuity of the Leray dissipation applies. Consequently anomalous viscous
dissipation is not a surviving defect in any of the nine energy-efficient
geometry--clock cells.

This still does not give strong compactness. Using Gavrilov's peer-reviewed
compactly supported smooth steady Euler flow, one can pack finer disjoint
copies and then take a diagonal vanishing-viscosity approximation. The result
is a family of exact smooth Navier--Stokes carrier equations with bounded
energy, vanishing normalised dissipation, any diffuse/partial/tight geometry,
and any prescribed shrinking, finite, or expanding forward observation
window. In the tight branch

\[
v_j\rightharpoonup0,
\qquad
v_j\otimes v_j
\stackrel{*}{\rightharpoonup}
c\,\mathbf1_Q I,
\qquad c>0.
\]

The isotropic stress is absorbed into pressure, so the velocity limit is the
zero Euler solution although a positive energy defect remains. These exact
families are smoothly extendible beyond the chosen observation endpoint and
are not rescalings of one candidate blow-up trajectory. They therefore test
local equation, energy, geometry, and interval-length arguments, but do not
realise the first-singular-time meaning of the R3C clock. The next theorem
must use common physical ancestry or terminal nonextendibility.

## 1. Carrier notation

Let

\[
b_j:=a_j^2R_j^3,
\qquad
\tau_j:=\frac{R_j}{a_j},
\qquad
\varepsilon_j:=\frac{\nu}{a_jR_j}.
\]

The amplitude-layer inequalities give the exact comparison

\[
b_j\le e_j\le4b_j.
\]

The carrier fields solve

\[
\partial_sv_j+
\mathbb P\nabla\!\cdot(v_j\otimes v_j)
=\varepsilon_j\Delta v_j
\]

on

\[
I_j=\left(-\frac{t_j}{\tau_j},H_j\right),
\qquad
\frac{t_j}{\tau_j}\longrightarrow\infty,
\qquad
H_j\longrightarrow H\in[0,\infty].
\]

In the energy-efficient branch,

\[
\sup_j\frac{E_0}{e_j}<\infty.
\]

Hence for some \(c_0>0\),

\[
e_j\ge c_0,
\qquad
b_j\ge\frac{c_0}{4},
\qquad
\sup_{j,s\in I_j}\|v_j(s)\|_2^2
\le\frac{4E_0}{c_0}
=:M.
\]

All convergence below is understood after one diagonal subsequence on compact
subintervals of

\[
I=(-\infty,H).
\]

When \(H=0\), uniform negative-Sobolev equicontinuity extends the limiting
field to \(s=0\). A separate weak \(L^2\) extraction of \(v_j(0)\) has that
same distributional limit, so the notation \(V(0)\) below is unambiguous.

## 2. Maximal compactness supplied by the equation

### Theorem 1: negative-Sobolev compactness and Euler--Reynolds limit

Let \(\varepsilon_j\to0\), let \(I_j\) exhaust \(I\) on compact subsets, and
suppose smooth divergence-free solutions satisfy

\[
\sup_{j,s\in I_j}\|v_j(s)\|_2^2\le M.
\]

Then, after a subsequence, there are

\[
V\in L^\infty_{\mathrm{loc}}(I;L^2(\mathbb R^3))
\]

and a positive-semidefinite symmetric matrix-valued Radon measure
\(\mathcal R\) on \(I\times\mathbb R^3\) such that

\[
v_j\rightharpoonup^*V
\quad\hbox{in}\quad
L^\infty_{\mathrm{loc}}(I;L^2),
\]

\[
v_j\longrightarrow V
\quad\hbox{in}\quad
C_{\mathrm{loc}}\bigl(I;H^{-r}_{\mathrm{loc}}(\mathbb R^3)\bigr)
\quad\hbox{for every }r>0,
\]

and

\[
v_j\otimes v_j
\stackrel{*}{\rightharpoonup}
V\otimes V\,dy\,ds+\mathcal R
\]

as matrix-valued measures locally in space-time. The limit obeys

\[
\boxed{
\partial_sV+
\mathbb P\nabla\!\cdot
\bigl(V\otimes V+\mathcal R\bigr)=0.
}
\]

Equivalently, for some scalar distribution \(Q\),

\[
\partial_sV+
\nabla\!\cdot
\bigl(V\otimes V+\mathcal R\bigr)
+\nabla Q=0,
\qquad
\nabla\!\cdot V=0.
\]

For every nonnegative test function \(\zeta\) and every
\(\xi\in\mathbb R^3\),

\[
\int\zeta\,\xi^\mathsf T\,d\mathcal R\,\xi\ge0.
\]

In particular, \(\mathcal R=0\) on a cylinder if and only if
\(v_j\to V\) strongly in local \(L^2\) on compact subcylinders.

### Proof

Fix \(m>5/2\). The projected equation and Sobolev embedding give

\[
\begin{aligned}
\|\partial_sv_j\|_{H^{-m}}
&\le
\|\mathbb P\nabla\!\cdot(v_j\otimes v_j)\|_{H^{-m}}
+\varepsilon_j\|\Delta v_j\|_{H^{-m}}\\
&\le
C_m\|v_j\otimes v_j\|_1
+C_m\varepsilon_j\|v_j\|_2\\
&\le C_m(M+\sqrt M)
\end{aligned}
\]

eventually. Thus the fields are uniformly Lipschitz in \(H^{-m}\). On every
fixed ball, \(L^2\) embeds compactly into \(H^{-r}\) for every \(r>0\).
Interpolation between the uniform \(L^2\) bound and the \(H^{-m}\)
equicontinuity, followed by Arzelà--Ascoli and a diagonal argument, gives the
stated strong negative-Sobolev convergence.

The tensors \(v_j\otimes v_j\) are bounded in local finite measures, so they
have a weak-star limit \(\mathsf M\). Put

\[
\mathcal R:=\mathsf M-V\otimes V\,dy\,ds.
\]

For \(\zeta\ge0\), the sequence
\(\sqrt\zeta\,\xi\cdot v_j\) converges weakly to
\(\sqrt\zeta\,\xi\cdot V\) in \(L^2\). Weak lower semicontinuity gives

\[
\int\zeta|\xi\cdot V|^2
\le
\lim_j\int\zeta|\xi\cdot v_j|^2,
\]

which is precisely positivity of \(\mathcal R\). The viscous term vanishes
against every smooth test because

\[
\left|
\varepsilon_j\int v_j\cdot\Delta\varphi
\right|
\le
\varepsilon_j\sqrt M\|\Delta\varphi\|_2
\longrightarrow0.
\]

Passing to the limit in the projected equation proves the
Euler--Reynolds identity. Finally, positivity makes
\(\operatorname{tr}\mathcal R=0\) equivalent to \(\mathcal R=0\).
Equality of the local weak \(L^2\) limit and local norm limit is equivalent
to strong \(L^2\) convergence.

## 3. The viscous defect vanishes on one energy-efficient trajectory

### Theorem 2: terminal dissipation collapse

For the carriers obtained from one smooth finite-energy Navier--Stokes
solution in the energy-efficient branch, let

\[
d\mu_j
:=
\varepsilon_j|\nabla_yv_j|^2\,dy\,ds.
\]

For every compact interval \(J\Subset I\), and also for
\(J=[-S,0]\) when \(H=0\),

\[
\boxed{
\mu_j(J\times\mathbb R^3)\longrightarrow0.
}
\]

Consequently the global normalised energy drop across \(J\) tends to zero.
After a subsequence \(b_j\to b>0\), and uniformly for \(s\) in compact
subintervals of \(I\),

\[
\|v_j(s)\|_2^2
\longrightarrow
\frac{E_*}{b},
\qquad
E_*:=\lim_{t\uparrow T^*}\|u(t)\|_2^2>0.
\]

### Proof

The exact change of variables gives

\[
\boxed{
\int_J\!\!\int_{\mathbb R^3}
\varepsilon_j|\nabla_yv_j|^2\,dy\,ds
=
\frac{\nu}{b_j}
\int_{t_j+\tau_jJ}\!\!\int_{\mathbb R^3}
|\nabla_xu|^2\,dx\,dt.
}
\]

The physical intervals \(t_j+\tau_jJ\) shrink to \(T^*\), because
\(\tau_j\to0\) and \(t_j\uparrow T^*\). The physical dissipation belongs to
\(L^1(0,T^*)\), while \(b_j\ge c_0/4\). Absolute continuity of the integral
proves the claim.

The rescaled energy identity is

\[
\frac12\|v_j(s_2)\|_2^2
+\int_{s_1}^{s_2}\!\!\int
\varepsilon_j|\nabla v_j|^2
=
\frac12\|v_j(s_1)\|_2^2.
\]

Hence the energy oscillation on every compact carrier interval vanishes.
Since \(b_j\) stays in a compact positive interval, take
\(b_j\to b>0\). Physical energy has the terminal limit \(E_*\), and
\(e_j\le\|u(t_j)\|_2^2\) with \(e_j\ge c_0\), so \(E_*>0\). The displayed
energy convergence follows.

### Scope

This removes limiting viscous dissipation only in the energy-efficient
branch. When \(e_j\to0\), the denominator \(b_j\asymp e_j\) also tends to
zero, and terminal physical absolute continuity need not control the
normalised dissipation.

The theorem also does not remove \(\mathcal R\). A sequence can carry
arbitrarily fine inviscid oscillation while
\(\varepsilon_j\|\nabla v_j\|_2^2\) tends to zero.

## 4. Exact terminal trace alternative

At \(s=0\), take weak-star limits of the matrix-valued measures:

\[
v_j(0)\otimes v_j(0)\,dy
\stackrel{*}{\rightharpoonup}
V(0)\otimes V(0)\,dy+\mathcal R_0.
\]

The same lower-semicontinuity argument as above gives

\[
\mathcal R_0\ge0.
\]

Its trace

\[
\mathcal T_0:=\operatorname{tr}\mathcal R_0
\]

is the terminal \(L^2\) trace defect. It vanishes locally exactly when
\(v_j(0)\to V(0)\) strongly in local \(L^2\).

### Theorem 3: retained layer mass cannot vanish silently

Suppose the carrier concentration parameter satisfies \(\theta>0\), covering
both partial and tight geometry. For every \(0<\eta<\theta\), there are
fixed \(K<\infty\) and carrier centres such that, after a subsequence,

\[
\boxed{
\int_{B_{K+1}}|V(0)|^2\,dy
+\mathcal T_0(B_{K+1})
\ge\eta.
}
\]

Therefore at least one of the following holds:

1. \(V(0)\ne0\), and distributional time continuity makes \(V\) nonzero on a
   carrier-time neighbourhood;
2. \(\mathcal T_0\ne0\), so the retained carrier survives only as terminal
   vector/frequency microstructure.

### Proof

By the definition of \(\theta\), choose centres so that

\[
\frac1{e_j}
\int_{A_j\cap B_{KR_j}(x_j)}|u(x,t_j)|^2\,dx
\ge\eta
\]

eventually. In carrier variables,

\[
\int_{\widetilde A_j\cap B_K}|v_j(y,0)|^2\,dy
\ge
\eta\frac{e_j}{b_j}
\ge\eta.
\]

Choose a continuous cutoff equal to one on \(B_K\) and supported in
\(B_{K+1}\), then pass to the terminal matrix-measure limit and take the
trace.

This theorem is a trace alternative, not trace persistence. It does not
choose between its two branches.

## 5. Exact equation-family survivor

The construction below uses the established theorem of
[Gavrilov](https://doi.org/10.1007/s00039-019-00476-6): there is a nonzero
pair

\[
U\in C_c^\infty(\mathbb R^3;\mathbb R^3),
\qquad
P\in C^\infty(\mathbb R^3)
\]

such that

\[
U\cdot\nabla U=-\nabla P,
\qquad
\nabla\cdot U=0,
\]

and \(\nabla P\) is compactly supported. The exact arXiv source states the
theorem at lines 44--66 and performs the localising cutoff at lines
292--303.

### 5.1 Fine steady packet clouds

Subtract the exterior constant from \(P\), making \(P\) compactly supported.
Choose a regular near-maximising distribution level, perturbing it if needed
so that twice that level is also regular. One fixed amplitude and spatial
normalisation then ensures:

- \(U\) and \(P\) are supported in the interior of a cube
  \(Q=(0,L)^3\);
- the level \(1\) is a strict half-extremiser for the weak-\(L^3\)
  distribution;
- \(1\) and \(2\) are regular levels of \(|U|\); and
- the layer \(A=\{1<|U|\le2\}\) has volume one.

For \(N=n^3\), put one copy

\[
U_{n,k}(x):=U(nx-Lk),
\qquad
P_{n,k}(x):=P(nx-Lk)
\]

in each of the \(n^3\) cells of \(Q\), and set

\[
W_n:=\sum_kU_{n,k},
\qquad
\Pi_n:=\sum_kP_{n,k}.
\]

The supports are disjoint, so

\[
W_n\cdot\nabla W_n=-\nabla\Pi_n,
\qquad
\nabla\cdot W_n=0.
\]

The distribution function of \(|W_n|\) is exactly that of \(|U|\).
Consequently

\[
|\{1<|W_n|\le2\}|=1,
\qquad
\|W_n\|_2=\|U\|_2,
\qquad
\|W_n\|_{L^{3,\infty}}=\|U\|_{L^{3,\infty}}.
\]

Because every compactly supported divergence-free field has zero mean,

\[
\int_{\mathbb R^3}U\,dx=0.
\]

Riemann sums therefore give

\[
W_n\rightharpoonup0\quad\hbox{in }L^2,
\]

while

\[
W_n\otimes W_n
\stackrel{*}{\rightharpoonup}
\frac{\mathbf1_Q}{L^3}
\int_Q U\otimes U\,dx.
\]

The limiting tensor is nonzero. It is also isotropic. Indeed, the compact
steady momentum equation and integration by parts give the virial identity

\[
\int_{\mathbb R^3}
\bigl(U_iU_j+P\delta_{ij}\bigr)\,dx=0.
\]

Thus for some \(c>0\),

\[
\frac1{L^3}\int U\otimes U\,dx=cI.
\]

The weak momentum defect is a pressure gauge, but its trace is the positive
energy defect \(3c\mathbf1_Q\,dx\).

### 5.2 All three geometry branches

The same packet has layer energy and volume proportional to \(N^{-1}\) after
the spatial shrinkage \(N^{1/3}\).

- Packing all \(N\) copies in one fixed cube gives \(\theta=1\).
- Sending the mutual distances to infinity gives \(\theta=0\), since every
  fixed ball captures at most \(o(N)\) packets.
- Packing a fraction tending to \(\theta\in(0,1)\) in one fixed cube and
  sending the rest apart gives that exact partial concentration parameter.

All sums remain smooth finite-energy steady Euler solutions because their
velocity and pressure-gradient supports are disjoint. Their amplitude-layer
volume is one and their total-to-layer energy ratio is fixed.

### 5.3 Diagonal exact Navier--Stokes approximation

For completeness, fix a smooth steady Euler field \(W\), a finite interval
\([0,T]\), and \(r>5/2\). If \(z=v^\varepsilon-W\), the standard
\(H^r\) commutator estimate for

\[
\partial_tv^\varepsilon+
\mathbb P\nabla\!\cdot
(v^\varepsilon\otimes v^\varepsilon)
=\varepsilon\Delta v^\varepsilon,
\qquad
v^\varepsilon(0)=W,
\]

gives, while \(\|z\|_{H^r}\le1\),

\[
\frac d{dt}\|z\|_{H^r}
\le
C_{r,W}\|z\|_{H^r}
+C_{r,W}\|z\|_{H^r}^2
+C_{r,W}\varepsilon.
\]

Gronwall and continuation show that for every fixed \(W,T\),

\[
\sup_{0\le t\le T}
\|v^\varepsilon(t)-W\|_{H^r}
\longrightarrow0
\quad\hbox{as}\quad
\varepsilon\downarrow0.
\]

Time-translate this construction, set \(v_n(-n)=W_n\), and apply it
separately to the \(n\)-th packet cloud on \([-n,H_n]\), where

\[
H_n\longrightarrow H\in[0,\infty].
\]

Choose the viscosity diagonally so small that

\[
\varepsilon_n\to0,
\qquad
\sup_{-n\le s\le H_n}
\|v_n(s)-W_n\|_{H^r}\le\frac1n.
\]

For \(H=0\), take \(H_n\downarrow0\); for finite positive \(H\), take
\(H_n\to H\); and for \(H=\infty\), take \(H_n\to\infty\). These are exact
smooth Navier--Stokes solutions with an arbitrarily long past.

The \(L^2\) and \(L^\infty\) closeness imply weak-\(L^3\) closeness by
interpolation. Uniform convergence and regularity of levels \(1\) and \(2\)
make the perturbed and steady layer indicators differ on a set of volume
\(o(1)\). Their layer-energy measures therefore converge in total variation,
uniformly over spatial balls. The strict near-extremising margin preserves
the selected level, while total-variation convergence preserves its
concentration parameter. Defining the exact terminal carrier radius from the
perturbed layer and renormalising space and time introduces only \(1+o(1)\)
factors. The energy identity and uniform \(L^2\) closeness also give

\[
\int_J\!\!\int
\varepsilon_n|\nabla v_n|^2\,dy\,ds\longrightarrow0
\]

for every \(J\Subset(-\infty,H)\), and for \(J=[-S,0]\) when \(H=0\).
The weak and quadratic limits are those of the packet clouds.

### Theorem 4: finite-window equation data do not force a nonzero profile

For each

\[
\theta\in\{0\}\cup(0,1)\cup\{1\},
\qquad
H\in\{0\}\cup(0,\infty)\cup\{\infty\},
\]

there is a sequence of exact smooth vanishing-viscosity Navier--Stokes
carrier equations satisfying:

1. uniformly bounded global energy and a selected-layer fraction uniformly
   bounded away from zero;
2. the prescribed diffuse, partial, or tight layer geometry;
3. a prescribed shrinking, finite, or expanding forward observation window
   and an infinite limiting past;
4. vanishing normalised viscous dissipation on compact time intervals; and
5. failure of strong local \(L^2\) compactness whenever a positive packet
   fraction is retained.

In the tight construction the limiting velocity is zero and the positive
defect is isotropic. In the diffuse construction the energy escapes every
fixed spatial compact set. The partial construction contains both effects.

These families use a different initial datum and a separately chosen small
carrier viscosity at every index. They are not carriers extracted from one
fixed-viscosity physical trajectory, and their forward endpoints are
artificial cut-offs across which the solutions remain smooth. Thus they do
not construct blow-up or realise the singular-horizon semantics of an R3C
clock cell.

They can nevertheless be put in the exact fixed-\(\nu\) carrier
normalisation, separately at every index. Set

\[
R_n=\frac{\varepsilon_n^2}{\nu^2},
\qquad
a_n=\frac{\nu^3}{\varepsilon_n^3},
\qquad
\tau_n=\frac{\varepsilon_n^5}{\nu^5}.
\]

Then

\[
u_n(x,t)
:=
a_n v_n\!\left(\frac{x}{R_n},\frac{t}{\tau_n}\right)
\]

solves viscosity-\(\nu\) Navier--Stokes,
\(a_n^2R_n^3=1\), and

\[
\|u_n(0)\|_{L^{3,\infty}}
=a_nR_n\|v_n(0)\|_{L^{3,\infty}}
\asymp\frac{\nu}{\varepsilon_n}\longrightarrow\infty.
\]

Thus the obstruction is not an artefact of inconsistent carrier units; its
missing ingredient is precisely one-trajectory ancestry and singular
terminality.

## 6. What the physical budget can and cannot see

A fixed amount of normalised viscous defect would map to

\[
\frac{\nu}{b_j}
\int_{t_j+\tau_jJ}\|\nabla u\|_2^2\,dt,
\]

and is impossible in the energy-efficient branch by Theorem 2.

A fixed normalised space-time Reynolds/energy defect instead maps to physical
space-time kinetic mass with prefactor

\[
b_j\tau_j
\asymp e_j\tau_j
\longrightarrow0.
\]

It therefore supplies no fixed physical charge. A terminal trace defect maps
to order-\(e_j\) energy, but that is an energy stock and may be reused at
successive carrier times.

The next live alternatives are consequently:

1. use common physical ancestry to turn terminal microstructure into a
   positive high-frequency flux or another non-reusable charge;
2. prove that a positive Reynolds/trace defect persists for enough physical
   time to become chargeable;
3. prove a one-trajectory rigidity theorem excluding the packed inviscid
   microstructure mechanism; or
4. handle the energy-vanishing branch, where even the global normalised
   \(L^2\) compactness used here is absent.

No alternative A--D of the Clay problem is proved.
