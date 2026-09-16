#!/usr/bin/env python3
"""Derive research/commitment_reconciliation.csv (PLAN.md S2 Done-when) from promoted rows only.

Rows: the denominator (METR's approximately $71M commitment statement), every identified compatible
component, every excluded or non-comparable amount with its stated reason, and the unresolved
remainder computed as denominator minus the compatible components. Sources are the MDP propositions
bound to C01 (compatibility decisions) and the MDF funding events they refer to. Nothing is summed
across money types: the compatible total is a sum of commitment-type USD amounts only.

Usage: python3 scripts/build_commitment_reconciliation.py
"""
from __future__ import annotations

import csv
import datetime as dt
import io
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / "casework.json").read_text("utf-8"))


def load(prefix: str) -> list[dict[str, str]]:
    path = ROOT / CONFIG["tables"][prefix]["file"]
    raw = path.read_text("utf-8-sig")
    body = "\n".join(l for l in raw.splitlines() if not l.startswith("#"))
    return [{k: (v or "").strip() for k, v in r.items()} for r in csv.DictReader(io.StringIO(body, newline=""))]


def main() -> int:
    case = json.loads((ROOT / "case.json").read_text("utf-8"))
    roles: dict[str, set] = {}
    elems: dict[str, set] = {}
    for c in case["claims"]:
        for e in c["elements"]:
            for b in e.get("bindings", []):
                roles.setdefault(b["row_id"], set()).add(b["role"])
                elems.setdefault(b["row_id"], set()).add(e["element_id"])
    mdp = load("MDP"); mdf = load("MDF")
    seed = lambda r: "seed transcription" in r.get("note", "") or "lineage transcription" in r.get("note", "")
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    out = []
    # denominator: MDF row bound as evidence to C01.E1 with money_type commitment
    denom = [r for r in mdf if not seed(r) and "C01.E1" in elems.get(r["row_id"], set()) and "evidence" in roles.get(r["row_id"], set()) and r.get("money_type") == "commitment"]
    for r in denom:
        out.append(dict(kind="denominator", row_id=r["row_id"], counterparty=r.get("from_entity", ""), money_type=r["money_type"],
                        amount_usd=r.get("amount_usd", ""), currency=r.get("currency", ""), date=r.get("date", ""), period=r.get("period", ""),
                        decision="denominator", reason="METR's own statement of commitments raised in the last 6 months; approximate", url=r.get("url", "")))
    # compatibility propositions: MDP rows bound to C01.E2 (compatible) or C01.E3 (excluded), evidence role
    for r in mdp:
        if seed(r):
            continue
        ids = elems.get(r["row_id"], set()); rl = roles.get(r["row_id"], set())
        if "evidence" not in rl:
            continue
        res = r.get("result", "")
        if "C01.E2" in ids and re.search(r"compatible=yes", res):
            kind, decision = "compatible_component", "included"
        elif "C01.E3" in ids and re.search(r"compatible=no|excluded", res + r.get("subject", ""), re.I):
            kind, decision = "excluded", "excluded"
        elif "C01.E4" in ids:
            kind, decision = "remainder_statement", "derived"
        else:
            continue
        out.append(dict(kind=kind, row_id=r["row_id"], counterparty=r.get("from_entity", ""), money_type=r.get("money_type", ""),
                        amount_usd=r.get("amount_usd", ""), currency=r.get("currency", ""), date=r.get("date", ""), period=r.get("period", ""),
                        decision=decision, reason=(r.get("limitation", "") or res)[:300], url=r.get("url", "")))
    comp = [o for o in out if o["kind"] == "compatible_component" and o["money_type"] == "commitment" and re.fullmatch(r"\d+", o["amount_usd"] or "")]
    total = sum(int(o["amount_usd"]) for o in comp)
    den = next((int(o["amount_usd"]) for o in out if o["kind"] == "denominator" and re.fullmatch(r"\d+", o["amount_usd"] or "")), None)
    den_url = next((o["url"] for o in out if o["kind"] == "denominator"), "")
    if den is not None:
        out.append(dict(kind="identified_compatible_total", row_id=";".join(o["row_id"] for o in comp), counterparty="", money_type="commitment",
                        amount_usd=str(total), currency="USD", date="", period="", decision="computed",
                        reason=f"sum of {len(comp)} compatible commitment-type USD component(s); no other money type included", url=den_url))
        out.append(dict(kind="unresolved_remainder", row_id="", counterparty="", money_type="commitment", amount_usd=str(den - total), currency="USD",
                        date="", period="", decision="computed", reason=f"denominator (around {den}) minus identified compatible total ({total}); inherits 'around'; composition unknown from public sources checked; residual, not a donor list", url=den_url))
    fields = ["kind", "row_id", "counterparty", "money_type", "amount_usd", "currency", "date", "period", "decision", "reason", "url"]
    buf = io.StringIO(newline="")
    buf.write(f"# metr_deep commitment reconciliation; derived from promoted rows only by scripts/build_commitment_reconciliation.py at {now}; "
              "seed and lineage context rows excluded; money types never summed across type; regenerate after every promotion\n")
    w = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n"); w.writeheader(); w.writerows(out)
    (ROOT / "research/commitment_reconciliation.csv").write_text(buf.getvalue(), encoding="utf-8")
    from collections import Counter
    print("commitment_reconciliation.csv", len(out), dict(Counter(o["kind"] for o in out)), "| denominator", den, "| compatible", total, "| remainder", (den - total) if den is not None else None)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
