# Review response: product-law pressure-trace identification

**Date:** 2026-07-24
**Route:** ROUTE-R3B
**Verdict:** valid in the stated conditional scope after Polish-space and
vector-variation repairs
**Clay status:** unsolved

The independent adversarial reviewer audited
[the repaired theorem](experiments/adjoint-pressure-product-trace.md)
against
`review-letter-adjoint-pressure-product-trace-2026-07-24.md` (archived in Git at `c277792`).
No invalid implication remains.

## Accepted theorem

On the independently reviewed norm-gated balanced first-hitting charged
finite-band branch, the reviewer accepted:

1. uniform spatial rooting gives scale-free mean modular, Kato, and
   full-pressure actions;
2. Markov's inequality, the transformed polar equation, and full-time
   Aubin--Lions compactness make the uniform-root profile laws tight;
3. adjoining an independent uniform scaled time gives the exact product
   law \(ds\otimes\rho_h\);
4. the reviewed source-volume modulus pushes forward as
   \[
   |\boldsymbol\nu_h|(A)
   \le C(ds\otimes\rho_h)(A)^{1/7};
   \]
5. this modulus survives vector-measure convergence and gives
   \[
   d\boldsymbol\nu
   =\boldsymbol f\,ds\,d\rho,
   \qquad
   \boldsymbol f\in L^{7/6,\infty}(ds\,d\rho);
   \]
6. every graph \(s=r(z)\) has zero limiting pressure mass;
7. the fixed-shape spatial reproducing kernel converts the compact
   window into a continuous profile-to-\(L^2\)-time observable;
8. temporal mollification is uniformly accurate on compact profile
   sets;
9. the one-seventh modulus converts product-law \(L^2\) error into
   vanishing pressure-weighted error; and
10. the complete spatially reproduced compact-window mark survives as
    the strictly positive pairing
    \[
    -
    \int_0^1\int_{\mathcal X_1}
    \mathscr E(z)(s)\cdot\boldsymbol f(s,z)
    \,d\rho(z)\,ds
    \ge p_{\rm win}>0.
    \]

## Repairs made during review

The theorem now states explicitly that the strong projective
\(L^2((0,1);L^2_{\rm loc})\) ambient space is separable and complete,
that the constraint \(|z|\le1\) is closed, and hence that
\(\mathcal X_1\) and
\(\mathcal Y=[0,1]\times\mathcal X_1\) are Polish. Translation
continuity also makes the prelimit root map Borel.

The vector-measure limit no longer risks suggesting convergence of
total variations. For continuous \(0\le\phi\le1\) and continuous vector
\(g\) with \(|g|\le\phi\), the proof first passes
\[
\left|\int g\cdot d\boldsymbol\nu_h\right|
\le
C\left(\int\phi\,d\overline m_h\right)^{1/7},
\]
then takes the continuous-vector supremum and uses Radon regularity to
recover the Borel-set modulus for \(\boldsymbol\nu\).

The profile-to-time observable is also assigned a jointly Borel
representative before the product-law pairings are written.

## Exact retained boundary

The density \(\boldsymbol f\) is the pushed-forward finite-band pressure
relative to independent Lebesgue time and the uniform-root profile law.
The positive pairing identifies the spatially reproduced compact-window
mark. It does **not** show that \(\boldsymbol f\) is a pressure
functional of \(z\), close the unwindowed amplitude, drift, or pressure
products, produce a limiting Oseen solution, close the strict
sub-\(h^9\) branch, or prove any Clay alternative A--D.

The remaining balanced gate is unwindowed product compactness and
identification sufficient to obtain an honest amplitude-normalised
Oseen limit, followed by a rigidity theorem.

## Validation

The reviewer ran:

- 8 focused product-trace tests;
- all 599 repository tests;
- records, links, and mathematical-markup validation;
- `git diff --check`.

All passed.
