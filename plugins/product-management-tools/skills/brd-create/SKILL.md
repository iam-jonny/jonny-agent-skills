---
name: brd-create
description: Create business requirements documents from product ideas, stakeholder requests, meeting notes, strategy context, opportunity briefs, customer signals, or synthesized intake. Use before PRD creation when the business objective, target segment, success metrics, constraints, ownership, and approval path need to be clarified.
---

# BRD Create

## Shared Reference

Use `../../references/product-management-principles.md` for general product
management principles. Apply discovery, metrics, prioritization, delivery, and
common failure mode sections when creating a business requirements document.

## Creation Stance

Treat the BRD as the bridge between strategy and product execution. The goal is
not to specify every feature; it is to justify the investment, define business
outcomes, clarify constraints, and create a decision-ready basis for PRD work.

## Workflow

1. Identify the business objective, customer or user segment, and trigger for
   the initiative.
2. Extract evidence, economics, risks, constraints, stakeholders, and decision
   owner.
3. Separate desired outcomes from solution ideas.
4. Define scope boundaries and non-goals.
5. State assumptions and unresolved decisions clearly.
6. Recommend whether the BRD is ready for PRD creation, needs more discovery,
   or needs stakeholder alignment first.

## BRD Structure

Use this default structure unless the user provides a house format:

- Executive summary.
- Business context and opportunity.
- Customer or user problem.
- Business objectives.
- Success metrics and decision use.
- Scope and non-goals.
- Stakeholders, decision owner, and approvers.
- Constraints.
- Risks and mitigations.
- Dependencies.
- Rollout or go-to-market considerations.
- Open questions.
- Approval path and next steps.

## Practical Operating Guidance

- Make the investment thesis explicit: why this, why now, and why this team.
- Include measurable outcomes but avoid fake precision when evidence is weak.
- Name the approval path and what decision the BRD should unlock.
- Preserve solution ideas as options unless the business has already committed.
- Flag when the initiative is not ready for a PRD because the problem,
  economics, or decision owner is unclear.

## Common Failure Modes

- The BRD is a feature request with business language attached.
- The customer or user segment is too broad to guide tradeoffs.
- Success metrics are not measurable or not attributable.
- Constraints and decision rights are omitted.
- The document hides unresolved stakeholder disagreement.

## Output

Return a concise BRD plus:

- Assumptions.
- Missing blocker information.
- Recommended next skill: `business-requirements-review`, `artifact-alignment`,
  or `prd-create`.

## Quality Bar

The BRD should allow leadership, product, design, engineering, GTM, operations,
and support to understand the business case and decide whether PRD work should
begin.
