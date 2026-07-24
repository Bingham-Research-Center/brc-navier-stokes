# Independent review response: skew Oseen compression and pressure depth

**Date:** 2026-07-24

**Reviewed packet:**
`review-letter-adjoint-pressure-skew-compression-2026-07-24.md` (archived in Git at `c277792`)

**Primary theorem:**
[`experiments/adjoint-pressure-skew-compression.md`](experiments/adjoint-pressure-skew-compression.md)

**Verdict:** accepted after two initial scope repairs; follow-up
strong-zero-trace refinement accepted without further repair

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI found no fatal algebraic, PDE, or logical
error.  Its first pass accepted the theorem as closing only the abstract
skew/Hodge/real-coupling/squared-projection-defect shortcut after two scope
repairs.  Its follow-up pass independently recomputed and accepted the
monomial strong-zero-trace refinement without requiring another change.

It did not validate pressure-depth summability for the actual
heat-normalised Oseen operator, feedback exclusion, regularity, breakdown,
or any Clay alternative A--D.

## Accepted identities

The reviewer independently recomputed the following.

1. For divergence-free \(b,z\),
   \[
   Q(b\cdot\nabla z)
   =
   Q(z\cdot\nabla b)
   =
   \mathcal T(z,b).
   \]
2. For \(A=PBP\) and \(C=QBP\),
   \[
   A^*=-A,
   \qquad
   PB^2P=A^2-C^*C,
   \qquad
   -PB^2P=A^*A+C^*C.
   \]
   This is weighted by \(B^*B\), not the identity, and does not telescope
   over \(A^m\).
3. The displayed \(3\times3\) block is skew, its solenoidal compression is
   a quarter-turn, and
   \[
   |CA^me_1|=1
   \quad(m\ge0).
   \]
4. With \(q=-(e_1+e_2)\), \(r=e_1\), and the critical causal operator
   \(\mathbb T\),
   \[
   r=\mathbb T(q+r),
   \qquad
   r=\sum_{m=1}^{N}\mathbb T^mq+\mathbb T^Nr,
   \qquad
   |\mathbb C\mathbb T^Nr|=1.
   \]
5. The real-coupling solution is
   \[
   r_\lambda
   =
   \frac{\lambda}{1+\lambda^2}
   \binom{1+\lambda}{\lambda-1},
   \qquad
   \|r_\lambda\|^2
   =
   \frac{2\lambda^2}{1+\lambda^2}\le2.
   \]
   Uniform real-axis energy control does not decay the Taylor/Dyson
   coefficients at \(\lambda=1\).
6. A unitary compression telescopes squared leakage, but the exact rational
   small-step family obeys
   \[
   \sum_{m=0}^{n-1}|s_nc_n^m|\longrightarrow2,
   \qquad
   \sum_{m=0}^{n-1}|s_nc_n^m|^2\longrightarrow0.
   \]
   Hence no uniform linear-leakage bound follows from the squared energy
   defect.
7. Every sign in the local primal--adjoint conservation law is correct.

## Scope repairs

The reviewer required two changes before acceptance.

1. The introduction no longer calls the constant weak-endpoint mode an
   actual zero-data Oseen solution.  It is now described as a feedback
   solution with no initial term but no strong zero right trace.  The
   theorem explicitly leaves actual parabolic trace regularity available.
2. The surviving frontier now lists the strong zero-right-trace structure
   alongside heat/spatial commutators, same-trajectory signed laws, and
   event ancestry.

An additional clarification records the exact rotation time
\(\vartheta_n=2\arctan(1/n)\) and

\[
s_nc_n^m
=
\int_0^{\vartheta_n}\cos(s)c_n^m\,ds.
\]

Thus the linear leakage term is already step-integrated; the comparison
with a time-\(L^1\) pressure impulse is not missing a time-step factor.

## Follow-up strong-trace review

For every fixed \(\eta\ge0\), the follow-up reviewer independently
recomputed

\[
\mathsf H_\gamma(t^\eta)
=
\mu_{\gamma,\eta}t^\eta,
\qquad
\mu_{\gamma,\eta}
=
\frac{B(\gamma,1-\gamma+\eta)}
     {B(\gamma,1-\gamma)}>0.
\]

With

\[
A_{\gamma,\eta}=\mu_{\gamma,\eta}^{-1}J,
\qquad
q_\eta(t)=-t^\eta(e_1+e_2),
\qquad
r_\eta(t)=t^\eta e_1,
\]

it verified

\[
r_\eta
=
(\mathsf H_\gamma\otimes A_{\gamma,\eta})(q_\eta+r_\eta),
\qquad
\left|
C(\mathsf H_\gamma\otimes A_{\gamma,\eta})^Nr_\eta(t)
\right|
=t^\eta
\quad(N\ge0).
\]

For \(\eta=1\), \(\mu_{\gamma,1}=1-\gamma\), both \(q_1\) and \(r_1\)
have genuine strong zero right trace, and the residual pressure cost is

\[
\int_0^T
\left|
C(\mathsf H_\gamma\otimes A_{\gamma,1})^Nr_1(t)
\right|\,dt
=\frac{T^2}{2}
\quad(N\ge0).
\]

This closes any fixed algebraic trace order as an abstract shortcut.  The
coefficient block depends on the prescribed \(\eta\), and the construction
still does not realise a single heat-linked spatial Oseen or
Navier--Stokes operator.

## Exact accepted frontier

The result proves:

> Skew full transport, orthogonal Leray-pressure splitting, critical
> weak-endpoint causality, real coupling stability, any prescribed
> algebraic strong zero-trace order, and even a unitary squared leakage
> telescope do not alone imply linear adjoint-pressure summability across
> interaction depth.

The actual Oseen branch can still exploit:

1. the componentwise spatial transport/heat relation and parabolic
   smoothing;
2. the Navier--Stokes evolution of the same coefficient;
3. a non-reusable signed pressure law; or
4. physical event ancestry.

## Validation

- `make adjoint-pressure-skew-compression`: passed.
- Targeted exact-rational tests: 9 passed.
- Reviewer full `make check`: 644 tests passed.
- Reviewer `git diff --check`: passed.
