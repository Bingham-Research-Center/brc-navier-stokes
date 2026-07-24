# Independent review request: exact next-event ancestry survivor

**Date:** 2026-07-24
**Route:** ROUTE-R3B
**Clay status claimed by author:** unsolved

Please review
`dossier/experiments/adjoint-pressure-ancestry-survivor.md` as an
adversarial mathematician.  The proposed result is only a scalar
time--frequency dissipation-ledger counterexample.  It does not claim a
coefficient field, an Oseen solution, a suitable solution, or a
Navier--Stokes singularity.

The inputs already accepted in their stated scopes are:

1. the stretched-history scalar ledger
   `dossier/experiments/adjoint-pressure-stretched-history.md`;
2. the logarithmic causal-depth theorem
   `dossier/experiments/adjoint-pressure-divergent-interaction-depth.md`;
3. the high--high-to-low terminal-return theorem and its physical
   high-frequency-tail ceiling
   `dossier/experiments/adjoint-pressure-terminal-return.md`.

The new claim chooses the event sequence recursively so that

\[
\sigma_{j+1}=\sigma_j/L_j,
\qquad
L_j=2^{\lfloor c_{\rm dep}\log(1/h_j)\rfloor}.
\]

Thus \(L_j/\sigma_j=1/\sigma_{j+1}\) exactly.  It then splits one finite
nested scalar dissipation history into bulk mass and a high-frequency
tail of exact cumulative mass

\[
\tau_j=A\sigma_jL_j^2h_j^{-3}
\]

above the physical threshold \(L_j/\sigma_j\).

Please try to falsify, in particular:

1. existence, uniqueness, and asymptotics of the recurrence in the
   stretched coordinate \(x=h^{-7/4}\);
2. the exact current-frequency/next-scale identity;
3. the claims that \(\tau_j/\rho_j\to0\), and that the tail and remaining
   bulk cumulative masses can both be made decreasing;
4. the time--frequency measure construction and both telescoping
   identities;
5. the kill-frequency formula
   \(L_{\rm kill}=h^{3/2}/\sqrt{\sigma}=e^{ac h^{-7/4}/2}\);
6. the conditional \(x_{j+1}/x_j=3/2\) threshold in equation (31);
7. any place where a scalar compatibility ledger is accidentally
   promoted to a PDE or Navier--Stokes claim.

Please classify the disposition as:

- valid in the exact stated scope;
- repairable, with precise corrections; or
- invalid, identifying the first fatal implication.

The executable audit is:

```bash
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_ancestry_survivor -v
make adjoint-pressure-ancestry-survivor
```
