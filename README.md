# Jonny Agent Skills

Local Codex and Claude Code plugin and skill definitions for product
management work.

## Overview

This repository contains local plugins that can be used from Codex and Claude
Code.

## Available Plugins

| Plugin | Purpose |
| --- | --- |
| `product-management-tools` | Turn messy product inputs into aligned BRDs, PRDs, PBIs, priorities, and roadmaps. |
| `project-management-tools` | Turn messy project inputs into aligned charters, plans, risks, status reports, change decisions, and retrospectives. |

## Product Management Tools

`product-management-tools` provides focused skills for turning messy product
inputs into decision-ready product artifacts and alignment steps:

- Meeting notes, transcripts, paper-note OCR, and stakeholder requests
- BRDs and business requirements
- PRDs and approval plans
- Mission, vision, and values
- Product backlog items
- Backlog prioritization
- Product roadmaps

The plugin is intended to help turn rough product context, strategy notes,
stakeholder requests, and draft documents into clearer, more decision-ready
artifacts.

## Workflow Model

The skills are designed to work together in layers:

- Intake layer: structure messy inputs before creating artifacts.
- Definition layer: create BRDs, PRDs, MVV drafts, and other core artifacts.
- Review layer: check artifact quality and readiness.
- Alignment layer: plan approvals, synthesize stakeholder feedback, and record
  decisions.
- Execution layer: refine PBIs, prioritize work, and create roadmaps.
- Orchestration layer: diagnose ambiguous requests and recommend the right
  sequence of skills.

Common workflow:

```text
meeting notes / paper notes / transcript / stakeholder request
  -> product-orchestrator
  -> product-intake-synthesize
  -> brd-create
  -> business-requirements-review
  -> artifact-alignment
  -> prd-create
  -> prd-review
  -> stakeholder-review-synthesize
  -> pbi-review / pbi-prioritize / roadmap-create
```

## Codex Plugin

The product management plugin lives at:

```text
plugins/product-management-tools
```

Its plugin manifest is:

```text
plugins/product-management-tools/.codex-plugin/plugin.json
```

Codex uses this manifest to discover the plugin name, display metadata, and
skills directory.

The project management plugin lives at:

```text
plugins/project-management-tools
```

Its plugin manifest is:

```text
plugins/project-management-tools/.codex-plugin/plugin.json
```

## Claude Code Marketplace

This repository also includes a Claude Code marketplace manifest:

```text
.claude-plugin/marketplace.json
```

The marketplace exposes the `product-management-tools` plugin from:

```text
plugins/product-management-tools
```

The Claude Code plugin manifest is:

```text
plugins/product-management-tools/.claude-plugin/plugin.json
```

After this repository is public, Claude Code users can add the marketplace:

```text
/plugin marketplace add iam-jonny/jonny-agent-skills
```

Then install a plugin:

```text
/plugin install product-management-tools@jonny-agent-skills
/plugin install project-management-tools@jonny-agent-skills
```

For local testing from a checkout of this repository:

```text
/plugin marketplace add ./path/to/jonny-agent-skills
/plugin install product-management-tools@jonny-agent-skills
/plugin install project-management-tools@jonny-agent-skills
```

## Skills

| Skill | Purpose |
| --- | --- |
| `product-orchestrator` | Diagnose ambiguous PM requests and recommend the right skill sequence. |
| `product-intake-synthesize` | Turn messy notes, transcripts, OCR, and stakeholder requests into structured PM context. |
| `brd-create` | Create business requirements documents before PRD work. |
| `artifact-alignment` | Plan stakeholder alignment, approvals, review meetings, and decision logs. |
| `stakeholder-review-synthesize` | Turn stakeholder feedback into decisions, required edits, action items, and follow-up. |
| `mvv-create` | Create mission, vision, and values drafts. |
| `mvv-review` | Review MVV drafts for clarity, specificity, and usefulness. |
| `business-requirements-review` | Review business requirements for outcomes, constraints, risks, and readiness. |
| `prd-create` | Create pragmatic product requirements documents from rough context. |
| `prd-review` | Review PRDs for clarity, completeness, and execution risk. |
| `pbi-review` | Review backlog items, user stories, epics, and acceptance criteria. |
| `pbi-prioritize` | Prioritize PBIs using explicit criteria such as impact, confidence, effort, risk, and strategic fit. |
| `roadmap-create` | Create outcome-oriented product roadmaps. |
| `roadmap-review` | Review roadmaps for strategy fit, sequencing, feasibility, and credibility. |

Each skill is defined by a `SKILL.md` file under:

```text
plugins/product-management-tools/skills/<skill-name>/SKILL.md
```

Some skills also include `agents/openai.yaml` metadata for Codex UI display
names, short descriptions, and default prompts.

## Product Management Reference

Shared product management guidance lives at:

```text
plugins/product-management-tools/references/product-management-principles.md
```

This reference summarizes textbook-style product management concepts and
practical operating guidance for discovery, delivery, metrics, prioritization,
roadmaps, and common failure modes. Each skill applies the relevant parts of
that reference and adds artifact-specific review or creation guidance.

## Project Management Tools

`project-management-tools` is organized around practical project execution:

- Intake layer: structure meeting notes, transcripts, OCR notes, stakeholder
  requests, risks, and decisions.
- Definition layer: create project charters and project plans.
- Control layer: manage risk registers, status reports, and change requests.
- Communication layer: plan stakeholder updates, decision asks, and
  escalations.
- Learning layer: turn retrospectives into concrete process improvements.
- Orchestration layer: diagnose ambiguous project work and recommend the right
  skill sequence.

Common workflow:

```text
meeting notes / stakeholder request / project idea
  -> project-orchestrator
  -> project-intake-synthesize
  -> project-charter-create
  -> project-plan-create
  -> risk-register-create
  -> stakeholder-communication-plan
  -> status-report-create / change-request-review
  -> meeting-action-synthesize / retrospective-synthesize
```

Project management skills:

| Skill | Purpose |
| --- | --- |
| `project-orchestrator` | Diagnose ambiguous project requests and recommend the right skill sequence. |
| `project-intake-synthesize` | Turn messy notes, transcripts, OCR, and stakeholder requests into structured project context. |
| `project-charter-create` | Create project charters before detailed planning. |
| `project-plan-create` | Create practical plans with milestones, owners, dependencies, risks, and communication cadence. |
| `risk-register-create` | Create risk registers with owners, triggers, mitigations, contingencies, and escalation thresholds. |
| `stakeholder-communication-plan` | Plan project stakeholder updates, decision asks, channels, cadence, and escalations. |
| `status-report-create` | Create sponsor-ready status reports with RAG status, progress, risks, decisions, and asks. |
| `change-request-review` | Review project change requests and recommend approve, reject, defer, split, or escalate. |
| `meeting-action-synthesize` | Turn project meetings into decisions, actions, risks, dependencies, and follow-up messages. |
| `retrospective-synthesize` | Turn retrospectives into lessons, owners, and process changes. |

Shared project management guidance lives at:

```text
plugins/project-management-tools/references/project-management-principles.md
```

## Example Prompts

```text
Use product-management-tools product-orchestrator to diagnose this product request and choose the next steps.
```

```text
Use product-management-tools product-intake-synthesize to organize these meeting notes into product context.
```

```text
Use product-management-tools brd-create to create a BRD from this stakeholder request.
```

```text
Use product-management-tools mvv-create to create an MVV for this product.
```

```text
Use product-management-tools prd-review to review this PRD and identify blockers.
```

```text
Use product-management-tools artifact-alignment to create an approval plan for this PRD.
```

```text
Use product-management-tools pbi-prioritize to rank these backlog items.
```

```text
Use project-management-tools project-orchestrator to diagnose this project request and choose the next steps.
```

```text
Use project-management-tools project-intake-synthesize to organize these meeting notes into project context.
```

```text
Use project-management-tools project-charter-create to create a charter from this project idea.
```

```text
Use project-management-tools status-report-create to create a sponsor-ready status report.
```

## Local Installation

This repository is structured as a local plugin source. To use the plugin in
Codex, install or reference the plugin directory from a Codex environment that
supports local plugins.

To use the plugin in Claude Code, add this repository as a marketplace and then
install the desired plugin from that marketplace.

The plugin display name is:

```text
Product Management Tools
```

The plugin package name is:

```text
product-management-tools
project-management-tools
```

## Development Notes

- Keep each skill focused on one product management job.
- Prefer concrete review criteria and decision-ready outputs.
- Mark assumptions clearly when source context is incomplete.
- Avoid generic language that could apply to any product or team.
- Put shared product management concepts in `references/` and keep skill files
  focused on how those concepts apply to a specific artifact.
- Update `.codex-plugin/plugin.json` when adding, renaming, or repositioning
  plugin-level capabilities.
