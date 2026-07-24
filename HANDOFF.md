# Handoff: R3C unthinned band stack

**Updated:** 2026-07-24 · **Clay status:** unsolved

**Live route:** `ROUTE-R3C` · **Checkpoint:** `EXP-TYPE-II-BAND-DISSIPATION-BUDGET-001`

## Load only

- [Critical band budget](dossier/experiments/type-ii-band-dissipation-budget.md)
- [`ROUTE-R3C`](dossier/records/routes.json)

## Exact live question

Can the unthinned first-record bands be counted across logarithmic scale, or
can NSE triads realise the remaining nonlinear rotation?

## Live result

Successive frozen-band works share the physical dissipation budget:

\[
\sum_j\left[
\nu\sqrt{\frac{r_j}{\gamma}}|W_j^{N}|
+
\frac{r_j^2|W_j^\nu|^2}{\gamma\nu\Delta t_j}
\right]
\lesssim
\nu\int_0^{T^*}\|\nabla u\|_2^2.
\]

Scale-separated bands have bounded-overlap correlation lifetimes. But their
fixed width forces geometric radii, so the nonlinear
\(\sum_j\sqrt{r_j}\) charge converges automatically. The \(q_j=4\) ledger's
viscous charges diverge; any survivor is eventually nonlinear.

## Next bounded cycle

Do not re-run elementary Bessel thinning. Seek a Carleson/variation estimate
for overlapping heat-scale intervals without discarding event density.
Otherwise test whether actual NSE triads can implement the critical
nonlinear rotation. Keep recentering, coherent trace, and divergent energy
separate.
