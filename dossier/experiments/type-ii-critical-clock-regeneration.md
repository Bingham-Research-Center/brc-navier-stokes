# The critical weak-\(L^3\) clock forces an ultraviolet increment

- **Experiment:** EXP-TYPE-II-CRITICAL-CLOCK-REGENERATION-001
- **Route:** ROUTE-R3C
- **Status:** complete conditional quantitative reduction; external review pending
- **Domain:** smooth finite-energy Navier--Stokes flow on \(\mathbb R^3\)
- **Clay status:** unsolved
- **Input:** [diffuse-fragmentation theorem](type-ii-diffuse-fragmentation.md)

## Verdict

The low-frequency side of the exact \(q=4\) spectral dichotomy is no
longer open.  A fixed future amplitude layer cannot be assembled at low
frequency across one fixed block of first-record intervals.

Let

\[
m_j:=\|u(t_j)\|_{L^{3,\infty}}\asymp 2^{2j},
\qquad
\Delta_j^{(L)}:=t_j-t_{j-L}
\asymp_L\frac{m_j^{-11/2}}j,
\]

where \(L\) is one sufficiently large fixed integer.  If the selected
layer \(A_j\) has energy

\[
0<c_0\le e_j:=\int_{A_j}|u(t_j)|^2\,dx\le E_0,
\qquad
R_j:=|A_j|^{1/3}\asymp m_j^{-2},
\]

then, for one fixed sufficiently small \(\kappa>0\), define

\[
\Lambda_j
:=
\kappa\bigl(m_j^2\Delta_j^{(L)}\bigr)^{-2/3}
\asymp_L m_j^{7/3}j^{2/3}
\asymp_L R_j^{-7/6}j^{2/3}.
\]

For a fixed smooth Littlewood--Paley split,

\[
\boxed{
\left\langle
P_{>\Lambda_j}\bigl(u(t_j)-u(t_{j-L})\bigr),
u(t_j)\mathbf 1_{A_j}
\right\rangle\ge c>0,
}
\]

and consequently

\[
\boxed{
\left\|
P_{>\Lambda_j}\bigl(u(t_j)-u(t_{j-L})\bigr)
\right\|_2\ge c.
}
\]

At least one endpoint \(s_j\in\{t_{j-L},t_j\}\) therefore obeys

\[
\boxed{
\|P_{>\Lambda_j}u(s_j)\|_2\ge c,
\qquad
\|\nabla u(s_j)\|_2^2
\gtrsim
\Lambda_j^2
\asymp
R_j^{-7/3}j^{4/3}.
}
\]

If the smooth solution has a Leray--Hopf continuation \(u_*=u(T^*)\),
then \(s_j\uparrow T^*\), \(u(s_j)\rightharpoonup u_*\) in \(L^2\), and
\(\|P_{>\Lambda_j}u_*\|_2\to0\).  Hence the left energy limit has a
strict defect:

\[
\boxed{
\lim_{t\uparrow T^*}\|u(t)\|_2^2-\|u_*\|_2^2\ge c.
}
\]

Thus every energy-efficient exact \(q=4\) branch requires anomalous
kinetic-energy loss at the first singular time.  It is conditionally
excluded by energy equality, or equivalently strong left \(L^2\)
continuity, at \(T^*\).  Energy equality for arbitrary Leray--Hopf
solutions is open, and the present \(q=4\) hypotheses have not been shown
to satisfy a known sufficient criterion.  The result therefore narrows
R3C but does not close it.

## 1. Setting and fixed Fourier split

Let \(u\) be a smooth divergence-free finite-energy solution on
\(\mathbb R^3\times[0,T^*)\), where \(T^*\) is its first possible
singular time.  Write

\[
\sup_{t<T^*}\|u(t)\|_2^2\le E_0.
\]

Choose exact \(q=4\) first-record times \(t_j\uparrow T^*\).  Besides the
displayed size and gap laws, first-record sampling gives

\[
\|u(t)\|_{L^{3,\infty}}\le m_j
\qquad(0\le t\le t_j).
\tag{1}
\]

Choose a real radial \(\psi\in C_c^\infty(\mathbb R^3)\) with

\[
0\le\psi\le1,\qquad
\psi(\xi)=1\quad(|\xi|\le1),\qquad
\psi(\xi)=0\quad(|\xi|\ge2),
\]

and set

\[
\widehat{P_{\le\Lambda}f}(\xi)
=\psi(\xi/\Lambda)\widehat f(\xi),
\qquad
P_{>\Lambda}:=I-P_{\le\Lambda}.
\tag{2}
\]

These multipliers are self-adjoint \(L^2\) contractions.  The multiplier
of \(P_{>\Lambda}\) vanishes on \(\{|\xi|\le\Lambda\}\), so

\[
\|P_{>\Lambda}f\|_2
\le\Lambda^{-1}\|\nabla f\|_2.
\tag{3}
\]

## 2. Two endpoint estimates

### Lemma 1: finite-volume weak-\(L^3\) capacity

For every measurable \(E\subset\mathbb R^3\) of finite measure and every
\(g\in L^{3,\infty}\),

\[
\boxed{
\int_E|g|^2\,dx
\le C|E|^{1/3}\|g\|_{L^{3,\infty}}^2.
}
\tag{4}
\]

#### Proof

Put \(M=\|g\|_{L^{3,\infty}}\) and
\(\lambda_0=M|E|^{-1/3}\).  The layer-cake formula and

\[
|\{|g|>\lambda\}|\le M^3\lambda^{-3}
\]

give

\[
\begin{aligned}
\int_E|g|^2
&=\int_0^\infty
2\lambda\,|E\cap\{|g|>\lambda\}|\,d\lambda\\
&\le\lambda_0^2|E|
+2M^3\int_{\lambda_0}^\infty\lambda^{-2}\,d\lambda\\
&\le3M^2|E|^{1/3}.
\end{aligned}
\]

### Lemma 2: critical low-pass clock

Let \(0\le s<t<T^*\), and suppose

\[
\sup_{s\le\tau\le t}
\|u(\tau)\|_{L^{3,\infty}}\le M.
\]

Then

\[
\boxed{
\|P_{\le\Lambda}(u(t)-u(s))\|_2
\le
C\left(
M^2\Lambda^{3/2}
+\nu\sqrt{E_0}\Lambda^2
\right)(t-s).
}
\tag{5}
\]

#### Proof

Apply \(P_{\le\Lambda}\) to the projected equation:

\[
\partial_tu
=-\mathbb P\nabla\cdot(u\otimes u)+\nu\Delta u.
\tag{6}
\]

For a tensor \(F\in L^{3/2,\infty}\), duality and Lorentz Hölder give

\[
\|P_{\le\Lambda}\mathbb P\nabla\cdot F\|_2
\le
C\|F\|_{3/2,\infty}
\sup_{\|h\|_2=1}
\|\nabla\mathbb P P_{\le\Lambda}h\|_{3,1}.
\tag{7}
\]

Plancherel and Fourier Cauchy--Schwarz yield

\[
\|\nabla\mathbb P P_{\le\Lambda}h\|_2
\le C\Lambda\|h\|_2,
\qquad
\|\nabla\mathbb P P_{\le\Lambda}h\|_\infty
\le C\Lambda^{5/2}\|h\|_2.
\]

Real interpolation of this one function between \(L^2\) and
\(L^\infty\) gives

\[
\|\nabla\mathbb P P_{\le\Lambda}h\|_{3,1}
\le C\Lambda^{3/2}\|h\|_2.
\tag{8}
\]

Since

\[
\|u\otimes u\|_{3/2,\infty}
\le C\|u\|_{3,\infty}^2,
\]

the nonlinear term in (6) is bounded in \(L^2\) by
\(CM^2\Lambda^{3/2}\).  The viscous term satisfies

\[
\|P_{\le\Lambda}\Delta u\|_2
\le C\Lambda^2\|u\|_2
\le C\sqrt{E_0}\Lambda^2.
\]

Integrate (6) from \(s\) to \(t\).

## 3. Fixed signed ultraviolet increment

### Theorem 3

Under the setting in Section 1 and the energy-efficient layer bounds,
there are fixed \(L\in\mathbb N\), \(\kappa>0\), \(c>0\), and \(j_0\)
such that the two boxed ultraviolet conclusions in the Verdict hold for
every \(j\ge j_0\).

#### Proof

Set \(i=j-L\) and

\[
f_j:=u(t_j)\mathbf1_{A_j},
\qquad
\|f_j\|_2^2=e_j.
\tag{9}
\]

Lemma 1, the record ratio
\(m_{j-L}/m_j\lesssim2^{-2L}\), and
\(R_jm_j^2\asymp1\) give

\[
\int_{A_j}|u(t_i)|^2\,dx
\le CR_jm_i^2
\le C2^{-4L}.
\tag{10}
\]

Choose \(L\) sufficiently large, depending only on the fixed ledger
constants, so that Cauchy--Schwarz and (10) imply

\[
|\langle u(t_i),f_j\rangle|
\le \frac{c_0}{4}.
\tag{11}
\]

Since \(\langle u(t_j),f_j\rangle=e_j\ge c_0\),

\[
\left\langle u(t_j)-u(t_i),f_j\right\rangle
\ge\frac{3c_0}{4}
=:c_1.
\tag{12}
\]

For fixed \(L\), summing the geometric record gaps gives

\[
\Delta_j^{(L)}
:=t_j-t_i
\asymp_L\frac{m_j^{-11/2}}j.
\tag{13}
\]

The first-record ceiling (1) permits Lemma 2 with \(M=m_j\).  Define

\[
\Lambda_j
=\kappa(m_j^2\Delta_j^{(L)})^{-2/3}.
\tag{14}
\]

Then

\[
m_j^2\Lambda_j^{3/2}\Delta_j^{(L)}
=\kappa^{3/2},
\tag{15}
\]

whereas

\[
\Delta_j^{(L)}\Lambda_j^2
\asymp_L
m_j^{-5/6}j^{1/3}
\longrightarrow0.
\tag{16}
\]

Choose \(\kappa\) sufficiently small, and then \(j\) sufficiently large,
so that (5), (15), and (16) imply

\[
\|P_{\le\Lambda_j}(u(t_j)-u(t_i))\|_2
\le\frac{c_1}{2\sqrt{E_0}}.
\tag{17}
\]

Pairing (17) with \(f_j\), then subtracting from (12), gives

\[
\left\langle
P_{>\Lambda_j}(u(t_j)-u(t_i)),f_j
\right\rangle
\ge\frac{c_1}{2}.
\tag{18}
\]

Thus

\[
\|P_{>\Lambda_j}(u(t_j)-u(t_i))\|_2
\ge\frac{c_1}{2\sqrt{E_0}}.
\tag{19}
\]

The triangle inequality makes at least one of the two endpoint
high-pass norms bounded below by a fixed constant.  Equation (3) then
gives the enstrophy floor.

Finally, (13)--(14), \(R_j\asymp m_j^{-2}\), and
\(m_j\asymp2^{2j}\) give

\[
\Lambda_j
\asymp_Lm_j^{7/3}j^{2/3}
\asymp_LR_j^{-7/6}j^{2/3},
\tag{20}
\]

and hence

\[
\|\nabla u(s_j)\|_2^2
\gtrsim
m_j^{14/3}j^{4/3}
\asymp
R_j^{-7/3}j^{4/3}.
\tag{21}
\]

The physical ultraviolet length is

\[
r_j:=\Lambda_j^{-1}
\asymp
R_j^{7/6}j^{-2/3},
\tag{22}
\]

strictly below the earlier Morrey fragmentation scale
\(R_j^{27/26+o(1)}\).

## 4. Terminal energy loss

### Corollary 4

Suppose \(u\) has a Leray--Hopf continuation through \(T^*\), represented
weakly continuously in \(L^2\), and put \(u_*=u(T^*)\).  Then

\[
\lim_{t\uparrow T^*}\|u(t)\|_2^2-\|u_*\|_2^2\ge c>0.
\tag{23}
\]

In particular, energy equality at \(T^*\) excludes the
energy-efficient exact \(q=4\) record branch.

#### Proof

Both possible endpoint sequences \(t_j\) and \(t_{j-L}\) converge to
\(T^*\).  Pass to an infinite subsequence on which the same endpoint
choice is used.  Weak continuity gives

\[
u(s_j)\rightharpoonup u_*
\quad\hbox{in }L^2.
\tag{24}
\]

Since \(\Lambda_j\to\infty\),

\[
\|P_{>\Lambda_j}u_*\|_2\longrightarrow0.
\tag{25}
\]

The endpoint floor and (25) imply

\[
\|u(s_j)-u_*\|_2
\ge
\|P_{>\Lambda_j}(u(s_j)-u_*)\|_2
\ge c-o(1).
\tag{26}
\]

The smooth energy equality below \(T^*\) makes
\(\|u(t)\|_2^2\) nonincreasing, so its left limit \(E_-\) exists.  By
(24),

\[
\|u(s_j)-u_*\|_2^2
=\|u(s_j)\|_2^2-\|u_*\|_2^2+o(1).
\tag{27}
\]

Equations (26)--(27) prove \(E_--\|u_*\|_2^2\ge c\).  Equality across
\(T^*\) would instead give \(E_-=\|u_*\|_2^2\).

The last conditional exclusion is not unconditional: the general
energy-equality problem for Leray--Hopf solutions remains open.  Known
Besov and mixed-norm hypotheses provide sufficient criteria, but no such
criterion is derived here from the exact \(q=4\) ledger.

## 5. Sharp static ledgers

The exponent in (21) cannot be improved from the layer geometry and
local Morrey information alone.

Let \(m\to\infty\), set

\[
R=m^{-2},
\qquad
r=m^{-7/3}j^{-2/3},
\qquad
a=m^3,
\qquad
N\asymp(R/r)^3\asymp mj^2.
\tag{28}
\]

Place \(N\) disjoint translates of one fixed smooth compactly supported
divergence-free packet, each with radius \(r\) and amplitude \(a\),
quasi-uniformly in a fixed cube.  The resulting field \(U_j\) obeys

\[
\|U_j\|_2^2\asymp1,
\qquad
\|U_j\|_{3,\infty}\asymp m,
\tag{29}
\]

and a fixed regular amplitude band has volume \(R^3\) and energy
comparable to one.  Moreover,

\[
\|\nabla U_j\|_2^2
\asymp Na^2r
\asymp r^{-2}
\asymp m^{14/3}j^{4/3},
\tag{30}
\]

\[
\operatorname{Per}(A_j)
\asymp Nr^2
\asymp R^{11/6}j^{2/3}.
\tag{31}
\]

Each packet has energy \(N^{-1}\asymp m^{-1}j^{-2}\), and quasi-uniform
placement gives, for every fixed \(0<\beta<1/9\),

\[
\sup_x\int_{B_\rho(x)}|U_j|^2\,dx
\le C_\beta\rho^\beta
\qquad(0<\rho\le1).
\tag{32}
\]

For \(\rho\le r\), this follows from the packet amplitude and (28); for
\(r\le\rho\) below the centre separation, one packet contributes at
most \(N^{-1}\le Cr^\beta\); above the separation, quasi-uniform packing
gives \(C(N^{-1}+\rho^3)\le C\rho^\beta\).

There is also a rate-sharp small core.  At
\(\Lambda=m^{7/3}j^{2/3}\), take a generic nonstationary
divergence-free bump of radius \(\Lambda^{-1}\) and amplitude

\[
b=m\Lambda=m^{10/3}j^{2/3}.
\tag{33}
\]

It has

\[
\|w\|_{3,\infty}\asymp m,
\qquad
\|w\|_2^2\asymp\frac{m^2}{\Lambda}
=m^{-1/3}j^{-2/3}\longrightarrow0,
\tag{34}
\]

while its nonlinear acceleration at frequencies
\(\lesssim\Lambda\) has the scale

\[
\|\mathbb P\nabla\cdot(w\otimes w)\|_2
\asymp b^2\Lambda^{-1/2}
=m^2\Lambda^{3/2}.
\tag{35}
\]

It obeys (32) for \(\beta\le1/7\).  Thus the
\(\Lambda^{3/2}\) clock rate is sharp under the instantaneous norm and
local-energy inputs.  Both constructions are kinematic families of
different fields, not one Navier--Stokes evolution, and neither realizes
the signed increment (18).

## 6. Charge and residence audit

The new pointwise enstrophy floor does not itself yield an integrated
lower bound.  Multiplying its scale by the entire record gap gives only
the formal weight

\[
\Delta_j^{(L)}\Lambda_j^2
\asymp
R_j^{5/12}j^{1/3},
\tag{36}
\]

which is summable.  The layer cubic and cutoff scales are likewise

\[
\Delta_j^{(L)}
\int_{A_j}|u(t_j)|^3\,dx
\asymp
\frac{R_j^{5/4}}j,
\tag{37}
\]

\[
\Delta_j^{(L)}r_j^{-1}
\int_{A_j}|u(t_j)|^3\,dx
\asymp
R_j^{1/12}j^{-1/3},
\tag{38}
\]

and the viscous cutoff scale agrees with (36).  These are exponent
audits, not signed event lower bounds; every displayed weight is
geometrically summable.

In carrier coordinates, whose physical turnover time is
\(\tau_j\asymp m_j^{-5}\), the forced length is

\[
\ell_j^{\rm clk}:=\frac{r_j}{R_j}
\asymp m_j^{-1/3}j^{-2/3}.
\tag{39}
\]

A fixed high-pass floor implies a fixed heat-filter subgrid floor by a
scale comparable to \(\ell_j^{\rm clk}\), so a canonical first-crossing
scale can be chosen no larger than this.  If it is comparable to
\(\ell_j^{\rm clk}\), the existing residence theorem gives physical
backward residence

\[
\tau_j
\frac{\ell_j^{\rm clk}}
{\log(e+C/\ell_j^{\rm clk})}
\asymp
m_j^{-16/3}j^{-5/3}.
\tag{40}
\]

Relative to the record gap, (40) has ratio

\[
\asymp m_j^{1/6}j^{-2/3}\longrightarrow\infty.
\tag{41}
\]

The energy would then be prestored across the block.  This still does
not control phase, sign, or spatial alignment: (18) may recycle an old
ultraviolet reservoir rather than create fresh energy.  If the canonical
scale is much smaller than (39), even the comparison (41) is unavailable.

## 7. What changed and what remains

### Robust findings, subject to external review

1. The critical low-pass clock improves the energy-only
   \(\Lambda^{5/2}\) rate to \(m_j^2\Lambda^{3/2}\).
2. Finite-volume Lorentz capacity gives a fixed signed change against
   the future amplitude layer across a fixed record block.
3. Frequencies below
   \(\Lambda_j\asymp R_j^{-7/6}j^{2/3}\) cannot supply that change.
4. A fixed ultraviolet \(L^2\) floor and the enstrophy power
   \(R_j^{-7/3}j^{4/3}\) follow at one endpoint.
5. A Leray--Hopf continuation must lose a fixed amount of kinetic
   energy at the first singular time.
6. Static packet clouds and a vanishing-energy driver show that the
   spatial exponent and instantaneous clock rate are sharp under the
   inputs used.

### Things still to prove

1. Derive energy equality or strong left \(L^2\) continuity at \(T^*\)
   from the exact \(q=4\) schedule; or prove that its failure is
   incompatible with another NSE law.
2. Exclude repeated phase/spatial recycling of a prestored ultraviolet
   reservoir by a nonsummable signed, orthogonal, or fresh charge.
3. Control a canonical subgrid scale far below (39).
4. Control the divergent-normalised-energy branch.
5. Treat Type-II schedules at or below the temporal five-power barrier.
6. Prove one complete Clay alternative for arbitrary admissible data.

### Conjecture: no anomalous-loss \(q=4\) branch

No Leray--Hopf continuation of a smooth finite-energy solution through
its first singular time can simultaneously have the exact \(q=4\)
first-record schedule and a fixed-energy near-extremising weak-\(L^3\)
layer.

The corollary proves this conjecture conditional on energy equality at
the first singular time.  That condition is not proved here.  The Clay
problem remains unsolved.
