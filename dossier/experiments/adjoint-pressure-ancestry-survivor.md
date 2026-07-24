# Exact next-event ancestry still permits the terminal-return tail charge

- **Experiment:** EXP-ADJOINT-PRESSURE-ANCESTRY-SURVIVOR-001
- **Route:** ROUTE-R3B
- **Status:** analytic scalar time--frequency ledger counterexample;
  [adversarially recomputed valid in scope](../review-ledger.md);
  not a Navier--Stokes construction
- **Domain:** one nested terminal dissipation history with an exact
  event-scale/frequency genealogy
- **Clay status:** unsolved
- **Inputs:** adversarially recomputed
  [stretched-history ledger theorem](adjoint-pressure-stretched-history.md),
  [causal interaction-depth theorem](adjoint-pressure-divergent-interaction-depth.md),
  and [terminal-return theorem](adjoint-pressure-terminal-return.md)

The terminal-return theorem gives a genuinely new same-trajectory
constraint.  If the zero-data terminal remainder returns fixed low-band
pressure after reaching normalised frequency \(L\), its physical
high-frequency dissipation charge is at least

\[
A\sigma L^2h^{-3}
\tag{1}
\]

for one fixed \(A>0\).  Finite physical spacetime enstrophy therefore
requires

\[
\sigma_jL_j^2h_j^{-3}\longrightarrow0.
\tag{2}
\]

At the reviewed logarithmic causal depth,

\[
N(h)=\left\lfloor c_{\rm dep}\log\frac1h\right\rfloor,
\qquad
L(h)=2^{N(h)}
\asymp h^{-\alpha_{\rm dep}},
\qquad
\alpha_{\rm dep}:=c_{\rm dep}\log2.
\tag{3}
\]

The interaction-depth theorem itself does **not** prove one dyadic upward
frequency move at every interaction.  This note grants that additional
Zeno-frequency interpretation and asks the strongest elementary
ancestry question:

> Does (2) become contradictory if the current top physical frequency is
> exactly the reciprocal of the next selected event scale?

The answer is no at the scalar time--frequency ledger level.

## 1. Exact ancestry-survivor theorem

Fix

\[
p:=\frac74,\qquad
c>0,\qquad
a>1,\qquad
c_{\rm dep}>0,\qquad
A>0.
\tag{4}
\]

Write

\[
\begin{aligned}
x(h)&:=h^{-p},\\
D(h)&:=h^{-3}e^{cx(h)},\\
\sigma(h)&:=h^3e^{-acx(h)},\\
\rho(h)&:=\sigma(h)D(h)
=e^{-(a-1)cx(h)},\\
\delta(h)&:=\sigma(h)^2h.
\end{aligned}
\tag{5}
\]

There is a strictly decreasing sequence \(h_j\downarrow0\), beginning
arbitrarily far down the genealogy, for which

\[
\boxed{
\sigma_{j+1}
=\frac{\sigma_j}{L_j},
\qquad
L_j:=L(h_j).
}
\tag{6}
\]

Consequently the normalised top frequency \(L_j\) is exactly the next
event's physical reciprocal scale:

\[
\boxed{
\frac{L_j}{\sigma_j}
=\frac1{\sigma_{j+1}}.
}
\tag{7}
\]

Despite (6)--(7), the terminal-return charge

\[
\tau_j
:=
A\sigma_jL_j^2h_j^{-3}
=Ae^{-acx_j}L_j^2
\tag{8}
\]

satisfies

\[
\boxed{
\tau_j\longrightarrow0,
\qquad
\frac{\tau_j}{\rho_j}
=Ae^{-cx_j}L_j^2
\longrightarrow0.
}
\tag{9}
\]

After starting sufficiently late, there is one finite nonnegative Borel
measure

\[
\mu\quad\hbox{on}\quad
(0,\delta_1)\times[0,\infty)
\tag{10}
\]

whose time marginal has an \(L^1\) density and which simultaneously
obeys

\[
\boxed{
\begin{aligned}
\mu\bigl((0,\delta_j)\times[0,\infty)\bigr)
&=\rho_j
=\sigma_jD(h_j),\\
\mu\bigl((0,\delta_j)\times
[L_j/\sigma_j,\infty)\bigr)
&=\tau_j
=A\sigma_jL_j^2h_j^{-3}
\end{aligned}}
\tag{11}
\]

for every \(j\).  Thus one finite nested history can pay the full
stretched-exponential coefficient floor, the quadratic terminal-return
tail toll, and the exact next-event frequency ancestry at every selected
event.

This is a theorem about compatibility of the remaining nonnegative
ledgers.  It is not a coefficient field, an Oseen solution, a suitable
solution, or a Navier--Stokes singularity.

## 2. Construction of the exact event genealogy

In the stretched coordinate \(x=h^{-p}\),

\[
\log\sigma(x)
=-\frac3p\log x-acx
\tag{12}
\]

is continuous and strictly decreasing from a finite value to
\(-\infty\).  Given \(x_j\), define \(x_{j+1}>x_j\) as the unique
solution of

\[
\boxed{
ac(x_{j+1}-x_j)
+\frac3p\log\frac{x_{j+1}}{x_j}
=N(h_j)\log2.
}
\tag{13}
\]

Equation (13) is exactly (6).  Its left-hand side is continuous,
strictly increasing from zero to infinity as \(x_{j+1}\) increases.
Thus the next node exists and is unique.

Choose \(h_1\) so that \(N(h_1)\ge1\).  If the increasing sequence
\(x_j\) had a finite limit, then \(L_j\) would eventually be a fixed
integer greater than one, while repeated use of (6) would force
\(\sigma_j\to0\), contradicting continuity of \(\sigma\) at that finite
limit.  Hence

\[
x_j\longrightarrow\infty,
\qquad
h_j\longrightarrow0,
\qquad
L_j\longrightarrow\infty.
\tag{14}
\]

The dyadic floor gives

\[
\frac12h^{-\alpha_{\rm dep}}
\le L(h)\le h^{-\alpha_{\rm dep}},
\tag{15}
\]

and therefore

\[
N(h_j)\log2
=\frac{\alpha_{\rm dep}}p\log x_j+O(1).
\tag{16}
\]

Writing \(\Delta_j=x_{j+1}-x_j\), equations (13) and (16) give

\[
\Delta_j
\sim
\frac{\alpha_{\rm dep}}{acp}\log x_j,
\qquad
\frac{x_{j+1}}{x_j}\longrightarrow1.
\tag{17}
\]

The survivor therefore makes infinitely many next-event moves, but
they are asymptotically close in the stretched coordinate \(h^{-7/4}\).

## 3. The terminal-return charge fits inside the same history

Equations (8) and (15) imply

\[
0<\tau_j
\le
A e^{-acx_j}x_j^{2\alpha_{\rm dep}/p}
\longrightarrow0.
\tag{18}
\]

Since \(\rho_j=e^{-(a-1)cx_j}\),

\[
0<\frac{\tau_j}{\rho_j}
\le
A e^{-cx_j}x_j^{2\alpha_{\rm dep}/p}
\longrightarrow0.
\tag{19}
\]

There is no hidden extra dissipation: in normalised variables,

\[
\frac{\tau_j}{\sigma_j}
=A L_j^2h_j^{-3}
\le D(h_j)
\tag{20}
\]

for all sufficiently large \(j\).

For completeness, the cumulative high-frequency and bulk masses can be
made separately monotone.  First,

\[
\frac{\rho_{j+1}}{\rho_j}
=e^{-(a-1)c\Delta_j}
\longrightarrow0.
\tag{21}
\]

The exact ancestry equation gives

\[
e^{-ac\Delta_j}
=\frac1{L_j}
\left(\frac{x_{j+1}}{x_j}\right)^{3/p}.
\tag{22}
\]

By (17), the dyadic order changes by at most one at each sufficiently
late step, so \(L_{j+1}/L_j\le2\).  Hence

\[
\frac{\tau_{j+1}}{\tau_j}
=
e^{-ac\Delta_j}
\left(\frac{L_{j+1}}{L_j}\right)^2
\le
\frac4{L_j}
\left(\frac{x_{j+1}}{x_j}\right)^{3/p}
\longrightarrow0.
\tag{23}
\]

Choose the first node late enough that \(\tau_j\), \(\rho_j\), and

\[
\beta_j:=\rho_j-\tau_j
\tag{24}
\]

are all positive and strictly decreasing.  This is possible by
(19), (21), and (23).  The physical terminal ages
\(\delta_j=\sigma_j^2h_j\) also decrease to zero.  We may additionally
ensure \(\kappa_1>1\).

Let

\[
\mathcal A_j:=(\delta_{j+1},\delta_j],
\qquad
\kappa_j:=\frac{L_j}{\sigma_j}
=\frac1{\sigma_{j+1}}.
\tag{25}
\]

On each \(\mathcal A_j\), place bulk mass
\(\beta_j-\beta_{j+1}\) at one fixed frequency
\(K_{\rm bulk}=1<\kappa_1\), and high mass
\(\tau_j-\tau_{j+1}\) at frequency \(\kappa_j\), uniformly in
terminal-age time:

\[
\begin{aligned}
d\mu(s,K)
:={}&
\sum_{j\ge1}
\frac{\mathbf1_{\mathcal A_j}(s)}{\delta_j-\delta_{j+1}}\,ds\\
&\quad\otimes
\left[
(\beta_j-\beta_{j+1})\delta_{K_{\rm bulk}}(dK)
+(\tau_j-\tau_{j+1})\delta_{\kappa_j}(dK)
\right].
\end{aligned}
\tag{26}
\]

Both coefficient series telescope, and
\(\mu((0,\delta_1)\times[0,\infty))=\rho_1<\infty\).
Moreover \(\kappa_k\ge\kappa_j\) for \(k\ge j\).  Summing (26) over
\(k\ge j\) proves both identities in (11).  This also proves directly
that the time marginal is a nonnegative \(L^1\) density.

## 4. The quantitative gap exposed by the survivor

The critical normalised frequency at which (2) stops vanishing is

\[
L_{\rm kill}(h,\sigma)
:=
\frac{h^{3/2}}{\sqrt{\sigma}}.
\tag{27}
\]

For the accelerated stretched-history zoom in (5),

\[
\boxed{
L_{\rm kill}(h,\sigma(h))
=\exp\!\left(\frac{ac}{2}h^{-7/4}\right),
}
\tag{28}
\]

whereas the reviewed logarithmic-depth dyadic frequency is only

\[
L(h)\asymp h^{-\alpha_{\rm dep}}.
\tag{29}
\]

Thus

\[
\frac{L(h)}{L_{\rm kill}(h,\sigma(h))}
\longrightarrow0
\tag{30}
\]

with a stretched-exponential margin.  The new tail theorem is strong,
but the presently proved causal depth supplies a polynomial frequency,
while this survivor requires a stretched-exponential frequency to make
the physical charge non-vanishing.

There is also an exact conditional next-event threshold.  Under (6),

\[
\sigma_jL_j^2h_j^{-3}
=
\left(\frac{x_{j+1}}{x_j}\right)^{6/p}
\exp\!\left(ac(2x_{j+1}-3x_j)\right).
\tag{31}
\]

Put \(q_j:=x_{j+1}/x_j\).  Equation (31) is equivalently

\[
\log\!\left(\sigma_jL_j^2h_j^{-3}\right)
=\frac6p\log q_j+acx_j(2q_j-3).
\tag{32}
\]

At the exact boundary \(q_j=3/2\), the charge equals

\[
\left(\frac32\right)^{6/p}>0.
\tag{33}
\]

Thus \(q_j\ge3/2\) along even one infinite subsequence contradicts
physical tail continuity.  More precisely, continuity requires

\[
acx_j(3-2q_j)-\frac6p\log q_j
\longrightarrow+\infty.
\tag{34}
\]

The exact survivor instead has \(q_j\to1\).  No estimate approaching
(34) from Navier--Stokes evolution is presently known or asserted here.

## 5. Exact route consequence

The following inputs, even together, do not close the feedback branch at
the scalar ledger level:

1. stretched-exponential normalised coefficient dissipation;
2. finite physical dissipation and absolute continuity;
3. nested terminal intervals;
4. logarithmically divergent causal interaction depth;
5. a dyadic top-frequency interpretation of that depth;
6. the full quadratic terminal-return tail charge;
7. vanishing global physical high-frequency tails; and
8. the exact identity “current top physical frequency equals reciprocal
   next event scale”.

This closes only the **bare scale identity** version of next-event
ancestry, not an actual Navier--Stokes genealogy.  A successful closure
must now supply at least one genuinely stronger input:

- a PDE lower bound driving the top frequency towards
  \(L_{\rm kill}\), rather than merely \(h^{-\alpha_{\rm dep}}\);
- a quantitative inter-event separation violating (34);
- a signed, vector, or flux charge whose fresh tail increments cannot be
  reused by (26); or
- a spacetime localisation law incompatible with this scalar
  time--frequency measure.

No regularity theorem, breakdown theorem, or Clay alternative A--D
follows.

## Reproduce

```bash
make adjoint-pressure-ancestry-survivor
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_ancestry_survivor -v
make check
```
