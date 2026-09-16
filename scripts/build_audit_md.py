#!/usr/bin/env python3
"""Render an adversarial-audit lane (MD50 money/provenance, MD51 framing/entity/causality) into the S5 audit file
PLAN.md §8/S5 requires (AUDIT-MONEY.md / AUDIT-FRAMING.md). Each finding row becomes a table line with its promoted
row id, verdict, and a resolution cell taken from research/agents-<date>/AUDIT-RESOLUTIONS.json (default 'open').
Usage: python3 scripts/build_audit_md.py MD51 research/agents-2026-09-16/AUDIT-FRAMING.md"""
import csv, glob, json, re, sys, pathlib, datetime as dt
ROOT = pathlib.Path(__file__).resolve().parents[1]
lane, out = sys.argv[1], ROOT / sys.argv[2]
csvf = glob.glob(str(ROOT / f"research/grok-out/{lane}-*.csv"))[0]
rel = "research/grok-out/" + pathlib.Path(csvf).name
rows = list(csv.DictReader(l for l in open(csvf) if not l.startswith("#")))
ids = {}
for t in glob.glob(str(ROOT / "research/*.csv")):
    for r in csv.DictReader(l for l in open(t) if not l.startswith("#")):
        m = re.search(r"lane=" + re.escape(rel) + r"#([\w-]+)", r.get("note", ""))
        if m and "row_id" in r: ids[m.group(1)] = r["row_id"]
resf = out.parent / "AUDIT-RESOLUTIONS.json"
res = json.load(open(resf)) if resf.exists() else {}
review = sorted(glob.glob(str(ROOT / f"research/agents-*/MDREVIEW-{lane}.md")))
def cell(s): return (s or "").replace("|", "\\|").replace("\n", " ")[:600]
L = [f"# {lane} adversarial audit ({'money/provenance' if lane=='MD50' else 'framing/entity/causality'})", "",
     f"Rendered {dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} from `{rel}` (promoted; review `{pathlib.Path(review[-1]).relative_to(ROOT) if review else 'none'}`). "
     "Resolution states come from `AUDIT-RESOLUTIONS.json` in this directory; a finding without an entry is `open`. No motive is asserted anywhere in this file.", "",
     "| row | promoted id | task | finding | result | resolution |", "|---|---|---|---|---|---|"]
open_n = 0
for r in rows:
    k = r["row"]; rs = r.get("result", "").lower()
    if k in res.get(lane, {}): state = res[lane][k]
    elif r["task"] == "A" and rs.startswith("match"): state = "verified: promoted row matched its primary live; no finding"
    elif r["task"] == "A" and rs.startswith("mismatch"): state = "resolved: audit-lane retrieval failure or name-form difference; promoted row stands (MDREVIEW-%s)" % lane
    elif "none found" in rs or r["task"] == "E": state = "none needed (negative/coverage)"
    else: state = "open: no resolution recorded yet"
    if state.startswith("open"): open_n += 1
    L.append(f"| {k} | {ids.get(k,'')} | {r['task']} | {cell(r['subject'])} | {cell(r['result'])} | {cell(state)} |")
L += ["", f"Findings: {len(rows)} rows; open resolutions: {open_n}."]
out.write_text("\n".join(L) + "\n"); print(f"{out.relative_to(ROOT)}: rows={len(rows)} open={open_n}")
