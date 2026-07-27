# A low-pass NSE clock excludes compact carriers on the \(q=4\) schedule

- **Experiment:** EXP-TYPE-II-COMPACT-CARRIER-CLOCK-001
- **Route:** ROUTE-R3C
- **Status:** complete conditional exclusion theorem; external review pending
- **Domain:** smooth finite-energy Navier--Stokes flow on \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** [carrier entrance](type-ii-inviscid-carrier-entrance.md),
  cross-record ledger, and
  local packet sharpness

## Verdict

The exact \(q_j=4\) power survivor cannot have an infinite subsequence whose
energy-normalised carrier profiles are nonzero and strongly precompact in
\(L^2\).

The reason is an unconditional low-frequency clock.  A bounded-energy smooth
NSE solution can change frequencies below \(\Lambda\) at most at rate

\[
C\left(E_*\Lambda^{5/2}
       +\nu\sqrt{E_*}\Lambda^2\right).
\]

At carrier radius \(R\), this makes an order-one low-frequency replacement
take at least \(cR^{5/2}\).  But the representative survivor has

\[
R_j\asymp2^{-4j},
\qquad
R_j^{5/2}\asymp2^{-10j},
\qquad
t_{j+1}-t_j\asymp\frac{2^{-11j}}j.
\]

After a fixed number of generations, a much smaller compact carrier has
evacuated the old carrier's low frequencies, independently of its new centre.
The allowed time is nevertheless \(o(R_j^{5/2})\), contradicting the clock.

This does **not** eliminate the Type-II route or even the full \(q=4\) scalar
ledger.  It proves that any NSE realisation of that ledger must lose strong
carrier compactness.  Any remaining mechanism must use unresolved
microstructure, escape or fragmentation in the carrier coordinates, or
another noncompact defect.  Charging that defect is the remaining problem.

## 1. Critical dilations

For \(R>0\) and \(z\in\mathbb R^3\), define the \(L^2\)-unitary
dilation-translation

\[
(\mathcal D_{R,z}f)(x)
:=
R^{-3/2}f\!\left(\frac{x-z}{R}\right).
\]

Fix a radial \(\chi\in C_c^\infty(\mathbb R^3)\) with

\[
0\le\chi\le1,
\qquad
\chi(\xi)=1\quad(|\xi|\le1),
\qquad
\chi(\xi)=0\quad(|\xi|\ge2),
\]

and let \(P_{\le\Lambda}\) be the Fourier multiplier
\(\chi(\xi/\Lambda)\).

### Lemma 1: compact sets evacuate low frequencies under strict dilation

Let \(\mathcal K\subset L^2(\mathbb R^3)\) be relatively compact and suppose

\[
d:=\inf_{f\in\mathcal K}\|f\|_2>0.
\]

There are \(K<\infty\), \(\lambda_0\in(0,1)\), and \(\delta>0\) such that
for every \(f,g\in\mathcal K\), \(z\in\mathbb R^3\), and
\(0<\lambda\le\lambda_0\),

\[
\boxed{
\left\|
P_{\le K}\bigl(f-\mathcal D_{\lambda,z}g\bigr)
\right\|_2
\ge\delta .
}
\]

#### Proof

The operators \(P_{\le K}\) converge strongly to the identity as
\(K\to\infty\).  Strong convergence is uniform on compact subsets, so choose
\(K\) such that

\[
\sup_{f\in\mathcal K}
\|(I-P_{\le K})f\|_2
\le\frac d8.
\]

Consequently

\[
\inf_{f\in\mathcal K}\|P_{\le K}f\|_2
\ge\frac{7d}{8}.
\]

With a unitary Fourier convention,

\[
\widehat{\mathcal D_{\lambda,z}g}(\xi)
=
\lambda^{3/2}e^{-iz\cdot\xi}\widehat g(\lambda\xi).
\]

Therefore

\[
\begin{aligned}
\|P_{\le K}\mathcal D_{\lambda,z}g\|_2^2
&=
\int_{\mathbb R^3}
\left|\chi\!\left(\frac{\eta}{\lambda K}\right)\right|^2
|\widehat g(\eta)|^2\,d\eta\\
&\le
\int_{|\eta|\le2\lambda K}|\widehat g(\eta)|^2\,d\eta .
\end{aligned}
\]

The bound is independent of \(z\).  For each fixed \(g\), it tends to zero
as \(\lambda\downarrow0\).  The convergence is uniform on
\(\mathcal K\): cover its closure by a finite \(L^2\) net and use that all
the displayed multipliers have operator norm at most one.  Thus

\[
\sup_{g\in\overline{\mathcal K},\,z\in\mathbb R^3}
\|P_{\le K}\mathcal D_{\lambda,z}g\|_2
\longrightarrow0.
\]

Shrink \(\lambda_0\) until this supremum is at most \(d/8\).  The triangle
inequality then gives

\[
\left\|
P_{\le K}\bigl(f-\mathcal D_{\lambda,z}g\bigr)
\right\|_2
\ge\frac{3d}{4}.
\]

Thus one may take \(\delta=3d/4\).

## 2. The energy-only low-pass clock

Let \(u\) be a smooth finite-energy solution of

\[
\partial_tu+\mathbb P\nabla\!\cdot(u\otimes u)
=\nu\Delta u,
\qquad
\nabla\cdot u=0,
\]

on \([s,t]\), and set

\[
E_*:=\sup_{\tau\in[s,t]}\frac12\|u(\tau)\|_2^2.
\]

### Theorem 2: low-frequency temporal Lipschitz estimate

For every \(\Lambda>0\),

\[
\boxed{
\|P_{\le\Lambda}(u(t)-u(s))\|_2
\le
C_\chi
\left(
E_*\Lambda^{5/2}
+\nu\sqrt{E_*}\Lambda^2
\right)(t-s).
}
\]

The constant depends only on the fixed cutoff and Fourier convention.

#### Proof

Integrating the projected equation gives

\[
\begin{aligned}
P_{\le\Lambda}(u(t)-u(s))
={}&
-\int_s^t
P_{\le\Lambda}\mathbb P\nabla\!\cdot(u\otimes u)(\tau)\,d\tau\\
&+
\nu\int_s^tP_{\le\Lambda}\Delta u(\tau)\,d\tau .
\end{aligned}
\]

Each component of the first operator has multiplier

\[
\chi(\xi/\Lambda)\,
i\xi_\ell
\left(\delta_{im}-\frac{\xi_i\xi_m}{|\xi|^2}\right).
\]

Its convolution kernel has \(L^2\) norm \(C_\chi\Lambda^{5/2}\):
this follows directly from Plancherel, or from one derivative and
three-dimensional kernel scaling.  Young's inequality and
\(\|u\otimes u\|_1\le\|u\|_2^2\) yield

\[
\|P_{\le\Lambda}\mathbb P\nabla\!\cdot(u\otimes u)\|_2
\le
C_\chi\Lambda^{5/2}\|u\|_2^2
\le
2C_\chi E_*\Lambda^{5/2}.
\]

The viscous multiplier is bounded by \(C_\chi\Lambda^2\), so

\[
\nu\|P_{\le\Lambda}\Delta u\|_2
\le
C_\chi\nu\Lambda^2\|u\|_2
\le
C_\chi\nu\sqrt{2E_*}\Lambda^2.
\]

Integrating these two pointwise bounds proves the theorem after enlarging
\(C_\chi\).

### Corollary 3: an order-one replacement needs turnover time

If

\[
\|P_{\le K/R}(u(t)-u(s))\|_2\ge\delta,
\]

then

\[
\boxed{
t-s
\ge
\frac{\delta R^{5/2}}
{C_\chi\left(E_*K^{5/2}
+\nu\sqrt{E_*}K^2R^{1/2}\right)}.
}
\]

For fixed \(E_*,\nu,K,\delta\) and \(R\downarrow0\), the right-hand side is
bounded below by \(cR^{5/2}\).

#### Proof

Apply Theorem 2 with \(\Lambda=K/R\) and rearrange.

The exponent \(5/2\) is the fixed-energy nonlinear turnover exponent.
Viscosity contributes \(R^2\), but its coefficient becomes
\(\nu R^{1/2}\) after the common \(R^{-5/2}\) factor is removed; hence it
does not accelerate the small-scale replacement.

## 3. Compact carrier exclusion

For arbitrary record centres \(x_j\), record radii \(R_j\downarrow0\), and
times \(t_j\uparrow T^*\), define the exact energy-normalised carrier state

\[
F_j(y)
:=
R_j^{3/2}u(x_j+R_jy,t_j).
\]

Then

\[
u(\cdot,t_j)=\mathcal D_{R_j,x_j}F_j
\]

and \(\|F_j\|_2=\|u(t_j)\|_2\).

### Theorem 4: compact carriers obey a cross-scale clock

Suppose \(\{F_j\}\) is relatively compact in \(L^2(\mathbb R^3)\) and

\[
\inf_j\|F_j\|_2>0.
\]

There are \(\lambda_0,c>0\), depending only on the compact carrier family,
the energy ceiling, viscosity, and cutoff, such that whenever \(j<k\) is
sufficiently large and

\[
\frac{R_k}{R_j}\le\lambda_0,
\]

one has

\[
\boxed{
t_k-t_j\ge cR_j^{5/2}.
}
\]

The estimate is uniform in both centres.

#### Proof

Apply Lemma 1 to the closure of \(\{F_j\}\).  In the coordinates of the
\(j\)-th carrier,

\[
\mathcal D_{R_j,x_j}^{-1}
\mathcal D_{R_k,x_k}F_k
=
\mathcal D_{\lambda,z}F_k,
\qquad
\lambda=\frac{R_k}{R_j},
\qquad
z=\frac{x_k-x_j}{R_j}.
\]

The low-pass covariance and unitarity of \(\mathcal D_{R_j,x_j}\) give

\[
\begin{aligned}
&\left\|
P_{\le K/R_j}
\bigl(u(t_j)-u(t_k)\bigr)
\right\|_2\\
&\qquad=
\left\|
P_{\le K}
\bigl(F_j-\mathcal D_{\lambda,z}F_k\bigr)
\right\|_2
\ge\delta .
\end{aligned}
\]

Corollary 3 now gives

\[
t_k-t_j
\ge
\frac{\delta R_j^{5/2}}
{C_\chi\left(E_*K^{5/2}
+\nu\sqrt{E_*}K^2R_j^{1/2}\right)}.
\]

Since \(R_j\to0\), the denominator is uniformly bounded for large \(j\).
This proves the claim.  The arbitrary vector \(z\) shows that moving record
centres do not evade this particular clock.

## 4. Exclusion of the compact \(q=4\) representative

The exact scalar survivor has, up to fixed comparison constants,

\[
R_j=2^{-4j},
\qquad
t_{j+1}-t_j=\frac{c_t2^{-11j}}j.
\]

### Corollary 5: the representative ledger has no compact-profile subsequence

No smooth finite-energy NSE trajectory can satisfy the preceding scale and
time schedule while an infinite subsequence of its exact carrier states
\(F_j\) is relatively compact in \(L^2\) and bounded away from zero.

#### Proof

Suppose such a subsequence exists and apply Theorem 4 to it.  For every
sufficiently large retained index \(j\), choose a later retained \(k\) with

\[
\frac{R_k}{R_j}\le\lambda_0.
\]

Theorem 4 requires

\[
t_k-t_j\ge cR_j^{5/2}=c2^{-10j}.
\]

On the other hand,

\[
t_k-t_j
\le
T^*-t_j
=
\sum_{n\ge j}\frac{c_t2^{-11n}}n
\le
C\frac{2^{-11j}}j.
\]

Consequently

\[
\frac{t_k-t_j}{R_j^{5/2}}
\le
C\frac{2^{-j}}j
\longrightarrow0,
\]

a contradiction.  The same proof works for two-sided comparable powers.

## 5. Relation to the Type-II carrier normalisation

The carrier entrance theorem uses

\[
v_j(y,0)
=
\frac1{a_j}u(x_j+R_jy,t_j),
\qquad
b_j=a_j^2R_j^3.
\]

Hence the present profile is exactly

\[
F_j=\sqrt{b_j}\,v_j(\cdot,0).
\]

In an energy-efficient cell, the amplitude layer gives
\(\|F_j\|_2^2\ge c\,b_j\), so a positive lower bound for \(b_j\) keeps the
profiles away from zero.  If \(b_j\) is bounded and a subsequence of
\(v_j(\cdot,0)\) is strongly \(L^2\)-precompact, then after taking a
convergent scalar subsequence the corresponding \(F_j\) are precompact.
Corollary 5 excludes even this subsequential configuration on the exact
\(q=4\) schedule.

This closes the most literal same-trajectory lift of the previous packet
family: completed compact carrier states cannot simply follow one another
at the representative record speed.  It also explains why the local
one-event construction does not settle the route.  The actual subgrid
radius

\[
r_j=R_j\ell_j\asymp2^{-5j}
\]

has local turnover

\[
r_j^{5/2}\asymp2^{-25j/2},
\]

which is shorter than the allowed record gap \(2^{-11j}/j\).  A packet
already stored below the carrier scale can therefore still act in time.
The theorem forces attention precisely onto that pre-storage.

## 6. What is now proved

Subject to external review, the robust conclusions are:

1. bounded energy alone gives an unconditional low-pass NSE Lipschitz clock;
2. strict critical dilation uniformly evacuates fixed low frequencies on
   every compact nonzero \(L^2\) family, uniformly in translations;
3. nonzero compact carrier profiles need \(cR^{5/2}\) to move through a
   sufficiently large fixed scale ratio;
4. the exact \(q=4\) record schedule is too fast by the factor
   \(2^{-j}/j\); and
5. the representative scalar ledger has no infinite nonzero strongly
   precompact carrier-profile subsequence.

These are theorem-level statements within the stated assumptions.  They are
new to this repository; no claim of novelty relative to the mathematical
literature is made before external review.

## 7. What remains open

The result does not prove:

1. that any putative Type-II singularity follows the representative \(q=4\)
   schedule;
2. a fixed old-scale low-frequency floor without strong carrier compactness;
3. that carrier noncompactness must be frequency ancestry rather than
   spatial escape, fragmentation, or oscillation;
4. a nonsummable charge for nested subgrid packets;
5. coherent Euler-trace rigidity;
6. control of the divergent-normalised-energy cells; or
7. regularity, breakdown, or any Clay alternative A--D.

The next exact question is:

> If a first-record trajectory outruns the carrier clock, can its mandatory
> failure of \(L^2\) compactness be decomposed into nested frequency ancestry
> and spatial escape, with either branch paying a nonsummable physical
> charge?

No executable artefact is added.  The content is an analytic Fourier/PDE
estimate, and a ceremonial exponent checker would add no independent
certificate.
