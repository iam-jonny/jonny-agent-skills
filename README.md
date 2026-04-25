# Jonny Agent Skills

Local Codex plugin and skill definitions for product management work.

## Overview

This repository contains a Codex plugin named `product-management-tools`.
The plugin provides focused skills for creating and reviewing common product
management artifacts:

- Mission, vision, and values
- Business requirements
- Product requirements documents
- Product backlog items
- Backlog prioritization
- Product roadmaps

The plugin is intended to help turn rough product context, strategy notes,
stakeholder requests, and draft documents into clearer, more decision-ready
artifacts.

## Plugin

The plugin lives at:

```text
plugins/product-management-tools
```

Its plugin manifest is:

```text
plugins/product-management-tools/.codex-plugin/plugin.json
```

Codex uses this manifest to discover the plugin name, display metadata, and
skills directory.

## Skills

| Skill | Purpose |
| --- | --- |
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

## Example Prompts

```text
Use product-management-tools mvv-create to create an MVV for this product.
```

```text
Use product-management-tools prd-review to review this PRD and identify blockers.
```

```text
Use product-management-tools pbi-prioritize to rank these backlog items.
```

## Local Installation

This repository is structured as a local Codex plugin source. To use the plugin,
install or reference the `plugins/product-management-tools` directory from a
Codex environment that supports local plugins.

The plugin display name is:

```text
Product Management Tools
```

The plugin package name is:

```text
product-management-tools
```

## Development Notes

- Keep each skill focused on one product management job.
- Prefer concrete review criteria and decision-ready outputs.
- Mark assumptions clearly when source context is incomplete.
- Avoid generic language that could apply to any product or team.
- Update `.codex-plugin/plugin.json` when adding, renaming, or repositioning
  plugin-level capabilities.
