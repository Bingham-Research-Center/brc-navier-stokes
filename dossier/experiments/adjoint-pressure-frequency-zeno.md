# A dyadic Zeno frequency path can retain terminal pressure

- **Experiment:** EXP-ADJOINT-PRESSURE-FREQUENCY-ZENO-001
- **Route:** ROUTE-R3B
- **Status:** independently reviewed analytic cross-band countermodel,
  critical packet ledger, and finite-depth Fourier/Leray colligation
- **Domain:** scalar Littlewood--Paley path majorant motivated by
  \(\mathbb R^3\) Oseen estimates
- **Clay status:** unsolved
- **Input:** the independently reviewed
  [fixed-band frequency-colligation theorem](adjoint-pressure-frequency-colligation.md)
- **Review:** [accepted after four precision repairs](../review-response-adjoint-pressure-frequency-zeno-2026-07-24.md)

The fixed-band theorem forces every logarithmically deep pressure packet
to leave each fixed comparable-frequency corridor.  The next question is
whether weak-\(L^3\) multiplication, heat damping, and scale bookkeeping
automatically sum the resulting frequency excursions.

This note gives an exact negative answer at the level of the sharp
positive cross-band majorant.

> A path can climb through dyadic frequencies on a summable sequence of
> heat clocks.  Each upward transition loses a factor \(1/2\), but a
> final high--high-to-low pressure observation gains the reciprocal
> factor \(2^m\).  The integrated pressure cost remains uniformly
> positive at every depth, even with any prescribed algebraic strong
> zero trace.

The same dyadic scaling is compatible, as a kinematic ledger, with a
bounded weak-\(L^3\) distribution tail and finite energy and
time-integrated dissipation.  There is also an exact finite-depth
complex Fourier colligation whose divergence-free polarisations realise
each selected upward transport coefficient and the terminal Hodge
return.  This is **not** an Oseen or Navier--Stokes solution.  It shows
that the remaining proof must use simultaneous spatial localisation and
overlap, a single uniformly critical drift with all cross-interactions,
or its Navier--Stokes evolution; elementary Fourier/Leray polarisation
compatibility alone is not the missing theorem.

## 1. The sharp positive cross-band kernel

Let \(z_R\) have Fourier support at frequency \(R\), and observe the
Oseen interaction at output frequency \(S\).  The same annular kernel,
Lorentz Hölder, and Bernstein estimates as in the fixed-band theorem give

\[
\begin{aligned}
&\left\|
\Delta_S e^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}(z_R\otimes b)(s)
\right\|_1
\\
&\qquad\le
KMR S
e^{-c\nu S^2(t-s)}
\|z_R(s)\|_1.
\end{aligned}
\tag{1}
\]

Indeed, the output differentiated multiplier contributes \(S\), while

\[
\|z_R\otimes b\|_1
\lesssim
\|z_R\|_{L^{3/2,1}}\|b\|_{L^{3,\infty}}
\lesssim
MR\|z_R\|_1.
\tag{2}
\]

After normalising the fixed constants \(KM/(c\nu)\), the scalar time
kernel for a transition \(R\to S\) is

\[
k_{S,R}(t)
:=
RS e^{-S^2t}
=
\frac{R}{S}
\left(S^2e^{-S^2t}\right),
\tag{3}
\]

and therefore

\[
\int_0^\infty k_{S,R}(t)\,dt
=
\frac{R}{S}.
\tag{4}
\]

This is a majorant, not an equality for the vector Oseen operator.
Its scale factor is sharp for the endpoint estimate being tested.

The corresponding instantaneous pressure observation from input
frequency \(R\) to output frequency \(S\) has majorant

\[
\|\Delta_S\mathbb Q
\operatorname{div}(z_R\otimes b)\|_1
\le
KMR S\|z_R\|_1.
\tag{5}
\]

## 2. Exact dyadic Zeno path

Set

\[
R_i:=2^i,
\qquad
\lambda_i:=R_i^2=4^i
\quad(i\ge1),
\tag{6}
\]

and retain only the upward itinerary

\[
R_0\longrightarrow R_1\longrightarrow\cdots
\longrightarrow R_m.
\tag{7}
\]

By (3), its \(i\)-th scalar transition kernel is

\[
\boxed{
k_i(t)
:=
R_{i-1}R_i e^{-R_i^2t}
=
\frac12\lambda_i e^{-\lambda_it}.
}
\tag{8}
\]

Thus every transition has mass \(1/2\).  Let
\(X_i\) be independent exponential random variables of rate
\(\lambda_i\), and put

\[
S_m:=X_1+\cdots+X_m.
\tag{9}
\]

Equivalently, on finitely supported causal band sequences
\(z=(z_0,z_1,\ldots)\), define the single weighted shift and observation

\[
(\mathfrak Tz)_0:=0,
\qquad
(\mathfrak Tz)_i:=k_i*z_{i-1},
\qquad
\mathfrak Cz:=\sum_{i\ge0}2^iz_i.
\tag{9a}
\]

If \(q\) is supported only in band zero, then
\(\mathfrak T^mq\) is supported only in band \(m\), and
\(\mathfrak C\mathfrak T^mq=2^m(\mathfrak T^mq)_m\).
Thus neither the transition rule nor the terminal observation is chosen
afresh at each depth.

If \(K_m:=k_m*\cdots*k_1\), then

\[
\boxed{
K_m(t)
=
2^{-m}f_{S_m}(t),
\qquad
\int_0^\infty K_m(t)\,dt=2^{-m},
}
\tag{10}
\]

where \(f_{S_m}\) is the probability density of \(S_m\).

For any fixed integer \(\eta\ge0\), take the causal input

\[
q_\eta(t):=t^\eta,
\qquad
u_{m,\eta}:=K_m*q_\eta.
\tag{11}
\]

Equation (10) gives the exact representation

\[
\boxed{
u_{m,\eta}(t)
=
2^{-m}
\mathbb E\left[(t-S_m)_+^\eta\right].
}
\tag{12}
\]

For \(\eta=0\), use the causal convention

\[
(x)_+^0:=\mathbf 1_{\{x>0\}}.
\tag{12a}
\]

The equality event has probability zero.  Every positive-depth output
\(m\ge1\) has a genuine strong zero right trace.  More precisely,

\[
u_{m,\eta}(t)=O(t^{m+\eta})
\qquad(t\downarrow0),
\tag{13}
\]

because the convolution of \(m\) bounded exponential densities is
\(O(t^{m-1})\) at the origin.

## 3. Exact finite-depth Fourier/Leray compatibility

The scale factors in the scalar path are not defeated by an elementary
polarisation obstruction.  On the complex Fourier side of
\(\mathbb T^3\), let \(e_1,e_2,e_3\) be the coordinate vectors and set

\[
\xi_i:=
\begin{cases}
R_i e_1,&i\ \text{even},\\
R_i e_2,&i\ \text{odd},
\end{cases}
\qquad
a:=e_3.
\tag{13a}
\]

Thus \(a\cdot\xi_i=0\) at every level.  Put
\(\eta_i:=\xi_i-\xi_{i-1}\) and choose

\[
\beta_i:=
\begin{cases}
R_i(e_1+\tfrac12e_2),&i\ \text{odd},\\
R_i(\tfrac12e_1+e_2),&i\ \text{even}.
\end{cases}
\tag{13b}
\]

A direct calculation gives

\[
\boxed{
\beta_i\cdot\eta_i=0,
\qquad
\beta_i\cdot\xi_{i-1}=R_iR_{i-1},
\qquad
\mathbb P_{\xi_i}a=a.
}
\tag{13c}
\]

Hence the drift mode
\(b_i(x)=\beta_i e^{i\eta_i\cdot x}\) is divergence-free and

\[
\mathbb P\bigl(b_i\cdot\nabla
  (a e^{i\xi_{i-1}\cdot x})\bigr)
=
iR_iR_{i-1}a e^{i\xi_i\cdot x}.
\tag{13d}
\]

This realises the numerator of the kernel \(k_i\) exactly, with no
Leray loss on the selected state polarisation.

The terminal pressure return has an equally explicit colligation.  Fix
the low output frequency \(\kappa:=e_3\).  If \(\xi_i=R_i e_{\alpha_i}\)
with \(\alpha_i\in\{1,2\}\), set

\[
\zeta_i:=\kappa-\xi_i,
\qquad
\gamma_i:=e_{\alpha_i}+R_i e_3.
\tag{13e}
\]

Then

\[
\boxed{
\gamma_i\cdot\zeta_i=0,
\qquad
\gamma_i\cdot\xi_i=R_i,
\qquad
\mathbb Q_\kappa a=a.
}
\tag{13f}
\]

Thus the divergence-free terminal drift mode
\(\gamma_i e^{i\zeta_i\cdot x}\) produces exactly the low-frequency
gradient component \(iR_i a e^{i\kappa\cdot x}\).  Since \(R_0=1\),
this is the terminal product factor \(R_iR_0\).

For every finite depth these modes give exact selected band-to-band
blocks and an exact terminal Hodge block.  Their sizes are

\[
|\beta_i|^2=\frac54R_i^2,
\qquad
|\gamma_i|^2=1+R_i^2,
\tag{13g}
\]

so they have the critical amplitude order used in the packet ledger
below.

The limitation is essential.  These are global complex torus modes:
their weak-\(L^3\) norms grow like \(R_i\).  The calculation does not
construct one uniformly weak-\(L^3\), spatially localised
\(\mathbb R^3\) drift; it does not control the extra cross-interactions
created by summing the modes; and it proves no Oseen or Navier--Stokes
trajectory.  Localising the modes while preserving the whole selected
chain, terminal return, overlap, and coefficient budget is precisely
part of the remaining PDE problem.

## 4. The terminal pressure return cancels every upward loss

At depth \(m\), observe pressure back at the base scale \(R_0=1\).
The cross-band pressure factor in (5) is

\[
\mathcal C_m:=R_mR_0=2^m.
\tag{14}
\]

It exactly cancels the path mass:

\[
\boxed{
\mathcal C_m\int_0^\infty K_m(t)\,dt
=
2^m2^{-m}=1.
}
\tag{15}
\]

More importantly, the cancellation survives a fixed finite horizon.
For \(T>0\), define

\[
\mathcal P_{m,\eta}(T)
:=
\int_0^T
\mathcal C_m u_{m,\eta}(t)\,dt.
\tag{16}
\]

Tonelli's theorem and (12) give

\[
\boxed{
\mathcal P_{m,\eta}(T)
=
\frac1{\eta+1}
\mathbb E\left[(T-S_m)_+^{\eta+1}\right].
}
\tag{17}
\]

The heat clocks form a Zeno sum:

\[
\boxed{
\mathbb ES_m
=
\sum_{i=1}^m4^{-i}
=
\frac{1-4^{-m}}3
<
\frac13.
}
\tag{18}
\]

Since \(x\mapsto(T-x)_+^{\eta+1}\) is convex for
\(\eta\ge0\), Jensen's inequality yields, at \(T=1\),

\[
\boxed{
\mathcal P_{m,\eta}(1)
\ge
\frac1{\eta+1}
\left(1-\mathbb ES_m\right)^{\eta+1}
\ge
\frac1{\eta+1}
\left(\frac23\right)^{\eta+1}
>0
}
\tag{19}
\]

for every \(m\).

In particular, the linear strong-zero-trace input \(\eta=1\) obeys

\[
\boxed{
\mathcal P_{m,1}(1)\ge\frac29
\qquad(m\ge1).
}
\tag{20}
\]

Thus actual exponential heat clocks, causal time ordering, increasing
trace order, and the sharp positive cross-band scale factors do not
force pressure-depth decay.

## 5. Critical packet budget

The scalar path also has the exact scaling of a critical packet tower.
At level \(i\), assign

\[
B_i:=R_i,
\qquad
V_i:=R_i^{-3},
\qquad
\tau_i:=R_i^{-2}.
\tag{21}
\]

Here \(B_i\) is amplitude, \(V_i\) is spatial volume, and \(\tau_i\) is
one heat clock.  The distribution tail at threshold \(R_j\) has charge

\[
\boxed{
R_j^3\sum_{i=j}^\infty V_i
=
R_j^3\sum_{i=j}^\infty R_i^{-3}
=
\frac87.
}
\tag{22}
\]

This is the weak-\(L^3\) scaling.  The energy ledger is

\[
\boxed{
\sum_{i=1}^\infty B_i^2V_i
=
\sum_{i=1}^\infty R_i^{-1}
=1.
}
\tag{23}
\]

The enstrophy rate and time-integrated dissipation of one packet are

\[
(B_iR_i)^2V_i=R_i,
\qquad
\tau_i(B_iR_i)^2V_i=R_i^{-1},
\tag{24}
\]

so

\[
\boxed{
\sum_{i=1}^\infty
\tau_i(B_iR_i)^2V_i
=1.
}
\tag{25}
\]

Finally,

\[
\boxed{
\sum_{i=1}^\infty\tau_i
=
\sum_{i=1}^\infty4^{-i}
=\frac13.
}
\tag{26}
\]

Equations (22)--(26) are only a kinematic scaling ledger.  They do not
construct one uniformly critical field whose localised packets realise
the exact Fourier blocks above and solve Oseen or Navier--Stokes.  In
particular, arranging the packet supports, all cross-interactions, and
interaction times compatibly on one physical drift is deliberately left
unresolved.

## 6. Exact conclusion

The countermodel closes the following norm-only proposal:

> Once fixed-band persistence is excluded, weak-\(L^3\) cross-band
> estimates, heat damping, strong zero trace, finite energy, and finite
> dissipation automatically sum every multiscale Oseen frequency path.

They do not.  A scale-accelerating path can fit infinitely many heat
clocks into a finite interval, while a terminal high--high-to-low
pressure return recovers the entire upward scale loss.

The result does **not** show that an actual Oseen or Navier--Stokes
trajectory can realise this path.  The live theorem is now more precise:
one must exclude at least one of the following on the same physical
trajectory:

1. a dyadically accelerating sequence of interacting frequency packets;
2. a terminal pressure return from the top frequency to the selected
   low band with reciprocal scale gain;
3. compatible spatial localisation and overlap for the exact selected
   Fourier/Leray blocks, without uncontrolled cross-interactions; or
4. reuse of one finite coefficient-energy budget along the entire path.

Equivalently, the next positive theorem must supply a same-trajectory
frequency ancestry, a scale-flux/Carleson charge, a signed pressure
cancellation, or a vector-valued estimate that is absent from the
positive path majorant.

## Reproduce

```bash
make adjoint-pressure-frequency-zeno
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_frequency_zeno -v
```
