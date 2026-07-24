# Finite dissipation history does not exclude stretched-exponential feedback

- **Experiment:** EXP-ADJOINT-PRESSURE-STRETCHED-HISTORY-001
- **Route:** ROUTE-R3B
- **Status:** analytic ledger-realisation theorem;
  [adversarially recomputed valid in scope](../review-ledger.md);
  not a Navier--Stokes construction
- **Domain:** scalar history ledger induced by the physical scale map
- **Clay status:** unsolved
- **Input:** adversarially recomputed
  [intermediate-localisation theorem](adjoint-pressure-intermediate-localization.md)

The reviewed feedback reduction now forces every selected zero-data
feedback layer to obey

\[
D_b(h)
\ge
h^{-3}\exp(c_{\rm sh}h^{-7/4}).
\tag{1}
\]

On one physical trajectory at zoom \(\sigma\), the exact identities are

\[
E=\sigma D_b(h),
\qquad
|I|=\sigma^2h,
\qquad
\lambda=\sigma h^{-3},
\qquad
\rho=\sigma D_b(h)=E.
\tag{2}
\]

It is tempting to combine (1) with finite physical dissipation and
absolute continuity to obtain a contradiction. That inference is false
at the scalar-ledger level, even when all selected physical time
intervals are nested at one terminal time.

## 1. Exact ledger-realisation theorem

Fix

\[
p:=\frac74,
\qquad
c>0,
\qquad
a>1,
\tag{3}
\]

and let \(h_j\downarrow0\) be any strictly decreasing sequence in
\((0,1]\). Define

\[
\boxed{
\begin{aligned}
D_j
&:=h_j^{-3}\exp(ch_j^{-p}),\\
\sigma_j
&:=h_j^3\exp(-ac h_j^{-p}),\\
\lambda_j
&:=\sigma_jh_j^{-3}
=\exp(-ac h_j^{-p}),\\
\rho_j
&:=\sigma_jD_j
=\exp(-(a-1)c h_j^{-p}),\\
\delta_j
&:=\sigma_j^2h_j
=h_j^7\exp(-2ac h_j^{-p}).
\end{aligned}}
\tag{4}
\]

Then \(\delta_j\downarrow0\) and \(\rho_j\downarrow0\). There exists one
nonnegative function

\[
e\in L^1(0,\delta_1)
\tag{5}
\]

such that

\[
\boxed{
\int_0^{\delta_j}e(s)\,ds
=
\rho_j
=
\sigma_jD_j
\qquad\text{for every }j.
}
\tag{6}
\]

Thus the nested physical intervals

\[
I_j=(-\delta_j,0)
\tag{7}
\]

all belong to one finite absolutely continuous terminal dissipation
history, yet their scaled dissipations satisfy the stretched-exponential
floor (1) with equality.

Here \(s=-t\) is terminal-age time: \(s=0\) is the common terminal
endpoint and \(0<s<\delta_j\) represents the physical interval \(I_j\).

## 2. Construction of the common history

Both scalar functions

\[
h\longmapsto
h^7\exp(-2ac h^{-p}),
\qquad
h\longmapsto
\exp(-(a-1)c h^{-p})
\tag{8}
\]

are strictly increasing on \((0,1]\). Hence the points

\[
(\delta_j,\rho_j)
\tag{9}
\]

decrease monotonically to \((0,0)\).

Define \(F(0)=0\), set \(F(\delta_j)=\rho_j\), and make \(F\) affine on
every interval \([\delta_{j+1},\delta_j]\). The slopes are

\[
m_j
:=
\frac{\rho_j-\rho_{j+1}}
     {\delta_j-\delta_{j+1}}
>0.
\tag{10}
\]

Put

\[
e(s):=F'(s)
\quad\text{for almost every }s.
\tag{11}
\]

For \(s\in[\delta_{j+1},\delta_j]\), the partial-interval calculation is

\[
\begin{aligned}
\int_0^s e(r)\,dr
&=
\sum_{k=j+1}^{\infty}
(\rho_k-\rho_{k+1})
+m_j(s-\delta_{j+1})\\
&=
\rho_{j+1}
+m_j(s-\delta_{j+1})
=F(s).
\end{aligned}
\tag{11a}
\]

The intervals in (10) are disjoint and

\[
\int_0^{\delta_1}e(s)\,ds
=
\sum_{j\ge1}
(\rho_j-\rho_{j+1})
=
\rho_1
<\infty.
\tag{12}
\]

Therefore \(F(s)=\int_0^s e(r)\,dr\), proving (5)--(6). In particular,
absolute continuity gives the required vanishing
\(\int_0^\delta e\to0\), but places no useful lower bound on the zoom
\(\sigma_j\).

## 3. Every reviewed scale identity still holds

The physical scale ordering is

\[
\boxed{
\frac{\sigma_j}{\lambda_j}=h_j^3\longrightarrow0,
\qquad
\frac{\lambda_j}{\rho_j}
=\exp(-ch_j^{-p})\longrightarrow0.
}
\tag{13}
\]

The logarithmic exterior depth is exactly

\[
\boxed{
\log\frac{\rho_j}{\lambda_j}
=
ch_j^{-7/4}.
}
\tag{14}
\]

The interaction and dissipation clocks are

\[
\boxed{
\frac{\delta_j}{\lambda_j^2}
=h_j^7,
\qquad
\frac{\delta_j}{\rho_j^2}
=
h_j^7\exp(-2ch_j^{-7/4}).
}
\tag{15}
\]

The physical packet is scale critical at its dissipation ancestor:

\[
\boxed{
\frac{1}{\rho_j}
\int_0^{\delta_j}e(s)\,ds
=1.
}
\tag{16}
\]

Nevertheless its raw physical cost tends to zero:

\[
\int_0^{\delta_j}e(s)\,ds=\rho_j\longrightarrow0.
\tag{17}
\]

Finally,

\[
\boxed{
\frac{\sigma_j}
{h_j^3\exp(-ch_j^{-7/4})}
=
\exp(-(a-1)ch_j^{-7/4})
=\rho_j
\longrightarrow0,
}
\tag{18}
\]

so the zoom genuinely outruns the reciprocal stretched exponential.

## 4. Why a raw event sum is not a telescope

The selected packets in (6) are cumulative terminal masses. They are
not disjoint payments. Their fresh increments are

\[
\int_{\delta_{j+1}}^{\delta_j}e(s)\,ds
=
\rho_j-\rho_{j+1},
\tag{19}
\]

and these telescope:

\[
\sum_{j\ge1}
\int_{\delta_{j+1}}^{\delta_j}e(s)\,ds
=\rho_1.
\tag{20}
\]

Thus infinitely many identities of the scale-critical form (16) can
reuse one finite nested history. Summing the normalised event costs
counts the same terminal dissipation repeatedly.

## 5. Exact route consequence

Equations (4)--(20) prove that the following inputs, even together, do
not exclude the stretched-exponential feedback branch:

1. the lower bound (1);
2. the exact physical scale map (2);
3. nested physical terminal intervals;
4. finite total physical dissipation;
5. absolute continuity of that dissipation;
6. \(\sigma_j=o(h_j^3e^{-ch_j^{-7/4}})\);
7. collapse of both normalised clocks; and
8. a scale-critical normalisation \(E_j/\rho_j=1\) at every event.

This is a theorem about the available scalar ledgers, not a construction
of a velocity, pressure, suitable solution, or Navier--Stokes
singularity. It does not show that the feedback branch is attainable.

The next successful estimate must use information absent from this
realisation. Viable targets are now sharply separated:

- a PDE relation coupling \(\sigma_j\) or \(h_j\) to the cumulative
  dissipation history;
- a signed or vector-valued charge whose fresh event increments cannot
  be reused on nested intervals;
- an ancestry relation comparing \(\rho_j\), \(\lambda_j\), and the next
  actual event scale; or
- a causal interaction-order estimate which improves the logarithmic
  exterior shell sum.

Finite energy and absolute continuity alone are closed as candidate
solutions to this gate. No regularity theorem, breakdown theorem, or
Clay alternative A--D follows.

## Reproduce

```bash
make adjoint-pressure-stretched-history
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_stretched_history -v
make check
```
