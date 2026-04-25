---
name: pbi-prioritize
description: Prioritize product backlog items, epics, feature candidates, or roadmap inputs using explicit product criteria such as impact, confidence, effort, risk, urgency, learning value, dependencies, and strategic fit. Use when Codex needs to rank work, explain tradeoffs, or recommend what to do next.
---

# PBI Prioritize

## Workflow

1. Identify the prioritization context: objective, time horizon, team capacity, constraints, and decision owner.
2. Choose a lightweight framework. Prefer RICE for comparable growth/product bets, WSJF for cost-of-delay contexts, and MoSCoW only for release-scope negotiation.
3. Normalize scores and call out low-confidence inputs.
4. Respect dependencies and sequencing; do not rank blocked work as immediately actionable without noting the blocker.

## Output

Return:

- Ranked list with rationale.
- Scoring table when enough data exists.
- Recommended next slice of work.
- Explicit tradeoffs and items to defer.
- Inputs that would change the ranking.

## Quality Bar

Do not present false precision. Use ranges or confidence notes when evidence is weak.
