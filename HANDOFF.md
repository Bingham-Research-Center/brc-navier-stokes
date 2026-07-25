# Handoff: R3C dynamic spectral shell

**Updated:** 2026-07-25 · **Clay status:** unsolved

**Live route:** `ROUTE-R3C` · `EXP-TYPE-II-RADIAL-TRIAD-SPECTRUM-001`

## Load only

- [Radial triad spectrum](dossier/experiments/type-ii-radial-triad-spectrum.md)
- [`ROUTE-R3C`](dossier/records/routes.json)

## Exact joint object

Push kinetic energy and nonlinear pairing to \(\lambda=2\nu|\xi|^2\):
\[
\mathcal E(r,s)=\int e^{-r\lambda}\,d\varepsilon_s,\qquad
\Pi_r(s)=\int e^{-r\lambda}\,d\mu_s.
\]
Here \(\varepsilon_s\ge0\), \(\mathcal E(\cdot,s)\) is completely monotone,
and the entrance equation gives
\[
\Pi=(\partial_s-\partial_r)\mathcal E,\qquad
\mu_s=\partial_s\varepsilon_s+\lambda\varepsilon_s.
\]
The weak-zero heat boundary reconstructs
\[
\mathcal E(r,s)=\int_0^s\Pi_{r+s-a}(a)\,da.
\]

## Correction and sharp survivor

The Laguerre kernel gives signed \(e^{-s\lambda}L_n^{(1)}(s\lambda)\) energy; it is closed.
Complete monotonicity still does not close q4. With
\[
L=s^{-9/11}\ell^{2/11},\quad A=\frac d2e^{-\int_0^sL},\quad
\mathcal E_\circ=Ae^{-rL},
\]
\[
\Pi^\circ_r=-ArL'e^{-rL}=\frac{Aa(s)}s(rL)e^{-rL}>0.
\]
Taking \(M=(sL)^{-1}\), \(Y^2=AL/\nu\) recovers the exact q4
power--log tails, \(MY^2\asymp s^{-1}\), all diagonal/recycling laws,
and an early-history fraction tending to one.

## Actual quadratic compatibility

For every \(n^2-3m^2=1\), an explicit divergence-free torus triad has
\[
Q_{n,m}(r)=\frac{nm}{2}e^{-8\nu m^2r}(1-e^{-2\nu r})>0,
\]
\[
Q_{n,m}\!\left(\frac{x}{8\nu m^2}\right)\to\frac{\sqrt3}{8}xe^{-x}.
\]
Thus adjacent-shell quadratic transfer has the survivor's heat shape,
but the Pell fields are snapshots and the shell ledger is not a velocity.

## Exact live question

Can \(\mu_s=\partial_s\varepsilon_s+\lambda\varepsilon_s\) sustain
repeated positive adjacent-shell triads along one q4 NSE trajectory?

## Next bounded cycle

Differentiate a fixed energy quantile of \(\varepsilon_s\). Derive its
shell-speed law from the triad density, then test whether the moving-shell
survivor forces a nonintegrable speed/genealogy cost against finite
unweighted dissipation. Use smooth shells before invoking spatial
capacity or the strong-trace drift.

All results await review. Keep slower clocks, divergent energy, and R3B separate.
