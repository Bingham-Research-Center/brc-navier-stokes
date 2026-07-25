# The q4 cross defect forces a pressure-blind commutator anomaly

- **Experiment:** EXP-TYPE-II-CROSS-CURRENT-ANOMALY-001
- **Route:** ROUTE-R3C
- **Status:** complete conditional reduction; external review pending
- **Domain:** smooth finite-energy Navier--Stokes flow on \(\mathbb R^3\)
- **Clay status:** unsolved
- **Input:** [zero-trace Oseen entrance](type-ii-oseen-entrance.md)

## Verdict

The nonzero terminal cross defect has two exact descriptions.

In physical space, if

\[
c:=u\cdot a,
\]

then

\[
\partial_t c+\nabla\cdot J=0,
\tag{1}
\]

where

\[
\boxed{
J_k
=u_kc+p\,a_k+q\,u_k
-\nu\bigl(\partial_k u_i\,a_i-u_i\partial_k a_i\bigr).
}
\tag{2}
\]

Thus the projected adjoint pressure \(q\) appears in a genuine local
cross-current.  Its exact local payment against a cutoff \(\phi\) is

\[
\mathcal P_\phi[t,s]
:=
\int_t^s\int_{\mathbb R^3}
(p\,a+q\,u)\cdot\nabla\phi\,dx\,d\tau.
\tag{3}
\]

This payment has no sign.

In Fourier space, every scalar multiplier commuting with the Leray
projection and the Laplacian removes both pressures exactly.  For a smooth
low-pass \(B_N\),

\[
\boxed{
\frac d{dt}\langle u,B_Na\rangle
=
\bigl\langle[(u\cdot\nabla),B_N]u,a\bigr\rangle.
}
\tag{4}
\]

The terminal low-pass pairing vanishes, but the full pairing is
\(c_0>0\).  Consequently, for every fixed \(t_0<T\),

\[
\boxed{
\lim_{N\to\infty}
\int_{t_0}^{T}
\bigl\langle[(u\cdot\nabla),B_N]u,a\bigr\rangle\,dt
=-c_0.
}
\tag{5}
\]

The survivor therefore forces a signed commutator flux through arbitrarily
high frequency.  Pressure is structurally essential for local
solenoidality, but it is not the global spectral payer.

The terminal support gives a second, independent certificate.  The
nonzero cross measure \(\zeta\) is supported on
\(\sigma\), where \(\mathcal H^1(\sigma)=0\).  Hence

\[
\boxed{\zeta\notin H^{-1}(\mathbb R^3).}
\tag{6}
\]

Equivalently, every inhomogeneous Littlewood--Paley decomposition satisfies

\[
\sum_{k\ge-1}2^{-2k}\|\Delta_k\zeta\|_2^2=\infty.
\tag{7}
\]

Along the selected terminal sequence,

\[
\boxed{
\|u(s_j)\cdot a(s_j)\|_{H^{-1}}\longrightarrow\infty.
}
\tag{8}
\]

The most useful new reduction is a renormalisation theorem.  Put

\[
M(t):=\|u(t)\|_{L^{3,\infty}},
\qquad
Y(t):=\|\nabla a(t)\|_2.
\]

If

\[
\int_{t_0}^{T}M(t)Y(t)^2\,dt<\infty
\tag{9}
\]

for one \(t_0<T\), then the weak zero trace of \(a\) is attained strongly
and \(a\equiv0\) on \((t_0,T)\).  The entrance theorem contradicts that
conclusion.  Therefore the q4 survivor forces

\[
\boxed{
\int_t^T
\|u(s)\|_{L^{3,\infty}}\|\nabla a(s)\|_2^2\,ds
=\infty
\quad\text{for every }t<T,
}
\tag{10}
\]

even though

\[
\int_t^T\|\nabla a(s)\|_2^2\,ds<\infty.
\tag{11}
\]

This is a genuine concentration statement, not a missing estimate hidden
in prose.  The remaining q4 gate is now narrower:

> exclude an adjoint dissipation measure that is finite unweighted but has
> infinite first moment against the weak-\(L^3\) record amplitude.

For example, the Lorentz improvement

\[
\nabla a\in
L_t^{22/9,\,2}L_x^2
\tag{12}
\]

on one terminal interval would make (9) finite and close the q4 branch.
No such reverse Hölder estimate is proved here.

## 1. Equations and notation

Write the smooth preterminal equations in pressure form:

\[
\partial_tu-\nu\Delta u+(u\cdot\nabla)u+\nabla p=0,
\qquad
\nabla\cdot u=0,
\tag{13}
\]

and

\[
\partial_ta+\nu\Delta a+(u\cdot\nabla)a+\nabla q=0,
\qquad
\nabla\cdot a=0.
\tag{14}
\]

The pressures have the whole-space representatives

\[
-\Delta p
=\partial_i\partial_\ell(u_i u_\ell),
\qquad
-\Delta q
=\partial_i\partial_\ell(u_\ell a_i).
\tag{15}
\]

The input theorem supplies

\[
u,a\in
L^\infty_tL^2_\sigma
\cap L^2_t\dot H^1_\sigma,
\qquad
\langle u(t),a(t)\rangle=c_0>0,
\tag{16}
\]

\[
a(t)\rightharpoonup0
\quad(t\uparrow T),
\tag{17}
\]

and signed measures

\[
u(s_j)\cdot a(s_j)\,dx
\overset{*}{\rightharpoonup}\zeta,
\qquad
\zeta(\mathbb R^3)=c_0,
\qquad
\operatorname{supp}\zeta\subset\sigma.
\tag{18}
\]

The selected measures have uniformly bounded total variation and are
tight.

## 2. Exact local cross-current

### Proposition 1: local conservation

Equations (1)--(3) hold for every preterminal time interval.

#### Proof

Differentiate \(c=u_i a_i\), insert (13)--(14), and use
\(\nabla\cdot u=\nabla\cdot a=0\):

\[
\begin{aligned}
\partial_t c
={}&
\nu(\Delta u_i\,a_i-u_i\Delta a_i)
-(u\cdot\nabla)c\\
&-\partial_i p\,a_i-u_i\partial_i q.
\end{aligned}
\]

Each term is a divergence:

\[
\Delta u_i\,a_i-u_i\Delta a_i
=
\partial_k(\partial_k u_i\,a_i-u_i\partial_k a_i),
\]

\[
(u\cdot\nabla)c=\nabla\cdot(uc),
\qquad
\nabla p\cdot a=\nabla\cdot(pa),
\qquad
u\cdot\nabla q=\nabla\cdot(qu).
\]

This proves (1)--(2).  Therefore, for a compactly supported smooth scalar
cutoff \(\phi\),

\[
\int\phi c(s)-\int\phi c(t)
=
\int_t^s\int J\cdot\nabla\phi.
\tag{19}
\]

The pressure contribution to (19) is exactly (3).

### Terminal-current representation

Let

\[
G_t:=\int_t^T J(s)\,ds
\tag{20}
\]

whenever the integral is read in the distributional spaces proved below.
Passing to the terminal measure in (19) gives

\[
\boxed{
\zeta=c(t)\,dx-\nabla\cdot G_t.
}
\tag{21}
\]

This identity isolates the direct Sobolev-capacity target: if
\(G_t\in L^2(\mathbb R^3)\) for one \(t<T\), then
\(\zeta\in H^{-1}\), because (23) puts \(c(t)\) there.  This is
impossible by Lemma 2 below.

## 3. The singular slice forces an infinite \(H^{-1}\) spectrum

### Lemma 2: the capacity endpoint

Let \(S\subset\mathbb R^3\) satisfy \(\mathcal H^1(S)=0\).  An
\(H^{-1}(\mathbb R^3)\) distribution supported on \(S\) is zero.

#### Proof

Let \(F\in H^{-1}\) be supported on \(S\), and fix a test function
\(\psi\).  Zero one-dimensional Hausdorff measure implies zero
\(W^{1,2}\)-capacity in \(\mathbb R^3\).  The compact set
\(\operatorname{supp}F\cap\operatorname{supp}\psi\subset S\) therefore
has smooth neighbourhood cutoffs \(\chi_n\) satisfying

\[
\chi_n=1\ \text{near }
\operatorname{supp}F\cap\operatorname{supp}\psi,
\qquad
\|\chi_n\|_{H^1}\longrightarrow0.
\tag{22}
\]

\[
\langle F,\psi\rangle
=
\langle F,\chi_n\psi\rangle.
\]

The right side tends to zero because multiplication by the fixed smooth
\(\psi\) is bounded on \(H^1\).  Hence \(F=0\).

### Theorem 3: forced microlocal divergence

Equations (6)--(8) hold.

#### Proof

The measure \(\zeta\) is nonzero and supported on the
\(\mathcal H^1\)-null set \(\sigma\).  Lemma 2 proves (6).
Littlewood--Paley characterisation of \(H^{-1}\) then gives (7).

For every preterminal time,

\[
\begin{aligned}
\|u(t)\cdot a(t)\|_{H^{-1}}
&\lesssim
\|u(t)\|_{L^{3,\infty}}\|a(t)\|_2\\
&\lesssim U_2M(t).
\end{aligned}
\tag{23}
\]

Indeed, \(\dot H^1\hookrightarrow L^{6,2}\), and Lorentz Hölder
controls the pairing of
\(L^{3,\infty}\), \(L^2\), and \(L^{6,2}\).

Suppose (8) failed.  A subsequence of
\(u(s_j)\cdot a(s_j)\) would be bounded in the Hilbert space
\(H^{-1}\) and would have an \(H^{-1}\)-weak limit.  Its distributional
limit is already fixed by (18) and equals \(\zeta\), contradicting
(6).

More explicitly, for every fixed dyadic cutoff \(K\), tight weak-star
measure convergence and the smooth Fourier kernels give

\[
\Delta_k(u(s_j)\cdot a(s_j))
\longrightarrow
\Delta_k\zeta
\quad\text{strongly in }L^2
\quad(-1\le k\le K).
\tag{24}
\]

Taking \(K\to\infty\) in (7) proves the same divergence by finite
partial sums.

## 4. Pressure-free spectral cascade

Let \(B_N=m(D/N)\), where \(m\) is real, even, smooth, equals one near
the origin, and has compact Fourier support.  Then \(B_N\) is
self-adjoint and commutes with \(\Delta\) and the Leray projection.

### Theorem 4: exact commutator flux

Equations (4)--(5) hold.

#### Proof

Set \(T_u:=u\cdot\nabla\).  Differentiate
\(\langle u,B_Na\rangle\).  The two diffusion terms cancel because
\(B_N\) commutes with \(\Delta\).  The Leray projections disappear
against solenoidal fields and commute with \(B_N\).  Finally,
\(T_u\) is skew-adjoint because \(u\) is divergence free.  Hence

\[
\begin{aligned}
\frac d{dt}\langle u,B_Na\rangle
&=
-\langle B_NT_uu,a\rangle
-\langle B_Nu,T_ua\rangle\\
&=
\langle T_uB_Nu-B_NT_uu,a\rangle,
\end{aligned}
\]

which is (4).

For fixed \(N\), the preceding q4 spatial tightness and weak convergence
of \(u(s_j)\) imply

\[
B_Nu(s_j)\longrightarrow B_Nu_*
\quad\text{strongly in }L^2.
\tag{25}
\]

Since \(a(s_j)\rightharpoonup0\),

\[
\langle u(s_j),B_Na(s_j)\rangle
=
\langle B_Nu(s_j),a(s_j)\rangle
\longrightarrow0.
\tag{26}
\]

Integrating (4) from \(t_0\) to \(s_j\) and taking \(j\to\infty\)
gives

\[
\int_{t_0}^{T}
\langle[T_u,B_N]u,a\rangle\,dt
=
-\langle u(t_0),B_Na(t_0)\rangle.
\tag{27}
\]

The fixed-\(N\) integral is legitimate: the smooth multiplier kernel
and its derivative bound the commutator in \(L^2\) using only the
uniform \(L^2\) norms.  Finally \(B_N\to I\) strongly on \(L^2\), so
(16) and \(N\to\infty\) prove (5).

No pressure term has been estimated or discarded in this proof.  It
cancels algebraically because pure Fourier localisation respects the
solenoidal projection.

## 5. Finite weighted adjoint dissipation forbids the entrance

Reverse time:

\[
\tau:=T-t,
\qquad
v(\tau):=a(T-\tau),
\qquad
b(\tau):=-u(T-\tau),
\qquad
Q(\tau):=-q(T-\tau).
\tag{28}
\]

Then

\[
\partial_\tau v-\nu\Delta v
+(b\cdot\nabla)v+\nabla Q=0,
\qquad
\nabla\cdot b=\nabla\cdot v=0,
\tag{29}
\]

and

\[
v(\tau)\rightharpoonup0
\quad(\tau\downarrow0).
\tag{30}
\]

### Theorem 5: weighted renormalisation criterion

Suppose, on \(0<\tau<\tau_0\),

\[
v,b\in
L^\infty_\tau L^2_x\cap L^2_\tau\dot H^1_x
\tag{31}
\]

solve (29), have the weak trace (30), and satisfy

\[
\int_0^{\tau_0}
\|b(\tau)\|_{L^{3,\infty}}
\|\nabla v(\tau)\|_2^2\,d\tau
<\infty.
\tag{32}
\]

Then \(v=0\) on \((0,\tau_0)\).

#### Proof

Let \(\rho_\varepsilon\) be a spatial mollifier and put

\[
R_\varepsilon
:=
(b\otimes v)_\varepsilon-b\otimes v_\varepsilon.
\tag{33}
\]

For almost every \(\tau\), Lorentz Sobolev and Lorentz Hölder give

\[
\|R_\varepsilon(\tau)\|_2
\lesssim
\|b(\tau)\|_{L^{3,\infty}}
\|\nabla v(\tau)\|_2,
\tag{34}
\]

while

\[
R_\varepsilon(\tau)\longrightarrow0
\quad\text{in }L^2.
\tag{35}
\]

Also
\(\|\nabla v_\varepsilon\|_2\le\|\nabla v\|_2\).  Therefore

\[
|R_\varepsilon:\nabla v_\varepsilon|_{L^1_x}
\lesssim
\|b\|_{L^{3,\infty}}\|\nabla v\|_2^2.
\tag{36}
\]

Assumption (32) and dominated convergence make the transport
commutator vanish in \(L^1_\tau\).

It remains important not to assume a strong initial trace.  Fix a compact
spatial cutoff \(\chi_R\).  For fixed \(R,\varepsilon\), the operator

\[
f\longmapsto\chi_R(\rho_\varepsilon*f)
\]

is compact on \(L^2\).  Thus (30) implies

\[
\|\chi_Rv_\varepsilon(\tau)\|_2
\longrightarrow0
\quad(\tau\downarrow0).
\tag{37}
\]

Since
\[
\partial_\tau v_\varepsilon-\nu\Delta v_\varepsilon
+\nabla\cdot(b\otimes v_\varepsilon)+\nabla Q_\varepsilon
=-\nabla\cdot R_\varepsilon,
\]
testing on \((\delta,\tau_1)\) with
\(\chi_R^2v_\varepsilon\) gives
\[
\begin{aligned}
&\frac12\int\chi_R^2|v_\varepsilon(\tau_1)|^2
+\nu\int_\delta^{\tau_1}\int\chi_R^2|\nabla v_\varepsilon|^2\\
={}&\frac12\int\chi_R^2|v_\varepsilon(\delta)|^2\\
&+\int_\delta^{\tau_1}\int
\left[
\frac{\nu}{2}|v_\varepsilon|^2\Delta\chi_R^2
+\frac12|v_\varepsilon|^2b\cdot\nabla\chi_R^2
+Q_\varepsilon v_\varepsilon\cdot\nabla\chi_R^2
\right]\\
&+\int_\delta^{\tau_1}\int
\left[
\chi_R^2R_\varepsilon:\nabla v_\varepsilon
+R_\varepsilon:(\nabla\chi_R^2\otimes v_\varepsilon)
\right].
\end{aligned}
\tag{37a}
\]
First let \(\delta\downarrow0\) using (37), then let
\(\varepsilon\downarrow0\).  Equations (35)--(36) remove the interior
commutator.  The cutoff commutator is bounded by

\[
C_R\|b\|_{L^{3,\infty}}\|\nabla v\|_2\|v\|_2.
\]

Here energy interpolation gives
\(\|b\|_{L^{3,\infty}}\in L^4_\tau\); hence this bound is integrable
in time, and (35) again makes the cutoff commutator vanish.

The remaining cutoff fluxes vanish as \(R\to\infty\).  Indeed, energy
interpolation gives

\[
b,v\in L^4_\tau L^3_x,
\tag{38}
\]

and Calderón--Zygmund theory applied to
\(-\Delta Q=\partial_i\partial_\ell(b_\ell v_i)\) gives

\[
Q\in L^2_\tau L^{3/2}_x.
\tag{39}
\]

Consequently,

\[
b|v|^2,\ Qv\in L^{4/3}_\tau L^1_x,
\qquad
|v|^2\in L^\infty_\tau L^1_x.
\tag{40}
\]

For almost every terminal time \(\tau_1\leq\tau_0\), since
\(\|\nabla\chi_R\|_\infty=O(R^{-1})\) and
\(\|\Delta\chi_R\|_\infty=O(R^{-2})\), no energy can enter from
spatial infinity.  The limiting global identity is

\[
\frac12\|v(\tau_1)\|_2^2
+\nu\int_0^{\tau_1}\|\nabla v(\tau)\|_2^2\,d\tau
=0.
\tag{41}
\]

Thus \(v=0\) almost everywhere, and therefore as an energy-class
solution.

### Corollary 6: forced divergent weighted dissipation

The Oseen entrance satisfies (10).

#### Proof

If (10) failed on one terminal interval, the reverse field from (28)
would satisfy Theorem 5 and vanish.  This contradicts
\(\langle u,a\rangle=c_0>0\).

### Corollary 7: one sufficient temporal gain

If (12) held on a terminal interval, then the entrance would be
impossible.

#### Proof

The exact q4 clock gives

\[
M\in L^{11/2,\infty}_t.
\]

Equation (12) implies

\[
Y^2\in L^{11/9,1}_t.
\]

Endpoint Lorentz Hölder yields

\[
\int MY^2
\lesssim
\|M\|_{L^{11/2,\infty}}
\|Y^2\|_{L^{11/9,1}}
<\infty,
\]

contradicting Corollary 6.

## 6. What the local pressure estimate actually supplies

Decompose (2) as

\[
J=J^{\rm cub}+J^\nu,
\]

\[
J^{\rm cub}:=u(u\cdot a)+pa+qu,
\qquad
J^\nu_k:=-\nu(\partial_k u_i\,a_i-u_i\partial_k a_i).
\tag{42}
\]

Put

\[
X(t):=\|\nabla u(t)\|_2,
\qquad
Y(t):=\|\nabla a(t)\|_2.
\]

### Proposition 8: optimised current hull

For \(0\le\theta<3/7\), define

\[
\frac1{r_\theta}
=\frac13-\frac{\theta}{12},
\qquad
p_\theta:=\frac6{5-\theta},
\qquad
\rho_\theta:=\frac2{1+\theta}.
\tag{43}
\]

Then

\[
\boxed{
\|J^{\rm cub}(t)\|_{L^{p_\theta,\rho_\theta}}
\lesssim
M(t)^{2-\theta}X(t)^\theta Y(t).
}
\tag{44}
\]

The right side belongs to \(L^1_t\).  Moreover,

\[
\boxed{
\|J^\nu(t)\|_{L^{3/2,1}}
\lesssim
\nu X(t)Y(t),
}
\tag{45}
\]

whose right side also belongs to \(L^1_t\).

#### Proof

Real interpolation between
\(L^{3,\infty}\) and \(\dot H^1\hookrightarrow L^{6,2}\) gives

\[
\|u\|_{L^{r_\theta,\,4/\theta}}
\lesssim
M^{1-\theta/2}X^{\theta/2},
\tag{46}
\]

with the second Lorentz exponent interpreted as infinity at
\(\theta=0\).  Also

\[
\|a\|_{L^{6,2}}\lesssim Y.
\tag{47}
\]

Apply Lorentz Hölder to the three factors in \(u(u\cdot a)\).
For the pressure terms, use (15), Lorentz Calderón--Zygmund bounds,
and the same three factors.  All three cubic terms give (44).

The time Hölder index is

\[
\frac{2(2-\theta)}{11}
+\frac{\theta}{2}
+\frac12
=
\frac{19+7\theta}{22}
<1.
\tag{48}
\]

Thus the coefficient in (44) is time integrable.  Equation (45)
follows from Lorentz Sobolev and Cauchy--Schwarz in time.

### Exact capacity gap

As \(\theta\uparrow3/7\),

\[
p_\theta\uparrow\frac{21}{16},
\qquad
\rho_\theta\downarrow\frac75.
\tag{49}
\]

The dual spatial exponent required of a cutoff gradient therefore
approaches

\[
\left(\frac{21}{16}\right)'=\frac{21}{5},
\tag{50}
\]

whereas \(\mathcal H^1(\sigma)=0\) supplies small
\(L^2\) gradients through \(W^{1,2}\)-capacity.  The viscous current
still asks for the \(L^{3,\infty}\) gradient endpoint.  Hence the direct
current estimate does not reach the singular-slice capacity.

Equivalently, the best cubic reciprocal exponent has the gap

\[
\frac{16}{21}-\frac12=\frac{11}{42}.
\tag{51}
\]

This is the exact output of the available Hölder--Sobolev interpolation
hull.  It is not a theorem that cancellation or a trajectory-specific
Morrey estimate cannot close the gap.

### Pressure has no coercive lower bound from cross density

Equation (15) shows that \(q\) sees the longitudinal double contraction
of \(u_\ell a_i\), whereas \(u\cdot a\) is its trace.  These contractions
have different kernels.

For an exact symbol test on \(\mathbb T^3\), choose
\(k\ne0\), \(A\cdot k=0\), and

\[
u(x)=a(x)=A\cos(k\cdot x).
\tag{52}
\]

Then

\[
(u\cdot\nabla)a=0,
\qquad
q=0,
\qquad
u\cdot a=|A|^2\cos^2(k\cdot x)\ne0.
\tag{53}
\]

Thus no algebraic inequality can force a positive \(q\)-cost from cross
density alone.  This is a kinematic periodic obstruction, not a
same-trajectory Navier--Stokes counterexample.

## 7. Position relative to critical scalar drift theory

Qian and Xi prove \(L^2\) initial-value well-posedness, an energy
inequality, and regularity for scalar divergence-form parabolic equations
whose skew coefficient is uniformly bounded in
\(L^\infty_t\mathrm{BMO}_x\), equivalently for their stated
\(L^\infty_t\mathrm{BMO}^{-1}_x\) divergence-free drift class.

Their theorem is a genuine critical comparison, but it does not settle
the present gate:

1. no uniform terminal \(L^\infty_t\mathrm{BMO}^{-1}_x\) bound is among
   the q4 inputs;
2. the entrance is specified only by a zero weak trace, not an already
   attained \(L^2\) initial datum; and
3. (29) is a projected vector system with the nonlocal pressure \(Q\).

Theorem 5 instead identifies one trajectory-specific condition that is
sufficient for renormalisation and proves that the q4 survivor must
violate it.

## 8. Exact frontier

### Robust findings, subject to external review

1. The local primal--adjoint cross density obeys the exact conservation
   law (1)--(2), with pressure payment (3).
2. The nonzero \(\mathcal H^1\)-null terminal cross measure is not in
   \(H^{-1}\), forcing the dyadic divergence (7)--(8).
3. Pure Fourier localisation cancels both pressures and forces the
   signed commutator cascade (5).
4. Finite \(M\)-weighted adjoint dissipation would renormalise the
   reverse equation and kill the entrance; therefore (10) diverges on
   every terminal interval.
5. The temporal Lorentz gain (12) would close q4.
6. The full cubic current, including both pressures, approaches but does
   not claim the \(L_x^{21/16,\,7/5}\) endpoint, while the viscous current
   reaches \(L_x^{3/2,1}\); neither meets the \(L^2\) capacity target.
7. The adjoint pressure has no coercive lower bound from cross density
   alone.

### Things still to prove

1. Prove (12), or directly prove
   \(\int M\|\nabla a\|_2^2<\infty\), using the fact that \(u\) is the
   same Navier--Stokes trajectory paired with \(a\).
2. Alternatively, prove equiintegrability of the commutators in (5);
   that would contradict their fixed signed limit.
3. Find a cancellation-sensitive Morrey or capacity estimate for the
   total current \(G_t\) that reaches the \(\mathcal H^1\)-null slice
   without separately coercing \(q\).
4. Extend a successful theorem beyond the energy-efficient exact q4
   cell to slower clocks and divergent normalised energy.
5. Prove one complete Clay alternative for arbitrary admissible data.

### Conjecture: self-generated adjoint reverse Hölder gain

Under the exact q4 hypotheses, the same-trajectory projected adjoint
satisfies, on some terminal interval,

\[
\nabla a\in L_t^{22/9,2}L_x^2.
\tag{54}
\]

Corollary 7 shows that this conjecture excludes the q4 terminal energy
defect.  It is not proved, and no Clay alternative is closed.
