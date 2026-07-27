# Review ledger

This is the durable summary of same-system adversarial recomputation.  It is
not evidence of independent human or external mathematical review.  The
repaired proof notes and canonical experiment records, not the old
correspondence, control the current statements.

## High-consequence dispositions

| Proof surface | Durable disposition |
|---|---|
| [Scale-indexed defect](experiments/scale-indexed-defect.md) | The one-radius shift-stationary PDE process was withdrawn: parent detector and tensor-carrier radii differ, and levelwise subsequences do not create one genealogy.  The two-scale conditional ledger and later same-event synchronisation survive. |
| [Fixed-shell localisation](experiments/fixed-shell-spatial-localization.md) and [continuation clock](experiments/continuation-clock-descent.md) | Restricted to \(\mathbb R^3\), put in one zero-background/Galilean frame, and stated with a safe mild-lifespan constant.  No torus analogue or local Fourier continuation scale is inferred. |
| [Terminal Besov ancestry](experiments/terminal-besov-ancestry.md) | The Albritton--Barker blow-down subspace is used with the critical Navier--Stokes amplitude required by the proof.  This is a proof-consistent repair, not a verbatim published theorem; external confirmation remains pending. |
| [Pressure trace participation](experiments/adjoint-pressure-trace-participation.md) | The first \(h^7\) participation argument and its moving-tube countermodel were rejected.  The repaired finite-band density split gives fixed positive source-cylinder participation. |
| [Terminal satellite tower](experiments/terminal-satellite-tower.md) | Retained only in the stated mild/suitable, first-singular-time, \(\mathbb R^3\) scope after bounded source and localisation clarifications. |
| [Terminal dissipation collapse](experiments/adjoint-pressure-terminal-dissipation-collapse.md) | The projected pairing, Young absorption, and physical scaling were recomputed.  The terminal pullback includes the vanishing genealogy shift \(\varepsilon_n\); this was incorporated before checkpoint `4bc2e6a`. |
| [Logarithmic heat schedule](experiments/adjoint-pressure-logarithmic-heat-schedule.md) | The schedule, Dini exponents, fixed scalar history, and disjoint-packet powers were recomputed with no fatal or major defect.  “Minimal” is restricted to what the heat-kernel majorant certifies; general necessity is not claimed. |
| [Frequency freshness](experiments/adjoint-pressure-freshness-without-floor.md) | Sparse disjoint-band summation, the conditional full retained gap-separated multiplicity bound, and power-survivor summability were recomputed with no fatal or major defect.  The survivor is kinematic and does not realise the NSE lower-band theorem. |
| [Terminal dimension pincer](experiments/type-ii-terminal-dimension-pincer.md) | Same-system adversarial recomputation found no theorem-critical exponent or sign error.  It required three precision repairs now incorporated: the Besov input is an additional surrogate rather than an embedding strengthening, the bounded-band mass occurs on an infinite subsequence, and the exhaustive spectral alternatives need not be mutually exclusive.  External review remains pending. |

Other recorded recomputations accepted only the theorem text's stated
conditional or countermodel scope after their corrections were folded into
that text.  Such acceptance does not make an antecedent true, turn a scalar
survivor into an NSE trajectory, or resolve any Clay alternative.

## External review

| Date | Reviewer | Record |
|---|---|---|
| 2026-07-27 | Claude (Fable 5), external system operated by John Lawson | [Full audit and curation record](reviews/2026-07-27-fable-audit.md): ledger layer structurally clean; q4 scale judged schedule-conditional; five milestones ranked in [the registry](milestones.md); four curation commits (status scoping, registry + router rules, this record, retirement of unreferenced notes). No mathematical claim was changed. This is an external process audit, not yet external review of the mathematics. |
| 2026-07-27 | Claude (Fable 5), second external session | Audit of the curation pass itself; addendum in [section 9 of the record](reviews/2026-07-27-fable-audit.md). Fixed: five stale provenance citations in archival rounds, four unpushed commits, missing round report. Added: the averaging-barrier classification and course round [2026-07-27-external-course-audit](rounds/2026-07-27-external-course-audit.tex), router rules binding new q4 cycles to averaging-breaking structure. No mathematical claim was changed. |

Two earlier external reports (2026-07-24, untracked at the repository
root) were deleted unread; their surviving conclusions are preserved in
section 5 of the linked record. Router rules now require reading and
logging any signed external review file here before deletion.

## Archive

The 54 detailed response transcripts remain recoverable from Git checkpoint
`4bc2e6a`; the paired one-use review requests are recoverable from
`c277792`.  To enumerate or inspect them without restoring them:

```bash
git ls-tree -r --name-only 4bc2e6a dossier | rg 'review-response-'
git show 4bc2e6a:dossier/review-response-2026-07-23.md
```

Future review should start from the current proof note.  Do not commit new
request/response transcripts unless a correction cannot be stated completely
in the proof and canonical record.
