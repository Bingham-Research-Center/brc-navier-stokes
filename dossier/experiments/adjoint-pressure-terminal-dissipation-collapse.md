# Current nonlinear work collapses into nested terminal dissipation

- **Experiment:** EXP-ADJOINT-PRESSURE-TERMINAL-DISSIPATION-COLLAPSE-001
- **Route:** ROUTE-R3B
- **Status:** conditional same-genealogy analytic reduction
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** [spatial high-pass payer](adjoint-pressure-spatial-highpass-payer.md)
  and [staggered entrance ancestry](adjoint-pressure-staggered-entrance-ancestry.md)
- **External review:** pending
- **Adversarial recomputation:** accepted; no fatal or major gap found

The preceding reductions left two upper-audit payers: current-window
spatially cut-off high-pass nonlinear work and staggered prehistory
dissipation.  The current work is not independent.

Testing its exact projected pairing before taking absolute values, using the
global weak-\(L^3\) coefficient bound, and absorbing one quarter of the local
filtered dissipation through the exact energy identity gives

\[
\Phi_{n,k}^+
\le
C E_{n,k}(-T)
+\frac{CM^2}{\nu}\Delta_n^{\rm cur}
+\frac{C\nu M^2T}{R_k},
\tag{1}
\]

where

\[
\Delta_n^{\rm cur}
:=
\int_{-T}^0\|\nabla u_n(t)\|_2^2\,dt.
\tag{2}
\]

Extend each staggered prehistory interval through the current window and let
\(\widehat\delta_{n,k}\) be the physical dissipation on that extended
interval.  Define

\[
\widehat{\mathfrak D}_n(T;r_\bullet)
:=
\sum_{k=0}^{K_n}
\left(
\frac{\widehat\delta_{n,k}}{r_{n,k}}
\right)^{1/2},
\qquad
r_{n,k}:=\rho_nR_k.
\tag{3}
\]

Then the whole pressure upper audit reduces to

\[
\boxed{
P_n(T)
\le
C
+C\widehat{\mathfrak D}_n(T;r_\bullet)
+\varepsilon_n(r_\bullet).
}
\tag{4}
\]

Thus divergent finite-window pressure histories force one precise nested
critical physical-dissipation action to diverge below every fixed admissible
physical cutoff.  Entrance energy, current nonlinear work, remote
inheritance, macroscopic shells, and spatial diffusion leakage are no longer
independent branches of this upper audit.

This is still not a pressure bound.  Finite physical dissipation gives no
uniform control of (3), because its intervals overlap and it has an
\(\ell^1\) square-root secondary index.  A terminal power modulus
\(s^\alpha\) controls (3) for every \(\alpha>1/2\); the scalar critical
survivor from the staggered-ancestry theorem remains at \(\alpha=1/2\).

## 1. Imported setting

Retain the smooth finite-energy genealogy \(u_n\) on \([-H_n,0]\), the
uniform bound

\[
\sup_n\sup_{-H_n\le t\le0}
\|u_n(t)\|_{L^{3,\infty}}
\le M,
\tag{5}
\]

the geometric radii \(R_k=L^kR_0\), and the exterior adjoint tail

\[
\mathcal A_{n,k}(T)\le A_*R_k^{-1/2}.
\tag{6}
\]

For a fixed admissible physical cutoff, let

\[
K_n=\max\{k:\rho_nR_k\le r_\bullet\},
\qquad
j_{n,k}=K_n-k,
\tag{7}
\]

and use the staggered lookback

\[
\ell_{n,k}
=
\frac{\gamma(j_{n,k}+1)R_k^2}{\nu}.
\tag{8}
\]

The preceding theorem proves that these lookbacks all fit inside the
genealogy horizon and that the entrance-energy aggregate satisfies

\[
\mathfrak E_n
\le C+C\mathfrak Z_n,
\qquad
\mathfrak Z_n
\le
C\mathfrak D_n^{\rm stag}.
\tag{9}
\]

Here \(\mathfrak D_n^{\rm stag}\) uses only
\([-T-\ell_{n,k},-T]\).  The present theorem adds the adjacent current
window \([-T,0]\).

## 2. Projected work estimate

Use real even Littlewood--Paley multipliers and put

\[
w_{n,k}
:=
\mathsf S_{>R_k^{-1}}u_n.
\tag{10}
\]

Let \(\chi_k\) be the annular cutoff from the spatial high-pass theorem,
write \(\Omega_k=\operatorname{supp}\chi_k\), and recall

\[
\Phi_{n,k}
=
-
\int_{-T}^0
\int_{\mathbb R^3}
\chi_k^2w_{n,k}\cdot
\mathsf S_{>R_k^{-1}}
\mathbb P\operatorname{div}(u_n\otimes u_n)
\,dx\,dt.
\tag{11}
\]

Self-adjointness of the real even multiplier and Leray projection gives the
exact representation

\[
\Phi_{n,k}
=
\int_{-T}^0
\int_{\mathbb R^3}
\nabla\mathbb P\mathsf S_{>R_k^{-1}}
(\chi_k^2w_{n,k})
:
(u_n\otimes u_n)
\,dx\,dt.
\tag{12}
\]

No spatial source localisation is asserted in (12).  The \(L^2\) multiplier
bound and the cutoff estimates imply

\[
\left\|
\nabla\mathbb P\mathsf S_{>R_k^{-1}}
(\chi_k^2w_{n,k})
\right\|_2
\le
C
\left(
\|\chi_k\nabla w_{n,k}\|_2
+R_k^{-1}\|1_{\Omega_k}w_{n,k}\|_2
\right).
\tag{13}
\]

Lorentz interpolation and Sobolev give

\[
\|u_n\otimes u_n\|_2
=\|u_n\|_4^2
\le
C\|u_n\|_{L^{3,\infty}}\|u_n\|_6
\le
CM\|\nabla u_n\|_2.
\tag{14}
\]

The high-pass multiplier is bounded on \(L^{3,\infty}\), while
\(|\Omega_k|\le C_LR_k^3\).  Hence

\[
R_k^{-1}\|1_{\Omega_k}w_{n,k}(t)\|_2
\le
CMR_k^{-1/2}.
\tag{15}
\]

With

\[
D_{n,k}
:=
\int_{-T}^0
\|\chi_k\nabla w_{n,k}(t)\|_2^2\,dt,
\tag{16}
\]

equations (12)--(15) and Cauchy--Schwarz in time yield

\[
\Phi_{n,k}^+
\le
CM D_{n,k}^{1/2}
(\Delta_n^{\rm cur})^{1/2}
+CM^2\sqrt T\,R_k^{-1/2}
(\Delta_n^{\rm cur})^{1/2}.
\tag{17}
\]

Young's inequality therefore gives

\[
\Phi_{n,k}^+
\le
\frac{\nu}{4}D_{n,k}
+\frac{CM^2}{\nu}\Delta_n^{\rm cur}
+\frac{C\nu M^2T}{R_k}.
\tag{18}
\]

## 3. Absorption through the local energy identity

The exact filtered-energy identity is

\[
\Phi_{n,k}
=
\frac12
\left(
E_{n,k}(0)-E_{n,k}(-T)
\right)
+\nu D_{n,k}
-\frac{\nu}{2}B_{n,k},
\tag{19}
\]

and its one-sided consequence is

\[
D_{n,k}
\le
\frac{\Phi_{n,k}^+}{\nu}
+\frac{E_{n,k}(-T)}{2\nu}
+\frac{|B_{n,k}|}{2}.
\tag{20}
\]

Insert (20) into the first term of (18) and absorb
\(\frac14\Phi_{n,k}^+\) into the left side.  The spatial boundary estimate

\[
|B_{n,k}|
\le
\frac{CM^2T}{R_k}
\tag{21}
\]

then proves (1).  This use of (19) is essential: a direct absolute-value
estimate of (11) alone would leave the unknown local filtered dissipation.

Taking square roots in (1) gives

\[
\left(\frac{\Phi_{n,k}^+}{\nu}\right)^{1/2}
\le
C\left(\frac{E_{n,k}(-T)}{\nu}\right)^{1/2}
+\frac{CM}{\nu}(\Delta_n^{\rm cur})^{1/2}
+CM\left(\frac{T}{R_k}\right)^{1/2}.
\tag{22}
\]

## 4. One extended physical action

Define the extended normalised interval and dissipation

\[
\widehat I_{n,k}
:=
[-T-\ell_{n,k},0],
\qquad
\widehat\Delta_{n,k}
:=
\int_{\widehat I_{n,k}}
\|\nabla u_n(t)\|_2^2\,dt.
\tag{23}
\]

Plainly

\[
\Delta_n^{\rm cur}\le\widehat\Delta_{n,k},
\qquad
\Delta_{n,k}\le\widehat\Delta_{n,k},
\tag{24}
\]

where \(\Delta_{n,k}\) is the staggered prehistory dissipation from the
preceding theorem.

Let \(\widehat J_{n,k}\) be the pullback of \(\widehat I_{n,k}\) to the
original physical trajectory and put

\[
\widehat\delta_{n,k}
:=
\int_{\widehat J_{n,k}}
\|\nabla v(t)\|_2^2\,dt.
\tag{25}
\]

The exact physical scaling is

\[
\widehat\Delta_{n,k}
=
\frac{\widehat\delta_{n,k}}
{\nu_{\rm phys}\rho_n}.
\tag{26}
\]

Multiply (22) by \(\mathcal A_{n,k}(T)\), use (6), (24), and (26), and
sum \(0\le k\le K_n\).  The final term is a geometric reciprocal-radius
sum, while the middle term becomes (3).  Thus

\[
\boxed{
\mathfrak F_n(T;r_\bullet)
\le
C
+C\mathfrak E_n(T;r_\bullet)
+\frac{CA_*M}{\nu\sqrt{\nu_{\rm phys}}}
\widehat{\mathfrak D}_n(T;r_\bullet).
}
\tag{27}
\]

Because \(\widehat\delta_{n,k}\) dominates the prehistory dissipation,
(9) also gives

\[
\mathfrak E_n(T;r_\bullet)
\le
C
+C\widehat{\mathfrak D}_n(T;r_\bullet).
\tag{28}
\]

Insert (27)--(28) into the spatial high-pass payer theorem:

\[
\boxed{
\mathfrak Q_n(T;r_\bullet)
\le
C
+C\widehat{\mathfrak D}_n(T;r_\bullet).
}
\tag{29}
\]

The one-heat-time pressure upper audit now proves (4).  In particular,

\[
\liminf_{n\to\infty}
\widehat{\mathfrak D}_n(T;r_\bullet)<\infty
\quad\Longrightarrow\quad
\mathfrak p^\mathcal G_{\psi,T}<\infty,
\tag{30}
\]

whereas

\[
P_{n_j}(T)\longrightarrow\infty
\quad\Longrightarrow\quad
\widehat{\mathfrak D}_{n_j}(T;r_\bullet)
\longrightarrow\infty
\tag{31}
\]

for every fixed admissible cutoff.

## 5. Geometry and the remaining endpoint

The intervals \(\widehat J_{n,k}\) end at the same physical preterminal time.
In the inward index \(j\), their normalised lengths are
\(T+\ell_j\), and

\[
\ell_{j+1}
=
\frac{j+2}{j+1}L^{-2}\ell_j
<\ell_j.
\tag{32}
\]

They are therefore nested.  For all sufficiently large \(n\), their
exact terminal pullback depth is

\[
T^*-\inf\widehat J_{n,k}
=
\frac{\rho_n^2}{\nu_{\rm phys}}
\left(
T+\ell_{n,k}+\varepsilon_n
\right).
\tag{33}
\]

The imported shift satisfies \(\varepsilon_n<1/n\), so this depth is at most

\[
C_0(j_{n,k}+1)r_{n,k}^2,
\tag{34}
\]

where \(C_0\) depends on the fixed parameters but not on \(n,k\).  The
additional current window costs only

\[
\frac{\rho_n^2T}{\nu_{\rm phys}}
\le
\frac{T}{\nu_{\rm phys}R_0^2}r_{n,k}^2.
\tag{35}
\]

Consequently, shrink the fixed cutoff so that
\(C_0r_\bullet^2<s_\alpha\).  If

\[
\int_{T^*-s}^{T^*}\|\nabla v(t)\|_2^2\,dt
\le C_\alpha s^\alpha
\tag{36}
\]

for some \(\alpha>1/2\) and \(0<s<s_\alpha\), then

\[
\widehat{\mathfrak D}_n(T;r_\bullet)
\le
C
r_\bullet^{\alpha-1/2}
\sum_{j\ge0}
(j+1)^{\alpha/2}
L^{-(\alpha-1/2)j}
<\infty.
\tag{37}
\]

At \(\alpha=1/2\), the geometric gain vanishes.  The triangular scalar
history in the staggered-ancestry theorem already obeys a uniform
square-root modulus while its corresponding action diverges.  It is not one
NSE trajectory, and logarithmic critical improvements remain unclassified.

## 6. Exact route consequence

Within the conditional pressure upper audit, this theorem closes:

1. current spatially cut-off nonlinear work as an independent payer;
2. the need to spatially localise the projected nonlinear source merely to
   estimate that payer;
3. all prior entrance, inheritance, macroscopic-shell, and boundary branches
   into the single extended action (3); and
4. every terminal dissipation power modulus strictly better than
   \(s^{1/2}\) as sufficient for a finite upper audit.

It does not prove:

1. finiteness of the critical action (3);
2. a logarithmic gain at the critical power;
3. disjointness, bounded overlap, non-reuse, or one charged block;
4. a finite event-index sum or contradiction with recurring Besov events;
5. exclusion of the coherent ancient profile; or
6. regularity, breakdown, or any Clay alternative A--D.

The next theorem must use actual NSE structure to control the critical nested
terminal action, compare it with the already forced lower-band decrements, or
produce a signed non-reuse law across event indices.

No executable certificate is claimed for the multiplier, Lorentz, or PDE
steps.
