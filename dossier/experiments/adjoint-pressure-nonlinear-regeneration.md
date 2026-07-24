# Borderline annular pressure must be nonlinearly regenerated

- **Experiment:** EXP-ADJOINT-PRESSURE-NONLINEAR-REGENERATION-001
- **Route:** ROUTE-R3B
- **Status:** conditional same-genealogy analytic reduction
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** [annular pressure cost](adjoint-pressure-annular-cost.md),
  [adjoint-pressure history](adjoint-pressure-history.md), and
  [physical outer profile](terminal-outer-profile.md)
- **External review:** pending

The annular cost theorem left one exact endpoint.  If

\[
\mathcal A_{n,k}(T)
:=
\left(
\int_0^T
\|a_{n,\psi}(\tau)\|_{L^2(|x|>2R_k)}^2\,d\tau
\right)^{1/2}
\lesssim R_k^{-1/2},
\tag{1}
\]

then centre-uniform coefficient dissipation permits order-one pressure
cost on every shell \(R_k=L^kR_0\).  A static cell cloud can saturate
those powers.

That cloud is not a passive survivor on the physical genealogy.
Split the coefficient on the \(R_k\)-shell at reciprocal frequency
\(R_k^{-1}\).

1. The low-frequency gradient costs \(R_k^{-1}\) after multiplication
   by (1), so its shell sum is finite.
2. Write the high-frequency coefficient by the exact forward
   Navier--Stokes Duhamel formula from the remote end of the same
   genealogy.  Its linearly inherited part has total annular cost

   \[
   C_{\psi,M,T}\,
   \mathcal E_n(\nu L_n)^{-3/4},
   \tag{2}
   \]

   where \(\mathcal E_n\) is the global \(L^2\) energy ceiling and
   \(L_n\) is the available look-back horizon.
3. On the physical outer genealogy,

   \[
   \mathcal E_n\lesssim\rho_n^{-1/2},
   \qquad
   L_n\asymp\rho_n^{-2},
   \tag{3}
   \]

   so (2) is \(O(\rho_n)\to0\).

Consequently every non-summable borderline annular cost must be carried
by the high-frequency nonlinear Duhamel regeneration field

\[
\mathcal R_{n,k}(\tau)
=
-
\mathsf S_{>R_k^{-1}}
\int_0^{L_n}
e^{\nu s\Delta}
\mathbb P\operatorname{div}
\bigl(
b_n(\tau+s)\otimes b_n(\tau+s)
\bigr)\,ds.
\tag{4}
\]

More precisely, define

\[
\mathfrak R_n(T)
:=
\sum_{k\ge0}
\mathcal A_{n,k}(T)
\left(
\int_0^T
\|\nabla\mathcal R_{n,k}(\tau)\|_{L^2(\mathcal C_k)}^2\,d\tau
\right)^{1/2},
\tag{5}
\]

where \(\mathcal C_k\) is the enlarged coefficient annulus from the
preceding theorem.  Then

\[
\boxed{
\int_0^T
\|\nabla\pi^*_{n,\psi}(\tau)\|_1\,d\tau
\le
C_{\psi,M,\nu,T,R_0}
+C\mathfrak R_n(T)
+o_{n\to\infty}(1).
}
\tag{6}
\]

Thus

\[
\liminf_{n\to\infty}\mathfrak R_n(T)<\infty
\quad\Longrightarrow\quad
\mathfrak p^\mathcal G_{\psi,T}<\infty.
\tag{7}
\]

The divergent global energy has now been removed twice: first by
annular localisation and then from the remote inherited high-frequency
field by heat erasure.  The live obstruction is an actual
Navier--Stokes nonlinear regeneration action on the same trajectory.

This does not bound (5), prove that regeneration is recent or
event-index fresh, control its sign, or exclude its repeated reuse.  It
does not prove the pressure cost finite, exclude the ancient profile,
or prove any Clay alternative.

## 1. Imported annular upper estimate

Let

\[
\mathcal G=\{(u_n,H_n)\}_{n\ge1}
\tag{8}
\]

be the smooth physical genealogy.  In reversed time write

\[
b_n(\tau)=u_n(-\tau),
\qquad
0\le\tau\le H_n.
\tag{9}
\]

Fix \(T>0\), one compact solenoidal terminal test \(\psi\), and let
\((a_{n,\psi},\pi^*_{n,\psi})\) solve the Oseen adjoint on \([0,T]\).
Retain

\[
\sup_n\sup_{0\le\tau\le H_n}
\|b_n(\tau)\|_{L^{3,\infty}}\le M.
\tag{10}
\]

The preceding theorem uses radii

\[
R_k=L^kR_0,
\qquad
L\ge16,
\tag{11}
\]

coefficient annuli

\[
\mathcal C_k
\subset
B_{8R_{k+1}}\setminus B_{4R_k},
\tag{12}
\]

and the exterior adjoint tails (1).  Its CLMS--Bogovskii estimate is

\[
\begin{aligned}
\int_0^T\|\nabla\pi^*_{n,\psi}\|_1\,d\tau
\le{}&
C_{\rm in}\\
&+
C\sum_{k\ge0}\mathcal A_{n,k}(T)
\bigg[
\left(
\int_0^T
\|\nabla b_n\|_{L^2(\mathcal C_k)}^2\,d\tau
\right)^{1/2}\\
&\hspace{42mm}
+M\left(\frac{T}{R_k}\right)^{1/2}
\bigg].
\end{aligned}
\tag{13}
\]

The last cutoff term in (13) is already summable under the endpoint
tail

\[
\boxed{
\mathcal A_{n,k}(T)\le A_*R_k^{-1/2},
}
\tag{14}
\]

uniformly on the selected genealogy diagonal.  Indeed,

\[
\sum_{k\ge0}
\mathcal A_{n,k}(T)
M\left(\frac{T}{R_k}\right)^{1/2}
\le
A_*M\sqrt T
\sum_{k\ge0}R_k^{-1}
<\infty.
\tag{15}
\]

Only the coefficient-gradient term needs further analysis.

## 2. Reciprocal-frequency low modes are summable

Let \(\mathsf S_{\le\kappa}\) be one fixed smooth
Littlewood--Paley low-pass multiplier, chosen so that its complementary
multiplier is supported in \(\{|\xi|\ge c_0\kappa\}\), and

\[
\mathsf S_{>\kappa}=I-\mathsf S_{\le\kappa}.
\tag{16}
\]

Lorentz multiplier boundedness and Bernstein give

\[
\|\nabla\mathsf S_{\le\kappa}b_n(\tau)\|_{L^{3,\infty}}
\le
C\kappa M.
\tag{17}
\]

The finite-volume Lorentz embedding on \(\mathcal C_k\) gives, at

\[
\kappa_k=R_k^{-1},
\tag{18}
\]

\[
\|\nabla\mathsf S_{\le\kappa_k}b_n(\tau)\|_{L^2(\mathcal C_k)}
\le
CM\kappa_kR_k^{1/2}
=
CMR_k^{-1/2}.
\tag{19}
\]

After time integration and multiplication by (14),

\[
\begin{aligned}
\sum_{k\ge0}
\mathcal A_{n,k}(T)
\left(
\int_0^T
\|\nabla\mathsf S_{\le\kappa_k}b_n\|_{L^2(\mathcal C_k)}^2
\,d\tau
\right)^{1/2}
&\le
CA_*M\sqrt T\sum_{k\ge0}R_k^{-1}\\
&<\infty.
\end{aligned}
\tag{20}
\]

Thus no coefficient mode whose wavelength is at least its spatial
shell radius can obstruct the annular budget.

## 3. Exact high-frequency ancestry

For \(n\) large enough that \(H_n>T\), put

\[
L_n:=\frac{H_n-T}{2}.
\tag{21}
\]

Then \(\tau+L_n\le H_n\) for every \(0\le\tau\le T\).
Applying the ordinary forward mild formula between physical times
\(-(\tau+L_n)\) and \(-\tau\) gives the exact reversed-coordinate
identity

\[
\boxed{
\begin{aligned}
b_n(\tau)
={}&
e^{\nu L_n\Delta}b_n(\tau+L_n)\\
&-
\int_0^{L_n}
e^{\nu s\Delta}
\mathbb P\operatorname{div}
\bigl(
b_n(\tau+s)\otimes b_n(\tau+s)
\bigr)\,ds.
\end{aligned}
}
\tag{22}
\]

After applying \(\mathsf S_{>\kappa_k}\), the second line is exactly
\(\mathcal R_{n,k}\) from (4).  Denote the first line by

\[
\mathcal I_{n,k}(\tau)
:=
\mathsf S_{>\kappa_k}
e^{\nu L_n\Delta}b_n(\tau+L_n).
\tag{23}
\]

Then

\[
\mathsf S_{>\kappa_k}b_n
=
\mathcal I_{n,k}+\mathcal R_{n,k}.
\tag{24}
\]

This is an identity on the same smooth genealogy, not a model
decomposition.

## 4. The inherited high-frequency shell sum vanishes

Define the genealogy energy ceiling

\[
\mathcal E_n
:=
\sup_{0\le s\le H_n}\|b_n(s)\|_2.
\tag{25}
\]

For \(X>0\), the complementary heat multiplier satisfies, after changing
absolute constants to absorb \(c_0\),

\[
\sup_{|\xi|\ge c_0R^{-1}}
|\xi|e^{-X|\xi|^2}
\le
CX^{-1/2}e^{-cX/R^2}.
\tag{26}
\]

Indeed, after writing \(y=\sqrt X|\xi|\), absorb the polynomial
factor \(y\) into half of the Gaussian.

Equations (23), (25), and (26) give

\[
\left(
\int_0^T
\|\nabla\mathcal I_{n,k}(\tau)\|_2^2\,d\tau
\right)^{1/2}
\le
C\sqrt T\,\mathcal E_n
(\nu L_n)^{-1/2}
\exp\left(-c\frac{\nu L_n}{R_k^2}\right).
\tag{27}
\]

The elementary dyadic heat-tail lemma is

\[
\boxed{
\sum_{k\ge0}
R_k^{-\beta}
\exp\left(-c\frac X{R_k^2}\right)
\le
C_{\beta,c,L}X^{-\beta/2}
\qquad(\beta>0).
}
\tag{28}
\]

To prove it, split at the first \(R_k\ge\sqrt X\).  The outer part is
a geometric series.  Moving inward from \(\sqrt X\), the Gaussian
decays supergeometrically and dominates the increasing
\(R_k^{-\beta}\) factor.

Multiplying (27) by the endpoint tail (14), summing, and applying
(28) with \(\beta=1/2\) gives

\[
\boxed{
\begin{aligned}
\sum_{k\ge0}
\mathcal A_{n,k}(T)
\left(
\int_0^T
\|\nabla\mathcal I_{n,k}\|_2^2\,d\tau
\right)^{1/2}
\le
C A_*\sqrt T\,\mathcal E_n
(\nu L_n)^{-3/4}.
\end{aligned}
}
\tag{29}
\]

More generally, an exterior adjoint tail \(R^{-\beta}\) produces
\(\mathcal E_n(\nu L_n)^{-(1+\beta)/2}\).

## 5. The physical genealogy satisfies heat erasure

For the physical outer profiles at radii \(\rho_n\to0\),

\[
V_n(y,s)
=
\frac{\rho_n}{\nu_{\rm phys}}
v\left(
x_n+\rho_ny,
T^*+\frac{\rho_n^2}{\nu_{\rm phys}}s
\right).
\tag{30}
\]

The original Leray energy inequality gives

\[
\mathcal E_n
\le
\frac{E_{\rm phys}}
{\nu_{\rm phys}\sqrt{\rho_n}}.
\tag{31}
\]

The genealogy construction chooses

\[
H_n
=
\frac{\nu_{\rm phys}T^*}{2\rho_n^2}
\tag{32}
\]

up to the harmless vanishing terminal translation.  Hence, for fixed
\(T\),

\[
L_n\asymp\rho_n^{-2}
\tag{33}
\]

and

\[
\boxed{
\mathcal E_n(\nu L_n)^{-3/4}
\le
C\rho_n
\longrightarrow0.
}
\tag{34}
\]

This is where the long physical prehistory enters.  Fixed-member energy
diverges, but only like \(H_n^{1/4}\); the annular heat-erasure threshold
allows growth strictly below \(H_n^{3/4}\).

## 6. Only nonlinear regeneration remains

Insert the low/high split (16), the exact ancestry (24), and estimates
(20), (29), and (34) into (13).  The coefficient cutoff term remains
(15), and the compact inner coefficient remains in \(C_{\rm in}\).
This proves (6).

The implication (7) follows after dividing by \(\sqrt{\nu T}\) and
taking the genealogy lower limit.

Conversely, if along a subsequence

\[
\int_0^T
\|\nabla\pi^*_{n,\psi}\|_1\,d\tau
\longrightarrow\infty,
\tag{35}
\]

then (6) forces

\[
\mathfrak R_n(T)\longrightarrow\infty
\tag{36}
\]

along that subsequence.  This is an implication from an upper bound,
not a claim that the actual cost diverges.

The endpoint static cloud from the annular audit has unit internal
frequency at spatial radius \(R\), hence lies above the reciprocal
cutoff for large \(R\).  Equations (29) and (34) show that such a cloud
cannot arrive as a passive heat evolution from the remote genealogy
edge.  If realised on the physical sequence, its relevant
high-frequency portion must occur inside the nonlinear Duhamel field
(4).

## 7. Exact route consequence

This theorem closes:

1. all reciprocal-or-lower coefficient frequencies as a source of
   nonsummable annular pressure;
2. the remote linearly inherited high-frequency coefficient on the
   physical genealogy;
3. the apparent conflict between divergent scaled energy and remote
   heat erasure;
4. a global-energy-free and inherited-energy-free sufficient criterion
   for finite adjoint-pressure cost; and
5. passive persistence of the endpoint static annular cloud.

It does not prove:

1. finiteness of the nonlinear regeneration action (5);
2. a positive exterior-adjoint tail power;
3. that regeneration occurs on disjoint or non-Zeno time intervals;
4. a sign, flux, or event-index charge for \(\mathcal R_{n,k}\);
5. finite adjoint-pressure cost;
6. exclusion of the coherent ancient profile;
7. regularity, breakdown, or any Clay alternative A--D.

The next target is no longer an arbitrary shell tail:

> Prove a finite secondary index for the high-frequency nonlinear
> Duhamel regeneration action (5), or show that infinitely many
> non-summable regeneration shells force fresh signed flux/decrement
> events on the same physical trajectory.

The reciprocal-frequency, heat-erasure, physical-scaling, and horizon
ledgers are checked in
`lab/navier_lab/adjoint_pressure_nonlinear_regeneration.py` and
`lab/tests/test_adjoint_pressure_nonlinear_regeneration.py`.
