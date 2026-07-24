# Adversarial review request: balanced finite-amplitude pressure window

**Date:** 2026-07-24
**Route:** ROUTE-R3B
**Claimed status:** conditional analytic reduction; review pending
**Clay status:** unsolved

Please review
[the amplitude-window theorem](experiments/adjoint-pressure-amplitude-window.md)
as a hostile mathematical referee. The intended scope is only the
balanced first-hitting charged finite-band branch already constructed in
the independently reviewed predecessor notes. The strong-profile
consequence additionally assumes the norm-gated path of the balanced
compactness theorem.

The new claim is:

\[
\left|
\int\zeta_{L\varepsilon_h}(a_h)\cdot H_h
\right|
\le CL^{-1/11},
\]

uniformly in \(h\), and consequently one fixed smooth compact window in
the relative amplitude \(|a_h|/\varepsilon_h\) retains positive
finite-band pressure charge.

Please audit these links independently:

1. the pointwise inequality
   \[
   |\zeta_{L\varepsilon}(a)|^2
   \le \frac2L
   \left(\sqrt{1+|a|^2/\varepsilon^2}-1\right);
   \]
2. the use of first-hitting mass to obtain
   \(\|\zeta_{L\varepsilon_h}\|_2^2\lesssim(L\varepsilon_h)^{-1}\);
3. the Bernstein-ball argument, including the
   \(\alpha^5K^{-3}\) local \(L^2\) cost and the \(27\)-colour
   disjointness step;
4. the time-uniform active-cell count
   \(N\lesssim K^3/(L\varepsilon_h\alpha^5)\);
5. measurability and applicability of the reviewed moving-grid capture
   estimate to that active family;
6. self-adjointness of the real even \(Q_K\) and the identity
   \(Q_KH_h=H_h\);
7. cancellation of all powers of \(h\) when
   \(K\asymp h^{-1/2}\) and
   \(\varepsilon_h=\theta_hh^9\);
8. optimisation at \(\alpha=L^{-1/11}\);
9. retention of positive charge by
   \(\beta_h^{(L)}=\zeta_{\varepsilon_h}-\zeta_{L\varepsilon_h}\);
10. the small- and large-relative-amplitude bounds used to replace the
    soft window by a genuinely compact smooth window;
11. the algebraic formula
    \[
    \mathcal B_L(z)
    =
    z\left[
    1-
    \bigl(|z|^2+L^2(1-|z|^2)\bigr)^{-1/2}
    \right]
    \]
    and smooth extension of the hard window on the closed unit ball;
12. transfer of strong local spacetime \(L^2\) tightness through this
    fixed Lipschitz map;
13. the exact semantic boundary: only the charged observable is
    protected from infinite-amplitude concentration; global amplitude
    compactness, Oseen product closure, and the moving pressure trace
    remain open.

A useful adverse verdict should identify the first invalid implication,
any missing hypothesis, any incorrect constant or exponent, or any
overstatement of what the window localisation closes.
