---
name: project-orchestrator
description: Diagnose ambiguous project management requests and recommend the right sequence of project-management-tools skills. Use when Codex needs to decide whether to synthesize intake, create a charter, create a project plan, manage risks, plan communications, report status, review changes, synthesize meeting actions, or run a retrospective.
---

# Project Orchestrator

## Shared Reference

Use `../../references/project-management-principles.md` for general project
management principles. Use this skill as the routing layer for the rest of the
project-management-tools plugin.

## Orchestration Stance

Act like a pragmatic project manager. Diagnose the project job before creating
artifacts. Recommend the smallest next step that clarifies outcomes, ownership,
scope, timeline, risks, dependencies, communication, or decisions.

## Skill Layers

- Intake layer: `project-intake-synthesize`, `meeting-action-synthesize`
- Definition layer: `project-charter-create`, `project-plan-create`
- Control layer: `risk-register-create`, `change-request-review`,
  `status-report-create`
- Communication layer: `stakeholder-communication-plan`
- Learning layer: `retrospective-synthesize`

## Workflow

1. Identify the input type: rough notes, transcript, meeting minutes, charter,
   plan, risks, status update, change request, or retrospective notes.
2. Identify the desired next state: structured intake, charter, plan, risk
   register, communication plan, status report, decision, or lessons learned.
3. Determine whether the blocker is unclear scope, ownership, timeline,
   dependencies, risk, stakeholder alignment, or change control.
4. Recommend the shortest skill sequence and explain why.
5. If the user asks to proceed, run the first useful step with explicit
   assumptions.

## Routing Rules

- If input is raw notes, transcript, OCR, chat, or mixed context, start with
  `project-intake-synthesize`.
- If a meeting produced decisions and follow-ups, use
  `meeting-action-synthesize`.
- If outcomes, sponsor, scope, or success criteria are unclear, use
  `project-charter-create`.
- If scope is known and execution coordination is needed, use
  `project-plan-create`.
- If uncertainty or exposure is central, use `risk-register-create`.
- If stakeholder cadence or decision communication is unclear, use
  `stakeholder-communication-plan`.
- If the user needs an update for leadership or a sponsor, use
  `status-report-create`.
- If scope, schedule, cost, quality, or risk is changing, use
  `change-request-review`.
- If the project ended or a milestone completed, use
  `retrospective-synthesize`.

## Output

Return:

- Diagnosed project job.
- Current artifact and decision state.
- Recommended skill sequence.
- Immediate next step.
- Assumptions and blockers.
- Optional prompt the user can run next.

## Quality Bar

Keep routing practical. Prefer one clear next action over a long process map.
Do not create a detailed plan when the charter-level decisions are still
unclear.
