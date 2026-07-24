# Staggered heat ancestry re-expresses entrance energy as zero-data work

- **Experiment:** EXP-ADJOINT-PRESSURE-STAGGERED-ENTRANCE-ANCESTRY-001
- **Route:** ROUTE-R3B
- **Status:** conditional same-genealogy analytic reduction
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** [spatial high-pass payer](adjoint-pressure-spatial-highpass-payer.md)
  and [one-heat-time regeneration](adjoint-pressure-parabolic-regeneration.md)
- **External review:** pending
- **Adversarial recomputation:** valid as an upper-audit bookkeeping
  reduction; no fresh NSE flux or non-reuse theorem is claimed

The spatial high-pass theorem left two possible divergent payer
aggregates: entrance high-pass energy and positive spatially cut-off
nonlinear work.  Within the upper audit, the entrance term can be
re-expressed as auxiliary zero-data-response work plus a summable
inherited endpoint.

Number the shells inward from the largest shell below a fixed physical
cutoff.  Give the \(j\)-th inward shell \(\gamma(j+1)\) heat times of
lookback.  Its physical radius falls like \(L^{-j}\), so

\[
\sup_{j\ge0}(j+1)L^{-2j}<\infty.
\tag{1}
\]

All staggered lookbacks therefore fit inside one fixed physical
parabolic horizon.  Meanwhile the high-pass heat multiplier gains
exponential decay in \(j\).  The inherited endpoint contribution is
summable.

What remains at the entrance is a zero-data high-pass Duhamel response.
Its generic forced-heat energy identity has an exactly nonnegative
auxiliary work term.  Consequently, for every sufficiently small fixed
admissible physical cutoff,

\[
\boxed{
\mathfrak Q_n(T;r_\bullet)
\le
C
+C\mathfrak F_n(T;r_\bullet)
+C\mathfrak Z_n(T;r_\bullet),
}
\tag{2}
\]

where \(\mathfrak F_n\) is the current-window spatially cut-off
positive work from the preceding theorem and \(\mathfrak Z_n\) is
positive work into zero-data high-pass responses on the staggered
prehistory windows.

Thus divergent pressure histories force

\[
\boxed{
\mathfrak F_{n_j}(T;r_\bullet)
+\mathfrak Z_{n_j}(T;r_\bullet)
\longrightarrow\infty.
}
\tag{3}
\]

Entrance energy has been re-expressed as nonlinear ancestry in this
bookkeeping sense.  This still gives an aggregate, not an individual
block or an event-index sum.  The staggered windows overlap, their
sources remain global, and the result does not exclude diffuse positive
work or prove causal independence.

## 1. Setting and staggered horizons

Retain the smooth forward genealogy \(u_n(t)\) on \([-H_n,0]\), put

\[
b_n(\tau):=u_n(-\tau),
\qquad
0\le\tau\le H_n,
\tag{4}
\]

and assume

\[
\rho_n\longrightarrow0,
\qquad
\sup_n\sup_{0\le\tau\le H_n}
\|b_n(\tau)\|_{L^{3,\infty}}
\le M,
\qquad
\rho_n^2H_n\longrightarrow h_*>0.
\tag{5}
\]

Let \(R_k=L^kR_0\), \(L\ge16\), and retain

\[
\mathcal A_{n,k}(T)\le A_*R_k^{-1/2}.
\tag{6}
\]

Fix \(\gamma\ge1\), \(T>0\), and a physical cutoff satisfying

\[
0<r_\bullet<
\sqrt{\frac{\nu h_*}{2\gamma}}.
\tag{7}
\]

For all large \(n\), define the outer index

\[
K_n:=
\max\{k\ge0:\rho_nR_k\le r_\bullet\}.
\tag{8}
\]

For \(0\le k\le K_n\), put

\[
j_{n,k}:=K_n-k,
\qquad
\ell_{n,k}:=
\frac{\gamma(j_{n,k}+1)R_k^2}{\nu}.
\tag{9}
\]

Writing \(r_{n,k}:=\rho_nR_k\), geometric spacing gives

\[
r_{n,k}=r_{n,K_n}L^{-j_{n,k}}
\le r_\bullet L^{-j_{n,k}}
\tag{10}
\]

and hence

\[
\rho_n^2\ell_{n,k}
\le
\frac{\gamma r_\bullet^2}{\nu}
(j_{n,k}+1)L^{-2j_{n,k}}
\le
\frac{\gamma r_\bullet^2}{\nu}.
\tag{11}
\]

The last inequality uses \(L\ge16\), for which the supremum in (1)
equals one.  Equations (5), (7), and (11) imply

\[
T+\ell_{n,k}\le H_n
\tag{12}
\]

for every \(0\le k\le K_n\) and all sufficiently large \(n\).
Thus every staggered lookback is on the same smooth genealogy.  In
physical variables their lengths are bounded by a fixed multiple of
\(r_\bullet^2\).

## 2. Exponential erasure of the inherited endpoint

Let \(\mathsf S_{>R_k^{-1}}\) be the smooth high-pass used in the
preceding theorems.  The exact mild formula at \(\tau=T\) is

\[
\mathsf S_{>R_k^{-1}}b_n(T)
=
\mathcal I_{n,k}
+\mathcal Z_{n,k},
\tag{13}
\]

where

\[
\mathcal I_{n,k}
:=
\mathsf S_{>R_k^{-1}}
e^{\nu\ell_{n,k}\Delta}
b_n(T+\ell_{n,k})
\tag{14}
\]

and

\[
\mathcal Z_{n,k}
:=
-
\mathsf S_{>R_k^{-1}}
\int_0^{\ell_{n,k}}
e^{\nu s\Delta}
\mathbb P\operatorname{div}
\bigl(
b_n(T+s)\otimes b_n(T+s)
\bigr)\,ds.
\tag{15}
\]

After the change \(\eta=R_k\xi\), the multiplier in (14) is

\[
m_j(\eta)
=
s_>(\eta)e^{-\gamma(j+1)|\eta|^2},
\qquad j=j_{n,k},
\tag{16}
\]

where \(s_>\) vanishes on a fixed neighbourhood of zero.  Standard
Fourier integration by parts therefore gives constants \(c,C>0\),
independent of \(j,k,n\), such that

\[
\|\mathcal F^{-1}m_j\|_1
\le Ce^{-c\gamma(j+1)}.
\tag{17}
\]

Polynomial factors from differentiating the Gaussian are absorbed by
reducing \(c\).  Lorentz convolution and (5) yield

\[
\|\mathcal I_{n,k}\|_{L^{3,\infty}}
\le
CM e^{-c\gamma(j_{n,k}+1)}.
\tag{18}
\]

Use the cutoff \(\chi_k\) from the spatial high-pass theorem.  Its
support has volume at most \(C_LR_k^3\), so finite-volume Lorentz
embedding gives

\[
\|\chi_k\mathcal I_{n,k}\|_2
\le
C_LMR_k^{1/2}
e^{-c\gamma(j_{n,k}+1)}.
\tag{19}
\]

Combining (6) and (19),

\[
\boxed{
\sum_{k=0}^{K_n}
\mathcal A_{n,k}(T)
\frac{\|\chi_k\mathcal I_{n,k}\|_2}{\sqrt\nu}
\le
\frac{C_LA_*M}{\sqrt\nu}
\sum_{j\ge0}e^{-c\gamma(j+1)}
<\infty,
}
\tag{20}
\]

uniformly in \(n\).  The derivative-free inherited endpoint is now
summable; one heat time per shell would not have supplied (20).

## 3. Exact positive work of the zero-data response

Put

\[
t^-_{n,k}:=-T-\ell_{n,k},
\qquad
t^+_{n,k}:=-T.
\tag{21}
\]

On \([t^-_{n,k},t^+_{n,k}]\), define

\[
z_{n,k}(t)
:=
-
\mathsf S_{>R_k^{-1}}
\int_{t^-_{n,k}}^t
e^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}
\bigl(u_n(s)\otimes u_n(s)\bigr)\,ds.
\tag{22}
\]

Then

\[
z_{n,k}(t^-_{n,k})=0,
\qquad
z_{n,k}(t^+_{n,k})=\mathcal Z_{n,k},
\tag{23}
\]

and

\[
\partial_tz_{n,k}-\nu\Delta z_{n,k}
=
-
\mathsf S_{>R_k^{-1}}
\mathbb P\operatorname{div}(u_n\otimes u_n).
\tag{24}
\]

Define the global nonlinear work

\[
\Psi_{n,k}
:=
-
\int_{t^-_{n,k}}^{t^+_{n,k}}
\int_{\mathbb R^3}
z_{n,k}\cdot
\mathsf S_{>R_k^{-1}}
\mathbb P\operatorname{div}(u_n\otimes u_n)
\,dx\,dt.
\tag{25}
\]

The mild identities also give

\[
z_{n,k}(t)
=
\mathsf S_{>R_k^{-1}}u_n(t)
-
e^{\nu(t-t^-_{n,k})\Delta}
\mathsf S_{>R_k^{-1}}u_n(t^-_{n,k}).
\tag{25a}
\]

Since each genealogy member is a smooth finite-energy solution, (25a)
puts \(z_{n,k}\) in
\(L^\infty_tL^2_x\cap L^2_t\dot H^1_x\) on its finite interval.
These norms may depend on \(n,k\); no uniform bound is used.  Pairing
(24) with \(z_{n,k}\) is therefore justified and gives

\[
\boxed{
\Psi_{n,k}
=
\frac12\|\mathcal Z_{n,k}\|_2^2
+\nu
\int_{t^-_{n,k}}^{t^+_{n,k}}
\|\nabla z_{n,k}(t)\|_2^2\,dt
\ge0.
}
\tag{26}
\]

This is an exact global identity.  It introduces no spatial
diffusion-boundary term and gives

\[
\|\mathcal Z_{n,k}\|_2
\le
\sqrt{2\Psi_{n,k}}.
\tag{27}
\]

Define the staggered nonlinear-ancestry aggregate

\[
\mathfrak Z_n(T;r_\bullet)
:=
\sum_{k=0}^{K_n}
\mathcal A_{n,k}(T)
\left(
\frac{\Psi_{n,k}}{\nu}
\right)^{1/2}.
\tag{28}
\]

The work \(\Psi_{n,k}\) is nonnegative because it is measured against
its own zero-data response.  This is the generic forced-heat energy
identity, not a new sign law for Navier--Stokes.  It is not asserted to
equal a sharp Fourier flux of \(u_n\), to be spatially local, or to be
additive in \(k\).

### Same-trajectory dissipation ceiling

Choose the Littlewood--Paley multipliers real and even.  Self-adjointness
of \(\mathsf S_>\) and \(\mathbb P\), incompressibility of \(z_{n,k}\),
and integration by parts give

\[
\Psi_{n,k}
=
\int_{t^-_{n,k}}^{t^+_{n,k}}
\int_{\mathbb R^3}
\nabla\mathsf S_{>R_k^{-1}}z_{n,k}
:
(u_n\otimes u_n)
\,dx\,dt.
\tag{28a}
\]

Lorentz interpolation and Sobolev imply, at each smooth time,

\[
\|u_n\otimes u_n\|_2
=\|u_n\|_4^2
\le
C\|u_n\|_{L^{3,\infty}}\|u_n\|_6
\le
CM\|\nabla u_n\|_2.
\tag{28b}
\]

Let

\[
\Delta_{n,k}
:=
\int_{t^-_{n,k}}^{t^+_{n,k}}
\|\nabla u_n(t)\|_2^2\,dt.
\tag{28c}
\]

The uniform \(H^1\)-multiplier bound, (28a)--(28b), Young's inequality,
and (26) yield

\[
\boxed{
\Psi_{n,k}
\le
\frac{CM^2}{\nu}\Delta_{n,k}.
}
\tag{28d}
\]

Indeed, Young's inequality bounds the right side of (28a) by the sum
of \(\frac{\nu}{2}\int\|\nabla z_{n,k}\|_2^2\) and
\(CM^2\Delta_{n,k}/\nu\); the first term is absorbed using (26).

For the physical genealogy, let \(J_{n,k}\) be the pullback of
\([t^-_{n,k},t^+_{n,k}]\) and put

\[
\delta_{n,k}
:=
\int_{J_{n,k}}\|\nabla v(t)\|_2^2\,dt,
\qquad
r_{n,k}:=\rho_nR_k.
\tag{28e}
\]

The exact scaling from the one-heat-time theorem is

\[
\Delta_{n,k}
=
\frac{\delta_{n,k}}{\nu_{\rm phys}\rho_n}.
\tag{28f}
\]

Consequently, if

\[
\mathfrak D_n^{\rm stag}(T;r_\bullet)
:=
\sum_{k=0}^{K_n}
\left(
\frac{\delta_{n,k}}{r_{n,k}}
\right)^{1/2},
\tag{28g}
\]

then

\[
\boxed{
\mathfrak Z_n(T;r_\bullet)
\le
\frac{CA_*M}{\nu\sqrt{\nu_{\rm phys}}}
\mathfrak D_n^{\rm stag}(T;r_\bullet).
}
\tag{28h}
\]

The physical intervals \(J_{n,k}\) are nested and end at the same
preterminal time.  Indeed, in the inward index \(j\), their lookback
lengths satisfy

\[
\frac{\ell_{j+1}}{\ell_j}
=
\frac{j+2}{j+1}L^{-2}<1.
\tag{28i}
\]

The actual physical genealogy has normalised viscosity \(\nu=1\);
the displayed \(\nu\)-dependence records the general analytic form.
Because the intervals are nested, (28h) is not an additive dissipation
estimate.

## 4. Entrance ancestry and the pressure-cost reduction

At \(t=-T\),

\[
w_{n,k}(-T)
:=
\mathsf S_{>R_k^{-1}}u_n(-T)
=
\mathcal I_{n,k}+\mathcal Z_{n,k}.
\tag{29}
\]

Therefore

\[
E_{n,k}(-T)^{1/2}
=
\|\chi_kw_{n,k}(-T)\|_2
\le
\|\chi_k\mathcal I_{n,k}\|_2
+\|\mathcal Z_{n,k}\|_2.
\tag{30}
\]

Multiplying by \(\mathcal A_{n,k}(T)/\sqrt\nu\), summing, and using
(20) and (27) gives

\[
\boxed{
\mathfrak E_n(T;r_\bullet)
\le
C+C\mathfrak Z_n(T;r_\bullet).
}
\tag{31}
\]

Insert (31) into the spatial high-pass payer bound

\[
\mathfrak Q_n
\le
C+C\mathfrak E_n+C\mathfrak F_n
\tag{32}
\]

to prove (2).  Combining this with the one-heat-time pressure upper
audit yields

\[
\boxed{
P_n(T)
\le
C
+C\mathfrak F_n(T;r_\bullet)
+C\mathfrak Z_n(T;r_\bullet)
+\varepsilon_n(r_\bullet),
}
\tag{33}
\]

where \(\varepsilon_n(r_\bullet)\to0\) for each fixed cutoff.
Equations (28h) and (33) also give

\[
\boxed{
P_n(T)
\le
C
+C\mathfrak F_n(T;r_\bullet)
+C\mathfrak D_n^{\rm stag}(T;r_\bullet)
+\varepsilon_n(r_\bullet).
}
\tag{33a}
\]

Consequently,

\[
\liminf_{n\to\infty}
\left(
\mathfrak F_n(T;r_\bullet)
+\mathfrak Z_n(T;r_\bullet)
\right)
<\infty
\quad\Longrightarrow\quad
\mathfrak p^\mathcal G_{\psi,T}<\infty.
\tag{34}
\]

If \(P_{n_j}(T)\to\infty\), (33) proves (3).  For each fixed
\(r_\bullet\), a further subsequence \(n_{j_\ell}\) has either
\(\mathfrak F_{n_{j_\ell}}\to\infty\) or
\(\mathfrak Z_{n_{j_\ell}}\to\infty\); the choice and subsequence may
depend on the cutoff.

## 5. Sharp scalar power-modulus threshold for (28g)

Finite dissipation and absolute continuity alone do not uniformly bound
(28g) over scalar histories.  Choose \(N\to\infty\) and
\(r_{\rm out,N}\to0\), and put

\[
r_{N,j}:=r_{\rm out,N}L^{-j},
\qquad
s_{N,j}:=c_0(j+1)r_{N,j}^2,
\qquad
d_{N,j}:=\frac{r_{N,j}}{N},
\tag{35}
\]

for \(0\le j<N\).  Both \(s_{N,j}\) and \(d_{N,j}\) decrease strictly
with \(j\).  There is a nonnegative \(L^1\) density \(g_N\) on
\((0,s_{N,0})\) such that

\[
\int_0^{s_{N,j}}g_N(t)\,dt=d_{N,j}
\qquad(0\le j<N).
\tag{36}
\]

Indeed, put mass \(d_{N,N-1}\) on
\((0,s_{N,N-1})\), and mass
\(d_{N,j}-d_{N,j+1}\) on each
\((s_{N,j+1},s_{N,j})\), using constant densities on those intervals.
Then

\[
\int_0^{s_{N,0}}g_N(t)\,dt
=\frac{r_{\rm out,N}}N\longrightarrow0,
\qquad
s_{N,0}=c_0r_{\rm out,N}^2\longrightarrow0,
\tag{37}
\]

but

\[
\boxed{
\sum_{j=0}^{N-1}
\sqrt{\frac{d_{N,j}}{r_{N,j}}}
=\sqrt N\longrightarrow\infty,
\qquad
\max_j
\sqrt{\frac{d_{N,j}}{r_{N,j}}}
=N^{-1/2}\longrightarrow0.
}
\tag{38}
\]

This is a scalar dissipation history, not an NSE trajectory.  It shows
that the nesting and staggered clocks add no uniform rate to terminal
dissipation absolute continuity.  More sharply, if

\[
F_N(s):=\int_0^s g_N(t)\,dt,
\tag{38a}
\]

then

\[
\frac{F_N(s_{N,j})}{\sqrt{s_{N,j}}}
=
\frac{d_{N,j}}{\sqrt{s_{N,j}}}
=
\frac{1}{N\sqrt{c_0(j+1)}}.
\tag{38b}
\]

The function \(F_N\) is affine between these nodes, while
\(\sqrt{s}\) is concave.  Hence

\[
\boxed{
F_N(s)
\le
\frac{1}{N\sqrt{c_0}}\sqrt{s}
\le C\sqrt{s}
\qquad(0\le s\le s_{N,0}).
}
\tag{38c}
\]

Thus even a uniform critical square-root modulus does not bound the
staggered action over this triangular scalar family.  The construction
uses a different \(g_N\) for each \(N\); it is not a survivor on one fixed
physical trajectory.  The one-history nested mechanism is already recorded
in [the stretched-history no-go](adjoint-pressure-stretched-history.md).

There is a matching sufficient power rate.  Suppose the physical
dissipation measure obeys, uniformly near \(T^*\),

\[
\int_{T^*-s}^{T^*}\|\nabla v(t)\|_2^2\,dt
\le C_\alpha s^\alpha
\qquad(0<s<s_\alpha)
\tag{39}
\]

for some \(\alpha>1/2\).  Shrink the fixed cutoff so that

\[
C_0r_\bullet^2<s_\alpha,
\tag{39a}
\]

where \(C_0\) depends only on
\(T,R_0,\gamma,\nu,\nu_{\rm phys}\).  The physical endpoint gap and
(9)--(11)
place \(J_{n,k}\) inside a terminal interval of length at most

\[
C_0(j_{n,k}+1)r_{n,k}^2.
\tag{40}
\]

Equations (39)--(40) imply

\[
\sqrt{\frac{\delta_{n,k}}{r_{n,k}}}
\le
C_{\alpha,C_0,C_\alpha}
(j_{n,k}+1)^{\alpha/2}
r_{n,k}^{\alpha-1/2}.
\tag{41}
\]

Since \(r_{n,k}\le r_\bullet L^{-j_{n,k}}\),

\[
\boxed{
\mathfrak D_n^{\rm stag}(T;r_\bullet)
\le
C_{\alpha,L,C_0,C_\alpha}
r_\bullet^{\alpha-1/2}
\sum_{j\ge0}
(j+1)^{\alpha/2}
L^{-(\alpha-1/2)j}
<\infty.
}
\tag{42}
\]

Thus, among power laws, geometric summability begins exactly at
\(\alpha>1/2\), while (38c) supplies a scalar survivor at
\(\alpha=1/2\).  This is not an exact general-modulus or PDE threshold:
logarithmic improvements at the critical power are not classified, and
the available terminal absolute continuity supplies no positive power.

## 6. Exact route consequence

Within the pressure upper audit, this theorem closes:

1. passive entrance high-pass energy as an independent bookkeeping
   branch;
2. derivative-free remote linear inheritance on all scale-zero shells,
   using staggered rather than common lookback;
3. a finite physical-horizon re-expression of every remaining entrance
   contribution as auxiliary zero-data-response work; and
4. a same-trajectory coefficient-dissipation ceiling for that auxiliary
   work;
5. every \(s^\alpha\), \(\alpha>1/2\), as a sufficient temporal
   dissipation power modulus, with a triangular scalar survivor at
   \(\alpha=1/2\).

It does not prove:

1. finiteness of either nonlinear-work aggregate;
2. an individual shell or a fixed block charge;
3. spatial localisation of the staggered source;
4. disjointness or bounded overlap of the staggered time windows;
5. finiteness of the critical nested dissipation action (28g);
6. a signed event-index telescope or non-Zeno event law;
7. causal independence, a new NSE positivity law, or non-reuse;
8. exclusion of the coherent ancient profile; or
9. regularity, breakdown, or any Clay alternative A--D.

The next theorem must use NSE structure beyond the global zero-data
energy identity: spatial source coherence, active-block control,
control of the nested critical dissipation action, comparison of the
staggered windows with selected Besov events, or a signed cross-event
functional.

No executable certificate is claimed for the multiplier, Lorentz, or
PDE steps.
