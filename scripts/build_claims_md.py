#!/usr/bin/env python3
"""Render research/CLAIMS.md: one section per PLAN §4 claim with the engine's readiness verdict, the element
evidence/negative/rebuttal counts, the open elements, and (for C10) the MD49 adjudication of each posted claim and
each METR-attributed response sentence, cited by promoted row id. Derived only from casework readiness and promoted
rows; asserts no motive. Usage: python3 scripts/build_claims_md.py"""
import csv, glob, json, re, subprocess, pathlib, datetime as dt
ROOT = pathlib.Path(__file__).resolve().parents[1]
out = subprocess.run(["python3", "-m", "casework", "readiness", "--pack", "metr_deep"], cwd="/home/kevin/repos/casework", capture_output=True, text=True).stdout.splitlines()
claims, cur = [], None
for l in out:
    m = re.match(r"CLAIM (C\d+) supported=(\w+) supported_primary=(\w+) contested=(\w+) floor=(\w+) title=(.*)", l)
    if m: cur = dict(id=m.group(1), supported=m.group(2), primary=m.group(3), contested=m.group(4), floor=m.group(5), title=m.group(6), elements=[]); claims.append(cur); continue
    m = re.match(r"ELEMENT (C\d+\.E\d+) evidence=(\d+)/(\d+) primary=(\d+) negative=(\d+) rebuttal=(\d+) missing=(\S+) text=(.*)", l)
    if m and cur: cur["elements"].append(dict(id=m.group(1), ev=int(m.group(2)), thr=int(m.group(3)), pr=int(m.group(4)), neg=int(m.group(5)), reb=int(m.group(6)), missing=m.group(7), text=m.group(8)))
VERDICT = {"supported_primary": "supported on primary sources", "supported": "supported (no primary-strength evidence on at least one element)", "open": "open (an element has no evidence binding)", "contested": "contested (a rebuttal is unresolved)"}
# MD49 adjudications
md49 = glob.glob(str(ROOT / "research/grok-out/MD49-*.csv"))
rows49 = list(csv.DictReader(l for l in open(md49[0]) if not l.startswith("#"))) if md49 else []
rel49 = "research/grok-out/" + pathlib.Path(md49[0]).name if md49 else ""
ids = {}
for t in glob.glob(str(ROOT / "research/*.csv")):
    for r in csv.DictReader(l for l in open(t) if not l.startswith("#")):
        m = re.search(r"lane=" + re.escape(rel49) + r"#([\w-]+)", r.get("note", "")) if rel49 else None
        if m and "row_id" in r: ids[m.group(1)] = r["row_id"]
def cell(s): return (s or "").replace("|", "\\|").replace("\n", " ")
L = ["# Claim-by-claim verdicts (metr_deep)", "", f"Rendered {dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} from `casework readiness --pack metr_deep` and the promoted tables. "
     "A verdict is the engine's readiness floor over the claim's elements; it never states a motive and never uses the barred conclusion vocabulary of casework.json. "
     "Money types are never summed across type. Open elements name the exact missing document or the lane that owns them.", ""]
for c in claims:
    L += [f"## {c['id']} — {c['title']}", "", f"**Verdict:** {VERDICT.get(c['floor'], c['floor'])} (supported={c['supported']}, supported_primary={c['primary']}, contested={c['contested']}).", "",
          "| element | evidence | primary | negatives | rebuttals | state | text |", "|---|---|---|---|---|---|---|"]
    for e in c["elements"]:
        L.append(f"| {e['id']} | {e['ev']}/{e['thr']} | {e['pr']} | {e['neg']} | {e['reb']} | {'ready' if e['missing']=='none' else 'OPEN: ' + e['missing']} | {cell(e['text'])} |")
    opens = [e for e in c["elements"] if e["missing"] != "none"]
    L += ["", "**Open elements:** " + ("; ".join(f"{e['id']} ({e['missing']})" for e in opens) if opens else "none"), ""]
    if c["id"] == "C10" and rows49:
        L += ["### Posted claims adjudicated (MD49 Task C, C10.E3)", "", "| row | promoted id | posted claim | verdict | missing document |", "|---|---|---|---|---|"]
        for r in rows49:
            if r["row"].startswith("C"): L.append(f"| {r['row']} | {ids.get(r['row'],'')} | {cell(r['subject'])} | {cell(r['result'])} | {cell(r.get('next_document',''))} |")
        L += ["", "### METR-attributed response sentences adjudicated (MD49 Task B, C10.E2)", "", "| row | promoted id | sentence (source) | verdict | missing document |", "|---|---|---|---|---|"]
        for r in rows49:
            if r["row"].startswith("B") and r["target_prefix"] == "MDP": L.append(f"| {r['row']} | {ids.get(r['row'],'')} | {cell(r['subject'])} | {cell(r['result'])} | {cell(r.get('next_document',''))} |")
        L.append("")
L += ["## Adversarial audits", "", "- Money/provenance: `research/agents-2026-09-16/AUDIT-MONEY.md` (MD50)", "- Framing/entity/causality: `research/agents-2026-09-16/AUDIT-FRAMING.md` (MD51)", ""]
txt = "\n".join(L) + "\n"
banned = json.load(open(ROOT / "casework.json")).get("banned_motive_words", [])
hits = [w for w in banned if re.search(r"\b" + re.escape(w) + r"\b", txt.split("## C10")[0], re.I)]
assert not hits, f"motive vocabulary in claim verdict text: {hits}"
(ROOT / "research/CLAIMS.md").write_text(txt); print("research/CLAIMS.md claims=%d open_elements=%d" % (len(claims), sum(1 for c in claims for e in c["elements"] if e["missing"] != "none")))
