---
name: folder-monitor-orchestrator
description: Diagnose folder monitoring requests and recommend manual scan, scheduled scan, event watch, file triage, or downstream document-intake routing. Use when Codex needs to design or operate local file detection workflows for transcripts, notes, PDFs, Word files, Markdown, or exports.
---

# Folder Monitor Orchestrator

## Shared Reference

Use `../../references/folder-monitoring-principles.md` for monitoring,
stability, state, routing, and safety guidance.

## Orchestration Stance

Act as the intake automation coordinator. Keep folder monitoring separate from
document interpretation. Detect files reliably, avoid duplicates, then route
eligible files to the right downstream workflow.

## Workflow

1. Identify watched folders, file types, cadence, and downstream workflow.
2. Choose mode: manual scan, scheduled scan, or event watch.
3. Define stability rules, state file location, size limits, and skip rules.
4. Recommend file triage and routing steps.
5. Produce the exact command or scheduler outline when useful.

## Routing Rules

- Use `folder-scan` when the user wants to inspect or process a folder now.
- Use `new-file-triage` when a candidate file has been detected.
- Use `monitoring-policy-create` when the user is designing an ongoing setup.
- Route meeting/transcript/document files to `document-intake-tools` after
  detection.

## Output

Return:

- Recommended monitoring mode.
- Watch folder and file type assumptions.
- Stability and duplicate-prevention rules.
- Downstream routing plan.
- Manual command or scheduled command.
- Safety notes and open questions.

## Quality Bar

Favor reliable scheduled scans over fragile real-time watchers unless the user
has a strong need for immediate processing.
