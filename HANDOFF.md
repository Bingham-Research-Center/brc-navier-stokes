# Handoff: R3C spatial-import non-reuse

**Updated:** 2026-07-24 · **Clay status:** unsolved

**Live route:** `ROUTE-R3C` · **Checkpoint:**
`EXP-TYPE-II-MULTIRECORD-SPATIAL-IMPORT-001`

## Load only

- [Multirecord import theorem](dossier/experiments/type-ii-multirecord-spatial-import.md)
- [`ROUTE-R3C`](dossier/records/routes.json)

## Exact live question

Can carrier genealogy remove the summable \(R_j\) weight from the finite
pressure-plus-kinetic flux action, or give repeated imports finite crossing
multiplicity along energy-transport paths?

## Live theorem

On the original exact \(q=4\) grid, set
\[
i_j=j-\lfloor j/4\rfloor.
\]
Every retained partial/tight energy-efficient endpoint forces
\[
\mathsf X_j:=
\int_{t_{i_j}}^{t_j}\!\!\int
\left(\frac12|u|^2+p\right)u\cdot\nabla\chi_j\,dx\,dt
\ge\gamma/4.
\]
An infinite subsequence has disjoint time windows, hence
\(\sum\mathsf X_j=\infty\). The direct common budget is only
\[
\sum R_j|\mathsf X_j|\lesssim
\int_0^{T^*}\!\!\int(|u|^3+|p||u|)<\infty,
\]
which is compatible with geometric \(R_j\). No packet freshness or Clay
alternative is proved.

## Next bounded cycle

Decompose the signed energy flux into transport paths/tubes and test whether
one packet can cross infinitely many shrinking moving cutoffs without a
scale-free pressure, deformation, or residence cost. Do not rederive
terminal infrared evacuation or local import; keep diffuse and
divergent-normalised-energy branches separate.
