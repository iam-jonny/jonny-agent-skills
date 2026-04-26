---
name: local-doc-context-gather
description: Search local repositories or documentation folders for relevant context before drafting, updating, or finalizing product or project artifacts. Use when meeting notes reference existing PRDs, BRDs, project plans, architecture docs, decisions, roadmaps, or status documents.
---

# Local Doc Context Gather

## Shared Reference

Use `../../references/meeting-intake-principles.md` for context discovery and
candidate confirmation guidance.

## Gathering Stance

Search broadly, then narrow. Do not assume a matching file is relevant until
the user or content confirms it.

## Search Targets

Prefer likely documentation paths:

- `README*`
- `docs/`
- `requirements/`
- `prd/`
- `brd/`
- `roadmap/`
- `architecture/`
- `decisions/`
- `adr/`
- `CHANGELOG*`
- `release-notes/`

## Output

Return:

- Search roots.
- Relevant document candidates.
- Why each candidate may matter.
- Recommended files to inspect.
- User confirmation question when multiple candidates compete.
- Suggested downstream workflow.

## Quality Bar

Avoid dumping every match. Return the smallest useful candidate set with clear
relevance reasons.
