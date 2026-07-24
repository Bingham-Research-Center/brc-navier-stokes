# Handoff: R3C flux residence and freshness

**Updated:** 2026-07-24

**Clay status:** unsolved

**Live route:** `ROUTE-R3C`

**Checkpoint:** `EXP-TYPE-II-SUBGRID-TRANSPORT-001`

## Load only

- [Current subgrid theorem](dossier/experiments/type-ii-subgrid-transport.md).
- [Canonical R3C record](dossier/records/routes.json).

Everything else is durable in [status](dossier/status.md) or
[records](dossier/records/README.md). Do not load frozen R3B without new
input or external review.

## Exact live question

Can actual NSE flux geometry prevent one energy packet from traversing
infinitely many increasing carrier subscales with finite viscous action?

## Progress marker

Entrance remains the \(2\times3\times3\) ledger. In all nine
energy-efficient cells, normalised viscous dissipation vanishes on every
fixed interval and the whole remaining forward horizon.

For the terminal-microstructure branch, positive convolution subgrid energy
recovers exactly half the trace-defect measure. Its smooth local-energy
balance gives, one fixed carrier time backwards:

1. inherited nonnegative subgrid energy;
2. positive signed nonlinear transfer; or
3. positive signed spatial import through the cutoff.

Every integrated term pulls back by \(b_j\asymp e_j\ge c>0\), so either
transfer branch has a fixed physical energy floor on a shrinking interval.

## Known unknown

An exact adjacent-shell Zeno ledger moves the same positive surviving energy
through infinitely many increasing boundaries on disjoint intervals while
paying finite total dissipation and a vanishing terminal dissipation tail.
Thus signed fixed flux is not fresh merely because times and scales differ.

The coherent weak trace still needs propagation and Euler rigidity. The
divergent-normalised-energy branch still lacks global compactness.

## Next bounded cycle

1. Derive the sharpest NSE flux-rate/residence bound at filter
   \(\ell_j\), using the terminal normalisation
   \(\|v_j(0)\|_{L^{3,\infty}}\asymp1\).
2. Split \(\ell_j\) against \(\varepsilon_j\) and the next carrier scale:
   forced viscous residence, fresh onward transfer, or a Zeno survivor.
3. Turn positive spatial import into a recentered ancestry alternative and
   test whether moving cutoffs can reuse the same packet.

Before reporting or committing: `make check` and `git diff --check`.
