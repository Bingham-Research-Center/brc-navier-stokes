# Handoff: R3C adjoint commutator anomaly

**Updated:** 2026-07-25 · **Clay status:** unsolved

**Live route:** `ROUTE-R3C` · **Checkpoint:**
`EXP-TYPE-II-CROSS-CURRENT-ANOMALY-001`

## Load only

- [Cross-current anomaly](dossier/experiments/type-ii-cross-current-anomaly.md)
- [`ROUTE-R3C`](dossier/records/routes.json)

## Exact q4 survivor

- One projected-Oseen entrance has
  \[
  \langle u(t),a(t)\rangle=c_0>0,\quad
  a(t)\rightharpoonup0,\quad
  \inf_{t<T^*}\|a(t)\|_2>0.
  \]
- Its cross measure is nonzero on an \(\mathcal H^1\)-null slice, hence is
  not in \(H^{-1}\); the preterminal cross \(H^{-1}\) norm diverges.
- Every Fourier low-pass cancels both pressures and forces signed
  commutator flux tending to \(-c_0\) as the cutoff tends to infinity.
- Despite \(\nabla a\in L_t^2L_x^2\), necessarily
  \[
  \int_t^{T^*}\|u\|_{L^{3,\infty}}\|\nabla a\|_2^2\,ds=\infty
  \quad(t<T^*).
  \]

## Exact live question

Can the same-trajectory equation force
\[
\nabla a\in L_t^{22/9,2}L_x^2
\]
on one terminal interval? Lorentz Hölder would then make the displayed
weighted dissipation finite and close q4.

## Next bounded cycle

Work only on reverse-time Caccioppoli/Meyers improvement for \(a\), split
over weak-\(L^3\) amplitude slabs. Determine whether self-generation of the
drift supplies any gain above \(L_t^2\dot H^1\). Track projected pressure;
do not seek a pressure lower bound, since transverse modes defeat it. Stop
and record the exact endpoint if the \(22/9\) gain is unavailable.

These are conditional repository theorems pending external review. Keep
slower clocks, divergent normalised energy, and R3B separate. No Clay
alternative is proved.
