# Frequency freshness without a scale-zero floor is insufficient

- **Experiment:** EXP-ADJOINT-PRESSURE-FRESHNESS-WITHOUT-FLOOR-001
- **Route:** ROUTE-R3B
- **Status:** conditional same-trajectory summation theorem and sharp route
  obstruction
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** [lower-band decrement](adjoint-pressure-flux-decrement.md),
  [defect-event suspension](defect-event-suspension.md), and
  [parabolic tail ancestry](adjoint-pressure-parabolic-ancestry.md)
- **Same-system review:** accepted after scope clarifications; this is not
  independent external review
- **External review:** pending

The lower-band theorem left interval and frequency overlap as a possible
reason why infinitely many event charges need not fit one finite dissipation
budget.  Frequency overlap is not the decisive obstruction.

For every late event, that theorem gives

\[
\int_{\widetilde J_j}
\left\|
\nabla Q_{\eta K_j<|\xi|\le K_j}v(t)
\right\|_2^2\,dt
\ge
c_*\frac{\nu^2}{M^2}T_j,
\qquad
K_j\longrightarrow\infty.
\tag{1}
\]

An infinite subsequence of the annuli in (1) can always be made pairwise
disjoint.  Plancherel then sums its charges even if all time intervals
overlap:

\[
\boxed{
\sum_m T_{j_m}
\le
\frac{M^2}{c_*\nu^2}
\int_{t_{\rm w}}^{T^*}\|\nabla v(t)\|_2^2\,dt
<\infty.
}
\tag{2}
\]

If one additionally grants the still-unproved coupling which identifies
each pressure boundary with the next defect-event scale, the full retained
gap-separated event family has uniformly bounded frequency multiplicity, and
the same estimate holds with \(\sum_j\) in place of \(\sum_m\).

This does not produce a contradiction.  The exact power-law ancestry
survivor already has next-event matching, eventually disjoint comparable
bands, and

\[
T_j\asymp h_j^{q-3},
\qquad q>3,
\qquad
\sum_jT_j<\infty.
\tag{3}
\]

Thus bounded overlap converts the lower-band theorem into a finite physical
sum, but no existing event law says that sum must diverge.  The live missing
theorem is a nonsummable scale-zero floor, or an equivalent rigidity law,
not frequency freshness by itself.

## 1. The sparse same-trajectory summation theorem

Let \(v\) be the conditional smooth finite-energy trajectory on
\((t_{\rm w},T^*)\), with

\[
\operatorname*{ess\,sup}_{t_{\rm w}<t<T^*}
\|v(t)\|_{L^{3,\infty}}\le M
\tag{4}
\]

and

\[
\mathcal D_*:=
\int_{t_{\rm w}}^{T^*}\|\nabla v(t)\|_2^2\,dt<\infty.
\tag{5}
\]

Retain the fixed \(0<\eta<1\), the terminal intervals
\(\widetilde J_j\subset(t_{\rm w},T^*)\), and (1) from the lower-band
decrement theorem.  Since \(K_j\to\infty\), recursively choose

\[
j_1<j_2<\cdots
\quad\text{so that}\quad
\eta K_{j_{m+1}}>K_{j_m}.
\tag{6}
\]

The sharp annuli

\[
\mathcal A_m:=
\{\xi:\eta K_{j_m}<|\xi|\le K_{j_m}\}
\tag{7}
\]

are pairwise disjoint.  For almost every time, Plancherel gives

\[
\sum_m
\left\|
\nabla Q_{\mathcal A_m}v(t)
\right\|_2^2
\le
\|\nabla v(t)\|_2^2.
\tag{8}
\]

Time overlap is harmless because
\(\mathbf1_{\widetilde J_{j_m}}\le1\).  Tonelli, (8), and (1) yield

\[
\begin{aligned}
c_*\frac{\nu^2}{M^2}\sum_mT_{j_m}
&\le
\sum_m
\int_{\widetilde J_{j_m}}
\|\nabla Q_{\mathcal A_m}v(t)\|_2^2\,dt
\\
&\le
\int_{t_{\rm w}}^{T^*}
\sum_m
\|\nabla Q_{\mathcal A_m}v(t)\|_2^2\,dt
\\
&\le\mathcal D_*.
\end{aligned}
\tag{9}
\]

This proves (2).  It is an actual same-trajectory consequence within the
conditional R3B genealogy.  It uses neither disjoint event times nor a
selected event inside a last-hitting interval.

The conclusion also explains its own limitation.  Any positive sequence
tending to zero has a summable subsequence, so sparse freshness alone cannot
turn infinite event count into a contradiction.

## 2. What full retained gap-separated next-event coupling would buy

The defect-event theorem gives logarithmic event roots
\(\theta_j\) with

\[
\theta_{j+1}-\theta_j\ge d_0,
\qquad d_0=1
\tag{10}
\]

after thinning.  Write their physical scale factors as

\[
\sigma_j=e^{-\theta_j}.
\tag{11}
\]

To test the strongest direct coupling, assume that the pressure boundary at
event \(j\) is uniformly comparable with the next event frequency:

\[
\boxed{
\frac{c_-}{\sigma_{j+1}}
\le K_j\le
\frac{c_+}{\sigma_{j+1}}
}
\tag{12}
\]

for fixed \(0<c_-\le c_+<\infty\).  This would follow from exact next-event
matching together with the already proved \(K_j/\Lambda_j\to1\), but (12)
itself is not proved by the current genealogy.

If \(l=j+m\), then (10)--(12) imply

\[
\frac{K_l}{K_j}
\ge
\frac{c_-}{c_+}e^{md_0}.
\tag{13}
\]

If one frequency belongs to both
\((\eta K_j,K_j]\) and \((\eta K_l,K_l]\), their upper cutoffs differ by
less than \(1/\eta\).  Equations (12)--(13) therefore bound the number of
annuli containing any fixed frequency by

\[
\boxed{
N_\eta
:=
1+
\left\lceil
\frac1{d_0}
\log\frac{c_+}{\eta c_-}
\right\rceil.
}
\tag{14}
\]

Consequently,

\[
\sum_j
\left\|
\nabla Q_{\eta K_j<|\xi|\le K_j}v(t)
\right\|_2^2
\le
N_\eta\|\nabla v(t)\|_2^2
\tag{15}
\]

for almost every \(t\).  The same Tonelli argument proves

\[
\boxed{
\sum_jT_j
\le
\frac{N_\eta M^2}{c_*\nu^2}\mathcal D_*.
}
\tag{16}
\]

Thus even the hoped-for event-to-next-frequency identification would solve
the multiplicity bookkeeping completely.  Its reward is summability of the
shrinking physical floors, not finite event count.

## 3. Exact ancestry permits the summable conclusion

The power-law survivor in the parabolic-ancestry theorem fixes
\(q>3\), \(\kappa\ge1\), and \(0<h_1<1\), and defines

\[
\begin{aligned}
h_{j+1}
&=
\kappa^{-1/q}h_j^{\,1+1/(2q)},\\
\sigma_j&=h_j^q,\\
\Lambda_j&=\frac1{\sigma_{j+1}},\\
T_j&=C_T\sigma_jh_j^{-3}
=C_Th_j^{q-3}.
\end{aligned}
\tag{17}
\]

Put \(y_j=\log(1/h_j)\).  Then

\[
y_{j+1}
=
\left(1+\frac1{2q}\right)y_j
+\frac1q\log\kappa,
\tag{18}
\]

so \(y_j\) grows geometrically.  Therefore

\[
\boxed{
\sum_jT_j
=
C_T\sum_j
\exp\bigl(-(q-3)y_j\bigr)
<\infty.
}
\tag{19}
\]

Moreover,

\[
\log\frac{\sigma_j}{\sigma_{j+1}}
=
q(y_{j+1}-y_j)
\longrightarrow\infty.
\tag{20}
\]

Hence the event gaps exceed (10), exact next-event matching holds, and the
annuli around \(K_j\sim\Lambda_j\) are eventually pairwise disjoint.  The
sequence is stronger than the multiplicity hypothesis used in (16).

The existing kinematic realisation of (17) is not an NSE solution and does
not realise the lower-band flux theorem.  It is used here only for the exact
logical comparison: the physical amounts demanded by (1) can be
proportional to the summable sequence (19), so finite dissipation and
frequency freshness do not contradict the quantified lower bounds.  A
geometrically or super-geometrically decaying flux chain is likewise
compatible with a fixed fractional decrement.

## 4. Route consequence

This experiment closes bounded frequency overlap as a standalone R3B
solution:

1. sparse frequency freshness follows unconditionally from
   \(K_j\to\infty\);
2. time overlap cannot spoil the corresponding Plancherel sum;
3. full bounded multiplicity would follow from the strongest natural
   next-event scale identification;
4. both forms yield only summability of \(T_j\); and
5. the exact ancestry survivor permits that summability with room to spare.

It does not prove the coupling (12), an event floor, exclusion of the
conditional ancient profile, regularity, breakdown, or any Clay alternative
A--D.

The pressure/freshness subbranch now needs at least one genuinely new
NSE-specific theorem of a stronger type:

1. \(\sum_jT_j=\infty\) or a fixed positive floor on an infinite fresh
   subsequence;
2. a conversion of the fixed normalised Besov/adjoint-pressure event cost
   into a nonsummable unnormalised physical charge;
3. a rigidity theorem excluding an infinite decaying signed-flux cascade
   even when its total dissipation is finite; or
4. a pressure-visible event-index telescope with a fixed increment not
   proportional to \(T_j\).

No executable certificate is claimed: the proof consists of Plancherel,
Tonelli, the exact event-scale algebra, and the already recorded
power-survivor recurrence.
