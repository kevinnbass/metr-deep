#!/usr/bin/env python3
"""Figure lint for PLAN.md S5 Done-when: every rendered figure under figures/ must cite promoted row ids, show an
unknown/undisclosed block, keep money types separate (no summed cross-type total), avoid pipe geometry toward METR for
undocumented passage (checked as the absence of the seed-figure defect phrases MD51 recorded), and contain none of
casework.json banned_motive_words. Prints one line per figure and exits 1 on any failure."""
import glob, json, re, sys, pathlib, csv
ROOT = pathlib.Path(__file__).resolve().parents[1]
cfg = json.load(open(ROOT / "casework.json")); banned = cfg.get("banned_motive_words", [])
ids = set()
for t in glob.glob(str(ROOT / "research/*.csv")):
    for r in csv.DictReader(l for l in open(t) if not l.startswith("#")):
        if "row_id" in r: ids.add(r["row_id"])
DEFECT = ["Dustin Moskovitz / Coefficient", "Jaan Tallinn / Survival", "Schmidt Sciences / Eric", "METR's parent", "reach METR through", "Who gets ordained", "came after the money", "Stop pretending METR is independent", "The investigator's subcontractor", "The Vanguard channel"]
figs = sorted(glob.glob(str(ROOT / "figures/*.html"))); ok = True
for f in figs:
    t = open(f, encoding="utf-8", errors="replace").read(); text = re.sub(r"<[^>]+>", " ", t)
    cited = sorted(set(re.findall(r"\bMD[EFIPQRST]\d{4}\b", t))); unknown_ids = [i for i in cited if i not in ids]
    probs = []
    if not cited: probs.append("no promoted row ids cited")
    if unknown_ids: probs.append("unknown ids %s" % unknown_ids[:5])
    if not re.search(r"unknown|undisclosed|not stated|not disclosed", text, re.I): probs.append("no unknown/undisclosed block")
    hits = [w for w in banned if re.search(r"\b" + re.escape(w) + r"\b", text, re.I)]
    if hits: probs.append("banned motive words %s" % hits)
    d = [p for p in DEFECT if p in text]
    if d: probs.append("seed-figure defect phrase %s" % d)
    if re.search(r"\btotal\b[^.]{0,80}\b(commitment|filed_grant|recommendation|transfer|contract|in_kind)\b[^.]{0,40}\+", text, re.I): probs.append("possible cross-type sum")
    print(("FAIL " if probs else "PASS ") + pathlib.Path(f).name + (" :: " + "; ".join(probs) if probs else f" :: cites {len(cited)} rows"))
    ok &= not probs
if not figs: print("no figures under figures/"); ok = False
sys.exit(0 if ok else 1)
