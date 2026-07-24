# Adversarial review request: product-law pressure-trace identification

**Date:** 2026-07-24
**Route:** ROUTE-R3B
**Claimed status:** conditional analytic reduction; review pending
**Clay status:** unsolved

Please review
[the product-trace theorem](experiments/adjoint-pressure-product-trace.md)
as a hostile mathematical referee. Its scope is the independently
reviewed norm-gated balanced first-hitting charged finite-band branch.

The claimed new conclusion is that the residual conditional moving
trace for the fixed compact window can be closed. If \(\rho\) is a
uniform-spatial-root strong profile law, then the limiting vector
finite-band pressure has

\[
d\boldsymbol\nu(s,z)
=
\boldsymbol f(s,z)\,ds\,d\rho(z),
\qquad
\boldsymbol f\in L^{7/6,\infty}(ds\,d\rho),
\]

and the complete compact-window mark satisfies

\[
-
\int
\mathscr E(z)(s)\cdot\boldsymbol f(s,z)
\,ds\,d\rho(z)
\ge p_{\rm win}>0.
\]

Here \(\mathscr E\) is the exact fixed-scale spatial reproduction of the
window, so no pointwise spatial evaluation is asserted.

Please audit these links independently:

1. Fubini over \(x\in B_{BR}\) gives the uniform-root mean factors
   \[
   (R^3\varepsilon_h)^{-1},
   \qquad
   \ell^2(R^3\varepsilon_hh)^{-1},
   \qquad
   (R^3\varepsilon_h)^{-1}
   \]
   for the modular, Kato, and full-pressure actions;
2. \(R=h^{-3}\), \(\varepsilon_h\asymp h^9\), and
   \(\ell^2\asymp h\) make all three factors scale free;
3. expectation bounds, Markov, the exact polar derivative estimate, and
   the full-time Aubin--Lions argument give tightness of uniform-spatial
   profile laws on
   \(L^2((0,1);L^2_{\rm loc}(\mathbb R^3))\);
4. the map \((t,x)\mapsto(t/h,\mathsf Z_{h,x})\) sends uniform
   source-cylinder measure exactly to \(ds\otimes\rho_h\), because the
   full profile depends on \(x\) but not on the independently chosen
   root time \(t\);
5. total variation under pressure pushforward is bounded by the
   reviewed \(D^{1/7}\) source-volume modulus;
6. this modulus makes the vector pressure measures tight whenever the
   product probabilities are tight;
7. the modulus passes to weak limits despite possible cancellation in
   vector measures; please check the layer-cake/continuous-vector-test
   argument rather than assuming convergence of total variations;
8. the limiting density exponent is exactly \(7/6\);
9. a measurable graph \(s=r(z)\) has zero
   \(ds\otimes\rho\)-measure and therefore zero limiting pressure mass;
10. the fixed-shape reproducing kernel gives
    \[
    Q_KW_h(hs,x)=
    \int q(y)\mathcal W(\mathsf Z_{h,x}(s,y))\,dy;
    \]
11. the map
    \(\mathscr E:\mathcal X_1\to L^2(0,1)\) is continuous, including the
    Schwartz tail outside every fixed spatial ball;
12. the exterior pressure tail justifies restricting both the raw and
    reproduced pairings to \(B_{BR}\);
13. time mollification makes
    \(G_\delta(s,z)\) bounded continuous on the product space;
14. compactness of the profile law makes the product-law \(L^2\)
    mollification error vanish uniformly along the extracted sequence;
15. splitting the error at height \(\gamma\), then using Chebyshev and
    the one-seventh modulus, makes the pressure-weighted error vanish;
16. weak convergence passes the mollified pairing and the two
    approximation limits recover the unmollified pairing;
17. the positive prelimit compact-window mark therefore survives as the
    displayed product-law pairing;
18. the claimed boundary is exact: this identifies the compact-window
    trace but not the unwindowed amplitude, drift, or pressure products,
    a limiting Oseen equation, the strict sub-\(h^9\) branch, or Clay
    A--D.

Please return the first invalid implication, any missing uniformity or
Polish-space hypothesis, every misuse of total variation or
Portmanteau, and the narrowest defensible interpretation of the limiting
pairing.
