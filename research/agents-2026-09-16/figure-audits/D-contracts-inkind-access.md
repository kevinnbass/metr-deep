# Figure audit D — government/consortium contracts, in-kind resources, access and project terms, lab-cash negatives

Pack: `/mnt/f/projects/anthropic/metr_deep` (read-only). Audited 2026-09-16 against the promoted tables MDI (119 rows), MDQ (181), MDF (1032; 9 superseded skipped), MDP (744), MDS (1690; 18 superseded skipped), MDT (435; 2 superseded skipped), MDR (207) and the derived `independence_matrix.csv` (22 engagements). Companion JSON: `D-contracts-inkind-access.json` (607 row ids cited; every id verified present and not superseded).

Conventions. No currency is converted; no money types are summed; EUR is written as EUR. "Seed" = row imported by lane S0-seed-import from the 10-metr pack (context-only until re-verified); "lane" = row promoted from a reviewed MD lane. The `lane` column is empty on every row; provenance was read from `note` (`lane=research/grok-out/...`). Only public people in public roles are named, exactly as the rows name them. No motive language.

---

## 1. Government and consortium contracts

### 1.1 European AI Office / European Commission DG CNECT — TED 864574-2025, LOT-0003, contract 4500137790

| cell | value | rows |
|---|---|---|
| award id | TED contract award notice 864574-2025; LOT-0003; procedure EC-CNECT/2025/OP/0032; contract CON-0003; tender TEN-0003; legal commitment / EASE reference 4500137790 (FTS line 4500137790.00010, registration 2615985) | MDF0150, MDF0151, MDP0132 |
| contracting authority | European Commission, DG CNECT (CNECT.A Artificial Intelligence Office / CNECT.A.3 AI Safety). METR's wording: "a technical assistance contract with the European AI Office, supporting their approach and technical methods for assessing loss of control risks" | MDF0150, MDP0131, MDP0313 |
| legal recipient | tendering party TPA-0009 = EquiStamp Inc. (ORG-0009, group leader) + Model Evaluation and Threat Research, Inc. (ORG-0010, GroupLeadIndicator=false) + Epoch Artificial Intelligence, Inc. (ORG-0011). FTS 2025 names only EQUISTAMP INC. as beneficiary (invoicing party; consortium members may be omitted) | MDP0132, MDP0282, MDF0151, MDP0134 |
| value / currency | **EUR 1,167,484** — PayableAmount of the lot, i.e. the consortium total; not converted; not summed with LOT-0004 (EquiStamp, EUR 881,345) or other lots; award is not a receipt; FTS consumed=0 | MDF0150, MDF0151, MDF0236, MDS0834 |
| period | award decision 2025-11-28; IssueDate/conclusion 2025-12-15; planned duration 36 months; FTS project 15/12/2025–14/12/2028 | MDF0150, MDF0151, MDR0109 |
| METR's share | **not disclosed** anywhere published (TED XML, FTS, procurement docs 404); the lane rules say "do not infer 1/3"; subcontracting flagged yes with percentage/value unknown | MDP0132, MDP0133, MDP0137, MDS1610 |
| award criteria | quality 65 / price 35; narrative deferred to unpublished procurement documents | MDP0291, MDP0299 |
| about-page chronology | EU sentence first appears on metr.org/about in the 2026-01-27 → 2026-02-02 unique-digest window; "European AI Office" enters the supporter list by 2026-03-11 (page-change dates, not transaction dates) | MDT0068, MDT0069, MDT0430 |

Seed vs lane. Seed MDF0017 (S0 import; role=context; `amount_usd` holds text "undisclosed share of EUR 1,167,484 …") was re-verified by the MD20 lane from the live TED XML (MDF0150, sha256 373117f2…) and from the FTS 2025 dataset (MDF0151), re-checked by MD44 (MDF0236) and audited by MD50 (MDF0613, MDF0614, MDF0699 = match). MDP0051 and MDP0517 carry the seed as an "excluded, compatible=no" line in the $71M reconciliation.

Bounded negatives (all "none found in <source> as of <UTC>"):
- FTS 2025: no beneficiary METR / legal name / Epoch / ARC (MDS0373); FTS 2024: none of the aliases, EquiStamp or 4500137790 (MDS0374).
- TED expert search winner-name "Model Evaluation and Threat Research" → exactly one notice, 864574-2025 (MDS0367); "Alignment Research Center"/"ARC Evals" → 0 (MDS0375); "METR" → 22 Romanian school-equipment notices (MDS0376).
- TED XML has no signed-contract text and no METR share (MDS0834); Commission documents register JS shell (MDS0839); AskTheEU no prior request for 4500137790 (MDS0831).
- Funding & Tenders tender-details 404; eTendering empty (MDS0378); related notices 272332/450513/476039 HTTP 202 WAF = cap (MDS0372); live TED HTML/XML HTTP 202 empty in MD14/MD23/MD45/MD46 windows (MDS0341, MDS0507, MDS1142, MDS1179) but the daily-package XML succeeded (MDS1141, MDS0368).
- Unpublished and un-requested: signed contract text, tender specs, share annex; EASE route named; draft saved `approved_for_send: false` (MDP0135–MDP0137, MDP0309, MDP0310, MDP0316, MDP0319).

Table defects on this contract:
- `amount_usd` = 1167484 with `currency` = EUR on MDF0150, MDF0151, MDP0132, MDF0613, MDF0614, MDP0670. The column name is wrong for the content; a figure must key on `currency`.
- MDF0150 is DIFFERS (audit-1 filled `quantity_or_value` the lane left blank).
- MD50 audits MDF0480 (of seed MDF0017) and MDF0925 (of MDF0462) report "mismatch: to_entity not in primary" because the re-fetched primary was a jina rendering of the TED viewer shell; the substantive lot facts were separately audited as match on MDF0613/MDF0614/MDF0699.
- MDF0462 (MD23 rerun) has only the TED API search JSON as primary (notice body empty that window).

### 1.2 UK AI Security Institute (DSIT) — no award id, no published instrument

| cell | value | rows |
|---|---|---|
| award id | none found | MDS0523–MDS0527, MDS0536, MDS0816, MDS0822 |
| authority | DSIT / AI Security Institute (AISI is a DSIT directorate); earlier Frontier AI Taskforce | MDP0305, MDR0034, MDR0120 |
| recipient | METR ("partnering with the AI Security Institute"; AISI listed among supporters on metr.org/about); 2023 Taskforce partnership announced with ARC Evals (METR's former name) | MDF0016, MDP0197, MDR0034, MDR0035 |
| value / currency | **undisclosed**; no GBP figure. Adjacent GBP figures are programme ceilings, not METR amounts: Challenge Fund £50,000–£200,000 per project (notice 4113c27b, awards[] empty); Alignment Project £15m→£27m; nearest AISI Contracts Finder award is RAND Europe CNI Monitoring £348,959 (a different legal entity) | MDP0196, MDP0200, MDP0201, MDP0311, MDS0535 |
| period | undated. About page: "partnering with the AI Security Institute" first in the 2025-02-11→2025-02-15 window (MDT0066/0067); AISI in the funding paragraph from the 2025-12-03→2025-12-07 window (MDT0080/0081, MDT0428) |
| METR's share | not disclosed (no instrument) | MDP0204 |
| in-kind adjacent | AISI "worked with METR … including unpublished work by METR, at the Summit" (unquantified) (MDI0004, MDI0118, MDR0121, MDP0205); evals-bounty page "thank METR for their guidance and help" (MDI0005, MDI0116) |

Seed vs lane. Seed MDF0016 (money_type=contract, amount "undisclosed", date "undated") was audited as match by MD50 (MDF0479, with the note that its quote_300 is a research note, not a verbatim quote). MD19 lane rows MDP0196–MDP0205 and MDS0523–MDS0539 are new; MDP0196/0197/0200/0201 and MDS0535 are DIFFERS because audit-1 stripped the lane's `money_type=contract` (correct: the Challenge Fund notice and RAND Europe award are not METR contracts).

Bounded negatives: Contracts Finder v2 keyword METR / quoted legal name / quoted "ARC Evals" all hitCount=0 (MDS0523–0525, MDS0816); 34 AISI-named notices and 5 "AI Security Institute" notices name no METR supplier (MDS0526); Find a Tender JS shell (MDS0527); AISI /grants, example-projects, 60-awardee blog and the Alignment Project awardee PDF have no METR line — the PDF lists Alignment Research Center / Jacob Hilton, a separate entity (MDS0322, MDS0528–0530, MDS0534, MDS0537, MDS0833, MDP0199, MDP0202); DSIT £25k spend CSVs 2024–2025 (21 files) no METR supplier (MDS0532, MDS0538); DSIT FOI releases none (MDS0830, MDS0837, MDS0940, MDS0945, MDT0177); GOV.UK 2023 news distinguishes "working with" ARC Evals from "new contracts" with Advai/Gryphon/Faculty (MDP0198). UK FOIA draft unsent (MDP0314, MDP0317).

Table defects: MDI0005/MDI0116 and MDI0004/MDI0118 record from_entity=AISI, to_entity=METR, provider=METR for acknowledgements in which METR gave guidance/work to AISI — the in-kind direction is reversed relative to the from/to columns.

### 1.3 US NIST / CAISI — consortium membership and CRADA/DTA listing; no award

| cell | value | rows |
|---|---|---|
| award id | none; NIST AI Consortium (AISIC) member list names "Model Evaluation and Threat Research (METR, formerly ARC Evals)"; CAISI 2026-03-27 slide lists METR with Scale under "CRADAs and DTAs – Access to private benchmarks" | MDR0031, MDR0119, MDR0122, MDI0003, MDI0075, MDI0076, MDP0155, MDP0290 |
| authority | NIST / Center for AI Standards and Innovation | same |
| recipient | METR (member list); executed instrument not posted | MDP0153, MDP0302, MDP0312, MDS0829, MDS0836 |
| value / currency | not stated (no CRADA number, dollars, dates); a consortium CRADA is a membership condition, not a funded award | MDP0154, MDP0155, MDS0471 |
| period | slide 2026-03-27; member list 2026-09-03 / re-check 2026-09-16; "not stated on this slide" | MDI0003, MDR0122 |
| METR's share | n/a | |

USAspending / SAM / grants.gov negatives (all bounded to endpoint and date): recipient listing by legal name and by EIN 99-1219864 total=0 (MDS0452, MDS0456); spending_by_award grants results=[] from 2007-10-01 (MDS0453, MDS0598); award-count all zero (MDS0454); subawards [] (MDS0455); contracts legal-name [] (MDS0817, MDS0823); SAM SGS q=METR and q=EIN totalElements=0, Entity API needs key (MDS0458–0460, MDS0468, MDS0470, MDS1022); grants.gov keyword METR JS shell / 0 buckets, API 405 (MDS0339, MDS0599, MDS0750, MDS1181, MDS0654); Federal Register quoted phrase count=0 (MDS0463); NSF awardeeName=METR 0 (MDS0467); CanadaBuys/AusTender over-broad (MDS0473, MDS1023, MDS1024). Caps: GET 405 (MDS0451, MDS0105, MDS0241); POST 422/502/timeout (MDS1062, MDS0598); "METR" substring = METROPOLITAN* 28,513 hits (MDS0457); UEI never recovered (MDS0468, MDS0469). CAISI home page and the OpenMined CRADA announcement do not name METR (MDS0462, MDS0461, MDS0832). US FOIA draft unsent (MDP0308, MDP0315, MDP0318).

Table defects: MDP0315 DIFFERS (lane wrote target_prefix=MDI on a statutory-request row); MDS0463 DIFFERS (source_class normalised).

---

## 2. In-kind resources by provider and project

Quantified cells (a source gives a figure) — only these:
1. **~$400K API credits** (GPT-5.6 Sol) spent over six days of the OpenAI/Hugging Face investigation — METR's own estimate, single investigation, not an invoice, not annual. Rows: MDI0047 (blog), MDI0048 (PDF), MDI0009, MDI0035, MDI0036, seed MDI0002; audits MDI0077, MDI0079, MDI0080; MDQ0102. OpenAI's technical report is silent on credits (MDI0056).
2. **Approximately $600,000** — METR's valuation of free API credits stolen in its security incident; the granting "model developer" is unnamed. Rows: MDI0043, MDI0051; audits MDI0078, MDI0081; MDI0095.
3. Data counts, not money: ~1.2 million message-board entries; ~1300 transcripts; six days on premises (MDI0050, MDI0052, MDI0009).
4. A request, not a grant: FRR requested rate limits ≥4M input tokens/min, 1M output/min, 1K rpm (MDI0007).
5. Not a gift at all: FRR Table 3 "~$500–$5K (500M tokens)" is METR's per-task inference budget assumption (MDI0049) — must not be drawn as received in-kind.

Everything else is unquantified. Provider-by-project summary (full list with row ids in the JSON `in_kind` array):

| provider | project | in-kind type | quantity | rows | seed/lane |
|---|---|---|---|---|---|
| frontier AI companies (unspecified) | about page; funding update | "significant free tokens"; "a significant amount of free tokens" | unquantified | MDI0001 (seed), MDI0031, MDI0027, MDI0034, MDI0111 | seed re-verified by MD26/MD27 |
| OpenAI; Anthropic; Google DeepMind; Meta; Amazon | about page partnerships | "access and tokens" | unquantified, no per-lab split | MDI0032, MDI0074, MDI0006 | lane |
| OpenAI; Anthropic; xAI | home / risk-assessment pages | "access and tokens" | unquantified | MDI0033, MDT0136 | lane |
| OpenAI | HF investigation | free API credits; data dump; transcripts; on-prem; HPIM withheld | ~$400K est.; counts | MDI0009, MDI0010, MDI0035, MDI0036, MDI0047, MDI0048, MDI0050, MDI0052 | seed + lane |
| OpenAI | GPT-5 | 4 weeks' pre-release API; reasoning traces (some); background info | unquantified | MDI0012, MDI0038, MDI0054 | lane |
| OpenAI | gpt-oss-120b review | MFT draft; task/data descriptions; o4-mini transcripts (no live query access stated) | unquantified | MDI0030, MDS0675 | lane |
| OpenAI | Codex-Max | early checkpoint Nov 4; reasoning-trace endpoint Nov 5 without ZDR; compaction scaffolding | two weeks | MDI0013, MDI0040, MDI0055 | lane |
| OpenAI | GPT-5.6 Sol | final + railfree checkpoints via API; raw CoT via API; harness guide | unquantified | MDI0011, MDI0037, MDS0712, MDS0715 | lane |
| OpenAI | o1-preview/o1-mini | API access Aug 26/28, Sep 3 2024; CoT not accessible | unquantified | MDI0014, MDI0015, MDI0045, MDI0068, MDS0622 | lane |
| OpenAI | o3/o4-mini | earlier checkpoints; internal-eval subset | 3 weeks (METR) / 15 days (OpenAI) | MDI0016, MDI0039, MDI0069 | lane |
| OpenAI | GPT-4.5 | earlier checkpoint; internal-eval subset | 7 days / "a week" | MDI0017, MDI0041, MDI0070 | lane |
| OpenAI | monitorability work | reasoning-trace access | unquantified | MDI0046 | lane |
| OpenAI → ARC | GPT-4 (ARC era) | early access | unquantified | MDI0018, MDI0053 | lane |
| Anthropic | Opus 4.6 sabotage review | unredacted report; draft with proposed redactions; joint Slack; document comments | unquantified | MDI0020, MDI0029, MDI0066 | lane |
| Anthropic | agent-monitoring red team | internal systems access; staff time | 3 weeks; 1 staff (David Rein) | MDI0021, MDQ0108 | lane |
| Anthropic | R&D-section review | additional non-public materials | unquantified; no MDI row | MDQ0109, MDS0671 | lane |
| Anthropic | Aug 2026 Risk Report | continued pilot external review | unquantified | MDI0067 | lane |
| Anthropic, PBC | 2026-09-09 incident investigation | transcripts beyond window; employees may share confidential info; eight weeks; (Jul 30: "sampling access" — not restated Sep 9) | unquantified | MDI0019, MDI0058, MDI0071, MDI0072 | lane |
| Anthropic | Mythos Preview / 5.1 | pre-release testing; Anthropic-supplied information | unquantified | MDI0024, MDI0025, MDI0059, MDI0060 | lane |
| Anthropic → ARC | Claude 2 (ARC era) | model access; engineers finetuned a snapshot | unquantified | MDI0026, MDI0057 | lane |
| Anthropic | Claude 3.5 Sonnet | not stated | undisclosed | MDQ0111, MDS0668 | lane |
| Google DeepMind | FSF v1.0 | acknowledgement of METR expertise (given by METR) | unquantified | MDI0061; negatives MDS0701–0703, MDS0727, MDS0818 | lane |
| Meta | FRR participant only | complimentary access as participant | unquantified; no Meta-titled page | MDQ0098, MDS0783, MDS0700, MDS0718 | lane |
| Amazon | Nova Premier; Nova 2.0 Lite / Nova 2 | lab-supplied transcripts, logs, rubrics, judge notes (no live API stated) | unquantified | MDI0022, MDI0023, MDI0063–0065, MDI0073, MDS0614, MDS0713 | lane |
| Amazon | FMSF | acknowledgement of METR feedback (given by METR) | unquantified | MDI0062, MDQ0101 | lane |
| Amazon (+GDM, Anthropic, Magic, G42) | 2024 annual report | "credited METR for assistance establishing their first policies" (given by METR) | unquantified | MDI0044, MDQ0110 | lane |
| Amazon | FRR Table 2 | non-participant (public materials only) | none | MDQ0100, MDS0779 | lane |
| AISI (UK) | Summit showcase; evals bounty | unpublished METR work showcased; METR guidance (given by METR) | undisclosed | MDI0004, MDI0005, MDI0116, MDI0118 | lane |
| CAISI/NIST | CRADA/DTA slide | access to private benchmarks | not disclosed | MDI0003, MDI0075, MDI0076 | lane |
| unnamed developer | security incident | free API credits (stolen) | ≈$600,000 valuation | MDI0043, MDI0051 | lane |

METR's own statement on free resources — exact wordings and dates (no promoted row contains the phrase "significant free compute credits"):
- "though we make use of free compute credits" — about page, first 2025-07-14 capture (MDT0130); still on 2026-07-19 capture (MDT0131; seed MDT0002).
- "companies have provided access and compute credits" — donate footnote, 2026-02-05 capture, label "To date, September 2025" (MDT0129).
- "though we make use of significant free tokens" — about page from the 2026-08-04 capture and live (MDT0133, MDI0031, MDI0027).
- "frontier AI companies currently provide a significant amount of free tokens" — funding update 2026-08-14 (MDI0034, MDT0127).
- "Use of free compute credits is acceptable." — COI policy v1.0, 2026-08-28 (MDQ0014).
- FRR: "METR's work with nonpublic models and use of free tokens incentivize a cordial relationship with AI companies." (MDI0042).

---

## 3. Access and project terms per engagement (C04.E3)

Cell legend: **D** = documented in the engagement document (quote on the row); **DA** = documented absence (the document itself says the term was not requested / not present); **U** = undisclosed in checked documents (a bounded "none found" row exists); **U\*** = undisclosed with no evidence row at all.

| project (date) | provider | compensation | access | safe harbor | publication / redaction | exit | policy in force | staff-conflict disclosure |
|---|---|---|---|---|---|---|---|---|
| GPT-5 (2025-08-07) | OpenAI | U (MDQ0103) | D: 4 weeks; some reasoning traces (MDI0012, MDI0054) | U\* | D: standard NDA; comms/legal review and approval; "not true of any other METR reports" (MDQ0009, MDQ0021, MDQ0103) | U\* | D: none in force (MDQ0180) | U\* (MDR0113 relationship only) |
| gpt-oss-120b (2025-10-23) | OpenAI | U (MDQ0106, MDS0631) | D: MFT draft, descriptions, o4-mini transcripts (MDI0030) | U (MDS0631) | D: NDA required review and approval; one material edit (MDQ0025, MDQ0026, MDQ0029, MDQ0106) | U (MDS0631) | D: none (MDQ0180) | U\* |
| Codex-Max (2025-11-19) | OpenAI | U (MDQ0104) | D: early checkpoint; traces w/o ZDR; compaction (MDI0013, MDI0040, MDI0055) | U\* | D: standard NDA; comms/legal approval (MDQ0010, MDQ0104) | U\* | D: none (MDQ0180) | U\* |
| GPT-5.6 Sol (2026-06-26) | OpenAI | U (MDQ0105) | D: final + railfree; raw CoT via API (MDI0011, MDI0037) | U\* | D: standard NDA; comms/legal approval (MDQ0008, MDQ0020, MDQ0105) | U\* | D: none (MDQ0180) | U\* |
| Opus 4.6 sabotage review (2026-03-12) | Anthropic | U (MDQ0107) | D: unredacted report; draft w/ proposed redactions; Slack; comments (MDI0020, MDI0029) | U\* | D: mutual NDA; publication review; redaction of sensitive info; METR could flag redactions; one minor rephrase only; general veto as pilot (MDQ0023, MDQ0024, MDQ0027, MDQ0028) | U\* | D: none (MDQ0179) | DA: authors named, no CoI text (MDQ0041) |
| R&D-section review (2026-05-08) | Anthropic | U (MDQ0109) | D: additional non-public materials (MDQ0109) | U\* | D: publication review w/ redaction control; general veto as pilot; no redactions happened (MDQ0109) | U\* | D: none (MDQ0179) | DA (MDQ0043) |
| Frontier Risk Report (window 2026-02-16→03-16; pub. 2026-05-19) | Anthropic, Google, Meta, OpenAI | D: "did not request or receive compensation"; complimentary access (MDQ0051, MDQ0063, MDQ0096–0099, MDP0256) | D: complimentary access; API w/ CoT; requested rate limits; ZDR if possible; no training on tasks (MDI0007, MDI0008, MDQ0015) | DA: AEF-1 1.5 "Not requested" (MDQ0002) | D: no editorial control over final report; control over non-public info; may redact certain findings not the top-level summary sentence; draft ~1 week before; no approval rights (MDQ0003–0005, MDQ0016, MDQ0022, MDQ0053) | D: silent exit by either party; treated as never participated; whether any exited undisclosed (MDQ0003, MDQ0017) | D: none at project start; AEF-1 2.3 = No; COI v1.0 later (MDQ0044, MDQ0049, MDQ0080, MDQ0089–0091, MDQ0177) | D aggregate: "at least 6" unnamed; 2.5 recusal = Yes (unnamed); no formal process (MDQ0036, MDQ0045, MDQ0052, MDQ0064, MDQ0085) |
| OpenAI/HF investigation (2026-08-26) | OpenAI | D: "did not take payment"; free credits per policy (MDQ0102, MDS0591) | D: dump, transcripts, credits, 6 days on-prem; HPIM withheld; no infra access (MDI0009, MDI0010, MDI0047, MDI0050, MDI0052) | U\* | D: could describe scope/terms; OpenAI could redact any non-public info; feedback beyond redactions, METR edited tone/structure; METR didn't see OpenAI's report first (MDQ0006, MDQ0007, MDQ0018, MDQ0019) | DA: no silent-exit clause stated (MDQ0102) | D: none on 2026-08-26 (MDQ0046, MDQ0178) | D: Wijk, Cotra, Greenblatt named; 2026-09-13 footnotes on Cotra/Christiano (OpenAI SSC 2026-09-09) and Greenblatt/Barnes (not involved); PDF lacks footnotes (MDQ0038–0040, MDQ0046, MDS0632) |
| Anthropic incident investigation (agreement 2026-09-09; 8 weeks) | Anthropic, PBC | U: not disclosed on Anthropic page, METR X posts, Redwood X post (MDP0245); COI v1.0 general sentence only (MDQ0095) | D (issuer): transcripts beyond window; employees may share confidential info; Jul 30 "sampling access" not restated (MDI0019, MDI0071, MDI0072) | U (MDS0610) | U: not disclosed; METR says reports will describe terms (MDP0246, MDS0610) | U\* | v1.0 predates agreement; not stated as applied (MDQ0181) | U: investigators not named on Anthropic page (MDS0645); Greenblatt self-identifies (MDQ0094); Redwood subcontract terms undisclosed (MDR0079) |
| Amazon FMSF feedback | Amazon | U (MDQ0101) | n/a acknowledgement (MDI0062) | U\* | U (MDQ0101) | U (MDQ0101) | U\* | U\* |
| Amazon Nova Premier / Nova 2 | Amazon | U\* (MDP0250) | D (issuer): lab-supplied results/transcripts (MDI0022, MDI0023, MDI0073) | U (MDS0614) | U (MDS0614) | U (MDS0614) | U\* | U\* |
| Anthropic agent-monitoring red team (2026-03-25) | Anthropic | U (MDQ0108) | D: 3 weeks internal-systems access (MDI0021) | U\* | partly D: 26-page report to Anthropic; redacted copy inside METR; rights not stated (MDS0621) | U (MDS0621) | U\* | DA: David Rein named, no CoI text (MDQ0042) |
| o1-preview/o1-mini (2024-09-12) | OpenAI | U\* | D (MDI0014, MDI0015, MDI0045; CoT not accessible MDS0622) | U (MDS0611) | U (MDS0611) | U (MDS0611) | U\* | U\* |
| o3/o4-mini (2025-04-16) | OpenAI | U\* | D (MDI0016, MDI0069) | U (MDS0612) | U (MDS0612) | U (MDS0612) | U\* | U\* |
| GPT-4.5 (2025-02-27) | OpenAI | U\* | D (MDI0017, MDI0070) | U (MDS0613) | U (MDS0613) | U (MDS0613) | U\* | U\* |
| GPT-4o (2024-08-07) | OpenAI | U (MDQ0112) | U (MDQ0112) | U\* | U (MDQ0112) | U\* | U\* | U\* |
| Claude 3.5 Sonnet (2024-10-30) | Anthropic | U (MDQ0111) | U (MDQ0111) | U\* | U (MDQ0111) | U\* | U\* | U\* |
| Mythos Preview / 5.1 (2026-04-07 / 2026-09-01) | Anthropic | U\* | D (issuer): pre-release testing (MDI0024, MDI0025) | U\* | U (MDS0617) | U (MDS0617) | U\* | U\* |
| GDM FSF input | Google DeepMind | U\* | n/a acknowledgement (MDI0061) | U\* | U\* | U\* | U\* | U\* |
| GPT-4 / Claude 2 (ARC era) | OpenAI / Anthropic | U\* | D (issuer) early access to ARC (MDI0018, MDI0026) | U (MDS0615, MDS0616) | U (MDS0615, MDS0616) | U\* | U\* | U\* |

Observations across the grid:
- Only two engagements state compensation at all, both as "none, as METR states": FRR and the HF investigation (MDS1616). Every other compensation cell is undisclosed.
- Safe harbor is never granted in any document; the only explicit statement is FRR's "Not requested" (MDQ0002). AEF-1 lists it as a recommendation (MDQ0012).
- Exit rights are documented only for FRR (silent exit) and, as an absence, for HF (MDQ0102). The Opus 4.6 "general ability to veto publication" is a publication right, not an exit right.
- No METR personnel COI policy was in force on any engagement dated before 2026-08-28 (MDQ0177–MDQ0180); v1.0 predates only the 2026-09-09 Anthropic agreement and is not stated as applied (MDQ0181).
- Signed instruments are never published: FRR pilot agreement (MDS0620), OpenAI NDAs (MDS0611–0613, MDS0631), Anthropic agreement (MDS0610).

---

## 4. Direct lab-cash bounded negatives (row ids)

METR's own statements (issuer rule, not filing lines): MDT0124, MDI0031, MDI0027 (about: "has not accepted funding from AI companies"); MDT0127, MDS0607 (funding update: "have not accepted funding from these companies … do not accept donations made by or at the direction of their staff"); MDT0136 (home: "does not accept compensation for this work"); MDT0128, MDT0129 (donate footnote April/September 2025); MDQ0095, MDQ0014 (COI v1.0); MDS0590 (no lab named as a funder on any supporter list); MDS0591 / MDQ0102 (HF: "did not take payment from OpenAI").

METR's FY2024 Form 990 (2024-05-01→2024-12-31): no lab name in XML (MDS0585); Schedule B RESTRICTED (MDS0586); RelatedOrganizationsAmt 4,501,424 = ARC transfer (MDS0587); AllOtherContributionsAmt 9,101,611 unnamed (MDS0588); CYProgramServiceRevenueAmt 0, GovernmentGrantsAmt absent (MDS0589); MDS1617 restates. ProPublica full-text: 8 hits, none a lab (MDS0584). IRS index 2026: no lab-foundation or METR return (MDS0604).

Per lab:
- OpenAI / OpenAI Foundation (EIN 81-0861541): MDS0574 (foundation site), MDS0575 (People-First 208-grantee list), MDS0576 (TY2024 990 Schedule I, 22 rows, no METR); project docs silent on credits/payment MDI0056, MDS0714, MDS0786; openai.com 403 caps MDS0603, MDS0629.
- Anthropic, PBC: MDS0569, MDS0570, MDS0571, MDS0572, MDS0573, MDS0608 (news pages, sitemap, IRS index, incident research page); engagement compensation not disclosed MDP0245.
- Google DeepMind / Google.org / Google Foundation (EIN 20-1548253): MDS0577, MDS0578, MDS0579; FSF documents MDS0702, MDS0703, MDS0701, MDS0818.
- Meta Platforms, Inc.: MDS0580, MDS0581 (Newsroom; Wayback ai.meta.com), MDS0602 (HTTP 400 cap), MDS0700, MDS0718, MDS0726 (scaling framework), MDS0783 (no Meta page on metr.org).
- Amazon / AmazonSmile Foundation (EIN 46-2626883): MDS0582, MDS0609, MDS0583 (pre-METR 990-PF; XML GET hung), MDS1279 (MD50: MDS0583 is "unbounded in form"), MDS0713.
- Caps recorded as caps, not negatives: EDGAR efts 403/500 (MDS0596); CourtListener opinions 0 (MDS0597); TEOS 403 (MDS0595); Candid login (MDS0600); r.jina.ai 403 (MDS0601); CA OAG landing (MDS0605); no statutory request sent (MDS0606); press not used as money source (MDS0607).

---

## 5. Contradictions and differences recorded in the tables (not reconciled by the pack)

1. GPT-5 report: comms/legal approval "is not true of any other METR reports shared on our website" vs identical sentence on later Codex-Max and Sol posts (MDQ0009 vs MDQ0104/MDQ0105; MDS0780 none-found for an explanation).
2. FRR Table A.1 2.5 "recused any individuals with a significant financial interest … Yes" vs preamble "did not run a formal recusal or disclosures process" — both on the same page; MD35 grades this "undetermined" (MDQ0064, MDQ0085).
3. Access-window wording: o3 three weeks (METR) vs 15 days (OpenAI) (MDI0016/MDI0069); GPT-4.5 "a week prior" vs 7 days (MDI0017/MDI0070); o1-preview-early named on the OpenAI card and METR's access paragraph but omitted on METR's summary sentence (MDI0014/MDI0015/MDI0045/MDI0068).
4. HF credits: METR states ~$400K; OpenAI's technical report does not mention credits (MDI0047 vs MDI0056).
5. Anthropic Jul 30 "sampling access to the relevant models" vs Sep 9 transcripts + employees only (MDI0072 vs MDI0071).
6. Provider list: about page (OpenAI, Anthropic, Google DeepMind, Meta, Amazon) vs home/risk-assessment (OpenAI, Anthropic, xAI) (MDI0032 vs MDI0033).
7. Amazon: named partner and token provider on the about page, credited in the 2024 annual report and FMSF, yet a Table 2 non-participant in the FRR with no explanation in any checked document (MDI0032, MDI0044, MDI0062, MDQ0100, MDS0779).
8. Within the tables — HF investigation window: "June 26–July 13, 2026" (MDI0009) vs "July 7–13" (MDQ0102). FRR window: "Feb 16–Mar 16, 2026" (MDI0007, MDQ0048, MDQ0089) vs "Feb–May 2026 assessment window" (MDQ0096–MDQ0099).

## 6. Table defects (all tables, this topic)

- `amount_usd` carrying non-USD or non-numeric content: MDF0150, MDF0151, MDP0132, MDF0613, MDF0614, MDP0670 (1167484 EUR); MDF0017 (text); MDF0014 ("EUR 128,000"); MDP0045, MDP0483, MDP0511 (128000 EUR). Key on `currency`.
- Inconsistent `amount_usd` for the ~$400K estimate: MDI0009/MDI0077 = 400000; MDI0047/MDI0048 empty by design; MDP0652/MDP0671 = 400000 resolving to MDI0047; MDP0672 = 600000 resolving to MDI0043 (empty).
- Direction reversed on acknowledgement rows: MDI0005, MDI0116 (provider=METR while from=AISI, to=METR); MDI0004, MDI0118 similar; MDI0061, MDI0062, MDI0044 are acknowledgements of METR's input typed as in-kind to METR.
- MDI0044 quote_300 is four words ("Amazon credited METR for assistance"); the full sentence is on MDQ0110.
- MD50 audit mismatches on entity-name form only: MDI0080, MDF0480, MDF0925.
- DIFFERS verdicts in scope: MDF0150, MDQ0051, MDQ0063, MDP0196, MDP0197, MDP0200, MDP0201, MDP0315, MDS0535, MDS0463, MDS0317 (all audit-1 field normalisations; read the promoted field).
- independence_matrix.csv and figures/metr-deep-04 cite MDQ0094 (Greenblatt X post) as the bounding row for the Anthropic engagement's compensation/terms; the bounding rows are MDP0245, MDP0246, MDS0610. MDQ0142's quote/date come from the X post while its url is the Anthropic page.
- Matrix bounded-negative gaps: gpt-5-1-codex-max and amazon-fmsf have negative_rows=0.
- Seed rows are context-only: MDI0001, MDI0002, MDF0016, MDF0017, MDQ0001, MDT0002 — each has a lane re-verification (listed in the JSON cautions), except that MDF0017's MD50 audit (MDF0480) is a jina-shell mismatch.
- `lane` column empty on all 3,000+ rows; lane must be parsed from `note`.

## 7. Suggested figures (details and row lists in the JSON)

- **D1** Three public-sector relationships card (EU / UK / US): id, authority, recipient(s), value as written in its own currency, period, METR share, instrument published?, bounded negatives.
- **D2** In-kind ledger: provider × resource type; only two quantified cells (~$400K; ≈$600,000) plus data counts; a separate "given by METR" band for acknowledgements; ARC-era band; MDI0049 excluded or labelled as METR's own budget.
- **D3** C04.E3 project-terms grid with the D / DA / U / U\* legend above and per-cell row ids; replaces figure 04's MDQ0094 citation with MDP0245/MDP0246/MDS0610.
- **D4** Timeline of METR's own wording (donate footnote → "free compute credits" → "significant free tokens" → funding update → COI v1.0 → HF "did not take payment" → Sep 13 footnotes), every date labelled as a page-change or post date.
- **D5** Lab-cash negatives matrix: lab × source class, "none found as of 2026-09-16" vs cap cells shaded separately; Schedule B redaction and the unnamed 9,101,611 line shown as blind spots.
- **D6** METR-vs-lab wording pairs (o1, GPT-4.5, o3, GPT-5, Codex-Max, HF credits, Anthropic Jul 30 vs Sep 9) as observations only.

Existing figures 03 (independence stack) and 04 (project terms) already cover the top-level in-kind and terms story; D2–D4 add the per-provider quantification rule, the explicit undisclosed-cell inventory with negative row ids, and the dated wording history that figure 03 compresses into a single "significant free tokens" quote.
