# Review response: balanced finite-amplitude pressure window

**Date:** 2026-07-24
**Route:** ROUTE-R3B
**Verdict:** valid after minor scope and notation repairs
**Clay status:** unsolved

The independent adversarial reviewer audited the thirteen links in
`review-letter-adjoint-pressure-amplitude-window-2026-07-24.md` (archived in Git at `c277792`)
against
[the theorem](experiments/adjoint-pressure-amplitude-window.md), its
reviewed predecessors, and the executable ledger.

No invalid mathematical implication was found. The reviewer independently
confirmed:

1. the pointwise softened-polar modular bound and the resulting
   \(C/(L\varepsilon_h)\) spatial \(L^2\) ceiling;
2. the Bernstein-ball cost \(\alpha^5K^{-3}\);
3. the \(27\)-class grid colouring and active-cell count
   \[
   N\lesssim\frac{K^3}{L\varepsilon_h\alpha^5};
   \]
4. Borel measurability of the moving threshold family and applicability
   of the moving-grid capture theorem;
5. the exact cancellation
   \[
   h^{7/4}K^{1/2}\varepsilon_h^{-1/6}
   \asymp\theta_h^{-1/6};
   \]
6. optimisation at \(\alpha=L^{-1/11}\);
7. retention of at least \(5p_{\rm pol}/8\) after subtraction and smooth
   amplitude cutoff;
8. the algebraic closed-ball window map and transfer of strong local
   spacetime \(L^2\) law tightness.

Two repairs were required and accepted.

## Repair 1: support notation

The opening summary originally advertised the interval
\([r_-,r_+]\), while the smooth cutoff constructed later is supported in
\([r_-/2,2r_+]\). The summary and final consequence now state the actual
support.

## Repair 2: signed-observable semantics

The theorem now explicitly writes

\[
W_h
=
\chi(r)m_{L_0}(r)\zeta_h^{(1)},
\qquad
m_L(r)
=
1-\frac{\sqrt{r^2+1}}{\sqrt{r^2+L^2}}.
\]

The weight \(m_L\) is positive but nonconstant. The proved conclusion is
therefore:

> A fixed compactly supported smooth test of the net signed amplitude
> observable retains positive finite-band pressure charge.

It is not decay of absolute pressure mass at large amplitude and not
positivity of the raw indicator-truncated polar on one amplitude
interval.

With this boundary, infinite relative amplitude cannot be the sole
carrier of the positive mark in the signed-observable, vague-amplitude
sense. Global amplitude compactness, uncharged Oseen-product
concentration, the moving pressure trace, the strict sub-\(h^9\) branch,
and every Clay alternative remain open.

## Accepted theorem scope

On every balanced first-hitting charged finite-band subsequence,

\[
\left|
\int\zeta_h^{(L)}\cdot H_h
\right|
\le CL^{-1/11}.
\]

One fixed compact relative-amplitude observable consequently retains a
uniform positive signed pairing. On the additionally norm-gated path,
its rooted profile laws inherit the previously established strong local
spacetime \(L^2\) tightness. No pressure-trace passage or limiting Oseen
equation is asserted.

The focused ledger tests, the full repository checks, and
`git diff --check` passed in the review.
