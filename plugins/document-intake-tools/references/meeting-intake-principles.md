# Meeting and Document Intake Principles

Use this reference when turning meeting files and local documentation context
into useful outputs.

## Role

Document intake connects raw files to the right business workflow. It should
classify the input, ask minimal user questions, gather relevant local context,
and route to the right draft, update, or finalize action.

## Meeting Types

Use a small, practical set by default:

- 1on1.
- Huddle.
- Requirements definition.
- Design.
- All Hands.
- Sharing or sync.
- Decision review.
- Stakeholder review.
- Planning.
- Retrospective.
- Incident or postmortem.
- Customer interview.
- Other.

If the meeting type changes the output, confirm it with the user.

## Minimal Questions

Ask only what changes the result:

- What meeting type is this?
- Which product, project, or initiative is related?
- What output mode is needed: Draft, Update, Finalize, or Summary only?
- Which existing document or repository should be referenced?
- Where should the output go: Slack, email, Notion, Confluence, Markdown,
  Word, PowerPoint outline, or other?

## Context Discovery

Local repositories may contain relevant documents:

- README.
- docs/.
- requirements/.
- prd/.
- brd/.
- roadmap/.
- architecture/.
- decisions/.
- adr/.
- project plans.
- status reports.
- CHANGELOG.
- release notes.

Search first, then ask the user to confirm relevant candidates before relying
on them.

## Output Modes

- Draft: create a new artifact with assumptions and open questions.
- Update: identify changes to an existing artifact, with rationale.
- Finalize: prepare a polished, shareable output with decisions, owners, risks,
  and follow-up.
- Summary only: create a concise recap without changing artifacts.

## Routing

Route product artifacts to `product-management-tools`. Route project artifacts
to `project-management-tools`. Use `folder-monitor-tools` only for detection
and scan state, not interpretation.

## Safety

- Do not auto-post sensitive meeting content without confirmation.
- Preserve uncertainty from transcripts or OCR.
- Separate decisions from discussion.
- Identify owners and due dates when available.
- Keep private context out of public outputs unless explicitly requested.
