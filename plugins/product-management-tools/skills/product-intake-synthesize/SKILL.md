---
name: product-intake-synthesize
description: Synthesize messy product inputs such as meeting notes, call transcripts, paper-note OCR, Slack threads, stakeholder requests, and rough bullets into structured product context. Use before BRD or PRD creation when inputs mix facts, opinions, decisions, requests, risks, and solution ideas.
---

# Product Intake Synthesize

## Shared Reference

Use `../../references/product-management-principles.md` for general product
management principles. Apply the discovery, delivery, metrics, prioritization,
and common failure mode sections when turning raw input into product context.

## Synthesis Stance

Treat raw input as signals, not requirements. Separate what was said from what
was decided, and separate problems from solution ideas. Preserve uncertainty
instead of over-cleaning the input into false agreement.

## Workflow

1. Identify input source and reliability: transcript, meeting notes, OCR,
   chat, interview, stakeholder request, or mixed notes.
2. Extract confirmed facts, claims, assumptions, decisions, open questions, and
   action items.
3. Separate customer/user problems, business goals, stakeholder requests,
   solution ideas, constraints, risks, and dependency signals.
4. Note confidence and evidence strength when the input is ambiguous.
5. Recommend the next artifact: BRD, PRD, PBI, roadmap, MVV, alignment plan, or
   more discovery.

## Product Management Principles

- A sentence from a meeting is not automatically a requirement.
- A repeated request may signal a problem, but the underlying problem still
  needs to be named.
- Decisions need owners, dates, and implications.
- Raw notes should preserve disagreement and uncertainty so later artifacts do
  not hide risk.

## Practical Operating Guidance

- Mark OCR or transcript uncertainty explicitly when wording may be wrong.
- Attribute stakeholder positions when names or roles are available.
- Do not ask for every missing detail. Distinguish blockers from assumptions.
- Convert scattered notes into structured product inputs that downstream skills
  can use.
- Call out when BRD is the right next step instead of PRD.

## Output

Return:

- Input summary.
- Confirmed facts.
- User or customer problems.
- Business goals and success signals.
- Stakeholder requests and positions.
- Solution ideas.
- Requirement candidates.
- Constraints and dependencies.
- Risks.
- Decisions already made.
- Decisions still needed.
- Action items.
- Open questions, grouped by blocker vs can-assume.
- Recommended next artifact and next skill.

## Common Failure Modes

- Turning the loudest comment into the main requirement.
- Losing dissenting views during summarization.
- Treating solution ideas as validated user needs.
- Dropping action items or decision owners.
- Presenting uncertain OCR or transcript content as fact.

## Quality Bar

The output should make messy input usable without pretending it is more certain
than it is. It should help a PM decide whether to create a BRD, PRD, alignment
plan, or discovery follow-up.
