# Handoff: R3C boundary heat impulse

**Updated:** 2026-07-25 · **Clay status:** unsolved

**Live route:** `ROUTE-R3C` · `EXP-TYPE-II-BOUNDARY-HEAT-IMPULSE-001`

## Load only

- [Boundary heat impulse](dossier/experiments/type-ii-boundary-heat-impulse.md)
- [`ROUTE-R3C`](dossier/records/routes.json)

## Exact object

For the reversed full-defect entrance, put \(U=v+c\),
\(M=\|U\|_{3,\infty}\), and \(Y=\|\nabla v\|_2\). The weak-zero boundary
term vanishes after fixed-time heat propagation:
\[
v(\tau)=-\int_0^\tau e^{\nu(\tau-s)\Delta}
\mathbb P((U\cdot\nabla)v)(s)\,ds.
\]
\[
\|v(\tau)\|_2^2
=-\int_0^\tau\!\left\langle
(U\cdot\nabla)v,\,
e^{\nu(\tau-s)\Delta}v(\tau)-v(s)
\right\rangle ds.
\]
The subtraction retains \(\langle(U\cdot\nabla)v,v\rangle=0\). This
nonlinear heat-deviation work tends to \(d\), but its density has no sign.

## Forced impulse

With \(f=MY\) and \(I_\alpha f(\tau)=\int_0^\tau(\tau-s)^{\alpha-1}f(s)\,ds\),
\[
\|v(\tau)\|_2\lesssim\nu^{-1/2}I_{1/2}f(\tau),\qquad
\|v(\tau)\|_{3,\infty}\lesssim\nu^{-3/4}I_{1/4}f(\tau).
\]
Hence every small \(h\) and every q4 record satisfy
\[
\int_0^hMY\gtrsim\sqrt{\nu d\,h},\qquad
\left(\int_0^hM^2\right)\left(\int_0^hY^2\right)\gtrsim\nu dh,\qquad
I_{1/4}(MY)(\tau_j)\gtrsim\nu^{3/4}m_j.
\]
In particular \(MY\notin L^{2,q}_\tau\) for every finite \(q\).

## Sharp survivor

For \(\ell=\log(e/s)\),
\[
M_\sharp=s^{-2/11}\ell^{-2/11},\qquad
Y_\sharp=s^{-9/22}\ell^{1/11}
\]
saturates the q4 \(M^2\) tail and \(Y^2\) floor, has
\(M_\sharp Y_\sharp^2=s^{-1}\), and satisfies both fractional impulses.
It is scalar, with no sign, phase, pressure, or same-trajectory content.

## Closed shortcut

The mild formulation and small q4 \(L^2_\tau L^{3,\infty}_x\) tail do not
force zero: the nonlinear impulse is necessarily critical and order one.

## Exact live question / Next bounded cycle

Make the positive heat-deviation work non-reusable across nested q4
detectors. Seek a finite temporal secondary index for \(MY\), an
orthogonal signed frequency decomposition, or a rate making the
strong-drift work negligible.

All results are conditional and await external review. Keep slower clocks,
divergent normalised energy, and R3B separate. No Clay alternative is proved.
