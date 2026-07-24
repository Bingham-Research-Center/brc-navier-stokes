# Annular localisation removes global energy but stops at \(L^{5/2}\)

- **Experiment:** EXP-ADJOINT-PRESSURE-ANNULAR-COST-001
- **Route:** ROUTE-R3B
- **Status:** conditional analytic localisation criterion
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** [adjoint-pressure history](adjoint-pressure-history.md),
  [feedback localisation](adjoint-pressure-feedback-tail.md), and the
  established [local-energy restart](../records/claims.json)
- **External review:** pending

The fixed-member CLMS upper bound for the adjoint pressure uses the
coefficient's global \(L^2\) norm.  That norm grows like
\(\rho_n^{-1/2}\) on the physical outer-profile genealogy, so it does
not survive the genealogy limit.

The global norm is not the real obstruction.  An annular coefficient
decomposition, an exterior Bogovskii correction of the adjoint, and
centre-uniform Navier--Stokes local energy give

\[
\boxed{
\begin{aligned}
\int_0^T\|\nabla\pi^*(\tau)\|_1\,d\tau
\le{}& C_{\rm in}\\
&+
C\sum_{k\ge0}\mathcal A_k(T)
\left[
\left(R_k+\frac{\nu T}{R_k}\right)^{1/2}
+M\left(\frac{T}{R_k}\right)^{1/2}
\right],
\end{aligned}
}
\tag{1}
\]

where \(R_k=L^kR_0\), \(L\ge16\), and

\[
\mathcal A_k(T)
:=
\left(
\int_0^T
\|a(\tau)\|_{L^2(|x|>2R_k)}^2\,d\tau
\right)^{1/2}.
\tag{2}
\]

No global kinetic-energy or global coefficient-dissipation norm occurs
in (1).  Thus a uniform finite-secondary-index tail

\[
\sum_{k\ge0}R_k^{1/2}\mathcal A_k(T)<\infty
\tag{3}
\]

would give the desired finite genealogy-level cost.

The already proved full-feedback tail is exactly
\(\mathcal A_k(T)\lesssim R_k^{-1/2}\), up to faster terms.  It supplies
only

\[
\sup_k R_k^{1/2}\mathcal A_k(T)<\infty,
\tag{4}
\]

so every dyadic annulus is still allowed to contribute order one to
(1).  The present bounds are therefore one full sequence-space index
short of a pressure budget.

There is an equivalent one-trajectory threshold.  A uniform
spacetime \(L^p\) bound for the coefficient gradient, together with
(4), sums (1) for every \(2<p<3\).  Under physical parabolic rescaling,
however,

\[
\|\nabla V_n\|_{L^p_{s,x}}^p
=
\nu_{\rm phys}^{\,1-p}\rho_n^{\,2p-5}
\|\nabla v\|_{L^p_{t,x}(\text{physical window})}^p.
\tag{5}
\]

The exact scale-invariant threshold is \(p=5/2\).  The available
Barker gain is \(p=2+\delta_B<5/2\), so its prefactor in (5) diverges
and absolute continuity supplies no compensating rate.  A strong
\(L^{5/2}_{t,x}\) input would close this annular budget, but that is
itself a critical gradient regularity-strength theorem.

This result removes a false obstruction and identifies the genuine
one.  It does not prove that the pressure cost is infinite, construct a
Navier--Stokes survivor saturating every shell, sum the event packets,
exclude the conditional ancient profile, or prove any Clay alternative.

## 1. The dual pressure factorisation

Let \(b\) be a smooth finite-energy reversed Navier--Stokes coefficient
on \([0,T]\):

\[
\partial_\tau b+\nu\Delta b-\mathbb P(b\cdot\nabla b)=0,
\qquad
\nabla\cdot b=0,
\tag{6}
\]

\[
\sup_{0\le\tau\le T}
\|b(\tau)\|_{L^{3,\infty}}\le M.
\tag{7}
\]

Let the solenoidal Oseen adjoint solve

\[
\partial_\tau a-\nu\Delta a-b\cdot\nabla a+\nabla\pi^*=0,
\qquad
\nabla\cdot a=0,
\qquad
a(0)=\psi.
\tag{8}
\]

Its energy identity gives

\[
\sup_{0\le\tau\le T}\|a(\tau)\|_2\le\|\psi\|_2.
\tag{9}
\]

Taking the divergence of (8) and using both divergence constraints gives

\[
\Delta\pi^*
=
\partial_kb_i\,\partial_i a_k
=
\partial_i(a_k\partial_kb_i).
\tag{10}
\]

For a divergence-free vector field \(z\), define

\[
\mathcal T(z,c)
:=
\nabla\Delta^{-1}\operatorname{div}
\bigl((z\cdot\nabla)c\bigr).
\tag{11}
\]

For every component \(c_i\), \(z\) is divergence free and
\(\nabla c_i\) is curl free.  CLMS div--curl and the
\(\mathcal H^1\to L^1\) Riesz-matrix bound give

\[
\boxed{
\|\mathcal T(z,c)\|_1
\le C_{\rm dH}\|z\|_2\|\nabla c\|_2.
}
\tag{12}
\]

Equation (10) says

\[
\nabla\pi^*=\mathcal T(a,b).
\tag{13}
\]

## 2. Exterior solenoidalisation

Choose a radial cutoff \(\zeta_R\) with

\[
\zeta_R=0\quad\text{on }B_{2R},
\qquad
\zeta_R=1\quad\text{outside }B_{4R},
\qquad
|\nabla\zeta_R|\le CR^{-1}.
\tag{14}
\]

Since \(a\) is divergence free,

\[
f_R:=\nabla\zeta_R\cdot a
\tag{15}
\]

is supported in \(B_{4R}\setminus B_{2R}\) and has zero integral.
The scale-invariant Bogovskii operator on this annulus produces \(v_R\)
with

\[
\nabla\cdot v_R=f_R,
\qquad
\|v_R\|_2
\le C\|a\|_{L^2(B_{4R}\setminus B_{2R})}.
\tag{16}
\]

Hence

\[
\widetilde a_R:=\zeta_Ra-v_R
\tag{17}
\]

is divergence free,

\[
\widetilde a_R=a\quad\text{outside }B_{4R},
\tag{18}
\]

and

\[
\boxed{
\|\widetilde a_R\|_2
\le C\|a\|_{L^2(|x|>2R)}.
}
\tag{19}
\]

This is the device that lets the CLMS estimate see the adjoint tail
rather than its full \(L^2\) norm.

## 3. Annular coefficient decomposition

Fix \(L\ge16\) and

\[
R_k=L^kR_0.
\tag{20}
\]

Let \(\eta_R\) be radial, zero on \(B_{4R}\), one outside \(B_{8R}\),
and satisfy \(|\nabla\eta_R|\le CR^{-1}\).  Put

\[
c_{-1}:=(1-\eta_{R_0})b,
\qquad
c_k:=(\eta_{R_k}-\eta_{R_{k+1}})b
\quad(k\ge0).
\tag{21}
\]

The decomposition telescopes:

\[
b=c_{-1}+\sum_{k\ge0}c_k.
\tag{22}
\]

For \(k\ge0\), the support of \(\nabla c_k\) lies outside
\(B_{4R_k}\).  Thus (18) gives the exact identity

\[
\mathcal T(a,c_k)
=
\mathcal T(\widetilde a_{R_k},c_k).
\tag{23}
\]

If

\[
\mathcal C_k
\subset
B_{8R_{k+1}}\setminus B_{4R_k}
\tag{24}
\]

is a fixed enlargement of that support, then

\[
\|\nabla c_k\|_2
\le
C_L
\left(
\|\nabla b\|_{L^2(\mathcal C_k)}
+R_k^{-1}\|b\|_{L^2(\mathcal C_k)}
\right).
\tag{25}
\]

Equations (12), (19), (23), and Cauchy--Schwarz in time yield

\[
\boxed{
\begin{aligned}
\int_0^T\|\mathcal T(a,c_k)\|_1\,d\tau
\le C_L\mathcal A_k(T)
\bigg[
&\left(
\int_0^T
\|\nabla b\|_{L^2(\mathcal C_k)}^2\,d\tau
\right)^{1/2}\\
&+
R_k^{-1}
\left(
\int_0^T
\|b\|_{L^2(\mathcal C_k)}^2\,d\tau
\right)^{1/2}
\bigg].
\end{aligned}
}
\tag{26}
\]

For each fixed smooth finite-energy member, the omitted exterior
remainder after a finite telescoping sum tends to zero by the global
\(L^2\) CLMS estimate.  Thus summing (26) is legitimate in the extended
sense even when its right side is infinite.

## 4. Navier--Stokes local energy closes the coefficient side

Finite-volume Lorentz embedding gives, uniformly in time,

\[
\|b(\tau)\|_{L^2(\mathcal C_k)}
\le C_LMR_k^{1/2}.
\tag{27}
\]

Therefore

\[
R_k^{-1}
\left(
\int_0^T
\|b\|_{L^2(\mathcal C_k)}^2\,d\tau
\right)^{1/2}
\le
C_LM\left(\frac{T}{R_k}\right)^{1/2}.
\tag{28}
\]

For the gradient term, divide \([0,T]\) into reversed intervals of
length at most \(cR_k^2/\nu\).  On each interval, reversing once more
starts an ordinary forward Navier--Stokes solution at its exact back
edge.  The weak-\(L^3\) ceiling gives the required uniform local-\(L^2\)
datum, while finite energy gives vanishing local mass at spatial
infinity.  The recorded Barker--Prange restart estimate therefore gives
\(CR_k\) dissipation per interval.  Summation over the intervals gives

\[
\boxed{
\int_0^T
\|\nabla b\|_{L^2(\mathcal C_k)}^2\,d\tau
\le
C_{\rm LE}
\left(
R_k+\frac{\nu T}{R_k}
\right),
}
\tag{29}
\]

where \(C_{\rm LE}\) depends on \(M/\nu,\nu,L\), but not on the global
energy or the centre.

The inner coefficient \(c_{-1}\) is handled by (9), (12), and the same
local estimates:

\[
\boxed{
C_{\rm in}
\le
C\|\psi\|_2
\left[
\sqrt{T}
\left(
R_0+\frac{\nu T}{R_0}
\right)^{1/2}
+MT R_0^{-1/2}
\right].
}
\tag{30}
\]

Substituting (28)--(30) into (26) proves (1).

For an admissible physical genealogy
\(\mathcal G=\{(u_n,H_n)\}\), let \(\mathcal A_{n,k}(T)\) be (2) for
the \(n\)-th adjoint.  Equation (1) gives the precise sufficient
condition

\[
\liminf_{\substack{n\to\infty\\H_n\ge T}}
\sum_{k\ge0}\mathcal A_{n,k}(T)
\left[
\left(R_k+\frac{\nu T}{R_k}\right)^{1/2}
+M\left(\frac{T}{R_k}\right)^{1/2}
\right]
<\infty
\tag{31}
\]

for
\(\mathfrak p^\mathcal G_{\psi,T}<\infty\).

## 5. The proved adjoint tail lands exactly at the endpoint

For the preferred band-limited Schwartz detector on a selected short
layer \(0<h\le1\), the recorded decomposition is

\[
a=\varphi+q+r.
\tag{32}
\]

The cube estimate for the direct response gives

\[
\int_0^h
\|q(\tau)\|_{L^2(|x|>R)}^2\,d\tau
\le
C\left(
h^3R^{-5}
+h^{3/2}R^{-13}
\right).
\tag{33}
\]

The feedback localisation gives

\[
\int_0^h
\|r(\tau)\|_{L^2(|x|>2R)}^2\,d\tau
\le
C\left(
h^{7/2}R^{-1}
+h^{5/2}R^{-15}
\right).
\tag{34}
\]

Together with the Schwartz tail of \(\varphi\), these imply

\[
\boxed{
\begin{aligned}
\mathcal A_k(h)
\le C_N\bigg[
&\sqrt h\,R_k^{-N}
+h^{3/2}R_k^{-5/2}
+h^{3/4}R_k^{-13/2}\\
&+h^{7/4}R_k^{-1/2}
+h^{5/4}R_k^{-15/2}
\bigg].
\end{aligned}
}
\tag{35}
\]

For \(R_k\ge\max\{2,\sqrt{\nu h}\}\), the leading weight in (1) is
\(R_k^{1/2}\).  The last slow term in (35) therefore gives

\[
R_k^{1/2}\mathcal A_k(h)
\le C h^{7/4}+o_{k\to\infty}(1),
\tag{36}
\]

with no decay in \(k\).  The current theorem proves neither that all
these shell actions are simultaneously realised nor that they cancel.
It proves that the recorded tail and local-energy estimates alone do
not sum them.

Any improvement

\[
\mathcal A_k(h)
\lesssim R_k^{-1/2-\varepsilon}
\qquad(\varepsilon>0)
\tag{37}
\]

would make (1) geometrically summable.  More generally, the exact
missing datum is the finite secondary index (3), not a global-energy
ceiling.

## 6. The \(L^{5/2}\) threshold

Suppose, additionally, that for some \(2<p<3\),

\[
G_p(T)
:=
\int_0^T\int_{\mathbb R^3}|\nabla b|^p\,dx\,d\tau
<\infty
\tag{38}
\]

and that

\[
\mathcal A_k(T)\le A_*R_k^{-1/2}.
\tag{39}
\]

Write \(G_{p,k}\) for (38) restricted to \(\mathcal C_k\).  Hölder on
the spacetime annulus gives

\[
\left(
\int_0^T
\|\nabla b\|_{L^2(\mathcal C_k)}^2\,d\tau
\right)^{1/2}
\le
C
G_{p,k}^{1/p}
T^{(p-2)/(2p)}
R_k^{3(p-2)/(2p)}.
\tag{40}
\]

Multiplication by (39) produces the radius power

\[
-\frac12+\frac{3(p-2)}{2p}
=
1-\frac3p
<0.
\tag{41}
\]

Hölder in shell index and finite overlap of the \(\mathcal C_k\) give

\[
\boxed{
\begin{aligned}
\sum_{k\ge0}
\mathcal A_k(T)
\left(
\int_0^T
\|\nabla b\|_{L^2(\mathcal C_k)}^2\,d\tau
\right)^{1/2}
\le{}&
C A_*T^{(p-2)/(2p)}G_p(T)^{1/p}\\
&\times
R_0^{1-3/p}
\left(
1-L^{(p-3)/(p-1)}
\right)^{-(p-1)/p}.
\end{aligned}
}
\tag{42}
\]

The cutoff contribution in (28) is already summable under (39).
Thus a genealogy-uniform \(G_p(T)\) closes (31).

For the physical outer scaling

\[
V_n(s,y)
=
\frac{\rho_n}{\nu_{\rm phys}}
v\left(
T^*+\frac{\rho_n^2}{\nu_{\rm phys}}s,
x^*+\rho_n y
\right),
\tag{43}
\]

direct change of variables gives (5).  Hence:

- if \(p>5/2\), the prefactor \(\rho_n^{2p-5}\) vanishes;
- if \(p=5/2\), the norm is scale invariant and strong absolute
  continuity on the shrinking physical window makes it vanish;
- if \(2<p<5/2\), the prefactor diverges and strong \(L^p\) membership
  alone gives no rate that offsets it.

The available exponent \(p=2+\delta_B\), with
\(\delta_B<1/2\), lies strictly in the last regime.  Reaching
\(p=5/2\) is exactly the critical gradient Serrin scale

\[
\frac2{5/2}+\frac3{5/2}=2.
\tag{44}
\]

Thus this natural route to a finite pressure budget asks for a genuinely
new critical theorem, not a routine use of the known higher-integrability
gain.

## 7. Endpoint norm sharpness before PDE coupling

The shell powers in (36) are simultaneously saturated by a static cell
ledger.  In an annulus of radius \(R\), take \(N\asymp R^3\) separated
unit cells, coefficient amplitude \(R^{-1}\), adjoint amplitude
\(R^{-2}\), and unit internal frequency.  Then

\[
\|b_R\|_{L^{3,\infty}}\asymp1,
\qquad
\|a_R\|_2\asymp R^{-1/2},
\qquad
\|\nabla b_R\|_2\asymp R^{1/2},
\tag{45}
\]

while

\[
\int|a_R||\nabla b_R|\,dx\asymp1.
\tag{46}
\]

Compact divergence-free cell templates can enforce the div--curl
geometry without changing these powers.  This is only a norm-scaling
stress test.  It is not claimed to solve either evolution equation, to
come from one Navier--Stokes trajectory, or to make the pressure
contributions have one sign.

## 8. Exact route consequence

This theorem closes:

1. the apparent obstruction caused solely by the
   \(\rho_n^{-1/2}\) global kinetic-energy factor;
2. a global-energy-free annular upper estimate for every smooth
   genealogy member;
3. the exact exterior-adjoint secondary index sufficient for a finite
   genealogy-level cost;
4. the fact that the proved \(R^{-1/2}\) feedback tail is precisely
   borderline; and
5. \(p=5/2\) as the exact physical one-trajectory integrability threshold
   for this localisation.

It does not prove:

1. the finite-secondary-index estimate (3);
2. any positive tail power beyond \(R^{-1/2}\);
3. a uniform \(L^{5/2}_{t,x}\) gradient bound;
4. divergence of the actual genealogy cost;
5. an event-index pressure sum;
6. exclusion of the coherent ancient profile;
7. regularity, breakdown, or any Clay alternative A--D.

The subsequent
[nonlinear-regeneration reduction](adjoint-pressure-nonlinear-regeneration.md)
shows that reciprocal-or-lower coefficient frequencies sum at this endpoint
and that remote inherited high frequencies vanish on the physical genealogy.
It therefore narrows the live question further:

> Prove a finite secondary index for the high-frequency nonlinear Duhamel
> regeneration action, or show that its non-summable shells force fresh
> signed flux/decrement events. A positive exterior-adjoint tail power or
> scale-critical \(L^{5/2}\)-type gain remains sufficient.

The local-energy, shell, tail, cell-cloud, and \(L^p\) scaling ledgers
are checked in
`lab/navier_lab/adjoint_pressure_annular_cost.py` and
`lab/tests/test_adjoint_pressure_annular_cost.py`.
