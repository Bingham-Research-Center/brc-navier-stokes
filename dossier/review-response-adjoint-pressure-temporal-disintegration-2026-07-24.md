# Independent review response: temporal disintegration of the signed pressure law

**Date:** 2026-07-24

**Reviewed packet:**
[review request](review-letter-adjoint-pressure-temporal-disintegration-2026-07-24.md)

**Primary theorem:**
[temporal-disintegration reduction](experiments/adjoint-pressure-temporal-disintegration.md)

**Verdict:** valid in its stated conditional scope

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found no fatal implication in the proposed
mass-gain selection, quadratic Kato scale, temporal capture estimates, or
measure disintegration.

During review, retaining the exact scaled-time second moment sharpened the
initial statement. The accepted theorem is stronger than the first review
draft:

\[
\nu_h^{\rm hi}(A)^2
\le
C
\left(\int_A s^2\,ds\right)\eta_h(A)
\]

for the coupled high-coefficient pressure and energy-time laws, while

\[
\Gamma_h^{\rm fb}(A\times E\times\mathfrak M)
\le
C
\left(
|A|\int_A s^2\,ds
\right)^{1/2}
|E|^{1/6}
\]

for finite-band macro-grid unions. The reviewer recomputed and accepted
both sharpenings.

The theorem does not prove temporal continuity, a limiting Oseen equation,
event additivity, a finite budget, branch exclusion, regularity,
breakdown, or any Clay alternative A--D.

## Accepted mathematical chain

The reviewer checked the following links.

1. The reviewed zero-data feedback-energy proof may be stopped at every
   \(0<t\le h\), giving
   \[
   \|r(t)\|_2^2
   +\nu\int_0^t\|\nabla r\|_2^2
   \lesssim t^2
   \]
   with constants uniform over the selected layers.

2. The existing running-\(L^1\) stopping proof retains actual regularised
   mass gain:
   \[
   \sup_{\varepsilon,s}
   \left[
   L_\varepsilon(a(s))-L_\varepsilon(\varphi)
   \right]
   \ge q_0.
   \]

3. The relaxed mass-gain early--late alternative is exhaustive with the
   inherited event and common-genealogy quantifiers. In the late branch,
   retaining the same \(\varepsilon\) at both endpoints and the
   nonnegative Kato remainder gives the positive stopped late work.

4. A fixed \(L^1\) tail radius for the band-limited Schwartz detector,
   together with the fixed-ball \(O(h)\) difference estimate, transfers
   terminal mass gain to
   \[
   \int\rho_{\varepsilon_h}(w_h(h))
   \ge\frac{3\gamma}{4}.
   \]

5. The inequality
   \[
   \rho_\varepsilon(z)\le\frac{|z|^2}{2\varepsilon}
   \]
   and \(\|w_h(h)\|_2\le F_\varphi h\) give the correctly directed
   ceiling
   \[
   \varepsilon_h
   \le
   \frac{2F_\varphi^2}{3\gamma}h^2.
   \]

6. Every fixed-mass Kato capture has volume at least \(ch^{-2}\) and
   needs at least \(c\kappa^3h^{-7/2}\) descendant cells. The smooth
   solenoidal models saturate the stated powers. The band-resolved curl
   carrier has \(O(h^2)\) spacetime gradient cost and permits arbitrarily
   many effective-polar sign flips at bulk roots, but is correctly
   labelled kinematic rather than Oseen, Navier--Stokes, or
   pressure-coupled.

7. For the charged high-coefficient branch, weighted Hardy
   Cauchy--Schwarz gives
   \[
   \nu_h^{\rm hi}(A)^2
   \le
   C
   \left(\int_A s^2\,ds\right)\eta_h(A).
   \]
   The continuous-cutoff form passes under common weak convergence.

8. If
   \[
   d\nu^{\rm hi}=g_{\rm hi}\,ds,
   \qquad
   d\eta=e_{\rm hi}\,ds+d\eta^\perp,
   \]
   Lebesgue differentiation gives
   \[
   g_{\rm hi}(s)^2
   \le Cs^2e_{\rm hi}(s)
   \quad\hbox{almost everywhere}.
   \]
   Hence
   \[
   \frac{g_{\rm hi}}s\in L^2(0,1),
   \qquad
   \nu^{\rm hi}([0,\delta])
   =O(\delta^{3/2}).
   \]

9. In the finite-band branch, restricting the two weighted factors to
   \(hA\) gives
   \[
   h^{3/2}
   \left(\int_A s^2\,ds\right)^{1/2}
   \quad\hbox{and}\quad
   h^{1/2}|A|^{1/2}K^{1/2}N^{1/6}.
   \]
   With \(K=\kappa h^{-1/2}\), their product has the asserted
   \(h^{7/4}\) power and weighted time factor.

10. The macro mesh
    \(\delta_h=\kappa^{-1}h^{7/2}\) converts the cell estimate to the
    scale-free rectangle law. The prelimit claim is correctly restricted
    to macro-grid unions.

11. The reviewed off-diagonal tail places every limiting finite-band law
    inside one fixed source-coordinate ball. Open-set Portmanteau and
    outer regularity transfer the rectangle estimate to all limiting
    Borel rectangles.

12. Lebesgue-time disintegration and a countable rational-box argument
    give, on one common full-measure time set,
    \[
    \mu_s(E)\le Cs|E|^{1/6}
    \]
    for every Borel \(E\). Therefore
    \[
    \|f_s\|_{L^{6/5,\infty}}\le Cs,
    \qquad
    g_{\rm fb}(s)\le Cs,
    \]
    and the finite-band terminal-edge mass is \(O(\delta^2)\).

13. Positive integrated effective-polar alignment and the bounded slice
    mass imply a positive-Lebesgue-measure set of times with positive
    slice alignment. No relation between different slices is inferred.

## Precision repairs

Review and self-audit produced four clarifications before the final
verdict.

1. The prelimit finite-band spatial estimate is stated only for
   macro-grid unions; arbitrary Borel sets enter after the weak limit.
2. The band-resolved kinematic carrier asserts order-one effective polar
   at bulk roots or in a fixed local norm, and distinguishes an upper
   gradient cost from two-sided saturation.
3. The weak-limit rectangle passage now explicitly uses open-set
   Portmanteau followed by outer regularity.
4. The coupled high-branch inequality now displays its
   continuous-cutoff form, so joint weak-limit passage is termwise.

The reviewer edited no files.

## Exact accepted frontier

The new theorem excludes time atoms and vanishing terminal-edge
concentration in both charged local branches:

\[
\nu^{\rm hi}([0,\delta])
=O(\delta^{3/2}),
\qquad
\nu^{\rm fb}([0,\delta])
=O(\delta^2).
\]

The high branch also forces an absolutely continuous component of the
high-frequency energy-time law. The finite-band branch has
almost-every-time weak-\(L^{6/5}\) spatial slices whose unnormalised norm
vanishes linearly at the terminal edge.

The remaining obstruction is not existence, sign, spatial compactness,
or terminal-edge temporal concentration. It is the absence of a relation
between different slices and different events. The next exact gate is one
of:

1. a time-translation or bounded-variation estimate for the effective
   polar decoration;
2. a limiting Oseen balance for the disintegrated law; or
3. one finite same-trajectory functional whose increments realise the
   positive slice alignment.

The signed late-annulus, direct inverse-\(15/4\), exterior
stretched-exponential, and high-coefficient spatial branches remain
unexcluded.

## Validation

- Targeted temporal ledger: passed.
- Focused temporal tests: 10 passed.
- Full repository check: 552 tests passed; 80 experiment records,
  569 links, and mathematical markup passed.
- `git diff --check`: passed.
