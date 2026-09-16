#!/usr/bin/env python3
"""Ten-minute supervision tick for metr_deep (PLAN.md §10).

Runs the shared runner's tick for this pack, reads each launched lane's goal state and output, and
appends one JSON line per tick to research/SUPERVISION.jsonl with the decisions the parent session
took. It launches nothing and stops nothing; those go through lanes.py so the runner owns the PID.

Usage: python3 scripts/supervise.py [--note "free text decision"]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = Path("/mnt/f/projects/anthropic/tools")
SUP = ROOT / "research/SUPERVISION.jsonl"


def utc() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--note", default="")
    parser.add_argument("--event", default="tick", help="tick | wave-open | wave-close")
    args = parser.parse_args()
    tick = subprocess.run(["python3", str(TOOLS / "lanes.py"), "tick", "--pack", "metr_deep"],
                          capture_output=True, text=True)
    text = tick.stdout + tick.stderr
    lanes = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(("RUNNING", "EXITED", "STOPPED")):
            lanes.append(stripped)
    problems = next((l.split(":", 1)[1].strip() for l in text.splitlines() if l.startswith("problems:")), "")
    new_outputs = next((l.split(":", 1)[1].strip() for l in text.splitlines() if l.startswith("new outputs")), "")
    row = {"utc": utc(), "event": args.event, "lanes": lanes, "new_outputs": new_outputs,
           "problems": problems, "note": args.note, "tick_exit": tick.returncode}
    SUP.parent.mkdir(parents=True, exist_ok=True)
    with SUP.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(text.rstrip())
    print(f"SUPERVISION appended event={args.event} lanes={len(lanes)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
