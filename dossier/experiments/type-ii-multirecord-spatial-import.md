# Fast retained Type-II cores force multirecord spatial import

- **Experiment:** EXP-TYPE-II-MULTIRECORD-SPATIAL-IMPORT-001
- **Route:** ROUTE-R3C
- **Status:** complete conditional theorem; external review pending
- **Domain:** smooth finite-energy Navier--Stokes flow on \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** [carrier entrance](type-ii-inviscid-carrier-entrance.md) and
  [terminal infrared evacuation](type-ii-terminal-infrared-evacuation.md)

## Verdict

The retained exact \(q=4\) survivor cannot hide each future carrier core as
arbitrarily old energy already stored in the same tiny physical ball.

For the record \(t_j\), look backwards to

\[
i_j:=j-\left\lfloor\frac j4\right\rfloor.
\]

This crosses an unbounded number of first records.  At the earlier time
\(t_{i_j}\), the first-record weak-\(L^3\) ceiling implies

\[
\int_{B_{(A+1)R_j}(x_j)}
|u(x,t_{i_j})|^2\,dx
\lesssim
\left(\frac{m_{i_j}}{m_j}\right)^2
\longrightarrow0.
\]

At \(t_j\), the retained amplitude layer supplies a fixed energy amount in
\(B_{AR_j}(x_j)\).  The viscous cutoff correction between the two times is
also \(o(1)\):

\[
\nu\frac{t_j-t_{i_j}}{R_j^2}
\longrightarrow0.
\]

The exact local kinetic-energy equality therefore forces

\[
\boxed{
\liminf_{j\to\infty}
\int_{t_{i_j}}^{t_j}\!\!\int_{\mathbb R^3}
\left(\frac12|u|^2+p\right)
u\cdot\nabla\chi_j\,dx\,dt
>0,
}
\]

where

\[
\chi_j(x):=\chi\!\left(\frac{x-x_j}{R_j}\right),
\]

\(\chi=1\) on \(B_A\), and \(\chi\) is supported in \(B_{A+1}\).
With the sign convention of the local energy identity, this is a fixed net
weighted pressure-plus-kinetic energy import through the future carrier
annulus.

The previous terminal-infrared theorem says that the retained endpoint core
is ultraviolet.  The present theorem separately says that a fixed total
energy amount entered the future carrier ball across an interval spanning a
linear number of earlier records.  It does not identify the imported amount
with the Fourier-detected packet or prove packet freshness.  Thus the fast
retained branch is no longer allowed to choose pure local prestorage.

A subsequence of these multirecord intervals is pairwise disjoint, so one
trajectory has infinitely many fixed import events.  This is not yet a Clay
contradiction: different shrinking moving cutoffs have no known common
finite unweighted flux budget, and one packet can cross a nested sequence
of boundaries.

## 1. First-record carriers and retained energy

Let \(u\) be a smooth divergence-free solution of

\[
\partial_tu+u\cdot\nabla u=-\nabla p+\nu\Delta u,
\qquad
\nabla\cdot u=0
\]

on \(\mathbb R^3\times[0,T^*)\), with

\[
\sup_{t<T^*}\frac12\|u(t)\|_2^2\le E_0.
\]

Let

\[
t_j\uparrow T^*
\]

be first record times for

\[
m_j:=\|u(t_j)\|_{L^{3,\infty}}.
\]

Thus

\[
\|u(t)\|_{L^{3,\infty}}\le m_j
\qquad(0\le t\le t_j).
\]

Choose a near-extremising amplitude layer

\[
A_j:=\{a_j<|u(t_j)|\le2a_j\},
\]

with layer energy and volume radius

\[
e_j:=\int_{A_j}|u(t_j)|^2\,dx,
\qquad
R_j:=|A_j|^{1/3}.
\]

In the energy-efficient branch,

\[
0<c_0\le e_j\le2E_0
\]

and the layer theorem gives

\[
R_j\asymp\frac{e_j}{m_j^2}.
\]

In a partial or tight geometry cell, fix \(0<\eta<\theta\).  After selecting
centres \(x_j\), there are \(A<\infty\) and

\[
\gamma:=\eta c_0>0
\]

such that

\[
\boxed{
\int_{B_{AR_j}(x_j)}
|u(x,t_j)|^2\,dx
\ge\gamma
}
\]

eventually.

The terminal-infrared theorem adds that this retained endpoint energy is
detected at frequencies above \(K_j/R_j\) for some \(K_j\to\infty\).  The
proof below needs only the boxed local energy floor; the ultraviolet
conclusion controls its interpretation.

## 2. Weak-\(L^3\) capacity of a future carrier ball

### Lemma 1: finite-volume Lorentz capacity

For every measurable set \(\Omega\subset\mathbb R^3\) of finite volume and
every \(f\in L^{3,\infty}\),

\[
\boxed{
\int_\Omega|f|^2\,dx
\le
C|\Omega|^{1/3}
\|f\|_{L^{3,\infty}}^2.
}
\]

#### Proof

The finite-measure Lorentz embedding

\[
L^{3,\infty}(\Omega)\hookrightarrow L^2(\Omega)
\]

gives

\[
\|f\|_{L^2(\Omega)}
\le
C|\Omega|^{1/6}
\|f\|_{L^{3,\infty}}.
\]

Squaring proves the claim.

Choose any earlier indices \(i_j<j\) for which

\[
\boxed{
\frac{m_{i_j}}{m_j}\longrightarrow0.
}
\]

At time \(t_{i_j}\), Lemma 1 and the first-record property give

\[
\begin{aligned}
&\int_{B_{(A+1)R_j}(x_j)}
|u(x,t_{i_j})|^2\,dx\\
&\qquad\le
C_AR_jm_{i_j}^2\\
&\qquad\le
C_AE_0
\left(\frac{m_{i_j}}{m_j}\right)^2
\longrightarrow0.
\end{aligned}
\]

The estimate is uniform in the future centres \(x_j\).  It says more than
weak convergence: the complete kinetic energy inside the future carrier
ball vanishes at the earlier record.

## 3. Exact local kinetic-energy balance

Choose

\[
0\le\chi\in C_c^\infty(\mathbb R^3),
\qquad
\chi=1\ \hbox{on }B_A,
\qquad
\operatorname{supp}\chi\subset B_{A+1},
\]

with \(\chi\) radial and nonincreasing in radius, and set

\[
\chi_j(x):=
\chi\left(\frac{x-x_j}{R_j}\right).
\]

Define the local kinetic energy

\[
\mathcal E_j(t)
:=
\frac12\int_{\mathbb R^3}
\chi_j(x)|u(x,t)|^2\,dx.
\]

The smooth local energy equality is

\[
\partial_t\frac{|u|^2}{2}
+
\nabla\cdot
\left[
\left(\frac{|u|^2}{2}+p\right)u
\right]
=
\nu\Delta\frac{|u|^2}{2}
-\nu|\nabla u|^2.
\]

Multiplication by \(\chi_j\) and integration on
\([t_{i_j},t_j]\times\mathbb R^3\) give

\[
\boxed{
\mathcal E_j(t_j)-\mathcal E_j(t_{i_j})
=
\mathsf X_j-\mathsf D_j+\mathsf C_j,
}
\]

where

\[
\mathsf X_j
:=
\int_{t_{i_j}}^{t_j}\!\!\int
\left(\frac12|u|^2+p\right)
u\cdot\nabla\chi_j\,dx\,dt,
\]

\[
\mathsf D_j
:=
\nu
\int_{t_{i_j}}^{t_j}\!\!\int
\chi_j|\nabla u|^2\,dx\,dt
\ge0,
\]

and

\[
\mathsf C_j
:=
\frac{\nu}{2}
\int_{t_{i_j}}^{t_j}\!\!\int
|u|^2\Delta\chi_j\,dx\,dt.
\]

The pressure gauge does not affect \(\mathsf X_j\), since

\[
\int u\cdot\nabla\chi_j\,dx=0.
\]

With this sign convention, positive \(\mathsf X_j\) is net kinetic-energy
import through the carrier annulus supporting \(\nabla\chi_j\).

## 4. The only unsigned error is negligible

Because

\[
\|\Delta\chi_j\|_\infty
=
R_j^{-2}\|\Delta\chi\|_\infty
\]

and the global energy is bounded,

\[
\boxed{
|\mathsf C_j|
\le
C_{\chi,E_0}\,
\nu\frac{t_j-t_{i_j}}{R_j^2}.
}
\]

Thus the exact abstract separation needed below is

\[
\boxed{
\frac{m_{i_j}}{m_j}\longrightarrow0,
\qquad
\nu\frac{t_j-t_{i_j}}{R_j^2}\longrightarrow0.
}
\]

No estimate of the pressure flux and no absolute value of
\(\mathsf X_j\) is used.  The nonnegative viscous loss
\(\mathsf D_j\) strengthens, rather than weakens, the required import.

## 5. Forced multirecord spatial import

### Theorem 2: retained-core import

Assume the energy-efficient retained layer floor from Section 1 and the two
separations from Section 4.  Then

\[
\boxed{
\liminf_{j\to\infty}\mathsf X_j
\ge\frac{\gamma}{2}>0.
}
\]

In particular, for all sufficiently large \(j\),

\[
\mathsf X_j\ge\frac{\gamma}{4}.
\]

#### Proof

Because \(\chi_j=1\) on the retained ball,

\[
\mathcal E_j(t_j)\ge\frac{\gamma}{2}.
\]

Lemma 1 and \(m_{i_j}/m_j\to0\) give

\[
\mathcal E_j(t_{i_j})\longrightarrow0.
\]

The cutoff estimate and the second separation give

\[
\mathsf C_j\longrightarrow0.
\]

Rearranging the exact local energy identity,

\[
\mathsf X_j
=
\mathcal E_j(t_j)-\mathcal E_j(t_{i_j})
+\mathsf D_j-\mathsf C_j.
\]

Since \(\mathsf D_j\ge0\), taking the lower limit proves the claim.

The conclusion is a physical energy floor with no carrier normalisation
left to undo.

## 6. Exact \(q=4\) audit

The representative ledger has, up to fixed comparison constants,

\[
m_j\asymp2^{2j},
\qquad
R_j\asymp2^{-4j},
\]

\[
t_{j+1}-t_j
\asymp
\frac{2^{-11j}}j.
\]

Choose

\[
N_j:=\left\lfloor\frac j4\right\rfloor,
\qquad
i_j:=j-N_j.
\]

Then

\[
j-i_j=N_j\longrightarrow\infty
\]

and

\[
\frac{m_{i_j}}{m_j}
\asymp
2^{-2N_j}
\longrightarrow0.
\]

The geometric gap sum gives

\[
t_j-t_{i_j}
\le
C\frac{2^{-11i_j}}{i_j}.
\]

Since \(R_j^2\asymp2^{-8j}\),

\[
\begin{aligned}
\nu\frac{t_j-t_{i_j}}{R_j^2}
&\le
\frac{C\nu}{i_j}
2^{-11(j-N_j)+8j}\\
&=
\frac{C\nu}{i_j}
2^{-3j+11N_j}\\
&\le
\frac{C\nu}{j}
2^{-j/4}
\longrightarrow0.
\end{aligned}
\]

Here \(j\) remains the original \(q=4\) record-grid index.  A partial or
tight geometry subsequence is retained as an infinite subset of that grid
and is not renumbered.  Theorem 2 applies at every sufficiently late
retained index of any smooth trajectory realising the exact survivor.

More generally, any fixed

\[
0<\alpha\le\frac3{11}
\]

works with

\[
i_j=j-\lfloor\alpha j\rfloor.
\]

The number of crossed records is linear in \(j\), while the earlier ball
capacity and viscous cutoff correction both vanish.  At the endpoint
\(\alpha=3/11\), the exponential factor is bounded and the remaining
\(1/i_j\) factor tends to zero.

## 7. Disjoint fixed import events

For the choice \(i_j=j-\lfloor j/4\rfloor\), one has

\[
i_j\longrightarrow\infty.
\]

Choose \(j_n\) recursively so that

\[
i_{j_{n+1}}>j_n.
\]

Then the intervals

\[
[t_{i_{j_n}},t_{j_n}]
\]

are pairwise disjoint.  Every sufficiently late interval satisfies

\[
\boxed{
\int_{t_{i_{j_n}}}^{t_{j_n}}\!\!\int
\left(\frac12|u|^2+p\right)
u\cdot\nabla\chi_{j_n}\,dx\,dt
\ge\frac{\gamma}{4}.
}
\]

Consequently the numerical sum of these signed event totals diverges:

\[
\sum_n\mathsf X_{j_n}=+\infty.
\]

This is a same-trajectory nonsummable event ledger, but it is not yet a
nonsummable charge against a known finite quantity.  Each term uses a
different moving, shrinking cutoff.  The same energy can therefore be
counted repeatedly as it enters nested carrier balls.

## 8. The available common flux budget is scale-weighted

Choose the whole-space pressure representative

\[
p=\mathcal R_a\mathcal R_b(u_au_b).
\]

Sobolev interpolation gives

\[
\|u(t)\|_3^3
\le
C\|u(t)\|_2^{3/2}
\|\nabla u(t)\|_2^{3/2}.
\]

The energy equality and Hölder in time therefore imply

\[
\int_0^{T^*}\|u(t)\|_3^3\,dt<\infty.
\]

The Riesz-transform estimate

\[
\|p(t)\|_{3/2}\le C\|u(t)\|_3^2
\]

also gives

\[
\boxed{
\mathcal F_*:=
\int_0^{T^*}\!\!\int_{\mathbb R^3}
\left(
|u|^3+|p||u|
\right)\,dx\,dt
<\infty.
}
\]

Since

\[
\|\nabla\chi_j\|_\infty\le\frac{C_\chi}{R_j},
\]

the disjoint event intervals satisfy the genuine common budget

\[
\boxed{
\sum_n
R_{j_n}|\mathsf X_{j_n}|
\le
C_\chi\mathcal F_*.
}
\]

This does not contradict the fixed unweighted floors because

\[
\sum_nR_{j_n}<\infty.
\]

Thus the direct energy-class estimate introduces one carrier-radius weight.
Closing the retained branch requires a scale-free non-reuse law or a
genealogical mechanism that prevents the same \(L^1\) flux from being
amplified by successively steeper cutoffs.

## 9. What changed and what remains

Subject to external review, this round proves:

1. the future \(R_j\)-ball is asymptotically empty at a record a linear
   number of generations earlier;
2. the retained endpoint contains a fixed physical energy amount;
3. viscous diffusion through the carrier cutoff is negligible across that
   multirecord window;
4. a fixed positive signed pressure-plus-kinetic energy import through the
   future carrier boundary is compulsory;
5. the endpoint energy is ultraviolet by the preceding terminal-infrared
   theorem; and
6. infinitely many fixed import events can be placed on pairwise disjoint
   intervals of one trajectory; while
7. the common \(L^1\) energy-flux budget controls only the summably weighted
   quantities \(R_j|\mathsf X_j|\).

It does not prove:

1. that imports through different moving cutoffs draw on fresh energy;
2. removal of the summable carrier-radius weight from the finite global
   pressure-plus-kinetic transport action;
3. control of centre motion or spatial nesting between successive carriers;
4. a residence cost after energy crosses a carrier boundary;
5. exclusion of the diffuse or divergent-normalised-energy branches; or
6. regularity, breakdown, or any Clay alternative A--D.

The exact next question is:

> Can repeated positive imports through shrinking moving carrier boundaries
> be assigned finite crossing multiplicity along energy-transport paths, or
> can carrier genealogy remove the summable \(R_j\) weight from the finite
> pressure-plus-kinetic transport action?

No executable artefact is added.  The result is an analytic consequence of
finite-volume Lorentz capacity, the exact local energy identity, and the
exact \(q=4\) powers.
