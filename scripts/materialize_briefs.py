#!/usr/bin/env python3
"""Materialize the frozen metr_deep lane briefs (PLAN.md §6) through the casework engine.

This calls the engine's own `generate_plan_lanes` as a library so the brief shape, metadata comment
and safety checks are the engine's, not this pack's. It does not modify the engine and it does not
launch a lane. Re-running is idempotent: an unchanged brief is reported SKIP.

Usage: python3 scripts/materialize_briefs.py
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, "/home/kevin/repos/casework")
sys.path.insert(0, str(ROOT / "scripts"))

from casework.lanes import generate_plan_lanes  # noqa: E402
from casework.packs import load_pack  # noqa: E402

from lanes_spec import LANES  # noqa: E402

PREFACE = (
    "Slice {slice}, wave {wave}. This lane belongs to /mnt/f/projects/anthropic/metr_deep/PLAN.md; its id, slug and "
    "scope are frozen and are never renumbered or repurposed.\n\n"
    "Scope: {title}.\nPrimary routes: {routes}.\n\n"
    "Embargo: this lane sends nothing and contacts nobody. It may read any public material published by METR, a "
    "funder, an intermediary, a lab or a government body, but it may not email, message, telephone, file, submit or "
    "post anything, and it may not ask anyone how the approximately $71 million commitment total was composed or "
    "allocated. A draft is not a transmission; any draft this lane writes stays unsent.\n\n"
    "Row typing: put the target table prefix in target_prefix on every row (MDE entity, MDF funding event, MDI "
    "in-kind or access, MDP provenance proposition, MDQ project conflict, MDR relationship, MDS source coverage and "
    "bounded negative, MDT timeline event) and put the case element ids this row would support in element_ids, "
    "semicolon separated, from: {elements}. Leave any column that does not apply to a row empty rather than "
    "guessing."
)


def main() -> int:
    config = load_pack("metr_deep")
    plan_sha = hashlib.sha256((ROOT / "PLAN.md").read_bytes()).hexdigest()
    lanes = []
    for lane_id, spec in LANES.items():
        directive = PREFACE.format(
            slice=spec["slice"], wave=spec["wave"], title=spec["title"],
            routes=spec["routes"], elements=", ".join(spec["elements"]),
        )
        lanes.append({
            "lane_id": lane_id,
            "title": spec["title"],
            "slug": spec["slug"],
            "directive": directive,
            "elements": spec["elements"],
            "tasks": spec["tasks"],
            "outputs": [f"research/grok-out/{lane_id}-{spec['slug']}.csv"],
        })
    wrote = skipped = 0
    for action, path in generate_plan_lanes(config, lanes, plan_sha):
        wrote += action == "WROTE"
        skipped += action == "SKIP"
    print(f"BRIEFS wrote={wrote} skipped={skipped} total={len(lanes)} plan_sha256={plan_sha[:12]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
