#!/usr/bin/env python3
"""Scan a folder for stable, unprocessed files.

This script is intentionally small and dependency-free so it can be used from
cron, launchd, or a manual shell command. It does not call an LLM or post to
Slack; it emits JSON candidates that downstream automation can process.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Any


DEFAULT_EXTENSIONS = [".txt", ".vtt", ".srt", ".md", ".docx", ".pdf"]


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"files": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def save_state(path: Path, state: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")


def is_hidden_or_temp(path: Path) -> bool:
    if any(part.startswith(".") for part in path.parts):
        return True
    name = path.name.lower()
    return name.endswith(".tmp") or name.endswith(".part") or name.endswith(".crdownload")


def file_record(path: Path) -> dict[str, Any]:
    stat = path.stat()
    return {
        "path": str(path.resolve()),
        "size": stat.st_size,
        "mtime": stat.st_mtime,
    }


def scan(args: argparse.Namespace) -> dict[str, Any]:
    watch_dir = Path(args.watch_dir).expanduser().resolve()
    state_path = Path(args.state_file).expanduser().resolve()
    extensions = {ext.lower() if ext.startswith(".") else f".{ext.lower()}" for ext in args.extensions}
    state = load_state(state_path)
    files_state = state.setdefault("files", {})
    now = time.time()
    candidates = []
    skipped = []

    pattern = "**/*" if args.recursive else "*"
    for path in sorted(watch_dir.glob(pattern)):
        if not path.is_file():
            continue
        if is_hidden_or_temp(path):
            continue
        if path.suffix.lower() not in extensions:
            continue

        record = file_record(path)
        key = record["path"]
        previous = files_state.get(key)
        age = now - record["mtime"]

        if previous and previous.get("status") == "processed":
            skipped.append({"path": key, "reason": "already_processed"})
            continue
        if record["size"] > args.max_bytes:
            files_state[key] = {**record, "status": "skipped", "reason": "too_large"}
            skipped.append({"path": key, "reason": "too_large"})
            continue
        if age < args.stability_seconds:
            files_state[key] = {**record, "status": "detected", "first_detected": previous.get("first_detected", now) if previous else now}
            skipped.append({"path": key, "reason": "not_stable_yet", "age_seconds": round(age, 2)})
            continue
        if previous and previous.get("size") != record["size"] and age < args.size_change_wait_seconds:
            files_state[key] = {**record, "status": "detected", "first_detected": previous.get("first_detected", now)}
            skipped.append({"path": key, "reason": "size_changed_recently"})
            continue

        files_state[key] = {
            **record,
            "status": "detected",
            "first_detected": previous.get("first_detected", now) if previous else now,
            "ready_detected": now,
        }
        candidates.append(files_state[key])

    if not args.dry_run:
        save_state(state_path, state)

    return {
        "watch_dir": str(watch_dir),
        "state_file": str(state_path),
        "dry_run": args.dry_run,
        "candidates": candidates,
        "skipped": skipped,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan a folder for stable, unprocessed files.")
    parser.add_argument("watch_dir")
    parser.add_argument("--state-file", default=".folder-monitor-state.json")
    parser.add_argument("--extensions", nargs="+", default=DEFAULT_EXTENSIONS)
    parser.add_argument("--stability-seconds", type=int, default=60)
    parser.add_argument("--size-change-wait-seconds", type=int, default=120)
    parser.add_argument("--max-bytes", type=int, default=20 * 1024 * 1024)
    parser.add_argument("--recursive", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    print(json.dumps(scan(args), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
