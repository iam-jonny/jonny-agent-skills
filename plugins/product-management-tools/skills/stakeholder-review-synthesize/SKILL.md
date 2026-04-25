---
name: stakeholder-review-synthesize
description: Synthesize stakeholder review comments, meeting notes, approval discussions, PRD feedback, roadmap feedback, and objections into decisions, unresolved issues, action items, artifact edits, and follow-up communication. Use after review meetings or async comment rounds.
---

# Stakeholder Review Synthesize

## Shared Reference

Use `../../references/product-management-principles.md` for general product
management principles. Apply delivery, metrics, prioritization, roadmap, and
common failure mode sections when turning feedback into decisions and next
steps.

## Synthesis Stance

Treat feedback as decision input. Do not flatten all comments into equal tasks.
Separate approvals, blockers, objections, suggestions, questions, and unrelated
opinions. Preserve who said what when attribution affects decision making.

## Workflow

1. Identify the artifact reviewed, review format, participants, and decision
   goal.
2. Classify feedback by type: approval, blocker, risk, requirement change,
   scope concern, metric concern, dependency, question, suggestion, or FYI.
3. Extract decisions made, decisions deferred, and action items.
4. Identify changes required before approval versus optional improvements.
5. Draft artifact edits, owner assignments, and follow-up communication.
6. Recommend whether to proceed, revise, re-review, or escalate.

## Product Management Principles

- Not every comment should become scope.
- Objections should be converted into decision questions or risk mitigations.
- Approval requires a recorded decision, not only a positive meeting tone.
- Follow-up should reduce ambiguity: what changed, who owns it, and by when.

## Practical Operating Guidance

- Preserve attribution for blockers, approvals, and owner commitments.
- Mark feedback that conflicts with prior decisions or non-goals.
- Distinguish "must resolve before approval" from "can handle during delivery".
- Convert scattered comments into a decision log and edit queue.
- Draft a concise follow-up that prevents "I thought we agreed..." drift.

## Output

Return:

- Review summary.
- Participants and stakeholder positions.
- Decisions made.
- Open decisions.
- Blockers.
- Required artifact changes.
- Optional improvements.
- Action items with owners and due dates when available.
- Risks introduced by feedback.
- Approval state: `Approved`, `Conditionally approved`, `Needs revision`, or
  `Not aligned`.
- Follow-up message draft.
- Recommended next skill: `artifact-alignment`, `prd-review`,
  `business-requirements-review`, `pbi-review`, or `roadmap-review`.

## Common Failure Modes

- Treating every comment as a requirement.
- Losing the distinction between approval conditions and nice-to-have edits.
- Missing unresolved disagreement because the meeting ended politely.
- Failing to assign owners to follow-up work.
- Sending a follow-up that summarizes discussion but not decisions.

## Quality Bar

The output should leave the team with a clear decision log, edit path, and
follow-up message. It should make it obvious whether the artifact can proceed.
