# Handoff: R3C compactness defect

**Updated:** 2026-07-24

**Clay status:** unsolved

**Live route:** `ROUTE-R3C`

**Checkpoint:** `EXP-TYPE-II-INVISCID-CARRIER-001`

## Load only

- [Current carrier theorem](dossier/experiments/type-ii-inviscid-carrier-entrance.md).
- [Canonical R3C record](dossier/records/routes.json).

Everything else is durable in [status](dossier/status.md) or
[records](dossier/records/README.md). Do not load frozen R3B without new
input or external review.

## Exact live question

Can actual NSE dynamics turn the exhaustive inviscid carrier ledger into a
contradiction: either by strong compactness with trace persistence to a rigid
nonzero ancient Euler object, or by charging every failure of compactness to
one finite physical budget?

## Progress marker

Entrance is classified; no PDE cell is eliminated. Every weak-\(L^3\)
Type-II sequence has a carrier normalisation with viscosity tending to zero,
an arbitrarily long past, and an exhaustive first \(2\times3\times3\) ledger:

1. bounded/divergent normalised energy;
2. diffuse/partial/tight carrier energy;
3. zero/finite/infinite forward horizon.

The coherent self-similar subbranch is restricted to
\(2/5\le\gamma<1/2\) under additional stated hypotheses. Scalar energy,
scaling, and necessary vorticity tests cannot close it: the proof note gives a
sharp divergence-free kinematic survivor which is not an NSE solution.

## Known unknown

In the bounded-energy retained branch, strong
\(L^2_{\mathrm{loc}}\) space-time compactness passes the nonlinearity, but a
nonzero ancient Euler limit also needs trace persistence. The alternatives
are Reynolds stress, anomalous dissipation, temporal-trace loss,
vector/frequency oscillation, fragmentation, energy escape, and the three
forward-clock cells.

## Next bounded cycle

1. Derive the strongest local space-time and trace compactness available from
   the actual rescaled NSE equation in the bounded-energy retained branch.
2. If strong compactness fails, express the Reynolds/dissipation defect as an
   exact positive or signed same-trajectory quantity and test whether it is
   summable.
3. Stress-test both outcomes against partial concentration and
   zero/infinite-horizon cells before claiming exhaustiveness.

Before reporting or committing: `make check` and `git diff --check`.
