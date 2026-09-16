#!/usr/bin/env python3
"""Shared helpers for metr_deep figures (PLAN.md §8 conventions).

Every figure: cites promoted row ids as <span class="id">MDxNNNN</span>, carries an "Unknown / undisclosed" block, keeps
money types separate (never a cross-type total), names only public people in public roles, uses no banned motive word
(casework.json banned_motive_words), and renders as self-contained HTML (inline SVG, no external assets).
"""
import csv, glob, html as _html, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[1]
CFG = json.load(open(ROOT / "casework.json"))
BANNED = CFG.get("banned_motive_words", [])

CSS = """
*{box-sizing:border-box}
html,body{margin:0;background:#f7f4ee;color:#191b1a;font-family:Arial,Helvetica,sans-serif}
body{padding:40px 48px 36px;max-width:1480px}
.kicker{font-size:13px;letter-spacing:2.4px;text-transform:uppercase;color:#5c5f58;font-weight:700}
h1{font-size:30px;letter-spacing:-0.7px;margin:10px 0 12px;line-height:1.18;max-width:1200px}
.sub{font-size:16px;line-height:1.45;color:#3f423c;margin:0 0 20px;max-width:1180px}
.unknown{background:#f3ead0;border:2px solid #c4a35a;border-radius:10px;padding:16px 20px;margin:0 0 22px}
.unknown h2{margin:0 0 8px;font-size:14px;letter-spacing:1.1px;text-transform:uppercase}
.unknown p,.unknown li{font-size:14px;line-height:1.45;margin:0 0 6px}
.kpis{display:flex;gap:14px;flex-wrap:wrap;margin:0 0 20px}
.kpi{background:#efece4;border-radius:10px;padding:14px 18px;min-width:210px;flex:1}
.kpi .l{font-size:12px;color:#5c5f58;letter-spacing:1px;text-transform:uppercase;font-weight:700}
.kpi .v{font-size:26px;font-weight:700;margin-top:4px;letter-spacing:-0.4px}
.kpi .d{font-size:13px;color:#5c5f58;margin-top:4px;line-height:1.35}
table{width:100%;border-collapse:collapse;font-size:13.5px;margin:0 0 18px;background:#f7f4ee}
th,td{border-bottom:1px solid #cdcfc6;text-align:left;padding:8px 10px;vertical-align:top}
th{font-size:11px;letter-spacing:1px;text-transform:uppercase;color:#5c5f58}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
.id{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:12px;color:#1b4d3e}
.muted{color:#5c5f58}
.tag{display:inline-block;font-size:11px;letter-spacing:.6px;text-transform:uppercase;padding:2px 7px;border-radius:5px;background:#e4e0d5;color:#3f423c;margin-right:4px;white-space:nowrap}
.tag.k{background:#d7e6df;color:#1b4d3e}.tag.u{background:#f3ead0;color:#6b5314}.tag.n{background:#e9dcdc;color:#6b2a2a}.tag.c{background:#dfe4ec;color:#2a3d5c}
.layers{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px;margin:0 0 20px}
.layer{background:#efece4;border-radius:10px;padding:14px 16px}
.layer h3{margin:0 0 8px;font-size:14px}
.layer p{margin:0;font-size:13.5px;line-height:1.4}
.two{display:grid;grid-template-columns:1fr 1fr;gap:16px}
h2.sec{font-size:15px;letter-spacing:1.2px;text-transform:uppercase;margin:18px 0 8px}
.foot{margin-top:22px;border-top:1px solid #cdcfc6;padding-top:12px;font-size:13px;line-height:1.5;color:#5c5f58}
.note{font-size:13px;color:#5c5f58;margin:0 0 14px;line-height:1.4}
svg text{font-family:Arial,Helvetica,sans-serif}
.legend{display:flex;gap:16px;flex-wrap:wrap;font-size:13px;margin:6px 0 14px}
.legend span i{display:inline-block;width:14px;height:14px;border-radius:3px;vertical-align:-2px;margin-right:6px}
@media(max-width:900px){.two{grid-template-columns:1fr} body{padding:24px}}
"""

# palette: known/documented, unknown/undisclosed, negative, context, per money type
C = {"known": "#1b4d3e", "known2": "#3d7a63", "unknown": "#c4a35a", "unknownbg": "#f3ead0", "neg": "#8a3b3b", "ctx": "#5b6f8f",
     "grid": "#cdcfc6", "ink": "#191b1a", "mute": "#5c5f58", "bg": "#efece4",
     "commitment": "#1b4d3e", "paid_grant": "#2f6f5a", "filed_grant": "#4f8f78", "transfer": "#7a5c2e", "recommendation": "#8f7a4f",
     "regrant": "#a08a5a", "contract": "#2a3d5c", "in_kind_estimate": "#6b6b6b", "equity_value": "#9a9a9a", "": "#bbb"}

def esc(s): return _html.escape(str(s if s is not None else ""), quote=True)
def ids(*rows):
    out = []
    for r in rows:
        for i in (r if isinstance(r, (list, tuple, set)) else [r]):
            if i and i not in out: out.append(i)
    return " ".join(f'<span class="id">{esc(i)}</span>' for i in out)
def money(v, cur="USD"):
    try: n = float(str(v).replace(",", ""))
    except Exception: return esc(v)
    s = f"{n:,.0f}"
    return ("$" + s) if cur in ("USD", "", None) else f"{s} {cur}"

def load(table):
    rows = list(csv.DictReader(l for l in open(ROOT / f"research/{table}.csv", encoding="utf-8") if not l.startswith("#")))
    return [r for r in rows if "superseded by" not in r.get("note", "")]
def all_ids():
    s = set()
    for t in glob.glob(str(ROOT / "research/*.csv")):
        for r in csv.DictReader(l for l in open(t, encoding="utf-8") if not l.startswith("#")):
            if r.get("row_id"): s.add(r["row_id"])
    return s
def role(r):
    m = re.search(r"role=(\w+)", r.get("note", "") + " " + r.get("review_verdict", "")); return m.group(1) if m else ""
def strength(r):
    m = re.search(r"strength=(\w+)", r.get("note", "") + " " + r.get("review_verdict", "")); return m.group(1) if m else ""
def lane_of(r):
    m = re.search(r"lane=([^#\s]+)", r.get("note", "")); return (m.group(1).split("/")[-1].replace(".csv", "") if m else "seed")

def unknown_block(items):
    """items: list of (text, [ids])"""
    lis = "".join(f"<li>{esc(t)} {ids(i)}</li>" for t, i in items)
    return f'<div class="unknown"><h2>Unknown / undisclosed / not stated / not disclosed</h2><ul style="margin:0;padding-left:18px">{lis}</ul></div>'
def kpi(label, value, desc, idlist=()):
    return f'<div class="kpi"><div class="l">{esc(label)}</div><div class="v">{esc(value)}</div><div class="d">{esc(desc)} {ids(idlist)}</div></div>'
def table(headers, rows, num_cols=()):
    th = "".join(f'<th class="{"num" if i in num_cols else ""}">{esc(h)}</th>' for i, h in enumerate(headers))
    body = ""
    for r in rows:
        body += "<tr>" + "".join(f'<td class="{"num" if i in num_cols else ""}">{c}</td>' for i, c in enumerate(r)) + "</tr>"
    return f"<table><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table>"
def legend(pairs):
    return '<div class="legend">' + "".join(f'<span><i style="background:{c}"></i>{esc(t)}</span>' for t, c in pairs) + "</div>"

def page(stem, question, title, sub, body, foot_extra="", kicker="PLAN.md §8"):
    h = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title><style>{CSS}</style></head><body>
<div class="kicker">{esc(kicker)} · {esc(stem)}</div>
<h1>{esc(title)}</h1>
<p class="sub">{esc(question)} {esc(sub)}</p>
{body}
<div class="foot">Every figure cites promoted row ids from research/*.csv (metr_deep pack). Money types (commitment, paid grant, filed grant, transfer, recommendation, regrant, contract, in-kind estimate, equity value) are never added together. Only public people in public roles are named; no private donor is identified. A page or archive date bounds when a page changed, never when money moved. {foot_extra}</div>
</body></html>"""
    text = re.sub(r"<[^>]+>", " ", h)
    hits = [w for w in BANNED if re.search(r"\b" + re.escape(w) + r"\b", text, re.I)]
    assert not hits, f"{stem}: banned words {hits}"
    known = all_ids(); cited = set(re.findall(r"\bMD[EFIPQRST]\d{4}\b", h)); bad = sorted(cited - known)
    assert cited, f"{stem}: no ids cited"; assert not bad, f"{stem}: unknown ids {bad[:5]}"
    out = ROOT / "figures" / f"{stem}.html"; out.write_text(h, encoding="utf-8"); return out

# ---------------------------------------------------------------- SVG helpers
def svg_open(w, h): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px;display:block;margin:0 0 16px">'
def rect(x, y, w, h, fill, extra=""): return f'<rect x="{x:.1f}" y="{y:.1f}" width="{max(w,0):.1f}" height="{h:.1f}" fill="{fill}" {extra}/>'
def text(x, y, s, size=12, fill=None, anchor="start", weight="normal", extra=""):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill or C["ink"]}" text-anchor="{anchor}" font-weight="{weight}" {extra}>{esc(s)}</text>'
def line(x1, y1, x2, y2, stroke=None, w=1, dash=""):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke or C["grid"]}" stroke-width="{w}" {"stroke-dasharray=\"%s\"" % dash if dash else ""}/>'
def circle(x, y, r, fill, extra=""): return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" {extra}/>'

def hbar_chart(items, width=1200, row_h=30, label_w=340, value_fmt=money, log=False, max_value=None, title=""):
    """items: [(label, value, color, right_label, ids)] one bar per row; values on one scale. Never mix money types here."""
    import math
    n = len(items); h = 30 + n * row_h + 10
    mv = max_value or max((v for _, v, *_ in items if v), default=1)
    x0 = label_w; x1 = width - 250
    s = svg_open(width, h)
    if title: s += text(0, 16, title, 13, C["mute"], weight="bold")
    for i, (label, v, color, right, idl) in enumerate(items):
        y = 30 + i * row_h
        s += text(x0 - 10, y + row_h * 0.62, label, 13, anchor="end")
        if v:
            frac = (math.log10(v) / math.log10(mv)) if log and v > 1 else (v / mv)
            w = max((x1 - x0) * frac, 2)
            s += rect(x0, y + 6, w, row_h - 12, color)
        else:
            s += rect(x0, y + 6, 6, row_h - 12, C["unknown"], 'stroke="#c4a35a" stroke-dasharray="3,2" fill="none"')
        s += text(x1 + 8, y + row_h * 0.62, right, 12, C["mute"])
    s += "</svg>"
    return s
