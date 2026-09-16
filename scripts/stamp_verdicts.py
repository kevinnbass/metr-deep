#!/usr/bin/env python3
"""Fill the `review_verdict` column of promoted rows from the review file that promoted them.

PLAN.md §3 requires every table row to carry `review_verdict`. The engine records the promoting
review in the row's note (`lane=<file>#<row>; review=<file>`) but has no column for the verdict
itself, so this reads that review back and writes the verdict into the row's own column. It only
ever fills an empty cell, and it refuses to change a cell that already has a different value.

Usage: python3 scripts/stamp_verdicts.py
"""
from __future__ import annotations

import csv
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, "/home/kevin/repos/casework")

from casework.review import parse_review  # noqa: E402

CONFIG = json.loads((ROOT / "casework.json").read_text("utf-8"))


def markers(note: str) -> tuple[str | None, str | None]:
    lane = review = None
    for part in note.split(";"):
        part = part.strip()
        if part.startswith("lane="):
            lane = part[5:]
        elif part.startswith("review="):
            review = part[7:]
    return lane, review


def main() -> int:
    verdict_cache: dict[str, dict[str, str]] = {}
    stamped = conflicts = 0
    for prefix, spec in sorted(CONFIG["tables"].items()):
        path = ROOT / spec["file"]
        if not path.exists():
            continue
        raw = path.read_text("utf-8-sig")
        comments = [line for line in raw.splitlines() if line.startswith("#")]
        body = "\n".join(line for line in raw.splitlines() if not line.startswith("#"))
        reader = csv.DictReader(io.StringIO(body, newline=""))
        fields = list(reader.fieldnames or [])
        rows = [dict(r) for r in reader]
        if "review_verdict" not in fields:
            continue
        changed = False
        for row in rows:
            lane, review = markers(row.get("note", "") or "")
            if not lane or not review:
                continue
            if review not in verdict_cache:
                review_path = ROOT / review
                if not review_path.exists():
                    continue
                _, parsed = parse_review(review_path)
                verdict_cache[review] = {v["row"]: v["verdict"] for v in parsed}
            key = lane.split("#", 1)[1] if "#" in lane else None
            verdict = verdict_cache.get(review, {}).get(key or "")
            if not verdict:
                continue
            current = (row.get("review_verdict") or "").strip()
            if current == verdict:
                continue
            if current:
                print(f"CONFLICT {row['row_id']} has review_verdict={current!r}, review says {verdict!r}")
                conflicts += 1
                continue
            row["review_verdict"] = verdict
            stamped += 1
            changed = True
        if changed:
            buffer = io.StringIO(newline="")
            for comment in comments:
                buffer.write(comment + "\n")
            writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n", extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)
            path.write_text(buffer.getvalue(), encoding="utf-8")
    print(f"STAMP stamped={stamped} conflicts={conflicts}")
    return 1 if conflicts else 0


if __name__ == "__main__":
    raise SystemExit(main())
