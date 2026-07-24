# Independent review response: spatial primal--adjoint cutoff flux

**Date:** 2026-07-24

**Reviewed packet:**
`review-letter-adjoint-pressure-spatial-pairing-2026-07-24.md` (archived in Git at `c277792`)

**Primary theorem:**
[`experiments/adjoint-pressure-spatial-pairing.md`](experiments/adjoint-pressure-spatial-pairing.md)

**Verdict:** valid after gauge and scope repairs

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found the same-trajectory Beltrami
cancellation mathematically valid after one essential pressure-gauge
repair and a corresponding scope tightening.  The local conservation
identity itself was already recorded in the reviewed skew-compression
note.  The new, incremental result is that an exact periodic
Navier--Stokes trajectory and its Oseen adjoint cancel that spatial
current in the displayed gauges, while all gauge-invariant cutoff fluxes
vanish and the adjoint-pressure history remains positive.

The review validates no pressure-polar no-go, canonically gauge-fixed
current norm estimate, finite-energy \(\mathbb R^3\) counterexample,
Besov-event genealogy, regularity theorem, breakdown theorem, or Clay
alternative A--D.

## Accepted mathematical chain

The reviewer independently recomputed and accepted:

1. the reversed-time primal and forward-adjoint signs;
2. the viscous Wronskian, transport, adjoint-pressure, and
   primal-pressure signs in
   \[
   \partial_\tau(a\cdot b)+\nabla\cdot\mathcal J=0;
   \]
3. the cutoff identity
   \[
   \frac d{d\tau}\int\eta\,a\cdot b
   =
   \int\nabla\eta\cdot\mathcal J;
   \]
4. the reciprocal Beltrami amplitudes and the displayed pressures;
5. the exact coefficients
   \[
   -qb=-2A^2Be^{\nu R^2\tau}wU,
   \qquad
   \pi_ab+p_ba=2A^2Be^{\nu R^2\tau}wU;
   \]
6. vanishing of the viscous Wronskian and of the complete current in
   the displayed gauges;
7. inheritance of that cancellation by both the one-radius and
   high--high-to-fixed-low Beltrami families;
8. the pressure-history floors \(32\pi|AB|NT\) and
   \[
   16\pi^2|AB|
   \left(1-\frac1{2R_n^2}\right)T;
   \]
9. the nonuniform paired-family budget
   \[
   \sup_{\tau\le T}\|\widetilde b_n(\tau)\|_2^2
   =
   2(2\pi)^3A^2e^{2\nu R_n^2T},
   \]
   \[
   \nu\int_0^T\|\nabla\widetilde b_n\|_2^2\,d\tau
   =
   (2\pi)^3A^2
   \left(e^{2\nu R_n^2T}-1\right).
   \]

## Gauge repair

Pressure shifts by time-dependent constants change the current by

\[
\mathcal J
\longmapsto
\mathcal J+c_a(\tau)b+c_b(\tau)a.
\]

The added current is divergence free.  Consequently
\(\mathcal J\equiv0\) is not gauge invariant, but the two statements

\[
\nabla\cdot\mathcal J=0,
\qquad
\int\nabla\eta\cdot\mathcal J=0
\]

hold in every pressure gauge for the Beltrami examples.  The primary
note now restricts pointwise vanishing to the displayed gauges and uses
the divergence and cutoff-gradient identities for its invariant
conclusion.

## Exact accepted frontier

The following bare proposal is closed:

> Telescope the gauge-invariant signed spatial cutoff currents of the
> conserved primal--adjoint pairing to coerce the adjoint-pressure event
> cost.

The pressure component can cancel the other current components exactly.
This does not exclude:

1. a pressure-polar or pressure-component functional;
2. a norm or other functional of a canonically gauge-fixed current;
3. a new sign or transversality theorem preventing cancellation;
4. a controlled divergence-defect functional; or
5. direct same-trajectory ancestry.

This cancellation is distinct from the spectral audit: the spectral
mechanism is Hodge orthogonality at every Fourier projector, whereas the
spatial mechanism is pointwise cancellation among pressure and transport
components of the total current.

## Validation

- Targeted spatial-pairing tests: 8 passed.
- Independent full check before final canonical sync: 817 tests passed.
- `git diff --check`: passed.
