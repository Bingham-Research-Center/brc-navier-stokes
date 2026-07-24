# Independent review request: fixed-band Oseen frequency colligation

**Date:** 2026-07-24

**Primary note:**
[`experiments/adjoint-pressure-frequency-colligation.md`](experiments/adjoint-pressure-frequency-colligation.md)

**Executable certificate:**
[`../lab/navier_lab/adjoint_pressure_frequency_colligation.py`](../lab/navier_lab/adjoint_pressure_frequency_colligation.py)

**Tests:**
[`../lab/tests/test_adjoint_pressure_frequency_colligation.py`](../lab/tests/test_adjoint_pressure_frequency_colligation.py)

**Clay status:** unsolved

## Requested verdict

Please decide whether the note proves the following narrow theorem without
overclaiming:

> For an arbitrary divergence-free drift uniformly bounded in
> \(L^{3,\infty}\), the Oseen Dyson paths projected back to one smooth
> annulus after every interaction have factorial depth decay in
> \(L^\infty_tL^1_x\), and their band-resolved linear pressure costs have
> a factorial tail on a parabolic window.

This is not asserted for the unprojected Oseen remainder or for the sum
over changing frequency itineraries.

## 1. Multiplier estimate

Please check that smooth annular localisation gives

\[
\|\Delta_Re^{\nu\tau\Delta}\mathbb P\operatorname{div}F\|_1
\le
K R e^{-c\nu R^2\tau}\|F\|_1
\]

and

\[
\|\Delta_R\mathbb Q\operatorname{div}F\|_1
\le KR\|F\|_1.
\]

Please also check the Lorentz product and Bernstein step

\[
\|z\otimes b\|_1
\lesssim
\|z\|_{L^{3/2,1}}\|b\|_{L^{3,\infty}}
\lesssim
MR\|z\|_1,
\]

for \(z\) supported in the selected annulus.

## 2. Time-simplex factorial

From the resulting bound

\[
\|\mathcal V_{R,b}z(t)\|_1
\le KMR^2\int_0^t\|z(s)\|_1\,ds,
\]

please verify

\[
\|\mathcal V_{R,b}^{\,m}q_R(t)\|_1
\le
Q_T\frac{(KMR^2t)^m}{m!}
\]

and

\[
\int_0^T
\|\mathcal C_{R,b}\mathcal V_{R,b}^{\,m}q_R(t)\|_1\,dt
\le
Q_T\frac{(KMR^2T)^{m+1}}{(m+1)!}.
\]

Does \(T\le\Lambda/(\nu R^2)\) make the tail uniform in \(R\), with
dimensionless action \(KM\Lambda/\nu\)?

Please also check the logarithmic-depth corollary: if
\(N(h)=\lfloor c\log(1/h)\rfloor\), \(R_h^2h=O(1)\), and the input
band has at most polynomial \(L^1\) growth, Stirling makes the fixed-band
pressure tail vanish with dominant logarithm
\(-c\log(1/h)\log\log(1/h)\).

## 3. Plane-wave ray

For \(b=\beta e^{ik\cdot x}\), \(k\cdot\beta=0\), and
\(k\times\xi_0\ne0\), please check:

1. \(\beta\cdot(\xi_0+jk)\) is constant;
2. the normal polarisation never leaks to pressure;
3. the in-plane leakage along a one-sided affine frequency ray is
   \[
   |a_0^\parallel|
   \left(\prod_{j=1}^m|\cos\delta_j|\right)
   |\sin\delta_{m+1}|;
   \]
4. monotone angular variation gives total linear leakage below
   \(\pi|a_0^\parallel|\).

## 4. Backtracking audit

For

\[
\xi_\pm=(n^2-1,\pm2n,0),
\qquad
k=(0,4n,0),
\]

please recompute the exact \(c_n,s_n\), the unweighted sum

\[
\frac{s_n}{1-c_n}=\frac{n^2-1}{2n},
\]

and the \(h_n=c_n\) heat-weighted sum

\[
\frac{1}{s_n}\sim\frac n4.
\]

Please check the effective parabolic time and the coefficient audit

\[
\frac{-\log c_n}{1-c_n^2}\to\frac12,
\qquad
\frac{B_n}{R_n}\sim\frac{n^2}{8}
\quad\text{for unit integrated Duhamel action},
\]

whereas \(B_n=MR_n\) gives action \(\sim8M/n^2\).

The note now labels this last comparison as a local
\(\mathbb R^3\) packet-scaling audit, not an exact uniformly
weak-\(L^3\) torus plane-wave family.

The intended conclusion is only that pure normalised angle/heat geometry
can mislead unless the actual coefficient-time action is retained.

## 5. Scope

Please reject the note if it implicitly claims any of the following:

- summability of all changing-band frequency paths;
- an unconditional bound for the full unprojected pressure \(L^1\) norm;
- a Navier--Stokes same-trajectory frequency law;
- regularity, feedback exclusion, or a Clay alternative A--D.

## Reproduce

```bash
make adjoint-pressure-frequency-colligation
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_frequency_colligation -v
make check
```
