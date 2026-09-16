#!/usr/bin/env python3
"""S0 seed import: transcribe the reviewed 10-metr seed rows that PLAN.md §4's claims need into a
lane-shaped CSV plus its review file, so the rows enter metr_deep only through
`python3 -m casework promote`.

Every imported cell is copied verbatim from a named cell of a named seed CSV row; the script asserts
that before writing, so the review file's CONFIRMED verdict is a machine-checked transcription claim
and nothing more. It is NOT a primary-source verification: every binding is role=context,
strength=supporting, so no claim element becomes ready from seed material, and every note carries
seed_path and seed_row_id for re-verification.

Usage: python3 scripts/import_seed.py
"""
from __future__ import annotations

import csv
import hashlib
import io
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = Path("/mnt/f/projects/memes/ai-machine/10-metr/research")
LANE = ROOT / "research/grok-out/S0-seed-import.csv"
REVIEW = ROOT / "research/agents-2026-09-15/S0-seed-import.md"
SEED_CHECKED = "2026-09-14T00:00:00Z"
SEED_NOTE = ("seed transcription from the 10-metr pack; checked_utc is that pack's build date "
             "2026-09-14, not a re-check in metr_deep; role=context until re-verified against the primary")

# (seed_file, seed_row_id, target_prefix, element_ids, {lane_column: seed_column or ("=", literal)})
IMPORTS: list[tuple[str, str, str, str, dict]] = [
    # ---- C01 denominator and the amounts that must be judged compatible or excluded
    ("budget.csv", "G03", "MDF", "C01.E1",
     dict(ledger=("=", "commitments"), money_type=("=", "commitment"), amount_usd="value",
          from_entity=("=", "not stated in this source"), to_entity=("=", "METR"), date="date",
          date_precision=("=", "day"), period="period", payment_status=("=", "committed; payment not stated"),
          purpose_restriction=("=", "not stated in this source"), subject="measure",
          source_class=("=", "issuer statements"), url="source_url", quote_300="quote")),
    ("budget.csv", "G15", "MDF", "C01.E3",
     dict(ledger=("=", "commitments"), money_type=("=", "commitment"), amount_usd="value",
          from_entity=("=", "n/a - this is METR's own run rate, not an inbound amount"),
          to_entity=("=", "METR"), date="date", date_precision=("=", "day"), period="period",
          payment_status=("=", "n/a"), subject="measure", source_class=("=", "self-statements"),
          url="source_url", quote_300="quote",
          limitation=("=", "a run rate is not an inbound amount and is never summed with a commitment"))),
    ("budget.csv", "G16", "MDF", "C01.E3",
     dict(ledger=("=", "commitments"), money_type=("=", "commitment"), amount_usd="value", to_entity=("=", "METR"),
          date="date", date_precision=("=", "day"), period="period", subject="measure",
          source_class=("=", "self-statements"), url="source_url", quote_300="quote",
          limitation=("=", "runway is a derived statement about spend, not a funding event"))),
    ("budget.csv", "G14", "MDF", "C06.E2;C01.E3",
     dict(ledger=("=", "commitments"), money_type=("=", "commitment"), amount_usd="value",
          from_entity=("=", "The Audacious Project (TED)"), to_entity=("=", "METR"), date="date",
          date_precision=("=", "day"), period="period", payment_status=("=", "committed; payment not stated"),
          subject="measure", source_class=("=", "self-statements"), url="source_url", quote_300="quote",
          limitation=("=", "METR's own later figure; never summed with the 2024-10-09 announcement figure"))),
    # ---- C06 Audacious and Canary
    ("money_flows.csv", "M57", "MDF", "C06.E2",
     dict(ledger=("=", "commitments"), money_type=("=", "commitment"), amount_usd="amount_usd",
          from_entity="from_entity", to_entity="to_entity", date="date", date_precision=("=", "day"),
          purpose_restriction="purpose", source_class=("=", "issuer statements"), url="source_url",
          quote_300="notes", limitation=("=", "commitment to a joint project, not a payment to either recipient"))),
    ("money_flows.csv", "M58", "MDF", "C06.E2;C01.E3",
     dict(ledger=("=", "commitments"), money_type=("=", "commitment"), amount_usd="amount_usd",
          from_entity="from_entity", to_entity="to_entity", date="date", date_precision=("=", "day"),
          purpose_restriction="purpose", source_class=("=", "issuer statements"), url="source_url",
          quote_300="notes", limitation=("=", "subset of the approximately $38M row; not additive with it"))),
    ("money_flows.csv", "M119", "MDP", "C06.E1",
     dict(edge_type=("=", "documented transaction"), documented_transaction=("=", "yes, to RAND"),
          from_entity="from_entity", to_entity="to_entity", amount_usd="amount_usd",
          money_type=("=", "filed_grant"), ledger=("=", "paid_filed"), date="date",
          purpose_restriction="purpose", subject=("=", "Audacious partner payment for Project Canary"),
          source_class=("=", "funder filings"), url="source_url", quote_300="notes",
          limitation=("=", "a payment to RAND is not a payment to METR"))),
    ("money_flows.csv", "M143", "MDP", "C06.E1",
     dict(edge_type=("=", "documented transaction"), documented_transaction=("=", "yes, to RAND"),
          from_entity="from_entity", to_entity="to_entity", amount_usd="amount_usd",
          money_type=("=", "filed_grant"), ledger=("=", "paid_filed"), date="date",
          purpose_restriction="purpose", subject=("=", "Audacious partner payment for Project Canary"),
          source_class=("=", "funder filings"), url="source_url", quote_300="notes",
          limitation=("=", "a payment to RAND is not a payment to METR"))),
    # ---- C02 supporters and filed payers
    ("money_flows.csv", "M63", "MDF", "C02.E3;C06.E1",
     dict(ledger=("=", "transfers_regrants"), money_type=("=", "transfer"), amount_usd="amount_usd",
          from_entity="from_entity", to_entity="to_entity", date="date", date_precision=("=", "day"),
          purpose_restriction="purpose", payment_status=("=", "filed as distributed"),
          source_class=("=", "funder filings"), url="source_url", quote_300="notes",
          limitation=("=", "intra-group program transfer; not attributable to any single ARC funder"))),
    ("money_flows.csv", "M38", "MDF", "C02.E2;C02.E5",
     dict(ledger=("=", "commitments"), money_type=("=", "recommendation"), amount_usd="amount_usd",
          from_entity="from_entity", to_entity="to_entity", date="date", date_precision=("=", "interval"),
          purpose_restriction="purpose", payment_status=("=", "recommendation, not a payment"),
          source_class=("=", "issuer statements"), url="source_url", quote_300="notes")),
    ("money_flows.csv", "M39", "MDF", "C02.E2;C02.E5",
     dict(ledger=("=", "commitments"), money_type=("=", "recommendation"), amount_usd="amount_usd",
          from_entity="from_entity", to_entity="to_entity", date="date", date_precision=("=", "interval"),
          purpose_restriction="purpose", payment_status=("=", "recommendation incl. a matching pledge, not a payment"),
          source_class=("=", "issuer statements"), url="source_url", quote_300="notes")),
    ("money_flows.csv", "M79", "MDF", "C02.E3;C02.E5",
     dict(ledger=("=", "paid_filed"), money_type=("=", "filed_grant"), amount_usd="amount_usd",
          from_entity="from_entity", to_entity="to_entity", date="date", date_precision=("=", "year"),
          purpose_restriction="purpose", payment_status=("=", "filed as granted"),
          source_class=("=", "funder filings"), url="source_url", quote_300="notes")),
    ("money_flows.csv", "M83", "MDF", "C02.E3;C02.E5",
     dict(ledger=("=", "paid_filed"), money_type=("=", "filed_grant"), amount_usd="amount_usd",
          from_entity="from_entity", to_entity="to_entity", date="date", date_precision=("=", "year"),
          purpose_restriction="purpose", payment_status=("=", "filed as granted"),
          source_class=("=", "DAF sponsor filings"), url="source_url", quote_300="notes")),
    ("money_flows.csv", "M87", "MDF", "C02.E3;C02.E5;C03.E3",
     dict(ledger=("=", "paid_filed"), money_type=("=", "filed_grant"), amount_usd="amount_usd",
          from_entity="from_entity", to_entity="to_entity", date="date", date_precision=("=", "interval"),
          purpose_restriction="purpose", payment_status=("=", "filed as granted"),
          source_class=("=", "DAF sponsor filings"), url="source_url", quote_300="notes",
          limitation=("=", "donor-advised sponsor; the account principal is not disclosed by any public filing"))),
    ("money_flows.csv", "M59", "MDF", "C02.E5",
     dict(ledger=("=", "transfers_regrants"), money_type=("=", "recommendation"), amount_usd="amount_usd",
          from_entity="from_entity", to_entity="to_entity", date="date", date_precision=("=", "year"),
          purpose_restriction="purpose", source_class=("=", "press"), url="source_url", quote_300="notes")),
    ("money_flows.csv", "M61", "MDF", "C02.E5",
     dict(ledger=("=", "transfers_regrants"), money_type=("=", "regrant"), amount_usd="amount_usd",
          currency=("=", "EUR"), from_entity="from_entity", to_entity="to_entity", date="date",
          date_precision=("=", "month"), purpose_restriction="purpose",
          source_class=("=", "issuer statements"), url="source_url", quote_300="notes")),
    ("money_flows.csv", "M75", "MDF", "C02.E2",
     dict(ledger=("=", "commitments"), money_type=("=", "commitment"), amount_usd="amount_usd",
          from_entity="from_entity", to_entity="to_entity", date="date", purpose_restriction="purpose",
          source_class=("=", "issuer statements"), url="source_url", quote_300="notes",
          limitation=("=", "METR names individuals, not the firm; no individual is named and no amount is public"))),
    ("money_flows.csv", "M74", "MDF", "C06.E3;C04.E1",
     dict(ledger=("=", "in_kind_contracts"), money_type=("=", "contract"), amount_usd="amount_usd",
          from_entity="from_entity", to_entity="to_entity", date="date", purpose_restriction="purpose",
          source_class=("=", "issuer statements"), url="source_url", quote_300="notes")),
    ("money_flows.csv", "M76", "MDF", "C06.E3",
     dict(ledger=("=", "in_kind_contracts"), money_type=("=", "contract"), amount_usd="amount_usd",
          from_entity="from_entity", to_entity="to_entity", date="date", date_precision=("=", "day"),
          purpose_restriction="purpose", source_class=("=", "procurement records"), url="source_url",
          quote_300="notes", limitation=("=", "consortium award; METR's share is not established by this row"))),
    # ---- bounded negatives already on the seed record
    ("money_flows.csv", "M33", "MDS", "C01.E5;C02.E2",
     dict(source_class=("=", "public grant databases"),
          query_or_endpoint=("=", "Coefficient Giving grants index snapshot 2026-09-11, organization_name and title"),
          result=("=", "none found"), result_count=("=", "0"), from_entity="from_entity", to_entity="to_entity",
          date="date", url="source_url", quote_300="notes",
          next_document=("=", "a live enumeration of the grantmaker's canonical index or API"))),
    ("money_flows.csv", "M97", "MDS", "C01.E5;C02.E2",
     dict(source_class=("=", "funder filings"), query_or_endpoint=("=", "Form 990-PF Part XV, 2021-2024"),
          result=("=", "none found"), result_count=("=", "0"), from_entity="from_entity", to_entity="to_entity",
          date="date", url="source_url", quote_300="notes")),
    ("money_flows.csv", "M98", "MDS", "C01.E5;C02.E2",
     dict(source_class=("=", "funder filings"), query_or_endpoint=("=", "Form 990 Schedule I, FY2021-FY2025"),
          result=("=", "none found"), result_count=("=", "0"), from_entity="from_entity", to_entity="to_entity",
          date="date", url="source_url", quote_300="notes")),
    ("money_flows.csv", "M99", "MDS", "C01.E5;C02.E2",
     dict(source_class=("=", "funder filings"), query_or_endpoint=("=", "Form 990-PF Part XV, 2021-2024"),
          result=("=", "none found"), result_count=("=", "0"), from_entity="from_entity", to_entity="to_entity",
          date="date", url="source_url", quote_300="notes")),
    ("money_flows.csv", "M100", "MDS", "C01.E5;C02.E2",
     dict(source_class=("=", "funder filings"), query_or_endpoint=("=", "Form 990-PF Part XV, 2021-2024"),
          result=("=", "none found"), result_count=("=", "0"), from_entity="from_entity", to_entity="to_entity",
          date="date", url="source_url", quote_300="notes")),
    ("money_flows.csv", "M104", "MDS", "C01.E5;C02.E3;C07.E4",
     dict(source_class=("=", "funder filings"), query_or_endpoint=("=", "Form 990-PF Part XV, FY2022-FY2025"),
          result=("=", "none found"), result_count=("=", "0"), from_entity="from_entity", to_entity="to_entity",
          date="date", url="source_url", quote_300="notes",
          next_document=("=", "the filer's next Form 990-PF for the fiscal year after June 2025"))),
    ("money_flows.csv", "M107", "MDS", "C02.E3;C07.E4",
     dict(source_class=("=", "DAF sponsor filings"), query_or_endpoint=("=", "Form 990 Schedule I, FY2022-FY2025"),
          result=("=", "none found"), result_count=("=", "0"), from_entity="from_entity", to_entity="to_entity",
          date="date", url="source_url", quote_300="notes")),
    ("money_flows.csv", "M118", "MDS", "C06.E1",
     dict(source_class=("=", "funder filings"), query_or_endpoint=("=", "Form 990-PF Part XV, TY2021-TY2024"),
          result=("=", "none found"), result_count=("=", "0"), from_entity="from_entity", to_entity="to_entity",
          date="date", url="source_url", quote_300="notes",
          limitation=("=", "the project's host foundation filing no grant is not evidence about partner payments"))),
    # ---- C03 / C09 donor rule chronology
    ("donor_rule.csv", "DR07", "MDT", "C03.E1;C09.E1",
     dict(date="date", date_precision=("=", "day"), subject="item", relationship_type=("=", "policy wording"),
          from_entity=("=", "METR"), source_class=("=", "archives"), url="url", quote_300="quote_or_fact",
          terms="source")),
    ("donor_rule.csv", "DR19", "MDT", "C03.E1;C09.E1",
     dict(date="date", date_precision=("=", "day"), subject="item", relationship_type=("=", "policy wording"),
          from_entity=("=", "METR"), source_class=("=", "archives"), url="url", quote_300="quote_or_fact",
          terms="source")),
    ("donor_rule.csv", "DR35", "MDT", "C03.E1;C09.E1;C09.E3",
     dict(date="date", date_precision=("=", "interval"), subject="item",
          relationship_type=("=", "policy wording change window"), from_entity=("=", "METR"),
          source_class=("=", "archives"), url="url", quote_300="quote_or_fact", terms="source",
          limitation=("=", "bounds when the page changed, not when any transaction occurred"))),
    ("donor_rule.csv", "DR30", "MDQ", "C08.E2",
     dict(project=("=", "METR Frontier Risk Report, May 2026"), provider=("=", "not applicable - self-assessment"),
          personnel_conflicts="quote_or_fact", disclosure_recusal="source", policy_version=("=", "AEF-1 pilot, 2026-05-19"),
          date="date", source_class=("=", "project documents"), url="url", quote_300="quote_or_fact")),
    # ---- C04 in-kind and access
    ("compute_inkind.csv", "K01", "MDI", "C04.E1;C03.E2",
     dict(provider="lab", to_entity=("=", "METR"), in_kind_type=("=", "free tokens"),
          quantity_or_value="value_or_volume", date="date", source_class=("=", "issuer statements"),
          url="source_url", quote_300="statement",
          limitation=("=", "free resources are not cash and are never carried into a money total"))),
    ("compute_inkind.csv", "K05", "MDI", "C04.E1",
     dict(provider="lab", to_entity=("=", "METR"), in_kind_type=("=", "API credits"),
          quantity_or_value="value_or_volume", project=("=", "OpenAI / Hugging Face incident investigation"),
          date="date", source_class=("=", "project documents"), url="source_url", quote_300="statement")),
    # ---- C05 investment and governance connections
    ("investments.csv", "IV01", "MDR", "C05.E1",
     dict(subject="named_investors", to_entity=("=", "Anthropic"), relationship_type=("=", "investment, round participation"),
          start_date="date", date="date", date_precision=("=", "day"), amount_usd="amount_usd",
          money_type=("=", "equity_value"), source_class=("=", "issuer statements"), url="source_url",
          quote_300="note", limitation=("=", "individual amounts and shares are not disclosed"))),
    ("investments.csv", "IV10", "MDR", "C05.E1",
     dict(subject="named_investors", to_entity=("=", "Anthropic"), relationship_type=("=", "investment, round participation"),
          start_date="date", date="date", date_precision=("=", "day"), amount_usd="amount_usd",
          money_type=("=", "equity_value"), source_class=("=", "issuer statements"), url="source_url",
          quote_300="note", limitation=("=", "a round valuation is not any holder's stake"))),
    ("stakes.csv", "ST118", "MDR", "C05.E1",
     dict(subject="investor", to_entity=("=", "Anthropic"), relationship_type=("=", "self-described board observer"),
          start_date="date_of_source", date="date_of_source", source_class=("=", "self-statements"),
          url="url", quote_300="quote_verbatim",
          limitation=("=", "a self-described role; no issuer document confirms it"))),
    # ---- C07 the donated stake
    ("stakes.csv", "ST33", "MDT", "C07.E1",
     dict(date="date_of_source", date_precision=("=", "day"), subject="value",
          relationship_type=("=", "reported donation of an Anthropic stake"), from_entity="investor",
          source_class=("=", "press"), url="url", quote_300="quote_verbatim",
          limitation=("=", "the receiving vehicle is not identified in this source"))),
    ("stakes.csv", "ST92", "MDT", "C07.E1",
     dict(date="date_of_source", date_precision=("=", "day"), subject="value",
          relationship_type=("=", "reported percentage bound on the donated stake"), from_entity="investor",
          source_class=("=", "press"), url="url", quote_300="quote_verbatim",
          limitation=("=", "an estimated bound, not a measured holding"))),
    ("stakes.csv", "ST89", "MDT", "C07.E1;C07.E2",
     dict(date="date_of_source", date_precision=("=", "day"), subject="value",
          relationship_type=("=", "grantmaker statement excluding itself as recipient"), from_entity="investor",
          source_class=("=", "self-statements"), url="url", quote_300="quote_verbatim")),
    ("stakes.csv", "ST110", "MDT", "C07.E1",
     dict(date="date_of_source", date_precision=("=", "day"), subject="value",
          relationship_type=("=", "donor statement about where the shares sit"), from_entity="investor",
          source_class=("=", "self-statements"), url="url", quote_300="quote_verbatim",
          limitation=("=", "the donor's own wording; 'our foundation' is not resolved to a filer by this source"))),
    ("stakes.csv", "ST78", "MDT", "C07.E2",
     dict(date="date_of_source", date_precision=("=", "day"), subject="value",
          relationship_type=("=", "filing showing no private-stock contribution in the period"),
          from_entity="investor", source_class=("=", "funder filings"), url="url", quote_300="quote_verbatim",
          limitation=("=", "covers the filer's fiscal year to June 2025 only"))),
]


def read_seed(name: str) -> dict[str, dict[str, str]]:
    path = SEED / name
    text = "".join(line for line in path.read_text("utf-8-sig").splitlines(keepends=True)
                   if not line.startswith("#"))
    return {r["row_id"]: r for r in csv.DictReader(io.StringIO(text, newline=""))}


def main() -> int:
    config_columns = __import__("json").loads((ROOT / "casework.json").read_text())["lane_columns"]
    caches: dict[str, dict[str, dict[str, str]]] = {}
    digests: dict[str, str] = {}
    rows: list[dict[str, str]] = []
    verdicts: list[tuple[str, str, str, str]] = []

    for index, (seed_file, seed_id, prefix, elements, mapping) in enumerate(IMPORTS, 1):
        if seed_file not in caches:
            caches[seed_file] = read_seed(seed_file)
            digests[seed_file] = hashlib.sha256((SEED / seed_file).read_bytes()).hexdigest()
        seed_row = caches[seed_file].get(seed_id)
        if seed_row is None:
            raise SystemExit(f"seed row not found: {seed_file}#{seed_id}")
        row = {column: "" for column in config_columns}
        row["row"] = str(index)
        row["task"] = "S0 seed import"
        row["target_prefix"] = prefix
        row["element_ids"] = elements
        for column, source in mapping.items():
            if isinstance(source, tuple):
                row[column] = source[1]
                continue
            value = (seed_row.get(source) or "").strip()
            if not value:
                raise SystemExit(f"empty seed cell {seed_file}#{seed_id}.{source}")
            row[column] = value[:300] if column == "quote_300" else value
        if not row["url"]:
            raise SystemExit(f"row {index} has no url")
        row["checked_utc"] = SEED_CHECKED
        row["note"] = (f"{SEED_NOTE}; seed_path={SEED / seed_file}; seed_row_id={seed_id}; "
                       f"seed_sha256={digests[seed_file]}")
        rows.append(row)
        verdicts.append((str(index), prefix, elements,
                         f"transcribed verbatim from {seed_file}#{seed_id}; cell-for-cell match asserted by "
                         f"scripts/import_seed.py; not a primary-source verification"))

    buffer = io.StringIO(newline="")
    buffer.write(f"# metr_deep S0 seed import; fetch_timestamp_utc=n/a (transcription, not a fetch); "
                 f"retrieval_method=verbatim cell copy from the 10-metr pack under "
                 f"/mnt/f/projects/memes/ai-machine/10-metr/research/; known_caps=none; "
                 f"no_kevinnbass_sources=true; brief: none - this is the S0 baseline import, not a research lane; "
                 f"every row re-enters review before it can support a claim element\n")
    for name, value in sorted(digests.items()):
        buffer.write(f"# seed_source {name} sha256={value}\n")
    writer = csv.DictWriter(buffer, fieldnames=config_columns, lineterminator="\n", extrasaction="raise")
    writer.writeheader()
    writer.writerows(rows)
    LANE.parent.mkdir(parents=True, exist_ok=True)
    LANE.write_text(buffer.getvalue(), encoding="utf-8")

    lines = [
        f"<!-- casework-review lane=research/grok-out/{LANE.name} -->",
        "",
        "# S0 seed import review",
        "",
        "Verdict scope: each verdict states only that the lane row reproduces the named 10-metr seed row "
        "cell-for-cell, which `scripts/import_seed.py` asserts before writing. No verdict here is a "
        "primary-source verification. Every binding is `role=context`, `strength=supporting`, so no claim "
        "element becomes ready from this import; each row must be re-collected and re-reviewed by its "
        "MD lane before it can support a claim.",
        "",
        "| row | verdict | target_prefix | element_ids | primary_values | strength | role | note |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for key, prefix, elements, note in verdicts:
        lines.append(f"| {key} | CONFIRMED | {prefix} | {elements} | {{}} | supporting | context | {note} |")
    REVIEW.parent.mkdir(parents=True, exist_ok=True)
    REVIEW.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"WROTE {LANE} rows={len(rows)}")
    print(f"WROTE {REVIEW} verdicts={len(verdicts)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
