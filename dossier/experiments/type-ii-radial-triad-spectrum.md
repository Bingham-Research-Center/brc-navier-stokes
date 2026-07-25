# The q4 flux is a characteristic derivative of positive spectral energy

- **Experiment:** EXP-TYPE-II-RADIAL-TRIAD-SPECTRUM-001
- **Route:** ROUTE-R3C
- **Status:** complete conditional reduction and sharp kinematic countermodel;
  external review pending
- **Domains:** \(\mathbb R^3\) for the conditional entrance and spectral
  measure; \(\mathbb T^3\) for the exact triad certificate
- **Clay status:** unsolved
- **Inputs:** [diagonal Gaussian flux](type-ii-diagonal-heat-flux-recycling.md),
  [triad-packet sharpness](type-ii-triad-packet-sharpness.md)

## Verdict

The diagonal flux has an exact signed radial spectrum.  With the unitary
Fourier transform, put

\[
F(s):=\mathbb P((U\cdot\nabla)v)(s)
\tag{1}
\]

and push the two Fourier measures forward by

\[
\lambda=2\nu|\xi|^2:
\tag{2}
\]

\[
\boxed{
\begin{aligned}
\varepsilon_s(B)
&:=
\frac12\int_{\{2\nu|\xi|^2\in B\}}
|\widehat v(s,\xi)|^2\,d\xi,\\
\mu_s(B)
&:=
-\operatorname{Re}
\int_{\{2\nu|\xi|^2\in B\}}
\widehat F(s,\xi)\cdot
\overline{\widehat v(s,\xi)}\,d\xi.
\end{aligned}
}
\tag{3}
\]

Then

\[
\boxed{
\mathcal E(r,s)
:=
\frac12\|e^{\nu r\Delta}v(s)\|_2^2
=
\int_0^\infty e^{-r\lambda}\,d\varepsilon_s(\lambda),
}
\tag{4}
\]

\[
\boxed{
\Pi_r(s)
=
\int_0^\infty e^{-r\lambda}\,d\mu_s(\lambda).
}
\tag{5}
\]

The nonlinear measure is not independent of the positive energy measure:

\[
\boxed{
\Pi_r(s)
=
(\partial_s-\partial_r)\mathcal E(r,s),
\qquad
\mu_s
=
\partial_s\varepsilon_s+\lambda\varepsilon_s.
}
\tag{6}
\]

The second equality is distributional in \(s\) and \(\lambda\).
For every fixed \(s>0\), \(\mathcal E(\cdot,s)\) is completely monotone:

\[
\boxed{
(-1)^k\partial_r^k\mathcal E(r,s)
=
\int_0^\infty
\lambda^ke^{-r\lambda}\,d\varepsilon_s(\lambda)
\ge0.
}
\tag{7}
\]

The weak-zero heat boundary gives the exact characteristic reconstruction

\[
\boxed{
\mathcal E(r,s)
=
\int_0^s
\Pi_{r+s-a}(a)\,da.
}
\tag{8}
\]

This extra positivity corrects the preceding scalar stress test.  The
constant-energy Laguerre flux reconstructs

\[
\mathcal E_n(r,s)
=
\frac d2
\left[
1-\left(\frac r{r+s}\right)^{n+1}
\right].
\tag{9}
\]

Its inverse Laplace density is

\[
\frac d2\,s e^{-s\lambda}L_n^{(1)}(s\lambda),
\tag{10}
\]

which changes sign for every \(n\ge1\).  Thus (9) is not completely
monotone and is not a kinetic-energy spectrum.  The slowly varying
energy factor in the preceding full survivor does not repair this
boundary-scale sign defect.  That particular survivor is closed.

Complete monotonicity does not close q4.  Let

\[
\ell(s):=\log(e/s),
\qquad
L(s):=s^{-9/11}\ell(s)^{2/11},
\tag{11}
\]

\[
A(s):=\frac d2
\exp\left(-\int_0^sL(a)\,da\right),
\qquad
\mathcal E_\circ(r,s):=A(s)e^{-rL(s)}.
\tag{12}
\]

This is the positive energy spectrum of one ideal radial shell.  It has
the exact energy law

\[
A'(s)=-L(s)A(s)
\tag{13}
\]

and exact characteristic flux

\[
\boxed{
\Pi^\circ_r(s)
=
-A(s)rL'(s)e^{-rL(s)}
=
\frac{A(s)a(s)}s
\bigl(rL(s)\bigr)e^{-rL(s)}>0,
}
\tag{14}
\]

where

\[
a(s):=-\frac{sL'(s)}{L(s)}
=
\frac9{11}+\frac{2}{11\ell(s)}.
\tag{15}
\]

Define its q4 ledgers by

\[
Y_\circ(s)^2:=\frac{A(s)L(s)}{\nu},
\qquad
M_\circ(s):=\frac1{sL(s)}.
\tag{16}
\]

Then

\[
M_\circ
=s^{-2/11}\ell^{-2/11},
\qquad
Y_\circ^2
\asymp s^{-9/11}\ell^{2/11},
\qquad
M_\circ Y_\circ^2
=\frac{A(s)}{\nu s}.
\tag{17}
\]

Thus the positive shell model satisfies the exact q4 \(M^2\) tail,
dissipation tail, divergent \(MY^2\) budget, pointwise heat estimate,
Gaussian variation budget, diagonal energy identity, and recycling law.
For every fixed \(0<q<1\),

\[
\boxed{
\frac{
\int_0^{q\tau}\Pi^\circ_{\tau-s}(s)\,ds
}{
\int_0^\tau\Pi^\circ_{\tau-s}(s)\,ds
}
\longrightarrow1
\qquad(\tau\downarrow0).
}
\tag{18}
\]

The dominant source time solves

\[
\tau L(s_\tau)\asymp1,
\qquad
\frac{s_\tau}{\tau}\longrightarrow0.
\tag{19}
\]

This is an exact positive-energy, heat-spectral, q4-compatible reuse
countermodel.  Its moving delta shell has a distributional transfer
density and is not yet an NSE field.

The missing instantaneous quadratic shape is also locally admissible.
For every positive Pell solution

\[
n^2-3m^2=1,
\tag{20}
\]

the explicit divergence-free torus field

\[
\boxed{
\begin{aligned}
W_{n,m}(x,y,z)
:={}&
\bigl(
-m\sin(nx+my),\,
n\sin(nx+my),\\
&\qquad
\sin(2my)+\sin(nx-my)
\bigr)
\end{aligned}
}
\tag{21}
\]

has, for every radial multiplier with shell values \(\eta_j\),

\[
\boxed{
\fint_{\mathbb T^3}
W_{n,m}\otimes W_{n,m}:
\nabla(MW_{n,m})\,dx
=
\frac{nm}{2}
\bigl(\eta_{4m^2}-\eta_{4m^2+1}\bigr).
}
\tag{22}
\]

For \(M=e^{2\nu r\Delta}\), its actual self-interaction flux is

\[
\boxed{
Q_{n,m}(r)
=
\frac{nm}{2}
e^{-8\nu m^2r}
\left(1-e^{-2\nu r}\right)>0
\qquad(r>0).
}
\tag{23}
\]

Along the Pell sequence \(n/m\to\sqrt3\),

\[
\boxed{
Q_{n,m}\left(\frac{x}{8\nu m^2}\right)
\longrightarrow
\frac{\sqrt3}{8}xe^{-x}
}
\tag{24}
\]

locally uniformly for \(x\ge0\).  This is exactly the heat-age shape in
(14).  Hence incompressibility, endpoint cancellation, adjacent radial
shells, pressure projection, positivity for every heat age, and the
shell-derivative profile are all compatible with exact quadratic triads.

Equations (6)--(24) leave one sharper gate:

> Can the adjacent-shell triadic transfer (22) be dynamically identified
> with \(\partial_s\varepsilon_s+\lambda\varepsilon_s\) for an infinite
> q4 shell descent on one finite-energy NSE trajectory?

The shell model does not supply a velocity, while the Pell fields are
snapshots rather than one evolution.  No such dynamic identification or
exclusion is proved.  No Clay alternative is proved.

## 1. The actual radial spectral density

Use the unitary convention

\[
\widehat f(\xi)
:=
(2\pi)^{-3/2}
\int_{\mathbb R^3}e^{-ix\cdot\xi}f(x)\,dx.
\tag{25}
\]

At a positive smooth time, (3) is first read for rapidly decaying data;
the energy-space statement follows by the usual truncation and duality
limit.  Polar coordinates give the density

\[
\boxed{
\begin{aligned}
\frac{d\mu_s}{d\lambda}(\lambda)
=
-\frac1{4\nu}
\sqrt{\frac{\lambda}{2\nu}}\,
\operatorname{Re}
\int_{\mathbb S^2}
&\widehat F
\left(s,\sqrt{\frac{\lambda}{2\nu}}\omega\right)\\
&\cdot
\overline{
\widehat v
\left(s,\sqrt{\frac{\lambda}{2\nu}}\omega\right)}
\,d\omega .
\end{aligned}
}
\tag{26}
\]

This is signed.  Its total mass is

\[
\mu_s([0,\infty))
=-\langle F(s),v(s)\rangle
=0
\tag{27}
\]

by transport cancellation.

### Proposition 1: exact quadratic triad density

Put \(c_0=(2\pi)^{-3/2}\).  Before radial pushforward, the density in
(3) is

\[
\boxed{
\begin{aligned}
-\operatorname{Re}
\bigl(
\widehat F(s,\xi)\cdot
\overline{\widehat v(s,\xi)}
\bigr)
=c_0\operatorname{Im}\int_{\mathbb R^3}
&\bigl((\xi-\eta)\cdot\widehat U(s,\eta)\bigr)\\
&\times
\bigl(
\widehat v(s,\xi-\eta)\cdot
\overline{\widehat v(s,\xi)}
\bigr)\,d\eta .
\end{aligned}
}
\tag{28}
\]

#### Proof

Fourier transformation gives

\[
\widehat F_i(\xi)
=
ic_0P_{i\ell}(\xi)
\int_{\mathbb R^3}
(\xi-\eta)_j
\widehat U_j(\eta)
\widehat v_\ell(\xi-\eta)\,d\eta.
\tag{29}
\]

Since \(\widehat v(\xi)\perp\xi\), the Leray projector disappears when
(29) is paired with \(\overline{\widehat v(\xi)}\).  Finally
\(-\operatorname{Re}(iz)=\operatorname{Im}z\), proving (28).

### Interpretation

Pressure supplies no additional radial sign.  Every output shell receives
a sum of genuine Fourier triads.  Energy conservation imposes only (27);
higher radial moments are nonlinear enstrophy and derivative transfers
and have no universal three-dimensional sign.

The drift split gives

\[
\mu_s=\mu_s^{v}+\mu_s^{c}.
\tag{30}
\]

Both summands have total mass zero because \(v\) and \(c\) are
divergence-free.  Strong \(L^2\) convergence of \(c\) supplies no
clock-relative rate for their higher moments.

## 2. Positive heat energy and characteristics

### Theorem 2: spectral characteristic law

Equations (4)--(8) hold.

#### Proof

The first identity in (4) follows from self-adjointness and the semigroup
law:

\[
\frac12\langle v,S(2r)v\rangle
=
\frac12\|S(r)v\|_2^2.
\]

Plancherel and the pushforward definition of \(\varepsilon_s\) give the
second.  Equation (5) follows in the same way from the definition of
\(\Pi\) and \(\mu_s\).

Differentiating (4) in heat age gives

\[
\partial_r\mathcal E(r,s)
=
-\nu\|\nabla S(r)v(s)\|_2^2.
\tag{31}
\]

The entrance equation \(v_s=\nu\Delta v-F\) gives

\[
\begin{aligned}
\partial_s\mathcal E(r,s)
&=
\langle\nu\Delta v-F,S(2r)v\rangle\\
&=
-\nu\|\nabla S(r)v\|_2^2+\Pi_r(s).
\end{aligned}
\tag{32}
\]

Subtract (31) from (32) to obtain the first identity in (6).
Taking inverse Laplace transforms gives the second.

Repeated differentiation of (4) proves (7).  Finally, follow the
characteristic

\[
(r(a),a)=(r+s-a,a),
\qquad 0\le a\le s.
\]

Along it,

\[
\frac d{da}\mathcal E(r+s-a,a)
=
\Pi_{r+s-a}(a).
\]

The fixed-heat boundary theorem gives
\(\mathcal E(r+s,0)=0\).  Integration proves (8).

### Corollary 3: complete-monotonicity audit of a proposed flux

Any proposed diagonal flux kernel must reconstruct through (8) to a
completely monotone function of \(r\) at every \(s>0\).  Endpoint
cancellation and a signed Laplace representation of the flux alone are
not sufficient.

## 3. The former Laguerre survivor fails the audit

Freeze the limiting energy at \(d\) and consider

\[
\widetilde\Pi_n(r,s)
:=
\frac{(n+1)d}{2}
\frac{r^n}{(r+s)^{n+1}},
\qquad n\ge1.
\tag{33}
\]

### Proposition 4: sign-changing reconstructed energy spectrum

The characteristic reconstruction of (33) is (9), and its inverse
Laplace density is (10).  It is not nonnegative for any \(n\ge1\).

#### Proof

Since the two arguments of \(\widetilde\Pi_n\) sum to \(r+s\) along the
characteristic,

\[
\begin{aligned}
\int_0^s
\widetilde\Pi_n(r+s-a,a)\,da
&=
\frac{(n+1)d}{2(r+s)^{n+1}}
\int_0^s(r+s-a)^n\,da\\
&=
\frac d2
\left[
1-\left(\frac r{r+s}\right)^{n+1}
\right].
\end{aligned}
\]

Expanding the bracket gives

\[
\mathcal E_n(r,s)
=
\frac d2
\sum_{k=1}^{n+1}
(-1)^{k+1}
\binom{n+1}{k}
\frac{s^k}{(r+s)^k}.
\tag{34}
\]

Since

\[
\frac1{(r+s)^k}
=
\frac1{(k-1)!}
\int_0^\infty
\lambda^{k-1}e^{-(r+s)\lambda}\,d\lambda,
\]

the inverse density is

\[
\frac d2\,s e^{-s\lambda}
\sum_{j=0}^n
(-1)^j
\binom{n+1}{j+1}
\frac{(s\lambda)^j}{j!}
=
\frac d2\,s e^{-s\lambda}L_n^{(1)}(s\lambda).
\]

The generalized Laguerre polynomial \(L_n^{(1)}\) has \(n\) positive
simple roots and changes sign.  Bernstein's theorem therefore excludes
complete monotonicity.

For the full preceding factor \(E_\sharp(r+s)\), rescale \(r=sx\).
The factor converges with all derivatives on compact positive \(x\)
intervals to \(d\), with error of power--log order \(s^{2/11}\).
The strict complete-monotonicity violation above persists for small
\(s\).

### Disposition

The old scalar kernel remains a valid countermodel to the diagonal and
band estimates considered in that round, but not to the positive
heat-energy structure (4).  Its advertised constant-energy spectral core
is a signed flux spectrum, not a positive energy spectrum.

## 4. A positive q4 spectral-shell survivor

The complete-monotonicity correction is not a contradiction.  Use
(11)--(12) and note

\[
\int_0^sL(a)\,da
\asymp
s^{2/11}\ell(s)^{2/11}.
\tag{35}
\]

Thus

\[
A(s)\longrightarrow\frac d2,
\qquad
A(s)+\int_0^sA(a)L(a)\,da=\frac d2.
\tag{36}
\]

### Theorem 5: exact positive-energy q4 reuse ledger

The shell energy \(\mathcal E_\circ\) is completely monotone, vanishes
for fixed \(r>0\) as \(s\downarrow0\), and satisfies the exact energy,
diagonal, and recycling identities.  Its flux is (14), and the ledgers
(16) obey

\[
\int_0^hM_\circ^2
\asymp
h^{7/11}\ell(h)^{-4/11},
\tag{37}
\]

\[
\int_0^hY_\circ^2
\asymp
h^{2/11}\ell(h)^{2/11},
\tag{38}
\]

\[
\int_0^hM_\circ Y_\circ^2=\infty.
\tag{39}
\]

Moreover,

\[
|\Pi^\circ_r(s)|
\lesssim
r^{-1/2}M_\circ(s)Y_\circ(s),
\tag{40}
\]

\[
\operatorname{Var}_{r>0}\Pi^\circ_r(s)
=
\frac{2A(s)a(s)}{e\,s}
\asymp
M_\circ(s)Y_\circ(s)^2,
\tag{41}
\]

and the early-reuse law (18) holds.

#### Proof

Complete monotonicity is immediate from (12), which is the Laplace
transform of \(A(s)\delta_{L(s)}\).  Since \(L(s)\to\infty\), the fixed
positive heat boundary vanishes.  Equations (13)--(15) follow by direct
differentiation.  The characteristic law then supplies the diagonal and
recycling identities.

The energy identity in half-energy normalization is (36).  Definitions
(11) and (16) give (17), and one-sided power--log integration gives
(37)--(39).

For (40), put \(x=rL(s)\).  Then

\[
\Pi^\circ_r(s)
=
\frac{A(s)a(s)}sxe^{-x},
\tag{42}
\]

while

\[
r^{-1/2}M_\circ Y_\circ
=
\sqrt{\frac{A(s)}{\nu}}\,
\frac{x^{-1/2}}s.
\tag{43}
\]

The ratio is bounded because \(x^{3/2}e^{-x}\) is bounded.  The function
\(xe^{-x}\) rises from zero to \(e^{-1}\) and returns to zero, so its
total variation is \(2/e\), proving (41).

It remains to prove (18).  The total diagonal work equals \(A(\tau)\),
which tends to \(d/2\).  On \(q\tau\le s\le\tau\), use
\(xe^{-x}\le x\), \(s\asymp\tau\), and monotonicity of \(L\) to obtain

\[
\int_{q\tau}^{\tau}
\Pi^\circ_{\tau-s}(s)\,ds
\lesssim_q
\tau L(q\tau)
\lesssim_q
\tau^{2/11}\ell(\tau)^{2/11}
\longrightarrow0.
\tag{44}
\]

Thus all but a vanishing fraction of the work lies in \(s<q\tau\).
The regular-variation balance \(\tau L(s_\tau)\asymp1\) gives (19).

### Scope

The positive measure \(A(s)\delta_{L(s)}\) is a legitimate ideal energy
spectrum.  Its time derivative contains a derivative of a delta, so its
transfer in (6) is distributional in \(\lambda\).  Smooth positive shell
mollifications retain all asymptotic conclusions.  No quadratic velocity
field or NSE evolution is asserted.

## 5. Exact adjacent-shell quadratic triads

The transfer shape in (42) is not forbidden by incompressibility.  Let
\((n,m)\) solve (20).  The nonzero Fourier waves of (21) are

\[
\pm(0,-2m,0),
\qquad
\pm(n,m,0),
\qquad
\pm(-n,m,0),
\tag{45}
\]

with positive-wave coefficients \(i/2\) times

\[
(0,0,1),
\qquad
(m,-n,0),
\qquad
(0,0,1),
\tag{46}
\]

respectively.  Each coefficient is perpendicular to its wave.

### Theorem 6: positive Pell triad heat profile

Equations (22)--(24) hold.

#### Proof

The three waves sum to zero.  Their squared radii are

\[
4m^2,
\qquad
n^2+m^2=4m^2+1,
\tag{47}
\]

where the second equality uses (20).  Enumerating the six real Fourier
modes in

\[
\sum_{k+p+q=0}
\widehat W_\alpha(k)
\widehat W_\beta(p)
(iq_\beta)\eta_{|q|^2}
\widehat W_\alpha(q)
\tag{48}
\]

gives shell coefficients

\[
\frac{nm}{2},
\qquad
-\frac{nm}{2}.
\tag{49}
\]

This proves (22).  The exact enumeration is independently checked by
`lab/navier_lab/type_ii_triad_packet.py`.

Substitute
\(\eta_j=e^{-2\nu rj}\) to obtain (23), whose factors are strictly
positive for \(r>0\).

Finally, put \(r=x/(8\nu m^2)\).  Then

\[
\begin{aligned}
Q_{n,m}(r)
&=
\frac{nm}{2}e^{-x}
\left(1-e^{-x/(4m^2)}\right)\\
&\longrightarrow
\frac{\sqrt3}{8}xe^{-x},
\end{aligned}
\]

because Pell solutions satisfy \(n/m\to\sqrt3\).  The convergence is
locally uniform.

### Consequences

1. The nonlinear spectral measure has exactly two adjacent atoms.
2. Its total mass is zero, as required by transport cancellation.
3. Its first radial moment is nonzero, so three-dimensional
   incompressibility supplies no enstrophy-moment cancellation.
4. Its heat flux is positive for every \(r>0\).
5. Adjacent-shell quadratic transfer converges to the positive
   shell-derivative shape in the complete-monotone survivor.

For each fixed Pell pair, the standard vector-potential cutoff used in
the prior triad-packet theorem gives compact solenoidal
\(\mathbb R^3\) approximations on bounded heat-age ranges.  This does not
concatenate the Pell fields into one trajectory.

### Downstream disposition

The [spectral quantile-speed theorem](type-ii-spectral-quantile-speed.md)
derives the finite actual-trajectory budget
\[
\int_0^{s_0}\int_0^\infty
\lambda^{-1/2}|d\mu_s|\,ds<\infty.
\]
It excludes any nondegenerate fixed-energy q4 quantile that remains
smoothed inside adjacent or \(O(\sqrt L)\)-width shells.  Hence the
delta-shell interpretation and dynamically adjacent Pell shortcut are
closed.  A smooth positive shell of fixed relative width \(W\asymp L\)
pays this charge finitely while retaining all scalar q4 and early-reuse
laws, so broad-shell genealogy is the replacement live gate.  The exact
Pell snapshots proved above remain valid.

## 6. Exact frontier

### Robust findings, subject to external review

1. The actual diagonal flux is the Laplace transform of the signed radial
   quadratic measure (3), with explicit triad density (28).
2. The flux is the characteristic derivative of a positive completely
   monotone heat-energy spectrum.
3. This positivity excludes the preceding coherent Laguerre survivor as
   an actual kinetic-energy spectrum.
4. The positive moving-shell model restores every q4 scalar law,
   complete monotonicity, exact energy and recycling, and asymptotically
   total early-history reuse.
5. The Pell family gives exact divergence-free adjacent-shell
   self-interactions with positive flux at every heat age.
6. Its rescaled profile converges to the moving-shell
   \(xe^{-x}\) kernel.

### Closed shortcuts

The following cannot close q4:

1. the former Laguerre flux kernel;
2. complete monotonicity of heat energy by itself;
3. total-mass or any universal first-moment cancellation of the nonlinear
   spectrum;
4. positivity or sign rigidity of the self-interaction heat profile;
5. pressure projection or instantaneous incompressibility alone; and
6. separation into adjacent radial shells alone.

### Things still to prove

1. Rule out dynamic identification
   \[
   \mu_s=\partial_s\varepsilon_s+\lambda\varepsilon_s
   \]
   with repeated positive adjacent-shell triad transfer on one q4
   trajectory.
2. Derive a temporal genealogy or shell-speed cost from the exact
   quadratic convolution (28) that is finite under unweighted
   dissipation but violated by the moving-shell survivor.
3. Prove that the strong-trace drift cannot coherently steer the
   self-interaction Pell transfers across the q4 record schedule.
4. Combine the Hausdorff-one-null boundary energy measure with the radial
   shell descent; the present survivor has no spatial support geometry.
5. Treat smooth shell thickness quantitatively rather than through the
   delta-shell idealisation.
6. Treat slower clocks, divergent normalised energy, R3B, and the other
   Clay alternatives separately.

### Conjecture: no dynamically coherent q4 shell descent

No same-trajectory full-defect q4 entrance with finite unweighted
dissipation can simultaneously have:

1. positive energy spectrum concentrated near
   \(L(s)=s^{-9/11}\ell(s)^{2/11}\);
2. nonlinear transfer asymptotic to positive adjacent-shell Pell
   transfers at that moving shell; and
3. a fixed fraction of every terminal energy quantum supplied from
   source times \(s=o(\tau)\).

This conjecture is not proved.  The positive shell survivor is not a
velocity field, and the Pell family is not one evolution.  No q4 closure,
regularity theorem, breakdown theorem, energy-equality theorem, or Clay
alternative is proved.

## 7. Reproduce

Run

```text
make type-ii-triad-packet
PYTHONPATH=lab python -m unittest \
  lab.tests.test_type_ii_triad_packet -v
```

The certificate now checks the Pell recurrence, divergence-free modes,
adjacent shell radii, exact convolution coefficients, zero total
transfer, nonzero first shell moment, positive heat decrement, and
convergence of the rescaled coefficient to \(\sqrt3/8\).  It does not
certify the analytic characteristic law, regular-variation limit,
localisation, or any same-trajectory claim.
