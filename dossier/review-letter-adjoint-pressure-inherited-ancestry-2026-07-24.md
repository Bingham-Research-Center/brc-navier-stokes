# Independent review request: inherited high energy to historical signed flux

**Date:** 2026-07-24

**Clay status:** unsolved

**Primary note:**
[`experiments/adjoint-pressure-inherited-ancestry.md`](experiments/adjoint-pressure-inherited-ancestry.md)

**Reviewed inputs:**

- [`experiments/adjoint-pressure-parabolic-flux.md`](experiments/adjoint-pressure-parabolic-flux.md)
- [`experiments/adjoint-pressure-parabolic-coefficient-tail.md`](experiments/adjoint-pressure-parabolic-coefficient-tail.md)
- [`experiments/adjoint-pressure-parabolic-ancestry.md`](experiments/adjoint-pressure-parabolic-ancestry.md)

## Requested disposition

Please classify the new note as one of:

1. valid in its stated conditional same-trajectory scope;
2. repairable, with exact repairs;
3. fatal analytic gap; or
4. correct but duplicative of an earlier recorded result.

Do not assess it as a Clay solution.  It explicitly proves neither
regularity nor breakdown.

## Claim A: general last-hitting ancestry lemma

Let \(v\) be a smooth finite-energy Navier--Stokes solution on
\(\mathbb R^3\times(0,T^*)\).  Put

\[
E_K(t)=\|Q_{>K}v(t)\|_2^2
\]

and use the reviewed forward-time sign convention

\[
\Phi_K((a,b))
=
\frac12(E_K(b)-E_K(a))
+
\nu\int_a^b\|\nabla Q_{>K}v\|_2^2\,dt.
\]

Fix \(t_\circ\in(0,T^*)\).  Suppose

\[
a_j\to T^*,
\qquad
K_j\to\infty,
\qquad
\Theta_j>0,
\qquad
\Theta_jK_j^2\to\infty,
\]

and

\[
E_{K_j}(a_j)\ge\Theta_j.
\]

The note claims that for all sufficiently large \(j\) there is a last
hitting time

\[
s_j\in(t_\circ,a_j),
\qquad
E_{K_j}(s_j)=\Theta_j/2,
\]

such that

\[
\Phi_{K_j}((s_j,a_j))\ge\Theta_j/4.
\]

The proof uses

\[
E_{K_j}(t_\circ)
\le
K_j^{-2}\|\nabla v(t_\circ)\|_2^2
<
\Theta_j/2,
\]

time continuity of \(E_{K_j}\), and the exact identity.

Please check:

1. whether the stated smooth finite-energy hypotheses give the required
   \(H^1\) value and time continuity;
2. the sharp-projector Plancherel estimate;
3. existence and strict placement of the last hitting;
4. the sign and factor \(1/4\); and
5. whether a closed-interval or neighbourhood qualification is needed.

## Claim B: terminal localisation of the ancestor

The note further claims, if inherited-branch indices are infinite,

\[
s_j\to T^*
\quad\textnormal{along that index set}.
\]

If not, there are \(\delta>0\) and a subsequence with
\(s_j\le T^*-\delta\).  Smoothness on
\([t_\circ,T^*-\delta]\) gives

\[
M_\delta
:=
\sup_{t_\circ\le t\le T^*-\delta}
\|\nabla v(t)\|_2^2<\infty.
\]

At the hitting time,

\[
\frac{\Theta_jK_j^2}{2}
=
K_j^2E_{K_j}(s_j)
\le
\|\nabla v(s_j)\|_2^2
\le
M_\delta,
\]

contradicting \(\Theta_jK_j^2\to\infty\).

Please check whether the compact-time \(H^1\) bound follows in the exact
pre-first-singular-time setting and whether any issue is hidden by the
index-dependent sharp projector.

## Claim C: parabolic scale application

The reviewed tail-to-flux theorem uses

\[
T_j
=
\frac{c_\kappa}{C_\chi^2}\sigma_jh_j^{-3},
\qquad
\Lambda_j
=
\frac{\kappa h_j^{-1/2}}{\sigma_j},
\]

with \(h_j,\sigma_j\downarrow0\).  For arbitrary \(R_j>1\), the new note
sets

\[
K_j=R_j\Lambda_j,
\qquad
\Theta_j=\frac{\nu T_j}{2}.
\]

It computes

\[
\Theta_jK_j^2
=
\frac{\nu c_\kappa\kappa^2}{2C_\chi^2}
R_j^2\sigma_j^{-1}h_j^{-4}
\to\infty.
\]

Thus any occurrence of the inherited branch

\[
E_{K_j}(t_j^-)\ge\frac{\nu T_j}{2}
\]

forces some \(s_j<t_j^-\), \(s_j\to T^*\), with

\[
\Phi_{K_j}((s_j,t_j^-))
\ge
\frac{\nu T_j}{8}.
\]

Please check:

1. every scale power and constant;
2. that \(R_j>1\), even index-dependent, causes no loss;
3. that \(t_j^-\to T^*\) is the correct genealogy property;
4. that no use of \(T_j\to0\) has the comparison direction backwards;
   and
5. that fixing \(\kappa\) is explicit enough.

## Claim D: revised late-event trichotomy

Combining the new lemma with the reviewed trichotomy, the note claims
that for every sufficiently large \(j\), at least one of

\[
\int_{I_j}
\|\nabla Q_{\Lambda_j<|\xi|\le R_j\Lambda_j}v\|_2^2\,dt
\ge\frac{T_j}{2},
\]

\[
\Phi_{R_j\Lambda_j}(I_j)
\ge\frac{\nu T_j}{4},
\]

or

\[
\Phi_{R_j\Lambda_j}((s_j,t_j^-))
\ge\frac{\nu T_j}{8},
\qquad
s_j\to T^*
\]

holds.

The intended wording is not that entrance high-frequency energy is
impossible.  It is that entrance energy is no longer an unexplained
late-time resource: if present, it has a positive pre-event nonlinear
input ancestor on the same trajectory.

Please check the logic of replacing the reviewed inherited alternative
by this historical-flux alternative, including cases where more than
one original branch holds.

The note also merges the two flux cases on the indices where the
annular branch fails: there is an interval
\(J_j=(\alpha_j,\beta_j)\) such that

\[
\Phi_{R_j\Lambda_j}(J_j)\ge\frac{\nu T_j}{8}.
\]

It takes \(J_j=I_j\) in the original event-flux branch and
\(J_j=(s_j,t_j^-)\) in the inherited branch.  Along any infinite such
index set, both endpoints tend to \(T^*\).  Please check that this
merger loses no case and that the common constant is correct.

## Claim E: adaptive annulus squeezing forces flux at every late event

For fixed \(j\), define the finite frequency-dissipation measure

\[
\mu_j(B)
:=
\int_{I_j}\int_B
|\xi|^2|\widehat v(\xi,t)|^2\,d\xi\,dt.
\]

For

\[
A_j(R)=\{\xi:\Lambda_j<|\xi|\le R\Lambda_j\},
\]

the note uses continuity from above to claim

\[
\mu_j(A_j(R))\to0
\qquad(R\downarrow1).
\]

It therefore chooses

\[
1<R_j<1+\frac1j,
\qquad
D^\sharp_{\Lambda_j<|\xi|\le R_j\Lambda_j}(I_j)
<\frac{T_j}{4}.
\]

The sharp total floor then gives

\[
D^\sharp_{>R_j\Lambda_j}(I_j)>\frac{3T_j}{4}.
\]

The note reapplies the exact high-pass identity with a new entrance
split at \(\nu T_j\).  If the entrance energy is below \(\nu T_j\),
nonnegative exit energy gives

\[
\Phi_{R_j\Lambda_j}(I_j)
>
-\frac{\nu T_j}{2}
+
\frac{3\nu T_j}{4}
=
\frac{\nu T_j}{4}.
\]

If the entrance energy is at least \(\nu T_j\), Claims A--C apply with
\(\Theta_j=\nu T_j\); the half-level last hitting then gives historical
flux \(\nu T_j/4\).  Defining \(J_j\) by those two cases would prove

\[
K_j=R_j\Lambda_j,
\qquad
\frac{K_j}{\Lambda_j}\to1,
\qquad
\alpha_j,\beta_j\to T^*,
\qquad
\Phi_{K_j}(J_j)\ge\frac{\nu T_j}{4}
\]

for every sufficiently large \(j\).

Please check especially:

1. finiteness and continuity from above of \(\mu_j\);
2. whether the strict lower boundary at \(\Lambda_j\) makes the
   decreasing intersection empty;
3. whether event-dependent \(R_j\) is permitted by the reviewed
   trichotomy;
4. whether the construction works even if the event and inherited
   branches overlap;
5. convergence of both possible interval endpoints; and
6. the precise limitation that this is existential at
   \(K_j/\Lambda_j\to1\), not a floor at any prescribed fixed
   \(R>1\).

## Novelty and scope check

Please compare the result with the prior parabolic-flux and
parabolic-ancestry notes.  The proposed new content is:

1. one fixed-time \(H^1\) tail, combined with the exact parabolic
   threshold-frequency product, resolves the inherited entrance state
   into earlier flux;
2. the last-hitting ancestors themselves approach \(T^*\); and
3. an event-adaptive factor \(R_j\to1\) squeezes out the annular branch,
   so every late event has event or pre-event terminal flux.

The note does not claim:

- disjointness or summability of \((s_j,t_j^-)\);
- event-index freshness;
- a lower bound on the historical interval length;
- an intervening selected Besov event;
- exclusion of the conservative/Zeno cascade ledger;
- exclusion of the conditional ancient profile; or
- any Clay alternative A--D.

Please identify any overstatement of what “closes inherited state”
means, even if the mathematics is correct.
