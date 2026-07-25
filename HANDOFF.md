# Handoff: R3C nonlinear entrance from infinity

**Updated:** 2026-07-25 · **Clay status:** unsolved

**Live route:** `ROUTE-R3C` · `EXP-TYPE-II-NONLINEAR-DEFECT-ENTRANCE-001`

## Load only

- [Nonlinear entrance](dossier/experiments/type-ii-nonlinear-defect-entrance.md)
- [`ROUTE-R3C`](dossier/records/routes.json)

## Exact reduction

The full-defect entrance splits \(u=a+b\), with \(b(t)\to u_*\) strongly.
For \(\tau=T-t\), set \(v=-a(T-\tau)\), \(c=-b(T-\tau)\). Then
\[
\partial_\tau v-\nu\Delta v+
\mathbb P(((v+c)\cdot\nabla)v)=0,
\]
\[
\quad v(\tau)\rightharpoonup0,\qquad
c(\tau)\to-u_*\ {\rm strongly},\qquad
\|v(\tau)\|_2^2+2\nu\int_0^\tau\|\nabla v\|_2^2=d>0.
\]
Thus the lost component is itself a forward nonlinear flow entering from
frequency infinity, with strong-trace drift.

At exact q4 records,
\[
|v(\tau_j)|^2dx\rightharpoonup^*\vartheta,\qquad
\int_{A_j}|v(\tau_j)|^2\ge c,\qquad
\|v(\tau_j)\|_{3,\infty}\gtrsim m_j.
\]
The local energy law starts from the positive measure \(\vartheta/2\),
although the vector trace is weakly zero.

## Closed shortcut

For \(r=a\cdot b\), the two positive defect measures cancel:
\[
r(t)dx\rightharpoonup0,\qquad
\int r(t)=2\nu\int_t^T\|\nabla a\|_2^2.
\]
The exact spectral relative identity leaves
\(\langle[(u\cdot\nabla),B_N]b,a\rangle\), bounded by
\(\|u\|_{3,\infty}\|\nabla b\|_2\|\nabla a\|_2\).
Current hypotheses give no integrable majorant or sign.

## Sharp survivor

With \(m_j=2^{2j}\), \(\delta_j=2^{-11j}/j\), and
\(\Lambda_j=2^{14j/3}j^{2/3}\),
\[
m_j^2\Lambda_j^{3/2}\delta_j=1,\quad
\sum\delta_j\Lambda_j^2<\infty,\quad
\sum m_j\delta_j\Lambda_j^2=\infty.
\]
A Hilbert ledger also realises the weak-zero/positive-energy boundary and
strong remainder. It is not a PDE trajectory.

## Exact live question / Next bounded cycle

Prove or falsify a zero-trace nonlinear entrance theorem: the exact q4
same-trajectory coupling must force \(d=0\). Target a boundary energy
inequality, non-summable inverse-cascade charge, clock-relative compactness
modulus, or removability of the \(\mathcal H^1\)-null initial energy measure.

All results are conditional and await external review. Keep slower clocks,
divergent normalised energy, and R3B separate. No Clay alternative is proved.
