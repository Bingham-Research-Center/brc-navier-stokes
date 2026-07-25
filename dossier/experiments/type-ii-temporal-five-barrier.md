# The temporal weak-\(L^3\) five-power barrier excludes retained \(q=4\) carriers

- **Experiment:** EXP-TYPE-II-TEMPORAL-FIVE-BARRIER-001
- **Route:** ROUTE-R3C
- **Status:** complete conditional exclusion theorem; external review pending
- **Domain:** smooth finite-energy Navier--Stokes flow on \(\mathbb R^3\)
- **Clay status:** unsolved
- **Imported input:** Leslie--Shvydkoy's peer-reviewed energy-measure theorem

## Verdict

The retained partial/tight cell of the energy-efficient exact \(q=4\)
Type-II ledger is impossible.

The exact record schedule

\[
m_j\asymp 2^{2j},
\qquad
t_{j+1}-t_j\asymp \frac{2^{-11j}}j
\]

forces

\[
M(t):=\|u(t)\|_{L^{3,\infty}}
\in L^s(0,T^*)
\qquad\text{for every }s<\frac{11}{2}.
\]

Choose \(s=16/3\).  Interpolation with the energy-class bound
\(u\in L^2_tL^6_x\) gives

\[
u\in L^{256/53}_tL^{96/31}_x.
\]

These exponents lie strictly inside the Leslie--Shvydkoy
positive-energy-dimension region:

\[
\frac6p+\frac5q
=
\frac{761}{256}
<
3.
\]

Their theorem therefore gives the terminal local-energy bound

\[
\sup_{\substack{T^*-r^{72/29}<t<T^*\\x_0\in K}}
\int_{B_r(x_0)}|u(x,t)|^2\,dx
\le C_Kr^{1/29}
\]

for every fixed compact \(K\).

The retained geometry cell instead supplies centres \(x_j\), radii
\(R_j\asymp2^{-4j}\), and a fixed \(\gamma>0\) with

\[
\int_{B_{AR_j}(x_j)}|u(x,t_j)|^2\,dx\ge\gamma.
\]

Finite energy and finite total energy-flux action keep the centres in a
fixed compact set.  Moreover,

\[
\frac{T^*-t_j}{R_j^{72/29}}
\lesssim
\frac1j\,2^{-31j/29}
\longrightarrow0.
\]

The published local-energy bound applies at \(t_j\) with \(r=AR_j\) and
makes the displayed fixed floor tend to zero, a contradiction.

This closes the retained exact \(q=4\) cell.  It does not close the diffuse
energy-efficient cell, the divergent-normalised-energy branch, slower
record schedules at or below the temporal five-power threshold, or the
Clay problem.

## 1. Published input and source scope

Let

\[
\mathcal E
:=
\underset{t\uparrow T^*}{\operatorname{w^*\!-\!lim}}
|u(t)|^2\,dx
\]

be the terminal energy measure at a first possible blow-up time.
Leslie and Shvydkoy prove the following for a three-dimensional
Navier--Stokes solution regular before \(T^*\), with a Leray--Hopf weak
continuation through \(T^*\).

### Published energy-measure theorem

If

\[
u\in L^q_tL^p_x,
\qquad
3\le p<\infty,
\qquad
\frac6p+\frac5q\le3,
\]

then on every compact \(K\) the terminal energy measure has lower local
dimension at least

\[
\beta
:=
\frac{q}{q-1}
\left(
3-\frac6p-\frac5q
\right).
\]

Equivalently, their local estimate has the form

\[
\sup_{\substack{T^*-r^\alpha<t<T^*\\x_0\in K}}
\int_{B_r(x_0)}|u(x,t)|^2\,dx
\le C_Kr^\beta,
\qquad
\alpha
:=
\frac{q}{q-1}
\left(1+\frac3p\right).
\]

If the exponent inequality is strict, then \(\beta>0\), so
\(\mathcal E\) has no atoms.

The imported theorem is peer reviewed.  The interpolation, record-clock
conversion, tightness argument, and application to the repository's exact
\(q=4\) ledger are deductions made here and await external review.

The accepted source has an evident symbol typo in its viscous comparison:
it prints \(\beta>2\) where both the displayed Prodi--Serrin equivalence and
the comparison of \(r^{-2}\) with the time-cutoff power require
\(\alpha>2\).  Its following proposition states the Navier--Stokes
extension.  The explicit pair below has
\[
\frac3p+\frac2q=\frac{177}{128}>1,
\qquad
\alpha=\frac{72}{29}>2,
\]
so the corrected comparison is verified directly here.

## 2. Exact record clocks produce temporal weak-\(L^3\) integrability

Let \(t_j\uparrow T^*\) be first record times for

\[
m_j:=M(t_j)
=
\|u(t_j)\|_{L^{3,\infty}}.
\]

The first-record property gives

\[
M(t)\le m_{j+1}
\qquad
(t_j\le t\le t_{j+1}).
\]

### Lemma 1: clock-to-integrability conversion

Under the exact \(q=4\) schedule,

\[
M\in L^s(0,T^*)
\qquad
\text{for every }s<\frac{11}{2}.
\]

#### Proof

The solution is smooth on every compact subinterval of \([0,T^*)\), so
only the terminal tail matters.  On that tail,

\[
\begin{aligned}
\int_{t_J}^{T^*}M(t)^s\,dt
&\le
\sum_{j\ge J}
m_{j+1}^s(t_{j+1}-t_j)\\
&\lesssim
\sum_{j\ge J}
\frac{2^{(2s-11)j}}j.
\end{aligned}
\]

The series converges exactly when \(2s-11<0\).

At the endpoint \(s=11/2\), this estimate gives the harmonic series and
does not claim integrability.

## 3. Interpolation crosses the energy-dimension line

The finite-energy identity and Sobolev embedding give

\[
u\in L^\infty_tL^2_x\cap L^2_tL^6_x.
\]

The useful part here is \(u\in L^2_tL^6_x\).

### Lemma 2: weak-\(L^3\)/enstrophy interpolation

Assume

\[
M\in L^s_t,
\qquad
s>5.
\]

For \(0<\theta<1\), define

\[
\frac1p
=
\frac{1-\theta}{3}+\frac{\theta}{6},
\qquad
\frac1q
=
\frac{1-\theta}{s}+\frac{\theta}{2}.
\]

Then

\[
u\in L^q_tL^p_x
\]

and

\[
3-\frac6p-\frac5q
=
1-\frac5s
-
\theta\left(\frac32-\frac5s\right).
\]

In particular, because \(s>5\), sufficiently small positive \(\theta\)
makes the last quantity strictly positive.

#### Proof

Real interpolation between \(L^{3,\infty}\) and \(L^6\) gives

\[
\|u(t)\|_{L^p}
\le
C
M(t)^{1-\theta}
\|u(t)\|_{L^6}^{\theta}.
\]

Sobolev gives

\[
\|u(t)\|_{L^6}
\le C\|\nabla u(t)\|_2.
\]

Hölder in time, with the displayed definition of \(q\), yields

\[
\|u\|_{L^q_tL^p_x}
\le
C
\|M\|_{L^s_t}^{1-\theta}
\|\nabla u\|_{L^2_tL^2_x}^{\theta}.
\]

Since \(6/p=2-\theta\), direct substitution gives the final identity.

### Theorem 3: temporal five-power no-carrier barrier

Let \(u\) be a smooth finite-energy solution on
\(\mathbb R^3\times[0,T^*)\), where \(T^*\) is its first possible blow-up
time.  If

\[
\|u(t)\|_{L^{3,\infty}}
\in L^s(0,T^*)
\qquad\text{for some }s>5,
\]

then there are no sequences

\[
t_j\uparrow T^*,
\qquad
r_j\downarrow0,
\qquad
x_j\in\mathbb R^3
\]

and no \(\gamma>0\) such that

\[
\int_{B_{r_j}(x_j)}
|u(x,t_j)|^2\,dx
\ge\gamma
\]

for every \(j\).

#### Proof

Choose \(\theta>0\) small enough that Lemma 2 gives

\[
\frac6p+\frac5q<3.
\]

The published energy-measure theorem then gives positive local dimension,
so

\[
\mathcal E(\{x\})=0
\qquad
\text{for every }x\in\mathbb R^3.
\]

It remains only to rule out escape of the proposed centres to spatial
infinity.  This is done in the next lemma.  Once the centres are bounded,
take a subsequence \(x_j\to x_*\).  For every \(\rho>0\), the shrinking
carrier ball is eventually contained in \(\overline B_\rho(x_*)\).
Weak-star convergence of the energy measures and the closed-set
Portmanteau inequality give

\[
\mathcal E(\overline B_\rho(x_*))
\ge
\limsup_{j\to\infty}
\int_{\overline B_\rho(x_*)}|u(x,t_j)|^2\,dx
\ge\gamma.
\]

Letting \(\rho\downarrow0\) gives

\[
\mathcal E(\{x_*\})\ge\gamma,
\]

contradicting the no-atom conclusion.

The number \(5\) is the exact threshold for this interpolation route.  At
\(s=5\), the positive term \(1-5/s\) vanishes and every
\(\theta>0\) moves the exponent to the wrong side.

## 4. Uniform spatial tightness

### Lemma 4: finite-energy trajectories cannot lose a fixed carrier at infinity

For a smooth finite-energy solution on a finite interval,

\[
\lim_{R\to\infty}
\sup_{0\le t<T^*}
\int_{|x|>R}|u(x,t)|^2\,dx
=0.
\]

#### Proof

Choose the whole-space pressure representative

\[
p=\mathcal R_a\mathcal R_b(u_au_b).
\]

Energy interpolation and the Riesz-transform bound imply

\[
\mathcal F_*
:=
\int_0^{T^*}\!\!\int_{\mathbb R^3}
\left(|u|^3+|p||u|\right)\,dx\,dt
<\infty.
\]

Let \(0\le\psi_R\le1\) vanish on \(B_R\), equal one outside \(B_{2R}\),
and satisfy

\[
\|\nabla\psi_R\|_\infty\lesssim R^{-1},
\qquad
\|\Delta\psi_R\|_\infty\lesssim R^{-2}.
\]

Approximate this exterior cutoff by compactly supported cutoffs and pass to
the limit using finite energy and \(\mathcal F_*<\infty\).  The local energy
equality, with the nonnegative local dissipation dropped, gives

\[
\begin{aligned}
\sup_{t<T^*}
\int_{|x|>2R}|u(x,t)|^2\,dx
\lesssim{}&
\int_{|x|>R}|u_0(x)|^2\,dx\\
&+\frac{\mathcal F_*}{R}
+\frac{\nu T^*}{R^2}
\sup_{t<T^*}\|u(t)\|_2^2.
\end{aligned}
\]

Every term tends to zero with \(R\).

Consequently, a family of balls carrying one fixed positive energy amount
has bounded centres once their radii tend to zero.

## 5. Explicit \(q=4\) exclusion

Take

\[
s=\frac{16}{3},
\qquad
\theta=\frac1{16}.
\]

Lemma 2 gives

\[
\frac1p=\frac{31}{96},
\qquad
\frac1q=\frac{53}{256},
\]

or

\[
p=\frac{96}{31},
\qquad
q=\frac{256}{53}.
\]

The published admissibility gap is

\[
3-\frac6p-\frac5q
=
\frac7{256}>0.
\]

The corresponding local-dimension and time-window exponents are

\[
\boxed{
\beta
=
\frac{q}{q-1}
\left(3-\frac6p-\frac5q\right)
=
\frac1{29},
}
\]

\[
\boxed{
\alpha
=
\frac{q}{q-1}
\left(1+\frac3p\right)
=
\frac{72}{29}.
}
\]

Thus for every compact \(K\),

\[
\sup_{\substack{T^*-r^{72/29}<t<T^*\\x_0\in K}}
\int_{B_r(x_0)}|u(x,t)|^2\,dx
\le
C_Kr^{1/29}.
\]

For the exact record schedule,

\[
T^*-t_j
\lesssim
\frac{2^{-11j}}j,
\qquad
R_j\asymp2^{-4j}.
\]

Therefore

\[
\frac{T^*-t_j}{R_j^{72/29}}
\lesssim
\frac1j
2^{-\left(11-\frac{288}{29}\right)j}
=
\frac1j2^{-31j/29}
\longrightarrow0.
\]

The retained geometry floor at radius \(AR_j\) lies inside the theorem's
terminal window, while

\[
C_K(AR_j)^{1/29}\longrightarrow0.
\]

This contradicts its fixed lower bound \(\gamma\).

### Corollary 5: retained exact \(q=4\) cell is empty

No smooth finite-energy trajectory can realise simultaneously:

1. the original exact \(q=4\) first-record schedule;
2. the energy-efficient layer \(e_j\ge c_0>0\);
3. a partial or tight geometry subsequence with a fixed local energy floor.

Hence an actual energy-efficient exact \(q=4\) survivor must be in the
diffuse selected-layer cell.

The earlier terminal-infrared and multirecord-import theorems remain valid
conditional statements.  This theorem proves that their retained exact
\(q=4\) premises cannot all occur on a smooth trajectory.

## 6. Optimised terminal-dimension consequence

The explicit pair above is enough for contradiction.  The full exact clock
gives a sharper limiting statement.

For every

\[
5<s<\frac{11}{2},
\]

let \(\theta\downarrow0\) in Lemma 2.  The Leslie--Shvydkoy lower
local-dimension exponent tends to

\[
\frac{s-5}{s-1}.
\]

For sufficiently small \(\theta\), one has \(3<p<q\),
\(1/p+1/q>1/2\), and \(6/p+5/q<3\), so the pair lies in their Region II.
The refined concentration-dimension bound then tends to

\[
\frac{3(s-5)}{s-3}.
\]

Finally let \(s\uparrow11/2\).  The exact \(q=4\) terminal energy measure
therefore satisfies

\[
\boxed{
d(x,\mathcal E)\ge\frac19
\quad\text{for every }x,
\qquad
D(\mathcal E)\ge\frac35.
}
\]

These dimension bounds are additional quantitative consequences of the
published theorem and the exact clock.  The no-atom part alone closes the
retained cell.

## 7. Route disposition

### Closed

- Every retained partial/tight energy-efficient exact \(q=4\) carrier cell.
- More generally, every fixed-energy shrinking-carrier sequence on a branch
  with \(M\in L^s_tL^{3,\infty}_x\) for some \(s>5\).
- The proposed need to defeat repeated reuse of imported energy inside the
  exact \(q=4\) retained cell: that cell is empty before genealogy is needed.

### Still open

- The diffuse energy-efficient selected-layer cell.
- The divergent-normalised-energy branch.
- Other Type-II schedules that fail \(L^s_tL^{3,\infty}_x\) for every
  \(s>5\), including the temporal five-power endpoint.
- Regularity, breakdown, and all Clay alternatives A--D.

The next bounded problem is to quantify fragmentation in the diffuse
selected layer: fixed energy occupies total volume \(R_j^3\), but every
radius-\(R_j\) carrier ball captures a vanishing fraction.  The desired
output is a nonsummable interface, enstrophy, or pressure-transport charge,
or a recentering theorem that returns the layer to the now-excluded retained
cell.
