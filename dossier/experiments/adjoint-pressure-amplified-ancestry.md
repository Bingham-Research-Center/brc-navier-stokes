# Spatial--frequency amplification still admits an exact scalar ancestry survivor

- **Experiment:** EXP-ADJOINT-PRESSURE-AMPLIFIED-ANCESTRY-001
- **Route:** ROUTE-R3B
- **Status:** adversarially recomputed analytic scalar time--frequency
  ledger counterexample; not a Navier--Stokes construction
- **Domain:** one nested terminal dissipation history with an exact
  polynomial-frequency event ancestry
- **Clay status:** unsolved
- **Inputs:** adversarially recomputed
  [spatial--frequency amplification theorem](adjoint-pressure-spatial-frequency.md)
  and [exact ancestry-survivor theorem](adjoint-pressure-ancestry-survivor.md)
- **Review:** [accepted after two precision repairs](../review-ledger.md)

The spatial--frequency theorem proves the conditional implication

\[
\mathfrak P_{S,F(h)}(h)\ge p_{\rm sf}>0
\quad\Longrightarrow\quad
D_b(h)
\ge
h^{-3}
\exp\!\left(
c_{\rm sf}\frac{F(h)}S h^{-7/4}
\right).
\tag{1}
\]

For fixed \(S\), take \(F(h)=h^{-\beta}\).  The exponent in (1) is then
\(h^{-(7/4+\beta)}\).  Absorb the fixed positive output-band factor by
setting

\[
c:=\frac{c_{\rm sf}}S.
\tag{1a}
\]

All occurrences of \(c\) below mean this renamed constant.  This note
asks the exact adversarial question:

> Does the amplified cost in (1), together with exact next-event
> frequency ancestry and the quadratic terminal-return tail toll, now
> contradict finite physical dissipation?

The answer remains no at the scalar nonnegative-ledger level.  The
amplification replaces the stretched coordinate \(h^{-7/4}\) by
\(h^{-(7/4+\beta)}\), but the event zoom can accelerate in the same new
coordinate.

This does not realise the pressure antecedent in (1), a coefficient
field, an Oseen state, or a Navier--Stokes trajectory.  It proves only
that the newly forced cost and the exact nonnegative ancestry ledgers
are mutually compatible.

## 1. Amplified ancestry-survivor theorem

Fix

\[
p_0:=\frac74,
\qquad
\beta>0,
\qquad
\widehat p:=p_0+\beta,
\qquad
c>0,
\qquad
a>1,
\qquad
A>0.
\tag{2}
\]

Put

\[
\begin{aligned}
y(h)&:=h^{-\widehat p},\\
F(h)&:=h^{-\beta},\\
D(h)&:=h^{-3}e^{cy(h)},\\
\sigma(h)&:=h^3e^{-acy(h)},\\
\rho(h)&:=\sigma(h)D(h)
=e^{-(a-1)cy(h)},\\
\delta(h)&:=\sigma(h)^2h.
\end{aligned}
\tag{3}
\]

The spatial--frequency cost is saturated exactly:

\[
\boxed{
\log\!\bigl(D(h)h^3\bigr)
=
cy(h)
=
cF(h)h^{-7/4}.
}
\tag{4}
\]

There is a strictly decreasing sequence \(h_j\downarrow0\), beginning
arbitrarily far down the genealogy, such that

\[
\boxed{
\sigma_{j+1}
=
\frac{\sigma_j}{F_j},
\qquad
F_j:=F(h_j).
}
\tag{5}
\]

Thus the current top physical frequency is exactly the reciprocal next
event scale:

\[
\boxed{
\frac{F_j}{\sigma_j}
=
\frac1{\sigma_{j+1}}.
}
\tag{6}
\]

The physical total dissipation mass is finite and tends to zero:

\[
\boxed{
\rho_j
=
\sigma_jD(h_j)
=
e^{-(a-1)cy_j}
\longrightarrow0.
}
\tag{7}
\]

Equivalently, the physical zoom satisfies the exact little-\(o\)
ceiling forced by (1):

\[
\boxed{
\frac{\sigma(h)}
{h^3e^{-cy(h)}}
=
e^{-(a-1)cy(h)}
\longrightarrow0.
}
\tag{7a}
\]

The quadratic terminal-return tail payment

\[
\tau_j
:=
A\sigma_jF_j^2h_j^{-3}
=
Ae^{-acy_j}F_j^2
\tag{8}
\]

obeys

\[
\boxed{
\tau_j\longrightarrow0,
\qquad
\frac{\tau_j}{\rho_j}
=
Ae^{-cy_j}F_j^2
\longrightarrow0.
}
\tag{9}
\]

After starting sufficiently late, there is one finite nonnegative Borel
measure

\[
\mu
\quad\hbox{on}\quad
(0,\delta_1)\times[0,\infty)
\tag{10}
\]

whose time marginal has an \(L^1\) density and for which

\[
\boxed{
\begin{aligned}
\mu\bigl((0,\delta_j)\times[0,\infty)\bigr)
&=\rho_j,\\
\mu\bigl((0,\delta_j)\times
[F_j/\sigma_j,\infty)\bigr)
&=\tau_j
\end{aligned}}
\tag{11}
\]

for every \(j\).  Hence one finite nested history pays simultaneously:

1. the amplified spatial--frequency total cost;
2. the quadratic terminal-return high-frequency toll; and
3. exact current-frequency/next-event ancestry.

## 2. Exact event recursion

In the new stretched coordinate \(y=h^{-\widehat p}\),

\[
\log\sigma(y)
=
-\frac3{\widehat p}\log y-acy,
\qquad
\log F(y)
=
\frac{\beta}{\widehat p}\log y.
\tag{12}
\]

Start with \(y_1>1\).  Given \(y_j\), define \(y_{j+1}>y_j\) as the
unique solution of

\[
\boxed{
ac(y_{j+1}-y_j)
+\frac3{\widehat p}
\log\frac{y_{j+1}}{y_j}
=
\frac{\beta}{\widehat p}\log y_j.
}
\tag{13}
\]

The left side is continuous and strictly increasing from zero to
infinity.  Equation (13) is exactly (5).

The sequence \(y_j\) cannot have a finite limit: the right side would
then retain a fixed positive value while the increments tend to zero.
Thus

\[
y_j\longrightarrow\infty,
\qquad
h_j\longrightarrow0,
\qquad
F_j\longrightarrow\infty.
\tag{14}
\]

Writing \(\Delta_j=y_{j+1}-y_j\), equation (13) gives

\[
\boxed{
\Delta_j
\sim
\frac{\beta}{ac\widehat p}\log y_j,
\qquad
\frac{y_{j+1}}{y_j}\longrightarrow1.
}
\tag{15}
\]

The amplified ancestry therefore remains asymptotically dense in its
own stretched coordinate.

## 3. One finite nested history

Equations (3) and (8) give

\[
\tau_j
=
Ae^{-acy_j}y_j^{2\beta/\widehat p},
\qquad
\frac{\tau_j}{\rho_j}
=
Ae^{-cy_j}y_j^{2\beta/\widehat p}.
\tag{16}
\]

This proves (9) and also shows that the normalised tail fits inside the
amplified dissipation:

\[
\frac{\tau_j}{\sigma_j}
=
AF_j^2h_j^{-3}
\le
D(h_j)
\tag{17}
\]

for all sufficiently large \(j\).

Let \(q_j=y_{j+1}/y_j\).  Exact ancestry gives

\[
e^{-ac\Delta_j}
=
\frac{q_j^{3/\widehat p}}{F_j}.
\tag{18}
\]

Consequently,

\[
\frac{\tau_{j+1}}{\tau_j}
=
\frac{
q_j^{(3+2\beta)/\widehat p}
}{F_j}
\longrightarrow0,
\tag{19}
\]

while

\[
\frac{\rho_{j+1}}{\rho_j}
=
e^{-(a-1)c\Delta_j}
\longrightarrow0.
\tag{20}
\]

Start late enough that \(\tau_j\), \(\rho_j\), and

\[
\gamma_j:=\rho_j-\tau_j
\tag{21}
\]

are positive and strictly decreasing.  The terminal ages
\(\delta_j=\sigma_j^2h_j\) also decrease to zero.  Put

\[
\mathcal A_j:=(\delta_{j+1},\delta_j],
\qquad
\kappa_j:=\frac{F_j}{\sigma_j}
=\frac1{\sigma_{j+1}}.
\tag{22}
\]

Choose \(K_{\rm bulk}<\kappa_1\).  On \(\mathcal A_j\), place the fresh
bulk mass \(\gamma_j-\gamma_{j+1}\) at \(K_{\rm bulk}\), and the fresh
tail mass \(\tau_j-\tau_{j+1}\) at \(\kappa_j\), uniformly in terminal
age:

\[
\begin{aligned}
d\mu(s,K)
:={}&
\sum_{j\ge1}
\frac{\mathbf1_{\mathcal A_j}(s)}
{\delta_j-\delta_{j+1}}\,ds\\
&\quad\otimes
\left[
(\gamma_j-\gamma_{j+1})\delta_{K_{\rm bulk}}(dK)
+(\tau_j-\tau_{j+1})\delta_{\kappa_j}(dK)
\right].
\end{aligned}
\tag{23}
\]

Both coefficient series telescope.  Since \(\kappa_j\) increases,
summing (23) over \(k\ge j\) proves (11).  Its total mass is
\(\rho_1<\infty\), and its time marginal is explicitly an \(L^1\)
density.

## 4. Kill frequency and the unchanged ancestry boundary

The quadratic terminal-return kill frequency is

\[
F_{\rm kill}(h,\sigma)
:=
\frac{h^{3/2}}{\sqrt{\sigma}}.
\tag{24}
\]

For (3), the polynomial powers cancel exactly:

\[
\boxed{
F_{\rm kill}(h,\sigma(h))
=
\exp\!\left(\frac{ac}{2}h^{-\widehat p}\right).
}
\tag{25}
\]

By contrast,

\[
F(h)=h^{-\beta},
\qquad
\frac{F(h)}{F_{\rm kill}(h,\sigma(h))}
\longrightarrow0
\tag{26}
\]

with a stretched-exponential margin.

There is again an exact next-event separation threshold.  Under (5),

\[
\boxed{
\log\!\left(
\sigma_jF_j^2h_j^{-3}
\right)
=
\frac6{\widehat p}\log q_j
+acy_j(2q_j-3).
}
\tag{27}
\]

At \(q_j=3/2\), the charge equals the fixed positive constant

\[
\left(\frac32\right)^{6/\widehat p}.
\tag{28}
\]

Thus physical tail continuity requires

\[
acy_j(3-2q_j)
-\frac6{\widehat p}\log q_j
\longrightarrow+\infty.
\tag{29}
\]

The survivor has \(q_j\to1\), so it remains strictly inside this
boundary.

## 5. Exact route consequence

Even granting at every event:

1. a polynomially growing high-state pressure threshold
   \(F=h^{-\beta}\);
2. the complete amplified cost
   \(D\ge h^{-3}\exp(cFh^{-7/4})\);
3. finite and absolutely continuous physical dissipation;
4. the quadratic terminal-return tail toll; and
5. exact current-frequency/next-event ancestry,

the nonnegative scalar history is consistent.  The new theorem raises
the cost but does not supply a lower bound on the physical zoom
\(\sigma\); the zoom can outrun the raised exponent.

This closes the proposal that spatial--frequency amplification plus bare
ancestry is already an arithmetic contradiction.  A genuine closure
must use information absent from (23):

- a PDE lower bound preventing the accelerated zoom in (3);
- an exhaustive history decomposition forcing non-negligible terminal
  high-state pressure, rather than merely visiting high frequency;
- a signed or vector-valued fresh tail which cannot be reused; or
- a quantitative charge for histories which return below \(F\) before
  the terminal pressure observation.

No regularity theorem, breakdown theorem, or Clay alternative A--D
follows.

## Reproduce

```bash
make adjoint-pressure-amplified-ancestry
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_amplified_ancestry -v
make check
```
