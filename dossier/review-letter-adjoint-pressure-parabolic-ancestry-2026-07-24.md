# Independent review request: parabolic tail ancestry

**Date:** 2026-07-24

**Clay status:** unsolved

**Primary note:**
[`experiments/adjoint-pressure-parabolic-ancestry.md`](experiments/adjoint-pressure-parabolic-ancestry.md)

**Reviewed input:**
[`experiments/adjoint-pressure-parabolic-coefficient-tail.md`](experiments/adjoint-pressure-parabolic-coefficient-tail.md)

## Requested disposition

Please classify the new note as one of:

1. valid in its stated conditional/kinematic scope;
2. repairable, with exact repairs;
3. fatal analytic gap; or
4. correct but duplicative of an earlier recorded result.

Do not assess it as a Clay solution.  It explicitly proves neither
regularity nor breakdown.

## Claim A: conditional \(7/6\) same-trajectory ceiling

The reviewed fixed-\(\kappa\) coefficient-tail theorem and exact
physical scaling give

\[
\mathcal E_j
:=
\int_{I_j}
\|\nabla(I-S_{\Lambda_j})v\|_2^2\,dt
\ge
c_\kappa\sigma_jh_j^{-3},
\qquad
\Lambda_j
=
\frac{\kappa h_j^{-1/2}}{\sigma_j}.
\]

For one finite-enstrophy trajectory, \(\Lambda_j\to\infty\) implies
\(\mathcal E_j\to0\), hence

\[
\sigma_jh_j^{-3}\to0.
\]

Assume the cutoff reaches the next event:

\[
\Lambda_j\ge\frac{a_0}{\sigma_{j+1}}.
\]

The note derives

\[
\frac{\sigma_{j+1}}{\sigma_j}
\ge
\frac{a_0}{\kappa}h_j^{1/2},
\]

and therefore

\[
\frac{\sigma_j^7}{\sigma_{j+1}^6}\to0.
\]

With \(x_j=\log(1/\sigma_j)\), this is

\[
6x_{j+1}-7x_j\to-\infty,
\qquad
\limsup\frac{x_{j+1}}{x_j}\le\frac76.
\]

Please check:

1. the direction of the cutoff/next-event inequality;
2. use of global Fourier-tail continuity;
3. every exponent and logarithmic sign;
4. whether any unmentioned nesting of \(I_j\) is needed; and
5. the general \(1+b/a\) exponent ledger.

## Claim B: sharp power-law survivor

For \(q>3\), the note sets

\[
\sigma_j=h_j^q,
\qquad
h_{j+1}
=
\kappa^{-1/q}h_j^{1+1/(2q)}.
\]

It claims

\[
\sigma_{j+1}
=
\frac{\sigma_j}{\kappa h_j^{-1/2}},
\qquad
\frac{\kappa h_j^{-1/2}}{\sigma_j}
=
\frac1{\sigma_{j+1}},
\]

\[
\tau_j
:=
\sigma_jh_j^{-3}
=
h_j^{q-3}\to0,
\]

and

\[
\frac{\sigma_j^7}{\sigma_{j+1}^6}
=
\kappa^6\tau_j.
\]

For \(\kappa=1\),

\[
\frac{x_{j+1}}{x_j}
=
1+\frac1{2q}<\frac76,
\]

approaching \(7/6\) as \(q\downarrow3\).  The mean event roof diverges
because \(x_j\) grows geometrically.

Please check exact sharpness and whether this genuinely distinguishes a
relative log-scale ceiling from finite mean roof.

## Claim C: smooth kinematic realisation

The note constructs:

1. compact annular solenoidal packets
   \(G_j(x)=\sigma_j^{-1}G(x/\sigma_j)\);
2. the terminal trace \(g=\sum_jG_j\);
3. the smooth approach
   \[
   B(s)=\sum_j\alpha(s/\sigma_j^2)G_j;
   \]
4. tail corrections on disjoint time annuli,
   \[
   H(s)
   =
   \sum_j\sqrt{m_j}\eta_j(s)W_{K_j}(x),
   \]
   where
   \(W_K(x)=K^{1/2}W(Kx)\) has unit gradient norm and
   weak-\(L^3\) norm \(O(K^{-1/2})\).

The claimed properties are:

- \(g\in L^2\cap L^{3,\infty}\);
- one fixed compact solenoidal detector has an exact positive mark at
  every scale \(\sigma_j\);
- \(B(s)\to g\) strongly in \(L^2\);
- \(B\) has finite integrated enstrophy and uniform weak-\(L^3\);
- the decreasing target
  \(M_j=4(\sup_{k\ge j}\mathcal B_k+\tau_j)\) is realised exactly as
  the cumulative high-frequency dissipation of \(H\);
- the \(K_j\) can simultaneously enforce Fourier support above
  \(\Lambda_j\), a uniform weak-\(L^3\) ceiling, and strong zero
  terminal \(L^2\) trace for \(H\); and
- the Hilbert inequality
  \[
  \|X+Y\|^2\ge\frac12\|Y\|^2-\|X\|^2
  \]
  gives the required tail floor for \(B+H\).

Please audit:

1. support separation in the terminal detector;
2. the weak-\(L^3\) distribution estimate for the packet tower;
3. strong terminal \(L^2\) convergence;
4. finite integrated enstrophy;
5. monotonicity and telescoping of \(M_j,m_j\);
6. the scaling of every \(W_K\) norm;
7. the smoothness of the accumulating time-annulus construction; and
8. the final high-pass lower bound in the presence of cross terms.

## Scope boundary to enforce

The smooth survivor is not claimed to:

- solve Navier--Stokes;
- satisfy the feedback-pressure antecedent;
- obey a Navier--Stokes local energy inequality;
- identify its far-finer carrier frequencies with actual event states;
- produce a singularity; or
- prove any Clay alternative.

The proposed route consequence is only:

> fixed-parabolic tail/next-event coupling would impose a sharp
> \(7/6\) relative log-scale ceiling, but nonnegative nested Fourier
> tails plus the current endpoint budgets do not prevent event-index
> reuse; an NSE-specific annular localisation, signed flux, cascade
> speed, or intervening-event theorem is still required.
