#!/usr/bin/env python3
"""S5 Done-when checker: MD46-MD53 (and any MD70-MD89 successor lanes) promoted; casework verify exit 0; CLAIMS.md
covers every claim with a verdict and open-element list; AUDIT-MONEY.md and AUDIT-FRAMING.md exist with every finding
carrying a resolution state (open items explicit); every rendered figure passes scripts/lint_figures.py; casework
frontier has no UNTOUCHED line and no PARTIAL element without a lane, with exceptions recorded in EXHAUSTION-GATE.json;
the allocation request was not drafted or sent in S5."""
import csv, json, pathlib, re, subprocess, sys, glob
ROOT = pathlib.Path(__file__).resolve().parents[1]; ok = True
lanes = {r["lane"]: r for r in csv.DictReader(open(ROOT/"research/LANES.csv"))}
S5 = ["MD%d" % i for i in range(46, 54)] + [l for l in lanes if re.fullmatch(r"MD[78]\d", l)]
nd = [l for l in S5 if lanes.get(l, {}).get("status") not in {"promoted", "replaced", "rerun-promoted"}]
print("1 S5 lanes promoted: %d/%d" % (len(S5) - len(nd), len(S5)) + ("  pending=%s" % nd if nd else "")); ok &= not nd
v = subprocess.run(["python3","-m","casework","verify","--pack","metr_deep"], cwd="/home/kevin/repos/casework", capture_output=True, text=True)
print("2 casework verify exit=%d" % v.returncode); ok &= v.returncode == 0
cl = (ROOT/"research/CLAIMS.md").read_text() if (ROOT/"research/CLAIMS.md").exists() else ""
claims = re.findall(r"^## (C\d+) ", cl, re.M); verdicts = len(re.findall(r"\*\*Verdict:\*\*", cl)); opens = len(re.findall(r"\*\*Open elements:\*\*", cl))
print("3 CLAIMS.md claims=%d verdicts=%d open-lists=%d" % (len(claims), verdicts, opens)); ok &= len(claims) == 10 and verdicts == 10 and opens == 10
ab = []
for name in ("AUDIT-MONEY.md", "AUDIT-FRAMING.md"):
    fs = sorted(glob.glob(str(ROOT/"research/agents-*"/name)))
    if not fs: ab.append(name + " missing"); continue
    t = open(fs[-1]).read(); rows = [l for l in t.splitlines() if l.startswith("| ") and not l.startswith("| row")]
    unres = [l for l in rows if l.rstrip().endswith("|  |") or l.rstrip().endswith("| open |") or "open: no resolution recorded yet" in l]
    print("   %s rows=%d unresolved-blank=%d open=%d" % (name, len(rows), len(unres), sum(1 for l in rows if "| open" in l or "| USER_AUTHORITY_WAIT" in l)))
    if unres: ab.append(name + " has blank resolutions")
print("4 audits: %s" % (ab or "both present, every finding carries a resolution state")); ok &= not ab
lint = subprocess.run(["python3", str(ROOT/"scripts/lint_figures.py")], capture_output=True, text=True)
print("5 figure lint exit=%d: %s" % (lint.returncode, " | ".join(l for l in lint.stdout.splitlines() if l.startswith("FAIL") or l.startswith("no figures")) or "all PASS")); ok &= lint.returncode == 0
fr = subprocess.run(["python3","-m","casework","frontier","--pack","metr_deep"], cwd="/home/kevin/repos/casework", capture_output=True, text=True).stdout.splitlines()
unt = [l for l in fr if l.endswith(" UNTOUCHED")]; part = [l for l in fr if l.endswith(" PARTIAL")]; nolane = [l for l in fr if l.startswith("OPEN ") and "lane=none" in l]
gate = ROOT/"research/EXHAUSTION-GATE.json"; g = json.load(open(gate)) if gate.exists() else {}
exc = {e.get("line") for e in g.get("exceptions", [])} if g else set()
unt_x = [l for l in unt if l not in exc]
print("6 frontier UNTOUCHED=%d (unexcepted %d) PARTIAL=%d OPEN-without-lane=%d gate=%s" % (len(unt), len(unt_x), len(part), len(nolane), "present" if g else "absent")); ok &= not unt_x and not nolane and bool(g)
sent = list((ROOT/"research/outreach/receipts").glob("*")) if (ROOT/"research/outreach/receipts").exists() else []
md99 = (ROOT/"research/outreach/MD99-71m-allocation.md").exists()
print("7 outreach: receipts=%d MD99 draft exists=%s (must be False in S5)" % (len(sent), md99)); ok &= not sent and not md99
print("S5 DONE-WHEN:", "GREEN" if ok else "NOT YET"); sys.exit(0 if ok else 1)
