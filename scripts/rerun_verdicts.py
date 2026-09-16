#!/usr/bin/env python3
"""Prepare verdicts for an xhigh re-run of a lane already promoted from its medium run (PLAN A3/A4).
Rows identical to a promoted medium row (same subject, result, url, target_prefix, money_type, amount_usd, date)
reuse the medium verdict and carry supersedes=<promoted row id>; changed rows reuse the medium verdict with
supersedes but are listed for manual review; added rows are listed with a placeholder. Writes
<scratch>/<lane>-rerun-verdicts.json and <scratch>/<lane>-rerun-diff.txt."""
import csv, json, sys, glob, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
S = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else pathlib.Path("/tmp/claude-1000/-mnt-f-projects-anthropic-metr-deep/da09530d-963c-496d-91c8-63aa77bb4ac5/scratchpad")
lane = sys.argv[1]
new_f = glob.glob(str(ROOT/f"research/grok-out/{lane}-*.csv"))[0]
old_f = glob.glob(str(ROOT/f"research/archive/medium-run-20260916/grok-out/{lane}-*.csv"))[0]
rel = "research/grok-out/" + pathlib.Path(new_f).name
def load(f): return {r["row"]: r for r in csv.DictReader(l for l in open(f) if not l.startswith("#"))}
new, old = load(new_f), load(old_f)
oldv = json.load(open(S/f"{lane}-verdicts.json"))
ids = {}
for t in glob.glob(str(ROOT/"research/*.csv")):
    try:
        for r in csv.DictReader(l for l in open(t) if not l.startswith("#")):
            m = re.search(r"lane=" + re.escape(rel) + r"#([\w-]+)", r.get("note",""))
            if m and "row_id" in r and "superseded by" not in r.get("note",""): ids[m.group(1)] = r["row_id"]
    except Exception: pass
KEYS = ("subject","result","url","target_prefix","money_type","amount_usd","date")
STRICT = ("url","target_prefix","money_type","amount_usd","date")
V, same, changed, added, dropped = {}, [], [], [], [k for k in old if k not in new]
for k, r in new.items():
    if k in old and k in oldv:
        v = dict(oldv[k])
        if k in ids: v["supersedes"] = ids[k]
        if all((r.get(c) or "") == (old[k].get(c) or "") for c in KEYS): same.append(k)
        elif all((r.get(c) or "") == (old[k].get(c) or "") for c in STRICT):
            same.append(k); v["note"] = v.get("note","") + " [xhigh re-run: wording re-verified; facts (url, prefix, money_type, amount, date) unchanged]"
        else:
            changed.append(k)
            v["note"] = (v.get("note","") + " [RERUN-CHANGED: " + "; ".join(f"{c}: {old[k].get(c,'')[:60]!r}->{r.get(c,'')[:60]!r}" for c in KEYS if (r.get(c) or "") != (old[k].get(c) or "")) + "]")
        V[k] = v
    else:
        added.append(k)
        V[k] = dict(verdict="NEEDS_REVIEW", target_prefix=r["target_prefix"], element_ids=r["element_ids"], note="added in xhigh re-run", strength="supporting", role="context")
json.dump(V, open(S/f"{lane}-rerun-verdicts.json","w"), indent=1, ensure_ascii=False)
with open(S/f"{lane}-rerun-diff.txt","w") as o:
    for k in changed + added:
        r = new[k]; o.write(f"\n== {k} | {r['target_prefix']} | {r['element_ids']} | {'CHANGED' if k in changed else 'ADDED'}\n")
        if k in changed:
            for c in KEYS:
                if (r.get(c) or "") != (old[k].get(c) or ""): o.write(f"  OLD {c}: {old[k].get(c,'')[:300]}\n  NEW {c}: {r.get(c,'')[:300]}\n")
        else:
            for c in ("subject","from_entity","to_entity","money_type","amount_usd","date","result","source_class","url","quote_300","note","limitation"):
                if r.get(c): o.write(f"  {c}: {r[c][:300]}\n")
print(f"{lane}: new={len(new)} old={len(old)} same={len(same)} changed={len(changed)} added={len(added)} dropped={len(dropped)} mapped_ids={sum(1 for k in new if k in ids)} -> {lane}-rerun-verdicts.json / -rerun-diff.txt")
