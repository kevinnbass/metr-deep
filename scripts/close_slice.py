#!/usr/bin/env python3
"""Close a slice: run its Verify commands, write the receipt, tick the PLAN.md Status box with an
evidence pointer, append the ledger line, and re-render STATE.md. Refuses unless the slice's checker
is green and every Verify command exits 0. It never edits a Done-when criterion or slice text.

Usage: python3 scripts/close_slice.py S1 --checker scripts/check_s1.py --next S2
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASEWORK = Path("/home/kevin/repos/casework")
VERIFY = {
    "S1": ["python3 /mnt/f/projects/anthropic/tools/lanes.py status --pack metr_deep",
           "python3 -m casework verify --pack metr_deep", "python3 -m casework frontier --pack metr_deep"],
    "S2": ["python3 -m casework verify --pack metr_deep", "python3 -m casework readiness --pack metr_deep --gaps"],
    "S3": ["python3 -m casework verify --pack metr_deep", "python3 -m casework readiness --pack metr_deep --gaps"],
    "S4": ["python3 -m casework verify --pack metr_deep", "python3 -m casework frontier --pack metr_deep"],
    "S5": ["python3 -m casework verify --pack metr_deep", "python3 -m casework readiness --pack metr_deep --gaps",
           "python3 -m casework frontier --pack metr_deep"],
}


def utc() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(cmd: str) -> dict:
    cwd = CASEWORK if cmd.startswith("python3 -m casework") else ROOT
    p = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    out = (p.stdout + p.stderr).strip()
    return {"command": cmd, "cwd": str(cwd), "exit": p.returncode, "output_sha256": hashlib.sha256(out.encode()).hexdigest(),
            "output_head": out[:4000]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("slice")
    ap.add_argument("--checker", required=True)
    ap.add_argument("--next", required=True)
    ap.add_argument("--artifacts", nargs="*", default=[])
    args = ap.parse_args()
    chk = subprocess.run(["python3", args.checker], cwd=ROOT, capture_output=True, text=True)
    print(chk.stdout)
    if chk.returncode:
        print("checker not green; refusing to close")
        return 1
    results = [run(c) for c in VERIFY[args.slice]]
    if any(r["exit"] for r in results):
        print("a Verify command failed; refusing to close")
        for r in results:
            print(r["exit"], r["command"])
        return 1
    arts = ["case.json", "research/LANES.csv", "research/STATE.md", "LEDGER.jsonl", "CHANGELOG.md",
            "research/supporter_coverage.csv"] + args.artifacts
    arts += [str(p.relative_to(ROOT)) for p in sorted((ROOT / "research").glob("*.csv"))]
    arts = list(dict.fromkeys(a for a in arts if (ROOT / a).exists()))
    now = utc()
    receipt = {"slice": args.slice, "verified_utc": now, "checker": args.checker, "checker_output": chk.stdout,
               "verify_commands": results, "artifacts": {a: sha(ROOT / a) for a in arts}}
    rdir = ROOT / f"research/receipts/{args.slice}"
    rdir.mkdir(parents=True, exist_ok=True)
    rpath = rdir / f"{args.slice}-verification.json"
    rpath.write_text(json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    rhash = sha(rpath)
    # ledger
    entry = {"utc": now, "slice": args.slice, "lane": "local", "action": f"{args.slice} verified",
             "command": " && ".join(VERIFY[args.slice]), "exit": 0,
             "artifact_paths": [str(rpath.relative_to(ROOT))] + arts,
             "sha256": {str(rpath.relative_to(ROOT)): rhash, **receipt["artifacts"]},
             "cause": f"{args.checker} green and every Verify command exit 0", "next": f"open {args.next}"}
    with (ROOT / "LEDGER.jsonl").open("a", encoding="utf-8") as s:
        s.write(json.dumps(entry, sort_keys=True, ensure_ascii=False) + "\n")
    lines = (ROOT / "LEDGER.jsonl").read_text("utf-8").splitlines()
    line_no = len(lines)
    # PLAN status
    plan = ROOT / "PLAN.md"
    t = plan.read_text("utf-8")
    pat = re.compile(rf"^- \[ \] {args.slice} (.+?)   ← current$", re.M)
    m = pat.search(t)
    if not m:
        print("PLAN status line for the slice not found in the expected form; ledger and receipt written, PLAN not edited")
        return 1
    t = t[:m.start()] + f"- [x] {args.slice} {m.group(1)}   — evidence: `{rpath.relative_to(ROOT)}` sha256 {rhash}; `LEDGER.jsonl` line {line_no} `{args.slice} verified`" + t[m.end():]
    nxt = re.compile(rf"^(- \[ \] {args.next} .+?)$", re.M)
    t = nxt.sub(lambda mm: mm.group(1) + "   ← current", t, count=1)
    t = re.sub(r"^Last verified: .*$", f"Last verified: {now} by Claude ({args.slice} complete and verified)   (UTC; re-verify on every resume)", t, count=1, flags=re.M)
    t = re.sub(r"^Current slice: .*$", f"Current slice: {args.next}", t, count=1, flags=re.M)
    plan.write_text(t, encoding="utf-8")
    subprocess.run(["python3", "-m", "casework", "state", "--pack", "metr_deep"], cwd=CASEWORK, capture_output=True, text=True)
    print(f"CLOSED {args.slice}: receipt {rpath.relative_to(ROOT)} sha256 {rhash}; ledger line {line_no}; PLAN current slice -> {args.next}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
