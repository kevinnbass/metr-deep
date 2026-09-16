#!/usr/bin/env python3
"""S6 Done-when checker (PLAN.md S6). Exit 0 only when every line passes.

1. research/EXHAUSTION-GATE.json exists with gate_pass true.
2. research/outreach/MD99-71m-allocation.md exists, cites the gate file and its sha256, and links the reconciliation.
3. The draft carries approved_for_send: false and USER_AUTHORITY_WAIT (unsent), or an approved transmission receipt exists.
4. The draft contains no banned motive word, no seed-defect phrase, no allegation vocabulary and no compound rhetorical question.
5. The draft asks only the six residual cells and nothing already established.
6. No receipt exists unless approved_for_send is true and Kevin's approval is recorded in the draft.
"""
import hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ok = True
def line(n, good, msg):
    global ok
    ok = ok and good
    print("%d %s %s" % (n, "PASS" if good else "FAIL", msg))

gate_p = ROOT / "research/EXHAUSTION-GATE.json"
gate = json.load(open(gate_p)) if gate_p.exists() else {}
gate_sha = hashlib.sha256(gate_p.read_bytes()).hexdigest() if gate_p.exists() else ""
line(1, bool(gate.get("gate_pass")), "exhaustion gate present gate_pass=%s sha256=%s" % (gate.get("gate_pass"), gate_sha[:16]))

draft_p = ROOT / "research/outreach/MD99-71m-allocation.md"
text = draft_p.read_text() if draft_p.exists() else ""
cites_gate = "EXHAUSTION-GATE.json" in text and gate_sha[:16] in text
cites_recon = "commitment_reconciliation.csv" in text
line(2, draft_p.exists() and cites_gate and cites_recon, "draft exists=%s cites gate+hash=%s links reconciliation=%s" % (draft_p.exists(), cites_gate, cites_recon))

m_app = re.search(r"approved_for_send:\s*(true|false)", text)
approved = bool(m_app and m_app.group(1) == "true")
wait = "USER_AUTHORITY_WAIT" in text
receipts = [p for p in (ROOT / "research/outreach/receipts").glob("*") if p.is_file()]
line(3, bool(m_app) and ((not approved and wait and not receipts) or (approved and receipts)), "approved_for_send=%s USER_AUTHORITY_WAIT=%s receipts=%d" % (m_app.group(1) if m_app else None, wait, len(receipts)))

cfg = json.load(open(ROOT / "casework.json")); banned = cfg.get("banned_motive_words", [])
body = text.split("\n---\n", 2)[-1] if text.startswith("---") else text
hits = [w for w in banned if re.search(r"\b" + re.escape(w) + r"\b", body, re.I)]
alleg = [w for w in ("allege", "allegation", "accuse", "cover-up", "cover up", "conceal", "hiding", "misleading", "dishonest", "secret") if re.search(r"\b" + re.escape(w) + r"\b", body, re.I)]
questions = [q.strip() for q in re.findall(r"[^.?!\n]*\?", body)]
compound = [q for q in questions if re.search(r"\bwhy\b|\bisn't\b|\bdon't you\b|\bor is it\b|\bsurely\b|\bhow can\b", q, re.I) or q.count("?") > 1 or q.count(" or ") >= 2]
line(4, not hits and not alleg and not compound, "banned=%s allegation=%s compound_questions=%s" % (hits, alleg, [q[:60] for q in compound]))

cells = ["donor or vehicle", "committed amount", "commitment date", "cash paid", "restriction", "in-kind"]
missing = [c for c in cells if c not in body.lower()]
established = [s for s in ("Packard", "350,000") if re.search(r"(ask|confirm|tell)[^.\n]{0,80}" + s, body)]
line(5, not missing and not established, "residual cells present (missing=%s); re-asks established=%s" % (missing, established))

line(6, not receipts or (approved and re.search(r"approved_by:\s*Kevin", text)), "no transmission without recorded approval (receipts=%d)" % len(receipts))
print("S6 DONE-WHEN:", "GREEN" if ok else "RED")
sys.exit(0 if ok else 1)
