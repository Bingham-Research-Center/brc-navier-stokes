# Independent review response: weak-\(L^3\) lower-band flux decrement

**Date:** 2026-07-24

**Reviewed request:**
`review-letter-adjoint-pressure-flux-decrement-2026-07-24.md` (archived in Git at `c277792`)

**Primary theorem:**
[`experiments/adjoint-pressure-flux-decrement.md`](experiments/adjoint-pressure-flux-decrement.md)

**Verdict:** valid and nonduplicative in the stated conditional
same-trajectory scope after five precision repairs

**Clay status:** unsolved

## Reviewer disposition

The independent mathematical AI recomputed the sharp high-pass flux
sign, the mixed sharp/smooth Fourier decomposition, every
divergence-free cancellation, the endpoint Lorentz estimates, and both
terminal-interval constant ledgers.  It found no fatal analytic gap and
no duplication of an earlier repository theorem.

The theorem supplies the first quantitative weak-\(L^3\) decrement for
the terminal flux forced by the reviewed pressure-tail chain.  It rules
out the preceding conservative ledger's asymptotically lossless
distinct-shell traversal.  It does not yet make different physical
event indices fresh.

## Accepted sharp/smooth decomposition

With

\[
h=Q_{>K}v,
\qquad
u=S_Lv,
\qquad
m=P_{\le K}v-S_Lv,
\qquad
4L<K,
\]

the reviewer confirmed

\[
v=u+m+h
\]

and the exact support separation

\[
\operatorname{supp}\widehat u\subset\{|\xi|\le2L\},
\quad
\operatorname{supp}\widehat m\subset\{L\le|\xi|\le K\},
\quad
\operatorname{supp}\widehat h\subset\{|\xi|>K\}.
\]

The high-pass sign is

\[
\mathcal F_K
=
-
\left\langle
Q_{>K}\mathbb P\operatorname{div}(v\otimes v),h
\right\rangle
=
\int v_i v_j\partial_jh_i.
\]

The \(u\)-\(u\) term vanishes by Fourier support.  The remaining part
with no \(m\)-factor is

\[
\mathcal A_{L,K}
=
-
\int h_i h_j\partial_ju_i.
\]

The tensor identity

\[
v\otimes v-(u+h)\otimes(u+h)
=
m\otimes v+(u+h)\otimes m
\]

and two integrations by parts leave a remainder satisfying

\[
|\mathcal R_{L,K}|
\le
C_0M\|\nabla h\|_2\|\nabla m\|_2.
\]

The reviewer specifically confirmed that no false
\(L^{3,\infty}\)-boundedness of the sharp ball multiplier is used.
Sharp projectors occur only in \(L^2\).  The sole weak-\(L^3\) factor in
the endpoint product is the full velocity \(v\).

## Accepted far-low estimate

For the fixed smooth low-pass,

\[
\|\nabla S_Lv\|_\infty
\le
C_{\rm lp}ML^2
\]

by Lorentz Young, while Plancherel gives

\[
\|h\|_2\le K^{-1}\|\nabla h\|_2,
\qquad
\|m\|_2\le L^{-1}\|\nabla m\|_2.
\]

Thus

\[
|\mathcal A_{L,K}|
\le
C_{\rm lp}M(L/K)^2\|\nabla h\|_2^2.
\]

The reviewed choice

\[
\eta
=
\min\left\{
\frac18,
\left(\frac{\nu}{12C_{\rm lp}M}\right)^{1/2}
\right\},
\qquad
L=\eta K,
\]

makes the integrated far-low contribution at most
\(\nu D_h/12\).

## Accepted interval constants

On a low-entrance interval,

\[
E_K(a)<\nu T,
\qquad
D_h>\frac{3T}{4},
\]

the exact high-pass identity gives

\[
F>\frac{\nu T}{4},
\qquad
\nu D_h<3F.
\]

The reviewer confirmed

\[
D_m
\ge
\frac{3}{16C_0^2}\frac{\nu}{M^2}F
\ge
\frac{3}{64C_0^2}\frac{\nu^2}{M^2}T.
\]

On a half-to-full hitting interval,

\[
E_K(a)=\frac{\Theta}{2},
\qquad
E_K(b)=\Theta,
\]

one has

\[
F=\frac{\Theta}{4}+\nu D_h,
\qquad
\nu D_h\le F,
\]

and the accepted constant is

\[
D_m
\ge
\frac{121}{144C_0^2}\frac{\nu}{M^2}F
\ge
\frac{121}{576C_0^2}\frac{\nu}{M^2}\Theta.
\]

If \(D_h=0\), the remainder estimate would contradict
\(F=\Theta/4>0\), so no unhandled zero-denominator case remains.

## Accepted pressure-tail application

In the low-entrance branch, the adaptive annulus squeeze gives

\[
E_{K_j}(t_j^-)<\nu T_j,
\qquad
D_{>K_j}(I_j)>\frac{3T_j}{4}.
\]

In the high-entrance branch, the reviewed last hit of
\(\nu T_j/2\) is followed by a first hit of \(\nu T_j\).  The reviewer
confirmed that this first hit exists, lies before \(t_j^-\), and that
both endpoints tend to \(T^*\) along every infinite high-entrance index
set.

The explicit terminal assumption

\[
\operatorname*{ess\,sup}_{t_{\rm w}<t<T^*}
\|v(t)\|_{L^{3,\infty}}
\le M
\]

therefore covers every sufficiently late historical interval.
Consequently every late pressure-tail event has a terminal interval
\(\widetilde J_j\) satisfying

\[
\int_{\widetilde J_j}
\left\|
\nabla(P_{\le K_j}-S_{\eta K_j})v
\right\|_2^2\,dt
\ge
c_*\frac{\nu^2}{M^2}T_j.
\]

Because \(0\le\chi_{\rm lp}\le1\), this implies the genuine sharp
annular bound

\[
\int_{\widetilde J_j}
\|\nabla Q_{\eta K_j<|\xi|\le K_j}v\|_2^2\,dt
\ge
c_*\frac{\nu^2}{M^2}T_j.
\]

## Required and incorporated precision repairs

The review required five repairs, all incorporated.

1. The weak-\(L^3\) bounds are written as essential suprema.
2. \(R_j\to1\) is used without an unproved monotonicity assertion, and
   convergence of \(s_j,r_j\) is scoped to infinite high-entrance
   index sets.
3. The smooth lower-band dissipation is explicitly dominated by the
   corresponding sharp annular dissipation.
4. The shell consequence is restricted to the specific near-lossless
   distinct-shell ledger.  Geometric decay across the physical event
   sequence still requires fresh or bounded-overlap charges.
5. The executable target is registered in the Makefile.

## Exact surviving gap

The accepted theorem gives the per-boundary decrement

\[
\frac{\nu D_m}{F}
\ge
c_{\rm dec}\left(\frac{\nu}{M}\right)^2.
\]

It does not prove that event-index intervals or bands are distinct.
Nor does it prevent an infinite geometrically decaying cascade whose
physical event floors tend to zero.  Those are now the exact surviving
reuse mechanisms.

No ancient Liouville theorem, regularity theorem, breakdown theorem, or
Clay alternative A--D is proved.

## Validation

The reviewer reported:

- all 9 targeted scalar-ledger tests passed;
- all 834 repository tests passed at the review snapshot; and
- `git diff --check` passed.
