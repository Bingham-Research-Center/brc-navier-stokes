# Spatial high-pass identity exposes two aggregate payers

- **Experiment:** EXP-ADJOINT-PRESSURE-SPATIAL-HIGHPASS-PAYER-001
- **Route:** ROUTE-R3B
- **Status:** conditional same-genealogy analytic reduction plus
  endpoint-weighted scalar extraction no-go
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** [one-heat-time aggregate](adjoint-pressure-parabolic-regeneration.md),
  [annular pressure cost](adjoint-pressure-annular-cost.md), and the
  [frequency-energy-flux audit](frequency-energy-flux.md)
- **External review:** pending
- **Adversarial recomputation:** analytic bridge accepted; the initial
  physical/normalised ledger mismatch was repaired and the repair accepted

Retain \(R_k=L^kR_0\), \(L\ge16\), the smooth finite-energy genealogy,
its uniform weak-\(L^3\) bound \(M\), and the endpoint exterior-adjoint
tail from the one-heat-time theorem.  That theorem left the aggregate
high-frequency nonlinear Duhamel action

\[
\mathfrak Q_n(T;r_\bullet)
=
\sum_{\rho_nR_k\le r_\bullet}
\mathcal A_{n,k}(T)
\left(
\int_0^T
\|\nabla\mathcal Q_{n,k}\|_{L^2(\mathcal C_k)}^2\,d\tau
\right)^{1/2}.
\tag{1}
\]

An exact spatially local high-pass energy identity now gives a
two-payer upper reduction.  For every fixed admissible \(r_\bullet\) and
all sufficiently large \(n\),

\[
\boxed{
\mathfrak Q_n(T;r_\bullet)
\le
C
+
C\mathfrak E_n(T;r_\bullet)
+
C\mathfrak F_n(T;r_\bullet),
}
\tag{2}
\]

with \(C\) independent of \(n\), where:

- \(\mathfrak E_n\) is the adjoint-weighted square-root local
  high-pass energy at the entrance \(t=-T\) of the measured window;
- \(\mathfrak F_n\) is the adjoint-weighted square-root positive
  nonlinear work into the same spatially cut-off high-pass fields.

The spatial diffusion-boundary action is summable and is absorbed into
\(C\).  Thus, along any subsequence on which the pressure histories
diverge,

\[
\boxed{
\mathfrak E_{n_j}(T;r_\bullet)+
\mathfrak F_{n_j}(T;r_\bullet)
\longrightarrow\infty
}
\tag{3}
\]

for every fixed admissible \(r_\bullet\).  After a further subsequence,
at least one of the two aggregates diverges.

This extracts spatially cut-off positive nonlinear work as a genuine
branch.  It still does not localise the projected source or extract an
individual shell with a fixed charge.  An endpoint-weighted scalar
array shows that the local identity and physical quadratic budgets
alone cannot perform that extraction.  On \(N\) geometric physical
shells one may set

\[
d_{N,k}=\frac{r_{N,k}}{N}.
\tag{4}
\]

Then

\[
\sum_{k=1}^N
\sqrt{\frac{d_{N,k}}{r_{N,k}}}
=
\sqrt N\longrightarrow\infty,
\qquad
\max_k
\sqrt{\frac{d_{N,k}}{r_{N,k}}}
=
N^{-1/2}\longrightarrow0,
\tag{5}
\]

while

\[
\sum_{k=1}^Nd_{N,k}
\le
\frac{r_{\rm out,N}}{N(1-L^{-1})}.
\tag{6}
\]

After the exact physical-to-normalised pullback, both an
entrance-energy array and a positive-work array satisfy the local
identity.  If \(r_{\rm out,N}\to0\), their total physical quadratic
charge and total natural clock vanish even though (5) diverges.

The array is not a Navier--Stokes, Duhamel, or adjoint construction and
does not prove sharpness of (2).  It proves only that the
endpoint-weighted scalar identity, finite physical quadratic budgets,
scale-zero support, and even proportional decrements do not by
themselves convert the square-root aggregate into an individually
fresh event.  A closing theorem must add non-diffuse NSE structure.

## 1. Spatially local smooth high-pass identity

Return to the forward genealogy member \(u_n(t)\) on
\([-H_n,0]\), and fix \([-T,0]\).  Use the same smooth
Littlewood--Paley high-pass as in the one-heat-time theorem:

\[
w_{n,k}(t)
:=
\mathsf S_{>R_k^{-1}}u_n(t).
\tag{7}
\]

Choose \(\chi_k\in C_c^\infty(\mathbb R^3)\) such that

\[
0\le\chi_k\le1,
\qquad
\chi_k=1\quad\hbox{on }\mathcal C_k,
\tag{8}
\]

\[
\operatorname{supp}\chi_k
\subset
B_{16R_{k+1}}\setminus B_{2R_k},
\qquad
\|\nabla^m\chi_k\|_\infty
\le C_LR_k^{-m}
\quad(m=1,2).
\tag{9}
\]

These enlarged supports have overlap bounded only by \(L\).

Define

\[
E_{n,k}(t)
:=
\int_{\mathbb R^3}
\chi_k^2|w_{n,k}(t)|^2\,dx,
\tag{10}
\]

\[
D_{n,k}
:=
\int_{-T}^0
\int_{\mathbb R^3}
\chi_k^2|\nabla w_{n,k}|^2\,dx\,dt,
\tag{11}
\]

\[
B_{n,k}
:=
\int_{-T}^0
\int_{\mathbb R^3}
\Delta(\chi_k^2)|w_{n,k}|^2\,dx\,dt,
\tag{12}
\]

and the spatially cut-off high-pass nonlinear work

\[
\Phi_{n,k}
:=
-
\int_{-T}^0
\int_{\mathbb R^3}
\chi_k^2w_{n,k}\cdot
\mathsf S_{>R_k^{-1}}
\mathbb P\operatorname{div}(u_n\otimes u_n)
\,dx\,dt.
\tag{13}
\]

The filtered equation is

\[
\partial_tw_{n,k}-\nu\Delta w_{n,k}
=
-
\mathsf S_{>R_k^{-1}}
\mathbb P\operatorname{div}(u_n\otimes u_n).
\tag{14}
\]

Pairing (14) with \(\chi_k^2w_{n,k}\), integrating by parts in
space and time, and using

\[
-
\int\Delta w\cdot\chi^2w
=
\int\chi^2|\nabla w|^2
-
\frac12\int\Delta(\chi^2)|w|^2
\tag{15}
\]

gives the exact identity

\[
\boxed{
\Phi_{n,k}
=
\frac12
\left(
E_{n,k}(0)-E_{n,k}(-T)
\right)
+
\nu D_{n,k}
-
\frac{\nu}{2}B_{n,k}.
}
\tag{16}
\]

No pressure gauge occurs because the equation was Leray projected
before spatial localisation.  The operator in (13) remains nonlocal;
(16) does not localise the nonlinear source to
\(\operatorname{supp}\chi_k\).

Writing \(\Phi_{n,k}^+=\max\{\Phi_{n,k},0\}\), using
\(E_{n,k}(0)\ge0\), and rearranging (16) gives

\[
\boxed{
D_{n,k}
\le
\frac{\Phi_{n,k}^+}{\nu}
+
\frac{E_{n,k}(-T)}{2\nu}
+
\frac{|B_{n,k}|}{2}.
}
\tag{17}
\]

This is the local positive-payer inequality.

## 2. The spatial boundary action is summable

The smooth high-pass multiplier is bounded on
\(L^{3,\infty}\), so

\[
\sup_{-T\le t\le0}
\|w_{n,k}(t)\|_{L^{3,\infty}}
\le
CM.
\tag{18}
\]

The support in (9) has volume at most \(C_LR_k^3\).
Finite-volume Lorentz embedding therefore gives

\[
\|w_{n,k}(t)\|_{L^2(\operatorname{supp}\chi_k)}^2
\le
C_LM^2R_k.
\tag{19}
\]

Equations (9), (12), and (19) imply

\[
|B_{n,k}|
\le
C_LM^2\frac{T}{R_k}.
\tag{20}
\]

Under the endpoint adjoint tail

\[
\mathcal A_{n,k}(T)\le A_*R_k^{-1/2},
\tag{21}
\]

the complete boundary action satisfies

\[
\boxed{
\begin{aligned}
\sum_{k\ge0}
\mathcal A_{n,k}(T)|B_{n,k}|^{1/2}
&\le
C_LA_*M\sqrt T
\sum_{k\ge0}R_k^{-1}\\
&<\infty,
\end{aligned}
}
\tag{22}
\]

uniformly in \(n\).  Spatial diffusion leakage is therefore not the
missing secondary index.

## 3. Connection to the one-heat-time Duhamel aggregate

For \(\tau=-t\), the preceding theorem gives

\[
\mathsf S_{>R_k^{-1}}b_n(\tau)
=
\mathcal J_{n,k}(\tau)
+
\mathcal Q_{n,k}(\tau),
\tag{23}
\]

where the weighted local gradient action of
\(\mathcal J_{n,k}\) is uniformly summable.

Because \(\chi_k=1\) on \(\mathcal C_k\), Minkowski's inequality in
spacetime gives

\[
\begin{aligned}
&
\left(
\int_0^T
\|\nabla\mathcal Q_{n,k}\|_{L^2(\mathcal C_k)}^2\,d\tau
\right)^{1/2}\\
&\qquad\le
D_{n,k}^{1/2}
+
\left(
\int_0^T
\|\nabla\mathcal J_{n,k}\|_{L^2(\mathcal C_k)}^2\,d\tau
\right)^{1/2}.
\end{aligned}
\tag{24}
\]

Multiplication by \(\mathcal A_{n,k}(T)\), summation over
\(\rho_nR_k\le r_\bullet\), and the inherited estimate give

\[
\boxed{
\mathfrak Q_n(T;r_\bullet)
\le
C
+
\sum_{\rho_nR_k\le r_\bullet}
\mathcal A_{n,k}(T)D_{n,k}^{1/2}.
}
\tag{25}
\]

Define

\[
\mathfrak E_n(T;r_\bullet)
:=
\sum_{\rho_nR_k\le r_\bullet}
\mathcal A_{n,k}(T)
\left(
\frac{E_{n,k}(-T)}{\nu}
\right)^{1/2}
\tag{26}
\]

and

\[
\mathfrak F_n(T;r_\bullet)
:=
\sum_{\rho_nR_k\le r_\bullet}
\mathcal A_{n,k}(T)
\left(
\frac{\Phi_{n,k}^+}{\nu}
\right)^{1/2}.
\tag{27}
\]

Taking square roots in (17), summing, and applying (22) proves (2).

Combining (2) with the one-heat-time upper audit gives the sufficient
criterion

\[
\liminf_{n\to\infty}
\left(
\mathfrak E_n(T;r_\bullet)
+
\mathfrak F_n(T;r_\bullet)
\right)
<\infty
\quad\Longrightarrow\quad
\mathfrak p^\mathcal G_{\psi,T}<\infty.
\tag{28}
\]

Conversely, if \(P_{n_j}(T)\to\infty\), then the preceding theorem
forces \(\mathfrak Q_{n_j}(T;r_\bullet)\to\infty\) for each fixed
admissible \(r_\bullet\).  Equation (2) then proves (3).  For that
fixed cutoff, a further subsequence \(n_{j_\ell}\) has either
\(\mathfrak E_{n_{j_\ell}}\to\infty\) or
\(\mathfrak F_{n_{j_\ell}}\to\infty\).  The choice and subsequence may
depend on \(r_\bullet\).

This is an aggregate alternative.  It does not assign either payer to
one shell, and \(\Phi_{n,k}^+\) is positive spatially cut-off high-pass
nonlinear work rather than an event-index-additive flux.

This does not duplicate the earlier full-domain flux results.  The
[frequency-energy-flux audit](frequency-energy-flux.md) starts from a
detector moment and shows that it need not force nonlinear work.  The
[parabolic flux theorem](adjoint-pressure-parabolic-flux.md) starts from
one event's sharp Fourier-dissipation floor.  Here the input is instead
the newly isolated genealogy-level annular Duhamel aggregate, and the
new conclusion is the two-payer bound (2) with a summable spatial
diffusion boundary.  The scalar extraction no-go in Section 4 is only
the endpoint square-root specialisation of the previously recorded
geometrically decaying flux survivors; it is not a new PDE survivor.

## 4. An endpoint-weighted scalar extraction no-go

The normalised quantities in (16) must not be confused with physical
charges.  Fix \(L\ge16\), \(R_0>0\), an integer \(N\ge1\), and an outer
physical radius \(r_{\rm out,N}>0\).  Put

\[
\rho_N
:=
\frac{r_{\rm out,N}L^{1-N}}{R_0},
\qquad
R_{N,k}:=R_0L^{k-1},
\qquad
r_{N,k}:=\rho_NR_{N,k}
=r_{\rm out,N}L^{k-N}.
\tag{29}
\]

Let the physical coefficient-enstrophy charge and its exact normalised
pullback be

\[
d_{N,k}:=\frac{r_{N,k}}{N},
\qquad
D_{N,k}:=
\frac{d_{N,k}}{\nu_{\rm phys}\rho_N}.
\tag{30}
\]

Choose abstract saturated endpoint weights

\[
\mathcal A_{N,k}:=aR_{N,k}^{-1/2},
\qquad
0<a\le A_*.
\tag{31}
\]

Then the exact zoom cancellation from the preceding theorem gives

\[
\boxed{
\mathcal A_{N,k}D_{N,k}^{1/2}
=
\frac{a}{\sqrt{\nu_{\rm phys}}}
\sqrt{\frac{d_{N,k}}{r_{N,k}}}
=
\frac{a}{\sqrt{\nu_{\rm phys}N}}.
}
\tag{32}
\]

Thus the weighted aggregate grows like \(\sqrt N\), while every
individual weighted action tends to zero.  The physical enstrophy and
natural-clock totals are

\[
\boxed{
\sum_{k=1}^Nd_{N,k}
=
\frac{r_{\rm out,N}}{N}
\frac{1-L^{-N}}{1-L^{-1}},
\qquad
\frac1{\nu_{\rm phys}}\sum_{k=1}^Nr_{N,k}^2
=
\frac{r_{\rm out,N}^2}{\nu_{\rm phys}}
\frac{1-L^{-2N}}{1-L^{-2}}.
}
\tag{33}
\]

Now take the normalised viscosity in (16) to be one.  Two scalar payer
arrays satisfy that identity exactly.

### Positive-work array

For every \(k\), set

\[
\Phi_{N,k}=D_{N,k},
\qquad
E_{N,k}(-T)=E_{N,k}(0)=B_{N,k}=0.
\tag{34}
\]

### Entrance-energy array

Alternatively set

\[
E_{N,k}(-T)=2D_{N,k},
\qquad
E_{N,k}(0)=\Phi_{N,k}=B_{N,k}=0.
\tag{35}
\]

The positive-work contribution to \(\mathfrak F_N\) is exactly (32);
the entrance-energy contribution to \(\mathfrak E_N\) is
\(\sqrt2\) times (32).

Under the genealogy scaling used by the preceding theorem, normalised
energy and work are their physical counterparts divided by
\(\nu_{\rm phys}^2\rho_N\).  Hence

\[
\Phi^{\rm phys}_{N,k}
=\nu_{\rm phys}d_{N,k},
\qquad
E^{\rm phys}_{N,k}(-T)
=2\nu_{\rm phys}d_{N,k}.
\tag{36}
\]

Therefore, if \(r_{\rm out,N}\to0\), (32)--(36) give:

1. the endpoint-weighted normalised aggregate diverges like
   \(\sqrt N\);
2. every individual weighted action tends to zero;
3. total physical enstrophy, entrance energy, and positive work tend
   to zero;
4. the total physical natural clock tends to zero; and
5. any fixed proportional physical quadratic decrement also has
   vanishing sum.

The normalised \(D_{N,k},E_{N,k},\Phi_{N,k}\) totals need not vanish.
These are scalar arrays with abstract saturated weights, not a
Navier--Stokes field, a Duhamel decomposition, or an adjoint
realisation.  They prove only that (16), the endpoint weight (21),
nonnegativity, finite physical quadratic budgets, and natural clocks
cannot by themselves extract a fixed block from (3).  They do not
prove sharpness of (2).

## 5. Exact route consequence

This theorem closes:

1. spatial diffusion-boundary leakage as the missing annular
   secondary index;
2. the exact exhaustive alternative between divergent entrance-energy
   and positive-work payer aggregates, after a cutoff-dependent
   subsequence;
3. the endpoint-weighted scalar local identity as a route from aggregate
   square-root divergence to one fixed charged block; and
4. finite physical quadratic payer, proportional-decrement, and
   natural-clock totals as automatic contradictions to an abstract
   diffuse aggregate.

It does not prove:

1. that either aggregate payer is finite;
2. spatial localisation of the projected nonlinear source;
3. a fixed individual block or event charge;
4. bounded active-block count, bounded event-index overlap, or
   non-Zeno transfer;
5. a signed cross-event telescope;
6. exclusion of the coherent ancient profile;
7. regularity, breakdown, or any Clay alternative A--D.

The next positive theorem must supply at least one of:

1. a non-diffusion estimate upgrading a quadratic payer to linear
   control of the square-root action;
2. an NSE bound on the effective number of active spatial-frequency
   blocks;
3. a source-locality or coherence theorem forcing block aggregation;
4. an ancestry theorem that turns the entrance aggregate into earlier
   selected events; or
5. a signed functional telescoping the positive-work aggregate across
   event index.

The identity signs and the finite geometric ledger were recomputed
directly in the adversarial review.  No executable certificate is
claimed for the Lorentz, multiplier, or PDE steps.
