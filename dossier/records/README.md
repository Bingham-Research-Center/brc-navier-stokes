# Research records

These JSON ledgers are the stable interface between prose, proof obligations, and code.

## Record types

- **Source:** exact bibliographic object, version, review status, and last verification.
- **Claim:** one proposition with quantifiers, assumptions, conclusion, provenance, and
  epistemic status.
- **Route:** one branch of the regularity/breakdown possibility tree with a success and
  kill criterion.
- **Experiment:** a falsifiable test with invariants, artifacts, and certificate policy.
- **Obligation:** one independently closable arrow in a paper's proof.

The public type definitions are in
[research-ledgers.schema.json](../../lab/schemas/research-ledgers.schema.json). The
dependency-free validator is **lab/navier_lab/records.py**.

## Status semantics

### Claims

- **established:** supported by a primary peer-reviewed theorem.
- **established_reading:** the conclusion follows from a peer-reviewed proof
  via an explicit in-repository reading or extension; the statement is not
  verbatim in the source and external confirmation is pending.
- **repaired_source_theorem:** a peer-reviewed proof supports the recorded
  corrected statement, but the statement is not a verbatim published theorem
  and external confirmation of the repair is pending.
- **conditional_preprint:** a conditional theorem stated in a preprint; the record's
  audit field says whether independent checking is pending or complete.
- **preprint_claim:** a preprint's reported result, not yet independently reproduced here.
- **official_status:** time-sensitive status from an official authority.
- **definition:** controlling formulation or convention.
- **open:** an explicit unsolved proposition.

### Routes

- **closed:** the route's question is closed by an argument unconditional at
  its entry assumptions.
- **closed_conditional:** the route's question is closed only inside a
  recorded conditional chain; antecedent claims keep their own status and no
  unconditional closure is asserted.

### Obligations

- **open:** no matching proof or counterexample recorded.
- **partially_mechanized:** some algebra is checked, but analytic content remains.
- **verified:** independently checked with matching hypotheses.
- **repaired:** the original step needed a documented correction that now closes.
- **unsupported:** a counterexample or unrepairable gap defeats the stated step.

No status is upgraded by prose alone. Add evidence and rerun **make check**.

## Review hygiene

Proof notes and these records are canonical.  Incorporated review
correspondence is removed; the compact
[review ledger](../review-ledger.md) preserves high-consequence dispositions
and exact Git recovery points.  Same-system review is adversarial
recomputation, never external confirmation.  Generate any new external packet
from the current proof rather than stale correspondence.

## Churn rule

A routine frontier result changes one proof note, its canonical record, and
`HANDOFF.md`.  Change `status.md` only for a durable result or gate, and the
possibility tree only when a node changes.  Never mirror a derivation across
those surfaces.  Add executable artefacts only when they can catch a
nontrivial finite error.
