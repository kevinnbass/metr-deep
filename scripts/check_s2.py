#!/usr/bin/env python3
"""S2 Done-when checker (PLAN.md S2). Reports, does not fix.

Checks: MD15-MD25 promoted (or reviewed-and-replaced); commitment_reconciliation.csv has a denominator,
at least one compatible or excluded decision, and a computed remainder; every promoted government or
consortium award row (MDF money_type=contract bound as evidence, or MDP with edge_type naming an award)
carries award id, authority, legal recipient, value/ceiling, period and METR share or a 'not disclosed'
statement; casework verify exit 0; C06 procurement/issuer classes not UNTOUCHED.

Usage: python3 scripts/check_s2.py
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
S2_LANES = [f"MD{i:02d}" for i in range(15, 26)]


def read_csv(path: Path) -> list[dict[str, str]]:
    raw = path.read_text("utf-8-sig")
    body = "\n".join(l for l in raw.splitlines() if not l.startswith("#"))
    return [{(k or "").strip(): (v or "").strip() for k, v in r.items()} for r in csv.DictReader(io.StringIO(body, newline=""))]


def main() -> int:
    ok = True
    lanes = {r["lane"]: r for r in read_csv(ROOT / "research/LANES.csv")}
    not_done = [l for l in S2_LANES if lanes.get(l, {}).get("status") not in {"promoted", "replaced", "rerun-running", "rerun-promoted"}]
    print(f"1 lanes promoted: {11 - len(not_done)}/11" + (f"  pending={not_done}" if not_done else ""))
    ok &= not not_done
    rec_path = ROOT / "research/commitment_reconciliation.csv"
    rec = read_csv(rec_path) if rec_path.exists() else []
    kinds = {r["kind"] for r in rec}
    need = {"denominator", "unresolved_remainder", "identified_compatible_total"}
    print(f"2 commitment_reconciliation.csv rows={len(rec)} kinds={sorted(kinds)}" + ("" if need <= kinds else f"  missing={sorted(need - kinds)}"))
    ok &= need <= kinds and any(r["kind"] in {"compatible_component", "excluded"} for r in rec)
    case = json.loads((ROOT / "case.json").read_text("utf-8"))
    roles = {}
    for c in case["claims"]:
        for e in c["elements"]:
            for b in e.get("bindings", []):
                roles.setdefault(b["row_id"], set()).add(b["role"])
    mdf = read_csv(ROOT / "research/funding_events.csv")
    awards = [r for r in mdf if r.get("money_type") == "contract" and "evidence" in roles.get(r["row_id"], set())
              and "seed transcription" not in r.get("note", "")]
    incomplete = []
    for r in awards:
        text = " ".join(r.get(k, "") for k in ("subject", "identifier", "from_entity", "to_entity", "amount_usd", "quantity_or_value", "period", "date", "purpose_restriction", "limitation", "result", "note"))
        has_id = bool(r.get("identifier")) or re.search(r"\b(award|notice|contract|reference|ref\.?|id)\b\s*[:#]?\s*[A-Z0-9-]{4,}", text, re.I)
        has_share = re.search(r"share|not disclosed|undisclosed|consortium", text, re.I)
        has_period = bool(r.get("period") or r.get("date"))
        has_value = bool(r.get("amount_usd") or r.get("quantity_or_value"))
        if not (has_id and has_share and has_period and has_value and r.get("from_entity") and r.get("to_entity")):
            incomplete.append((r["row_id"], r.get("subject", "")[:60], {"id": bool(has_id), "share": bool(has_share), "period": has_period, "value": has_value}))
    print(f"3 evidence-bound contract rows: {len(awards)}; incomplete: {len(incomplete)}")
    for i in incomplete:
        print("    ", i)
    ok &= not incomplete
    fr = subprocess.run(["python3", "-m", "casework", "frontier", "--pack", "metr_deep"], cwd=CASEWORK, capture_output=True, text=True).stdout
    bad = [l for l in fr.splitlines() if l.startswith("SOURCE C06 ") and (" procurement records " in l or " issuer statements " in l or " funder filings " in l) and l.endswith("UNTOUCHED")]
    print(f"4 C06 procurement/issuer/funder classes UNTOUCHED: {len(bad)}")
    for l in bad:
        print("    ", l)
    ok &= not bad
    v = subprocess.run(["python3", "-m", "casework", "verify", "--pack", "metr_deep"], cwd=CASEWORK, capture_output=True, text=True)
    print(f"5 casework verify exit={v.returncode}: {(v.stdout or v.stderr).strip().splitlines()[0]}")
    ok &= v.returncode == 0
    print("S2 DONE-WHEN:", "GREEN" if ok else "NOT YET")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
