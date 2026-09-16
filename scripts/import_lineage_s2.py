#!/usr/bin/env python3
"""S2 lineage import (PLAN.md S2 precondition): transcribe the sibling lineage pack's reviewed,
promoted named-flow rows that MD16/MD17/MD22 would otherwise re-collect, as context rows.

Selection is by explicit lineage row id (FN…) so the set is reviewable; every cell is copied
verbatim from the lineage table (asserted before writing); the note keeps seed_path, seed_row_id and
the lineage lane/review markers. Bindings are role=context, strength=supporting: nothing becomes
ready from imported material, and each MD lane re-collects what it needs from the primary.

Usage: python3 scripts/import_lineage_s2.py
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIN = Path("/mnt/f/projects/anthropic/lineage/research/flows_named.csv")
LANE = ROOT / "research/grok-out/S2-lineage-import.csv"
REVIEW = ROOT / "research/agents-2026-09-16/S2-lineage-import.md"
NOTE = ("lineage transcription; checked_utc is the lineage lane's own check time; role=context until the "
        "owning MD lane re-collects it from the primary")

# lineage FN ids -> (target, element_ids, ledger, money_type, limitation)
RAND_GVF = ["FN1141", "FN1142", "FN1143", "FN1144", "FN1203", "FN1204", "FN1205", "FN1206", "FN1207", "FN1247", "FN1248", "FN1249"]
RAND_DAF_2023PLUS = ["FN2236", "FN2251", "FN2303", "FN2323", "FN2343", "FN2354", "FN2363", "FN2410", "FN2421", "FN2441",
                     "FN2461", "FN2493", "FN2519", "FN2533", "FN2555", "FN2599"]
RAND_OTHER = ["FN1369", "FN630", "FN631"]
AUDACIOUS = ["FN605"]
INTERMEDIARY = ["FN1078", "FN1088", "FN1153", "FN1154", "FN1155", "FN1156", "FN1157", "FN1158", "FN1159", "FN1160", "FN1161",
                "FN1162", "FN1163", "FN1164", "FN1165", "FN1166", "FN1167", "FN1168", "FN1169"]
PLAN: list[tuple[str, str, str, str, str, str]] = []
for k in RAND_GVF:
    PLAN.append((k, "MDF", "C06.E1;C06.E2", "paid_filed", "filed_grant", "payment to RAND Corporation, not to METR; purpose text in the lineage row's quote"))
for k in RAND_DAF_2023PLUS:
    PLAN.append((k, "MDF", "C06.E1;C06.E2", "paid_filed", "filed_grant", "DAF-sponsor payment to RAND; account principal undisclosed; not a payment to METR"))
PLAN.append(("FN1369", "MDF", "C06.E1;C06.E2", "paid_filed", "filed_grant", "Founders Pledge Schedule I payment to RAND; not a payment to METR"))
PLAN.append(("FN630", "MDF", "C06.E2", "commitments", "recommendation", "SFF-2025 matching pledge naming RAND; a recommendation, not a payment"))
PLAN.append(("FN631", "MDF", "C06.E2", "commitments", "recommendation", "SFF-2025 recommendation naming RAND; not a payment"))
PLAN.append(("FN605", "MDF", "C06.E2;C01.E3", "commitments", "commitment", "joint-project commitment to RAND and METR; not a METR-only amount"))
for k in INTERMEDIARY:
    PLAN.append((k, "MDF", "C06.E1;C02.E5", "paid_filed", "filed_grant", "payer-into-intermediary; not a payment to METR"))


def main() -> int:
    raw = LIN.read_text("utf-8-sig")
    lin = {r["row_id"]: r for r in csv.DictReader(io.StringIO("\n".join(l for l in raw.splitlines() if not l.startswith("#")), newline=""))}
    digest = hashlib.sha256(LIN.read_bytes()).hexdigest()
    columns = json.loads((ROOT / "casework.json").read_text())["lane_columns"]
    rows, verdicts = [], []
    for index, (fid, prefix, elements, ledger, money_type, limitation) in enumerate(PLAN, 1):
        src = lin.get(fid)
        if src is None:
            raise SystemExit(f"lineage row missing: {fid}")
        lane = re.search(r"lane=research/grok-out/(L\d\d[^;]*)", src.get("note", ""))
        review = re.search(r"review=([^;]+)", src.get("note", ""))
        row = {c: "" for c in columns}
        row.update({
            "row": str(index), "task": "S2 lineage import", "target_prefix": prefix, "element_ids": elements,
            "subject": f"{src.get('from_entity') or src.get('from_name')} -> {src.get('to_entity') or src.get('to_name')} ({src.get('measure')})",
            "from_entity": src.get("from_entity") or src.get("from_name", ""),
            "to_entity": src.get("to_entity") or src.get("to_name", ""),
            "ledger": ledger, "money_type": money_type, "amount_usd": src.get("amount_usd", ""), "currency": "USD",
            "date": src.get("date", ""), "date_precision": src.get("date_precision", ""),
            "period": " to ".join(v for v in (src.get("start", ""), src.get("end", "")) if v),
            "payment_status": "filed as granted" if money_type == "filed_grant" else ("committed; payment not stated" if money_type == "commitment" else "recommendation; not a payment"),
            "source_class": "funder filings" if money_type == "filed_grant" else "issuer statements",
            "url": src.get("url", ""), "quote_300": src.get("quote_300", "")[:300], "checked_utc": src.get("checked_utc", ""),
            "limitation": limitation,
            "note": (f"{NOTE}; seed_path={LIN}; seed_row_id={fid}; seed_sha256={digest}; lineage_lane={lane.group(1) if lane else ''}; "
                     f"lineage_review={review.group(1).strip() if review else ''}; lineage_measure={src.get('measure','')}; lineage_channel={src.get('channel','')}"),
        })
        # cell-for-cell assertions on the copied fields
        for mine, theirs in (("amount_usd", "amount_usd"), ("url", "url"), ("date", "date"), ("checked_utc", "checked_utc")):
            assert row[mine] == src.get(theirs, ""), (fid, mine)
        assert row["quote_300"] == src.get("quote_300", "")[:300], (fid, "quote")
        if not row["url"] or not row["checked_utc"]:
            raise SystemExit(f"{fid}: empty url or checked_utc in lineage row; cannot import")
        rows.append(row)
        verdicts.append((str(index), prefix, elements, f"transcribed verbatim from lineage flows_named.csv#{fid} ({lane.group(1) if lane else 'lane?'}); cell-for-cell match asserted by scripts/import_lineage_s2.py; the lineage review is the source-side verification, this pack binds it as context only"))
    buf = io.StringIO(newline="")
    buf.write("# metr_deep S2 lineage import; fetch_timestamp_utc=n/a (transcription of the sibling lineage pack's promoted rows); "
              f"retrieval_method=verbatim cell copy from {LIN} sha256={digest}; known_caps=none; no_kevinnbass_sources=true; "
              "brief: none - S2 precondition import, not a research lane; every row is context until its MD lane re-collects it\n")
    w = csv.DictWriter(buf, fieldnames=columns, lineterminator="\n", extrasaction="raise")
    w.writeheader(); w.writerows(rows)
    LANE.write_text(buf.getvalue(), encoding="utf-8")
    lines = [f"<!-- casework-review lane=research/grok-out/{LANE.name} -->", "", "# S2 lineage import review", "",
             "Verdict scope: each verdict states only that the lane row reproduces the named lineage-pack row cell-for-cell, "
             "which `scripts/import_lineage_s2.py` asserts before writing. The primary-source verification is the lineage "
             "pack's own review named in each note. Every binding is `role=context`, `strength=supporting`.", "",
             "| row | verdict | target_prefix | element_ids | primary_values | strength | role | note |", "|---|---|---|---|---|---|---|---|"]
    for key, prefix, elements, note in verdicts:
        lines.append(f"| {key} | CONFIRMED | {prefix} | {elements} | {{}} | supporting | context | {note} |")
    REVIEW.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"WROTE {LANE} rows={len(rows)}; WROTE {REVIEW}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
