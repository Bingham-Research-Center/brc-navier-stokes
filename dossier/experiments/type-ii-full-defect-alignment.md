# The full q4 defect aligns the Oseen entrance and reaches the nonlinear clock

- **Experiment:** EXP-TYPE-II-FULL-DEFECT-ALIGNMENT-001
- **Route:** ROUTE-R3C
- **Status:** complete conditional reduction; external review pending
- **Domain:** smooth finite-energy Navier--Stokes flow on \(\mathbb R^3\)
- **Clay status:** unsolved
- **Input:** [cross-frequency corridor](type-ii-cross-frequency-corridor.md)

## Verdict

The sub-clock cross-frequency corridor is not a survivor for a canonical
**full-defect** Oseen entrance.  The terminal detectors in the original
entrance construction can be chosen to exhaust the entire downward kinetic
energy jump, rather than merely one fixed ultraviolet portion.

Let

\[
E_-:=\lim_{t\uparrow T}\|u(t)\|_2^2,
\qquad
u_*:=u(T),
\qquad
d:=E_--\|u_*\|_2^2>0,
\tag{1}
\]

and let \(s_j\uparrow T\) be the selected exact q4 record endpoints.  Put

\[
w_j:=u(s_j)-u_*.
\tag{2}
\]

Uniform spatial tightness and \(w_j\rightharpoonup0\) permit finite annular
detectors \(g_j\) satisfying

\[
\boxed{
\|g_j-w_j\|_2\longrightarrow0,
\qquad
\|g_j\|_2^2\longrightarrow d,
\qquad
\langle u(s_j),g_j\rangle\longrightarrow d.
}
\tag{3}
\]

Launching the projected backward Oseen adjoints from \(g_j\) and taking the
usual compact-time limit gives one entrance field \(a\) with

\[
\langle u(t),a(t)\rangle=d,
\qquad
a(t)\rightharpoonup0
\quad(t\uparrow T).
\tag{4}
\]

The full-defect normalisation adds the exact alignment laws

\[
\boxed{
\|a(t)\|_2^2\le d,
\qquad
\lim_{t\uparrow T}\|a(t)\|_2^2=d,
\qquad
\|a(s_j)-w_j\|_2\longrightarrow0.
}
\tag{5}
\]

In fact the remainder

\[
b(t):=u(t)-a(t)
\tag{6}
\]

attains the Leray--Hopf trace strongly:

\[
\boxed{
b(t)\longrightarrow u_*
\quad\hbox{strongly in }L^2
\quad(t\uparrow T).
}
\tag{7}
\]

Thus the entrance field is exactly the missing terminal kinetic-energy
component, while \(b\) is the strongly continuous component.  If
\(\vartheta\) is the terminal kinetic-energy defect measure, then along the
record sequence

\[
\boxed{
|a(s_j)|^2\,dx
\overset{*}{\rightharpoonup}\vartheta,
\qquad
u(s_j)\cdot a(s_j)\,dx
\overset{*}{\rightharpoonup}\vartheta.
}
\tag{8}
\]

The cross defect is therefore positive and is exactly the primal energy
defect; it is not an arbitrary signed measure.

Let \(B_N=\psi(D/N)\), with \(0\le\psi\le1\) radial, nonincreasing in
\(|\xi|\), equal to one on the unit ball, and supported in the ball of
radius two.  Define

\[
K_N(t):=\langle u(t),B_Na(t)\rangle.
\tag{9}
\]

The strong decomposition (7) gives the uniform spectral identity

\[
\boxed{
\sup_{N>0}
\left|
K_N(t)-\langle a(t),B_Na(t)\rangle
\right|
\longrightarrow0
\quad(t\uparrow T).
}
\tag{10}
\]

At the selected records it also gives

\[
\boxed{
\sup_{N>0}
\left|
K_N(s_j)-\langle w_j,B_Nw_j\rangle
\right|
\longrightarrow0.
}
\tag{11}
\]

Hence the moving cross front is asymptotically the positive spectral-energy
front of both the adjoint entrance and the primal terminal defect.  Phase
and sign cannot sustain a separate sub-clock mechanism.

Let \(\kappa_j\) be the first dyadic cutoff for which
\(K_{\kappa_j}(s_j)\ge d/2\).  The terminal weak-\(L^3\) low-pass clock
proves

\[
\boxed{
\kappa_j\gtrsim
\Lambda_j
:=
m_j^{7/3}j^{2/3}.
}
\tag{12}
\]

Thus the earlier interval

\[
m_j^{9/4}j^{1/2}
\lesssim\kappa_j\ll
m_j^{7/3}j^{2/3}
\tag{13}
\]

is empty for the full-defect entrance.  The actual survivor is now entirely
at the nonlinear clock or above it.

The result does not close q4.  A fixed clock-scale energy packet over one
record tail has only

\[
(T-s_j)\Lambda_j^2
\asymp
m_j^{-5/6}j^{1/3},
\tag{14}
\]

which is summable along geometric records.  A theorem must still force
non-reusable residence, exploit the positive defect measure, or obtain
strong left continuity of \(u\).  No Clay alternative is proved.

## 1. Full-defect finite-band detectors

The exact q4 branch supplies a Leray--Hopf continuation, uniform spatial
tightness,

\[
\lim_{R\to\infty}
\sup_{t<T}
\int_{|x|>R}|u(x,t)|^2\,dx
=0,
\tag{15}
\]

and a nonzero energy jump \(d\) in (1).  Weak continuity gives

\[
u(s_j)\rightharpoonup u_*
\quad\hbox{in }L^2.
\tag{16}
\]

Consequently

\[
w_j\rightharpoonup0,
\qquad
\|w_j\|_2^2
=
\|u(s_j)\|_2^2-\|u_*\|_2^2+o(1)
\longrightarrow d.
\tag{17}
\]

The family \(w_j\) is uniformly spatially tight by (15) and
\(u_*\in L^2\).

### Lemma 1: fixed low frequencies vanish strongly

For every fixed \(L<\infty\),

\[
\boxed{
\|\Pi_{\le L}w_j\|_2\longrightarrow0.
}
\tag{18}
\]

Here \(\Pi_{\le L}\) may be any fixed smooth compactly supported Fourier
low pass.

#### Proof

The fields \(\Pi_{\le L}w_j\) are uniformly bounded in \(H^1\).  They are
also uniformly spatially tight.  To see the latter, write the low pass as
convolution with its Schwartz kernel.  Split \(w_j\) into its part inside a
large ball and its uniformly small exterior part.  Young's inequality
controls the exterior input, while the Schwartz tail controls the output
of the interior input outside a still larger ball.

Rellich compactness on bounded balls, followed by tightness, makes
\(\{\Pi_{\le L}w_j\}\) precompact in \(L^2(\mathbb R^3)\).  Its only
possible weak limit is zero by (17), proving (18).

### Lemma 2: a detector exhausting the whole defect

There are frequencies

\[
1<L_j<\Omega_j<\infty,
\qquad
L_j\longrightarrow\infty,
\tag{19}
\]

and solenoidal finite-band fields

\[
g_j
:=
\Pi_{L_j<|\xi|\le\Omega_j}w_j
\tag{20}
\]

for which (3) holds.

#### Proof

Apply Lemma 1 successively at \(L=1,2,\ldots\), and choose a staircase
\(L_j\uparrow\infty\) slowly enough that

\[
\|\Pi_{\le L_j}w_j\|_2\longrightarrow0.
\tag{21}
\]

For each fixed \(j\), Fourier-tail convergence permits
\(\Omega_j>L_j\) such that

\[
\|\Pi_{>\Omega_j}w_j\|_2\le j^{-1}.
\tag{22}
\]

Orthogonality of the three Fourier regions gives
\(\|g_j-w_j\|_2\to0\).  Equations (17) and (20) then give

\[
g_j\rightharpoonup0,
\qquad
\|g_j\|_2^2\longrightarrow d.
\tag{23}
\]

Finally,

\[
\begin{aligned}
\langle u(s_j),g_j\rangle
&=
\langle u_*+w_j,g_j\rangle\\
&=
\langle u_*,g_j\rangle+\|w_j\|_2^2
+\langle w_j,g_j-w_j\rangle
\longrightarrow d.
\end{aligned}
\]

This proves (3).  Smooth annular cutoffs may replace the sharp projections
after an arbitrarily small \(L^2\) approximation.

## 2. The full-defect Oseen entrance

For each \(j\), solve

\[
\partial_ta_j+\nu\Delta a_j
+\mathbb P((u\cdot\nabla)a_j)=0,
\qquad
a_j(s_j)=g_j.
\tag{24}
\]

The exact identities are

\[
\|a_j(t)\|_2^2
+2\nu\int_t^{s_j}\|\nabla a_j(r)\|_2^2\,dr
=
\|g_j\|_2^2,
\tag{25}
\]

and

\[
\langle u(t),a_j(t)\rangle
=
\langle u(s_j),g_j\rangle.
\tag{26}
\]

The compact-time argument from the Oseen entrance theorem gives, after
extraction,

\[
a\in
L^\infty(0,T;L^2_\sigma)
\cap
L^2(0,T;\dot H^1_\sigma),
\tag{27}
\]

solving (24) on \((0,T)\), with (4).

### Theorem 3: exact terminal alignment

Equations (5)--(8) hold.

#### Proof

Weak lower semicontinuity in the compact-time limit and (25) give, for
every \(t<T\),

\[
\|a(t)\|_2^2
\le
\liminf_j\|a_j(t)\|_2^2
\le
\lim_j\|g_j\|_2^2
=d.
\tag{28}
\]

At the selected record times, (4) and the zero weak terminal trace give

\[
\begin{aligned}
\langle w_j,a(s_j)\rangle
&=
\langle u(s_j),a(s_j)\rangle
-\langle u_*,a(s_j)\rangle\\
&=
d-o(1).
\end{aligned}
\tag{29}
\]

Equations (17), (28), (29), and Cauchy--Schwarz imply

\[
\sqrt d
\le
\liminf_j\|a(s_j)\|_2
\le
\limsup_j\|a(s_j)\|_2
\le
\sqrt d.
\tag{30}
\]

Therefore \(\|a(s_j)\|_2^2\to d\), and

\[
\begin{aligned}
\|a(s_j)-w_j\|_2^2
&=
\|a(s_j)\|_2^2+\|w_j\|_2^2
-2\langle a(s_j),w_j\rangle\\
&\longrightarrow d+d-2d=0.
\end{aligned}
\tag{31}
\]

The adjoint energy identity makes \(\|a(t)\|_2\) nondecreasing as
\(t\uparrow T\).  Its terminal limit exists, (28) bounds it above by
\(\sqrt d\), and (30) reaches that bound along \(s_j\).  Hence

\[
\lim_{t\uparrow T}\|a(t)\|_2^2=d.
\tag{32}
\]

Let \(b=u-a\).  It converges weakly to \(u_*\), and

\[
\begin{aligned}
\|b(t)\|_2^2
&=
\|u(t)\|_2^2+\|a(t)\|_2^2
-2\langle u(t),a(t)\rangle\\
&\longrightarrow
E_-+d-2d
=
\|u_*\|_2^2.
\end{aligned}
\tag{33}
\]

Weak convergence plus norm convergence proves (7).

Let

\[
\mathcal E
=
\operatorname*{w^*\!-\!lim}_j
|u(s_j)|^2\,dx,
\qquad
\vartheta:=\mathcal E-|u_*|^2\,dx.
\tag{34}
\]

The terminal-dimension theorem gives
\(\vartheta\ge0\), \(\vartheta(\mathbb R^3)=d\), and
\(\operatorname{supp}\vartheta\subset\sigma\).
Equation (31) implies

\[
\bigl\||a(s_j)|^2-|w_j|^2\bigr\|_{L^1}
\longrightarrow0.
\tag{35}
\]

The measures \(|w_j|^2dx\) converge to \(\vartheta\): expand
\(|u(s_j)-u_*|^2\), use weak convergence against compactly supported
multiples of \(u_*\), and use tightness for global mass.  This proves the
first statement in (8).

For the cross measures,

\[
u(s_j)\cdot a(s_j)-|w_j|^2
=
w_j\cdot(a(s_j)-w_j)+u_*\cdot a(s_j).
\tag{36}
\]

The first term tends to zero in \(L^1\).  The second tends weakly to zero
as a measure because \(a(s_j)\rightharpoonup0\); its tails are uniform by
Cauchy--Schwarz and \(u_*\in L^2\).  This proves the second statement in
(8).

### Corollary 4: exact terminal energy splitting

For every \(t<T\),

\[
\boxed{
\|a(t)\|_2^2
+2\nu\int_t^T\|\nabla a(r)\|_2^2\,dr
=d,
}
\tag{37}
\]

and

\[
\boxed{
\langle a(t),b(t)\rangle
=
d-\|a(t)\|_2^2
=
2\nu\int_t^T\|\nabla a(r)\|_2^2\,dr.
}
\tag{38}
\]

#### Proof

Apply the adjoint energy equality between \(t\) and \(r<T\), then let
\(r\uparrow T\) and use (32).  The second identity follows from
\(\langle u,a\rangle=d\) and \(b=u-a\).

The scalar product in (38) is global; it does not assert pointwise
positivity of \(a\cdot b\).

## 3. Uniform removal of the phase ambiguity

The following elementary compactness fact is useful.

### Lemma 5: the low-pass orbit of one \(L^2\) field is compact

For every \(f\in L^2\), the set

\[
\mathcal C_f
:=
\{B_Nf:0<N<\infty\}
\cup\{0,f\}
\tag{39}
\]

is norm-compact in \(L^2\).

#### Proof

The map \(N\mapsto B_Nf\) is norm-continuous by dominated convergence.
It tends to zero as \(N\downarrow0\) and to \(f\) as \(N\uparrow\infty\).
Thus it extends continuously to the compactified parameter interval
\([0,\infty]\), proving the claim.

### Theorem 6: the cross spectrum is positive asymptotically

Equations (10)--(11) hold.

#### Proof

Since \(u=a+b\),

\[
K_N(t)-\langle a(t),B_Na(t)\rangle
=
\langle b(t),B_Na(t)\rangle.
\tag{40}
\]

The contribution of \(b(t)-u_*\) is bounded uniformly in \(N\) by

\[
\|b(t)-u_*\|_2\|a(t)\|_2
\longrightarrow0
\tag{41}
\]

using (7).  By self-adjointness,

\[
\langle u_*,B_Na(t)\rangle
=
\langle B_Nu_*,a(t)\rangle.
\]

Weak convergence \(a(t)\rightharpoonup0\) is uniform on the norm-compact
set \(\mathcal C_{u_*}\) from Lemma 5.  This proves (10).

At \(t=s_j\), write

\[
\begin{aligned}
K_N(s_j)-\langle w_j,B_Nw_j\rangle
={}&
\langle u(s_j),B_N(a(s_j)-w_j)\rangle\\
&+
\langle B_Nu_*,w_j\rangle.
\end{aligned}
\tag{42}
\]

The first term tends uniformly to zero by (31).  The second does so
because \(w_j\rightharpoonup0\) uniformly on the compact set
\(\mathcal C_{u_*}\).  This proves (11).

Since \(0\le\psi\le1\) is radially nonincreasing,

\[
N\longmapsto\langle f,B_Nf\rangle
\tag{43}
\]

is nonnegative and nondecreasing.  Thus (10)--(11) remove, up to a
uniform \(o(1)\), every phase, sign, and nonmonotonicity ambiguity from
the cross spectrum near the terminal boundary.

## 4. The terminal low-pass clock

Put

\[
M(t):=\|u(t)\|_{L^{3,\infty}},
\qquad
B_{2,j}:=\int_{s_j}^TM(t)^2\,dt,
\qquad
\tau_j:=T-s_j.
\tag{44}
\]

The exact q4 tail satisfies

\[
B_{2,j}\lesssim\frac{m_j^{-7/2}}j,
\qquad
\tau_j\lesssim\frac{m_j^{-11/2}}j.
\tag{45}
\]

### Lemma 7: terminal weak-\(L^3\) low-pass freezing

For every \(N>0\),

\[
\boxed{
\|B_Nw_j\|_2
\lesssim
N^{3/2}B_{2,j}
+\nu U N^2\tau_j,
}
\tag{46}
\]

where \(U:=\sup_{t<T}\|u(t)\|_2\).

#### Proof

Apply \(B_N\) to the projected Navier--Stokes equation.  Lorentz duality
and Bernstein give

\[
\|B_N\mathbb P\nabla\cdot(u\otimes u)\|_2
\lesssim
N^{3/2}\|u\otimes u\|_{L^{3/2,\infty}}
\lesssim
N^{3/2}M(t)^2.
\tag{47}
\]

Also

\[
\|B_N\Delta u(t)\|_2
\lesssim
N^2U.
\tag{48}
\]

Integrating from \(s_j\) to \(r<T\) yields the right side of (46), with
the terminal integrals truncated at \(r\).

For fixed \(N\), the same estimate makes \(B_Nu(r)\) strongly Cauchy as
\(r\uparrow T\).  Its weak limit is \(B_Nu_*\), so its strong limit is
\(B_Nu_*\).  Let \(r\uparrow T\) to obtain (46).

### Theorem 8: collapse of the sub-clock corridor

Let

\[
\kappa_j
:=
\min\{2^k:K_{2^k}(s_j)\ge d/2\}.
\tag{49}
\]

Then (12) holds for all sufficiently large \(j\).

#### Proof

The uniform alignment (11) gives

\[
\langle w_j,B_{\kappa_j}w_j\rangle
\ge
\frac d3
\tag{50}
\]

for large \(j\).  Because \(B_{2\kappa_j}=1\) on the Fourier support of
the symbol of \(B_{\kappa_j}\),

\[
\begin{aligned}
\frac d3
&\le
\langle B_{2\kappa_j}w_j,B_{\kappa_j}w_j\rangle\\
&\le
\|B_{2\kappa_j}w_j\|_2\|w_j\|_2.
\end{aligned}
\tag{51}
\]

The norms of \(w_j\) are bounded and tend to \(\sqrt d\).  Equations
(46) and (51) therefore imply

\[
1
\lesssim
\kappa_j^{3/2}B_{2,j}
+\nu U\kappa_j^2\tau_j.
\tag{52}
\]

If the first term pays, then

\[
\kappa_j
\gtrsim
B_{2,j}^{-2/3}
\gtrsim
m_j^{7/3}j^{2/3}.
\tag{53}
\]

If the second term pays, then

\[
\kappa_j
\gtrsim
\tau_j^{-1/2}
\gtrsim
m_j^{11/4}j^{1/2}.
\tag{54}
\]

The ratio of the last scale to \(\Lambda_j\) is

\[
\frac{m_j^{11/4}j^{1/2}}
{m_j^{7/3}j^{2/3}}
=
m_j^{5/12}j^{-1/6}
\longrightarrow\infty.
\tag{55}
\]

Thus both alternatives imply (12).

### Interpretation

The refined cross-commutator estimate previously allowed

\[
\kappa_j
\int_{s_j}^TM(t)\|\nabla a(t)\|_2\,dt
\gtrsim1
\tag{56}
\]

at a frequency below \(\Lambda_j\).  The full-defect construction shows
why this was an artefact of incomplete genealogy: for the canonical
entrance, \(K_N(s_j)\) is the actual low-pass energy of \(w_j\), up to
\(o(1)\).  A fixed amount of that energy cannot appear below
\(\Lambda_j\), by the terminal primal low-pass clock (46).

This is not a rearrangement of the absolute commutator norm bounds.  It
uses three additional same-trajectory facts: full capture of the kinetic
defect, strong primal--adjoint terminal alignment, and the terminal
Navier--Stokes low-pass evolution.

## 5. Individual enstrophy and weighted-action consequences

The preceding cross-frequency theorem recorded the product
\(XY\gtrsim\kappa^2\).  The one-derivative high-pass estimates give
individual bounds.

### Proposition 9: individual moving-front floors

In reverse time \(\tau=T-t\), let

\[
B_1(\tau):=\int_0^\tau M(T-r)\,dr,
\quad
X(\tau):=\|\nabla u(T-\tau)\|_2,
\quad
Y(\tau):=\|\nabla a(T-\tau)\|_2.
\tag{57}
\]

For the full-defect entrance and all sufficiently small \(\tau\),

\[
\boxed{
X(\tau)^2
\gtrsim
\kappa(\tau)^2
\gtrsim
B_1(\tau)^{-1},
\qquad
Y(\tau)^2
\gtrsim
\kappa(\tau)^2
\gtrsim
B_1(\tau)^{-1}.
}
\tag{58}
\]

Consequently, with
\(\ell(\tau)=\log(e+\tau_0/\tau)\),

\[
\boxed{
\int_0^\tau X(r)^2\,dr
\gtrsim
\tau^{2/11}\ell(\tau)^{2/11},
\qquad
\int_0^\tau Y(r)^2\,dr
\gtrsim
\tau^{2/11}\ell(\tau)^{2/11}.
}
\tag{59}
\]

Both amplitude-weighted actions diverge:

\[
\boxed{
\int_0^{\tau_0}M(T-\tau)X(\tau)^2\,d\tau
=\infty,
\qquad
\int_0^{\tau_0}M(T-\tau)Y(\tau)^2\,d\tau
=\infty.
}
\tag{60}
\]

#### Proof

At the dyadic predecessor \(N=\kappa(\tau)/2\),

\[
\frac d2
<
\langle u,(I-B_N)a\rangle.
\tag{61}
\]

The high-pass multiplier obeys

\[
\|(I-B_N)f\|_2
\lesssim
N^{-1}\|\nabla f\|_2.
\tag{62}
\]

Using (28), the uniform kinetic-energy bound, and self-adjointness in
(61) gives separately

\[
X(\tau)\gtrsim\kappa(\tau),
\qquad
Y(\tau)\gtrsim\kappa(\tau).
\tag{63}
\]

The coarse commutator speed from the preceding theorem gives

\[
\kappa(\tau)^2B_1(\tau)\gtrsim1.
\tag{64}
\]

This proves (58).  The q4 clock bound

\[
B_1(\tau)
\lesssim
\tau^{9/11}\ell(\tau)^{-2/11}
\tag{65}
\]

and direct integration prove (59).

Finally \(B_1'(\tau)=M(T-\tau)\) almost everywhere.  Hence, for
\(0<\epsilon<\tau_0\),

\[
\int_\epsilon^{\tau_0}
\frac{M(T-\tau)}{B_1(\tau)}\,d\tau
=
\log B_1(\tau_0)-\log B_1(\epsilon)
\longrightarrow\infty
\tag{66}
\]

as \(\epsilon\downarrow0\).  Combine (58) and (66) to obtain (60).

At the q4 records, Theorem 8 strengthens (58) to

\[
\boxed{
\|\nabla u(s_j)\|_2^2
\gtrsim\Lambda_j^2,
\qquad
\|\nabla a(s_j)\|_2^2
\gtrsim\Lambda_j^2.
}
\tag{67}
\]

## 6. Sharp remaining clock ledger

The clock conclusion is still compatible with both unweighted energy
classes.  Take the representative q4 powers

\[
m_j:=2^{2j},
\qquad
\delta_j:=\frac{2^{-11j}}j,
\qquad
\Lambda_j:=2^{14j/3}j^{2/3}.
\tag{68}
\]

Then

\[
\delta_j\Lambda_j^2
=
2^{-5j/3}j^{1/3},
\tag{69}
\]

and therefore

\[
\sum_j\delta_j\Lambda_j^2<\infty.
\tag{70}
\]

On the other hand,

\[
m_j\delta_j\Lambda_j^2
=
2^{j/3}j^{1/3},
\tag{71}
\]

whose sum diverges.  Thus an order-one packet whose characteristic
frequency moves at the clock scale can have finite primal and adjoint
unweighted dissipation while saturating the forced weighted-action
divergence.

This is a temporal-frequency ledger, not a velocity field or a
Navier--Stokes construction.  It shows sharply that Theorem 8 removes the
sub-clock corridor but does not turn clock-scale pointwise concentration
into a contradiction.

## 7. Exact frontier

### Robust conditional findings, subject to external review

1. Uniform spatial tightness permits finite-band terminal data exhausting
   the entire kinetic-energy defect \(d\).
2. The resulting projected-Oseen entrance has pairing \(d\), norm at most
   \(\sqrt d\), terminal norm exactly \(\sqrt d\), and exact terminal
   energy identity (37).
3. Along the selected records,
   \(a(s_j)-(u(s_j)-u_*)\to0\) strongly in \(L^2\).
4. The complementary field \(b=u-a\) attains \(u_*\) strongly at \(T\).
5. The adjoint energy measure and primal--adjoint cross measure both equal
   the positive kinetic-energy defect measure \(\vartheta\).
6. Uniformly over all Fourier cutoffs, the cross spectrum becomes the
   positive spectral energy of \(a\), and at records also of \(w_j\).
7. The terminal weak-\(L^3\) low-pass clock forces
   \(\kappa_j\gtrsim\Lambda_j\); the sub-clock corridor is empty for this
   full-defect entrance.
8. Both individual enstrophy tails obey the stronger floor (59), and both
   weak-\(L^3\)-weighted actions diverge.

### Closed shortcut

The live obstruction is no longer arbitrary cross phase or sign.  For the
canonical full-defect entrance, phase aligns positively with the primal
energy defect and the sub-clock front is excluded.  Merely summing the
resulting clock-scale pointwise floors still fails: (68)--(71) show that
their unweighted residence charge is geometrically summable.

### Things still to prove

1. Turn the clock-scale defect quantile into a non-reusable residence,
   flux, or projective-motion charge.
2. Exploit the exact positive identity
   \(\zeta=\mathcal A=\vartheta\) in the local cross-current or terminal
   capacity equation.
3. Use the strong component \(b=u-a\to u_*\) to obtain a coercive relative
   energy or pressure identity for the remaining entrance component.
4. Prove strong left \(L^2\) continuity, energy equality, finite weighted
   adjoint action, or another established sufficient criterion.
5. Treat slower clocks, divergent normalised energy, and the other Clay
   alternatives separately.

### Conjecture: no clock-scale full-defect entrance

No smooth finite-energy Navier--Stokes trajectory approaching its first
singular time can possess a full-defect projected-Oseen entrance \(a\)
such that

\[
a(t)\rightharpoonup0,
\qquad
u(t)-a(t)\longrightarrow u_* \ \hbox{strongly},
\qquad
\kappa_j\gtrsim\Lambda_j,
\tag{72}
\]

while the common positive defect measure is supported on an
\(\mathcal H^1\)-null terminal singular slice.

The conjecture is not proved.  The result above closes only the sub-clock
corridor inside the conditional energy-efficient exact q4 branch.  No
Clay alternative is proved.
