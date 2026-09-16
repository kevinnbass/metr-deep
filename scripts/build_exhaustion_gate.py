#!/usr/bin/env python3
"""Build research/EXHAUSTION-GATE.json per PLAN.md §7 from the pack's own files. Every field is computed, never
asserted: slice receipts, the frontier command receipt (hash of full output), source-class states for the C01/C02
elements (COVERED / N/A-with-reason / PARTIAL with the reason no public route remains), named-supporter coverage,
records-route states from REQUESTS.jsonl, calendar closers, reconciliation decisions, audit resolutions, the embargo
check over every draft, and the two independent review receipts. `gate_pass` is true only when no field fails; every
residual condition is listed under `exceptions` with its next-check date or the decision it waits on.
Usage: python3 scripts/build_exhaustion_gate.py"""
import csv, glob, hashlib, json, pathlib, re, subprocess, datetime as dt
ROOT = pathlib.Path(__file__).resolve().parents[1]
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
G = {"built_utc": now, "exceptions": []}
# 1 slices
G["slices_complete"] = {}
for s in ("S0", "S1", "S2", "S3", "S4", "S5"):
    r = ROOT / f"research/receipts/{s}/{s}-verification.json"
    G["slices_complete"][s] = {"receipt": str(r.relative_to(ROOT)), "sha256": sha(r)} if r.exists() else None
# 2 frontier
cmd = ["python3", "-m", "casework", "frontier", "--pack", "metr_deep"]
fr = subprocess.run(cmd, cwd="/home/kevin/repos/casework", capture_output=True, text=True)
lines = fr.stdout.splitlines()
G["frontier_command"] = {"command": "cd /home/kevin/repos/casework && " + " ".join(cmd), "utc": now, "exit": fr.returncode, "output_sha256": hashlib.sha256(fr.stdout.encode()).hexdigest(), "lines": len(lines)}
# 3 source classes for C01/C02 elements
case = json.load(open(ROOT / "case.json")); cfg = json.load(open(ROOT / "casework.json")); na = cfg.get("source_class_na", {})
sc = {}
for cl in case["claims"]:
    if cl["claim_id"] not in ("C01", "C02"): continue
    for l in lines:
        m = re.match(r"SOURCE (C0[12]) (.+?) (COVERED|PARTIAL|UNTOUCHED|N/A.*)$", l)
        if m and m.group(1) == cl["claim_id"]: sc.setdefault(cl["claim_id"], {})[m.group(2)] = m.group(3)
opens = {m.group(1): m.group(2) for m in (re.match(r"OPEN (C\d+\.E\d+) lane=(\S+)", l) for l in lines) if m}
for c, d in sc.items():
    for k, v in d.items():
        if v == "UNTOUCHED": G["exceptions"].append({"field": "source_classes", "line": f"SOURCE {c} {k} UNTOUCHED", "reason": "no N/A reason recorded", "next_check": "before MD99"})
        if v == "PARTIAL": G["exceptions"].append({"field": "source_classes", "line": f"SOURCE {c} {k} PARTIAL", "reason": "open element on this claim: " + ", ".join(e for e in opens if e.startswith(c)) + "; no currently actionable public route (MD52 Task B)", "next_check": "calendar closers CAL02/CAL04 2026-11-16"})
G["source_classes"] = sc
# 4 named supporters
subprocess.run(["python3", str(ROOT / "scripts/build_supporter_coverage.py")], capture_output=True, text=True)
supp = list(csv.DictReader(l for l in open(ROOT / "research/supporter_coverage.csv") if not l.startswith("#")))
G["named_supporters"] = {"file": "research/supporter_coverage.csv", "rows": len(supp), "without_coverage": [r["supporter"] for r in supp if not (r.get("positive_rows") or "").strip() and not (r.get("negative_rows") or "").strip()], "statuses": sorted({r["status"] for r in supp})}
# 5 records routes
reqs = [json.loads(l) for l in open(ROOT / "research/records/REQUESTS.jsonl") if l.strip()]
inclock = [r["request_id"] for r in reqs if r.get("sent_utc") and r.get("state") in ("sent", "pending")]
G["records_routes"] = {"requests": [{"id": r["request_id"], "state": r["state"], "approved_for_send": r["approved_for_send"], "sent_utc": r.get("sent_utc")} for r in reqs], "in_clock": inclock}
if inclock: G["exceptions"].append({"field": "records_routes", "line": ",".join(inclock), "reason": "an ordinary in-clock request prevents the gate", "next_check": "response clock"})
waiting = [r["request_id"] for r in reqs if r["state"] == "USER_AUTHORITY_WAIT"]
if waiting: G["exceptions"].append({"field": "records_routes", "line": ",".join(waiting), "reason": "drafts unsent and unapproved; Kevin has neither approved nor explicitly declined them; no clock is running", "next_check": "Kevin's decision"})
# 6 calendar
cal = list(csv.DictReader(l for l in open(ROOT / "research/calendar.csv") if not l.startswith("#")))
G["calendar"] = [{"closer_id": r["closer_id"], "earliest_expected": r["earliest_expected"], "state": r["state"], "last_checked_utc": r["last_checked_utc"]} for r in cal]
for r in cal:
    if r["state"] == "future": G["exceptions"].append({"field": "calendar", "line": r["closer_id"], "reason": r["document"][:120], "next_check": r["earliest_expected"]})
# 7 reconciliation
rec = list(csv.DictReader(l for l in open(ROOT / "research/commitment_reconciliation.csv") if not l.startswith("#")))
undec = [r["row_id"] for r in rec if not r.get("decision")]
cells = [r for r in csv.DictReader(l for l in open(glob.glob(str(ROOT / "research/grok-out/MD46-*.csv"))[0]) if not l.startswith("#")) if r["task"] == "D"]
G["reconciliation"] = {"file": "research/commitment_reconciliation.csv", "rows": len(rec), "undecided": undec, "residual_cells": [c["subject"] for c in cells]}
# 8 audits
res = json.load(open(ROOT / "research/agents-2026-09-16/AUDIT-RESOLUTIONS.json"))
G["audits"] = {}
for lane in ("MD50", "MD51"):
    items = res.get(lane, {}); op = {k: v for k, v in items.items() if v.startswith("open") or v.startswith("USER_AUTHORITY_WAIT")}
    G["audits"][lane] = {"review": sorted(glob.glob(str(ROOT / f"research/agents-*/MDREVIEW-{lane}.md")))[-1].replace(str(ROOT) + "/", ""), "resolved": len(items) - len(op), "open": op}
    for k, v in op.items(): G["exceptions"].append({"field": "audits", "line": f"{lane} {k}", "reason": v, "next_check": "see reason"})
# 9 embargo
drafts = list((ROOT / "research/primary").glob("MD*/draft-*.md")) + list((ROOT / "research/outreach/drafts").glob("*.md"))
bad = [str(d.relative_to(ROOT)) for d in drafts if re.search(r"(who|which donors?|composition|allocat)[^.\n]{0,80}\$?71", d.read_text(), re.I) and "not a request" not in d.read_text()]
sent = list((ROOT / "research/outreach/receipts").glob("*"))
G["embargo_check"] = {"drafts": len(drafts), "drafts_asking_allocation": bad, "transmissions": len(sent)}
if bad or sent: G["exceptions"].append({"field": "embargo_check", "line": ",".join(bad) or "receipts", "reason": "a draft or transmission touches the allocation", "next_check": "immediate"})
# 10 reviewers
G["reviewers"] = [{"lane": lane, "review": G["audits"][lane]["review"], "sha256": sha(ROOT / G["audits"][lane]["review"])} for lane in ("MD50", "MD51")]
hard = [e for e in G["exceptions"] if e["field"] in ("source_classes", "embargo_check") or (e["field"] == "records_routes" and e["next_check"] == "response clock")]
G["gate_pass"] = not hard and all(G["slices_complete"].values()) and not undec
G["gate_note"] = ("gate passes with the listed exceptions (future documents, the embargoed remainder, unsent drafts awaiting Kevin's decision, and audit items open by date)" if G["gate_pass"] else "gate fails: see exceptions with field source_classes/embargo_check/records_routes or missing slice receipts")
(ROOT / "research/EXHAUSTION-GATE.json").write_text(json.dumps(G, indent=1))
print("EXHAUSTION-GATE.json gate_pass=%s exceptions=%d hard=%d" % (G["gate_pass"], len(G["exceptions"]), len(hard)))
