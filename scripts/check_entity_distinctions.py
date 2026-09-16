#!/usr/bin/env python3
"""Adversarial entity-distinction check for S3: scans promoted MDE/MDR/MDQ/MDF rows for pairs of legal entities
that must never be merged and flags any row that names both members of a pair without an explicit separation word.
Writes research/agents-<today>/S3-ENTITY-CHECK.md listing every flagged row for the reviewer's adjudication."""
import csv, re, pathlib, datetime
ROOT = pathlib.Path(__file__).resolve().parents[1]
def load(name): return [r for r in csv.DictReader(l for l in open(ROOT/"research"/name) if not l.startswith("#"))]
PAIRS = [
 ("Alignment Research Center|ARC Evals", "METR|Model Evaluation and Threat Research"),
 ("Google DeepMind", r"\bGoogle\b(?! DeepMind)"),
 (r"individuals from Jane Street", r"Jane Street (Group|Capital|Global Trading)"),
 (r"Eric Schmidt", r"Schmidt Sciences|Schmidt Fund"),
 (r"OpenAI Foundation", r"OpenAI(?! Foundation)"),
 (r"Redwood", r"METR"),
 (r"Moskovitz Investments LLC", r"Moskovitz Investment Holdings"),
 (r"Good Ventures", r"Open Philanthropy|Coefficient"),
 (r"RAND Europe", r"\bRAND\b(?! Europe)"),
 (r"DAF sponsor|National Philanthropic Trust|Silicon Valley Community Foundation|Vanguard Charitable", r"adviser|account principal|donor-advised account"),
]
SEP = re.compile(r"distinguish|not merged|kept (separate|apart|distinct)|separate legal|different legal|not the same|is not METR|not METR|unmerged|a different (entity|legal)|kept distinct|separately", re.I)
flag = []
for name in ("entities.csv","relationships.csv","project_coi.csv","funding_events.csv","in_kind_access.csv"):
    for r in load(name):
        blob = " ".join(str(r.get(c,"")) for c in ("subject","from_entity","to_entity","intermediary","provider","result","edge_type","relationship_type"))
        for a, b in PAIRS:
            if re.search(a, blob) and re.search(b, blob):
                if not SEP.search(blob + " " + r.get("note","") + " " + r.get("limitation","")):
                    flag.append((r["row_id"], name, a, b, blob[:220]))
today = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d")
d = ROOT/"research"/f"agents-{today}"; d.mkdir(exist_ok=True)
p = d/"S3-ENTITY-CHECK.md"
with open(p, "w") as f:
    f.write(f"# S3 adversarial entity-distinction check ({today})\n\nPairs of legal entities that must never be merged were searched across the promoted MDE/MDR/MDQ/MDF/MDI rows; a row is flagged when it names both members of a pair without an explicit separation statement in its own text or note.\n\n")
    f.write(f"FLAGGED: {len(flag)}\n\n| row_id | table | pair | text |\n|---|---|---|---|\n")
    for rid, name, a, b, blob in flag: f.write(f"| {rid} | {name} | {a} vs {b} | {blob.replace('|','/')} |\n")
    f.write("\nADJUDICATION (reviewer; persisted in S3-ENTITY-ADJUDICATIONS.json; a flagged row without an entry is unresolved until the reviewer adds one):\n")
    import json
    ap = d/"S3-ENTITY-ADJUDICATIONS.json"; adj = json.load(open(ap)) if ap.exists() else {}
    for rid, *_ in flag: f.write(f"{rid} -> {adj[rid]}\n" if rid in adj else f"{rid} -> unresolved: no adjudication yet\n")
    f.write("\nUNRESOLVED: %d\n" % sum(1 for rid, *_ in flag if rid not in adj))
print(f"flagged={len(flag)} -> {p}")
for x in flag: print(x[0], x[1], x[2], "vs", x[3], "|", x[4][:120])
