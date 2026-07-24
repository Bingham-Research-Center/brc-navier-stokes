# Independent review response: first-hitting polar vacuum

**Date:** 2026-07-24

**Reviewed packet:**
`review-letter-adjoint-pressure-polar-vacuum-2026-07-24.md` (archived in Git at `c277792`)

**Primary theorem:**
[first-hitting polar-vacuum reduction](experiments/adjoint-pressure-polar-vacuum.md)

**Verdict:** valid in its stated conditional finite-band scope

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found no fatal implication in the
first-hitting refinement, moving-grid capture law, inverse-ninth
regularisation ceiling, pressure-weighted vacuum limit, or
balanced-versus-subcritical amplitude fork.

The accepted conclusion applies only after the reviewed signed branch tree
is rerun on the canonical first-hitting layers and reaches the charged
finite-band child:

\[
\boxed{\varepsilon_h\lesssim h^9.}
\]

At the same time, the \(h^2\)-normalised descendant-rooted adjoint tends
to zero in local \(L^2\), in probability under the finite-band pressure
law, even though the effective polar retains positive alignment.

This is a conditional reduction. It proves no lower bound on
\(\varepsilon_h\), strong compactness of the amplitude-normalised adjoint,
event telescope, finite budget, regularity theorem, breakdown theorem, or
Clay alternative A--D.

## Accepted mathematical chain

The reviewer checked the following links.

1. For fixed \(\varepsilon>0\), the algebraic difference bound for
   \(\rho_\varepsilon\) and \(L^2\) continuity of the smooth Oseen adjoint
   make \(L_\varepsilon(a(t))\) continuous.

2. Replacing a mass-gain terminal interval by its first half-threshold
   hitting time preserves a fixed positive Kato-polar work packet. The
   complete reviewed pressure branch tree may be rerun with unchanged
   powers and smaller fixed constants.

3. First hitting gives the uniform earlier-time bound
   \[
   L_{\varepsilon_h}(a_h(t))
   \le\|\varphi\|_1+\gamma_*.
   \]

4. The pointwise inequality
   \[
   |\zeta_\varepsilon(z)|^2
   \le
   \frac{2}{\varepsilon}\rho_\varepsilon(z)
   \]
   therefore yields
   \(\|\zeta_h(t)\|_2^2\lesssim\varepsilon_h^{-1}\).

5. The finite-band kernel proof is pointwise in time and extends to
   measurable moving cube families:
   \[
   \int_0^h\int_{U(t)}|H_h|
   \lesssim
   h^{3/2}
   \left(
   K\int_0^hN(t)^{1/3}\,dt
   \right)^{1/2}.
   \]

6. Positive signed work leaves fixed \(|H_h|\)-mass where
   \(|Q_K\zeta_h|\) is bounded below. The Schwartz kernel tail and local
   Cauchy--Schwarz force \(cK^{-3}\) local polar \(L^2\) mass at every
   such point.

7. Bounded overlap then permits at most
   \(CK^3/\varepsilon_h\) polar-active descendant cubes at each time.

8. Substitution into moving-grid capture gives
   \[
   1
   \lesssim
   h^{3/2}\varepsilon_h^{-1/6},
   \]
   and hence \(\varepsilon_h\lesssim h^9\). The polar-active set reaches
   the full \(h^{-21/2}\) source-volume cell power at some times.

9. The pointwise adjoint-difference bound gives at most
   \(Ch^{-7/2}(t/h)^2\) cells where the \(h^{-2}\) rooted zero-data
   adjoint has fixed local \(L^2\) size. Moving capture makes their
   pressure probability \(O(h^{7/6})\).

10. Choosing the detector core \(S_h=h^{-2/3}\) makes its pressure
    probability \(O(h^{7/6})\) as well. Schwartz decay removes the fixed
    detector outside that core, so the complete rooted adjoint is vacuum
    at quadratic amplitude.

11. With \(\theta_h=\varepsilon_h/h^9\), the rooted amplitude-normalised
    Orlicz mass satisfies
    \[
    \Gamma_h\{\mathfrak O^D>L\}
    \lesssim
    (\theta_hL)^{-1/6}.
    \]
    Thus \(\liminf\theta_h>0\) gives pressure-probability Orlicz
    tightness, while \(\theta_h\to0\) is a strict amplitude cascade.

12. The descendant Oseen rescaling has diffusion coefficient
    \(\nu\kappa^2\), critical drift norm at most \(\kappa^2M\), and
    pressure-gradient factor \(h/\varepsilon_h\). The source-cell average
    of its normalised pressure mass is of order \(\theta_h^{-1}\).

13. The two-mode curl carrier is exactly solenoidal. Its nonlinear polar
    has a nonzero \((2,1)\)-type gradient harmonic. A real even annular
    multiplier and the orthogonal gradient projection therefore produce
    an exact artificial annular gradient mark with positive pairing.

14. The kinematic model has regularisation \(h^9\), spatial volume
    \(h^{-9}\), \(h^{-21/2}\) descendant cells, and order-one Kato
    dissipation. Its artificial mark saturates the finite-band capture
    powers. It is not an Oseen solution, a Navier--Stokes trajectory, or
    a pressure factorisation.

## Review-driven repairs

The review required the following nonfatal repairs before acceptance.

1. The theorem and canonical record were restricted explicitly to charged
   finite-band children after the first-hitting branch rerun.
2. Moving threshold families were defined through suprema over closed
   cubes, making their time-membership sets Borel.
3. The growing detector core was changed from \(h^{-1}\) to
   \(h^{-2/3}\), matching the \(O(h^{7/6})\) zero-data rate.
4. The kinematic envelope was required to equal one on a nonempty ball,
   and all bulk Fourier claims were restricted to that plateau.
5. The time modulation was required to spend a fixed fraction of the
   layer on nonzero-amplitude plateaux; pointwise two-sided norm claims
   were restricted accordingly.
6. The two-mode polar divergence and its nonzero gradient harmonic were
   displayed explicitly.
7. The artificial annular multiplier was required to have a real even
   symbol on symmetric harmonic neighbourhoods, and the projected
   \(L^2\) lower bound was displayed before the signed pairing.
8. Orlicz tightness was kept distinct from strong compactness, and the
   average source-cell interpretation was kept distinct from cellwise
   equidistribution.

The reviewer edited no files.

## Exact accepted frontier

The naive proposal to pass from the old quadratic regularisation ceiling
to a nonzero \(h^2\)-normalised limiting Oseen state is closed. In the
charged first-hitting finite-band branch, the underlying quadratic-scale
state is zero while the effective polar remains nonzero; the polar graph
has become singular at vacuum.

The surviving finite-band fork is:

\[
\begin{array}{ll}
\liminf\varepsilon_h/h^9>0:
&
\text{amplitude-normalised Orlicz tightness, without strong compactness};
\\[1mm]
\varepsilon_h/h^9\to0:
&
\text{strict amplitude cascade, with no current finite budget.}
\end{array}
\]

The next exact task is to compactify and identify the balanced
amplitude-normalised Oseen law, charge the strict sub-\(h^9\) cascade by a
finite same-trajectory quantity, or construct a telescope which uses the
first-hitting Kato mass without requiring continuity of the polar graph at
zero.

## Validation

- Targeted polar-vacuum ledger: passed.
- Focused polar-vacuum tests: 10 passed.
- Full repository check: 562 tests passed.
- `git diff --check`: passed.
