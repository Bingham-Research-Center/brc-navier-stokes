# Record-high Type-II carriers force logarithmic subgrid residence

- **Experiment:** EXP-TYPE-II-RECORD-RESIDENCE-001
- **Route:** ROUTE-R3C
- **Status:** complete analytic reduction with scaling survivor
- **Clay status:** unsolved

This note continues the
[signed subgrid-ancestry theorem](type-ii-subgrid-transport.md). It uses one
piece of common physical ancestry that arbitrary varying-trajectory packet
families do not possess: the Type-II sampling times may be chosen as first
record highs of the physical weak-\(L^3\) norm.

## Verdict

Record-high sampling makes every rescaled carrier uniformly bounded in
\(L^{3,\infty}\) over its entire ancient past. This converts the formal
phrase “NSE flux rate” into a quantitative endpoint estimate. At heat-filter
length \(\ell\),

\[
\left|\int_{\mathbb R^3}\Pi_\ell[v]\,dy\right|
\le
\frac{C}{\ell}
\|v\|_{L^{3,\infty}}^3
\log\left(
e+\frac{C\|v\|_2^2}
{\ell\|v\|_{L^{3,\infty}}^2}
\right).
\]

The logarithm is the endpoint loss in pairing a weak-\(L^{3/2}\) stress with an
\(L^{3,1}\) filtered gradient.

For a positive terminal trace defect, define its canonical subgrid length
\(\ell_j\) as the first heat-filter scale at which a fixed amount of global
subgrid energy appears. Then \(\ell_j\to0\). The flux ceiling prevents that
energy from appearing instantaneously: it remains at least half present for
a backward carrier-time interval of length

\[
h_j
\gtrsim
\frac{\ell_j}
\log(e+C/\ell_j).
\]

During that interval,
\(\|\nabla v_j\|_2^2\gtrsim\ell_j^{-2}\). Terminal absolute continuity of
the physical dissipation therefore forces

\[
\boxed{
\frac{\varepsilon_j}
{\ell_j\log(e+C/\ell_j)}
\longrightarrow0.
}
\]

Equivalently, at the physical defect length \(r_j=R_j\ell_j\),

\[
\frac{a_jr_j}{\nu}
\log\left(e+C\frac{R_j}{r_j}\right)
\longrightarrow\infty.
\]

Thus record-high Type-II trace microstructure must live in a
logarithmically corrected inertial range. In particular, the transfer timing
in the previous fixed-viscosity shell ledger cannot model one
record-normalised carrier history: it is too fast to respect the uniform
critical ceiling.

It does not yet exclude a cross-carrier Zeno genealogy. The compatible power
ledger

\[
\ell_j=2^{-j},
\qquad
\varepsilon_j=2^{-2j}
\]

has the forced residence \(h_j\asymp2^{-j}/j\), while the residence theorem
forces only
\(\varepsilon_j\ell_j^{-2}h_j\asymp2^{-j}/j\) normalised viscous action.
These forced lower charges have finite sum, so the present inequalities alone
give no contradiction. A closing theorem must therefore relate successive
canonical defect scales to successive carrier normalisations, or prove that
their order-one physical transfers are fresh.

## 1. First-record carrier sequence

Write

\[
m(t):=\|u(t)\|_{L^{3,\infty}(\mathbb R^3)}.
\]

Before a first singular time, smoothness and interpolation give continuity
of \(m(t)\). Indeed,

\[
\|f\|_{L^{3,\infty}}
\le
C\|f\|_2^{2/3}\|f\|_\infty^{1/3},
\]

and the smooth solution is continuous in both \(L^2\) and \(L^\infty\) on
every compact subinterval of \([0,T^*)\). Applied to a time difference, this
makes its weak-\(L^3\) quasi-norm tend to zero. For completeness, the
distribution-function inclusion gives, for \(0<\eta<1\),

\[
\|f\|_{L^{3,\infty}}
\le
\frac{\|g\|_{L^{3,\infty}}}{1-\eta}
+
\frac{\|f-g\|_{L^{3,\infty}}}{\eta}.
\]

Apply this inequality in both directions and then let the difference tend to
zero followed by \(\eta\downarrow0\). Thus the particular distribution
quasi-norm used here is continuous in time.

If \(m(t)\) is unbounded as \(t\uparrow T^*\), choose increasing levels
\(M_j>m(0)\), \(M_j\to\infty\), and let \(t_j\) be the first time at which

\[
m(t_j)=M_j.
\]

Continuity and boundedness on compact preterminal intervals give

\[
t_j\uparrow T^*,
\qquad
m(t)\le m(t_j)
\quad(0\le t\le t_j).
\]

At \(t_j\), choose the half-extremising amplitude layer from the entrance
theorem. Its exact volume bounds are

\[
\frac38\frac{m_j^3}{a_j^3}
\le |A_j|
\le\frac{m_j^3}{a_j^3},
\qquad
m_j:=m(t_j).
\]

Since \(R_j=|A_j|^{1/3}\),

\[
\left(\frac38\right)^{1/3}m_j
\le a_jR_j\le m_j.
\]

The carrier scaling therefore gives, throughout its whole physical past,

\[
\begin{aligned}
\|v_j(s)\|_{L^{3,\infty}}
&=
\frac{
m(t_j+\tau_js)
}{a_jR_j}\\
&\le
\left(\frac83\right)^{1/3}
=:L_*,
\qquad
-\frac{t_j}{\tau_j}\le s\le0.
\end{aligned}
\]

At the selected time,

\[
1
\le
\|v_j(0)\|_{L^{3,\infty}}
\le L_*.
\]

After the usual subsequence split, this note treats the energy-efficient
branch

\[
\sup_{j,s}\|v_j(s)\|_2^2\le M,
\qquad
\varepsilon_j\to0.
\]

The record-high choice does not remove any energy, geometry, or clock
alternative; it strengthens their common backward history.

## 2. Global heat-filter energy and the canonical defect scale

Use the centred Gaussian filter

\[
\Gamma_\ell(y)
:=
(2\pi\ell^2)^{-3/2}
\exp\left(-\frac{|y|^2}{2\ell^2}\right),
\qquad
\overline v_\ell:=\Gamma_\ell*v.
\]

Define

\[
\tau_\ell(v,v)
:=
\overline{v\otimes v}_\ell
-\overline v_\ell\otimes\overline v_\ell,
\]

\[
k_\ell[v]
:=
\frac12
\left(
\overline{|v|^2}_\ell-|\overline v_\ell|^2
\right),
\qquad
\Pi_\ell[v]
:=
-\tau_{\ell,ij}\partial_j\overline v_{\ell,i},
\]

and the global subgrid energy

\[
\mathcal K_\ell[v(s)]
:=
\int_{\mathbb R^3}k_\ell(v(s);y)\,dy
=
\frac12
\left(
\|v(s)\|_2^2-\|\overline v_\ell(s)\|_2^2
\right).
\]

The global version of the exact subgrid balance is

\[
\boxed{
\frac d{ds}\mathcal K_\ell[v]
=
\int_{\mathbb R^3}\Pi_\ell[v]\,dy
-
\varepsilon
\int_{\mathbb R^3}d_\ell[v]\,dy,
}
\]

where

\[
d_\ell[v]
:=
\overline{|\nabla v|^2}_\ell
-|\nabla\overline v_\ell|^2
\ge0.
\]

This identity also follows directly by subtracting the filtered global
energy identity from the exact global energy identity, so no spatial or
pressure boundary term is present.

For the Gaussian multiplier,

\[
\mathcal K_\ell[v]
=
\frac12
\int_{\mathbb R^3}
\left(1-e^{-\ell^2|\xi|^2}\right)
|\widehat v(\xi)|^2\,d\xi.
\]

It is continuous and nondecreasing in \(\ell\), with
\(\mathcal K_0[v]=0\), and

\[
\boxed{
\mathcal K_\ell[v]
\le
\frac{\ell^2}{2}\|\nabla v\|_2^2.
}
\]

Now suppose the terminal trace-defect measure satisfies

\[
\Delta_\chi
:=
\int\chi\,d\mathcal T_0>0,
\qquad
0\le\chi\le1,
\]

for some \(\chi\in C_c^\infty\). Fixed-filter convergence and then the
zero-filter limit give

\[
\lim_{\ell\downarrow0}\lim_{j\to\infty}
\int\chi k_\ell(v_j(0);y)\,dy
=
\frac{\Delta_\chi}{2}.
\]

Fix

\[
\delta:=\frac{\Delta_\chi}{8}.
\]

For every sufficiently small fixed \(\ell>0\), the local filtered energy,
and hence the global \(\mathcal K_\ell[v_j(0)]\), exceeds \(\delta\)
eventually. By continuity and monotonicity there is a first scale
\(\ell_j>0\) such that

\[
\boxed{
\mathcal K_{\ell_j}[v_j(0)]=\delta.
}
\]

For every fixed \(\rho>0\) small enough,
\(\ell_j\le\rho\) eventually. Hence

\[
\ell_j\longrightarrow0.
\]

Unlike an arbitrary diagonal filter, this first-crossing scale cannot be
chosen artificially slowly relative to \(\varepsilon_j\).

## 3. Endpoint Lorentz flux ceiling

### Lemma 1: a three-norm \(L^{3,1}\) estimate

Suppose a measurable vector field \(f\) satisfies

\[
\|f\|_{L^{3,\infty}}\le A,
\qquad
\|f\|_\infty\le B,
\qquad
\|f\|_2\le C_2.
\]

Then

\[
\boxed{
\|f\|_{L^{3,1}}
\le
C A
\left[
1+
\log_+\left(
\frac{C_2^6B^3}{A^9}
\right)
\right].
}
\]

The assertion is trivial when \(A=0\).

#### Proof

The decreasing rearrangement obeys

\[
f^*(r)
\le
\min\{B,Ar^{-1/3},C_2r^{-1/2}\}.
\]

Put

\[
r_0:=\left(\frac AB\right)^3,
\qquad
r_1:=\left(\frac{C_2}{A}\right)^6.
\]

When \(r_0<r_1\), split the defining \(L^{3,1}\) integral at
\(r_0,r_1\). The \(L^\infty\) and \(L^2\) tails each contribute at most a
constant times \(A\), while the weak-\(L^3\) middle contributes

\[
A\log(r_1/r_0).
\]

When \(r_0\ge r_1\), direct interpolation between \(L^2\) and \(L^\infty\)
gives a bound by a constant times \(A\). Combining the cases proves the
claim.

### Theorem 1: critical logarithmic flux-rate bound

Let

\[
E:=\|v\|_2^2,
\qquad
L:=\|v\|_{L^{3,\infty}}>0.
\]

Then

\[
\boxed{
\left|
\int_{\mathbb R^3}\Pi_\ell[v]\,dy
\right|
\le
\frac{C_G L^3}{\ell}
\log\left(
e+\frac{C_GE}{L^2\ell}
\right).
}
\]

### Proof

Weak Lorentz Hölder and convolution boundedness give

\[
\|\tau_\ell(v,v)\|_{L^{3/2,\infty}}
\le C_GL^2.
\]

For \(f=\nabla\overline v_\ell\), Lorentz Young, ordinary Young, and the
Gaussian kernel scalings give

\[
\|f\|_{L^{3,\infty}}
\le\frac{C_GL}{\ell},
\]

\[
\|f\|_\infty
\le\frac{C_GL}{\ell^2},
\]

\[
\|f\|_2
\le\frac{C_G\sqrt E}{\ell}.
\]

Lemma 1 therefore yields

\[
\|\nabla\overline v_\ell\|_{L^{3,1}}
\le
\frac{C_GL}{\ell}
\log\left(
e+\frac{C_GE}{L^2\ell}
\right).
\]

The \(L^{3/2,\infty}\)--\(L^{3,1}\) pairing now proves the flux bound.

The logarithm comes only from the exact endpoint Lorentz pairing. Removing
it requires additional cancellation or structure; ordinary energy and weak
\(L^3\) interpolation do not remove it.

## 4. Residence and viscous-scale separation

For a record-high carrier, Theorem 1 and the monotonicity of

\[
L^3\log\left(e+\frac{C M}{L^2\ell}\right)
\]

in \(L>0\) give the uniform instantaneous bound

\[
\left|
\int\Pi_{\ell_j}[v_j(s)]\,dy
\right|
\le
B_j,
\]

\[
B_j
:=
\frac{C_0}{\ell_j}
\log\left(e+\frac{C_1}{\ell_j}\right)
\]

throughout the carrier past.

Define

\[
h_j:=\frac{\delta}{2B_j}.
\]

Since \(\ell_j\to0\), one has \(h_j\to0\), so
\([-h_j,0]\) lies in the carrier past eventually.

### Theorem 2: fixed defect forces terminal residence

For every \(s\in[-h_j,0]\),

\[
\boxed{
\mathcal K_{\ell_j}[v_j(s)]
\ge\frac{\delta}{2}.
}
\]

Consequently

\[
\boxed{
\varepsilon_j
\int_{-h_j}^{0}\|\nabla v_j(s)\|_2^2\,ds
\ge
\frac{c\,\varepsilon_j}
{\ell_j\log(e+C/\ell_j)}.
}
\]

Since the left side is bounded above by the normalised physical dissipation
on any fixed terminal carrier interval, terminal absolute continuity forces

\[
\boxed{
\frac{\varepsilon_j}
{\ell_j\log(e+C/\ell_j)}
\longrightarrow0.
}
\]

### Proof

For \(s\le0\), the global subgrid identity and \(d_{\ell_j}\ge0\) give

\[
\begin{aligned}
\delta-\mathcal K_{\ell_j}[v_j(s)]
&=
\int_s^0\!\!\int\Pi_{\ell_j}[v_j]\,dy\,d\sigma
-
\varepsilon_j
\int_s^0\!\!\int d_{\ell_j}[v_j]\,dy\,d\sigma\\
&\le B_j(0-s).
\end{aligned}
\]

The definition of \(h_j\) proves the first claim. The Gaussian spectral
inequality then gives

\[
\|\nabla v_j(s)\|_2^2
\ge
\frac{2\mathcal K_{\ell_j}[v_j(s)]}{\ell_j^2}
\ge
\frac{\delta}{\ell_j^2}
\]

throughout that interval. Thus

\[
\varepsilon_j
\int_{-h_j}^0\|\nabla v_j\|_2^2\,ds
\ge
\frac{\varepsilon_j\delta h_j}{\ell_j^2}
=
\frac{\varepsilon_j\delta^2}
{2B_j\ell_j^2},
\]

which has the stated lower bound. The dissipation-collapse theorem makes
this quantity tend to zero and proves the necessary scale separation.

## 5. Physical interpretation

Set

\[
r_j:=R_j\ell_j.
\]

The local Reynolds number based on carrier amplitude \(a_j\) and physical
defect length \(r_j\) is

\[
\operatorname{Re}_j(r_j)
:=
\frac{a_jr_j}{\nu}
=
\frac{\ell_j}{\varepsilon_j}.
\]

Theorem 2 is exactly

\[
\boxed{
\operatorname{Re}_j(r_j)
\log\left(
e+C\frac{R_j}{r_j}
\right)
\longrightarrow\infty.
}
\]

The physical residence time is

\[
\tau_jh_j
\gtrsim
\frac{\tau_j\ell_j}
{\log(e+C/\ell_j)}.
\]

During this time a fixed fraction of the normalised defect energy remains
above the canonical filter boundary. All terms multiply by
\(b_j\asymp e_j\ge c>0\) under physical pullback.

This is stronger than merely locating some slowly shrinking diagonal filter:
\(\ell_j\) is the first scale at which the fixed global defect amount
appears. The conclusion excludes terminal trace defects whose canonical
length has bounded logarithmically corrected Reynolds number.

## 6. Surviving cross-carrier power ledger

The residence theorem rules out the overly fast timing of the fixed-viscosity
shell survivor under a uniform record-high critical ceiling. It does not yet
relate different carrier normalisations.

The powers

\[
\ell_j:=2^{-j},
\qquad
\varepsilon_j:=2^{-2j}
\]

satisfy

\[
B_j\asymp2^j j,
\qquad
h_j\asymp\frac{2^{-j}}{j},
\]

and

\[
\varepsilon_j\ell_j^{-2}h_j
\asymp
\frac{2^{-j}}{j}.
\]

Hence the sum of the viscous lower charges forced by the residence theorem is
finite:

\[
\sum_j
\varepsilon_j\ell_j^{-2}h_j
<\infty.
\]

To express the same ledger in the energy-efficient physical powers, take
\(e_j\asymp1\). Since

\[
\varepsilon_j\asymp\frac{\nu}{m_j},
\qquad
a_j\asymp m_j^3,
\qquad
R_j\asymp m_j^{-2},
\qquad
\tau_j\asymp m_j^{-5},
\]

the choice \(\varepsilon_j=2^{-2j}\) corresponds, up to fixed powers of
\(\nu\), to

\[
m_j\asymp2^{2j},
\quad
a_j\asymp2^{6j},
\quad
R_j\asymp2^{-4j},
\quad
\tau_j\asymp2^{-10j}.
\]

The physical canonical defect length and residence time are then

\[
r_j=R_j\ell_j\asymp2^{-5j},
\]

\[
\tau_jh_j
\asymp
\frac{2^{-11j}}{j}.
\]

At the level of this power ledger, these physical intervals can be disjoint
and accumulate at \(T^*\), while the order-\(b_j\) transfer floor remains
fixed and the forced viscous lower charges are summable.

This is a scaling ledger, not a Navier--Stokes solution and not a proved
cross-event ancestry. It shows sharply that the record-high ceiling,
endpoint flux estimate, residence theorem, energy efficiency, and terminal
absolute continuity still do not contradict a sufficiently accelerating
sequence of carrier normalisations.

## 7. Route consequence

The terminal trace-defect branch now obeys an NSE-specific necessary law:

\[
\boxed{
\text{first-record weak-}L^3\text{ ceiling}
\Longrightarrow
\text{logarithmic flux residence}
\Longrightarrow
\text{log-corrected inertial defect scale}.
}
\]

The next closing theorem must add at least one of:

1. a cross-event ancestry inequality forcing
   \(\ell_j\) to decay no faster than the effective viscosity
   \(\varepsilon_j\) can afford;
2. a fresh-energy or fresh-enstrophy assignment for successive canonical
   defect scales;
3. cancellation improving the endpoint flux ceiling enough to defeat the
   surviving power ledger;
4. a spatial recentering theorem linking the global canonical defect scale
   back to the retained amplitude layer; or
5. coherent-trace propagation and ancient-Euler rigidity in the
   \(\mathcal T_0=0\), \(V(0)\ne0\) branch.

The energy-vanishing nine cells remain separate. No alternative A--D of the
Clay problem is proved.
