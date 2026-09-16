# Figure audit C — METR's own filings and statements about its own money

Pack: `/mnt/f/projects/anthropic/metr_deep` (read-only). Subject: Model Evaluation and Threat Research, Inc. (METR), EIN 99-1219864. Audit date 2026-09-16. Companion JSON: `C-metr-own-filings.json` (same directory).

Method. All seven research tables plus `research/commitment_reconciliation.csv` were parsed (4,341 rows; 30 rows whose note contains "superseded by" were skipped and are listed in §6). The FY2024 Form 990 was re-read leaf by leaf from the pack primary `research/primary/MD01-metr-recipient-baseline/metr-fy2024-990-202523209349300367-20260916T053316Z.xml`; its SHA-256 was recomputed here as `84979ec8023f9e286198370353fab8d8bf01d76befe637ff8c1bf2bd9d20c8d9`, identical to the two other captures in the same folder and to the hash every pack row cites. Every amount below was checked against that XML. Rules applied: money types are never summed across type; a commitment statement is not revenue; no motive language. Seed rows (lane `S0-seed-import`, checked_utc 2026-09-14) are the baseline and are marked **seed**; rows added by MDnn lanes are marked **new**. Note on lanes: the `lane` column is empty on every row; lane provenance is in `note` as `lane=research/grok-out/<file>#<row>` (or `research/rerun/...-xhigh-added.csv`).

---

## 1. FY2024 Form 990 — the only fiscal year filed

**Period.** TaxPeriodBeginDt 2024-05-01, TaxPeriodEndDt 2024-12-31, TaxYr 2024, `InitialReturnInd=X`, `FormationYr=2024`, `LegalDomicileStateCd=DE`. Schedule A Part VI: "TAX YEAR 2024 IS A SHORT YEAR AS IT IS THE ORGANIZATION'S INITIAL YEAR OF ACIVITY." (sic). Schedule O: "FIRST FORM 990 SUBMITTED AS AN ORGANIZATION WILL BE FOR THIS YEAR (2024)." Eight months, not a calendar year (MDF0410 **new**, MDP0277 **new**, MDS1112 **new**). Index hits: index_2024 0, index_2025 1, index_2026 0 (MDP0277). FY2025 return not yet indexed; due after 2026-11-16 (MDP0603, MDS0345, MDS1189).

**Filing.** ReturnTs 2025-11-16T12:01:28-06:00; SignatureDt 2025-11-14; signing officer BHASKAR CHATURVEDI, SECRETARY (ReturnHeader, not Part VII — MDE0089 **new**); preparer ABBOTT STRINGHAM & LYNCH; PrincipalOfficerNm ELIZABETH BARNES; books in care of GRAPHITE FINANCIAL GROUP LLC. Locator: IRS index_2025 row `,EFILE,991219864,202412,2025,MODEL EVALUATION AND THREAT RESEARCH INC,990,93493320003675,202523209349300367,2025_TEOS_XML_11C` (MDS0115 **new**). Primary URLs: `https://apps.irs.gov/pub/epostcard/990/xml/2025/2025_TEOS_XML_11C.zip` (member `202523209349300367_public.xml`) and `https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202523209349300367_public.xml` (byte-identical). ProPublica restates Revenue $13,639,155 / Expenses $8,234,524 (MDP0031); ProPublica API `filings_with_data` empty (MDP0262, MDS0748). IRS TEOS app HTTP 403 from this host (MDS0019 etc.); per-object IRS URL 404 (MDS0122).

### 1.1 Lines (as filed; XML-verified in this audit)

| Line | Amount | Pack rows | Strength |
|---|---|---|---|
| GrossReceiptsAmt | 13,639,155 | MDF0410 (quantity_or_value) **new** | primary |
| Part VIII 1h / Part I 8 — CYContributionsGrantsAmt = TotalContributionsAmt | **13,603,035** | MDF0146, MDF0410 (quantity_or_value only); MDS0588, MDS0587 (quote); MDP0619; Schedule A PublicSupportTotal170Amt 13,603,035 (MDS1026) | primary; **no standalone amount row** |
| Part VIII 1d — RelatedOrganizationsAmt (from Alignment Research Center, EIN 86-3605182) | **4,501,424** | MDF0034 **new** (DIFFERS), MDP0032 **new** (DIFFERS), MDF0497, MDS0587, MDP0587, MDS1617 | primary; Schedule R type C InvolvedAmt 4,501,424, FAIR MARKET VALUE |
| Part VIII 1f — AllOtherContributionsAmt ("all other contributions", unnamed) | **9,101,611** | MDF0411 **new** (supersedes MDF0035), MDF0498, MDF0874, MDS0588, MDS0432 | primary |
| Part VIII 1e — GovernmentGrantsAmt | **element absent** (not reported) | MDS0589 **new** | primary (absence verified) |
| Part VIII 2g / Part I 9 — CYProgramServiceRevenueAmt | **0** | MDS0589 | primary |
| Part VIII 3 — CYInvestmentIncomeAmt | 36,120 | MDF0410 (quantity_or_value); MDS0587/MDS0588 (quote) | primary; inside other rows only |
| CYOtherRevenueAmt | 0 | MDF0410 (quantity_or_value) | primary |
| Part I 12 — CYTotalRevenueAmt | **13,639,155** | MDF0146 **new** (MD25 B01), MDF0410 **new** (supersedes MDF0031), MDP0031 **new** (recon excluded), MDF0494/0609/0873 (audit rows), MDP0497, MDP0639 | primary |
| Part I 18 / Part IX 25 — CYTotalExpensesAmt | **8,234,524** (program 6,924,735; M&G 1,144,255; fundraising 165,534) | MDF0147 **new** (DIFFERS), MDF0610 | primary |
| Expense components | salaries/comp/benefits 4,505,180; other expenses 3,729,344; grants paid 0; professional fundraising 0 | MDF0147 quantity_or_value (salaries only) | primary; mostly XML-only |
| Part IX selected lines | officer comp 1,118,235; other salaries 2,962,402; IT 1,127,374; "DATA & RESEARCH CONTRAC" 1,103,985; occupancy 429,410; "AWARDS" 204,427; legal 191,234; "RECRUITMENT" 184,544; other fees 198,593; management fees 123,859 | none | XML-only |
| Part I 19 — CYRevenuesLessExpensesAmt | **5,404,631** (= 13,639,155 − 8,234,524, checked) | MDF0147 quantity_or_value | primary |
| Part X 32 — NetAssetsOrFundBalancesEOYAmt | **5,404,631** (BOY 0); total assets 6,544,206; liabilities 1,139,575; cash 854,773 + savings/temp 5,225,268; AR 325,984 | MDF0032 **new**, MDF0495 | primary |
| Part X 27-29 — restricted-fund lines | `OrgDoesNotFollowFASB117Ind=X`; `DonorRstrOrQuasiEndowmentsInd=0`; RtnEarnEndowmentIncmOthFndsGrp EOY 5,404,631; with/without-donor-restriction groups **absent** | MDP0150 **new** (DIFFERS), MDF0032 | primary; no restricted split filed |
| Schedule B (public copy) | `ScheduleBRequiredInd=1`; one ContributorInformationGrp with ContributorNum, name, address lines, city, state, ZIP and TotalContributionsAmt all the literal token **RESTRICTED**; `DonorAdvisedFundInd=0` | MDS0011 **new**, MDS0094, MDS0586, MDS0769, MDS0238, MDS0270, MDS0415, MDS0895, MDP0606 | primary; legal §6104(d) redaction |
| Schedule A | 170(b)(1)(A)(vi) public charity; `First5Years170Ind=X`; support 13,603,035 + 36,120 = 13,639,155; no named substantial contributors | MDS1026 **new** | primary |
| Schedule D Parts XI-XII (audited-statement reconciliation) | audited revenue 14,080,505; **DonatedServicesAndUseFcltsAmt 441,350**; 990 revenue 13,639,155; audited expenses 8,675,875; expenses not reported 441,351 (441,350 + "ROUNDING 1."); `FSAuditedInd=1`, `IndependentAuditFinclStmtInd=1`, `AuditCommitteeInd=1`; `binaryAttachmentCnt="0"` | MDS0112 **new** (note), MDF0032 (note), MDP0273 (Schedule O: "THE AUDIT COMMITTEE FORMED IN 2025 TO REVIEW THE FY2024 AUDIT.") | XML-only for 441,350; **not in in_kind_access.csv** |
| Schedule R | related org ALIGNMENT RESEARCH CENTER, EIN 863605182, 440 N BARRANCA AVE **9807** COVINA CA (METR: 440 N BARRANCA AVE **3345**), 501(C)3, LINE 7, `ControlledOrganizationInd=0`; transactions: C 4,501,424; **E 490,182** (loans/guarantees by related org); **D 325,431** (loans/guarantees to related org); Part V `LoansOrGuaranteesToOtherOrgInd=1`, `LoansOrGuaranteesFromOthOrgInd=1` | MDF0034 (limitation names D and E), MDE0132, MDS0587 | primary for C; XML-only for D/E |
| Schedule I | **absent** (schedules present: A, B, D, F, J, O, R); `CYGrantsAndSimilarPaidAmt 0` | MDS1112 **new** | primary |
| Schedule F | 63 employees/contractors outside the US in 6 regions, 0 offices, TotalSpentAmt 396,556 (Europe 324,366 / 45 people, "REMOTE EMPLOYEE AND CONTRACTOR SERVICES") | MDE0038 (limitation mentions 63) | XML-only |
| Part I 5 / Part V — employees | TotalEmployeeCnt 38; EmployeeCnt 38; volunteers 3; IRPDocumentCnt 24; 18 individuals > $100K | MDE0038 **new**, MDE0039 **new** | primary |
| Part VII — officers/directors (org / related org / other comp) | ELIZABETH BARNES CTO/CEO 172,737 / 75,637 / 6,416; EMMA ABELE CEO/COO 190,395 / 52,375 / 6,849; RAJIV DATTANI COO AND TREASURER 230,384 / 0 / 630; ADAM GLEAVE DIRECTOR (0.50 h/wk) 0; KYLE SCOTT SECRETARY AND TREASURER 141,577 / 94,127 / 630 | MDE0084-MDE0088 **new** (names and titles only) | amounts XML-only |
| Part VII — key and highest-paid | CHRIS PAINTER (policy) 167,556 / 84,123 / 7,358; BEN WEST 215,587 / 0 / 5,048; MAKSYM TARAN 243,560; KATHARYN GARCIA 226,183 / 0 / 4,948; TAO LIN 184,335 / 84,127 / 5,993; HANNES HJALMAR WIJK 160,170 / 67,212 / 6,486; HAROLD BROADLEY 144,693 / 0 / 7,674; totals 2,077,177 org / **457,601 related org** / 52,032 other; contractor QALLY'S (RESEARCH CONTRACTOR) 147,200 | none | XML-only |
| Schedule J | compensation committee, independent consultant, other orgs' 990s, written contracts, survey, board approval all X; no bonus / deferred / severance / equity-based / revenue-based comp | MDP0275 (Schedule O line 15 text) | primary |
| Part VI governance | 3 voting members, **1 independent**; `ConflictOfInterestPolicyInd=1`; annual disclosure 1; monitoring/enforcement 1; whistleblower 1; document retention 0; Schedule O 12C "AS PART OF THE BI-ANNUAL REGULAR BOARD MEETINGS, THE BOARD DISCUSSES AND DOCUMENTS ALL POTENTIAL CONFLICTS OF INTEREST…"; 11B "THE 990 IS REVIEWED BY THE OPERATIONS TEAM, TREASURER, AND BOARD MEMBERS BEFORE FILING."; 19 "METR GOVERNING DOCUMENTS, CONFLICT OF INTEREST POLICY AND FINANCIAL STATEMENTS ARE MADE AVAILABLE TO THE PUBLIC UPON REQUEST…"; `UponRequestInd=X`; copy filed with CA | MDP0272, MDP0674, MDP0675, MDP0231, MDP0269, MDP0270, MDP0271, MDP0273, MDP0274, MDP0275, MDS0663, MDS0789, MDQ0069 (all **new**) | primary |
| Mission | "METR IS ADVANCING SCIENTIFIC METHODS TO ASSESS CATASTROPHIC RISKS FROM AI SYSTEMS' CAPABILITIES AND ENABLE INFORMED AI DEVELOPMENT AND GOVERNANCE."; single program-service expense 6,924,735 | MDE0053, MDS0585 | primary |

Arithmetic checks done here: 4,501,424 + 9,101,611 = 13,603,035; 13,603,035 + 36,120 = 13,639,155; 13,639,155 − 8,234,524 = 5,404,631; 6,924,735 + 1,144,255 + 165,534 = 8,234,524; 13,639,155 + 441,350 = 14,080,505; 8,234,524 + 441,351 = 8,675,875. All hold.

Related-organization line vs ARC-side filing: ARC's own FY2024 Schedule I shows CashGrantAmt 4,477,169 (MDF0064 **new**) plus NonCashAssistanceAmt 76,766 "COMPUTERS" at book (MDF0065 **new**), Schedule N DistributionDt 2024-04-30. The seed row MDF0007 **seed** carries 4,553,935, which is cash + non-cash summed. Pack rule (MDP0587): these are different filed figures for one spin-off, never two payments. MDF0064's note says the cash difference is "$47,511"; 4,501,424 − 4,477,169 = 24,255 (note defect, §6).

Schedule B availability: "Public Schedule B contributor identities are restricted" is the legal public-inspection state of a public charity's return (MDS0011 limitation; MDP0606). Redaction is not evidence of any named contributor.

---

## 2. METR's public statements about its own money (exact quotes)

Each entry: date · document · quote · money type · rows · what it does not say. **seed**/**new** as marked.

**S1. 2026-08-14 funding update** (`https://metr.org/blog/2026-08-14-funding-update/`; JSON-LD datePublished 2026-08-14T00:00:00-07:00; live SHA-256 ea456b2a…; Wayback 20260827031340 MDP0479).
- "In the last 6 months, METR raised commitments of around $71 million." — commitment; around $71,000,000. MDF0089 **new** (primary re-fetch), MDF0001 **seed**, MDF0145, MDF0463, MDP0029, MDT0033.
- "This will fund ambitious projects: studying autonomous capabilities, tracking recursive self-improvement, evaluating monitoring systems, conducting risk assessments, investigating AI incidents, and more." — use-of-funds gloss, not a restriction or allocation. MDP0171 **new**.
- "We work to maintain our independence from frontier AI companies, especially as our risk assessments become more consequential. We have not accepted funding from these companies, and we do not accept donations made by or at the direction of their staff. However, frontier AI companies currently provide a significant amount of free tokens for our evaluations, research, and engineering." — rule statement; in-kind unquantified. MDP0279, MDT0127, MDI0034, MDS0719 (all **new**).
- "Thank you to everyone who has supported METR over the years: The Audacious Project, through which we received our first institutional-scale funding; individuals from Jane Street; foundations like the Sijbrandij Foundation, The Pew Charitable Trusts, Schmidt Sciences and the Packard Foundation; and many others, including David Farhi, Geoff Ralston, Dylan Field and Steve Newman." — acknowledgment, no amounts. MDP0027, MDT0252, MDF0019/MDF0482, MDF0024/0026/0028/0030, MDP0049, MDP0147, MDS0450.
- Does not say: composition; per-donor amounts; whether any is paid; whether in-kind is inside; the calendar bounds of "the last 6 months" (pack derives ≈2026-02-14 to 2026-08-14); whether Audacious/Canary multi-year money is inside; instrument dates (MDF0089 limitation; MDS1689; MDP0524-MDP0529).

**S2. 2025-09-28 Beth Barnes shortform comment** (GreaterWrong render, postedAt 2025-09-28T20:34:12.755Z per LessWrong GraphQL, SHA-256 e31dca3c…; LessWrong HTML rate-limited, EA Forum GraphQL missing_document).
- "Budget: We run at ~$13m p.a. rn (~$15m for the next year under modest growth assumptions, quite plausibly $17m++ given the increasingly insane ML job market)." — run-rate (spend); not inbound. MDF0465 **new** (supersedes MDF0002 **seed**), MDP0059, MDP0036 (recon excluded), MDP0502.
- "Runway: Depending on spend/growth assumptions, we have between 12 and 16 months of runway." — runway; not a funding event. MDF0466 **new** (supersedes MDF0003 **seed**), MDP0037, MDT0034, MDP0503.
- "Audacious funding: This ended up being a bit under $16m, and is a commitment across 3 years." — commitment restatement; not an exact integer; not additive with the 2024 ~$17M. MDF0169 **new**, MDF0004 **seed**, MDF0172, MDP0035, MDP0152, MDP0501.
- "The audacious funding was a one-off, and we need to make sure we have a sustainable funding model." — nature clause. MDP0145 **new**.
- "Our fundraising goal for the end of 2025 is to raise $10M" — goal, not revenue. MDP0060 **new** (DIFFERS).
- Does not say: fiscal basis of "p.a."; cash balance; committed-but-unpaid balance; 3-year start/end; paid-to-date.

**S3. 2024-10-09 Audacious announcement.** METR blog: "Approximately $17 million of this will support work at METR." (MDF0166 **new**, MDF0006 **seed**, MDP0034). RAND press release: "The Audacious Project, a collaborative funding initiative housed at TED, has committed approximately $38 million to RAND and METR for Canary, a new research collaboration designed to help make future AI systems safer." (MDF0165, MDF0173, MDF0005 **seed**, MDP0033, MDP0586; live rand.org HTTP 403, quote via r.jina.ai/Wayback). Does not say: payment schedule, term, or payer of record. The only filed Audacious-partner payments found went to RAND (Valhalla $10,000,000; High Tide $333,334 — MDP0046, MDP0047).

**S4. 2024 Annual Report PDF** (`https://metr.org/2024-annual-report.pdf`, SHA-256 e7f0c272…, 10,749,402 bytes, robots-disallowed, live 200).
- "METR achieved this and more on a total 2024 budget of $10 million." — budget; type empty. MDP0057 **new** (DIFFERS), MDS1025.
- "In 2025, we seek to raise and deploy $15 million, and intend to achieve even more than in 2024." — target. MDP0058 **new** (DIFFERS).
- Not a 990 or audited statement; names no net assets (MDS1025). No 2025 annual report exists (`/2025-annual-report.pdf` 404, MDS0348).

**S5. metr.org/about, funding paragraph** (live 2026-09-16; funding section first captured 2025-07-14, MDT0061).
- Live: "METR is funded by donations. We are grateful to METR's many supporters: from METR's first institutional-scale funding through The Audacious Project (a funding initiative housed at TED); to individuals from Jane Street; foundations such as the Sijbrandij Foundation, The Pew Charitable Trusts, Schmidt Sciences, the Packard Foundation, LaCentra-Sumerlin Foundation, Astralis Foundation and Expa.org…" (MDF0018 **new** DIFFERS; MDP0028 DIFFERS; MDP0004; MDP0054; MDP0048; MDP0717).
- Earlier: "METR is funded by donations. Our largest funding to date was through The Audacious Project, a funding initiative housed at TED. METR has not accepted funding from AI companies, though we make use of free compute credits, as noted above. Being independently funded has been crucial…" (2025-07-14 capture, MDT0061/MDT0065/MDT0130/MDT0306). "Our largest funding to date" persists through capture 2026-07-19T23:27:59Z (MDT0411) and is replaced by "first institutional-scale funding" from capture 2026-08-04T07:49:10Z (MDT0412) — before the 2026-08-14 post.
- Live rule sentence: "METR has not accepted funding from AI companies, though we make use of significant free tokens, which we use for evaluations, research, and engineering, as noted above. Independent funding has been crucial for our ability to pursue the most promising research directions and set standards for evidence-based understanding of risks from AI." (MDP0230 **new**, MDI0001 **seed**, MDP0238). Wording path: "free compute credits" (2025-07-14) → "significant free compute credits" (by 2026-07-19, MDT0116) → "significant free tokens" (by 2026-08-04).
- Live: "(Note: METR cannot accept donations made by or at the direction of frontier AI company employees.)" — first on /about 2026-07-19T17:12:36Z without "Note:" (MDT0071, MDT0131, MDT0002/MDT0003 **seed**); "Note:" prefix by 2026-08-04 (MDT0115); live MDT0016, MDT0125.
- Live: "Additionally, a small part of our income is from a technical assistance contract with the European AI Office, supporting their approach and technical methods for assessing loss of control risks." — first captured 2026-02-02 (MDT0069); MDP0051, MDP0182, MDP0187, MDF0017 **seed**. TED notice 864574-2025 consortium total EUR 1,167,484; METR share undisclosed. UK AISI partnership: no public amount (MDP0050, MDF0016 **seed**).
- Does not say: any amount, date or vehicle for any named supporter; token volumes or values; whether contracts count as "funding".

**S6. metr.org/donate** (live 2026-09-16; EIN 99-1219864 and legal name "Model Evaluation and Threat Research, Inc." on the page, MDE0016/MDE0036).
- "Donations fund our assessment of AI capabilities, risks and mitigations, and are crucial for our ability to pursue groundbreaking projects. We keep our evaluations independent and trustworthy by relying on support from a wide range of independent donors." (MDS0022, MDS1652, MDS0720).
- "(METR cannot accept donations made by or at the direction of frontier AI company employees.) All every.org donations are re-granted to METR as batched, unrestricted donations. Every.org does not charge METR for use of the platform, but transaction fees are deducted out of your donation." (MDT0126, MDP0138; parenthesis first on /donate at capture 2026-08-04T02:46:01Z, absent 2026-07-03 — MDT0108/MDT0109/MDT0132). 2025-04-01 wording: "All donations are unrestricted, even if you give to a specific fundraiser." (MDT0134).
- Historical footnote: "To date, April 2025, we have not accepted compensation from AI companies for the evaluations we have conducted." (first capture 2025-04-18, MDT0107/MDT0128, MDT0001 **seed**) → "To date, September 2025, we have not accepted compensation from AI companies for the evaluations we have conducted. However, companies have provided access and compute credits to enable evaluations and evaluation research." (by 2025-10-02, MDT0113/MDT0129) → footnote absent between captures 2026-02-05 and 2026-02-11 (MDT0110/MDT0111).
- No $71M sentence, no supporter names, no amounts on the donate page (MDS1122, MDS1652).

**S7. Frontier Risk Report, 2026-05-19** (`https://metr.org/blog/2026-05-19-frontier-risk-report/`; assessment window 2026-02-16 to 2026-03-16). The brief says 2025-05-19; every pack row and the URL say **2026-05-19**.
- Table A.1 item 2.1 = **Yes**: "METR did not request or receive compensation for this assessment. Participants provided complimentary access to their models." (MDQ0051 DIFFERS, MDP0250, MDP0256, MDQ0063)
- Item 2.3 = **No**: "The evaluator has published a conflict of interest policy, and it was applied to the evaluation." (MDQ0049, MDQ0082)
- Item 2.4 sub-answers all No, including: "Does a meaningful fraction of the evaluator's funding come from the system provider, its employees, or its direct competitors? No. Note that METR's work with nonpublic models and use of free tokens incentivize a cordial relationship with AI companies." (MDQ0084)
- Item 2.4.6: "Several of the staff and collaborators directly involved in this pilot (at least 6) have close personal relationships with AI company staff." (MDQ0054, MDQ0083, MDQ0001 **seed**)
- Item 2.5 = **Yes**: "The evaluator recused any individuals with a significant financial interest in the system provider from carrying out the evaluation." (MDQ0052, MDQ0085)
- Item 5.4 = **No**: "METR has not established a specific responsible disclosure policy." (MDQ0050)
- Preamble: "METR did not have an applicable personnel conflict of interest (CoI) policy in place at the start of this project, and as such we did not run a formal recusal or disclosures process. Given this, this pilot was not compliant with all of the requirements of the AEF-1 standard." (MDQ0044, MDQ0080, MDQ0048, MDQ0064, MDP0716; no policy in force per MDQ0089/MDQ0090/MDQ0177; COI policy v1.0 is dated 2026-08-28)
- Institutional sentence: "…not accepting cash payments or donations from AI companies and AI lab executives. Also note that some METR staff have strong social ties to employees of AI companies, and METR currently works out of a shared research center (Constellation) which hosts some AI…" (MDQ0055)
- Table 3 inference budget: "~$500-$5K (500M tokens)" (MDI0049).
- The two "No" answers are 2.3 and 5.4. The page does not name the at-least-6, does not value complimentary access, and does not reconcile 2.5 Yes with the preamble (MDQ0052, MDQ0064 "undetermined").

**S8. 2026-08-26 OpenAI / Hugging Face investigation.** "We estimate we spent roughly ~$400K in API credits over the six days of our investigation." — in_kind_estimate. MDI0047 **new**, MDI0002 **seed**, MDP0052 (recon excluded; dated after 2026-08-14).

**S9. 2026-08-31 security update.** "These credits would have been worth approximately $600,000, although the model developer had granted them to METR for free." — in_kind_estimate (valuation of free credits). MDI0043, MDI0051, MDI0078, MDI0081, MDP0672 (all **new**). Not summed with S8.

**S10. 2026-09-11 Business Insider (press).** Barnes: "Ideally, we'd like to scale really large, but in practice, we've been able to fundraise as much as we need, and the bottleneck is much more talent," — qualitative; no amount. MDP0061 **new** (DIFFERS).

---

## 3. Reconciliation of the ~$71M (`research/commitment_reconciliation.csv`)

Header: derived from promoted rows only by `scripts/build_commitment_reconciliation.py` at 2026-09-16T18:36:38Z; 66 data rows (1 denominator, 1 compatible_component, 31 excluded, 31 remainder_statement, 2 computed).

**Denominator** — MDF0089, commitment, 71,000,000 USD, 2026-08-14, period "the last 6 months (sentence as of 2026-08-14; derived window approximately 2026-02-14 to 2026-08-14)", reason "METR's own statement of commitments raised in the last 6 months; approximate". Working integer inherits "around" (MDP0055).

**Compatible** — MDP0030, The David and Lucile Packard Foundation, commitment, 350,000 USD, 2026-07-06 (JSON-LD datePublished of the grantee page), "award year 2026; listing 2026-07-06 inside window"; catalog fields Year 2026 / Term 12 / Amount $350,000 / Purpose for general support (MDF0020 **new**, DIFFERS). Caveats: listing date is not an instrument date; paid vs approved not on the page (MDP0585, MDP0589, MDP0591, MDP0598); MDF0020 itself says the lane "has no source connecting the $350,000 to METR's approximately $71 million Feb-Aug 2026 total" — compatibility is a period/type/currency test. If Packard is later excluded, compatible total becomes 0 and the remainder the whole ~$71M (MDP0055). The same award sits on MDF0020, MDF0021, MDF0078, MDF0090-0092, MDF0191-0193, MDF0416 (MDP0585): never sum `funding_events.csv`.

**Remainder** — 71,000,000 − 350,000 = 70,650,000 commitment-USD, "inherits around", "residual, not a donor list" (MDP0055, MDP0056 DIFFERS, MDP0521, MDP0522, MDP0592, MDP0739). Computed rows: `identified_compatible_total` (row_id written as MDP0030 — duplicate) and `unresolved_remainder` (row_id blank). Side-by-side discipline: do not add ~$71M to $13,639,155, to the $10M budget, to the ~$13M run-rate, to Audacious/Canary figures or to EUR; do not compute 71,000,000 − 13,639,155 (MDP0062, MDP0063, MDP0523).

**Excluded (31), reason column verbatim:**

| row | counterparty | type | amount | ccy | date | reason |
|---|---|---|---|---|---|---|
| MDP0031 | (METR itself) | filed_grant | 13,639,155 | USD | 2024-12-31 | Filed revenue is not a commitment. FY2024 is before the last-6-months window. |
| MDP0032 | Alignment Research Center | transfer | 4,501,424 | USD | 2024-12-31 | This lane re-fetched the FY2024 Form 990 XML. RelatedOrganizationsAmt is a transfer, not a commitment, and FY2024 is before the last-6-months window. |
| MDP0033 | The Audacious Project (TED) | commitment | 38,000,000 | USD | 2024-10-09 | Joint-project commitment; not a METR-only amount. Approximate. |
| MDP0034 | The Audacious Project (TED) | commitment | 17,000,000 | USD | 2024-10-09 | Subset of the ~$38M Canary commitment; not additive with it or with the later bit-under-$16m restatement. |
| MDP0035 | The Audacious Project (TED) | commitment | <16,000,000 | USD | 2025-09-28 | Not an exact integer. Not additive with the 2024-10-09 $17 million figure. |
| MDP0036 | (METR run-rate) | commitment (typing defect) | ~13,000,000 per year | USD | 2025-09-28 | A run rate is not an inbound amount. |
| MDP0037 | (METR runway) | — | — | — | 2025-09-28 | Runway is derived spend coverage, not a funding event. |
| MDP0038 | Survival and Flourishing Fund (Jaan Tallinn) | recommendation | 204,000 | USD | SFF-2024 | Round label SFF-2024 is not a day date. A recommendation is not a commitment and not a payment. |
| MDP0039 | Survival and Flourishing Fund (Jaan Tallinn) | recommendation | 120,000 + 428,000 matching pledge | USD | SFF-2025 | Two figures on one row are not summed. Matching pledge is not a payment. Round 2025 is not the last-6-months-to-2026-08-14 window. |
| MDP0040 | Survival and Flourishing Fund | recommendation | 220,000 | USD | 2025-02-15 | Page last published 2025-02-15. Adjacent $1,210,000 column is not added. Recommendation not commitment. |
| MDP0041 | Founders Pledge Inc | filed_grant | 184,000 | USD | 2024 | TY2024 filed grant is not a 2026 commitment. A filed_grant is not a commitment. |
| MDP0042 | Silicon Valley Community Foundation | filed_grant | 20,000 | USD | 2024 | TY2024 filed grant. DAF sponsor is not the account principal. |
| MDP0043 | Vanguard Charitable Endowment Program | filed_grant | 4,000,000 | USD | FY2025 (2024-07-01 to 2025-06-30) | Live ProPublica Schedule I HTML is a JS shell without grant rows; gt990datalake S3 XML 404; IRS 2026_TEOS_XML_05A.zip (521158638 bytes) listing does not contain OBJECT_ID 202621329349306657. Amount is a seed-held known amount quoted from S0-seed-import.csv. |
| MDP0044 | Longview Philanthropy (public fund) | recommendation | 220,000 | USD | 2023 | Recommendation not payment. 2023 period. |
| MDP0045 | Effektiv Spenden (Giving Fund: Safeguarding the future) | regrant | 128,000 | EUR | 2023-08 | Live page HTTP 403 this host. Quote is from Wayback 20250126120532 capture. EUR is not USD. Never convert and add. |
| MDP0046 | Valhalla Foundation | filed_grant | 10,000,000 | USD | 2024 | A payment to RAND is not a payment to METR. ProPublica /full HTML is a shell; XML is the primary. |
| MDP0047 | High Tide Foundation | filed_grant | 333,334 | USD | 2024 | A payment to RAND is not a payment to METR. Purpose text is as filed (tTHE). |
| MDP0048 | individuals from Jane Street | commitment | undisclosed | — | undated | METR names individuals, not the firm. No individual is named and no amount is public. This lane does not deanonymize Jane Street individuals. |
| MDP0049 | David Farhi; Geoff Ralston; Dylan Field; Steve Newman | commitment | undisclosed | — | undated | Page appearance of a name is not a gift date (STATE.md). Individuals, employers and any DAF accounts stay unmerged. Wave 1 MD08 found no public gift amounts. |
| MDP0050 | AI Security Institute (UK) | contract | undisclosed | — | undated | No public METR award amount on the about page. Contract is not a commitment. |
| MDP0051 | European AI Office | contract | undisclosed share of EUR 1,167,484 | EUR | 2025-12-15 | TED notice 864574-2025 GET returned HTTP 202 empty body this lane (cap). Consortium award; METR share not on the about page. EUR not USD. |
| MDP0052 | (OpenAI API credits, HF investigation) | in_kind_estimate | 400,000 | USD | 2026-08-26 | In-kind estimate is not a cash commitment. Date 2026-08-26 is after 2026-08-14. |
| MDP0053 | Coefficient Giving | paid_grant | — | — | 2025-12 | A staff suggestion to individual donors is not a Coefficient grant. Date of the note is 2025, before the window. |
| MDP0054 | The Pew Charitable Trusts; Schmidt Sciences; Sijbrandij Foundation; LaCentra-Sumerlin Foundation; Astralis Foundation; Expa.org | — | undisclosed | — | — | Wave 1 MD03-MD06 found no METR grant amounts. Packard is the exception and is counted once in C02, not here. Sibling Wave 1 may still be incomplete for MD09-MD13. |
| MDP0481 | Alignment Research Center | transfer | 4,477,169 | USD | 2024-04-30 | A 2024 program spin-off transfer is not a 2026 commitment. Non-cash $76,766 is a different money_type (in_kind_estimate) and is not added here. |
| MDP0484 | Jaan Tallinn | paid_grant | 184,000 | USD | 2024-12-06 | Three 2024 disbursements; not summed here with each other for the denominator test. A paid_grant is not a commitment. 2024 is before the window. |
| MDP0485 | Open Philanthropy | recommendation | 265,000 | USD | 2022-03 | Live Open Philanthropy grants index redirected (E06); Wayback id_ used because the live grant URL is gone with the rebrand, said so in this note. |
| MDP0486 | Open Philanthropy | recommendation | 1,250,000 | USD | 2022-11 | Not summed with the March 2022 $265,000 recommendation. Not a METR amount. |
| MDP0487 | FTX Foundation | paid_grant | 1,250,000 | USD | 2022 | ARC receipt, not a METR receipt. Not summed with the Open Philanthropy November 2022 $1,250,000 recommendation. |
| MDP0488 | Future of Life Institute | recommendation | 1,401,000 | USD | — | ARC Evals Team at ARC is not METR Inc. |
| MDP0489 | Open Philanthropy | commitment | 10,000,000 | USD | 2025-09 | A gift to RAND is not a gift to METR. September 2025 is before the derived window. Live Open Philanthropy grants index redirected (E06); Wayback id_ used, said so in this note. |

Note: MDP0485-MDP0489 add a column the excluded set did not previously have — ARC-era and RAND-bound amounts (not METR receipts) — their exclusion reason is entity, not period alone. MDP0032 and MDP0481 are the same spin-off seen from each side; neither is subtracted.

Remainder-statement rows (31): MDP0055, MDP0056, MDP0062, MDP0063 (MD14/MD25 discipline), MDP0585-MDP0593 (MD50 double-count / period / cross-type attacks, all CONFIRMED with no defect found in the arithmetic), MDP0594-MDP0611 (MD50 gate corrections; see §6 for two that are now stale).

---

## 4. What METR does not state

1. Composition of the ~$71M — who, how many, any per-donor amount (MDF0089; MDS1689 bounded negative on the funding-update and about pages; MDP0524-MDP0528 "unknown from public sources checked").
2. Cash paid to date on any of it ("raised commitments"; MDP0527).
3. Whether in-kind (free tokens, credits, complimentary access) is counted inside the ~$71M (MDP0529, MDI0119).
4. The calendar bounds of "the last 6 months" (MDT0033).
5. Whether the unpaid balance of the Audacious/Canary 3-year commitment is inside the ~$71M; whether the 2024 ~$17M was paid in full (MDF0169, MDP0035).
6. Any annual or lab-by-lab dollar value of free tokens/credits (MDS0719); only two event-level in-kind figures exist (~$400K; ~$600,000).
7. Who is inside AllOtherContributionsAmt $9,101,611 and Schedule B (MDS0588, MDS0011).
8. FY2025 revenue, expenses, net assets (no FY2025 990; no 2025 annual report).
9. METR's share of the EU AI Office contract; any UK AISI contract amount (MDP0051, MDP0050, MDP0607).
10. Packard instrument date and paid/approved status (MDF0020, MDP0598).
11. Audited FY2024 financial statements (exist; "available upon request"; not attached; not requested — MDS0112).
12. Which related organization paid the $457,601 Part VII "related organization" compensation (Schedule R names only ARC; XML-only observation).
13. Any bridge between the "$10 million" 2024 budget and the FY2024 990 / audited figures (MDP0057, MDS1025).
14. Any reason for the /about and /donate wording changes (dates are capture bounds; no motive asserted).

---

## 5. Contradictions and tensions (dated; no motive)

- **X1** FY2024 990 Part VI `ConflictOfInterestPolicyInd=1` + Schedule O 12C (MDP0231/MDP0269/MDP0271) vs FRR 2026-05-19 "did not have an applicable personnel conflict of interest (CoI) policy in place at the start of this project" (MDQ0044). Different document kinds (organisational vs personnel policy); pack: undetermined / not the same document (MDQ0069).
- **X2** FRR item 2.5 "Yes" (recused individuals with significant financial interest) vs same-page "did not run a formal recusal or disclosures process" (MDQ0052; MDQ0064 "undetermined"). Quote both if either is shown.
- **X3** "Approximately $17 million" (2024-10-09, MDF0166) vs "a bit under $16m … across 3 years" (2025-09-28, MDF0169): dated restatement; show both, never replace or add (MDF0006).
- **X4** /about "Our largest funding to date was through The Audacious Project" (2025-07-14 … 2026-07-19T23:27:59Z, MDT0306/MDT0411) vs "first institutional-scale funding" (from 2026-08-04T07:49:10Z, MDT0412; funding update 2026-08-14). Wording change bounded by captures; not stated by METR to be linked to the raise.
- **X5** 2024 annual report "$10 million" budget (calendar 2024) vs FY2024 990 expenses $8,234,524 (May-Dec) and audited-statement expenses $8,675,875: **not** a contradiction — different periods and bases; METR states no bridge.
- **X6** MDS0247 "none found in IRS index_2025.csv" vs MDS0115 index row: MDS0247 withdrawn (truncated download).
- **X7** MDP0602 "MD46 … is not present" vs the present `research/grok-out/MD46-funding-reconciliation.csv` (48 promoted rows): stale.
- **X8** philanthropy.org "$8.7 million across 3 grants from 3 funders" (MDS0057) vs 990 contributions 13,603,035: different bases (third-party funder-side aggregation vs recipient-side totals); not METR's statement.

---

## 6. Table defects found

- **D1** `lane` column empty on all 4,341 rows; lane is in `note`.
- **D2** `commitment_reconciliation.csv` computed rows: `identified_compatible_total` re-uses row_id MDP0030; `unresolved_remainder` has a blank row_id. Cite MDP0521/MDP0522 instead.
- **D3** MDP0036 (recon excluded) types the run-rate as `commitment`; seed MDF0002/MDF0003/MDF0004 likewise typed run-rate/runway/Audacious-restatement as `commitment` (MDF0002/0003 superseded by MDF0465/0466 with empty type; MDP0036 remains).
- **D4** MDF0064 note: "the $47,511 difference is not attributed" — 4,501,424 − 4,477,169 = 24,255.
- **D5** Seed MDF0007 amount 4,553,935 sums ARC cash 4,477,169 and non-cash 76,766 across money types; context only; MDF0064/MDF0065 split it (MDF0007 not marked superseded).
- **D6** MDP0602 stale (MD46 file exists). **D7** MDP0610 stale (computed rows now carry the funding-update url; STATE.md confirms).
- **D8** MDS0247 withdrawn none-found (truncated index copy).
- **D9** `review_verdict=DIFFERS` on key rows: MDP0032, MDF0034, MDF0147, MDP0150, MDP0497, MDP0057, MDP0058, MDP0059, MDP0060, MDP0061, MDF0018, MDP0028, MDQ0051, MDQ0063, MDP0056 — field-level lane/review differences logged as audit-1/2/3 in notes; amounts re-verified against primaries here.
- **D10** `figures/metr-deep-01-71m-known-and-unknown.html` shows 15 exclusions (MDF-keyed) against 31 in the recon (MDP-keyed) and labels MDF0166 ($17M, 2024-10-09) "Audacious METR-side restatement"; the restatement is MDF0169 ("a bit under $16m").
- **D11** Brief date for the Frontier Risk Report (2025-05-19) vs pack (2026-05-19).
- **D12** No standalone amount row for contributions 13,603,035; none for officer compensation, Schedule R loan lines (490,182 / 325,431), Schedule F spend (396,556), Schedule D donated services (441,350) or audited-FS revenue (14,080,505) — all XML-only, surfaced in notes of MDF0146/MDF0410, MDF0034, MDE0038, MDS0112, MDF0032.
- **D13** The same 990 XML is cited alternately by IRS-zip URL and gt990datalake URL; MDP0032's url field carries the zip while its note says the lane cited the lake URL. Both are byte-identical (SHA-256 84979ec8…); cite the SHA.
- Superseded rows skipped (30): MDF0002, MDF0003, MDF0031, MDF0035, MDF0068, MDF0076, MDF0077, MDF0155, MDF0163, MDS0001-MDS0008, MDS0151, MDS0214-MDS0221, MDS0466, MDT0055, MDT0056, MDE0012.

---

## 7. Cautions for anyone drawing a figure

1. Never place ~$71M (commitment), 13,639,155 (filed revenue), $10M (budget), ~$13M p.a. (run-rate), 4,000,000 / 184,000 / 20,000 (filed grants), SFF figures (recommendations), EUR 128,000 (regrant), ~$400K / ~$600K / 441,350 (in-kind) on one value axis (MDP0523, MDP0062, MDP0063).
2. FY2024 is an 8-month initial year; do not annualise.
3. GovernmentGrantsAmt is absent, not zero; say "not reported".
4. No restricted/unrestricted split is filed (fund-accounting election); do not draw one.
5. Schedule B "RESTRICTED" is the statutory public-copy redaction, not a METR choice about a particular donor.
6. Use one figure for the ARC spin-off (4,501,424 METR-side or 4,477,169 + 76,766 ARC-side), never both, never 4,553,935.
7. For XML-only lines, cite the primary file and SHA plus the note-bearing row.
8. Seed rows are context; every seed fact used here has a re-verified MDnn counterpart.
9. Named supporters other than Packard have no public amount or date; do not allocate any remainder share; keep individuals, employers and DAF accounts unmerged (MDP0048, MDP0049, MDP0054, MDP0599).
10. Wording-change dates are Wayback unique-digest capture bounds.
11. METR has not been asked about the ~$71M (MD99 draft unsent, `approved_for_send: false`, MDP0744); write "not published", never "declined".
12. Use 2026-05-19 for the Frontier Risk Report.

---

## 8. Suggested figures (all single-type or explicitly non-additive)

- **C-1 FY2024 Form 990 waterfall.** Contributions 13,603,035 = related-org 4,501,424 + all-other (unnamed) 9,101,611; + investment 36,120 = revenue 13,639,155; − expenses 8,234,524 (program 6,924,735 / M&G 1,144,255 / fundraising 165,534) = net assets 5,404,631; program-service revenue 0; government grants not reported; Schedule B RESTRICTED. Rows MDF0410/MDF0146, MDF0034, MDF0411, MDS0589, MDF0147, MDF0032, MDS0011. Label "2024-05-01 to 2024-12-31, initial short year".
- **C-2 What METR said, by date and money type.** Dated strip, one lane per type, no shared axis: 2024-10-09 ~$17M (commitment) · 2024 AR $10M budget / $15M 2025 target · 2025-09-28 ~$13M p.a., 12-16 months runway, "bit under $16m"/3 yrs, $10M end-2025 goal · 2026-08-14 ~$71M commitments / free tokens · 2026-08-26 ~$400K credits · 2026-08-31 ~$600K valuation · 2026-09-11 "fundraise as much as we need" · FY2024 990 filed 2025-11-16. Rows MDF0166, MDP0057, MDP0058, MDF0465, MDF0466, MDF0169, MDP0060, MDP0145, MDF0089, MDI0034, MDI0047, MDI0043, MDP0061, MDF0410.
- **C-3 Reconciliation ledger.** Three commitment tiles (~71,000,000 / 350,000 / ~70,650,000) and the 31 exclusions grouped by reason (period · type · entity · currency · no amount), reason text verbatim. Extends figure 01 (15 rows) to the full recon.
- **C-4 Rule-wording chronology on /about and /donate.** Capture-bounded snippets 2025-04-01 → 2026-09-15 (see S5/S6 for the sequence and rows). Label "capture bounds, not decision dates".
- **C-5 FRR Table A.1 self-grade panel.** 2.1 Yes · 2.3 No · 2.4 ×5 No (+ free-tokens note) · 2.4.6 "at least 6" · 2.5 Yes beside the preamble · 5.4 No · "not compliant with all of the requirements of the AEF-1 standard". Rows MDQ0051, MDQ0049, MDQ0084, MDQ0054, MDQ0052, MDQ0050, MDQ0044, MDQ0064, MDQ0055.
- **C-6 Residual-cell matrix.** who/vehicle · amount · date · cash paid · restriction · in-kind inside — six cells, all "not published" (MDP0524-MDP0529, MDS1689).
- **C-7 METR's own in-kind figures, unsummed.** 441,350 donated services (FY2024 audited statements, MDS0112 + XML) · 76,766 computers (ARC-side, MDF0065) · complimentary access, no figure (MDQ0051) · ~$400K (MDI0047) · ~$600,000 (MDI0043) · "significant free tokens", no figure (MDI0034, MDP0230).
