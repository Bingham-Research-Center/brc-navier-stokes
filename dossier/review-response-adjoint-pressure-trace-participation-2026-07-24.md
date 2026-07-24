# Review response: finite-band bulk pressure participation

**Date:** 2026-07-24
**Route:** ROUTE-R3B
**Verdict:** valid in the stated conditional scope after one topology repair
**Clay status:** unsolved

The independent adversarial reviewer audited
[the repaired theorem](experiments/adjoint-pressure-trace-participation.md)
against
[the review request](review-letter-adjoint-pressure-trace-participation-2026-07-24.md).
No invalid implication remains.

## Disposition of the first submission

The first \(h^7\)-participation version is withdrawn. Its preliminary

\[
\int_0^h\|H_h(t)\|_2^2\,dt\lesssim h
\]

estimate was valid, but its proposed sharp moving tube checked only
fixed cell families. The cells active at each time form a legal moving
selector of size \(h^{-7/2}\), whose reviewed capture ceiling is

\[
Ch^{7/4}(h^{-7/2})^{1/6}
=Ch^{7/6}\longrightarrow0.
\]

It therefore cannot carry the model's asserted order-one pressure mass.
The executable ledger now records this as a rejected countermodel.

## Accepted repaired theorem

The reviewer accepted all of the following links:

1. the low-pass factors and high-pass projection put \(H_h\) in one
   fixed annulus \(K\lesssim|\xi|\lesssim C_AK\);
2. a scale-\(K\) reproducing kernel bounds \(H_h\) on each cell by
   lattice-summable weighted pressure mass;
3. the low-density part of any source-cylinder set costs
   \(C\lambda Z_h\);
4. the high-density cells form a measurable variable-count moving
   family;
5. Jensen and the full moving-grid theorem give the high-density cost
   \(C(\mathfrak d_h(F)/\lambda)^{1/6}\);
6. the scale factor cancels exactly because
   \(h^2KR^{1/2}\asymp1\);
7. \(\lambda=\mathfrak d_h(F)^{1/7}\) gives
   \[
   \int_F|H_h|
   \le
   C\min\{1,\mathfrak d_h(F)^{1/7}\};
   \]
8. exterior removal, a fixed \(|W_h|\)-threshold, and positive-part
   selection retain fixed compact-window charge;
9. that charge forces fixed source-cylinder participation,
   \[
   |E_h|\gtrsim hR^3\asymp h^{-8};
   \]
10. full-duty cell grouping gives fixed positive pressure-root
    probability of a window profile bounded away from zero.

## Topology repair

The initial profile corollary referred ambiguously to
\(L^2_{\rm loc}((0,1)\times\mathbb R^3)\). In its conventional meaning,
that topology can discard bumps concentrating at either time endpoint,
so the full-layer norm event need not be closed.

The underlying Aubin--Lions proof already gives compactness on
\((0,1)\times B_D\) for every \(D\). The theorem and its balanced-polar
input now name the exact topology

\[
\mathcal X
=
L^2\!\left((0,1);L^2_{\rm loc}(\mathbb R^3)\right),
\]

whose projective seminorms use the whole scaled time interval. In this
topology,

\[
\mathcal C_0
=
\left\{
w:
\|w\|_{L^2((0,1)\times B_{\sqrt3})}^2
\ge\eta^2\delta_0
\right\}
\]

is closed, and the reviewer confirmed the Portmanteau direction

\[
q_0
\le
\limsup_h\mu_h(\mathcal C_0)
\le
\mu(\mathcal C_0).
\]

## Exact retained boundary

The accepted conclusion is:

- fixed charge cannot concentrate on sets whose relative
  source-cylinder volume tends to zero;
- every limiting compact-window profile law assigns a fixed positive
  probability to nonzero full-time, local-in-space \(L^2\) profiles.

The theorem does **not** associate the pressure-root time with the
limiting profile, identify the signed point trace, close the unwindowed
Oseen products, construct a nonzero Oseen solution, close the strict
sub-\(h^9\) branch, or prove any Clay alternative A--D.

The remaining balanced gate is conditional signed-trace/profile
identification followed by closure of the unwindowed Oseen products.

## Validation

The reviewer ran:

- 10 focused trace-participation tests;
- all 591 repository tests;
- records, links, and mathematical-markup validation;
- `git diff --check`.

All passed.
