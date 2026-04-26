---
name: folder-scan
description: Plan or run a manual or scheduled folder scan for stable, unprocessed files. Use when Codex needs to scan local folders for transcripts, notes, PDFs, Word files, Markdown files, or exports and prepare candidates for downstream processing.
---

# Folder Scan

## Shared Reference

Use `../../references/folder-monitoring-principles.md` for monitoring,
stability, state, and safety guidance. Prefer the bundled
`scripts/scan_folder.py` script for concrete scans.

## Workflow

1. Confirm watch folder, recursive behavior, file extensions, stability wait,
   state file, and dry-run preference.
2. Run or provide a scan command.
3. Summarize ready candidates, skipped files, and reasons.
4. Recommend downstream routing for ready files.
5. Mark files processed only after downstream processing succeeds.

## Command Pattern

```bash
python3 plugins/folder-monitor-tools/scripts/scan_folder.py ~/Documents/Zoom \
  --recursive \
  --state-file .folder-monitor-state.json \
  --stability-seconds 60
```

## Output

Return:

- Scan settings.
- Ready files.
- Skipped files and reasons.
- Recommended next workflow.
- Mark-processed command for successful files.

## Quality Bar

Do not treat detected as processed. A file becomes processed only after the
downstream workflow completes.
