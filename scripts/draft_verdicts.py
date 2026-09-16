#!/usr/bin/env python3
"""Draft a verdict JSON for a landed lane from mechanical rules, for the reviewing agent to correct.

Rules (conservative; the reviewer overrides row by row):
- MDS rows whose result says none-found and whose limitation/result names a route failure
  (403, 404, 429, 202 empty, login wall, JS shell, DNS, captcha, blocked, timeout) -> CONFIRMED, context.
- other MDS none-found rows -> CONFIRMED, negative, supporting.
- MDS rows that are positive enumeration receipts -> CONFIRMED, evidence, supporting.
- rows whose (from_entity,to_entity,amount_usd,money_type) already exist on a promoted non-seed
  MDF row -> CONFIRMED, context (duplicate of an existing funding event).
- MDP/MDR/MDE/MDT/MDI/MDQ rows -> CONFIRMED, evidence, supporting (reviewer upgrades to primary).
- MDF rows with a new amount -> CONFIRMED, evidence, primary (reviewer must verify).
- source_class not in the config vocabulary -> DIFFERS with a mapped value.
Nothing here is a verdict until the reviewer has checked the row against its primary.

Usage: python3 scripts/draft_verdicts.py MD16-canary-award-structure > draft.json
"""
from __future__ import annotations

import csv
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / "casework.json").read_text("utf-8"))
CLASSES = set(CONFIG["source_classes"])
CLASS_MAP = {"government filings": "state registries", "public grant listings": "public grant databases",
             "named on-record statements": "self-statements", "retained archives": "archives",
             "high-quality press": "press", "government filings and procurement records": "procurement records"}
FAIL = re.compile(r"\b(403|404|429|500|504|202 empty|0 bytes|0-byte|login wall|login/register|js shell|javascript|client-rendered|dns|captcha|challenge|blocked|timed out|timeout|access denied|not recoverable|route failure|not used|not needed|scope note)\b", re.I)


def read(lane: str):
    raw = (ROOT / f"research/grok-out/{lane}.csv").read_text("utf-8-sig")
    body = "\n".join(l for l in raw.splitlines() if not l.startswith("#"))
    rows = [{(k or "").strip(): (v or "").strip() for k, v in r.items()} for r in csv.DictReader(io.StringIO(body, newline=""))]
    for i, r in enumerate(rows, 1):
        r.setdefault("row", "")
        if not r["row"]:
            r["row"] = str(i)
    return rows


def promoted_mdf():
    raw = (ROOT / CONFIG["tables"]["MDF"]["file"]).read_text("utf-8-sig")
    body = "\n".join(l for l in raw.splitlines() if not l.startswith("#"))
    out = set()
    for r in csv.DictReader(io.StringIO(body, newline="")):
        r = {k: (v or "").strip() for k, v in r.items()}
        if "seed transcription" in r.get("note", "") or "lineage transcription" in r.get("note", ""):
            continue
        out.add((r.get("to_entity", "").lower()[:24], r.get("amount_usd", ""), r.get("money_type", "")))
    return out


def main() -> int:
    lane = sys.argv[1]
    rows = read(lane)
    held = promoted_mdf()
    out = {}
    for r in rows:
        p = r.get("target_prefix", "") or "MDS"
        e = r.get("element_ids", "")
        text = " ".join(r.get(k, "") for k in ("result", "limitation", "subject", "quote_300"))
        pv = {}
        if r.get("source_class") and r["source_class"] not in CLASSES:
            pv["source_class"] = CLASS_MAP.get(r["source_class"], "issuer statements")
        nf = re.search(r"none found", r.get("result", ""), re.I)
        if p == "MDS":
            if nf and FAIL.search(text):
                v = dict(verdict="CONFIRMED", strength="supporting", role="context", note="route failure or scope note, not a content negative; context")
            elif nf:
                v = dict(verdict="CONFIRMED", strength="supporting", role="negative", note="bounded negative as stated")
            else:
                v = dict(verdict="CONFIRMED", strength="supporting", role="evidence", note="source-coverage receipt")
        elif p == "MDF":
            key = (r.get("to_entity", "").lower()[:24], r.get("amount_usd", ""), r.get("money_type", ""))
            if r.get("amount_usd") and key in held:
                v = dict(verdict="CONFIRMED", strength="supporting", role="context", note="same funding event as an already promoted row; context so one event is one row")
            elif not r.get("amount_usd") and nf:
                v = dict(verdict="DIFFERS", strength="supporting", role="negative", note="none-found typed as MDF; retargeted to MDS")
                p = "MDS"; pv.setdefault("money_type", "")
            elif not r.get("amount_usd"):
                v = dict(verdict="CONFIRMED", strength="supporting", role="context", note="no amount; acknowledgment or restatement; context")
            else:
                v = dict(verdict="CONFIRMED", strength="primary", role="evidence", note="NEW AMOUNT - reviewer must verify against the primary")
        else:
            v = dict(verdict="CONFIRMED", strength="supporting", role="evidence", note="proposition/entity/relationship/timeline row as stated; reviewer to upgrade or demote")
        if pv:
            v["verdict"] = "DIFFERS"; v["primary_values"] = pv; v["note"] = "vocabulary corrected; " + v["note"]
        v.update(target_prefix=p, element_ids=e)
        out[r["row"]] = v
    json.dump(out, sys.stdout, indent=1, ensure_ascii=False)
    from collections import Counter
    print("\n#", lane, len(out), dict(Counter(v["role"] for v in out.values())), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
