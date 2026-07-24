# Adversarial review request: stretched feedback history ledger

**Date:** 2026-07-24
**Route:** ROUTE-R3B
**Clay status:** unsolved

Please audit the proposed ledger-realisation theorem in
[the experiment note](experiments/adjoint-pressure-stretched-history.md).
This request is deliberately narrower than a Navier--Stokes review. The
claim is that the presently available scalar history data are compatible,
not that a PDE trajectory realises them.

## Proposed theorem

For

\[
p=\frac74,\qquad c>0,\qquad a>1,\qquad h_j\downarrow0,
\]

define

\[
\begin{aligned}
D_j&=h_j^{-3}e^{ch_j^{-p}},\\
\sigma_j&=h_j^3e^{-ach_j^{-p}},\\
\lambda_j&=e^{-ach_j^{-p}},\\
\rho_j&=e^{-(a-1)ch_j^{-p}},\\
\delta_j&=h_j^7e^{-2ach_j^{-p}}.
\end{aligned}
\]

The note claims that one nonnegative
\(e\in L^1(0,\delta_1)\) can satisfy

\[
\int_0^{\delta_j}e(s)\,ds=\rho_j=\sigma_jD_j
\]

for every \(j\), while

\[
\frac{\sigma_j}{\lambda_j}=h_j^3,\qquad
\frac{\lambda_j}{\rho_j}=e^{-ch_j^{-7/4}},
\]

and

\[
\frac{\delta_j}{\lambda_j^2}=h_j^7,\qquad
\frac{\delta_j}{\rho_j^2}
=h_j^7e^{-2ch_j^{-7/4}}.
\]

The construction linearly interpolates the decreasing nodes
\((\delta_j,\rho_j)\) and takes the almost-everywhere derivative.

## Questions requiring an explicit verdict

1. Are \(\delta(h)\) and \(\rho(h)\) strictly increasing functions of
   \(h\), so that every strictly decreasing \(h_j\) gives valid nested
   nodes?
2. Is the countably piecewise-affine interpolation genuinely absolutely
   continuous at the accumulation point \(0\), with derivative in
   \(L^1\), rather than merely continuous and monotone?
3. Do all four scale and clock identities follow exactly from the
   definitions?
4. Does
   \[
   \sigma_j=o(h_j^3e^{-ch_j^{-7/4}})
   \]
   hold exactly as claimed?
5. Is the fresh-increment telescope
   \[
   \sum_j\int_{\delta_{j+1}}^{\delta_j}e
   =\rho_1
   \]
   compatible with infinitely many cumulative normalisations
   \(\rho_j^{-1}\int_0^{\delta_j}e=1\)?
6. Does the note ever overreach from a scalar ledger realisation to a
   velocity field, local-energy solution, pressure, or Navier--Stokes
   construction?
7. Is the route consequence stated at the correct strength: finite raw
   dissipation, absolute continuity, nesting, and the exact scale map
   alone cannot exclude the stretched-exponential branch, so a genuinely
   PDE, non-reusable signed, ancestry, or interaction-order input remains?

Please look specifically for a hidden failure of absolute continuity, a
reversed interval ordering, reuse of the wrong physical scale, or an
implicit assumption that cumulative event packets are disjoint.

## Executable checks

```bash
make adjoint-pressure-stretched-history
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_stretched_history -v
make records
make links
make markup
git diff --check
```

The executable is only an algebra and finite-interpolation certificate;
the infinite absolutely continuous construction must be checked from
the proof.
