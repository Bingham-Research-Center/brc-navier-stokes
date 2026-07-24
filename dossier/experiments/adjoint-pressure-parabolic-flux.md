# A parabolic coefficient tail forces an annulus, inherited high energy, or signed NSE flux

- **Experiment:** EXP-ADJOINT-PRESSURE-PARABOLIC-FLUX-001
- **Route:** ROUTE-R3B
- **Status:** independently reviewed conditional same-trajectory theorem
  plus exact algebraic shell-ledger obstruction
- **Review:** [valid and nonduplicative after two precision
  repairs](../review-response-adjoint-pressure-parabolic-flux-2026-07-24.md)
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** independently reviewed
  [parabolic coefficient-tail theorem](adjoint-pressure-parabolic-coefficient-tail.md),
  [parabolic tail-ancestry theorem](adjoint-pressure-parabolic-ancestry.md),
  and the earlier
  [frequency-energy-flux audit](frequency-energy-flux.md)

The reviewed adjoint-pressure theorem forces actual physical
dissipation above the parabolic coefficient cutoff

\[
\Lambda_j
=
\frac{\kappa h_j^{-1/2}}{\sigma_j}.
\]

The kinematic ancestry survivor hid every such payment at a frequency
arbitrarily larger than \(\Lambda_j\).  That freedom is no longer free
for a Navier--Stokes solution.  The exact sharp high-pass energy identity
gives the following exhaustive alternative at every factor \(R>1\):

\[
\boxed{
\begin{array}{ll}
\textnormal{(A)}
&
\displaystyle
\int_{I_j}
\|\nabla Q_{\Lambda_j<|\xi|\le R\Lambda_j}v\|_2^2\,dt
\ge \frac{T_j}{2},
\\[8pt]
\textnormal{(B)}
&
\displaystyle
\|Q_{>R\Lambda_j}v(t_j^-)\|_2^2
\ge \frac{\nu T_j}{2},
\\[8pt]
\textnormal{(C)}
&
\displaystyle
\Phi_{R\Lambda_j}(I_j)
\ge \frac{\nu T_j}{4},
\end{array}}
\tag{1}
\]

where \(I_j=(t_j^-,t_j^+)\),

\[
T_j
=
\frac{c_\kappa}{C_\chi^2}
\sigma_jh_j^{-3},
\qquad
C_\chi:=\|1-\chi\|_\infty,
\tag{2}
\]

and positive \(\Phi_K\) means signed nonlinear energy input into
frequencies \(>K\).

Thus an actual NSE trajectory cannot merely place the reviewed
dissipation arbitrarily far above the cutoff without paying one of:

1. a comparable-annulus charge;
2. an inherited high-frequency state at the entrance to the event
   interval; or
3. positive nonlinear frequency flux across the farther boundary.

This is a genuine PDE consequence absent from the kinematic survivor.
It does not yet close event-index reuse.  An exact conservative shell
ledger below shows why: one almost lossless cascade can cross
arbitrarily many boundaries, making every cumulative signed flux
positive while dissipating almost all of its energy only at the final
shell.  The ledger satisfies all integrated shell-energy balances and
fits arbitrarily many natural heat clocks into one event interval, but
it is **not** a Navier--Stokes solution.  The next missing theorem is
therefore a quantitative flux-decrement, locality, cascade-speed, or
inherited-state ancestry law.

## 1. Smooth and sharp physical tails

Fix one smooth radial multiplier \(\chi\) such that

\[
\chi(\xi)=1\quad(|\xi|\le1),
\qquad
\chi(\xi)=0\quad(|\xi|\ge2),
\tag{3}
\]

and put

\[
S_\Lambda:=\chi(D/\Lambda),
\qquad
C_\chi:=\|1-\chi\|_{L^\infty}.
\tag{4}
\]

Let

\[
Q_{>K}
:=
\mathbf 1_{\{|\xi|>K\}}(D)
\tag{5}
\]

be the orthogonal sharp high-pass projector, and write

\[
Q_{\Lambda<|\xi|\le R\Lambda}
:=
Q_{>\Lambda}-Q_{>R\Lambda}.
\tag{5a}
\]

For a time interval
\(I=(a,b)\), define

\[
D^\chi_{>\Lambda}(I)
:=
\int_I
\|\nabla(I-S_\Lambda)v(t)\|_2^2\,dt
\tag{6}
\]

and

\[
D^\sharp_{>K}(I)
:=
\int_I
\|\nabla Q_{>K}v(t)\|_2^2\,dt.
\tag{7}
\]

The multiplier \(1-\chi(\xi/\Lambda)\) vanishes on
\(\{|\xi|\le\Lambda\}\).  Plancherel therefore gives the exact
comparison

\[
\boxed{
D^\chi_{>\Lambda}(I)
\le
C_\chi^2D^\sharp_{>\Lambda}(I).
}
\tag{8}
\]

Consequently, any smooth-tail floor

\[
D^\chi_{>\Lambda}(I)\ge P
\tag{9}
\]

implies the sharp floor

\[
\boxed{
D^\sharp_{>\Lambda}(I)
\ge
T,
\qquad
T:=\frac{P}{C_\chi^2}.
}
\tag{10}
\]

For every \(R>1\), orthogonality gives the exact split

\[
\boxed{
D^\sharp_{>\Lambda}(I)
=
D^\sharp_{\Lambda<|\xi|\le R\Lambda}(I)
+
D^\sharp_{>R\Lambda}(I).
}
\tag{11}
\]

No smooth-partition overlap or Littlewood--Paley constant occurs in
(11).

## 2. Exact signed high-pass energy identity

Let \(v\) be a smooth finite-energy solution of the unforced
Navier--Stokes equations on a neighbourhood of
\(\mathbb R^3\times[a,b]\):

\[
\partial_tv-\nu\Delta v
=
-\mathbb P\operatorname{div}(v\otimes v),
\qquad
\nabla\cdot v=0.
\tag{12}
\]

Put

\[
E_K(t)
:=
\|Q_{>K}v(t)\|_2^2
\tag{13}
\]

and define the signed nonlinear input into the sharp high-pass region by

\[
\boxed{
\Phi_K(I)
:=
-
\int_a^b
\left\langle
Q_{>K}\mathbb P\operatorname{div}(v\otimes v),
Q_{>K}v
\right\rangle\,dt.
}
\tag{14}
\]

Applying \(Q_{>K}\) to (12), pairing with \(Q_{>K}v\), and integrating
in time gives

\[
\boxed{
\Phi_K(I)
=
\frac12\bigl(E_K(b)-E_K(a)\bigr)
+
\nu D^\sharp_{>K}(I).
}
\tag{15}
\]

The sign convention in (14) is therefore unambiguous: positive
\(\Phi_K\) is nonlinear energy input into \(>K\), while a negative value
is nonlinear output.

For the selected preterminal genealogy intervals the common physical
trajectory is smooth, so (15) is a classical identity.  No endpoint
testing of a rough suitable solution is used.

## 3. The annulus--inheritance--flux theorem

### Theorem

Assume (9) on one smooth Navier--Stokes interval \(I=(a,b)\).  Fix any
\(R>1\), and let \(T=P/C_\chi^2\).  At least one of the following holds:

\[
\boxed{
D^\sharp_{\Lambda<|\xi|\le R\Lambda}(I)
\ge
\frac{T}{2};
}
\tag{16}
\]

\[
\boxed{
E_{R\Lambda}(a)
\ge
\frac{\nu T}{2};
}
\tag{17}
\]

\[
\boxed{
\Phi_{R\Lambda}(I)
\ge
\frac{\nu T}{4}.
}
\tag{18}
\]

### Proof

If (16) holds, there is nothing to prove.  Otherwise, (10)--(11) give

\[
D^\sharp_{>R\Lambda}(I)
>
\frac{T}{2}.
\tag{19}
\]

If (17) holds, again there is nothing to prove.  Otherwise,

\[
E_{R\Lambda}(a)
<
\frac{\nu T}{2}.
\tag{20}
\]

Since \(E_{R\Lambda}(b)\ge0\), the exact identity (15), (19), and (20)
give

\[
\begin{aligned}
\Phi_{R\Lambda}(I)
&=
\frac12
\left(
E_{R\Lambda}(b)-E_{R\Lambda}(a)
\right)
+
\nu D^\sharp_{>R\Lambda}(I)
\\
&>
-\frac{\nu T}{4}
+
\frac{\nu T}{2}
=
\frac{\nu T}{4}.
\end{aligned}
\tag{21}
\]

This proves the exhaustive alternative. \(\square\)

The constants \(1/2,1/2,1/4\) are not intended as sharp optimisation.
Their value is that they are absolute, independent of \(\Lambda\),
\(R\), and the event index.

## 4. Application to one adjoint-pressure event

Retain the reviewed physical pullback

\[
b_j(x,\tau)
=
\sigma_j
v(x_j+\sigma_jx,t_j-\sigma_j^2\tau),
\qquad
0<\tau<h_j,
\tag{22}
\]

and put

\[
I_j
=
(t_j^-,t_j^+)
:=
(t_j-\sigma_j^2h_j,t_j).
\tag{23}
\]

For every fixed \(\kappa\ge1\), the reviewed feedback-pressure floor
forces

\[
D^\chi_{>\Lambda_j}(I_j)
\ge
P_j,
\qquad
P_j:=c_\kappa\sigma_jh_j^{-3},
\tag{24}
\]

where

\[
\Lambda_j
:=
\frac{\kappa h_j^{-1/2}}{\sigma_j}.
\tag{25}
\]

Set

\[
T_j
:=
\frac{P_j}{C_\chi^2}
=
\frac{c_\kappa}{C_\chi^2}
\sigma_jh_j^{-3}.
\tag{26}
\]

The theorem gives (1) for every fixed or index-dependent \(R_j>1\).
No comparison between \(\Lambda_j\) and the next Besov-event frequency
is needed.

The same conclusion applies to the genuinely superparabolic cutoff

\[
\Lambda_{j,\varepsilon}
\asymp
\frac{
h_j^{-1/2}\sqrt{\log(1/h_j)}
}{\sigma_j}
\tag{27}
\]

with

\[
P_{j,\varepsilon}
=
c_\varepsilon\sigma_jh_j^{-3+\varepsilon}.
\tag{28}
\]

The fixed-\(\kappa\) form (24) is quantitatively stronger when available;
(27) records that the theorem also follows the reviewed escaping
cutoff.

Global Fourier-tail continuity still gives

\[
T_j\longrightarrow0.
\tag{29}
\]

Thus (17) is not contradicted by a fixed global kinetic-energy bound,
and one cannot sum (18) merely by observing that each term is positive.
The theorem identifies the PDE alternatives; it does not yet prove that
their event-index occurrences are disjoint.

## 5. Why this does not duplicate the earlier flux no-go

The earlier
[frequency-energy-flux audit](frequency-energy-flux.md) proved that a
fresh tensor-detector moment does not algebraically force nonlinear
frequency flux: an exact Beltrami heat solution has a positive detector
increment and zero projected nonlinearity.

The present theorem starts from strictly stronger information: an actual
positive high-pass **viscous dissipation floor** on one NSE interval.
If that floor is neither retained in a comparable annulus nor already
present as entrance energy, the exact balance (15) forces positive
signed flux.  The Beltrami example does not violate this assertion:
its dissipation stays at its original frequency and therefore lies in
the comparable-annulus branch.

## 6. Exact conservative shell survivor

The signed flux in (18) is cumulative.  The following finite-depth
ledger shows that cumulative positivity alone does not make the payments
fresh.

Fix a depth \(m\ge1\), a total input \(P>0\), and \(0<r<1\).  Use shells
\(0,1,\ldots,m\), and let boundary \(n\) separate shells
\(\{0,\ldots,n\}\) from \(\{n+1,\ldots,m\}\).  Prescribe the positive
upward fluxes

\[
\boxed{
F_n:=Pr^n,
\qquad
0\le n\le m-1.
}
\tag{30}
\]

Let \(V_n\ge0\) denote the time-integrated viscous energy cost in shell
\(n\), already including the viscosity factor.  Set

\[
V_0:=0,
\tag{31}
\]

\[
V_n
:=
F_{n-1}-F_n
=
P(1-r)r^{n-1},
\qquad
1\le n\le m-1,
\tag{32}
\]

and

\[
V_m:=F_{m-1}=Pr^{m-1}.
\tag{33}
\]

Only the low reservoir changes energy:

\[
\Delta E_0=-2P,
\qquad
\Delta E_n=0
\quad(1\le n\le m).
\tag{34}
\]

Taking the initial low-shell energy at least \(2P\) makes all endpoint
energies nonnegative.  The integrated shell balances are exact:

\[
\frac12\Delta E_0+V_0=-F_0,
\tag{35}
\]

\[
\frac12\Delta E_n+V_n=F_{n-1}-F_n,
\qquad
1\le n\le m-1,
\tag{36}
\]

\[
\frac12\Delta E_m+V_m=F_{m-1}.
\tag{37}
\]

They sum to the global energy identity

\[
\frac12\sum_{n=0}^m\Delta E_n
+
\sum_{n=0}^mV_n
=0.
\tag{38}
\]

More importantly, the cost above every boundary telescopes:

\[
\boxed{
\sum_{k=n+1}^mV_k
=
F_n
\qquad(0\le n\le m-1).
}
\tag{39}
\]

Thus every cumulative high-pass balance sees positive signed input
equal to the full tail dissipation, yet all boundaries are paid by one
and the same cascade.

For \(m\ge2\), make the retention depth-dependent:

\[
r_m:=1-\frac1{m^2}.
\tag{40}
\]

Then

\[
\boxed{
\frac{V_m}{P}
=
r_m^{m-1}
\longrightarrow1,
}
\tag{41}
\]

while

\[
\frac1P\sum_{n=1}^{m-1}V_n
=
1-r_m^{m-1}
\longrightarrow0.
\tag{42}
\]

The integrated balances therefore permit an arbitrarily deep,
asymptotically lossless transfer followed by almost complete
dissipation at the top shell.

This is an algebraic conservative shell-energy ledger, not a shell-model
differential equation, Galerkin solution, Oseen solution, or
Navier--Stokes solution.  It proves only that the signs, global energy
identity, and all cumulative high-pass identities do not themselves
supply a uniform decrement per crossed annulus.

## 7. The parabolic clock does not impose finite depth

The shell ledger is also compatible with the natural heat-clock
bookkeeping.  Let

\[
K_n=L^n\Lambda,
\qquad
n\ge1,
\qquad
L>1.
\tag{43}
\]

The sum of the natural viscous times is

\[
\boxed{
\sum_{n=1}^{\infty}
\frac1{\nu K_n^2}
=
\frac1{
\nu\Lambda^2(L^2-1)
}.
}
\tag{44}
\]

For one physical event,

\[
\delta
:=
|I_j|
=
\sigma_j^2h_j,
\qquad
\Lambda_j^{-2}
=
\frac{\delta}{\kappa^2}.
\tag{45}
\]

Hence

\[
\sum_{n=1}^{\infty}
\frac1{\nu(L^n\Lambda_j)^2}
=
\frac{\delta}{
\nu\kappa^2(L^2-1)
}.
\tag{46}
\]

For any fixed \(\nu,\kappa>0\), choosing
\(\nu\kappa^2(L^2-1)>1\) fits infinitely many such clocks strictly
inside the event interval.  In the unit-viscosity normalisation with
\(\kappa\ge1\), the dyadic choice \(L=2\) gives

\[
\sum_{n=1}^{\infty}
K_n^{-2}
=
\frac{\delta}{3\kappa^2}
\le
\frac{\delta}{3}.
\tag{47}
\]

This is only a timing ledger.  It neither constructs the nonlinear
interactions nor proves that NSE can realise the near-lossless shell
path.  It does show that a lower bound of one heat time per octave would
still allow Zeno frequency depth.

## 8. Exact consequence for ROUTE-R3B

The kinematic survivor's arbitrary far-frequency placement has now been
reduced to three NSE-specific branches:

1. **comparable annulus:** the reviewed adjoint-pressure payment is
   physically localised within one chosen frequency factor;
2. **inherited state:** the farther tail already carries enough kinetic
   energy at the event entrance;
3. **signed flux:** NSE nonlinearity transports a definite amount of
   energy through the farther boundary during the event.

This is a strict advance over a bare nonnegative Fourier-tail floor.
However, the exact shell ledger closes the proposal that positive
cumulative flux and the ordinary high-pass energy balances alone make
the payments event-index fresh.

The next positive theorem must add at least one genuinely
NSE-specific quantitative input:

1. a uniform fraction of flux lost or dissipated in every comparable
   annulus;
2. a lower bound on transfer time whose sum cannot be Zeno;
3. a locality theorem preventing direct or near-lossless passage through
   arbitrarily many shells under the inherited weak-\(L^3\) ceiling;
4. an ancestry theorem turning entrance high-frequency energy into an
   earlier selected Besov event; or
5. a signed adjoint-pressure/energy-flux functional whose increments,
   unlike cumulative high-pass flux, telescope across event index.

No such theorem is proved here.  In particular, this note does not
exclude the conditional ancient profile, prove regularity or breakdown,
or establish any Clay alternative A--D.

The subsequent independently reviewed
[spectral primal--adjoint pairing audit](adjoint-pressure-spectral-pairing.md)
closes the bare version of item 5: the shell pairing telescopes exactly,
but pressure contributes no scalar term because it is orthogonal to the
projected divergence-free fields.  A viable mixed functional must add a
pressure-visible coupling.  The subsequent
[spatial cutoff-flux audit](adjoint-pressure-spatial-pairing.md) shows
that merely replacing Fourier localisation by the unseparated local
current is also insufficient: pressure can cancel transport exactly in
every gauge-invariant cutoff flux.

The subsequent independently reviewed
[terminal signed-flux ancestry theorem](adjoint-pressure-inherited-ancestry.md)
does close item 4 at the level needed to remove inherited energy as an
unaccounted resource.  A fixed-time \(H^1\) tail and last-hitting
argument turn every late entrance threshold into pre-event cumulative
flux.  Continuity from above of the sharp annular dissipation then
allows an event-adaptive \(R_j\to1\), yielding terminal intervals
\(J_j\) with
\[
\Phi_{R_j\Lambda_j}(J_j)\ge\frac{\nu T_j}{4}.
\]
This does not make the intervals disjoint or the cumulative flux
event-index fresh; items 1--3 and 5 remain live in that stricter form.

## 9. Executable certificate

The smooth-to-sharp conversion, exact energy identity, exhaustive
constants, physical parabolic phase, shell balances, cumulative
telescope, near-lossless depth limit, and Zeno clock are checked by

```bash
make adjoint-pressure-parabolic-flux
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_parabolic_flux -v
```
