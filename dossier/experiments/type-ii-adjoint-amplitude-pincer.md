# The q4 adjoint dissipation is pinned to high-amplitude drift slabs

- **Experiment:** EXP-TYPE-II-ADJOINT-AMPLITUDE-PINCER-001
- **Route:** ROUTE-R3C
- **Status:** complete conditional reduction; external review pending
- **Domain:** smooth finite-energy Navier--Stokes flow on \(\mathbb R^3\)
- **Clay status:** unsolved
- **Input:** [cross-current anomaly](type-ii-cross-current-anomaly.md)

## Verdict

Put, on a terminal interval \(I=(t_0,T)\),

\[
M(t):=\|u(t)\|_{L^{3,\infty}},
\qquad
Y(t):=\|\nabla a(t)\|_2,
\qquad
p_*:=\frac{11}{2}.
\tag{1}
\]

The exact q4 clock gives

\[
|\{t\in I:M(t)>\lambda\}|
\lesssim
\frac{\lambda^{-p_*}}{\log(e+\lambda)}.
\tag{2}
\]

The preceding renormalisation theorem says that the q4 entrance forces

\[
\int_I M(t)Y(t)^2\,dt=\infty
\tag{3}
\]

on every terminal interval, although \(Y\in L^2(I)\).

This round identifies the exact rearrangement space that would contradict
(3).  If \(Y_I^*\) denotes the decreasing rearrangement on \(I\), set

\[
\ell_I(s):=\log\left(e+\frac{|I|}{s}\right)
\qquad(0<s<|I|)
\tag{4}
\]

and

\[
\boxed{
\mathfrak Z_I(Y)^2
:=
\int_0^{|I|}
s^{-2/11}\ell_I(s)^{-2/11}
\bigl(Y_I^*(s)\bigr)^2\,ds.
}
\tag{5}
\]

Then

\[
\boxed{
\mathfrak Z_I(Y)<\infty
\quad\Longrightarrow\quad
\int_I MY^2<\infty.
}
\tag{6}
\]

Consequently every q4 entrance must satisfy

\[
\boxed{\mathfrak Z_I(Y)=\infty}
\tag{7}
\]

on every terminal interval.  Condition (5) is strictly weaker than

\[
Y\in L^{22/9,2}(I),
\tag{8}
\]

the sufficient target recorded in the previous round.  It uses the
logarithmic improvement in the exact first-record clock rather than
discarding it.

The amplitude-slab form is even more concrete.  Let

\[
A_n:=\{t\in I:2^n<M(t)\le 2^{n+1}\},
\qquad
d_n:=\int_{A_n}Y(t)^2\,dt.
\tag{9}
\]

Then

\[
\sum_n d_n<\infty,
\qquad
\boxed{\sum_{n\ge N}2^n d_n=\infty
\quad\text{for every }N.}
\tag{10}
\]

Moreover, for every positive summable sequence
\((\varepsilon_n)\), infinitely many \(n\) obey

\[
d_n\ge 2^{-n}\varepsilon_n
\tag{11}
\]

and at some Lebesgue point \(t_n\in A_n\),

\[
\boxed{
Y(t_n)
\gtrsim
2^{9n/4}\bigl(n\varepsilon_n\bigr)^{1/2}.
}
\tag{12}
\]

For example, choosing
\(\varepsilon_n=[n(\log n)^2]^{-1}\) gives a sequence
\(t_n\uparrow T\) such that

\[
\boxed{
Y(t_n)
\gtrsim
\frac{M(t_n)^{9/4}}
{\log\log(e^e+M(t_n))}.
}
\tag{13}
\]

Thus an entrance does not merely need an unspecified failure of temporal
higher integrability.  Its adjoint enstrophy must correlate with the
largest weak-\(L^3\) drift slabs at essentially the exact
\(M^{9/4}\) amplitude.

The requested Caccioppoli/Meyers audit does not close this pincer.
It gives three exact negative conclusions.

1. Standard differentiated energy produces an \(X^4Y^2\) coefficient,
   where \(X=\|\nabla u\|_2\); the ledger has \(X\in L^2_t\), not
   \(X\in L^4_t\).
2. Existing BMO-skew reverse Hölder theory is local in space-time, assumes
   a uniform-in-time BMO coefficient, and gives only some exponent
   \(2+\epsilon\) depending on that uniform norm.  On q4 record blocks the
   norm grows without bound.  In addition, the projected pressure enters
   as a divergence forcing known only at the base \(L^2\) level, making the
   desired \(p>2\) estimate circular.
3. Even with the self-generated drift \(b=0\), the heat equation with
   arbitrary \(L^2\) initial data has no universal
   \(L_t^{2+\epsilon}L_x^2\) estimate for its gradient.  Any successful
   theorem must use the zero weak trace and the nonzero same-trajectory
   cross defect, not parabolic smoothing alone.

The live q4 question is therefore narrower than (8):

> Can the same-trajectory cross defect force
> \(\mathfrak Z_I(Y)<\infty\), or an equivalent summable
> amplitude-slab anti-correlation, despite the projected pressure?

No such estimate is proved here.

## 1. Exact rearrangement closure

### Lemma 1: inversion of the q4 clock

There is a constant \(C_I\) such that

\[
M_I^*(s)
\le
C_I\left[
1+s^{-2/11}\ell_I(s)^{-2/11}
\right]
\qquad(0<s<|I|).
\tag{14}
\]

#### Proof

Only small \(s\) matters.  Let

\[
\lambda_s
:=
A\,s^{-1/p_*}\ell_I(s)^{-1/p_*}.
\]

For sufficiently small \(s\),

\[
\log(e+\lambda_s)\asymp\ell_I(s).
\]

Using (2),

\[
|\{M>\lambda_s\}|
\lesssim
A^{-p_*}s.
\]

Choose \(A\) larger than the implicit constant.  The defining property of
decreasing rearrangements gives
\(M_I^*(s)\le\lambda_s\).  A constant controls the remaining values of
\(s\).

### Theorem 2: logarithmically relaxed closing space

Equation (6) holds.  In particular, (7) is necessary for the q4
entrance.

#### Proof

The Hardy--Littlewood rearrangement inequality and Lemma 1 give

\[
\begin{aligned}
\int_I MY^2
&\le
\int_0^{|I|}
M_I^*(s)\bigl(Y_I^*(s)\bigr)^2\,ds\\
&\lesssim_I
\int_IY^2
+\mathfrak Z_I(Y)^2.
\end{aligned}
\tag{15}
\]

The first term is finite by the adjoint energy bound.  Therefore (5)
implies finite weighted dissipation, contradicting the entrance theorem.

For \(q_*=22/9\),

\[
\|Y\|_{L^{q_*,2}(I)}^2
\asymp
\int_0^{|I|}
s^{2/q_*-1}\bigl(Y_I^*(s)\bigr)^2\,ds
=
\int_0^{|I|}
s^{-2/11}\bigl(Y_I^*(s)\bigr)^2\,ds.
\tag{16}
\]

Since \(\ell_I^{-2/11}\le1\), (8) implies (5), while the converse need
not hold.  For example, near \(s=0\), the rearrangement
\[
\bigl(Y_I^*(s)\bigr)^2
=
s^{-9/11}\bigl[\log(e/s)\bigr]^{-10/11}
\]
has finite (5), but its \(L^{22/9,2}\) norm diverges.

### Endpoint warning: strong \(L^{22/9}\) is not enough

The logarithm in (5) cannot be discarded using (2) alone.  This can be
seen on the scalar rearrangement interval
\(0<s<e^{-e}\).  Put

\[
L(s):=\log(e/s),
\qquad
L_2(s):=\log L(s),
\tag{17}
\]

\[
M_0(s):=
s^{-2/11}L(s)^{-2/11},
\tag{18}
\]

and

\[
Z_0(s):=
s^{-9/11}L(s)^{-9/11}L_2(s)^{-1},
\qquad
Y_0:=Z_0^{1/2}.
\tag{19}
\]

The decreasing function \(M_0\) has, up to constants, the distribution
in (2).  Also

\[
\int_0^{e^{-e}}Y_0^{22/9}\,ds
=
\int_0^{e^{-e}}
\frac{ds}{sL(s)L_2(s)^{11/9}}
<\infty,
\tag{20}
\]

whereas

\[
\int_0^{e^{-e}}M_0Y_0^2\,ds
=
\int_0^{e^{-e}}
\frac{ds}{sL(s)L_2(s)}
=\infty.
\tag{21}
\]

This is a scalar saturation ledger, not a Navier--Stokes construction.
It proves that strong endpoint \(L^{22/9}\) alone cannot close (3) from
the clock distribution.

## 2. The amplitude-slab pincer

### Theorem 3: forced dissipation on arbitrarily high slabs

Equations (10)--(12) hold.

#### Proof

The unweighted sum in (10) is bounded by
\(\int_IY^2\).  On \(A_n\), \(M\le2^{n+1}\).  Hence

\[
\int_I MY^2
\le
C_N\int_IY^2
+2\sum_{n\ge N}2^nd_n.
\tag{22}
\]

Equation (3) forces the tail series in (10) to diverge.

If (11) failed for all sufficiently large \(n\), then

\[
\sum_{n\ge N}2^nd_n
\le
\sum_{n\ge N}\varepsilon_n
<\infty,
\]

a contradiction.

By (2),

\[
|A_n|
\lesssim
\frac{2^{-11n/2}}{n}.
\tag{23}
\]

For every \(n\) satisfying (11), a Lebesgue point in \(A_n\) can be
chosen above a fixed fraction of the slab average, and hence

\[
\begin{aligned}
Y(t_n)^2
&\ge
\frac{d_n}{|A_n|}\\
&\gtrsim
n\varepsilon_n\,2^{(11/2-1)n}
=
n\varepsilon_n\,2^{9n/2}.
\end{aligned}
\]

This is (12).  The selected indices tend to infinity.  Smoothness on
compact preterminal intervals makes \(M\) locally bounded, so their
times approach \(T\); after passing to a subsequence they increase to
\(T\).

### Corollary 4: exact pointwise amplitude barrier

For every \(\beta>0\), \(C>0\), and terminal interval \(I\), the
inequality

\[
Y(t)^2
\le
C\left[
1+\frac{M(t)^{9/2}}
{\log(e+M(t))^\beta}
\right]
\tag{24}
\]

fails on a set of positive measure.

#### Proof

The distribution formula and (2) imply

\[
\int_I
\frac{M^{11/2}}
{\log(e+M)^\beta}\,dt
<\infty.
\tag{25}
\]

Indeed, layer cake reduces its large-\(\lambda\) part to

\[
\int^\infty
\frac{d\lambda}
{\lambda[\log(e+\lambda)]^{1+\beta}},
\]

which converges.  If (24) held almost everywhere, then
\(\int_I MY^2<\infty\), contradicting (3).

Thus any survivor must outrun every \(M^{9/4}\) pointwise ceiling having
an arbitrarily small logarithmic saving.  This is a necessary
concentration statement, not an upper estimate for \(Y\).

## 3. What differentiated energy can and cannot do

Reverse time as in the input proof:

\[
\partial_\tau v-\nu\Delta v
+(b\cdot\nabla)v+\nabla Q=0,
\qquad
\nabla\cdot b=\nabla\cdot v=0.
\tag{26}
\]

Put

\[
X(\tau):=\|\nabla b(\tau)\|_2,
\qquad
Y(\tau):=\|\nabla v(\tau)\|_2,
\qquad
Z(\tau):=\|\Delta v(\tau)\|_2.
\tag{27}
\]

### Proposition 5: the enstrophy hull lands on \(X^4\)

At smooth positive reverse times,

\[
\frac12\frac d{d\tau}Y^2
+\frac{\nu}{2}Z^2
\lesssim
\nu^{-3}X^4Y^2.
\tag{28}
\]

More generally, interpolate

\[
\|b\|_{L^{r_\alpha}}
\lesssim
M^{1-\alpha}X^\alpha,
\qquad
\frac1{r_\alpha}
=
\frac13-\frac{\alpha}{6},
\qquad
0<\alpha\le1.
\tag{29}
\]

The corresponding differentiated-energy estimate has coefficient

\[
\boxed{
M^{4/\alpha-4}X^4.
}
\tag{30}
\]

No value of \(\alpha\) removes the fourth power of \(X\).

#### Proof

Pair (26) with \(-\Delta v\).  Pressure vanishes against the
divergence-free field \(\Delta v\), and

\[
\int(b\cdot\nabla)v\cdot(-\Delta v)
=
\int
\partial_kb_\ell\,\partial_\ell v_i\,\partial_kv_i.
\tag{31}
\]

Thus

\[
|\text{(31)}|
\le
X\|\nabla v\|_4^2
\lesssim
XY^{1/2}Z^{3/2}.
\]

Young's inequality proves (28).

For (30), let \(q_\alpha\) satisfy

\[
\frac1{r_\alpha}+\frac1{q_\alpha}+\frac12=1.
\]

Sobolev interpolation gives

\[
\|\nabla v\|_{q_\alpha}
\lesssim
Y^{1-\gamma_\alpha}Z^{\gamma_\alpha},
\qquad
\gamma_\alpha:=\frac3{r_\alpha}=1-\frac{\alpha}{2}.
\]

Consequently the transport work is bounded by

\[
M^{1-\alpha}X^\alpha
Y^{1-\gamma_\alpha}Z^{1+\gamma_\alpha}.
\]

Young's conjugate exponent on the coefficient is

\[
\frac2{1-\gamma_\alpha}
=
\frac4\alpha.
\]

The resulting factor is exactly

\[
\left(M^{1-\alpha}X^\alpha\right)^{4/\alpha}Y^2
=
M^{4/\alpha-4}X^4Y^2.
\]

The q4 ledger supplies \(X\in L^2_\tau\), so (28)--(30) do not provide
an integrable Grönwall coefficient.

At the endpoint \(r=3\), the estimate is instead

\[
|\text{transport work}|
\lesssim MZ^2,
\]

which can be absorbed only when \(M\) is uniformly small relative to
\(\nu\).  The terminal record slabs have \(M\to\infty\).

## 4. BMO-skew Meyers theory and the projected-pressure gate

For a divergence-free \(b\in L^{3,\infty}(\mathbb R^3)\), define the
skew matrix

\[
D_{ij}
:=
\partial_j(-\Delta)^{-1}b_i
-\partial_i(-\Delta)^{-1}b_j.
\tag{32}
\]

\[
\partial_iD_{ij}=b_j,
\qquad
\|D\|_{\mathrm{BMO}}
\lesssim
\|b\|_{L^{3,\infty}}.
\tag{33}
\]

The BMO estimate follows directly by splitting the order-\(-1\) kernel
into \(2B\) and dyadic far annuli.  On \(2B\), weak-\(L^3\) gives
\(\int_{2B}|b|\lesssim M r^2\); in the far field the kernel difference
contributes a summable \(M2^{-k}\).

Ignoring pressure, each component of (26) can therefore be written as a
divergence-form parabolic equation with symmetric part \(\nu I\) and
skew part \(D\).

Zhang's arXiv v5 preprint proves local Caccioppoli and reverse Hölder
estimates for parabolic systems with a skew part in
\(L^\infty_t\mathrm{BMO}_x\).  The resulting exponent is some
\(p>2\) sufficiently close to two, and both \(p\) and the implicit
constant depend on the uniform BMO norm.

This does not supply (5) for the q4 entrance:

1. on successive first-record blocks the available uniform norm grows
   like the record amplitude \(m_j\to\infty\), so no record-uniform
   exponent above two follows;
2. the theorem is a local space-time estimate, whereas (5) is a
   terminal mixed norm of the global \(L_x^2\) gradient; and
3. the projected equation is
   \[
   \partial_\tau v
   -\nabla\cdot((\nu I-D)\nabla v)
   =
   -\nabla Q
   =
   \nabla\cdot(-QI).
   \tag{34}
   \]
   On a block where \(M\le K\), Calderón--Zygmund and Lorentz Sobolev
   give only
   \[
   \|Q(\tau)\|_2
   \lesssim
   M(\tau)Y(\tau),
   \qquad
   Q\in L^2_{\tau,x}.
   \tag{35}
   \]
   The preprint's \(p>2\) gradient conclusion requires the divergence
   forcing in the same \(L^p\) class.  Asking \(Q\in L^p\) is already a
   higher-integrability request and is circular here.

The pressure is not being blamed for a signed lower bound.  Equation
(35) records the precise integrability mismatch in the available
positive theorem.

## 5. Generic parabolic smoothing has no temporal gain

### Proposition 6: heat-flow boundary saturation

For every \(\epsilon>0\), there is a divergence-free
\(f\in L^2(\mathbb R^3)\) such that the heat solution

\[
v(\tau)=e^{\nu\tau\Delta}f
\tag{36}
\]

satisfies

\[
\int_0^\infty\|\nabla v(\tau)\|_2^2\,d\tau<\infty,
\tag{37}
\]

but

\[
\int_0^1
\|\nabla v(\tau)\|_2^{2+\epsilon}\,d\tau
=\infty.
\tag{38}
\]

One \(f\) can be chosen so that (38) holds simultaneously for every
\(\epsilon>0\).

#### Proof

Choose mutually disjoint solenoidal Fourier annuli at frequencies

\[
N_k:=4^k
\]

and fields \(f_k\) supported in those annuli with

\[
\|f_k\|_2=\frac1k.
\]

Then

\[
f:=\sum_{k\ge1}f_k\in L^2.
\]

Plancherel gives

\[
\int_0^\infty\|\nabla e^{\nu\tau\Delta}f\|_2^2\,d\tau
=
\frac1{2\nu}\|f\|_2^2.
\]

On a disjoint time interval \(J_k\) of length comparable to
\(N_k^{-2}\), centred at the heat time \(N_k^{-2}\), the \(k\)-th
Fourier block obeys

\[
\|\nabla e^{\nu\tau\Delta}f_k\|_2
\gtrsim
\frac{N_k}{k}.
\]

For every \(p>2\),

\[
\begin{aligned}
\int_0^1
\|\nabla e^{\nu\tau\Delta}f\|_2^p\,d\tau
&\ge
\sum_k\int_{J_k}
\|\nabla e^{\nu\tau\Delta}f_k\|_2^p\,d\tau\\
&\gtrsim
\sum_k
N_k^{p-2}k^{-p}
=\infty.
\end{aligned}
\]

Taking \(b=0\) makes the drift a smooth self-generated Navier--Stokes
trajectory and \(Q=0\).  This example has the nonzero strong trace
\(f\), not the q4 zero weak trace.  It proves exactly that neither
parabolicity nor the phrase “same Navier--Stokes drift” alone can yield
the temporal improvement.

## 6. Exact frontier

### Robust conditional findings, subject to external review

1. The logarithmically relaxed rearrangement norm (5), strictly weaker
   than \(L_t^{22/9,2}\), is sufficient to close the q4 entrance.
2. Every survivor has the divergent slab ledger (10), the general spike
   law (12), and in particular the near-\(M^{9/4}\) spikes (13).
3. Strong \(L_t^{22/9}\) alone is not sufficient under the clock
   distribution; (18)--(21) saturate the missing iterated logarithm.
4. Differentiated adjoint energy lands on the unavailable \(X^4\)
   coefficient for the entire Hölder--Sobolev interpolation hull.
5. Current BMO-skew Meyers theory has three mismatches: unbounded record
   norms, local space-time rather than terminal mixed control, and the
   projected pressure at only the base forcing exponent.
6. Generic heat smoothing admits no \(L_t^{2+\epsilon}L_x^2\) gradient
   gain at an \(L^2\) initial boundary.

### Closed shortcuts

1. Do not ask generic Caccioppoli or heat smoothing to prove (8).
2. Do not treat the Zhang reverse Hölder exponent as uniform over q4
   record slabs.
3. Do not feed \(Q\in L^2\) into a theorem requiring \(Q\in L^p\),
   \(p>2\).
4. Do not replace the exact Lorentz--Zygmund gate by strong
   \(L^{22/9}\); the scalar ledger disproves that implication.
5. Do not infer that the forced lower spikes (12) are upper bounds or a
   contradiction by themselves.

### Things still to prove

1. Prove \(\mathfrak Z_I(Y)<\infty\) from the same-trajectory cross
   defect, contradicting (7).
2. Equivalently, prove enough amplitude-slab anti-correlation to make
   \(\sum2^nd_n\) finite.
3. Develop a pressure-compatible boundary reverse Hölder theorem whose
   gain is uniform across the unbounded first-record coefficients, or
   show that the cross defect supplies the missing pressure
   equiintegrability.
4. Alternatively close the Fourier commutator or
   \(\mathcal H^1\)-capacity routes from the preceding round.
5. Treat slower clocks, divergent normalised energy, and the other Clay
   alternatives separately.

### Conjecture: same-trajectory Lorentz--Zygmund gain

Under the exact q4 hypotheses, the projected-Oseen entrance satisfies

\[
\mathfrak Z_I\bigl(\|\nabla a\|_2\bigr)<\infty
\]

on some terminal interval \(I\).

Theorem 2 would exclude the q4 terminal defect.  The conjecture is not
proved.

## Source provenance

Guoming Zhang,
*On regularity for nonhomogeneous parabolic systems with a
skew-symmetric part in BMO*, arXiv:2403.01741v5 (preprint).

- pinned source archive:
  `lab/cache/arxiv/2403.01741/source.tar`
- archive SHA-256:
  `98ba2c1b92ceff3946f5fb67e2ec992632c5f523da5861f1966fd01e467d17b1`
- exact source:
  `lab/cache/arxiv/2403.01741/Gz967sa.tex`
- source SHA-256:
  `02f6f3c055992464d99adf0ade44bd4e608bef768a85d0cd19dd5b84de12755c`
- source anchors:
  lines 367--381 state the uniform
  \(L^\infty_t\mathrm{BMO}_x\) assumption, the local \(p>2\)
  estimates, and norm dependence; lines 607--630 give the improved
  Caccioppoli/reverse Hölder step; lines 717--719 perform the Gehring
  gain to \(p>2\).

The literature statement is recorded as a preprint claim, not as an
externally established theorem.
