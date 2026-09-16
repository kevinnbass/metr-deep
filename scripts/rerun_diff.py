#!/usr/bin/env python3
"""Content-keyed comparison of an xhigh re-run against the promoted medium run (PLAN A4/A4.1). Row numbers shift
between runs, so rows are matched by content, never by number. Classes: SAME (url, prefix, money_type, amount,
date and subject match a medium row, or the row is already promoted under its own marker), CHANGED (same url and
near-identical subject but a money/date field differs: candidate correction), ADDED (no medium counterpart:
must be reviewed and promoted from research/rerun/<lane>-xhigh-added.csv under X-prefixed row ids so the marker
never collides), DROPPED (medium row with no xhigh counterpart: the promoted row stands, noted in the review).
Usage: python3 scripts/rerun_diff.py MD16 [scratch_dir]"""
import csv, json, sys, glob, re, pathlib, difflib
ROOT = pathlib.Path(__file__).resolve().parents[1]
S = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else pathlib.Path("/tmp/claude-1000/-mnt-f-projects-anthropic-metr-deep/da09530d-963c-496d-91c8-63aa77bb4ac5/scratchpad")
lane = sys.argv[1]
new_f = glob.glob(str(ROOT/f"research/grok-out/{lane}-*.csv"))[0]
old_f = glob.glob(str(ROOT/f"research/archive/medium-run-20260916/grok-out/{lane}-*.csv"))[0]
rel = "research/grok-out/" + pathlib.Path(new_f).name
def load(f):
    lines = open(f).read().splitlines(True)
    hdr = [l for l in lines if l.startswith("#")]
    rows = list(csv.DictReader(l for l in lines if not l.startswith("#")))
    return hdr, rows
hdr, new = load(new_f); _, old = load(old_f)
promoted_subject = {}
for t in glob.glob(str(ROOT/"research/*.csv")):
    try:
        for r in csv.DictReader(l for l in open(t) if not l.startswith("#")):
            m = re.search(r"lane=" + re.escape(rel) + r"#([\w-]+)", r.get("note",""))
            if m and "row_id" in r: promoted_subject.setdefault(m.group(1), []).append((r["row_id"], r.get("subject") or r.get("name") or r.get("title") or ""))
    except Exception: pass
def norm(s): return re.sub(r"\W+", " ", (s or "").lower()).strip()
def strict(r): return tuple((r.get(c) or "").strip() for c in ("url","target_prefix","money_type","amount_usd","date"))
def sim(a, b): return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()
unmatched_old = {r["row"]: r for r in old}
same, changed, added = [], [], []
for r in new:
    k = r["row"]
    # already promoted under this exact marker with the same subject (xhigh rows promoted earlier)?
    if any(sim(s, r["subject"]) >= 0.9 for _, s in promoted_subject.get(k, [])) and not (k in unmatched_old and sim(unmatched_old[k]["subject"], r["subject"]) < 0.9 and strict(unmatched_old[k]) != strict(r)):
        same.append((k, k, "marker")); unmatched_old.pop(k, None); continue
    best = None
    for ok, o in unmatched_old.items():
        if strict(o) == strict(r):
            sc = sim(o["subject"], r["subject"])
            if sc >= 0.55 and (best is None or sc > best[1]): best = (ok, sc)
    if best:
        same.append((k, best[0], "content")); unmatched_old.pop(best[0]); continue
    cand = None
    for ok, o in unmatched_old.items():
        if (o.get("url") or "") == (r.get("url") or "") and o.get("target_prefix") == r.get("target_prefix"):
            sc = sim(o["subject"], r["subject"])
            if sc >= 0.75 and (cand is None or sc > cand[1]): cand = (ok, sc)
    if cand:
        changed.append((k, cand[0])); unmatched_old.pop(cand[0]); continue
    added.append(k)
dropped = sorted(unmatched_old)
newmap = {r["row"]: r for r in new}; oldmap = {r["row"]: r for r in old}
out_dir = ROOT/"research/rerun"; out_dir.mkdir(exist_ok=True)
added_csv = out_dir/f"{lane}-xhigh-added.csv"
if added or changed:
    with open(added_csv, "w", newline="") as f:
        f.writelines(hdr)
        w = csv.DictWriter(f, fieldnames=list(new[0].keys()), lineterminator="\n"); w.writeheader()
        for k in added:
            r = dict(newmap[k]); r["row"] = "X" + k; r["note"] = (r.get("note","") + f" [xhigh re-run row {k} of {rel}; no medium counterpart]").strip(); w.writerow(r)
        for k, ok in changed:
            pid = ",".join(i for i,_ in promoted_subject.get(ok, []))
            r = dict(newmap[k]); r["row"] = "C" + k; r["note"] = (r.get("note","") + f" [xhigh re-run row {k} of {rel}; candidate correction of medium row {ok} (promoted {pid})]").strip(); w.writerow(r)
    V = {"X"+k: dict(verdict="NEEDS_REVIEW", target_prefix=newmap[k]["target_prefix"], element_ids=newmap[k]["element_ids"], note="added in xhigh re-run", strength="supporting", role="context") for k in added}
    for k, ok in changed:
        V["C"+k] = dict(verdict="NEEDS_REVIEW", target_prefix=newmap[k]["target_prefix"], element_ids=newmap[k]["element_ids"], note="changed in xhigh re-run", strength="supporting", role="context", supersedes=",".join(i for i,_ in promoted_subject.get(ok, [])))
    json.dump(V, open(S/f"{lane}-xhigh-added-verdicts.json","w"), indent=1, ensure_ascii=False)
elif added_csv.exists(): added_csv.unlink()
with open(S/f"{lane}-xhigh-diff.txt","w") as o:
    o.write(f"{lane}: new={len(new)} old={len(old)} same={len(same)} changed={len(changed)} added={len(added)} dropped={len(dropped)}\n")
    for k, ok in changed:
        r, oo = newmap[k], oldmap[ok]; o.write(f"\n== CHANGED new#{k} vs old#{ok} | {r['target_prefix']} | {r['element_ids']} | promoted={[i for i,_ in promoted_subject.get(ok,[])]}\n")
        for c in ("subject","money_type","amount_usd","date","result","quote_300"):
            if (r.get(c) or "") != (oo.get(c) or ""): o.write(f"  OLD {c}: {oo.get(c,'')[:300]}\n  NEW {c}: {r.get(c,'')[:300]}\n")
    for k in added:
        r = newmap[k]; o.write(f"\n== ADDED X{k} | {r['target_prefix']} | {r['element_ids']}\n")
        for c in ("subject","from_entity","to_entity","money_type","amount_usd","date","result","source_class","url","quote_300","note","limitation"):
            if r.get(c): o.write(f"  {c}: {r[c][:300]}\n")
    for ok in dropped:
        oo = oldmap[ok]; o.write(f"\n== DROPPED old#{ok} | {oo['target_prefix']} | promoted={[i for i,_ in promoted_subject.get(ok,[])]} | {oo['subject'][:120]}\n")
print(f"{lane}: new={len(new)} old={len(old)} same={len(same)} changed={len(changed)} added={len(added)} dropped={len(dropped)}")
