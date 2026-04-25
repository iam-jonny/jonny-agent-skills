---
name: prd-create
description: Create pragmatic product requirements documents from product ideas, research notes, business requirements, roadmap items, stakeholder requests, or rough feature descriptions. Use when Codex needs to turn ambiguous product context into an implementation-ready PRD with goals, non-goals, users, requirements, metrics, risks, and open questions.
---

# PRD Create

## Shared Reference

Use `../../references/product-management-principles.md` for general product
management principles. Apply the discovery, delivery, metrics, prioritization,
roadmap, and common failure mode sections when drafting the PRD.

## Workflow

1. Identify the product problem, target users, business goal, and decision deadline.
2. Ask for missing information only when it blocks a useful PRD. Otherwise state assumptions.
3. Distinguish requirements from solution ideas, constraints, and open questions.
4. Make the smallest PRD that can align design, engineering, data, GTM, support, and leadership.

## Product Management Principles

- Start with the problem, segment, evidence, and desired outcome before
  specifying the solution.
- Requirements should be testable statements of behavior, capability, quality,
  or constraint.
- Scope is defined by both goals and non-goals.
- A PRD should expose risks and open decisions early enough to change the plan.
- Metrics should support a launch, iteration, rollback, or investment decision.

## Practical Operating Guidance

- Convert stakeholder asks into problem statements before writing requirements.
- Mark assumptions when evidence is missing; do not bury uncertainty in
  confident language.
- Include the minimum UX, data, QA, support, GTM, legal, privacy, security, and
  operational context needed for planning.
- Separate must-have launch requirements from later enhancements.
- Include rollout, instrumentation, support readiness, and failure handling for
  user-facing changes.

## PRD Structure

Use this default structure unless the user provides a house format:

- Summary
- Problem and context
- Goals and non-goals
- Users and key scenarios
- Requirements
- UX and content considerations
- Data, analytics, and success metrics
- Dependencies and constraints
- Risks and mitigations
- Rollout and experiment plan
- Open questions

## Common Failure Modes

- The PRD starts with a feature and never proves the problem matters.
- Goals describe shipping rather than changed user or business outcomes.
- Requirements mix user needs, design ideas, engineering tasks, and open
  questions.
- Non-goals are missing, causing scope expansion during execution.
- Metrics are listed without baseline, target, decision use, or owner.
- Dependencies and rollout risks appear too late.

## Quality Bar

Write requirements that are testable, unambiguous, and traceable to a user or business outcome. Mark assumptions clearly instead of hiding uncertainty.
