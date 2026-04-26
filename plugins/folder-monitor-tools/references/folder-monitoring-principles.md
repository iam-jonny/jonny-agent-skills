# Folder Monitoring Principles

Use this reference when designing local file intake automation.

## Role

Folder monitoring should answer:

- Which folders are watched?
- Which file types are eligible?
- When is a file stable enough to process?
- How is duplicate processing prevented?
- What happens on success, skip, and failure?
- Which downstream workflow should receive the file?

## Recommended Modes

- Manual scan: user points at a folder or file and runs processing now.
- Scheduled scan: cron, launchd, GitHub Actions runner, or another scheduler
  scans at an interval.
- Event watch: filesystem events trigger processing immediately.

Prefer manual plus scheduled scan for reliability. Event watch can be useful,
but transcript and cloud-sync files may be written, renamed, or updated after
initial creation.

## File Stability

Do not process a file immediately after detection. A file is stable when:

- Its last modified time is older than the stability wait.
- Its size has not changed across checks.
- Its extension is supported.
- It is not a temporary, partial, or hidden file.

## Processing State

Keep a state file to avoid double processing. Store:

- Absolute path.
- Size.
- Modified time.
- Optional content hash.
- First detected time.
- Processed time.
- Status: detected, processed, skipped, failed.

## Routing

Folder monitoring should not decide final business meaning by itself. It should
triage the file and route to a downstream workflow such as:

- `document-intake-tools` for meeting/document processing.
- `product-management-tools` for product artifacts.
- `project-management-tools` for project artifacts.

## Safety

- Do not post private transcript content automatically without an explicit
  destination rule.
- Keep dry-run mode available.
- Log skipped and failed files.
- Avoid reading giant files without size limits.
- Keep secrets such as Slack webhooks outside the repository.
