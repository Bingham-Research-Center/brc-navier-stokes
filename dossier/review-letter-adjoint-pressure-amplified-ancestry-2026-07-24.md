# Independent review request: amplified spatial--frequency ancestry survivor

**Date:** 2026-07-24
**Route:** ROUTE-R3B
**Clay status claimed by author:** unsolved

Please review
`dossier/experiments/adjoint-pressure-amplified-ancestry.md`
adversarially.  The note tests whether the newly reviewed conditional
cost

\[
D(h)\ge h^{-3}\exp(cF(h)h^{-7/4})
\]

becomes contradictory when \(F(h)=h^{-\beta}\) is also the exact
next-event ancestry frequency.

Please try to falsify, in particular:

1. the identity \(Fh^{-7/4}=h^{-(7/4+\beta)}\);
2. the exact recurrence (13) and its equivalence to
   \(\sigma_{j+1}=\sigma_j/F_j\);
3. divergence of \(y_j\), the increment asymptotic, and \(q_j\to1\);
4. the total physical mass and terminal-tail formulae;
5. eventual positivity and monotonicity of the bulk/tail split;
6. the single nested measure and both cumulative identities;
7. the amplified kill frequency;
8. the generalised \(q=3/2\) boundary;
9. whether the construction really satisfies the little-\(o\) physical
   zoom ceiling forced by the spatial--frequency theorem; and
10. every scope boundary, especially that no high-state pressure floor,
    coefficient field, Oseen solution, or Navier--Stokes trajectory is
    constructed.

Please classify the disposition as:

- valid in the exact stated scalar scope;
- repairable, with precise corrections; or
- invalid, identifying the first fatal implication.

The executable certificate is:

```bash
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_amplified_ancestry -v
PYTHONPATH=lab python -m \
  navier_lab.adjoint_pressure_amplified_ancestry
```
