# Feedback pressure forces a genuine superparabolic coefficient tail

- **Experiment:** EXP-ADJOINT-PRESSURE-PARABOLIC-COEFFICIENT-TAIL-001
- **Route:** ROUTE-R3B
- **Status:** adversarially recomputed proof-level smooth-layer conditional
  theorem
- **Review:** [valid in scope with no fatal or repairable
  gap](../review-ledger.md)
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** adversarially recomputed
  [direct-response decomposition](adjoint-pressure-direct-response.md),
  [feedback-tail energy bounds](adjoint-pressure-feedback-tail.md),
  [last-return renewal theorem](adjoint-pressure-last-return-renewal.md),
  and [no-return parabolic-exclusion theorem](adjoint-pressure-no-return-parabolic.md)

The reviewed renewal theorems reduce the complete feedback branch to a
stretched-exponential coefficient cost or superparabolic LP--Dyson
capture escape.  The latter is an operator-series statement and was not
known to imply an actual Fourier tail of the coefficient.

This note supplies that missing implication.

Fix a smooth radial multiplier \(\chi\) which equals one on the unit
ball and zero outside the ball of radius two.  At a frequency

\[
V=\kappa h^{-1/2},\qquad \kappa\ge1,
\]

split the actual smooth coefficient into

\[
c=S_Vb:=\chi(D/V)b,
\qquad
d=(I-S_V)b.
\]

The low coefficient satisfies
\(\|c\|_\infty\lesssim MV\).  Its critical Volterra parameter is
therefore only \(MV\sqrt h\lesssim M\kappa\), and its complete
zero-data feedback pressure obeys

\[
\boxed{
\|\mathscr P_{S,c}r_c\|_{L^1_{t,x}}
\le
C e^{A\kappa^2}h^{7/4}.
}
\tag{1}
\]

There is also an exact comparison identity.  If \(q_b,r_b\) are the
direct and feedback states for \(b\), and \(q_c,r_c\) are those for
\(c\), then

\[
q_b-q_c=T_d\varphi,
\]

\[
\boxed{
r_b-r_c
=
(I-T_c)^{-1}
\left[
T_c(q_b-q_c)+T_d(q_b+r_b)
\right].
}
\tag{2}
\]

Thus every term in the difference contains one actual high-coefficient
factor \(d\), chosen at its last chronological occurrence; every later
interaction uses only \(c\).  Lorentz--Volterra estimates, the reviewed
zero-data energy bounds, and the final low-pressure kernel give

\[
\boxed{
\|\mathscr P_{S,b}r_b-\mathscr P_{S,c}r_c\|_{L^1_{t,x}}
\le
C e^{A\kappa^2}h^{3/2}
\left(
\int_0^h\|\nabla(I-S_V)b(t)\|_2^2\,dt
\right)^{1/2}.
}
\tag{3}
\]

Consequently, a fixed feedback pressure floor

\[
\|\mathscr P_{S,b}r_b\|_{L^1_{t,x}}\ge p_0>0
\]

forces, whenever the right side of (1) is at most \(p_0/2\),

\[
\boxed{
\int_0^h
\|\nabla(I-S_{\kappa h^{-1/2}})b(t)\|_2^2\,dt
\ge
c_{p_0}e^{-2A\kappa^2}h^{-3}.
}
\tag{4}
\]

In particular, every fixed parabolic multiple carries an
inverse-cubic coefficient tail.  More strongly, for every fixed
\(0<\varepsilon<1\), take

\[
\kappa_\varepsilon(h)
:=
\left(
\frac{\varepsilon}{2A}\log\frac1h
\right)^{1/2}.
\]

Then \(\kappa_\varepsilon(h)\to\infty\), so the cutoff is genuinely
superparabolic, while (1), (3), and (4) give

\[
\boxed{
\int_0^h
\left\|
\nabla
\left(
I-S_{\kappa_\varepsilon(h)h^{-1/2}}
\right)b(t)
\right\|_2^2\,dt
\ge
c_\varepsilon h^{-3+\varepsilon}.
}
\tag{5}
\]

This converts the common LP--Dyson capture escape into an actual
same-layer, frequency-localised coefficient-dissipation charge.  It
does not yet make the charges at different Besov events additive:
their physical frequency tails are nested and the physical weights can
still vanish.

## 1. Smooth-layer equations and reviewed bounds

Fix \(0<h\le1\), viscosity \(\nu>0\), a detector output frequency
\(S>0\), and a fixed band-limited solenoidal Schwartz detector
\(\varphi\).  Let

\[
b\in L^\infty(0,h;L^\infty\cap L^2),
\qquad
\nabla\cdot b=0,
\qquad
\sup_{0<t<h}\|b(t)\|_{L^{3,\infty}}\le M
\tag{6}
\]

be one smooth finite-energy genealogy layer.  For a solenoidal
coefficient \(e\), put

\[
(T_ez)(t)
:=
\int_0^t
e^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}
\bigl(z(s)\boxtimes e(s)\bigr)\,ds,
\qquad
(z\boxtimes e)_{ik}:=z_ie_k.
\tag{7}
\]

The direct response and zero-data feedback state for \(b\) satisfy

\[
q_b(t)
=
\int_0^t
e^{\nu(t-s)\Delta}
\left[
\nu\Delta\varphi
+\mathbb P\operatorname{div}
(\varphi\boxtimes b(s))
\right]\,ds,
\tag{8}
\]

\[
r_b=T_bq_b+T_br_b.
\tag{9}
\]

The adversarially recomputed estimates give

\[
\|q_b(t)\|_{L^{3/2,1}}
\le C_qt^{3/4},
\tag{10}
\]

\[
\|q_b(t)\|_2+\|r_b(t)\|_2
\le C_Et,
\tag{11}
\]

\[
\int_0^h
\left(
\|\nabla q_b(t)\|_2^2+
\|\nabla r_b(t)\|_2^2
\right)\,dt
\le C_Eh^2.
\tag{12}
\]

Only (6) and the smooth solenoidal Oseen equations are used below.
In particular, the comparison does not assume an endpoint adjoint on
the rough limiting hull.

Let

\[
\mathbb Q:=I-\mathbb P,
\qquad
\mathscr P_{S,e}z
:=
S_S\mathbb Q\operatorname{div}(z\boxtimes e),
\tag{13}
\]

where \(S_S\) is the fixed smooth pressure-output cutoff.  Its kernel
has \(L^1\) norm at most \(C S\), and therefore

\[
\|\mathscr P_{S,e}z\|_1
\le
CS\|z\boxtimes e\|_1.
\tag{14}
\]

Assume along the selected feedback sequence that

\[
\boxed{
\|\mathscr P_{S,b}r_b\|_{L^1((0,h)\times\mathbb R^3)}
\ge p_0.
}
\tag{15}
\]

## 2. A parabolic low--high split of the actual coefficient

Choose one real radial
\(\chi\in C^\infty_c(\mathbb R^3)\) satisfying

\[
\chi(\xi)=1\quad(|\xi|\le1),
\qquad
\chi(\xi)=0\quad(|\xi|\ge2).
\tag{16}
\]

For \(V>0\), define

\[
S_V:=\chi(D/V),
\qquad
c:=S_Vb,
\qquad
d:=(I-S_V)b.
\tag{17}
\]

Both fields are smooth and solenoidal.  Multiplier boundedness and
Lorentz--Bernstein give

\[
\|c(t)\|_{L^{3,\infty}}\le C_\chi M,
\qquad
\|c(t)\|_\infty\le C_\chi MV.
\tag{18}
\]

Because \(1-\chi(\xi/V)\) vanishes on \(|\xi|\le V\), Plancherel gives

\[
\|d(t)\|_2
\le
V^{-1}\|\nabla d(t)\|_2.
\tag{19}
\]

Put

\[
E_d(h):=\int_0^h\|d(t)\|_2^2\,dt,
\tag{20}
\]

\[
\boxed{
D_{b,>V}^{\chi}(h)
:=
\int_0^h\|\nabla d(t)\|_2^2\,dt.
}
\tag{21}
\]

Then

\[
\boxed{
E_d(h)\le V^{-2}D_{b,>V}^{\chi}(h).
}
\tag{22}
\]

The quantity in (21) is an actual smooth Littlewood--Paley tail of the
coefficient, not a Dyson-path label.

## 3. The low-coefficient Volterra resolvent

Let

\[
Z_h:=L^1(0,h;L^{3/2,1}(\mathbb R^3)).
\tag{23}
\]

The nonstationary Stokes kernel and (18) give

\[
\|(T_cz)(t)\|_{L^{3/2,1}}
\le
C_\nu\|c\|_\infty
\int_0^t(t-s)^{-1/2}
\|z(s)\|_{L^{3/2,1}}\,ds.
\tag{24}
\]

Iterating the half-order Volterra kernel and integrating in \(t\)
yields

\[
\boxed{
\|T_c^mz\|_{Z_h}
\le
\frac{
\left(
C_0M V\sqrt h
\right)^m
}{
\Gamma(m/2+1)
}
\|z\|_{Z_h}.
}
\tag{25}
\]

Consequently,

\[
\boxed{
\|(I-T_c)^{-1}\|_{Z_h\to Z_h}
\le
\mathcal R(C_0MV\sqrt h),
}
\tag{26}
\]

where

\[
\mathcal R(x)
:=
\sum_{m=0}^\infty
\frac{x^m}{\Gamma(m/2+1)}
\le
C_R e^{C_Rx^2}.
\tag{27}
\]

Take

\[
V=\kappa h^{-1/2},
\qquad
\kappa\ge1.
\tag{28}
\]

After enlarging one constant \(A=A(\nu,M,\chi)\),

\[
\boxed{
\|(I-T_c)^{-1}\|_{Z_h\to Z_h}
\le
Ce^{A\kappa^2}.
}
\tag{29}
\]

This is the decisive scale cancellation: although
\(\|c\|_\infty\) is of order \(h^{-1/2}\), its Volterra time is only
\(\sqrt h\).

## 4. Complete low-coefficient feedback vanishes

Define \(q_c,r_c\) by (8)--(9) with \(b\) replaced by \(c\).
The proof of the reviewed direct-response estimate (10) uses only the
weak-\(L^3\) ceiling and the fixed detector.  Hence

\[
\|q_c(t)\|_{L^{3/2,1}}\le C_qt^{3/4},
\qquad
\|q_c\|_{Z_h}\le C h^{7/4}.
\tag{30}
\]

Since

\[
r_c=(I-T_c)^{-1}T_cq_c,
\tag{31}
\]

equations (25), (29), and (30) imply

\[
\|r_c\|_{Z_h}
\le
Ce^{A\kappa^2}h^{7/4}.
\tag{32}
\]

Indeed, the series for \(r_c\) starts at depth one and initially
contributes one factor \(C_0MV\sqrt h\lesssim\kappa\).  After enlarging
the constant \(A\) in (29),
\[
\kappa e^{A_0\kappa^2}\le Ce^{A\kappa^2}
\qquad(\kappa\ge1),
\]
so that factor is already included in (32).

Lorentz Hölder, (14), and (18) now give

\[
\begin{aligned}
\|\mathscr P_{S,c}r_c\|_{L^1_{t,x}}
&\le
CS
\int_0^h
\|r_c(t)\|_{L^{3/2,1}}
\|c(t)\|_{L^{3,\infty}}\,dt\\
&\le
Ce^{A\kappa^2}h^{7/4}.
\end{aligned}
\tag{33}
\]

This proves (1).  It sums the complete low-coefficient feedback
resolvent; no interaction-depth truncation, positivity, or
frequency-path participation assumption is used.

## 5. Exact last-high-coefficient identity

The heat term \(\nu\Delta\varphi\) cancels when the two direct
responses are subtracted, so

\[
\boxed{
\delta q:=q_b-q_c=T_d\varphi.
}
\tag{34}
\]

Let

\[
\delta r:=r_b-r_c.
\tag{35}
\]

Subtracting the two feedback equations gives

\[
\begin{aligned}
\delta r
&=
T_b(q_b+r_b)-T_c(q_c+r_c)\\
&=
T_c\delta r
+T_c\delta q
+T_d(q_b+r_b).
\end{aligned}
\tag{36}
\]

Therefore

\[
\boxed{
\delta r
=
(I-T_c)^{-1}
\left[
T_c\delta q+T_d(q_b+r_b)
\right].
}
\tag{37}
\]

Chronologically, the factor \(T_d\) or the \(d\)-factor inside
\(\delta q\) is the last high-coefficient occurrence.  The resolvent
to its left contains only later \(c\)-interactions.  Equation (37) is
an exact operator identity, not a formal rearrangement of a
nonconvergent series.  It is first obtained in
\(C([0,h];L^2_\sigma)\), where both smooth Volterra problems are
classical.  The estimates below then show that its right-hand side
belongs to \(Z_h\); uniqueness identifies that \(Z_h\) representative
with the classical difference.

The pressure difference is likewise exact:

\[
\boxed{
\mathscr P_{S,b}r_b-\mathscr P_{S,c}r_c
=
\mathscr P_{S,c}\delta r
+\mathscr P_{S,d}r_b.
}
\tag{38}
\]

Thus every term in the difference contains the genuine coefficient
tail \(d\) at least once.

## 6. Quantitative comparison

Lorentz Hölder gives

\[
\|\varphi\boxtimes d(t)\|_{L^{3/2,1}}
\le
C\|\varphi\|_{L^{6,2}}\|d(t)\|_2.
\tag{39}
\]

Using the Stokes kernel as in (24), reversing the time integrations,
and applying Cauchy--Schwarz gives

\[
\boxed{
\|\delta q\|_{Z_h}
\le
C\sqrt h\int_0^h\|d(t)\|_2\,dt
\le
ChE_d(h)^{1/2}.
}
\tag{40}
\]

Put

\[
z_b:=q_b+r_b.
\tag{41}
\]

Lorentz--Sobolev and (12) give

\[
\int_0^h\|z_b(t)\|_{L^{6,2}}^2\,dt
\le
C\int_0^h\|\nabla z_b(t)\|_2^2\,dt
\le
Ch^2.
\tag{42}
\]

Therefore the same calculation yields

\[
\boxed{
\|T_dz_b\|_{Z_h}
\le
C\sqrt h
\int_0^h
\|z_b(t)\|_{L^{6,2}}\|d(t)\|_2\,dt
\le
Ch^{3/2}E_d(h)^{1/2}.
}
\tag{43}
\]

Equations (25), (29), (37), (40), and (43) now give

\[
\boxed{
\|\delta r\|_{Z_h}
\le
Ce^{A\kappa^2}
\left(
\kappa h+h^{3/2}
\right)
E_d(h)^{1/2}.
}
\tag{44}
\]

For the first term in (38), equations (14), (18), and (44) imply

\[
\|\mathscr P_{S,c}\delta r\|_{L^1_{t,x}}
\le
Ce^{A\kappa^2}
\left(
\kappa h+h^{3/2}
\right)
E_d(h)^{1/2}.
\tag{45}
\]

For the second term, (11) gives

\[
\begin{aligned}
\|\mathscr P_{S,d}r_b\|_{L^1_{t,x}}
&\le
CS
\int_0^h\|r_b(t)\|_2\|d(t)\|_2\,dt\\
&\le
Ch^{3/2}E_d(h)^{1/2}.
\end{aligned}
\tag{46}
\]

Use (22) and \(V=\kappa h^{-1/2}\).  The leading term in (45)
satisfies

\[
\kappa hE_d(h)^{1/2}
\le
h^{3/2}
D_{b,>V}^{\chi}(h)^{1/2}.
\tag{47}
\]

All other terms are smaller for \(0<h\le1\) and \(\kappa\ge1\).
Equations (38), (45)--(47) prove (3).

## 7. The physical coefficient-tail theorem

Combine the pressure floor (15), the low-coefficient estimate (33),
and the comparison (3).  If

\[
Ce^{A\kappa^2}h^{7/4}\le\frac{p_0}{2},
\tag{48}
\]

then reverse triangle gives

\[
\frac{p_0}{2}
\le
Ce^{A\kappa^2}h^{3/2}
D_{b,>V}^{\chi}(h)^{1/2}.
\tag{49}
\]

Hence

\[
\boxed{
D_{b,>\kappa h^{-1/2}}^{\chi}(h)
\ge
c_{p_0}e^{-2A\kappa^2}h^{-3}.
}
\tag{50}
\]

For every fixed \(\kappa\), condition (48) holds for all sufficiently
small selected \(h\).  Thus no fixed parabolic coefficient-frequency
ceiling can carry all but a vanishing fraction of the inverse-cubic
coefficient dissipation required by the feedback pressure.

The cutoff may also grow.  Hereafter \(A\) denotes the final enlarged
constant used simultaneously in (29), (32), and (45).  Fix
\(0<\varepsilon<1\), and put

\[
\kappa_\varepsilon(h)
:=
\left(
\frac{\varepsilon}{2A}
\log\frac1h
\right)^{1/2}.
\tag{51}
\]

Then

\[
e^{A\kappa_\varepsilon(h)^2}
=h^{-\varepsilon/2},
\tag{52}
\]

so the left side of (48) is
\(Ch^{7/4-\varepsilon/2}\to0\).  Equation (50) becomes

\[
\boxed{
D_{b,>
\kappa_\varepsilon(h)h^{-1/2}}^{\chi}(h)
\ge
c_\varepsilon h^{-3+\varepsilon}.
}
\tag{53}
\]

The frequency in (53) is

\[
\kappa_\varepsilon(h)h^{-1/2}
\asymp
h^{-1/2}\sqrt{\log(1/h)},
\tag{54}
\]

strictly above every fixed parabolic multiple.  This proves (5).

More generally, any \(\kappa(h)\to\infty\) satisfying

\[
e^{A\kappa(h)^2}h^{7/4}\longrightarrow0
\tag{55}
\]

gives the tail floor (50).  For example,
\(\kappa(h)=\sqrt{\log\log(e^e/h)}\) loses only a fixed power of
\(\log(1/h)\) from \(h^{-3}\).

## 8. Exact physical scaling

Suppose the layer is the parabolic pullback of one common finite-energy
physical trajectory \(v\):

\[
b_j(x,\tau)
=
\sigma_j
v(x_j+\sigma_jx,t_j-\sigma_j^2\tau).
\tag{56}
\]

The normalised cutoff \(V_j\) is the physical cutoff

\[
\Lambda_j:=\frac{V_j}{\sigma_j}.
\tag{57}
\]

The frequency-tail dissipation scales exactly as

\[
\boxed{
\sigma_jD_{b_j,>V_j}^{\chi}(h_j)
=
\int_{I_j}
\left\|
\nabla
\left(
I-S_{\Lambda_j}
\right)v(t)
\right\|_2^2\,dt.
}
\tag{58}
\]

For a finite-energy Leray--Hopf trajectory,

\[
\int_0^{T^*}
\left\|
\nabla
\left(
I-S_\Lambda
\right)v(t)
\right\|_2^2\,dt
\longrightarrow0
\qquad(\Lambda\to\infty).
\tag{59}
\]

Since \(V_j\to\infty\) and \(\sigma_j\to0\), one has
\(\Lambda_j\to\infty\).  Combining (53), (58), and (59) gives the
same-trajectory necessary condition

\[
\boxed{
\sigma_jh_j^{-3+\varepsilon}\longrightarrow0
\qquad
\text{for every fixed }0<\varepsilon<1.
}
\tag{60}
\]

The stronger information is (58): the payment lies in the actual
physical Fourier tail above
\(\Lambda_j\), not merely in the total dissipation of the event
interval.

## 9. Exact consequence and open boundary

The reviewed complete feedback dichotomy was:

1. superparabolic LP--Dyson capture escape in a pressure-bearing
   renewal block; or
2. the \(9/4\) stretched-exponential total coefficient cost.

Equations (50)--(53) add a theorem valid throughout the selected
feedback branch:

> A fixed feedback pressure packet forces a genuine coefficient
> dissipation tail above every fixed parabolic frequency, and even
> forces \(h^{-3+\varepsilon}\) dissipation above a
> \(\sqrt{\log(1/h)}\)-superparabolic cutoff.

Thus operator-series capture escape can no longer remain detached from
the physical coefficient spectrum.  The remaining obstruction is
event-index reuse: the physical tails in (58) are nested, their lower
bounds carry the shrinking factor \(\sigma_j\), and (60) is compatible
with the already known accelerated zoom laws.

This theorem does not:

- prove that the physical tail charges are disjoint or summable;
- contradict finite physical dissipation;
- give a lower bound on the physical event scale \(\sigma_j\);
- identify the tail with the next Besov event;
- establish a theorem on the rough limiting hull;
- prove regularity, breakdown, or any Clay alternative A--D.

The next theorem must couple the frequency
\(\kappa_\varepsilon(h_j)h_j^{-1/2}/\sigma_j\) to the next event scale,
or prove that the nested physical tail payments in (58) cannot be
reused with the weights forced by (53).

The subsequent adversarially recomputed
[parabolic tail-ancestry theorem and kinematic survivor](adjoint-pressure-parabolic-ancestry.md)
now resolves the bare coupling proposal.  If a fixed-parabolic cutoff
reaches the reciprocal next event scale, then
\[
\frac{\sigma_j^7}{\sigma_{j+1}^6}\to0,
\qquad
\limsup
\frac{\log(1/\sigma_{j+1})}{\log(1/\sigma_j)}
\le\frac76.
\]
This relative log-scale ceiling is sharp and does not force finite
empirical roof mean.  A smooth divergence-free finite-dissipation
kinematic path can still realise the terminal marks, exact cutoff
matching, and every nested tail payment by placing the mass arbitrarily
far above the cutoff.  The remaining theorem must therefore be
NSE-specific: comparable-annulus localisation, signed frequency flux,
a cascade-speed ceiling, or an intervening-event law.

The subsequent adversarially recomputed
[parabolic tail-to-flux theorem](adjoint-pressure-parabolic-flux.md)
now proves the exact NSE alternative.  At every farther cutoff the
payment lies in a comparable annulus, is inherited as entrance
high-frequency energy, or is supplied by positive signed nonlinear
input.  Its exact shell and Zeno ledgers show that cumulative flux
positivity and ordinary high-pass energy balances alone still do not
make the payment event-index fresh.

## 10. Executable ledger

The half-order resolvent growth, low-pressure power, comparison power,
slowly growing cutoff, and resulting coefficient-tail exponent are
checked by

```bash
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_parabolic_coefficient_tail -v
PYTHONPATH=lab python -m \
  navier_lab.adjoint_pressure_parabolic_coefficient_tail
```
