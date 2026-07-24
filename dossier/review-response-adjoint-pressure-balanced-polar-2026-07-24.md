# Independent review response: balanced Kato-polar compactness

**Date:** 2026-07-24

**Reviewed packet:**
`review-letter-adjoint-pressure-balanced-polar-2026-07-24.md` (archived in Git at `c277792`)

**Primary theorem:**
[balanced first-hitting polar compactness](experiments/adjoint-pressure-balanced-polar.md)

**Verdict:** valid after scope repairs

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found no fatal analytic gap after two
scope repairs.

The theorem applies only on the **norm-gated** first-hitting finite-band
path: the direct and exterior \(L^1_{t,x}\)-norm gates must have been
rejected before the charged finite-band child is selected. Mere
coexistence of a charged \(H_h\) component does not bound the full
pressure, because arbitrarily large direct or exterior components could
have zero polar pairing.

The accepted conclusion is tightness, and hence subsequential weak
convergence, of the pushed-forward polar-profile laws on the **strong**
local spacetime \(L^2\) topology. It is not convergence in probability on
the original varying probability spaces.

No amplitude-normalised Oseen limit, pressure-trace identification,
strict sub-\(h^9\) cascade cost, event telescope, regularity theorem,
breakdown theorem, or Clay alternative A--D was validated.

## Accepted mathematical chain

The reviewer independently checked the following implications.

1. On the norm-gated path,
   \[
   \begin{aligned}
   P_{\rm all}
   \le{}&
   C\sqrt h+P_q+P_{\rm out}\\
   &+
   C
   \left(\int_0^h\|r\|_2^2\right)^{1/2}
   D_{\rm in}(h)^{1/2}
   \le C.
   \end{aligned}
   \]
   The last product is \(O(1)\) because its factors have powers
   \(h^{3/2}\) and \(h^{-3/2}\).

2. At first hitting,
   \[
   \nu\int\mathcal K_{\varepsilon_h}(a_h)
   =
   -\int\zeta_h\cdot\nabla\pi_h^*-\gamma_*
   \le P_{\rm all},
   \]
   so the total Kato dissipation is uniformly bounded.

3. The exact rooted conversions are
   \[
   \mathfrak O
   =
   \frac1{\varepsilon h\ell^3}\int\rho_\varepsilon,
   \qquad
   \mathfrak K
   =
   \frac1{\varepsilon h\ell}\int\mathcal K_\varepsilon,
   \qquad
   \mathfrak P
   =
   \frac1{\varepsilon\ell^3}\int|\nabla\pi^*|.
   \]

4. With
   \(\varepsilon_h\asymp h^9\) and \(\ell\asymp h^{1/2}\), all three
   action-bad cube counts are at most
   \(CL^{-1}h^{-21/2}\), including fixed buffered enlargements.

5. The finite-band capture law therefore gives the common
   pressure-root tail
   \[
   CL^{-1/6}h^{7/4}
   \left(h^{-21/2}\right)^{1/6}
   =
   CL^{-1/6}.
   \]

6. For
   \(\Phi(A)=\sqrt{1+|A|^2}-1\) and
   \(\mathsf Z=\nabla\Phi(A)\),
   \[
   (D^2\Phi)^2\le D^2\Phi,
   \qquad
   |\nabla\mathsf Z|^2\le\mathcal K_\Phi(A).
   \]

7. The displayed third-derivative formula is correct. Radial--tangential
   decomposition gives
   \[
   |D^3\Phi(A)[v,v]|
   \le
   4\,v\cdot D^2\Phi(A)v.
   \]

8. The transformed polar equation has the displayed positive
   \(D^3\Phi\) sign. On buffered balls, diffusion is controlled by
   \(\nabla\mathsf Z\in L^2\); the critical weak-\(L^3\) drift is locally
   \(L^2\), so its product with \(\nabla\mathsf Z\) is locally \(L^1\);
   and the pressure and curvature terms are \(L^1\).

9. Since
   \(W^{1,6}_0(B_D)\hookrightarrow L^\infty(B_D)\),
   those \(L^1\) terms lie in \(W^{-1,6/5}(B_D)\). Thus
   \(\partial_s\mathsf Z\) is bounded in
   \(L^1_sW^{-1,6/5}_y\) on action-good roots.

10. A diagonal choice of action thresholds over expanding buffered balls,
    together with Aubin--Lions--Simon compactness, gives tightness of the
    profile laws on strong \(L^2_{\rm loc}\). The temporal-translation
    probability statement follows uniformly on the resulting compact
    sets.

11. The modular action has only linear growth. It controls local modular
    size but gives no uniform integrability or amplitude compactness. The
    example
    \[
    A_n=n^3e_1\mathbf1_{B_{1/n}}
    \]
    has bounded modular and concentrating order-one \(L^1\) mass.

12. The moving-time bump model correctly shows that strong profile
    compactness, fixed variation, and an atomless averaged time law do
    not identify a self-weighted pressure trace.

## Review-driven repairs

1. The theorem was restricted from any charged finite-band component to
   the norm-gated finite-band path on which the direct and exterior norm
   children have actually been rejected.
2. The conclusion was stated as tightness and subsequential weak
   convergence of pushforward laws on a strong topology, not strong
   convergence in probability on a common space.
3. The ball-exhaustion argument now specifies buffered balls and a
   summable diagonal choice of action thresholds.
4. The rooted \(\Phi\)-quantity is called linear-growth modular-action
   tightness, not amplitude or superlinear Orlicz compactness.
5. The algebraic inverse of a limiting polar is explicitly distinguished
   from a limiting amplitude, and the concentration example is recorded.

The reviewer edited no files.

## Exact accepted frontier

The earlier kinematic time-flip obstruction does not survive the complete
balanced Oseen pressure and Kato budgets. On the norm-gated balanced
finite-band path, the regularised polar has compact bulk spacetime
dynamics in law.

Two defects remain before this can become an honest
amplitude-normalised Oseen limit:

1. linear-growth amplitude concentration, which can disappear from the
   strong polar profile; and
2. a moving pressure-trace defect, which can keep a nonzero
   pressure-weighted mark while the associated thin time layer disappears
   in strong spacetime \(L^2\).

The next balanced-branch theorem must use Oseen pressure structure to
exclude or identify those defects. The strict
\(\varepsilon_h/h^9\to0\) cascade remains a separate branch with no
finite same-trajectory charge.

## Validation

- Balanced-polar ledger: passed.
- Focused balanced-polar tests: 9 passed.
- Full repository check: 571 tests passed.
- `git diff --check`: passed.
