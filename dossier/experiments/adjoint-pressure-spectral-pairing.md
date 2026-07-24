# Frequency-localised primal--adjoint pairing telescopes but is blind to adjoint pressure

- **Experiment:** EXP-ADJOINT-PRESSURE-SPECTRAL-PAIRING-001
- **Route:** ROUTE-R3B
- **Status:** adversarially recomputed exact pairing identity and
  same-trajectory periodic counterexamples, valid after precision repairs
- **Review:** [valid after six precision
  repairs](../review-ledger.md)
- **Domains:** identity on \(\mathbb R^3\) or \(\mathbb T^3\);
  counterexample on \(\mathbb T^3\)
- **Clay status:** unsolved
- **Inputs:** adversarially recomputed
  [adjoint-pressure history](adjoint-pressure-history.md),
  [skew-compression obstruction](adjoint-pressure-skew-compression.md),
  and [parabolic tail-to-flux theorem](adjoint-pressure-parabolic-flux.md)

The reviewed coefficient-energy theorem leaves a positive signed
high-pass flux branch.  A natural next proposal is to combine it with
the exactly conserved primal--adjoint pairing.  Frequency-localising
that pairing appears to offer precisely the missing shell telescope.

The telescope is real, but it is pressure-blind.

Let \(b\) be a reversed smooth Navier--Stokes coefficient and \(a\) its
forward solenoidal Oseen adjoint:

\[
\partial_\tau b+\nu\Delta b-b\cdot\nabla b+\nabla p_b=0,
\tag{1}
\]

\[
\partial_\tau a-\nu\Delta a-b\cdot\nabla a+\nabla\pi_a=0.
\tag{2}
\]

Pressures are defined up to functions of time.  For any fixed orthogonal
Fourier **frequency** projector \(P\) acting componentwise on vector
fields and therefore preserving solenoidality, put

\[
\mathcal C_P(\tau)
:=
\langle Pa(\tau),Pb(\tau)\rangle.
\tag{3}
\]

Then

\[
\boxed{
\frac d{d\tau}\mathcal C_P
=
-
\left\langle
(I-P)a,\,
b\cdot\nabla Pb
\right\rangle
+
\left\langle
Pa,\,
b\cdot\nabla(I-P)b
\right\rangle.
}
\tag{4}
\]

The two viscous terms cancel exactly.  Both pressure contributions pair
to zero against the divergence-free projected fields.  The projector
need not annihilate either pressure gradient.  Only a signed transport
commutator crosses the projector.  Nested versions of
\(\mathcal C_P\) telescope perfectly across frequency shells, but this
bare telescope contains no term that can charge
\(\|\nabla\pi_a\|_{L^1}\).

This is not merely a missing estimate.  There is an exact
same-trajectory example.  For \(N\in\mathbb N\), on
\(\mathbb T^3\), let

\[
U_N(x,y,z)
=
\left(
-\sin(Ny),\,
\cos(Nx),\,
-\sin(Nx)+\cos(Ny)
\right).
\tag{5}
\]

It satisfies

\[
\nabla\cdot U_N=0,
\qquad
\nabla\times U_N=NU_N,
\qquad
\Delta U_N=-N^2U_N,
\tag{6}
\]

and

\[
(U_N\cdot\nabla)U_N
=
\nabla w_N,
\qquad
w_N:=\frac{|U_N|^2}{2}
=
1-\sin(Nx)\cos(Ny).
\tag{7}
\]

For nonzero constants \(A,B\), define

\[
b(\tau)
=
Ae^{\nu N^2\tau}U_N,
\qquad
a(\tau)
=
Be^{-\nu N^2\tau}U_N.
\tag{8}
\]

Equations (1)--(2) hold exactly with

\[
p_b(\tau)
=
A^2e^{2\nu N^2\tau}w_N,
\qquad
\boxed{
\pi_a(\tau)=ABw_N.
}
\tag{9}
\]

Thus

\[
\langle a(\tau),b(\tau)\rangle
=
AB\|U_N\|_2^2
\tag{10}
\]

is constant, while the adjoint pressure gradient is nonzero and
time-independent.  On the standard torus \([0,2\pi]^3\),

\[
\boxed{
\int_0^T
\|\nabla\pi_a(\tau)\|_{L^1(\mathbb T^3)}\,d\tau
\ge
32\pi|AB|NT
>0.
}
\tag{11}
\]

The separation is even spectral.  The solenoidal fields \(a,b\) occupy
only Fourier radius \(N\), whereas the nonconstant pressure gradient
occupies radius \(\sqrt2N\).  Hence, for

\[
N<K<\sqrt2N,
\tag{12}
\]

\[
\boxed{
P_{>K}a=P_{>K}b=0,
\qquad
P_{>K}\nabla\pi_a=\nabla\pi_a\ne0.
}
\tag{13}
\]

The high-pass primal--adjoint pairing and its shell flux vanish, while
the adjoint-pressure history is strictly positive above the same
cutoff.

There is also an exact **high--high-to-fixed-low** version.  For
\(n\in\mathbb N\), \(n\ge1\), let

\[
k_n=(n,-n-1,0),
\qquad
\ell_n=(n+1,-n,0).
\tag{13a}
\]

Then

\[
|k_n|=|\ell_n|
=
R_n
:=
\sqrt{2n^2+2n+1}
\longrightarrow\infty,
\qquad
\ell_n-k_n=(1,1,0).
\tag{13b}
\]

Two positive-helicity modes at \(k_n,\ell_n\) sum to a Beltrami
eigenfield \(W_n\) at radius \(R_n\).  Its pressure potential contains
the fixed low mode

\[
\boxed{
\left(
1-\frac1{2R_n^2}
\right)
\cos(x+y).
}
\tag{13c}
\]

For every cutoff

\[
\sqrt2<K<R_n,
\tag{13d}
\]

the low-pass solenoidal pairing is zero, while the low-pass adjoint
pressure is nonzero and its coefficient tends to one.  Thus the
pressure-blindness persists in the exact high--high-to-low geometry of
the reviewed terminal-return branch; it is not an artefact of placing
the pressure above the velocity frequency.

Therefore adjoining this bare \(L^2\) spectral-pairing telescope to the
reviewed coefficient-energy balance supplies no pressure term and hence
does not by itself turn the reviewed pressure cost into a fresh event
charge.  The examples do not exclude a genuinely mixed functional.  A
successful extension must add a pressure-sensitive coupling: for example
a non-solenoidal or \(L^1\)-polar dual, a spatial pressure flux, or
another term that does not share the orthogonal pressure cancellation in
(4).

## 1. Exact localised pairing balance

Let \(P=m(D)I_3\) be a fixed orthogonal componentwise Fourier frequency
projector, with scalar symbol \(m\) taking values in \(\{0,1\}\), which:

1. commutes with spatial derivatives and \(\Delta\);
2. maps divergence-free vector fields to divergence-free vector fields;
3. is self-adjoint on \(L^2\).

Sharp high-pass, low-pass, and annular projectors all qualify.  Assume
the fields are smooth on a closed time interval and are either periodic
or decay sufficiently fast on \(\mathbb R^3\).

This \(P\) is not the Leray projector onto the solenoidal range.  It may
preserve a nonzero projected pressure gradient; its componentwise scalar
symbol merely ensures that it preserves divergence-free vector fields.

Equations (1)--(2) give

\[
\begin{aligned}
\frac d{d\tau}\mathcal C_P
&=
\nu\langle P\Delta a,Pb\rangle
-
\nu\langle Pa,P\Delta b\rangle
\\
&\quad
+
\langle P(b\cdot\nabla a),Pb\rangle
+
\langle Pa,P(b\cdot\nabla b)\rangle
\\
&\quad
-
\langle P\nabla\pi_a,Pb\rangle
-
\langle Pa,P\nabla p_b\rangle.
\end{aligned}
\tag{14}
\]

Self-adjointness and commutation with \(\Delta\) give

\[
\nu\langle P\Delta a,Pb\rangle
-
\nu\langle Pa,P\Delta b\rangle
=0.
\tag{15}
\]

Since \(Pa\) and \(Pb\) are divergence free,

\[
\langle P\nabla\pi_a,Pb\rangle
=
\langle\nabla\pi_a,Pb\rangle
=0,
\tag{16}
\]

\[
\langle Pa,P\nabla p_b\rangle
=
\langle Pa,\nabla p_b\rangle
=0.
\tag{17}
\]

Thus the two scalar pressure contributions vanish by divergence-free
orthogonality.  Neither identity asserts
\(P\nabla\pi_a=0\) or \(P\nabla p_b=0\); equation (13) below gives the
opposite behaviour explicitly.

Write

\[
a=Pa+(I-P)a,
\qquad
b=Pb+(I-P)b.
\tag{18}
\]

Self-adjointness removes \(P\) from the transport pairings, and
\(\nabla\cdot b=0\) gives

\[
\langle b\cdot\nabla a,Pb\rangle
=
-\langle a,b\cdot\nabla Pb\rangle.
\tag{19}
\]

The \(Pa\)--\(Pb\) terms cancel between the two transport pairings,
leaving exactly (4).

For \(P=I\), the right side vanishes and one recovers the global
conserved pairing.  For a proper spectral projector, (4) is a genuine
signed cross-frequency commutator.

## 2. The frequency telescope is exact

Let \(P_0,\ldots,P_m\) be nested orthogonal radial projectors and set

\[
\mathcal C_n(\tau)
:=
\langle P_na(\tau),P_nb(\tau)\rangle.
\tag{20}
\]

At every time,

\[
\boxed{
\sum_{n=0}^{m-1}
\left(
\mathcal C_{n+1}-\mathcal C_n
\right)
=
\mathcal C_m-\mathcal C_0.
}
\tag{21}
\]

The same holds after differentiating and using (4).  Thus there is no
loss of summability index analogous to the squared-versus-linear
skew-compression problem.

But equations (16)--(17) hold separately at every \(n\).  The exact
telescope contains no pressure contribution because each projected
pressure gradient pairs to zero against the corresponding
divergence-free field.  No inequality of the form

\[
\int_0^T\|\nabla\pi_a\|_1\,d\tau
\lesssim
\sum_n
\left|
\Delta_\tau
(\mathcal C_{n+1}-\mathcal C_n)
\right|
\tag{22}
\]

where
\(\Delta_\tau F:=F(T)-F(0)\), can hold under these structural
hypotheses alone.

## 3. Exact Beltrami primal--adjoint solution

The identities (6)--(7) follow from direct differentiation and the
Beltrami vector identity

\[
(U\cdot\nabla)U
=
\nabla\frac{|U|^2}{2}
-
U\times(\nabla\times U).
\tag{23}
\]

For (8),

\[
\partial_\tau b+\nu\Delta b=0,
\tag{24}
\]

\[
\partial_\tau a-\nu\Delta a=0,
\tag{25}
\]

and

\[
b\cdot\nabla b
=
A^2e^{2\nu N^2\tau}\nabla w_N,
\tag{26}
\]

\[
b\cdot\nabla a
=
AB\nabla w_N.
\tag{27}
\]

Equations (9) therefore solve (1)--(2).

The coefficient is the time reversal of the exact unforced physical
Navier--Stokes solution

\[
u(t)=Ae^{-\nu N^2t}U_N.
\tag{28}
\]

With the convention
\(\partial_tu-\nu\Delta u+u\cdot\nabla u+\nabla p_u=0\), its physical
pressure and reversed pressure are

\[
p_u(t)=-A^2e^{-2\nu N^2t}w_N,
\qquad
p_b(\tau)=-p_u(-\tau).
\tag{28a}
\]

Thus the separation is not an arbitrary Oseen drift construction.
It uses one actual NSE trajectory and its exact adjoint.

To prove (11), retain only the first component:

\[
\partial_xw_N
=
-N\cos(Nx)\cos(Ny).
\tag{29}
\]

For integer \(N\),

\[
\int_0^{2\pi}|\cos(Nx)|\,dx=4.
\tag{30}
\]

Consequently

\[
\begin{aligned}
\|\nabla w_N\|_{L^1(\mathbb T^3)}
&\ge
\|\partial_xw_N\|_1
\\
&=
N\cdot4\cdot4\cdot2\pi
=
32\pi N,
\end{aligned}
\tag{31}
\]

which gives (11).

Finally, the modes of \(U_N\) are

\[
(\pm N,0,0),
\qquad
(0,\pm N,0),
\tag{32}
\]

while the nonconstant modes of \(w_N\) are

\[
(\pm N,\pm N,0).
\tag{33}
\]

This proves (13).

## 4. Exact high--high-to-fixed-low separation

For a nonzero integer wavevector

\[
q=(q_1,q_2,0),
\qquad
|q|=R,
\tag{33a}
\]

define

\[
H_q(x)
:=
\left(
-\frac{q_2}{R}\sin(q\cdot x),\,
\frac{q_1}{R}\sin(q\cdot x),\,
\cos(q\cdot x)
\right).
\tag{33b}
\]

Direct differentiation gives

\[
\nabla\cdot H_q=0,
\qquad
\nabla\times H_q=RH_q,
\qquad
|H_q|=1.
\tag{33c}
\]

Use the equal-radius vectors in (13a)--(13b) and put

\[
W_n:=H_{k_n}+H_{\ell_n}.
\tag{33d}
\]

Then

\[
\nabla\times W_n=R_nW_n,
\qquad
\Delta W_n=-R_n^2W_n.
\tag{33e}
\]

Writing

\[
\alpha_n:=k_n\cdot x,
\qquad
\beta_n:=\ell_n\cdot x,
\tag{33f}
\]

one computes

\[
H_{k_n}\cdot H_{\ell_n}
=
\frac{k_n\cdot\ell_n}{R_n^2}
\sin\alpha_n\sin\beta_n
+
\cos\alpha_n\cos\beta_n.
\tag{33g}
\]

Since

\[
k_n\cdot\ell_n
=
2n(n+1)
=
R_n^2-1,
\tag{33h}
\]

the pressure potential is

\[
\boxed{
\begin{aligned}
\widetilde w_n
:=
\frac{|W_n|^2}{2}
&=
1
+
\left(
1-\frac1{2R_n^2}
\right)
\cos(\alpha_n-\beta_n)
\\
&\quad
+
\frac1{2R_n^2}
\cos(\alpha_n+\beta_n).
\end{aligned}
}
\tag{33i}
\]

Now

\[
\alpha_n-\beta_n=-(x+y),
\tag{33j}
\]

whereas

\[
\alpha_n+\beta_n=(2n+1)(x-y).
\tag{33k}
\]

Thus the first nonconstant term in (33i) has fixed Fourier radius
\(\sqrt2\) and coefficient

\[
c_n
:=
1-\frac1{2R_n^2}
\longrightarrow1,
\tag{33l}
\]

while the solenoidal field lies entirely at radius \(R_n\).

As before,

\[
\widetilde b_n(\tau)
=
Ae^{\nu R_n^2\tau}W_n,
\qquad
\widetilde a_n(\tau)
=
Be^{-\nu R_n^2\tau}W_n
\tag{33m}
\]

solve the exact reversed primal and forward adjoint equations with

\[
\widetilde\pi_n=AB\widetilde w_n.
\tag{33n}
\]

Let \(P_{\le K}\) be the sharp radial low-pass projector with
\(\sqrt2<K<R_n\).  The high pressure mode in (33k) also lies above
\(R_n\), since its radius is
\(\sqrt2(2n+1)>R_n\), so

\[
\boxed{
P_{\le K}\widetilde a_n
=
P_{\le K}\widetilde b_n
=0,
}
\tag{33o}
\]

but

\[
\boxed{
P_{\le K}\nabla\widetilde\pi_n
=
ABc_n\nabla\cos(x+y)
\ne0.
}
\tag{33p}
\]

Using only its \(x\)-component gives the uniform history floor

\[
\boxed{
\int_0^T
\|P_{\le K}\nabla\widetilde\pi_n\|_1\,d\tau
\ge
16\pi^2|AB|c_nT.
}
\tag{33q}
\]

The right side tends to
\(16\pi^2|AB|T\) while \(R_n\to\infty\).  This is an exact
same-trajectory high--high-to-fixed-low pressure return with zero
low-frequency primal--adjoint pairing.

For fixed \(A\ne0\) and every fixed \(T>0\), however, this family has no
coefficient-energy or coefficient-dissipation bound uniform in \(n\):
\[
\sup_{0\le\tau\le T}\|\widetilde b_n(\tau)\|_2^2
+\nu\int_0^T\|\nabla\widetilde b_n(\tau)\|_2^2\,d\tau
\longrightarrow\infty.
\tag{33r}
\]
It therefore does not contradict the reviewed terminal-return toll or
its finite-energy physical genealogy.

## 5. Relation to the parabolic tail-to-flux theorem

The reviewed
[parabolic tail-to-flux theorem](adjoint-pressure-parabolic-flux.md)
concerns the coefficient's own high-pass kinetic-energy identity:

\[
\Phi_K
=
\frac12\Delta\|Q_{>K}v\|_2^2
+
\nu D^\sharp_{>K}.
\tag{34}
\]

Its \(\Phi_K\) is a genuine nonlinear energy input into the coefficient
tail.  The present \(\mathcal C_P\) instead pairs the coefficient with
the Oseen adjoint.  Equation (4) shows that merely adjoining these two
bare \(L^2\) identities introduces no adjoint-pressure term: Hodge
orthogonality removes its scalar pairing before any frequency telescope
is taken.

The Beltrami examples are consistent with the earlier theorem.  Their
coefficient energy remains at one input radius, so any coefficient-tail
payment there lies in a comparable annulus.  What fails is only the
proposed implication from adjoint-pressure history---including an exact
high--high-to-fixed-low return---to a spectral primal--adjoint flux.

## 6. Exact consequence for ROUTE-R3B

This closes one tempting candidate for the missing event-index
functional:

> Frequency-localise the conserved primal--adjoint \(L^2\) pairing and
> sum its signed shell fluxes to charge each adjoint-pressure event.

The shell fluxes do telescope, but at every frequency the pressure term
pairs to zero against the divergence-free projected coefficient or
adjoint.  The projected pressure gradient itself may be nonzero.  Exact
same-trajectory periodic solutions have positive pressure history where
the localised pairing is identically zero, including a
high--high-to-fixed-low return whose low pressure coefficient tends to
one as the input frequency diverges.

The example does **not**:

- live on \(\mathbb R^3\) with finite total kinetic energy;
- realise the reviewed Besov-event genealogy or coefficient-tail floor;
- construct an infinite cascade or singularity;
- disprove an estimate using spatial decay, event localisation, or the
  full pressure-polar \(L^1\) structure, including a genuinely mixed
  pressure-sensitive functional; or
- prove regularity, breakdown, or any Clay alternative A--D.

The surviving target is narrower.  It must combine the coefficient
annulus/inherited-energy/signed-flux trichotomy either with a
pressure-sensitive functional or with a theorem that bypasses the
pressure telescope.  Candidates must use at least one of:

1. a pressure-polar \(L^1\) functional and a new event-index
   cancellation law;
2. the spatial bilinear conservation law, with quantitative control of
   its pressure boundary flux;
3. a non-solenoidal dual corrected by an exactly controlled divergence
   defect; or
4. a direct ancestry/locality theorem which bypasses the adjoint
   pressure telescope altogether.

The subsequent adversarially recomputed
[spatial cutoff-flux audit](adjoint-pressure-spatial-pairing.md) closes
the bare version of item 2: for reciprocal amplitudes of an exact
periodic Beltrami NSE field, pressure cancels transport in the local
current, and every gauge-invariant cutoff flux vanishes despite positive
adjoint-pressure history.  A viable spatial functional must separate
the pressure component or add cancellation control.

The subsequent adversarially recomputed
[terminal signed-flux ancestry theorem](adjoint-pressure-inherited-ancestry.md)
does realise item 4 far enough to force positive cumulative nonlinear
input on a terminal interval across some
\(K_j/\Lambda_j\to1\).  It does not make those intervals disjoint.
Thus a pressure-sensitive or other telescoping functional is now
needed for event-index freshness of an already forced flux, rather
than to prove that flux exists.

## 7. Executable certificate

The finite-dimensional pairing identity, pressure blindness, exact
shell telescope, Beltrami potentials, reciprocal heat amplitudes,
pressure spectral gap, fixed-low return, and \(L^1\)-history lower
bounds are checked by

```bash
make adjoint-pressure-spectral-pairing
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_spectral_pairing -v
```
