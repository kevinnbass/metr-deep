#!/usr/bin/env python3
"""Derive research/supporter_coverage.csv (PLAN.md S1 Done-when) from promoted rows only.

One row per supporter METR names plus every filed payer already known. Status is computed, never
typed by hand: `amount_identified` when a promoted MDF row to METR carries a public amount from a
funder-side or recipient-side document; `acknowledged_no_amount` when METR names the supporter but
no promoted row gives an amount; `filed_payer_unnamed_by_metr` for payers that appear only in
filings; `bounded_negative` when the only promoted rows are MDS negatives. Every status cites the
promoted row ids it rests on, so the table can be regenerated after each promotion.

Usage: python3 scripts/build_supporter_coverage.py
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

# canonical supporter key -> (display name, how METR names it, regex over from_entity/subject, owning lanes)
SUPPORTERS = [
    ("audacious", "The Audacious Project (TED)", "named on metr.org/about and the 2026-08-14 update", r"audacious", "MD15;MD16;MD18"),
    ("jane_street_individuals", "individuals from Jane Street", "named on metr.org/about and the 2026-08-14 update", r"jane street", "MD07"),
    ("sijbrandij", "Sijbrandij Foundation", "named on metr.org/about and the 2026-08-14 update", r"sijbrandij", "MD05"),
    ("pew", "The Pew Charitable Trusts", "named on metr.org/about and the 2026-08-14 update", r"\bpew\b", "MD03"),
    ("schmidt", "Schmidt Sciences", "named on metr.org/about and the 2026-08-14 update", r"schmidt", "MD04"),
    ("packard", "The David and Lucile Packard Foundation", "named on metr.org/about and the 2026-08-14 update", r"packard", "MD02"),
    ("lacentra", "LaCentra-Sumerlin Foundation", "named on metr.org/about; 'Frontier Fund' in the 2026-08-14 image alt", r"la ?centra", "MD06"),
    ("astralis", "Astralis Foundation", "named on metr.org/about and the 2026-08-14 image alt", r"astralis", "MD06"),
    ("expa", "Expa.org", "named on metr.org/about and the 2026-08-14 image alt", r"\bexpa", "MD06"),
    ("aisi", "AI Security Institute (UK)", "named on metr.org/about ('partnering with')", r"ai security institute|aisi", "MD19"),
    ("longview", "Longview Philanthropy (pooled funds)", "named on metr.org/about as a pooled fund", r"longview", "MD10"),
    ("effektiv", "Effektiv Spenden (pooled funds)", "named on metr.org/about as a pooled fund", r"effektiv", "MD10"),
    ("sff", "Survival and Flourishing Fund (recommendations)", "named on metr.org/about as recommendations", r"survival and flourishing|\bsff\b", "MD09"),
    ("farhi", "David Farhi", "named on metr.org/about and the 2026-08-14 update", r"farhi", "MD08"),
    ("ralston", "Geoff Ralston", "named on metr.org/about and the 2026-08-14 update", r"ralston", "MD08"),
    ("field", "Dylan Field", "named on metr.org/about and the 2026-08-14 update", r"dylan field", "MD08"),
    ("newman", "Steve Newman", "named on metr.org/about and the 2026-08-14 update", r"steve newman", "MD08"),
    ("arc", "Alignment Research Center (program transfer)", "not named as a supporter; filed related-organisation transfer", r"alignment research center", "MD12;MD01"),
    ("founders_pledge", "Founders Pledge Inc", "not named by METR; filed Schedule I payer", r"founders pledge", "MD10;MD22"),
    ("svcf", "Silicon Valley Community Foundation (DAF sponsor)", "not named by METR; filed Schedule I payer", r"silicon valley community", "MD11"),
    ("vanguard", "Vanguard Charitable Endowment Program (DAF sponsor)", "not named by METR; filed Schedule I payer", r"vanguard charitable", "MD11"),
    ("eu_ai_office", "European AI Office (contract)", "named on metr.org/about as a technical-assistance contract", r"european ai office|eu ai office", "MD20"),
]
METR = re.compile(r"metr|model evaluation", re.I)


def load(prefix: str) -> list[dict[str, str]]:
    path = ROOT / CONFIG["tables"][prefix]["file"]
    if not path.exists():
        return []
    raw = path.read_text("utf-8-sig")
    body = "\n".join(l for l in raw.splitlines() if not l.startswith("#"))
    return [{k: (v or "").strip() for k, v in r.items()} for r in csv.DictReader(io.StringIO(body, newline=""))]


def main() -> int:
    tables = {p: load(p) for p in CONFIG["tables"]}
    seed_only = lambda r: "seed transcription" in r.get("note", "")
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    out = []
    for key, name, how_named, pattern, lanes in SUPPORTERS:
        rx = re.compile(pattern, re.I)
        def hits(prefix):
            return [r for r in tables[prefix] if not seed_only(r)
                    and (rx.search(r.get("from_entity", "")) or rx.search(r.get("subject", "")))]
        mdf = [r for r in hits("MDF") if METR.search(r.get("to_entity", ""))]
        amounts = [r for r in mdf if (r.get("amount_usd") and re.search(r"\d", r["amount_usd"]))
                   or (r.get("currency") and r["currency"] != "USD" and re.search(r"\d", r.get("quantity_or_value", "")))]
        # promoted rows bound as context are not evidence; read the binding role from case.json
        case = json.loads((ROOT / "case.json").read_text("utf-8"))
        roles = {}
        for c in case["claims"]:
            for e in c["elements"]:
                for b in e.get("bindings", []):
                    roles.setdefault(b["row_id"], set()).add(b["role"])
        evid = [r for r in amounts if "evidence" in roles.get(r["row_id"], set())]
        mdr = [r for r in hits("MDR") if METR.search(r.get("to_entity", ""))]
        mdp = [r for r in hits("MDP")]
        mds = [r for r in hits("MDS")]
        mdt = [r for r in hits("MDT")]
        ack = [r for r in mdf + mdr + mdp if re.search(r"acknowledg|named", (r.get("payment_status", "") + r.get("relationship_type", "") + r.get("subject", "")), re.I)]
        if evid:
            status = "amount_identified"
            detail = "; ".join(f"{r['row_id']}: {r.get('money_type') or 'untyped'} {r.get('amount_usd') or r.get('quantity_or_value')} {r.get('currency') or ''} {r.get('date') or r.get('period')}".strip() for r in evid)
        elif ack or any(METR.search(r.get("to_entity", "")) for r in mdf + mdr):
            status = "acknowledged_no_amount"
            detail = "named by METR; no promoted row gives an amount, date or vehicle"
        elif mds and not (mdf or mdr or mdp):
            status = "bounded_negative"
            detail = f"{len(mds)} bounded negatives; no positive row"
        elif not (mdf or mdr or mdp or mds or mdt):
            status = "not_yet_reviewed"
            detail = f"owning lane(s) {lanes} not yet promoted"
        else:
            status = "context_only"
            detail = "promoted rows exist but none is an evidence-bound amount or acknowledgment"
        vehicle = "; ".join(sorted({r.get("money_type") for r in mdf if r.get("money_type")})) or "undisclosed"
        ids = sorted({r["row_id"] for r in mdf + mdr + mdp + mds + mdt})
        out.append({
            "supporter_key": key, "supporter": name, "how_metr_names_it": how_named, "status": status,
            "amount_detail": detail, "money_types_seen": vehicle,
            "positive_rows": ";".join(sorted({r["row_id"] for r in mdf + mdr + mdp})),
            "negative_rows": ";".join(sorted({r["row_id"] for r in mds})),
            "timeline_rows": ";".join(sorted({r["row_id"] for r in mdt})),
            "owning_lanes": lanes, "computed_utc": now,
        })
    fields = list(out[0].keys())
    buf = io.StringIO(newline="")
    buf.write(f"# metr_deep supporter coverage; derived from promoted rows only by scripts/build_supporter_coverage.py at {now}; "
              "seed-context rows excluded; status is computed, never typed by hand; regenerate after every promotion\n")
    w = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(out)
    (ROOT / "research/supporter_coverage.csv").write_text(buf.getvalue(), encoding="utf-8")
    from collections import Counter
    print("supporter_coverage.csv", len(out), dict(Counter(r["status"] for r in out)))
    for r in out:
        print(f"  {r['supporter_key']:24} {r['status']:24} {r['amount_detail'][:110]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
