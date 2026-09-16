#!/usr/bin/env python3
"""S4 Done-when checker. Checks: MD37-MD45 promoted; research/records/REQUESTS.jsonl well-formed with every
request in a dated terminal or USER_AUTHORITY_WAIT state, unsent drafts unapproved, draft hashes current, cleaned
drafts free of the ~$71M figure; research/calendar.csv well-formed with every future document dated, checked and
N/A-with-reason; every filing/registry source class named on the S4 claims (C05-C07) COVERED in casework frontier
(PARTIAL only where the open element already has a lane); nothing transmitted; casework verify exits 0."""
import csv, hashlib, json, pathlib, re, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
ok = True
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
lanes = {r["lane"]: r for r in csv.DictReader(open(ROOT/"research/LANES.csv"))}
S4 = ["MD%d" % i for i in range(37, 46)]
nd = [l for l in S4 if lanes.get(l, {}).get("status") not in {"promoted", "replaced", "rerun-running", "rerun-promoted"}]
print("1 S4 lanes promoted: %d/9" % (9 - len(nd)) + ("  pending=%s" % nd if nd else "")); ok &= not nd
# requests
rp = ROOT/"research/records/REQUESTS.jsonl"; reqs = [json.loads(l) for l in open(rp) if l.strip()] if rp.exists() else []
TERMINAL = {"USER_AUTHORITY_WAIT", "sent", "produced", "denied", "appealed", "pending", "closed"}
need = {"request_id","lane","custodian","route","scope","lane_draft","cleaned_draft","state","approved_for_send","drafted_utc","registered_utc","sent_utc","transmission_receipt","embargo_check"}
bad = []
for r in reqs:
    miss = need - set(r)
    if miss: bad.append((r.get("request_id"), "missing %s" % sorted(miss))); continue
    if r["state"] not in TERMINAL: bad.append((r["request_id"], "state %s" % r["state"]))
    if r["state"] == "USER_AUTHORITY_WAIT" and (r["approved_for_send"] or r["sent_utc"]): bad.append((r["request_id"], "unsent request marked approved/sent"))
    if r["sent_utc"] and not r["transmission_receipt"]: bad.append((r["request_id"], "sent without receipt"))
    for k in ("lane_draft", "cleaned_draft"):
        p = ROOT/r[k]["path"]
        if not p.exists() or sha(p) != r[k]["sha256"]: bad.append((r["request_id"], "%s hash/path stale" % k))
    ct = (ROOT/r["cleaned_draft"]["path"]).read_text() if (ROOT/r["cleaned_draft"]["path"]).exists() else ""
    if re.search(r"\$71|71 million|71M|seventy-one", ct): bad.append((r["request_id"], "cleaned draft names the figure"))
    if "approved_for_send: false" not in ct: bad.append((r["request_id"], "cleaned draft not marked unapproved"))
    if r.get("custodian_is_donor_side") and "METR" in "\n".join(l for l in ct.splitlines() if not l.startswith("#")): bad.append((r["request_id"], "donor-side draft names METR"))
    ec = r["embargo_check"]
    if ec.get("asks_allocation") or ec.get("asks_donor_composition") or ec.get("asks_custodian_to_create_analysis"): bad.append((r["request_id"], "embargo check failed"))
print("2 REQUESTS.jsonl entries=%d states=%s problems=%s" % (len(reqs), sorted({r.get("state") for r in reqs}), bad)); ok &= bool(reqs) and not bad
# calendar
cal = [r for r in csv.DictReader(l for l in open(ROOT/"research/calendar.csv") if not l.startswith("#"))]
COLS = ["closer_id","earliest_expected","document","issuer","release_point","claims","last_checked_utc","state","note"]
CST = {"future", "USER_AUTHORITY_WAIT", "not started", "recovered", "checked-not-posted"}
cbad = []
if list(cal[0].keys()) != COLS: cbad.append("columns %s" % list(cal[0].keys()))
for r in cal:
    if not r["earliest_expected"]: cbad.append((r["closer_id"], "no earliest_expected"))
    if not re.match(r"\d{4}-\d{2}-\d{2}T", r["last_checked_utc"]): cbad.append((r["closer_id"], "not checked"))
    if r["state"] not in CST: cbad.append((r["closer_id"], "state %s" % r["state"]))
    if r["state"] == "future" and not re.search(r"next check (on|\d{4}-\d{2}-\d{2})", r["note"]): cbad.append((r["closer_id"], "no next-check date"))
    if re.search(r"searched and absent|none found", r["note"], re.I): cbad.append((r["closer_id"], "future document worded as a negative"))
print("3 calendar.csv rows=%d problems=%s" % (len(cal), cbad)); ok &= bool(cal) and not cbad
# frontier
fr = subprocess.run(["python3","-m","casework","frontier","--pack","metr_deep"], cwd="/home/kevin/repos/casework", capture_output=True, text=True).stdout.splitlines()
case = json.load(open(ROOT/"case.json"))
FILING = {"recipient filings","funder filings","DAF sponsor filings","IRS TEOS and e-file index","state registries","SEC","court dockets","public grant databases","procurement records","statutory records requests"}
opens = {}
for l in fr:
    m = re.match(r"OPEN (C\d+)\.E\d+ lane=(\S+)", l)
    if m: opens.setdefault(m.group(1), []).append(m.group(2))
fbad = []; seen = 0
for cl in case["claims"]:
    if cl["claim_id"] not in ("C05", "C06", "C07"): continue
    classes = {s for e in cl["elements"] for s in e.get("source_classes", [])} & FILING
    for s in sorted(classes):
        pre = "SOURCE %s %s " % (cl["claim_id"], s); st = next((l[len(pre):] for l in fr if l.startswith(pre)), "?"); seen += 1
        if st == "COVERED": continue
        if st == "PARTIAL" and opens.get(cl["claim_id"]) and all(x != "none" for x in opens[cl["claim_id"]]): continue
        fbad.append((cl["claim_id"], s, st))
print("4 frontier S4 filing/registry classes checked=%d not-covered=%s" % (seen, fbad)); ok &= not fbad
warn = [(c, ls) for c, ls in opens.items() if c in ("C05","C06","C07") and "none" in ls]
if warn: print("   note: open S4-claim elements without a lane (S5 MD52 scope): %s" % warn)
# nothing sent
rcpt = [p for p in (ROOT/"research/outreach/receipts").glob("*") if p.is_file()] if (ROOT/"research/outreach/receipts").exists() else []
drafts = list((ROOT/"research/primary").glob("MD*/draft-*.md")) + list((ROOT/"research/outreach/drafts").glob("*.md"))
sent = [str(p) for p in drafts if "approved_for_send: false" not in p.read_text() or re.search(r"sent_utc: \d", p.read_text())]
print("5 transmissions: receipts=%d drafts=%d drafts-not-unapproved=%s" % (len(rcpt), len(drafts), sent)); ok &= not rcpt and not sent and len(drafts) >= 5
v = subprocess.run(["python3","-m","casework","verify","--pack","metr_deep"], cwd="/home/kevin/repos/casework", capture_output=True, text=True)
print("6 casework verify exit=%d: %s" % (v.returncode, (v.stdout.strip().splitlines() or [""])[-1])); ok &= v.returncode == 0
print("S4 DONE-WHEN:", "GREEN" if ok else "NOT YET"); sys.exit(0 if ok else 1)
