# The full q4 defect is a nonlinear entrance from frequency infinity

- **Experiment:** EXP-TYPE-II-NONLINEAR-DEFECT-ENTRANCE-001
- **Route:** ROUTE-R3C
- **Status:** complete conditional reduction; external review pending
- **Domain:** smooth finite-energy Navier--Stokes flow on \(\mathbb R^3\)
- **Clay status:** unsolved
- **Input:** [full-defect alignment](type-ii-full-defect-alignment.md)

## Verdict

The positive full-defect alignment has a stronger dynamical
interpretation.  After reversing terminal time and changing sign, the
lost component is itself a forward Navier--Stokes field with an additional
divergence-free drift that has a strong \(L^2\) initial trace.

Let

\[
u=a+b,
\qquad
b(t)\longrightarrow u_*
\quad\hbox{strongly in }L^2
\quad(t\uparrow T),
\tag{1}
\]

where \(a\) is the full-defect projected-Oseen entrance and

\[
d
:=
\lim_{t\uparrow T}\|u(t)\|_2^2-\|u_*\|_2^2
>0.
\tag{2}
\]

For reverse time \(\tau=T-t\), define

\[
v(\tau):=-a(T-\tau),
\qquad
c(\tau):=-b(T-\tau).
\tag{3}
\]

Then

\[
\boxed{
\partial_\tau v-\nu\Delta v
+\mathbb P\bigl(((v+c)\cdot\nabla)v\bigr)=0,
\qquad
\nabla\cdot v=\nabla\cdot c=0.
}
\tag{4}
\]

In particular \(v\) advects itself.  Its boundary behaviour is

\[
\boxed{
v(\tau)\rightharpoonup0,
\qquad
c(\tau)\longrightarrow-u_*
\ \hbox{strongly in }L^2,
\qquad
\|v(\tau)\|_2^2
+2\nu\int_0^\tau\|\nabla v(s)\|_2^2\,ds
=d.
}
\tag{5}
\]

Thus \(v\) has zero weak vector trace but positive initial energy \(d\).
Along the exact q4 records \(\tau_j=T-t_j\),

\[
|v(\tau_j)|^2\,dx
\overset{*}{\rightharpoonup}\vartheta,
\tag{6}
\]

where \(\vartheta\) is the positive terminal kinetic-energy defect,
\(\vartheta(\mathbb R^3)=d\), and
\(\operatorname{supp}\vartheta\subset\sigma\) with
\(\mathcal H^1(\sigma)=0\).

Writing \(e_v=|v|^2/2\), the smooth positive-time local energy law is

\[
\partial_\tau e_v
+\nabla\cdot
\left(
(v+c)e_v+Qv-\nu\nabla e_v
\right)
=
-\nu|\nabla v|^2.
\tag{7}
\]

It has the exact measure-valued initial trace

\[
\boxed{
\frac12\vartheta
=
e_v(\tau)\,dx
+\nu\int_0^\tau|\nabla v(s)|^2\,ds\,dx
+\nabla\cdot
\int_0^\tau
\left(
(v+c)e_v+Qv-\nu\nabla e_v
\right)ds.
}
\tag{8}
\]

The field \(v\) is not a remote dual mode.  It owns the original
energy-efficient q4 amplitude layer.  If \(A_j\) is the first-record layer,
then

\[
\int_{A_j}|v(\tau_j)|^2\,dx\ge c>0,
\qquad
\boxed{
\|v(\tau_j)\|_{L^{3,\infty}}
\gtrsim m_j.
}
\tag{9}
\]

The problem has therefore become a nonlinear **coming down from frequency
infinity** obstruction:

> Can a dissipative forward Navier--Stokes field have zero weak initial
> vector data, positive singular initial energy measure, and q4-scale
> amplitude, when its additional drift has a strong energy-class trace?

The relative-energy calculation does not answer this automatically.  In
the original time direction, put

\[
r:=a\cdot b.
\tag{10}
\]

The two copies of the positive defect \(\vartheta\) cancel exactly:

\[
r(t)\,dx\rightharpoonup0
\quad(t\uparrow T),
\qquad
\int r(t)\,dx
=
2\nu\int_t^T\|\nabla a(s)\|_2^2\,ds.
\tag{11}
\]

There is an exact local relative-current law with the favourable source
\(-2\nu|\nabla a|^2\), and an exact pressure-free spectral version.
However, its commutator is bounded only by

\[
\|u\|_{L^{3,\infty}}
\|\nabla b\|_2
\|\nabla a\|_2,
\tag{12}
\]

whose terminal integral need not be finite.  Strong \(L^2\) convergence
of \(b\) supplies no rate for its vanishing high-frequency shadow.

The q4 Zeno ledger remains sharp:

\[
m_j^2\Lambda_j^{3/2}\delta_j\asymp1,
\qquad
\sum_j\delta_j\Lambda_j^2<\infty,
\qquad
\sum_jm_j\delta_j\Lambda_j^2=\infty.
\tag{13}
\]

It represents order-one nonlinear clock transfer through every record
while spending finite unweighted dissipation.  It is not a
Navier--Stokes construction.  The next missing result is a genuinely new
zero-trace nonlinear entrance theorem, a quantitative compactness theorem
for the strong remainder at the clock, or a non-summable inverse-cascade
charge.  No Clay alternative is proved.

## 1. Reverse-time nonlinearisation

The full-defect entrance solves, in pressure form,

\[
\partial_ta+\nu\Delta a
+(u\cdot\nabla)a+\nabla q=0,
\qquad
\nabla\cdot a=0.
\tag{14}
\]

Since \(u=a+b\), it is already semilinear in the entrance component:

\[
\partial_ta+\nu\Delta a
+((a+b)\cdot\nabla)a+\nabla q=0.
\tag{15}
\]

### Theorem 1: a perturbed Navier--Stokes entrance

Equations (4)--(5) hold.  In pressure form,

\[
\partial_\tau v-\nu\Delta v
+((v+c)\cdot\nabla)v+\nabla Q=0,
\tag{16}
\]

where

\[
Q(\tau):=q(T-\tau),
\qquad
-\Delta Q
=
\partial_i\partial_\ell
\bigl((v_\ell+c_\ell)v_i\bigr).
\tag{17}
\]

#### Proof

The definitions (3) give

\[
u(T-\tau)=-(v(\tau)+c(\tau)).
\]

Also

\[
\partial_ta(T-\tau)=\partial_\tau v(\tau),
\qquad
\Delta a(T-\tau)=-\Delta v(\tau).
\]

Substitution in (14) gives (16), hence (4).  The pressure equation follows
from the projected-Oseen pressure formula.

The full-defect theorem gives

\[
a(t)\rightharpoonup0,
\qquad
b(t)\to u_*
\quad(t\uparrow T),
\]

which becomes the first two statements in (5).  Its exact terminal
adjoint energy identity is

\[
\|a(t)\|_2^2
+2\nu\int_t^T\|\nabla a(s)\|_2^2\,ds
=d.
\]

Changing variables gives the third statement.

### Interpretation

For \(0<\epsilon<\tau\),

\[
\|v(\tau)\|_2^2
+2\nu\int_\epsilon^\tau\|\nabla v(s)\|_2^2\,ds
=
\|v(\epsilon)\|_2^2.
\tag{18}
\]

This is the standard forward dissipative energy equality away from the
initial boundary.  The failure is entirely at \(\tau=0\):

\[
v(0)=0
\quad\hbox{only weakly},
\qquad
\lim_{\tau\downarrow0}\|v(\tau)\|_2^2=d.
\tag{19}
\]

If (18) extended to the boundary with the ordinary \(L^2\) datum zero,
then \(v\equiv0\), contradicting \(d>0\).  Proving that extension under
the exact q4 hypotheses would close the conditional cell.

## 2. Positive initial energy measure

Let \(t_j\) now be the exact first-record sequence itself.  Once \(d>0\)
is known, the full-defect finite-band construction may be run along this
sequence.  Put

\[
\tau_j:=T-t_j.
\tag{20}
\]

The full-defect alignment gives

\[
|a(t_j)|^2\,dx
\overset{*}{\rightharpoonup}\vartheta.
\tag{21}
\]

Equation (6) follows immediately from \(v(\tau_j)=-a(t_j)\).

### Proposition 2: local energy law from the measure trace

Let

\[
F_v
:=
(v+c)e_v+Qv-\nu\nabla e_v.
\tag{22}
\]

Then (7) holds classically for every \(\tau>0\).  For every
\(\phi\in C_c^\infty(\mathbb R^3)\) and every fixed \(\tau>0\),

\[
\boxed{
\frac12\int\phi\,d\vartheta
=
\int\phi e_v(\tau)\,dx
+\nu\int_0^\tau\int\phi|\nabla v|^2\,dx\,ds
-\int_0^\tau\int F_v\cdot\nabla\phi\,dx\,ds.
}
\tag{23}
\]

This is the distributional identity (8).

#### Proof

Dot (16) with \(v\).  Since \(v+c\) and \(v\) are divergence free,

\[
v\cdot((v+c)\cdot\nabla v)
=
\nabla\cdot((v+c)e_v),
\qquad
v\cdot\nabla Q
=
\nabla\cdot(Qv).
\]

The diffusion identity

\[
-\nu v\cdot\Delta v
=
-\nu\Delta e_v+\nu|\nabla v|^2
\]

gives (7).

Integrate (7) from \(\epsilon\) to \(\tau\) against \(\phi\), then take
\(\epsilon=\tau_j\downarrow0\) along the defect sequence.  The boundary
term converges by (21).  The energy-class bounds put the cubic and pressure
fluxes locally in \(L^{10/9}_{\tau,x}\), while
\(v\nabla v\) is locally integrable.  Hence the flux integrals converge.
This proves (23).

Taking cutoffs \(\phi\uparrow1\) recovers the global identity (5).

### Consequence

The entrance does not create scalar energy from zero.  It starts from the
nonzero positive measure \(\vartheta\), even though its vector barycentre
is zero.  Any boundary energy inequality that reads only the weak vector
trace loses precisely this microlocal energy datum.

## 3. The entrance owns the q4 amplitude layer

At the first record \(t_j\), let

\[
A_j:=\{\alpha_j<|u(t_j)|\le2\alpha_j\},
\qquad
e_j:=\int_{A_j}|u(t_j)|^2\,dx,
\tag{24}
\]

with

\[
e_j\ge e_0>0,
\qquad
R_j:=|A_j|^{1/3}\asymp m_j^{-2}.
\tag{25}
\]

### Theorem 3: Type-II amplitude inheritance

For all sufficiently large \(j\),

\[
\boxed{
\int_{A_j}|a(t_j)|^2\,dx
\ge\frac{e_0}{4},
\qquad
\|a(t_j)\|_{L^{3,\infty}}
\gtrsim m_j.
}
\tag{26}
\]

Equivalently, (9) holds for \(v(\tau_j)\).

#### Proof

Since \(b(t_j)\to u_*\) strongly in \(L^2\),

\[
\int_{A_j}|b(t_j)|^2\,dx
\le
2\|b(t_j)-u_*\|_2^2
+2\int_{A_j}|u_*|^2\,dx.
\tag{27}
\]

The first term tends to zero.  The second does too, because
\(|A_j|=R_j^3\to0\) and the \(L^1\) integral of \(|u_*|^2\) is uniformly
absolutely continuous.  Hence

\[
\|a(t_j)\|_{L^2(A_j)}
\ge
\|u(t_j)\|_{L^2(A_j)}
-\|b(t_j)\|_{L^2(A_j)}
\ge
\sqrt{e_0}-o(1),
\]

which proves the first statement.

The finite-volume weak-\(L^3\) inequality gives

\[
\int_{A_j}|a(t_j)|^2\,dx
\lesssim
|A_j|^{1/3}
\|a(t_j)\|_{L^{3,\infty}}^2.
\tag{28}
\]

Using \(|A_j|^{1/3}=R_j\asymp m_j^{-2}\) proves the second statement.

Thus the full-defect component inherits both fixed carrier energy and the
record weak-\(L^3\) amplitude scale.  The strongly convergent remainder
cannot carry that energy on the shrinking layer.

## 4. Exact local relative-energy cancellation

Return to the original time variable.  The fields satisfy

\[
\partial_tu-\nu\Delta u
+(u\cdot\nabla)u+\nabla p=0,
\tag{29}
\]

\[
\partial_ta+\nu\Delta a
+(u\cdot\nabla)a+\nabla q=0.
\tag{30}
\]

Subtracting gives

\[
\partial_tb-\nu\Delta b
+(u\cdot\nabla)b+\nabla(p-q)
=
2\nu\Delta a.
\tag{31}
\]

Define \(r=a\cdot b\) and the relative current

\[
\boxed{
\begin{aligned}
\mathcal J_k^{\rm rel}
:={}&
u_kr+(p-q)a_k+qb_k\\
&+
\nu\left(
u_i\partial_ka_i
-a_i\partial_ku_i
-2a_i\partial_ka_i
\right).
\end{aligned}
}
\tag{32}
\]

### Theorem 4: relative-current law

For every preterminal time,

\[
\boxed{
\partial_t r+\nabla\cdot\mathcal J^{\rm rel}
=
-2\nu|\nabla a|^2.
}
\tag{33}
\]

Moreover,

\[
r(t)\,dx\rightharpoonup0
\quad(t\uparrow T),
\tag{34}
\]

and

\[
\boxed{
\int_{\mathbb R^3}r(t)\,dx
=
2\nu\int_t^T\|\nabla a(s)\|_2^2\,ds.
}
\tag{35}
\]

#### Proof

The cross-current theorem gives

\[
\partial_t(u\cdot a)+\nabla\cdot J^{\rm cross}=0,
\]

\[
J_k^{\rm cross}
=
u_k(u\cdot a)+pa_k+qu_k
-\nu(\partial_ku_i\,a_i-u_i\partial_ka_i).
\tag{36}
\]

The local adjoint-energy identity is

\[
\partial_t|a|^2
+\nabla\cdot
\left(
u|a|^2+2qa+2\nu a_i\nabla a_i
\right)
=
2\nu|\nabla a|^2.
\tag{37}
\]

Subtract (37) from (36), use \(b=u-a\), and obtain (32)--(33).

The full-defect theorem gives

\[
u(t)\cdot a(t)\,dx\rightharpoonup\vartheta,
\qquad
|a(t)|^2\,dx\rightharpoonup\vartheta
\]

along the defect sequence, so their difference has terminal measure zero.
The same conclusion holds distributionally for the full terminal limit
because \(b(t)\to u_*\) strongly and \(a(t)\rightharpoonup0\).  This is
(34).

Finally,

\[
\int r
=
\langle a,u-a\rangle
=
d-\|a(t)\|_2^2,
\]

and the exact adjoint terminal energy identity gives (35).

### Local terminal representation

For every compactly supported scalar test \(\phi\),

\[
\boxed{
2\nu\int_t^T\int\phi|\nabla a|^2
=
\int\phi\,a(t)\cdot b(t)
+\int_t^T\int
\mathcal J^{\rm rel}\cdot\nabla\phi.
}
\tag{38}
\]

Unlike the terminal cross measure, neither term on the right has a known
sign.  Positivity of \(\vartheta\) has cancelled before (38) is reached.

## 5. Exact spectral relative-energy balance

Let \(B_N\) be the smooth self-adjoint low pass from the preceding round,
and put

\[
R_N(t)
:=
\langle b(t),B_Na(t)\rangle.
\tag{39}
\]

The cross and adjoint low-pass identities are

\[
\frac d{dt}\langle u,B_Na\rangle
=
\langle[(u\cdot\nabla),B_N]u,a\rangle,
\tag{40}
\]

\[
\frac d{dt}\langle a,B_Na\rangle
=
2\nu\langle\nabla a,B_N\nabla a\rangle
+\langle[(u\cdot\nabla),B_N]a,a\rangle.
\tag{41}
\]

### Theorem 5: pressure-free relative balance

\[
\boxed{
\frac d{dt}R_N
=
\langle[(u\cdot\nabla),B_N]b,a\rangle
-2\nu\langle\nabla a,B_N\nabla a\rangle.
}
\tag{42}
\]

The full-defect spectral alignment gives

\[
\sup_{N>0}|R_N(t)|\longrightarrow0
\quad(t\uparrow T).
\tag{43}
\]

Consequently,

\[
\boxed{
R_N(t)
=
2\nu\int_t^T
\langle\nabla a,B_N\nabla a\rangle\,ds
-
\int_t^T
\langle[(u\cdot\nabla),B_N]b,a\rangle\,ds.
}
\tag{44}
\]

#### Proof

Since \(R_N=\langle u,B_Na\rangle-\langle a,B_Na\rangle\), subtract
(41) from (40).  The two commutators combine linearly:

\[
\bigl[(u\cdot\nabla),B_N\bigr]\,(u-a)
=
[(u\cdot\nabla),B_N]b.
\]

This proves (42).  Equation (43) is exactly the uniform positive-spectrum
theorem from the full-defect round.  Integrating (42) to \(T\) proves
(44).

At \(N=\infty\), the commutator vanishes and (44) becomes (35).  Thus the
global relative identity contains no independent extra charge.

### Lemma 6: available relative commutator bounds

With

\[
M:=\|u\|_{L^{3,\infty}},
\qquad
Y:=\|\nabla a\|_2,
\qquad
Z:=\|\nabla b\|_2,
\tag{45}
\]

one has

\[
\boxed{
\left|
\langle[(u\cdot\nabla),B_N]b,a\rangle
\right|
\lesssim
MZY.
}
\tag{46}
\]

If
\[
A:=\sup_{t<T}\|a(t)\|_2,
\qquad
B:=\sup_{t<T}\|b(t)\|_2,
\]
then also

\[
\boxed{
\left|
\langle[(u\cdot\nabla),B_N]b,a\rangle
\right|
\lesssim
BNMY+ABN^2M.
}
\tag{47}
\]

#### Proof

For the first commutator piece, skew-adjointness gives

\[
\begin{aligned}
|\langle(u\cdot\nabla)B_Nb,a\rangle|
&=
|\langle B_Nb,(u\cdot\nabla)a\rangle|\\
&\lesssim
\|B_Nb\|_{L^{6,2}}MY
\lesssim MZY.
\end{aligned}
\]

For the second,

\[
\begin{aligned}
|\langle B_N(u\cdot\nabla)b,a\rangle|
&=
|\langle b,(u\cdot\nabla)B_Na\rangle|\\
&\lesssim
\|b\|_{L^{6,2}}M\|\nabla B_Na\|_2\\
&\lesssim MZY.
\end{aligned}
\]

This proves (46).

Alternatively,

\[
\|B_Nb\|_{L^{6,2}}\lesssim NB,
\qquad
\|\nabla B_Na\|_{L^{6,2}}\lesssim N^2A,
\]

which gives the two terms in (47).

### Exact obstruction

The available energy estimate controls \(Z\) only through
\(Z^2\in L^1_t\), while \(M\) is unbounded and the preceding q4 theorem
forces

\[
\int_t^TMY^2=\infty.
\]

These facts do not prove that the commutator integral diverges.  They show
that neither (46) nor (47) supplies a uniform integrable majorant at the
clock.  Strong \(L^2\) convergence of \(b\) does imply that its terminal
path is norm-compact and that its high-frequency \(L^2\) tail vanishes
uniformly.  It supplies no rate after multiplication by \(N\) or \(N^2\),
and no control of the high-frequency gradient shadow.  Therefore the
current hypotheses give (44) neither a coercive sign nor a finite
commutator budget.

## 6. The Zeno coming-down ledger

Take

\[
m_j:=2^{2j},
\qquad
\delta_j:=\frac{2^{-11j}}j,
\qquad
\Lambda_j:=2^{14j/3}j^{2/3}.
\tag{48}
\]

Then the direct nonlinear clock capacity on one record block is exactly

\[
\boxed{
m_j^2\Lambda_j^{3/2}\delta_j=1.
}
\tag{49}
\]

The unweighted clock action is

\[
q_j
:=
\delta_j\Lambda_j^2
=
2^{-5j/3}j^{1/3},
\tag{50}
\]

so

\[
\sum_jq_j<\infty.
\tag{51}
\]

The weak-\(L^3\)-weighted action is

\[
m_jq_j
=
2^{j/3}j^{1/3},
\tag{52}
\]

and its sum diverges.

### A Hilbert-frequency realisation of every scalar budget

Let \(\{e_j\}\) be an orthonormal sequence and assign frequency
\(\Lambda_j\) to \(e_j\).  Put

\[
D_j:=\sum_{k\ge j}q_k,
\qquad
A_j:=(d-2\nu D_j)^{1/2},
\tag{53}
\]

for large \(j\), and define

\[
v(\tau_j):=A_je_j.
\tag{54}
\]

Then

\[
v(\tau_j)\rightharpoonup0,
\qquad
\|v(\tau_j)\|_2^2+2\nu D_j=d.
\tag{55}
\]

Choose a fixed vector \(c_*\) orthogonal to all \(e_j\), and put

\[
c(\tau_j)
:=
c_*+\beta_je_j,
\qquad
\beta_j:=\frac{2\nu D_j}{A_j}.
\tag{56}
\]

Then

\[
c(\tau_j)\longrightarrow c_*
\quad\hbox{strongly},
\qquad
\langle v(\tau_j),c(\tau_j)\rangle
=
2\nu D_j.
\tag{57}
\]

Thus the discrete ledger simultaneously realises:

1. zero weak vector trace and positive limiting energy;
2. a strongly convergent remainder with a vanishing high-frequency shadow;
3. the exact global relative overlap;
4. clock-scale frequency escape;
5. finite unweighted and infinite amplitude-weighted action; and
6. order-one nonlinear capacity on every Zeno block.

It does not define spatial fields, the pressure, the local current, or a
Navier--Stokes solution.  Separately, the
[triad-packet sharpness theorem](type-ii-triad-packet-sharpness.md)
constructs genuine smooth one-event Navier--Stokes packets with either
sign of band transfer and the sharp vanishing dissipation power.  That
theorem varies the trajectory from event to event.  Together the two
sharpness results show exactly why a same-trajectory inverse-cascade or
boundary-energy theorem is still required.

## 7. Exact frontier

### Robust conditional findings, subject to external review

1. The full-defect entrance becomes a forward perturbed Navier--Stokes
   solution after terminal reversal and sign change.
2. Its additional drift has a strong \(L^2\) initial trace, but the
   nonlinear component has zero weak vector trace and positive energy \(d\).
3. The positive measure \(\vartheta\) is the exact initial energy trace in
   the local balance (8).
4. The nonlinear entrance owns a fixed portion of every q4 amplitude layer
   and has weak-\(L^3\) norm at least a fixed multiple of \(m_j\).
5. The common positive defect cancels exactly in the relative density
   \(a\cdot b\); its total mass is only the shrinking future adjoint
   dissipation.
6. The local and spectral relative balances (33), (42), and (44) are exact
   and pressure-consistent.
7. Available relative commutator bounds require \(MZY\) or clock-amplified
   strong-remainder norms; neither is controlled by strong \(L^2\) trace.
8. The Zeno ledger satisfies every scalar energy, overlap, clock, and
   weighted-action constraint with a strongly convergent remainder.

### Closed shortcut

Subtracting the equal positive primal and adjoint defects does not leave a
second fixed positive reservoir.  It leaves the shrinking quantity

\[
2\nu\int_t^T\|\nabla a\|_2^2,
\]

and a sign-indefinite relative current.  Strong \(L^2\) convergence of the
remainder, without a clock-relative rate or gradient compactness, does not
make that current summable.

### Things still to prove

1. Prove a zero-trace nonlinear entrance theorem: under the exact q4 clock,
   (4)--(6) force \(d=0\).
2. Equivalently, extend the forward energy inequality in (18) to
   \(\tau=0\) using the zero weak vector trace, strong-trace drift, and
   same-trajectory coupling.
3. Prove a non-summable inverse-cascade or projective-motion charge for
   coming down from frequency infinity.
4. Obtain a quantitative clock-relative compactness modulus for \(c\), or
   a finite bound for the relative commutator in (44).
5. Exclude the positive initial energy measure \(\vartheta\) by its
   \(\mathcal H^1\)-null support or the coupled pressure law.
6. Treat slower clocks, divergent normalised energy, and the other Clay
   alternatives separately.

### Conjecture: no q4 nonlinear entrance from infinity

Let

\[
v,c\in
L^\infty_\tau L^2_\sigma
\cap L^2_\tau\dot H^1_\sigma
\]

satisfy (4) on \((0,\tau_0)\), with

\[
v(\tau)\rightharpoonup0,
\qquad
c(\tau)\to c_0\ \hbox{strongly in }L^2,
\qquad
\lim_{\tau\downarrow0}\|v(\tau)\|_2^2=d.
\]

If \(v+c\) comes from the exact q4 first-record reversal of one smooth
Navier--Stokes trajectory and \(v\) carries the energy-efficient q4
layers, then \(d=0\).

The conjecture is not proved.  Its same-trajectory and q4 clauses are
essential: the Hilbert ledger is a scalar obstruction, and generic weak
solutions are not being claimed to satisfy terminal rigidity.  No Clay
alternative is proved.
