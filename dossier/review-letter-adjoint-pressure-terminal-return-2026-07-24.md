# Independent review request: terminal high--high-to-low pressure return

**Date:** 2026-07-24

**Primary theorem:**
[`experiments/adjoint-pressure-terminal-return.md`](experiments/adjoint-pressure-terminal-return.md)

**Executable certificate:**
[`../lab/navier_lab/adjoint_pressure_terminal_return.py`](../lab/navier_lab/adjoint_pressure_terminal_return.py)

**Tests:**
[`../lab/tests/test_adjoint_pressure_terminal_return.py`](../lab/tests/test_adjoint_pressure_terminal_return.py)

**Clay status:** unsolved

## Requested verdict

Please decide whether the note proves the following bounded theorem:

> For an \(L^\infty_tL^2_x\) state and an
> \(L^2_t\dot H^1_x\) drift, the complete resonant input tail above
> \(L\) returning to pressure output below \(S\ll L\) is bounded by
> \(C(S/L)\sqrt T\,Q\sqrt{D_{b,>L}}\).

Reject any implication that this alone supplies a uniform bound across
the rescaled physical event genealogy or resolves Navier--Stokes.

## 1. Fourier support and multiplier

Fix the convention

\[
\operatorname{supp}\widehat{\Delta_R}
\subset\{R/2\le|\xi|\le2R\},
\qquad
P_{>L}=\sum_{R\ge L}\Delta_R.
\]

For

\[
\mathcal H_{>L}(z,b)
=
\sum_{R\ge L}\Delta_Rz\otimes\widetilde\Delta_Rb,
\]

please verify that low output \(S\), with \(L\ge16S\), sees only
comparable high--high inputs and gives the exact cutoff identity

\[
\Pi_S((P_{>L}z)\otimes b)
=
\Pi_S\mathcal H_{>L}(z,b).
\]

Check that the low-localised multiplier

\[
S_S\mathbb Q\operatorname{div}
\]

has an \(L^1\) convolution-kernel norm \(O(S)\).

## 2. Dyadic square-function estimate

Please re-derive

\[
\begin{aligned}
\|S_S\mathbb Q\operatorname{div}
\mathcal H_{>L}(z,b)\|_1
&\lesssim
S\sum_{R\ge L}
\|\Delta_Rz\|_2\|\widetilde\Delta_Rb\|_2\\
&\lesssim
\frac SL
\|z\|_2
\left(
\sum_{R\ge L}
\|\widetilde\Delta_R\nabla b\|_2^2
\right)^{1/2}.
\end{aligned}
\]

Then check Cauchy--Schwarz in time:

\[
\int_0^T
\|\Pi_S\mathcal H_{>L}(z,b)\|_1\,dt
\lesssim
\frac SL\sqrt T\,
\|z\|_{L^\infty_tL^2_x}
D_{b,>L}^{1/2}.
\]

Please flag any hidden homogeneous low-frequency, tensor-index, or
Littlewood--Paley overlap issue.

## 3. Inversion and adjoint energy

Check that a pressure floor \(p\) forces

\[
D_{b,>L}
\gtrsim
\frac{p^2L^2}{S^2Q^2T}.
\]

For the smooth divergence-free Oseen adjoint, verify that skew transport
gives \(Q=\|\psi\|_2\) and hence the claimed high-tail pressure return
bound.

## 4. Scaling audit

Please recompute the critical packet ledger:

\[
\|z_R\|_2^2\asymp1,\quad
\|b_R\|_2^2\asymp R^{-1},\quad
\|\nabla b_R\|_2^2\asymp R,
\]

\[
\|z_R\otimes b_R\|_1^2\asymp R^{-1}.
\]

Check that it saturates the \(S/R\) power at norm level.  Also verify
that scalar Zeno \(L^1\) mass \(R^{-1}\) in volume \(R^{-3}\) has
\(L^2\) square \(R\), and that a unit \(L^2\) ceiling forces volume at
least \(R^{-2}\).

For the terminal remainder with \(Q\lesssim h\), \(T=h\), verify

\[
D_{b,>L}(h)\gtrsim L^2h^{-3}.
\]

Finally check the parabolic scaling

\[
D_{\rm norm}=\sigma^{-1}D_{\rm phys}.
\]

A normalised band \(R\) is the physical band \(R/\sigma\).  Please
verify that the full pulled-back tail charge is

\[
D_{v,\rm tail}^{\rm phys}
\gtrsim
\sigma_j\frac{p_j^2L_j^2}{S_j^2Q_j^2T_j}.
\]

On the terminal layer this becomes

\[
D_{v,\rm tail}^{\rm phys}
\gtrsim\sigma_jL_j^2h_j^{-3}
\]

for fixed pressure and output floors.  The physical tails are nested
and may reuse finer-frequency dissipation; no disjoint-band summation
is asserted.

## 5. Global physical-tail supplement

Please also verify the same-trajectory tail-continuity consequence.
For a finite-dissipation physical trajectory, define

\[
\mathcal E_{\ge\Lambda}(v)
=
\int_0^{T^*}
\sum_{K\ge\Lambda}
\|\widetilde\Delta_K\nabla v(t)\|_2^2\,dt.
\]

Check

\[
\mathcal E_{\ge\Lambda}(v)\to0
\qquad(\Lambda\to\infty)
\]

and, for the event pullback restricted to its physical time interval,

\[
\sigma_jD_{b_j,>L_j}
\lesssim
\mathcal E_{\ge cL_j/\sigma_j}(v).
\]

Does \(L_j/\sigma_j\to\infty\) therefore force

\[
\sigma_j
\frac{p_j^2L_j^2}{S_j^2Q_j^2T_j}
\to0?
\]

On the terminal layer, verify

\[
\sigma_jL_j^2h_j^{-3}\to0.
\]

For \(L_j=2^{N(h_j)}\) and
\(N(h)=\lfloor c_{\rm dep}\log(1/h)\rfloor\), check

\[
L_j\asymp h_j^{-c_{\rm dep}\log2}
\]

up to a fixed dyadic factor, hence

\[
\sigma_j
=
o\!\left(
h_j^{3+2c_{\rm dep}\log2}
\right).
\]

This is only a necessary ancestry ceiling, not a contradiction.

## 6. Scope

Require repair if the note claims any of:

- summation of all intermediate Oseen frequency paths;
- a uniform dissipation ceiling across physical rescalings;
- non-reuse or disjointness of the forced physical bands;
- a Navier--Stokes event-ancestry theorem;
- regularity or a Clay alternative.

The intended remaining gate is to contradict the forced upper ceiling
using a stronger lower frequency law, make the vanishing nested charges
quantitatively non-reusable, or couple the multiscale itinerary to
physical event ancestry.

## Reproduce

```bash
make adjoint-pressure-terminal-return
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_terminal_return -v
make check
git diff --check
```
