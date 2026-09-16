#!/usr/bin/env python3
"""S1 Done-when checker (PLAN.md S1). Reports, does not fix.

Checks: every MD01-MD14 lane promoted (or reviewed-and-replaced); supporter_coverage.csv has one status
per supporter and no `not_yet_reviewed` row owned by an S1 lane; every promoted MDF row to METR bound as
evidence carries a money_type from the vocabulary (untyped amounts are listed with their reason); the
frontier has no UNTOUCHED public-grant-database, recipient-filing or funder-filing class for C01/C02;
casework verify exits 0.

Usage: python3 scripts/check_s1.py
"""
from __future__ import annotations

import csv
import io
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASEWORK = Path("/home/kevin/repos/casework")
VOCAB = {"commitment", "paid_grant", "filed_grant", "recommendation", "transfer", "regrant", "contract", "in_kind_estimate", "equity_value"}
S1_LANES = [f"MD{i:02d}" for i in range(1, 15)]
S1_CLASSES = {"public grant databases", "recipient filings", "funder filings", "DAF sponsor filings", "IRS TEOS and e-file index"}


def read_csv(path: Path) -> list[dict[str, str]]:
    raw = path.read_text("utf-8-sig")
    body = "\n".join(l for l in raw.splitlines() if not l.startswith("#"))
    return [{(k or "").strip(): (v or "").strip() for k, v in r.items()} for r in csv.DictReader(io.StringIO(body, newline=""))]


def main() -> int:
    ok = True
    lanes = {r["lane"]: r for r in read_csv(ROOT / "research/LANES.csv")}
    not_done = [l for l in S1_LANES if lanes.get(l, {}).get("status") not in {"promoted", "replaced"}]
    print(f"1 lanes promoted: {14 - len(not_done)}/14" + (f"  pending={not_done}" if not_done else ""))
    ok &= not not_done
    cov = read_csv(ROOT / "research/supporter_coverage.csv")
    pending = [r["supporter_key"] for r in cov if r["status"] == "not_yet_reviewed" and any(l in S1_LANES for l in r["owning_lanes"].split(";"))]
    from collections import Counter
    print(f"2 supporter_coverage rows={len(cov)} statuses={dict(Counter(r['status'] for r in cov))}" + (f"  S1-owned pending={pending}" if pending else ""))
    ok &= not pending
    case = json.loads((ROOT / "case.json").read_text("utf-8"))
    roles = {}
    for c in case["claims"]:
        for e in c["elements"]:
            for b in e.get("bindings", []):
                roles.setdefault(b["row_id"], set()).add(b["role"])
    mdf = read_csv(ROOT / "research/funding_events.csv")
    metr = re.compile(r"metr|model evaluation", re.I)
    untyped = []
    aggregates = []
    for r in mdf:
        if "seed transcription" in r.get("note", ""):
            continue
        if not metr.search(r.get("to_entity", "")):
            continue
        if "evidence" not in roles.get(r["row_id"], set()):
            continue
        if r.get("amount_usd") and re.search(r"\d", r["amount_usd"]) and r.get("money_type") not in VOCAB:
            if re.search(r"recipient's own Form 990|AllOtherContributionsAmt|net assets|program service revenue", r.get("payment_status", "") + r.get("subject", ""), re.I):
                aggregates.append((r["row_id"], r.get("subject", "")[:70], r.get("amount_usd")))
            else:
                untyped.append((r["row_id"], r.get("subject", "")[:70], r.get("amount_usd")))
    print(f"3 evidence-bound MDF rows to METR with an amount but no vocabulary money_type: {len(untyped)}"
          f"  (recipient-side aggregates, intentionally untyped: {len(aggregates)})")
    for u in untyped:
        print("    UNTYPED", u)
    for a in aggregates:
        print("    aggregate", a)
    ok &= not untyped
    fr = subprocess.run(["python3", "-m", "casework", "frontier", "--pack", "metr_deep"], cwd=CASEWORK, capture_output=True, text=True).stdout
    bad = [l for l in fr.splitlines() if l.startswith("SOURCE C0") and l.split()[1] in {"C01", "C02"}
           and " ".join(l.split()[2:-1]) in S1_CLASSES and l.endswith("UNTOUCHED")]
    print(f"4 C01/C02 filing and grant-database classes UNTOUCHED: {len(bad)}")
    for l in bad:
        print("    ", l)
    ok &= not bad
    v = subprocess.run(["python3", "-m", "casework", "verify", "--pack", "metr_deep"], cwd=CASEWORK, capture_output=True, text=True)
    print(f"5 casework verify exit={v.returncode}: {v.stdout.strip().splitlines()[0] if v.stdout else v.stderr.strip()}")
    ok &= v.returncode == 0
    gaps = subprocess.run(["python3", "-m", "casework", "readiness", "--pack", "metr_deep", "--gaps"], cwd=CASEWORK, capture_output=True, text=True).stdout
    print(f"6 open elements: {len([l for l in gaps.splitlines() if l.startswith('GAP')])} (informational)")
    print("S1 DONE-WHEN:", "GREEN" if ok else "NOT YET")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
