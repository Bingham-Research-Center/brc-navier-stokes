# Independent review response: terminal signed-flux ancestry

**Date:** 2026-07-24

**Reviewed request:**
[`review-letter-adjoint-pressure-inherited-ancestry-2026-07-24.md`](review-letter-adjoint-pressure-inherited-ancestry-2026-07-24.md)

**Primary theorem:**
[`experiments/adjoint-pressure-inherited-ancestry.md`](experiments/adjoint-pressure-inherited-ancestry.md)

**Verdict:** valid and nonduplicative in the stated conditional
same-trajectory scope after two quantifier/scope repairs; the subsequent
adaptive-annulus strengthening is also valid

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI recomputed the sharp Fourier-tail
bound, the last-hitting construction, the high-pass sign and constants,
the parabolic scale product, terminal localisation of the hitting
times, and the merged event/historical flux conclusion.  It found no
fatal analytic gap and no duplication of an earlier recorded theorem.

The prior parabolic-ancestry theorem concerns cutoff-to-next-event
scale distortion.  The prior parabolic-flux theorem leaves inherited
entrance energy as one branch.  The present theorem supplies the
missing same-trajectory accounting: an entrance threshold at the
reviewed frequencies cannot come solely from the tail at any fixed
earlier time; it has a terminal pre-event positive cumulative-flux
ancestor.

In a follow-up pass, the reviewer also accepted the event-adaptive
annulus squeeze.  The finite sharp frequency-dissipation measure lets
one choose \(K_j/\Lambda_j\to1\) so that the annular branch is absent.
Reapplying the exact energy identity then forces a terminal signed-flux
interval at every sufficiently late event.

## Accepted last-hitting lemma

For

\[
E_K(t)=\|Q_{>K}v(t)\|_2^2
\]

and \(v\in C_{\rm loc}((0,T^*);H^1)\), the map
\(t\mapsto E_K(t)\) is continuous.  At a fixed earlier time
\(t_\circ\),

\[
E_{K_j}(t_\circ)
\le
K_j^{-2}\|\nabla v(t_\circ)\|_2^2.
\]

If

\[
\Theta_jK_j^2\to\infty,
\qquad
E_{K_j}(a_j)\ge\Theta_j,
\]

then the fixed-time tail is eventually below \(\Theta_j/2\).  The
half-level set is nonempty and compact, and its last point
\(s_j\) satisfies

\[
t_\circ<s_j<a_j,
\qquad
E_{K_j}(s_j)=\frac{\Theta_j}{2}.
\]

The exact forward-time high-pass identity gives

\[
\begin{aligned}
\Phi_{K_j}((s_j,a_j))
&=
\frac12
\left(
E_{K_j}(a_j)-E_{K_j}(s_j)
\right)
+
\nu D^\sharp_{>K_j}((s_j,a_j))
\\
&\ge
\frac{\Theta_j}{4}.
\end{aligned}
\]

The reviewer confirmed the sign, the factor \(1/4\), and legitimacy of
the index-dependent sharp projector.

## Accepted terminal localisation

If the hitting times failed to approach \(T^*\), some
\(\delta>0\) and subsequence would satisfy
\(s_j\le T^*-\delta\).  Compact-time \(H^1\) continuity gives

\[
M_\delta
:=
\sup_{t_\circ\le t\le T^*-\delta}
\|\nabla v(t)\|_2^2
<
\infty.
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

contradicting the scale hypothesis.  Thus \(s_j\to T^*\) along every
infinite set of indices on which the inherited threshold occurs.

## Accepted parabolic scale

For

\[
T_j
=
\frac{c_\kappa}{C_\chi^2}\sigma_jh_j^{-3},
\qquad
K_j
=
R_j\frac{\kappa h_j^{-1/2}}{\sigma_j},
\]

and the reviewed inherited threshold
\(\Theta_j=\nu T_j/2\), the reviewer confirmed

\[
\Theta_jK_j^2
=
\frac{\nu c_\kappa\kappa^2}{2C_\chi^2}
R_j^2\sigma_j^{-1}h_j^{-4}
\longrightarrow\infty.
\]

Hence the inherited branch produces

\[
\Phi_{K_j}((s_j,t_j^-))
\ge
\frac{\nu T_j}{8}.
\]

This remains valid for arbitrary index-dependent \(R_j>1\), with
\(\kappa\) fixed.  The fact that \(T_j\to0\) does not reverse the
comparison; the product with \(K_j^2\) diverges.

## Accepted quantifier and scope repairs

The first review required two repairs, both now incorporated.

1. Last-hitting ancestors are defined only on inherited-branch
   indices.  If that index set is infinite, \(s_j\to T^*\) along it.
   Sequence convergence is not embedded unqualified inside a
   per-index disjunction.
2. The note no longer says that inherited energy is impossible or
   literally removed.  Its exact statement is:

   > The entrance threshold cannot be accounted for solely by the tail
   > present at any fixed earlier time; the inherited-energy
   > bookkeeping branch is replaced by a terminal pre-event
   > cumulative-flux branch.

This leaves open reuse of one earlier cascade reservoir across many
indices.

## Accepted adaptive-annulus strengthening

For fixed \(j\), define

\[
\mu_j(B)
:=
\int_{I_j}\int_B
|\xi|^2|\widehat v(\xi,t)|^2\,d\xi\,dt.
\]

This is a finite measure.  The annuli

\[
A_j(R)
=
\{\xi:\Lambda_j<|\xi|\le R\Lambda_j\}
\]

decrease to the empty set as \(R\downarrow1\).  Continuity from above
therefore gives

\[
\mu_j(A_j(R))\to0.
\]

Choose

\[
1<R_j<1+\frac1j,
\qquad
D^\sharp_{\Lambda_j<|\xi|\le R_j\Lambda_j}(I_j)
<
\frac{T_j}{4}.
\]

The exact sharp total floor then yields

\[
D^\sharp_{>R_j\Lambda_j}(I_j)
>
\frac{3T_j}{4}.
\]

If the entrance energy above \(K_j=R_j\Lambda_j\) is below
\(\nu T_j\), the exact identity gives

\[
\Phi_{K_j}(I_j)
>
-\frac{\nu T_j}{2}
+
\frac{3\nu T_j}{4}
=
\frac{\nu T_j}{4}.
\]

If it is at least \(\nu T_j\), apply the last-hitting lemma with
\(\Theta_j=\nu T_j\).  The historical interval then also satisfies

\[
\Phi_{K_j}((s_j,t_j^-))
\ge
\frac{\nu T_j}{4}.
\]

The two entrance-energy cases are disjoint and exhaustive.  Thus, for
every sufficiently large \(j\), one obtains an interval
\(J_j=(\alpha_j,\beta_j)\) such that

\[
\boxed{
\frac{K_j}{\Lambda_j}\to1,
\qquad
\alpha_j,\beta_j\to T^*,
\qquad
\Phi_{K_j}(J_j)\ge\frac{\nu T_j}{4}.
}
\]

The reviewer confirmed that event-dependent \(R_j\) is legitimate.
The conclusion is existential at a cutoff asymptotic to
\(\Lambda_j\); it does not assert the flux floor at any prescribed
fixed factor \(R>1\).

## Exact accepted frontier

The reviewed parabolic pressure tail now forces genuine positive
signed nonlinear input on a terminal interval of the same physical
Navier--Stokes trajectory, across a frequency boundary asymptotic to
the parabolic cutoff.  Comparable-annulus and inherited-state
bookkeeping are no longer terminal alternatives for this
event-adaptive conclusion.

The flux is still cumulative.  Neither the theorem nor its tests prove
that the intervals are disjoint, that the payments sum, that one
cascade cannot cross many boundaries, that an intervening selected
Besov event occurs, or that the terminal cascade has non-Zeno depth.
This does not exclude the conditional ancient profile, prove
regularity or breakdown, or establish any Clay alternative A--D.

## Validation

The focused suite has eight passing tests.  After canonical
synchronisation, full validation reported:

- 35 sources, 30 claims, 23 routes, 109 experiments, and 16
  obligations;
- 880 valid local-link targets;
- 33,264 balanced math delimiters;
- all 825 tests passing; and
- `git diff --check` passing.
