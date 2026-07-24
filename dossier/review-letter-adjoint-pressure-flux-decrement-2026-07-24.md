# Independent review request: weak-\(L^3\) lower-band flux decrement

**Date:** 2026-07-24

**Clay status:** unsolved

**Primary note:**
[`experiments/adjoint-pressure-flux-decrement.md`](experiments/adjoint-pressure-flux-decrement.md)

**Reviewed input:**
[`experiments/adjoint-pressure-inherited-ancestry.md`](experiments/adjoint-pressure-inherited-ancestry.md)

## Requested disposition

Please classify the candidate note as one of:

1. valid in its stated conditional same-trajectory scope;
2. repairable, with exact repairs;
3. fatal analytic gap; or
4. correct but duplicative of an earlier recorded result.

Do not assess it as a Clay solution.  It explicitly leaves an infinite
geometrically decaying cascade open.

## Claim A: exact sharp/smooth flux decomposition

For a smooth finite-energy Navier--Stokes velocity with

\[
\sup_{t\in I}\|v(t)\|_{L^{3,\infty}}\le M,
\]

put

\[
h=Q_{>K}v,
\qquad
u=S_Lv,
\qquad
m=P_{\le K}v-S_Lv,
\qquad
0<L<K/4,
\]

where the smooth multiplier \(S_L\) is one below \(L\) and zero above
\(2L\).  The note claims

\[
\mathcal F_K
:=
-
\left\langle
Q_{>K}\mathbb P\operatorname{div}(v\otimes v),h
\right\rangle
=
-
\int h_i h_j\partial_ju_i
+\mathcal R_{L,K},
\]

and

\[
|\mathcal R_{L,K}|
\le
C_0M\|\nabla h\|_2\|\nabla m\|_2.
\]

Please check:

1. the sign relating the projected nonlinearity to
   \(\int v_i v_j\partial_jh_i\);
2. exactness of \(v=u+m+h\);
3. all support statements, especially vanishing of the \(u\)-\(u\)
   term when \(4L<K\);
4. the tensor expansion
   \[
   v\otimes v-(u+h)\otimes(u+h)
   =
   m\otimes v+(u+h)\otimes m;
   \]
5. both integrations by parts in the remainder;
6. whether the proof ever uses false \(L^p\) boundedness of the sharp
   ball projector; and
7. whether Lorentz Hölder and
   \(\dot H^1\hookrightarrow L^{6,2}\) give the asserted endpoint
   product.

## Claim B: far-low strain is viscosity-small

The smooth low-pass estimate and spectral gaps give

\[
\|\nabla u\|_\infty\le C_{\rm lp}ML^2,
\]

\[
\|h\|_2\le K^{-1}\|\nabla h\|_2,
\qquad
\|m\|_2\le L^{-1}\|\nabla m\|_2.
\]

Hence

\[
\left|
\int h_i h_j\partial_ju_i
\right|
\le
C_{\rm lp}M(L/K)^2\|\nabla h\|_2^2.
\]

With

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

the time integral is at most \(\nu D_h/12\).

Please check the endpoint Lorentz--Young estimate for the smooth kernel,
the powers \(L^2\) and \(K^{-1}L^{-1}\), and the cutoff-ratio constant.

## Claim C: low-entrance decrement

Suppose

\[
E_K(a)<\nu T,
\qquad
D_h(I)>\frac{3T}{4}.
\]

The high-pass identity gives

\[
F:=\Phi_K(I)>\frac{\nu T}{4},
\qquad
\nu D_h(I)<3F.
\]

After subtracting the far-low term, the note obtains

\[
C_0M\sqrt{D_hD_m}\ge\frac{3F}{4},
\]

and therefore

\[
D_m
\ge
\frac{3}{16C_0^2}\frac{\nu}{M^2}F
\ge
\frac{3}{64C_0^2}\frac{\nu^2}{M^2}T.
\]

Please recompute every inequality direction and constant, including the
use of \(E_K(b)\ge0\).

## Claim D: half-to-full hitting decrement

If

\[
E_K(a)=\frac{\Theta}{2},
\qquad
E_K(b)=\Theta,
\]

then

\[
F=\frac{\Theta}{4}+\nu D_h,
\qquad
\nu D_h\le F.
\]

The claimed conclusion is

\[
D_m
\ge
\frac{121}{144C_0^2}\frac{\nu}{M^2}F.
\]

Please check the \(11/12\) remainder fraction and whether \(D_h=0\)
needs separate treatment.

## Claim E: terminal pressure-tail application

For the reviewed adaptive cutoff \(K_j/\Lambda_j\to1\), the note uses:

1. low entrance:
   \[
   E_{K_j}(t_j^-)<\nu T_j,
   \qquad
   D_{>K_j}(I_j)>3T_j/4;
   \]
2. high entrance:
   a last hit of \(\nu T_j/2\), followed by the first hit of
   \(\nu T_j\).

It concludes in both cases that a terminal interval
\(\widetilde J_j\) satisfies

\[
\int_{\widetilde J_j}
\left\|
\nabla(P_{\le K_j}-S_{\eta K_j})v
\right\|_2^2\,dt
\ge
c_*\frac{\nu^2}{M^2}T_j.
\]

Please check:

1. existence and placement of the first full-level hit;
2. convergence of both endpoints to \(T^*\);
3. availability of the uniform weak-\(L^3\) ceiling on the historical
   interval;
4. whether the multiplier is genuinely confined to a fixed comparable
   lower band; and
5. whether the conclusion holds for every sufficiently late event.

## Claim F: exact scope of the advance

The note says that the near-lossless conservative shell ledger is
excluded because every charged boundary now obeys

\[
\frac{\nu D_m}{F}
\ge
c_{\rm dec}\left(\frac{\nu}{M}\right)^2>0.
\]

It does **not** claim that:

- event intervals or bands are disjoint;
- \(T_j\) has a scale-zero lower bound;
- a geometrically decaying cascade has finite depth;
- the direct-response ancestor is excluded;
- the limiting adjoint-pressure cost is finite; or
- any Clay alternative is proved.

Please decide whether “near-lossless ledger excluded” is exact in this
restricted sense, and whether any earlier repository theorem already
proves the same lower-band decrement.
