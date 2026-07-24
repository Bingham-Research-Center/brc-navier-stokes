# Independent review response: one prescribed multistage Oseen itinerary

**Date:** 2026-07-24

**Route:** ROUTE-R3B

**Clay status:** unsolved

**Reviewed request:**
`review-letter-adjoint-pressure-multistage-path-2026-07-24.md` (archived in Git at `c277792`)

**Reviewed note:**
[`experiments/adjoint-pressure-multistage-path.md`](experiments/adjoint-pressure-multistage-path.md)

## Verdict

**Valid in the exact stated conditional scope.**

The independent mathematical AI found no fatal implication and required
no mathematical repair.  It independently re-derived the path indexing,
kernel normalisation, endpoint telescope, exponential-clock law,
simplex and subset bounds, dyadic slow-clock ceiling, and both exponent
inversions.

## Verified derivation

The initial state \(w_0\) already contains the reviewed separated
high-to-\(R_0\) return.  Therefore \(m\) counts only later interactions:
there are \(m+1\) heat clocks but only \(m\) cross-band factors
\(A_x\).  With

\[
e_j(t)=\lambda_je^{-\lambda_jt},
\qquad
\lambda_j=c_0\nu R_j^2,
\]

the reviewer recovered

\[
C_xMR_{j-1}R_je^{-\lambda_jt}
=
A_x\frac{R_{j-1}}{R_j}e_j(t).
\]

The initial kernel contributes \(\lambda_0^{-1}\), while

\[
\prod_{j=1}^m\frac{R_{j-1}}{R_j}
=
\frac{R_0}{R_m}.
\]

Combining these factors with the final pressure multiplier gives

\[
C_pMSR_m\lambda_0^{-1}
A_x^m\frac{R_0}{R_m}
=
A_pA_x^m\frac{S}{R_0}.
\]

Thus every intermediate frequency cancels.  The \(m=0\) case reduces
to the reviewed one-return estimate.

Tonelli is used only after replacing the signed vector blocks by
nonnegative norm majorants.  The reviewer confirmed that no equality
between the positive scalar kernel and the vector Oseen operator is
claimed.

The convolution \(e_0*\cdots*e_m\) is the density of a sum of
independent exponentials.  Its finite-window distribution therefore
obeys

\[
\Theta_{\boldsymbol R}(h)
\le
\min\{1,\lambda_0h\}
\]

and

\[
\Theta_{\boldsymbol R}(h)
\le
\min\left\{
1,\frac{h^{m+1}}{(m+1)!}
\prod_{j=0}^m\lambda_j
\right\}.
\]

The same simplex argument applies to every nonempty subset of clocks.
For \(R_j=2^{-j}R_0\), the reviewer recovered

\[
\prod_{j=0}^m\lambda_j
=
(c_0\nu)^{m+1}
R_0^{2(m+1)}
2^{-m(m+1)}
\]

and, for \(n\) consecutive slow clocks,

\[
\Theta_{\boldsymbol R}(h)
\le
\frac{2^{-n(n-1)}}{n!}.
\]

For a complete descent to a fixed scale,

\[
n
=
\min\left\{\beta,\frac12\right\}
\log_2(1/h)+O(1).
\]

At fixed depth the reviewer confirmed

\[
\frac74+\beta+(1-2\beta)_+
=
\frac94+\left|\beta-\frac12\right|.
\]

At logarithmic depth, if
\(\delta=\kappa\log_+A\), the strict condition

\[
\delta<\beta+(1-2\beta)_+
\]

is necessary: without it the constant source term need not vanish, so
the logarithmic dissipation term cannot be identified as the payer.
Under this condition the exponent is correctly reduced by \(\delta\).
The bound \(A_pA_x^m\le A^{m+1}\) remains valid when \(0<A<1\).

## Precision changes adopted

The accepted note now states explicitly that:

1. all scales, \(h\), and \(\nu\) are positive;
2. the annular multipliers are uniform dilations of one fixed symbol;
3. \(c_0\) is chosen below both reviewed heat-decay constants;
4. \((z\boxtimes b)_{ik}=z_ib_k\), matching the reviewed Oseen tensor
   convention;
5. \(M>0\) in the fixed-floor discussion; and
6. the slow-clock count has the explicit asymptotic displayed above.

These are notation and hypothesis clarifications, not repairs to the
argument.

## Scope boundary

The theorem controls one prescribed, actual iterated component through
a positive norm majorant.  It does not prove a decomposition of the
complete returned-low state, bound the number of admissible
itineraries, control their pressure recombination, derive a
participation floor, construct a singularity, or resolve any Clay
alternative.

The first invalid extrapolation would be to replace this single-path
bound by a bound for the complete returned-low pressure without proving
those missing aggregate statements.
