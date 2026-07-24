# Fast Type-II records evacuate every carrier-local infrared mode

- **Experiment:** EXP-TYPE-II-TERMINAL-INFRARED-EVACUATION-001
- **Route:** ROUTE-R3C
- **Status:** complete conditional decomposition theorem; external review pending
- **Domain:** smooth finite-energy Navier--Stokes flow on \(\mathbb R^3\)
- **Clay status:** unsolved
- **Inputs:** [carrier entrance](type-ii-inviscid-carrier-entrance.md),
  [carrier defect](type-ii-carrier-defect-compactness.md), and
  [compact-carrier clock](type-ii-compact-carrier-clock.md)

## Verdict

If realised by a smooth finite-energy trajectory in the energy-efficient
branch, the selected amplitude layer of the exact \(q_j=4\) survivor now
has an exhaustive spatial/frequency decomposition.

Let

\[
F_j(y):=R_j^{3/2}u(x_j+R_jy,t_j)
\]

be the complete energy-normalised carrier state.  Its terminal time tail
satisfies

\[
\frac{T^*-t_j}{R_j^{5/2}}
\asymp
\frac{2^{-11j}/j}{2^{-10j}}
=
\frac{2^{-j}}j
\longrightarrow0.
\]

For every fixed carrier ball \(B_A\) and every fixed dimensionless frequency
\(K\),

\[
\boxed{
\|\mathbf1_{B_A}P_{\le K}F_j\|_2\longrightarrow0.
}
\]

Thus no bounded carrier frequency survives locally.  The geometry ledger
becomes:

1. in the diffuse cell, the selected layer energy escapes every carrier
   ball;
2. in every partial or tight cell, a fixed local energy amount lies above
   \(K_j/R_j\) for some \(K_j\to\infty\).

Equivalently, every retained core in the fast branch already contains a
fixed-energy subcarrier tail at a physical length \(R_j/K_j=o(R_j)\).
That tail forces an enstrophy excess by the unbounded factor \(K_j^2\).
Moreover the weak terminal carrier trace is zero, so the retained
partial/tight layer belongs to the positive terminal trace defect rather
than the coherent-trace alternative.

This is a genuine same-trajectory decomposition and an actual Fourier
detector.  It does not yet prove that the ultraviolet tail is the next
record packet, that its energy is fresh, or that repeated tails pay a
nonsummable charge.

## 1. Setup and the super-turnover condition

Let \(u\) be a smooth divergence-free solution on
\(\mathbb R^3\times[0,T^*)\):

\[
\partial_tu+\mathbb P\nabla\!\cdot(u\otimes u)
=\nu\Delta u,
\qquad
\sup_{t<T^*}\frac12\|u(t)\|_2^2\le E_0.
\]

In the first-singular-time setting, continue \(u\) as a Leray--Hopf
solution and denote its weak \(L^2\) trace at \(T^*\) by

\[
u_*\in L^2(\mathbb R^3).
\]

Let

\[
t_j\uparrow T^*,
\qquad
R_j\downarrow0,
\qquad
x_j\in\mathbb R^3,
\]

and suppose the records have a **super-turnover terminal tail**:

\[
\boxed{
h_j:=
\frac{T^*-t_j}{R_j^{5/2}}
\longrightarrow0.
}
\]

Define the unitary carrier rescalings

\[
F_j(y)
:=
R_j^{3/2}u(x_j+R_jy,t_j),
\]

\[
G_j(y)
:=
R_j^{3/2}u_*(x_j+R_jy).
\]

Fix the smooth radial low-pass multiplier \(P_{\le\Lambda}\) from the
compact-carrier theorem, whose symbol lies in \([0,1]\), and put

\[
P_{>K}:=I-P_{\le K}.
\]

## 2. Every old-scale low pass freezes to the terminal trace

### Proposition 1: terminal low-pass freezing

For every fixed \(0<K<\infty\),

\[
\boxed{
\|P_{\le K}(F_j-G_j)\|_2
\le
C_K
\left(E_0+\nu\sqrt{E_0}R_j^{1/2}\right)h_j
\longrightarrow0.
}
\]

Equivalently, in physical variables,

\[
\left\|
P_{\le K/R_j}\bigl(u(t_j)-u_*\bigr)
\right\|_2
\longrightarrow0.
\]

#### Proof

For \(t_j<t<T^*\), the energy-only low-pass estimate gives

\[
\begin{aligned}
&\left\|
P_{\le K/R_j}\bigl(u(t)-u(t_j)\bigr)
\right\|_2\\
&\quad\le
C
\left(
E_0(K/R_j)^{5/2}
+\nu\sqrt{E_0}(K/R_j)^2
\right)(t-t_j).
\end{aligned}
\]

Let \(t\uparrow T^*\).  The left side converges weakly lower
semicontinuously to the expression with \(u_*\); alternatively, for this
fixed physical cutoff the same estimate makes the low-pass trajectory
strongly Cauchy and its weak limit identifies the strong limit.  Hence

\[
\begin{aligned}
&\left\|
P_{\le K/R_j}\bigl(u_*-u(t_j)\bigr)
\right\|_2\\
&\quad\le
C
\left(
E_0K^{5/2}R_j^{-5/2}
+\nu\sqrt{E_0}K^2R_j^{-2}
\right)(T^*-t_j)\\
&\quad=
C
\left(
E_0K^{5/2}
+\nu\sqrt{E_0}K^2R_j^{1/2}
\right)h_j.
\end{aligned}
\]

Carrier covariance of the low-pass multiplier gives the first displayed
estimate.

## 3. A fixed terminal trace becomes carrier-scale spatial escape

### Proposition 2: terminal-trace scaling ledger

For every fixed \(0<K,A<\infty\),

\[
\boxed{
\|P_{\le K}G_j\|_2
\longrightarrow
\|u_*\|_2,
}
\]

but

\[
\boxed{
\|\mathbf1_{B_A}P_{\le K}G_j\|_2
\longrightarrow0.
}
\]

Thus any nonzero terminal-trace component has fixed global norm but escapes
every fixed ball in carrier coordinates.

#### Proof

By scaling covariance,

\[
\|P_{\le K}G_j\|_2
=
\|P_{\le K/R_j}u_*\|_2.
\]

Since \(K/R_j\to\infty\), strong convergence of the low passes to the
identity proves the global limit.

For the local limit,

\[
\begin{aligned}
\|\mathbf1_{B_A}P_{\le K}G_j\|_2
&=
\left\|
\mathbf1_{B_{AR_j}(x_j)}
P_{\le K/R_j}u_*
\right\|_2\\
&\le
\left\|
\mathbf1_{B_{AR_j}(x_j)}u_*
\right\|_2
+
\|P_{\le K/R_j}u_*-u_*\|_2.
\end{aligned}
\]

The second term tends to zero.  For the first, the integrability of
\(|u_*|^2\) gives uniform absolute continuity:

\[
\sup_{x\in\mathbb R^3}
\int_{B_{AR_j}(x)}|u_*|^2\,dx
\longrightarrow0.
\]

This proves the claim uniformly in the moving centres.

## 4. Carrier-local infrared evacuation

### Theorem 3: all bounded carrier frequencies vanish locally

Under the super-turnover condition, for every fixed \(0<A,K<\infty\),

\[
\boxed{
\|\mathbf1_{B_A}P_{\le K}F_j\|_2
\longrightarrow0.
}
\]

At the same time,

\[
\boxed{
\|P_{\le K}F_j\|_2
\longrightarrow
\|u_*\|_2.
}
\]

Consequently

\[
F_j\longrightarrow0
\quad\hbox{in }\mathcal D'(\mathbb R^3)
\]

and strongly in \(H^{-s}_{\mathrm{loc}}(\mathbb R^3)\) for every \(s>0\).

#### Proof

The two norm assertions follow immediately by combining Propositions 1 and
2.

Let \(\varphi\in C_c^\infty(\mathbb R^3)\).  Since the multiplier is
self-adjoint,

\[
\begin{aligned}
|\langle F_j,\varphi\rangle|
&\le
|\langle P_{\le K}F_j,\varphi\rangle|
+
|\langle F_j,(I-P_{\le K})\varphi\rangle|\\
&\le
\|\mathbf1_{\operatorname{supp}\varphi}P_{\le K}F_j\|_2
\|\varphi\|_2\\
&\qquad
+
\sup_j\|F_j\|_2
\|(I-P_{\le K})\varphi\|_2.
\end{aligned}
\]

First let \(j\to\infty\) with \(K\) fixed, then let \(K\to\infty\).
This proves distributional convergence.  On each fixed ball the sequence is
bounded in \(L^2\), whose embedding into \(H^{-s}\) is compact.  Every
strong \(H^{-s}\) subsequential limit is the distributional limit zero, so
the whole sequence converges strongly.

### Interpretation

There are two visibly different components:

1. if \(u_*=0\), every fixed global carrier low pass vanishes, so all
   nonvanishing carrier energy escapes to dimensionless frequency infinity;
2. if \(u_*\ne0\), the fixed global low-pass norm tends to \(\|u_*\|_2\),
   but that entire component escapes spatially in the carrier coordinates.

In either case, bounded carrier frequencies contain no local core.

## 5. Exact geometry decomposition

Return to the energy-efficient Type-II layer.  Recall

\[
A_j:=\{a_j<|u(t_j)|\le2a_j\},
\qquad
e_j:=\int_{A_j}|u(t_j)|^2\,dx,
\qquad
e_j\ge c_0>0,
\]

and let \(\theta\in[0,1]\) be the canonical carrier concentration parameter.

### Theorem 4: diffuse escape or a fixed ultraviolet core

After the standard geometry subsequence, exactly the following alternatives
hold.

1. **Diffuse geometry, \(\theta=0\).**  No fixed carrier ball around any
   moving centre captures a positive fraction of the selected layer energy.
2. **Partial or tight geometry, \(\theta>0\).**  For every
   \(0<\eta<\theta\), there are fixed \(A<\infty\), centres \(x_j\), a
   number \(\gamma=\eta c_0>0\), and a sequence \(K_j\to\infty\) such that

   \[
   \int_{B_A}|F_j(y)|^2\,dy\ge\gamma
   \]

   and

   \[
   \boxed{
   \int_{B_A}
   |P_{>K_j}F_j(y)|^2\,dy
   \ge\frac{\gamma}{4}.
   }
   \]

   In physical variables,

   \[
   \boxed{
   \int_{B_{AR_j}(x_j)}
   \left|
   P_{>K_j/R_j}u(x,t_j)
   \right|^2\,dx
   \ge\frac{\gamma}{4}.
   }
   \]

Thus the partial/tight core contains fixed energy above a physical
frequency \(K_j/R_j\), or equivalently below a length
\(R_j/K_j=o(R_j)\).

#### Proof

The diffuse statement is the definition of \(\theta=0\).

If \(\theta>0\), the concentration-function construction gives fixed \(A\)
and centres such that

\[
\frac1{e_j}
\int_{A_j\cap B_{AR_j}(x_j)}
|u(x,t_j)|^2\,dx
\ge\eta
\]

eventually.  Since \(e_j\ge c_0\), carrier scaling gives

\[
\int_{B_A}|F_j|^2\,dy
=
\int_{B_{AR_j}(x_j)}|u(x,t_j)|^2\,dx
\ge\gamma.
\]

For every fixed \(K\), Theorem 3 and the triangle inequality imply

\[
\begin{aligned}
\|\mathbf1_{B_A}P_{>K}F_j\|_2
&\ge
\|\mathbf1_{B_A}F_j\|_2
-
\|\mathbf1_{B_A}P_{\le K}F_j\|_2\\
&\ge
\sqrt\gamma-o_j(1).
\end{aligned}
\]

For each integer \(n\ge1\), choose strictly increasing thresholds
\(J_n\to\infty\) so that the last low-pass norm is at most
\(\sqrt\gamma/2\) whenever \(j\ge J_n\) and \(K=n\).  For \(j\ge J_1\),
define \(K_j:=\max\{n:J_n\le j\}\), assigning arbitrary positive values
before \(J_1\).  This gives a staircase \(K_j\to\infty\).  Squaring gives
the claimed \(\gamma/4\) floor.  Fourier and carrier covariance give the
physical statement.

### Corollary 5: unbounded future-scale frequency depth and enstrophy excess

In the partial or tight alternative,

\[
\boxed{
\|\nabla u(t_j)\|_2^2
\ge
\frac{\gamma}{4}
\frac{K_j^2}{R_j^2}.
}
\]

For the exact \(q=4\) radii, there are integers \(N_j\to\infty\) such that
the detected high-pass component is supported beyond the carrier frequency
of record \(j+N_j\).

#### Proof

The multiplier \(P_{>K_j/R_j}\) vanishes below frequency \(K_j/R_j\) and
has magnitude at most one.  Plancherel and Theorem 4 give

\[
\begin{aligned}
\|\nabla u(t_j)\|_2^2
&=
\int |\xi|^2|\widehat u(\xi,t_j)|^2\,d\xi\\
&\ge
\frac{K_j^2}{R_j^2}
\|P_{>K_j/R_j}u(t_j)\|_2^2\\
&\ge
\frac{K_j^2}{R_j^2}
\|\mathbf1_{B_{AR_j}(x_j)}
P_{>K_j/R_j}u(t_j)\|_2^2\\
&\ge
\frac{\gamma}{4}\frac{K_j^2}{R_j^2}.
\end{aligned}
\]

When \(R_j=2^{-4j}\), put

\[
N_j:=\left\lfloor\log_{16}K_j\right\rfloor.
\]

Then \(N_j\to\infty\) and

\[
\frac{K_j}{R_j}
\ge
\frac{16^{N_j}}{R_j}
=
\frac1{R_{j+N_j}}.
\]

The Fourier support of the detected component therefore lies beyond the
carrier frequency of an unbounded number of future generations.

This is schedule-relative frequency depth only.  It identifies neither a
causal descendant nor any later carrier.

This is an instantaneous enstrophy lower bound, not a spacetime charge.
Without a residence estimate for the detected tail, finite total
dissipation does not yet contradict it.

### Corollary 6: the coherent terminal carrier trace is absent

In every partial or tight energy-efficient cell satisfying the
super-turnover condition, the carrier weak trace obeys

\[
\boxed{
V(0)=0.
}
\]

The retained layer floor therefore lies entirely in the positive terminal
trace defect:

\[
\boxed{
\mathcal T_0(B_{A+1})\ge\eta
}
\]

with the notation of the carrier-defect theorem.

#### Proof

Recall

\[
F_j=\sqrt{b_j}\,v_j(\cdot,0),
\qquad
0<c\le b_j\le C.
\]

After a scalar subsequence, \(b_j\to b>0\).  Theorem 3 gives
\(v_j(\cdot,0)\to0\) in distributions, so the carrier-defect weak trace is
\(V(0)=0\).  The retained-layer theorem there states

\[
\int_{B_{A+1}}|V(0)|^2\,dy
+\mathcal T_0(B_{A+1})
\ge\eta.
\]

The first term now vanishes.

This eliminates only the nonzero **terminal** coherent-trace alternative on
the super-turnover branch.  It does not prove that an ancient weak carrier
field vanishes at negative times.

## 6. The exact \(q=4\) audit

The representative ledger has

\[
R_j=2^{-4j},
\qquad
T^*-t_j
\asymp
\frac{2^{-11j}}j.
\]

Therefore

\[
h_j
=
\frac{T^*-t_j}{R_j^{5/2}}
\asymp
\frac{2^{-j}}j
\longrightarrow0.
\]

The two errors in Proposition 1 are explicitly

\[
E_0K^{5/2}\frac{2^{-j}}j
\]

and

\[
\nu\sqrt{E_0}K^2\frac{2^{-3j}}j.
\]

Both vanish for every fixed \(K\).  Thus Theorems 3 and 4, and Corollary 5,
apply to the exact power survivor.

The smaller defect scale remains

\[
r_j=R_j\ell_j\asymp2^{-5j}.
\]

The theorem proves only that some fixed energy lies at a scale
\(o(R_j)\).  It does not prove that the forced frequency factor \(K_j\)
reaches \(\ell_j^{-1}\asymp2^j\), nor that the detected tail equals the
canonical defect packet.

## 7. Progress and remaining obligation

Subject to external review, this round establishes:

1. an energy-only terminal low-pass freezing estimate for every
   smooth finite-energy super-turnover record sequence;
2. complete carrier-local evacuation of bounded frequencies;
3. an exhaustive diffuse-space versus fixed-energy-ultraviolet-core split
   for the selected amplitude layer (not for unrelated local energy);
4. an actual physical high-pass detector at frequency \(K_j/R_j\);
5. unbounded future-scale frequency depth and a \(K_j^2\) enstrophy excess;
6. zero terminal weak carrier trace in every retained-core cell; and
7. assignment of the retained layer floor to the positive terminal trace
   defect.

It does not establish:

1. a rate for \(K_j\to\infty\);
2. identification of the ultraviolet tail with the next first-record
   carrier;
3. freshness or orthogonality of successive tails;
4. a nonsummable dissipation, flux, spatial-import, or variation charge;
5. exclusion of the diffuse geometry;
6. control of the divergent-normalised-energy branch; or
7. regularity, breakdown, or any Clay alternative A--D.

The next exact question is:

> Does the first-record condition force the ultraviolet core detected at
> \(t_j\) to contain the later carrier at \(t_{j+1}\), or else force fixed
> spatial import across the carrier boundary?

No executable artefact is added: the content is an analytic terminal-trace
and Fourier compactness theorem, not a finite computation.
