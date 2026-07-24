# Adversarial review request: finite-band bulk pressure participation

**Date:** 2026-07-24
**Route:** ROUTE-R3B
**Claimed status:** conditional analytic reduction; review pending
**Clay status:** unsolved

Please review
[the repaired trace-participation theorem](experiments/adjoint-pressure-trace-participation.md)
as a hostile mathematical referee. Its scope is the independently
reviewed norm-gated balanced first-hitting charged finite-band branch.

The first submitted version is withdrawn. Its \(Ch\) pressure
\(L^2\)-squared estimate was valid, but its claimed \(h^7\)-duty sharp
model violated the moving-grid capture theorem: the time-dependent
active selector contained only \(h^{-7/2}\) cells and therefore had
capture ceiling \(Ch^{7/6}\), not order one.

The repaired claim uses that failure to prove the stronger
source-volume modulus

\[
\int_F|H_h|
\le
C_B\min\left\{
1,
\left(\frac{|F|}{hR^3}\right)^{1/7}
\right\},
\qquad
F\subset(0,h)\times B_{BR},
\]

where
\[
K=\kappa h^{-1/2},
\qquad
\ell=K^{-1},
\qquad
R=h^{-3}.
\]

It then claims that the thresholded positive compact-window alignment
occupies a fixed source-cylinder fraction:

\[
|E_h|\ge c hR^3\asymp ch^{-8}.
\]

Finally it claims that a fixed positive fraction of the finite-band
pressure-root probability sees a compact-window profile bounded away
from zero in strong full-time, local-in-space \(L^2\). It does **not**
claim that
the signed pressure-selected point mark has yet been identified with an
evaluation of that limiting profile.

Please audit these links independently:

1. the two low-pass factors and high-pass projection place \(H_h\) in
   one fixed annulus \(c_AK\le|\xi|\le C_AK\);
2. a Schwartz reproducing kernel therefore gives
   \[
   |H_h(t,x)|
   \le
   C\ell^{-3}
   \int(1+K\operatorname{dist}(y,Q_m))^{-N}|H_h(t,y)|\,dy
   \]
   for \(x\in Q_m\);
3. the corresponding cell weights have a lattice-summable overlap,
   \(\sum_mw_m(t)\lesssim\|H_h(t)\|_1\);
4. if \(F\) has relative density at most \(\lambda\) in a cell, its
   contribution is at most \(C\lambda Z_h\);
5. the high-density cells form a measurable moving family with
   \(N_\lambda(t)\le|F_t|/(\lambda\ell^3)\);
6. Jensen gives
   \[
   \int_0^hN_\lambda(t)^{1/3}\,dt
   \le
   h\left(
   \frac{\mathfrak d_h(F)N_{\rm src}}{\lambda}
   \right)^{1/3};
   \]
7. the full variable-count moving-grid theorem, rather than its
   fixed-\(N_*\) corollary, gives the high-density bound;
8. the scale factor cancels exactly:
   \[
   h^{3/2}(Kh)^{1/2}N_{\rm src}^{1/6}
   =
   h^2KR^{1/2}
   \asymp1;
   \]
9. optimisation at
   \(\lambda=\mathfrak d_h(F)^{1/7}\) proves the one-seventh modulus;
10. exterior removal, the fixed \(|W_h|\ge\eta\) threshold, and
    positive-part selection retain a fixed amount of absolute pairing;
11. applying the modulus to that set proves
    \(|E_h|\gtrsim hR^3\), while first-hitting mass gives the matching
    upper scale;
12. grouping cells by their full spacetime alignment duty \(q_m\)
    shows that fixed charge cannot live only in cells with
    \(q_m\to0\);
13. for a root in a cell with \(q_m>\delta_0\), the rooted
    \(W_h\)-profile has
    \(L^2((0,1)\times B_{\sqrt3})^2\ge\eta^2\delta_0\);
14. the pressure-root probability of those cells is uniformly positive,
    and strong-topology tightness plus the closed-set Portmanteau
    inequality retains this in every limiting window-profile law;
15. the old moving-tube ledger is now correctly rejected because its
    moving selector has ceiling \(h^{7/6}\);
16. the remaining disclaimer is exact: nonzero profile-law occupation
    is weaker than conditional pressure-trace identification, Oseen
    product closure, or a nonzero Oseen solution.

Please return the first invalid implication, every hidden measurability
or Fourier-support assumption, any incorrect use of Portmanteau, and
the narrowest defensible description of what kind of moving trace has
actually been excluded.
