# Independent review response: spectral primal--adjoint pairing

**Date:** 2026-07-24

**Reviewed packet:**
`review-letter-adjoint-pressure-spectral-pairing-2026-07-24.md` (archived in Git at `c277792`)

**Primary theorem:**
[`experiments/adjoint-pressure-spectral-pairing.md`](experiments/adjoint-pressure-spectral-pairing.md)

**Verdict:** valid after six precision repairs

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI classified the result as
precision-repairable.  It found Claims A--E mathematically correct, found
no fatal gap, and found the localised commutator identity and two exact
spectral separations nonduplicative of the earlier global cancellation
and abstract Hodge obstruction.

The review validates an exact frequency-localised primal--adjoint pairing
identity and periodic same-trajectory counterexamples.  It does not
validate a mixed pressure-sensitive no-go, an event genealogy, a
finite-energy \(\mathbb R^3\) counterexample, regularity, breakdown, or
any Clay alternative A--D.

## Accepted mathematical chain

The reviewer independently recomputed and accepted:

1. the reversed-time primal and forward Oseen-adjoint signs;
2. exact cancellation of the two viscous pairing terms;
3. vanishing of each scalar pressure contribution by pairing with a
   divergence-free projected field;
4. both signs in the transport commutator identity;
5. the exact telescope for nested fixed frequency projectors;
6. all identities for the one-radius Beltrami field \(U_N\), including
   the physical pressure
   \[
   p_u(t)=-A^2e^{-2\nu N^2t}w_N
   \]
   and \(p_b(\tau)=-p_u(-\tau)\);
7. the torus lower bound
   \[
   \int_0^T\|\nabla\pi_a\|_1\,d\tau
   \ge32\pi|AB|NT
   \]
   and the spectral gap \(N<K<\sqrt2N\);
8. equal radii and positive helicity for the paired modes
   \(k_n,\ell_n\);
9. the exact high--high-to-fixed-low pressure formula
   \[
   \frac{|W_n|^2}{2}
   =
   1+
   \left(1-\frac1{2R_n^2}\right)\cos(x+y)
   +
   \frac1{2R_n^2}\cos((2n+1)(x-y));
   \]
10. the pressure radii \(\sqrt2\) and \(\sqrt2(2n+1)>R_n\), and the
    fixed-low history floor
    \[
    \int_0^T
    \|P_{\le K}\nabla\widetilde\pi_n\|_1\,d\tau
    \ge
    16\pi^2|AB|
    \left(1-\frac1{2R_n^2}\right)T.
    \]

## Accepted repairs

The reviewed note now:

1. defines \(P\) as a fixed orthogonal componentwise Fourier frequency
   projector preserving solenoidality, not the Leray projector;
2. states that projected pressure gradients need not vanish and that
   only their scalar pairings against divergence-free projected fields
   are zero;
3. restricts the no-go to the bare pairing telescope, leaving genuinely
   mixed pressure-sensitive functionals open;
4. states \(N,n\in\mathbb N\), \(n\ge1\), and the pressure-gauge
   convention;
5. records that the fixed-low family has no coefficient-energy or
   coefficient-dissipation budget uniform in \(n\), so it does not
   contradict the reviewed terminal-return toll; and
6. defines \(\Delta_\tau F=F(T)-F(0)\).

The executable certificate was strengthened at the same time.  Its
finite-dimensional pressure vectors now survive the projector but are
orthogonal to the corresponding projected primal and adjoint fields.
It therefore checks pressure-pairing cancellation rather than artificial
annihilation by the projector.

## Exact accepted frontier

The bare proposal

> frequency-localise the conserved primal--adjoint \(L^2\) pairing and
> telescope its shell increments to pay the adjoint-pressure events

is closed.  Its telescope is exact, but it supplies no pressure term.
The live target must add a pressure-visible ingredient, such as an
\(L^1\)-polar pressure coupling, a spatial pressure boundary flux, a
controlled divergence defect, or direct same-trajectory ancestry.

The periodic examples do not rule out any such mixed functional.

## Validation

- Targeted spectral-pairing tests: 13 passed.
- Independent pre-repair audit: `make check` passed 809 tests.
- Final full repository validation is recorded with the canonical
  experiment update.
