---
name: product-orchestrator
description: Diagnose ambiguous product management requests and recommend the right sequence of product-management-tools skills. Use when Codex needs to decide whether to synthesize intake, create a BRD, create or review a PRD, support alignment, refine PBIs, prioritize work, or create a roadmap from messy context.
---

# Product Orchestrator

## Shared Reference

Use `../../references/product-management-principles.md` for general product
management principles. Use this skill as the routing layer for the rest of the
product-management-tools plugin.

## Orchestration Stance

Act like a senior product operator. Do not jump straight to a final artifact
when the input is messy, political, or decision-incomplete. Diagnose the user's
actual product job, identify the missing decision state, and sequence the
smallest set of skills that will move the work forward.

## Skill Layers

- Intake layer: `product-intake-synthesize`
- Definition layer: `brd-create`, `prd-create`, `mvv-create`
- Review layer: `business-requirements-review`, `prd-review`, `pbi-review`,
  `roadmap-review`, `mvv-review`
- Alignment layer: `artifact-alignment`, `stakeholder-review-synthesize`
- Execution layer: `pbi-prioritize`, `roadmap-create`

## Workflow

1. Identify the input type: idea, meeting notes, transcript, OCR notes,
   stakeholder request, BRD, PRD, PBIs, roadmap, comments, or mixed context.
2. Identify the desired next state: structured intake, BRD, PRD, approval,
   backlog, prioritization, roadmap, or stakeholder follow-up.
3. Determine whether the blocker is content quality, missing evidence,
   unresolved decisions, stakeholder alignment, or execution sequencing.
4. Recommend the shortest skill sequence and explain why.
5. If the user asks to proceed, run the first useful step rather than asking
   for every missing detail.

## Routing Rules

- If the input is raw notes, transcript, OCR, Slack, or rough bullets, start
  with `product-intake-synthesize`.
- If business objective, customer segment, economics, or decision owner are
  unclear, use `brd-create` before `prd-create`.
- If a PRD exists but approval is uncertain, use `prd-review` and then
  `artifact-alignment`.
- If the meeting produced comments, objections, or decisions, use
  `stakeholder-review-synthesize`.
- If the artifact is good but stakeholders are not aligned, use
  `artifact-alignment`.
- If delivery items exist but scope or readiness is unclear, use `pbi-review`.
- If options compete for capacity, use `pbi-prioritize`.
- If sequencing across time is needed, use `roadmap-create` or
  `roadmap-review`.

## Output

Return:

- Diagnosed product job.
- Current artifact and decision state.
- Recommended skill sequence.
- Immediate next step.
- Assumptions and blockers.
- Optional prompt the user can run next.

## Quality Bar

Keep routing practical. Prefer one clear next action over a long consulting
plan. Do not recommend a PRD when the business case or stakeholder decision is
not ready.
