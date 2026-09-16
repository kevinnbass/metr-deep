#!/usr/bin/env python3
"""Render a casework review file for a landed lane from a reviewer's verdict JSON (PLAN.md §9).

The reviewer (a human or a designated reviewing agent) records verdicts in a JSON file, one object
per lane row key:
  {"<row>": {"verdict": "CONFIRMED|DIFFERS|UNVERIFIABLE", "target_prefix": "MDF", "element_ids": "C02.E2;C01.E2",
             "primary_values": {"amount_usd": "350000"}, "note": "...", "strength": "primary", "role": "evidence",
             "supersedes": ""}}
This script only renders that JSON into the markdown table `python3 -m casework promote` parses; it
assigns no verdict itself. Every lane row must have a verdict or the engine refuses the review.
`--skeleton` writes a JSON skeleton with every row and empty verdicts for the reviewer to fill.

Usage:
  python3 scripts/review_lane.py research/grok-out/MD02-packard-grant.csv --skeleton > verdicts.json
  python3 scripts/review_lane.py research/grok-out/MD02-packard-grant.csv --verdicts verdicts.json \
      --out research/agents-2026-09-16/MDREVIEW-MD02.md
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERDICTS = {"CONFIRMED", "DIFFERS", "UNVERIFIABLE"}


def read_lane(path: Path) -> list[dict[str, str]]:
    raw = path.read_text("utf-8-sig")
    body = "\n".join(l for l in raw.splitlines() if not l.startswith("#"))
    reader = csv.DictReader(io.StringIO(body, newline=""))
    rows = []
    for i, r in enumerate(reader, 1):
        row = {(k or "").strip(): (v or "").strip() for k, v in r.items()}
        row.setdefault("row", "")
        if not row["row"]:
            row["row"] = str(i)
        rows.append(row)
    return rows


def cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("lane")
    ap.add_argument("--skeleton", action="store_true")
    ap.add_argument("--verdicts")
    ap.add_argument("--out")
    ap.add_argument("--title", default="")
    ap.add_argument("--summary", default="")
    args = ap.parse_args()
    lane_path = ROOT / args.lane if not Path(args.lane).is_absolute() else Path(args.lane)
    rows = read_lane(lane_path)
    if args.skeleton:
        skeleton = {r["row"]: {"verdict": "", "target_prefix": r.get("target_prefix", ""),
                               "element_ids": r.get("element_ids", ""), "primary_values": {},
                               "note": "", "strength": "primary", "role": "evidence", "supersedes": "",
                               "_lane": {k: r.get(k, "")[:160] for k in ("task", "subject", "from_entity", "to_entity",
                                                                          "money_type", "amount_usd", "date", "url",
                                                                          "quote_300", "result")}}
                    for r in rows}
        print(json.dumps(skeleton, indent=1, ensure_ascii=False))
        return 0
    if not args.verdicts or not args.out:
        sys.exit("need --verdicts and --out (or --skeleton)")
    verdicts = json.loads(Path(args.verdicts).read_text("utf-8"))
    keys = [r["row"] for r in rows]
    missing = [k for k in keys if k not in verdicts or not verdicts[k].get("verdict")]
    extra = [k for k in verdicts if k not in keys]
    if missing or extra:
        sys.exit(f"verdict coverage mismatch: missing={missing[:10]} extra={extra[:10]}")
    lines = [f"<!-- casework-review lane={lane_path.relative_to(ROOT)} -->", "",
             f"# {args.title or 'Review of ' + lane_path.stem}", ""]
    if args.summary:
        lines += [args.summary, ""]
    lines += ["| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |",
              "|---|---|---|---|---|---|---|---|---|"]
    counts = {v: 0 for v in VERDICTS}
    for k in keys:
        v = verdicts[k]
        verdict = v["verdict"].upper()
        if verdict not in VERDICTS:
            sys.exit(f"row {k}: bad verdict {verdict!r}")
        pv = v.get("primary_values") or {}
        if verdict == "DIFFERS" and not pv:
            sys.exit(f"row {k}: DIFFERS needs primary_values")
        if verdict == "UNVERIFIABLE" and not v.get("note"):
            sys.exit(f"row {k}: UNVERIFIABLE needs a note naming the route tried")
        counts[verdict] += 1
        lines.append("| " + " | ".join([
            cell(k), verdict, cell(v.get("target_prefix", "")), cell(v.get("element_ids", "")),
            cell(json.dumps(pv, ensure_ascii=False)) if pv else "{}",
            cell(v.get("strength", "primary")), cell(v.get("role", "evidence")), cell(v.get("supersedes", "")),
            cell(v.get("note", "")),
        ]) + " |")
    out = ROOT / args.out if not Path(args.out).is_absolute() else Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"WROTE {out} rows={len(keys)} {counts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
