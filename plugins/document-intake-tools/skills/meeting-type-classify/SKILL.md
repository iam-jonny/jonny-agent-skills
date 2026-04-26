---
name: meeting-type-classify
description: Classify meeting transcripts, notes, or summaries into practical meeting types such as 1on1, Huddle, Requirements Definition, Design, All Hands, Sharing/Sync, Decision Review, Stakeholder Review, Planning, Retrospective, Incident/Postmortem, Customer Interview, or Other. Use when meeting type affects output format or downstream routing.
---

# Meeting Type Classify

## Shared Reference

Use `../../references/meeting-intake-principles.md` for meeting type taxonomy
and minimal question guidance.

## Classification Stance

Infer the likely meeting type, but ask the user to confirm when the type
changes the output. Keep the choices short and operational.

## Output

Return:

- Primary meeting type.
- Alternative likely types.
- Confidence.
- Signals used.
- Recommended output mode.
- One concise confirmation question when needed.

## Quality Bar

Do not overfit on title alone. Use content signals such as participants,
decisions, design discussion, requirements language, status updates, or
retrospective patterns.
