---
name: prd-review
description: Review product requirements documents for clarity, completeness, user value, measurable outcomes, scope control, feasibility, risks, acceptance criteria, dependencies, and implementation readiness. Use when Codex needs to critique a PRD or feature specification before design, engineering planning, stakeholder approval, or delivery.
---

# PRD Review

## Shared Reference

Use `../../references/product-management-principles.md` for general product
management principles. Apply the discovery, delivery, metrics, prioritization,
and common failure mode sections when reviewing PRDs.

## Review Stance

Use a product and delivery readiness lens. Prioritize issues that could cause teams to build the wrong thing, disagree on scope, miss success criteria, or discover blockers late.

## Product Management Principles

- A PRD should align the team on problem, users, outcomes, scope, requirements,
  risks, and launch decision criteria.
- Review for decision readiness, not literary polish.
- Requirements must be testable and traceable to a user or business outcome.
- Missing non-goals, dependencies, metrics, and rollout criteria are delivery
  risks.

## Practical Operating Guidance

- Lead with blockers that could cause wrong scope, wrong solution, late
  discovery, or unmeasurable outcomes.
- Check whether design, engineering, QA, data, GTM, support, legal, privacy,
  and operations can act from the document.
- Look for hidden decisions disguised as requirements.
- Distinguish missing evidence from acceptable assumptions.
- Recommend concrete rewrites for vague requirements and acceptance criteria.

## Checklist

- Problem: specific user/business problem and evidence.
- Goals: measurable outcomes, not only shipped features.
- Scope: explicit non-goals and release boundaries.
- Requirements: testable, complete, and not mixed with vague aspirations.
- User experience: key flows, edge cases, errors, and accessibility needs.
- Metrics: baseline, target, instrumentation, and decision use.
- Dependencies: technical, operational, legal, data, and GTM dependencies.
- Risks: adoption, abuse, quality, privacy, support, migration, and rollout risks.

## Common Failure Modes

- The problem statement is too broad to guide tradeoffs.
- Target users are named but scenarios and jobs are unclear.
- Goals and metrics are not tied to launch or iteration decisions.
- Requirements cannot be tested.
- Edge cases, error states, accessibility, support load, migration, or rollback
  are omitted.
- The PRD implies certainty where discovery is still needed.

## Output

Lead with review findings ordered by severity. Include file or section references when available. End with a readiness verdict: `Ready`, `Ready with changes`, or `Not ready`.
