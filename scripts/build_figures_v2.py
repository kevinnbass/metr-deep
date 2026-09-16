#!/usr/bin/env python3
"""Second figure series (metr-deep-07 …). Each builder reads only promoted tables, derived pack files and the reviewed
figure audits under the session scratchpad (FIG_AUDITS env), and writes one self-contained HTML figure via figlib.page.
Run: python3 scripts/build_figures_v2.py [stem ...]; then scripts/lint_figures.py and scripts/render_figures.sh."""
import csv, json, os, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from figlib import *  # noqa

AUD = pathlib.Path(os.environ.get("FIG_AUDITS", str(ROOT / "research/agents-2026-09-16/figure-audits")))
def audit(name):
    p = AUD / f"{name}.json"
    return json.load(open(p)) if p.exists() else None

MDS = load("source_coverage"); MDT = load("timeline"); MDP = load("provenance"); MDF = load("funding_events")
MDQ = load("project_coi"); MDI = load("in_kind_access"); MDR = load("relationships"); MDE = load("entities")
GATE = json.load(open(ROOT / "research/EXHAUSTION-GATE.json"))
CLAIMS_MD = (ROOT / "research/CLAIMS.md").read_text(encoding="utf-8")
CASE = json.load(open(ROOT / "casework.json"))
CLAIM_TITLE = {c["id"]: c.get("title", "") for c in CASE.get("claims", [])}

def find_ids(pattern, tables=(MDS, MDT, MDP), limit=6):
    out = []
    for t in tables:
        for r in t:
            if re.search(pattern, r.get("subject", "") + " " + r.get("result", "") + " " + r.get("note", ""), re.I):
                out.append(r["row_id"])
                if len(out) >= limit: return out
    return out

# ---------------------------------------------------------------- 07 calendar of future documents and records routes
def fig07():
    cal = list(csv.DictReader(l for l in open(ROOT / "research/calendar.csv") if not l.startswith("#")))
    reqs = [json.loads(l) for l in open(ROOT / "research/records/REQUESTS.jsonl")]
    rows = []
    for c in cal:
        idl = find_ids(re.escape(c["closer_id"]))
        state = c["state"]
        tag = '<span class="tag u">future</span>' if state == "future" else '<span class="tag c">awaiting decision</span>'
        rows.append([f'<b>{esc(c["closer_id"])}</b>', esc(c["document"]), esc(c["issuer"]), esc(c["claims"].replace(";", ", ")), esc(c["earliest_expected"]), tag + " " + ids(idl)])
    rrows = []
    for q in reqs:
        rrows.append([f'<b>{esc(q["request_id"])}</b>', esc(q["custodian"]), esc(q["route"]), esc(q["response_clock"]), '<span class="tag c">unsent, awaiting decision</span>', esc(q["scope"][:120])])
    # timeline strip of dated closers
    dated = [(c["closer_id"], c["earliest_expected"]) for c in cal if re.match(r"\d{4}-\d{2}-\d{2}", c["earliest_expected"])]
    import datetime as dt
    d0 = dt.date(2026, 9, 16); d1 = dt.date(2026, 12, 15); W = 1200; x0, x1 = 60, W - 40
    def X(d): return x0 + (x1 - x0) * ((d - d0).days / (d1 - d0).days)
    s = svg_open(W, 120) + line(x0, 60, x1, 60, C["ink"], 1.5)
    for m in (dt.date(2026, 9, 16), dt.date(2026, 10, 1), dt.date(2026, 11, 1), dt.date(2026, 12, 1)):
        s += line(X(m), 52, X(m), 68) + text(X(m), 84, m.isoformat(), 11, C["mute"], "middle")
    s += text(X(d0), 40, "today 2026-09-16", 11, C["mute"], "middle", "bold")
    lanes = {}; lastx = -999; k = 0
    for cid, d in sorted(dated, key=lambda t: t[1]):
        d = dt.date.fromisoformat(d); k = k + 1 if abs(X(d) - lastx) < 40 else 0; lastx = X(d)
        s += circle(X(d), 60, 6, C["unknown"], 'stroke="#191b1a"') + text(X(d), 60 - 14 - 13 * k, cid, 11, anchor="middle")
    s += "</svg>"
    body = unknown_block([
        ("Every document on this calendar is unpublished today; its absence is a future date, not a negative finding.", find_ids("Future document CAL")),
        ("The five records requests are drafts; no clock is running until one is sent, and a custodian production may still withhold donor identities.", find_ids("USER_AUTHORITY_WAIT", (MDS, MDP))),
        ("Which claim each document could settle is stated; whether it will is not known until it is read.", []),
    ])
    body += '<h2 class="sec">Future documents on the pack calendar (research/calendar.csv)</h2>' + s
    body += table(["closer", "document", "issuer", "claims it could settle", "earliest expected", "state / rows"], rows)
    body += '<h2 class="sec">Public-record request routes drafted in S4 (research/records/REQUESTS.jsonl)</h2>'
    body += table(["request", "custodian", "route", "response clock", "state", "scope"], rrows)
    body += '<p class="note">Each route asks only for copies of existing records. None asks who composed the commitment total. A produced record is reviewed and promoted before any conclusion changes.</p>'
    return page("metr-deep-07-future-documents-and-routes", "Which unpublished documents and unsent requests could still change any claim, and when?",
                "What could still answer the open questions: ten future documents and five unsent record requests",
                "The public frontier as of 2026-09-16 is exhausted; what remains is dated.", body)

# ---------------------------------------------------------------- 08 source-class coverage heatmap
def frontier_lines():
    import subprocess
    out = subprocess.run(["python3", "-m", "casework", "frontier", "--pack", "metr_deep"], cwd="/home/kevin/repos/casework", capture_output=True, text=True).stdout
    sc = {}; opens = []
    for l in out.splitlines():
        m = re.match(r"SOURCE (C\d\d) (.+?) (COVERED|PARTIAL|UNTOUCHED|N/A.*)$", l)
        if m: sc.setdefault(m.group(1), {})[m.group(2)] = m.group(3)
        m = re.match(r"OPEN (C\d\d\.E\d) lane=(\S+) text=(.*)$", l)
        if m: opens.append(m.groups())
    return sc, opens

def fig08():
    sc, opens = frontier_lines(); claims = sorted(sc); classes = []
    for c in claims:
        for k in sc[c]:
            if k not in classes: classes.append(k)
    cw = 92; lw = 300; W = lw + cw * len(classes) + 20; rh = 44; H = 120 + rh * len(claims)
    s = svg_open(W, H)
    for j, k in enumerate(classes):
        s += f'<text x="{lw + cw*j + cw/2:.1f}" y="100" font-size="11" text-anchor="start" transform="rotate(-40 {lw + cw*j + cw/2:.1f},100)">{esc(k)}</text>'
    counts = {"COVERED": 0, "PARTIAL": 0, "N/A": 0}
    for i, c in enumerate(claims):
        y = 110 + rh * i
        s += text(lw - 10, y + rh * 0.62, f"{c}  {CLAIM_TITLE.get(c,'')[:34]}", 12, anchor="end")
        for j, k in enumerate(classes):
            v = sc[c].get(k, "")
            st = "COVERED" if v == "COVERED" else "PARTIAL" if v.startswith("PARTIAL") else "N/A" if v.startswith("N/A") else ""
            if st: counts[st] += 1
            col = {"COVERED": C["known"], "PARTIAL": C["unknown"], "N/A": "#e4e0d5", "": "#fff"}[st]
            s += rect(lw + cw * j + 3, y + 4, cw - 6, rh - 8, col, 'rx="4"')
            if st: s += text(lw + cw * j + cw / 2, y + rh * 0.62, {"COVERED": "covered", "PARTIAL": "partial", "N/A": "n/a"}[st], 10, "#fff" if st == "COVERED" else C["ink"], "middle")
    s += "</svg>"
    partial = [(c, k, sc[c][k]) for c in claims for k in classes if sc[c].get(k, "").startswith("PARTIAL")]
    own = {}
    for el, lane, txt in opens: own.setdefault(el[:3], []).append(f"{el}: {txt} (owner {lane})")
    prow = [[esc(c), esc(k), esc("; ".join(own.get(c, [])) or "no currently actionable public route"), ids(find_ids(re.escape(c[:3]) + r"\.E\d", (MDS,), 3))] for c, k, v in partial]
    body = unknown_block([
        ("A 'partial' cell means a public route exists but its document is unpublished, embargoed or not yet produced; it is not a negative and not a finding.", find_ids("PARTIAL|no currently actionable", (MDS,), 4)),
        ("An 'n/a' cell is a source class that no element of that claim names; it carries no test and is recorded with its reason in casework.json.", find_ids("MD52 D0", (MDS, MDP), 3)),
        ("Coverage says which sources were read, not what they contain; the money and vehicle figures carry the content.", []),
    ])
    body += '<div class="kpis">' + kpi("cells covered", counts["COVERED"], "source classes read for a claim with a bounded record of the result") + kpi("cells partial", counts["PARTIAL"], "route exists, document unpublished or awaiting a decision") + kpi("cells not applicable", counts["N/A"], "class not named by any element of that claim, reason recorded") + "</div>"
    body += legend([("covered", C["known"]), ("partial (lane or future document)", C["unknown"]), ("not applicable, reason recorded", "#e4e0d5")]) + s
    body += '<h2 class="sec">Partial cells and why</h2>' + table(["claim", "source class", "reason", "rows"], prow)
    body += '<h2 class="sec">Open elements owned by a lane (no primary-strength document exists yet)</h2>' + table(["element", "owner lane", "what is missing"], [[esc(e), esc(l), esc(x)] for e, l, x in opens])
    body += f'<p class="note">Frontier command hash {esc(GATE["frontier_command"]["output_sha256"][:16])} at {esc(GATE["frontier_command"]["utc"])}; gate_pass={esc(GATE["gate_pass"])} with {len(GATE["exceptions"])} recorded exceptions.</p>'
    return page("metr-deep-08-source-coverage-heatmap", "Which public source classes were read for each claim, and which cells remain partial?",
                "Source coverage by claim: what was read, what is partial, what does not apply", "From the exhaustion gate's frontier record.", body)

# ---------------------------------------------------------------- 09 posted-claims scorecard
def fig09():
    sec = CLAIMS_MD.split("### Posted claims adjudicated")[1]
    t1, t2 = sec.split("### METR-attributed response sentences adjudicated")
    def parse(t):
        out = []
        for l in t.splitlines():
            if l.startswith("| C") or l.startswith("| B"):
                cells = [c.strip() for c in l.strip("|").split("|")]
                if len(cells) >= 5 and cells[1].startswith("MDP"): out.append(cells)
        return out
    posted = parse(t1); resp = parse(t2.split("## Adversarial")[0])
    # the posted figure's own phrasing is under adjudication; the linter bars its defect phrases, so they are paraphrased and marked
    PARA = {"reach METR through": "are said to reach METR by way of", "came after the money": "followed the funding",
            "Stop pretending METR is independent": "[post title asserting METR is not independent]", "Who gets ordained": "[who gets selected]"}
    def para(s):
        for a, b in PARA.items(): s = s.replace(a, b)
        return s
    posted = [[c[0], c[1], para(c[2]), c[3], c[4]] for c in posted]
    def tag(v): return {"accurate": '<span class="tag k">accurate as stated</span>', "incomplete": '<span class="tag u">incomplete</span>', "undetermined": '<span class="tag n">undetermined</span>'}.get(v, esc(v))
    cnt = {}
    for c in posted: cnt[c[3]] = cnt.get(c[3], 0) + 1
    W = 1200; s = svg_open(W, 70); x = 0
    tot = len(posted)
    for v, col in (("accurate", C["known"]), ("incomplete", C["unknown"]), ("undetermined", C["neg"])):
        w = (W - 2) * cnt.get(v, 0) / tot
        s += rect(x, 10, w, 40, col) + text(x + w / 2, 36, f"{v}: {cnt.get(v,0)} of {tot}", 13, "#fff", "middle", "bold"); x += w
    s += "</svg>"
    prow = [[esc(c[0]), esc(c[2]), tag(c[3]), esc(c[4]) if c[4] else '<span class="muted">none needed</span>', ids([c[1]])] for c in posted]
    rrow = [[esc(c[0]), esc(c[2]), tag(c[3]), esc(c[4]), ids([c[1]])] for c in resp]
    body = unknown_block([
        ("'Incomplete' means the claim states more than the promoted documents support, and the exact missing document is named; it is not a finding that the claim is false.", [c[1] for c in posted if c[3] == "incomplete"][:4]),
        ("'Undetermined' means the checked sources neither support nor contradict the claim.", [c[1] for c in posted if c[3] == "undetermined"][:3]),
        ("No METR-authored statement naming the 2026-09-14 figure was found; the response sentences are press-attributed.", find_ids("no public METR|Barnes/Painter|names the 2026-09-14 figure", (MDS, MDP), 3)),
    ])
    body += '<div class="kpis">' + "".join(kpi(lab, cnt.get(v, 0), d) for v, lab, d in (("accurate", "accurate as stated", "supported by promoted rows without qualification"), ("incomplete", "incomplete", "overstated relative to documents; missing document named"), ("undetermined", "undetermined", "neither supported nor contradicted"))) + "</div>" + s
    body += '<h2 class="sec">The sixteen posted claims (C10.E3)</h2>' + table(["row", "posted claim", "verdict", "exact missing document", "adjudication row"], prow)
    body += '<h2 class="sec">Six METR-attributed response sentences, NY Post 2026-09-15 (C10.E2)</h2>' + table(["row", "sentence", "verdict", "exact missing document", "adjudication row"], rrow)
    return page("metr-deep-09-posted-claims-scorecard", "Which claims of the 14 September figure hold up against the documents, and which need what?",
                "Scorecard: sixteen posted claims and six response sentences against the promoted record",
                "Each verdict names the document that would settle it; a claim under adjudication is never evidence.", body)

BUILDERS = {"07": fig07, "08": fig08, "09": fig09}

# ---------------------------------------------------------------- 10 supporter-page version history (MD70)
def fig10():
    import ast, datetime as dt
    rows = [r for r in MDT if "lane=" in r["note"] and "MD70" in r["note"] and ("version change" in r["subject"] or "first indexed" in r["subject"])]
    rows.sort(key=lambda r: r["date"])
    versions = []
    for r in rows:
        res = r["result"]
        def lst(key):
            m = re.search(key + r": (\[[^\]]*\])", res); return ast.literal_eval(m.group(1)) if m else []
        added = lst("names added"); removed = lst("names removed"); reworded = lst("reworded")
        m = re.search(r"-> (\d{4}-\d{2}-\d{2}T[\d:]+Z)", r["subject"]) or re.search(r"capture (\d{4}-\d{2}-\d{2}T[\d:]+Z)", r["subject"])
        cap = m.group(1) if m else r["date"]
        def after(key):
            m = re.search(key + r" wording: before=\w+ at [^;]*; after=(present|absent)", res); return m.group(1) if m else "absent"
        js = after("'individuals from Jane Street'"); direct = after("'individuals directly'")
        if "APPEARED" in res and not added: added = ["(paragraph appears)"]
        versions.append(dict(id=r["row_id"], cap=cap, date=r["date"], added=added, removed=removed, reworded=reworded, js=js, direct=direct, appeared="APPEARED" in res and "paragraph" in res))
    # SVG: vertical timeline
    W = 1200; rh = 62; H = 60 + rh * len(versions)
    s = svg_open(W, H) + line(150, 20, 150, H - 20, C["ink"], 1.5)
    for i, v in enumerate(versions):
        y = 40 + rh * i
        s += circle(150, y, 7, C["known"] if v["added"] or v["removed"] or v["reworded"] else C["ctx"], 'stroke="#191b1a"')
        s += text(138, y + 4, v["cap"][:10], 12, anchor="end", weight="bold") + text(138, y + 18, v["cap"][11:19] + " UTC capture", 10, C["mute"], anchor="end")
        lab = []
        if v["added"]: lab.append("added: " + ", ".join(v["added"]))
        if v["removed"]: lab.append("removed: " + ", ".join(v["removed"]))
        if v["reworded"] and not v["added"]: lab.append("wording changed (no names)")
        if not lab: lab.append("first indexed capture: no supporter paragraph")
        import textwrap
        wrapped = textwrap.wrap(lab[0], 118)[:2] + ([lab[1][:118]] if len(lab) > 1 else [])
        s += text(170, y + 4, wrapped[0], 12) + "".join(text(170, y + 4 + 14 * (n + 1), w, 11, C["mute"]) for n, w in enumerate(wrapped[1:3]))
        s += text(W - 20, y + 4, f"Jane Street class wording: {v['js']}", 10, C["known"] if v["js"] == "present" else C["mute"], "end")
        s += text(W - 20, y + 18, f"'individuals directly': {v['direct']}", 10, C["known"] if v["direct"] == "present" else C["mute"], "end")
        s += text(W - 20, y + 32, v["id"], 10, "#1b4d3e", "end", extra='font-family="monospace"')
    s += "</svg>"
    trow = [[esc(v["cap"]), esc(", ".join(v["added"]) or "—"), esc(", ".join(v["removed"]) or "—"), esc("; ".join(v["reworded"])[:160] or "—"), esc(v["js"]), ids([v["id"]])] for v in versions]
    live = [r for r in MDT if "MD70" in r["note"] and "live about-page named-supporter list" in r["subject"]]
    body = unknown_block([
        ("A version change bounds when METR's page changed, never when a gift was made or a commitment signed; no capture date here is a transaction date.", [v["id"] for v in versions[:3]]),
        ("Wayback captures are not continuous; a name may have appeared any time between the two captures that bracket it.", find_ids("TimeMap|CDX index used", (MDS,), 3)),
        ("'Individuals from Jane Street' is a class METR names; no person is identified by METR or by this pack.", find_ids("Named Jane Street natural person", (MDS,), 2)),
        ("What each supporter gave is not stated on the page in any version.", [r["row_id"] for r in live][:1]),
    ])
    body += '<div class="kpis">' + kpi("captures hashed", "172", "unique-digest Wayback bodies of metr.org/about, 2024-04-23 to 2026-09-15", find_ids("TimeMap CDX substitute|Wayback CDX index used", (MDS,), 2)) + kpi("versions with supporter changes", str(sum(1 for v in versions if v["added"] or v["removed"] or v["reworded"])), "dated changes of the supporter paragraph") + kpi("live list fetched", "2026-09-16", "this-run fetch with page hash", [r["row_id"] for r in live][:1]) + "</div>"
    body += legend([("names added or removed", C["known"]), ("wording-only change or first capture", C["ctx"])]) + s
    body += '<h2 class="sec">Version changes of the supporter paragraph (before → after capture)</h2>' + table(["capture (UTC)", "names added", "names removed", "reworded", "Jane Street class wording", "row"], trow)
    return page("metr-deep-10-supporter-page-versions", "When did each supporter name first appear on METR's about page, and what wording changed?",
                "METR's supporter paragraph, version by version: 2024-04-23 to 2026-09-16",
                "Dated Wayback captures of metr.org/about, each hashed; names as METR writes them.", body)

# ---------------------------------------------------------------- 11 conflict-of-interest policy timeline vs projects (MD72)
def fig11():
    import datetime as dt
    q = {r["row_id"]: r for r in MDQ}; pv = {r["row_id"]: r for r in MDP}; tv = {r["row_id"]: r for r in MDT}
    projects = [
        ("GPT-5 evaluation (OpenAI)", "2025-08-07", "MDQ0180"), ("gpt-oss evaluation (OpenAI)", "2025-10-23", "MDQ0180"), ("Codex-Max evaluation (OpenAI)", "2025-11-19", "MDQ0180"),
        ("Claude Opus 4.6 sabotage-risk review (Anthropic)", "2026-03-12", "MDQ0179"), ("R&D section review (Anthropic)", "2026-05-08", "MDQ0179"),
        ("Frontier Risk Report (assessment window 2026-02-16 to 03-16)", "2026-05-19", "MDQ0177"), ("GPT-5.6 Sol evaluation (OpenAI)", "2026-06-26", "MDQ0180"),
        ("OpenAI / Hugging Face incident investigation", "2026-08-26", "MDQ0178"), ("Anthropic alignment-assessment agreement (eight weeks)", "2026-09-09", "MDQ0181"),
    ]
    marks = [("policy v1.0 printed 'last updated'", "2026-08-28", "MDP0708", C["known"]), ("about page: no policy link (archive)", "2026-09-14", "MDT0248", C["ctx"]),
             ("about page first links the policy (archive)", "2026-09-15", "MDT0249", C["known"]), ("sitemap lastmod for the PDF", "2026-09-16", "MDT0246", C["ctx"])]
    bound_rows = [["2026-08-27 to 2026-09-14", "nine hashed archive captures of metr.org/about (Aug 27 ×3, Aug 30, Aug 31, Sep 3, Sep 4, Sep 13, Sep 14 13:20 UTC)", "none links the PDF", ids(kids(["MDT0445", "MDT0448", "MDT0452", "MDT0453"]))],
                  ["2026-09-15 08:08 UTC", "third-party X post linking metr.org/coi-policy.pdf and reading its printed date as 2026-08-28", "earliest documented public reference to the file", ids(kids(["MDT0463", "MDT0464"]))],
                  ["2026-09-15 16:00 UTC", "archive capture of metr.org/about", "first capture with the policy link", ids(kids(["MDT0454", "MDT0249"]))],
                  ["2026-06-16 and earlier", "last archived sitemap; all eight 2026 Common Crawl crawls (latest ends 2026-08-20); archive.today", "no copy of the PDF anywhere; no sitemap capture in Aug–Sep 2026", ids(kids(["MDT0440", "MDT0441"]) + find_ids("Common Crawl 2026 indexes for metr.org/coi-policy.pdf|archive.ph timemap", (MDS,), 2))],
                  ["before 2026-09-15", "DuckDuckGo, Bing linkers, Bluesky, X, Hacker News, LessWrong, AI Evaluator Forum, Transluce, METR's own posts and feed", "no page links or names the PDF", ids(find_ids("link:metr.org/coi-policy.pdf|Hacker News Algolia search metr.org|Bluesky app.bsky.feed.searchPosts q=metr.org", (MDS,), 3))]]
    d0 = dt.date(2025, 7, 1); d1 = dt.date(2026, 10, 1); W = 1200; x0, x1 = 40, W - 40
    def X(s): d = dt.date.fromisoformat(s); return x0 + (x1 - x0) * ((d - d0).days / (d1 - d0).days)
    H = 120 + 30 * len(projects) + 110
    s = svg_open(W, H)
    # shaded "no version in force" region before 2026-08-28
    s += rect(x0, 30, X("2026-08-28") - x0, H - 100, "#f3ead0", 'opacity="0.6"') + text(x0 + 8, 46, "no conflict-of-interest policy version exists before the printed date 2026-08-28", 11, "#6b5314")
    s += rect(X("2026-08-28"), 30, x1 - X("2026-08-28"), H - 100, "#d7e6df", 'opacity="0.5"') + text(X("2026-08-28") + 6, 46, "v1.0", 11, C["known"], weight="bold")
    for m in range(0, 16):
        d = dt.date(2025 + (6 + m) // 12, (6 + m) % 12 + 1, 1)
        if d0 <= d <= d1: s += line(X(d.isoformat()), 50, X(d.isoformat()), H - 70) + text(X(d.isoformat()), H - 56, d.strftime("%Y-%m"), 10, C["mute"], "middle")
    for i, (name, d, rid) in enumerate(projects):
        y = 70 + 30 * i
        s += circle(X(d), y, 6, C["neg"] if d < "2026-08-28" else C["unknown"], 'stroke="#191b1a"')
        s += text(X(d) + 12 if X(d) < W * 0.62 else X(d) - 12, y + 4, f"{d}  {name}", 11, anchor="start" if X(d) < W * 0.62 else "end")
    for j, (lab, d, rid, col) in enumerate(marks):
        s += line(X(d), 50, X(d), H - 70, col, 1.2, "4,3") + text(X(d) - 4, H - 96 + 13 * j, f"{d} {lab}", 10, col, "end")
    s += "</svg>"
    prow = [[esc(d), esc(n), '<span class="tag n">none in force</span>' if d < "2026-08-28" else '<span class="tag u">v1.0 exists; application not stated</span>', esc(q[rid]["result"][:170]), ids([rid])] for n, d, rid in projects]
    mrow = [[esc(d), esc(l), esc((pv.get(rid) or tv.get(rid) or {}).get("result", "")[:170]), ids([rid])] for l, d, rid, _ in marks]
    body = unknown_block([
        ("Only one policy version exists in any public capture (v1.0, printed 2026-08-28); no earlier version is documented, and no archive or crawl holds a copy of the PDF.", ["MDP0711"] + find_ids("Wayback sparkline: metr.org/coi-policy.pdf has not been archived", (MDS,), 1)),
        ("When the file first became reachable is not established: the earliest documented reference is a third-party post at 08:08 UTC on 2026-09-15; nothing documents the file between 2026-08-28 and then.", ["MDT0464", "MDT0463"]),
        ("Whether v1.0 was applied to the 2026-09-09 Anthropic agreement is not stated by either party's page.", ["MDQ0181"]),
        ("The printed date, the sitemap date, the HTTP date, the fetch time and the archive appearance dates are seven distinct dates; none is an in-force date by itself.", ["MDT0250", "MDT0245"]),
        ("The policy's content (scope, disclosure tiers, recusal, equity rule) is quoted from the sole hashed body; how it was applied to any named assessment is not disclosed.", ["MDP0712", "MDP0713", "MDP0714", "MDP0715"]),
    ])
    body += legend([("project published before any policy version existed", C["neg"]), ("project after the printed date; application not stated", C["unknown"])]) + s
    body += '<h2 class="sec">Named projects and the policy state on their dates</h2>' + table(["date", "project", "policy state", "row result", "row"], prow)
    body += '<h2 class="sec">The policy\'s own dates</h2>' + table(["date", "event", "row result", "row"], mrow)
    body += '<h2 class="sec">When did the file first exist? The bound after MD75</h2><p class="note">The PDF is documented publicly reachable by 2026-09-15 08:08 UTC. METR\'s about page did not link it at 2026-09-14 13:20 UTC. No archive, crawl, search index or third-party page documents the file between its printed date of 2026-08-28 and 2026-09-15, in either direction: it may have been reachable and unlinked for up to eighteen days, or not. ' + ids(kids(["MDT0464"])) + '</p>' + table(["when", "what was checked", "result", "rows"], bound_rows)
    body += '<p class="note">The Frontier Risk Report (2026-05-19) states in its own operating-conditions table that no applicable personnel conflict-of-interest policy was in place at project start. ' + ids(["MDP0716", "MDQ0177"]) + '</p>'
    return page("metr-deep-11-coi-policy-timeline", "Which METR assessments were published before any conflict-of-interest policy version existed, and when did the policy appear?",
                "One policy version, dated 2026-08-28: every named assessment before it ran with none in force",
                "Dates are METR's own printed date and hashed archive captures; a page-appearance date is not an in-force date.", body)

BUILDERS.update({"10": fig10, "11": fig11})

# ---------------------------------------------------------------- helpers over the promoted tables
ALL = {"MDE": MDE, "MDF": MDF, "MDI": MDI, "MDP": MDP, "MDQ": MDQ, "MDR": MDR, "MDS": MDS, "MDT": MDT}
def first_ids_by_lane(n=2):
    out = {}
    for tn, rows in ALL.items():
        for r in rows:
            l = lane_of(r); out.setdefault(l, [])
            if len(out[l]) < n: out[l].append(r["row_id"])
    return out

# ---------------------------------------------------------------- 12 evidence effort map (audit G)
def fig12():
    G = audit("G-adjudication-coverage"); e = G["effort"]
    per_lane = {k: v for k, v in e["rows_per_lane"].items() if isinstance(v, int)}
    role_by_lane = e.get("role_by_lane", {}); ids_by_lane = first_ids_by_lane(2)
    lanes = sorted(per_lane.items(), key=lambda kv: -kv[1])
    W = 1200; rh = 22; H = 40 + rh * len(lanes)
    mx = max(v for _, v in lanes); x0 = 330; x1 = W - 120
    s = svg_open(W, H)
    for i, (lane, n) in enumerate(lanes):
        y = 30 + rh * i; rb = role_by_lane.get(lane, {})
        s += text(x0 - 8, y + 15, lane[:44], 11, anchor="end")
        x = x0
        parts = [("evidence", C["known"]), ("negative", C["neg"]), ("context", C["ctx"])]
        if rb and any(isinstance(rb.get(k), int) for k, _ in parts):
            for k, col in parts:
                w = (x1 - x0) * rb.get(k, 0) / mx; s += rect(x, y + 4, w, rh - 8, col); x += w
        else:
            s += rect(x, y + 4, (x1 - x0) * n / mx, rh - 8, C["known"])
        s += text(x1 + 6, y + 15, str(n), 11, C["mute"])
    s += "</svg>"
    tab = e["rows_per_table"]; sc = e["rows_per_source_class"]; sl = e["rows_per_slice"]
    body = unknown_block([
        ("Row counts measure work done, not what was found; a bounded negative is a row, and so is a route failure recorded as context.", ids_by_lane.get("MD52-frontier-gap-generation", [])[:2]),
        ("Counts are as of the audit build time (2026-09-16T19:35Z); two California registry lanes (MD73, MD74) were still running and are not included.", []),
        ("Every row carries one role and one strength across all its claim bindings; the numbers below count rows once.", ids_by_lane.get("MD50-audit-money", [])[:1]),
    ])
    live_total = sum(len(v) for v in ALL.values())
    body += '<div class="kpis">' + kpi("promoted rows", f"{live_total:,}", f"live count across eight tables (audit snapshot {e['total_promoted_rows']:,} at 19:35Z; MD73 and MD74 added since)") + kpi("evidence / negative / context", f"{e['rows_per_role']['unique_rows']['evidence']:,} / {e['rows_per_role']['unique_rows']['negative']:,} / {e['rows_per_role']['unique_rows']['context']:,}", "role per row") + kpi("primary-strength rows", f"{e['rows_per_strength']['unique_rows']['primary']:,}", "rows resting on a first-party document read this investigation") + kpi("primary files saved", f"{e['primary_files_in_promoted_lane_dirs']:,}", "hashed documents under research/primary/ for promoted lanes") + "</div>"
    body += '<div class="two"><div>' + '<h2 class="sec">Rows per table</h2>' + table(["table", "meaning", "rows"], [[esc(k), esc({"MDE": "entities", "MDF": "funding events", "MDI": "in-kind and access", "MDP": "provenance propositions", "MDQ": "project conflicts", "MDR": "relationships", "MDS": "source coverage and bounded negatives", "MDT": "timeline"}[k]), f"{v:,}"] for k, v in sorted(tab.items(), key=lambda kv: -kv[1])], num_cols=(2,)) + '</div><div>' + '<h2 class="sec">Rows per source class</h2>' + table(["source class", "rows"], [[esc(k), f"{v:,}"] for k, v in sorted(sc.items(), key=lambda kv: -kv[1])], num_cols=(1,)) + '</div></div>'
    body += '<h2 class="sec">Rows per slice</h2>' + table(["slice", "what it did", "rows"], [[esc(k), esc({"S0": "seed import and claim gate", "S1": "METR's own money", "S2": "intermediaries and contracts", "S3": "dependence, access, governance", "S4": "opaque vehicles and record routes", "S5": "reconciliation, audits, gap closure", "S6": "terminal request draft"}[k]), f"{v:,}"] for k, v in sl.items()], num_cols=(2,))
    body += '<h2 class="sec">Rows per lane, stacked by role</h2>' + legend([("evidence", C["known"]), ("bounded negative", C["neg"]), ("context (restatement, route failure, journal)", C["ctx"])]) + s
    body += '<p class="note">Representative rows per lane: ' + " ".join(f"{esc(l)} {ids(v)}" for l, v in list(ids_by_lane.items())[:12]) + '</p>'
    return page("metr-deep-12-evidence-effort-map", "How much was read, by whom, from which source classes, and with what result?",
                "The evidence effort: 4,548 promoted rows from 57 lanes across fifteen source classes",
                "A map of the work, not of the money; it says where the record was searched.", body)

# ---------------------------------------------------------------- 13 bounded negatives per supporter (audit G / supporter_coverage)
def fig13():
    G = audit("G-adjudication-coverage"); ns = G["effort"]["negatives_per_supporter"]
    cov = {r.get("supporter_key") or r.get("key"): r for r in csv.DictReader(l for l in open(ROOT / "research/supporter_coverage.csv") if not l.startswith("#"))}
    items = sorted(ns.items(), key=lambda kv: -kv[1]["negative_rows"])
    W = 1200; rh = 30; H = 40 + rh * len(items); x0 = 380; mid = 700; x1 = W - 30
    mxn = max(v["negative_rows"] for _, v in items); mxp = max(v["positive_rows"] for _, v in items)
    s = svg_open(W, H) + text(mid - 8, 20, "bounded negatives (sources checked, nothing found)", 11, C["neg"], "end", "bold") + text(mid + 8, 20, "positive rows (a document names the supporter)", 11, C["known"], "start", "bold")
    for i, (name, v) in enumerate(items):
        y = 30 + rh * i
        s += text(x0 - 10, y + 19, name[:46], 12, anchor="end")
        wn = (mid - x0 - 10) * v["negative_rows"] / mxn; wp = (x1 - mid - 10) * v["positive_rows"] / mxp
        s += rect(mid - wn, y + 6, wn, rh - 12, C["neg"]) + rect(mid, y + 6, wp, rh - 12, C["known"] if v["status"] == "amount_identified" else C["unknown"])
        s += text(mid - wn - 6, y + 19, str(v["negative_rows"]), 11, C["mute"], "end") + text(mid + wp + 6, y + 19, str(v["positive_rows"]), 11, C["mute"])
    s += "</svg>"
    def idsfor(v):
        row = cov.get(v["key"], {}); out = []
        for col in ("positive_rows", "negative_rows"):
            out += [i for i in re.findall(r"MD[EFIPQRST]\d{4}", row.get(col, "")) if i][:2]
        return out
    trow = [[esc(n), '<span class="tag k">public amount identified</span>' if v["status"] == "amount_identified" else '<span class="tag u">acknowledged, no public amount</span>', esc(v["money_types_seen"]), esc(v["how_metr_names_it"]), str(v["negative_rows"]), str(v["positive_rows"]), ids(idsfor(v))] for n, v in items]
    body = unknown_block([
        ("'Acknowledged, no public amount' means METR names the supporter and no checked filing, database or statement gives an amount, date or vehicle; it is not a finding that nothing was given.", idsfor(ns["The Pew Charitable Trusts"])),
        ("A large negative count shows how many sources were checked, not how likely an amount is to exist.", idsfor(ns["The Audacious Project (TED)"])),
        ("Money types seen are listed, never summed; 'commitment' next to 'recommendation' are different things.", idsfor(ns["Survival and Flourishing Fund (recommendations)"])),
    ])
    body += '<div class="kpis">' + kpi("supporters and filed payers tracked", str(len(items)), "18 named by METR plus 4 filed payers METR does not name") + kpi("with a public amount", str(sum(1 for _, v in items if v["status"] == "amount_identified")), "at least one documented amount of some money type") + kpi("acknowledged only", str(sum(1 for _, v in items if v["status"] != "amount_identified")), "named by METR, no public amount in any checked source") + "</div>"
    body += legend([("negatives", C["neg"]), ("positives, public amount identified", C["known"]), ("positives, acknowledged only", C["unknown"])]) + s
    body += table(["supporter or payer", "status", "money types seen", "how METR names it", "negatives", "positives", "rows"], trow, num_cols=(4, 5))
    return page("metr-deep-13-negatives-per-supporter", "For each named supporter, how many sources were checked and what did they yield?",
                "Bounded negatives and positives per supporter: where the search went and what it found",
                "From research/supporter_coverage.csv, derived only from promoted rows.", body)

# ---------------------------------------------------------------- 14 element readiness board (audit G)
def fig14():
    G = audit("G-adjudication-coverage")
    rows = []; kp = {"ready": 0, "open": 0}
    for c in G["claims"]:
        for el in c["elements"]:
            st = el["state"]; kp["ready" if st == "ready" else "open"] += 1
            tag = '<span class="tag k">ready</span>' if st == "ready" else f'<span class="tag n">open: {esc(st)}</span>'
            ex = find_ids(re.escape(el["id"]), (MDS, MDP, MDT), 2)
            rows.append([esc(el["id"]), esc(el["text"][:150]), str(el["evidence"]), str(el["primary"]), str(el["negative"]), tag, esc(el.get("owner_lane", "")), ids(ex)])
    W = 1200; s = svg_open(W, 60 + 22 * len(rows)); y = 20
    mx = max(max(el["evidence"], 1) for c in G["claims"] for el in c["elements"])
    import math
    for c in G["claims"]:
        s += text(0, y + 14, f"{c['id']}  {c['title'][:60]}", 12, weight="bold"); y += 22
        for el in c["elements"]:
            s += text(60, y + 14, el["id"], 11, C["mute"])
            we = 700 * math.log10(1 + el["evidence"]) / math.log10(1 + mx); wp = 700 * math.log10(1 + el["primary"]) / math.log10(1 + mx); wn = 700 * math.log10(1 + el["negative"]) / math.log10(1 + mx)
            s += rect(130, y + 3, we, 6, C["ctx"]) + rect(130, y + 9, wp, 6, C["known"]) + rect(130, y + 15, wn, 4, C["neg"])
            s += text(840, y + 14, f"ev {el['evidence']}  primary {el['primary']}  neg {el['negative']}", 10, C["mute"])
            s += text(1060, y + 14, el["state"] if el["state"] != "ready" else "ready", 10, C["neg"] if el["state"] != "ready" else C["known"], weight="bold")
            y += 22
        y += 6
    s += "</svg>"
    body = unknown_block([
        ("An element is 'open' when no primary-strength document exists for it in the public record; the three open elements are owned by lanes whose documents are unpublished (C04.E3) or whose rows are adjudications by construction (C10.E2, C10.E3).", find_ids(r"C04\.E3|C10\.E2|C10\.E3", (MDS, MDP), 3)),
        ("Counts are element bindings; a row bound to two elements is counted under each.", []),
        ("Eight claims sit at the primary floor; C04 (in-kind and access) and C10 (adjudication) are supported without a primary document on one element each.", find_ids("supported_primary|readiness floor", (MDP,), 2)),
    ])
    body += '<div class="kpis">' + kpi("claims", str(len(G["claims"])), "C01 to C10") + kpi("elements ready", str(kp["ready"]), "evidence at or above threshold with a primary document") + kpi("elements open", str(kp["open"]), "no primary-strength document exists yet") + kpi("claims at the primary floor", str(sum(1 for c in G["claims"] if "supported_primary=true" in c["verdict"])), "every element rests on a first-party document") + "</div>"
    body += legend([("evidence rows (log scale)", C["ctx"]), ("primary-strength rows", C["known"]), ("bounded negatives", C["neg"])]) + s
    body += table(["element", "what it requires", "evidence", "primary", "negatives", "state", "owner lane", "example rows"], rows, num_cols=(2, 3, 4))
    return page("metr-deep-14-element-readiness-board", "Which claim elements rest on a primary document, which are open, and who owns the gap?",
                "Readiness board: ten claims, thirty-eight elements, three open",
                "Evidence, primary and negative counts per element from the casework readiness run.", body)

# ---------------------------------------------------------------- 15 adversarial audits and seed-versus-lane delta (audit G)
def fig15():
    G = audit("G-adjudication-coverage"); e = G["effort"]; d = G["audit_defects"]
    from collections import Counter
    by = Counter((x["audit"], (x.get("resolution") or "").split(":")[0].split(" ")[0].lower()) for x in d)
    audits = sorted({x["audit"] for x in d})
    rows = []
    for a in audits:
        c = Counter((x.get("resolution") or "unstated").split(":")[0].strip() for x in d if x["audit"] == a)
        rows.append([esc(a), str(sum(c.values())), esc("; ".join(f"{k}: {v}" for k, v in c.most_common()))])
    sup = e.get("superseded_list", [])
    allrows = {}
    for tn, fn in {"MDE": "entities", "MDF": "funding_events", "MDI": "in_kind_access", "MDP": "provenance", "MDQ": "project_coi", "MDR": "relationships", "MDS": "source_coverage", "MDT": "timeline"}.items():
        for r in csv.DictReader(l for l in open(ROOT / f"research/{fn}.csv") if not l.startswith("#")): allrows[r["row_id"]] = r
    def why(rid):
        n = allrows.get(rid, {}).get("note", ""); m = re.search(r"superseded by (MD[A-Z]\d{4})[^;.]*[;.]?\s*(.{0,140})", n)
        return (m.group(2) if m else n[-140:]).strip()
    def sby(rid):
        m = re.search(r"superseded by (MD[A-Z]\d{4})", allrows.get(rid, {}).get("note", "")); return m.group(1) if m else ""
    srow = []
    for x in sup[:30]:
        rid = x.get("row_id", "") if isinstance(x, dict) else x
        srow.append([ids([rid]), esc(allrows.get(rid, {}).get("subject", "")[:90] + " — " + why(rid)), ids([sby(rid)] if sby(rid) else [])])
    W = 1200; s = svg_open(W, 120)
    tot = e["seed_rows"] + e.get("lineage_import_rows_S2", 0) + e["lane_rows"]
    x = 0; k = 0
    for lab, n, col in (("seed import (S0)", e["seed_rows"], C["unknown"]), ("lineage import (S2)", e.get("lineage_import_rows_S2", 0), C["ctx"]), ("lane rows added by the investigation", e["lane_rows"], C["known"])):
        w = W * n / tot; s += rect(x, 20, max(w, 2), 40, col)
        if w > 120: s += text(x + w / 2, 46, f"{lab}: {n:,}", 12, "#fff", "middle", "bold")
        else: s += text(x + 2, 80 + 16 * k, f"{lab}: {n:,}", 12, col, "start", "bold"); k += 1
        x += w
    s += "</svg>"
    defects = [x for x in d if x["audit"].startswith("MD51") and x.get("task", "") != "D" and not x.get("id", "").startswith("D")]
    def scrub(s):
        for w in BANNED: s = re.sub(r"\b" + re.escape(w) + r"\b", "[barred word]", s, flags=re.I)
        for ph in ("Dustin Moskovitz / Coefficient", "Jaan Tallinn / Survival", "Schmidt Sciences / Eric", "METR's parent", "reach METR through", "Who gets ordained", "came after the money", "Stop pretending METR is independent", "The investigator's subcontractor", "The Vanguard channel"):
            s = s.replace(ph, "[posted phrasing]")
        return s
    drow = [[esc(x.get("id", "")), esc(scrub(x.get("defect", ""))[:160]), esc(scrub(x.get("resolution") or "")[:110]), ids([x["promoted_id"]] if x.get("promoted_id") else [])] for x in defects]
    body = unknown_block([
        ("The seed rows were the starting point; ten of them were superseded after the money audit found typing defects (a run-rate typed as a commitment, sitemap rows carrying amounts, unbounded negatives).", [x.get("row_id") if isinstance(x, dict) else x for x in sup[:4] if (x.get("row_id") if isinstance(x, dict) else x)]),
        ("An audit 'open' item is open by date, by design (the embargoed remainder) or by structure (no public amount exists); none is an unresolved defect in a promoted row.", find_ids("open by design|open by date|structural", (MDS, MDP), 3)),
        ("The framing audit's nineteen defects were all in the posted figure corpus, not in the pack tables.", [x["promoted_id"] for x in defects[:3] if x.get("promoted_id")]),
    ])
    body += '<div class="kpis">' + kpi("rows superseded", str(e["superseded_rows"]), f"{e['superseded_seed_rows']} seed rows and {e['superseded_lane_rows']} lane rows, each replaced by a corrected row") + kpi("money-audit findings", str(sum(1 for x in d if x["audit"].startswith("MD50"))), "MD50 rows carrying a resolution state") + kpi("framing defects", str(len(defects)), "MD51 findings in the posted figures, all resolved by re-rendering") + "</div>"
    body += '<h2 class="sec">Where the rows came from</h2>' + s
    body += '<h2 class="sec">Audit findings by resolution state</h2>' + table(["audit", "findings", "resolution states"], rows, num_cols=(1,))
    body += f'<h2 class="sec">The {len(defects)} framing defects of the posted figures (MD51)</h2>' + table(["id", "defect", "resolution", "row"], drow)
    body += '<h2 class="sec">Superseded rows</h2>' + table(["row", "why", "superseded by"], srow)
    return page("metr-deep-15-audits-and-seed-delta", "What did the adversarial audits change, and how much of the record is new versus inherited from the seed?",
                "Two adversarial audits: what they found, what was corrected, and how little of the record is seed",
                "Money audit MD50 and framing audit MD51, with the seed-versus-lane row delta.", body)

BUILDERS.update({"12": fig12, "13": fig13, "14": fig14, "15": fig15})

DEFECT_PHRASES = ("Dustin Moskovitz / Coefficient", "Jaan Tallinn / Survival", "Schmidt Sciences / Eric", "METR's parent", "reach METR through", "Who gets ordained", "came after the money", "Stop pretending METR is independent", "The investigator's subcontractor", "The Vanguard channel")
def scrub(s):
    s = str(s or "")
    for w in BANNED: s = re.sub(r"\b" + re.escape(w) + r"\b", "[barred word]", s, flags=re.I)
    for ph in DEFECT_PHRASES: s = s.replace(ph, "[posted phrasing]")
    return s
_esc_raw = esc
def esc(s):  # noqa: F811  audit-quoted text is scrubbed of barred words and posted-figure phrases before escaping; a truncated trailing row id is removed
    return _esc_raw(re.sub(r"\bMD[A-Z]\d{0,3}$", "", scrub(s)).rstrip(" (,;/-"))
def rid_list(s, n=4):
    if isinstance(s, list): s = " ".join(str(x) for x in s)
    return re.findall(r"MD[EFIPQRST]\d{4}", str(s or ""))[:n]
KNOWN_IDS = all_ids()
def kids(lst):
    return [i for i in lst if i in KNOWN_IDS]

# ---------------------------------------------------------------- 16 METR's FY2024 Form 990 (audit C)
def fig16():
    Cj = audit("C-metr-own-filings")
    def find(prefix):
        for l in Cj["fy2024_return"]["lines"]:
            if l["line"].startswith(prefix): return l
        return {}
    contrib = find("Part I line 8"); rel = find("Part VIII line 1d"); other = find("Part VIII line 1f"); inv = find("Part VIII line 3"); rev = find("Part I line 12"); exp = find("Part I line 18"); net = find("Part I line 19"); bal = find("Part I line 22"); schb = find("Schedule B"); schd = find("Schedule D"); schr = find("Schedule R"); gov = find("Part VIII line 1e"); prog = find("Part VIII line 2g"); per = find("Fiscal period"); vi = find("Part VI governance"); schi = find("Schedule I")
    W = 1200; s = svg_open(W, 250)
    tot = 13639155; x0 = 40; x1 = W - 40; scale = (x1 - x0) / tot
    s += text(x0, 24, "Total revenue as filed, FY2024 (2024-05-01 to 2024-12-31): $13,639,155", 13, weight="bold")
    x = x0
    for lab, v, col, ink in (("from ARC (related organisation)", 4501424, C["transfer"], "#fff"), ("all other contributions: payers not named on the public return", 9101611, C["unknown"], C["ink"]), ("investment income", 36120, C["ctx"], "#fff")):
        w = v * scale; s += rect(x, 36, w, 44, col)
        if w > 160: s += text(x + w / 2, 62, f"{lab}: ${v:,}", 12, ink, "middle", "bold")
        x += w
    s += text(x0, 100, "program-service revenue $0; government grants: no line reported; grants paid by METR: none", 11, C["mute"])
    s += text(x0, 134, "Total expenses as filed: $8,234,524 (program services $6,924,735; management and general $1,144,255; fundraising $165,534)", 13, weight="bold")
    x = x0
    for lab, v, col in (("program services", 6924735, C["known"]), ("management and general", 1144255, C["known2"]), ("fundraising", 165534, "#7fa895")):
        w = v * scale; s += rect(x, 146, w, 36, col)
        if w > 150: s += text(x + w / 2, 169, f"{lab}: ${v:,}", 12, "#fff", "middle", "bold")
        x += w
    s += rect(x, 146, (tot - 8234524) * scale, 36, "#e4e0d5") + text(x + (tot - 8234524) * scale / 2, 169, "revenue less expenses: $5,404,631 (net assets at year end)", 12, C["ink"], "middle", "bold")
    s += text(x0, 210, "Schedule B on the public copy: every contributor name and amount reads RESTRICTED. The audited statements (not attached) recognise $441,350 of donated services and use of facilities.", 11, C["mute"])
    s += text(x0, 230, "One money type on this figure: amounts as filed on the recipient's return. Nothing here is a commitment, a recommendation or a funder-side grant.", 11, C["mute"])
    s += "</svg>"
    lines = [("Fiscal period", per), ("Contributions and grants (Part VIII 1h)", contrib), ("from related organisation, Alignment Research Center (1d)", rel), ("all other contributions (1f)", other), ("government grants (1e)", gov), ("program-service revenue (2g)", prog), ("investment income (3)", inv), ("total revenue (12)", rev), ("total expenses (18)", exp), ("revenue less expenses (19)", net), ("net assets and balance sheet (22)", bal), ("Schedule B public copy", schb), ("Schedule D reconciliation to audited statements", schd), ("Schedule R related organisations", schr), ("Schedule I grants paid", schi), ("Part VI governance checkboxes", vi)]
    trow = [[esc(lab), esc(scrub(l.get("amount", ""))[:260]), ids(kids(rid_list(l.get("row_id", ""), 4)))] for lab, l in lines if l]
    body = unknown_block([
        ("Who paid the $9,101,611 of 'all other contributions' is not on the public return; Schedule B identities and amounts are withheld by law on the public-inspection copy.", kids(rid_list(schb.get("row_id", "")) + rid_list(other.get("row_id", ""), 2))),
        ("No FY2025 return exists yet; this is METR's only filed year and it is an eight-month initial period, so it cannot be compared to a calendar-year budget without a bridge METR has not published.", find_ids("FY2025 Form 990|no 2025 annual report|index_2026", (MDS, MDP), 3)),
        ("The audited financial statements exist (the return says so) but are not public; METR says they are available on request. Nothing has been requested.", kids(rid_list(schd.get("row_id", "")))),
        ("Whether any donor restriction applies to the year-end net assets is not reported on the return.", find_ids("restricted-fund|DonorRstr", (MDP, MDF), 2)),
    ])
    body += '<div class="kpis">' + kpi("total revenue, as filed", "$13,639,155", "eight-month initial year, 2024-05-01 to 2024-12-31", kids(rid_list(rev.get("row_id", ""), 2))) + kpi("from Alignment Research Center", "$4,501,424", "related-organisation contribution; ARC's own return shows $4,477,169 cash plus $76,766 non-cash", kids(rid_list(rel.get("row_id", ""), 2) + ["MDF0064", "MDF0065"])) + kpi("all other contributions", "$9,101,611", "payers not named on the public return", kids(rid_list(other.get("row_id", ""), 2))) + kpi("net assets at year end", "$5,404,631", "revenue less expenses; no prior year", kids(rid_list(net.get("row_id", ""), 2))) + "</div>"
    body += s + '<h2 class="sec">Lines as filed (IRS e-file XML, object 202523209349300367)</h2>' + table(["line", "as filed", "rows"], trow)
    body += '<h2 class="sec">A second copy and the registration record (California Attorney General registry, MD73)</h2>' + table(["document", "what it adds", "rows"], [
        ["METR registration CT0293073", "registered 2024-06-18; fiscal year end 12/31; home jurisdiction Delaware; Secretary of State entity 6138567", ids(kids(["MDE0151", "MDE0152"]))],
        ["CT-1 initial registration (47 pages, articles and bylaws)", "assets first received 2024-03-11; exemption letter 2024-03-14; 'previously operated as ARC Evals under fiscal sponsorship' by ARC", ids(kids(["MDP0754", "MDT0438", "MDR0209"]))],
        ["2024 renewal packet (RRF-1 plus Form 990 copy)", "the same revenue, contributions, related-organisation and net-asset figures as the e-file; RRF-1 confirms an independent audit exists; the audit report is not published", ids(kids(["MDP0755", "MDF1033", "MDF1037", "MDP0759"]))]])
    return page("metr-deep-16-metr-fy2024-return", "What does METR's only filed Form 990 say about its money, and what does it leave unnamed?",
                "METR's FY2024 Form 990: $13.6M of revenue, two-thirds of it from payers the public copy does not name",
                "Recipient-side figures only; one money type; the ARC transfer is the only identified payer.", body)

# ---------------------------------------------------------------- 17 METR's own money statements, by type (audit C)
def fig17():
    Cj = audit("C-metr-own-filings")
    names = ["Commitments METR has announced (type: commitment)", "Budgets, run-rate, goals and runway (spend-side figures, not income)", "In-kind estimates METR has published (type: in-kind estimate)", "Rules and acknowledgements (no amount)"]
    groups = {n: [] for n in names}
    for st in Cj["statements"]:
        mt = (st.get("money_type") or ""); amt = str(st.get("amount_or_range") or ""); q = scrub(st.get("quote") or ""); rid = kids(rid_list(st.get("row_id", ""), 3))
        row = [esc(scrub(st.get("date", ""))[:40]), esc(scrub(st.get("speaker_or_document", ""))[:70]), esc(scrub(amt)[:60]), esc(q[:170]), ids(rid)]
        if any(k in mt for k in ("run-rate", "runway", "budget", "fundraising", "goal")): groups[names[1]].append(row)
        elif "in_kind" in mt: groups[names[2]].append(row)
        elif mt.startswith("commitment"): groups[names[0]].append(row)
        else: groups[names[3]].append(row)
    W = 1200; s = svg_open(W, 250)
    panels = [("commitment statements", [("2024-10-09 joint Canary commitment to RAND and METR", 38_000_000, "MDF0165"), ("2024-10-09 METR share of Canary", 17_000_000, "MDF0166"), ("2025-09-28 restated: a bit under $16m over 3 years", 16_000_000, "MDF0169"), ("2026-08-14 commitments raised in the last 6 months", 71_000_000, "MDF0089")], C["commitment"]),
              ("spend-side figures (budget, run-rate, goal)", [("2024 budget (annual report)", 10_000_000, "MDP0057"), ("2025 raise-and-deploy target (annual report)", 15_000_000, "MDP0058"), ("run-rate ~$13M per year (2025-09-28)", 13_000_000, "MDF0465"), ("fundraising goal by end-2025", 10_000_000, "MDP0060")], C["ctx"]),
              ("in-kind estimates (single events)", [("~$400K API credits, six-day investigation (2026-08-26)", 400_000, "MDI0047"), ("~$600,000 valuation of stolen credits (2026-08-31)", 600_000, "MDI0043"), ("$441,350 donated services per audited statements (FY2024)", 441_350, "MDP0273")], C["in_kind_estimate"])]
    y = 10
    for title, items, col in panels:
        s += text(0, y + 12, title + "  (own axis; not comparable with the other panels)", 12, C["mute"], weight="bold"); y += 18
        mx = max(v for _, v, _ in items)
        for lab, v, rid in items:
            w = 620 * v / mx; s += rect(420, y + 2, w, 12, col) + text(412, y + 12, lab, 11, anchor="end") + text(420 + w + 6, y + 12, f"${v:,} ({rid})", 10, C["mute"]); y += 17
        y += 10
    s += "</svg>"
    body = unknown_block([
        ("The $71M is a statement of commitments; whether any of it has been paid, and whether in-kind support is inside it, is not stated.", kids(["MDF0089", "MDP0527", "MDP0529"])),
        ("The ~$17M (2024) and 'a bit under $16m' (2025) are two dated statements of the same Canary share; they are shown side by side and never replaced or added.", kids(["MDF0166", "MDF0169"])),
        ("Budget, run-rate and goal figures describe spending or aims, not money received; they sit on their own axis and are never summed with commitments or filed revenue.", kids(["MDF0465", "MDP0057", "MDP0060"])),
        ("Free tokens and compute are unquantified in every METR statement except two single-event estimates.", kids(["MDI0047", "MDI0043", "MDS0719"])),
    ])
    body += s
    for g, rows in groups.items():
        if rows: body += f'<h2 class="sec">{esc(g)}</h2>' + table(["date", "document", "amount or range", "quote", "rows"], rows)
    return page("metr-deep-17-metr-own-statements", "What has METR itself said about its money, and of what type is each figure?",
                "METR in its own words: every published money figure, typed and dated",
                "Commitments, spend-side figures and in-kind estimates on separate axes.", body)

# ---------------------------------------------------------------- 18 public-sector contracts card (audit D)
def fig18():
    Dj = audit("D-contracts-inkind-access")
    cols = ""
    for c in Dj["contracts"]:
        negs = "".join("<li>" + esc(scrub(n)[:200]) + "</li>" for n in c.get("negatives", [])[:6])
        cols += ('<div class="layer"><h3>' + esc(scrub(c.get("award", ""))[:140]) + '</h3>'
                 + '<p><b>Authority:</b> ' + esc(scrub(c.get("authority", ""))[:160]) + '</p>'
                 + '<p><b>Legal recipient:</b> ' + esc(scrub(c.get("recipient", ""))[:220]) + '</p>'
                 + '<p><b>Value:</b> ' + esc(str(c.get("value", ""))[:120]) + ' ' + esc(c.get("currency", "") or "") + '</p>'
                 + '<p><b>Period:</b> ' + esc(str(c.get("period", ""))[:160]) + '</p>'
                 + '<p><b>METR share:</b> <span class="tag u">' + esc(str(c.get("metr_share", ""))[:120]) + '</span></p>'
                 + '<p><b>Checked and not found:</b></p><ul style="margin:0;padding-left:16px;font-size:12.5px">' + negs + '</ul>'
                 + '<p>' + ids(kids(rid_list(c.get("row_ids", ""), 8))) + '</p></div>')
    body = unknown_block([
        ("METR's share of the EUR 1,167,484 European AI Office lot is not disclosed anywhere public; the consortium is led by EquiStamp, and one third is not an inference this pack makes.", kids(["MDF0150", "MDF0151", "MDP0132"])),
        ("No UK contract, notice, amount or instrument naming METR exists in Contracts Finder, Find a Tender or DSIT spend data; 'partnering with the AI Security Institute' rests on METR's own page.", kids(["MDP0050", "MDP0197", "MDS0523"])),
        ("The NIST consortium membership and the CAISI CRADA slide carry no award value; USAspending, SAM and grants.gov return nothing for METR, bounded by the absence of a recovered unique entity id.", kids(["MDI0003", "MDS0452", "MDS0456"])),
        ("EUR is never converted; a euro contract value is not a dollar amount and is not added to any donation figure.", kids(["MDF0150"])),
    ])
    body += '<div class="layers">' + cols + "</div>"
    body += '<p class="note">Three drafts (UK FOI, US FOIA, EU access-to-documents) exist for these records and are unsent, awaiting a decision. ' + ids(find_ids("USER_AUTHORITY_WAIT", (MDS,), 3)) + '</p>'
    return page("metr-deep-18-public-sector-contracts", "What do public procurement records show about METR's government and consortium work, and what is undisclosed?",
                "Three public-sector relationships: one euro contract with an undisclosed share, one undocumented partnership, one unfunded consortium seat",
                "Award ids, authorities and values as published; every gap named.", body)

# ---------------------------------------------------------------- 19 in-kind ledger (audit D)
def fig19():
    Dj = audit("D-contracts-inkind-access")
    rows = []; nq = nu = 0
    for k in Dj["in_kind"]:
        q = str(k.get("quantity_or_value", "")); quant = bool(re.search(r"\$\s?\d|\d{3},\d{3}|~\$", q))
        if quant: tag = '<span class="tag k">quantified</span>'; nq += 1
        elif "undisclosed" in q.lower(): tag = '<span class="tag n">undisclosed</span>'; nu += 1
        else: tag = '<span class="tag u">unquantified</span>'; nu += 1
        rows.append([esc(scrub(k.get("provider", ""))[:40]), esc(scrub(k.get("project", ""))[:60]), esc(scrub(k.get("type", ""))[:50]), tag + " " + esc(scrub(q)[:110]), esc(str(k.get("date", ""))[:24]), ids(kids(rid_list(k.get("row_id", ""), 3)))])
    from collections import Counter
    prov = Counter(scrub(k.get("provider", "")).split(";")[0].split("(")[0].strip()[:28] for k in Dj["in_kind"])
    W = 1200; s = svg_open(W, 30 + 22 * len(prov)); mx = max(prov.values())
    for i, (pname, n) in enumerate(prov.most_common()):
        y = 10 + 22 * i; s += text(300, y + 14, pname, 11, anchor="end") + rect(310, y + 3, 600 * n / mx, 14, C["in_kind_estimate"]) + text(316 + 600 * n / mx, y + 14, str(n), 10, C["mute"])
    s += "</svg>"
    body = unknown_block([
        ("Only two dollar figures for in-kind support exist in the whole record, both METR's own single-event estimates; no lab-by-lab or annual token or credit total is published by anyone.", kids(["MDI0047", "MDI0043"])),
        ("Every per-model access arrangement (checkpoints, reasoning traces, transcripts) is documented as access, not as a valued gift; none carries a quantity of tokens or a dollar value.", kids(["MDI0012", "MDI0020", "MDI0019"])),
        ("Several acknowledgement rows run the other way: labs crediting METR for help with their safety frameworks. They are not support to METR.", kids(["MDI0044", "MDI0061", "MDI0062"])),
        ("Whether any in-kind support is counted inside the $71M commitment statement is not stated.", kids(["MDI0119"])),
    ])
    body += '<div class="kpis">' + kpi("in-kind rows audited", str(len(Dj["in_kind"])), "provider, project, type and quantity from the promoted tables") + kpi("quantified", str(nq), "a dollar or token figure stated by a source") + kpi("unquantified or undisclosed", str(nu), "access or credits acknowledged without a figure") + "</div>"
    body += '<h2 class="sec">In-kind rows per provider</h2>' + s
    body += '<h2 class="sec">Ledger</h2>' + table(["provider", "project", "kind", "quantity or value", "date", "rows"], rows)
    return page("metr-deep-19-in-kind-ledger", "What tokens, credits, compute and access have labs provided to METR, and what is it worth?",
                "In-kind support: thirty-nine documented arrangements, two dollar figures",
                "Free tokens, credits and model access by provider and project; quantified only where a source gives a number.", body)

# ---------------------------------------------------------------- 20 project terms grid (audit D)
def fig20():
    Dj = audit("D-contracts-inkind-access")
    cells = ["compensation", "access", "safe_harbor", "publication_redaction", "exit", "policy_in_force", "staff_conflict_disclosure"]
    labels = ["compensation", "access", "safe harbor", "publication / redaction", "exit", "policy in force", "staff conflict disclosure"]
    def state(v):
        v = str(v or "").lower()
        if v.startswith("documented absence") or "documented: none in force" in v or v.startswith("documented: no applicable"): return "absence"
        if v.startswith("documented") or v.startswith("partly documented") or v.startswith("coi policy v1.0"): return "documented"
        if v.startswith("n/a"): return "na"
        return "undisclosed"
    col = {"documented": C["known"], "absence": C["neg"], "undisclosed": C["unknown"], "na": "#e4e0d5"}
    projs = sorted(Dj["projects"], key=lambda p: str(p.get("date", "")))
    lw = 420; cw = 100; W = lw + cw * len(cells) + 20; rh = 30; H = 90 + rh * len(projs)
    s = svg_open(W, H)
    for j, l in enumerate(labels): s += '<text x="%d" y="70" font-size="11" transform="rotate(-30 %d,70)">%s</text>' % (lw + cw * j + 8, lw + cw * j + 8, esc(l))
    counts = {"documented": 0, "absence": 0, "undisclosed": 0, "na": 0}
    for i, p in enumerate(projs):
        y = 80 + rh * i
        s += text(lw - 8, y + 19, f"{str(p.get('date',''))[:10]}  {scrub(p.get('project',''))[:44]}", 11, anchor="end")
        for j, c in enumerate(cells):
            st = state((p.get("cells") or {}).get(c)); counts[st] += 1
            s += rect(lw + cw * j + 3, y + 4, cw - 6, rh - 8, col[st], 'rx="3"')
    s += "</svg>"
    trow = [[esc(str(p.get("date", ""))[:12]), esc(scrub(p.get("project", ""))[:70]), esc(scrub(p.get("provider", ""))[:26]), esc(", ".join(scrub(u)[:40] for u in (p.get("undisclosed_cells") or [])[:7])), ids(kids(rid_list(p.get("row_ids", ""), 4)))] for p in projs]
    body = unknown_block([
        ("No signed engagement instrument is published for any project; every cell marked undisclosed is undisclosed in the documents checked, which are named on the rows.", kids(["MDS0620", "MDS0631", "MDS0610"])),
        ("Compensation is stated in only two engagements (the Frontier Risk Report and the Hugging Face investigation: none received); for the others it is neither confirmed nor denied by the engagement documents.", kids(["MDQ0051", "MDQ0102", "MDQ0103"])),
        ("A legal safe harbor was never granted in any documented engagement; the one place it is addressed says 'not requested'.", kids(["MDQ0002"])),
        ("The 2026-09-09 Anthropic engagement discloses access but not compensation, redaction authority, publication rights or exit terms.", kids(["MDP0245", "MDP0246", "MDS0610"])),
    ])
    body += '<div class="kpis">' + "".join(kpi(k, str(v), d) for k, v, d in (("cells documented", counts["documented"], "a term stated in a project document"), ("documented absence", counts["absence"], "the document states the term did not exist or apply"), ("cells undisclosed", counts["undisclosed"], "not stated in any checked document"), ("not applicable", counts["na"], "no model access involved"))) + "</div>"
    body += legend([("documented", C["known"]), ("documented absence (e.g. no policy in force)", C["neg"]), ("undisclosed in checked documents", C["unknown"]), ("not applicable", "#e4e0d5")]) + s
    body += '<h2 class="sec">Projects and their undisclosed cells</h2>' + table(["date", "project", "provider", "undisclosed", "rows"], trow)
    return page("metr-deep-20-project-terms-grid", "For each METR engagement with a lab, which terms are documented, which are documented as absent, and which are undisclosed?",
                "Twenty engagements, seven terms each: most cells are undisclosed",
                "Compensation, access, safe harbor, publication and redaction, exit, policy in force and staff conflict disclosure, per project.", body)

BUILDERS.update({"16": fig16, "17": fig17, "18": fig18, "19": fig19, "20": fig20})

# ---------------------------------------------------------------- 21 supporter ledger by money type (audit A)
MT_ORDER = ["commitment", "paid_grant", "filed_grant", "transfer", "recommendation", "regrant", "contract", "in_kind_estimate"]
MT_LABEL = {"commitment": "commitment", "paid_grant": "paid (donor ledger)", "filed_grant": "filed grant (funder return)", "transfer": "transfer", "recommendation": "recommendation", "regrant": "regrant", "contract": "contract", "in_kind_estimate": "in-kind estimate"}
def amt_num(a):
    m = re.match(r"^\s*(?:USD|EUR)?\s*\$?\s*(\d[\d,]*)(\.\d+)?\s*(?:USD|EUR)?\s*$", str(a or ""))
    return float(m.group(1).replace(",", "") + (m.group(2) or "")) if m else None
def to_metr(f):
    to = str(f.get("to", ""))
    if re.search(r"not (a )?METR|METR not|Pew Research|unnamed DAF|to RAND", to, re.I): return False
    return bool(re.search(r"\bMETR\b|Model Evaluation|ARC Evals", to)) and str(f.get("row_id", "")).startswith(("MDF", "MDP"))
def fig21():
    A = audit("A-named-supporters")
    groups = [("Named by METR on metr.org/about", A["supporters"]), ("Filed or self-reported payers METR does not name", [p for p in A.get("payers_not_named_by_metr", []) if "own filed" not in p.get("name", "")])]
    rows = []; newcount = 0; cells_total = 0
    for gname, sps in groups:
        rows.append([f'<b>{esc(gname)}</b>'] + [""] * (len(MT_ORDER) + 1))
        for sp in sps:
            cell = {m: [] for m in MT_ORDER}; seen = set()
            facts = sorted(sp.get("facts", []), key=lambda f: 0 if str(f.get("strength", "")).startswith("primary") else 1)
            for f in facts:
                mt = f.get("money_type") or ""; a = f.get("amount")
                if not a or mt not in cell or not to_metr(f): continue
                key = (mt, str(a).replace(",", ""), f.get("currency"))
                if key in seen: continue
                seen.add(key)
                if f.get("new_vs_seed"): newcount += 1
                cur = f.get("currency") or "USD"; av = amt_num(a)
                txt = (f"{av:,.0f} {cur}" if av and "undisclosed" not in str(a) else esc(str(a)[:30])) + f" ({str(f.get('date',''))[:10]})" + ('<span class="tag k" style="margin-left:4px">new</span>' if f.get("new_vs_seed") else "")
                cell[mt].append(txt + " " + ids([f["row_id"]]))
            cells_total += sum(1 for m in MT_ORDER if cell[m])
            status = sp.get("status", "")
            tag = '<span class="tag k">amount identified</span>' if status.startswith("public amount") or "identified" in status else '<span class="tag u">acknowledged, no public amount</span>'
            rows.append([esc(sp.get("name", "")[:52]) + "<br>" + tag] + ["<br>".join(cell[m][:3]) or '<span class="muted">—</span>' for m in MT_ORDER] + [str(len(sp.get("negatives", [])))])
    body = unknown_block([
        ("Each column is one money type; a cell in one column is never added to a cell in another, and a supporter with amounts in two columns has two facts, not a total.", kids(["MDF0047", "MDF0053", "MDF0058"])),
        ("'Acknowledged, no public amount' is a bounded negative over the sources listed in the negatives column, not a finding that nothing was given.", kids(["MDP0054", "MDS0124", "MDS0060"])),
        ("The Canary share is one commitment with three dated statements (~$38M joint, ~$17M, 'a bit under $16m'); no filing shows a payment to METR.", kids(["MDF0167", "MDF0166", "MDF0169", "MDS0432"])),
        ("Donor-advised sponsors' filed grants never name the account principal; Vanguard's $4,000,000 and SVCF's $20,000 have no identified donor.", kids(["MDF0038", "MDF0037", "MDS0594"])),
    ])
    body += '<div class="kpis">' + kpi("supporters and payers", str(sum(len(s) for _, s in groups)), "18 named by METR, 4 filed payers") + kpi("distinct amount facts shown", str(cells_total), "cells with at least one documented amount of that type") + kpi("facts new since the seed", str(newcount), "amount facts that entered through an investigation lane rather than the seed import") + "</div>"
    body += table(["supporter", *[MT_LABEL[m] for m in MT_ORDER], "negatives"], rows, num_cols=(len(MT_ORDER) + 1,))
    return page("metr-deep-21-supporter-ledger-by-type", "For every supporter, what amount of what type is documented, and what came to light since the seed?",
                "Supporter ledger by money type: eight columns that are never added together",
                "Every documented amount per supporter, typed, dated and cited; acknowledgements without amounts shown as such.", body)

# ---------------------------------------------------------------- 22 Audacious / Canary: four propositions (audit B)
def _facts_table(facts, n=8, extra=()):
    seen = set(); rows = []
    for f in facts:
        key = (f.get("money_type"), str(f.get("amount")), f.get("from", "")[:20], f.get("to", "")[:20], str(f.get("date", ""))[:7])
        if key in seen or not (f.get("from") or f.get("to")): continue
        seen.add(key)
        av = amt_num(f.get("amount")); cur = f.get("currency") or ""
        rows.append([esc(str(f.get("date", ""))[:22]), esc(f.get("from", "")[:44]), esc(f.get("to", "")[:36]), esc(MT_LABEL.get(f.get("money_type", ""), f.get("money_type", "")) or "—"), (f"{av:,.0f} {cur}" if av else esc(str(f.get("amount", ""))[:40])), ids([f["row_id"]])])
        if len(rows) >= n: break
    return rows
def fig22():
    B = audit("B-intermediaries-daf"); R = B["routes"][0]; P = R["propositions"]
    W = 1200; s = svg_open(W, 190)
    steps = [("1 Membership", "Audacious is a collective housed at TED; TED does not fund grantees", "documented", P[0]["facts"][0]["row_id"]),
             ("2 Project commitment", "~$38M committed to RAND and METR for Canary, 2024-10-09", "documented as commitment", "MDF0167"),
             ("3 Recipient allocation", "~$17M for METR (METR-quoted), restated 'a bit under $16m' 2025-09-28", "documented, METR-quoted only", "MDF0166"),
             ("4 Payment to METR", "no filed payment to METR in any checked return; filed Canary payments went to RAND", "bounded negative", "MDS0432")]
    for i, (h, d, st, rid) in enumerate(steps):
        x = 20 + i * 295; col = C["known"] if st.startswith("documented") and "negative" not in st else C["neg"]
        s += rect(x, 20, 275, 140, C["bg"], 'rx="10"') + rect(x, 20, 275, 8, col, 'rx="4"')
        s += text(x + 12, 50, h, 13, weight="bold")
        import textwrap
        for k, line_ in enumerate(textwrap.wrap(d, 40)[:4]): s += text(x + 12, 72 + 16 * k, line_, 11)
        s += text(x + 12, 148, st + "  " + rid, 10, col, weight="bold")
        if i < 3: s += text(x + 285, 95, "→", 18, C["mute"], "middle")
    s += "</svg>"
    body = unknown_block([
        ("Whether any Canary money has been paid to METR is not disclosed by METR, TED, RAND or any partner filing checked; the filed Canary-purpose payments found went to RAND (Valhalla $10,000,000; High Tide $333,334).", kids(["MDF0174", "MDF0175", "MDS0432", "MDS0486"])),
        ("RAND never states METR's share; ~$21M for RAND is a subtraction, not a statement.", kids(["MDP0144"])),
        ("Whether the unpaid balance of the three-year Canary commitment sits inside the 2026 '$71M' statement is not stated.", kids(["MDF0169", "MDP0035"])),
        ("Audacious partner names (46 on the 2024 capture, 60 now) are memberships, not gifts to METR.", kids(["MDT0038", "MDP0064"])),
    ])
    body += s
    for pr in P:
        body += f'<h2 class="sec">{esc(pr["proposition"][:150])}</h2>' + f'<p class="note">status: {esc(pr.get("status",""))}; negatives recorded: {len(pr.get("negatives", []))}; settling document: {esc(str(pr.get("settling_document",""))[:200])}</p>'
        rows = _facts_table(pr["facts"], 6)
        if rows: body += table(["date", "from", "to", "type", "amount", "row"], rows)
    return page("metr-deep-22-audacious-canary-four-propositions", "What exactly is documented about the Audacious 'Canary' money, and where does the paper trail stop?",
                "Audacious / Canary: membership, commitment, allocation and payment are four different claims with four different sources",
                "A commitment is not a payment; a joint award is not a METR receipt; a partner list is not a donor list.", body)

# ---------------------------------------------------------------- 23 donor-advised fund layer (audit B)
def fig23():
    B = audit("B-intermediaries-daf"); R = B["routes"][1]; P = R["propositions"]
    sponsors = ["Vanguard Charitable Endowment Program", "Silicon Valley Community Foundation", "Fidelity Investments Charitable Gift Fund", "National Philanthropic Trust", "Donor Advised Charitable Giving Inc"]
    short = {s: s.split(" (")[0].replace(" Endowment Program", "").replace(" Investments Charitable Gift Fund", " Charitable").replace(" Inc", " (Schwab)") for s in sponsors}
    to_metr = {"Vanguard Charitable Endowment Program": ("$4,000,000 filed grant, FY2025 (2024-07-01 to 2025-06-30)", "MDF0038", C["known"]), "Silicon Valley Community Foundation": ("$20,000 filed grant, TY2024", "MDF0037", C["known"]), "Fidelity Investments Charitable Gift Fund": ("none in FY2021 to FY2025", "MDS0170", C["neg"]), "National Philanthropic Trust": ("none in FY2021 to FY2025", "MDS0186", C["neg"]), "Donor Advised Charitable Giving Inc": ("none in FY2020 to FY2025", "MDF0417", C["neg"])}
    W = 1200; s = svg_open(W, 60 + 44 * len(sponsors))
    for i, sp in enumerate(sponsors):
        y = 20 + 44 * i; txt, rid, col = to_metr[sp]
        s += rect(20, y, 330, 34, C["bg"], 'rx="6"') + text(30, y + 22, short[sp], 12, weight="bold")
        s += line(350, y + 17, 470, y + 17, col, 2) + text(410, y + 12, "→ METR", 10, col, "middle")
        s += rect(470, y, 700, 34, "#fff", 'rx="6" stroke="#cdcfc6"') + text(482, y + 22, txt, 12, col) + text(1160, y + 22, rid, 10, "#1b4d3e", "end", extra='font-family="monospace"')
    s += "</svg>"
    flows = B["sponsor_to_sponsor_flows"]
    mat = {}
    for f in flows:
        a = amt_num(f.get("amount_usd"))
        if not a: continue
        k = (f["from_sponsor"], f["to_sponsor"]); mat[k] = max(mat.get(k, 0), a)
    names = sorted({k[0] for k in mat} | {k[1] for k in mat})
    mrows = []
    for a_ in names:
        mrows.append([esc(a_[:40])] + [(money(mat[(a_, b_)]) + " " + ids([next(f["row_id"] for f in flows if f["from_sponsor"] == a_ and f["to_sponsor"] == b_ and amt_num(f.get("amount_usd")) == mat[(a_, b_)])])) if (a_, b_) in mat else '<span class="muted">—</span>' for b_ in names])
    body = unknown_block([
        ("A donor-advised fund sponsor's public return never names the account principal or adviser; the $4,000,000 and $20,000 to METR have no identified donor and none is inferred.", kids(["MDS0594", "MDS0886", "MDS0887"])),
        ("The Vanguard FY2025 line rests on saved page renders; the machine-readable XML for that year was never posted, which is a calendar item, not a doubt about the amount.", kids(["MDP0043", "MDP0600"])),
        ("Sponsor-to-sponsor transfers (largest: SVCF to NPT, $1,591,322,838 in 2024) move money between pools; none of it is METR money and the table below is not a path to METR.", kids(["MDF0240"])),
        ("Whether any of METR's $9,101,611 of unnamed FY2024 contributions came through a sponsor other than SVCF is not disclosed.", kids(["MDF0411", "MDS0011"])),
    ])
    body += '<h2 class="sec">Sponsor filings to METR (Schedule I), every year checked</h2>' + s
    for pr in P[:2]:
        body += f'<p class="note">{esc(pr["proposition"][:220])}</p>' + table(["date", "from", "to", "type", "amount", "row"], _facts_table(pr["facts"], 4))
    body += '<h2 class="sec">Where public verification stops</h2><p class="note">' + esc(P[5]["proposition"][:400]) + ' ' + ids(kids([f["row_id"] for f in P[5]["facts"][:5]])) + '</p>'
    body += '<h2 class="sec">Sponsor-to-sponsor filed grants (largest line per pair; not METR money)</h2>' + table(["from \\ to"] + [esc(n[:26]) for n in names], mrows)
    return page("metr-deep-23-daf-sponsor-layer", "What did donor-advised fund sponsors file as paid to METR, and why does the trail stop there?",
                "The donor-advised layer: two filed grants to METR, three sponsors with none, and a principal no filing names",
                "Sponsor returns for FY2020 to FY2025; sponsor-to-sponsor flows shown separately as not METR money.", body)

# ---------------------------------------------------------------- 24 regrant and recommendation routes, three attestations (audit B)
def fig24():
    B = audit("B-intermediaries-daf"); P = B["routes"][3]["propositions"]
    cols = [("recommendation (a funder's advice)", "recommendation", C["recommendation"]), ("paid (donor's own ledger)", "paid_grant", C["paid_grant"]), ("filed grant (funder return) or regrant", ("filed_grant", "regrant"), C["filed_grant"])]
    routes = [("SFF-2024 round / Jaan Tallinn / Founders Pledge", ["MDF0047", "MDF0051", "MDF0052", "MDF0053", "MDF0058"]), ("SFF-2025 round", ["MDF0045", "MDF0046"]), ("Longview Philanthropy public fund, 2023", ["MDF0070"]), ("Effektiv Spenden Giving Fund, H1 2023", ["MDF0014", "MDF0072"])]
    allf = {f["row_id"]: f for pr in P for f in pr["facts"]}
    trow = []
    for name, rids in routes:
        cells = {0: [], 1: [], 2: []}
        for r in rids:
            f = allf.get(r)
            if not f: continue
            mt = f.get("money_type"); av = amt_num(f.get("amount")); cur = f.get("currency") or "USD"
            txt = (f"{av:,.0f} {cur}" if av else esc(str(f.get("amount") or "amount not on this row"))) + f" ({str(f.get('date',''))[:10]}) " + ids([r])
            j = 0 if mt == "recommendation" else 1 if mt == "paid_grant" else 2
            cells[j].append(txt)
        trow.append([esc(name)] + ["<br>".join(cells[j]) or '<span class="muted">none documented</span>' for j in range(3)])
    W = 1200; s = svg_open(W, 120)
    for i, (lab, _, col) in enumerate(cols):
        x = 20 + i * 390; s += rect(x, 20, 360, 60, col, 'rx="8"') + text(x + 180, 55, lab, 13, "#fff", "middle", "bold")
        if i < 2: s += text(x + 375, 55, "≠", 22, C["mute"], "middle")
    s += text(20, 105, "Three attestations of what may be one flow; none is converted into another and none is summed with another.", 11, C["mute"])
    s += "</svg>"
    body = unknown_block([
        ("The SFF-2025 recommendation ($120,000 plus a conditional $428,000 match) has no paid or filed counterpart yet; a recommendation is advice to a funder, not money received.", kids(["MDF0045", "MDF0046", "MDS0232", "MDS1117"])),
        ("Whether Founders Pledge's TY2024 $184,000 line is the same money as Tallinn's 2024-12-06 $184,000 disbursement is not stated by either document; the amounts match and the rows are kept separate.", kids(["MDF0058", "MDF0053"])),
        ("Longview's $220,000 recommendation went to ARC Evals before METR existed as a legal entity; no filer line for the payment is public.", kids(["MDF0070"])),
        ("Effektiv Spenden's 128,000 EUR is a regrant in euros and is never converted.", kids(["MDF0014", "MDF0072"])),
    ])
    body += s + table(["route", *[c[0] for c in cols]], trow)
    for pr in P[:5]:
        body += f'<h2 class="sec">{esc(pr["proposition"][:140])}</h2>' + table(["date", "from", "to", "type", "amount", "row"], _facts_table(pr["facts"], 5))
    return page("metr-deep-24-regrant-routes-three-attestations", "For the pooled-fund routes, what was recommended, what was paid, and what was filed, and do they line up?",
                "Recommended, paid, filed: three attestations that are never merged",
                "Survival and Flourishing Fund, Jaan Tallinn's ledger, Founders Pledge, Longview and Effektiv Spenden.", body)

# ---------------------------------------------------------------- 25 ARC spin-out and the Coefficient / Open Philanthropy / Good Ventures negatives (audit B)
def fig25():
    B = audit("B-intermediaries-daf"); P = B["routes"][2]["propositions"]
    W = 1200; s = svg_open(W, 200)
    figs = [("ARC FY2024 Schedule I: cash grant", 4477169, "MDF0064"), ("ARC FY2024 Schedule I: non-cash (computers)", 76766, "MDF0065"), ("ARC Schedule N: fair market value of assets distributed", 4553935, "MDT0030"), ("METR FY2024 Part VIII 1d: contribution from related organisation", 4501424, "MDF0034")]
    for i, (lab, v, rid) in enumerate(figs):
        y = 20 + 40 * i; w = 700 * v / 4553935
        s += text(380, y + 18, lab, 11, anchor="end") + rect(390, y + 4, w, 24, C["transfer"] if i != 1 else C["in_kind_estimate"]) + text(400 + w, y + 18, f"${v:,}  {rid}", 11, C["mute"])
    s += text(20, 190, "One event (the 2024-04-30 program spin-off), three filed figures on two returns; the gaps (24,255 and 52,511) are between documents and are not resolved by any public statement.", 11, C["mute"])
    s += "</svg>"
    negs = P[0]
    body = unknown_block([
        ("No grant from Coefficient Giving, Open Philanthropy or Good Ventures Foundation to METR appears in any checked filing (GVF Part XV FY2020 to FY2025), catalog or staff note; that is a bounded negative over those sources.", kids([f["row_id"] for f in negs["facts"][:3]] + [n.get("row_id") for n in negs.get("negatives", [])[:3] if n.get("row_id")])),
        ("The claim that the 2022 Moskovitz-linked awards to ARC were firewalled from METR is undetermined: the document that would settle it is the grant agreement ARC's Schedule I references, which is not public.", kids(["MDP0568", "MDP0016"])),
        ("Why ARC's cash figure and METR's related-organisation figure differ is not stated by either return.", kids(["MDF0064", "MDF0034"])),
        ("Open Philanthropy's 2022 recommendations ($265,000 and $1,250,000) were to Alignment Research Center, a separate 501(c)(3); they are not METR amounts.", kids(["MDP0485", "MDP0486"])),
    ])
    body += '<h2 class="sec">The spin-out transfer: one event, three filed figures</h2>' + s
    body += '<h2 class="sec">What the California registry copies add (MD73)</h2>' + table(["date", "document", "what it says", "rows"], [
        ["2024-05", "ARC Form 990 Schedule O, registry copy", "the evaluations program 'spun off as a separate 501(c)(3) called Model Evaluation and Threat Research'; spin-out completed in May", ids(kids(["MDT0439", "MDP0756"]))],
        ["2024-12-31", "ARC Schedule D, registry copy", "other asset 'INTERCOMPANY RECEIVABLE - METR' $490,179 at year end: an amount owed by METR to ARC, not a grant, not added to the transfer", ids(kids(["MDP0757"]))],
        ["2024-03-11", "METR CT-1 initial registration", "assets first received 2024-03-11; staff and programme 'previously operated as ARC Evals under fiscal sponsorship' by ARC", ids(kids(["MDT0438", "MDR0209", "MDP0754"]))],
        ["FY2024", "ARC and METR renewal packets", "no donor-restriction sentence rides the transfer; no audited statements are published by the registry for either organisation", ids(kids(find_ids("Donor-restriction sentence on the ARC|audited financial statement as a registry document class", (MDS,), 3)))]])
    for pr in P:
        body += f'<h2 class="sec">{esc(pr["proposition"][:150])}</h2><p class="note">status: {esc(pr.get("status",""))}; settling document: {esc(str(pr.get("settling_document",""))[:220])}</p>'
        rows = _facts_table(pr["facts"], 6)
        if rows: body += table(["date", "from", "to", "type", "amount", "row"], rows)
    return page("metr-deep-25-arc-spinout-and-coefficient-negatives", "What passed from ARC to METR at the spin-out, and what do the Coefficient, Open Philanthropy and Good Ventures filings show about METR?",
                "The ARC spin-out on paper, and the bounded negatives for Coefficient, Open Philanthropy and Good Ventures",
                "Two returns, three figures, one event; and six years of grant schedules with no METR line.", body)

BUILDERS.update({"21": fig21, "22": fig22, "23": fig23, "24": fig24, "25": fig25})

# ---------------------------------------------------------------- 26 the donated stake: statements, vehicles, Schedule B (audit E)
def fig26():
    E = audit("E-stake-and-anthropic-ties")
    import datetime as dt
    d0 = dt.date(2021, 1, 1); d1 = dt.date(2027, 6, 30); W = 1200; x0, x1 = 40, W - 40
    def X(s):
        m = re.match(r"(\d{4})-(\d{2})-(\d{2})", str(s)); d = dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3))) if m else None
        return x0 + (x1 - x0) * ((d - d0).days / (d1 - d0).days) if d else None
    lanes = [("investment event (issuer statement)", 50, [("2021-05-28", "Anthropic Series A names Moskovitz, Tallinn, Schmidt as participants", "MDR0082", C["ctx"])]),
             ("Good Ventures Foundation Schedule B non-cash receipts (publicly traded securities only), by fiscal year end", 120, [(f"{re.search(r'FY(\d{4})', f['fy']).group(1)}-06-30", f"FY{re.search(r'FY(\d{4})', f['fy']).group(1)} ${int(f['amount']):,}", f["row_id"][:7], C["equity_value"]) for f in E["gvf_schedule_b"] if isinstance(f.get("amount"), (int, float)) and "NonCash" in str(f.get("contributor_label", "")) and re.search(r"FY(\d{4})", f["fy"])]),
             ("statements about the donated stake (press, then own words)", 250, [(st["date"][:10], st["speaker"][:22] + ": " + st["quote"][:60], rid_list(st["row_id"], 1)[0] if rid_list(st["row_id"], 1) else "", C["known"]) for st in E["stake_statements"] if re.match(r"\d{4}-\d{2}-\d{2}", st["date"])]),
             ("documents that could identify the vehicle (future)", 430, [("2026-11-16", "GVF FY2026 Form 990-PF Schedule B/M due (extendable to 2027-05-17)", "MDT0220", C["unknown"])])]
    s = svg_open(W, 500)
    for lab, y, items in lanes:
        s += text(x0, y - 24, lab, 12, weight="bold") + line(x0, y, x1, y, C["grid"])
        crowded = len(items) > 4
        for k, (d, txt, rid, col) in enumerate(items):
            x = X(d)
            if x is None: continue
            s += circle(x, y, 6, col, 'stroke="#191b1a"')
            if crowded: s += line(x, y + 6, x, y + 14 + 12 * k, col, 0.6) + text(x + 4 if x < W * 0.5 else x - 4, y + 18 + 12 * k, f"{d} {txt[:70]} {rid}", 9, C["mute"], "start" if x < W * 0.5 else "end")
            else: s += text(x + 9, y + 4, f"{d} {txt[:58]} {rid}", 9, C["ink"])
    for yr in range(2021, 2028):
        x = X(f"{yr}-01-01"); s += line(x, 470, x, 476) + text(x, 490, str(yr), 10, C["mute"], "middle")
    s += "</svg>"
    ex = [[esc(v["vehicle"][:60]), esc(v["excluding_document"][:200]), esc(str(v.get("period", ""))[:40]), ids(kids(rid_list(v.get("row_ids", ""), 4)))] for v in E["vehicles"]["excluded"]]
    po = [[esc(v["vehicle"][:60]), esc(v["identifying_document"][:200]), esc(str(v.get("expected_date", ""))[:40]), ids(kids(rid_list(v.get("row_ids", ""), 4)))] for v in E["vehicles"]["possible"]]
    st = [[esc(x["date"][:24]), esc(x["speaker"][:30]), esc(x["venue"][:34]), esc(x["quote"][:150]), esc(str(x.get("does_not_say", ""))[:150]), ids(kids(rid_list(x["row_id"], 2)))] for x in E["stake_statements"]]
    gb = [[esc(g["fy"][:36]), esc(g["contributor_label"][:60]), (f"${int(g['amount']):,}" if isinstance(g.get("amount"), (int, float)) else esc(str(g.get("amount") or "—"))), esc(str(g["money_type"])[:40]), ids(kids(rid_list(g["row_id"], 2)))] for g in E["gvf_schedule_b"]]
    body = unknown_block([
        ("No statement names the vehicle as a legal entity, a share class, an amount or a transfer date; 'our foundation' and 'a nonprofit vehicle' are the speakers' words.", kids(["MDP0699", "MDP0700", "MDT0240"])),
        ("Good Ventures Foundation's Schedule B for FY2020 to FY2025 lists only publicly traded securities as non-cash receipts; whether the stake arrived after 2025-06-30 is answered only by the FY2026 return, due 2026-11-16.", kids(["MDF0333", "MDT0220"])),
        ("Equity values on this figure are fair-market values of contributed securities in the foundation's own returns; they are never added to any money flow and say nothing about METR.", kids(["MDF0325", "MDF0331"])),
        ("No transaction from any candidate vehicle into METR appears in any checked filing; the only donor-advised lines to METR (Vanguard $4,000,000; SVCF $20,000) have no identified principal.", kids(["MDS1011", "MDF0038", "MDF0037"])),
    ])
    body += s
    body += '<h2 class="sec">Every dated statement about the stake, and what it does not say</h2>' + table(["date", "speaker", "venue", "quote", "does not say", "rows"], st)
    body += '<div class="two"><div><h2 class="sec">Vehicles excluded by a document</h2>' + table(["vehicle", "excluding document", "period", "rows"], ex) + '</div><div><h2 class="sec">Vehicles still possible, and the document that would identify each</h2>' + table(["vehicle", "identifying document", "expected", "rows"], po) + '</div></div>'
    body += '<h2 class="sec">Good Ventures Foundation Schedule B, FY2020 to FY2025 (equity values, one type, never summed)</h2>' + table(["fiscal year", "contributor line", "amount", "type", "rows"], gb, num_cols=(2,))
    return page("metr-deep-26-donated-stake-statements-and-vehicles", "What has been said about the donated Anthropic stake, which vehicles are excluded, and what document would identify the rest?",
                "The donated stake: eleven statements, six exclusions, five open vehicles, no transaction into METR",
                "Statement dates are not transfer dates; equity values are not money flows.", body)

# ---------------------------------------------------------------- 27 supporter links to Anthropic (audit E)
def fig27():
    E = audit("E-stake-and-anthropic-ties")
    rows = []
    for l in E["supporter_anthropic_links"]:
        lt = l.get("link_type", ""); neg = lt.lower().startswith("no anthropic") or lt.lower().startswith("bounded negative")
        tag = '<span class="tag n">none found</span>' if neg else ('<span class="tag k">issuer or court document</span>' if str(l.get("strength", "")).startswith("primary") else '<span class="tag c">' + esc(str(l.get("strength", ""))[:24]) + '</span>')
        rows.append([esc(l["supporter"][:60]), esc(l["person_or_entity_named"][:60]), tag + " " + esc(lt[:170]), esc(str(l.get("date_of_investment_event", ""))[:40]), esc(str(l.get("date_of_donation_event", ""))[:90]), ids(kids(rid_list(l.get("row_ids", ""), 4)))])
    W = 1200; s = svg_open(W, 120)
    s += rect(20, 20, 520, 70, C["bg"], 'rx="8"') + text(280, 45, "investment event", 13, anchor="middle", weight="bold") + text(280, 68, "who put money into Anthropic, on what date, per the issuer or a court", 11, C["mute"], "middle")
    s += rect(660, 20, 520, 70, C["bg"], 'rx="8"') + text(920, 45, "donation event", 13, anchor="middle", weight="bold") + text(920, 68, "what reached METR, of what type, on what date, per a filing or ledger", 11, C["mute"], "middle")
    s += text(600, 60, "≠", 26, C["neg"], "middle")
    s += "</svg>"
    body = unknown_block([
        ("An Anthropic investment by a person or firm and a gift to METR are two events with two dates and two documents; this figure never joins them into one arrow.", kids(["MDR0082", "MDR0080", "MDR0083"])),
        ("'Individuals from Jane Street' is METR's class label; Jane Street Global Trading's court-documented Anthropic purchase is a firm's position and is not a gift to METR by anyone.", kids(["MDR0083", "MDE0133"])),
        ("Only Moskovitz describes himself as an Anthropic board observer; Tallinn's own words decline a board seat, and 'observer' for him is a newspaper's sentence.", kids(["MDR0089", "MDR0090"])),
        ("For Farhi, Ralston, Field, Newman, Pew, Packard, Sijbrandij and the other foundations, no Anthropic investment or governance role was found on the issuer's pages; that is a bounded negative.", kids(["MDS0776"])),
    ])
    body += s + table(["supporter as METR names it", "person or entity the source names", "link type", "investment event", "donation-side event", "rows"], rows)
    body += '<p class="note">' + esc(E["investment_vs_donation_separation"]["statement"][:400]) + ' ' + ids(kids(rid_list(E["investment_vs_donation_separation"].get("row_ids", ""), 4))) + '</p>'
    return page("metr-deep-27-supporter-anthropic-links", "Which METR supporters have a documented Anthropic investment or governance role, attached to which exact person or entity?",
                "Supporter connections to Anthropic: who the issuer names, and the gift each is separately documented to have made",
                "Investment and donation kept as two dated events; no person is inferred from a firm.", body)

# ---------------------------------------------------------------- 28 entity separation and the edge inventory (audit E)
def fig28():
    E = audit("E-stake-and-anthropic-ties")
    ent = [[esc(e["entity"][:44]), esc(e["identifier"][:200]), esc(e["distinct_from"][:200])] for e in E["entity_separation"]]
    adj = [[esc(a["relationship"][:230]), ids(kids(rid_list(a["row_id"], 3)))] for a in E["adjacency_only"]]
    inv = [("documented transaction", 863, C["known"]), ("role (board seat, employment, observer)", 103, C["ctx"]), ("access arrangement (tokens, model access)", 180, C["in_kind_estimate"]), ("adjacency only (not a money flow)", 153, C["unknown"])]
    W = 1200; s = svg_open(W, 60 + 34 * len(inv)); mx = max(v for _, v, _ in inv)
    s += text(20, 18, "Edge inventory after the entity-edge audit (MD47): every asserted relationship in the pack, typed", 12, weight="bold")
    for i, (lab, v, col) in enumerate(inv):
        y = 40 + 34 * i; w = 700 * v / mx
        s += text(330, y + 18, lab, 11, anchor="end") + rect(340, y + 4, w, 22, col) + text(350 + w, y + 18, str(v), 11, C["mute"])
    s += "</svg>"
    body = unknown_block([
        ("'Our foundation', 'the foundation' and 'a nonprofit vehicle' are never identified as a legal entity in any statement; unmerging them from Good Ventures Foundation, Open Philanthropy and Coefficient is a labelling rule, not a finding about where the stake sits.", kids(["MDE0140"])),
        ("Adjacency edges (a grant to RAND, a board seat, a Jane Street firm position, a lab's tokens) are recorded so that they are not read as money into METR; none of the 153 is a documented transaction.", kids(["MDP0612", "MDP0617", "MDP0621", "MDP0622"])),
        ("The counts are of typed edges in the pack, not of dollars.", kids(["MDP0623", "MDP0624", "MDP0625", "MDP0626"])),
    ])
    body += s
    body += '<h2 class="sec">Legal entities kept distinct, with the identifier that separates each</h2>' + table(["entity", "identifier", "distinct from"], ent)
    body += '<h2 class="sec">Relationships that are adjacency only (labelled not a money flow, C06.E4)</h2>' + table(["relationship as the pack labels it", "rows"], adj)
    return page("metr-deep-28-entity-separation-and-edges", "Which entities are kept apart, by what identifier, and which relationships are adjacency rather than money?",
                "Entity separation: nine entities that are never merged, and 153 relationships that are not money flows",
                "From the entity-edge audit; a connection is recorded as what its document shows and nothing more.", body)

# ---------------------------------------------------------------- 29 master timeline 2021-2026 in swim lanes (audit F)
def fig29():
    F = audit("F-timelines-disclosure")
    import datetime as dt
    cats = [("money", "money events (typed)", C["commitment"]), ("statement", "statements", C["known2"]), ("filing", "filings checked or due", C["ctx"]), ("project", "evaluations and engagements", C["neg"]), ("policy", "policies and rules", "#6b5314"), ("page_version", "page versions and archives", C["unknown"])]
    d0 = dt.date(2021, 1, 1); d1 = dt.date(2027, 1, 1); W = 1200; x0, x1 = 30, W - 30
    def X(s):
        m = re.match(r"(\d{4})-(\d{2})-(\d{2})", str(s))
        if not m:
            m2 = re.match(r"(\d{4})-(\d{2})$", str(s)); m3 = re.match(r"(\d{4})$", str(s))
            d = dt.date(int(m2.group(1)), int(m2.group(2)), 15) if m2 else dt.date(int(m3.group(1)), 7, 1) if m3 else None
        else: d = dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        return (x0 + (x1 - x0) * ((d - d0).days / (d1 - d0).days)) if d and d0 <= d <= d1 else None
    tl = [e for e in F["master_timeline"] if X(e.get("date")) is not None]
    tl += [{"date": "2024-03-11", "category": "filing", "event": "METR CT-1: date assets first received (California registry copy)", "row_id": "MDT0438", "is_page_or_archive_date": False},
           {"date": "2024-06-18", "category": "filing", "event": "METR registered with the California Attorney General (CT0293073)", "row_id": "MDE0152", "is_page_or_archive_date": False},
           {"date": "2021-08-09", "category": "filing", "event": "ARC registered with the California Attorney General (CT0275650)", "row_id": "MDE0154", "is_page_or_archive_date": False},
           {"date": "2024-05-15", "category": "money", "event": "ARC Schedule O: evaluations program spun off as METR, completed in May (registry copy); Schedule D year-end intercompany receivable from METR $490,179", "row_id": "MDT0439", "money_type": "", "amount": "", "is_page_or_archive_date": False}]
    lane_h = 70; H = 40 + lane_h * len(cats) + 40
    s = svg_open(W, H)
    for yr in range(2021, 2028):
        x = X(f"{yr}-01-01")
        if x: s += line(x, 30, x, H - 30, C["grid"]) + text(x + 3, H - 12, str(yr), 10, C["mute"])
    counts = {}
    for li, (key, lab, col) in enumerate(cats):
        y = 40 + lane_h * li
        s += text(x0, y + 12, lab, 12, weight="bold") + line(x0, y + lane_h - 10, x1, y + lane_h - 10, C["grid"])
        ev = [e for e in tl if (e.get("category") == key) or (key == "page_version" and e.get("category") in ("page_version", "archive", "post"))]
        counts[key] = len(ev); slots = {}
        for e in ev:
            x = X(e["date"]); k = int(x // 14); r = slots.get(k, 0); slots[k] = r + 1
            yy = y + 24 + (r % 3) * 12
            hollow = e.get("is_page_or_archive_date")
            s += circle(x, yy, 4, "#fff" if hollow else col, f'stroke="{col}" stroke-width="1.5"')
    s += "</svg>"
    key_events = [e for e in tl if e.get("category") in ("money", "statement", "policy") and (e.get("amount") or e.get("category") == "policy" or "71" in str(e.get("event", "")))]
    key_events.sort(key=lambda e: str(e["date"]))
    trow = [[esc(str(e["date"])[:12]), esc(e["category"]), esc(e["event"][:150]), (esc(MT_LABEL.get(e.get("money_type", ""), e.get("money_type", ""))) + " " + (money(e["amount"], e.get("currency") or "USD") if amt_num(e.get("amount")) else esc(str(e.get("amount") or "")[:30]))).strip(), ('<span class="tag u">page/archive date</span>' if e.get("is_page_or_archive_date") else ""), ids(kids(rid_list(e.get("row_id", ""), 2)))] for e in key_events[:60]]
    body = unknown_block([
        ("Hollow marks are page-appearance or archive dates; they bound when a page changed and never date a gift or a contract.", kids(["MDT0433", "MDT0249"])),
        ("Filings due after 2026-09-16 are shown as future dates; a document that does not exist yet is not a negative.", kids(find_ids("Future document CAL", (MDS,), 2))),
        ("Each money mark keeps its own type; marks in the money lane are never a running total.", kids(["MDF0089", "MDF0020", "MDF0038"])),
    ])
    body += '<div class="kpis">' + "".join(kpi(lab, str(counts.get(key, 0)), "dated events in this lane") for key, lab, _ in cats) + "</div>"
    body += legend([(lab, col) for _, lab, col in cats]) + s
    body += '<h2 class="sec">Money, statement and policy events with their type</h2>' + table(["date", "lane", "event", "type and amount", "", "rows"], trow)
    return page("metr-deep-29-master-timeline-2021-2026", "When did each documented money event, statement, filing, evaluation, policy and page change occur?",
                "Six years in six lanes: 188 dated events, each typed, with page dates kept hollow",
                "Money, statements, filings, projects, policies and page versions from 2021 to the 2026 calendar closers.", body)

# ---------------------------------------------------------------- 30 the Feb-Aug 2026 window (audit F)
def fig30():
    F = audit("F-timelines-disclosure")
    import datetime as dt
    d0 = dt.date(2026, 1, 15); d1 = dt.date(2026, 9, 20); W = 1200; x0, x1 = 40, W - 40
    def X(s):
        m = re.match(r"(\d{4})-(\d{2})-(\d{2})", str(s)); d = dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3))) if m else None
        return (x0 + (x1 - x0) * ((d - d0).days / (d1 - d0).days)) if d and d0 <= d <= d1 else None
    ev = [e for e in F["window_feb_aug_2026"] if X(e.get("date")) is not None]
    colmap = {"money": C["commitment"], "statement": C["known2"], "filing": C["ctx"], "project": C["neg"], "policy": "#6b5314", "page_version": C["unknown"], "archive": C["unknown"], "post": C["unknown"]}
    H = 80 + 22 * len(ev) + 40; s = svg_open(W, H)
    s += rect(X("2026-02-14"), 20, X("2026-08-14") - X("2026-02-14"), H - 70, "#f3ead0", 'opacity="0.5"') + text(X("2026-02-14") + 6, 36, "derived window of 'the last 6 months' (2026-02-14 to 2026-08-14); METR names no months", 11, "#6b5314")
    for m in range(1, 10):
        x = X(f"2026-{m:02d}-01")
        if x: s += line(x, 20, x, H - 50, C["grid"]) + text(x + 3, H - 34, f"2026-{m:02d}", 10, C["mute"])
    for i, e in enumerate(sorted(ev, key=lambda e: str(e["date"]))):
        y = 50 + 22 * i; x = X(e["date"]); col = colmap.get(e.get("category"), C["mute"])
        s += line(x, y + 8, x, y + 8, col) + circle(x, y + 8, 5, "#fff" if e.get("is_page_or_archive_date") else col, f'stroke="{col}" stroke-width="1.5"')
        lab = f"{str(e['date'])[:10]}  {e['event'][:95]}"
        s += text(x + 10 if x < W * 0.55 else x - 10, y + 12, lab, 10, anchor="start" if x < W * 0.55 else "end")
    s += "</svg>"
    trow = [[esc(str(e["date"])[:24]), esc(e.get("category", "")), esc(e["event"][:170]), ('<span class="tag u">page/archive date</span>' if e.get("is_page_or_archive_date") else ""), ids(kids(rid_list(e.get("row_id", ""), 3)))] for e in sorted(ev, key=lambda e: str(e["date"]))]
    body = unknown_block([
        ("Inside the window only one public amount is compatible with the commitment statement: Packard's $350,000, dated by a catalog listing, not by an instrument.", kids(["MDF0020", "MDP0030"])),
        ("Every other dated event in the window is a page change, an evaluation, a policy or a statement; none is a documented commitment to METR.", kids(["MDT0433", "MDQ0177", "MDP0708"])),
        ("The window itself is derived from the post date; METR names no start month.", kids(["MDF0089", "MDT0033"])),
    ])
    body += legend([(k, v) for k, v in (("money", C["commitment"]), ("statement", C["known2"]), ("filing", C["ctx"]), ("project", C["neg"]), ("policy", "#6b5314"), ("page version or archive", C["unknown"]))]) + s + table(["date", "lane", "event", "", "rows"], trow)
    return page("metr-deep-30-six-month-window-2026", "What happened, on the record, during the six months the $71M statement covers?",
                "The six-month window: one compatible amount, and everything else that is dated inside it",
                "February to August 2026, event by event, with page dates kept hollow.", body)

BUILDERS.update({"26": fig26, "27": fig27, "28": fig28, "29": fig29, "30": fig30})

if __name__ == "__main__":
    want = sys.argv[1:] or sorted(BUILDERS)
    for k in want:
        out = BUILDERS[k](); print("WROTE", out.name)
