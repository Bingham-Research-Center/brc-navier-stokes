# An exact Beltrami spatial cutoff flux vanishes despite positive pressure history

- **Experiment:** EXP-ADJOINT-PRESSURE-SPATIAL-PAIRING-001
- **Route:** ROUTE-R3B
- **Status:** adversarially recomputed same-trajectory cancellation of
  every gauge-invariant cutoff flux for the previously recorded local
  conservation identity, valid after gauge repair
- **Review:** [valid after gauge and scope
  repairs](../review-ledger.md)
- **Domains:** identity on \(\mathbb R^3\) or \(\mathbb T^3\);
  counterexamples on \(\mathbb T^3\)
- **Clay status:** unsolved
- **Inputs:** adversarially recomputed
  [adjoint-pressure history](adjoint-pressure-history.md),
  [skew-compression obstruction](adjoint-pressure-skew-compression.md),
  [parabolic tail-to-flux theorem](adjoint-pressure-parabolic-flux.md),
  and
  [spectral primal--adjoint pairing audit](adjoint-pressure-spectral-pairing.md)

The earlier skew-compression audit already recorded the exact local
primal--adjoint conservation law, and the spectral audit showed that
Fourier localisation supplies no pressure term.  This note tests the
remaining proposal that the **spatial** total current might coerce the
pressure boundary flux.

For completeness, put

\[
q:=a\cdot b
\tag{1}
\]

for the reversed smooth Navier--Stokes coefficient

\[
\partial_\tau b+\nu\Delta b-b\cdot\nabla b+\nabla p_b=0,
\qquad
\nabla\cdot b=0,
\tag{2}
\]

and its forward solenoidal Oseen adjoint

\[
\partial_\tau a-\nu\Delta a-b\cdot\nabla a+\nabla\pi_a=0,
\qquad
\nabla\cdot a=0.
\tag{3}
\]

Then

\[
\boxed{
\partial_\tau q+\nabla\cdot\mathcal J=0,
}
\tag{4}
\]

where

\[
\boxed{
\mathcal J
=
\nu\sum_{i=1}^3
\left(
a_i\nabla b_i-b_i\nabla a_i
\right)
-q\,b
+\pi_a b
+p_ba.
}
\tag{5}
\]

Thus every fixed smooth spatial cutoff \(\eta\) obeys

\[
\boxed{
\frac d{d\tau}\int\eta\,a\cdot b
=
\int\nabla\eta\cdot\mathcal J.
}
\tag{6}
\]

Unlike the frequency-localised identity, the previously recorded
identity (5) visibly contains pressure.  But it contains pressure only
inside a signed total current.

For every periodic Beltrami eigenfield

\[
\nabla\cdot U=0,
\qquad
\nabla\times U=RU,
\qquad
\Delta U=-R^2U,
\tag{7}
\]

write

\[
w:=\frac{|U|^2}{2}.
\tag{8}
\]

For nonzero constants \(A,B\), set

\[
b(\tau)=Ae^{\nu R^2\tau}U,
\qquad
a(\tau)=Be^{-\nu R^2\tau}U.
\tag{9}
\]

These solve (2)--(3) with

\[
p_b=A^2e^{2\nu R^2\tau}w,
\qquad
\pi_a=ABw.
\tag{10}
\]

If \(w\) is nonconstant, the adjoint-pressure gradient is nonzero.  In
the pressure gauges displayed in (10), the current (5) vanishes
**pointwise**:

\[
\boxed{
\mathcal J\equiv0.
}
\tag{11}
\]

Other time-dependent gauges add a divergence-free linear combination of
\(a\) and \(b\) to the current.  Therefore, in **every** pressure gauge,

\[
\boxed{
\nabla\cdot\mathcal J=0,
\qquad
\int\nabla\eta\cdot\mathcal J=0
\quad\hbox{for every fixed smooth }\eta.
}
\tag{11a}
\]

Indeed, the viscous Wronskian vanishes, while

\[
-q\,b
=
-2A^2Be^{\nu R^2\tau}wU,
\tag{12}
\]

and

\[
\pi_ab+p_ba
=
2A^2Be^{\nu R^2\tau}wU.
\tag{13}
\]

Hence all spatially localised pairings are constant.  The
displayed-gauge current is identically zero, and the divergence and every
cutoff-gradient pairing of the current vanish in any gauge, while

\[
\int_0^T\|\nabla\pi_a(\tau)\|_1\,d\tau
=
|AB|T\|\nabla w\|_1
>0.
\tag{14}
\]

The high--high-to-fixed-low Beltrami family from the spectral audit has
the same displayed-gauge pointwise cancellation and gauge-invariant
cutoff-flux cancellation.  Its solenoidal input frequency tends to
infinity, while its adjoint pressure retains a fixed low mode with
coefficient tending to one.

Therefore the bare spatial conservation law does not convert pressure
history into an event-index charge.  A successful use of its pressure
boundary flux must prevent or quantify its cancellation against
transport, primal pressure, and the viscous Wronskian.  The result does
not exclude a pressure-polar functional, a signed boundary selection
with new transversality, a controlled divergence defect, or direct
same-trajectory ancestry.

## 1. Re-derivation of the recorded pointwise conservation law

Equations (2)--(3) are equivalent to

\[
\partial_\tau b
=
-\nu\Delta b+b\cdot\nabla b-\nabla p_b,
\tag{15}
\]

\[
\partial_\tau a
=
\nu\Delta a+b\cdot\nabla a-\nabla\pi_a.
\tag{16}
\]

Differentiate \(q=a\cdot b\):

\[
\begin{aligned}
\partial_\tau q
={}&
\nu\left(
\Delta a\cdot b-a\cdot\Delta b
\right)
+(b\cdot\nabla a)\cdot b
+a\cdot(b\cdot\nabla b)
\\
&-\nabla\pi_a\cdot b
-a\cdot\nabla p_b.
\end{aligned}
\tag{17}
\]

The viscous difference is a divergence:

\[
\Delta a\cdot b-a\cdot\Delta b
=
\nabla\cdot
\sum_{i=1}^3
\left(
b_i\nabla a_i-a_i\nabla b_i
\right).
\tag{18}
\]

The two transport terms combine because the same coefficient drives both
equations:

\[
(b\cdot\nabla a)\cdot b
+a\cdot(b\cdot\nabla b)
=
b\cdot\nabla(a\cdot b)
=
\nabla\cdot(qb).
\tag{19}
\]

Finally, solenoidality gives

\[
-\nabla\pi_a\cdot b
-a\cdot\nabla p_b
=
-\nabla\cdot(\pi_ab+p_ba).
\tag{20}
\]

Equations (17)--(20) are exactly (4)--(5), agreeing with equation (42)
of the
[skew-compression audit](adjoint-pressure-skew-compression.md).  This
identity is an input being audited for coercivity, not the new result of
the present note.

Pressures are defined up to functions of time.  Such gauge changes add
a linear combination of \(a\) and \(b\) to \(\mathcal J\), hence add a
divergence-free current.  Both (4) and the cutoff identity (6) are gauge
independent.

For a smooth periodic cutoff, or for
\(\eta\in C_c^\infty(\mathbb R^3)\), integration by parts in (4) proves
(6).  All statements here are classical; no endpoint test of a rough
suitable solution is used.

## 2. Spatial shells telescope but retain only the total current

Let \(\eta_0,\ldots,\eta_m\) be any fixed smooth cutoffs and put

\[
\mathcal C_n(\tau)
:=
\int\eta_n\,a\cdot b.
\tag{21}
\]

Their increments telescope algebraically:

\[
\boxed{
\sum_{n=0}^{m-1}
\left(
\mathcal C_{n+1}-\mathcal C_n
\right)
=
\mathcal C_m-\mathcal C_0.
}
\tag{22}
\]

After differentiation,

\[
\frac d{d\tau}
\left(
\mathcal C_{n+1}-\mathcal C_n
\right)
=
\int
\nabla(\eta_{n+1}-\eta_n)\cdot\mathcal J.
\tag{23}
\]

The right side sees only the total current (5).  It does not separately
control

\[
\int\nabla\eta\cdot\pi_ab,
\tag{24}
\]

let alone the unweighted polar cost

\[
\int_0^T\|\nabla\pi_a\|_1\,d\tau.
\tag{25}
\]

This distinction is structural.  The next section gives a solution for
which the pressure part of (5) is nonzero but cancels the transport part
pointwise.

## 3. Generic reciprocal Beltrami cancellation

The vector identity

\[
(U\cdot\nabla)U
=
\nabla\frac{|U|^2}{2}
-U\times(\nabla\times U)
\tag{26}
\]

and (7) give

\[
(U\cdot\nabla)U=\nabla w.
\tag{27}
\]

The reciprocal heat amplitudes in (9) obey

\[
\partial_\tau b+\nu\Delta b=0,
\qquad
\partial_\tau a-\nu\Delta a=0.
\tag{28}
\]

Also,

\[
b\cdot\nabla b
=
A^2e^{2\nu R^2\tau}\nabla w,
\qquad
b\cdot\nabla a
=
AB\nabla w.
\tag{29}
\]

This proves (10).  The pairing density is

\[
q=a\cdot b=AB|U|^2=2ABw,
\tag{30}
\]

and is independent of \(\tau\) at every point.

For the viscous part of (5),

\[
\sum_i
\left(
a_i\nabla b_i-b_i\nabla a_i
\right)
=
AB
\sum_i
\left(
U_i\nabla U_i-U_i\nabla U_i
\right)
=0.
\tag{31}
\]

Equations (12)--(13) prove that the remaining terms cancel.  Thus
(11)--(11a) are stronger than constancy of the global pairing: every
fixed spatial cutoff has zero flux in every gauge, and in the displayed
gauges the complete local current vanishes at every point.

The coefficient is the reversal of the physical Navier--Stokes
solution

\[
u(t)=Ae^{-\nu R^2t}U,
\qquad
p_u(t)=-A^2e^{-2\nu R^2t}w.
\tag{32}
\]

Hence this is one actual periodic NSE trajectory and its exact Oseen
adjoint, not an arbitrary prescribed drift.

## 4. One-radius and fixed-low pressure histories

For \(N\in\mathbb N\), take

\[
U_N
=
\left(
-\sin(Ny),\,
\cos(Nx),\,
-\sin(Nx)+\cos(Ny)
\right).
\tag{33}
\]

Then

\[
w_N
=
1-\sin(Nx)\cos(Ny),
\tag{34}
\]

and, on \([0,2\pi]^3\),

\[
\|\nabla w_N\|_1
\ge
32\pi N.
\tag{35}
\]

Therefore, in the displayed gauges, (11) and (14) give simultaneously

\[
\boxed{
\mathcal J_N\equiv0,
\qquad
\int_0^T\|\nabla\pi_{a,N}\|_1\,d\tau
\ge
32\pi|AB|NT.
}
\tag{36}
\]

For the stronger fixed-low family, let \(n\in\mathbb N\), \(n\ge1\),

\[
k_n=(n,-n-1,0),
\qquad
\ell_n=(n+1,-n,0),
\tag{37}
\]

\[
R_n=|k_n|=|\ell_n|
=
\sqrt{2n^2+2n+1},
\tag{38}
\]

and use the paired Beltrami field \(W_n\) from the
[spectral audit](adjoint-pressure-spectral-pairing.md).  Its pressure
potential is

\[
\widetilde w_n
=
1
+\left(
1-\frac1{2R_n^2}
\right)\cos(x+y)
+\frac1{2R_n^2}\cos((2n+1)(x-y)).
\tag{39}
\]

For every \(\sqrt2<K<R_n\),

\[
P_{\le K}\widetilde a_n
=
P_{\le K}\widetilde b_n
=0,
\tag{40}
\]

while

\[
P_{\le K}\nabla\widetilde\pi_n
=
AB
\left(
1-\frac1{2R_n^2}
\right)
\nabla\cos(x+y).
\tag{41}
\]

In the displayed gauges, the same reciprocal-amplitude calculation gives

\[
\boxed{
\mathcal J_n\equiv0,
}
\tag{42}
\]

but

\[
\boxed{
\int_0^T
\|P_{\le K}\nabla\widetilde\pi_n\|_1\,d\tau
\ge
16\pi^2|AB|
\left(
1-\frac1{2R_n^2}
\right)T.
}
\tag{43}
\]

The pressure floor tends to \(16\pi^2|AB|T\) as the input frequency
\(R_n\) diverges.

For fixed \(A\ne0\) and \(T>0\), this family has no energy or
viscosity-weighted dissipation bound uniform in \(n\):

\[
\sup_{0\le\tau\le T}\|\widetilde b_n(\tau)\|_2^2
+\nu
\int_0^T
\|\nabla\widetilde b_n(\tau)\|_2^2\,d\tau
\longrightarrow\infty.
\tag{44}
\]

Thus it does not contradict the reviewed finite-energy terminal-return
toll.

## 5. What is closed and what remains live

The following bare gauge-invariant proposal is closed:

> Spatially localise the conserved primal--adjoint pairing and telescope
> its signed cutoff-current increments to obtain a coercive
> adjoint-pressure event charge.

The local law is exact and pressure-visible, but its conserved current is
a signed sum.  On exact same-trajectory Beltrami solutions, in the
displayed gauges the adjoint and primal pressure fluxes cancel transport
pointwise and the viscous Wronskian vanishes.  In every pressure gauge,
the current divergence and every cutoff-gradient pairing vanish despite
positive adjoint-pressure history.

This result does **not**:

- rule out an estimate for the pressure component of (5) under an
  independent sign, transversality, or spatial localisation theorem;
- rule out the pressure-polar \(L^1\) functional from the reviewed
  adjoint history;
- rule out a mixed functional coupling pressure to the coefficient
  annulus/inherited-energy/signed-flux trichotomy;
- rule out a norm or other functional of a canonically gauge-fixed
  current;
- provide finite-energy data on \(\mathbb R^3\), a Besov-event
  genealogy, an infinite cascade, or a singularity; or
- prove regularity, breakdown, or any Clay alternative A--D.

The next target is no longer a bare conserved pairing.  It must either:

1. isolate the adjoint-pressure component with a sign or polar field and
   quantitatively control cancellation by the transport, primal-pressure,
   and viscous currents;
2. derive a pressure-boundary transversality law from the actual
   Besov-event genealogy;
3. introduce a controlled divergence defect whose source is summable
   across event index; or
4. bypass pressure pairing through a direct same-trajectory
   frequency/spatial ancestry theorem.

The subsequent adversarially recomputed
[terminal signed-flux ancestry theorem](adjoint-pressure-inherited-ancestry.md)
implements item 4 at the cumulative level.  Fixed-time \(H^1\),
last-hitting ancestry, and an event-adaptive sharp-annulus squeeze
force terminal positive nonlinear input across some
\(K_j/\Lambda_j\to1\).  The remaining gap is precisely event-index
freshness: the flux intervals may overlap and one cascade may pay many
boundaries.

## 6. Executable certificate

The reciprocal amplitudes, pointwise current coefficients, exact
pressure--transport cancellation, positive pressure history, and
nonuniform paired-family energy/dissipation budget are checked by

```bash
make adjoint-pressure-spatial-pairing
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_spatial_pairing -v
```
