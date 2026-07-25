# The q4 boundary work is a diagonal Gaussian flux with an exact recycling law

- **Experiment:** EXP-TYPE-II-DIAGONAL-HEAT-FLUX-RECYCLING-001
- **Route:** ROUTE-R3C
- **Status:** complete conditional reduction; external review pending
- **Domain:** smooth finite-energy Navier--Stokes flow on \(\mathbb R^3\)
- **Clay status:** unsolved
- **Input:** [boundary heat impulse](type-ii-boundary-heat-impulse.md)

## Verdict

The future-dependent heat-deviation work has an exact current-time form.
Put

\[
F(s):=\mathbb P((U\cdot\nabla)v)(s),
\qquad
S(r):=e^{\nu r\Delta},
\tag{1}
\]

and, for fixed \(\tau>0\), define the moving heat field

\[
w_\tau(s):=S(\tau-s)v(s),
\qquad
0<s\le\tau.
\tag{2}
\]

The opening heat cutoff cancels viscosity:

\[
\boxed{
\partial_s w_\tau(s)
=
-S(\tau-s)F(s).
}
\tag{3}
\]

The weak-zero boundary theorem gives

\[
w_\tau(s)\longrightarrow0
\quad\hbox{strongly in }L^2
\quad(s\downarrow0),
\qquad
w_\tau(\tau)=v(\tau).
\tag{4}
\]

Therefore

\[
\boxed{
\frac12\|v(\tau)\|_2^2
=
\int_0^\tau\Pi_{\tau-s}(s)\,ds,
}
\tag{5}
\]

where the exact diagonal Gaussian flux is

\[
\boxed{
\begin{aligned}
\Pi_r(s)
&:=
-\langle F(s),S(2r)v(s)\rangle\\
&=
\int_{\mathbb R^3}
U_j(s)v_i(s)
\partial_jS(2r)v_i(s)\,dx.
\end{aligned}
}
\tag{6}
\]

Pressure is absent.  The flux uses only the field at time \(s\), and

\[
\Pi_0(s)=0
\tag{7}
\]

by instantaneous transport cancellation.  Thus (5) preserves the
endpoint cancellation without a future detector.

The heat-age dependence is itself a signed band integral:

\[
\boxed{
\Pi_r(s)
=
\langle F(s),(I-S(2r))v(s)\rangle
=
-2\nu\int_0^r
\langle F(s),\Delta S(2\rho)v(s)\rangle\,d\rho.
}
\tag{8}
\]

For two terminal ages \(0<\sigma<\tau\), (5) and the entrance energy
identity give the exact recycling law

\[
\boxed{
\begin{aligned}
&\int_0^\sigma
\bigl(
\Pi_{\sigma-s}(s)-\Pi_{\tau-s}(s)
\bigr)\,ds\\
&\qquad=
\int_\sigma^\tau\Pi_{\tau-s}(s)\,ds
+\nu\int_\sigma^\tau\|\nabla v(s)\|_2^2\,ds.
\end{aligned}
}
\tag{9}
\]

The left side is work through the positive Gaussian band

\[
S(2(\sigma-s))-S(2(\tau-s)).
\tag{10}
\]

Equation (9) says exactly how the same energy quantum can be reused:
new-block work plus viscous loss is paid by shifting the shared earlier
history through one Gaussian heat band.

These bands have a genuine \(\ell^1\) orthogonality estimate.  If
\(\{[a_k,b_k]\}\) are disjoint heat-age intervals and

\[
B_k:=S(2a_k)-S(2b_k)\ge0,
\tag{11}
\]

then

\[
\boxed{
\sum_k
\left|
\langle F(s),B_kv(s)\rangle
\right|
\lesssim
M(s)Y(s)^2,
}
\tag{12}
\]

where

\[
M(s):=\|U(s)\|_{L^{3,\infty}},
\qquad
Y(s):=\|\nabla v(s)\|_2.
\tag{13}
\]

Consequently, for any decreasing terminal schedule
\(\tau_0>\tau_1>\cdots\downarrow0\), the absolute recycling variation
over finitely many adjacent bands obeys

\[
\boxed{
\sum_{j=J}^K|\mathcal R_j|
\lesssim
\int_0^{\tau_{J+1}}M(s)Y(s)^2\,ds,
}
\tag{14}
\]

with

\[
\mathcal R_j
:=
\int_0^{\tau_{j+1}}
\bigl(
\Pi_{\tau_{j+1}-s}(s)
-\Pi_{\tau_j-s}(s)
\bigr)\,ds.
\tag{15}
\]

This is the desired Gaussian-band non-reuse inequality, but its budget is
not finite.  The preceding q4 entrance theorem already forces

\[
\int_0^hM(s)Y(s)^2\,ds=\infty
\qquad(h>0).
\tag{16}
\]

The orthogonality therefore lands exactly on the known divergent
amplitude-weighted dissipation rather than the finite unweighted
dissipation.

This failure is sharp for the scalar diagonal, recycling, magnitude, and
variation constraints.  Moreover, the constant-energy core of the
survivor below has an exact signed heat-spectrum representation.  Let

\[
\ell(s):=\log(e/s),
\quad
M_\sharp=s^{-2/11}\ell^{-2/11},
\quad
Y_\sharp=s^{-9/22}\ell^{1/11},
\tag{17}
\]

\[
D_\sharp(t):=\int_0^tY_\sharp(s)^2\,ds,
\qquad
E_\sharp(t):=d-2\nu D_\sharp(t)>0
\tag{18}
\]

for small \(t\).  For any integer \(n\ge1\), set

\[
\boxed{
\Pi_n^\sharp(r,s)
:=
\frac{(n+1)E_\sharp(r+s)}2
\frac{r^n}{(r+s)^{n+1}}.
}
\tag{19}
\]

Then

\[
\Pi_n^\sharp(0,s)=0,
\qquad
\int_0^\tau
\Pi_n^\sharp(\tau-s,s)\,ds
=\frac12E_\sharp(\tau),
\tag{20}
\]

so the positive kernel satisfies the exact endpoint cancellation,
diagonal work identity, energy decay, and recycling law.  It obeys the
same heat bound as an actual flux:

\[
\Pi_n^\sharp(r,s)
\lesssim_n
r^{-1/2}M_\sharp(s)Y_\sharp(s)
\tag{21}
\]

near the boundary.  Its total heat-age variation satisfies

\[
\operatorname{Var}_{r>0}
\Pi_n^\sharp(r,s)
\lesssim_n
s^{-1}
=
M_\sharp(s)Y_\sharp(s)^2,
\tag{22}
\]

so it also saturates the Gaussian-band budget (12).

It can recycle arbitrarily much work through shared early history.  If
\(\sigma=q\tau\), \(0<q<1\), then

\[
\boxed{
\frac{
\int_0^{q\tau}
\Pi_n^\sharp(\tau-s,s)\,ds
}{
\int_0^\tau
\Pi_n^\sharp(\tau-s,s)\,ds
}
=
1-(1-q)^{n+1}.
}
\tag{23}
\]

For fixed \(q\), this tends to one as \(n\to\infty\).

The core heat-age profile is not arbitrary.  It has the exact signed
Laplace representation

\[
\boxed{
\frac{r^n}{(r+s)^{n+1}}
=
\int_0^\infty
e^{-r\lambda}e^{-s\lambda}
L_n(s\lambda)\,d\lambda,
}
\tag{24}
\]

where

\[
L_n(z)
:=
\sum_{k=0}^n
\binom nk\frac{(-z)^k}{k!}.
\tag{25}
\]

Thus endpoint cancellation, positivity of the diagonal total,
the proved scalar band budget, q4 magnitude, and arbitrarily strong
early-history reuse remain mutually compatible.  Formula (24) adds an
exact Gaussian spectral representation only for the leading
constant-energy core.  It does not realise the full factor
\(E_\sharp(r+s)\), a Navier--Stokes triad, or one trajectory.

The live gate is sharper:

> Prove that the actual nonlinear spectral density
> \(F=\mathbb P((U\cdot\nabla)v)\) cannot realise a coherent
> Laguerre-type reuse kernel on one q4 trajectory, or replace the
> divergent budget in (12) by a finite same-trajectory charge.

No such theorem is established here.  No Clay alternative is proved.

## 1. Moving heat energy

The input theorem gives

\[
\partial_sv-\nu\Delta v+F=0,
\tag{26}
\]

\[
v(s)\rightharpoonup0,
\qquad
\|v(s)\|_2^2
+2\nu\int_0^sY(r)^2\,dr
=d.
\tag{27}
\]

The zero-boundary mild theorem also proves, for every fixed \(\tau>0\),

\[
S(\tau-s)v(s)\longrightarrow0
\quad\hbox{strongly in }L^2
\quad(s\downarrow0).
\tag{28}
\]

### Theorem 1: viscosity-free moving heat evolution

Equations (3)--(7) hold.

#### Proof

Differentiate (2).  Since

\[
\partial_sS(\tau-s)=-\nu\Delta S(\tau-s),
\]

equation (26) gives

\[
\begin{aligned}
\partial_sw_\tau
&=
-\nu\Delta S(\tau-s)v
+S(\tau-s)(\nu\Delta v-F)\\
&=
-S(\tau-s)F,
\end{aligned}
\]

which is (3).  Equation (4) is (28) at the lower boundary and the
definition at the upper boundary.

Now

\[
\begin{aligned}
\frac d{ds}\frac12\|w_\tau(s)\|_2^2
&=
-\langle S(\tau-s)F(s),S(\tau-s)v(s)\rangle\\
&=
-\langle F(s),S(2(\tau-s))v(s)\rangle\\
&=
\Pi_{\tau-s}(s).
\end{aligned}
\tag{29}
\]

Integrating (29) from zero to \(\tau\) proves (5)--(6).
At \(r=0\),

\[
\Pi_0(s)
=
-\langle\mathbb P((U\cdot\nabla)v),v\rangle
=0,
\]

which proves (7).

### Interpretation

The cutoff in (2) opens at exactly the heat rate.  Its time derivative
cancels physical viscosity, so its energy can change only through
nonlinear flux.  The boundary defect is therefore one half of a moving
Gaussian low-pass flux, with no pressure and no explicit dissipative
error.

## 2. Continuous Gaussian bands

### Proposition 2: heat-age band representation

Equation (8) holds.

#### Proof

The cancellation (7) gives

\[
\Pi_r
=
\langle F,(I-S(2r))v\rangle.
\tag{30}
\]

Since

\[
I-S(2r)
=
-2\nu\int_0^r\Delta S(2\rho)\,d\rho,
\tag{31}
\]

substitution gives (8).

### Pointwise heat estimate

Lorentz Hölder and heat smoothing give

\[
\|F(s)\|_{L^{6/5,2}}
\lesssim
M(s)Y(s),
\tag{32}
\]

\[
\|S(2r)v(s)\|_{L^{6,2}}
\lesssim
(\nu r)^{-1/2}\|v(s)\|_2.
\tag{33}
\]

Consequently

\[
\boxed{
|\Pi_r(s)|
\lesssim
\sqrt d\,(\nu r)^{-1/2}M(s)Y(s).
}
\tag{34}
\]

This is the exact heat-flux magnitude tested by the survivor (21).

## 3. Nested terminal recycling

### Theorem 3: exact recycling identity

Equation (9) holds for every \(0<\sigma<\tau\).

#### Proof

Define

\[
\Phi(\tau)
:=
\int_0^\tau\Pi_{\tau-s}(s)\,ds
=\frac12\|v(\tau)\|_2^2.
\tag{35}
\]

Then

\[
\begin{aligned}
\Phi(\tau)-\Phi(\sigma)
={}&
\int_0^\sigma
\bigl(
\Pi_{\tau-s}-\Pi_{\sigma-s}
\bigr)\,ds\\
&+
\int_\sigma^\tau\Pi_{\tau-s}\,ds.
\end{aligned}
\tag{36}
\]

The energy identity (27) gives

\[
\Phi(\tau)-\Phi(\sigma)
=
-\nu\int_\sigma^\tau Y(s)^2\,ds.
\tag{37}
\]

Rearranging (36)--(37) proves (9).

### Interpretation

For \(s<\sigma\), the heat-age intervals

\[
[\sigma-s,\tau-s]
\tag{38}
\]

move one shared piece of history through the Gaussian band (10).
Equation (9) is an equality, not a bound: it is the exact bookkeeping
law for reuse between two terminal detectors.

## 4. Orthogonality of disjoint heat bands

### Theorem 4: the Gaussian \(\ell^1\) band budget

For every fixed positive \(s\), let

\[
0\le a_k<b_k<\infty
\tag{39}
\]

be pairwise disjoint intervals.  Then (12) holds.

#### Proof

The Fourier symbol of \(B_k\) is

\[
\beta_k(\xi)
=
e^{-2\nu a_k|\xi|^2}
-e^{-2\nu b_k|\xi|^2}
\ge0.
\tag{40}
\]

Disjointness and monotonicity of the exponential give

\[
\sum_k\beta_k(\xi)\le1
\qquad(\xi\in\mathbb R^3).
\tag{41}
\]

Let \(C_k:=B_k^{1/2}\).  In the
\(\dot H^{-1}\)--\(\dot H^1\) duality,

\[
\langle F,B_kv\rangle
=
\langle C_kF,C_kv\rangle.
\tag{42}
\]

Therefore Cauchy--Schwarz first over \(k\), then in Fourier space, gives

\[
\begin{aligned}
\sum_k|\langle F,B_kv\rangle|
&\le
\left(\sum_k\|C_kF\|_{\dot H^{-1}}^2\right)^{1/2}
\left(\sum_k\|C_kv\|_{\dot H^1}^2\right)^{1/2}\\
&\le
\|F\|_{\dot H^{-1}}\|\nabla v\|_2.
\end{aligned}
\tag{43}
\]

For every solenoidal test field \(\phi\),

\[
\begin{aligned}
|\langle F,\phi\rangle|
&=
\left|
\int U_jv_i\partial_j\phi_i
\right|\\
&\lesssim
\|U\|_{L^{3,\infty}}
\|v\|_{L^{6,2}}
\|\nabla\phi\|_2\\
&\lesssim
M Y\|\nabla\phi\|_2.
\end{aligned}
\tag{44}
\]

Thus

\[
\|F\|_{\dot H^{-1}}\lesssim M Y.
\tag{45}
\]

Equations (43)--(45) prove (12).

### Corollary 5: recycling variation

Equations (14)--(15) hold for every finite \(J\le K\).

#### Proof

For a fixed \(s\), the intervals

\[
[\tau_{j+1}-s,\tau_j-s],
\qquad
s<\tau_{j+1},
\tag{46}
\]

are pairwise disjoint.  Apply Theorem 4, integrate in \(s\), and use
the triangle inequality.

### Exact obstruction

If \(\int_0^hMY^2\) were finite, (14) would give a finite total-variation
budget for all Gaussian recycling bands.  But the full-defect entrance
already forces (16).  Orthogonality has therefore recovered the exact
divergent action rather than a contradiction.

## 5. A coherent positive reuse kernel

Use the power--log functions (17).  They obey

\[
\int_0^tM_\sharp^2
\asymp
t^{7/11}\ell(t)^{-4/11},
\tag{47}
\]

\[
D_\sharp(t)
\asymp
t^{2/11}\ell(t)^{2/11},
\tag{48}
\]

\[
M_\sharp(t)Y_\sharp(t)^2=t^{-1}.
\tag{49}
\]

Choose the terminal interval small enough that \(E_\sharp>0\).

### Proposition 6: exact diagonal and recycling saturation

For every integer \(n\ge1\), the kernel (19) satisfies
(20)--(23).

#### Proof

Positivity and the endpoint identity are immediate.  Along the diagonal
\(r+s=\tau\),

\[
\begin{aligned}
\int_0^\tau\Pi_n^\sharp(\tau-s,s)\,ds
&=
\frac{(n+1)E_\sharp(\tau)}
{2\tau^{n+1}}
\int_0^\tau(\tau-s)^n\,ds\\
&=
\frac12E_\sharp(\tau).
\end{aligned}
\tag{50}
\]

Since

\[
E_\sharp(\tau)-E_\sharp(\sigma)
=
-2\nu\int_\sigma^\tau Y_\sharp(s)^2\,ds,
\tag{51}
\]

subtracting (50) at \(\tau\) and \(\sigma\) gives the scalar version of
the recycling identity (9).

For (21), put \(x=r/s\).  Since

\[
r^{-1/2}M_\sharp(s)Y_\sharp(s)
=
s^{-12/11}\ell(s)^{-1/11}x^{-1/2},
\tag{52}
\]

one has

\[
\frac{
\Pi_n^\sharp(r,s)
}{
r^{-1/2}M_\sharp(s)Y_\sharp(s)
}
\lesssim_n
s^{1/11}\ell(s)^{1/11}
\frac{x^{n+1/2}}{(1+x)^{n+1}}.
\tag{53}
\]

The \(x\)-factor is bounded and the \(s\)-factor tends to zero.  This
proves (21) near the boundary.

For fixed \(s\), the core

\[
\frac{r^n}{(r+s)^{n+1}}
=
s^{-1}\frac{(r/s)^n}{(1+r/s)^{n+1}}
\tag{54}
\]

is unimodal and has total \(r\)-variation \(C_n/s\).  The factor
\(E_\sharp(r+s)\) is positive, bounded, and monotone, with total
variation at most \(d\).  The product rule for bounded variation
therefore gives

\[
\operatorname{Var}_r\Pi_n^\sharp(r,s)
\lesssim_n s^{-1},
\tag{55}
\]

which is (22).

Finally,

\[
\begin{aligned}
\frac{
\int_0^{q\tau}\Pi_n^\sharp(\tau-s,s)\,ds
}{
\int_0^\tau\Pi_n^\sharp(\tau-s,s)\,ds
}
&=
\frac{n+1}{\tau^{n+1}}
\int_0^{q\tau}(\tau-s)^n\,ds\\
&=
1-(1-q)^{n+1}.
\end{aligned}
\tag{56}
\]

This proves (23).

### Proposition 7: signed heat-spectrum realisation of the core

Equations (24)--(25) hold.

#### Proof

Expand \(r^n=((r+s)-s)^n\):

\[
\frac{r^n}{(r+s)^{n+1}}
=
\sum_{k=0}^n
\binom nk
\frac{(-s)^k}{(r+s)^{k+1}}.
\tag{57}
\]

For each \(k\),

\[
\frac1{(r+s)^{k+1}}
=
\frac1{k!}
\int_0^\infty
\lambda^k e^{-(r+s)\lambda}\,d\lambda.
\tag{58}
\]

Substitute (58) into (57) and collect the polynomial (25).  This proves
(24).  Setting \(r=0\) shows directly that the signed spectral density
has total zero for \(n\ge1\), matching the transport cancellation.

### Scope of the survivor

The kernel is positive on every diagonal and can put an arbitrarily
large fraction of its work in the earlier interval shared by nested
detectors.  Its heat-age variation costs exactly the divergent
\(M_\sharp Y_\sharp^2=s^{-1}\) budget.  The leading constant-energy core
has an exact signed heat-spectrum representation.

It is not a spatial velocity, does not impose
\(F=\mathbb P((U\cdot\nabla)v)\), and does not realise the coupled
pressure or one Navier--Stokes trajectory.

## 6. Exact frontier

### Robust conditional findings, subject to external review

1. The moving heat field evolves only by filtered nonlinearity; viscosity
   cancels exactly.
2. Half of the full entrance energy is the diagonal Gaussian flux (5).
3. The flux vanishes at zero heat age and is an accumulated signed heat
   band.
4. Nested terminal detectors obey the exact recycling identity (9).
5. Disjoint positive Gaussian bands have the \(\ell^1\) orthogonality
   budget (12).
6. That budget is exactly \(MY^2\), already forced to diverge by q4.
7. The coherent positive kernel satisfies the endpoint, diagonal,
   recycling, magnitude, band-variation, and power--log constraints.
8. Its leading constant-energy heat-age shape has an exact signed
   Laguerre spectral representation, while the full scalar kernel can
   concentrate arbitrarily much work in shared early history.

### Closed shortcut

Gaussian heat bands are orthogonal enough to prevent unrestricted
double-counting, but only in the amplitude-weighted dissipation budget
\(\int MY^2\).  That budget is necessarily infinite in the surviving q4
branch.  Positivity of the total diagonal work, endpoint cancellation,
and positive heat-band multipliers therefore do not alone create a finite
charge.

### Things still to prove

1. Use the exact quadratic relation
   \(F=\mathbb P((U\cdot\nabla)v)\), rather than its
   \(\dot H^{-1}\) norm, to exclude the coherent Laguerre reuse pattern.
2. Replace the \(MY^2\) right side of (12) by a finite same-trajectory
   budget through phase, genealogy, pressure, or spatial capacity.
3. Prove that actual q4 recycling bands have a fixed fresh component
   charged to unweighted dissipation.
4. Make the strong-drift contribution negligible at the moving Gaussian
   clock and isolate a self-interaction sign law.
5. Combine the Hausdorff-one-null initial energy measure with the
   moving-heat evolution.
6. Treat slower clocks, divergent normalised energy, and the other Clay
   alternatives separately.

### Conjecture: no coherent nonlinear Gaussian reuse

No one same-trajectory q4 entrance can have its actual flux

\[
\Pi_r(s)
=
-\left\langle
\mathbb P((U\cdot\nabla)v)(s),
S(2r)v(s)
\right\rangle
\tag{59}
\]

asymptotically realise a coherent family of the form (19) across every
record block while retaining finite unweighted dissipation.

The conjecture is not proved.  The scalar kernel does not realise the
quadratic Navier--Stokes relation.  No Clay alternative is proved.

## Downstream disposition

The subsequent
[radial triad-spectrum reduction](type-ii-radial-triad-spectrum.md)
adds the positive heat-energy constraint
\(\Pi=(\partial_s-\partial_r)\mathcal E\).  It excludes the Laguerre
kernel above as a kinetic-energy spectrum, replaces it by a completely
monotone moving-shell survivor with the same q4 budgets and stronger
early reuse, and exhibits exact adjacent-shell quadratic triads with the
survivor's limiting heat profile.  The live gate is now temporal
compatibility of those two structures on one NSE trajectory.
