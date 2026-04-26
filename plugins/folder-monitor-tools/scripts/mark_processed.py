#!/usr/bin/env python3
"""Mark a scanned file as processed in the folder monitor state file."""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Mark a file as processed.")
    parser.add_argument("file")
    parser.add_argument("--state-file", default=".folder-monitor-state.json")
    parser.add_argument("--status", default="processed", choices=["processed", "failed", "skipped"])
    parser.add_argument("--note", default="")
    args = parser.parse_args()

    state_path = Path(args.state_file).expanduser().resolve()
    state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {"files": {}}
    file_path = str(Path(args.file).expanduser().resolve())
    record = state.setdefault("files", {}).setdefault(file_path, {"path": file_path})
    record["status"] = args.status
    record["processed_time"] = time.time()
    if args.note:
        record["note"] = args.note
    state_path.write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(record, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
