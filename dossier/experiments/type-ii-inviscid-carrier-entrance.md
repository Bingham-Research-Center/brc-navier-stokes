# Type-II amplitude layers enter an inviscid carrier ledger

- **Experiment:** EXP-TYPE-II-INVISCID-CARRIER-001
- **Route:** ROUTE-R3C
- **Status:** complete analytic reduction with sharp kinematic survivor
- **Clay status:** unsolved

This note treats the unforced whole-space equation. It does not assume the
weak-\(L^3\) Type-I ceiling or the conditional Besov genealogy used in R3B.
Here “weak-\(L^3\) Type II” means precisely that
\(\|u(t_j)\|_{L^{3,\infty}}\to\infty\) along terminal times; other Type-I/II
conventions require a separate comparison.

## Verdict

Every sequence on which the velocity weak-\(L^3\) norm diverges has a
near-extremising amplitude layer whose amplitude, volume radius, energy, and
turnover time are fixed up to universal constants. Nondimensionalising at that
layer gives

\[
\partial_s v_j+v_j\cdot\nabla v_j
=-\nabla q_j+\varepsilon_j\Delta v_j,
\qquad
\varepsilon_j\asymp\frac{\nu}{m_j}\longrightarrow0.
\]

The rescaled past horizon tends to infinity. After taking a subsequence, the
entrance is classified by:

1. bounded or divergent normalised global energy;
2. diffuse, partially concentrated, or tight layer energy at the carrier
   volume scale; and
3. zero, finite-positive, or infinite remaining turnover horizon.

This is an exhaustive scalar-measure and clock reduction. It is not an Euler
profile theorem: strong space-time compactness can still fail through vector
oscillation, frequency escape, nonlinear Reynolds stress, or anomalous
dissipation, and even space-time convergence can lose a carrier confined to
the selected time trace.

For a coherent Euler-normalised similarity core, a repository adaptation of
the Constantin--Ignatova--Vicol strain argument gives the lower exponent
\(\gamma\ge2/5\). Their current v3 preprint gives, under a separate
inner/outer vorticity decomposition, \(\gamma\le1/2\). Hence the Type-II part
of that jointly conditioned cell is

\[
\frac25\le\gamma<\frac12.
\]

The same preprint excludes the subparabolic part for broad outgoing and
axisymmetric globally self-similar Euler profiles under its exact standing
assumptions. It does not exclude non-self-similar, noncompact, non-outgoing,
or defect-carrying Navier--Stokes entrances.

Finally, a smooth compactly supported divergence-free path realises the
energy identity, finite total dissipation, diverging weak \(L^3\), and the
necessary vorticity blow-up integral throughout
\(2/5\le\gamma<1/2\). It is not a Navier--Stokes solution. It proves that
energy, scaling, and the necessary vorticity divergence do not close R3C.

## 1. Exact amplitude-layer theorem

Let \(u\) be a smooth finite-energy solution on
\(\mathbb R^3\times[0,T^*)\) of

\[
\partial_tu+u\cdot\nabla u=-\nabla p+\nu\Delta u,
\qquad
\nabla\cdot u=0,
\qquad
\nu>0.
\]

Use the weak-\(L^3\) quasi-norm convention

\[
m(t)
:=
\sup_{\lambda>0}
\lambda\,\bigl|\{x:|u(x,t)|>\lambda\}\bigr|^{1/3}
\]

and put \(E_0=\|u(0)\|_2^2\). Suppose

\[
t_j\uparrow T^*,
\qquad
m_j:=m(t_j)\longrightarrow\infty.
\]

For every \(j\), choose \(a_j>0\) such that

\[
a_j^3\bigl|\{|u(t_j)|>a_j\}\bigr|
\ge\frac12m_j^3
\]

and define

\[
A_j:=\{a_j<|u(t_j)|\le2a_j\},
\qquad
e_j:=\int_{A_j}|u(x,t_j)|^2\,dx,
\qquad
R_j:=|A_j|^{1/3}.
\]

### Theorem 1: layer ledger

There are absolute constants \(0<c<C<\infty\) such that

\[
c\frac{m_j^3}{a_j^3}
\le |A_j|
\le C\frac{m_j^3}{a_j^3},
\qquad
c\frac{m_j^3}{a_j}
\le e_j
\le C\frac{m_j^3}{a_j},
\]

and therefore

\[
a_j\asymp\frac{m_j^3}{e_j},
\qquad
R_j\asymp\frac{e_j}{m_j^2},
\qquad
a_jR_j\asymp m_j.
\]

Moreover,

\[
\|\nabla u(t_j)\|_2^2
\gtrsim a_jm_j
\asymp\frac{m_j^4}{e_j}
\ge\frac{m_j^4}{E_0}.
\]

At every smooth time the same argument applies, so the energy identity yields
the endpoint occupation estimate

\[
\boxed{
\int_0^{T^*}m(t)^4\,dt
\lesssim
E_0\int_0^{T^*}\|\nabla u(t)\|_2^2\,dt
\le\frac{E_0^2}{2\nu}.
}
\]

Thus Type-II weak-\(L^3\) growth is temporally sparse in \(m^4dt\), but it is
not excluded.

### Proof

Write

\[
\mu_j(\lambda)=|\{|u(t_j)|>\lambda\}|.
\]

The choice of \(a_j\) and the definition of \(m_j\) give

\[
\mu_j(a_j)\ge\frac{m_j^3}{2a_j^3},
\qquad
\mu_j(2a_j)\le\frac{m_j^3}{8a_j^3}.
\]

Consequently,

\[
\frac{3m_j^3}{8a_j^3}
\le |A_j|
=\mu_j(a_j)-\mu_j(2a_j)
\le\frac{m_j^3}{a_j^3}.
\]

Since \(a_j<|u|\le2a_j\) on \(A_j\),

\[
a_j^2|A_j|
\le e_j
\le4a_j^2|A_j|.
\]

This proves the volume, energy, amplitude, and radius comparisons. Also,

\[
\|u(t_j)\|_6^2
\ge
\left(\int_{A_j}|u(t_j)|^6\,dx\right)^{1/3}
\ge a_j^2|A_j|^{1/3}
\gtrsim a_jm_j.
\]

The homogeneous Sobolev inequality gives the gradient bound. Since
\(e_j\le E_0\), integration against the exact smooth energy identity proves
the occupation estimate.

## 2. Carrier nondimensionalisation

Set the turnover time

\[
\tau_j:=\frac{R_j}{a_j}
\asymp\frac{e_j^2}{m_j^5}.
\]

It tends to zero because \(e_j\le E_0\) and \(m_j\to\infty\). For a centre
\(x_j\), define

\[
v_j(y,s)
:=
\frac1{a_j}
u(x_j+R_jy,t_j+\tau_js),
\qquad
q_j(y,s)
:=
\frac1{a_j^2}
p(x_j+R_jy,t_j+\tau_js).
\]

Direct substitution gives

\[
\partial_sv_j+v_j\cdot\nabla v_j
=-\nabla q_j+\varepsilon_j\Delta v_j,
\qquad
\varepsilon_j:=\frac{\nu}{a_jR_j}
\asymp\frac{\nu}{m_j}\longrightarrow0.
\]

The time domain is

\[
-\frac{t_j}{\tau_j}<s<
H_j,
\qquad
H_j:=
\frac{T^*-t_j}{\tau_j}
\asymp
(T^*-t_j)\frac{m_j^5}{e_j^2}.
\]

Because \(t_j/\tau_j\to\infty\), every carrier has an arbitrarily long
rescaled past. After a subsequence,

\[
H_j\longrightarrow H\in[0,\infty].
\]

At \(s=0\), the rescaled layer

\[
\widetilde A_j:=\frac{A_j-x_j}{R_j}
\]

has measure one, and \(1<|v_j|\le2\) there. Furthermore,

\[
\|v_j(\cdot,s)\|_2^2
\le
\frac{E_0}{a_j^2R_j^3}
\asymp
\frac{E_0}{e_j}
=:\chi_j
\]

whenever the corresponding physical time lies in \([0,T^*)\).

The key point is structural: normalising both amplitude and volume radius is
not a Navier--Stokes symmetry. Type II makes the resulting Reynolds number
\(a_jR_j/\nu\) diverge and pushes the carrier equation towards Euler.

## 3. Exhaustive energy, geometry, and clock split

After a further subsequence, exactly one of

\[
\sup_j\chi_j<\infty
\qquad\hbox{or}\qquad
\chi_j\to\infty
\]

holds. These are respectively the **energy-efficient** and
**energy-vanishing** layer branches.

To retain geometry without choosing a fixed centre, form the probability
measure

\[
d\sigma_j(x)
:=
\frac{|u(x,t_j)|^2\mathbf1_{A_j}(x)}{e_j}\,dx
\]

and its carrier-scale concentration function

\[
Q_j(K)
:=
\sup_{x\in\mathbb R^3}
\sigma_j(B_{KR_j}(x)),
\qquad
K>0.
\]

A diagonal subsequence makes \(Q_j(K)\) converge for every positive rational
\(K\). With

\[
\theta
:=
\lim_{\substack{K\to\infty\\K\in\mathbb Q}}\,\lim_{j\to\infty}Q_j(K),
\]

exactly one of the following occurs:

1. **Diffuse:** \(\theta=0\). No fixed multiple of \(R_j\), around any moving
   centre, captures positive layer-energy fraction.
2. **Partial concentration:** \(0<\theta<1\). A positive core can be centred,
   but a positive fraction remains in separated, hierarchical, or escaping
   pieces.
3. **Tight:** \(\theta=1\). For every \(\delta>0\), some fixed \(K\) and
   centres \(x_j\) satisfy
   \(\sigma_j(B_{KR_j}(x_j))\ge1-\delta\) eventually.

Monotonicity of \(Q_j\) proves these assertions directly. No connectedness,
single-core, tube, sheet, or point geometry has been assumed.

The clock limit independently has the three cases

\[
H=0,
\qquad
0<H<\infty,
\qquad
H=\infty.
\]

They mean that the chosen layer has respectively no forward turnover before
the candidate terminal time, an order-one number of turnovers, or
arbitrarily many turnovers. The \(2\times3\times3\) ledger is exhaustive
after subsequence extraction and permits arbitrary rate and scale
oscillation.

## 4. The exact compactness defect

In the energy-efficient branch, \(v_j\) is bounded in global \(L^2\) on every
fixed rescaled time interval. In a partial or tight geometry branch, centres
can retain positive layer energy locally. This still gives only weak
compactness.

If, in addition, a subsequence is strongly compact in
\(L^2_{\mathrm{loc}}(dy\,ds)\), then

\[
v_j\otimes v_j\longrightarrow V\otimes V
\]

locally in \(L^1\), while
\(\varepsilon_j\Delta v_j\to0\) distributionally. The limit is a
finite-energy ancient Euler solution on its limiting time interval. To prove
that it is nonzero, one additionally needs either strong trace compactness at
\(s=0\) or persistence of a fixed amount of carrier energy on a positive
rescaled time interval. Snapshot layer mass alone does not provide this.

Without that strong compactness, the exact obstruction is a Reynolds defect

\[
\mathcal R
:=
\operatorname*{w\!-\!lim}_{j\to\infty}
(v_j\otimes v_j)-V\otimes V,
\]

possibly accompanied by a limiting viscous-dissipation defect. Scalar layer
tightness does not control either. Frequency oscillation can make \(V=0\)
while the normalised layer energy stays positive, and temporal concentration
can make a nonzero \(s=0\) carrier disappear from the space-time limit.

Thus the first high-consequence R3C unknown is precise: either promote at
least one carrier branch to a nonzero Euler object with enough structure for
rigidity, or show that every failure of compactness pays a non-reusable
Navier--Stokes charge.

## 5. Coherent self-similar subbranch

Put \(\tau=T^*-t\). The Euler-normalised similarity ledger is

\[
\omega_{\rm in}(x,t)
\sim
\tau^{-1}\Omega\!\left(\frac{x-x(t)}{\tau^\gamma}\right),
\qquad
u_{\rm in}(x,t)
\sim
\tau^{\gamma-1}U\!\left(\frac{x-x(t)}{\tau^\gamma}\right).
\]

For nonzero profiles with the displayed norms finite,

\[
\|u_{\rm in}\|_{L^{3,\infty}}
\asymp\tau^{2\gamma-1},
\qquad
\|u_{\rm in}\|_2^2
\asymp\tau^{5\gamma-2},
\qquad
\|\omega_{\rm in}\|_2^2
\asymp\tau^{3\gamma-2}.
\]

Hence finite energy requires \(\gamma\ge2/5\), the core is
energy-efficient only at \(\gamma=2/5\), and Type-II weak-\(L^3\) growth
requires \(\gamma<1/2\).

### Repository theorem: viscous two-fifths gate

Assume a smooth finite-energy Navier--Stokes solution blows up at \(T^*\) and
for some \(\gamma>0\)

\[
\sup_{t<T^*}
(T^*-t)^{1+\gamma}
\|\nabla\omega(t)\|_\infty
<\infty.
\]

Then

\[
\boxed{\gamma\ge\frac25.}
\]

The proof adapts the instantaneous strain split in the
[Constantin--Ignatova--Vicol v3 preprint](https://arxiv.org/abs/2602.17570).
For every radius \(R>0\), their Biot--Savart calculation gives

\[
|\alpha(x,t)|
\lesssim
R\|\nabla\omega(t)\|_\infty
+R^{-5/2}\|u(t)\|_2.
\]

Optimising in \(R\), using the nonincreasing Navier--Stokes energy, yields

\[
\|\alpha(t)\|_\infty
\lesssim
(T^*-t)^{-5(1+\gamma)/7}.
\]

For \(\gamma<2/5\) this is time-integrable. The viscous vorticity magnitude
obeys the Kato inequality

\[
(\partial_t+u\cdot\nabla-\nu\Delta)|\omega|
\le\alpha|\omega|.
\]

The maximum principle bounds \(\|\omega(t)\|_\infty\) up to \(T^*\), so the
standard vorticity continuation criterion rules out blow-up. The source
states the argument for Euler; the favourable viscous extension above is a
repository theorem and awaits independent external review.

### Current preprint boundaries

The same v3 preprint proves that if

\[
\omega=\omega_{\rm in}+\omega_{\rm out},
\qquad
\operatorname{supp}\omega_{\rm in}
\subset B_{C\tau^\gamma}(x(t)),
\]

\[
\|\omega_{\rm in}(t)\|_2
\le C\tau^{-1+3\gamma/2},
\qquad
\omega_{\rm out}\in L^4_tL^2_x,
\]

then blow-up implies \(\gamma\le1/2\). Combining this source claim with the
repository lower gate gives \([2/5,1/2]\); the Type-II portion is
\([2/5,1/2)\).

For \(\gamma<1/2\), the viscosity coefficient in similarity variables is
\(\nu\tau^{1-2\gamma}\to0\). A sufficiently compact coherent limit therefore
solves the stationary Euler profile equation. Under the preprint's exact
normalisation and far-field assumptions, either its local outgoing property
or axisymmetry with a \(C^2\) profile forces \(\gamma\ge1/2\). A Type-II
survivor must therefore fail at least one of profile convergence, far-field
control, outgoing geometry, axisymmetry, or the required smoothness.

These are preprint claims, not established theorems in this repository.

## 6. Sharp energy-class survivor

Choose a nonzero compactly supported smooth divergence-free
\(\phi:\mathbb R^3\to\mathbb R^3\) with nonzero curl. Fix

\[
\frac25\le\gamma<\frac12,
\qquad
R(t)=(T^*-t)^\gamma,
\qquad
c_\phi=\frac{\|\nabla\phi\|_2^2}{\|\phi\|_2^2}.
\]

Let \(e(t)>0\) solve

\[
e'(t)=-2\nu c_\phi\frac{e(t)}{R(t)^2}
\]

and define

\[
u_{\rm kin}(x,t)
:=
\frac{\sqrt{e(t)}}{\|\phi\|_2R(t)^{3/2}}
\phi\!\left(\frac{x}{R(t)}\right).
\]

Because \(2\gamma<1\),

\[
e(t)
=
e(0)\exp\!\left(
-2\nu c_\phi\int_0^t(T^*-s)^{-2\gamma}\,ds
\right)
\longrightarrow e_*>0.
\]

The path is smooth, compactly supported, and divergence-free at every
\(t<T^*\), and it satisfies the exact scalar energy identity

\[
\|u_{\rm kin}(t)\|_2^2=e(t),
\qquad
\|\nabla u_{\rm kin}(t)\|_2^2
=c_\phi\frac{e(t)}{R(t)^2},
\qquad
\frac d{dt}\|u_{\rm kin}\|_2^2
+2\nu\|\nabla u_{\rm kin}\|_2^2=0.
\]

Its remaining ledgers are

\[
\|u_{\rm kin}(t)\|_{L^{3,\infty}}
\asymp R(t)^{-1/2}
\asymp(T^*-t)^{-\gamma/2},
\]

so

\[
\int_0^{T^*}
\|u_{\rm kin}(t)\|_{L^{3,\infty}}^4\,dt<\infty.
\]

\[
\|\omega_{\rm kin}(t)\|_\infty
\asymp R(t)^{-5/2}
\asymp(T^*-t)^{-5\gamma/2},
\qquad
\int_0^{T^*}\|\omega_{\rm kin}(t)\|_\infty\,dt=\infty,
\]

while

\[
\int_0^{T^*}
\|\nabla u_{\rm kin}(t)\|_2^2\,dt<\infty.
\]

Its selected amplitude layer is energy-efficient and tight. At
\(\gamma=2/5\), its velocity and vorticity amplitudes have exactly the
Euler-normalised powers \(\tau^{-3/5}\) and \(\tau^{-1}\), and its turnover
horizon is order one. For \(\gamma>2/5\), the horizon tends to infinity and
the vorticity grows faster than the Euler-normalised rate.

This path is **not** a Navier--Stokes solution; it need not satisfy the
momentum equation for any pressure. It is an exact countermodel only to
arguments using divergence freedom, energy equality, Sobolev scaling, and
the necessary vorticity-integral divergence without the evolution equation.

## 7. What remains

The entrance theorem closes the vague phrase “handle Type II” into a finite
first ledger, but no ledger cell is yet excluded for arbitrary
Navier--Stokes data. The next major theorem must do at least one of:

1. produce strong carrier compactness with trace persistence and then
   classify every resulting nonzero finite-energy ancient Euler object;
2. assign a positive, non-reusable charge to Reynolds stress, anomalous
   dissipation, fragmentation, or energy escape;
3. prove a clock law excluding the zero- or infinite-horizon defect cells; or
4. force all first singularities back into a previously controlled critical
   class.

No alternative A--D of the Clay problem is proved.
