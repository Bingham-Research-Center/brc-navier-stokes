# Review response: second causal feedback interaction

**Date:** 2026-07-24
**Route:** ROUTE-R3B
**Verdict:** valid in the stated conditional scope
**Clay status:** unsolved

The independent adversarial reviewer audited
[the theorem](experiments/adjoint-pressure-second-interaction.md) against
`review-letter-adjoint-pressure-second-interaction-2026-07-24.md` (archived in Git at `c277792`).
No repair to the claimed reduction is required.

## Accepted theorem

For the first heat-mediated feedback response

\[
r^{[1]}(\tau)
=
\int_0^\tau
e^{\nu(\tau-s)\Delta}
\mathbb P\operatorname{div}(q\otimes b)(s)\,ds,
\]

the complete adjoint-pressure cost vanishes:

\[
\int_0^h
\|\nabla\pi^*_{[r^{[1]},b]}(\tau)\|_1\,d\tau
\longrightarrow0.
\]

Hence the reviewed fixed feedback packet passes to
\(r^{[\ge2]}=r-r^{[1]}\), which solves

\[
\partial_\tau r^{[\ge2]}
-\nu\Delta r^{[\ge2]}
-\mathbb P(b\cdot\nabla r^{[\ge2]})
=
\mathbb P(b\cdot\nabla r^{[1]}),
\qquad
r^{[\ge2]}(0)=0.
\]

## Referee checks

The reviewer independently confirmed:

1. \(\operatorname{div}(q\otimes b)=b\cdot\nabla q\) with the stated
   tensor convention and \(\nabla\cdot b=0\);
2. the reviewed cube estimate gives
   \(\|q(t)\|_1\lesssim t^{1/4}\), and interpolation with
   \(\|q(t)\|_2\lesssim t\) gives
   \(\|q(t)\|_{L^{3/2,1}}\lesssim t^{3/4}\);
3. the kernel of
   \(e^{\nu\theta\Delta}\mathbb P\operatorname{div}\) has fourth-power
   spatial decay, with no slower projection tail;
4. the source inner/outer split controls the complete projected
   convolution and creates no omitted cutoff term;
5. the three pointwise-time and integrated exterior-tail exponent pairs
   are exact;
6. the Bogovskii replacement covers every far
   coefficient-gradient support;
7. centre-uniform local energy makes all exterior coefficient-shell
   contributions summable without a hidden \(D_b(h)\) remainder; and
8. the remainder equation and fixed pressure-floor transfer are exact.

The note now explicitly cites incompressibility in the tensor identity
and notes that the off-diagonal kernel-radius condition is invoked only
for sufficiently small \(h\), as optional clarity requested by the
reviewer.

## Exact retained boundary

The first heat-mediated feedback response is excluded as payer. The
surviving packet has causal feedback depth at least two. This does not
give a uniform estimate in interaction depth, sum a Dyson series, exclude
the complete feedback or direct-response branches, or prove any Clay
alternative A--D.

## Validation

The reviewer ran:

- the focused executable and all 6 focused tests;
- the full repository suite with 616 tests;
- records, links, and mathematical-markup validation; and
- `git diff --check`.

All passed.
