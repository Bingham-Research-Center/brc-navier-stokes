# The q4 defect forces a zero-trace Oseen entrance state

- **Experiment:** EXP-TYPE-II-OSEEN-ENTRANCE-001
- **Route:** ROUTE-R3C
- **Status:** complete conditional reduction; external review pending
- **Domain:** smooth finite-energy Navier--Stokes flow on \(\mathbb R^3\)
- **Clay status:** unsolved
- **Input:** [terminal dimension and spectral pincer](type-ii-terminal-dimension-pincer.md)

## Verdict

The terminal ultraviolet energy defect can be bundled into one genuine
same-trajectory adjoint object.  It is not necessary to choose between the
bounded clock-band and super-clock alternatives.

Let \(T=T^*\), let

\[
u_*:=u(T),
\qquad
w_j:=u(s_j)-u_*,
\]

and retain the forced high-pass floor

\[
\|\Pi_{>\Lambda_j}w_j\|_2\ge d_1>0,
\qquad
\Lambda_j\longrightarrow\infty.
\tag{1}
\]

There are finite upper cutoffs \(\Omega_j>\Lambda_j\) and solenoidal
finite-band terminal data

\[
g_j
:=
\Pi_{\Lambda_j<|\xi|\le\Omega_j}w_j
\tag{2}
\]

such that

\[
\|g_j\|_2\ge \frac{d_1}{2},
\qquad
g_j\rightharpoonup0
\quad\hbox{in }L^2.
\tag{3}
\]

Launch the projected backward Oseen adjoint

\[
\partial_t a_j+\nu\Delta a_j
+\mathbb P\bigl((u\cdot\nabla)a_j\bigr)=0,
\qquad
\nabla\cdot a_j=0,
\qquad
a_j(s_j)=g_j.
\tag{4}
\]

Here “projected Oseen adjoint” means the adjoint of the
frozen-drift operator
\[
\mathcal L_u v
:=
\partial_t v-\nu\Delta v+\mathbb P((u\cdot\nabla)v).
\]
It is not the adjoint of the full Fréchet linearisation of
Navier--Stokes, which would also contain the variation of the advecting
field.

After extraction, these adjoints produce one field

\[
a\in
L^\infty(0,T;L^2_\sigma)
\cap L^2(0,T;\dot H^1_\sigma)
\tag{5}
\]

which solves (4) on every compact subinterval of \((0,T)\) and satisfies

\[
\boxed{
\langle u(t),a(t)\rangle=c_0>0
\quad(0<t<T),
\qquad
a(t)\rightharpoonup0
\quad(t\uparrow T).
}
\tag{6}
\]

Consequently,

\[
\boxed{
\inf_{0<t<T}\|a(t)\|_2
\ge
\frac{c_0}{\sup_{0<t<T}\|u(t)\|_2}
>0.
}
\tag{7}
\]

In reverse time, \(a\) is therefore a nonzero finite-energy
**entrance state** with zero weak initial trace.  It is not asserted to
satisfy the initial energy inequality at that trace.  This distinction is
essential: calling (6) a standard zero-data energy solution would silently
assume the very strong-trace property that remains to be proved.

The same construction yields a nonzero terminal cross-defect measure
between \(u\) and \(a\), supported on the terminal singular set
\(\sigma\).  Thus the q4 branch has been reduced from infinitely many
changing tests to one pressure-coupled linear terminal-trace obstruction.

There is also an exact negative result for the more literal piecewise
adjoint proposal.  On every bounded-band event, resetting the unforced
adjoint to the event detector costs a fixed amount in \(L^2\).  Hence the
canonical patched adjoint has source variation growing linearly with the
number of events.  The reset cost is not a summable correction.

The route now closes if one proves the following genuinely new statement:

> Every energy-class solution of the projected Oseen adjoint driven by
> this same q4 Navier--Stokes trajectory that has zero weak terminal trace
> also has zero strong terminal trace.

The theorem is linear in the adjoint but not a generic scalar
advection--diffusion statement: solenoidal projection creates a nonlocal
adjoint pressure, and the drift lies strictly on the supercritical side of
the known scalar scaling line.  No such terminal rigidity theorem is
proved here.  The Clay problem remains unsolved.

## 1. A finite-band terminal detector

Let

\[
U_2:=\sup_{0<t<T}\|u(t)\|_2<\infty.
\tag{8}
\]

For each \(j\), monotone convergence of the Fourier tail permits a finite
\(\Omega_j>\Lambda_j\) for which

\[
\left\|
\Pi_{\Lambda_j<|\xi|\le\Omega_j}w_j
\right\|_2
\ge\frac{d_1}{2}.
\tag{9}
\]

Define \(g_j\) by (2).  The support of \(\widehat g_j\) escapes every
fixed ball, so \(g_j\rightharpoonup0\) in \(L^2\).  Also
\(\|g_j\|_2\le\|w_j\|_2\le2U_2\).  Moreover,

\[
\begin{aligned}
\langle u(s_j),g_j\rangle
&=
\langle w_j,g_j\rangle+\langle u_*,g_j\rangle\\
&=
\|g_j\|_2^2+\langle u_*,g_j\rangle.
\end{aligned}
\tag{10}
\]

Since

\[
|\langle u_*,g_j\rangle|
\le
\|\Pi_{>\Lambda_j}u_*\|_2\|g_j\|_2
\longrightarrow0,
\tag{11}
\]

we may pass to a subsequence such that

\[
\langle u(s_j),g_j\rangle\longrightarrow c_0,
\qquad
c_0\ge\frac{d_1^2}{4}>0.
\tag{12}
\]

The individual upper cutoffs \(\Omega_j\) are allowed to diverge
arbitrarily fast.  This is why the construction applies to both sides of
the earlier spectral alternative.

## 2. Exact projected-Oseen identities

For each \(j\), (4) is a smooth terminal-value problem on
\([0,s_j]\).  In pressure form it is

\[
\partial_ta_j+\nu\Delta a_j
+(u\cdot\nabla)a_j+\nabla q_j=0,
\qquad
\nabla\cdot a_j=0,
\tag{13}
\]

where

\[
-\Delta q_j
=
\partial_i u_\ell\,\partial_\ell(a_j)_i.
\tag{14}
\]

The pressure has zero global pairing with solenoidal fields but is
nonlocal and does not preserve a Fourier band.

### Lemma 1: adjoint energy and primal--adjoint pairing

For \(0\le t\le s_j\),

\[
\boxed{
\|a_j(t)\|_2^2
+2\nu\int_t^{s_j}\|\nabla a_j(\tau)\|_2^2\,d\tau
=
\|g_j\|_2^2
}
\tag{15}
\]

and

\[
\boxed{
\langle u(t),a_j(t)\rangle
=
\langle u(s_j),g_j\rangle.
}
\tag{16}
\]

#### Proof

Pair (13) with \(a_j\).  In reverse time the diffusion is dissipative,
while

\[
\int (u\cdot\nabla)a_j\cdot a_j=0,
\qquad
\int\nabla q_j\cdot a_j=0.
\]

This gives (15).

The projected Navier--Stokes equation is

\[
\partial_tu
=
\nu\Delta u-\mathbb P((u\cdot\nabla)u).
\]

Differentiate \(\langle u,a_j\rangle\).  The two diffusion terms cancel
by self-adjointness.  The transport terms cancel because

\[
\langle (u\cdot\nabla)u,a_j\rangle
=
-\langle u,(u\cdot\nabla)a_j\rangle.
\]

The two pressures pair to zero.  Hence the pairing is constant, proving
(16).

## 3. The Oseen entrance theorem

### Theorem 2: nonzero zero-trace adjoint entrance

After passing to a subsequence, there is a field \(a\) satisfying (5)--(7).
More precisely:

1. \(a\) solves
   \[
   \partial_t a+\nu\Delta a
   +\mathbb P((u\cdot\nabla)a)=0
   \tag{17}
   \]
   distributionally on \((0,T)\);
2. on every compact time interval inside \((0,T)\), \(a\) is the weak
   energy limit of \(a_j\);
3. \(\langle u(t),a(t)\rangle=c_0\) for every \(t<T\);
4. \(a(t)\rightharpoonup0\) in \(L^2\) as \(t\uparrow T\); and
5. \(a\) cannot converge strongly to zero at \(T\).

#### Proof

Equation (15) gives uniform bounds in

\[
L^\infty(0,T;L^2)
\cap L^2(0,T;\dot H^1)
\tag{18}
\]

after ignoring the vanishing terminal pieces on which \(a_j\) is not
defined.  On every interval \([0,T-\varepsilon]\), the coefficient \(u\)
is smooth.  The equation bounds \(\partial_ta_j\) in the corresponding
negative Sobolev space.  Standard weak compactness and a diagonal
extraction therefore give \(a\), with convergence in
\(C_{\rm w}([0,T-\varepsilon];L^2)\), and permit passage to (17).

For every fixed \(t<T\), equations (12) and (16) give

\[
\langle u(t),a(t)\rangle=c_0.
\tag{19}
\]

Let \(h\) be a solenoidal Schwartz field.  Pair (13) with \(h\), integrate
from \(t\) to \(s_j\), and integrate the drift by parts.  The energy
bounds for both fields give

\[
\begin{aligned}
|\langle a_j(t)-g_j,h\rangle|
\le{}&
C U_2\nu(s_j-t)\|\Delta h\|_2\\
&+
C U_2^2(s_j-t)\|\nabla h\|_\infty.
\end{aligned}
\tag{20}
\]

Indeed, (15) gives \(\|a_j\|_2\le2U_2\), while

\[
\|u\cdot\nabla h\|_2
\le
U_2\|\nabla h\|_\infty.
\]

Let \(j\to\infty\).  Since \(g_j\rightharpoonup0\),

\[
|\langle a(t),h\rangle|
\le
C_h(T-t).
\tag{21}
\]

The right side tends to zero as \(t\uparrow T\).  Density and the uniform
\(L^2\) bound prove \(a(t)\rightharpoonup0\).

Finally, (19) and Cauchy--Schwarz imply

\[
\|a(t)\|_2
\ge
\frac{c_0}{\|u(t)\|_2}
\ge
\frac{c_0}{U_2}.
\]

Thus the convergence cannot be strong.

### Interpretation

Reverse time by writing \(\tau=T-t\).  Then (17) becomes a forward
parabolic system with zero weak initial trace at \(\tau=0\), but (7)
shows a fixed amount of \(L^2\) energy immediately inside every positive
time.  The limit is an entrance law, not a standard solution known to
attain zero initial data strongly.

This is the exact compactness defect.  Proving that it cannot occur for a
self-generated Navier--Stokes drift would close the q4 terminal-energy
branch.

## 4. One cross-defect measure on the singular slice

The construction also retains spatial information.

### Proposition 3: singular support of the cross defect

After a further extraction along the record times, the signed measures

\[
u(s_j)\cdot a(s_j)\,dx
\tag{22}
\]

converge weak-star to a finite signed measure \(\zeta\) satisfying

\[
\boxed{
\zeta(\mathbb R^3)=c_0,
\qquad
\operatorname{supp}\zeta\subset\sigma.
}
\tag{23}
\]

In particular, if \(\mathcal A\) is a simultaneous local weak-star limit
of \(|a(s_j)|^2dx\), then

\[
\mathcal A(\sigma)>0.
\tag{24}
\]

#### Proof

The measures in (22) have uniformly bounded total variation.  The
previous q4 theorem supplies uniform spatial \(L^2\)-tightness of
\(u(s_j)\); Cauchy--Schwarz therefore makes the cross measures tight as
well.  Their total mass is \(c_0\) by (19), proving the first statement in
(23).

If \(K\Subset\mathbb R^3\setminus\sigma\), regularity near
\(K\times\{T\}\) gives

\[
u(s_j)\longrightarrow u_*
\quad\hbox{strongly in }L^2(K).
\]

Theorem 2 gives \(a(s_j)\rightharpoonup0\) in \(L^2\).  Testing with a
cutoff supported near \(K\) makes the cross pairing tend to zero.  An
exhaustion of the regular set proves the support statement.

The measure-valued Cauchy--Schwarz inequality gives, for Borel \(B\),

\[
|\zeta|(B)^2
\le
\mathcal E(B)\mathcal A(B),
\tag{25}
\]

where \(\mathcal E\) is the terminal energy measure of \(u\).  Since
\(\zeta\ne0\) and is supported on \(\sigma\), (24) follows.

Thus the adjoint entrance is not a remote algebraic mode: its cross energy
is anchored to the same terminal singular slice as the primal defect.

## 5. Piecewise adjoints pay a fixed reset

Return temporarily to Alternative A of the preceding spectral theorem.
Relabel its separated event times by \(s_k\), and let \(g_k\) be the
bounded clock-band detector.  The endpoint construction gives

\[
\langle u(s_{k+1})-u(s_k),g_k\rangle
\le-\frac{3\eta}{4}.
\tag{26}
\]

Let \(b_k\) solve the projected backward adjoint on
\([s_k,s_{k+1}]\) with

\[
b_k(s_{k+1})=g_k.
\tag{27}
\]

Define the reset

\[
r_k:=g_k-b_k(s_k).
\tag{28}
\]

### Proposition 4: exact reset floor

Every event satisfies

\[
\boxed{
\langle u(s_k),r_k\rangle
\ge\frac{3\eta}{4},
\qquad
\|r_k\|_2
\ge
\frac{3\eta}{4U_2}.
}
\tag{29}
\]

Consequently, the canonical forced piecewise adjoint which resets from
\(b_k(s_k)\) to \(g_k\) has \(L^2\)-valued source variation at least

\[
\sum_{k=1}^N\|r_k\|_2
\ge
\frac{3\eta}{4U_2}N.
\tag{30}
\]

#### Proof

Adjoint pairing conservation on \([s_k,s_{k+1}]\) gives

\[
\langle u(s_k),b_k(s_k)\rangle
=
\langle u(s_{k+1}),g_k\rangle.
\]

Subtract this identity from the pairing with \(g_k\) at \(s_k\) and use
(26).  This proves the first inequality in (29); Cauchy--Schwarz proves
the second.  A reset appears as the impulse
\(r_k\delta_{s_k}\) in the forced adjoint equation, so total variation
adds its \(L^2\) norms and gives (30).

The statement does not exclude every weighted or cancellation-sensitive
square function.  It does exclude the direct proposal that the event
detectors can be sewn together by finite \(L^2\)-variation jumps.

The unforced limit in Theorem 2 avoids the jumps only by retaining a
nonzero terminal entrance defect.

## 6. Diffusion, strain, and pressure audit

The exact q4 tail estimates also identify why elementary adjoint
perturbation does not remove the entrance state.

With
\[
M(t):=\|u(t)\|_{L^{3,\infty}},
\]
the record schedule gives

\[
\int_{s_j}^T M(t)\,dt
\lesssim
\frac{m_j^{-9/2}}{j},
\qquad
T-s_j
\lesssim
\frac{m_j^{-11/2}}{j},
\tag{31}
\]

while

\[
\Lambda_j\asymp m_j^{7/3}j^{2/3}.
\tag{32}
\]

### Pure diffusion is negligible in a bounded clock band

Under Alternative A, \(g_j\) is supported below \(A\Lambda_j\).  If
\(H_j\) is the backward heat evolution with terminal value \(g_j\), then

\[
\begin{aligned}
\|H_j(s_j)-g_j\|_2
&\le
\nu(s_{j+1}-s_j)(A\Lambda_j)^2\|g_j\|_2\\
&\lesssim
A^2m_j^{-5/6}j^{1/3}
\longrightarrow0.
\end{aligned}
\tag{33}
\]

Thus the fixed reset in (29) is not caused by heat acting on the original
clock band.  Transport or transport-generated frequencies must do the
work.

### The available Lipschitz estimate is supercritical

For a smooth low-pass cutoff,

\[
\|\nabla\Pi_{\le\mu}u(t)\|_\infty
\lesssim
\mu^2M(t).
\tag{34}
\]

Consequently,

\[
\int_{s_j}^T
\|\nabla\Pi_{\le\mu}u(t)\|_\infty\,dt
\lesssim
\mu^2\frac{m_j^{-9/2}}{j}.
\tag{35}
\]

The largest frequency for which this upper estimate remains order one is

\[
\mu_j\asymp m_j^{9/4}j^{1/2}.
\tag{36}
\]

It lies strictly below the clock:

\[
\boxed{
\frac{\Lambda_j}{\mu_j}
\asymp
m_j^{1/12}j^{1/6}
\longrightarrow\infty.
}
\tag{37}
\]

At \(\mu=\Lambda_j\), the right side of (35) is

\[
\lesssim m_j^{1/6}j^{1/3},
\tag{38}
\]

which is not perturbatively small.  Equation (38) is only the available
upper estimate, not a lower bound on actual strain.  It proves that the
standard bandlimited Lipschitz argument loses exactly the factor in (37).

### Pressure is energetically silent but structurally essential

The adjoint pressure (14) has zero global \(L^2\) work and does not alter
(15) or (16).  Variable transport already mixes frequencies; pressure
adds nonlocal component coupling through the solenoidal projection and
prevents a componentwise scalar maximum principle.  Dropping it changes
(4) into a different, non-solenoidal problem.

The remaining theorem must therefore control the complete projected
transport, not merely heat decay, low-frequency strain, or a scalar
maximum principle.

## 7. Location relative to scalar drift theory

The q4 velocity does enter strong sub-endpoint scalar drift spaces, but
only on the supercritical side.

Let \(0<\theta<1\) and define \(q_\theta\in(2,3)\) by

\[
\frac1{q_\theta}
=
\frac{1-\theta}{2}+\frac{\theta}{3}.
\tag{39}
\]

Real interpolation between \(L^2\) and weak \(L^3\) gives

\[
\|u(t)\|_{q_\theta}
\lesssim
U_2^{1-\theta}M(t)^\theta.
\tag{40}
\]

Hence

\[
u\in L^\ell_tL^{q_\theta}_x
\qquad
\hbox{for every }\theta\ell<\frac{11}{2}.
\tag{41}
\]

At the limiting exponent \(\ell=11/(2\theta)\), the scalar parabolic
index is

\[
\frac2\ell+\frac3{q_\theta}
=
\frac32-\frac{3\theta}{22}
>
\frac{15}{11}
>1.
\tag{42}
\]

Strong exponents approach but do not attain the rightmost limit
\(15/11\).

Qian and Xi prove Aronson-type upper estimates for smooth
divergence-free scalar drifts with index in \([1,2)\), but explicitly
state that regularity remains open in their supercritical regime; their
weak-solution uniqueness theorem is for the critical
\(L^\infty_tL^n_x\) case.  Their result therefore does not supply the
terminal strong-trace theorem required here.  In addition, (17) is a
projected vector system with the pressure (14), not their scalar
equation.

This comparison is contextual only.  No claim is made that the scalar
open problem and the projected Oseen gate are equivalent.

## 8. Exact frontier

### Robust findings, subject to external review

1. The entire q4 high-pass defect, not only one spectral alternative,
   yields finite-band terminal data with fixed \(L^2\) mass and weak
   limit zero.
2. The projected backward adjoints compactify to one nonzero
   energy-class entrance field whose zero weak terminal trace follows
   from finite kinetic energy alone.
3. Its constant primal pairing gives a nonzero cross-defect measure
   supported on the terminal singular set.
4. A literal piecewise-adjoint construction pays a fixed \(L^2\) reset
   per bounded-band event and therefore has linearly divergent source
   variation.
5. Pure heat is negligible at the bounded clock band, while the standard
   low-pass strain estimate loses the factor
   \(m_j^{1/12}j^{1/6}\).
6. Known scalar drift estimates place the q4 hull strictly in a
   supercritical regime and do not prove the required projected terminal
   strong trace.

### Things still to prove

1. Prove terminal strong-trace rigidity for the self-generated projected
   Oseen adjoint:
   \[
   a(t)\rightharpoonup0
   \quad\Longrightarrow\quad
   \|a(t)\|_2\to0.
   \]
2. Alternatively, show that the nonzero cross-defect measure in (23)
   cannot be supported on the Caffarelli--Kohn--Nirenberg terminal slice.
3. Find a pressure-sensitive compactness or microlocal budget that rules
   out the entrance state without assuming an unavailable scalar maximum
   principle.
4. Extend any successful theorem beyond the energy-efficient exact q4
   cell to the divergent-normalised-energy and slower-clock branches.
5. Prove one complete Clay alternative for arbitrary admissible data.

### Conjecture: self-generated Oseen terminal rigidity

Let \(u\) be a smooth finite-energy Navier--Stokes trajectory before its
first possible singular time and suppose its exact q4 record clock holds.
Every field

\[
a\in L^\infty_tL^2_\sigma\cap L^2_t\dot H^1_\sigma
\]

solving (17) on \((0,T)\) with \(a(t)\rightharpoonup0\) as \(t\uparrow T\)
must satisfy

\[
\|a(t)\|_2\longrightarrow0.
\]

Theorem 2 shows that this conjecture excludes the q4 terminal energy
defect.  The conjecture is not proved, and no Clay alternative is closed.
