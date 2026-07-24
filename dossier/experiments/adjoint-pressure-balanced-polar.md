# Balanced first-hitting layers compactify the Kato polar in spacetime

- **Experiment:** EXP-ADJOINT-PRESSURE-BALANCED-POLAR-001
- **Route:** ROUTE-R3B
- **Status:** conditional analytic reduction;
  [adversarially recomputed valid after scope repair](../review-ledger.md)
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** adversarially recomputed
  [signed aggregate](adjoint-pressure-signed-aggregate.md),
  [temporal disintegration](adjoint-pressure-temporal-disintegration.md),
  and [first-hitting polar vacuum](adjoint-pressure-polar-vacuum.md)

The first-hitting theorem leaves a balanced finite-band branch

\[
0<\theta_-
\le
\theta_h:=\frac{\varepsilon_h}{h^9}
\le\theta_+<\infty.
\tag{1}
\]

It previously supplied only pressure-probability tightness of a
linear-growth modular for \(a_h/\varepsilon_h\). The actual Oseen equation
gives more.

The theorem concerns the **norm-gated finite-band path**: before the
charged finite-band component is selected, the direct and exterior
children must have been rejected by their spacetime \(L^1\)-norm gates.
Mere coexistence of a charged finite-band component is insufficient,
because an arbitrarily large component with zero polar pairing could
otherwise remain in the full pressure. On the norm-gated path, every
pressure component discarded earlier in the branch tree has bounded
spacetime \(L^1\) norm, while the complete source-localised inner
feedback also has bounded \(L^1\) norm. The whole adjoint pressure packet
is therefore uniformly bounded. First hitting then bounds the total
regularised Kato dissipation.

After descendant and amplitude normalisation, both of those budgets, and
the linear-growth modular budget, cost exactly \(h^{21/2}\) per cell.
This is the reciprocal of the already forced \(h^{-21/2}\) source-cell
count. The moving pressure-capture law therefore turns the global bounds
into pressure-probability local bounds, with no residual power of \(h\).

The regularised polar

\[
\mathsf Z
=
\frac{A}{\sqrt{1+|A|^2}}
\]

then has locally bounded \(L^2_sH^1_y\) norm. Its transformed Oseen
equation bounds \(\partial_s\mathsf Z\) in
\(L^1_sW^{-1,6/5}_y\). Aubin--Lions gives tightness of the pushed-forward
profile laws on the strong full-time, local-in-space \(L^2\) topology
\(\mathcal X\) defined in (48).

This is genuine temporal compactness for the balanced polar, but it does
not yet identify the amplitude-normalised Oseen state. Linear-growth
entropy permits amplitude concentration, and a pressure measure can
sample a moving thin time layer which disappears in strong spacetime
\(L^2\). The exact remaining balanced-branch obstruction is therefore a
pressure-trace/amplitude-concentration defect, not arbitrary bulk time
oscillation.

## 1. The selected finite-band branch bounds the full pressure

Retain the first-hitting finite-band notation

\[
\partial_\tau a_h
-\nu\Delta a_h
-b_h\cdot\nabla a_h
+\nabla\pi_h^*=0,
\qquad
\nabla\cdot a_h=\nabla\cdot b_h=0,
\tag{2}
\]

\[
\rho_{\varepsilon}(z)
:=
\sqrt{|z|^2+\varepsilon^2}-\varepsilon,
\qquad
\zeta_h
:=
\frac{a_h}{\sqrt{|a_h|^2+\varepsilon_h^2}},
\tag{3}
\]

\[
L_{\varepsilon_h}(a_h(h))
-L_{\varepsilon_h}(\varphi)
=\gamma_*,
\tag{4}
\]

\[
K=\kappa h^{-1/2},
\qquad
\ell=K^{-1},
\qquad
H_h=P_{>K}\mathcal T(r^{\rm lo},b^{\rm lo}),
\tag{5}
\]

\[
0<p_{\rm pol}
\le
Z_h:=\int_0^h\int_{\mathbb R^3}|H_h|
\le C_{\rm pol}.
\tag{6}
\]

The complete pressure is linear in the adjoint entry. With the reviewed
decomposition \(a_h=\varphi+q_h+r_h\),

\[
\nabla\pi_h^*
=
\nabla\pi^*_{[\varphi,b_h]}
+\nabla\pi^*_{[q_h,b_h]}
+\mathcal T(r_h,b_h^{\rm in})
+\mathcal T(r_h,b_h^{\rm out}).
\tag{7}
\]

Following the branch tree to the finite-band child records four upper
bounds, not merely one positive lower bound.

1. The frozen-detector pressure is \(O(\sqrt h)\).
2. The direct-response payer is absent, so its \(L^1_{t,x}\) norm is below
   the fixed direct-branch threshold.
3. The stretched-exponential exterior payer is absent, so its
   \(L^1_{t,x}\) norm is below the fixed exterior-branch threshold.
4. The reviewed arbitrary-terminal-time estimate and inner local-energy
   saturation give
   \[
   \int_0^h\|r_h(\tau)\|_2^2\,d\tau\le Ch^3,
   \qquad
   D_{\rm in}(h)
   :=
   \int_0^h\|\nabla b_h^{\rm in}\|_2^2\,d\tau
   \le Ch^{-3}.
   \tag{8}
   \]
   Hence the Hardy div--curl estimate gives
   \[
   \begin{aligned}
   \|\mathcal T(r_h,b_h^{\rm in})\|_{L^1_{t,x}}
   &\le
   C
   \left(
   \int_0^h\|r_h\|_2^2
   \right)^{1/2}
   D_{\rm in}(h)^{1/2}\\
   &\le C.
   \end{aligned}
   \tag{9}
   \]

Thus the complete norm-gated first-hitting finite-band path has the
additional uniform estimate

\[
\boxed{
P_h^{\rm all}
:=
\int_0^h
\|\nabla\pi_h^*(\tau)\|_1\,d\tau
\le C_{\rm all}.
}
\tag{10}
\]

This conclusion is branch-specific. It is not asserted on the direct or
stretched-exponential children.

The exact Kato identity at first hitting is

\[
-\int_0^h\!\!\int
\zeta_h\cdot\nabla\pi_h^*
=
\gamma_*
+\nu\int_0^h\!\!\int
\mathcal K_{\varepsilon_h}(a_h).
\tag{11}
\]

Since the absolute value of the left side is at most (10),

\[
\boxed{
\int_0^h\!\!\int
\mathcal K_{\varepsilon_h}(a_h)
\le C_{\rm K}.
}
\tag{12}
\]

This is the new global input. The earlier \(h^9\) theorem used only the
regularised mass part of first hitting.

## 2. Three balanced rooted actions have the same cell scale

For a spatial root \(x\), define

\[
A_{h,x}(s,y)
:=
\frac{a_h(hs,x+\ell y)}{\varepsilon_h},
\qquad
\mathsf Z_{h,x}(s,y)
:=
\frac{A_{h,x}(s,y)}
{\sqrt{1+|A_{h,x}(s,y)|^2}},
\tag{13}
\]

\[
B_{h,x}(s,y)
:=
\frac h\ell b_h(hs,x+\ell y),
\qquad
\Pi_{h,x}(s,y)
:=
\frac{h}{\varepsilon_h\ell}
\pi_h^*(hs,x+\ell y).
\tag{14}
\]

Let

\[
\Phi(A):=\sqrt{1+|A|^2}-1
\tag{15}
\]

and

\[
\mathcal K_\Phi(A)
:=
\sum_{j=1}^3
\partial_jA\cdot D^2\Phi(A)\partial_jA.
\tag{16}
\]

For fixed \(D>0\), introduce the complete rooted spacetime actions

\[
\mathfrak O_{h,x}^D
:=
\int_0^1\int_{B_D}\Phi(A_{h,x}),
\tag{17}
\]

\[
\mathfrak K_{h,x}^D
:=
\int_0^1\int_{B_D}\mathcal K_\Phi(A_{h,x}),
\tag{18}
\]

\[
\mathfrak P_{h,x}^D
:=
\int_0^1\int_{B_D}|\nabla_y\Pi_{h,x}|.
\tag{19}
\]

Their exact physical conversions are

\[
\mathfrak O_{h,x}^D
=
\frac1{\varepsilon_hh\ell^3}
\int_0^h\int_{B_{D\ell}(x)}
\rho_{\varepsilon_h}(a_h),
\tag{20}
\]

\[
\mathfrak K_{h,x}^D
=
\frac1{\varepsilon_hh\ell}
\int_0^h\int_{B_{D\ell}(x)}
\mathcal K_{\varepsilon_h}(a_h),
\tag{21}
\]

\[
\mathfrak P_{h,x}^D
=
\frac1{\varepsilon_h\ell^3}
\int_0^h\int_{B_{D\ell}(x)}
|\nabla\pi_h^*|.
\tag{22}
\]

The first-hitting mass bound, (10), and (12) give

\[
\int_0^h\int\rho_{\varepsilon_h}(a_h)\le C h,
\qquad
\int_0^h\int|\nabla\pi_h^*|\le C,
\qquad
\int_0^h\int\mathcal K_{\varepsilon_h}(a_h)\le C.
\tag{23}
\]

Use the physical grid of \(\ell\)-cubes. Bounded overlap of fixed
enlargements and (20)--(23) show that the roots where one of
\(\mathfrak O^D,\mathfrak K^D,\mathfrak P^D\) exceeds \(L\) meet at most

\[
N_{\mathfrak O}(L)
\le
\frac{C_D}{L\varepsilon_h\ell^3},
\tag{24}
\]

\[
N_{\mathfrak K}(L)
\le
\frac{C_D}{L\varepsilon_hh\ell},
\tag{25}
\]

\[
N_{\mathfrak P}(L)
\le
\frac{C_D}{L\varepsilon_h\ell^3}
\tag{26}
\]

grid cubes. In the balanced branch,

\[
\varepsilon_hh\ell
\asymp
\varepsilon_h\ell^3
\asymp
h^{21/2},
\tag{27}
\]

where the two quantities differ only by a fixed power of \(\kappa\).
Consequently each count in (24)--(26) is at most

\[
CL^{-1}h^{-21/2}.
\tag{28}
\]

This is exactly the full source-cell power.

## 3. Moving pressure capture turns the counts into tightness

Let the finite-band pressure-root law be

\[
\int F\,d\Gamma_h^{\rm fb}
:=
\frac1{Z_h}
\int_0^h\int_{\mathbb R^3}
F(\tau,x)|H_h(\tau,x)|\,dx\,d\tau.
\tag{29}
\]

The reviewed capture estimate for a union of \(N\) descendant cubes is

\[
\int_0^h\int_{U_N}|H_h|
\le
C_{\rm cap}h^{7/4}N^{1/6}.
\tag{30}
\]

For a root inside a bad cube, enlarge the cube by the fixed stencil
needed to contain \(B_{D\ell}(x)\). Apply (30) to the bad union and use
\(Z_h\ge p_{\rm pol}\). Equations (24)--(28) give, for
\(\mathfrak A\in\{\mathfrak O,\mathfrak K,\mathfrak P\}\),

\[
\boxed{
\Gamma_h^{\rm fb}
\left\{
\mathfrak A_{h,x}^D>L
\right\}
\le
C_D L^{-1/6}.
}
\tag{31}
\]

The cancellation is exact:

\[
h^{7/4}
\left(h^{-21/2}\right)^{1/6}
=1.
\tag{32}
\]

Thus the complete spacetime linear-growth modular, Kato, and
full-pressure actions are tight under the same pressure-root law. This is
stronger than the single-time modular estimate in the preceding theorem.
It is not Orlicz-space compactness in the superlinear de la Vallée
Poussin sense.

## 4. Exact polar differential algebra

The amplitude-normalised equation is

\[
\partial_sA_{h,x}
-\nu\kappa^2\Delta_yA_{h,x}
-B_{h,x}\cdot\nabla_yA_{h,x}
+\nabla_y\Pi_{h,x}
=0,
\tag{33}
\]

with the critical drift bound

\[
\|B_{h,x}(s)\|_{L^{3,\infty}_y}
\le\kappa^2M.
\tag{34}
\]

Write

\[
\mathsf H(A):=D^2\Phi(A)
=
\frac I{\sqrt{1+|A|^2}}
-
\frac{A\otimes A}{(1+|A|^2)^{3/2}}.
\tag{35}
\]

Since \(\mathsf Z=\nabla\Phi(A)\),

\[
\partial_j\mathsf Z=\mathsf H(A)\partial_jA.
\tag{36}
\]

All eigenvalues of \(\mathsf H\) lie in \([0,1]\), so

\[
\boxed{
|\nabla\mathsf Z|^2
\le
\mathcal K_\Phi(A).
}
\tag{37}
\]

The third derivative is also paid by the same Kato density. For
\(S=\sqrt{1+|A|^2}\) and a vector \(v\),

\[
D^3\Phi(A)[v,v]
=
-
\frac{2(A\cdot v)v+|v|^2A}{S^3}
+
\frac{3(A\cdot v)^2A}{S^5}.
\tag{38}
\]

Decomposing \(v\) into its radial and tangential parts relative to \(A\)
and applying \(2ab\le a^2+b^2\) gives

\[
\boxed{
\left|D^3\Phi(A)[v,v]\right|
\le
4\,v\cdot D^2\Phi(A)v.
}
\tag{39}
\]

Apply \(D^2\Phi(A)\) to (33) and use

\[
\Delta\mathsf Z
=
D^2\Phi(A)\Delta A
+
\sum_jD^3\Phi(A)[\partial_jA,\partial_jA].
\tag{40}
\]

The polar therefore satisfies the exact smooth equation

\[
\boxed{
\begin{aligned}
\partial_s\mathsf Z
&-\nu\kappa^2\Delta\mathsf Z
-B\cdot\nabla\mathsf Z
+D^2\Phi(A)\nabla\Pi\\
&+\nu\kappa^2
\sum_jD^3\Phi(A)[\partial_jA,\partial_jA]
=0.
\end{aligned}
}
\tag{41}
\]

On \(B_D\), Lorentz Hölder, (34), and (37)--(39) imply

\[
\boxed{
\begin{aligned}
\|\partial_s\mathsf Z_{h,x}\|
_{L^1(0,1;W^{-1,6/5}(B_D))}
\le C_D\big[
&(1+\kappa^2M)
(\mathfrak K_{h,x}^{D+1})^{1/2}\\
&+\mathfrak K_{h,x}^{D+1}
+\mathfrak P_{h,x}^{D+1}
\big].
\end{aligned}
}
\tag{42}
\]

Here \(L^1(B_{D+1})\hookrightarrow W^{-1,6/5}(B_D)\) follows from
\(W^{1,6}_0(B_D)\hookrightarrow L^\infty(B_D)\). The drift term uses

\[
L^{3,\infty}\cdot L^2
\longrightarrow L^{6/5,2}
\hookrightarrow W^{-1,6/5}(B_D).
\tag{43}
\]

No derivative of the critical drift is used.

## 5. Pressure-probability Aubin--Lions compactness

Equations (31), (37), and (42) imply that, outside a set of
\(\Gamma_h^{\rm fb}\)-mass at most \(C_DL^{-1/6}\),

\[
\|\mathsf Z_{h,x}\|_{L^2(0,1;H^1(B_D))}
\le C_{D,L},
\tag{44}
\]

\[
\|\partial_s\mathsf Z_{h,x}\|
_{L^1(0,1;W^{-1,6/5}(B_D))}
\le C_{D,L}.
\tag{45}
\]

The compact triple

\[
H^1(B_D)
\Subset
L^2(B_D)
\hookrightarrow
W^{-1,6/5}(B_D)
\tag{46}
\]

and the Aubin--Lions--Simon theorem make the set in (44)--(45)
precompact in \(L^2((0,1)\times B_D)\). Choose thresholds
\(L_D\uparrow\infty\) on a countable exhaustion by buffered balls
\(B_{D+1}\), so that the probability losses in (31) are summable. It
follows that the pushforwards of \(\Gamma_h^{\rm fb}\) by

\[
(\tau,x)
\longmapsto
\mathsf Z_{h,x}
\tag{47}
\]

are tight in the strong projective topology

\[
\boxed{
\mathcal X
:=
L^2\!\left(
(0,1);L^2_{\rm loc}(\mathbb R^3)
\right).
}
\tag{48}
\]

Here the defining seminorms are the **full-time** norms

\[
\|z\|_{L^2((0,1)\times B_D)},
\qquad D=1,2,\ldots.
\tag{48a}
\]

Thus ``local'' refers only to space; this topology does not discard
either time endpoint. The diagonal construction preceding (48) gives
tightness in exactly this topology because (44)--(45) hold on the whole
interval \((0,1)\) for every fixed spatial ball.

This is tightness, hence subsequential weak convergence of the
pushforward probability laws on a strong function-space topology. It is
not strong convergence in probability on the original varying
probability spaces, and no canonical coupling of those spaces is
asserted.

Equivalently, for every \(D<\infty\) and \(\eta>0\),

\[
\boxed{
\lim_{\delta\downarrow0}
\limsup_{h\downarrow0}
\Gamma_h^{\rm fb}
\left\{
\left\|
\mathsf Z_{h,x}(\,\cdot+\delta,\cdot)
-\mathsf Z_{h,x}
\right\|_
{L^2((0,1-\delta)\times B_D)}
>\eta
\right\}
=0.
}
\tag{49}
\]

Thus the balanced effective polar cannot retain the arbitrary bulk time
flips permitted by the earlier non-PDE kinematic carrier.

The modular action in (31) also implies that every limiting polar profile
\(\mathsf Z\) satisfies \(|\mathsf Z|<1\) almost everywhere and defines
an algebraic regular amplitude

\[
A^{\rm reg}
:=
\frac{\mathsf Z}{\sqrt{1-|\mathsf Z|^2}}
\in L^1_{\rm loc}.
\tag{50}
\]

This definition does not identify a limiting amplitude and does not prove
\(A_{h,x}\to A^{\rm reg}\) in \(L^1\), weakly, or distributionally. The
integrand \(\Phi\) has only linear growth, so a vector-valued
concentration measure may be lost by the strong polar limit. For example,
after smoothing the boundary if desired,

\[
A_n(y):=n^3e_1\mathbf1_{B_{1/n}}(y)
\tag{50a}
\]

has bounded \(\int\Phi(A_n)\), while its \(L^1\) mass stays order one and
concentrates at the origin. Thus no graph relation
\(\mathsf Z=\nabla\Phi(A)\) for a limiting amplitude is inferred.

## 6. Strong profile compactness does not identify a pressure trace

There is a second, independent closure issue. Strong spacetime
compactness does not make evaluation at a pressure-selected time
continuous.

An exact abstract model makes this visible. Work on the time circle
\(\mathbb T\). Choose a nonnegative smooth bump \(\chi\), supported in a
proper subinterval, and a unit vector \(e\). For \(r\in\mathbb T\), put

\[
z_n^r(s):=\chi(n(s-r))e,
\tag{51}
\]

with periodic interpretation, and

\[
d\mu_n^r(s)
:=
\frac{n\chi(n(s-r))}{\int_{\mathbb R}\chi}\,ds.
\tag{52}
\]

Then

\[
\|z_n^r\|_{L^2(\mathbb T)}^2
=
\frac1n\int_{\mathbb R}\chi^2
\longrightarrow0,
\qquad
\operatorname{Var}(z_n^r)
=
\int_{\mathbb R}|\chi'|.
\tag{53}
\]

Averaging the sampling measures over the moving centre gives exactly
Lebesgue time:

\[
\int_{\mathbb T}\mu_n^r\,dr=ds.
\tag{54}
\]

Nevertheless,

\[
\boxed{
\int_{\mathbb T}z_n^r\,d\mu_n^r
=
\frac{\int\chi^2}{\int\chi}\,e
\ne0.
}
\tag{55}
\]

Thus the profiles converge strongly to zero, have uniformly bounded
time variation, and have an atomless averaged time law, while their
self-weighted traces stay nonzero. This is a functional-analytic
countermodel, not an Oseen or Navier--Stokes construction. It proves that
the existing compactness statements alone cannot identify the limiting
pressure-weighted polar mark with the value of the strong spacetime
profile.

## 7. Exact consequence and remaining gate

Conditional on the first-hitting branch rerun reaching the norm-gated
charged finite-band child, with the direct and exterior norm gates
rejected, and on the balanced lower bound in (1), the following chain is
now closed:

1. the complete adjoint pressure packet has uniformly bounded spacetime
   \(L^1\) mass;
2. first hitting gives uniformly bounded total Kato dissipation;
3. rooted linear-growth modular, Kato, and pressure actions have a common
   \(L^{-1/6}\) pressure-probability tail;
4. its profile laws are tight on strong full-time, local-in-space
   \(L^2\);
5. its temporal translations vanish in pressure probability.

This closes arbitrary balanced-polar bulk time oscillation. It does not
prove:

- strong or weak compactness of \(A_h=a_h/\varepsilon_h\) without an
  amplitude concentration measure;
- identification of the positive pressure-weighted mark with a time
  trace of the compact polar profile;
- closure of the limiting Oseen products;
- any finite charge for \(\varepsilon_h/h^9\to0\);
- an event telescope, finite critical budget, regularity theorem,
  breakdown theorem, or Clay alternative A--D.

The later [finite-amplitude theorem](adjoint-pressure-amplitude-window.md)
localises fixed charge to a compact window, and the subsequent
[bulk-participation theorem](adjoint-pressure-trace-participation.md)
excludes the source-volume-vanishing realisation of (51)--(55) while
retaining nonzero full-time window profiles. The abstract example still
shows that compactness alone does not identify the conditional
pressure-root time.

The balanced branch is now reduced to the sharper question:

> Can the Oseen pressure structure identify the signed pressure-root
> time with the nonzero compact-window profile law and close unwindowed
> amplitude concentration in (50), so that the positive Kato-polar mark
> belongs to an honest amplitude-normalised Oseen limit?

The strict sub-\(h^9\) amplitude cascade remains the other finite-band
branch.

## Reproduce

```bash
make adjoint-pressure-balanced-polar
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_balanced_polar -v
make check
git diff --check
```
