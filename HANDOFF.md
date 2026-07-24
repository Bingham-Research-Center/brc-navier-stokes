# Handoff: Type-II compactness defect

**Updated:** 2026-07-24

**Clay status:** unsolved

**Live route:** `ROUTE-R3C`

**Checkpoint:** `EXP-TYPE-II-INVISCID-CARRIER-001`

This is replace-not-append working memory. Durable results live in
[`dossier/status.md`](dossier/status.md), exact metadata in
[`dossier/records/`](dossier/records/README.md), and derivations in their
named experiment notes.

## Load only

- [Clay target](dossier/clay-target.md).
- [Current carrier theorem](dossier/experiments/type-ii-inviscid-carrier-entrance.md).
- [Canonical R3C record](dossier/records/routes.json).

Do not load the R3B chain unless a new theorem or external review directly
reopens it. Its result, assumptions, gates, failed shortcuts, and proof links
are preserved in the
[durable R3B status](dossier/status.md#2-conditional-r3b-profile-reduction).

## Exact live question

Can actual NSE dynamics turn the exhaustive inviscid carrier ledger into a
contradiction: either by strong compactness with trace persistence to a rigid
nonzero ancient Euler object, or by charging every failure of compactness to
one finite physical budget?

## State in one minute

For every sequence with
\(m_j=\|u(t_j)\|_{L^{3,\infty}}\to\infty\), the current theorem selects an
amplitude layer with

\[
a_j\asymp m_j^3/e_j,\qquad
R_j\asymp e_j/m_j^2,\qquad
\tau_j=R_j/a_j\asymp e_j^2/m_j^5.
\]

Carrier normalisation gives viscosity
\(\varepsilon_j\asymp\nu/m_j\to0\) and an arbitrarily long past. After a
subsequence, the exact first ledger is:

1. bounded or divergent \(E_0/e_j\);
2. diffuse, partially concentrated, or tight layer energy at scale \(R_j\);
3. zero, finite-positive, or infinite forward turnover horizon.

In the bounded-energy, spatially retained branch, strong
\(L^2_{\mathrm{loc}}\) space-time compactness would pass the nonlinearity to a
finite-energy ancient Euler solution; trace persistence is additionally
needed to make it nonzero. The precise survivors are Reynolds stress,
anomalous dissipation, temporal-trace loss, vector/frequency oscillation,
fragmentation, and energy escape.

A current v3 preprint claims exclusion of outgoing and axisymmetric smooth
stationary Euler profiles in the subparabolic similarity range under its
exact assumptions. It does not control the defect branches. A sharp
divergence-free kinematic path satisfies energy equality and the listed
necessary vorticity ledger but is not a Navier--Stokes solution.

## Next bounded cycle

1. Derive the strongest local space-time and trace compactness available from
   the actual rescaled NSE equation in the bounded-energy retained branch.
2. If strong compactness fails, express the Reynolds/dissipation defect as an
   exact positive or signed same-trajectory quantity and test whether it is
   summable.
3. Stress-test both outcomes against partial concentration and
   zero/infinite-horizon cells before claiming exhaustiveness.

## Frozen boundary

R3B remains a conditional weak-\(L^3\) Type-I branch pending independent
external review. No critical nested-action bound, fresh fixed event charge,
event-index contradiction, or Clay alternative A--D is proved. The
Albritton--Barker critical-amplitude repair also awaits external confirmation.

Before reporting or committing: `make check` and `git diff --check`.
