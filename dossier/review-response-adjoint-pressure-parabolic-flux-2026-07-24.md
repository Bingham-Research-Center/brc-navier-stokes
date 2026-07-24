# Independent review response: parabolic tail to signed NSE flux

**Date:** 2026-07-24

**Reviewed request:**
`review-letter-adjoint-pressure-parabolic-flux-2026-07-24.md` (archived in Git at `c277792`)

**Primary theorem:**
[`experiments/adjoint-pressure-parabolic-flux.md`](experiments/adjoint-pressure-parabolic-flux.md)

**Verdict:** valid and nonduplicative in the stated
conditional/algebraic scope after two precision repairs

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI recomputed the smooth-to-sharp
comparison, the forward physical-time high-pass energy identity, all
three thresholds, the physical pullback, every shell balance, the
near-lossless limit, and the Zeno heat-clock sum.  It found no fatal
analytic gap.

The theorem is genuinely new relative to the earlier
frequency-energy-flux audit.  That audit starts from a tensor-detector
moment and permits zero nonlinear flux.  The new theorem starts from the
reviewed positive viscous high-pass dissipation floor.  If the payment is
neither in a comparable annulus nor already present as high-frequency
entrance energy, the exact NSE identity forces positive signed nonlinear
input into the farther tail.

## Accepted smooth-to-sharp step

Since

\[
1-\chi(\xi/\Lambda)=0
\qquad(|\xi|\le\Lambda)
\]

and

\[
|1-\chi(\xi/\Lambda)|\le C_\chi,
\]

Plancherel gives

\[
D^\chi_{>\Lambda}(I)
\le
C_\chi^2D^\sharp_{>\Lambda}(I).
\]

Thus

\[
D^\chi_{>\Lambda}(I)\ge P
\]

implies

\[
D^\sharp_{>\Lambda}(I)
\ge
T,
\qquad
T=\frac{P}{C_\chi^2}.
\]

The sphere \(\{|\xi|=\Lambda\}\) is Fourier-null for \(L^2\) data, and
the sharp annulus/far-tail split is orthogonal and exact.

## Accepted high-pass trichotomy

For

\[
\Phi_K(I)
:=
-
\int_I
\left\langle
Q_{>K}\mathbb P\operatorname{div}(v\otimes v),
Q_{>K}v
\right\rangle\,dt,
\]

the physical forward-time identity is

\[
\Phi_K(I)
=
\frac12
\left(
E_K(b)-E_K(a)
\right)
+
\nu D^\sharp_{>K}(I).
\]

Positive \(\Phi_K\) is input into \(>K\).  If the comparable annulus
contains less than \(T/2\), the farther tail contains more than \(T/2\).
If its entrance energy is also less than \(\nu T/2\), nonnegativity of
the terminal energy gives

\[
\Phi_{R\Lambda}(I)
>
-\frac{\nu T}{4}
+
\frac{\nu T}{2}
=
\frac{\nu T}{4}.
\]

Therefore the comparable-annulus, inherited-high-energy, and
positive-signed-flux alternatives are exhaustive with the stated
constants.

The reviewer confirmed that the sharp projector is legitimate as an
orthogonal \(L^2/H^1\) multiplier commuting with \(\Delta\) and
\(\mathbb P\).  On the selected preterminal physical intervals all
pairings are classical.

## Accepted physical scaling

For

\[
b(x,\tau)
=
\sigma v(x_0+\sigma x,t_0-\sigma^2\tau),
\]

the normalised tail dissipation is \(\sigma^{-1}\) times the physical
tail dissipation, and a normalised cutoff \(V\) becomes
\(\Lambda=V/\sigma\).  Hence the reviewed fixed-parabolic floor becomes

\[
P_j
=
c_\kappa\sigma_jh_j^{-3},
\qquad
\Lambda_j
=
\frac{\kappa h_j^{-1/2}}{\sigma_j}.
\]

The superparabolic form similarly gives
\(c_\varepsilon\sigma_jh_j^{-3+\varepsilon}\).

## Accepted shell and clock obstruction

For

\[
F_n=Pr^n,
\qquad
V_n=F_{n-1}-F_n
\quad(1\le n<m),
\qquad
V_m=F_{m-1},
\]

with \(V_0=0\), \(\Delta E_0=-2P\), and all other endpoint energy
changes zero, the reviewer checked:

\[
\frac12\Delta E_0=-F_0,
\]

\[
V_n=F_{n-1}-F_n,
\]

\[
V_m=F_{m-1},
\]

\[
\frac12\sum_{n=0}^m\Delta E_n
+
\sum_{n=0}^mV_n
=0,
\]

and

\[
\sum_{k=n+1}^mV_k=F_n.
\]

For \(m\ge2\),

\[
r_m=1-\frac1{m^2}
\]

gives

\[
r_m^{m-1}\to1,
\qquad
1-r_m^{m-1}\to0.
\]

Thus endpoint integrated balances and cumulative positive flux alone
permit arbitrarily deep near-lossless finite ledgers.  The reviewer
agreed that the note does not promote this to a time-resolved shell ODE
or NSE construction.

The heat-clock sum is also exact:

\[
\sum_{n=1}^\infty
\frac1{\nu(L^n\Lambda)^2}
=
\frac1{\nu\Lambda^2(L^2-1)}.
\]

At an event cutoff this equals

\[
\frac{\delta}{\nu\kappa^2(L^2-1)}.
\]

It is correctly labelled only as proof that a natural-clock lower
ledger does not impose finite depth, not as a construction of the shell
transfers.

## Precision repairs

The review requested and the note now includes two qualifications:

1. the high-pass theorem assumes smoothness on a neighbourhood of the
   closed physical interval \([a,b]\), so the endpoint \(L^2\) traces
   in the exact identity are explicit;
2. the depth-dependent choice
   \(r_m=1-m^{-2}\) is restricted to \(m\ge2\).

No other repair was required.

## Exact accepted frontier

The kinematic survivor can no longer hide the reviewed physical tail
payment at an arbitrary farther frequency for free.  On the actual NSE
trajectory it must generate a comparable annulus, inherited high-state
energy, or positive signed nonlinear input.

The signed input is cumulative rather than event-index fresh.  The
accepted shell ledger shows that its positivity and the ordinary
high-pass balances alone do not prevent reuse.  The next theorem must
quantify flux decrement, frequency locality, non-Zeno cascade speed,
high-state ancestry, or a genuinely telescoping event-index functional.

This does not exclude the conditional ancient profile, prove regularity
or breakdown, or establish any Clay alternative A--D.

## Validation

- Targeted executable tests: 10 passed.
- Independent review: no fatal analytic gap; two precision repairs
  accepted.
- Current canonical repository validation: 35 sources, 30 claims,
  23 routes, 106 experiments, 16 obligations, 829 local-link targets,
  32,088 mathematical delimiters, and 796 tests passed.
- Whitespace validation: passed.
