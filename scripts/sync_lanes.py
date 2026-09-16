#!/usr/bin/env python3
"""Sync research/LANES.csv from the shared runner ledger (tools/lanes.jsonl): newest launch per lane wins.
Promoted lanes relaunched at xhigh become rerun-running; briefed lanes become running. Idempotent."""
import csv, json, datetime, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
rows = [json.loads(l) for l in open("/mnt/f/projects/anthropic/tools/lanes.jsonl")]
launch = {}
for r in rows:
    if r.get("pack") == "metr_deep" and r.get("event") == "launch":
        launch[r["lane"]] = r
p = ROOT / "research/LANES.csv"
data = list(csv.DictReader(open(p))); hdr = list(data[0].keys()); n = 0
for d in data:
    r = launch.get(d["lane"])
    if not r or d["pid"] == str(r["pid"]):
        continue
    was = d["status"]
    d["launched_utc"] = r["utc"]; d["pid"] = str(r["pid"]); d["log"] = r["log"]
    if was == "promoted":
        d["status"] = "rerun-running"
        d["note"] += "; xhigh re-run launched %s pid=%d on account=%s under A3/A4 (medium output archived in research/archive/medium-run-20260916/; medium review stays on record)" % (r["utc"], r["pid"], r["account"])
    else:
        d["status"] = "running"
        d["note"] += "; launched %s via tools/lanes.py on account=%s effort=%s max_turns=None under A4 (launch-ahead; promotion waits for slice order)" % (r["utc"], r["account"], r["effort"])
    n += 1
if n:
    w = open(p, "w", newline=""); cw = csv.DictWriter(w, fieldnames=hdr); cw.writeheader(); cw.writerows(data); w.close()
print("LANES.csv rows updated:", n)
