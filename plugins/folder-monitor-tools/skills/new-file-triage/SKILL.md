---
name: new-file-triage
description: Triage newly detected local files by type, likely source, meeting/document category, sensitivity, and downstream workflow. Use after a folder scan finds candidate files that need routing before summarization or artifact updates.
---

# New File Triage

## Shared Reference

Use `../../references/folder-monitoring-principles.md` for routing and safety
guidance.

## Triage Stance

Do not read more content than needed to decide routing. Identify file type,
likely source, sensitivity, and the next workflow. Ask for user confirmation
when the meeting type or destination is ambiguous.

## Workflow

1. Identify file extension, name, path, size, and modified time.
2. Infer likely source: Zoom transcript, meeting note, export, PDF, Word,
   Markdown, or other.
3. Recommend meeting/document type candidates.
4. Identify sensitivity and whether automatic Slack posting is appropriate.
5. Route to `document-intake-tools` with the right prompt.

## Output

Return:

- File summary.
- Likely source.
- Suggested meeting or document type.
- Sensitivity concerns.
- Recommended downstream skill.
- User questions needed before processing.
- Suggested prompt for the downstream skill.

## Quality Bar

When unsure, ask concise confirmation questions instead of guessing the meeting
type or posting destination.
