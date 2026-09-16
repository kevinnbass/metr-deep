#!/usr/bin/env python3
"""Write research/BASELINE.json: the reproducible S0 baseline for the frozen public clone, the
posted-image commit, the seed pack paths this pack imports from, and the sibling plans.

Read-only outside the pack. The public clone is inventoried by git object ids (exact and cheap on a
FUSE mount) plus sha256 of the small text artifacts the plan actually reasons about; the repository
audit is recorded verbatim with its exit code, defects included.

Usage: python3 scripts/build_baseline.py
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT / "repo"
SEED = Path("/mnt/f/projects/memes/ai-machine/10-metr")
POSTED = "f64df65a16400fd88a77536111851695acc9a928"
SIBLINGS = ["toner", "congress", "lineage"]


def utc() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            value.update(chunk)
    return value.hexdigest()


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, text=True, check=True).stdout.strip()


def tree_digest(ref: str) -> dict:
    listing = subprocess.run(["git", "-C", str(REPO), "ls-tree", "-r", "--long", ref],
                             capture_output=True, text=True, check=True).stdout
    return {
        "files": len(listing.splitlines()),
        "ls_tree_sha256": hashlib.sha256(listing.encode()).hexdigest(),
        "bytes": sum(int(line.split()[3]) for line in listing.splitlines() if line.split()[3].isdigit()),
    }


def main() -> int:
    audit = subprocess.run(["python3", "scripts/audit.py"], cwd=REPO, capture_output=True, text=True)
    audit_text = (audit.stdout + audit.stderr).strip()
    head = git("rev-parse", "HEAD")
    status = git("status", "--short")

    figures = sorted((REPO / "figures").glob("*.html"))
    research = sorted((REPO / "research").glob("*.csv"))
    seed_paths = [
        SEED / "HANDOFF.md", SEED / "README.md", SEED / "research/STATE.md", SEED / "research/WATCHLIST.md",
        SEED / "research/NOTES-finance.md", SEED / "research/NOTES-audacious.md", SEED / "research/NOTES-vanguard.md",
        SEED / "research/money_flows.csv", SEED / "research/stakes.csv", SEED / "research/finances.csv",
        SEED / "research/budget.csv", SEED / "research/donor_rule.csv", SEED / "research/audacious-partners.csv",
        SEED / "research/compute_inkind.csv", SEED / "research/board.csv", SEED / "research/aef1.csv",
        SEED / "research/investments.csv", SEED / "research/shared_donors.csv",
    ]

    baseline = {
        "generated_utc": utc(),
        "generator": "scripts/build_baseline.py",
        "pack": "metr_deep",
        "public_clone": {
            "path": str(REPO),
            "remote": git("remote", "get-url", "origin"),
            "head_commit": head,
            "head_commit_utc": git("show", "-s", "--format=%cI", "HEAD"),
            "head_subject": git("show", "-s", "--format=%s", "HEAD"),
            "working_tree_clean": status == "",
            "working_tree_status": status,
            "head_tree": tree_digest("HEAD"),
            "log": [
                {"commit": line.split(" ", 1)[0], "subject": line.split(" ", 1)[1]}
                for line in git("log", "--format=%H %s").splitlines()
            ],
            "small_artifact_sha256": {
                str(path.relative_to(REPO)): sha256(path)
                for path in [REPO / "README.md", REPO / "NOTES.md", REPO / "MANIFEST.csv",
                             REPO / "EVIDENCE.txt", REPO / "EVIDENCE-keyed.txt",
                             REPO / "research/STATE.md", REPO / "research/AUDIT-4.md",
                             REPO / "scripts/audit.py", REPO / "scripts/generate.py"]
                if path.exists()
            },
            "figure_html_sha256": {str(p.relative_to(REPO)): sha256(p) for p in figures},
            "research_csv_sha256": {str(p.relative_to(REPO)): sha256(p) for p in research},
        },
        "posted_image_commit": {
            "commit": POSTED,
            "commit_utc": git("show", "-s", "--format=%cI", POSTED),
            "subject": git("show", "-s", "--format=%s", POSTED),
            "tree": tree_digest(POSTED),
            "figure_png_sha256_at_commit": {},
        },
        "posted_vs_current": {
            "rule": "The image readers saw on 2026-09-14 is fixed at commit f64df65. Later commits may improve the "
                    "current repository but do not alter what was posted. Every claim about 'the figure' names which "
                    "version it refers to.",
            "commits_after_posted": [
                {"commit": line.split(" ", 1)[0], "subject": line.split(" ", 1)[1]}
                for line in git("log", "--format=%H %s", f"{POSTED}..HEAD").splitlines()
            ],
            "files_changed_after_posted": git("diff", "--name-only", POSTED, "HEAD").splitlines(),
        },
        "baseline_audit": {
            "command": "cd repo && python3 scripts/audit.py",
            "run_utc": utc(),
            "exit_code": audit.returncode,
            "stdout_stderr": audit_text,
            "stdout_sha256": hashlib.sha256(audit_text.encode()).hexdigest(),
            "reading": "A failing seed audit is evidence about the seed repository's citation coverage, not about any "
                       "external funding fact. The nine missing RP row ids are all cited by "
                       "figures/metr-13-the-subcontractor.html; the two money figures metr-01 and metr-01b cite no "
                       "missing row id.",
        },
        "seed_pack": {
            "path": str(SEED),
            "note": "Read-only. Facts from here are leads until re-reviewed in this pack; an imported fact gets a new "
                    "MD* id and keeps seed_path and seed_row_id in its note.",
            "sha256": {str(p.relative_to(SEED)): (sha256(p) if p.exists() else None) for p in seed_paths},
        },
        "sibling_plans": {
            name: {
                "plan": f"/mnt/f/projects/anthropic/{name}/PLAN.md",
                "sha256": sha256(Path(f"/mnt/f/projects/anthropic/{name}/PLAN.md")),
            }
            for name in SIBLINGS
            if Path(f"/mnt/f/projects/anthropic/{name}/PLAN.md").exists()
        },
        "plan_sha256": sha256(ROOT / "PLAN.md"),
        "casework_f1_receipt": str(Path("/home/kevin/repos/casework/work/receipts/F1.json")),
        "casework_f1_present": Path("/home/kevin/repos/casework/work/receipts/F1.json").exists(),
    }

    for stem in ("metr-01-money-that-doesnt-show-up", "metr-01b-money-that-doesnt-show-up-with-anthropic"):
        for ext in ("png", "html"):
            name = f"figures/{stem}.{ext}"
            blob = subprocess.run(["git", "-C", str(REPO), "rev-parse", f"{POSTED}:{name}"],
                                  capture_output=True, text=True)
            if blob.returncode:
                continue
            raw = subprocess.run(["git", "-C", str(REPO), "cat-file", "blob", blob.stdout.strip()],
                                 capture_output=True, check=True).stdout
            baseline["posted_image_commit"]["figure_png_sha256_at_commit"][name] = {
                "git_blob": blob.stdout.strip(), "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw),
            }

    out = ROOT / "research/BASELINE.json"
    out.write_text(json.dumps(baseline, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"WROTE {out} audit_exit={audit.returncode} figures={len(figures)} research_csv={len(research)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
