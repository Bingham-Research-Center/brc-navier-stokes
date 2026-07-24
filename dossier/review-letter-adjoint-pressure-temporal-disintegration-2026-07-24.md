# Independent review request: temporal disintegration of the signed pressure law

**Date:** 2026-07-24
**Route:** ROUTE-R3B
**Clay status:** unsolved

Please review
[the proposed temporal-disintegration reduction](experiments/adjoint-pressure-temporal-disintegration.md)
against its independently reviewed inputs:

- [Kato-polar signed aggregate](experiments/adjoint-pressure-signed-aggregate.md);
- [direct-response reduction](experiments/adjoint-pressure-direct-response.md);
- [frequency-or-maximal-dust reduction](experiments/adjoint-pressure-feedback-dust.md).

Executable ledgers are:

- `lab/navier_lab/adjoint_pressure_temporal.py`;
- `lab/tests/test_adjoint_pressure_temporal.py`.

The proposed theorem makes no Clay-resolution claim. It claims a stronger
mass-gain stopping selection, a quadratic upper ceiling on the selected
Kato regularisation, branch-dependent time-set capture estimates, and a
finite-band Lebesgue-time disintegration.

## Questions requiring adversarial recomputation

Please identify the earliest fatal implication, if any. In particular,
check the following links rather than accepting the displayed powers.

1. **Stopped feedback energy.** Does the proof of the reviewed estimate
   \[
   \sup_{\tau\le h}\|r(\tau)\|_2^2
   +\nu\int_0^h\|\nabla r\|_2^2\lesssim h^2
   \]
   legitimately rerun at every \(0<t\le h\) to give
   \(\|r(t)\|_2^2\lesssim t^2\), with constants independent of the
   selected layer?

2. **Mass-gain floor.** Does the existing running-\(L^1\) stopping proof
   give
   \[
   \sup_{\varepsilon,s}
   \bigl[L_\varepsilon(a(s))-L_\varepsilon(\varphi)\bigr]\ge q_0,
   \]
   rather than only positive completed Kato-polar work?

3. **Early--late quantifiers.** Is the dichotomy based on the relaxed
   mass-gain functional exhaustive with the stated event/genealogy
   quantifiers? In the late branch, may the same \(\varepsilon\) be held
   fixed between \(\eta T_0\) and the selected stopping time so that the
   nonnegative Kato remainder gives the signed late work?

4. **Schwartz detector tail.** Since the preferred detector is
   band-limited Schwartz rather than compactly supported, do the fixed-ball
   Lipschitz estimate and fixed \(L^1\) tail correctly transfer a positive
   mass gain to
   \(\int\rho_{\varepsilon_h}(w_h(h))\)?

5. **Quadratic regularisation ceiling.** From
   \[
   \rho_\varepsilon(z)
   \le |z|^2/(2\varepsilon),
   \qquad
   \|w_h(h)\|_2\le F_\varphi h,
   \]
   is the direction
   \(\varepsilon_h\lesssim h^2\) correct? Check that the theorem does not
   accidentally use it as a lower bound.

6. **Cloud volume and cells.** Does
   \(\rho_\varepsilon\le|\cdot|\) give the \(h^{-2}\) capture-volume floor
   and hence \(h^{-7/2}\) cells at
   \(\ell=\kappa^{-1}\sqrt h\)? Does the smooth solenoidal scaling model
   genuinely saturate all three powers without being represented as a PDE
   solution? Also check the band-resolved curl construction: does it put
   an order-one polar component at \(K_h\), spend only \(O(h^2)\)
   spacetime gradient energy, and permit arbitrarily many temporal sign
   changes only as a kinematic no-go rather than a PDE claim?

7. **High-coefficient time capture.** On a scaled time set
   \(A\subset[0,1]\), do pointwise feedback energy, Hardy div--curl,
   \(E_{\rm hi}\lesssim h^{-3}\), and pressure-mass normalisation give
   \[
   \nu_h^{\rm hi}(A)^2
   \lesssim
   \left(\int_A s^2\,ds\right)\eta_h(A),
   \]
   where \(\eta_h\) is normalised high-frequency energy time? Does a
   common weak limit satisfy
   \(g_{\rm hi}^2\lesssim s^2e_{\rm hi}\), and hence
   \(g_{\rm hi}/s\in L^2\) and terminal-edge mass
   \(O(\delta^{3/2})\)?

8. **Finite-band mixed capture.** Recompute the two weighted factors on
   \(hA\). Do they give
   \[
   h^{3/2}\left(\int_A s^2\,ds\right)^{1/2}
   \quad\hbox{and}\quad
   h^{1/2}|A|^{1/2}K^{1/2}N^{1/6},
   \]
   and hence
   \[
   h^{7/4}
   \left(
   |A|\int_A s^2\,ds
   \right)^{1/2}
   N^{1/6}
   \]
   after
   \(K=\kappa h^{-1/2}\)?

9. **Macro-coordinate conversion.** With
   \(\delta_h=\ell/R=\kappa^{-1}h^{7/2}\), does the preceding estimate
   become
   \[
   \Gamma_h(A\times E\times\mathfrak M)
   \lesssim
   \left(
   |A|\int_A s^2\,ds
   \right)^{1/2}
   |E|^{1/6}
   \]
   for macro-grid unions uniformly in \(h\), with fixed
   \(\kappa\)-dependence absorbed into the constant? Is arbitrary Borel
   \(E\) correctly deferred to the weak limit?

10. **Support and weak limit.** Is the already proved off-diagonal tail
    strong enough to put every finite-band weak limit inside one fixed
    source-coordinate ball, so that taking the whole spatial support in
    the rectangle estimate yields a time density bounded by \(Cs\)?

11. **Disintegration and slices.** Does the rectangle estimate pass to a
    Lebesgue-time disintegration \(ds\,\Gamma_s\)? Can a countable rational
    box argument legitimately give, for almost every common time,
    \[
    \mu_s(E)\lesssim s|E|^{1/6}
    \quad\hbox{for all Borel }E,
    \]
    and hence a weak-\(L^{6/5}\) density of norm at most \(Cs\) for the
    unnormalised spatial slice? Does this give terminal-edge mass
    \(O(\delta^2)\)? Check the warning about division by a small slice
    mass.

12. **Positive aligned times.** Does positive integrated effective-polar
    alignment plus the \(L^\infty\) slice-mass ceiling imply a
    positive-Lebesgue-measure set of times with positive slice alignment?

13. **Logical boundary.** Does any sentence overstate temporal
    compactness, a limiting Oseen law, event additivity, branch exclusion,
    regularity, breakdown, or a Clay alternative?

## Requested verdict

Please return:

1. the earliest fatal flaw, if one exists;
2. every repair needed for a valid conditional theorem;
3. a link-by-link verdict on the thirteen questions;
4. the strongest conclusion that survives;
5. the exact remaining gate after repair.

Please do not edit repository files.
