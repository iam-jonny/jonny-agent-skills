---
name: monitoring-policy-create
description: Create monitoring policies for local folders, transcript drops, document exports, or team intake folders. Use when Codex needs to define scan cadence, file types, stability rules, processed state, routing, failure handling, privacy guardrails, and manual override behavior.
---

# Monitoring Policy Create

## Shared Reference

Use `../../references/folder-monitoring-principles.md` for monitoring modes,
stability, state, routing, and safety guidance.

## Policy Stance

Design for reliability and auditability. The policy should make it clear what
gets processed, when, where it goes, what is never auto-posted, and how humans
override the automation.

## Output

Return:

- Watch folders.
- Eligible file types.
- Monitoring mode: manual, scheduled, event watch, or hybrid.
- Scan cadence.
- Stability rules.
- State file and duplicate prevention.
- Routing rules.
- Failure handling.
- Privacy and approval guardrails.
- Manual override commands.
- Open setup questions.

## Quality Bar

The policy should be concrete enough that an engineer or ops owner can
implement it without inventing missing rules.
