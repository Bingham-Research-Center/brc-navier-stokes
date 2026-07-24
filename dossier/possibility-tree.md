# Possibility tree

The tree is a falsifiable partition of current routes, not a claim that mathematics has
already supplied a finite exhaustive taxonomy. Any uncovered scenario creates a new
node. The machine-readable version is [`records/routes.json`](records/routes.json).

```text
CLAY
├── R  Prove global regularity
│   ├── R1  Derive a universal critical bound
│   │   ├── R1a  velocity endpoint control
│   │   ├── R1b  vorticity-direction depletion
│   │   ├── R1c  frequency-flux/cascade barrier
│   │   └── R1d  analyticity versus geometric sparseness
│   ├── R2  Minimal-blow-up reduction
│   │   ├── R2a  concentration compactness
│   │   ├── R2b  ancient-solution classification
│   │   └── R2c  backward uniqueness / Liouville rigidity
│   └── R3  Remove assumptions from conditional criteria
│       ├── R3a  point core → arbitrary/multiple cores
│       ├── R3b  imposed direction control → equation-derived control
│       └── R3c  fixed critical profile → general Type-II dynamics
└── B  Prove breakdown
    ├── B1  Unforced smooth-data singularity
    │   ├── B1a  backward self-similar or discretely self-similar
    │   ├── B1b  non-self-similar physical-space concentration
    │   └── B1c  frequency cascade implementing the true nonlinearity
    ├── B2  Smooth-forced Clay construction
    │   ├── B2a  whole-space rapidly decaying force
    │   └── B2b  periodic smooth force
    └── B3  Bridge rough/singular-data mechanisms to Clay data
        ├── B3a  unstable forward self-similar profiles
        ├── B3b  positive-time matching from a smooth prehistory
        └── B3c  certified instability plus exact continuation failure
```

## Classification axes

Every candidate singularity or exclusion theorem must state its cell on each axis.

| Axis | Values initially tracked |
|---|---|
| Domain | \(\mathbb R^3\), \(\mathbb T^3\) |
| Force | zero, smooth allowed force |
| Time rate | Type-I, Type-II, unknown |
| Similarity | continuous, discrete, asymptotic, none |
| Geometry | point, curve/tube, sheet, multi-core, diffuse |
| Scale behavior | single scale, cascade, scale oscillation |
| Location | physical space, frequency space, coupled |
| Symmetry | general, axisymmetric with/without swirl, other |
| Solution class | classical, mild/strong, suitable, Leray–Hopf, weaker |

## Closure rule for a node

A route node closes only by one of these records:

1. **Exclusion theorem:** exact assumptions cover the node and imply regularity.
2. **Reduction theorem:** every object in the node maps into already closed children.
3. **Construction:** an exact example satisfies the node and its terminal Clay
   quantifiers.
4. **Logical redundancy:** the node is proven equivalent to or contained in another
   tracked node.

Numerical absence, physical implausibility, and failure to find an example do not close a
node.

## The three highest-leverage bridges

### Universal logarithmic depletion

Show that the true viscous dynamics force *some* vanishing control of stretching on every
shrinking high-vorticity region. This would turn geometric conditional criteria into a
global argument. The 2607.08866 audit probes one proposed version.

### Minimal-object rigidity

Assume failure, rescale around the most economical concentration, extract a compact
ancient solution, then show energy, pressure, and unique continuation force it to vanish.
The hard step is gaining enough compactness at a supercritical energy level.

The current ROUTE-R3B distance normalization gives a conditional
two-singularity suitable weak-\(L^3\) ancient profile. Local terminal
singular-set finiteness excludes exact continuous and discrete
self-similarity, so the surviving cell is B1b with genuinely
scale-aperiodic physical-space concentration. The subsequent countable
packing theorem permits only finitely many distinct positive limiting
satellite radii in one distance profile and forces every radially ordered
infinite tower to have adjacent-distance ratio liminf zero. The surviving
cell therefore consists of finite or radially collapsed clusters separated
by arbitrarily severe gaps. Inter-satellite compactification and the
quantitative local singular count now bound every microscopic tangent
cloud by one uniform branching number; overcrowding instead forces a
packet-to-cluster no-neck ratio. The remaining cell is an infinite-depth,
uniformly finite-branching hierarchy. An exact divergence-free
log-quasiperiodic terminal trace shows that both weak critical endpoints,
two locally finite non-locally-bounded spatial points, absence of exact
DSS, compact
aperiodic scale recurrence, and a uniform positive Besov quotient defect
can coexist without any additive log-depth bound. This is not a
Navier--Stokes solution, but it closes the depth-charge shortcut based
only on that retained package of marks. The next closure test is a
genuinely dynamical
scale-hull Liouville theorem, same-trajectory signed flux, Lyapunov
quantity, or backward-uniqueness law for the coherent ancient suitable
profile.

On the adjoint-pressure subroute, intermediate localisation now excludes
the inverse-cubic source-localised feedback payer and forces
stretched-exponential coefficient dissipation. A reviewed scalar
ledger-realisation shows that finite physical dissipation, absolute
continuity, nested terminal intervals, and the exact physical scale map
still permit the zoom to outrun that exponential while all fresh raw
increments telescope. The surviving cell therefore requires genuinely
PDE zoom--history coupling, a non-reusable signed or vector charge,
actual next-event ancestry, or a stronger causal interaction-order law.
The reviewed Stokes--Duhamel induction already forces the pressure packet
beyond
\[
N(h)=\left\lfloor c_{\rm dep}\log\frac1h\right\rfloor
\]
interactions: the removed iterates have total pressure
\(O(h^{33/32})\), while the exact remainder \(T_b^{N(h)}r\) retains the
floor.  The surviving causal node is therefore summability or
quasi-nilpotence beyond logarithmic depth, not merely a fixed later
interaction.  A raw energy telescope is no longer an open shortcut.

The positive norm-majorant version of that node is now closed as well.
The reviewed critical Hardy--Volterra operator
\[
(\mathsf H_\gamma f)(t)
=B(\gamma,1-\gamma)^{-1}
\int_0^t(t-s)^{\gamma-1}s^{-\gamma}f(s)\,ds
\]
has \(\mathsf H_\gamma^m1=1\) at every depth, whereas any fixed positive
time-power gain gives \(C^m/(m!)^\gamma\) decay.  Barker's available
\(\nabla b\in L^{2+\delta_B}_{x,t}\) gain lies strictly below the
threshold \(\delta=1/2\), the exact threshold for a positive same-space Oseen
time margin.  Changing Lebesgue exponents only adds a bounded
telescoping endpoint correction, and weak-\(L^3\) interpolation stays
super-Serrin.  At the threshold the generated velocity pair is already
\(L^{5/2}_tL^{15}_x\), on the Prodi--Serrin regularity line.  The
surviving node must therefore use solenoidal/tensor or pressure
cancellation, actual trajectory ancestry, or another PDE input invisible
to a positive scalar causal majorant.

The abstract skew/Hodge version of that escape is now closed as well.
For the exact projected transport blocks
\[
A_b=\mathbb P(b\cdot\nabla)\mathbb P,
\qquad
C_b=(I-\mathbb P)(b\cdot\nabla)\mathbb P,
\]
\(A_b\) is skew and \(C_b\) is the adjoint-pressure observation, but
\[
-\mathbb P B_b^2\mathbb P=A_b^*A_b+C_b^*C_b
\]
is weighted by \(B_b^*B_b\) and does not telescope over powers of \(A_b\).
A reviewed critical skew-compression model retains unit absolute pressure
at every interaction depth despite uniform real-coupling energy stability.
A unitary one-step replacement telescopes only squared leakage; its exact
small-step limit can retain order-one linear leakage while the squared
defect vanishes.  The independently reviewed exact monomial refinement
\(r_\eta(t)=t^\eta e_1\) retains that nondecay at every fixed algebraic
trace order; \(\eta=1\) has a genuine linear zero right trace.  This is
still not an Oseen counterexample, because it does not realise the
componentwise spatial transport/heat relation.  The first such spatial
block is now controlled: the reviewed fixed-band theorem makes every
repeatedly re-filtered parabolic annulus factorially summable in
interaction depth, including the reviewed logarithmic depth after any
fixed polynomial input loss.  Hence the surviving node is specifically a
summable **multiscale frequency-itinerary** or pressure-recombination
estimate, a same-trajectory signed law, or event ancestry.  A surviving
packet must leave every fixed comparable-frequency corridor.

The reviewed dyadic Zeno countermodel now closes the norm-only version
of that surviving node.  The sharp cross-band kernel has mass \(R/S\);
an upward dyadic path therefore loses \(2^{-m}\), but its summable heat
clocks fit inside mean time \(1/3\), and a terminal high--high-to-low
Hodge observation gains \(2^m\).  The resulting finite-horizon pressure
has a depth-uniform positive floor at every fixed algebraic strong
zero-trace order.  A critical packet ledger simultaneously has bounded
weak-\(L^3\) tail charge and finite energy and dissipation.  Exact
finite-depth complex Fourier modes realise the selected divergence-free
Leray blocks and terminal Hodge return, eliminating elementary
polarisation incompatibility as an escape.  They do not realise one
uniformly weak-\(L^3\), spatially localised drift or control its full
cross-interaction sum.  The surviving node is therefore a genuinely
same-trajectory localisation/overlap, signed pressure-recombination,
coefficient-charge, or event-ancestry theorem—not another positive
cross-band majorant.

The reviewed terminal-return theorem now supplies the first
same-trajectory coefficient charge.  Littlewood--Paley support,
adjoint \(L^2\) energy, and coefficient dissipation give the complete
high--high input tail the bound
\[
\int_0^T\|\Pi_S\mathcal H_{>L}(z,b)\|_1\,dt
\lesssim
\frac SL\sqrt T\,
\|z\|_{L^\infty_tL^2_x}D_{b,>L}^{1/2}.
\]
Thus an order-one low-band return costs \(D_{b,>L}\gtrsim L^2\) on a
fixed unit window, and \(D_{b,>L}(h)\gtrsim L^2h^{-3}\) for the
zero-data terminal remainder.  The scalar Zeno reciprocal terminal
gain is therefore incompatible with a uniformly energy-bounded state
and fixed finite coefficient dissipation.  After physical pullback the
charge is \(\sigma L^2h^{-3}\).  Finite physical spacetime enstrophy
makes its global high-frequency tail vanish, forcing
\[
\sigma_jL_j^2h_j^{-3}\to0.
\]
At the reviewed logarithmic depth this becomes
\(\sigma_j=o(h_j^{3+2c_{\rm dep}\log2})\).  Successive tails are still
nested.  The surviving node is now to contradict this explicit upper
ceiling with a stronger lower top-frequency law, make the vanishing
nested charge quantitatively non-reusable, or force an
event-scale/next-event ancestry relation.

The reviewed exact ancestry-survivor theorem closes the bare identity
version of the last proposal.  It recursively chooses the selected
events so that
\[
\sigma_{j+1}=\frac{\sigma_j}{L_j},
\qquad
\frac{L_j}{\sigma_j}=\frac1{\sigma_{j+1}},
\]
yet one finite nonnegative time--frequency history pays the exact
terminal-return tail mass
\[
A\sigma_jL_j^2h_j^{-3}
\]
above that next-event reciprocal frequency at every node.  The mass and
its fraction of the total physical dissipation both vanish.  The
reviewed polynomial frequency
\(L(h)\asymp h^{-c_{\rm dep}\log2}\) is
stretched-exponentially below
\[
L_{\rm kill}
=\frac{h^{3/2}}{\sqrt{\sigma}}
=e^{ac h^{-7/4}/2}.
\]
For \(x=h^{-7/4}\) and \(q_j=x_{j+1}/x_j\), exact ancestry makes
\(q_j=3/2\) the constant-charge boundary; tail continuity requires
\[
acx_j(3-2q_j)-\frac6p\log q_j\to+\infty.
\]
The survivor has \(q_j\to1\).  The remaining node therefore needs a
quantitative PDE ancestry gap, a top-frequency law approaching
\(L_{\rm kill}\), or a non-reusable signed/vector/spacetime charge—not
merely a name-level identification of current frequency with next
event scale.

The reviewed spatial--frequency theorem now charges one precise
high-frequency child.  If a fixed low-band pressure fraction is carried
by state frequencies above \(F(h)\to\infty\), then
\[
D_b(h)
\ge
h^{-3}
\exp\!\left(c\frac{F(h)}S h^{-7/4}\right).
\]
Thus \(F=h^{-\beta}\) raises the stretched exponent from \(7/4\) to
\(7/4+\beta\), and physical absolute continuity forces the matching
accelerated upper bound on \(\sigma_h\).  This is conditional on a
high-state pressure floor.  Causal depth alone does not supply that
floor, so the surviving child is now an exhaustive frequency-itinerary
theorem: force terminal high-state participation, or charge histories
which return below \(F\) before the final pressure observation.

The reviewed amplified-ancestry survivor closes the bare combination of
that stronger cost with exact event ancestry.  For \(F=h^{-\beta}\), the
new stretched coordinate is \(y=h^{-(7/4+\beta)}\).  The scalar history
can saturate
\[
D=h^{-3}e^{cy},
\qquad
\sigma=h^3e^{-acy},
\]
and choose every next event so that
\[
\sigma_{j+1}=\sigma_j/F_j,
\qquad
F_j/\sigma_j=1/\sigma_{j+1},
\]
while its total physical mass and complete quadratic terminal-return
tail both vanish.  Hence exponent amplification plus bare ancestry is
not an arithmetic contradiction.  The remaining child must prevent the
accelerated zoom by a PDE law, force terminal high-state participation,
charge returned-low histories, or produce a signed/vector increment
which the nested scalar measure cannot reuse.

The reviewed one-return theorem now charges one genuine returned-low
component.  A state tail above \(64F\) which makes one heat--Leray Oseen
return into the annulus \(F\) before producing fixed low-band pressure
obeys
\[
\mathfrak R^{(1)}_{S,F}(h)
\lesssim
M\frac SF\min\{1,F^2h\}
\left\{
1+h^{7/4}[1+\log_+(D_bh^3)]+o(1)
\right\}.
\]
At \(F=h^{-\beta}\), a fixed one-return fraction forces exponent
\[
\gamma_1(\beta)
=\frac94+\left|\beta-\frac12\right|
\ge\frac94.
\]
Thus one separated final downcrossing cannot evade amplification.  The
reviewed multistage-path theorem now controls any one prescribed
continuation
\[
R_0\longrightarrow\cdots\longrightarrow R_m\longrightarrow S.
\]
Every intermediate cross-band ratio telescopes, leaving \(S/R_0\) and
the distribution function of \(m+1\) exponential heat clocks.  Fixed
depth retains the same one-return exponent.  A logarithmic dyadic
descent with \(n\) slow clocks has ceiling \(2^{-n(n-1)}/n!\), which
beats every fixed interaction constant raised to that depth.

The reviewed full-corridor theorem now sums the remaining path entropy.
For every ceiling \(U\), all finite paths with \(R_j\le U\), including
arbitrary dyadic jumps and arbitrary depth, have an absolutely
convergent recombined pressure series.  The infinite lower-band count is
paid by
\[
h\sum_{Q\le U}c\nu Q^2,
\]
which is finite.  If \(F=h^{-\beta}\), \(0<\beta\le1/2\), and
\(F\le U\lesssim h^{-1/2}\), a fixed corridor floor forces exponent
\(11/4-\beta\ge9/4\).  The reviewed smooth-layer identification theorem
now proves that this pressure series is exactly the truncated
LP--Dyson mild continuation on each fixed smooth genealogy layer.  It
also sums every separated starting-return band below \(U\); a
parabolic aggregate floor forces the \(9/4\) exponent.  Every fixed
layer has a finite capture ceiling.  The reviewed last-separated-return
renewal theorem now partitions every feedback Dyson word exactly into
an all-complementary word or a word grouped by its last chargeable
separated return.  Hence a complete pressure floor yields the
exhaustive trichotomy: a fixed no-chargeable-feedback-return pressure
floor, superparabolic LP--Dyson capture escape for the last-return
block, or the \(9/4\) stretched-exponential coefficient cost.
Separated-return participation is no longer an antecedent.  The
reviewed no-return parabolic-exclusion theorem then sums every
all-complementary path and every starting band below \(U\), obtaining
\[
\|\mathscr P_{S,b}r_{{\rm no},U}\|_1
\lesssim
Sh^{7/4}(e^{A_{\rm no}H_U}-1).
\]
Thus the no-chargeable-return block also cannot carry fixed pressure
under a parabolic ceiling.  The returned-low tree now has one common
live child: superparabolic LP--Dyson capture escape.  The independently
reviewed parabolic coefficient-tail theorem now charges that child in
the actual coefficient spectrum.  Every fixed feedback packet forces
\[
D_{b,>\,h^{-1/2}\sqrt{\log(1/h)}}^\chi(h)
\gtrsim_\varepsilon h^{-3+\varepsilon}.
\]
The surviving child is therefore no longer an unphysical
operator-series escape.  The reviewed parabolic tail-ancestry theorem
shows that reaching the next event frequency forces the sharp
relative log-scale ceiling
\[
\limsup
\frac{\log(1/\sigma_{j+1})}{\log(1/\sigma_j)}
\le\frac76,
\]
but does not force finite empirical roof mean.  Its smooth kinematic
survivor realises the terminal marks, exact cutoff matching, and every
nested tail payment by placing the dissipation arbitrarily far above
the cutoff.  Bare next-scale coupling and nonnegative tail monotonicity
are closed as sufficient children.  The reviewed
[parabolic tail-to-flux theorem](experiments/adjoint-pressure-parabolic-flux.md)
now forces the actual NSE payment into an exhaustive trichotomy:
comparable-annulus dissipation, inherited high-frequency entrance
energy, or positive signed cumulative flux.  Its exact conservative
shell ledger and Zeno heat-clock schedule show that ordinary high-pass
balances and cumulative flux positivity still do not make the payment
fresh.  The subsequent independently reviewed
[terminal signed-flux ancestry theorem](experiments/adjoint-pressure-inherited-ancestry.md)
uses a fixed-time \(H^1\) tail and last hitting to turn the inherited
branch into pre-event cumulative flux.  It then chooses an
event-adaptive \(R_j\to1\) whose intervening sharp annulus costs less
than \(T_j/4\).  Every sufficiently late event therefore has
\[
\frac{K_j}{\Lambda_j}\to1,
\qquad
\alpha_j,\beta_j\to T^*,
\qquad
\Phi_{K_j}((\alpha_j,\beta_j))
\ge\frac{\nu T_j}{4}.
\]
The live child is now strictly event-index freshness for this forced
terminal flux: a quantitative NSE flux decrement, frequency-locality,
non-Zeno cascade-speed, intervening-event, or telescoping theorem.  The
other branch is the \(9/4\) coefficient cost, which still requires the
same-trajectory clock/zoom closure.
The independently reviewed
[weak-\(L^3\) lower-band decrement theorem](experiments/adjoint-pressure-flux-decrement.md)
now closes the near-lossless flux-decrement child.  At each charged
terminal boundary, a smooth far-low/high/comparable-band split and the
weak-\(L^3\) ceiling force
\[
\nu
\int_{\widetilde J_j}
\|\nabla
Q_{\eta K_j<|\xi|\le K_j}v\|_2^2\,dt
\gtrsim
\left(\frac{\nu}{M}\right)^2
\Phi_{K_j}(\widetilde J_j).
\]
Thus the conservative survivor with relative shell loss tending to zero
is not compatible with the conditional NSE trajectory.  The live child
is narrower: different event bands and intervals may overlap, and a
fresh infinite chain may retain geometrically decaying rather than
near-constant flux.  Bounded overlap, a scale-zero event floor, an
intervening selected event, or a cross-event telescope is still needed.
The independently reviewed
[spectral primal--adjoint pairing audit](experiments/adjoint-pressure-spectral-pairing.md)
closes the bare \(L^2\) version of the event-index telescope.  Its
frequency-localised pairing and shell increments telescope exactly, but
the projected pressure contribution pairs to zero against the
divergence-free projected field.  Periodic same-trajectory Beltrami
examples retain nonzero projected pressure with zero localised pairing,
including a high--high-to-fixed-low return.  They do not have the
uniform energy/dissipation genealogy required by the terminal toll and
do not exclude a mixed functional.  The live child is therefore
strictly pressure-visible: pressure-polar \(L^1\), spatial pressure
boundary flux, a controlled divergence defect, or direct ancestry
coupled to the annulus/inheritance/flux trichotomy.
The independently reviewed
[spatial cutoff-flux audit](experiments/adjoint-pressure-spatial-pairing.md)
closes the bare spatial-current child.  In canonical displayed gauges,
an exact periodic Beltrami NSE trajectory and its Oseen adjoint cancel
the pressure and transport currents pointwise.  In every pressure gauge,
the total current divergence and every cutoff-gradient pairing vanish,
despite positive adjoint-pressure history; the high--high-to-fixed-low
family has the same cancellation.  The live pressure-visible child must
therefore separate the pressure component and control cancellation,
use a canonically gauge-fixed current norm, retain a summable divergence
defect, or bypass the pressure telescope by direct ancestry.

### Singular-to-smooth construction bridge

Certified forward self-similar solutions from singular data provide exact unstable
objects. A breakdown proof would need to connect one to a smooth earlier state—or use an
admissible smooth force—without smuggling the singularity into the initial data or force.

## Adversarial coverage test

For every proposed “complete” argument, construct a survivor table asking whether it
covers:

- multiple concentration centers moving in time;
- anisotropic tubes or sheets rather than balls;
- Type-II rates and oscillatory rescaling;
- energy arriving from far field or distant frequencies;
- vorticity-direction defects at zeros;
- loss of compactness through translation, dilation, or frequency drift;
- the exact endpoint rather than every nearby exponent.

Any “unknown” answer remains an open branch.
