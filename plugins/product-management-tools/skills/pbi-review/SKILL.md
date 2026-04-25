---
name: pbi-review
description: Review product backlog items, user stories, epics, tickets, and acceptance criteria for clarity, independence, value, testability, sizing risk, dependencies, and readiness for refinement or sprint planning. Use when Codex needs to inspect whether backlog work is actionable for product, design, engineering, or QA.
---

# PBI Review

## Review Stance

Treat each PBI as a delivery contract. Check whether a team can estimate, build, test, and accept the item without hidden product decisions.

## Checklist

- User value: the beneficiary and value are clear.
- Scope: small enough to deliver and verify.
- Acceptance criteria: observable and testable.
- Dependencies: upstream decisions, data, design, APIs, and releases are named.
- Edge cases: errors, permissions, empty states, localization, accessibility, and analytics are considered when relevant.
- Split quality: item is not an unfocused bundle of unrelated work.

## Output

For each PBI, return `Ready`, `Needs refinement`, or `Split/rewrite`. Include the highest-impact fix and a rewritten version when useful.
