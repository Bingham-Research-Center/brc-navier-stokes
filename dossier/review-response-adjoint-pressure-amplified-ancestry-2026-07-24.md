# Independent review response: amplified spatial--frequency ancestry survivor

**Date:** 2026-07-24

**Reviewed packet:**
[`review-letter-adjoint-pressure-amplified-ancestry-2026-07-24.md`](review-letter-adjoint-pressure-amplified-ancestry-2026-07-24.md)

**Primary theorem:**
[`experiments/adjoint-pressure-amplified-ancestry.md`](experiments/adjoint-pressure-amplified-ancestry.md)

**Verdict:** accepted after two precision repairs

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI checked the amplified stretched
coordinate, exact next-event recurrence, physical mass and tail
formulae, nested time--frequency measure, kill frequency, and
generalised \(3/2\) boundary.  It found the scalar construction
mathematically sound in its stated scope.

Two repairs were requested and made:

1. the fixed output-band factor was absorbed explicitly by defining
   \(c=c_{\rm sf}/S\), so every later exponential literally saturates
   the reviewed spatial--frequency cost; and
2. the event recursion now starts with \(y_1>1\), making its target
   strictly positive and closing existence of the unique
   \(y_{j+1}>y_j\).

The reviewer then returned **ACCEPT** without further correction.  No
reviewer edits were made.

## Accepted construction

For

\[
\widehat p=\frac74+\beta,
\qquad
y=h^{-\widehat p},
\qquad
F=h^{-\beta},
\qquad
c=\frac{c_{\rm sf}}S,
\]

set

\[
D=h^{-3}e^{cy},
\qquad
\sigma=h^3e^{-acy},
\qquad
\rho=\sigma D=e^{-(a-1)cy},
\qquad a>1.
\]

Then

\[
\log(Dh^3)=cy=cFh^{-7/4},
\qquad
\frac{\sigma}{h^3e^{-cy}}=e^{-(a-1)cy}\to0.
\]

The unique recurrence

\[
ac(y_{j+1}-y_j)
+\frac3{\widehat p}\log\frac{y_{j+1}}{y_j}
=\frac{\beta}{\widehat p}\log y_j
\]

gives the exact ancestry identities

\[
\boxed{
\sigma_{j+1}=\frac{\sigma_j}{F_j},
\qquad
\frac{F_j}{\sigma_j}=\frac1{\sigma_{j+1}}.
}
\]

Moreover,

\[
y_j\to\infty,
\qquad
y_{j+1}-y_j
\sim
\frac{\beta}{ac\widehat p}\log y_j,
\qquad
\frac{y_{j+1}}{y_j}\to1.
\]

## Accepted physical history

The terminal-return tail toll is

\[
\tau_j
=A\sigma_jF_j^2h_j^{-3}
=Ae^{-acy_j}F_j^2.
\]

Both

\[
\tau_j\to0,
\qquad
\frac{\tau_j}{\rho_j}=Ae^{-cy_j}F_j^2\to0
\]

hold.  After a finite truncation, one finite nonnegative Borel measure
with an \(L^1\) time marginal realises simultaneously

\[
\mu((0,\delta_j)\times[0,\infty))=\rho_j
\]

and

\[
\mu\!\left(
(0,\delta_j)\times[F_j/\sigma_j,\infty)
\right)=\tau_j
\]

at every event.  Thus the amplified cost, quadratic high-frequency
tail toll, and exact current-frequency/next-scale identity remain
arithmetically compatible.

The kill frequency is

\[
F_{\rm kill}
=\frac{h^{3/2}}{\sqrt{\sigma}}
=\exp\!\left(\frac{ac}{2}h^{-\widehat p}\right),
\]

which remains stretched-exponentially above the polynomial \(F\).  If
\(q_j=y_{j+1}/y_j\), the exact charge boundary remains

\[
\log(\sigma_jF_j^2h_j^{-3})
=\frac6{\widehat p}\log q_j+acy_j(2q_j-3).
\]

At \(q_j=3/2\) the charge is the fixed positive constant
\((3/2)^{6/\widehat p}\); the survivor has \(q_j\to1\).

## Exact accepted frontier

Spatial--frequency amplification does not by itself defeat accelerated
physical zoom, even when the named high frequency is exactly the next
event reciprocal scale and the complete quadratic tail toll is imposed.
The construction is a nonnegative scalar history, not a high-pressure
state, coefficient field, Oseen solution, Navier--Stokes trajectory, or
singularity.

The remaining branch needs genuinely PDE information absent from the
construction: a lower bound on physical zoom, exhaustive terminal
high-state participation, a charge for returned-low histories, or a
non-reusable signed/vector increment.

## Validation

- Targeted exact tests: 12 passed.
- Executable certificate: passed.
- Reviewer `make check`: 712 tests passed.
- `git diff --check`: passed.
