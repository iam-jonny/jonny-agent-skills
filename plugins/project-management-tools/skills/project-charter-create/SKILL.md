---
name: project-charter-create
description: Create project charters from rough project ideas, stakeholder requests, meeting notes, business context, or synthesized intake. Use when a project needs clear purpose, sponsor, scope, success criteria, constraints, assumptions, risks, milestones, and decision rights before detailed planning.
---

# Project Charter Create

## Shared Reference

Use `../../references/project-management-principles.md` for general project
management principles. Apply core model, planning, stakeholder, risk, and change
control sections when creating the charter.

## Creation Stance

Treat the charter as the authorization and alignment artifact for the project.
It should clarify why the project exists, who owns it, what is in and out of
scope, and what must be true before detailed execution planning is useful.

## Workflow

1. Identify sponsor, decision owner, project objective, and desired outcome.
2. Extract scope, non-scope, stakeholders, constraints, assumptions, risks,
   dependencies, and success criteria.
3. Separate goals from deliverables and activities.
4. State open decisions and approval path.
5. Recommend whether to proceed to project planning, stakeholder alignment, or
   more intake.

## Charter Structure

Use this default structure unless the user provides a house format:

- Project summary.
- Background and business context.
- Objectives and success criteria.
- Scope and out of scope.
- Key deliverables.
- Stakeholders, sponsor, and decision owner.
- Milestones or target timeline.
- Constraints and assumptions.
- Dependencies.
- Initial risks.
- Governance and communication expectations.
- Open questions.
- Approval path and next steps.

## Output

Return a concise project charter plus assumptions, blocker questions, and the
recommended next skill: `project-plan-create`, `stakeholder-communication-plan`,
or `risk-register-create`.

## Quality Bar

The charter should let a sponsor and delivery team decide whether the project
is worth planning and who has authority to make tradeoffs.
