# Every feedback Dyson word has a last chargeable return or none

- **Experiment:** EXP-ADJOINT-PRESSURE-LAST-RETURN-001
- **Route:** ROUTE-R3B
- **Status:** adversarially recomputed valid in the stated smooth-layer
  conditional scope
- **Review:** [accepted after filter-topology, source-scope, and
  quantifier repairs](../review-ledger.md)
- **Domain:** \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** adversarially recomputed
  [feedback Dyson identity](adjoint-pressure-divergent-interaction-depth.md),
  [one-return theorem](adjoint-pressure-one-return.md),
  [full-corridor theorem](adjoint-pressure-corridor-sum.md), and
  [smooth-layer identification theorem](adjoint-pressure-corridor-identification.md)

The preceding theorem treated the continuation of a separated-return
source, but a fixed pressure floor for that continuation remained an
antecedent.  This note removes that antecedent from the exhaustive
frequency split.

On each fixed smooth physical layer, split the Oseen Volterra operator
as

\[
T_b=\mathsf A_b+\mathsf B_b.
\tag{1}
\]

Here \(\mathsf B_b\) contains precisely the LP blocks which take an
input state above \(64F\) to an output band \(F\ge F_*\), where
\(F_*\ge16S\) is fixed.  The complementary operator
\(\mathsf A_b\) contains every other block.

For the actual feedback remainder

\[
r=g+T_br,
\tag{2}
\]

the exact renewal identity is

\[
\boxed{
r
=
\underbrace{(I-\mathsf A_b)^{-1}g}_{r_{\rm no}}
+
\underbrace{(I-\mathsf A_b)^{-1}\mathsf B_br}_{r_{\rm last}}.
}
\tag{3}
\]

After the fixed source \(g=T_bq\), the first term contains feedback
Dyson words with no chargeable \(\mathsf B_b\)-return.  The source
itself already contains one interaction.  The second groups every other
word by its last chronological \(\mathsf B_b\)-return; after that
return, only \(\mathsf A_b\)-interactions occur.  Nothing is
double-counted.

If the complete selected low-output feedback pressure has a fixed
floor \(p_0\), equation (3) gives the exhaustive alternative

\[
\boxed{
\|\mathscr P_{S,b}r_{\rm no}\|_{L^1_{t,x}}
\ge\frac{p_0}{2}
\quad\hbox{or}\quad
\|\mathscr P_{S,b}r_{\rm last}\|_{L^1_{t,x}}
\ge\frac{p_0}{2}.
}
\tag{4}
\]

The last-return branch has a finite smooth-layer capture ceiling.  If
that ceiling is parabolic, all separated starting bands and all later
no-return paths satisfy

\[
\|\mathscr P_{S,b}r_{{\rm last},U}\|_{L^1_{t,x}}
\le
C_\kappa S h^{1/2}\mathcal B_0(h)
+C_\kappa\frac S{F_*}h^7
\qquad
(U\le\kappa h^{-1/2}),
\tag{5}
\]

so a fixed floor forces

\[
\boxed{
D_b(h)
\ge
h^{-3}\exp\!\left(c h^{-9/4}\right).
}
\tag{6}
\]

Here and below, (6) holds for all sufficiently small \(h\) along the
selected parabolic-capture branch.

Consequently, along every selected collapsing sequence with a complete
feedback pressure floor, one may pass to a subsequence on which at
least one of the following holds:

1. the no-chargeable-feedback-return block carries a fixed pressure
   floor;
2. the last-return block requires a superparabolic LP capture ceiling;
3. the coefficient pays the \(9/4\) stretched-exponential cost (6).

This makes participation of the separated-return block an exhaustive
alternative rather than an assumption.  It does not eliminate the
first two branches.

## 1. Smooth-layer feedback equation

Fix \(h,\nu,S>0\) and a dyadic \(F_*\ge16S\).  On one fixed smooth
finite-energy genealogy layer, assume

\[
b\in L^\infty(0,h;L^\infty\cap L^2),
\qquad
\nabla\cdot b=0,
\qquad
\sup_{0<t<h}\|b(t)\|_{L^{3,\infty}}\le M.
\tag{7}
\]

Put

\[
B_\infty:=\|b\|_{L^\infty_{t,x}}<\infty.
\tag{8}
\]

Also retain the reviewed coefficient-dissipation notation

\[
D_b(h)
:=
\int_0^h\|\nabla b(t)\|_2^2\,dt.
\tag{8a}
\]

The constant \(M\) is uniform along the reviewed genealogy;
\(B_\infty\) need not be.  Let

\[
X_h:=C([0,h];L^2_\sigma(\mathbb R^3)).
\tag{9}
\]

Retain the reviewed smooth feedback equation

\[
r=g+T_br,
\qquad
g:=T_bq,
\qquad
r,g\in X_h,
\tag{10}
\]

where

\[
(T_bz)(t)
:=
\int_0^t
e^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}
\bigl(z(s)\boxtimes b(s)\bigr)\,ds.
\tag{11}
\]

The retained tensor orientation is
\((z\boxtimes b)_{ik}:=z_i b_k\).
The plus sign is the reviewed feedback convention.  With the opposite
PDE convention, insert the same sign in
\(T_b,\mathsf A_b,\mathsf B_b\); the norm estimates are unchanged.

Use the fixed homogeneous LP resolution
\(\{\Delta_R\}_{R\in2^{\mathbb Z}}\), and put

\[
P_{>64F}:=
\sum_{\substack{R\in2^{\mathbb Z}\\R>64F}}\Delta_R.
\tag{12}
\]

Every series below is first defined with finite upper and lower
cutoffs.  The \(L^2\) limits are then taken as proved in Section 2.

## 2. The separated-downcross operator is a Volterra operator

Define

\[
\boxed{
\begin{aligned}
(\mathsf B_bz)(t)
:={}&
\sum_{\substack{F\in2^{\mathbb Z}\\F\ge F_*}}
\int_0^t
\Delta_F e^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}\\
&\qquad\qquad
\bigl((P_{>64F}z(s))\boxtimes b(s)\bigr)\,ds,
\end{aligned}
}
\tag{13}
\]

and set

\[
\boxed{\mathsf A_b:=T_b-\mathsf B_b.}
\tag{14}
\]

For each output band \(Q\), put

\[
\mathsf J_Q
:=
\begin{cases}
I,&Q<F_*,\\
I-P_{>64Q},&Q\ge F_*,
\end{cases}
\tag{14a}
\]

and write the two output blocks as

\[
\begin{aligned}
\mathsf A_{b,Q}z(t)
&:=
\int_0^t
\Delta_Qe^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}
\bigl((\mathsf J_Qz(s))\boxtimes b(s)\bigr)\,ds,\\
\mathsf B_{b,Q}z(t)
&:=
\mathbf 1_{\{Q\ge F_*\}}
\int_0^t
\Delta_Qe^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}
\bigl((P_{>64Q}z(s))\boxtimes b(s)\bigr)\,ds.
\end{aligned}
\tag{14b}
\]

Then

\[
\mathsf A_b=\sum_Q\mathsf A_{b,Q},
\qquad
\mathsf B_b=\sum_Q\mathsf B_{b,Q},
\tag{14c}
\]

because, output band by output band,
\(\mathsf J_Q+\mathbf 1_{\{Q\ge F_*\}}P_{>64Q}=I\).
This is an exact complementary **filter** partition, not a positivity
or disjoint-support assertion.  Smooth LP symbols overlap; no later
argument treats the two filters as characteristic functions.

Let \(K_{\mathsf B}(t,s)\) denote the integrand operator in (13), with
\(\tau=t-s>0\).  Heat decay on the output annulus, LP almost
orthogonality, and multiplication by \(b(s)\) give

\[
\begin{aligned}
\|K_{\mathsf B}(t,s)z\|_2^2
&\le
CB_\infty^2
\sum_{F\ge F_*}
F^2e^{-c\nu F^2\tau}
\|P_{>64F}z\|_2^2\\
&\le
CB_\infty^2
\sum_R\|\widetilde\Delta_Rz\|_2^2
\sum_{\substack{F<R/32\\F\ge F_*}}
F^2e^{-c\nu F^2\tau}.
\end{aligned}
\tag{16}
\]

Here \(\widetilde\Delta_R\) is one fixed finite enlargement of the
band-\(R\) multiplier.  The second line is the weighted
Littlewood--Paley tail inequality obtained by expanding the nested
high-pass tails and swapping the \(F\)- and \(R\)-sums.  Finite overlap
gives
\(\sum_R\|\widetilde\Delta_Rz\|_2^2\lesssim\|z\|_2^2\).
The inner dyadic heat-rate sum satisfies

\[
\sum_{F<R/32}
F^2e^{-c\nu F^2\tau}
\le
\sum_{F\in2^{\mathbb Z}}
F^2e^{-c\nu F^2\tau}
\le
\frac C{\nu\tau}.
\tag{17}
\]

Consequently,

\[
\boxed{
\|K_{\mathsf B}(t,s)z\|_2
\le
\frac{C B_\infty}{\sqrt{\nu(t-s)}}\|z\|_2.
}
\tag{18}
\]

The same bound is standard for \(T_b\), so (14) gives it for
\(\mathsf A_b\) as well.  In particular, both operators map
\(X_h\) continuously to itself.  Fractional Volterra iteration gives,
for \(\mathsf C_b=\mathsf A_b\) or \(\mathsf B_b\),

\[
\boxed{
\|\mathsf C_b^mz\|_{X_h}
\le
\|z\|_{X_h}
\frac{
\bigl(CB_\infty\Gamma(1/2)\sqrt{h/\nu}\bigr)^m
}{
\Gamma(m/2+1)
}.
}
\tag{19}
\]

Mixed words in \(\mathsf A_b,\mathsf B_b\) have the same majorant with
one fixed constant enlarged by a factor two.  Hence all operator
series used below converge in \(X_h\), without smallness of
\(B_\infty\sqrt{h/\nu}\).

There is also an explicit high-output operator tail.  For
\(\mathsf C_{b,Q}=\mathsf A_{b,Q}\) or
\(\mathsf B_{b,Q}\), the input filter in (14b) is uniformly
\(L^2\)-bounded, so

\[
\|\mathsf C_{b,Q}z\|_{X_h}
\le
CB_\infty\|z\|_{X_h}
\int_0^h Qe^{-c\nu Q^2\tau}\,d\tau
\le
\frac{CB_\infty}{\nu Q}\|z\|_{X_h}.
\tag{19a}
\]

Almost orthogonality of the output annuli and the dyadic geometric
sum now give

\[
\boxed{
\left\|
\sum_{Q>U}\mathsf C_{b,Q}z
\right\|_{X_h}
\le
\frac{CB_\infty}{\nu U}\|z\|_{X_h}.
}
\tag{19b}
\]

Thus the upper-output truncations of both operators converge in
operator norm at rate \(O(U^{-1})\).  Since \(\mathsf B_b\) has the
fixed lower output floor \(F_*\), its whole output series converges in
operator norm.  The all-low-frequency end of the homogeneous series
for \(\mathsf A_b\) is instead understood in the strong \(L^2\) sense
fixed by \(\mathsf A_b=T_b-\mathsf B_b\); no operator-norm convergence
at frequency zero is asserted, and no polynomial remainder occurs in
\(L^2\).

## 3. Exact renewal by the last separated return

Define

\[
\boxed{
r_{\rm no}
:=
\sum_{m=0}^\infty\mathsf A_b^mg
=
(I-\mathsf A_b)^{-1}g
}
\tag{20}
\]

and

\[
\boxed{
r_{\rm last}
:=
\sum_{m=0}^\infty
\mathsf A_b^m\mathsf B_br
=
(I-\mathsf A_b)^{-1}\mathsf B_br.
}
\tag{21}
\]

Since \(T_b=\mathsf A_b+\mathsf B_b\), equation (10) gives

\[
(I-\mathsf A_b)r=g+\mathsf B_br.
\tag{22}
\]

Apply the convergent Volterra inverse
\((I-\mathsf A_b)^{-1}\) to obtain (3).

The word interpretation is exact.  Expanding the full smooth-layer
Dyson solution

\[
r=\sum_{m=0}^\infty
(\mathsf A_b+\mathsf B_b)^mg
\tag{23}
\]

gives one all-\(\mathsf A_b\) word at each depth, which belongs to
\(r_{\rm no}\).  Every other word has a unique last chronological
\(\mathsf B_b\).  The arbitrary earlier prefix is already contained in
\(r\) on the right of \(\mathsf B_b\), while the later suffix consists
only of \(\mathsf A_b\)'s and is generated by the inverse in (21).
Thus (21) contains every word with a chargeable separated return
exactly once.

Let

\[
\Pi_S:=S_S\mathbb Q\operatorname{div},
\qquad
(\mathscr P_{S,b}z)(t)
:=
\Pi_S\bigl(z(t)\boxtimes b(t)\bigr).
\tag{24}
\]

Here \(S_S\) is the fixed smooth low-output multiplier and
\(\mathbb Q\) is the pressure projection used in the reviewed
one-return theorem.
The reviewed fixed-band kernel bound gives the continuous map

\[
\mathscr P_{S,b}:X_h
\longrightarrow
Y_h:=L^1((0,h)\times\mathbb R^3).
\tag{25}
\]

Applying it to (3) gives

\[
\mathscr P_{S,b}r
=
\mathscr P_{S,b}r_{\rm no}
+\mathscr P_{S,b}r_{\rm last}
\quad\hbox{in }Y_h.
\tag{26}
\]

The triangle inequality proves (4) from the reviewed floor

\[
\|\mathscr P_{S,b}r\|_{Y_h}\ge p_0.
\tag{27}
\]

No sign or cancellation assumption is used.

## 4. The last-return source is exactly the reviewed source sum

For each dyadic \(F\ge F_*\), define

\[
\boxed{
w_F(t)
:=
\int_0^t
\Delta_Fe^{\nu(t-s)\Delta}
\mathbb P\operatorname{div}
\bigl((P_{>64F}r(s))\boxtimes b(s)\bigr)\,ds.
}
\tag{28}
\]

These are exactly the one-return sources in the reviewed theorem.
Equation (13) gives the strong \(X_h\) identity

\[
\boxed{
\mathsf B_br
=
\sum_{\substack{F\in2^{\mathbb Z}\\F\ge F_*}}w_F.
}
\tag{29}
\]

Unlike a termwise absolute source estimate, (29) follows directly from
the strong output-tail convergence just proved for the bounded operator
\(\mathsf B_b\).  No uniform smooth Sobolev ceiling is required.

For dyadic \(U\ge F_*\), put

\[
W_U
:=
\sum_{\substack{F\in2^{\mathbb Z}\\F_*\le F\le U}}w_F
=
\left(\sum_{F_*\le Q\le U}\mathsf B_{b,Q}\right)r.
\tag{30}
\]

Define the output-truncated complementary operator directly by

\[
\boxed{
\mathsf A_{b,U}
:=
\sum_{\substack{Q\in2^{\mathbb Z}\\Q\le U}}
\mathsf A_{b,Q}.
}
\tag{30b}
\]

Thus \(\mathsf A_{b,U}\) is the direct sum of complementary filtered
output blocks whose output is at most \(U\).  It is not defined as the
composition of two overlapping smooth cutoffs.  More explicitly, if
\(\mathsf L_U:=\sum_{Q\le U}\Delta_Q\), then finite cutoffs and (14b)
give

\[
\mathsf A_{b,U}
=
\mathsf L_UT_b
-
\sum_{F_*\le Q\le U}\mathsf B_{b,Q}.
\tag{30c}
\]

This identity supplies the strong homogeneous \(L^2\) limit at the
all-low-frequency end.  In general (30c) is not the overlapping
cutoff composition \(\mathsf L_U\mathsf A_b\).  Now define

\[
\boxed{
r_{{\rm last},U}
:=
\sum_{m=0}^\infty
\mathsf A_{b,U}^mW_U.
}
\tag{31}
\]

The operator-tail estimate (19b) gives

\[
W_U\longrightarrow\mathsf B_br
\quad\hbox{in }X_h,
\qquad
\|\mathsf A_b-\mathsf A_{b,U}\|_{X_h\to X_h}
\le\frac{CB_\infty}{\nu U}
\longrightarrow0.
\tag{32}
\]

The second statement implies convergence of every fixed-depth iterate
on \(X_h\).  Restricting output bands does not enlarge the kernel
estimate (18), so the Gamma tails from (19) are uniform in \(U\).  The
same two-term dominated-convergence argument as in the smooth-layer
identification theorem therefore gives

\[
\boxed{
r_{{\rm last},U}
\longrightarrow
r_{\rm last}
\quad\hbox{in }X_h,
\qquad
\mathscr P_{S,b}r_{{\rm last},U}
\longrightarrow
\mathscr P_{S,b}r_{\rm last}
\quad\hbox{in }Y_h.
}
\tag{33}
\]

Thus a nonzero last-return pressure always has a finite layerwise
capture ceiling.

## 5. Every captured last-return path is dominated by the corridor sum

Sections 5--6 retain **all** hypotheses, cutoff conventions, and the
source ledger of the reviewed one-return theorem.  In particular, each
\(w_F\) has the nonnegative source \(G_F\) and the bound encoded by
\(\mathcal B(h,F)\).  The smooth-layer assumptions (7)--(10) alone
prove the renewal topology; they do not imply that source ledger.

At finite LP cutoffs, expand (31).  Its depth-zero source has one
starting band \(F_*\le F\le U\).  Every later
\(\mathsf A_{b,U}\)-interaction has output frequency at most \(U\).
For \(Q\ge F_*\), the selector
\(I-P_{>64Q}\) is the strong sum of the complementary indexed LP input
bands.  Smooth LP symbols overlap, so it is best to regard the
resulting terms as a fixed-overlap **filtered corridor family**, rather
than as a literal subfamily of disjoint Fourier sets.  The same
sequence of output annuli indexes a path in the reviewed full-corridor
family

\[
\mathscr C_m(F;U).
\tag{34}
\]

Put

\[
C_{\rm LP}
:=
\sup_Q\|\mathsf J_Q\|_{L^1\to L^1}<\infty,
\qquad
A_{\rm filt}:=\max\{1,C_{\rm LP}\}A.
\tag{34a}
\]

The reviewed path bounds are absolute.  At depth \(m\), the
complementary filters cost at most \(C_{\rm LP}^m\), which is absorbed
in the enlarged **per-depth** constant \(A_{\rm filt}\), not merely in
the front constant.  Summing first over every filtered
\(\mathsf A_b\)-path, then over every starting band
\(F_*\le F\le U\), gives

\[
\boxed{
\begin{aligned}
\|\mathscr P_{S,b}r_{{\rm last},U}\|_{Y_h}
\le{}&
C_{\rm src}c_0\nu Sh\Phi_{A_{\rm filt}}(H_U)\\
&{}\times
\left[
\mathcal B_0(h)
\sum_{F_*\le F\le U}F
+h^6
\sum_{F_*\le F\le U}F^{-1}
\right],
\end{aligned}
}
\tag{35}
\]

where

\[
H_U=h\sum_{Q\le U}c_0\nu Q^2,
\qquad
\Phi_{A_{\rm filt}}(H)
:=\frac{e^{A_{\rm filt}H}-1}{H},
\tag{36}
\]

and

\[
\begin{aligned}
\mathcal B_0(h)
:=
1
&+h^{7/4}
\left[
1+\log_+\!\bigl(D_b(h)h^3\bigr)
\right]\\
&+h^{21/4}+h^{89/4}+h^{103/4}.
\end{aligned}
\tag{37}
\]

The sums in (35) are over dyadic \(F\), and satisfy

\[
\sum_{F_*\le F\le U}F<2U,
\qquad
\sum_{F_*\le F\le U}F^{-1}<\frac2{F_*}.
\tag{38}
\]

If \(U\le\kappa h^{-1/2}\), then \(H_U\le C_\kappa\), so
(35)--(38) prove (5).

## 6. Exhaustive pressure alternative

Assume (27).  If

\[
\|\mathscr P_{S,b}r_{\rm no}\|_{Y_h}<\frac{p_0}{2},
\tag{39}
\]

then (4) gives

\[
\|\mathscr P_{S,b}r_{\rm last}\|_{Y_h}
\ge\frac{p_0}{2}.
\tag{40}
\]

Define the last-return capture ceiling

\[
\boxed{
U_{\rm last}(h)
:=
\min\left\{
U\in2^{\mathbb Z}:U\ge F_*,\
\|\mathscr P_{S,b}
(r_{\rm last}-r_{{\rm last},U})\|_{Y_h}
\le\frac{p_0}{4}
\right\}.
}
\tag{41}
\]

It is finite by (33), and reverse triangle gives

\[
\|\mathscr P_{S,b}r_{{\rm last},U_{\rm last}(h)}\|_{Y_h}
\ge\frac{p_0}{4}.
\tag{42}
\]

Now take a selected sequence \(h_j\downarrow0\) with the same
uniform pressure floor, weak-\(L^3\) ceiling, and cutoff conventions.
After passing to a subsequence, either:

1. the no-return floor
   \[
   \|\mathscr P_{S,b}r_{\rm no}\|_{Y_h}
   \ge\frac{p_0}{2}
   \tag{43}
   \]
   holds throughout;
2. the capture ceiling escapes superparabolically:
   \[
   U_{\rm last}(h_j)\sqrt{h_j}\longrightarrow\infty,
   \tag{44}
   \]
   equivalently, for every \(\kappa<\infty\), eventually
   \(U_{\rm last}(h_j)\sqrt{h_j}>\kappa\), so no uniformly parabolic
   ceiling captures the fixed last-return pressure fraction; or
3. for some \(\kappa<\infty\),
   \(U_{\rm last}(h_j)\le\kappa h_j^{-1/2}\), in which case (5), (42),
   and the one-return source ledger force (6) for all sufficiently
   large \(j\).

These alternatives are exhaustive.  In branch 2, equation (44) is only
an LP--Dyson capture statement.  It is not yet an instantaneous
Fourier-energy tail or a physical dissipation charge.

The label \(r_{\rm no}\) means **no chargeable separated feedback
return after the fixed source \(g=T_bq\)**:
\(\mathsf B_b\) counts only feedback downcrossings by more than \(64\)
which land at \(F\ge F_*\).  Thus \(r_{\rm no}\) may include a feature
already present in \(g\), gradual later descents, later upcrossings, and
a direct later landing below the detector threshold \(F_*\).  Those
are now one exact complementary operator block rather than a vague
remainder.

This theorem treats the oriented feedback block in (10).  It does not
silently include another tensor orientation or a stretching term.  It
does not exclude either branch 1 or branch 2, produce a singular
solution, prove regularity or breakdown, or establish any Clay
alternative A--D.

The subsequent adversarially recomputed
[no-return parabolic-exclusion theorem](adjoint-pressure-no-return-parabolic.md)
eliminates branch 1 below every uniformly parabolic ceiling.  Thus the
two renewal blocks now have one common unresolved frequency branch:
superparabolic LP--Dyson capture escape.  The captured last-return branch
still pays the \(9/4\) stretched-exponential coefficient cost.

The later adversarially recomputed
[parabolic coefficient-tail theorem](adjoint-pressure-parabolic-coefficient-tail.md)
closes that frequency-identification gap.  Every selected complete
feedback packet forces actual coefficient dissipation above
\(h^{-1/2}\sqrt{\log(1/h)}\), of size at least
\(h^{-3+\varepsilon}\).  The remaining boundary is event-index
non-reuse of those nested physical tails, not whether the renewal
escape belongs to the common coefficient.

## 7. Executable ledger

The binary-word partition, last-return resolvent identity, separated
heat-rate entropy, inverse-linear high-output tail, and parabolic
\(9/4\) exponent are checked by

```bash
PYTHONPATH=lab python -m unittest \
  lab.tests.test_adjoint_pressure_last_return -v
PYTHONPATH=lab python -m \
  navier_lab.adjoint_pressure_last_return
```
