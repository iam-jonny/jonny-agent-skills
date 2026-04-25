---
name: pbi-prioritize
description: Prioritize product backlog items, epics, feature candidates, or roadmap inputs using explicit product criteria such as impact, confidence, effort, risk, urgency, learning value, dependencies, and strategic fit. Use when Codex needs to rank work, explain tradeoffs, or recommend what to do next.
---

# PBI Prioritize

## Shared Reference

Use `../../references/product-management-principles.md` for general product
management principles. Apply the prioritization, metrics, roadmap, and common
failure mode sections when ranking work.

## Workflow

1. Identify the prioritization context: objective, time horizon, team capacity, constraints, and decision owner.
2. Choose a lightweight framework. Prefer RICE for comparable growth/product bets, WSJF for cost-of-delay contexts, and MoSCoW only for release-scope negotiation.
3. Normalize scores and call out low-confidence inputs.
4. Respect dependencies and sequencing; do not rank blocked work as immediately actionable without noting the blocker.

## Product Management Principles

- Prioritization is a sequencing decision under capacity constraints.
- Ranking should reflect outcomes, confidence, effort, urgency, risk reduction,
  dependencies, and strategic fit.
- Scores are decision aids, not truth. Explain judgment calls and confidence.
- Work that unlocks learning or removes risk may deserve priority even when
  direct impact is uncertain.

## Practical Operating Guidance

- Start by naming the objective and time horizon; rankings change when the goal
  changes.
- Use RICE for comparable growth or product opportunities.
- Use WSJF when cost of delay, urgency, or enablement is central.
- Use MoSCoW only to negotiate release scope, not as a general strategy model.
- Adjust raw scores for dependencies, team capacity, sequencing, compliance,
  operational readiness, and stakeholder commitments.
- Separate "do now", "prepare next", "defer", and "reject" when a flat ranking
  would hide important decisions.

## Output

Return:

- Ranked list with rationale.
- Scoring table when enough data exists.
- Recommended next slice of work.
- Explicit tradeoffs and items to defer.
- Inputs that would change the ranking.

## Common Failure Modes

- Ranking work without naming the objective.
- Treating stakeholder volume as impact.
- Ignoring confidence and presenting speculative numbers as precise.
- Ranking blocked items as immediately actionable.
- Forgetting non-feature work such as migration, quality, instrumentation,
  support, compliance, and enablement.

## Quality Bar

Do not present false precision. Use ranges or confidence notes when evidence is weak.
