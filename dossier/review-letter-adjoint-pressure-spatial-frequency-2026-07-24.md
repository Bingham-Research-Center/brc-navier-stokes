# Independent review request: spatial-shell/frequency-tail amplification

**Date:** 2026-07-24
**Route:** ROUTE-R3B
**Clay status claimed by author:** unsolved

Please review
`dossier/experiments/adjoint-pressure-spatial-frequency.md`
adversarially.  The proposed theorem combines three independently
reviewed inputs:

1. the zero-data state energy and exterior \(L^2_{t,x}\) tail;
2. the spatial shell coefficient caps and logarithmic shell sum; and
3. the \(S/F\) high--high-to-low terminal-return gain.

The new analytic step is the off-diagonal Littlewood--Paley estimate
(16), which localises the high state to the same spatial annulus as the
coefficient up to \((FL)^{-2}\) leakage.

Please try to falsify, in particular:

1. the exact support identity leading to (17);
2. the two off-diagonal estimates (18)--(19), including whether
   annular Bernstein can be used with the stated local factors;
3. the \(F^{-1}\), rather than merely \(F^{-1/2}\), summation in (21);
4. applicability of the inner gradient budget (11) on the exterior
   feedback branch;
5. the shell error sum \(h^6F^{-2}\) in (24);
6. the complete estimate (25) and inversion to
   \(\log(D_bh^3)\gtrsim(F/S)h^{-7/4}\);
7. the exponent \(7/4+\alpha_{\rm dep}\) at the dyadic logarithmic
   depth; and
8. every scope boundary, especially the explicit refusal to infer
   frequency ascent from causal interaction depth.

Please classify the disposition as:

- valid in the exact stated scope;
- repairable, with precise corrections; or
- invalid, identifying the first fatal implication.

The executable exponent audit is:

```bash
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_spatial_frequency -v
make adjoint-pressure-spatial-frequency
```
