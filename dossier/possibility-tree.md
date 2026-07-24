# Possibility tree

This is a falsifiable route partition, not an assertion that the taxonomy is
complete. The canonical machine-readable version is
[`records/routes.json`](records/routes.json). The detailed pre-slim narrative
is recoverable with
`git show a7ae140:dossier/possibility-tree.md`.

```text
CLAY
├── R   Global regularity
│   ├── R1   Universal critical control
│   │   ├── R1A  velocity endpoint
│   │   ├── R1B  vorticity-direction depletion
│   │   ├── R1C  frequency-flux barrier
│   │   └── R1D  analyticity versus sparseness
│   ├── R2   Minimal blow-up and rigidity
│   │   ├── R2A  concentration compactness
│   │   ├── R2B  ancient-solution classification
│   │   └── R2C  backward uniqueness / Liouville rigidity
│   └── R3   Remove assumptions from conditional criteria
│       ├── R3A  single point to arbitrary cores       [conditional closure]
│       ├── R3B  imposed geometry to derived geometry  [active]
│       └── R3C  critical profile to Type-II dynamics  [open]
└── B   Finite-time breakdown
    ├── B1   unforced smooth-data singularity
    │   ├── B1A  similarity mechanism
    │   └── B1B  non-self-similar cascade
    ├── B2   smooth-forced Clay construction
    └── B3   bridge singular-data mechanisms to Clay data
        ├── B3A  independent certified profile reproduction
        └── B3B  smooth prehistory or force embedding
```

## Classification axes

Every proposed singularity or exclusion theorem must identify its cell.

| Axis | Values tracked |
|---|---|
| Domain | \(\mathbb R^3\), \(\mathbb T^3\) |
| Force | zero, admissible smooth force |
| Rate | Type I, Type II, unknown |
| Similarity | continuous, discrete, asymptotic, none |
| Geometry | point, tube, sheet, multi-core, diffuse |
| Scale behaviour | single scale, cascade, oscillatory |
| Location | physical, frequency, coupled |
| Solution class | classical, mild, suitable, Leray--Hopf, weaker |

## Closure rule

A node closes only through:

1. an exclusion theorem covering its exact assumptions;
2. a reduction into already closed children;
3. an exact construction satisfying the node and Clay quantifiers; or
4. a proved equivalence or containment in another node.

Numerical absence, physical implausibility, more prose, and failure to find an
example do not close a node.

## Current route map

### R3A: repaired conditional criterion

The 2607 audit and finite-overlap localisation remove the extra fixed-ball,
component, fragmentation, and anisotropy hypotheses from that conditional
chain. They do not derive its vorticity-direction depletion from arbitrary
NSE data. See the [audit](papers/2607.08866-audit.md) and
[proof map](papers/2607.08866-proof-map.md).

### R3B: active weak-\(L^3\) Type-I branch

The conditional structural reduction retains a nonzero coherent ancient
suitable distance profile with two terminal singular points, no exact
continuous or discrete self-similarity, and recurring positive Besov defect.
The [current status](status.md) gives the shortest dependency path.

The latest actual-NSE consequence is:

\[
\Phi_{K_j}(\widetilde J_j)\ge\frac{\nu T_j}{4},
\qquad
\nu\int_{\widetilde J_j}
\|\nabla Q_{\eta K_j<|\xi|\le K_j}v\|_2^2\,dt
\ge
c\left(\frac{\nu}{M}\right)^2
\Phi_{K_j}(\widetilde J_j),
\]

with \(K_j/\Lambda_j\to1\). Thus each late event has positive terminal
signed flux and a fixed fractional lower-band decrement. The near-lossless
shell survivor is closed.

The remaining survivor may reuse overlapping intervals and bands while its
flux and physical floors decay geometrically. R3B closes only if one obtains:

- a bound for current spatially cut-off nonlinear work or the nested critical
  physical dissipation action left by staggered entrance ancestry;
- bounded time-frequency overlap or a scale-zero decrement;
- a non-Zeno/intervening-event theorem;
- a pressure-visible cross-event telescope; or
- a clock/zoom law making the stretched coefficient cost nonsummable.

The direct inverse-\(15/4\), finite-secondary-index packet, no-neck,
parent-rigidity, and two-scale genealogy children also remain open.

### R3C: Type II

R3B assumes a uniform weak-\(L^3\) Type-I branch. Even a complete R3B
exclusion would leave Type-II and oscillatory concentration. A Clay
regularity proof must cover R3C or prove that all first singularities enter
the R3B class.

### Breakdown side

No smooth Clay-admissible singularity is constructed. Certified or numerical
singular-data mechanisms remain outside the target until they acquire a
smooth prehistory or an admissible smooth force. See the
[HWY bridge note](papers/2509.25116-bridge-note.md).

## Three highest-leverage bridges

1. **Universal critical gain:** derive a power, logarithm, or modulus that
   strictly improves a scale-critical quantity for every candidate
   concentration.
2. **Minimal-object rigidity:** extract the weakest genuine ancient object
   from a putative singularity and prove it must vanish.
3. **Singular-to-smooth construction:** connect a certified unstable
   singular-data mechanism to exact smooth Clay data without hiding the
   singularity in the initial state or force.

## Adversarial coverage test

Before calling an argument exhaustive, test:

- moving or multiple centres;
- tubes, sheets, and diffuse concentration;
- Type-II rates and scale oscillation;
- far-field and cross-frequency energy;
- vorticity-direction defects at zeros;
- translation, dilation, and frequency loss of compactness;
- the exact endpoint rather than nearby exponents; and
- whether every conditional antecedent is actually derived.

Any unknown answer remains an open child.
