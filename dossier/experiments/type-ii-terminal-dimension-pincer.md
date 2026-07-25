# The q4 energy defect forces a terminal dimension pincer

- **Experiment:** EXP-TYPE-II-TERMINAL-DIMENSION-PINCER-001
- **Route:** ROUTE-R3C
- **Status:** complete conditional reduction; external review pending
- **Domain:** smooth finite-energy Navier--Stokes flow on \(\mathbb R^3\)
- **Clay status:** unsolved
- **Input:** [critical-clock theorem](type-ii-critical-clock-regeneration.md)

## Verdict

The exact \(q=4\) clock has a genuine weak endpoint:

\[
M(t):=\|u(t)\|_{L^{3,\infty}}
\quad\Longrightarrow\quad
M\in L_t^{11/2,\infty}
\cap\bigcap_{r>11/2}L_t^{11/2,r}.
\]

This does **not** supply a known energy-equality theorem.  Even after
granting the additional favourable surrogate assumption
\(L_t^{11/2,\infty}B^0_{3,\infty}\), the entire interpolation hull with

\[
L_t^\infty L_x^2
\cap L_t^2H_x^1
\]

misses the Cheskidov--Luo sufficient Besov smoothness in every parameter
region.  Optimising the Leslie--Shvydkoy first-time criterion over the
corresponding mixed-norm hull gives exactly

\[
\sup f(p,q)=\frac35.
\]

Let \(\mathcal E\) be the terminal energy measure, \(u_*=u(T^*)\) the
weakly continuous Leray--Hopf trace, and

\[
\vartheta:=\mathcal E-|u_*|^2\,dx.
\]

The critical-clock theorem makes \(\vartheta\) a nonzero positive measure.
It is supported on the terminal singular set \(\sigma\).  The optimised
Leslie--Shvydkoy concentration theorem makes it vanish on every set of
Hausdorff dimension below \(3/5\).  Consequently,

\[
\boxed{
\frac35\le \dim_{\mathrm H}\sigma\le1,
\qquad
\mathcal H^1(\sigma)=0.
}
\]

The upper statement is Caffarelli--Kohn--Nirenberg.  The lower statement is
a conditional repository deduction from the exact \(q=4\) branch and is
pending external review.  It is not a regularity theorem.

The pressure route also has an exact numerical obstruction.  The clock
gives

\[
\pi\in L_t^{11/4,\infty}L_x^{3/2,\infty},
\qquad
\frac2{11/4}+\frac3{3/2}
=2+\frac8{11}.
\]

Every direct interpolation with the energy-class pressure line has
supercriticality \(\gamma\ge8/11\).  Barker--Wang require
\(\gamma<1/2\), and their dimension formula could enter the
\(<3/5\) closing region only if \(\gamma<1/4\).  Thus direct norm
interpolation misses the dimension-closing pressure region by at least

\[
\frac8{11}-\frac14=\frac{21}{44}.
\]

Finally, the terminal defect obeys an exhaustive spectral alternative.
Along a subsequence, either:

1. a fixed defect amount lies in
   \(\{\Lambda_j<|\xi|\le A\Lambda_j\}\) for one fixed \(A\); then
   disjoint time intervals carry fixed-sign nonlinear work against
   event-dependent clock-band tests, while the viscous work tends to zero;
   or
2. defect energy escapes above \(A_j\Lambda_j\) with \(A_j\to\infty\),
   forcing the stronger pointwise enstrophy floor
   \[
   \|\nabla u(s_j)\|_2^2
   \gtrsim A_j^2\Lambda_j^2.
   \]

In the first branch the available nonlinear capacity is exactly order one
per event, so its sum is not controlled.  In the second branch no residence
time at the super-clock frequency is known.  These are now the two precise
survivors.

## 1. Exact endpoint of the record clock

Let \(t_j\uparrow T^*\) be the exact \(q=4\) first-record times.  Thus

\[
m_j:=M(t_j)\asymp2^{2j},
\qquad
t_{j+1}-t_j\lesssim\frac{2^{-11j}}j,
\tag{1}
\]

and

\[
M(t)\le m_j\qquad(0\le t\le t_j).
\tag{2}
\]

### Lemma 1: logarithmically improved endpoint distribution

For all sufficiently large \(\lambda\),

\[
\boxed{
\left|\{t<T^*:M(t)>\lambda\}\right|
\le
\frac{C\lambda^{-11/2}}{\log(e+\lambda)}.
}
\tag{3}
\]

Consequently,

\[
\boxed{
M\in L^{11/2,\infty}(0,T^*)
\cap
\bigcap_{r>11/2}L^{11/2,r}(0,T^*).
}
\tag{4}
\]

#### Proof

If \(m_j\le\lambda<m_{j+1}\), the first-record property gives

\[
\{M>\lambda\}\subset(t_j,T^*).
\]

The geometric tail of (1) satisfies

\[
T^*-t_j
\lesssim
\sum_{k\ge j}\frac{2^{-11k}}k
\lesssim\frac{2^{-11j}}j.
\]

Since \(\lambda\asymp2^{2j}\) and \(j\asymp\log(e+\lambda)\), this is
(3).

Put \(p_*=11/2\) and let \(\mu_M\) denote the distribution function.
The weak endpoint follows from

\[
\sup_{\lambda>0}\lambda^{p_*}\mu_M(\lambda)<\infty.
\]

For \(r<\infty\), the distribution-function form of the Lorentz norm gives

\[
\|M\|_{L^{p_*,r}}^r
\asymp
\int_0^\infty
\left[\lambda\mu_M(\lambda)^{1/p_*}\right]^r
\frac{d\lambda}{\lambda}.
\]

The terminal part is bounded by

\[
C\int^\infty
\frac{d\lambda}
{\lambda[\log(e+\lambda)]^{r/p_*}},
\]

which converges exactly when \(r>p_*\).  Smoothness controls the
nonterminal part.  The argument does not prove strong
\(L^{11/2}\): at \(r=p_*\) the displayed upper estimate is harmonic.

## 2. The direct Besov route misses in every region

No embedding comparison between the actual endpoint
\(L_x^{3,\infty}\) and \(B^0_{3,\infty}\) is being used.  To make the
audit one-sided in favour of energy equality, temporarily grant the
additional surrogate assumption

\[
C:=L_t^{11/2,\infty}B^0_{3,\infty}.
\tag{5}
\]

Combine it with

\[
A:=L_t^\infty B^0_{2,2},
\qquad
B:=L_t^2B^1_{2,2}.
\tag{6}
\]

Let \(a,b,c\ge0\), \(a+b+c=1\), be interpolation weights on
\(A,B,C\).  The resulting optimistic exponent triple is

\[
\frac1\beta=\frac b2+\frac{2c}{11},
\qquad
\frac1p=\frac12-\frac c6,
\qquad
\alpha_{\rm av}=b.
\tag{7}
\]

Cheskidov and Luo record the following minimal sufficient spatial
smoothness across the four strong-time interpolation regions:

\[
\alpha_{\rm req}=
\begin{cases}
\dfrac2\beta+\dfrac2p-1,
 & \beta\ge3,\ p\ge\beta,\\[1mm]
\dfrac1\beta+\dfrac3p-1,
 & \beta\ge3,\ p\le\beta,\\[1mm]
\dfrac5{2\beta}+\dfrac3p-\dfrac32,
 & \beta\le3,\ \dfrac1\beta+\dfrac2p\ge1,\\[1mm]
\dfrac2\beta+\dfrac2p-1,
 & \beta\le3,\ \dfrac1\beta+\dfrac2p\le1.
\end{cases}
\tag{8}
\]

Their weak-in-time theorem supplies the corresponding first-region
endpoint under its strict parameter assumptions.

### Proposition 2: strict convex-hull gap

No admissible point of (7) reaches (8).  More precisely, in the four
regions of (8), respectively,

\[
\alpha_{\rm req}-\alpha_{\rm av}
=
\begin{cases}
\dfrac c{33},\\[1mm]
\dfrac a2+\dfrac{2c}{11},\\[1mm]
\dfrac b4-\dfrac c{22},\\[1mm]
\dfrac c{33}.
\end{cases}
\tag{9}
\]

Every applicable expression is strictly positive.

#### Proof

Substitute (7) into (8).  Only the third line needs an additional
observation.  Its region condition gives

\[
\frac1\beta+\frac2p\ge1
\quad\Longrightarrow\quad
\frac b2+\frac{2c}{11}\ge\frac c3
\quad\Longrightarrow\quad
b\ge\frac{10c}{33}.
\]

Hence

\[
\frac b4-\frac c{22}\ge\frac c{33},
\]

and it is positive also when \(c=0\), because that region then requires
\(b>0\).

In the first and fourth lines, equality in (9) would require \(c=0\).
Then \(p=2\).  This is incompatible with the first region
\((p\ge\beta\ge3)\); in the fourth region its second inequality forces
\(b=0\), which is incompatible with \(\beta\le3\).  In the second line,
equality would be the pure \(B\) point, which has \(\beta=p=2\) and is
not in that region.

Thus even with the additional favourable surrogate assumption, every
direct Cheskidov--Luo interpolation criterion is missed.  This excludes only this
interpolation mechanism; it does not exclude a new structural route to
energy equality.

The audit also covers the usual post-interpolation Sobolev/Besov
embedding.  If \(h\ge0\) units of reciprocal spatial integrability are
gained, then

\[
\frac1p\mapsto\frac1p-h,
\qquad
\alpha_{\rm av}\mapsto\alpha_{\rm av}-3h.
\]

In the four lines of (8), the gap in (9) respectively increases by
\(h\), stays fixed, stays fixed, or increases by \(h\).  Lowering the
time exponent on the finite interval only increases the required
smoothness.  Hence the no-go includes the standard embeddings of
\(H^1\), such as \(L_t^2H_x^1\subset L_t^2L_x^6\).

## 3. The \(3/5\) mixed-norm ceiling

Write mixed-norm exponent coordinates as

\[
x:=\frac1p,\qquad y:=\frac1q.
\]

The strong interior exponents available from the endpoint clock and the
energy class lie in the convex hull of

\[
A_0=\left(\frac12,0\right),
\quad
B_0=\left(\frac16,\frac12\right),
\quad
C_0=\left(\frac13,\frac2{11}\right).
\tag{10}
\]

The point \(C_0\) itself is only a weak endpoint, but it controls the
closure of the hull.

In Leslie--Shvydkoy Regions I--II,

\[
f(p,q)
=
3-\frac{2y}{1-2x-y}.
\tag{11}
\]

In Region III,

\[
f(p,q)
=
3-
\frac{2y(6x-1)}
{(2-3x-3y)(1-2x)}.
\tag{12}
\]

### Proposition 3: sharp optimisation

Every admissible point in the hull (10) satisfies

\[
\boxed{f(p,q)\le\frac35.}
\tag{13}
\]

The supremum \(3/5\) occurs at the weak endpoint \(C_0\); it is approached
by strong interior exponents.

#### Proof

First suppose \(x\le1/3\), equivalently \(p\ge3\).  The affine inequality

\[
12x+11y\ge6
\tag{14}
\]

holds at all three vertices of (10), with equality at \(A_0\) and
\(C_0\), and hence throughout the hull.  In the positive-denominator
region of (11), (14) is equivalent to

\[
\frac{2y}{1-2x-y}\ge\frac{12}{5}.
\]

This proves (13).

Now suppose \(1/3<x<1/2\).  The hull lies above the edge \(A_0C_0\):

\[
y\ge\frac6{11}(1-2x).
\tag{15}
\]

It does not enter Leslie--Shvydkoy Regions IV--V: every hull point has
\(x+y\ge1/2\), and the sole equality vertex \(A_0\) fails their other
condition.  Thus only Region III is relevant.  For fixed \(x\), the
subtracted quotient in (12) increases with \(y\), so \(f\) is maximised
on the lower edge (15).

Set \(z=1-2x\in(0,1/3)\).  Substitution of \(y=6z/11\) gives

\[
f
=
3-\frac{24(2-3z)}{11-3z}.
\tag{16}
\]

The right side is strictly increasing in \(z\), and its limit at
\(z=1/3\), the vertex \(C_0\), is \(3/5\).

## 4. The terminal dimension pincer

Assume now the full critical-clock conclusion.  Choose its endpoint
sequence \(s_j\uparrow T^*\) and let

\[
E_-:=\lim_{t\uparrow T^*}\|u(t)\|_2^2.
\]

Let \(\mathcal E\) be a weak-star limit of
\(|u(s_j)|^2\,dx\).  The uniform spatial tightness proved in the temporal
five-power note gives

\[
\mathcal E(\mathbb R^3)=E_-.
\tag{17}
\]

Weak continuity of the Leray--Hopf continuation gives

\[
u(s_j)\rightharpoonup u_*
\quad\hbox{in }L^2,
\qquad
u_*:=u(T^*).
\tag{18}
\]

Convex lower semicontinuity on compactly supported tests implies

\[
\vartheta:=\mathcal E-|u_*|^2\,dx\ge0.
\tag{19}
\]

The critical-clock energy jump gives

\[
\vartheta(\mathbb R^3)
=E_--\|u_*\|_2^2
\ge d_0>0.
\tag{20}
\]

### Lemma 4: defect support

The measure \(\vartheta\) is supported on the terminal singular set

\[
\sigma
:=
\{x:(x,T^*)\text{ is a singular point of the continuation}\}.
\tag{21}
\]

#### Proof

If \(K\Subset\mathbb R^3\setminus\sigma\), finitely many regular
parabolic neighbourhoods cover \(K\times\{T^*\}\).  Local regularity in
their smaller cylinders gives strong \(L^2(K)\) convergence of
\(u(t)\) to the trace \(u_*\) as \(t\uparrow T^*\).  Hence

\[
\mathcal E\lfloor_K=|u_*|^2\,dx\lfloor_K.
\]

Exhaust the open regular set by such compact sets.

### Theorem 5: dimension pincer

Every Leray--Hopf continuation of the energy-efficient exact \(q=4\)
branch satisfies

\[
\boxed{
\frac35\le\dim_{\mathrm H}\sigma\le1,
\qquad
\mathcal H^1(\sigma)=0.
}
\tag{22}
\]

#### Proof

The temporal five-power theorem and Proposition 3 give the
Leslie--Shvydkoy concentration-dimension bound

\[
D(\mathcal E)\ge\frac35.
\tag{23}
\]

Thus \(\mathcal E(S)=0\) for every Borel set \(S\) with
\(\dim_{\mathrm H}S<3/5\).  Since \(0\le\vartheta\le\mathcal E\), the
same holds for \(\vartheta\).

If \(\dim_{\mathrm H}\sigma<3/5\), Lemma 4 would give

\[
0<\vartheta(\mathbb R^3)
=\vartheta(\sigma)=0,
\]

a contradiction.  This proves the lower bound.  Caffarelli--Kohn--Nirenberg
gives \(\mathcal H^1(\sigma)=0\), hence the upper bound.

The strict gap between \(3/5\) and \(1\) is real in the present
information.  Neither endpoint yields energy equality.

## 5. Pressure audit

For the whole-space pressure representative

\[
\pi=\mathcal R_a\mathcal R_b(u_au_b),
\]

Lorentz Calderón--Zygmund bounds and Lemma 1 give

\[
\boxed{
\pi\in
L_t^{11/4,\infty}L_x^{3/2,\infty}.
}
\tag{24}
\]

In pressure coordinates \((1/r,1/p)\), this point has

\[
\frac2r+\frac3p
=\frac8{11}+2
=2+\frac8{11}.
\tag{25}
\]

The ordinary energy class yields the pressure line

\[
\frac2r+\frac3p=3.
\tag{26}
\]

Every direct interpolation between (24) and (26) therefore satisfies

\[
\frac2r+\frac3p
=2+\gamma,
\qquad
\gamma\ge\frac8{11}.
\tag{27}
\]

Barker and Wang's peer-reviewed supercritical theorem assumes
\(0<\gamma<1/2\) and

\[
\delta>\frac{3\gamma}{2+2\gamma},
\tag{28}
\]

then concludes \(\mathcal H^{2\delta}(\sigma)=0\), subject to its further
parameter conditions.  Equation (27) is already outside its theorem.

Moreover, entering the dimension-closing range \(2\delta<3/5\) would
require, even before the further conditions,

\[
\frac{3\gamma}{1+\gamma}<\frac35
\quad\Longleftrightarrow\quad
\gamma<\frac14.
\tag{29}
\]

Thus the direct pressure hull misses this necessary closing range by

\[
\boxed{\frac8{11}-\frac14=\frac{21}{44}.}
\tag{30}
\]

This is a norm-interpolation no-go, not a theorem that pressure
cancellation, oscillation, or another structural estimate cannot supply
the missing gain.

## 6. Clock-band correlation or super-clock escape

Retain the sequence \(s_j\), the terminal trace \(u_*\), and the clock
frequencies

\[
\Lambda_j\asymp m_j^{7/3}j^{2/3}.
\tag{31}
\]

Set

\[
w_j:=u(s_j)-u_*.
\tag{32}
\]

Then \(w_j\rightharpoonup0\) in \(L^2\), and the critical-clock high-pass
floor, together with the vanishing high-frequency tail of \(u_*\), gives

\[
\|\Pi_{>\Lambda_j}w_j\|_2\ge d_1>0
\tag{33}
\]

after harmless fixed changes of the cutoff.  Here \(\Pi\) denotes the
sharp orthogonal Fourier projection; it dominates the smooth high-pass
multiplier used in the critical-clock theorem.

### Theorem 6: exhaustive spectral alternative

At least one of the following alternatives holds; they are not asserted to
be mutually exclusive.  If Alternative A fails, Alternative B holds.

#### A. Bounded clock band

There are fixed \(A>1\) and \(\eta>0\) such that, on an infinite
subsequence,

\[
\left\|
\Pi_{\Lambda_j<|\xi|\le A\Lambda_j}w_j
\right\|_2^2
\ge\eta.
\tag{34}
\]

There is a further subsequence \(j_k\) and band-limited divergence-free
tests

\[
g_k
:=
\Pi_{\Lambda_{j_k}<|\xi|\le A\Lambda_{j_k}}w_{j_k}
\tag{35}
\]

such that the disjoint intervals
\(I_k=[s_{j_k},s_{j_{k+1}}]\) obey

\[
\boxed{
\int_{I_k}\!\!\int_{\mathbb R^3}
u\otimes u:\nabla g_k\,dx\,dt
\le-\frac{\eta}{4}
}
\tag{36}
\]

for all sufficiently large \(k\).  Meanwhile,

\[
\left|
\nu\int_{I_k}\!\!\int
\nabla u:\nabla g_k\,dx\,dt
\right|\longrightarrow0.
\tag{37}
\]

#### B. Super-clock escape

There are \(A_k\to\infty\) and a subsequence \(j_k\) such that

\[
\left\|
\Pi_{>A_k\Lambda_{j_k}}u(s_{j_k})
\right\|_2
\ge\eta_0>0.
\tag{38}
\]

Consequently,

\[
\boxed{
\|\nabla u(s_{j_k})\|_2^2
\gtrsim
A_k^2\Lambda_{j_k}^2.
}
\tag{39}
\]

#### Proof

If (34) holds for some \(A,\eta\) on an infinite set, define \(g_j\) by
(35).  For each fixed \(g_j\), weak convergence \(w_n\rightharpoonup0\)
allows the next index to be chosen so far out that

\[
|\langle w_{j_{k+1}},g_k\rangle|
\le\frac{\eta}{4}.
\]

Since \(g_k\) is an orthogonal projection of \(w_{j_k}\),

\[
\begin{aligned}
\langle
u(s_{j_{k+1}})-u(s_{j_k}),g_k
\rangle
&=
\langle w_{j_{k+1}},g_k\rangle-\|g_k\|_2^2\\
&\le-\frac{3\eta}{4}.
\end{aligned}
\tag{40}
\]

Pairing the smooth equation on \(I_k\) with the fixed \(g_k\) gives

\[
\begin{aligned}
\langle u(s_{j_{k+1}})-u(s_{j_k}),g_k\rangle
={}&
\int_{I_k}\!\!\int u\otimes u:\nabla g_k\\
&-
\nu\int_{I_k}\!\!\int\nabla u:\nabla g_k.
\end{aligned}
\tag{41}
\]

The exact record tail has the two bounds

\[
T^*-s_j\lesssim\frac{m_j^{-11/2}}j,
\qquad
\int_{s_j}^{T^*}M(t)^2\,dt
\lesssim\frac{m_j^{-7/2}}j.
\tag{42}
\]

Band-limited Lorentz Bernstein gives

\[
\|\nabla g_k\|_{L^{3,1}}
\lesssim
(A\Lambda_{j_k})^{3/2}\|g_k\|_2.
\tag{43}
\]

Thus the total nonlinear capacity of the whole terminal tail is

\[
\begin{aligned}
\int_{s_j}^{T^*}
\left|\int u\otimes u:\nabla g_j\right|dt
&\lesssim
(A\Lambda_j)^{3/2}
\int_{s_j}^{T^*}M(t)^2dt\\
&\lesssim A^{3/2},
\end{aligned}
\tag{44}
\]

because
\(\Lambda_j^{3/2}\asymp m_j^{7/2}j\).
This is order one, not summable.

Put

\[
D_j^\nu
:=
\nu\int_{s_j}^{T^*}\|\nabla u(t)\|_2^2\,dt
\longrightarrow0.
\]

Cauchy--Schwarz, (42), and
\(\|\nabla g_j\|_2\le A\Lambda_j\|g_j\|_2\) give

\[
\begin{aligned}
\left|
\nu\int_{s_j}^{T^*}\!\!\int\nabla u:\nabla g_j
\right|
&\lesssim
A\Lambda_j(T^*-s_j)^{1/2}(D_j^\nu)^{1/2}\\
&\lesssim
A\,m_j^{-5/12}j^{1/6}(D_j^\nu)^{1/2}
\longrightarrow0.
\end{aligned}
\tag{45}
\]

Equations (40)--(45) prove (36)--(37).

If Alternative A fails, then for every fixed \(A>1\),

\[
\left\|
\Pi_{\Lambda_j<|\xi|\le A\Lambda_j}w_j
\right\|_2\longrightarrow0.
\tag{46}
\]

Combine (46) with (33), choose \(A_k\to\infty\) diagonally, and obtain

\[
\|\Pi_{>A_k\Lambda_{j_k}}w_{j_k}\|_2\ge d_1/2.
\]

Since \(A_k\Lambda_{j_k}\to\infty\),

\[
\|\Pi_{>A_k\Lambda_{j_k}}u_*\|_2\to0.
\]

This proves (38); Plancherel proves (39).

## 7. Exact frontier

### Robust findings, subject to external review

1. The exact clock reaches weak \(L_t^{11/2}\), with a logarithmic
   Lorentz improvement, but not strong \(L_t^{11/2}\) by the present
   estimate.
2. Direct interpolation misses every relevant Cheskidov--Luo Besov
   threshold, even under the additional favourable surrogate assumption
   \(L_t^{11/2,\infty}B^0_{3,\infty}\).
3. The entire Leslie--Shvydkoy mixed-norm hull has sharp ceiling \(3/5\).
4. A nonzero q4 terminal energy defect forces
   \(3/5\le\dim_{\mathrm H}\sigma\le1\).
5. Direct pressure interpolation has \(\gamma\ge8/11\); the
   Barker--Wang pincer-closing region requires at least
   \(\gamma<1/4\).
6. At least one spectral alternative holds: the terminal defect pays
   infinitely many fixed-sign nonlinear clock-band correlations, while
   failure of that alternative forces escape to super-clock frequencies.

### Things still to prove

1. Sum or cancel the event-dependent nonlinear works in (36) against one
   finite same-trajectory budget.  A transported adjoint or a genuine
   square-function estimate would do this.
2. In Alternative B, turn the amplified pointwise enstrophy (39) into
   positive residence or dissipation.
3. Derive structural pressure cancellation or oscillation sufficient to
   cross the \(21/44\) direct-interpolation deficit.
4. Prove energy equality or strong left \(L^2\) continuity at \(T^*\).
5. Control the divergent-normalised-energy branch and clocks at or below
   the five-power barrier.
6. Prove one complete Clay alternative for arbitrary admissible data.

### Conjecture: the dimension pincer is empty for first singularities

No first singular time arising from smooth finite-energy data supports a
nonzero anomalous energy defect on a terminal singular set of Hausdorff
dimension in \([3/5,1]\).

The present theorem proves that every energy-efficient exact \(q=4\)
survivor would have precisely such a defect.  It does not prove the
conjecture.  The Clay problem remains unsolved.
