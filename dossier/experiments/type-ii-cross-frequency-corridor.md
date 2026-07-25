# The q4 cross defect forces a moving frequency corridor

- **Experiment:** EXP-TYPE-II-CROSS-FREQUENCY-CORRIDOR-001
- **Route:** ROUTE-R3C
- **Status:** complete conditional reduction; external review pending
- **Domain:** smooth finite-energy Navier--Stokes flow on \(\mathbb R^3\)
- **Clay status:** unsolved
- **Input:** [amplitude-slab pincer](type-ii-adjoint-amplitude-pincer.md)

## Downstream disposition

The subsequent
[full-defect alignment theorem](type-ii-full-defect-alignment.md) chooses
the Oseen terminal data to exhaust the entire kinetic-energy jump.  For
that canonical entrance, the cross spectrum becomes the positive primal
defect-energy spectrum at records and the terminal low-pass clock forces
\(\kappa_j\gtrsim\Lambda_j\).  Thus the corridor derived here remains a
sharp theorem for an incompletely normalised entrance, but it is no longer
the live R3C survivor.

## Verdict

The pressure-free commutator anomaly, when used through the Lorentz norm
bounds proved here, does not force the desired amplitude
anti-correlation.  It instead forces a moving cross-pairing frequency
and persistent **joint concentration** of primal and adjoint enstrophy.

Write, in reverse terminal time \(0<\tau<\tau_0\),

\[
M(\tau):=\|u(T-\tau)\|_{L^{3,\infty}},
\qquad
X(\tau):=\|\nabla u(T-\tau)\|_2,
\qquad
Y(\tau):=\|\nabla a(T-\tau)\|_2.
\tag{1}
\]

For a smooth low-pass \(B_N\), put

\[
K_N(\tau)
:=
\langle u(T-\tau),B_Na(T-\tau)\rangle.
\tag{2}
\]

For fixed \(N\), \(K_N(\tau)\to0\) as \(\tau\downarrow0\), whereas

\[
\lim_{N\to\infty}K_N(\tau)=c_0>0
\qquad(\tau>0).
\tag{3}
\]

Define the first dyadic cross-pairing frequency

\[
\boxed{
\kappa(\tau)
:=
\min\{2^k:K_{2^k}(\tau)\ge c_0/2\}.
}
\tag{4}
\]

Let

\[
B_1(\tau):=\int_0^\tau M(s)\,ds,
\qquad
B_2(\tau):=\int_0^\tau M(s)^2\,ds,
\qquad
H(\tau):=\int_0^\tau M(s)Y(s)\,ds,
\tag{5}
\]

where all fields in the integrals are evaluated at \(T-s\).  The exact
commutator identity and Lorentz Bernstein estimates give

\[
\boxed{
\kappa(\tau)^2B_1(\tau)\gtrsim1,
\qquad
X(\tau)Y(\tau)\gtrsim\kappa(\tau)^2.
}
\tag{6}
\]

Consequently,

\[
\boxed{
X(\tau)Y(\tau)
\gtrsim
\frac1{B_1(\tau)}.
}
\tag{7}
\]

The logarithmic q4 clock gives, with
\(\ell(\tau):=\log(e+\tau_0/\tau)\),

\[
B_1(\tau)
\lesssim
\tau^{9/11}\ell(\tau)^{-2/11}.
\tag{8}
\]

Thus every entrance satisfies the pointwise joint-enstrophy floor

\[
\boxed{
X(\tau)Y(\tau)
\gtrsim
\tau^{-9/11}\ell(\tau)^{2/11}
}
\tag{9}
\]

for almost every sufficiently small \(\tau\).  If

\[
P(\tau):=\int_0^\tau X(s)^2\,ds,
\qquad
D(\tau):=\int_0^\tau Y(s)^2\,ds,
\tag{10}
\]

then

\[
\boxed{
P(\tau)D(\tau)
\gtrsim
\tau^{4/11}\ell(\tau)^{4/11}.
}
\tag{11}
\]

In particular both terminal dissipation tails have a quantitative
lower floor of this order, with constants depending on the finite total
tail of the other field.  The cross defect also forces the inverse-clock
condition

\[
\boxed{
\int_0^{\tau_0}\frac{d\tau}{B_1(\tau)}<\infty.
}
\tag{12}
\]

There is a sharper frequency dichotomy.  The refined commutator bound is

\[
|\partial_\tau K_N|
\lesssim
N^{3/2}M^2+NMY.
\tag{13}
\]

At the transition frequency, either

\[
\boxed{
\kappa(\tau)
\gtrsim
B_2(\tau)^{-2/3},
\qquad
X(\tau)Y(\tau)
\gtrsim
B_2(\tau)^{-4/3},
}
\tag{14}
\]

or

\[
\boxed{
\kappa(\tau)H(\tau)\gtrsim1,
\qquad
H(\tau)^2X(\tau)Y(\tau)\gtrsim1.
}
\tag{15}
\]

The first is the **clock branch**; the second is the
**cross-frequency corridor**.  On a q4 record tail beginning at \(s_j\),

\[
\int_{s_j}^TM\,dt\lesssim \frac{m_j^{-9/2}}j,
\qquad
\int_{s_j}^TM^2\,dt\lesssim \frac{m_j^{-7/2}}j.
\tag{16}
\]

Therefore

\[
\kappa_j\gtrsim
\mu_j:=m_j^{9/4}j^{1/2},
\tag{17}
\]

and (14) is precisely

\[
\kappa_j\gtrsim
\Lambda_j:=m_j^{7/3}j^{2/3}.
\tag{18}
\]

These are the two frequencies already isolated independently in the
Oseen and q4 clock audits.  The present theorem explains their roles:
\(\mu_j\) is the minimum frequency at which the cross pairing can enter,
while \(\Lambda_j\) is the frequency at which direct high--high
nonlinear capacity becomes order one.

The estimates do not contradict the energy class.  The scalar temporal
ledger

\[
M_0(\tau)
=
\tau^{-2/11}\ell(\tau)^{-2/11},
\qquad
X_0(\tau)=Y_0(\tau)
=
\tau^{-9/22}\ell(\tau)^{1/11}
\tag{19}
\]

has \(X_0,Y_0\in L^2\), saturates (7), (9), (11), and (15), lies strictly
below the clock branch, and still has

\[
\int_0 M_0Y_0^2\,d\tau
=
\int_0\frac{d\tau}{\tau}
=\infty.
\tag{20}
\]

This is not a Navier--Stokes construction.  It proves that the clock,
energy budgets, and all norm-level cross-pairing transition inequalities
derived here are mutually consistent at the exact q4 endpoint.  At this
checkpoint a contradiction required unspent phase, sign, or genealogy.
The downstream full-defect theorem supplies enough genealogy to remove
the sub-clock case, leaving clock-scale residence.  No Clay alternative
is proved.

## 1. Setting and terminal pairing

Let

\[
U:=\sup_{t<T}\|u(t)\|_2,
\qquad
A:=\sup_{t<T}\|a(t)\|_2.
\tag{21}
\]

The input theorem supplies

\[
U+A<\infty,
\qquad
\langle u(t),a(t)\rangle=c_0>0,
\tag{22}
\]

\[
u,a\in L^2_t\dot H^1_x,
\qquad
a(t)\rightharpoonup0
\quad(t\uparrow T).
\tag{23}
\]

Choose a real radial
\(\psi\in C_c^\infty(\mathbb R^3)\) with

\[
\psi=1\quad(|\xi|\le1),
\qquad
\psi=0\quad(|\xi|\ge2),
\tag{24}
\]

and let

\[
B_N:=\psi(D/N).
\tag{25}
\]

The pressure-free identity from the input round is

\[
\frac d{dt}\langle u,B_Na\rangle
=
\langle[(u\cdot\nabla),B_N]u,a\rangle.
\tag{26}
\]

For fixed \(N\), its terminal value is zero.  Equivalently,

\[
K_N(\tau)
=
-\int_{T-\tau}^T
\langle[(u\cdot\nabla),B_N]u,a\rangle\,dt.
\tag{27}
\]

The sign in (27) will not matter.  For every fixed positive \(\tau\),
strong convergence \(B_N\to I\) on \(L^2\) gives (3).

The functions \(M\), \(M^2\), and \(MY\) are integrable on terminal
intervals.  Indeed, the q4 clock puts \(M\) in weak
\(L^{11/2}_t\), while \(Y\in L^2_t\).

## 2. Coarse commutator speed

### Lemma 1: an \(N^2M\) speed limit

For every \(N>0\) and almost every preterminal time,

\[
\boxed{
\left|
\langle[(u\cdot\nabla),B_N]u,a\rangle
\right|
\lesssim
UA\,N^2M.
}
\tag{28}
\]

#### Proof

Put \(T_u:=u\cdot\nabla\).  The two pieces are

\[
\langle T_uB_Nu,a\rangle,
\qquad
-\langle B_NT_uu,a\rangle.
\]

Lorentz Hölder and Bernstein give

\[
\begin{aligned}
|\langle T_uB_Nu,a\rangle|
&\le
\|u\|_{L^{3,\infty}}
\|\nabla B_Nu\|_{L^{6,2}}
\|a\|_2\\
&\lesssim
M\,N^2U A.
\end{aligned}
\tag{29}
\]

For the second piece, use self-adjointness and integrate the drift by
parts:

\[
\begin{aligned}
|\langle B_NT_uu,a\rangle|
&=
|\langle T_uu,B_Na\rangle|\\
&=
\left|\int u_i u_j\partial_jB_Na_i\right|\\
&\lesssim
\|u\|_{L^{3,\infty}}\|u\|_2
\|\nabla B_Na\|_{L^{6,2}}\\
&\lesssim
M\,N^2UA.
\end{aligned}
\]

This proves (28).  Both pressure terms and the two viscous terms have
already cancelled in (26).

### Theorem 2: forced cross-frequency motion

The transition frequency in (4) is finite and obeys (6)--(7).

#### Proof

For a fixed \(\tau>0\),

\[
K_{2^k}(\tau)\longrightarrow0
\quad(k\to-\infty),
\qquad
K_{2^k}(\tau)\longrightarrow c_0
\quad(k\to\infty).
\]

Hence (4) is well-defined.  Equations (27)--(28) imply

\[
|K_N(\tau)|
\lesssim
UA\,N^2B_1(\tau).
\tag{30}
\]

At \(N=\kappa(\tau)\), the left side is at least \(c_0/2\).  This
proves the first inequality in (6).

Minimality gives

\[
K_{\kappa(\tau)/2}(\tau)<\frac{c_0}{2}.
\]

Since the full pairing is \(c_0\),

\[
\frac{c_0}{2}
<
\left\langle
u(T-\tau),
(I-B_{\kappa(\tau)/2})a(T-\tau)
\right\rangle.
\tag{31}
\]

The multiplier \(I-\psi(2\xi/\kappa)\) vanishes on a ball of radius
comparable to \(\kappa\).  Plancherel therefore gives

\[
\left|
\langle u,(I-B_{\kappa/2})a\rangle
\right|
\lesssim
\kappa^{-2}\|\nabla u\|_2\|\nabla a\|_2
=
\kappa^{-2}XY.
\tag{32}
\]

Equations (31)--(32) prove the second inequality in (6).  Combining the
two inequalities gives (7).

## 3. Consequences of the logarithmic q4 clock

### Lemma 3: terminal clock integrals

For sufficiently small \(\tau\),

\[
\boxed{
B_1(\tau)
\lesssim
\tau^{9/11}\ell(\tau)^{-2/11},
\qquad
B_2(\tau)
\lesssim
\tau^{7/11}\ell(\tau)^{-4/11}.
}
\tag{33}
\]

#### Proof

The decreasing rearrangement estimate from the input round is

\[
M^*(s)
\lesssim
1+s^{-2/11}\ell(s)^{-2/11}.
\]

Hardy--Littlewood and integration over \(0<s<\tau\) give the first
bound.  Squaring the rearrangement and integrating gives the second.
The slowly varying logarithms are comparable on
\([\tau/2,\tau]\), and the same standard dyadic decomposition controls
the full integral.

### Corollary 4: joint terminal dissipation floor

Equations (9), (11), and (12) hold.

#### Proof

Equations (7) and (33) give (9).  Hence

\[
\begin{aligned}
\int_0^\tau X(s)Y(s)\,ds
&\gtrsim
\int_0^\tau
s^{-9/11}\ell(s)^{2/11}\,ds\\
&\gtrsim
\tau^{2/11}\ell(\tau)^{2/11}.
\end{aligned}
\tag{34}
\]

Cauchy--Schwarz gives

\[
\int_0^\tau XY
\le
P(\tau)^{1/2}D(\tau)^{1/2},
\]

which proves (11).  Since \(P(\tau_0)\) and \(D(\tau_0)\) are finite,
(11) also gives the stated individual lower floors.

Finally, (7) and Cauchy--Schwarz on \((0,\tau_0)\) imply

\[
\int_0^{\tau_0}\frac{d\tau}{B_1(\tau)}
\lesssim
\int_0^{\tau_0}XY\,d\tau
\le
P(\tau_0)^{1/2}D(\tau_0)^{1/2}
<\infty.
\]

This proves (12).

## 4. Refined clock-versus-corridor dichotomy

### Lemma 5: refined commutator speed

For every \(N>0\),

\[
\boxed{
\left|
\langle[(u\cdot\nabla),B_N]u,a\rangle
\right|
\lesssim
A\,N^{3/2}M^2
+U\,NMY.
}
\tag{35}
\]

#### Proof

For the first commutator piece, use skew-adjointness of \(T_u\):

\[
\begin{aligned}
|\langle T_uB_Nu,a\rangle|
&=
|\langle B_Nu,T_ua\rangle|\\
&\lesssim
\|B_Nu\|_{L^{6,2}}
\|u\|_{L^{3,\infty}}
\|\nabla a\|_2\\
&\lesssim
UNMY.
\end{aligned}
\tag{36}
\]

For the second piece,

\[
|\langle B_NT_uu,a\rangle|
=
\left|\int u_i u_j\partial_jB_Na_i\right|.
\]

O'Neil Hölder and band-limited Lorentz Bernstein give

\[
\|u\otimes u\|_{L^{3/2,\infty}}
\lesssim M^2,
\qquad
\|\nabla B_Na\|_{L^{3,1}}
\lesssim N^{3/2}A.
\tag{37}
\]

The latter estimate also follows by interpolating its band-limited
\(L^2\) and \(L^\infty\) bounds.  Equations (36)--(37) prove (35).

### Theorem 6: the cross-frequency corridor

For almost every sufficiently small \(\tau\), at least one of
(14)--(15) holds.

#### Proof

Integrate (35) in (27).  At \(N=\kappa(\tau)\),

\[
\frac{c_0}{2}
\lesssim
A\,\kappa(\tau)^{3/2}B_2(\tau)
+U\,\kappa(\tau)H(\tau).
\tag{38}
\]

At least one term on the right is bounded below by a fixed positive
constant.

If the first term pays, then

\[
\kappa(\tau)\gtrsim B_2(\tau)^{-2/3}.
\]

The high-frequency estimate in Theorem 2 gives the second statement in
(14).  If the second term pays, then
\(\kappa(\tau)H(\tau)\gtrsim1\), and Theorem 2 gives

\[
H(\tau)^2X(\tau)Y(\tau)
\gtrsim
H(\tau)^2\kappa(\tau)^2
\gtrsim1.
\]

This is (15).

### Record-scale interpretation

Put \(\kappa_j:=\kappa(T-s_j)\).  On the exact q4 record tails, (16)
and Theorem 2 give (17).  Applying Theorem 6 and the second estimate in
(16) gives the alternative

\[
\kappa_j\gtrsim m_j^{7/3}j^{2/3}
\]

or

\[
\kappa_j
\int_{s_j}^T
M(t)Y(t)\,dt
\gtrsim1.
\tag{39}
\]

Thus the gap

\[
\frac{\Lambda_j}{\mu_j}
\asymp
m_j^{1/12}j^{1/6}
\longrightarrow\infty
\tag{40}
\]

is now an exact corridor, not merely a mismatch between two unrelated
upper estimates.

## 5. Exact scalar saturation

Work on \(0<\tau<e^{-e}\) and put

\[
L(\tau):=\log(e/\tau).
\]

Define the functions in (19).  Direct integration gives

\[
\begin{aligned}
B_{1,0}(\tau)
&\asymp
\tau^{9/11}L(\tau)^{-2/11},\\
B_{2,0}(\tau)
&\asymp
\tau^{7/11}L(\tau)^{-4/11},\\
H_0(\tau)
&\asymp
\tau^{9/22}L(\tau)^{-1/11},\\
P_0(\tau)=D_0(\tau)
&\asymp
\tau^{2/11}L(\tau)^{2/11}.
\end{aligned}
\tag{41}
\]

Set

\[
\kappa_0(\tau)
:=
B_{1,0}(\tau)^{-1/2}
\asymp
\tau^{-9/22}L(\tau)^{1/11}.
\tag{42}
\]

Then

\[
X_0Y_0
\asymp
\kappa_0^2
\asymp
B_{1,0}^{-1},
\tag{43}
\]

\[
H_0^2X_0Y_0\asymp1,
\qquad
P_0D_0
\asymp
\tau^{4/11}L(\tau)^{4/11}.
\tag{44}
\]

The clock frequency is

\[
\Lambda_0(\tau)
:=
B_{2,0}(\tau)^{-2/3}
\asymp
\tau^{-14/33}L(\tau)^{8/33}.
\tag{45}
\]

It strictly exceeds the corridor frequency:

\[
\frac{\kappa_0(\tau)}{\Lambda_0(\tau)}
\asymp
\tau^{1/66}L(\tau)^{-5/33}
\longrightarrow0.
\tag{46}
\]

Moreover,

\[
\kappa_0(\tau)^{3/2}B_{2,0}(\tau)
\asymp
\tau^{1/44}L(\tau)^{-5/22}
\longrightarrow0,
\tag{47}
\]

while \(\kappa_0H_0\asymp1\).  Thus the direct clock term vanishes and
the corridor term pays exactly.

Finally,

\[
M_0Y_0^2=\tau^{-1},
\tag{48}
\]

so the weighted adjoint dissipation diverges while all unweighted
energy-class integrals remain finite.

The transition itself can also be represented at the scalar level.
Choose a smooth nondecreasing function
\(\Phi:[0,\infty)\to[0,1]\) with

\[
\Phi(z)=0\quad(z\le1/2),
\qquad
\Phi(z)=1\quad(z\ge1),
\tag{49}
\]

and set

\[
K_N^0(\tau)
:=
c_0\Phi\left(\frac{N}{\kappa_0(\tau)}\right).
\tag{50}
\]

Then

\[
\lim_{\tau\downarrow0}K_N^0(\tau)=0,
\qquad
\lim_{N\to\infty}K_N^0(\tau)=c_0,
\tag{51}
\]

and its first half-pairing frequency is comparable to \(\kappa_0\).
The derivative is supported where \(N\asymp\kappa_0\), and there

\[
|\partial_\tau K_N^0|
\lesssim
\tau^{-1}
\asymp
N^2M_0
\asymp
NM_0Y_0.
\tag{52}
\]

Thus the synthetic front saturates both the coarse speed limit and the
corridor term while the direct clock term vanishes as in (47).

This ledger verifies sharp consistency of every scalar exponent in the
new pincer.  It has no spatial fields, pressure, cross measure, or
Navier--Stokes dynamics; in particular \(K_N^0\) is not asserted to be a
PDE pairing.  It is not a counterexample to the route.

## 6. Exact frontier

### Robust conditional findings, subject to external review

1. The cross defect defines a dyadic transition frequency
   \(\kappa(\tau)\to\infty\).
2. Pressure-free commutator speed and the high-frequency pairing tail
   give \(\kappa^2B_1\gtrsim1\), \(XY\gtrsim\kappa^2\), and hence
   \(XY\gtrsim B_1^{-1}\).
3. The q4 clock forces the pointwise law (9), the joint tail floor (11),
   and the inverse-clock condition (12).
4. Refined Lorentz commutator bounds split every time into the clock
   branch (14) or the corridor branch (15).
5. At q4 records, the universal entrance scale is exactly
   \(\mu_j=m_j^{9/4}j^{1/2}\), while direct nonlinear capacity becomes
   order one at
   \(\Lambda_j=m_j^{7/3}j^{2/3}\).
6. The scalar ledger (19), (41)--(52) saturates the moving corridor,
   both speed bounds, and every energy-class exponent while retaining
   infinite \(M\)-weighted adjoint dissipation.

### Closed shortcut

The pressure-free cross identity, after taking only the Lorentz norm
bounds and logarithmic clock used here, cannot force the summable
amplitude anti-correlation sought in the preceding round.  Those norm
consequences have the opposite sign: persistent joint enstrophy
concentration.  The saturation ledger shows why no rearrangement of
these scalar inequalities can manufacture a contradiction; it does not
discard possible phase or sign information in the exact identity.

### Things still to prove

1. Exclude persistent corridor transfer
   \(\kappa_j\ll\Lambda_j\) using same-trajectory phase, sign, genealogy,
   or projected-pressure structure absent from the scalar ledger.
2. Alternatively force \(\kappa_j\gtrsim\Lambda_j\) on enough record
   blocks and turn the resulting pointwise \(XY\) floor into a
   non-reusable residence or dissipation charge.
3. Prove a frequency-front non-reuse theorem: successive order-one
   cross-pairing transitions cannot recycle one finite primal--adjoint
   energy reservoir.
4. A direct proof of finite Lorentz--Zygmund adjoint cost, commutator
   equiintegrability, current removability, strong left \(L^2\)
   continuity, or energy equality still closes q4.
5. Treat slower clocks, divergent normalised energy, and the other Clay
   alternatives separately.

### Conjecture: no persistent sub-clock cross corridor

Under the exact q4 hypotheses, the transition frequency cannot satisfy

\[
\kappa_j=o(\Lambda_j)
\]

through infinitely many first-record blocks while

\[
\kappa_j
\int_{s_j}^T
M(t)Y(t)\,dt
\gtrsim1.
\]

The conjecture is not proved.  Even if proved, a residence or non-reuse
step may still be needed to exclude the clock branch.
