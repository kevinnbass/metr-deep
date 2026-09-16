#!/usr/bin/env python3
"""Scaffold the metr_deep pack's MD* tables (PLAN.md §3) so `python3 -m casework promote` has a
table to mint into.

Idempotent and additive: an existing table keeps every row and column; a missing table is created;
a missing column is appended to the header and left empty on existing rows. No row or cell is ever
removed. Every table carries every lane output column declared in casework.json, because promotion
copies a reviewed lane row column-for-column and drops whatever the target header lacks.

Usage: python3 scripts/build_tables.py
"""
from __future__ import annotations

import csv
import datetime as dt
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / "casework.json").read_text("utf-8"))
LANE = [c for c in CONFIG["lane_columns"] if c not in ("row", "note")]
COMMON = ["url", "quote_300", "source_class", "checked_utc", "review_verdict", "lane", "note"]

# table-specific columns; the lane columns and the common evidence columns are appended to each
SPECIFIC: dict[str, list[str]] = {
    "MDE": ["subject", "entity_type", "aliases", "identifier"],
    "MDF": ["ledger", "money_type", "amount_usd", "currency", "from_entity", "to_entity",
            "date", "date_precision", "period", "payment_status", "purpose_restriction"],
    "MDI": ["provider", "to_entity", "project", "in_kind_type", "quantity_or_value", "terms"],
    "MDP": ["subject", "from_entity", "intermediary", "to_entity", "edge_type", "documented_transaction"],
    "MDQ": ["project", "provider", "policy_version", "terms", "disclosure_recusal", "provider_authority",
            "personnel_conflicts"],
    "MDR": ["subject", "to_entity", "relationship_type", "start_date", "end_date"],
    "MDS": ["source_class", "query_or_endpoint", "result", "result_count", "limitation", "next_document"],
    "MDT": ["date", "date_precision", "subject", "from_entity", "to_entity", "relationship_type"],
}


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def header_for(prefix: str) -> list[str]:
    out = ["row_id"]
    for column in SPECIFIC[prefix] + LANE + COMMON:
        if column not in out:
            out.append(column)
    return out


def read_table(path: Path) -> tuple[list[str], list[str], list[dict[str, str]]]:
    if not path.exists():
        return [], [], []
    raw = path.read_text("utf-8-sig")
    comments = [line for line in raw.splitlines() if line.startswith("#")]
    body = "\n".join(line for line in raw.splitlines() if not line.startswith("#"))
    reader = csv.DictReader(io.StringIO(body, newline=""))
    fields = [str(v).strip() for v in (reader.fieldnames or [])]
    rows = [{str(k).strip(): (v or "") for k, v in row.items()} for row in reader]
    return comments, fields, rows


def main() -> int:
    for prefix, spec in sorted(CONFIG["tables"].items()):
        path = ROOT / spec["file"]
        comments, fields, rows = read_table(path)
        wanted = header_for(prefix)
        merged = list(fields) + [c for c in wanted if c not in fields]
        if not fields:
            merged = wanted
            comments = [
                f"# metr_deep {prefix} table {path.name}; scaffolded by scripts/build_tables.py {utc_now()}; "
                f"ids {prefix}NNN; rows enter only through `python3 -m casework promote` from a reviewed lane, "
                f"or from a reviewed seed import named in note; rows are never deleted, corrections append an audit note"
            ]
        buffer = io.StringIO(newline="")
        for comment in comments:
            buffer.write(comment + "\n")
        writer = csv.DictWriter(buffer, fieldnames=merged, lineterminator="\n", extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({c: row.get(c, "") for c in merged})
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(buffer.getvalue(), encoding="utf-8")
        print(f"TABLE {prefix} {spec['file']} columns={len(merged)} rows={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
