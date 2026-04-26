---
name: artifact-lifecycle-router
description: Decide whether meeting or document intake should create a Draft, update an existing artifact, Finalize a shareable artifact, or produce Summary only. Use when Codex needs to route transcripts or notes into product/project documentation workflows.
---

# Artifact Lifecycle Router

## Shared Reference

Use `../../references/meeting-intake-principles.md` for output modes, routing,
and safety guidance.

## Routing Stance

Choose the lifecycle action based on the user's intent and artifact state. Do
not update or finalize an artifact when the transcript only supports a summary.

## Output Modes

- Draft: create a new artifact with assumptions and open questions.
- Update: propose changes to an existing artifact with rationale.
- Finalize: produce a polished, shareable output with decisions, owners, risks,
  and next steps.
- Summary only: recap without changing artifacts.

## Output

Return:

- Recommended lifecycle mode.
- Target artifact.
- Required context.
- Downstream product/project skill.
- Output destination format.
- Safety or approval notes.

## Quality Bar

Make the distinction between Draft, Update, Finalize, and Summary only clear.
Route to the smallest action that matches the evidence.
