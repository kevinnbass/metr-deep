# PLAN — METR funding, access dependence, and project-level independence

## Status
Last verified: 2026-09-16T18:37:18Z by Claude (S5 complete and verified)   (UTC; re-verify on every resume)
Current slice: S6
- [x] S0 Foundation and baseline — register the pack, preserve the posted/current distinction, import reviewed seed evidence, and establish the claim/source frontier   — evidence: `research/receipts/S0/S0-verification.json` sha256 b02bdfa905674fefd3372535e5fcb09af58169ab525f7c17bf08950cf25f0d17; `LEDGER.jsonl` line 2 `S0 verified`
- [x] S1 Reconstruct METR's funding from public records — every named supporter and every currently discoverable amount, date, vehicle, purpose, and payment status   — evidence: `research/receipts/S1/S1-verification.json` sha256 b3a5f1da870050630052245e4e00a7ad1a89e62bf324b350d8abf64689652260; `LEDGER.jsonl` line 19 `S1 verified`
- [x] S2 Intermediaries, contracts, and the commitment ledger — Audacious/Canary, DAFs, government work, and the approximately $71 million denominator   — evidence: `research/receipts/S2/S2-verification.json` sha256 39ce31f22019e971d8d23844d368ccd0dafcc2595b034be6660c3f9270b39a80; `LEDGER.jsonl` line 36 `S2 verified`
- [x] S3 Independence beyond cash — lab-supplied access and tokens, project terms, personnel conflicts, governance, and evaluator selection   — evidence: `research/receipts/S3/S3-verification.json` sha256 3de8c07e0048a3fe693ea8dd239cb37b0ca8e19da650040d365e22a6381168d7; `LEDGER.jsonl` line 52 `S3 verified`
- [x] S4 Opaque vehicles and record-producing routes — statutory documents, public-record requests, the donated stock vehicle, and calendar closers   — evidence: `research/receipts/S4/S4-verification.json` sha256 529fc49048a45e83f64445aba816381290de1f577b0ac5acf848f0f415c37669; `LEDGER.jsonl` line 62 `S4 verified`
- [x] S5 Reconciliation, adversarial audit, gap closure, and figures — exhaust the current public frontier before any allocation request   — evidence: `research/receipts/S5/S5-verification.json` sha256 9f3223806f8c76f1fa74df28308afe87c18a706b42e322b66146de739bd34065; `LEDGER.jsonl` line 96 `S5 verified`
- [ ] S6 Terminal outreach — only after the exhaustion gate, draft and, with Kevin's explicit approval, send the single consolidated request for the $71 million allocation   — state: USER_AUTHORITY_WAIT since 2026-09-16T19:25Z; draft `research/outreach/MD99-71m-allocation.md` (approved_for_send false), `scripts/check_s6.py` GREEN, `LEDGER.jsonl` line 98; not complete until Kevin approves the exact draft or waives sending   ← current

## Running this file under /goal
Goal kind: analysis. Run one slice at a time; do not one-shot the file. The parent session launches research lanes through `/mnt/f/projects/anthropic/tools/lanes.py` and supervises them under §10. Codex is used only for audits when Kevin explicitly approves it in the same session.

- S0: `/goal Do slice S0 of /mnt/f/projects/anthropic/metr_deep/PLAN.md per its Per-slice contract. Verify with: cd /home/kevin/repos/casework && python3 -m casework verify --pack metr_deep. Done when the baseline receipt, seed manifest, registered pack, claims, tables and briefs exist and verify. Stop when S0 is green or a Stop-and-ask item is reached.`
- S1: `/goal Do slice S1 of /mnt/f/projects/anthropic/metr_deep/PLAN.md per its Per-slice contract. Verify with: cd /home/kevin/repos/casework && python3 -m casework verify --pack metr_deep. Done when every named supporter has reviewed public-source coverage and the funding ledger reconciles every known amount by money type. Do not contact METR or a funder. Stop when S1 is green or a Stop-and-ask item is reached.`
- S2: `/goal Do slice S2 of /mnt/f/projects/anthropic/metr_deep/PLAN.md per its Per-slice contract. Verify with: cd /home/kevin/repos/casework && python3 -m casework verify --pack metr_deep. Done when intermediary, contract and commitment lanes are reviewed and promoted and the known/unknown portion of the $71M is mechanically stated. Do not ask anyone for the allocation. Stop when S2 is green or a Stop-and-ask item is reached.`
- S3: `/goal Do slice S3 of /mnt/f/projects/anthropic/metr_deep/PLAN.md per its Per-slice contract. Verify with: cd /home/kevin/repos/casework && python3 -m casework verify --pack metr_deep. Done when each material project has an evidence-backed independence profile and all lab, donor and entity distinctions pass review. Do not contact METR or a funder. Stop when S3 is green or a Stop-and-ask item is reached.`
- S4: `/goal Do slice S4 of /mnt/f/projects/anthropic/metr_deep/PLAN.md per its Per-slice contract. Verify with: cd /home/kevin/repos/casework && python3 -m casework verify --pack metr_deep. Done when every currently available record-producing route has a reviewed result or a dated pending/NEEDS_HUMAN state. The $71M allocation question remains prohibited. Stop when S4 is green or a Stop-and-ask item is reached.`
- S5: `/goal Do slice S5 of /mnt/f/projects/anthropic/metr_deep/PLAN.md per its Per-slice contract. Verify with: cd /home/kevin/repos/casework && python3 -m casework frontier --pack metr_deep. Done when two adversarial reviews confirm the current public frontier is empty or N/A-with-reason, corrections are applied, and every figure and claim matrix passes verification. Stop before drafting any allocation request.`
- S6: `/goal Do slice S6 of /mnt/f/projects/anthropic/metr_deep/PLAN.md per its Per-slice contract. Verify with: test -f research/EXHAUSTION-GATE.json && test -f research/outreach/MD99-71m-allocation.md. Done when the terminal request is evidence-tailored and unsendable by default; send only after Kevin explicitly approves the exact draft. Stop on USER_AUTHORITY_WAIT if approval is absent.`

## Read-first (closed set)
Read in this order and nothing else by default:

1. This file, top to bottom.
2. `research/STATE.md`, `research/LANES.csv`, and the last 20 lines of `LEDGER.jsonl` once they exist.
3. `repo/research/STATE.md`, `repo/research/AUDIT-4.md`, and `repo/NOTES.md` as the public-repository baseline; `repo/` is read-only.
4. `/mnt/f/projects/memes/ai-machine/10-metr/HANDOFF.md` for the larger source inventory, treating its claims as leads until re-reviewed here.
5. For S0 or lane execution only: `/home/kevin/repos/casework/README.md`, `/mnt/f/projects/anthropic/tools/README.md`, and `~/GROK_HEADLESS_GOAL.md`.

On demand only: the exact sibling-pack table or reviewed lane named in §6, the primary document for a row under review, and the applicable casework command help. Do not bulk-read sibling packs. Chat memory is advisory; this file, the authoritative tables, `research/STATE.md`, `research/LANES.csv`, `LEDGER.jsonl`, and saved receipts are the restart authority.

## State that rots

| Quoted or operational state | Re-measure with |
|---|---|
| Public-repo revision (`17539bac…` when this plan was written) | `git -C repo rev-parse HEAD && git -C repo status --short` |
| Public-repo audit result (12 figures, 579 cited IDs, nine missing `RP` rows when written) | `cd repo && python3 scripts/audit.py` |
| METR's approximately $71M commitment statement and supporter list | fetch `https://metr.org/blog/2026-08-14-funding-update/` and `https://metr.org/about`; save response hashes and UTC |
| Packard grant ($350,000, 2026, 12 months when found) | fetch `https://www.packard.org/grantee/model-evaluation-and-threat-research/`; record page fields, metadata and hash |
| COI-policy version (v1.0, updated 2026-08-28 when written) | fetch `https://metr.org/coi-policy.pdf`; hash and extract first-page version/date |
| Named-funder databases and grant pages | re-run each lane's saved canonical URL/API query; a search older than the source's freshness window is history |
| Form 990, 990-PF, Schedule B/M/I availability | IRS TEOS index/API plus the lane's saved object-id query; never infer availability from last run |
| UK/EU/US contract and procurement state | re-run the saved official procurement query in the applicable MD19–MD21 or MD44 receipt |
| Anthropic S-1 or other holder disclosure | `https://www.sec.gov/edgar/search/` issuer/Cik query saved by MD42 |
| Lane/account capacity | `python3 /mnt/f/projects/anthropic/tools/lanes.py accounts` and `python3 /mnt/f/projects/anthropic/tools/lanes.py status --pack metr_deep` |
| Claim/source frontier | `cd /home/kevin/repos/casework && python3 -m casework frontier --pack metr_deep` |
| F1 engine receipt | `test -f /home/kevin/repos/casework/work/receipts/F1.json && echo present` |
| Request/appeal state | `tail -20 research/records/REQUESTS.jsonl` once created; a draft is not a sent request |

Anything older than its stated freshness window is history, not live state. Default freshness: 90 days for filings/registries, 30 days for web pages/press, and same-day for lane/process state. A future document is `N/A-with-reason` until its availability date, not “searched and absent.”

## Per-slice contract

### S0 — Foundation and baseline
Goal: create a restartable, verified case that distinguishes the image posted on September 14 from later repository corrections.

Goal kind: analysis.

Preconditions:
- `/mnt/f/projects/anthropic/metr_deep/PLAN.md` exists and `repo/.git` resolves.
- `/home/kevin/GOAL_SPEC_STANDARD.md` exists; this plan has B1–B9 in order.
- Casework F1 receipt exists, checked read-only.

Steps:
1. Register `metr_deep` with casework; create the pack skeleton, `casework.json`, `case.json`, authoritative MD* tables in §3, `research/STATE.md`, `research/LANES.csv`, `LEDGER.jsonl`, `CHANGELOG.md`, and receipt directories.
2. Hash and inventory the public clone, the posted-image commit `f64df65`, the current commit, the full 10-metr seed paths used, and the three sibling plans. Never alter the seed clone or sibling packs.
3. Record the baseline audit faithfully, including the current nine missing `RP` references and the fact that the main two money figures have no missing row IDs. A failing seed audit is evidence, not a reason to edit the seed.
4. Import only evidence needed for §4's claims into MD* tables after review, minting new MD* IDs and retaining the source pack/path/original row id in `note`. Do not silently adopt narrative conclusions from HANDOFF.
5. Materialize briefs MD01–MD53 and MD99 from §6 without launching later slices; seed the source-class frontier and posted/current version claim.

Done when:
- `cd /home/kevin/repos/casework && python3 -m casework verify --pack metr_deep` exits 0.
- `research/BASELINE.json` records seed paths, commits, hashes, audit exit/output and the posted/current chronology.
- `case.json` contains every claim in §4 with open elements defaulting to not-ready.
- `research/LANES.csv` maps every frozen lane id to exactly one brief and slice.
- `LEDGER.jsonl` has `S0 opened` and `S0 verified` entries with artifact hashes.

Verify with:
`cd /home/kevin/repos/casework && python3 -m casework verify --pack metr_deep && python3 -m casework readiness --pack metr_deep --gaps && python3 -m casework frontier --pack metr_deep`

Evidence written to: `research/BASELINE.json`, `research/receipts/S0/`, `LEDGER.jsonl`, `CHANGELOG.md`.

Non-goals: new web research; fixing or publishing the seed repository; contacting anyone.

Must NOT: edit `repo/`, sibling packs, `case.json` by hand after registration, or reinterpret a seed audit defect as a substantive funding defect.

Stop-and-ask: any need to alter `/home/kevin/repos/casework` beyond registering this pack in `packs.json`; any proposed deletion or rewrite of seed evidence.

### S1 — Public funding reconstruction
Goal: recover every currently public METR funding fact without asking METR or its supporters for the approximately $71 million allocation.

Goal kind: analysis.

Preconditions:
- S0 is `[x]` with an evidence pointer.
- MD01–MD14 briefs exist and the seed frontier is current.

Steps:
1. Run MD01–MD14 in the order and dependency groups in §6; supervise and review each lane as it lands.
2. Promote only CONFIRMED or corrected DIFFERS rows. Every named supporter receives an amount/date/vehicle/purpose/payment-status row or a bounded-negative row listing exact sources checked.
3. Maintain four separate ledgers: commitments, paid/filed grants, transfers/regrants, and in-kind/contracts. Never use one as evidence of another.
4. Reconcile funder-side disclosures to recipient-side revenue only where periods and entities match; unmatched totals remain unmatched.

Done when:
- All MD01–MD14 lanes are complete or have a reviewed replacement under MD70–MD89.
- `research/supporter_coverage.csv` has one current status for every supporter named by METR plus every filed payer already known.
- Every known number is typed as commitment, paid/filed grant, recommendation, transfer, contract, or in-kind estimate.
- Casework verification exits 0 and the S1 claim frontier has no `UNTOUCHED` public grant-database or currently available recipient/funder-filing class.

Verify with:
`python3 /mnt/f/projects/anthropic/tools/lanes.py status --pack metr_deep; cd /home/kevin/repos/casework && python3 -m casework verify --pack metr_deep && python3 -m casework frontier --pack metr_deep`

Evidence written to: `research/grok-out/MD01-*.csv` through `MD14-*.csv`, review files, promoted MD* rows, `research/receipts/S1/`, ledger.

Non-goals: proving bias; identifying private Jane Street donors without public evidence; requesting the $71M allocation.

Must NOT: contact METR, a named supporter, its employees, or its representatives; equate a person with their employer or family foundation; count the $350,000 Packard grant inside the $71M unless a source connects it.

Stop-and-ask: a source exposes a private donor identity not already public; a proposed paid database or logged-in source.

### S2 — Intermediaries, contracts, and commitment ledger
Goal: determine how much of METR's known support can be traced through public intermediary, contract and commitment records.

Goal kind: analysis.

Preconditions:
- S1 is `[x]`.
- MD15–MD25 briefs have imported reviewed overlap from lineage rather than duplicating it.

Steps:
1. Run MD15–MD25. Treat Audacious membership, project funding, recipient allocation and payment as four different propositions.
2. Reconcile Canary statements and funder filings at RAND and METR separately; a payment to RAND is not a payment to METR.
3. Search official UK, EU and US procurement/grant systems and archive every award/contract document; distinguish consortium ceiling from METR's share.
4. Build the commitment reconciliation: approximately $71M as the denominator stated by METR, public commitments attributable to a named source as the identified numerator, and an explicit unknown remainder. Do not force equality where periods differ.
5. Diff archived donor/funding pages to identify when supporters and rules appeared, without inferring grant dates solely from page appearance.

Done when:
- MD15–MD25 and reviews are complete or replaced by reviewed gap lanes.
- `research/commitment_reconciliation.csv` states the $71M denominator, every compatible known component, every excluded/non-comparable component, and the unresolved remainder/range.
- Each government or consortium line has award id, contracting authority, legal recipient, ceiling/value, period, and METR share or “not disclosed in checked document.”
- Casework verify exits 0; relevant source classes are COVERED or N/A-with-reason.

Verify with:
`cd /home/kevin/repos/casework && python3 -m casework verify --pack metr_deep && python3 -m casework readiness --pack metr_deep --gaps`

Evidence written to: promoted MDF/MDG/MDP rows, `research/commitment_reconciliation.csv`, `research/receipts/S2/`, ledger.

Non-goals: treating all historical supporters as participants in the six-month raise; outreach; stock-vehicle conclusions.

Must NOT: ask METR or a supporter which part of the $71M they supplied; infer Audacious project donors from the general partner list; aggregate contracts, commitments and grants.

Stop-and-ask: an official public-record request is the only remaining route for a specific contract document; draft it for S4 and continue.

### S3 — Independence beyond cash
Goal: produce a project-by-project account of financial, in-kind, access, personnel and governance dependencies.

Goal kind: analysis.

Preconditions:
- S2 is `[x]`.
- MD26–MD36 briefs exist; the current COI-policy hash is recorded.

Steps:
1. Run MD26–MD36 and promote reviewed rows.
2. For each material METR engagement, record provider, dates, compensation, credits/tokens, access, safe harbor, provider redaction/exit authority, evaluator editorial control, personnel disclosures and applicable policy version.
3. Separate direct equity, firm/entity investment, donor/investor overlap, former employment, close personal relationship, board role, model access and mere ecosystem adjacency.
4. Compare like projects using a fixed matrix; differences are observations, not evidence of motive.
5. Test the strongest and weakest possible readings of METR's independence against AEF-1, its own policy, and other published evaluator standards.

Done when:
- Every named Anthropic, OpenAI, Google DeepMind, Meta and Amazon engagement in scope has an MDQ project profile or a bounded gap.
- `research/independence_matrix.csv` has one row per project and no cell based solely on affiliation inference.
- Direct-lab cash, in-kind resources and access dependence are separate columns and claims.
- MD33's investor mapping distinguishes every relevant individual, firm, foundation and investment vehicle.
- Casework verification exits 0 and an adversarial reviewer has checked the entity distinctions.

Verify with:
`cd /home/kevin/repos/casework && python3 -m casework verify --pack metr_deep && python3 -m casework readiness --pack metr_deep --gaps`

Evidence written to: MDQ/MDI/MDR rows, `research/independence_matrix.csv`, review report, `research/receipts/S3/`, ledger.

Non-goals: grading scientific conclusions for correctness unless required to understand project terms; asserting capture, coordination or motive.

Must NOT: use shared employment, friendship, office space or investor status as a money flow; describe free access as cash; apply the August 2026 policy retroactively without saying so.

Stop-and-ask: a proposed row would expose nonpublic personal information; a conclusion depends on confidential material not in scope.

### S4 — Opaque vehicles and record-producing routes
Goal: use every lawful document-producing route that can resolve intermediary, stock, contract or donor-provenance questions without asking for the $71M allocation.

Goal kind: operations/service plus analysis. Every external transmission requires Kevin's explicit approval of the exact draft; research continues while a request is pending.

Preconditions:
- S3 is `[x]`.
- MD37–MD45 briefs exist.

Steps:
1. Exhaust live filings, registries, archives and issuer records first.
2. Prepare narrowly scoped §6104(d), Form 4506-A or public-record drafts only for existing records, never explanatory questions and never a disguised request for the $71M allocation.
3. On approval, send through the authorized channel, record exact text/time/receipt, track deadlines and appeals, and ingest productions through review. Without approval, mark `USER_AUTHORITY_WAIT` and continue other lanes.
4. Monitor Good Ventures FY2026, CY2025 intermediary returns, Audacious-partner returns, METR filings and any Anthropic securities filing. Currently unavailable records are calendar closers, not negative evidence.
5. Keep the donated-stock investigation independent of the METR-funding conclusion: identifying the vehicle still would not establish onward funding to METR.

Done when:
- MD37–MD45 are reviewed and promoted or have a dated pending/USER_AUTHORITY_WAIT state.
- Every currently available filing and registry class is COVERED; future-only documents are N/A-with-reason and next-check date.
- Every approved request has a receipt and terminal current state (produced, denied, appealed, pending within clock, or closed by Kevin).
- `research/records/REQUESTS.jsonl` and `research/calendar.csv` pass their casework checks.
- No request sent in this slice asks who supplied or how METR allocated the approximately $71M.

Verify with:
`cd /home/kevin/repos/casework && python3 -m casework verify --pack metr_deep && python3 -m casework frontier --pack metr_deep; tail -20 /mnt/f/projects/anthropic/metr_deep/research/records/REQUESTS.jsonl`

Evidence written to: `research/records/`, `research/calendar.csv`, MD37–MD45 outputs/reviews, `research/receipts/S4/`, ledger.

Non-goals: private discovery, subpoenas, paid data brokers, asking METR or donors for the allocation.

Must NOT: send without approval; ask a public-record custodian to create an analysis; call a DAF contribution Moskovitz's or Anthropic stock without a source naming it.

Stop-and-ask: every transmission; fees; identity verification; legal representation; any appeal beyond a routine administrative appeal.

### S5 — Reconciliation, adversarial audit, gap closure, and figures
Goal: close the current public-source frontier and state exactly what the evidence proves, rebuts and leaves unknown.

Goal kind: analysis.

Preconditions:
- S4 is `[x]` or every S4 wait is recorded and no currently available independent work remains.
- MD46–MD53 briefs exist; all earlier lanes have reviews.

Steps:
1. Run MD46–MD53, then generate MD70–MD89 only from actual open elements or untouched source classes.
2. Recompute the funding reconciliation, project matrix, investor/entity map and stock-vehicle state from promoted rows only.
3. Commission two independent adversarial reviews: one money/provenance audit and one framing/entity/causality audit. Apply corrections with append-only audit notes.
4. Render only figures whose claims are ready. Each figure must show unknowns, distinguish money types, and avoid pipe geometry where onward passage is not established.
5. Run casework frontier after corrections. Create `research/EXHAUSTION-GATE.json` only if §7's gate is satisfied; S5 itself must not draft the allocation request.

Done when:
- Casework verify exits 0; every promoted row has a review verdict and source.
- Every claim in §4 has a verdict and a list of evidence, rebuttal and open elements.
- Both adversarial reviews exist and every DIFFERS finding is resolved or explicitly open.
- Every rendered figure passes collision, evidence, money-type, bounded-negative and motive-language checks.
- `casework frontier --pack metr_deep` contains no `UNTOUCHED` class and no actionable `PARTIAL` element lacking a lane; `EXHAUSTION-GATE.json` records exact exceptions and future dates.

Verify with:
`cd /home/kevin/repos/casework && python3 -m casework verify --pack metr_deep && python3 -m casework readiness --pack metr_deep --gaps && python3 -m casework frontier --pack metr_deep`

Evidence written to: `research/agents-*/AUDIT-MONEY.md`, `AUDIT-FRAMING.md`, `research/EXHAUSTION-GATE.json`, figures, README, `research/receipts/S5/`, ledger.

Non-goals: publication; outreach; maximizing the number of figures.

Must NOT: declare exhaustion from prose or model confidence; weaken a claim to make it ready; draft or send the $71M request; turn an adjacency graph into a cash-flow chart.

Stop-and-ask: Codex audit spend; public-repo synchronization; any figure naming a private person or implying misconduct.

### S6 — Terminal $71M allocation request
Goal: after every independent route is exhausted, ask one consolidated, evidence-tailored question for the unresolved allocation.

Goal kind: operations/service.

Preconditions:
- S0–S5 are `[x]` with evidence pointers.
- `research/EXHAUSTION-GATE.json` passes every gate in §7 and has two reviewer approvals.
- No currently available source, pending production within its ordinary clock, or unreviewed lane could answer the same elements.

Steps:
1. MD99 drafts one short request using the final unknown matrix. Ask for donor/vehicle, committed amount, commitment date, cash paid to date, restriction/purpose and whether in-kind support is included in the approximately $71M. Do not re-ask facts already established.
2. Attach or link the public-source reconciliation so the recipient can correct specific cells rather than respond to a theory.
3. Save the draft with `approved_for_send: false`. Present the exact draft to Kevin.
4. Send only after Kevin explicitly approves that exact version. Record the transmission and any response; review and promote new facts before changing conclusions.

Done when:
- `research/outreach/MD99-71m-allocation.md` exists, cites the exhaustion gate and contains no allegation or compound rhetorical question.
- The file remains unsent with `USER_AUTHORITY_WAIT`, or an approved transmission receipt exists in `research/outreach/receipts/`.
- Any response received is preserved verbatim, reviewed and bound to claim elements; no response is not evidence of an allocation.

Verify with:
`test -f research/EXHAUSTION-GATE.json && test -f research/outreach/MD99-71m-allocation.md && rg -n 'approved_for_send|USER_AUTHORITY_WAIT|sent_utc' research/outreach/MD99-71m-allocation.md research/outreach/receipts 2>/dev/null`

Evidence written to: `research/outreach/MD99-71m-allocation.md`, optional receipt/response, review, ledger.

Non-goals: argument, publicity, repeated follow-ups, asking donors separately to reconstruct the total.

Must NOT: begin before the gate; send without exact approval; split the request among funders to evade the sequencing rule; characterize silence as confirmation.

Stop-and-ask: sending, follow-up, publication or quoting a response outside this pack.

## Stop conditions (global)
Complete means S0–S6 are `[x]` with same-line evidence pointers and the exact verification commands in each slice exit 0. S6 may close without transmission only if Kevin explicitly waives sending and that waiver is recorded; absent approval it remains `[ ] USER_AUTHORITY_WAIT`, not complete.

Not terminal: a red verification check, 429/529, a wall, one failed fetch, an empty lane that records bounded negatives, context compaction, a missing future filing, a pending request still inside its clock, or a choice the plan already decides. Fix, route around, calendar, or continue another independent lane.

Terminal without completion: a `STOP` sentinel in the pack root; Kevin stops the work; an external permission needed for the only remaining action; a source requiring prohibited access; or the same route failing three times. After three failed attempts at one route, record the URL, command, responses and next lawful alternative, then move on. Never keep retrying merely to fill turns.

For standing monitoring, a run is a bounded shift: done when its stated UTC shift end or `STOP` is reached and every due calendar check has a receipt. `ONLINE_IDLE_READY` is not investigation completion.

## Guardrails
Allowed write-set: `/mnt/f/projects/anthropic/metr_deep/**` except the frozen `repo/**`; the single pack-registration entry in `/home/kevin/repos/casework/packs.json`; casework-generated review/receipt state for pack `metr_deep`; and an optional mirror under `~/Downloads/anthropic/metr_deep/`. Every sibling pack is read-only.

Standing authorization: read public sources; run commands in Verify; launch and supervise Grok lanes through the shared runner; write within the allowed pack paths. Asking for an already authorized local/read-only action is a defect. Anything else is `NEEDS_HUMAN`; log it and continue authorized work.

Rules:

- **Allocation-request embargo:** before S6, no message, form, email, post or question to METR, its personnel, its board, a named supporter, Audacious, RAND or a donor may ask or imply a request for the donor-by-donor composition of the approximately $71M. Searching their public materials is permitted. A statutory request for an existing public record is not an allocation question, but still requires Kevin's approval before transmission.
- No external message, records request, appeal, publication, repo push or public correction without Kevin's explicit approval of the exact action.
- No use of posts by `@kevinnbass` as evidence. They may identify a source to locate independently.
- No motive, coordination, corruption, laundering, capture or dependence conclusion unless the claim's required elements are independently supported; motive vocabulary is barred from figure text.
- Keep legal entities separate: individual, employer, investment vehicle, foundation, DAF sponsor/account, grantmaker, project and recipient. A connection between two does not merge them.
- Keep money types separate: commitment, payment, filed grant, recommendation, transfer, contract, in-kind credit and equity value are never summed across type. No visual pipe implies onward passage without a documented transaction.
- A bounded negative names exact sources and dates. Never “nothing more can be pulled.”
- Only public people in public roles; no deanonymization of Jane Street individuals, DAF advisers or private donors through probabilistic matching.
- Primary sources first, retained press second. Every promoted row has URL, quote, checked UTC, source class and provenance.
- Corrections append an audit note; rows, source files and reviews are never deleted. A slice description or Done-when criterion is never weakened in place; add a dated amendment.
- Do not modify `repo/`, any sibling pack, or casework engine code as part of this plan. Stop if registration alone is insufficient.
- No network/system changes; no `nmcli`, `resolvectl`, `protonvpn`, `sudo`, `systemctl`, `ip`, `iptables` or `nft`.
- Obey the fleet process-kill ban: never kill by process name, pattern, run id or slug; stop only a PID launched and recorded by the shared runner, otherwise use its soft-stop mechanism.
- Codex quota only with Kevin's explicit approval in the same session. Default research lanes are Grok.
- Eight concurrent lanes per pack; ten goal lanes per account across the shared fleet; logs outside the pack; never poll with `pgrep -f`.
- No placeholders, stubs, fallback evidence or test theater; no editing/skipping checks to pass.
- Pre-empt these failure modes: premature done on the first grant found; one-shotting the plan; wandering into a later slice while the current gate is red; checkbox flips without evidence; stale state treated as live; extending scope or deadlines in place; re-asking authorization; increasing concurrency after throttling; claiming files changed without receipts; compaction drift; and spending tokens after useful work has ended.

Immutable values: lane IDs in §6; the posted-image commit `f64df65`; the direct-allocation embargo through S5; the requirement for two adversarial S5 reviews; the user-approval send gate; money-type separation. Amendments may add evidence or a successor lane but may not renumber or weaken these values.

## Resume protocol
Run these in order after restart or compaction:

1. `cd /mnt/f/projects/anthropic/metr_deep && pwd`
2. `sed -n '/^## Status/,/^## Running this file/p' PLAN.md; test -f LEDGER.jsonl && tail -20 LEDGER.jsonl || true`
3. `test -f casework.json && (cd /home/kevin/repos/casework && python3 -m casework frontier --pack metr_deep) || git -C repo rev-parse HEAD`
4. `sed -n '/^## 0\. Governing question/,/^## 1\./p' PLAN.md` — then restate the current slice and governing question in one sentence; mismatch means drift and requires re-anchoring before work.
5. `test -f casework.json && (cd /home/kevin/repos/casework && python3 -m casework verify --pack metr_deep) || (cd repo && python3 scripts/audit.py); python3 /mnt/f/projects/anthropic/tools/lanes.py status --pack metr_deep`

Never replay a completed fetch, transmission, promotion or render. Search the ledger, lane state and receipts before acting; do not assume an artifact is missing. After S6 begins, confirm `EXHAUSTION-GATE.json` and `approved_for_send` before touching outreach.

## Progress ledger
`LEDGER.jsonl` is append-only with schema:

`{"utc":"ISO-8601Z","slice":"S0..S6","lane":"MDnn|local","action":"string","command":"string|null","exit":0,"artifact_paths":["path"],"sha256":{"path":"hex"},"cause":"string","next":"string"}`

`research/LANES.csv` is the per-lane state table: `lane,slice,wave,slug,status,launched_utc,pid,log,done_utc,rows_out,review,promoted_utc,note`. Status moves `planned → briefed → launched → landed → reviewed → promoted`, or `failed/replaced/pending-record/USER_AUTHORITY_WAIT`. `research/SUPERVISION.jsonl` records every ten-minute tick and decision. `research/records/REQUESTS.jsonl` records draft/transmission/deadline/production state. `CHANGELOG.md` records promoted corrections and rendered releases. Every Status checkbox must cite a ledger line or hashed receipt on the same line; transcript prose is not evidence.

---

## 0. Governing question and ordering

The investigation asks a narrower, answerable question than the September 14 rhetoric:

> What money, in-kind resources, access, personnel relationships and governance conditions support METR's work; which of those have documented Anthropic investor or company connections; and what does the public record establish about their relevance to specific evaluations?

The work is ordered by impact. First establish a valid ledger and claim gate. Then reconstruct METR's own money. Then trace intermediaries and contracts. Then examine the forms of dependence that direct-donation policies do not answer. Only after those routes are exhausted does the plan pursue opaque vehicles and records requests, synthesize the result, and finally ask for the unresolved $71M allocation.

The goal is not to confirm the post. The goal is to make the strongest true statement and identify the exact missing document for every stronger statement.

## 1. Outputs

The pack produces:

1. A donor-by-donor public ledger with exact legal entities and typed money events.
2. A reconciliation of the approximately $71M commitment announcement: identified compatible components, excluded/non-comparable amounts, and unresolved remainder/range.
3. A project-level independence matrix covering money, in-kind resources, access, disclosure, redaction/exit authority, personnel and policy version.
4. A provenance map for Audacious, Canary, DAFs, ARC and government contracts that never converts adjacency into flow.
5. A bounded state of the Moskovitz donated-stock question, including why vehicle identification would or would not affect the METR claims.
6. A claim matrix adjudicating the public response sentence by sentence and the underlying post claim by claim.
7. A small figure set, an evidence bibliography, a complete could-not-yet-obtain list and a filing/records calendar.
8. Only after all of the above, one consolidated allocation request.

## 2. Pack layout and source hierarchy

| Artifact | Path |
|---|---|
| Plan and ledgers | `PLAN.md`, `LEDGER.jsonl`, `CHANGELOG.md` |
| Casework configuration | `casework.json`, `case.json` |
| Authoritative evidence | `research/*.csv` |
| State/frontier | `research/STATE.md`, `research/supporter_coverage.csv`, `research/commitment_reconciliation.csv` |
| Briefs and immutable lane output | `research/grok-briefs/`, `research/grok-out/` |
| Reviews | `research/agents-YYYY-MM-DD/` |
| Primary captures | `research/primary/MDNN/` |
| Requests and productions | `research/records/`, `research/outreach/` |
| Figures | `figures/` |
| Frozen public clone | `repo/` |

Source order: issuer/recipient/funder document; government filing or procurement record; retained archive; named on-record statement; high-quality press; secondary database used only to locate a primary. A filing can prove its own fields, not facts outside its reporting period or legal entity.

Sibling work is imported, not repeated. In particular, consult reviewed outputs for lineage L09–L16 (filings/capital), L28 (evaluator people), L45 (equity), L46 (lab money), L48 (Audacious), L49 (evaluator timeline) and L50 (Coefficient statements). If the sibling lane is incomplete, record the dependency; do not launch a duplicate broad lane. A `metr_deep` lane must target a METR-specific unresolved element.

## 3. Data model

All new row ids use three-letter prefixes not used by the seed pack:

| Prefix | Table | Purpose |
|---|---|---|
| MDE | `entities.csv` | canonical legal entity/person/project, identifiers, aliases, entity distinctions |
| MDF | `funding_events.csv` | amount, currency, date/period, from/to, money type, paid/committed status, restriction and purpose |
| MDI | `in_kind_access.csv` | tokens, compute, model access, technical help, safe harbor and estimated value if sourced |
| MDP | `provenance.csv` | intermediary, DAF, regrant and project-allocation propositions with confidence bounded by documents |
| MDQ | `project_coi.csv` | project, provider, policy version, personnel conflicts, disclosure/recusal, redaction and exit rights |
| MDR | `relationships.csv` | investor, observer, board, employment, contracting and personal-relationship facts, typed separately |
| MDS | `source_coverage.csv` | exact query/source class, checked UTC, result, freshness, limitation and next document |
| MDT | `timeline.csv` | funding, policy, filing, engagement and disclosure events with date precision |

Every row includes `url`, `quote_300`, `source_class`, `checked_utc`, `review_verdict`, `lane`, and `note`. Imported facts receive a new MD* id and preserve `seed_path` and `seed_row_id` in `note`.

`MDF.money_type` is one of `commitment`, `paid_grant`, `filed_grant`, `recommendation`, `transfer`, `regrant`, `contract`, `in_kind_estimate`, or `equity_value`. Only rows of the same compatible type, period and currency may be totaled. The $71M announcement is a commitment denominator, not revenue or cash.

## 4. Claims and required answers

| Claim | Question | Ready only when |
|---|---|---|
| C01 | What publicly recoverable commitments compose the approximately $71M raised in February–August 2026? | Denominator, compatible identified components, exclusions and unresolved remainder are documented; no unsupported allocation is imputed. |
| C02 | Who has funded METR, in what amount, vehicle, period and form? | Every named supporter and filed payer has a current positive or bounded-negative record. |
| C03 | Has METR received frontier-lab money or employee-directed donations? | Direct payments, contracts, donations, DAF directions and the limits of public verification are separately tested. |
| C04 | What in-kind resources and access does each lab provide? | Provider/project/value/terms are documented or explicitly undisclosed. |
| C05 | Which METR donors have Anthropic investment or governance connections? | Exact individuals/entities/vehicles are distinguished; investment and donation events are separately sourced. |
| C06 | Which intermediary money actually reached METR? | Every asserted path has a transaction into METR or is labelled adjacency/project-partner context. |
| C07 | Where is Moskovitz's donated Anthropic stake, and does that answer any METR funding element? | Vehicle state is bounded; no onward-funding inference is made without a transaction. |
| C08 | What conflicts or dependencies applied to each company-identifying assessment? | Applicable policy, personnel, money, access, disclosure, redaction and provider authority are recorded per project. |
| C09 | How did METR's funding and COI disclosures change over time? | Wayback/live differences have dated captures and do not substitute page appearance for transaction date. |
| C10 | Which parts of the response to the September 14 post are accurate, incomplete or incorrect? | Each sentence is adjudicated against C01–C09, with the posted and corrected figures distinguished. |

## 5. Investigation rules

- The unit of analysis is a proposition, not a node in a network. “X funded Y,” “X invested in Z,” “X and Y share a director,” and “X funded a project involving Y” are four different rows.
- A total is a reconciliation, not a collage. Every included row states why it is compatible with the denominator; every visually tempting but incompatible amount is listed as excluded.
- The public repository's own audits are evidence about the figure, not proof of external facts. External facts still require their primary source.
- The posted image is fixed at commit `f64df65`. Later fixes may improve the current repository but do not retroactively alter what readers saw.
- Search failures are reproducible records: exact term, endpoint, filters, result count, UTC, response hash and known blind spots.
- Dynamic grant databases are enumerated by canonical pages/APIs/sitemaps as well as keyword search. The Packard miss is the model for why.
- The terminal request is a residual instrument. Its questions are generated from missing cells after the public-source frontier closes, never used as a shortcut.

## 6. Lane map (IDs frozen)

Each lane writes one schema-conforming CSV plus saved primaries under `research/primary/<lane>/`. The engine-generated brief expands the lane into Tasks A–E: A–D cover the named source classes and required elements; E records bounded negatives and sources checked. Every lane first reads `research/STATE.md` and relevant reviewed sibling outputs.

### Wave 1 / S1 — METR's own funding and every named supporter

| Lane | Scope | Primary routes |
|---|---|---|
| MD01 | Recipient-side financial baseline: METR 990s, audited statements if public, revenue, restrictions, related entities, fiscal periods | IRS/CA registry/METR |
| MD02 | Packard: reproduce the $350K record, history, modification timeline, payment/commitment status | Packard grant DB/990-PF |
| MD03 | Pew: every grant database and filing route, exact METR/ARC aliases | Pew disclosures/990 |
| MD04 | Schmidt Sciences and Schmidt entities: amount, legal payer, purpose, investor-entity distinction | Schmidt sites/990s/issuer records |
| MD05 | Sijbrandij Foundation: grant, commitment, timing, restrictions, related vehicles | foundation site/990-PF |
| MD06 | LaCentra-Sumerlin, Astralis and Expa.org | entity sites/990-PF/registries |
| MD07 | “Individuals from Jane Street”: public acknowledgments only; firm/individual separation; no deanonymization | METR, donor self-statements, filings |
| MD08 | Farhi, Ralston, Field and Newman: public gifts/vehicles/timing; employment status at gift date | self-statements, DAF/stock filings, FEC only for employment corroboration |
| MD09 | SFF/Tallinn: every METR/ARC recommendation, match, legal recipient and paid-status evidence | SFF tables/Tallinn ledger/recipient filings |
| MD10 | Longview, Effektiv Spenden and pooled/regrant routes | grant pages/annual reports/990s |
| MD11 | Vanguard and other filed DAF grants to METR, refreshed beyond the closed adviser hunt | sponsor 990 Schedule I/B/M; recipient aliases |
| MD12 | ARC spinout and restricted-fund provenance | ARC/METR 990s, transfer documents, announcements |
| MD13 | Universal grant-database sweep: canonical pages, sitemaps/APIs and exact EIN/name aliases for all supporters | official databases/Candid only as locator |
| MD14 | Six-month window chronology and denominator compatibility | METR archives, all Wave 1 rows, fiscal/payment dates |

### Wave 2 / S2 — intermediaries, contracts and commitment reconstruction

| Lane | Scope | Primary routes |
|---|---|---|
| MD15 | Audacious partner list by date and project-funder rules | Audacious/TED live+Wayback, partner descriptions |
| MD16 | Canary award structure and all project-specific funder disclosures | METR/RAND/Audacious announcements |
| MD17 | RAND-side Canary receipts and directed grants | RAND reports/990s/funder filings |
| MD18 | METR-side Canary commitment, payments, term changes and restricted revenue | METR statements/990s/funder filings |
| MD19 | UK AI Security Institute grants/contracts and in-kind arrangements | Contracts Finder/Find a Tender/AISI publications |
| MD20 | EU AI Office technical-assistance contract and consortium share | TED/FTS/Commission documents |
| MD21 | US and other public-sector awards or agreements | USAspending/SAM/NIST/state records |
| MD22 | Intermediary recipient/payer returns: Longview, Founders Pledge, Every.org, Effective Ventures, relevant sponsors | IRS/foreign charity filings |
| MD23 | Restrictions and grant purposes across all identified support | grant letters/pages/filings/recipient disclosures |
| MD24 | Funding-page and donor-rule chronology | Wayback/CDX/live hashes |
| MD25 | Revenue, commitments, runway, headcount and expenditure reconciliation | recipient filings, job data, Barnes/METR budget statements |

### Wave 3 / S3 — independence, access and project terms

| Lane | Scope | Primary routes |
|---|---|---|
| MD26 | Tokens, credits, compute and engineering help by lab/project; quantify only when sourced | METR reports/lab acknowledgments |
| MD27 | Model access, safe harbor, NDAs, publication, redaction and silent-exit rights | assessment reports/agreements/policies |
| MD28 | February–March 2026 Frontier Risk Report team and COI process | report/AEF-1/policy timeline |
| MD29 | September 2026 Anthropic incident engagement: selection, scope, payment, subcontractors, RSP/LTBT applicability | Anthropic/METR/Redwood/RSP documents |
| MD30 | Project staff: direct equity, recent lab work, simultaneous work, close relationships, disclosures and recusals | report disclosures/bios/policy; public only |
| MD31 | Board/advisers and institutional governance safeguards | METR 990s/about/board bios/policy |
| MD32 | Direct lab payment and employee-directed donation negative sweep | lab disclosures, METR filings/pages, relevant DAF rules |
| MD33 | Donor-investor map with strict entity resolution | issuer announcements/SEC/court sales/donor records |
| MD34 | Compare terms and treatment across Anthropic, OpenAI, Google, Meta and Amazon projects | METR reports and provider statements |
| MD35 | External-evaluator independence standards compared to METR practice | AEF-1, government standards, published evaluator policies |
| MD36 | Evaluator-selection market and alternatives; who selected/endorsed METR for each role | procurement/RFI/company/government records |

### Wave 4 / S4 — document-producing routes and opaque vehicles

| Lane | Scope | Primary routes |
|---|---|---|
| MD37 | NPT public Schedule B Parts I–II and audit-note route; existing records only | §6104(d), NPT/PA filings |
| MD38 | SVCF and other DAF sponsor Schedule B/M and account-transfer evidence | sponsor filings/audits |
| MD39 | Good Ventures FY2026 and later arrival test | IRS/CA registry/990-PF |
| MD40 | Moskovitz Investments LLC, Monster Growth Ventures, family vehicles and purchaser/transfer evidence | state records/SEC/issuer records |
| MD41 | Remainder-interest trust: type and Form 5227/4506-A route | IRS/SEC/public trust records |
| MD42 | Anthropic S-1/holder tables/transfer rules and later securities disclosures | EDGAR/issuer charter and bylaws |
| MD43 | Audacious-partner and Canary funder calendar closers | 2025/2026 990-PF/annual reports |
| MD44 | UK/EU/US public-record requests for contract amounts/terms after procurement exhaustion | FOI/FOIA/Commission access-to-documents |
| MD45 | Calendar monitor: METR return, intermediary returns, investigation report, procurement updates | official release points only |

### Wave 5 / S5 — joins, refutation and outputs

| Lane | Scope | Output |
|---|---|---|
| MD46 | Full typed funding reconciliation | `commitment_reconciliation.csv` plus exclusions |
| MD47 | Entity and causal-edge audit | every graph edge classified as transaction/role/access/adjacency |
| MD48 | Project independence synthesis | `independence_matrix.csv` |
| MD49 | Claim-by-claim post/response adjudication | `research/CLAIMS.md` |
| MD50 | Money/provenance adversarial audit | `AUDIT-MONEY.md` |
| MD51 | Framing/entity/causality adversarial audit | `AUDIT-FRAMING.md` |
| MD52 | Frontier-driven gap generation and review | MD70–MD89 only where the engine shows a real gap |
| MD53 | Figures, bibliography, README verdicts and release lint | local artifacts only; no publication |

### Terminal / S6

| Lane | Scope | Output |
|---|---|---|
| MD99 | Single consolidated request for unresolved cells in the approximately $71M allocation, generated only from a passing exhaustion gate | `research/outreach/MD99-71m-allocation.md` |

MD54–MD69 are reserved. MD70–MD89 are gap/replacement lanes and must cite the finding that created them. MD90–MD98 are reserved for response verification if MD99 is sent. No lane is renumbered or repurposed.

## 7. Exhaustion gate before MD99

`research/EXHAUSTION-GATE.json` may be created only in S5 and must contain:

1. `slices_complete`: evidence pointers for S0–S5.
2. `frontier_command`: the exact `casework frontier` command, UTC, exit and full output hash.
3. `source_classes`: for each C01/C02 allocation element, every class is `COVERED` or `N/A-with-reason`; none is `UNTOUCHED`, and a `PARTIAL` has no currently actionable public route.
4. `named_supporters`: every METR-named supporter and filed payer has a current coverage row.
5. `records_routes`: approved statutory/public-record requests are produced, denied/appealed, explicitly declined by Kevin, or pending beyond the investigation's current bounded shift; an ordinary in-clock request prevents the gate.
6. `calendar`: every filing/document available as of gate UTC is ingested; future documents carry the next check date and do not masquerade as negatives.
7. `reconciliation`: every known amount has an inclusion/exclusion decision and money type; the residual cells to ask are enumerated.
8. `audits`: MD50 and MD51 both approve the gate or list resolved corrections.
9. `embargo_check`: no earlier outgoing draft or transmission asked for the allocation.
10. `reviewers`: two independent review receipts with hashes.

If any field fails, MD99 remains prohibited. The remedy is a targeted gap lane or wait state, not softer gate language.

## 8. Figures and written synthesis

Render only after MD50/MD51 corrections:

| Stem | Question answered |
|---|---|
| `metr-deep-01-71m-known-and-unknown` | Which compatible components of the commitment total are public, which are excluded, and how much remains unallocated? |
| `metr-deep-02-supporter-ledger` | Every named supporter: known amount/vehicle/date/purpose or exact public gap. |
| `metr-deep-03-independence-stack` | Direct money, in-kind resources, access authority, personnel COI and governance as separate layers. |
| `metr-deep-04-project-terms` | Provider-by-project comparison of compensation, access, disclosure, redaction and exit terms. |
| `metr-deep-05-provenance` | Only documented transactions into METR; adjacent organizations shown outside the money-flow layer. |
| `metr-deep-06-stock-question` | Known, excluded and unresolved vehicle evidence; no METR funding implication without an onward transaction. |

The flagship is not another all-network spaghetti graph. It is the typed reconciliation plus a visible unknown block. README states the posted/current version distinction, the strongest supported thesis, the strongest unsupported thesis, current filing calendar, and every outstanding document.

## 9. Review and promotion loop

For every landed lane:

1. Prepare the casework review package.
2. A reviewing agent checks every figure-capable row against the primary and assigns `CONFIRMED`, `DIFFERS` or `UNVERIFIABLE`.
3. Promote CONFIRMED; promote corrected DIFFERS with the original lane value in an audit note; leave UNVERIFIABLE in immutable lane output and bind it only as a gap/context where appropriate.
4. Re-run casework verify, readiness, frontier and state.
5. If the row opens a new material element, generate one targeted gap brief. If it merely adds detail without changing a claim, do not grow scope.

No lane result is a finding until this loop completes.

## 10. Supervision loop

Before the first launch, read `~/GROK_HEADLESS_GOAL.md` completely and probe accounts. Launch no more than eight lanes concurrently through the shared runner. The parent session appends wave open/close and every ten-minute tick to `research/SUPERVISION.jsonl`.

At each tick:

1. Read `lanes.py tick --pack metr_deep` and each lane's goal state/output.
2. If a lane is on brief, let it continue. If stuck or off brief, stop only through the runner that owns its recorded PID and launch a revised MD70–MD89 replacement.
3. Review completed output immediately; do not wait for the wave to finish.
4. Promote after review, then recompute frontier. Findings, not turn availability, determine follow-ons.
5. Close a wave only when every lane is reviewed/promoted or has a recorded replacement/pending-record state and casework verify is green.

Never resume a finished lane with a new objective, widen scope to use turns, poll by prompt/process pattern, or place launch logs inside the pack.

## 11. Calendar closers

Dates are re-measured and updated in `research/calendar.csv`; these are initial anchors, not live state:

| Earliest expected date | Document/event | Claims |
|---|---|---|
| Approximately 2026-11-04 | METR's Anthropic incident report if the initial eight-week schedule holds | C03, C04, C08 |
| 2026-11-16 | CY2025 filings: SVCF, Coefficient entities and other calendar-year intermediaries/funders | C01, C02, C06, C07 |
| 2026-11-15, extendable to 2027-05-15 | Good Ventures FY2026 990-PF | C05, C07 |
| As filed | METR's next Form 990 and any audited statements | C01, C02 |
| As published | Anthropic S-1 or holder disclosure | C05, C07 |
| Per request clock | NPT/FOIA/FOI/Commission productions | C01, C02, C06, C07 |

A future closer does not force the active investigation to idle if all current routes are exhausted, but the final report must say what could change when it arrives.

## 12. Definition of done

1. The public repository's strengths, defects and posted/current chronology are preserved in a reproducible baseline.
2. Every METR-named supporter and every public payer has a reviewed row or bounded negative.
3. The approximately $71M is reconciled as commitments, with every identified compatible component and every incompatibility visible.
4. Every material lab engagement has a project independence profile.
5. Every asserted cash-flow edge into METR is a documented transaction; all other relationships are visibly typed as something else.
6. The donated-stock vehicle is either identified by a document or bounded by the current record without being used as a substitute for a METR transaction.
7. Every current public source class and approved records route is covered; future documents are calendared.
8. Two adversarial audits pass after corrections; casework verify and release lint exit 0.
9. MD99 was not begun before the exhaustion gate. Its exact draft is either awaiting Kevin's authority, sent with a receipt, or explicitly waived by Kevin.
10. Nothing is published or pushed without a separate explicit instruction.

## Amendments

- **2026-09-15 (A1, initial plan):** The direct request for the approximately $71M allocation is deliberately terminal. S0–S5 must exhaust public, archival, filing, procurement, intermediary, project-document, statutory-record and adversarial-review routes first. This ordering is immutable except by a dated user amendment that explicitly changes it.

- **2026-09-16 (A2, concurrency):** Kevin confirmed in session that the shared runner now permits up to 30 concurrent Grok lanes per pack and 10 concurrent per account (tools/lanes.py changed 2026-09-16 00:03 local). The Guardrails rule "Eight concurrent lanes per pack" is raised to the runner's cap of 30 for this pack; the ten-per-account figure is now the runner's concurrent cap. Recorded in `LEDGER.jsonl` at this UTC. No other rule changes.

### Amendment A3 (2026-09-16, Kevin's instruction)

Every Grok lane launched for this plan runs at `--effort xhigh` and with no turn cap (`--max-turns 0`), never `medium`. Applies to all future launches (S3-S6, re-runs, audits MD50/MD51, MD99) and to any lane found running at a lower effort, which is stopped (only via the shared runner's recorded PID) and relaunched at xhigh; its lower-effort output is set aside and never promoted. Lanes that had already completed and been promoted at medium before this amendment (MD01-MD18, MD20-MD23, MD25) were reviewed against primaries and stand unless Kevin asks for a re-run.

### Amendment A4 (2026-09-16, Kevin's instruction: run as many Grok lanes as the runner allows)

Lanes may be *launched* ahead of their slice when their brief exists, their brief needs no promoted rows from an earlier slice as input, and the standing prohibitions (allocation embargo, no external transmission without Kevin's approval of the exact action) are carried in the brief. Launch-ahead applies to S3 (MD26-MD36) and S4 (MD37-MD45) while S2 is still closing. It does not apply to S5 (MD46-MD53), which audit and reconcile promoted rows and would be run against an incomplete state, nor to MD99. Review, promotion, Done-when checks and slice closure keep their original order: no S3 row is promoted before S2 is `[x]`, no S4 row before S3 is `[x]`, and the S4 `USER_AUTHORITY_WAIT` rule is unchanged (MD44 produces drafts only; nothing is sent). Under A3, the 23 lanes that completed at effort=medium (MD01-MD18, MD20-MD23, MD25) are re-run at xhigh into their original output paths; their medium outputs and primaries are archived first under `research/archive/medium-run-20260916/`; each xhigh re-run is reviewed like a new lane and promoted with `supersedes` where its rows differ from the promoted medium rows, and the medium reviews remain on record.

### Amendment A4.1 (2026-09-16, engine behaviour on xhigh re-runs)

The casework engine identifies a promoted row by its lane marker (`lane=<csv>#<row>`); an xhigh re-run that writes to the same CSV path with the same row keys therefore cannot duplicate or supersede a same-key medium row. Practice under A4: same-key rows are re-verified in the re-run review (recorded in `MDREVIEW-MDnn-xhigh.md`); where the re-run changed a material fact (url, target, money type, amount, date) the reviewer adjudicates the difference in that review and files a correction against the medium row when the medium row is wrong; rows added by the re-run are promoted normally. The medium review remains on record.

### Amendment A4.2 (2026-09-16, content-keyed adjudication of xhigh re-runs)

Row numbers shift between a lane's medium run and its xhigh re-run, so the marker-based dedupe in A4.1 is not a content check. Practice from this amendment: `scripts/rerun_diff.py <lane>` matches the xhigh rows to the archived medium rows by content (url, target prefix, money type, amount, date and subject), never by row number. Rows matching a promoted fact stay on the medium row (the medium review stands). Rows with no medium counterpart and candidate corrections are written to `research/rerun/<lane>-xhigh-added.csv` under `X<row>` (added) and `C<row>` (correction, `supersedes` prefilled with the medium row id) so their markers never collide, and are reviewed and promoted with `scripts/promote_lane.py <lane> research/rerun/<lane>-xhigh-added.csv --no-goal-check --review-suffix=-xhigh-added`. A correction supersedes the medium row only when the reviewer confirms the re-run's version (typically a stray money type or amount cleared from an aggregate, entity or negative row, or a missing date filled). Medium rows with no xhigh counterpart stand as promoted and are listed in the diff. Applied on 2026-09-16 to MD01-MD17, MD20-MD23 and MD25 (MD18 had no added rows); the earlier `-xhigh` promotions of MD02, MD15, MD18 and MD20 are unaffected.

### Amendment A5 (2026-09-16, Kevin's instruction: 20-lane cap)

The shared runner's per-pack concurrency cap is 20 (tools/lanes.py MAX_CONCURRENT = 20 as of 2026-09-16T16:40Z, lowered from 100 to keep host RAM in bounds). A2's 30 and the later 60/100 are superseded. Per-account cap stays 10. Launch order and slice rules are unchanged; the cap is a concurrency limit, not a budget.

### Amendment A6 (2026-09-16, Kevin's instruction: 15-agent cap)

The shared runner's per-pack concurrency cap is 15 (tools/lanes.py MAX_CONCURRENT = 15 as of 2026-09-16T19:05Z, lowered from 20). A5's 20 is superseded. Per-account cap stays 10. No more than 15 lanes run at any time; launch order, slice rules and the xhigh rule (A3) are unchanged.
