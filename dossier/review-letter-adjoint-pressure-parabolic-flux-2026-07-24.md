# Independent review request: parabolic tail to signed NSE flux

**Date:** 2026-07-24

**Clay status:** unsolved

**Primary note:**
[`experiments/adjoint-pressure-parabolic-flux.md`](experiments/adjoint-pressure-parabolic-flux.md)

**Reviewed inputs:**

- [`experiments/adjoint-pressure-parabolic-coefficient-tail.md`](experiments/adjoint-pressure-parabolic-coefficient-tail.md)
- [`experiments/adjoint-pressure-parabolic-ancestry.md`](experiments/adjoint-pressure-parabolic-ancestry.md)
- [`experiments/frequency-energy-flux.md`](experiments/frequency-energy-flux.md)

## Requested disposition

Please classify the new note as one of:

1. valid in its stated conditional/algebraic scope;
2. repairable, with exact repairs;
3. fatal analytic gap; or
4. correct but duplicative of an earlier recorded result.

Do not assess it as a Clay solution.  It explicitly proves neither
regularity nor breakdown.

## Claim A: smooth-tail to sharp-tail conversion

For a smooth radial cutoff \(\chi\), put

\[
S_\Lambda=\chi(D/\Lambda),
\qquad
C_\chi=\|1-\chi\|_\infty,
\qquad
Q_{>K}=\mathbf 1_{\{|\xi|>K\}}(D).
\]

The note claims

\[
\int_I\|\nabla(I-S_\Lambda)v\|_2^2\,dt
\le
C_\chi^2
\int_I\|\nabla Q_{>\Lambda}v\|_2^2\,dt.
\]

Thus a reviewed smooth-tail floor \(P\) gives the sharp floor
\(T=P/C_\chi^2\).  For every \(R>1\), the sharp tail splits exactly into
the annulus \(\Lambda<|\xi|\le R\Lambda\) and the farther tail.

Please check the comparison direction, the cutoff support, and whether
any boundary or multiplier qualification is missing.

## Claim B: exact high-pass energy identity and trichotomy

The signed nonlinear input is defined by

\[
\Phi_K(I)
:=
-
\int_I
\left\langle
Q_{>K}\mathbb P\operatorname{div}(v\otimes v),
Q_{>K}v
\right\rangle\,dt.
\]

For a smooth finite-energy unforced NSE solution on \(I=(a,b)\), the
note uses

\[
\Phi_K(I)
=
\frac12
\left(
\|Q_{>K}v(b)\|_2^2-\|Q_{>K}v(a)\|_2^2
\right)
+
\nu\int_I\|\nabla Q_{>K}v\|_2^2\,dt.
\]

It then claims that, for every \(R>1\), at least one of

\[
\int_I
\|\nabla Q_{\Lambda<|\xi|\le R\Lambda}v\|_2^2\,dt
\ge\frac T2,
\]

\[
\|Q_{>R\Lambda}v(a)\|_2^2
\ge\frac{\nu T}{2},
\]

\[
\Phi_{R\Lambda}(I)
\ge\frac{\nu T}{4}
\]

must hold.

Please check:

1. the sign convention and endpoint order;
2. the factor of \(\nu\);
3. all three constants;
4. whether sharp projection is legitimate at the stated smooth
   preterminal level; and
5. whether any regularity or temporal endpoint hypothesis was suppressed.

## Claim C: physical adjoint-pressure application

The reviewed coefficient-tail theorem supplies

\[
P_j=c_\kappa\sigma_jh_j^{-3},
\qquad
\Lambda_j
=
\frac{\kappa h_j^{-1/2}}{\sigma_j}
\]

on
\(I_j=(t_j-\sigma_j^2h_j,t_j)\).  The note applies Claim B with

\[
T_j
=
\frac{c_\kappa}{C_\chi^2}\sigma_jh_j^{-3}.
\]

Please check exact physical scaling and whether this is a genuinely new
same-trajectory PDE consequence rather than a restatement of either the
reviewed tail theorem or the earlier Beltrami flux no-go.  In
particular, the proposed distinction is that the earlier no-go starts
from a detector moment, whereas this theorem starts from an actual
positive high-pass viscous dissipation floor.

## Claim D: exact shell-ledger obstruction

For shells \(0,\ldots,m\), input \(P>0\), and \(0<r<1\), the note sets

\[
F_n=Pr^n
\quad(0\le n\le m-1),
\]

\[
V_0=0,
\qquad
V_n=F_{n-1}-F_n
\quad(1\le n\le m-1),
\qquad
V_m=F_{m-1},
\]

and

\[
\Delta E_0=-2P,
\qquad
\Delta E_n=0
\quad(n\ge1).
\]

It claims every integrated shell balance, the global balance, and the
cumulative identities

\[
\sum_{k=n+1}^mV_k=F_n
\]

hold exactly.  With

\[
r_m=1-\frac1{m^2},
\]

the top dissipation fraction satisfies

\[
\frac{V_m}{P}=r_m^{m-1}\to1,
\]

while total intermediate loss tends to zero.

Please check:

1. every sign and factor \(1/2\);
2. nonnegativity and total conservation;
3. the cumulative-tail identities;
4. the near-lossless limit; and
5. whether the conclusion is stated narrowly enough.

The asserted scope is only that integrated shell balances and positive
cumulative flux do not themselves force a uniform loss per crossed
annulus.  The ledger is not claimed to be a shell-model ODE, Galerkin
solution, Oseen solution, or NSE solution.

## Claim E: Zeno heat-clock compatibility

For \(K_n=L^n\Lambda\), the note records

\[
\sum_{n=1}^{\infty}\frac1{\nu K_n^2}
=
\frac1{\nu\Lambda^2(L^2-1)}.
\]

Since the event duration and cutoff obey

\[
\delta=\sigma^2h,
\qquad
\Lambda^{-2}=\delta/\kappa^2,
\]

the clock sum is

\[
\frac{\delta}{\nu\kappa^2(L^2-1)}.
\]

Thus a sufficiently large fixed \(L\) fits infinite natural heat clocks
inside one event; at \(\nu=1\), \(\kappa\ge1\), the dyadic choice gives
at most \(\delta/3\).

Please check the scaling and whether this is appropriately labelled as a
timing ledger rather than a transfer construction.

## Scope boundary to enforce

The proposed route consequence is only:

> Actual far-tail dissipation on the selected NSE trajectory forces a
> comparable annulus, inherited high-frequency entrance energy, or
> positive signed high-pass flux.  Positive cumulative flux alone still
> need not be fresh at the level of exact integrated energy balances.
> Closing the branch requires an NSE-specific flux-decrement, locality,
> cascade-speed, inherited-state ancestry, or event-index telescoping
> theorem.

The note does not claim:

- that any branch is excluded;
- that the shell ledger is dynamically realisable;
- that flux charges sum across events;
- that the conditional ancient profile is excluded; or
- any Clay alternative A--D.
