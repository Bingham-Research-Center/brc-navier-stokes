# Handoff: R3C diagonal Gaussian reuse

**Updated:** 2026-07-25 · **Clay status:** unsolved

**Live route:** `ROUTE-R3C` ·
`EXP-TYPE-II-DIAGONAL-HEAT-FLUX-RECYCLING-001`

## Load only

- [Diagonal Gaussian flux](dossier/experiments/type-ii-diagonal-heat-flux-recycling.md)
- [`ROUTE-R3C`](dossier/records/routes.json)

## Exact reduction

For the reversed full-defect entrance, put
\[
F=\mathbb P((U\cdot\nabla)v),\quad S(r)=e^{\nu r\Delta},\quad
\Pi_r(s)=-\langle F(s),S(2r)v(s)\rangle .
\]
The moving heat field \(S(\tau-s)v(s)\) has derivative
\(-S(\tau-s)F(s)\), tends strongly to zero at the entrance, and gives
\[
\frac12\|v(\tau)\|_2^2=\int_0^\tau\Pi_{\tau-s}(s)\,ds,\qquad \Pi_0=0.
\]

## Non-reuse gained, obstruction exposed

Nested terminal detectors satisfy the exact recycling law
\[
\int_0^\sigma(\Pi_{\sigma-s}-\Pi_{\tau-s})\,ds
=\int_\sigma^\tau\Pi_{\tau-s}\,ds
+\nu\int_\sigma^\tau\|\nabla v\|_2^2\,ds.
\]
For disjoint heat-age bands \(B_k\),
\[
\sum_k|\langle F,B_kv\rangle|\lesssim M\|\nabla v\|_2^2.
\]
This is genuine \(\ell^1\) Gaussian-band control, but q4 already forces
its time integral to diverge.

## Sharp scalar survivor

With the recorded power--log \(M_\sharp,Y_\sharp\),
\[
\Pi_n^\sharp(r,s)=
\frac{(n+1)E_\sharp(r+s)}2\frac{r^n}{(r+s)^{n+1}}
\]
satisfies every scalar endpoint, diagonal, recycling, magnitude, and
variation constraint. For \(\sigma=q\tau\), its shared-history fraction
is \(1-(1-q)^{n+1}\to1\). Only its constant-energy core has the proved
signed Laguerre heat spectrum; it is not an NSE trajectory.

## Exact live question

Can \(F=\mathbb P((U\cdot\nabla)v)\) realise coherent Laguerre-type reuse
on one q4 trajectory, or does its triadic phase/pressure/genealogy force
a fresh component paid by a finite same-trajectory charge?

## Next bounded cycle

Write the actual radial heat spectral density and its quadratic triad
formula. Test whether incompressibility, frequency support, or the
strong-trace drift imposes a moment/sign restriction absent from the
scalar survivor. Do not revisit norm-only impulse or abstract Gaussian
orthogonality without a new finite charge.

All results are conditional and await external review. Keep slower
clocks, divergent normalised energy, R3B, and other Clay alternatives
separate.
