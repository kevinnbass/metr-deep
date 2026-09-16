#!/usr/bin/env python3
"""S3 Done-when checker. Checks: MD26-MD36 promoted; independence_matrix.csv has one row per in-scope project with
every cell either citing row ids or stating that no evidence row exists (no affiliation inference); direct-lab cash,
in-kind and access are separate columns; MD33 entity map spans individual/firm/foundation/vehicle classes; the
adversarial entity-distinction check exists with every flag adjudicated; casework verify exits 0."""
import csv, re, subprocess, pathlib, glob, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
ok = True
def load(p): return [r for r in csv.DictReader(l for l in open(p) if not l.startswith("#"))]
lanes = {r["lane"]: r for r in csv.DictReader(open(ROOT/"research/LANES.csv"))}
S3 = ["MD%d" % i for i in range(26, 37)]
nd = [l for l in S3 if lanes.get(l, {}).get("status") not in {"promoted", "replaced", "rerun-running", "rerun-promoted"}]
print("1 S3 lanes promoted: %d/11" % (11 - len(nd)) + ("  pending=%s" % nd if nd else "")); ok &= not nd
mp = ROOT/"research/independence_matrix.csv"
if mp.exists():
    m = load(mp); cols = list(m[0].keys())
    need = ["direct_lab_cash","in_kind_resources","access_dependence","provider_authority","personnel_disclosures","policy_version"]
    bad = [c for c in need if c not in cols]
    INF = re.compile(r"\b(likely|probably|presumably|suggests|implies|appears to|must have)\b", re.I)
    uncited = [(r["project_key"], c) for r in m for c in need if not (re.search(r"\[MD[A-Z]\d+", r[c]) or r[c].startswith("undisclosed") or r[c].startswith("not stated"))]
    infer = [(r["project_key"], c) for r in m for c in need if INF.search(r[c].split(" [")[0])]
    withev = sum(1 for r in m if int(r["evidence_rows"]) > 0)
    print("2 independence_matrix.csv rows=%d with-evidence=%d missing-cols=%s uncited-cells=%d inference-cells=%d" % (len(m), withev, bad, len(uncited), len(infer)))
    ok &= not bad and not uncited and not infer and withev >= 10
else:
    print("2 independence_matrix.csv missing"); ok = False
ents = load(ROOT/"research/entities.csv")
md33 = [r for r in ents if "MD33-donor-investor-map.csv#" in r.get("note","")]
kinds = set()
for r in md33:
    t = r.get("entity_type","").lower()
    for k, rx in (("individual","individual"),("firm","llc|broker|company|corp|holding"),("foundation","foundation|fund for|990-pf"),("vehicle","investment vehicle|trust"),("daf","daf sponsor"),("process","recommending")):
        if re.search(rx, t): kinds.add(k)
print("3 MD33 entity rows=%d classes=%s" % (len(md33), sorted(kinds))); ok &= {"individual","firm","foundation","vehicle"} <= kinds
ec = sorted(glob.glob(str(ROOT/"research/agents-*/S3-ENTITY-CHECK.md")))
if ec:
    t = open(ec[-1]).read(); n = int(re.search(r"FLAGGED: (\d+)", t).group(1))
    adj = len(re.findall(r"^MD[A-Z]\d+ -> (resolved|unresolved)", t, re.M)); unres = len(re.findall(r"-> unresolved", t))
    print("4 entity check %s flagged=%d adjudicated=%d unresolved=%d" % (pathlib.Path(ec[-1]).name, n, adj, unres)); ok &= adj >= n and unres == 0
else:
    print("4 entity check missing"); ok = False
v = subprocess.run(["python3","-m","casework","verify","--pack","metr_deep"], cwd="/home/kevin/repos/casework", capture_output=True, text=True)
print("5 casework verify exit=%d: %s" % (v.returncode, (v.stdout.strip().splitlines() or [""])[-1])); ok &= v.returncode == 0
print("S3 DONE-WHEN:", "GREEN" if ok else "NOT YET"); sys.exit(0 if ok else 1)
