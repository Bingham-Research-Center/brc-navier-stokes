# A fixed parabolic frequency block has factorial Oseen depth

- **Experiment:** EXP-ADJOINT-PRESSURE-FREQUENCY-COLLIGATION-001
- **Route:** ROUTE-R3B
- **Status:** independently reviewed proof-level fixed-band theorem and
  exact Fourier counter-audit
- **Domain:** \(\mathbb R^3\) for the fixed-band theorem;
  \(\mathbb T^3\) for the integer-frequency geometry
- **Clay status:** unsolved
- **Input:** the independently reviewed
  [skew-compression theorem](adjoint-pressure-skew-compression.md)
- **Review:** [accepted after two scope precisions](../review-response-adjoint-pressure-frequency-colligation-2026-07-24.md)

The preceding theorem showed that abstract skew transport, Hodge
orthogonality, real-coupling stability, prescribed algebraic zero trace,
and a squared leakage telescope do not sum the linear adjoint-pressure
cost.  This note restores two pieces that the abstract model omitted:
the actual differentiated heat propagator and the scale-critical
weak-\(L^3\) multiplication law.

The result is a positive but sharply bounded advance.

> If every intermediate Oseen interaction is projected back to one
> dyadic annulus of frequency \(R\), its Dyson iterates and its
> band-resolved linear \(L^1_x\) pressure observations have a factorial
> tail on a parabolic window \(T\lesssim(\nu R^2)^{-1}\).

Thus a pressure packet surviving to unbounded interaction depth cannot
remain in one comparable-frequency block.  It must use an unbounded
multiscale frequency itinerary, or structure lost when the full pressure
is decomposed into bands.  This is not yet a summation of those
itineraries and does not prove regularity.

## 1. Band-restricted Oseen and pressure operators

Fix a smooth annular Fourier multiplier

\[
\Delta_R f
=
\mathcal F^{-1}
\left[
\chi\left(\frac{\xi}{R}\right)\widehat f(\xi)
\right],
\qquad
\operatorname{supp}\chi
\subset
\{c_\chi\le|\xi|\le C_\chi\},
\tag{1}
\]

where \(R>0\).  Let \(b\) be divergence-free and satisfy

\[
\sup_{0<s<T}\|b(s)\|_{L^{3,\infty}(\mathbb R^3)}
\le M.
\tag{2}
\]

On vector fields \(z\) whose Fourier support lies in the annulus in
(1), define the all-stay-in-band Oseen block

\[
(\mathcal V_{R,b}z)(t)
:=
\int_0^t
\Delta_R e^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}
\bigl(z\otimes b\bigr)(s)\,ds,
\tag{3}
\]

and its band-resolved pressure observation

\[
\mathcal C_{R,b}z(t)
:=
\Delta_R\mathbb Q\operatorname{div}
\bigl(z\otimes b\bigr)(t),
\qquad
\mathbb Q:=I-\mathbb P.
\tag{4}
\]

The tensor convention is
\(((z\otimes b)_{ik}=z_i b_k)\), so

\[
\operatorname{div}(z\otimes b)=b\cdot\nabla z
\tag{5}
\]

when \(\nabla\cdot b=0\).  Equation (4) is therefore precisely the
frequency-\(R\) part of the reviewed pressure operator
\(\mathbb Q(b\cdot\nabla z)\).

## 2. Fixed-band factorial theorem

### Theorem

There is a constant \(K_\chi\ge1\), depending only on the fixed
multiplier and Fourier normalisation, such that, for

\[
q_R=\Delta_Rq,
\qquad
Q_T:=\sup_{0<t<T}\|q_R(t)\|_{L^1}<\infty,
\tag{6}
\]

and

\[
u_0:=q_R,
\qquad
u_m:=\mathcal V_{R,b}^{\,m}q_R
\quad(m\ge1),
\tag{7}
\]

one has

\[
\boxed{
\|u_m(t)\|_{L^1}
\le
Q_T\frac{(K_\chi M R^2t)^m}{m!}
\qquad(0<t<T).
}
\tag{8}
\]

Moreover,

\[
\boxed{
\int_0^T
\|\mathcal C_{R,b}u_m(t)\|_{L^1}\,dt
\le
Q_T
\frac{(K_\chi M R^2T)^{m+1}}{(m+1)!}.
}
\tag{9}
\]

Consequently, if

\[
T\le\frac{\Lambda}{\nu R^2},
\tag{10}
\]

then the complete pressure-depth series is bounded by

\[
\boxed{
\sum_{m=0}^{\infty}
\int_0^T
\|\mathcal C_{R,b}u_m(t)\|_1\,dt
\le
Q_T
\left[
\exp\left(\frac{K_\chi M\Lambda}{\nu}\right)-1
\right],
}
\tag{11}
\]

and its tail tends to zero factorially, uniformly in \(R\).

### Proof

The annular differentiated heat multiplier has an integrable kernel with

\[
\left\|
\Delta_Re^{\nu\tau\Delta}
\mathbb P\operatorname{div}F
\right\|_{L^1}
\le
K_\chi R
e^{-c_\chi\nu R^2\tau}
\|F\|_{L^1}.
\tag{12}
\]

The corresponding annular pressure multiplier obeys

\[
\left\|
\Delta_R\mathbb Q\operatorname{div}F
\right\|_{L^1}
\le
K_\chi R\|F\|_{L^1}.
\tag{13}
\]

Both statements follow by scaling the smooth annular multiplier kernels;
the apparent singularity of \(\mathbb P\) and \(\mathbb Q\) is absent
away from frequency zero.

Lorentz Hölder and annular Lorentz--Bernstein give

\[
\begin{aligned}
\|z\otimes b\|_{L^1}
&\le
C
\|z\|_{L^{3/2,1}}
\|b\|_{L^{3,\infty}},
\\
\|z\|_{L^{3/2,1}}
&\le
C_\chi R\|z\|_{L^1}.
\end{aligned}
\tag{14}
\]

After enlarging \(K_\chi\), (12)--(14) imply

\[
\|\mathcal V_{R,b}z(t)\|_1
\le
K_\chi MR^2
\int_0^t\|z(s)\|_1\,ds
\tag{15}
\]

and

\[
\|\mathcal C_{R,b}z(t)\|_1
\le
K_\chi MR^2\|z(t)\|_1.
\tag{16}
\]

Induction in the ordered time simplex gives

\[
\|u_m(t)\|_1
\le
Q_T(K_\chi MR^2)^m
\int_{0<s_1<\cdots<s_m<t}
ds_1\cdots ds_m,
\tag{17}
\]

which is (8).  Applying (16) and integrating (8) in time gives
(9).  Summing the exponential series and using (10) proves (11).
\(\square\)

### Exact tail form

Put

\[
a:=K_\chi MR^2T.
\tag{18}
\]

The depth-\(m\) pressure term in (9) is \(Q_Ta^{m+1}/(m+1)!\).  If
\(a<N+2\), then

\[
\boxed{
\sum_{m=N}^{\infty}
Q_T\frac{a^{m+1}}{(m+1)!}
\le
Q_T\frac{a^{N+1}}{(N+1)!}
\frac{N+2}{N+2-a}.
}
\tag{19}
\]

This rational majorant is what the executable certificate checks.

### Logarithmic-depth consequence

The reviewed feedback theorem reaches the depth

\[
N(h)
=
\left\lfloor c_{\rm dep}\log\frac1h\right\rfloor.
\tag{19a}
\]

Suppose a selected band \(R_h\) satisfies

\[
\nu R_h^2h\le\Lambda,
\qquad
Q_h:=\sup_{0<t<h}\|q_{R_h}(t)\|_1
\le Ch^{-A}
\tag{19b}
\]

for fixed \(A,\Lambda<\infty\).  Then (19) and the elementary exponential
tail bound give

\[
\sum_{m=N(h)}^\infty
\int_0^h
\|\mathcal C_{R_h,b}
\mathcal V_{R_h,b}^{\,m}q_{R_h}(t)\|_1\,dt
\le
Q_h e^a\frac{a^{N(h)+1}}{(N(h)+1)!},
\qquad
a:=\frac{K_\chi M\Lambda}{\nu}.
\tag{19c}
\]

Stirling's inequality yields

\[
\log\left(
h^{-A}e^a\frac{a^{N(h)+1}}{(N(h)+1)!}
\right)
\le
-c_{\rm dep}\log\frac1h
\log\log\frac1h
+O\left(\log\frac1h\right),
\tag{19d}
\]

whose dominant term is
\(-c_{\rm dep}\log(1/h)\log\log(1/h)\).  Thus (19c) tends to
zero despite any fixed polynomial growth of the input \(L^1\) bound.
The logarithmically deep pressure packet cannot be carried by the
all-stay-in-one-band block.

## 3. Exact plane-wave colligation

The factorial theorem is consistent with a sharper geometric fact for a
single Fourier shift.

Let

\[
b(x)=\beta e^{ik\cdot x},
\qquad
k\cdot\beta=0,
\qquad
k\times\xi_0\ne0,
\tag{20}
\]

and let the input be
\(z_0(x)=a_0e^{i\xi_0\cdot x}\), with
\(\xi_0\cdot a_0=0\).  Put

\[
\xi_j:=\xi_0+jk.
\tag{21}
\]

The non-collinearity in (20) ensures that every \(\xi_j\) is nonzero
and that the common frequency plane is genuinely two-dimensional.

Because \(\beta\cdot k=0\), the scalar transport factor is constant:

\[
\beta\cdot\xi_j=\beta\cdot\xi_0.
\tag{22}
\]

After factoring out this scalar, the projected and pressure parts of one
step are exactly

\[
a\longmapsto P_{\xi_{j+1}}a,
\qquad
a\longmapsto Q_{\xi_{j+1}}a.
\tag{23}
\]

All \(\xi_j\) lie in the plane spanned by \(\xi_0\) and \(k\).  Its
normal component is preserved and never leaks to pressure.  On the
remaining one-dimensional solenoidal polarisation, let
\(\delta_j\) be the angle from \(\xi_{j-1}\) to \(\xi_j\).  The
depth-\(m\) pressure leakage is

\[
\ell_m
=
|a_0^\parallel|
\left(\prod_{j=1}^{m}|\cos\delta_j|\right)
|\sin\delta_{m+1}|.
\tag{24}
\]

Along the one-sided affine ray \(\xi_0+jk\), the direction turns
monotonically through an angle strictly below \(\pi\).  Hence

\[
\boxed{
\sum_{m=0}^{\infty}\ell_m
\le
|a_0^\parallel|
\sum_{j=1}^{\infty}|\delta_j|
<
\pi|a_0^\parallel|.
}
\tag{25}
\]

Any scalar heat weights in \([0,1]\) can only decrease the left-hand
side.  Thus one unidirectional Fourier ray already has the desired
linear, not merely squared, Hodge-leakage summability.

The drift in (20) is complex.  A real drift contains both \(+k\) and
\(-k\), so frequency paths may backtrack.  The next exact audit shows
why monotone ray geometry alone cannot treat that branching.

## 4. An integer-frequency backtracking audit

For an integer \(n\ge3\), set

\[
\begin{aligned}
\xi_-&=(n^2-1,-2n,0),\\
\xi_+&=(n^2-1, 2n,0),\\
k&=(0,4n,0),\\
R_n&=|\xi_-|=|\xi_+|=n^2+1.
\end{aligned}
\tag{26}
\]

Take the drift polarisation \(\beta=e_1\), so
\(\beta\cdot k=0\) and

\[
\beta\cdot\xi_-=\beta\cdot\xi_+=n^2-1.
\tag{27}
\]

Let \(\delta_n\) be the angle between \(\xi_-\) and \(\xi_+\).
The exact rational values are

\[
\boxed{
c_n:=\cos\delta_n
=
\frac{n^4-6n^2+1}{(n^2+1)^2},
\qquad
s_n:=\sin\delta_n
=
\frac{4n(n^2-1)}{(n^2+1)^2}.
}
\tag{28}
\]

They satisfy \(c_n^2+s_n^2=1\) and are positive for \(n\ge3\).
If a normalised frequency path alternates forever between
\(\xi_-\) and \(\xi_+\), its linear leakage is

\[
\boxed{
\sum_{m=0}^{\infty}s_nc_n^m
=
\frac{s_n}{1-c_n}
=
\frac{n^2-1}{2n}
\longrightarrow\infty.
}
\tag{29}
\]

Even insert the exact heat multiplier \(h_n=c_n\) after every completed
projected interaction.  The continued amplitude then has ratio
\(c_n^2\).  The current pressure observation precedes the next heat
propagation, so

\[
\boxed{
\sum_{m=0}^{\infty}
s_n(c_n^2)^m
=
\frac{1}{s_n}
\sim\frac n4.
}
\tag{30}
\]

This apparent obstruction occupies only a parabolic effective time.
Indeed, for viscosity one choose

\[
\Delta t_n:=\frac{-\log c_n}{R_n^2}.
\tag{31}
\]

Then

\[
\boxed{
R_n^2
\frac{\Delta t_n}{1-c_n^2}
=
\frac{-\log c_n}{1-c_n^2}
\longrightarrow\frac12.
}
\tag{32}
\]

Equations (30)--(32) do **not** contradict the fixed-band theorem.
They silently assign unit transport action to every microstep.  For a
constant pulse of drift amplitude \(B_n\), the exact viscosity-one
Duhamel action on the target mode is

\[
\lambda_n
=
B_n(n^2-1)
\int_0^{\Delta t_n}e^{-R_n^2s}\,ds
=
B_n(n^2-1)\frac{1-c_n}{R_n^2}.
\tag{33}
\]

For \(\lambda_n=1\),

\[
\boxed{
\frac{B_n}{R_n}
=
\frac{R_n}
{(n^2-1)(1-c_n)}
\sim\frac{n^2}{8},
}
\tag{34}
\]

which is supercritical.  By contrast, a scale-critical packet amplitude
\(B_n=MR_n\) gives

\[
\boxed{
\lambda_n
=
M\frac{n^2-1}{n^2+1}(1-c_n)
\sim\frac{8M}{n^2}.
}
\tag{35}
\]

The freely normalised backtracking series therefore omits exactly the
coefficient-time action restored in (15).  This is the discrete
plane-wave shadow of the factorial theorem.

The exact frequency geometry in (26)--(32) lives on the torus.  A global
torus plane wave of amplitude \(B_n\) has
\(\|b\|_{L^{3,\infty}}\asymp B_n\); consequently \(B_n=MR_n\) is not a
uniform weak-\(L^3\) torus family.  Equations (34)--(35) are instead the
dimensional audit for a spatially localised scale-\(R_n\) packet on
\(\mathbb R^3\).  They do not construct an exact weak-\(L^3\)-bounded
Fourier Oseen or Navier--Stokes trajectory.

## 5. Consequence and open boundary

The result closes the following proposed escape:

> A pressure-bearing critical Dyson remainder can stay for unbounded
> depth inside one comparable-frequency annulus merely by repeatedly
> backtracking through small Leray angles.

It cannot: once the actual weak-\(L^3\) coefficient-time action is
included, the all-stay-in-band block has the factorial tail (9).

What remains is genuinely multiscale.  Insert a Littlewood--Paley
partition after every Oseen interaction.  The full remainder becomes a
sum over frequency itineraries

\[
R_0\to R_1\to\cdots\to R_m.
\tag{36}
\]

This note controls only the paths trapped in one comparable block.  It
does not yet:

1. sum paths making arbitrarily many dyadic scale changes;
2. control the \(L^1\) recombination of all pressure bands;
3. exploit or prove a same-trajectory Navier--Stokes frequency law; or
4. couple a frequency itinerary to the physical event ancestry.

The next live theorem is therefore a multiscale frequency-path estimate:
either show that long paths pay a summable scale-change charge, or extract
an actual one-trajectory frequency ancestry whose repeated scale escape
contradicts the existing energy, weak-\(L^3\), or event ledger.

## Reproduce

```bash
make adjoint-pressure-frequency-colligation
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_frequency_colligation -v
```
