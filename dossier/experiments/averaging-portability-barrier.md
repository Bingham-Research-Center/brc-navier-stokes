# Averaging portability barrier

**Record:** `EXP-AVERAGING-PORTABILITY-BARRIER-001`

**Route:** `ROUTE-R3C` (method audit; no route closure)

**Status:** conditional method classification; external review pending

**Clay status:** unsolved

## Exact claim

Fix Tao's particular finite-time-blow-up averaged Euler bilinear operator
\(\widetilde B_*\). Call a premise **operator-portable** when it has been
proved both for the true Navier--Stokes evolution and for the
\(\widetilde B_*\) evolution, with a finite constant that may depend on
\(\widetilde B_*\).

If a purported global-regularity proof uses only operator-portable premises,
then the same deduction applies to the blowing-up
\(\widetilde B_*\) solution. Therefore no such proof can be valid.

This is a logical corollary of Tao's averaged-equation blow-up theorem, not a
new Navier--Stokes theorem. It does not say that a portable estimate is
useless inside a proof which also uses a true-Navier--Stokes premise.

## Proof

Assume a deduction from premises \(P_1,\ldots,P_N\) concludes that every
smooth solution continues globally. By operator portability, each \(P_i\)
holds for the selected \(\widetilde B_*\) evolution. The same deduction would
therefore continue Tao's finite-time-blow-up solution globally, a
contradiction. Hence at least one premise or inference in a valid
Navier--Stokes regularity proof must distinguish the true nonlinearity from
that averaged operator.

Uniform constants over every averaged operator are neither needed nor
claimed.

## Audit of the current q4 stack

The following parts are common or kinematic:

- energy cancellation and its global energy ledger;
- radial pushforward identities once the corresponding spectral balance is
  available;
- quantile calculus and heat-transform arithmetic applied to such a balance.

The load-bearing transfer estimate
\[
 \|\widetilde B_*(u,u)\|_{\dot H^{-1}}
 \lesssim_{\widetilde B_*}
 \|u\|_{L^{3,\infty}}\|\nabla u\|_2
\]
has not yet been written out for the selected averaged operator. Tao's
rotation, dilation, and order-zero-multiplier representation makes transfer
plausible, but the Lorentz endpoint and every constant still require an
item-by-item proof. Accordingly, “the whole charged q4 stack is portable” is
a candidate classification, not a theorem.

The following inputs are not automatically shared:

- the local energy inequality and energy-measure consequences for suitable
  Navier--Stokes solutions;
- moving-ball carrier identities tied to physical-space transport;
- the true quadratic pressure identity and its local pressure flux;
- exact Fourier-triad convolution support and phase geometry.

An averaged equation can be represented with a scalar pressure after
projection. The missing feature is the canonical local quadratic pressure
structure of the true Navier--Stokes nonlinearity, not “pressure” as a word.

## Two distinct realization obligations

### O-AVG-001a: shell rung

Constructing an energy-cancelling shell trajectory with the broad q4 radial
profile would prove compatibility only with the finite list of budgets
explicitly verified on that model. It would be a useful method countermodel,
but it would not settle every future portable estimate or realize a
Navier--Stokes velocity field.

Failure to construct such a trajectory has no automatic positive
consequence: the obstruction may be an artefact of the chosen shell model.

### O-AVG-001b: Tao-operator rung

Constructing a solution of the selected \(\widetilde B_*\) equation in the
q4 cell would give a genuine operator-relative barrier: any exclusion of
that cell for true Navier--Stokes would have to use a premise not shared by
that evolution.

Proving that the selected averaged class avoids the q4 cell would not by
itself produce a portable charge. The reason could depend on special
features of \(\widetilde B_*\), and a quantitative inequality would still
have to be extracted and transferred separately.

## Balance verdict

The averaging lens is valuable because it identifies where a proof must
eventually spend true-equation structure. It does not establish an exact
portable/non-portable partition of the repository, and it does not make both
branches of either realization attempt decisive. The defensible next use is
an item-by-item transfer audit or a bounded model construction, after Gate 0
has verified the higher-value milestone inputs.

No q4 route is closed here. No regularity, breakdown, energy-equality, or
Clay alternative A--D theorem is asserted.
