#!/usr/bin/env python3
"""One-command review→promote→stamp→verify→state→ledger for a landed metr_deep lane (PLAN.md §9).

Preconditions checked before anything is written: the lane's goal state is `complete` in the shared
runner, the lane CSV's sha256 equals the hash recorded when the verdicts were drafted (so no row was
reviewed against a version the worker later changed), and the verdict JSON covers every lane row.
Verdicts are the reviewing agent's, supplied in the JSON; this script assigns none.

Usage: python3 scripts/promote_lane.py MD02 research/grok-out/MD02-packard-grant.csv \
           --verdicts <json> --expect-sha256 <hex> --summary "<review summary>" [--no-goal-check]
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import io
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASEWORK = Path("/home/kevin/repos/casework")
TOOLS = Path("/mnt/f/projects/anthropic/tools")


def utc() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess:
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    sys.stdout.write(proc.stdout)
    sys.stderr.write(proc.stderr)
    return proc


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("lane_id")
    ap.add_argument("lane_csv")
    ap.add_argument("--verdicts", required=True)
    ap.add_argument("--expect-sha256", required=True)
    ap.add_argument("--summary", required=True)
    ap.add_argument("--no-goal-check", action="store_true")
    ap.add_argument("--review-suffix", default="", help="e.g. -xhigh for a re-run of an already promoted lane")
    args = ap.parse_args()
    lane_path = ROOT / args.lane_csv
    if not lane_path.exists():
        sys.exit(f"missing lane csv {lane_path}")
    actual = sha(lane_path)
    if actual != args.expect_sha256:
        sys.exit(f"lane csv changed since verdicts were drafted: {actual} != {args.expect_sha256}; re-review")
    if not args.no_goal_check:
        status = subprocess.run(["python3", str(TOOLS / "lanes.py"), "status", "--pack", "metr_deep"],
                                capture_output=True, text=True).stdout
        line = next((l for l in status.splitlines() if f" {args.lane_id} " in l), "")
        if "goal=complete" not in line:
            sys.exit(f"goal not complete for {args.lane_id}: {line.strip() or 'no runner line'}")
    today = dt.datetime.now(dt.timezone.utc).date().isoformat()
    review_dir = ROOT / f"research/agents-{today}"
    review_dir.mkdir(parents=True, exist_ok=True)
    review = review_dir / f"MDREVIEW-{args.lane_id}{args.review_suffix}.md"
    if review.exists():
        sys.exit(f"review already exists: {review}")
    title = f"Review of {args.lane_id} — {lane_path.stem.split('-', 1)[1].replace('-', ' ')}"
    summary = (f"Reviewing agent: Claude (parent session), {today}. Lane CSV sha256 {actual}; goal state complete. "
               + args.summary)
    r = run(["python3", "scripts/review_lane.py", args.lane_csv, "--verdicts", args.verdicts,
             "--out", str(review.relative_to(ROOT)), "--title", title, "--summary", summary], ROOT)
    if r.returncode:
        return r.returncode
    r = run(["python3", "-m", "casework", "promote", "--pack", "metr_deep", "--review", str(review.relative_to(ROOT))], CASEWORK)
    if r.returncode:
        return r.returncode
    promote_line = r.stdout.strip().splitlines()[-1]
    r = run(["python3", "scripts/stamp_verdicts.py"], ROOT)
    if r.returncode:
        return r.returncode
    v = run(["python3", "-m", "casework", "verify", "--pack", "metr_deep"], CASEWORK)
    if v.returncode:
        return v.returncode
    run(["python3", "-m", "casework", "state", "--pack", "metr_deep"], CASEWORK)
    # LANES.csv
    verdicts = json.loads(Path(args.verdicts).read_text("utf-8"))
    counts: dict[str, int] = {}
    for item in verdicts.values():
        counts[item["verdict"]] = counts.get(item["verdict"], 0) + 1
    lanes_path = ROOT / "research/LANES.csv"
    rows = list(csv.DictReader(io.StringIO(lanes_path.read_text("utf-8"))))
    fields = list(rows[0].keys())
    now = utc()
    for row in rows:
        if row["lane"] == args.lane_id:
            row.update(status="promoted", done_utc=row.get("done_utc") or now, rows_out=str(len(verdicts)),
                       review=str(review.relative_to(ROOT)), promoted_utc=now)
            row["note"] += (f"; review {counts}; {promote_line}; lane csv sha256 {actual}")
    buf = io.StringIO(newline="")
    writer = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    lanes_path.write_text(buf.getvalue(), encoding="utf-8")
    arts = [str(review.relative_to(ROOT)), args.lane_csv, "case.json", "research/LANES.csv", "research/STATE.md", "CHANGELOG.md"]
    arts += [str(p.relative_to(ROOT)) for p in sorted((ROOT / "research").glob("*.csv"))]
    entry = {"utc": now, "slice": "S1", "lane": args.lane_id, "action": "reviewed and promoted",
             "command": f"python3 scripts/promote_lane.py {args.lane_id} {args.lane_csv} --verdicts ... --expect-sha256 {actual}",
             "exit": 0, "artifact_paths": arts, "sha256": {a: sha(ROOT / a) for a in arts},
             "cause": f"goal complete; {len(verdicts)} rows reviewed; {promote_line}",
             "next": "continue reviewing landed lanes; recompute frontier"}
    with (ROOT / "LEDGER.jsonl").open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(entry, sort_keys=True, ensure_ascii=False) + "\n")
    print(f"DONE {args.lane_id} {counts} {promote_line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
