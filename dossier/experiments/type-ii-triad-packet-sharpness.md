# Smooth NSE triad packets saturate the Type-II half-radius charge

- **Experiment:** EXP-TYPE-II-TRIAD-PACKET-SHARPNESS-001
- **Route:** ROUTE-R3C
- **Status:** complete varying-trajectory sharpness theorem; external review pending
- **Domain:** \(\mathbb R^3\), with an exact periodic seed
- **Clay status:** unsolved
- **Input:** [critical frozen-band budget](type-ii-band-dissipation-budget.md)

The common band-work theorem charges every nonlinear correlation death by

\[
\nu\sqrt{\gamma r},
\]

where \(r\) is the lower physical Gaussian radius.  This note asks whether
that vanishing half-radius factor is merely a loss in the proof.

It is not.  There is an explicit divergence-free Fourier triad with exact
nonzero work against a positive Gaussian band.  A standard solenoidal cutoff
turns it into compactly supported data on \(\mathbb R^3\).  Fixed-energy
concentration at physical scale \(r\) then gives actual smooth
Navier--Stokes solutions, one trajectory for each \(r\downarrow0\), with:

\[
\text{initial band energy}=\gamma,
\]

\[
|\text{nonlinear frozen-band work}|\ge\beta\gamma,
\]

\[
\text{event time}\asymp r^{5/2},
\qquad
\|u_r(0)\|_{L^{3,\infty}}\asymp r^{-1/2},
\]

and

\[
\boxed{
\nu\int_0^{t_r}\|\nabla u_r(t)\|_2^2\,dt
\asymp
\nu\sqrt r.
}
\]

The constant \(\beta>0\) and the implicit constants are independent of
\(r\).  Replacing the seed by its negative reverses the nonlinear work
without changing its energy.

Thus no one-event estimate based only on bounded kinetic energy, fixed band
energy, viscosity, and local NSE dynamics can improve
\(\sqrt r\) to \(r^{1/2-\delta}\), \(\delta>0\).  Any improvement must use
the fact that all events belong to one first-record trajectory: genealogy,
reuse, spatial ancestry, terminal trace, or an unthinned temporal-scale
law.

This is not a singular solution and not a same-trajectory cascade.  It
removes a local analytic escape route; it does not close R3C.

## 1. An exact Gaussian-band triad

Work first on \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\).  Let

\[
\Phi(x,y)
:=
\cos x+\cos(2y)+\cos(x+2y)
\]

and define the two-dimensional velocity embedded in three dimensions:

\[
U
:=
(\partial_y\Phi,-\partial_x\Phi,0).
\]

Explicitly,

\[
U=
\left(
-2\sin(2y)-2\sin(x+2y),
\ \sin x+\sin(x+2y),
\ 0
\right).
\]

It is smooth, real, mean zero, and divergence-free.

Let \(M\) be any radial Fourier multiplier.  Denote its values at squared
frequencies \(1,4,5\) by

\[
\mu_1,\qquad\mu_4,\qquad\mu_5.
\]

### Proposition 1: exact triad flux

With normalized torus mean \(\fint_{\mathbb T^3}\),

\[
\boxed{
\fint_{\mathbb T^3}
U\otimes U:\nabla(MU)\,dx
=
-\frac12\mu_1+2\mu_4-\frac32\mu_5.
}
\]

#### Proof

The stream function has only the six modes

\[
\pm(1,0,0),
\qquad
\pm(0,2,0),
\qquad
\pm(1,2,0).
\]

For a stream-function coefficient \(\widehat\Phi(k)\),

\[
\widehat U(k)
=
i(k_2,-k_1,0)\widehat\Phi(k).
\]

The normalized cubic mean is

\[
\sum_{k+p+q=0}
\sum_{\alpha,\beta=1}^3
\widehat U_\alpha(k)
\widehat U_\beta(p)
(iq_\beta)\mu_{|q|^2}
\widehat U_\alpha(q).
\]

Enumerating the six modes gives coefficients

\[
-\frac12,\qquad 2,\qquad-\frac32
\]

for the squared frequencies \(1,4,5\), respectively.  The exact convolution
is independently reproduced by
`lab/navier_lab/type_ii_triad_packet.py`.

Choose the Gaussian heat-scale band

\[
S_*:=
G_{\sqrt{\log2}}^2-G_{\sqrt{2\log2}}^2.
\]

Its multiplier at squared integer frequency \(n\) is

\[
\mu_n
=
e^{-(\log2)n}-e^{-(2\log2)n}
=
2^{-n}-4^{-n}.
\]

Consequently

\[
\mu_1=\frac14,
\qquad
\mu_4=\frac{15}{256},
\qquad
\mu_5=\frac{31}{1024}.
\]

Proposition 1 gives the exact nonzero flux

\[
\boxed{
Q_{\mathbb T}
:=
\fint_{\mathbb T^3}
U\otimes U:\nabla(S_*U)\,dx
=
-\frac{109}{2048}.
}
\]

The positive band pairing is also exact:

\[
\boxed{
H_{\mathbb T}
:=
\fint_{\mathbb T^3}U\cdot S_*U\,dx
=
\frac{651}{2048}>0.
}
\]

Replacing \(U\) by \(-U\) preserves \(H_{\mathbb T}\) and reverses
\(Q_{\mathbb T}\).  The Navier--Stokes quadratic algebra therefore permits
both instantaneous directions of band transfer.

## 2. Compact solenoidal localization on \(\mathbb R^3\)

The periodic seed is used only to make the triad calculation exact.  It can
be localized without losing the sign.

Let

\[
\mathcal A:=(0,0,\Phi),
\qquad
\nabla\times\mathcal A=U.
\]

Choose \(\chi_L\in C_c^\infty(\mathbb R^3)\) equal to one on
\([-L,L]^3\), supported in its unit enlargement, with derivatives bounded
independently of \(L\).  Put

\[
v_L:=\nabla\times(\chi_L\mathcal A).
\]

Then \(v_L\in C^\infty_{c,\sigma}(\mathbb R^3)\), and \(v_L=U\) in the
interior cube.

### Proposition 2: localization preserves the triad flux

As \(L\to\infty\),

\[
\frac1{|[-L,L]^3|}
\int_{\mathbb R^3}
v_L\otimes v_L:\nabla(S_*v_L)\,dx
\longrightarrow
Q_{\mathbb T},
\]

and

\[
\frac1{|[-L,L]^3|}
\langle v_L,S_*v_L\rangle
\longrightarrow
H_{\mathbb T}.
\]

In particular, for all sufficiently large \(L\),

\[
\langle v_L,S_*v_L\rangle>0,
\qquad
\int v_L\otimes v_L:\nabla(S_*v_L)\ne0.
\]

#### Proof

Both \(S_*\) and \(\nabla S_*\) are convolution operators with Schwartz
kernels.  On points a fixed distance from the cutoff layer, applying either
operator to \(v_L\) differs from applying the periodic heat operator to
\(U\) by a tail tending rapidly to zero with that distance.  The cutoff
layer has volume \(O(L^2)\), while \(v_L\) and all fixed derivatives are
uniformly bounded there.  Split the integral into:

1. an interior whose distance from the cutoff tends slowly to infinity;
2. the resulting boundary layer; and
3. the Schwartz-kernel tail.

The first part is the periodic mean times
\(|[-L,L]^3|+o(L^3)\).  The other two parts are \(o(L^3)\).  The same
argument, with one fewer derivative, gives the quadratic pairing limit.

Fix one such large \(L\), reverse its sign if desired, and write simply

\[
v:=v_L,
\qquad
H_*:=\frac12\langle v,S_*v\rangle>0,
\qquad
Q_*:=\int v\otimes v:\nabla(S_*v)\,dx\ne0.
\]

## 3. Fixed-energy packet scaling

Let

\[
\rho_{\mathrm L}:=\sqrt{\log2},
\qquad
\rho_{\mathrm H}:=\sqrt{2\log2}.
\]

For a packet radius \(r>0\), define

\[
S_r
:=
G_{\rho_{\mathrm L}r}^2-G_{\rho_{\mathrm H}r}^2.
\]

Fix a desired physical band energy \(\gamma>0\) and choose

\[
A:=\sqrt{\frac{\gamma}{H_*}}.
\]

Set

\[
u_r^0(x)
:=
A r^{-3/2}v(x/r).
\]

Gaussian covariance gives

\[
S_ru_r^0(x)
=
A r^{-3/2}(S_*v)(x/r),
\]

and therefore

\[
\boxed{
\frac12\langle u_r^0,S_ru_r^0\rangle
=
A^2H_*
=
\gamma.
}
\]

The total kinetic energy is also independent of \(r\):

\[
\frac12\|u_r^0\|_2^2
=
\frac{A^2}{2}\|v\|_2^2.
\]

The endpoint norm diverges at the exact fixed-energy packet rate:

\[
\boxed{
\|u_r^0\|_{L^{3,\infty}}
=
A r^{-1/2}\|v\|_{L^{3,\infty}}.
}
\]

## 4. Actual short-time Navier--Stokes dynamics

Let \(u_r\) be the smooth Navier--Stokes solution with viscosity \(\nu>0\)
and initial datum \(u_r^0\).  Introduce

\[
y:=x/r,
\qquad
s:=\frac{A}{r^{5/2}}t,
\qquad
u_r(x,t)
=
A r^{-3/2}V_r(y,s).
\]

Then \(V_r\) solves

\[
\partial_sV_r
+\mathbb P\nabla_y\!\cdot(V_r\otimes V_r)
=
\varepsilon_r\Delta_yV_r,
\qquad
V_r(0)=v,
\]

with effective viscosity

\[
\boxed{
\varepsilon_r
=
\frac{\nu\sqrt r}{A}
\longrightarrow0.
}
\]

Let \(V\) be the smooth Euler solution from \(v\).  Standard high-Sobolev
local theory gives a time \(s_0>0\), independent of sufficiently small
\(\varepsilon_r\), on which \(V_r\) and \(V\) exist smoothly and

\[
V_r\longrightarrow V
\]

in a Sobolev space strong enough to pass the cubic band pairing uniformly
on \([0,s_0]\).

For completeness, the difference \(w_r=V_r-V\) obeys an energy estimate of
the form

\[
\frac{d}{ds}\|w_r\|_{H^{m-1}}^2
\le
C\|w_r\|_{H^{m-1}}^2
+C\varepsilon_r^2
\]

for fixed \(m>7/2\), after using the uniform \(H^m\) bounds of the two
solutions.  Since \(w_r(0)=0\), Gronwall gives

\[
\sup_{0\le s\le s_0}
\|V_r(s)-V(s)\|_{H^{m-1}}
\lesssim\varepsilon_r.
\]

The carrier nonlinear pairing

\[
q(s)
:=
\int_{\mathbb R^3}
V(s)\otimes V(s):\nabla(S_*v)\,dy
\]

is continuous and \(q(0)=Q_*\ne0\).  Shrink \(s_0\) so that \(q\) keeps
one sign and

\[
|q(s)|\ge\frac{|Q_*|}{2}
\qquad(0\le s\le s_0).
\]

The inviscid convergence then gives, for all sufficiently small \(r\),

\[
\left|
\int_0^{s_0}\!\!\int
V_r\otimes V_r:\nabla(S_*v)\,dy\,ds
\right|
\ge
\frac{s_0|Q_*|}{4}
=:w_*>0.
\]

Return to physical variables and set

\[
t_r:=\frac{s_0r^{5/2}}{A}.
\]

The work against the frozen initial band is exactly

\[
\begin{aligned}
\mathcal W_r^{\mathrm N}
&:=
\int_0^{t_r}\!\!\int
u_r\otimes u_r:\nabla(S_ru_r^0)\,dx\,dt\\
&=
A^2
\int_0^{s_0}\!\!\int
V_r\otimes V_r:\nabla(S_*v)\,dy\,ds.
\end{aligned}
\]

Consequently

\[
\boxed{
|\mathcal W_r^{\mathrm N}|
\ge
A^2w_*
=
\frac{w_*}{H_*}\gamma
=:\beta\gamma,
\qquad
\beta>0.
}
\]

This is fixed nonlinear band work on an actual smooth NSE interval.

## 5. Exact half-radius dissipation

The physical dissipation on the same interval is

\[
\begin{aligned}
\mathscr D_r
&:=
\nu\int_0^{t_r}\|\nabla u_r(t)\|_2^2\,dt\\
&=
\nu A\sqrt r
\int_0^{s_0}\|\nabla V_r(s)\|_2^2\,ds.
\end{aligned}
\]

The carrier integral converges to the corresponding positive Euler
integral.  Hence there are constants \(0<c<C<\infty\), independent of
small \(r\), such that

\[
\boxed{
c\nu A\sqrt r
\le
\mathscr D_r
\le
C\nu A\sqrt r.
}
\]

Since the lower physical band radius is

\[
r_r^{\mathrm L}=\rho_{\mathrm L}r,
\]

this is precisely the
\(\nu\sqrt{\gamma r_r^{\mathrm L}}\) scale in the common work budget, up
to fixed factors depending on the seed and \(\gamma\).

The remaining scale ledger is equally exact:

\[
t_r\asymp r^{5/2},
\qquad
\|u_r^0\|_{L^{3,\infty}}\asymp r^{-1/2},
\]

\[
\text{instantaneous nonlinear work rate}\asymp r^{-5/2},
\qquad
\|\nabla u_r^0\|_2^2\asymp r^{-2}.
\]

Moreover, uniform carrier bounds give

\[
\int_0^{t_r}
\|u_r(t)\|_{L^{3,\infty}}^4\,dt
\lesssim
\sqrt r.
\]

Thus fixed work, finite weak-\(L^3\) fourth-power occupation, vanishing
effective viscosity, and square-root dissipation coexist in genuine smooth
NSE packets.

## 6. Sharpness theorem

### Theorem 3: no stronger one-event radius charge

Fix \(\gamma,\nu>0\).  There is a family of smooth compactly supported
finite-energy NSE data \(u_r^0\), with energy bounded independently of
\(r\downarrow0\), and smooth solution intervals \([0,t_r]\), such that:

1. the initial positive Gaussian band has energy exactly \(\gamma\);
2. its frozen nonlinear work has magnitude at least \(\beta\gamma\);
3. the interval dissipation is at most \(C\nu\sqrt r\); and
4. the lower Gaussian radius is comparable to \(r\).

It follows that, for every \(\delta>0\), no estimate

\[
\mathscr D([0,t])
\ge
c_{\gamma,\nu,E}\,
(r^{\mathrm L})^{1/2-\delta}
\]

can hold uniformly for all smooth fixed-work events using only
\(\gamma,\nu\), a kinetic-energy ceiling, and local NSE evolution.

#### Proof

The construction above proves the four assertions.  If the proposed
stronger estimate held, then

\[
c_{\gamma,\nu,E}
(r^{\mathrm L})^{1/2-\delta}
\le
C\nu\sqrt r.
\]

Since \(r^{\mathrm L}\asymp r\), division by
\(r^{1/2-\delta}\) gives

\[
c_{\gamma,\nu,E}\le C'r^\delta\longrightarrow0,
\]

a contradiction.

## 7. What this does and does not decide

This round establishes:

1. exact nonzero positive-Gaussian-band work for an explicit
   divergence-free triad;
2. both signs of local nonlinear band transfer;
3. a compact \(\mathbb R^3\) solenoidal realization;
4. actual smooth NSE packet dynamics with fixed band energy and fixed work;
5. exact saturation of the half-radius dissipation charge;
6. simultaneous \(r^{1/2}\) weak-\(L^3\) fourth-power occupation; and
7. impossibility of improving the radius exponent by a purely local
   energy-class estimate.

It does not establish:

1. consecutive events on one solution;
2. first-record sampling for the packet family;
3. reuse of one fixed energy quantum through infinitely many bands;
4. spatial recentering or a terminal trace;
5. an unthinned logarithmic-scale Carleson law;
6. singularity, regularity, breakdown, or any Clay alternative A--D.

The packet family changes with \(r\).  The exact revised question is:

> Can one finite-energy first-record trajectory concatenate these locally
> sharp triadic transfers while reusing the same energy quantum, or does
> same-trajectory genealogy force a nonsummable ancestry, transport, or
> variation charge?

## 8. Reproduce

Run

```text
make type-ii-triad-packet
PYTHONPATH=lab python -m unittest \
  lab.tests.test_type_ii_triad_packet -v
```

The certificate checks the six divergence-free Fourier coefficients, exact
dyadic heat multipliers, convolution formula, nonzero flux, positive band
pairing, and all packet radius powers.  It does not certify the
infinite-dimensional local well-posedness argument or any same-trajectory
claim.
