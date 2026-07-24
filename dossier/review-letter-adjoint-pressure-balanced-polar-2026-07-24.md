# Independent review request: balanced Kato-polar compactness

**Date:** 2026-07-24
**Route:** ROUTE-R3B
**Clay status:** unsolved

Please adversarially review the proposed
[balanced-polar compactness theorem](experiments/adjoint-pressure-balanced-polar.md)
against its independently reviewed inputs:

- [signed Kato-polar aggregate](experiments/adjoint-pressure-signed-aggregate.md);
- [temporal disintegration](experiments/adjoint-pressure-temporal-disintegration.md);
- [first-hitting polar vacuum](experiments/adjoint-pressure-polar-vacuum.md).

The claimed advance is deliberately narrow. On the norm-gated charged
first-hitting finite-band path, after the direct and exterior
\(L^1_{t,x}\)-norm gates have been rejected, suppose

\[
0<\theta_-
\le\varepsilon_h/h^9
\le\theta_+<\infty,
\]

the pressure-rooted regularised polar profiles are claimed to be tight in
strong local spacetime \(L^2\). No amplitude-normalised Oseen limit,
pressure-trace identification, event telescope, regularity theorem, or
Clay conclusion is claimed.

## Links requiring independent verification

Please check each implication rather than accepting the exponent ledger.

1. **Full pressure upper bound.** Does following the reviewed branch tree
   all the way to the finite-band child really give
   \[
   \int_0^h\|\nabla\pi_h^*\|_1\le C?
   \]
   In particular, verify that the absent direct and exterior children
   contribute bounded norms and that
   \[
   \|\mathcal T(r,b^{\rm in})\|_{L^1_{t,x}}
   \lesssim
   (h^3)^{1/2}(h^{-3})^{1/2}
   \lesssim1.
   \]

2. **Kato upper budget.** Check the sign in the first-hitting identity and
   whether the full pressure upper bound implies
   \(\int\mathcal K_{\varepsilon_h}(a_h)\le C\).

3. **Rooted scaling factors.** Recompute
   \[
   \mathfrak O
   =
   \frac1{\varepsilon h\ell^3}\int\rho_\varepsilon,
   \quad
   \mathfrak K
   =
   \frac1{\varepsilon h\ell}\int\mathcal K_\varepsilon,
   \quad
   \mathfrak P
   =
   \frac1{\varepsilon\ell^3}\int|\nabla\pi^*|.
   \]

4. **Cell counts.** With \(\ell\asymp h^{1/2}\) and
   \(\varepsilon\asymp h^9\), verify that all three bad-root counts are
   \(O(L^{-1}h^{-21/2})\), including fixed enlargement and overlap.

5. **Pressure-probability tail.** Check that the finite-band capture law
   applies to those fixed bad cube families and gives exactly
   \(CL^{-1/6}\), with no hidden \(h\)-power or dependence on root time.

6. **Polar differential algebra.** Verify
   \[
   |\nabla\mathsf Z|^2\le\mathcal K_\Phi(A),
   \]
   the formula and constant in
   \[
   |D^3\Phi(A)[v,v]|
   \le4\,v\cdot D^2\Phi(A)v,
   \]
   and every sign in the transformed polar equation.

7. **Time derivative space.** Check the Lorentz product
   \(L^{3,\infty}L^2\to L^{6/5,2}\), its use as an element of
   \(W^{-1,6/5}\) on bounded balls, and the treatment of the \(L^1\)
   curvature and pressure terms.

8. **Aubin--Lions in probability.** Verify that the
   \(L^{-1/6}\) action tails on a countable ball exhaustion genuinely
   imply tightness of the pushed-forward profile laws in strong
   \(L^2_{\rm loc}\), and hence the stated temporal-translation limit.

9. **Limit amplitude statement.** Decide whether finite local
   \(\int\Phi(A_h)\) and strong polar convergence justify only the regular
   amplitude
   \[
   A^{\rm reg}=\mathsf Z/\sqrt{1-|\mathsf Z|^2}\in L^1_{\rm loc},
   \]
   while still allowing a lost concentration measure.

10. **Trace countermodel.** Check the moving-bump calculation:
    strong spacetime profile convergence, fixed variation, Lebesgue
    averaged time marginal, and fixed self-weighted trace.

11. **Scope.** Reject any wording that upgrades profile-law tightness to
    amplitude compactness, identifies the pressure-weighted mark, closes
    the strict sub-\(h^9\) branch, or proves a Clay alternative.

## Requested verdict

Return one of:

- valid in the stated conditional balanced finite-band scope;
- repairable, with exact corrections;
- fatal, identifying the first invalid implication.

Please also run:

```bash
make adjoint-pressure-balanced-polar
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_balanced_polar -v
make check
git diff --check
```
