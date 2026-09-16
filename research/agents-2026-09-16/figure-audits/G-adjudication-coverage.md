# G — Adjudication and coverage audit (metr_deep)

Built 2026-09-16T19:35:33Z from the pack at /mnt/f/projects/anthropic/metr_deep (read-only). Companion JSON: G-adjudication-coverage.json. No motive is asserted; the posted figure's text is quoted only as the claim under adjudication.

## 1. C10 adjudication tables

Posted claims (MD49 Task C, element C10.E3): 16 rows, promoted MDP0569-MDP0584. Verdicts: {'incomplete': 11, 'undetermined': 3, 'accurate': 2}.
METR-attributed response sentences (MD49 Task B, element C10.E2): 6 rows, promoted MDP0563-MDP0568. Verdicts: {'undetermined': 3, 'incomplete': 3}.
All 22 rows are review_verdict CONFIRMED, source_class archives (posted) or issuer statements (response), strength supporting. The MD49 lane also promoted 12 hash rows (MDP0551-MDP0562, C10.E1), 10 bounded none-found searches (MDS1227-MDS1236), 22 settling-document rows (MDS1237-MDS1258) and 10 Task E re-checks (MDS1259-MDS1268); 76 rows in all.

### 1a. Posted claims

| row | id | posted claim | verdict | missing document | what the pack establishes | rows |
|---|---|---|---|---|---|---|
| C01 | MDP0569 | Posted metr-01: Good Ventures, advised by Coefficient, has no METR grant on its books | incomplete | Good Ventures Foundation Form 990-PF TAX_PERIOD=202606 (FY2026, year beginning 2025-07-01 ending 2026-06-30) Part XV vs METR EIN 99-1219864 | Good Ventures Foundation's 990-PF Part XV carries no METR grantee line in the filings checked through FY2025 (2024-07-01 to 2025-06-30) (MDS1015; MDS1016), Coefficient's own 2025 staff note states METR is not a Coefficient Giving grantee (MDP0053), and no FY2026 990-PF (TAX_PERIOD 202606) is in the IRS e-file index (MDS0947), so the present-tense 'no METR grant on its books' is bounded to filings ending 2025-06-30. | MDS1015; MDS1016; MDP0053; MDS0947 |
| C02 | MDP0570 | Posted metr-01: ARC handed METR $4.55M at the spin-out, not attributable to any one ARC funder | incomplete | ARC FY2024 Form 990 Schedule I grant agreement (cash vs non-cash split is already filed: MDF0064 CashGrantAmt 4477169 and MDF0065 NonCashAssistanceAmt 76766) | ARC's FY2024 Form 990 Schedule I files a cash grant of $4,477,169 (MDF0064) and non-cash assistance of $76,766 in computers at book value (MDF0065) to METR dated 2024-04-30 with purpose PROGRAM SPIN-OFF, not attributable to any one ARC funder; the posted $4.55M is reached only by adding cash to in-kind, which the pack's money-type rule forbids (seed MDF0007 4553935 is context only). | MDF0064; MDF0065; MDF0007 |
| C03 | MDP0571 | Posted metr-01b: Series A investors include two board observers by their own account | incomplete | a first-person Tallinn statement that he is an Anthropic board observer (his public words decline a board seat: MDR0090); Anthropic issuer observer roster | Moskovitz's Series A participation (MDR0082) and his self-described observer status (MDR0089) are held, and Tallinn led the Series A (MDR0080), but Tallinn's own dated words decline a board seat (MDR0090) and his observer status is press-reported only (MDR0026), so one observer 'by his own account' is established, not two. | MDR0082; MDR0089; MDR0080; MDR0090; MDR0026 |
| C04 | MDP0572 | Posted metr-01b: Moskovitz donated a stake now worth up to $7.7B to what he calls our foundation; no filing shows where it sits | incomplete | Good Ventures Foundation FY2026 Form 990-PF Schedule B/M (calendar closer MDT/MDS0947) or a public Anthropic S-1 Item 403 holder table (MDS0938) | The pack holds Forbes's 'less than 0.8%' bound as seed context (MDT0005), the Series H $965B figure as a round valuation rather than a holder stake (MDR0008; MDR0087), Moskovitz's own words on the observer role and 'our foundation' (MDR0089), and a Good Ventures FY2025 Part XV with no METR line that does not identify the stake (MDS1016); the stake's location stays a C07 open point with the settling documents named (GV FY2026 990-PF, MDS0947; a public S-1, none found, MDS0938). | MDT0005; MDR0008; MDR0087; MDR0089; MDS1016; MDS0947; MDS0938 |
| C05 | MDP0573 | Posted metr-07: 22 documents on a FINRA for AI; only a podcaster, Amodei and Sacks name METR | undetermined | the 22-document corpus with a METR-name hit table (figure cites F-rows in the seed clone; those F-rows are not promoted metr_deep pack rows) | No promoted MDE/MDP/MDS row is a 22-document FINRA-for-AI census; the figure's F-rows live in the seed clone and are not pack rows, so the pack establishes nothing about the 22-document count either way. |  |
| C06 | MDP0574 | Posted metr-10: both TIME100 AI profiles of METR's CEO were written by a Tarbell fellow; Coefficient funds Tarbell; neither profile disclosed it | undetermined | TIME100 AI 2024 and 2026 bylines for Beth Barnes; Tarbell Center fellow roster for those years; Coefficient/Open Philanthropy grant pages to Tarbell Center (figure cites TB01–TB04, not promoted here) | No promoted row is a TIME100 byline, a Tarbell fellow roster or a Coefficient-to-Tarbell grant page; Tallinn ledger lines to the Tarbell Fellowship exist only as locators inside MD23/MD33 primaries and were not promoted, so the pack establishes nothing about the two profiles. |  |
| C07 | MDP0575 | Posted metr-11: METR's funders who also hold a piece of the labs it evaluates | incomplete | a documented Moskovitz/Coefficient paid_grant or commitment to METR (none in promoted rows; MDP0053 says METR is not a Coefficient grantee) | The pack holds Moskovitz's and Tallinn's Series A investments in Anthropic (MDR0082; MDR0080), Coefficient's statement that METR is not its grantee (MDP0053) with no Good Ventures Part XV line for METR (MDS1015; MDS1016), and METR's stated refusal of AI-company cash (MDI0031), so 'investor in a lab' is established while 'METR funder' is not, for the Moskovitz/Coefficient side. | MDR0082; MDR0080; MDP0053; MDS1015; MDS1016; MDI0031 |
| C08 | MDP0576 | Posted metr-12: METR raised $71M in the six months the evaluator's seat was being designed; investigations came after the money | incomplete | METR's commitment ledger with dates inside February–August 2026 (composition embargoed; remainder MDP0055/MDP0056) | METR's own words are 'commitments of around $71 million' in the last six months to 2026-08-14 (MDF0001), the only compatible identified addend is Packard's $350,000 with an unresolved remainder around $70.65M (MDP0055; MDP0056), the Frontier Risk Report was published 2026-05-19 inside the window (MDQ0048) and the Hugging Face investigation 2026-08-26 after the statement (MDI0035); 'the evaluator's seat being designed' is not a dated pack fact. | MDF0001; MDP0055; MDP0056; MDQ0048; MDI0035 |
| C09 | MDP0577 | Posted metr-13: Redwood's board held the funder's co-CEO, Anthropic's future trustee and METR's future staffer | undetermined | Redwood Research Form 990 Part VII / board minutes naming Karnofsky, Christiano and Cotra as directors, plus the METR–Redwood subcontract for the Anthropic investigation (terms undisclosed on METR pages; MDI/MD29) | MD29 records METR's Anthropic incident engagement, but no promoted row is a Redwood Research board roster or the METR-Redwood subcontract, so the pack establishes the engagement and not the board composition. |  |
| C10 | MDP0578 | Posted metr-14: Stop pretending METR is independent — Amodei names it, Altman signs on, Sacks objects, no METR reply found | incomplete | a METR_Evals or Barnes/Painter post between 2026-09-11 and 2026-09-14 16:55 UTC (posted-image commit time) that replies to Amodei/Sacks; this-run B01/B06 found none after 2026-09-14 | This-run searches found no METR reply on metr.org/blog (MDS1227, lane row B01) or on @METR_Evals (MDS1232, lane row B06) after 2026-09-14, and the NY Post 2026-09-15 spokesperson sentences (MDP0563; MDP0564) do not name the Amodei or Sacks posts; the Sep 11-14 X thread before the posted commit was not reconstructed post by post. | MDS1227; MDS1232; MDP0563; MDP0564 |
| C11 | MDP0579 | Posted metr-15: of twenty possible evaluators, nine hold Coefficient awards, one refuses lab money; three put forward this week were METR, Stanford and Hugging Face | incomplete | the 20-organization evaluator census with Coefficient index hits (figure's 2,911-row index snapshot) promoted as pack rows; Amodei 2026-09-09 essay naming METR | METR's own rule refusing AI-company funding (MDI0031) and a bounded none-found for Anthropic, OpenAI, Google DeepMind, Meta or Amazon as a funder on about/donate/funding-update (MDS0590) establish 'one refuses lab money'; the 20/9/3 evaluator census is not a promoted MD36 row. | MDI0031; MDS0590 |
| C12 | MDP0580 | Posted metr-17: Vanguard DAF money to the AI-safety cluster grew from $8M to $66M; no filing says whose it is | incomplete | Vanguard Charitable FY2023–FY2025 Schedule I lines with a stated cluster definition (the $8.2M/$65.6M body totals are not a promoted pack total; money types/grantees must stay unsummed) | Vanguard Charitable's FY2025 Schedule I $4,000,000 filed grant to METR is held (MDF0012; MDF0154) with the account principal undisclosed (MDS0215, restated in bounded form as MDS1104); the $8M-to-$66M cluster growth sums many grantees and is not a promoted pack total. | MDF0012; MDF0154; MDS0215; MDS1104 |
| C13 | MDP0581 | Posted metr-18: no direct Coefficient grant to METR in checked index/filings; ARC program transfer and Coefficient award to RAND partner exist | accurate |  | Accurate: Coefficient says METR is not its grantee (MDP0053), Good Ventures Part XV has no METR line (MDS1015; MDS1016), the ARC-to-METR program transfer is filed (MDF0064) and a $10M Open Philanthropy/Coefficient award to RAND in support of Canary exists (MDS0808). | MDP0053; MDS1015; MDS1016; MDF0064; MDS0808 |
| C14 | MDP0582 | Posted metr-21: METR graded its own independence in May 2026 — two No answers, no CoI policy, at least 6 close personal ties | accurate |  | Accurate: the Frontier Risk Report Table A.1 states no personnel conflict-of-interest policy at project start (MDQ0048), item 2.3 answered No (MDQ0049; MDQ0082) and 'at least 6' close personal relationships (MDQ0054; MDQ0083); the live COI policy v1.0 is dated 2026-08-28 and is not applied backward (MDQ0091). | MDQ0048; MDQ0049; MDQ0054; MDQ0082; MDQ0083; MDQ0091 |
| C15 | MDP0583 | Posted README lede: funders reach METR through parent, partner, pooled-fund donor, board org, contractor, office and a journalism fellowship | incomplete | documented transactions into METR for each named path (ARC transfer is documented MDF0064; Canary/Audacious is a commitment to RAND+METR MDF0005 with filed payments to RAND not METR; Longview is a 2023 recommendation MDF0013; FAR.AI/Gleave is a board role MDR0093 not a METR grant; Redwood subcontract terms undisclosed; Constellation office is not a grant; Tarbell is undetermined — C06) | Each path is a different edge type: the ARC program transfer is a filed transaction (MDF0064), Audacious/Canary is a commitment to RAND+METR with filed payments to RAND not METR (MDF0005), Longview is a 2023 $220,000 public-fund recommendation (MDF0013), Adam Gleave's FAR.AI link is a METR board role not a grant (MDR0093), the Redwood subcontract terms are undisclosed, the Constellation office is not a grant and the Tarbell path is undetermined. | MDF0064; MDF0005; MDF0013; MDR0093 |
| C16 | MDP0584 | Posted metr-01 body: Canary ~$38M (~$21M RAND, ~$17M METR; METR later a bit under $16m); filed payments found to RAND none to METR | incomplete | a METR-side Canary payment line on METR's next Form 990 or a funder 990-PF naming METR as Canary payee (MD18/MD17 held: no such payment found through checked filings) | The ~$38M joint Audacious commitment (MDF0005), METR's ~$17M share (MDF0006) and Barnes's later 'a bit under $16m' (MDF0004) are held as commitments dated 2024-2025, outside the Feb-Aug 2026 window (MDP0055 exclusions); filed Valhalla and High Tide payments are to RAND, not METR (MDP0467; MDP0468); the ~$21M RAND share is a subtraction bound only as context. | MDF0005; MDF0006; MDF0004; MDP0467; MDP0468; MDP0055 |

### 1b. METR-attributed response sentences (NY Post, 2026-09-15)

| row | id | sentence (source) | verdict | missing document | what the pack establishes | rows |
|---|---|---|---|---|---|---|
| B11 | MDP0563 | METR spokesperson sentence 1 in NY Post 2026-09-15 (does not name the 2026-09-14 post) | undetermined | a METR-authored statement on metr.org that both (a) repeats or withdraws this sentence and (b) names the 2026-09-14 figure | No promoted C01-C09 row tests a purpose statement, and ten bounded searches (MDS1227-MDS1236) found no metr.org, X, GreaterWrong or EA Forum origin for the sentence; the NY Post text is held as the only capture. | MDS1227; MDS1228; MDS1229; MDS1230; MDS1231; MDS1232; MDS1233; MDS1234; MDS1235; MDS1236 |
| B12 | MDP0564 | METR spokesperson sentence 2 in NY Post 2026-09-15 (funder control + no AI-company funding) | incomplete | METR grant agreements (funder-control clause) plus a lab-by-lab cash negative already held as MDS0590/MD32; a metr.org restatement that names the 2026-09-14 figure | METR's standing About text refuses AI-company funding while acknowledging significant free tokens (MDI0031; MDI0034) and a bounded none-found holds for any named lab as a funder on about/donate/funding-update (MDS0590); the 'funders have no say' clause has no public instrument among promoted rows. | MDI0031; MDI0034; MDS0590 |
| B13 | MDP0565 | METR official by phone: EA overlap and diverse ideological viewpoints (NY Post 2026-09-15) | undetermined | a METR-authored statement (metr.org or named official) that both (a) states or withdraws EA-overlap / viewpoint-diversity wording and (b) names the 2026-09-14 figure | No promoted row is a METR self-statement of EA overlap or staff viewpoint diversity, and the pack's bounded searches of metr.org and the named officials' accounts (MDS1227-MDS1236) found no origin, so nothing is established beyond the press paraphrase. | MDS1227; MDS1228; MDS1229; MDS1232; MDS1233; MDS1234; MDS1235; MDS1236 |
| B14 | MDP0566 | METR official: required to disclose COI including employee equity in investigated firms | incomplete | a named company-identifying assessment after 2026-08-28 with named staff equity disclosures under COI policy v1.0 (metr.org/coi-policy.pdf) | COI policy v1.0 dated 2026-08-28 scopes company-identifying assessments (MDQ0113); the May 2026 Frontier Risk Report had no personnel CoI policy at project start (MDQ0048) and disclosed 'at least 6' unnamed close personal relationships rather than named equity holdings (MDQ0054); the policy is not applied backward (MDQ0091). | MDQ0113; MDQ0048; MDQ0054; MDQ0091 |
| B15 | MDP0567 | METR official: no compensation from AI labs and no donations from lab executives or employees | incomplete | a METR restatement that names the 2026-09-14 figure and separates lab cash/donations from in-kind tokens/credits (already held MDI0031;MDI0047) | METR's standing text refusing lab cash and lab-staff donations (MDI0031; MDP0279) and the bounded lab none-found (MDS0590) hold the sentence's two refusals, while the same pages and the Hugging Face report document in-kind tokens and credits separately (MDI0031; MDI0047 ~$400K API credits; MDQ0051 complimentary access), never summed with cash. | MDI0031; MDP0279; MDS0590; MDI0047; MDQ0051 |
| B16 | MDP0568 | METR official: 2022 Moskovitz donation to ARC was firewalled and not used for METR operations | undetermined | ARC or METR instrument (grant restriction, spin-out agreement, or audited note) stating the 2022 Open Philanthropy/Coefficient awards to ARC were excluded from METR operations and from the 2024-04-30 program transfer | Promoted MDF0066 ($265,000) and MDF0067 ($1,250,000) are 2022 Open Philanthropy recommendations to Alignment Research Center for general support, not a named Moskovitz personal gift, and MDF0064 is the 2024-04-30 ARC-to-METR spin-off transfer not attributable to any one ARC funder; no promoted row states a firewall. | MDF0066; MDF0067; MDF0064 |

None of the six sentences names the 2026-09-14 figure; each row records that in its note. The quoted sentences are in the JSON (quote_300).

## 2. Claims C01-C10

### C01 — The approximately $71M commitment total

Verdict: supported on primary sources (supported=true, supported_primary=true, contested=false).

| element | evidence | primary | negatives | state | owner lane | source classes | text |
|---|---|---|---|---|---|---|---|
| C01.E1 | 4/1 | 1 | 1 | ready | MD14-six-month-chronology | issuer statements, archives | METR's own statement of the approximately $71 million total, with its date, the period it covers and the money type it uses |
| C01.E2 | 4/1 | 4 | 4 | ready | MD02-packard-grant | issuer statements, funder filings, public grant databases, press | Each publicly identified commitment compatible with that denominator's period and money type, with named source, amount and date |
| C01.E3 | 81/1 | 36 | 36 | ready | MD01-metr-recipient-baseline | recipient filings, funder filings, public grant databases, issuer statements | Every known METR amount excluded from the denominator, each with the stated reason it is not comparable |
| C01.E4 | 31/1 | 3 | 1 (live 3) | ready | MD14-six-month-chronology | issuer statements, recipient filings | The unresolved remainder or range, computed mechanically from the denominator minus the identified compatible components |
| C01.E5 | 27/1 | 2 | 48 | ready | MD13-grant-database-sweep | public grant databases, IRS TEOS and e-file index, DAF sponsor filings, archives | Bounded negatives naming each grant database, filing and archive checked for a February-August 2026 commitment with no responsive record |

Open elements: none

### C02 — Who has funded METR

Verdict: supported on primary sources (supported=true, supported_primary=true, contested=false).

| element | evidence | primary | negatives | state | owner lane | source classes | text |
|---|---|---|---|---|---|---|---|
| C02.E1 | 135/1 | 10 | 64 | ready | MD70-named-supporter-list-capture | issuer statements, archives | METR's own named-supporter list with the capture date and page version it was taken from |
| C02.E2 | 129/1 | 54 | 180 (live 182) | ready | MD02-packard-grant | funder filings, public grant databases, recipient filings, issuer statements | Amount, date, vehicle, purpose and payment status for each named supporter, or a bounded negative listing the exact sources checked |
| C02.E3 | 167/1 | 13 | 105 | ready | MD01-metr-recipient-baseline | recipient filings, funder filings, DAF sponsor filings, IRS TEOS and e-file index | Every payer to METR found in recipient-side or funder-side filings that METR does not name |
| C02.E4 | 32/1 | 22 | 14 | ready | MD01-metr-recipient-baseline | recipient filings, IRS TEOS and e-file index, state registries | METR's recipient-side revenue, restrictions, related entities and fiscal periods from its own filings |
| C02.E5 | 37/1 | 14 | 96 | ready | MD09-sff-tallinn | funder filings, DAF sponsor filings, public grant databases | Pooled, regrant and recommendation routes typed as recommendation or transfer rather than as donor identity |

Open elements: none

### C03 — Frontier-lab money and employee-directed donations

Verdict: supported on primary sources (supported=true, supported_primary=true, contested=false).

| element | evidence | primary | negatives | state | owner lane | source classes | text |
|---|---|---|---|---|---|---|---|
| C03.E1 | 15/1 | 11 | 1 | ready | MD24-funding-page-chronology | issuer statements, archives | METR's stated rule on funding from AI companies and on employee-directed donations, with the dated versions of that rule |
| C03.E2 | 3/1 | 1 | 25 | ready | MD32-lab-money-negative-sweep | recipient filings, issuer statements, project documents, funder filings | Any direct payment or contract from Anthropic, OpenAI, Google DeepMind, Meta or Amazon to METR, or a bounded negative naming the sources checked |
| C03.E3 | 9/1 | 3 | 30 | ready | MD08-named-individual-donors | DAF sponsor filings, IRS TEOS and e-file index, issuer statements | The intermediary and donor-advised routes that could carry lab-employee money, and the exact point at which public verification stops |

Open elements: none

### C04 — In-kind resources and access

Verdict: supported (no primary-strength evidence on at least one element) (supported=true, supported_primary=false, contested=false).

| element | evidence | primary | negatives | state | owner lane | source classes | text |
|---|---|---|---|---|---|---|---|
| C04.E1 | 42/1 | 18 | 65 | ready | MD19-uk-aisi-contracts | project documents, issuer statements, self-statements | Tokens, credits, compute and engineering support by provider and project, quantified only where a source gives a figure |
| C04.E2 | 78/1 | 52 | 7 | ready | MD27-access-and-project-terms | project documents, issuer statements | Model access, safe harbor, publication, redaction and exit terms for each engagement |
| C04.E3 | 2/1 | 0 | 18 | OPEN: primary | MD27-access-and-project-terms | project documents, issuer statements, archives | An explicit record of which terms are undisclosed and which documents were checked for them |

Open elements: C04.E3 (primary)

### C05 — Supporter connections to Anthropic

Verdict: supported on primary sources (supported=true, supported_primary=true, contested=false).

| element | evidence | primary | negatives | state | owner lane | source classes | text |
|---|---|---|---|---|---|---|---|
| C05.E1 | 41/1 | 17 | 23 | ready | MD04-schmidt-sciences | issuer statements, SEC, self-statements, court dockets | Each supporter's Anthropic investment or governance role, attached to the exact person or legal entity named by the source |
| C05.E2 | 10/1 | 2 | 7 | ready | MD09-sff-tallinn | funder filings, issuer statements, SEC | The donation event and the investment event separately sourced and separately dated |
| C05.E3 | 93/1 | 28 | 15 | ready | MD04-schmidt-sciences | state registries, SEC, issuer statements | Individuals, employers, foundations, donor-advised accounts and investment vehicles kept distinct, with the identifier that distinguishes each |

Open elements: none

### C06 — Intermediary money that reached METR

Verdict: supported on primary sources (supported=true, supported_primary=true, contested=false).

| element | evidence | primary | negatives | state | owner lane | source classes | text |
|---|---|---|---|---|---|---|---|
| C06.E1 | 92/1 | 19 | 149 | ready | MD10-longview-pooled-regrants | funder filings, recipient filings, DAF sponsor filings | For each asserted path, the document showing a transaction into METR, or the record of its absence in the filings checked |
| C06.E2 | 102/1 | 28 | 136 | ready | MD15-audacious-partners | issuer statements, funder filings, press | Audacious membership, project funding, recipient allocation and payment treated as four separate propositions with separate sources |
| C06.E3 | 50/1 | 16 | 55 | ready | MD19-uk-aisi-contracts | procurement records, issuer statements, statutory records requests | Each government or consortium award with award id, contracting authority, legal recipient, value, period and METR's share or the statement that it is not disclosed in the checked document |
| C06.E4 | 31/1 | 11 | 4 | ready | MD47-entity-edge-audit | issuer statements, press | Relationships that are adjacency only, explicitly labelled as not a money flow |

Open elements: none

### C07 — The donated Anthropic stake

Verdict: supported on primary sources (supported=true, supported_primary=true, contested=false).

| element | evidence | primary | negatives | state | owner lane | source classes | text |
|---|---|---|---|---|---|---|---|
| C07.E1 | 23/1 | 5 | 10 | ready | MD71-donation-statements-quoted | self-statements, press, archives | The dated public statements about the donation, quoted exactly |
| C07.E2 | 207/1 | 23 | 25 | ready | MD37-npt-schedule-b | funder filings, IRS TEOS and e-file index, DAF sponsor filings, state registries | Each vehicle excluded by a document, with that document and the period it covers |
| C07.E3 | 252/1 | 10 | 65 | ready | MD37-npt-schedule-b | DAF sponsor filings, SEC, statutory records requests, state registries | Each vehicle still possible and the exact document that would identify it |
| C07.E4 | 67/1 | 15 | 7 | ready | MD39-good-ventures-fy2026 | recipient filings, funder filings, DAF sponsor filings | A record of whether any transaction from any candidate vehicle into METR appears in the filings checked |

Open elements: none

### C08 — Project-level conflicts and dependence

Verdict: supported on primary sources (supported=true, supported_primary=true, contested=false).

| element | evidence | primary | negatives | state | owner lane | source classes | text |
|---|---|---|---|---|---|---|---|
| C08.E1 | 61/1 | 24 | 10 | ready | MD28-frontier-risk-report-coi | issuer statements, archives | The conflict-of-interest policy version in force at each engagement date, with its dated capture |
| C08.E2 | 79/1 | 18 | 19 | ready | MD28-frontier-risk-report-coi | project documents, issuer statements, self-statements | Personnel disclosures, recusals and stated close relationships for each project |
| C08.E3 | 65/1 | 38 | 16 | ready | MD27-access-and-project-terms | project documents, issuer statements | Provider redaction and exit authority and the evaluator's editorial control for each project |
| C08.E4 | 41/1 | 19 | 10 | ready | MD29-anthropic-incident-engagement | project documents, recipient filings | Compensation and in-kind terms for each project |
| C08.E5 | 96/1 | 41 | 22 | ready | MD35-evaluator-standards | project documents, issuer statements | METR's practice compared with AEF-1, its own policy and other published evaluator standards |

Open elements: none

### C09 — Change over time in funding and disclosure

Verdict: supported on primary sources (supported=true, supported_primary=true, contested=false).

| element | evidence | primary | negatives | state | owner lane | source classes | text |
|---|---|---|---|---|---|---|---|
| C09.E1 | 204/1 | 47 | 77 | ready | MD15-audacious-partners | archives, issuer statements | Dated archive snapshots of METR's funding, about and donor-rule pages showing when each supporter and rule first appeared |
| C09.E2 | 21/1 | 2 | 11 | ready | MD72-coi-policy-versions-hashed | issuer statements, archives | Dated versions of the conflict-of-interest policy with their hashes |
| C09.E3 | 167/1 | 36 | 57 | ready | MD24-funding-page-chronology | archives, funder filings | An explicit record that a page appearance date is not a transaction date, with any case where the two are known to differ |

Open elements: none

### C10 — Adjudication of the September 14 post and the response

Verdict: supported (no primary-strength evidence on at least one element) (supported=true, supported_primary=false, contested=false).

| element | evidence | primary | negatives | state | owner lane | source classes | text |
|---|---|---|---|---|---|---|---|
| C10.E1 | 14/1 | 12 | 0 | ready | MD49-claim-adjudication | archives | The posted image's content fixed at repository commit f64df65 and the current repository's content, each hashed and dated |
| C10.E2 | 15/1 | 0 | 18 | OPEN: primary | MD49-claim-adjudication | issuer statements, self-statements | Each sentence of the public response adjudicated against C01 to C09 with its evidence and open elements |
| C10.E3 | 17/1 | 0 | 9 | OPEN: primary | MD49-claim-adjudication | archives, issuer statements | Each claim of the underlying post adjudicated, naming the exact missing document for any stronger statement |

Open elements: C10.E2 (primary); C10.E3 (primary)

Owner lanes come from the engine (casework lanes map); the three open elements are owned by MD27-access-and-project-terms (C04.E3) and MD49-claim-adjudication (C10.E2, C10.E3). Counts are CLAIMS.md values; where the live readiness run differs it is shown in parentheses (see caution 1).

## 3. Frontier (casework frontier, re-run for this audit)

150 cells: {'COVERED': 55, 'N/A': 89, 'PARTIAL': 6}. Engine definitions (casework/frontier.py): COVERED = a fresh evidence or negative binding in the class and no open element names it; PARTIAL = fresh bindings exist but an open element names the class (or bindings exist but none is fresh); N/A = a reason recorded in casework.json source_class_na (MD52 Task D). No cell is UNTOUCHED.

| claim | recipient filings | funder filings | DAF sponsor filings | IRS TEOS and e-file index | state registries | SEC | court dockets | public grant databases | procurement records | issuer statements | self-statements | project documents | archives | press | statutory records requests |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C01 | COVERED | COVERED | COVERED | COVERED | N/A | N/A | N/A | COVERED | N/A | COVERED | N/A | N/A | COVERED | COVERED | N/A |
| C02 | COVERED | COVERED | COVERED | COVERED | COVERED | N/A | N/A | COVERED | N/A | COVERED | N/A | N/A | COVERED | N/A | N/A |
| C03 | COVERED | COVERED | COVERED | COVERED | N/A | N/A | N/A | N/A | N/A | COVERED | N/A | COVERED | COVERED | N/A | N/A |
| C04 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | PARTIAL | COVERED | PARTIAL | PARTIAL | N/A | N/A |
| C05 | N/A | COVERED | N/A | N/A | COVERED | COVERED | COVERED | N/A | N/A | COVERED | COVERED | N/A | N/A | N/A | N/A |
| C06 | COVERED | COVERED | COVERED | N/A | N/A | N/A | N/A | N/A | COVERED | COVERED | N/A | N/A | N/A | COVERED | COVERED |
| C07 | COVERED | COVERED | COVERED | COVERED | COVERED | COVERED | N/A | N/A | N/A | N/A | COVERED | N/A | COVERED | COVERED | COVERED |
| C08 | COVERED | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | COVERED | COVERED | COVERED | COVERED | N/A | N/A |
| C09 | N/A | COVERED | N/A | N/A | N/A | N/A | N/A | N/A | N/A | COVERED | N/A | N/A | COVERED | N/A | N/A |
| C10 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | PARTIAL | PARTIAL | N/A | PARTIAL | N/A | N/A |

PARTIAL cells and their reasons:
- C04 / issuer statements: class is named by open element(s) C04.E3 (fresh evidence/negative bindings exist; engine marks PARTIAL while a naming element is open)
- C04 / project documents: class is named by open element(s) C04.E3 (fresh evidence/negative bindings exist; engine marks PARTIAL while a naming element is open)
- C04 / archives: class is named by open element(s) C04.E3 (fresh evidence/negative bindings exist; engine marks PARTIAL while a naming element is open)
- C10 / issuer statements: class is named by open element(s) C10.E2, C10.E3 (fresh evidence/negative bindings exist; engine marks PARTIAL while a naming element is open)
- C10 / self-statements: class is named by open element(s) C10.E2 (fresh evidence/negative bindings exist; engine marks PARTIAL while a naming element is open)
- C10 / archives: class is named by open element(s) C10.E3 (fresh evidence/negative bindings exist; engine marks PARTIAL while a naming element is open)

Every N/A cell carries the same form of reason: "no element of Cnn names this class (MD52 Dkk, 2026-09-16); the claim's elements draw on the classes they list and this class carries no test for any of them" (D01-D89; full text per cell in the JSON). EXHAUSTION-GATE.json's source_classes block holds C01 and C02 only.

### 3a. The 22 gate exceptions (verbatim from research/EXHAUSTION-GATE.json)

| field | line | reason | next_check |
|---|---|---|---|
| records_routes | REQ-MD44-UK-DSIT-FOI,REQ-MD44-US-NIST-FOIA,REQ-MD44-EU-EASE-1049,REQ-MD37-NPT-6104D,REQ-MD41-IRS-4506A-5227 | drafts unsent and unapproved; Kevin has neither approved nor explicitly declined them; no clock is running | Kevin's decision |
| calendar | CAL01 | METR's Anthropic incident report if the initial eight-week schedule holds | 2026-11-04 |
| calendar | CAL02 | CY2025 Forms 990 for calendar-year intermediaries and donor-advised sponsors (SVCF, Coefficient entities, RAND, calendar | 2026-11-16 |
| calendar | CAL03 | Good Ventures Foundation FY2026 Form 990-PF (FYE 2026-06-30) | 2026-11-16 |
| calendar | CAL04 | METR's next Form 990 (CY2025) and any audited financial statement | 2026-11-16 |
| calendar | CAL05 | Anthropic registration statement or other holder disclosure | 2026-10-16 |
| calendar | CAL07 | National Philanthropic Trust FY2026 Form 990 (FYE 2026-06-30) | 2026-11-16 |
| calendar | CAL08 | Next unfiled returns of the named Audacious partners (MD43 Task A per-partner dates) | 2026-10-15 |
| calendar | CAL09 | Vanguard Charitable FY2025 Form 990 XML in the GivingTuesday lake and Fidelity/Schwab FY2026 returns | when posted |
| calendar | CAL10 | Overdeck Family Foundation TY2024 Statement 26 attachment as extractable text; Joe and Clara Tsai Foundation TY2025 990- | when posted |
| audits | MD50 C0010 | open (recorded): MDS0560 source_class mislabel; row retained as a bounded negative on the issuer page; no figure cites it | see reason |
| audits | MD50 C0011 | open (recorded): MDS0583 names a pre-formation period; retained as a locator negative; no figure cites it | see reason |
| audits | MD50 C0012 | open (recorded): MDS0917 result form; retained; the same negative is restated in bounded form by MD41 C-rows | see reason |
| audits | MD50 D0001 | open: money-side gate not approvable until D0002-D0018 are resolved or recorded N/A-with-reason; EXHAUSTION-GATE.json not written | see reason |
| audits | MD50 D0004 | open by design: the remainder's composition is embargoed until S6/MD99 (Kevin's decision) | see reason |
| audits | MD50 D0005 | open: calendar closer (Packard TY2025/TY2026 990-PF); listing date stated as not an instrument date on MDP0030 | see reason |
| audits | MD50 D0006 | open (structural): bounded negatives exist for every named supporter; no public amount exists to add | see reason |
| audits | MD50 D0007 | open: calendar/lake closer (Vanguard FY2025 XML); the $4,000,000 line was re-verified on the live ProPublica full-text stream by MD46 A15 | see reason |
| audits | MD50 D0010 | open by date: calendar closers CAL02/CAL04 (2026-11-16) and Packard 990-PF | see reason |
| audits | MD50 D0011 | USER_AUTHORITY_WAIT: five drafts unsent (REQUESTS.jsonl); no clock is running; Kevin decides whether any is sent or waived | see reason |
| audits | MD50 D0014 | open: METR's EU share and the UK AISI amount are undisclosed in checked documents; the EASE and DSIT drafts (unsent) are the routes; EUR never converted | see reason |
| audits | MD50 D0016 | open: frontier receipt and two review receipts are written at S5 closure; EXHAUSTION-GATE.json only if §7 is satisfied | see reason |

gate_pass = True; gate_note: gate passes with the listed exceptions (future documents, the embargoed remainder, unsent drafts awaiting Kevin's decision, and audit items open by date)

## 4. Effort statistics

Total promoted rows: 4548 (every row is bound to at least one element; 7133 bindings). Primary files saved: 11189 across 60 directories under research/primary/, of which 443 sit in running, unpromoted lanes (MD73-ca-ag-charity-registry 291, MD74-ca-sos-bizfile-corporate 152) and 10746 in promoted-lane directories plus S3-coi-policy. Named-supporter coverage: 22 rows.

### 4a. Rows per table

| table | file | rows | evidence | negative | context | primary | supporting | CONFIRMED | DIFFERS |
|---|---|---|---|---|---|---|---|---|---|
| MDE | research/entities.csv | 140 | 123 | 1 | 16 | 28 | 112 | 135 | 5 |
| MDF | research/funding_events.csv | 1032 | 182 | 0 | 850 | 56 | 976 | 981 | 51 |
| MDI | research/in_kind_access.csv | 119 | 67 | 0 | 52 | 40 | 79 | 119 | 0 |
| MDP | research/provenance.csv | 744 | 488 | 61 | 195 | 117 | 627 | 596 | 148 |
| MDQ | research/project_coi.csv | 181 | 108 | 0 | 73 | 67 | 114 | 179 | 2 |
| MDR | research/relationships.csv | 207 | 108 | 0 | 99 | 43 | 164 | 194 | 13 |
| MDS | research/source_coverage.csv | 1690 | 64 | 811 | 815 | 84 | 1606 | 1634 | 56 |
| MDT | research/timeline.csv | 435 | 311 | 53 | 71 | 65 | 370 | 434 | 1 |

### 4b. Rows per lane (lane= marker in note; xhigh re-run additions folded into the owning lane)

| lane | slice | rows | of which xhigh re-run | evidence | negative | context | primary | primary files |
|---|---|---|---|---|---|---|---|---|
| MD01-metr-recipient-baseline | S1 | 31 | 8 | 11 | 10 | 10 | 12 | 175 |
| MD02-packard-grant | S1 | 28 | 1 | 5 | 15 | 8 | 9 | 78 |
| MD03-pew | S1 | 37 | 8 | 3 | 22 | 12 | 9 | 49 |
| MD04-schmidt-sciences | S1 | 36 | 12 | 17 | 8 | 11 | 9 | 154 |
| MD05-sijbrandij-foundation | S1 | 31 | 7 | 9 | 14 | 8 | 5 | 157 |
| MD06-lacentra-astralis-expa | S1 | 53 | 17 | 17 | 18 | 18 | 12 | 183 |
| MD07-jane-street-individuals | S1 | 36 | 11 | 11 | 14 | 11 | 13 | 164 |
| MD08-named-individual-donors | S1 | 80 | 20 | 20 | 27 | 33 | 10 | 135 |
| MD09-sff-tallinn | S1 | 65 | 12 | 17 | 20 | 28 | 12 | 75 |
| MD10-longview-pooled-regrants | S1 | 57 | 13 | 14 | 14 | 29 | 6 | 414 |
| MD11-daf-filed-grants | S1 | 88 | 20 | 2 | 71 | 15 | 2 | 92 |
| MD12-arc-spinout-provenance | S1 | 38 | 4 | 12 | 8 | 18 | 12 | 161 |
| MD13-grant-database-sweep | S1 | 66 | 4 | 10 | 20 | 36 | 2 | 477 |
| MD14-six-month-chronology | S1 | 64 | 19 | 39 | 6 | 19 | 13 | 233 |
| MD15-audacious-partners | S2 | 105 | 1 | 29 | 67 | 9 | 13 | 106 |
| MD16-canary-award-structure | S2 | 43 | 11 | 21 | 5 | 17 | 8 | 204 |
| MD17-rand-canary-receipts | S2 | 57 | 11 | 7 | 25 | 25 | 13 | 105 |
| MD18-metr-canary-commitment | S2 | 30 | 0 | 6 | 17 | 7 | 13 | 236 |
| MD19-uk-aisi-contracts | S2 | 31 | 0 | 12 | 13 | 6 | 11 | 574 |
| MD20-eu-ai-office-contract | S2 | 25 | 2 | 14 | 3 | 8 | 7 | 100 |
| MD21-us-public-sector-awards | S2 | 32 | 3 | 6 | 20 | 6 | 9 | 184 |
| MD22-intermediary-returns | S2 | 134 | 72 | 13 | 35 | 86 | 2 | 425 |
| MD23-restrictions-and-purposes | S2 | 85 | 3 | 38 | 24 | 23 | 20 | 189 |
| MD24-funding-page-chronology | S2 | 93 | 0 | 38 | 13 | 42 | 26 | 360 |
| MD25-revenue-runway-reconciliation | S2 | 31 | 7 | 8 | 7 | 16 | 4 | 139 |
| MD26-tokens-credits-compute | S3 | 106 | 0 | 38 | 61 | 7 | 16 | 158 |
| MD27-access-and-project-terms | S3 | 74 | 0 | 51 | 17 | 6 | 44 | 72 |
| MD28-frontier-risk-report-coi | S3 | 71 | 0 | 51 | 9 | 11 | 11 | 149 |
| MD29-anthropic-incident-engagement | S3 | 33 | 0 | 17 | 10 | 6 | 9 | 196 |
| MD30-project-staff-conflicts | S3 | 44 | 0 | 29 | 10 | 5 | 11 | 54 |
| MD31-board-and-governance | S3 | 64 | 0 | 45 | 7 | 12 | 20 | 223 |
| MD32-lab-money-negative-sweep | S3 | 57 | 0 | 9 | 26 | 22 | 9 | 114 |
| MD33-donor-investor-map | S3 | 89 | 0 | 43 | 17 | 29 | 9 | 131 |
| MD34-cross-lab-project-terms | S3 | 44 | 0 | 35 | 4 | 5 | 12 | 139 |
| MD35-evaluator-standards | S3 | 85 | 0 | 59 | 9 | 17 | 32 | 107 |
| MD36-evaluator-selection | S3 | 56 | 0 | 36 | 13 | 7 | 9 | 232 |
| MD37-npt-schedule-b | S4 | 67 | 0 | 52 | 4 | 11 | 5 | 120 |
| MD38-daf-sponsor-schedules | S4 | 152 | 0 | 136 | 7 | 9 | 0 | 185 |
| MD39-good-ventures-fy2026 | S4 | 111 | 0 | 67 | 7 | 37 | 17 | 87 |
| MD40-moskovitz-vehicles | S4 | 51 | 0 | 17 | 19 | 15 | 1 | 203 |
| MD41-remainder-interest-trust | S4 | 35 | 0 | 13 | 16 | 6 | 3 | 333 |
| MD42-anthropic-securities-filings | S4 | 22 | 0 | 8 | 11 | 3 | 0 | 61 |
| MD43-partner-calendar-closers | S4 | 121 | 0 | 43 | 36 | 42 | 0 | 147 |
| MD44-public-record-requests | S4 | 31 | 0 | 1 | 9 | 21 | 0 | 132 |
| MD45-calendar-monitor | S4 | 36 | 0 | 22 | 8 | 6 | 0 | 110 |
| MD46-funding-reconciliation | S5 | 48 | 0 | 0 | 0 | 48 | 0 | 109 |
| MD47-entity-edge-audit | S5 | 257 | 0 | 22 | 1 | 234 | 11 | 223 |
| MD48-independence-synthesis | S5 | 70 | 0 | 1 | 0 | 69 | 0 | 88 |
| MD49-claim-adjudication | S5 | 76 | 0 | 35 | 15 | 26 | 12 | 122 |
| MD50-audit-money | S5 | 510 | 0 | 30 | 3 | 477 | 0 | 264 |
| MD51-audit-framing | S5 | 36 | 0 | 20 | 10 | 6 | 0 | 120 |
| MD52-frontier-gap-generation | S5 | 309 | 0 | 17 | 4 | 288 | 0 | 117 |
| MD53-figures-and-release | S5 | 94 | 0 | 2 | 10 | 82 | 0 | 40 |
| MD70-named-supporter-list-capture | S5 | 239 | 0 | 133 | 64 | 42 | 10 | 417 |
| MD71-donation-statements-quoted | S5 | 40 | 0 | 21 | 10 | 9 | 5 | 270 |
| MD72-coi-policy-versions-hashed | S5 | 35 | 0 | 19 | 11 | 5 | 2 | 844 |
| MD99-71m-allocation-request | S6 | 17 | 0 | 0 | 2 | 15 | 0 | 9 |
| S0-seed-import | S0 | 41 | 0 | 0 | 0 | 41 | 0 |  |
| S2-lineage-import | S2 | 51 | 0 | 0 | 0 | 51 | 0 |  |

Rows per slice: {'S0': 41, 'S1': 710, 'S2': 717, 'S3': 723, 'S4': 626, 'S5': 1714, 'S6': 17}. Primary directories without promoted rows: S3-coi-policy (1 file) and the running gap lanes MD73, MD74 (see caution 10).

### 4c. Rows per source class (all tables)

| source class | rows |
|---|---|
| issuer statements | 1098 |
| funder filings | 800 |
| archives | 520 |
| DAF sponsor filings | 442 |
| self-statements | 320 |
| project documents | 308 |
| public grant databases | 229 |
| IRS TEOS and e-file index | 170 |
| procurement records | 120 |
| SEC | 118 |
| recipient filings | 112 |
| state registries | 103 |
| press | 97 |
| statutory records requests | 73 |
| court dockets | 38 |

### 4d. Role and strength

Unique rows by role: {'context': 2171, 'evidence': 1451, 'negative': 926}. Bindings by role: {'context': 3145, 'evidence': 2544, 'negative': 1444}. Unique rows by strength: {'supporting': 4048, 'primary': 500}. Bindings by strength: {'supporting': 6354, 'primary': 779}. Bindings by role/strength: {'context/supporting': 3145, 'evidence/primary': 655, 'evidence/supporting': 1889, 'negative/supporting': 1320, 'negative/primary': 124}. Each row carries one role and one strength across all its bindings.

### 4e. Bounded negatives per named supporter (research/supporter_coverage.csv)

| supporter | status | negative rows | positive rows | timeline rows | lanes | money types seen | how METR names it |
|---|---|---|---|---|---|---|---|
| The Audacious Project (TED) | amount_identified | 55 | 75 | 18 | MD15;MD16;MD18 | commitment | named on metr.org/about and the 2026-08-14 update |
| individuals from Jane Street | acknowledged_no_amount | 20 | 16 | 4 | MD07 | commitment | named on metr.org/about and the 2026-08-14 update |
| Sijbrandij Foundation | acknowledged_no_amount | 27 | 10 | 3 | MD05 | undisclosed | named on metr.org/about and the 2026-08-14 update |
| The Pew Charitable Trusts | acknowledged_no_amount | 37 | 8 | 2 | MD03 | undisclosed | named on metr.org/about and the 2026-08-14 update |
| Schmidt Sciences | acknowledged_no_amount | 19 | 10 | 2 | MD04 | undisclosed | named on metr.org/about and the 2026-08-14 update |
| The David and Lucile Packard Foundation | amount_identified | 33 | 45 | 4 | MD02 | commitment | named on metr.org/about and the 2026-08-14 update |
| LaCentra-Sumerlin Foundation | acknowledged_no_amount | 18 | 8 | 6 | MD06 | undisclosed | named on metr.org/about; 'Frontier Fund' in the 2026-08-14 image alt |
| Astralis Foundation | acknowledged_no_amount | 18 | 7 | 4 | MD06 | undisclosed | named on metr.org/about and the 2026-08-14 image alt |
| Expa.org | acknowledged_no_amount | 12 | 7 | 4 | MD06 | undisclosed | named on metr.org/about and the 2026-08-14 image alt |
| AI Security Institute (UK) | acknowledged_no_amount | 31 | 29 | 6 | MD19 | contract | named on metr.org/about ('partnering with') |
| Longview Philanthropy (pooled funds) | amount_identified | 34 | 37 | 4 | MD10 | recommendation | named on metr.org/about as a pooled fund |
| Effektiv Spenden (pooled funds) | amount_identified | 11 | 21 | 2 | MD10 | regrant | named on metr.org/about as a pooled fund |
| Survival and Flourishing Fund (recommendations) | amount_identified | 34 | 73 | 2 | MD09 | commitment; paid_grant; recommendation | named on metr.org/about as recommendations |
| David Farhi | acknowledged_no_amount | 13 | 14 | 5 | MD08 | undisclosed | named on metr.org/about and the 2026-08-14 update |
| Geoff Ralston | acknowledged_no_amount | 11 | 10 | 5 | MD08 | undisclosed | named on metr.org/about and the 2026-08-14 update |
| Dylan Field | acknowledged_no_amount | 11 | 13 | 6 | MD08 | undisclosed | named on metr.org/about and the 2026-08-14 update |
| Steve Newman | acknowledged_no_amount | 9 | 9 | 5 | MD08 | undisclosed | named on metr.org/about and the 2026-08-14 update |
| Alignment Research Center (program transfer) | amount_identified | 36 | 27 | 7 | MD12;MD01 | in_kind_estimate; transfer | not named as a supporter; filed related-organisation transfer |
| Founders Pledge Inc | amount_identified | 17 | 25 | 2 | MD10;MD22 | filed_grant; paid_grant | not named by METR; filed Schedule I payer |
| Silicon Valley Community Foundation (DAF sponsor) | amount_identified | 20 | 31 | 2 | MD11 | filed_grant | not named by METR; filed Schedule I payer |
| Vanguard Charitable Endowment Program (DAF sponsor) | amount_identified | 30 | 35 | 3 | MD11 | filed_grant | not named by METR; filed Schedule I payer |
| European AI Office (contract) | acknowledged_no_amount | 3 | 15 | 2 | MD20 | contract | named on metr.org/about as a technical-assistance contract |

Sum of negative rows across the 22 lines: 499 (a row can serve more than one supporter). Statuses: {'amount_identified': 9, 'acknowledged_no_amount': 13}.

## 5. Seed-versus-lane delta

S0-seed-import rows: 41 (MDF 17, MDI 2, MDP 2, MDQ 1, MDR 3, MDS 8, MDT 8), all role=context ('seed transcription from the 10-metr pack ... role=context until re-verified'). S2-lineage-import rows: 51 (all MDF, all context). Lane rows (MD01-MD99 including xhigh re-run additions): 4456.

Superseded rows: 30 (10 seed, 20 lane). Seed rows superseded and why:

| row | superseded by | reason (MD50 audit) |
|---|---|---|
| MDF0002 | MDF0465 (2026-09-16) | A0002: money_type=commitment but the primary is a run-rate statement (resolved: seed row superseded, money type cleared) |
| MDF0003 | MDF0466 (2026-09-16) | A0003: money_type=commitment but the primary is a runway statement (resolved: seed row superseded, money type cleared) |
| MDS0001 | MDS1283 (2026-09-16) | C0002: unbounded in form and url is a local filesystem path (resolved: superseded by E0003 live Coefficient catalog none-found) |
| MDS0002 | MDS1271 (2026-09-16) | C0003: unbounded in form; 2021-2024 Packard 990-PF Part XV would not carry the 2026 award (resolved: bounded lane rows are the negatives of record) |
| MDS0003 | MDS1272 (2026-09-16) | C0004: unbounded in form (resolved: bounded lane rows are the negatives of record) |
| MDS0004 | MDS1273 (2026-09-16) | C0005: unbounded in form (resolved: bounded lane rows are the negatives of record) |
| MDS0005 | MDS1274 (2026-09-16) | C0006: unbounded in form (resolved: bounded lane rows are the negatives of record) |
| MDS0006 | MDS1275 (2026-09-16) | C0007: unbounded in form; FY2025 XML 404; ProPublica rendered page used as the filing (resolved: bounded lane rows are the negatives of record) |
| MDS0007 | MDS1276 (2026-09-16) | C0008: unbounded in form (resolved: bounded lane rows are the negatives of record) |
| MDS0008 | MDS1277 (2026-09-16) | C0009: unbounded in form (resolved: bounded lane rows are the negatives of record) |

Lane rows superseded (replaced by xhigh re-run or review-corrected rows of the same fact):

| row | lane | superseded by |
|---|---|---|
| MDE0012 | MD05-sijbrandij-foundation | MDE0125 (2026-09-16) |
| MDF0031 | MD01-metr-recipient-baseline | MDF0410 (2026-09-16) |
| MDF0035 | MD01-metr-recipient-baseline | MDF0411 (2026-09-16) |
| MDF0068 | MD12-arc-spinout-provenance | MDF0414 (2026-09-16) |
| MDF0076 | MD13-grant-database-sweep | MDF0539 (2026-09-16) |
| MDF0077 | MD13-grant-database-sweep | MDF0540 (2026-09-16) |
| MDF0155 | MD22-intermediary-returns | MDF0459 (2026-09-16) |
| MDF0163 | MD22-intermediary-returns | MDF0460 (2026-09-16) |
| MDS0151 | MD06-lacentra-astralis-expa | MDS1059 (2026-09-16) |
| MDS0214 | MD11-daf-filed-grants | MDS1105 (2026-09-16) |
| MDS0215 | MD11-daf-filed-grants | MDS1104 (2026-09-16) |
| MDS0216 | MD11-daf-filed-grants | MDS1106 (2026-09-16) |
| MDS0217 | MD11-daf-filed-grants | MDS1110 (2026-09-16) |
| MDS0218 | MD11-daf-filed-grants | MDS1111 (2026-09-16) |
| MDS0219 | MD11-daf-filed-grants | MDS1107 (2026-09-16) |
| MDS0220 | MD11-daf-filed-grants | MDS1108 (2026-09-16) |
| MDS0221 | MD11-daf-filed-grants | MDS1109 (2026-09-16) |
| MDS0466 | MD21-us-public-sector-awards | MDS1023 (2026-09-16) |
| MDT0055 | MD22-intermediary-returns | MDT0232 (2026-09-16) |
| MDT0056 | MD22-intermediary-returns | MDT0233 (2026-09-16) |

MD50 A0076/A0077 (MDF0076, MDF0077, MD13 sitemap enumerations) are the two lane rows whose amount and money type were cleared by the audit; the other 18 were superseded at review or xhigh re-run (MD01 revenue totals -> MDF0410/0411; MD12 gift totals -> MDF0414; MD22 transfers -> MDF0459/0460, MDT0232/0233; MD11 DAF negatives MDS0214-0221 -> MDS1104-1111; MD06 -> MDS1059; MD21 -> MDS1023; MD05 -> MDE0125).

## 6. Adversarial audits (MD50 money, MD51 framing)

MD51 (AUDIT-FRAMING.md): 36 rows; 19 defects in the posted figures (Task A entity merges 6, Task B adjacency-as-money 6, Task C unsupported conclusions and motive tokens 7) plus the D01 gate verdict; every entry resolved 2026-09-16 (MD53 rendered the six PLAN §8 figures without the defect; scripts/lint_figures.py PASS). 16 other rows are bounded negatives/coverage (none needed).

| id | promoted | defect | resolution |
|---|---|---|---|
| A01 | MDP0532 | Posted figure metr-11 node merges Dustin Moskovitz the individual with Coefficient Giving / Open Philanthropy — defect: person standing in for an organisation in figure metr-11 (posted commit f64df65; still present in current 17539ba) | resolved 2026-09-16: MD53 rendered the six PLAN §8 figures without this defect (scan-rendered-defect-phrases hits=[]; scripts/lint_figures.py PASS on all six) |
| A02 | MDP0533 | Posted figure metr-11 node merges Jaan Tallinn the individual with Survival and Flourishing Fund — defect: person standing in for an organisation in figure metr-11 | resolved 2026-09-16: MD53 rendered the six PLAN §8 figures without this defect (scan-rendered-defect-phrases hits=[]; scripts/lint_figures.py PASS on all six) |
| A03 | MDP0534 | Posted figure metr-11 node merges Schmidt Sciences with Eric Schmidt — defect: person standing in for an organisation in figure metr-11 | resolved 2026-09-16: MD53 rendered the six PLAN §8 figures without this defect (scan-rendered-defect-phrases hits=[]; scripts/lint_figures.py PASS on all six) |
| A04 | MDP0535 | Posted figure metr-11 places Jane Street the firm's Anthropic stakes on the METR-donor row labelled Jane Street (individuals) — defect: employer standing in for an individual in figure metr-11 (firm Anthropic stakes drawn on the individuals donor row) | resolved 2026-09-16: MD53 rendered the six PLAN §8 figures without this defect (scan-rendered-defect-phrases hits=[]; scripts/lint_figures.py PASS on all six) |
| A05 | MDP0536 | Posted figure metr-01 stands Dustin Moskovitz and Cari Tuna in for Good Ventures Foundation — defect: person standing in for an organisation in figure metr-01 (and metr-01b subtitle: Dustin Moskovitz and Cari Tuna's philanthropy is the money: Good Ventures Foundation) | resolved 2026-09-16: MD53 rendered the six PLAN §8 figures without this defect (scan-rendered-defect-phrases hits=[]; scripts/lint_figures.py PASS on all six) |
| A06 | MDP0537 | Posted figures metr-01 and metr-01b call Alignment Research Center METR's parent, merging two 501(c)(3)s for money-path framing — defect: two legal entities merged (ARC as METR's parent) in figure metr-01 title; metr-01b and metr-10 repeat METR's parent | resolved 2026-09-16: MD53 rendered the six PLAN §8 figures without this defect (scan-rendered-defect-phrases hits=[]; scripts/lint_figures.py PASS on all six) |
| B01 | MDP0538 | Posted figure metr-01 treats grants to ARC, RAND, Longview and a board member's organisation as money that reached METR — defect: adjacency (grants to other legal entities) used as if it were a money flow into METR | resolved 2026-09-16: MD53 rendered the six PLAN §8 figures without this defect (scan-rendered-defect-phrases hits=[]; scripts/lint_figures.py PASS on all six) |
| B02 | MDP0539 | Posted figure metr-01b title treats funders of ARC, RAND, Longview and pooled funds as funders that reach METR — defect: adjacency and investor status used as if they were a money flow into METR | resolved 2026-09-16: MD53 rendered the six PLAN §8 figures without this defect (scan-rendered-defect-phrases hits=[]; scripts/lint_figures.py PASS on all six) |
| B03 | MDP0540 | Posted figure metr-01 draws office space, a board seat and a contractor into the money figure — defect: office space, board seat (Gleave) and contractor on METR drawn in the money figure | resolved 2026-09-16: MD53 rendered the six PLAN §8 figures without this defect (scan-rendered-defect-phrases hits=[]; scripts/lint_figures.py PASS on all six) |
| B04 | MDP0541 | Posted figure metr-11 uses lab-investor status as the other side of a METR-donor money table — defect: investor status used as if it were a money flow (donor table paired with 'Money in a frontier lab') | resolved 2026-09-16: MD53 rendered the six PLAN §8 figures without this defect (scan-rendered-defect-phrases hits=[]; scripts/lint_figures.py PASS on all six) |
| B05 | MDP0542 | Posted figure metr-17 treats Vanguard Charitable as a channel of unidentified money into the AI-safety cluster, including METR's $4M filed grant — defect: DAF-sponsor filed grants and cluster totals used as if they were a channelled money flow from an unidentified principal into METR | resolved 2026-09-16: MD53 rendered the six PLAN §8 figures without this defect (scan-rendered-defect-phrases hits=[]; scripts/lint_figures.py PASS on all six) |
| B06 | MDP0543 | Posted figure metr-10 treats Coefficient grants to Tarbell and Tarbell fellow bylines at TIME as a funding path behind METR's parent/partners — defect: shared employment/funding adjacency (Coefficient→Tarbell→TIME byline) used as if it were a money flow or control path into METR | resolved 2026-09-16: MD53 rendered the six PLAN §8 figures without this defect (scan-rendered-defect-phrases hits=[]; scripts/lint_figures.py PASS on all six) |
| C01 | MDP0544 | Posted figure metr-07 title uses ordination vocabulary for evaluator selection without independently supported coordination elements — defect: unsupported coordination/selection conclusion in figure text (ordination metaphor) | resolved 2026-09-16: MD53 rendered the six PLAN §8 figures without this defect (scan-rendered-defect-phrases hits=[]; scripts/lint_figures.py PASS on all six) |
| C02 | MDP0545 | Posted figure metr-12 concludes the investigations came after the money, a causal/dependence frame whose required elements are not independently supported — defect: unsupported dependence/causal conclusion in figure text | resolved 2026-09-16: MD53 rendered the six PLAN §8 figures without this defect (scan-rendered-defect-phrases hits=[]; scripts/lint_figures.py PASS on all six) |
| C03 | MDP0546 | Posted figure metr-17 ties DAF-sponsor cluster growth to Anthropic's first tender offer as if coordinated — defect: unsupported coordination conclusion in figure text (DAF totals in the year of a tender offer) | resolved 2026-09-16: MD53 rendered the six PLAN §8 figures without this defect (scan-rendered-defect-phrases hits=[]; scripts/lint_figures.py PASS on all six) |
| C04 | MDP0547 | Posted figure metr-13 concludes Redwood's board held the funder's co-CEO, Anthropic's future trustee and METR's future staffer as the investigator's subcontractor frame — defect: unsupported coordination/dependence conclusion in figure text (board composition as capture of the investigation) | resolved 2026-09-16: MD53 rendered the six PLAN §8 figures without this defect (scan-rendered-defect-phrases hits=[]; scripts/lint_figures.py PASS on all six) |
| C05 | MDP0548 | Posted figure metr-14 uses David Sacks's independence accusation as the figure's own title frame — defect: unsupported independence/coordination conclusion used as figure title (quoted accusation framed as the chart) | resolved 2026-09-16: MD53 rendered the six PLAN §8 figures without this defect (scan-rendered-defect-phrases hits=[]; scripts/lint_figures.py PASS on all six) |
| C06 | MDP0549 | Posted figure metr-21 uses banned motive token intended in figure text — defect: motive vocabulary in figure text (banned token intended) | resolved 2026-09-16: MD53 rendered the six PLAN §8 figures without this defect (scan-rendered-defect-phrases hits=[]; scripts/lint_figures.py PASS on all six) |
| C07 | MDP0550 | Posted figure metr-01b uses banned motive token captured in figure text — defect: motive vocabulary in figure text (banned token captured) | resolved 2026-09-16: MD53 rendered the six PLAN §8 figures without this defect (scan-rendered-defect-phrases hits=[]; scripts/lint_figures.py PASS on all six) |
| D01 | MDS1218 | Framing-side exhaustion-gate verdict — cannot be approved on the framing side until the listed corrections | resolved 2026-09-16: framing-side gate approved on the rendered pack figures (MD53 promoted; lint PASS); the posted seed corpus at f64df65 stays a separate, unmodified corpus |

MD50 (AUDIT-MONEY.md): 510 rows. Task A 468 re-verifications: 391 matched live; 73 mismatches resolved 'audit-lane retrieval failure or name-form difference; promoted row stands (MDREVIEW-MD50)'; 4 seed rows superseded (A0002, A0003, A0076, A0077). Task B 9 attacks recorded, no correction needed (reconciliation counts each fact once; MD53 figures must dedupe restated amounts by award). Task C 12: coverage row C0001, C0002-C0009 seed negatives superseded, C0010-C0012 open (recorded). Task D 18 gate items: {'open': 8, 'resolved': 7, 'USER_AUTHORITY_WAIT': 1, 'N/A-with-reason': 2}. Task E 3 bounded negatives. Findings by task and resolution: {'A:resolved': 77, 'B:recorded, no correction needed': 9, 'C:open': 3, 'C:resolved': 8, 'D:N/A-with-reason': 2, 'D:USER_AUTHORITY_WAIT': 1, 'D:open': 8, 'D:resolved': 7}.

Money defects other than the 73 retrieval/name-form A rows:

| id | promoted | task | finding | resolution |
|---|---|---|---|---|
| A0002 | MDF0465 | A | audit of promoted MDF0002: run-rate — mismatch: money_type=commitment but the primary is a run-rate or runway statement, not a commitment | resolved: seed row superseded (money type cleared) |
| A0003 | MDF0466 | A | audit of promoted MDF0003: runway — mismatch: money_type=commitment but the primary is a run-rate or runway statement, not a commitment | resolved: seed row superseded (money type cleared) |
| A0076 | MDF0539 | A | audit of promoted MDF0076: Giving What We Can charities sitemap enumeration — mismatch: amount 220000 not found in primary; to_entity not in primary: METR (formerly called ARC Evals) | resolved: seed sitemap row superseded (amount and money type cleared) |
| A0077 | MDF0540 | A | audit of promoted MDF0077: Future of Life Institute grant-sitemap enumeration — mismatch: amount 1401000 not found in primary | resolved: seed sitemap row superseded (amount and money type cleared) |
| B0001 | MDP0585 | B | double-count attack: Packard $350,000 appears on multiple promoted MDF rows and three recon lines — double-count risk: compatible_component MDP0030 $350000 is also remainder_statement MDP0055 amount_usd=350000 and identified_compatible_total $350000. The recon does not add those three lines together. Promoted MDF rows  | recorded, no correction needed: the reconciliation counts each fact once and never sums across type or period; MD53 figures must dedupe restated amounts by award (Packard 2026-79050; Audacious/Canary; ARC spin-off; FP $184,000) |
| B0002 | MDP0586 | B | double-count attack: Audacious/Canary $38 million, $17 million, and bit-under-$16 million restatement — double-count risk if treated as separate inbound amounts: recon excludes MDP0033 ~$38M joint RAND+METR, MDP0034 ~$17M METR-side subset, and MDP0035 bit-under-$16m restatement, and states they are not additive. Using the  | recorded, no correction needed: the reconciliation counts each fact once and never sums across type or period; MD53 figures must dedupe restated amounts by award (Packard 2026-79050; Audacious/Canary; ARC spin-off; FP $184,000) |
| B0003 | MDP0587 | B | double-count attack: ARC RelatedOrganizationsAmt $4,501,424 vs Schedule I cash $4,477,169 plus non-cash $76,766 — double-count risk: METR FY2024 RelatedOrganizationsAmt 4501424 (MDP0032 / MDF0034) and ARC FY2024 Schedule I CashGrantAmt 4477169 plus NonCashAssistanceAmt 76766 (MDF0064/MDF0065) describe the same program spin-off. They | recorded, no correction needed: the reconciliation counts each fact once and never sums across type or period; MD53 figures must dedupe restated amounts by award (Packard 2026-79050; Audacious/Canary; ARC spin-off; FP $184,000) |
| B0004 | MDP0588 | B | double-count / cross-type attack: Founders Pledge Inc TY2024 $184,000 and Jaan Tallinn public-ledger $184,000 via FP-US — double-count risk across money types: 7 promoted rows carry 184000 (Founders Pledge filed_grant and/or Tallinn public ledger via FP-US). Recon excludes MDP0041 as filed_grant, not a 2026 commitment. Adding the ledger lin | recorded, no correction needed: the reconciliation counts each fact once and never sums across type or period; MD53 figures must dedupe restated amounts by award (Packard 2026-79050; Audacious/Canary; ARC spin-off; FP $184,000) |
| B0005 | MDP0589 | B | period-mismatch attack: Packard award year 2026 / catalog listing 2026-07-06 used as a last-6-months commitment component — period mismatch: the $71 million denominator is commitments raised in the last 6 months as of 2026-08-14 (derived window approximately 2026-02-14 to 2026-08-14). Packard compatibility rests on JSON-LD datePublished 2026- | recorded, no correction needed: the reconciliation counts each fact once and never sums across type or period; MD53 figures must dedupe restated amounts by award (Packard 2026-79050; Audacious/Canary; ARC spin-off; FP $184,000) |
| B0006 | MDP0590 | B | period-mismatch attack: excluded amounts whose periods are before the last-6-months window, plus in-kind after 2026-08-14 — period mismatch if used as window evidence: FY2024 filed revenue MDP0031 is before the window and is excluded. in_kind_estimate MDP0052 ~$400k is dated 2026-08-26, after 2026-08-14, and is excluded. Recon decisions match | recorded, no correction needed: the reconciliation counts each fact once and never sums across type or period; MD53 figures must dedupe restated amounts by award (Packard 2026-79050; Audacious/Canary; ARC spin-off; FP $184,000) |
| B0007 | MDP0591 | B | cross-type attack: Packard catalog award typed as commitment and used as a component of METR's commitment total — money_type used as evidence of another: the primary is a funder catalog grant listing ('1 Grants / $350,000', purpose for general support), not a signed commitment instrument and not a paid/unpaid flag. Recon types it as | recorded, no correction needed: the reconciliation counts each fact once and never sums across type or period; MD53 figures must dedupe restated amounts by award (Packard 2026-79050; Audacious/Canary; ARC spin-off; FP $184,000) |
| B0008 | MDP0592 | B | cross-type attack: recon remainder is commitment minus commitment; excluded filed_grant/recommendation/transfer/contract/in_kind were not subtracted — cross-type check: identified_compatible_total 350000 and unresolved_remainder 70650000 are both money_type=commitment and 350000+70650000=71000000 uses the working integer of 'around $71 million'. Excluded filed_grant, r | recorded, no correction needed: the reconciliation counts each fact once and never sums across type or period; MD53 figures must dedupe restated amounts by award (Packard 2026-79050; Audacious/Canary; ARC spin-off; FP $184,000) |
| B0009 | MDP0593 | B | cross-type / provenance attack: Vanguard Charitable $4,000,000 recon line relies on a seed-held amount; GT XML 404 — provenance gap on an excluded filed_grant: recon MDP0043 reason says live ProPublica Schedule I HTML is a JS shell, gt990datalake S3 XML 404, and IRS 2026_TEOS_XML_05A.zip listing does not contain OBJECT_ID 2026213293493 | recorded, no correction needed: the reconciliation counts each fact once and never sums across type or period; MD53 figures must dedupe restated amounts by award (Packard 2026-79050; Audacious/Canary; ARC spin-off; FP $184,000) |
| C0002 | MDS1270 | C | bounded-negative attack on MDS0001: Coefficient Giving grants index snapshot 2026-09-11, organization_name and title — unbounded in form: result is not 'none found in <exact source> as of <UTC date>'; url is a local filesystem path, not a public source | resolved: MDS0001 superseded by E0003 |
| C0003 | MDS1271 | C | bounded-negative attack on MDS0002: Form 990-PF Part XV, 2021-2024 — unbounded in form: result is not 'none found in <exact source> as of <UTC date>'; 2021-2024 Packard 990-PF Part XV would not have carried the 2026 catalog award later promoted as the compatible component | resolved: seed negative superseded; bounded lane rows for the same source are the negatives of record |
| C0004 | MDS1272 | C | bounded-negative attack on MDS0003: Form 990 Schedule I, FY2021-FY2025 — unbounded in form: result is not 'none found in <exact source> as of <UTC date>' | resolved: seed negative superseded; bounded lane rows for the same source are the negatives of record |
| C0005 | MDS1273 | C | bounded-negative attack on MDS0004: Form 990-PF Part XV, 2021-2024 — unbounded in form: result is not 'none found in <exact source> as of <UTC date>' | resolved: seed negative superseded; bounded lane rows for the same source are the negatives of record |
| C0006 | MDS1274 | C | bounded-negative attack on MDS0005: Form 990-PF Part XV, 2021-2024 — unbounded in form: result is not 'none found in <exact source> as of <UTC date>' | resolved: seed negative superseded; bounded lane rows for the same source are the negatives of record |
| C0007 | MDS1275 | C | bounded-negative attack on MDS0006: Form 990-PF Part XV, FY2022-FY2025 — unbounded in form: result is not 'none found in <exact source> as of <UTC date>'; FY2025 XML 404; ProPublica rendered page used as the filing, a source that often does not carry Schedule I grant rows | resolved: seed negative superseded; bounded lane rows for the same source are the negatives of record |
| C0008 | MDS1276 | C | bounded-negative attack on MDS0007: Form 990 Schedule I, FY2022-FY2025 — unbounded in form: result is not 'none found in <exact source> as of <UTC date>' | resolved: seed negative superseded; bounded lane rows for the same source are the negatives of record |
| C0009 | MDS1277 | C | bounded-negative attack on MDS0008: Form 990-PF Part XV, TY2021-TY2024 — unbounded in form: result is not 'none found in <exact source> as of <UTC date>' | resolved: seed negative superseded; bounded lane rows for the same source are the negatives of record |
| C0010 | MDS1278 | C | bounded-negative attack on MDS0560: Separate gift/grant instrument dates for other about-page supporter names — source_class=funder filings but url is a METR issuer page, which would not carry a funder 990 grant line | open (recorded): MDS0560 source_class mislabel; row retained as a bounded negative on the issuer page; no figure cites it |
| C0011 | MDS1279 | C | bounded-negative attack on MDS0583: AmazonSmile Foundation TY2023 990-PF locator (pre-METR formation) — unbounded in form: result is not 'none found in <exact source> as of <UTC date>'; named source period predates METR's formation and would not have carried a METR payer record | open (recorded): MDS0583 names a pre-formation period; retained as a locator negative; no figure cites it |
| C0012 | MDS1280 | C | bounded-negative attack on MDS0917: IRS public files: none found for the remainder-interest trust as a 990-series or Form 5227 extract filer in the indexes this lane fetched — unbounded in form: result is not 'none found in <exact source> as of <UTC date>' | open (recorded): MDS0917 result form; retained; the same negative is restated in bounded form by MD41 C-rows |
| D0001 | MDP0594 | D | PLAN.md §7 exhaustion gate, money side: decision — cannot be approved on the money side | open: money-side gate not approvable until D0002-D0018 are resolved or recorded N/A-with-reason; EXHAUSTION-GATE.json not written |
| D0002 | MDP0595 | D | correction required before money-side gate approval: C01 source classes still UNTOUCHED on the STATE.md frontier: state registries, SEC, court dockets, procurement records, self-statements, project documents, statutory records reques — correction required: C01 source classes still UNTOUCHED on the STATE.md frontier: state registries, SEC, court dockets, procurement records, self-statements, project documents, statutory records requests | resolved 2026-09-16: every structural UNTOUCHED class now carries an N/A reason in casework.json source_class_na (MD52 Task D, 89 entries); frontier shows no UNTOUCHED line |
| D0003 | MDP0596 | D | correction required before money-side gate approval: C02 source classes still UNTOUCHED: SEC, court dockets, procurement records, self-statements, project documents, archives, press, statutory records requests; issuer statements PART — correction required: C02 source classes still UNTOUCHED: SEC, court dockets, procurement records, self-statements, project documents, archives, press, statutory records requests; issuer statements PARTIAL | resolved 2026-09-16: every structural UNTOUCHED class now carries an N/A reason in casework.json source_class_na (MD52 Task D, 89 entries); frontier shows no UNTOUCHED line |
| D0004 | MDP0597 | D | correction required before money-side gate approval: Unresolved remainder around $70.65 million of commitment-dollars in the statement window has no public composition; asking METR is embargoed until S6/MD99 — correction required: Unresolved remainder around $70.65 million of commitment-dollars in the statement window has no public composition; asking METR is embargoed until S6/MD99 | open by design: the remainder's composition is embargoed until S6/MD99 (Kevin's decision) |
| D0005 | MDP0598 | D | correction required before money-side gate approval: Packard $350,000 compatible component still lacks a signed-grant instrument day; period compatibility rests on catalog listing 2026-07-06 — correction required: Packard $350,000 compatible component still lacks a signed-grant instrument day; period compatibility rests on catalog listing 2026-07-06 | open: calendar closer (Packard TY2025/TY2026 990-PF); listing date stated as not an instrument date on MDP0030 |
| D0006 | MDP0599 | D | correction required before money-side gate approval: Named supporters without a public amount/vehicle/date remain: individuals from Jane Street; Sijbrandij Foundation; The Pew Charitable Trusts; Schmidt Sciences; LaCentra-Sumerlin Fo — correction required: Named supporters without a public amount/vehicle/date remain: individuals from Jane Street; Sijbrandij Foundation; The Pew Charitable Trusts; Schmidt Sciences; LaCentra-Sumerlin Foundation; Astralis  | open (structural): bounded negatives exist for every named supporter; no public amount exists to add |
| D0007 | MDP0600 | D | correction required before money-side gate approval: Vanguard Charitable FY2025 $4,000,000 XML was not recovered from GT/IRS zip; recon still cites a seed-held amount — correction required: Vanguard Charitable FY2025 $4,000,000 XML was not recovered from GT/IRS zip; recon still cites a seed-held amount | open: calendar/lake closer (Vanguard FY2025 XML); the $4,000,000 line was re-verified on the live ProPublica full-text stream by MD46 A15 |
| D0008 | MDP0601 | D | correction required before money-side gate approval: Seed MDS0001–MDS0008 are unbounded in form (result='none found') and MDS0001 uses a local path; they remain context until re-verified against a public source — correction required: Seed MDS0001–MDS0008 are unbounded in form (result='none found') and MDS0001 uses a local path; they remain context until re-verified against a public source | resolved: MDS0001-MDS0008 superseded (this lane C0002-C0009, E0003) |
| D0009 | MDP0602 | D | correction required before money-side gate approval: research/grok-out/MD46-funding-reconciliation.csv is not present; recon is a derived table from promoted MDP/MDF bindings, not a reviewed MD46 lane — correction required: research/grok-out/MD46-funding-reconciliation.csv is not present; recon is a derived table from promoted MDP/MDF bindings, not a reviewed MD46 lane | resolved 2026-09-16: MD46 promoted; commitment_reconciliation.csv rebuilt from promoted rows (66 rows) |
| D0010 | MDP0603 | D | correction required before money-side gate approval: Calendar closers not yet available as of gate UTC: METR FY2025 Form 990 (after 2026-11-16); Packard TY2025/TY2026 990-PF; several supporter TY2025 returns; June-year DAF FY2026 ret — correction required: Calendar closers not yet available as of gate UTC: METR FY2025 Form 990 (after 2026-11-16); Packard TY2025/TY2026 990-PF; several supporter TY2025 returns; June-year DAF FY2026 returns | open by date: calendar closers CAL02/CAL04 (2026-11-16) and Packard 990-PF |
| D0011 | MDP0604 | D | correction required before money-side gate approval: Statutory/public-record drafts exist unsent (MD44/MD37); PLAN.md §7 records_routes: an ordinary in-clock request prevents the gate, and nothing was sent this lane — correction required: Statutory/public-record drafts exist unsent (MD44/MD37); PLAN.md §7 records_routes: an ordinary in-clock request prevents the gate, and nothing was sent this lane | USER_AUTHORITY_WAIT: five drafts unsent (REQUESTS.jsonl); no clock is running; Kevin decides whether any is sent or waived |
| D0012 | MDP0605 | D | correction required before money-side gate approval: C02.E1 remains OPEN: METR's own named-supporter list with the capture date and page version it was taken from — correction required: C02.E1 remains OPEN: METR's own named-supporter list with the capture date and page version it was taken from | resolved: MD70 promoted 2026-09-16T18:40Z; METR's live named-supporter list captured with date and page hash (C02.E1 primary), nine dated supporter-paragraph version changes bound to C09.E1/E3 |
| D0013 | MDP0606 | D | correction required before money-side gate approval: Public Schedule B contributor identities are restricted; DAF sponsor Schedule I has no adviser/principal field — correction required: Public Schedule B contributor identities are restricted; DAF sponsor Schedule I has no adviser/principal field | N/A-with-reason (structural): public Schedule B contributor identities are restricted and DAF Schedule I has no principal field |
| D0014 | MDP0607 | D | correction required before money-side gate approval: EU contract 4500137790 METR share undisclosed; UK AISI contract amount undisclosed; EUR is never converted to USD — correction required: EU contract 4500137790 METR share undisclosed; UK AISI contract amount undisclosed; EUR is never converted to USD | open: METR's EU share and the UK AISI amount are undisclosed in checked documents; the EASE and DSIT drafts (unsent) are the routes; EUR never converted |
| D0015 | MDP0608 | D | correction required before money-side gate approval: PLAN.md §7 item 8: MD51 has not approved the gate; this lane lists corrections rather than approving — correction required: PLAN.md §7 item 8: MD51 has not approved the gate; this lane lists corrections rather than approving | resolved 2026-09-16: MD51 framing gate approved after MD53 rendering |
| D0016 | MDP0609 | D | correction required before money-side gate approval: PLAN.md §7 items 2, 9, 10: no frontier_command receipt, no two independent review receipts, no EXHAUSTION-GATE.json (this lane must not create it) — correction required: PLAN.md §7 items 2, 9, 10: no frontier_command receipt, no two independent review receipts, no EXHAUSTION-GATE.json (this lane must not create it) | open: frontier receipt and two review receipts are written at S5 closure; EXHAUSTION-GATE.json only if §7 is satisfied |
| D0017 | MDP0610 | D | correction required before money-side gate approval: identified_compatible_total and unresolved_remainder rows in commitment_reconciliation.csv have empty url fields — correction required: identified_compatible_total and unresolved_remainder rows in commitment_reconciliation.csv have empty url fields | resolved: build_commitment_reconciliation.py now writes the funding-update url on the computed rows |
| D0018 | MDP0611 | D | correction required before money-side gate approval: IRS TEOS interactive app remains HTTP 403 from this host; not a completed TEOS none-found — correction required: IRS TEOS interactive app remains HTTP 403 from this host; not a completed TEOS none-found | N/A-with-reason: TEOS interactive app is 403 from this host; the bulk e-file index is the completed TEOS-class route |

The 73 retrieval/name-form A rows (promoted row stands) are: A0012, A0014, A0017, A0021, A0038, A0039, A0069, A0091, A0103, A0104, A0105, A0110, A0115, A0116, A0119, A0120, A0145, A0154, A0170, A0171, A0172, A0187, A0192, A0206, A0211, A0256, A0257, A0258, A0259, A0260, A0261, A0262, A0263, A0264, A0265, A0266, A0267, A0272, A0273, A0274, A0275, A0276, A0277, A0278, A0279, A0292, A0293, A0294, A0331, A0332, A0333, A0393, A0394, A0395, A0396, A0397, A0398, A0399, A0400, A0401, A0402, A0403, A0404, A0405, A0406, A0407, A0408, A0409, A0417, A0457, A0458, A0462, A0467.

## 7. Cautions

1. CLAIMS.md was rendered 2026-09-16T18:36:38Z (EXHAUSTION-GATE.json 18:37:18Z, supporter_coverage.csv 18:37:19Z) before the MD99 promotion (case.json and tables modified 19:08-19:09Z; LEDGER 'S6 draft ready' 19:10:45Z). The live readiness run now differs from CLAIMS.md on two counts: C01.E4 negatives 1 -> 3 and C02.E2 negatives 180 -> 182. States and verdicts are unchanged. Figures should cite the live run or a re-rendered CLAIMS.md and must not mix the two.
2. EXHAUSTION-GATE.json's source_classes block holds only C01 and C02; the frontier command output (153 lines) is the complete record for C03-C10. gate_pass=true rests on the 22 listed exceptions.
3. C10 is 'supported', not 'supported on primary sources': C10.E2 and C10.E3 have zero primary-strength bindings; all 22 adjudication rows are supporting strength. Any figure must label the verdicts as adjudications of the posted text against pack rows, not as primary-sourced findings. C04.E3 is the other open element (0 primary), owner lane MD27-access-and-project-terms.
4. Posted-figure text (titles, kickers, README lede) is quoted in the tables only as the claim under adjudication (quote_300 of MDP0569-MDP0584 is the posted HTML/README at commit f64df65) and must never be drawn as evidence. The posted figure's own row ids (F-rows, TB01-TB04, RW-rows, the 2,911-row index snapshot) are not pack rows.
5. MDP0578 names 'B01;B06' in its identifier field; those are MD49 lane row ids. Their promoted ids are MDS1227 (metr.org/blog none found) and MDS1232 (@METR_Evals none found). Use the promoted ids.
6. Money-type rule for any drawn number: the posted $4.55M ARC figure is cash $4,477,169 plus in-kind $76,766 and must stay unsummed; the Audacious ~$38M / ~$17M / 'a bit under $16m' are restatements of one award, not three amounts; the Vanguard $8M -> $66M cluster is not a pack total; the $71M denominator has one identified addend ($350,000 Packard) and an unresolved remainder around $70.65M whose composition is embargoed (MD50 D0004).
7. MD50 open count: AUDIT-MONEY.md's footer says 'open resolutions: 11' while EXHAUSTION-GATE.json lists 12 MD50 audit lines as exceptions; the difference is D0011 (USER_AUTHORITY_WAIT), which the gate counts as an exception and the audit footer does not count as 'open'.
8. 266 promoted rows carry lane=research/rerun/MDxx-xhigh-added.csv rather than a grok-out marker (xhigh re-run additions to MD01-MD25). This audit folds them into their owning MD lane in rows_per_lane and reports them separately in rows_per_lane_of_which_xhigh_rerun_added. 51 MDF rows come from S2-lineage-import and, like the 41 S0-seed-import rows, are role=context only.
9. Superseded rows (30) are retained in the tables with 'superseded by <id> <date>' in note and remain bound as context; a figure must draw the superseding row, not the superseded one (list in effort.superseded_list). Seed rows MDF0005 and MDF0013, cited by MDP0583, are S0 context rows; the lane rows of record for the same facts are the MD15/MD16/MD18 Audacious rows (e.g. MDF0165-MDF0171) and the MD10 Longview rows.
10. MD73-ca-ag-charity-registry and MD74-ca-sos-bizfile-corporate are gap lanes created 2026-09-16T19:40Z at Kevin's instruction from route failures MDS0658/MDS1063/MDS0920 (California AG registry 404s; SOS bizfile JS shell) and launched 2026-09-16T19:19:51Z/19:19:52Z; LANES.csv state=running at build time, no research/grok-out CSV, no review, no promoted row. Their primary directories (counts in effort.primary_files_in_running_unpromoted_lanes; 443 files at build) are inside the primary_files total but hold no promoted row; LANES.csv says the gate is rebuilt on their promotion, so EXHAUSTION-GATE.json, the frontier (state registries for C02/C05/C07) and every count here will move when they promote.
11. The pack is live: promoted tables and case.json last changed 2026-09-16T19:09Z (MD99 promotion), LANES.csv at 19:20Z (MD73/MD74 launch), and research/primary/ grew from 10,746 files in 58 directories at the start of this audit (about 19:15Z) to the count recorded here at build time. Every number in this audit is as of built_utc; re-run the builder rather than editing numbers by hand.
12. supporter_coverage.csv has 22 rows: 18 supporters named by METR and 4 filed payers METR does not name (ARC program transfer, Founders Pledge, SVCF, Vanguard Charitable). Its negative_rows counts are computed from promoted rows and exclude seed-context rows; 'acknowledged_no_amount' means no promoted row gives an amount, date or vehicle (MD50 D0006: structural, no public amount exists to add).
13. Frontier PARTIAL is an engine state (casework/frontier.py): a class with fresh evidence/negative bindings is PARTIAL while an open element names it; C04's three PARTIAL classes are named by C04.E3 and C10's three by C10.E2/C10.E3. The 89 N/A cells are structural reasons recorded by MD52 Task D (D01-D89), not searches that failed.
14. No motive language: casework.json bans 'intended', 'scheme', 'secretly', 'coordinated', 'captured', 'wanted to', 'sought to', 'laundering', 'corruption', 'bribe', 'quid pro quo'. MD51 C06/C07 found 'intended' and 'captured' in the posted figures; the pack's own rendered figures passed scripts/lint_figures.py. Only public people in public roles are named (Moskovitz, Tuna, Tallinn, Schmidt, Barnes, Painter, Gleave, Karnofsky, Christiano, Cotra, Amodei, Altman, Sacks); Jane Street individuals and DAF principals stay unnamed.
15. Records routes: five drafted statutory requests (REQ-MD44-UK-DSIT-FOI, REQ-MD44-US-NIST-FOIA, REQ-MD44-EU-EASE-1049, REQ-MD37-NPT-6104D, REQ-MD41-IRS-4506A-5227) are unsent with no clock running; a figure may show them as drafted routes, never as pending or filed requests.

## 8. Suggested figures

- Adjudication grid: 16 posted claims (rows C01-C16, MDP0569-MDP0584) and 6 METR-attributed sentences (B11-B16, MDP0563-MDP0568) as a verdict strip: posted = 2 accurate (C13, C14), 11 incomplete, 3 undetermined (C05, C06, C09); response = 3 incomplete (B12, B14, B15), 3 undetermined (B11, B13, B16). Second column: the exact missing document (next_document). Third column: what the pack does establish, cited by promoted id. (source: research/CLAIMS.md C10 tables; provenance.csv MDP0563-MDP0584)
- Element readiness board: 10 claims x 38 elements: evidence count, primary count, negative count, state; 3 open elements highlighted (C04.E3 owner MD27; C10.E2 and C10.E3 owner MD49). Verdict floor per claim: 8 supported_primary, 2 supported (C04, C10). (source: casework readiness (live) or CLAIMS.md with the two negative-count deltas noted)
- Source-class frontier matrix: 10 claims x 15 source classes = 150 cells: 55 COVERED, 6 PARTIAL (C04: issuer statements, project documents, archives; C10: issuer statements, self-statements, archives), 89 N/A-with-reason (MD52 D01-D89). No UNTOUCHED cell. (source: casework frontier output; EXHAUSTION-GATE.json (C01-C02 only))
- Effort by lane and table: 4548 promoted rows across 8 tables (MDS 1690, MDF 1032, MDP 744, MDT 435, MDR 207, MDQ 181, MDE 140, MDI 119) and 57 promoted lanes plus two imports; saved primary files per lane (effort.primary_files_per_lane; exclude the running MD73/MD74 directories); per-lane bars with role (evidence/negative/context) stacking. (source: effort.rows_per_lane, effort.primary_files_per_lane)
- Seed-versus-lane delta: 41 S0 seed rows (all context) and 51 S2 lineage rows (all context) versus 4456 lane rows; 30 superseded rows (10 seed: MDF0002, MDF0003, MDS0001-MDS0008 via MD50 A0002/A0003/C0002-C0009/E0003; 20 lane rows replaced by xhigh re-run or review corrections). (source: effort.superseded_list; AUDIT-MONEY.md; AUDIT-RESOLUTIONS.json)
- Bounded negatives per named supporter: 22 supporter/payer rows: negative-row count and status (9 amount_identified, 13 acknowledged_no_amount); highest Audacious 55, Pew 37, ARC 36, Longview/SFF 34, Packard 33, AISI 31, Vanguard 30; lowest EU AI Office 3, Newman 9. (source: research/supporter_coverage.csv)
- Adversarial audit outcomes: MD50: 510 rows; Task A 468 (391 verified live, 73 mismatches resolved as retrieval/name-form with the promoted row standing, 4 seed rows superseded); Task B 9 double-count/period/cross-type attacks recorded with no correction; Task C 12 (1 coverage, 8 seed negatives superseded, 3 open-recorded); Task D 18 gate items (7 resolved: D0002, D0003, D0008, D0009, D0012, D0015, D0017; 2 N/A-with-reason: D0013, D0018; 8 open: D0001, D0004, D0005, D0006, D0007, D0010, D0014, D0016; 1 USER_AUTHORITY_WAIT: D0011); Task E 3 negatives. MD51: 36 rows; 19 framing defects in the posted figures, all resolved by MD53 rendering; gate D01 approved. (source: AUDIT-MONEY.md; AUDIT-FRAMING.md; AUDIT-RESOLUTIONS.json)
- Gate exceptions calendar: 22 exceptions: 1 records_routes line (5 unsent drafts), 9 calendar closers (CAL08 2026-10-15; CAL05 2026-10-16; CAL01 2026-11-04; CAL02/03/04/07 2026-11-16; CAL09/10 when posted), 12 MD50 audit lines (3 Task C open-recorded row-form items C0010-C0012; 8 Task D open items D0001, D0004, D0005, D0006, D0007, D0010, D0014, D0016; 1 USER_AUTHORITY_WAIT D0011). (source: research/EXHAUSTION-GATE.json exceptions)
