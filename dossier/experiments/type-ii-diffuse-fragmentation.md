# Diffuse Type-II layers force sharp Morrey fragmentation

- **Experiment:** EXP-TYPE-II-DIFFUSE-FRAGMENTATION-001
- **Route:** ROUTE-R3C
- **Status:** complete conditional quantitative reduction; external review pending
- **Domain:** smooth finite-energy Navier--Stokes flow on \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** [temporal five-power theorem](type-ii-temporal-five-barrier.md)
  and [carrier entrance](type-ii-inviscid-carrier-entrance.md)

## Verdict

The diffuse energy-efficient exact \(q=4\) layer pays a rigorously
quantifiable fragmentation cost, but the resulting charge is not yet
nonsummable.

For the explicit Leslie--Shvydkoy local-energy exponent
\(\beta=1/29\), define

\[
\rho_j:=L R_j^{3/(3-\beta)}
=L R_j^{87/86},
\]

where \(L\) is one sufficiently large fixed constant. Then the selected
layer has, subject to the finite-perimeter convention below,

\[
\boxed{
\operatorname{Per}(A_j)
\gtrsim R_j^{171/86},
}
\qquad
\boxed{
\|\nabla u(t_j)\|_2^2
\gtrsim R_j^{-87/43}.
}
\]

Thus

\[
\frac{\operatorname{Per}(A_j)}{R_j^2}
\gtrsim R_j^{-1/86}\longrightarrow\infty,
\qquad
R_j^2\|\nabla u(t_j)\|_2^2
\gtrsim R_j^{-1/43}\longrightarrow\infty.
\]

Using every temporal exponent below the exact \(11/2\) endpoint gives, for
each \(\varepsilon>0\),

\[
\boxed{
\operatorname{Per}(A_j)
\gtrsim_\varepsilon
R_j^{51/26+\varepsilon},
\qquad
\|\nabla u(t_j)\|_2^2
\gtrsim_\varepsilon
R_j^{-27/13+\varepsilon}.
}
\]

The corresponding limiting fragmentation scale, component-count scale,
and energy-per-piece scale are

\[
\rho_j=R_j^{27/26+o(1)},
\qquad
N_j=R_j^{-3/26+o(1)},
\qquad
N_j^{-1}=R_j^{3/26+o(1)}.
\]

These powers are sharp under the static inputs used here. A family of
smooth compactly supported divergence-free packet fields has fixed energy,
the required amplitude-layer scaling, local energy bounded by
\(Cr^\beta\) at every radius, and matching perimeter and enstrophy powers.
It is not one Navier--Stokes trajectory.

For the exact record gap

\[
\Delta t_j\asymp \frac{R_j^{11/4}}j,
\]

even the optimised formal full-gap enstrophy floor has weight

\[
\Delta t_j R_j^{-27/13+o(1)}
=\frac1jR_j^{35/52+o(1)},
\]

which is summable. Natural cubic-flux, cutoff-flux, and viscous-cutoff
weights are summable as well. Static fragmentation therefore does not
close the diffuse cell. The next live obligation is temporal/frequency
coherence at \(\rho_j\): either detect a fixed low-frequency energy fraction
at frequencies \(\lesssim\rho_j^{-1}\), or turn its failure into a
time-resident high-frequency charge.

## 1. Exact setting

Let \(u\) be a smooth divergence-free finite-energy solution on
\(\mathbb R^3\times[0,T^*)\), where \(T^*\) is its first possible singular
time. Let \(t_j\uparrow T^*\) be the exact \(q=4\) first-record sequence:

\[
m_j:=\|u(t_j)\|_{L^{3,\infty}}
\asymp2^{2j},
\qquad
t_{j+1}-t_j\asymp\frac{2^{-11j}}j.
\]

The near-extremising amplitude layer is

\[
A_j:=\{a_j<|u(t_j)|\le2a_j\},
\qquad
e_j:=\int_{A_j}|u(t_j)|^2\,dx,
\qquad
R_j:=|A_j|^{1/3}.
\]

Work in the energy-efficient branch

\[
0<c_0\le e_j\le E_0.
\]

The amplitude-layer theorem gives

\[
a_j^2R_j^3\asymp e_j,
\qquad
a_j\asymp R_j^{-3/2},
\qquad
R_j\asymp m_j^{-2}\asymp2^{-4j}.
\]

The temporal five-power theorem supplies the following explicit local
energy estimate on every fixed compact \(K\):

\[
\sup_{\substack{T^*-r^{72/29}<t<T^*\\x\in K}}
\int_{B_r(x)}|u(y,t)|^2\,dy
\le C_Kr^{1/29}.
\tag{1}
\]

Uniform spatial tightness permits one fixed ball \(K_0\) such that

\[
\int_{A_j\cap K_0}|u(t_j)|^2\,dx\ge\frac{c_0}{2}
\tag{2}
\]

for every sufficiently large \(j\).

## 2. A local \(L^{10/3}\) concentration inequality

### Lemma 1

There is an absolute \(C\) such that, for every \(f\in H^1(\mathbb R^3)\)
and every \(r>0\),

\[
\boxed{
\|f\|_{10/3}^{10/3}
\le
C\left(
\sup_{x\in\mathbb R^3}
\int_{B_{2r}(x)}|f|^2
\right)^{2/3}
\left(
\|\nabla f\|_2^2+r^{-2}\|f\|_2^2
\right).
}
\tag{3}
\]

#### Proof

Tile \(\mathbb R^3\) by disjoint cubes \(Q\) of side \(r\). On one cube,
interpolation between \(L^2\) and \(L^6\), followed by the scaled local
Sobolev inequality, gives

\[
\begin{aligned}
\int_Q|f|^{10/3}
&\le
\|f\|_{L^2(Q)}^{4/3}
\|f\|_{L^6(Q)}^2\\
&\le
C\left(\int_Q|f|^2\right)^{2/3}
\left(
\int_Q|\nabla f|^2
+r^{-2}\int_Q|f|^2
\right).
\end{aligned}
\]

Every \(Q\) lies in a ball of radius \(2r\). Take the largest local
\(L^2\) mass outside the sum and then sum over the disjoint cubes.

## 3. The optimised enstrophy surcharge

### Theorem 2

Suppose that, at the times \(t_j\), the local estimate

\[
\sup_{\substack{x\in K\\0<r<r_K}}
\int_{B_r(x)}|u(y,t_j)|^2\,dy
\le C_Kr^\beta
\tag{4}
\]

holds on every fixed compact set, for some \(0<\beta<3\). Suppose also
that \(t_j\) lies in the estimate's terminal window at the radii

\[
\rho_j:=L R_j^{3/(3-\beta)}.
\tag{5}
\]

Then one can choose the fixed constant \(L\) sufficiently large so that

\[
\boxed{
\|\nabla u(t_j)\|_2^2
\ge c_{\beta,L}R_j^{-6/(3-\beta)}
}
\tag{6}
\]

for every sufficiently large \(j\).

#### Proof

Choose \(\chi\in C_c^\infty(\mathbb R^3)\) equal to one on \(K_0\), with
support in a second fixed compact set, and put

\[
f_j:=\chi u(t_j).
\]

By (2), the amplitude bounds on \(A_j\), and
\(a_j^2R_j^3\asymp e_j\),

\[
\begin{aligned}
\|f_j\|_{10/3}^{10/3}
&\ge
\int_{A_j\cap K_0}|u(t_j)|^{10/3}\,dx\\
&\ge
a_j^{4/3}
\int_{A_j\cap K_0}|u(t_j)|^2\,dx\\
&\ge cR_j^{-2}.
\end{aligned}
\tag{7}
\]

Only balls meeting the fixed support of \(\chi\) enter Lemma 1. Hence
(4), enlarged to one fixed compact, gives

\[
\sup_x\int_{B_{2\rho_j}(x)}|f_j|^2
\le C\rho_j^\beta.
\]

Moreover,

\[
\|f_j\|_2^2\le E_0,
\qquad
\|\nabla f_j\|_2^2
\le C\bigl(\|\nabla u(t_j)\|_2^2+E_0\bigr).
\]

Apply Lemma 1 at \(r=\rho_j\) and combine it with (7):

\[
cR_j^{-2}
\le
C\rho_j^{2\beta/3}
\left(
\|\nabla u(t_j)\|_2^2+C\rho_j^{-2}
\right).
\]

After rearrangement,

\[
\|\nabla u(t_j)\|_2^2
\ge
cR_j^{-2}\rho_j^{-2\beta/3}
-C\rho_j^{-2}.
\tag{8}
\]

The choice (5) makes both terms have the same \(R_j\) power:

\[
R_j^{-2}\rho_j^{-2\beta/3}
=L^{-2\beta/3}R_j^{-6/(3-\beta)},
\]

\[
\rho_j^{-2}
=L^{-2}R_j^{-6/(3-\beta)}.
\]

Because \(2>2\beta/3\), one fixed sufficiently large \(L\) makes the
positive coefficient in (8) dominate the negative one. This proves (6).

### Explicit \(q=4\) exponents

For (1),

\[
\beta=\frac1{29},
\qquad
\rho_j=L R_j^{87/86},
\qquad
\frac6{3-\beta}=\frac{87}{43}.
\]

The terminal-window condition is valid because

\[
\rho_j^{72/29}
\asymp R_j^{108/43},
\qquad
\frac{T^*-t_j}{\rho_j^{72/29}}
\lesssim
\frac1jR_j^{41/172}
\longrightarrow0.
\]

Consequently,

\[
\|\nabla u(t_j)\|_2^2
\gtrsim R_j^{-87/43}.
\tag{9}
\]

This is stronger than the scale-\(R_j\) floor \(R_j^{-2}\) by the
unbounded factor \(R_j^{-1/43}\).

## 4. The optimised interface surcharge

Write \(\operatorname{Per}(A)\in[0,\infty]\) for the De Giorgi perimeter.
If an exact dyadic endpoint is exceptional and gives infinite perimeter,
the following lower bound is automatic.

### Theorem 3

Under the hypotheses of Theorem 2,

\[
\boxed{
\operatorname{Per}(A_j)
\ge
c_{\beta,L}
R_j^{\,2-\beta/(3-\beta)}.
}
\tag{10}
\]

#### Proof

Tile space by cubes \(Q\) of side \(\rho_j\). Retain only the finitely many
cubes meeting \(K_0\); they lie in one fixed larger compact set. Put

\[
v_Q:=|A_j\cap Q|.
\]

Because \(|u|>a_j\) on \(A_j\), (4) and
\(a_j^{-2}\lesssim R_j^3\) give

\[
v_Q
\le
a_j^{-2}\int_Q|u(t_j)|^2\,dx
\le
CR_j^3\rho_j^\beta.
\tag{11}
\]

On the other hand, (2), \(|u|\le2a_j\) on \(A_j\), and
\(a_j^{-2}\gtrsim R_j^3\) give

\[
\sum_Qv_Q
\ge |A_j\cap K_0|
\ge cR_j^3.
\tag{12}
\]

The ratio of the right side of (11) to \(|Q|=\rho_j^3\) is

\[
CR_j^3\rho_j^{\beta-3}
=CL^{\beta-3}.
\]

Increase the already fixed \(L\), if necessary, so that every retained
cube contains at most half its volume of \(A_j\). The relative
isoperimetric inequality on each cube and disjointness of their interiors
then imply

\[
\begin{aligned}
\operatorname{Per}(A_j)
&\ge c\sum_Qv_Q^{2/3}\\
&\ge
c\bigl(R_j^3\rho_j^\beta\bigr)^{-1/3}
\sum_Qv_Q\\
&\ge
cR_j^2\rho_j^{-\beta/3}\\
&=
c_{\beta,L}
R_j^{\,2-\beta/(3-\beta)}.
\end{aligned}
\]

For \(\beta=1/29\), this becomes

\[
\operatorname{Per}(A_j)
\gtrsim R_j^{171/86},
\qquad
\frac{\operatorname{Per}(A_j)}{R_j^2}
\gtrsim R_j^{-1/86}.
\tag{13}
\]

The absolute perimeter may still tend to zero. It is the perimeter
relative to one radius-\(R_j\) carrier that diverges.

## 5. Optimization below the unavailable endpoint

The exact \(q=4\) clock gives temporal weak-\(L^3\) integrability for every
\(s<11/2\). In the Leslie--Shvydkoy estimate, let \(s\uparrow11/2\) and
the interpolation parameter tend to zero. The local energy exponent and
terminal-window exponent approach

\[
\beta_*= \frac19,
\qquad
\alpha_*=\frac{22}{9}.
\]

Thus, for every \(0<b<1/9\), one may choose an admissible pair whose local
energy exponent is greater than \(b\), downgrade the resulting estimate to
\(Cr^b\), and retain a terminal-window exponent \(\alpha\) as close to
\(22/9\) as desired.

At the optimised radius

\[
\rho_j=L R_j^{3/(3-b)},
\]

the terminal-window requirement remains strict because

\[
\frac{3\alpha_*}{3-\beta_*}
=\frac{33}{13}
<\frac{11}{4}.
\]

Theorems 2 and 3 therefore give, for every \(b<1/9\),

\[
\|\nabla u(t_j)\|_2^2
\gtrsim_b R_j^{-6/(3-b)},
\tag{14}
\]

\[
\operatorname{Per}(A_j)
\gtrsim_b
R_j^{\,2-b/(3-b)}.
\tag{15}
\]

Letting \(b\uparrow1/9\) yields the convenient epsilon form

\[
\boxed{
\|\nabla u(t_j)\|_2^2
\gtrsim_\varepsilon
R_j^{-27/13+\varepsilon},
}
\tag{16}
\]

\[
\boxed{
\operatorname{Per}(A_j)
\gtrsim_\varepsilon
R_j^{51/26+\varepsilon}.
}
\tag{17}
\]

The limiting geometric ledger is

\[
\rho_j=R_j^{27/26+o(1)},
\qquad
\left(\frac{R_j}{\rho_j}\right)^3
=R_j^{-3/26+o(1)}.
\tag{18}
\]

The second quantity is the minimum equal-piece count suggested by the
Morrey bound. The theorems themselves do not assume that the layer has
connected components of comparable size.

## 6. A sharp divergence-free packet family

The powers in (14)--(15) cannot be improved using only:

1. fixed total layer energy;
2. amplitude \(a\asymp R^{-3/2}\) on total volume \(\asymp R^3\); and
3. the local energy Morrey bound \(\sup_x\int_{B_r(x)}|u|^2\lesssim r^b\).

Fix \(0<b<3\) and a nonzero
\(\phi\in C_c^\infty(B_1;\mathbb R^3)\) with
\(\nabla\cdot\phi=0\). Choose

\[
N\asymp R^{-3b/(3-b)},
\qquad
\rho:=RN^{-1/3}\asymp R^{3/(3-b)},
\qquad
a:=R^{-3/2}.
\]

Place \(N\) centres quasi-uniformly in a fixed unit cube, with separation

\[
d\asymp N^{-1/3}\gg\rho,
\]

and define the smooth compactly supported divergence-free field

\[
U_R(x)
:=
a\sum_{k=1}^N
\phi\!\left(\frac{x-x_k}{\rho}\right).
\tag{19}
\]

The supports are disjoint. Direct scaling gives

\[
\|U_R\|_2^2
\asymp a^2N\rho^3
\asymp1,
\]

\[
\|U_R\|_{L^{3,\infty}}
\asymp a(N\rho^3)^{1/3}
\asymp R^{-1/2},
\]

\[
\|\nabla U_R\|_2^2
\asymp a^2N\rho
\asymp R^{-6/(3-b)}.
\tag{20}
\]

A fixed regular amplitude band of \(\phi\), replicated in every packet,
has energy \(\asymp1\), total volume \(\asymp R^3\), volume radius
\(\asymp R\), and perimeter

\[
\asymp N\rho^2
\asymp R^{\,2-b/(3-b)}.
\tag{21}
\]

The local energy estimate holds at every radius \(0<r\le1\):

\[
\sup_x\int_{B_r(x)}|U_R|^2\,dx
\lesssim r^b.
\tag{22}
\]

Indeed:

- if \(r\le\rho\), boundedness of \(\phi\) gives
  \(R^{-3}r^3\le r^b\), because \(\rho^{3-b}=R^3\);
- if \(\rho\le r\le d\), a ball meets only \(O(1)\) packets and carries
  \(O(N^{-1})=O(\rho^b)\) energy;
- if \(d\le r\le1\), quasi-uniform packing gives at most
  \(O(1+Nr^3)\) packets, hence energy
  \(O(N^{-1}+r^3)=O(r^b)\).

This family saturates (14) and (15), even though its energy has no
shrinking spatial atom. It is a kinematic family of different fields, not
a Navier--Stokes evolution, and therefore does not kill ROUTE-R3C.

## 7. Exact \(q=4\) summability audit

At the limiting exponent \(b\uparrow1/9\),

\[
\rho_j=R_j^{27/26+o(1)},
\qquad
\|\nabla u(t_j)\|_2^2
\gtrsim R_j^{-27/13+o(1)}.
\]

Multiplying the pointwise floor by the entire record gap would give only

\[
\Delta t_j R_j^{-27/13+o(1)}
\asymp
\frac1jR_j^{11/4-27/13+o(1)}
=
\frac1jR_j^{35/52+o(1)}.
\tag{23}
\]

The series of these numerical floors converges geometrically. Equation
(23) is not an integrated enstrophy lower bound: no persistence across
the full gap has been proved. Its point is sharper and negative--even
that optimistic persistence would not contradict the finite dissipation
budget at the present power.

Likewise, the limiting perimeter floor
\(R_j^{51/26+o(1)}\) is itself summable, and the packet family attains
that scale. A large normalized interface is therefore not an absolute
interface budget contradiction.

The sharp packet family also has

\[
\|U_R\|_3^3\asymp a^3R^3\asymp R^{-3/2}.
\]

Consequently, the natural full-gap global cubic-action scale is

\[
\Delta t_j\|U_{R_j}\|_3^3
\asymp
\frac1jR_j^{5/4},
\tag{24}
\]

and a cutoff at the fragmentation radius contributes at most the
dimensional scale

\[
\frac{\Delta t_j}{\rho_j}
\|U_{R_j}\|_3^3
\asymp
\frac1jR_j^{11/52+o(1)}.
\tag{25}
\]

The pressure representative
\(p=\mathcal R_a\mathcal R_b(U_aU_b)\) satisfies

\[
\int|p||U_R|
\le C\|U_R\|_3^3,
\]

so it has the same summable cutoff scale. The viscous cutoff scale is

\[
\frac{\Delta t_j}{\rho_j^2}
\asymp
\frac1jR_j^{35/52+o(1)}.
\tag{26}
\]

These are scale audits, not lower bounds for an NSE event. They prove that
the existing static estimates do not manufacture a nonsummable pressure,
interface, or dissipation charge.

One favourable strict clock remains. The energy-only low-pass estimate
changes frequencies below \(\rho_j^{-1}\) on the time scale
\(\rho_j^{5/2}\), while

\[
\frac{\Delta t_j}{\rho_j^{5/2}}
\asymp
\frac1jR_j^{\,11/4-135/52+o(1)}
=
\frac1jR_j^{2/13+o(1)}
\longrightarrow0.
\tag{27}
\]

The missing premise is a fixed energy fraction visible below a controlled
multiple of \(\rho_j^{-1}\). Spatial Morrey fragmentation alone does not
supply it: arbitrarily small energy can carry arbitrarily large
enstrophy at higher frequencies.

## 8. Route disposition

### Closed in this round

- Diffuse exact \(q=4\) layers have a quantitative Morrey fragmentation
  scale.
- Their normalized perimeter and normalized enstrophy diverge at explicit
  powers.
- The powers are sharp for smooth compactly supported divergence-free
  static fields satisfying every static input used in the proof.
- The strongest currently available q4-weighted interface, enstrophy,
  cubic-action, cutoff-flux, and viscous-cutoff powers are summable.

### Still open

- Prove that a fixed fraction of the diffuse layer is visible below
  \(C/\rho_j\), or convert its failure into a fixed high-frequency energy
  floor.
- Give that spectral alternative enough same-trajectory residence,
  freshness, sign, or orthogonality to force a nonsummable charge.
- Control the divergent-normalised-energy branch and slower record clocks.
- Resolve any Clay alternative A--D.
