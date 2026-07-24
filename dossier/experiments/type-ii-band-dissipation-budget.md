# Type-II frozen-band works share a critical dissipation budget

- **Experiment:** EXP-TYPE-II-BAND-DISSIPATION-BUDGET-001
- **Route:** ROUTE-R3C
- **Status:** complete analytic reduction; external review pending
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Input:** [frozen-band correlation theorem](type-ii-cross-record-correlation.md)

The frozen-band theorem left a precise question.  At every failed
correlation event, nonlinear or viscous work has fixed magnitude, but the
test changes with the event.  Can those works be charged to one physical
budget?

Yes, after retaining the scale-critical weights.  If

\[
r_j:=r_j^{\mathrm L},
\qquad
I_j:=[t_j,t_{j+1}],
\qquad
h_j:=|I_j|,
\]

then

\[
\boxed{
\sum_j\left[
\nu\sqrt{\frac{r_j}{\gamma}}\,
|\mathcal W_j^{\mathrm N}|
+
\frac{
r_j^2|\mathcal W_j^\nu|^2
}{
\gamma\nu h_j
}
\right]
\lesssim
\nu\int_0^{T^*}\|\nabla u(t)\|_2^2\,dt.
}
\]

Consequently the failed-correlation indices can be partitioned into
nonlinear and viscous events so that

\[
\boxed{
\sum_{j\in\mathcal N}
\nu\sqrt{\gamma r_j}
+
\sum_{j\in\mathcal V}
\frac{\gamma r_j^2}{\nu h_j}
\lesssim E_*,
}
\]

where

\[
E_*:=\sup_{t<T^*}\frac12\|u(t)\|_2^2.
\]

This is the missing common same-trajectory budget.  It is not an unweighted
sum of the fixed works.  The nonlinear price decays like \(\sqrt{r_j}\), and
that exponent is exactly the energy-critical fractional-Sobolev exponent.

There is a second, less welcome conclusion.  One can thin the Gaussian bands
so their scale intervals are disjoint and extend every correlation until its
first death.  Bessel packing then bounds the number of simultaneously live
bands and the same budget sums over their overlapping lifetimes.  However,
the fixed quantile gap forces every band to have a uniform multiplicative
width.  Scale disjointness therefore makes the radii decay geometrically, so
\(\sum_j\sqrt{r_j}<\infty\) automatically.  The elementary
square-function route cannot turn the common budget into a contradiction.

For the exact \(q_j=4\) survivor, the viscous charges diverge while the
nonlinear charges converge.  Thus that survivor is no longer
branch-agnostic: all but finitely many correlation deaths must be paid by
nonlinear transfer.

## 1. Setup

Let \(u\) be a smooth finite-energy Navier--Stokes solution on
\([0,T^*)\):

\[
\partial_tu+\mathbb P\nabla\!\cdot(u\otimes u)=\nu\Delta u,
\qquad
\nabla\!\cdot u=0.
\]

Retain the two physical subgrid-energy quantiles from the preceding theorem:

\[
\mathbf K(r_j^{\mathrm L},t_j)=\eta_{\mathrm L},
\qquad
\mathbf K(r_j^{\mathrm H},t_j)=\eta_{\mathrm H},
\qquad
\gamma:=\eta_{\mathrm H}-\eta_{\mathrm L}>0.
\]

Write \(G_r=\Gamma_r*\) and

\[
S_j:=G_{r_j^{\mathrm L}}^2-G_{r_j^{\mathrm H}}^2,
\qquad
B_j:=S_j^{1/2},
\qquad
\psi_j:=S_ju(t_j).
\]

Its multiplier is

\[
\mathfrak s_j(\xi)
:=
e^{-(r_j^{\mathrm L})^2|\xi|^2}
-
e^{-(r_j^{\mathrm H})^2|\xi|^2}
\ge0,
\]

and

\[
\int_{\mathbb R^3}
\mathfrak s_j(\xi)|\widehat u(t_j,\xi)|^2\,d\xi
=
\|B_ju(t_j)\|_2^2
=2\gamma.
\]

For any endpoint \(s\in(t_j,T^*)\), put

\[
\begin{aligned}
\mathcal W_{j,s}^{\mathrm N}
&:=
\int_{t_j}^{s}\!\!\int_{\mathbb R^3}
u\otimes u:\nabla\psi_j\,dx\,dt,\\
\mathcal W_{j,s}^{\nu}
&:=
-
\nu\int_{t_j}^{s}\!\!\int_{\mathbb R^3}
\nabla u:\nabla\psi_j\,dx\,dt.
\end{aligned}
\]

The exact correlation identity is

\[
\mathcal C_j(s)-2\gamma
=
\mathcal W_{j,s}^{\mathrm N}
+
\mathcal W_{j,s}^{\nu},
\qquad
\mathcal C_j(s)
:=
\langle B_ju(s),B_ju(t_j)\rangle.
\]

Define the physical dissipation on an interval \(I\) by

\[
\mathscr D(I)
:=
\nu\int_I\|\nabla u(t)\|_2^2\,dt,
\qquad
\mathscr D_*:=\mathscr D((0,T^*))\le E_*.
\]

## 2. Exact fractional norms of a frozen Gaussian band

### Lemma 1: band-adapted Sobolev ceiling

For every \(\alpha\ge0\),

\[
\boxed{
\|\psi_j\|_{\dot H^\alpha}^2
\le
C_\alpha\gamma
(r_j^{\mathrm L})^{-2\alpha}.
}
\]

In particular,

\[
\|\psi_j\|_{\dot H^{1/2}}
\lesssim
\sqrt{\frac{\gamma}{r_j^{\mathrm L}}},
\qquad
\|\nabla\psi_j\|_2
\lesssim
\frac{\sqrt\gamma}{r_j^{\mathrm L}}.
\]

#### Proof

Set

\[
x:=(r_j^{\mathrm L})^2|\xi|^2,
\qquad
\rho_j:=\frac{r_j^{\mathrm H}}{r_j^{\mathrm L}}>1.
\]

Then

\[
\mathfrak s_j(\xi)=e^{-x}-e^{-\rho_j^2x}\le e^{-x}.
\]

Since

\[
x^\alpha\mathfrak s_j(\xi)
\le x^\alpha e^{-x}
\le C_\alpha,
\]

we have

\[
x^\alpha\mathfrak s_j(\xi)^2
\le C_\alpha\mathfrak s_j(\xi).
\]

Therefore

\[
\begin{aligned}
\|\psi_j\|_{\dot H^\alpha}^2
&=
\int |\xi|^{2\alpha}
\mathfrak s_j(\xi)^2
|\widehat u(t_j,\xi)|^2\,d\xi\\
&\le
C_\alpha(r_j^{\mathrm L})^{-2\alpha}
\int
\mathfrak s_j(\xi)
|\widehat u(t_j,\xi)|^2\,d\xi\\
&=
2C_\alpha\gamma
(r_j^{\mathrm L})^{-2\alpha}.
\end{aligned}
\]

This proves the claim.

## 3. The critical nonlinear dual estimate

### Lemma 2: energy-critical nonlinear action

For every divergence-free \(v\in H^1(\mathbb R^3)\),

\[
\boxed{
\|\mathbb P\nabla\!\cdot(v\otimes v)\|_{\dot H^{-1/2}}
\lesssim
\|\nabla v\|_2^2.
}
\]

Equivalently, for every solenoidal
\(\phi\in\dot H^{1/2}\),

\[
\left|
\int_{\mathbb R^3}v\otimes v:\nabla\phi\,dx
\right|
\lesssim
\|\nabla v\|_2^2\|\phi\|_{\dot H^{1/2}}.
\]

#### Proof

The Leray projector and
\(\dot H^{-1/2}\nabla\) are order-\(1/2\) Fourier multipliers, so

\[
\|\mathbb P\nabla\!\cdot(v\otimes v)\|_{\dot H^{-1/2}}
\lesssim
\|v\otimes v\|_{\dot H^{1/2}}.
\]

The fractional Leibniz rule with exponents \(3\) and \(6\), followed by
Sobolev embedding, gives

\[
\begin{aligned}
\|v\otimes v\|_{\dot H^{1/2}}
&\lesssim
\|D^{1/2}v\|_3\|v\|_6\\
&\lesssim
\|\nabla v\|_2^2.
\end{aligned}
\]

Duality proves the second formulation.

## 4. Common weighted-work budget

### Theorem 3: consecutive-record budget

Let \(I_j=[t_j,t_{j+1}]\), \(h_j=t_{j+1}-t_j\), and abbreviate

\[
\mathcal W_j^{\mathrm N}
:=\mathcal W_{j,t_{j+1}}^{\mathrm N},
\qquad
\mathcal W_j^\nu
:=\mathcal W_{j,t_{j+1}}^\nu.
\]

Then

\[
\boxed{
\sum_j\left[
\nu\sqrt{\frac{r_j^{\mathrm L}}{\gamma}}\,
|\mathcal W_j^{\mathrm N}|
+
\frac{
(r_j^{\mathrm L})^2|\mathcal W_j^\nu|^2
}{
\gamma\nu h_j
}
\right]
\lesssim
\mathscr D_*.
}
\]

#### Proof

Lemmas 1 and 2 give

\[
\begin{aligned}
|\mathcal W_j^{\mathrm N}|
&\lesssim
\|\psi_j\|_{\dot H^{1/2}}
\int_{I_j}\|\nabla u(t)\|_2^2\,dt\\
&\lesssim
\sqrt{\frac{\gamma}{r_j^{\mathrm L}}}\,
\frac{\mathscr D(I_j)}{\nu}.
\end{aligned}
\]

Hence

\[
\nu\sqrt{\frac{r_j^{\mathrm L}}{\gamma}}\,
|\mathcal W_j^{\mathrm N}|
\lesssim
\mathscr D(I_j).
\]

For the viscous work, Lemma 1 and Cauchy--Schwarz in time give

\[
\begin{aligned}
|\mathcal W_j^\nu|
&\le
\nu\|\nabla\psi_j\|_2
h_j^{1/2}
\left(
\int_{I_j}\|\nabla u(t)\|_2^2\,dt
\right)^{1/2}\\
&\lesssim
\frac{\sqrt\gamma}{r_j^{\mathrm L}}
\sqrt{\nu h_j\mathscr D(I_j)}.
\end{aligned}
\]

Therefore

\[
\frac{
(r_j^{\mathrm L})^2|\mathcal W_j^\nu|^2
}{
\gamma\nu h_j
}
\lesssim
\mathscr D(I_j).
\]

The intervals \(I_j\) are disjoint.  Summing the last two estimates proves
the theorem.

### Corollary 4: additive charges for correlation loss

Let

\[
\mathcal L
:=
\{j:\mathcal C_j(t_{j+1})<\gamma\}.
\]

There is a disjoint partition

\[
\mathcal L=\mathcal N\mathbin{\dot\cup}\mathcal V
\]

such that

\[
|\mathcal W_j^{\mathrm N}|\ge\frac\gamma2
\quad(j\in\mathcal N),
\qquad
|\mathcal W_j^\nu|\ge\frac\gamma2
\quad(j\in\mathcal V),
\]

and

\[
\boxed{
\sum_{j\in\mathcal N}
\nu\sqrt{\gamma r_j^{\mathrm L}}
+
\sum_{j\in\mathcal V}
\frac{
\gamma(r_j^{\mathrm L})^2
}{
\nu h_j
}
\lesssim
\mathscr D_*.
}
\]

In particular,

\[
\sum_{j\in\mathcal L}
\min\left\{
\nu\sqrt{\gamma r_j^{\mathrm L}},
\frac{\gamma(r_j^{\mathrm L})^2}{\nu h_j}
\right\}
<\infty.
\]

#### Proof

If \(j\in\mathcal L\), the correlation identity implies

\[
|\mathcal W_j^{\mathrm N}+\mathcal W_j^\nu|>\gamma.
\]

Assign \(j\) to a term whose magnitude is at least \(\gamma/2\), breaking
ties arbitrarily.  Substitute these floors into Theorem 3.

This is a common budget in the literal sense: every charge is paid by the
same dissipation measure on pairwise disjoint pieces of the same physical
trajectory.

## 5. Correlation lifetimes and Gaussian square packing

The preceding theorem sees only the next selected record.  The same argument
can follow old bands until they actually lose correlation.

Choose an infinite subsequence, relabelled by \(k\), such that

\[
r_{k+1}^{\mathrm H}<r_k^{\mathrm L}.
\]

This is possible because both physical quantile radii tend to zero.

### Lemma 5: exact Gaussian Bessel bound

For every \(f\in L^2(\mathbb R^3)\),

\[
\boxed{
\sum_k\|B_kf\|_2^2\le\|f\|_2^2.
}
\]

#### Proof

The multiplier has the scale-integral representation

\[
\mathfrak s_k(\xi)
=
\int_{(r_k^{\mathrm L})^2}^{(r_k^{\mathrm H})^2}
|\xi|^2e^{-a|\xi|^2}\,da.
\]

The integration intervals are pairwise disjoint subsets of \((0,\infty)\).
Consequently

\[
\sum_k\mathfrak s_k(\xi)
\le
\int_0^\infty|\xi|^2e^{-a|\xi|^2}\,da
=1.
\]

Plancherel proves the result.

For each \(k\), define its first correlation-death time by

\[
\sigma_k
:=
\inf\{t\in(t_k,T^*):\mathcal C_k(t)\le\gamma\},
\]

with \(\sigma_k=T^*\) if this set is empty.  Call the band alive on
\([t_k,\sigma_k)\).

### Theorem 6: bounded-overlap lifetime budget

At every \(t<T^*\), at most

\[
M:=\left\lceil\frac{4E_*}{\gamma}\right\rceil
\]

of the separated bands are alive.  At most \(M\) bands live until \(T^*\).
For all remaining bands, the lifetime intervals

\[
J_k:=[t_k,\sigma_k]
\]

have overlap multiplicity at most \(M\), and

\[
\boxed{
\sum_k\left[
\nu\sqrt{\frac{r_k^{\mathrm L}}{\gamma}}\,
|\mathcal W_{k,\sigma_k}^{\mathrm N}|
+
\frac{
(r_k^{\mathrm L})^2
|\mathcal W_{k,\sigma_k}^{\nu}|^2
}{
\gamma\nu(\sigma_k-t_k)
}
\right]
\lesssim
M\mathscr D_*.
}
\]

After assigning each finite death to a nonlinear or viscous work floor,

\[
\boxed{
\sum_{k\in\mathcal N_{\rm death}}
\nu\sqrt{\gamma r_k^{\mathrm L}}
+
\sum_{k\in\mathcal V_{\rm death}}
\frac{
\gamma(r_k^{\mathrm L})^2
}{
\nu(\sigma_k-t_k)
}
\lesssim
M\mathscr D_*.
}
\]

#### Proof

If band \(k\) is alive at time \(t\), then

\[
\gamma
<
\mathcal C_k(t)
\le
\|B_ku(t)\|_2\|B_ku(t_k)\|_2
=
\sqrt{2\gamma}\,\|B_ku(t)\|_2.
\]

Hence

\[
\|B_ku(t)\|_2^2>\frac\gamma2.
\]

Lemma 5 and the energy ceiling give

\[
\frac\gamma2
\#\{k:k\text{ is alive at }t\}
<
\sum_{k:\,\mathrm{alive}}\|B_ku(t)\|_2^2
\le
\|u(t)\|_2^2
\le2E_*.
\]

This proves the overlap bound.  It also permits at most \(M\) bands with
\(\sigma_k=T^*\).

For finite deaths, continuity gives

\[
\mathcal C_k(\sigma_k)=\gamma.
\]

The proof of Theorem 3 applies on \(J_k\).  Since the \(J_k\) have
multiplicity at most \(M\),

\[
\sum_k\mathscr D(J_k)
\le
M\mathscr D_*.
\]

This proves both displayed budgets.

## 6. Why the elementary square-function route still stops

The quantile gap itself forces each Gaussian band to occupy a fixed amount
of logarithmic scale.

### Lemma 7: uniform multiplicative width

For every \(j\),

\[
\boxed{
\frac{r_j^{\mathrm H}}{r_j^{\mathrm L}}
\ge
\Lambda
:=
\left(1+\frac{e\gamma}{E_*}\right)^{1/2}
>1.
}
\]

#### Proof

With \(\rho=r_j^{\mathrm H}/r_j^{\mathrm L}\),

\[
e^{-x}-e^{-\rho^2x}
=
\int_1^{\rho^2}xe^{-sx}\,ds
\le
(\rho^2-1)xe^{-x}
\le
\frac{\rho^2-1}{e}.
\]

Therefore

\[
2\gamma
\le
\frac{\rho^2-1}{e}\|u(t_j)\|_2^2
\le
\frac{2E_*(\rho^2-1)}{e}.
\]

Rearrangement proves the claim.

On the scale-disjoint subsequence,

\[
r_{k+1}^{\mathrm H}
<
r_k^{\mathrm L}
\le
\Lambda^{-1}r_k^{\mathrm H}.
\]

Thus

\[
\sum_k\sqrt{r_k^{\mathrm L}}
\le
\sum_k\sqrt{r_k^{\mathrm H}}
<\infty.
\]

This is the exact ceiling of the naive Bessel strategy.  Scale separation
gives bounded simultaneous correlation lifetimes, but it simultaneously
makes the critical nonlinear death charges geometrically summable.  The
common dissipation budget is therefore compatible with infinitely many
nonlinear deaths.

The result does not exclude a more structured square-function or adjoint
argument.  It proves that an argument using only:

1. Gaussian scale separation;
2. Bessel packing at a common time;
3. the energy identity; and
4. the critical fractional product estimate

cannot close R3C.

## 7. Exact survivor audit

For the existing representative ledger,

\[
r_j^{\mathrm L}\asymp2^{-5j},
\qquad
h_j\asymp\frac{2^{-11j}}j,
\qquad
\nu=1.
\]

The two death charges are

\[
\nu\sqrt{\gamma r_j^{\mathrm L}}
\asymp
\sqrt\gamma\,2^{-5j/2},
\]

and

\[
\frac{\gamma(r_j^{\mathrm L})^2}{\nu h_j}
\asymp
\gamma j2^j.
\]

Hence

\[
\sum_j\nu\sqrt{\gamma r_j^{\mathrm L}}<\infty,
\qquad
\sum_j
\frac{\gamma(r_j^{\mathrm L})^2}{\nu h_j}
=\infty.
\]

The old Hilbert rotation remains compatible only if all but finitely many
deaths are assigned to nonlinear work.  Its summable residence reservoir

\[
c_j\asymp\frac{2^{-j}}j
\]

is more than large enough to cover the new
\(2^{-5j/2}\) nonlinear charges.  The ledger remains non-NSE, but its
surviving branch is now sharply identified.

## 8. Route consequence

This round closes three narrower questions:

1. successive event-dependent nonlinear works do have a common weighted
   physical budget;
2. separated old-band lifetimes can be summed despite temporal overlap; and
3. the representative Zeno ledger cannot use viscous correlation death
   infinitely often.

It does not prove:

1. an unweighted sum of fixed replacement works;
2. a divergent lower bound for the critical \(\sqrt{r_j}\) charges;
3. control of the unthinned, heavily overlapping logarithmic-scale stack;
4. an adjoint cancellation improving the critical half-derivative;
5. a Navier--Stokes realisation or obstruction of the nonlinear rotation;
6. spatial recentering, coherent-trace rigidity, or divergent-energy
   control;
7. regularity, breakdown, or any Clay alternative A--D.

The next bounded question is:

> Does the unthinned first-record stack obey a logarithmic-scale
> Carleson/variation law that counts overlapping Gaussian bands without
> thinning them into an automatically summable geometric sequence, or can
> actual Navier--Stokes triads realise the remaining nonlinear rotation
> ledger?
