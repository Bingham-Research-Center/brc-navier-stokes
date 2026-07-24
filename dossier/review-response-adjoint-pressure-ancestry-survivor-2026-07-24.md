# Independent review response: exact next-event ancestry survivor

**Date:** 2026-07-24

**Reviewed packet:**
[`review-letter-adjoint-pressure-ancestry-survivor-2026-07-24.md`](review-letter-adjoint-pressure-ancestry-survivor-2026-07-24.md)

**Primary theorem:**
[`experiments/adjoint-pressure-ancestry-survivor.md`](experiments/adjoint-pressure-ancestry-survivor.md)

**Verdict:** accepted after two precision repairs

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI checked the stretched-coordinate
recurrence, the exact physical frequency/next-scale identity, the
tail-to-total comparison, separate monotonicity of the tail and bulk
cumulative masses, the finite time--frequency measure, both telescoping
identities, the kill frequency, and the inter-event threshold.  It
found no fatal mathematical error in the stated scalar scope.

Two repairs were requested and made:

1. a multiline inline expression in the review request was repaired so
   the markup validator could parse it; and
2. the inter-event boundary was sharpened from the merely sufficient
   \(q>3/2\) case to the exact \(q=3/2\) constant-charge boundary.

The reviewer then re-ran the packet and accepted it without further
correction.  No reviewer edits were made.

## Accepted construction

With \(p=7/4\), \(x=h^{-p}\),

\[
D(h)=h^{-3}e^{cx},
\qquad
\sigma(h)=h^3e^{-acx},
\qquad
\rho(h)=e^{-(a-1)cx},
\]

and

\[
L(h)=2^{\lfloor c_{\rm dep}\log(1/h)\rfloor},
\]

the unique recurrence

\[
ac(x_{j+1}-x_j)
+\frac3p\log\frac{x_{j+1}}{x_j}
=\log L_j
\]

gives

\[
\boxed{
\sigma_{j+1}=\frac{\sigma_j}{L_j},
\qquad
\frac{L_j}{\sigma_j}=\frac1{\sigma_{j+1}}.
}
\]

The reviewer confirmed

\[
x_j\to\infty,
\qquad
x_{j+1}-x_j
\sim
\frac{\alpha_{\rm dep}}{acp}\log x_j,
\qquad
\frac{x_{j+1}}{x_j}\to1.
\]

## Accepted tail-history split

The required terminal-return physical tail mass is

\[
\tau_j
=A\sigma_jL_j^2h_j^{-3}
=Ae^{-acx_j}L_j^2.
\]

Both

\[
\tau_j\to0,
\qquad
\frac{\tau_j}{\rho_j}
=Ae^{-cx_j}L_j^2\to0
\]

hold with a stretched-exponential margin.  After discarding finitely
many initial nodes, \(\tau_j\) and
\(\beta_j=\rho_j-\tau_j\) are positive and decreasing.  Placing their
fresh increments on the terminal annuli
\((\delta_{j+1},\delta_j]\), with the tail increment at frequency

\[
\kappa_j=\frac{L_j}{\sigma_j}=\frac1{\sigma_{j+1}},
\]

produces one finite nonnegative time--frequency measure whose time
marginal is in \(L^1\) and which satisfies

\[
\mu((0,\delta_j)\times[0,\infty))=\rho_j,
\]

\[
\mu((0,\delta_j)\times[\kappa_j,\infty))=\tau_j.
\]

The reviewer checked both telescopes exactly.

## Exact quantitative boundary

The kill frequency is

\[
\boxed{
L_{\rm kill}
=\frac{h^{3/2}}{\sqrt{\sigma}}
=e^{ac h^{-7/4}/2}.
}
\]

The reviewed causal frequency \(L(h)\asymp h^{-\alpha_{\rm dep}}\) is
stretched-exponentially smaller.

Under exact next-event ancestry, put
\(q_j=x_{j+1}/x_j\).  The physical charge is

\[
\sigma_jL_j^2h_j^{-3}
=q_j^{6/p}e^{acx_j(2q_j-3)}.
\]

At \(q_j=3/2\) it equals the fixed positive constant

\[
\left(\frac32\right)^{6/p}.
\]

Thus \(q_j\ge3/2\) on an infinite subsequence is already incompatible
with physical tail continuity.  The exact vanishing condition is

\[
\boxed{
acx_j(3-2q_j)-\frac6p\log q_j\longrightarrow+\infty.
}
\]

The survivor has \(q_j\to1\).

## Scope and validation

The accepted result closes only the bare scalar next-event scale
identity as a contradiction strategy.  The measure is not a
coefficient field, Oseen solution, suitable solution, Navier--Stokes
trajectory, or singularity.  A closure theorem still needs a genuinely
PDE inter-event gap, a top frequency approaching \(L_{\rm kill}\), or a
non-reusable signed/vector/spacetime-localised charge.

- Targeted exact tests: 11 passed.
- Reviewer full suite: 690 tests passed.
- `make adjoint-pressure-ancestry-survivor`: passed.
- `make check`: passed.
- `git diff --check`: passed.
