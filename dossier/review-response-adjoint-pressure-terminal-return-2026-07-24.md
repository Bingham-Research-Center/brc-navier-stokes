# Independent review response: terminal high--high-to-low pressure return

**Date:** 2026-07-24

**Reviewed packet:**
`review-letter-adjoint-pressure-terminal-return-2026-07-24.md` (archived in Git at `c277792`)

**Primary theorem:**
[`experiments/adjoint-pressure-terminal-return.md`](experiments/adjoint-pressure-terminal-return.md)

**Verdict:** accepted after two precision repairs and a follow-up
physical-tail audit

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI re-derived the low-output multiplier
kernel, comparable-frequency cutoff, Littlewood--Paley square sum,
time integration, inverse dissipation toll, Oseen energy application,
critical packet powers, terminal-layer exponent, and physical scaling.
It accepted the theorem after two repairs:

1. the annular support constants, \(P_{>L}\), and the exact
   comparable-frequency cutoff identity were made explicit; and
2. the physical charge retained all state, time, output-frequency, and
   pressure factors rather than only \(\sigma L^2\).

The physical frequency tails are correctly left nested and potentially
reusable.  No reviewer edits were made.

## Accepted theorem

For \(L\ge16S\), define

\[
\mathcal H_{>L}(z,b)
=
\sum_{R\ge L}
\Delta_Rz\otimes\widetilde\Delta_Rb.
\]

The fixed support convention gives

\[
\Pi_S((P_{>L}z)\otimes b)
=
\Pi_S\mathcal H_{>L}(z,b).
\]

The reviewer checked that the low-localised pressure-gradient
multiplier has \(L^1\) kernel norm \(O(S)\).  Annular Bernstein and
Littlewood--Paley orthogonality then give

\[
\boxed{
\int_0^T
\|\Pi_S\mathcal H_{>L}(z,b)\|_1\,dt
\le
C_{\rm ret}\frac SL\sqrt T\,
\|z\|_{L^\infty_tL^2_x}
D_{b,>L}^{1/2}.
}
\]

Thus an integrated pressure floor \(p\), with
\(\|z\|_{L^\infty_tL^2_x}\le Q\), forces

\[
\boxed{
D_{b,>L}
\ge
\frac{p^2L^2}
     {C_{\rm ret}^2S^2Q^2T}.
}
\]

For a smooth divergence-free Oseen adjoint, the exact energy identity
supplies \(Q=\|\psi\|_2\).

## Accepted scale audit

An energy-normalised state and critical drift packet in volume
\(R^{-3}\) obey

\[
\|z_R\|_2^2\asymp1,
\qquad
\|b_R\|_2^2\asymp R^{-1},
\qquad
\|\nabla b_R\|_2^2\asymp R,
\]

\[
\|z_R\otimes b_R\|_1^2\asymp R^{-1}.
\]

This saturates the \(S/R\) power at norm-scaling level.  Attempting to
put scalar Zeno \(L^1\) mass \(R^{-1}\) in volume \(R^{-3}\) instead
produces \(L^2\) square \(R\), violating uniform adjoint energy.

For the zero-data feedback remainder,
\(Q\lesssim h\) and \(T=h\), so a fixed high-tail pressure fraction
forces

\[
D_{b,>L}(h)\gtrsim L^2h^{-3}.
\]

## Physical charge and exact frontier

Under the parabolic pullback at physical event length \(\sigma\),

\[
D_{\rm norm}=\sigma^{-1}D_{\rm phys},
\qquad
R_{\rm physical}=\frac R\sigma.
\]

The accepted physical tail charge is therefore

\[
\boxed{
D_{v,\rm tail}^{\rm phys}
\gtrsim
\sigma\frac{p^2L^2}{S^2Q^2T}.
}
\]

On the terminal layer with fixed pressure and output floors this is
\(\sigma L^2h^{-3}\).  The weaker factor \(\sigma L^2\) is not enough.

## Accepted physical-tail ceiling

The follow-up review checked the global physical dissipation tail

\[
\mathcal E_{\ge\Lambda}(v)
=
\int_0^{T^*}
\sum_{K\ge\Lambda}
\|\widetilde\Delta_K\nabla v(t)\|_2^2\,dt.
\]

Finite spacetime enstrophy and Littlewood--Paley finite overlap give

\[
\mathcal E_{\ge\Lambda}(v)\to0
\qquad(\Lambda\to\infty).
\]

The event pullback satisfies

\[
\sigma_jD_{b_j,>L_j}
\lesssim
\mathcal E_{\ge cL_j/\sigma_j}(v).
\]

Consequently, if \(L_j/\sigma_j\to\infty\), the full charge obeys

\[
\boxed{
\sigma_j
\frac{p_j^2L_j^2}{S_j^2Q_j^2T_j}
\longrightarrow0.
}
\]

On the terminal layer this becomes

\[
\sigma_jL_j^2h_j^{-3}\to0.
\]

For
\(L_j=2^{\lfloor c_{\rm dep}\log(1/h_j)\rfloor}\), the reviewer
confirmed the necessary ancestry ceiling

\[
\boxed{
\sigma_j
=
o\!\left(
h_j^{3+2c_{\rm dep}\log2}
\right).
}
\]

The theorem closes the reciprocal terminal-gain mechanism for one
fixed energy-bounded, finite-dissipation Oseen window.  It does not
make the physical tails at successive zooms disjoint: nested tails may
reuse finer dissipation.  The global tail ceiling is necessary, not a
contradiction.  A stronger lower frequency law, quantitative
non-reuse, or event ancestry must now violate that ceiling.

## Validation

- Targeted exact tests: 11 passed.
- Reviewer full suite: 679 tests passed.
- `make check`: passed.
- `git diff --check`: passed.
