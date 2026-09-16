#!/usr/bin/env python3
"""Mechanical pre-review check of a landed metr_deep lane CSV (PLAN.md §9 step 1 support).

Reports, without assigning any verdict: header-comment presence, column set versus casework.json,
per-row empty url / checked_utc / target_prefix / element_ids, unknown prefixes or element ids,
money_type vocabulary, task coverage A-E, none-found rows, and rows whose url is a local path or a
@kevinnbass post. Exit 1 if the engine could not package the lane as it stands.

Usage: python3 scripts/check_lane.py research/grok-out/MD02-packard-grant.csv
"""
from __future__ import annotations

import csv
import io
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / "casework.json").read_text("utf-8"))
CASE = json.loads((ROOT / "case.json").read_text("utf-8"))
ELEMENTS = {e["element_id"] for c in CASE["claims"] for e in c["elements"]}
PREFIXES = set(CONFIG["tables"])
MONEY = {"commitment", "paid_grant", "filed_grant", "recommendation", "transfer", "regrant",
         "contract", "in_kind_estimate", "equity_value", ""}
CLASSES = set(CONFIG["source_classes"])


def main() -> int:
    path = ROOT / sys.argv[1] if not Path(sys.argv[1]).is_absolute() else Path(sys.argv[1])
    raw = path.read_text("utf-8-sig")
    lines = raw.splitlines()
    comments = [l for l in lines if l.startswith("#")]
    body = "\n".join(l for l in lines if not l.startswith("#"))
    reader = csv.DictReader(io.StringIO(body, newline=""))
    fields = [f.strip() for f in (reader.fieldnames or [])]
    rows = [{(k or "").strip(): (v or "").strip() for k, v in r.items()} for r in reader]
    fatal = []
    warn = []
    if not comments:
        fatal.append("no header comment")
    missing_cols = [c for c in CONFIG["lane_columns"] if c not in fields]
    extra_cols = [c for c in fields if c not in CONFIG["lane_columns"]]
    if "checked_utc" not in fields:
        fatal.append("no checked_utc column")
    if missing_cols:
        warn.append(f"missing columns: {missing_cols}")
    if extra_cols:
        warn.append(f"extra columns: {extra_cols}")
    if any(None in r for r in rows):
        fatal.append("ragged rows (extra fields)")
    tasks = Counter(r.get("task", "")[:1].upper() for r in rows)
    prefixes = Counter(r.get("target_prefix", "") for r in rows)
    classes = Counter(r.get("source_class", "") for r in rows)
    for i, r in enumerate(rows, 1):
        if not r.get("url"):
            fatal.append(f"row {r.get('row') or i}: empty url")
        elif r["url"].startswith("/") or "kevinnbass" in r["url"].lower():
            warn.append(f"row {r.get('row') or i}: url is local or a @kevinnbass post: {r['url'][:80]}")
        if not r.get("checked_utc"):
            fatal.append(f"row {r.get('row') or i}: empty checked_utc")
        elif not re.match(r"\d{4}-\d{2}-\d{2}", r["checked_utc"]):
            warn.append(f"row {r.get('row') or i}: checked_utc not ISO: {r['checked_utc']}")
        if r.get("target_prefix") not in PREFIXES:
            warn.append(f"row {r.get('row') or i}: target_prefix {r.get('target_prefix')!r} unknown")
        bad = [e for e in r.get("element_ids", "").split(";") if e.strip() and e.strip() not in ELEMENTS]
        if bad:
            warn.append(f"row {r.get('row') or i}: unknown element_ids {bad}")
        if not r.get("element_ids", "").strip():
            warn.append(f"row {r.get('row') or i}: empty element_ids")
        if r.get("money_type", "") not in MONEY:
            warn.append(f"row {r.get('row') or i}: money_type {r.get('money_type')!r} not in vocabulary")
        if r.get("source_class") and r["source_class"] not in CLASSES:
            warn.append(f"row {r.get('row') or i}: source_class {r['source_class']!r} not in config")
        if not r.get("quote_300"):
            warn.append(f"row {r.get('row') or i}: empty quote_300")
    none_found = sum(1 for r in rows if "none found" in (r.get("result", "") + r.get("quote_300", "")).lower())
    dup_rows = [k for k, v in Counter(r.get("row", "") for r in rows).items() if v > 1]
    if dup_rows:
        fatal.append(f"duplicate row keys: {dup_rows}")
    print(f"LANE {path.name} rows={len(rows)} comments={len(comments)} tasks={dict(sorted(tasks.items()))}")
    print(f"  prefixes={dict(prefixes)} none_found={none_found}")
    print(f"  source_classes={dict(classes)}")
    for w in warn[:60]:
        print("  WARN", w)
    if len(warn) > 60:
        print(f"  ... {len(warn) - 60} more warnings")
    for f in fatal:
        print("  FATAL", f)
    return 1 if fatal else 0


if __name__ == "__main__":
    raise SystemExit(main())
