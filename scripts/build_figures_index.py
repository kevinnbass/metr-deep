#!/usr/bin/env python3
"""Write research/FIGURES.md: one line per figures/*.html with its title, the question it answers, and the count of promoted ids it cites."""
import glob, re, pathlib, datetime
ROOT = pathlib.Path(__file__).resolve().parents[1]
out = ["# Figures (metr_deep)", "", f"Rendered {datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')}. Every figure is self-contained HTML under `figures/` with a PNG under `figures/png/`. Each cites promoted row ids, carries an unknown block, keeps money types separate, and passes `scripts/lint_figures.py`. Figures 01-06 are the PLAN.md §8 set (MD53); 07-30 are the second series built by `scripts/build_figures_v2.py` from the promoted tables and the seven figure audits under `research/agents-2026-09-16/figure-audits/`.", "", "| # | file | title | question | ids cited |", "|---|---|---|---|---|"]
for f in sorted(glob.glob(str(ROOT / "figures/*.html"))):
    t = open(f, encoding="utf-8").read(); stem = pathlib.Path(f).stem
    title = re.search(r"<title>(.*?)</title>", t, re.S).group(1).strip()
    q = re.search(r'<p class="sub">(.*?)</p>', t, re.S); q = re.sub(r"<[^>]+>", "", q.group(1)).strip() if q else ""
    q = q.split("?")[0] + "?" if "?" in q else q[:160]
    n = len(set(re.findall(r"\bMD[EFIPQRST]\d{4}\b", t)))
    out.append(f"| {stem.split('-')[2]} | `figures/{stem}.html` | {title} | {q} | {n} |")
(ROOT / "research/FIGURES.md").write_text("\n".join(out) + "\n", encoding="utf-8"); print("FIGURES.md", len(out) - 6, "figures")
