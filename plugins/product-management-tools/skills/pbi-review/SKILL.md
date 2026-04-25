---
name: pbi-review
description: Review product backlog items, user stories, epics, tickets, and acceptance criteria for clarity, independence, value, testability, sizing risk, dependencies, and readiness for refinement or sprint planning. Use when Codex needs to inspect whether backlog work is actionable for product, design, engineering, or QA.
---

# PBI Review

## Shared Reference

Use `../../references/product-management-principles.md` for general product
management principles. Apply the delivery, metrics, prioritization, and common
failure mode sections when reviewing backlog items.

## Review Stance

Treat each PBI as a delivery contract. Check whether a team can estimate, build, test, and accept the item without hidden product decisions.

## Product Management Principles

- A good PBI is small enough to deliver and verify, but large enough to create
  recognizable user or business value.
- Use INVEST as a practical test: independent, negotiable, valuable,
  estimable, small, and testable.
- Acceptance criteria should describe observable behavior and quality
  expectations.
- A PBI should not hide product decisions that still need discovery or
  stakeholder alignment.

## Practical Operating Guidance

- Check whether the user, job, trigger, expected behavior, and acceptance path
  are clear.
- Flag PBIs that bundle unrelated flows, roles, platforms, or system changes.
- Look for missing edge cases: permissions, errors, empty states, localization,
  accessibility, analytics, privacy, support, and rollback.
- Identify dependencies on design, data, APIs, migration, operations, legal,
  GTM, or release sequencing.
- Rewrite weak PBIs into a user story plus acceptance criteria when useful.

## Checklist

- User value: the beneficiary and value are clear.
- Scope: small enough to deliver and verify.
- Acceptance criteria: observable and testable.
- Dependencies: upstream decisions, data, design, APIs, and releases are named.
- Edge cases: errors, permissions, empty states, localization, accessibility, and analytics are considered when relevant.
- Split quality: item is not an unfocused bundle of unrelated work.

## Common Failure Modes

- The item describes implementation work but not user or business value.
- Acceptance criteria restate the solution instead of observable outcomes.
- The item is too large to estimate or test reliably.
- Dependencies are discovered during sprint execution.
- Analytics, support, migration, and rollback needs are omitted.

## Output

For each PBI, return `Ready`, `Needs refinement`, or `Split/rewrite`. Include the highest-impact fix and a rewritten version when useful.
