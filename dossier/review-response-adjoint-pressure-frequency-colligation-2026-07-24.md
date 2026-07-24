# Independent review response: fixed-band Oseen frequency colligation

**Date:** 2026-07-24

**Reviewed packet:**
[`review-letter-adjoint-pressure-frequency-colligation-2026-07-24.md`](review-letter-adjoint-pressure-frequency-colligation-2026-07-24.md)

**Primary theorem:**
[`experiments/adjoint-pressure-frequency-colligation.md`](experiments/adjoint-pressure-frequency-colligation.md)

**Verdict:** accepted after two scope precisions

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI re-derived the annular multiplier
estimate, Lorentz product step, ordered-simplex factorial, pressure
indexing, logarithmic-depth asymptotic, plane-wave geometry, rational
backtracking family, heat lifetime, and coefficient-action audit.  It
found the fixed-band theorem valid after two scope clarifications.

The result controls only the Oseen block re-filtered to the same annulus
after every interaction and the pressure observed in that annulus.  It
does not control the unprojected remainder, paths changing frequency
bands, pressure-band recombination, or a same-trajectory Navier--Stokes
law.

## Accepted analytic chain

For a smooth annular multiplier \(\Delta_R\), scaling its differentiated
heat--Leray symbol gives

\[
\|\Delta_Re^{\nu\tau\Delta}
\mathbb P\operatorname{div}F\|_1
\le
KR e^{-c\nu R^2\tau}\|F\|_1.
\]

The annular pressure multiplier has the corresponding bound

\[
\|\Delta_R\mathbb Q\operatorname{div}F\|_1
\le KR\|F\|_1.
\]

For annulus-supported \(z\), Lorentz Bernstein and O'Neil's product
inequality give

\[
\|z\|_{L^{3/2,1}}\le CR\|z\|_1,
\qquad
\|z\otimes b\|_1
\le C\|z\|_{L^{3/2,1}}\|b\|_{L^{3,\infty}}.
\]

Thus the band action is \(KMR^2\).  The ordered time simplex then yields

\[
\|\mathcal V_{R,b}^{\,m}q_R(t)\|_1
\le
Q_T\frac{(KMR^2t)^m}{m!},
\]

and

\[
\int_0^T
\|\mathcal C_{R,b}\mathcal V_{R,b}^{\,m}q_R(t)\|_1\,dt
\le
Q_T\frac{(KMR^2T)^{m+1}}{(m+1)!}.
\]

On \(T\le\Lambda/(\nu R^2)\), the action is at most
\(KM\Lambda/\nu\), uniformly in \(R\).  At
\(N(h)=\lfloor c\log(1/h)\rfloor\), Stirling gives the dominant tail
logarithm

\[
-c\log\frac1h\log\log\frac1h
+O\left(\log\frac1h\right),
\]

so the fixed-band tail vanishes even after any fixed polynomial input
loss.

## Accepted Fourier audit

On a non-collinear one-sided Fourier ray, the drift transport factor is
constant, the common normal polarisation never leaks, and the in-plane
linear pressure leakage is bounded by the finite monotone angular
variation, strictly below \(\pi\).

For

\[
\xi_\pm=(n^2-1,\pm2n,0),
\]

the reviewer recomputed

\[
c_n
=
\frac{n^4-6n^2+1}{(n^2+1)^2},
\qquad
s_n
=
\frac{4n(n^2-1)}{(n^2+1)^2},
\qquad
1-c_n
=
\frac{8n^2}{(n^2+1)^2}.
\]

The freely normalised backtracking sums are

\[
\frac{s_n}{1-c_n}
=
\frac{n^2-1}{2n},
\qquad
\frac{s_n}{1-c_n^2}
=
\frac1{s_n}
\sim\frac n4.
\]

Their effective parabolic lifetime tends to \(1/2\).  The exact
integrated pulse action is

\[
B_n(n^2-1)\frac{1-c_n}{(n^2+1)^2}.
\]

Unit action requires \(B_n/R_n\sim n^2/8\), whereas localised critical
packet scaling \(B_n=MR_n\) gives action \(\sim8M/n^2\).

## Scope precisions

1. The plane-wave ray now assumes \(k\times\xi_0\ne0\), preventing an
   undefined zero frequency or a collinear angle jump of exactly
   \(\pi\).
2. The exact integer-frequency geometry is toral, while the
   \(B_n=MR_n\) comparison is explicitly only a localised
   \(\mathbb R^3\) packet-scaling audit.  It is not an exact uniformly
   weak-\(L^3\) torus or Navier--Stokes family.

## Exact accepted frontier

The result proves:

> A logarithmically deep pressure-bearing remainder cannot persist by
> repeatedly interacting inside one comparable parabolic frequency
> block.  Any surviving Oseen frequency path must make a genuine
> unbounded scale excursion or exploit unresolved pressure-band
> recombination.

The remaining theorem must sum or rigidify changing-band itineraries,
couple their scale excursions to same-trajectory coefficient energy, or
identify them with physical event ancestry.

## Validation

- `make adjoint-pressure-frequency-colligation`: passed.
- Targeted executable tests: 12 passed.
- Reviewer full `make check`: 656 tests passed.
- Reviewer `git diff --check`: passed.
