---
name: document-intake-orchestrator
description: Diagnose document and meeting intake requests, ask minimal context questions, gather local documentation candidates, and route to draft, update, finalize, or summary workflows. Use when Codex receives meeting transcripts, notes, PDFs, Word files, Markdown, Notion or Confluence exports, or files detected by folder-monitor-tools.
---

# Document Intake Orchestrator

## Shared Reference

Use `../../references/meeting-intake-principles.md` for meeting types, minimal
questions, context discovery, output modes, routing, and safety.

## Orchestration Stance

Act as the intake coordinator between raw files and product/project workflows.
Do not over-ask. Confirm only the information that changes output quality,
destination, or risk.

## Workflow

1. Identify file/source type and likely meeting/document category.
2. Ask for missing essentials: meeting type, related product/project, output
   mode, target destination, and relevant local repo/docs path.
3. Decide whether local context is needed.
4. Route to context discovery, local doc gathering, lifecycle routing, or output
   drafting.
5. Recommend downstream product/project skill when appropriate.

## Routing Rules

- Use `meeting-type-classify` when meeting type is unclear.
- Use `context-discovery` when product/project/repository context is needed.
- Use `local-doc-context-gather` when local docs should be reviewed.
- Use `artifact-lifecycle-router` when deciding Draft, Update, Finalize, or
  Summary only.
- Use `meeting-output-draft` when creating a Slack/email/docs-ready output.
- Route product work to `product-management-tools`.
- Route project work to `project-management-tools`.

## Output

Return:

- Intake diagnosis.
- Required user confirmations.
- Context sources to inspect.
- Output mode.
- Downstream workflow.
- Suggested prompt for the next skill.

## Quality Bar

The output should make the next processing step obvious without forcing the
user to understand internal skill names.
