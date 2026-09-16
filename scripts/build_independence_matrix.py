#!/usr/bin/env python3
"""Build research/independence_matrix.csv: one row per METR lab engagement, every cell drawn only from
promoted rows bound with role=evidence (cash/in-kind/access/authority/personnel/policy) or role=negative (gaps),
each cell citing the row ids it rests on. Nothing is inferred from affiliation; a cell with no qualifying row
says so. Idempotent; re-run after every S3 promotion."""
import csv, json, re, pathlib, collections, datetime
ROOT = pathlib.Path(__file__).resolve().parents[1]
def load(name): return [r for r in csv.DictReader(l for l in open(ROOT/"research"/name) if not l.startswith("#"))]
case = json.load(open(ROOT/"case.json"))
roles = collections.defaultdict(set)
def walk(o):
    if isinstance(o, dict):
        if "row_id" in o and "role" in o: roles[o["row_id"]].add(o["role"])
        for v in o.values(): walk(v)
    elif isinstance(o, list):
        for v in o: walk(v)
walk(case)
PROJECTS = [  # key, label, providers, regex on (project + subject) lowercase
 ("frr-2026","METR Frontier Risk Report (Feb-Mar 2026; published 2026-05-19)","Anthropic; Google; Meta; OpenAI", r"frontier risk report|frr"),
 ("hf-incident-2026","OpenAI / Hugging Face incident investigation (Aug 2026)","OpenAI", r"hugging face|hf incident|hf report|hf blog"),
 ("gpt-5-6-sol","GPT-5.6 Sol pre-deployment evaluation","OpenAI", r"gpt-5\.6|sol evaluation|sol post|gpt-5-6"),
 ("gpt-5-1-codex-max","GPT-5.1-Codex-Max evaluation","OpenAI", r"codex-max|codex max|gpt-5\.1"),
 ("gpt-5","GPT-5 (gpt-5-thinking) evaluation","OpenAI", r"gpt-5(?![\.\-]\d)|gpt-5 report|gpt-5-thinking"),
 ("gpt-oss","gpt-oss-120b methodology review","OpenAI", r"gpt-oss"),
 ("o1-preview","OpenAI o1-preview / o1-mini evaluation","OpenAI", r"\bo1\b|o1-preview|o1-mini"),
 ("o3-o4-mini","OpenAI o3 / o4-mini evaluation","OpenAI", r"\bo3\b|o4-mini"),
 ("gpt-4-5","GPT-4.5 evaluation","OpenAI", r"gpt-4\.5|gpt-4-5"),
 ("gpt-4o","GPT-4o preliminary evaluation","OpenAI", r"gpt-4o"),
 ("gpt-4-arc","GPT-4 pre-deployment evaluation (ARC Evals era; Alignment Research Center, not METR)","OpenAI", r"gpt-4 |gpt-4 system card|gpt-4 pre"),
 ("anthropic-opus46-sabotage-review","External review of Anthropic Sabotage Risk Report (Claude Opus 4.6)","Anthropic", r"sabotage risk report|opus 4\.6|opus46|sabotage-report-review|sabotage report"),
 ("anthropic-rd-section-review","Review of the automated R&D section, Anthropic Risk Report Feb 2026","Anthropic", r"r&d section|automated r&d|rd-section|rd section"),
 ("anthropic-agent-monitoring","Red-teaming Anthropic internal agent monitoring systems","Anthropic", r"agent monitoring|agent-monitoring"),
 ("anthropic-incident-2026-09","Anthropic cybersecurity-evaluation incidents investigation (agreement 2026-09-09)","Anthropic", r"september 2026 anthropic incident|cybersecurity|cyber-incident|cyber incident|incident engagement"),
 ("claude-3-5-sonnet","Claude 3.5 Sonnet evaluation (2024)","Anthropic", r"claude 3\.5|claude-3-5|3\.5 sonnet"),
 ("anthropic-mythos","Claude Mythos Preview / Mythos 5.1 pre-deployment testing","Anthropic", r"mythos"),
 ("claude-2-arc","Claude 2 / earlier snapshot audits (ARC Evals era; Alignment Research Center, not METR)","Anthropic", r"claude 2|claude-2"),
 ("amazon-nova","Amazon Nova Premier / Nova 2 FMSF evaluations","Amazon", r"nova"),
 ("amazon-fmsf","Amazon Frontier Model Safety Framework feedback","Amazon", r"frontier model safety framework|fmsf"),
 ("gdm-fsf","Google DeepMind Frontier Safety Framework input","Google DeepMind", r"frontier safety framework|fsf"),
 ("policy-assistance-2024","Assistance establishing first frontier-safety policies (2024 annual report)","Google DeepMind; Anthropic; Amazon (credited)", r"annual report|safety policies|policy-assistance"),
]
NONPROJECT = re.compile(r"conflict of interest policy|confidentiality policy|aef-1|minimum operating conditions|cross-lab comparison")
def key_for(text):
    t = text.lower()
    if NONPROJECT.search(t) and not re.search(r"frontier risk report|hugging face", t): return None
    for k, _, _, rx in PROJECTS:
        if re.search(rx, t): return k
    return None
INFER = re.compile(r"\b(likely|probably|presumably|suggests|implies|appears to|must have)\b", re.I)
tables = {"MDQ": load("project_coi.csv"), "MDI": load("in_kind_access.csv"), "MDR": load("relationships.csv"), "MDS": load("source_coverage.csv"), "MDP": load("provenance.csv")}
by = collections.defaultdict(lambda: collections.defaultdict(list))
for pre, rows in tables.items():
    for r in rows:
        k = key_for(" ".join([r.get("project",""), r.get("subject","")]))
        if k: by[k][pre].append(r)
def ev(rows): return [r for r in rows if "evidence" in roles.get(r["row_id"], set())]
def neg(rows): return [r for r in rows if "negative" in roles.get(r["row_id"], set())]
def cell(rows, field, maxn=4):
    vals, ids = [], []
    for r in rows:
        v = (r.get(field) or "").strip()
        if v:
            ids.append(r["row_id"])
            s = re.sub(r"\s+", " ", v)[:110]
            if s not in vals: vals.append(s)
    if not ids: return "undisclosed (no evidence row)"
    return " || ".join(vals[:maxn]) + " [" + ",".join(ids) + "]"
def cash_cell(rows):
    txt = lambda r: " ".join([r.get("terms",""), r.get("result",""), r.get("subject",""), r.get("payment_status","")]).lower()
    none = [r for r in rows if re.search(r"did not request or receive compensation|did not take payment|no compensation|not accepted compensation|no cash payment|did not (receive|accept) (payment|compensation)", txt(r))]
    und = [r for r in rows if re.search(r"compensation[^.;]{0,60}(undisclosed|not disclosed|not stated)|payment[^.;]{0,40}(undisclosed|not disclosed|not stated)", txt(r))]
    if none: return "none, as METR states [" + ",".join(r["row_id"] for r in none) + "]"
    if und: return "undisclosed in the engagement documents [" + ",".join(r["row_id"] for r in und) + "]"
    return "undisclosed (no evidence row)"
def sh_cell(rows):
    hit = [r for r in rows if "safe harbor" in (" ".join(r.values())).lower()]
    return cell(hit, "terms") if hit else "not stated in any evidence row"
out = []
for k, label, providers, _ in PROJECTS:
    q, i, rr, s = ev(by[k]["MDQ"]), ev(by[k]["MDI"]), ev(by[k]["MDR"]), neg(by[k]["MDS"])
    allq = q + i
    row = {
     "project_key": k, "project": label, "providers": providers,
     "direct_lab_cash": cash_cell(allq + ev(by[k]["MDP"])),
     "in_kind_resources": cell(i, "in_kind_type"),
     "access_dependence": cell([r for r in i + q if re.search(r"access|api|checkpoint|transcript", (r.get("in_kind_type","")+" "+r.get("terms","")).lower())], "terms" if not i else "in_kind_type") if (i or q) else "undisclosed (no evidence row)",
     "provider_authority": cell(q, "provider_authority"),
     "safe_harbor": sh_cell(q),
     "personnel_disclosures": (cell(q, "personnel_conflicts") if any((r.get("personnel_conflicts") or "").strip() for r in q) else "undisclosed (no evidence row)") + ("; relationships [" + ",".join(r["row_id"] for r in rr) + "]" if rr else ""),
     "policy_version": cell(q, "policy_version"),
     "bounded_gaps": ("[" + ",".join(r["row_id"] for r in s) + "]") if s else "",
     "evidence_rows": len(allq) + len(rr), "negative_rows": len(s),
    }
    for c in ("direct_lab_cash","in_kind_resources","access_dependence","provider_authority","safe_harbor","personnel_disclosures","policy_version"):
        assert not INFER.search(row[c].split(" [")[0]), (k, c, row[c])
    out.append(row)
p = ROOT/"research"/"independence_matrix.csv"
with open(p, "w", newline="") as f:
    f.write("# metr_deep independence matrix; built %s by scripts/build_independence_matrix.py from promoted rows bound as evidence (cells) or negative (gaps); every cell cites row ids; a cell with no qualifying row says so; direct-lab cash, in-kind resources and access dependence are separate columns; ARC-era rows are labelled and belong to Alignment Research Center, not METR; differences between rows are observations, not evidence of motive\n" % datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ"))
    w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
print("independence_matrix.csv rows=%d; projects with evidence rows=%d; unmatched MDQ rows=%d" % (len(out), sum(1 for r in out if r["evidence_rows"]), sum(1 for r in tables["MDQ"] if not key_for(r.get("project","")+" "+r.get("subject","")))))
