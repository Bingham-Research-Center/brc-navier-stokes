# Handoff: R3C Oseen entrance defect

**Updated:** 2026-07-25 · **Clay status:** unsolved

**Live route:** `ROUTE-R3C` · **Checkpoint:**
`EXP-TYPE-II-OSEEN-ENTRANCE-001`

## Load only

- [Oseen entrance theorem](dossier/experiments/type-ii-oseen-entrance.md)
- [`ROUTE-R3C`](dossier/records/routes.json)

## Exact q4 survivor

- Every Leray--Hopf continuation has a nonzero terminal energy defect,
  supported on a singular slice with
  \(3/5\le\dim_{\rm H}\sigma\le1\) and \(\mathcal H^1(\sigma)=0\).
- Its whole high-pass floor yields one projected-Oseen adjoint
  \(a\in L^\infty L^2\cap L^2\dot H^1\) with
  \[
  \langle u(t),a(t)\rangle=c_0>0,\quad
  a(t)\rightharpoonup0,\quad
  \inf_{t<T^*}\|a(t)\|_2>0.
  \]
- The cross-defect is nonzero and supported on \(\sigma\).
- Piecewise adjoint sewing pays fixed \(L^2\) reset cost per event.

## Exact live question

Does every energy-class projected-Oseen adjoint driven by this same
trajectory satisfy
\[
a(t)\rightharpoonup0\quad\Longrightarrow\quad\|a(t)\|_2\to0
\quad(t\uparrow T^*)?
\]
This terminal strong-trace theorem would contradict the survivor.

## Next bounded cycle

Work on the single limiting pair \((u,a)\), not eventwise tests. Derive the
microlocal cross-defect equation and isolate exactly what projected pressure
pays at \(T^*\). Try to exclude a nonzero cross measure on the
\(\mathcal H^1\)-null slice. Stop if the pressure term is only critical.

These are conditional repository theorems pending external review. Keep
slower clocks, divergent normalised energy, and R3B separate. No Clay
alternative is proved.
