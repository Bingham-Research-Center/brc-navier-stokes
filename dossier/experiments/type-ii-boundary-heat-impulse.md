# The q4 nonlinear entrance forces a critical boundary heat impulse

- **Experiment:** EXP-TYPE-II-BOUNDARY-HEAT-IMPULSE-001
- **Route:** ROUTE-R3C
- **Status:** complete conditional reduction; external review pending
- **Domain:** smooth finite-energy Navier--Stokes flow on \(\mathbb R^3\)
- **Clay status:** unsolved
- **Input:** [nonlinear defect entrance](type-ii-nonlinear-defect-entrance.md)

## Verdict

The weak-zero boundary of the reversed full-defect component can be removed
from its mild equation exactly.  Put

\[
U:=v+c=-u(T-\tau),
\qquad
M(\tau):=\|U(\tau)\|_{L^{3,\infty}},
\qquad
Y(\tau):=\|\nabla v(\tau)\|_2.
\tag{1}
\]

The entrance equation is

\[
\partial_\tau v-\nu\Delta v
+\mathbb P((U\cdot\nabla)v)=0,
\qquad
v(\tau)\rightharpoonup0
\quad(\tau\downarrow0).
\tag{2}
\]

For every \(\tau>0\), it has the exact zero-boundary Duhamel formula

\[
\boxed{
v(\tau)
=
-\int_0^\tau
e^{\nu(\tau-s)\Delta}
\mathbb P((U\cdot\nabla)v)(s)\,ds.
}
\tag{3}
\]

Thus the positive entrance energy does not come from a surviving linear
heat datum.  Pairing (3) with \(v(\tau)\), and preserving the pointwise
transport cancellation, gives

\[
\boxed{
\begin{aligned}
\|v(\tau)\|_2^2
&=
-\int_0^\tau
\left\langle
(U\cdot\nabla)v(s),
e^{\nu(\tau-s)\Delta}v(\tau)-v(s)
\right\rangle ds\\
&=
\int_0^\tau\int_{\mathbb R^3}
U_j(s)v_i(s)
\partial_j\!\left(
e^{\nu(\tau-s)\Delta}v_i(\tau)-v_i(s)
\right)dx\,ds.
\end{aligned}
}
\tag{4}
\]

This is the exact **boundary heat-deviation work**.  Its total is positive
and tends to the full defect \(d\), but its time density has no known sign.
The subtraction in (4) is essential: at \(s=\tau\) the heat deviation is
zero, whereas a triangle inequality discards that endpoint cancellation.

Let

\[
f(s):=M(s)Y(s),
\qquad
(I_\alpha f)(\tau)
:=
\int_0^\tau(\tau-s)^{\alpha-1}f(s)\,ds.
\tag{5}
\]

Lorentz heat smoothing gives

\[
\boxed{
\|v(\tau)\|_2
\lesssim
\nu^{-1/2}I_{1/2}f(\tau),
\qquad
\|v(\tau)\|_{L^{3,\infty}}
\lesssim
\nu^{-3/4}I_{1/4}f(\tau).
}
\tag{6}
\]

Since \(\|v(\tau)\|_2^2\to d>0\), every sufficiently small \(h\) obeys

\[
\boxed{
\int_0^h M(s)Y(s)\,ds
\gtrsim
\sqrt{\nu d}\,h^{1/2}.
}
\tag{7}
\]

Consequently

\[
\boxed{
\left(\int_0^hM^2\right)
\left(\int_0^hY^2\right)
\gtrsim
\nu d\,h.
}
\tag{8}
\]

More sharply, \(MY\) cannot belong near zero to
\(L^{2,q}_\tau\) for any finite \(q\).  A finite temporal secondary
index would force the left side of (7) to be \(o(h^{1/2})\).  Thus the
entrance forces a non-vanishing weak-\(L^2\) endpoint impulse.

At the exact q4 records,

\[
\boxed{
I_{1/4}(MY)(\tau_j)
\gtrsim
\nu^{3/4}m_j,
}
\tag{9}
\]

because the nonlinear entrance owns the record weak-\(L^3\) amplitude.

This does not close q4.  The power--log ledger

\[
\ell(s):=\log(e/s),
\qquad
M_\sharp(s):=s^{-2/11}\ell(s)^{-2/11},
\qquad
Y_\sharp(s):=s^{-9/22}\ell(s)^{1/11}
\tag{10}
\]

has

\[
\int_0^hM_\sharp^2
\asymp h^{7/11}\ell(h)^{-4/11},
\qquad
\int_0^hY_\sharp^2
\asymp h^{2/11}\ell(h)^{2/11},
\tag{11}
\]

and

\[
\int_0^hM_\sharp Y_\sharp^2\,ds=\infty.
\tag{12}
\]

It also satisfies (7)--(9) with room to spare.  On the canonical schedule
\(h_j=m_j^{-11/2}/j\), \(\ell(h_j)\asymp j\),

\[
M_\sharp(h_j)\asymp m_j,
\qquad
\int_0^{h_j}M_\sharp^2
\asymp\frac{m_j^{-7/2}}j,
\qquad
\int_0^{h_j}Y_\sharp^2
\asymp m_j^{-1}.
\tag{13}
\]

The ledger is not a velocity field or a Navier--Stokes trajectory.  It
shows that the exact mild formulation, both fractional impulse bounds,
the q4 clock, the individual dissipation floor, and the divergent
amplitude-weighted action remain scalar-compatible.

The live theorem is now precise:

> Prove that the positive heat-deviation work in (4) cannot be reused
> down an infinite same-trajectory q4 cascade, or prove a finite temporal
> secondary index for \(MY\).

No such theorem is established here.  No Clay alternative is proved.

## 1. Setting

The input theorem supplies

\[
v,c\in
L^\infty_\tau L^2_\sigma
\cap
L^2_\tau\dot H^1_\sigma
\tag{14}
\]

on a terminal interval, with (2) and

\[
\|v(\tau)\|_2^2
+2\nu\int_0^\tau Y(s)^2\,ds
=d.
\tag{15}
\]

The q4 tail also gives

\[
M\in L^2(0,\tau_0).
\tag{16}
\]

Hence

\[
f=MY\in L^1(0,\tau_0).
\tag{17}
\]

The fields are smooth for every positive time.  All endpoint statements
below concern only \(\tau=0\).

Let

\[
S(r):=e^{\nu r\Delta}.
\tag{18}
\]

The heat semigroup and the Leray projection commute and are self-adjoint
on solenoidal \(L^2\).

## 2. Exact zero-boundary mild formula

### Theorem 1: the linear boundary datum vanishes after heat propagation

For every fixed \(\tau>0\), (3) holds in \(L^2_\sigma\).

#### Proof

For \(0<\epsilon<\tau\), ordinary positive-time mild evolution gives

\[
v(\tau)
=
S(\tau-\epsilon)v(\epsilon)
-
\int_\epsilon^\tau
S(\tau-s)\mathbb P((U\cdot\nabla)v)(s)\,ds.
\tag{19}
\]

Lorentz Hölder gives

\[
\|(U\cdot\nabla)v\|_{L^{6/5,2}}
\lesssim
M Y.
\tag{20}
\]

The heat estimate

\[
\|S(r)g\|_2
\lesssim
(\nu r)^{-1/2}
\|g\|_{L^{6/5,2}}
\tag{21}
\]

and (17) show that the integral in (19) converges strongly in \(L^2\)
as \(\epsilon\downarrow0\).  Near \(s=0\), the heat kernel has a fixed
positive time and \(MY\) is integrable.  Near \(s=\tau\), the fields are
smooth and the singular power in (21) is integrable.

For every \(g\in L^2_\sigma\),

\[
\left\langle
S(\tau-\epsilon)v(\epsilon),g
\right\rangle
=
\left\langle
v(\epsilon),S(\tau-\epsilon)g
\right\rangle
\longrightarrow0.
\tag{22}
\]

Indeed, \(v(\epsilon)\rightharpoonup0\) and
\(S(\tau-\epsilon)g\to S(\tau)g\) strongly in \(L^2\).
Thus the first term in (19) tends weakly to zero.  Since the integral
has a strong limit, (19) forces that weak limit to be the zero strong
limit and proves (3).

### Interpretation

The fixed-time heat flow destroys the escaping boundary oscillations.
All of \(v(\tau)\), including its order-one \(L^2\) energy, must therefore
be rebuilt by the nonlinear term on \((0,\tau)\).  This is stronger than
merely saying that the weak boundary vector is zero.

## 3. Exact heat-deviation work

### Theorem 2: pressure-free boundary work identity

Equation (4) holds for every \(\tau>0\).

#### Proof

Pair (3) with \(v(\tau)\).  Self-adjointness of \(S\) and the solenoidal
range of \(S(\tau-s)v(\tau)\) remove the Leray projection:

\[
\|v(\tau)\|_2^2
=
-\int_0^\tau
\left\langle
(U\cdot\nabla)v(s),
S(\tau-s)v(\tau)
\right\rangle ds.
\tag{23}
\]

For each positive \(s\),

\[
\left\langle
(U\cdot\nabla)v(s),v(s)
\right\rangle
=0
\tag{24}
\]

because \(U\) is divergence free.  Subtracting this exact zero inside
(23) gives the first line of (4).  Spatial integration by parts gives
the second.

The scalar time integrand in (4) is understood through (23) minus the
pointwise zero (24).  It is integrable by (20)--(21).  No estimate of the
two spatial-gradient terms separately is asserted: such a triangle
inequality would discard precisely the endpoint cancellation recorded
by (24).

### Split into self and strong-drift work

Since both \(v\) and \(c\) are divergence free, (4) splits exactly into

\[
\|v(\tau)\|_2^2
=
\mathcal W_v(\tau)+\mathcal W_c(\tau),
\tag{25}
\]

where

\[
\mathcal W_z(\tau)
:=
\int_0^\tau\int
z_j(s)v_i(s)
\partial_j\left(
S(\tau-s)v_i(\tau)-v_i(s)
\right)dx\,ds,
\quad z\in\{v,c\}.
\tag{26}
\]

Neither term has a known sign.  The strong \(L^2\) trace of \(c\) does
not provide a rate for the gradient of the heat deviation in (26).

## 4. Fractional impulse consequences

### Theorem 3: half- and quarter-order entrance bounds

Equations (6)--(9) hold.  In addition, for every sufficiently small
\(h>0\),

\[
\liminf_{h\downarrow0}
h^{-1/2}\int_0^hMY\,ds
>0,
\tag{27}
\]

and

\[
MY\notin L^{2,q}(0,\tau_0)
\qquad(1\le q<\infty).
\tag{28}
\]

#### Proof

Besides (21), Lorentz heat smoothing gives

\[
\|S(r)g\|_{L^{3,\infty}}
\lesssim
(\nu r)^{-3/4}
\|g\|_{L^{6/5,2}}.
\tag{29}
\]

Apply (20), (21), and (29) in (3) to obtain (6).

Equation (15) implies

\[
\|v(\tau)\|_2\longrightarrow\sqrt d.
\tag{30}
\]

Thus the first estimate in (6) gives, for all sufficiently small
\(\tau\),

\[
I_{1/2}f(\tau)
\gtrsim
\sqrt{\nu d}.
\tag{31}
\]

Integrate (31) from \(0\) to \(h\).  Tonelli gives

\[
\begin{aligned}
\int_0^hI_{1/2}f(\tau)\,d\tau
&=
\int_0^hf(s)
\int_s^h(\tau-s)^{-1/2}\,d\tau\,ds\\
&=
2\int_0^hf(s)(h-s)^{1/2}\,ds\\
&\le
2h^{1/2}\int_0^hf(s)\,ds.
\end{aligned}
\tag{32}
\]

This proves (7) and (27).  Cauchy--Schwarz then proves (8).

If \(f\in L^{2,q}(0,\tau_0)\) for finite \(q\), absolute continuity of
that Lorentz norm and Lorentz Hölder would give

\[
\int_0^hf(s)\,ds
\lesssim
h^{1/2}
\|f\|_{L^{2,q}(0,h)}
=o(h^{1/2}),
\tag{33}
\]

contradicting (7).  This proves (28).

Finally, the entrance amplitude theorem gives

\[
\|v(\tau_j)\|_{L^{3,\infty}}\gtrsim m_j.
\tag{34}
\]

The second inequality in (6) proves (9).

### Corollary 4: a tail-product floor

If

\[
\mathcal M_2(h):=\int_0^hM^2,
\qquad
\mathcal D_v(h):=\int_0^hY^2,
\tag{35}
\]

then

\[
\mathcal M_2(h)\mathcal D_v(h)
\gtrsim
\nu d\,h.
\tag{36}
\]

On a canonical exact q4 record with

\[
\tau_j\asymp\frac{m_j^{-11/2}}j,
\qquad
\mathcal M_2(\tau_j)
\lesssim\frac{m_j^{-7/2}}j,
\tag{37}
\]

this gives

\[
\mathcal D_v(\tau_j)\gtrsim \nu d\,m_j^{-2}.
\tag{38}
\]

The existing full-defect frequency theorem gives the stronger
\(m_j^{-1}\)-scale floor.  Thus (38) is a consistency check, not a new
q4 closure.

## 5. Exact scalar endpoint saturation

Let \(0<s<e^{-1}\) and define (10).  Then

\[
M_\sharp^2
=s^{-4/11}\ell^{-4/11},
\qquad
Y_\sharp^2
=s^{-9/11}\ell^{2/11}.
\tag{39}
\]

Both are integrable at zero.  Standard one-sided power--log integration
gives (11).  Their amplitude-weighted dissipation is exactly

\[
M_\sharp Y_\sharp^2
=s^{-1},
\tag{40}
\]

which proves (12).

Moreover,

\[
f_\sharp
:=
M_\sharp Y_\sharp
=
s^{-13/22}\ell^{-1/11}.
\tag{41}
\]

Scaling \(s=h\rho\) in the two fractional integrals gives

\[
I_{1/2}f_\sharp(h)
\asymp
h^{-1/11}\ell(h)^{-1/11},
\tag{42}
\]

\[
I_{1/4}f_\sharp(h)
\asymp
h^{-15/44}\ell(h)^{-1/11}.
\tag{43}
\]

The first diverges and therefore satisfies (31).  Define the continuous
q4 amplitude scale

\[
m(h):=h^{-2/11}\ell(h)^{-2/11}.
\tag{44}
\]

Then

\[
\frac{I_{1/4}f_\sharp(h)}{m(h)}
\asymp
h^{-7/44}\ell(h)^{1/11}
\longrightarrow\infty,
\tag{45}
\]

so the record impulse condition (9) also survives.

If \(m_j\asymp2^{2j}\) and
\(h_j=m_j^{-11/2}/j\), then \(\ell(h_j)\asymp j\), and direct
substitution gives (13).

This scalar schedule simultaneously realises:

1. the exact q4 weak-\(L^3\) tail;
2. finite entrance dissipation with the known \(m_j^{-1}\) tail floor;
3. infinite \(M\)-weighted entrance dissipation;
4. the uniform half-order boundary impulse;
5. the record quarter-order amplitude impulse; and
6. failure of every finite Lorentz secondary index in (28).

It does not realise the signed heat-deviation work, spatial localisation,
the Leray projection, the pressure, or one Navier--Stokes trajectory.

## 6. Exact frontier

### Robust conditional findings, subject to external review

1. The weak-zero entrance has the exact zero-boundary mild formula (3).
2. Its full positive energy is regenerated by the pressure-free
   heat-deviation work (4).
3. The instantaneous transport cancellation is retained exactly inside
   that work.
4. Every entrance forces a non-vanishing half-order impulse (7), the
   tail-product floor (8), and failure of all finite
   \(L^{2,q}_\tau\) secondary indices for \(MY\).
5. The q4 amplitude layer forces the stronger recordwise quarter-order
   impulse (9).
6. The exact power--log ledger satisfies all scalar consequences together
   with the prior q4 tail and dissipation laws.

### Closed shortcut

Weak convergence of the boundary data plus a formal mild representation
does not by itself give \(v=0\).  The linear heat datum does vanish, but
the nonlinear Duhamel term is necessarily order one.  The small q4
\(L^2_\tau L^{3,\infty}_x\) tail for \(U\) is offset by a critical
concentration of \(\|\nabla v\|_2\).  Cauchy--Schwarz reaches only (8),
which is weaker than the already known frequency floor.

### Things still to prove

1. Prove that the positive work in (4) cannot be reused for an infinite
   nested family of terminal heat detectors.
2. Derive a finite \(L^{2,q}_\tau\), \(q<\infty\), bound for \(MY\) from
   the same-trajectory q4 coupling.
3. Obtain a signed or orthogonal decomposition of the heat-deviation work
   across descending frequency fronts.
4. Use the strong trace of \(c\) to make \(\mathcal W_c\) negligible at
   the q4 clock, without assuming a rate absent from strong \(L^2\)
   convergence.
5. Combine the \(\mathcal H^1\)-null initial energy measure with (4) to
   force a non-summable spatial-capacity charge.
6. Treat slower clocks, divergent normalised energy, and the other Clay
   alternatives separately.

### Conjecture: no reusable q4 boundary heat work

Under the exact same-trajectory q4 hypotheses, the family

\[
\mathcal W(\tau)
:=
-\int_0^\tau
\left\langle
(U\cdot\nabla)v(s),
S(\tau-s)v(\tau)-v(s)
\right\rangle ds
\tag{46}
\]

cannot satisfy

\[
\mathcal W(\tau)=\|v(\tau)\|_2^2\longrightarrow d>0
\tag{47}
\]

while the unweighted dissipation remains finite.

The conjecture is not proved.  The scalar ledger does not test its sign,
phase, or same-trajectory non-reuse content.  No Clay alternative is
proved.

## Downstream disposition

The subsequent
[diagonal Gaussian-flux reduction](type-ii-diagonal-heat-flux-recycling.md)
rewrites this future-dependent work as a current-time moving-heat flux,
proves its exact nested recycling law and disjoint-band \(\ell^1\)
estimate, and shows why that estimate still does not close q4.  The
theorems above remain inputs; their former non-reuse conjecture is now
replaced by the sharper actual-quadratic Gaussian-reuse gate there.
