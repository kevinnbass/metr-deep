# F-timelines-disclosure — audit of everything dated in the metr_deep pack

Pack: `/mnt/f/projects/anthropic/metr_deep` (read-only). Companion machine-readable file: `F-timelines-disclosure.json` (same directory; 188 master-timeline entries, 8 pre-2021 context entries, 10 supporter-paragraph versions, 172 hashed about-page captures, COI policy dates/projects, CAL01–CAL10, five request drafts, 44 events in the Feb–Aug 2026 window, 31 cautions, 7 suggested figures).

Tables read: `research/timeline.csv` (MDT, 435 rows, 2 superseded), `research/provenance.csv` (MDP, 744), `research/funding_events.csv` (MDF, 1032, 9 superseded), `research/project_coi.csv` (MDQ, 181), `research/source_coverage.csv` (MDS, 1690, 18 superseded), `research/calendar.csv` (CAL01–CAL10), `research/records/REQUESTS.jsonl` (5). Rows whose note contains "superseded by" were skipped. `research/entities.csv` was consulted only as a locator for registry dates (flagged where used).

Reading rules applied throughout: a version difference bounds when a page changed, never when a gift occurred; a page-appearance, CMS, capture, fetch or check date is not an in-force date and not a transaction date; money types are never summed; no motive language; only public people in public roles.

---

## 0. Table-level facts a figure-maker must know first

1. **The `lane` column is empty in every row of every table.** Lane and cell are recoverable only from `note` ("lane=research/grok-out/<lane>.csv#<cell>" or "lane=research/rerun/<lane>-xhigh-added.csv#<cell>"). Seed baseline = `S0-seed-import` (timeline 8, provenance 2, funding_events 17, project_coi 1, source_coverage 8) plus `S2-lineage-import` (funding_events 51). Everything else is lane-added.
2. **Seed rows carry `checked_utc` 2026-09-14T00:00:00Z** (the 10-metr pack build date), not a metr_deep re-check. Each seed timeline locator was re-verified by a lane on 2026-09-16 (MDT0001→MDT0107/MDT0128; MDT0002→MDT0071/MDT0131; MDT0003→MDT0132; MDT0004–0007→MDT0240/0239/0234/0244; MDT0008→MDF0331/0333).
3. **Superseded rows (skipped):** MDT0055, MDT0056; MDF0002, MDF0003, MDF0031, MDF0035, MDF0068, MDF0076, MDF0077, MDF0155, MDF0163; MDS0001–MDS0008, MDS0151, MDS0214–MDS0221, MDS0466.
4. **MD50 audit rows MDF0464–MDF0926** ("audit of promoted MDFxxxx") repeat every promoted funding row with identical date and amount. Count events by primary row, not by row count. MD47/MD48/MD53 synthesis rows likewise repeat held dates.
5. **Date-column defects** (full list in JSON cautions X02–X06, X29):
   - Fourteen NY Post 2026-09-15 rows have an **empty date column** (MDP0563–MDP0568; MDS1239, MDS1240, MDS1255–MDS1258, MDS1266, MDS1593). The date is only in `subject`/`url`.
   - MD53 figure-bibliography rows MDP0666, MDP0667, MDP0682, MDP0683 (Tallinn $10,000 on 2024-07-23/24) have an empty date column.
   - MDQ0103 has prose in the date column ("undisclosed on this page beyond report publication on metr.org/evaluations/gpt-5-report/").
   - Round labels in the date column with precision `interval`: `SFF-2022-H2`, `SFF-2023-H1`, `SFF-2024`, `SFF-2025` (MDF0008/0009/0045–0050/0079–0081/0083/0088/0196–0198/0210/0215–0217/0415 and their MD50 copies; MDP0010–0012/0038/0039/0504/0505). Also `FY2025 (2024-07-01 to 2025-06-30)` (MDF0012; MDP0043/0482/0509), `2024 (TY2024 990-PF Part XV)` (MDP0001/0002), `undated` (MDF0015/0016/0018; MDP0048–0050/0514–0516).
   - `date_precision=year` on full-day fiscal-year-end dates in 100+ rows (MDP0057/0058; MDF0036/0499; MDF0156–0159/0161; MDF0414/0531; MDF0419–0453 and copies MDF0877–0916; MDS0380–0400; MDS1143–1146); `month` on full-day dates in MDP0222 (2024-02-01), MDP0290 (2026-03-27), MDP0495 (2026-06-30).
   - Interval encoding is inconsistent: `2024-10-09/2026-09-16` (MDT0035–0051), `2026-07-14 to 2026-07-19` (MDT0003), single day + precision `interval` for fiscal years (MDT0053/0054/0230–0233), window in `period` with a single day in `date` (MD24 B-rows MDT0060–0117).
6. **The only DIFFERS verdict in timeline.csv** is MDT0015 (issuer wording "individuals directly" typed as vehicle class); its xhigh copy MDT0227 is CONFIRMED.

---

## 1. Master timeline 2021–2026 (funding-relevant, every dated row family)

Category key: money | statement | filing | project | policy | page_version | post | archive. "PAGE" = page-appearance/archive/check date, never a transaction date. "seed" / "lane" / "seed+lane" per row family. Full entries with every row id, money type, amount, from/to and URL are in the JSON `master_timeline`; this section is the readable version.

### Pre-2021 context (vehicle and sponsor filings only)
- 2018-04-13 Facebook DEF 14A does not name the 2018 remainder-interest trust (MDS0902). 2020-04-10 Facebook DEF 14A names *Dustin Moskovitz Remainder Interest Trust dated 2018-03-10* (MDT0161); 2020-06-23 PRE 14C, 2020-07-08 DEF 14C same (MDP0452/0453). Meta Class B shares, not Anthropic.
- GVF Schedule B receipts: 2020-06-26 publicly traded securities $1,017,208,584 (MDF0318; contributor Moskovitz MDF0317); 2020-09-03 $269,719,012 (MDF0320/0319). money_type equity_value.
- TY/FY2020 sponsor and intermediary schedules checked vs METR/ARC, all none-found and pre-METR (MDS1037, MDS1092, MDS1097, MDS1099, MDS1103, MDS1143–1146, MDS1011; payers into FP Inc/Every Org MDF0435–0440, 0452, 0453).

### 2021
- 2021-04-09 Facebook 2021 DEF 14A drops the trust (MDS0903). filing, lane.
- **2021-05-28 Anthropic Series A** issuer page names Dustin Moskovitz as a participant (with McClave, CERR, Eric Schmidt) (MDS1624; MDP0707; MDP0571). statement, lane. **Investment date, not the donation event** (separation record MDP0707).
- 2021-06-30 FY2021 June-year filings vs METR and ARC: Pew MDS0136; Fidelity MDS0170/0194; Schwab MDS0176/0199; Vanguard MDS0182/0205/0397; NPT MDS0186/0207 (Schedule B Part I restricted MDP0333/MDS0844); GVF FY2021 MDS1012; EV USA MDS0389; sponsor equity lines MDP0387–0389, 0402–0404, 0417–0419, 0432–0434. filing, lane. Period-end date.
- 2021-07-15 Blue Owl S-1/A (MDS0862); 2021-12-07 Blue Owl 424B3 selling-stockholder table (MDS0861). filing.
- 2021-12-31 TY2021: SVCF MDS0191/0212/0400 (equity MDP0375–0377); Every Org MDS0384; FP Inc MDS0392; Schwab two-day return MDS0177/0200; payers into FP Inc incl. Open Philanthropy $1,000,000 and GVF $1,000,000 (MDF0429–0434); into Every Org (MDF0448–0451). filing. Payer-into-intermediary transfers are not METR grants.

### 2022 ("the 2022 awards")
- 2022-03 Open Philanthropy recommended **$265,000** to ARC, general support (MDF0066; MDP0485). recommendation, lane.
- 2022-04-08 Meta 2022 DEF 14A no trust (MDS0904).
- 2022 (year) FTX Foundation **$1.25M** received by ARC "earlier in 2022" (MDF0069; MDP0487). paid_grant, lane. 2022-11-15 ARC page: set aside, not to be spent (MDP0019, page published date). 2024 update: returned to the FTX estate, net not stated (MDT0032).
- 2022-06-03 GVF FY2022 Schedule B receipt $168,195,798 publicly traded (MDF0322; contributor MDF0321). 2022-06-30 GVF FY2022 Part XV: **$265,000 to ARC** (MDF0335, same amount as the OP March recommendation — two money types, one flow) and $1,000,000 to Founders Pledge Inc (MDF0336).
- 2022-06-30 FY2022 June-year checks (MDS0137/0171/0172/0178/0183/0187; ARC MDS0195/0196/0201/0206/0208/1098; NPT MDP0332/MDS0843; GVF MDS1013; EV USA MDS0388; equity MDP0390–0392, 0405–0407, 0420–0422, 0435–0437).
- 2022 Q4 LTFF $72,000 to ARC (MDF0085). recommendation.
- 2022-11 Open Philanthropy recommended **$1,250,000 over two years** to ARC (MDF0067; MDP0486); GVF FY2023 Part XV shows $1,250,000 to ARC (MDF0337).
- SFF-2022-H2 recommendation **$2,179,000** to ARC (MDF0050; MDF0415) — round label, no day. 2022-12-20 Tallinn ledger FP-US **$2,179,000** to ARC (MDF0057). TY2022 Founders Pledge Inc filed **$2,179,000** to ARC (MDF0061). Three attestations of one flow.
- 2022-12-31 TY2022 checks (MDS0192/0213/0399, MDS0383, MDS0391, TED MDS0436; SVCF equity MDP0378–0380; payers into FP Inc MDF0424–0428).

### 2023
- 2023-03 GPT-4 system card names ARC (MDS0813/0814). project (ARC era).
- 2023-03-06 ARC donate page `time.page__date`; body says "Evaluations team has spun off as METR" — the stamp precedes the 2023-09-19 announcement; sentence undated (MDT0031). PAGE.
- SFF-2023-H1 recommendation **$3,247,000** to ARC (Evals Team) (MDF0049; MDF0088; MDF0210).
- 2023-06-15 Tallinn ledger FP-US **$1,846,000** to ARC Evals Team (MDF0056); FP Inc TY2023 filed $1,846,000 (MDF0060). Same day: GVF FY2023 Schedule B receipt $1,907,189,117 (MDF0325; contributors MDF0323/0324).
- 2023-06-30 GVF FY2023 Part XV to ARC $1,250,000 (MDF0337) and to RAND $5.5M/$10M/$666,667/$10.5M (MDF0094–0097; MDF0359–0362). FY2023 checks incl. Vanguard $201,000 to ARC (MDF0042) and NPT FY2023 Schedule M/D (MDP0360–0369).
- 2023-07-21 White House voluntary commitments (MDP0296). policy.
- 2023-08 Longview public-fund report: **$220,000** ARC Evals/METR recommendation (MDF0070; seed MDF0013; MDP0022/0044); Effektiv Spenden **EUR 128,000** regrant (MDF0072; seed MDF0014; MDP0024/0045). seed+lane.
- 2023-09 UK Taskforce progress report (MDP0288). 2023-09-19 ARC Evals spin-out announcement (MDT0028) — same calendar day as Anthropic's LTBT page (MDS0741), unrelated. 2023-09-25 Longview CPT object names METR (MDP0478; MDS0297), PAGE. 2023-09-30 RAND FY2023 990 (MDS0474). 2023-11-14 Asana SC 13D/A (MDS0866). 2023-12 Longview ECF report no METR (MDP0025). 2023-12-04 renamed METR (MDT0029). 2023-12-28 Wayback /team/: advisers Karnofsky, Christiano (MDT0155) PAGE.
- 2023-12-31 TY2023: SVCF **$1,401,000 to ARC** (MDF0040); FP Inc $1,846,000 to ARC (MDF0060); TED none (MDS0435); Valhalla/High Tide vs RAND none (MDS0477/0478); payers into FP Inc (MDF0156–0159, 0419–0423) and Every Org (MDF0161, 0443–0447); UES gGmbH 2023 (MDS1085).

### 2024
- 2024 (year) annual report: Bengio advises (MDT0153); labs credit METR for first safety policies (MDQ0110/0156); budget statements (MDP0057/0058). No personnel CoI section (MDQ0047).
- 2024-02-01 GAGAS 3.18 (MDP0222, precision mismatch). 2024-02-05 GVF FY2024 Schedule B: **$446,082,975 publicly traded securities from DUSTIN A MOSKOVITZ REMAINDER INTEREST TRUST** (MDF0296/0329/0326).
- 2024-03 IRS EO BMF ruling 202403 for METR EIN 99-1219864 (entities.csv MDE0014, not a listed table); FY2024 short year begins 2024-05-01 (MDF0410); "formed May 2024" (MDS0583 note, derived). See caution X16.
- 2024-04 Founders Pledge grantee card, amount undisclosed (MDF0086; MDS0300) PAGE.
- **2024-04-23 first Wayback about capture; no supporter paragraph** (MDT0253; MDT0425; CDX MDS0540–0542) PAGE.
- 2024-04-26 Emma Abele Executive Director (MDT0154).
- **2024-04-30 ARC Schedule N DistributionDt: program to METR**; Schedule I cash **$4,477,169** + non-cash $76,766 (FMV $4,553,935) (MDT0030/0228; MDF0064/0065; seed MDF0007; MDP0015/0016/0481). transfer, seed+lane. Part III narrative "in May" (MDT0229). METR FY2024 990 related-org contribution **$4,501,424** (MDF0034; MDP0032). Three filed strings, not collapsed.
- 2024-05-19 Wayback /team/: Karnofsky only (MDT0156). 2024-05-21 Seoul commitments (MDP0295). 2024-06 Claude 3.5 addendum (MDP0297). 2024-06-13 EU AI Act Art. 31(4) (MDP0225).
- 2024-06-30 GVF FY2024: contributor 2 Moskovitz $354,990,800 (receipt 2024-06-30 $359,047,750; MDF0327/0330); Beneficial AI Foundation $164,128 (MDF0328); Part XV to RAND (MDF0098–0102; 0306–0310; 0388–0392). FY2024 checks incl. Fidelity $100,000 and Vanguard $1,000,000 to ARC (MDF0039/0043); NPT FY2024 Schedule M/D (MDP0350–0359).
- 2024-07-19 Tallinn SFF-spec $50,000 to ARC (MDF0054). **2024-07-23 and 2024-07-24 Tallinn SFF-spec $10,000 each to METR** (MDF0051; MDF0052; MDF0221/0222/0412). paid_grant, lane.
- SFF-2024 round: **$204,000** to METR Inc (MDF0047; seed MDF0008; MDF0075/0079/0198/0215; annotation ($20,000)† MDP0011) and $197,000 to ARC (MDF0048/0083; MDP0012). recommendation.
- 2024-08-07 GPT-4o evaluation (MDQ0112/0132); 2024-08-08 GPT-4o card (MDP0283/0293); 2024-09-12 o1 evaluation (MDQ0126; MDP0284); 2024-09-30 RAND FY2024 (MDS0475). project.
- **2024-10-09 Audacious announcement**: ~$38M for Canary (METR + RAND), ~$17M to support work at METR; METR X post 13:22:41Z; RAND press; TED blog; ~$21M arithmetic remainder (seed MDF0005/0006; S2 MDF0125; MDF0165–0168/0170/0171/0173/0194; MDP0033/0034/0144/0151/0184/0499/0500; MDT0121). commitment, seed+lane. Term not stated; no payment date. Same day: Audacious about page "Last Published Oct 09 2024 13:12:38 GMT" (MDT0052), baseline for 14 partner adds and 2 renames measured to 2026-09-16 (MDT0035–0051; MDP0130), interval only.
- 2024-10-30 Claude 3.5 Sonnet evaluation (MDQ0111/0144). 2024-11-03 first Wayback capture of the Audacious post (MDT0119; MDS0550; MDP0148) PAGE. 2024-11-06 Audacious Wayback title "Project Canary" (MDP0493) PAGE.
- 2024-11-21 Tallinn FP-US $147,000 to ARC (MDF0055); FP TY2024 filed $147,000 (MDF0059/0413). 2024-12-03 Wayback /team/: Gleave adviser and board member, Karnofsky, Bengio (MDT0157) PAGE.
- **2024-12-06 Tallinn FP-US $184,000 to METR** (MDF0053; MDF0218; MDP0484); FP Inc TY2024 filed $184,000 to METR (MDF0058; seed MDF0010; MDF0152/0203/0219). paid_grant / filed_grant, one flow.
- 2024-12 Longview Frontier AI Fund private aggregate 2024-12/2025-09, METR undisclosed (MDS0265).
- **2024-12-31 METR FY2024 Form 990** (short year 2024-05-01 to 2024-12-31; ReturnTs 2025-11-16): total revenue $13,639,155 (MDF0146/0410; MDP0031), contributions $13,603,035, all other contributions $9,101,611 (MDF0411), ARC related-org $4,501,424 (MDF0034), expenses $8,234,524 (MDF0147), net assets $5,404,631 (MDF0032), program-service/government 0 (MDF0033), written CoI policy checkbox (MDP0231/0269; MDQ0069; MDS0789), 1 of 3 independent directors (MDP0272), audit committee formed 2025 (MDP0273), no Canary line (MDS0432). filing, lane. Recipient revenue is not a commitment.
- 2024-12-31 TY2024 partner/sponsor filings: SVCF **$20,000 to METR** (MDF0037/0062; seed MDF0011) and $50,450 to ARC (MDF0041/0063); Valhalla **$10,000,000** and High Tide **$333,334 to RAND for Project Canary** (MDF0174/0175; seed MDP0001/0002; MDS0437/0438); FP Inc $1,000,000 to RAND (MDF0122/0177); Gates/Hewlett/Waking Up to RAND non-Canary (MDF0178–0185); MacArthur → CANARY MEDIA INC name collision (MDF0314); TED Foundation, Skoll, Gates, Longview USA, Every Org none (MDS0434/0807/0806/0380/0381); ARC with-donor-restriction 1,146,000→0 (MDP0017); SVCF CY2024 audited (MDP0447); 28 Audacious-partner filers' latest returns (MDT0185–0215).

### 2025
- 2025-01-07 /team/ redirects to /about (MDT0158; MDT0256) PAGE. 2025-02-10 Scale/US AISI (MDS0812).
- **2025-02-11 → 2025-02-15 about page first "partnering with the AI Security Institute"** (MDT0066/0067) page_version.
- 2025-02-15 SFF-2025 further-opportunities page, METR $220,000 column (MDF0093; MDP0040/0506) PAGE. 2025-02-27 GPT-4.5 evaluation (MDQ0130).
- SFF-2025 round: **$120,000** recommendation + **$428,000** conditional matching pledge to METR Inc (MDF0045/0046; seed MDF0009; MDF0074/0080/0081/0196/0197/0216/0217; annotation MDP0010); Tallinn → RAND TSPC $1,000,000 + $22,000 (MDF0123/0124; MDS0495). Note: MDF0081/MDF0217 type the matching pledge as `commitment`, MDF0046/MDF0197 as `recommendation`.
- 2025-03-05 AISI Challenge Fund notice (MDP0196); awards[] still empty at lastUpdated 2025-10-27 (MDT0175).
- **2025-04-01 → 2025-04-18 donate compensation footnote "To date, April 2025"** (seed MDT0001; MDT0106/0107; MDT0128/0134) page_version, seed+lane.
- 2025-04-16 o3/o4-mini evaluation (MDQ0128). 2025-04-30 Rippleworks FYE (MDT0202).
- **2025-06-30 GVF FY2025 Schedule B: $1,395,695,354 publicly traded securities received 2025-06-30 from the Remainder Interest Trust; no private-stock contribution** (seed MDT0008; MDF0331/0333; MDF0332 BAIF $150,027; Part XV to RAND MDF0103–0105; MDS1016; return signed 2026-05-15 MDT0218). filing, seed+lane.
- **2025-06-30 Vanguard Charitable FY2025 Schedule I: $4,000,000 to METR** (MDF0038; seed MDF0012; MDF0154/0206/0211; MDP0043/0482/0509; MDS0441) and $1,500,000 to ARC (MDF0044). filed_grant; principal undisclosed; grant day not on the schedule.
- 2025-06-30 other FY2025 June-year filings: NPT $61,646,790, Fidelity $18,202,491, Schwab $4,858,600 to RAND (MDF0118/0186/0187/0417); Pew FY2025 none to METR/RAND (MDS0140/0481), Pew → Pew Research Center $38,100,000 (MDF0036); NPT Schedule B Part I restricted (MDP0329), Part II noncash (MDS0840), Schedule M/D (MDP0335–0349); audited statements (MDP0448–0451); EV USA (MDS0385); sponsor equity (MDP0399–0401, 0414–0416, 0429–0431, 0444–0446).
- 2025-07-07 Amazon Nova Premier (MDQ0150; MDP0287). 2025-07-10 EU GPAI CoP (MDP0226).
- **2025-07-11 → 2025-07-14 about page "How is METR funded?" section, Audacious first named, AI-company funding rule first appears, supporter paragraph APPEARED** (MDT0060–0065; MDT0426; MDT0306; MDT0130/0135; MDT0121) page_version.
- 2025-08 GPT-5 system card (MDP0285). **2025-08-07 GPT-5 evaluation** (NDA; OpenAI comms/legal approval) (MDQ0009/0021/0103/0122; MDQ0180). project.
- 2025-09 Open Philanthropy $10M over three years to RAND for Canary (MDF0176; MDP0489; MDS0808). commitment, to RAND.
- 2025-09-10 → 2025-10-02 donate footnote label April → September 2025 (MDT0112/0113) page_version.
- **2025-09-28 Beth Barnes shortform**: Audacious "a bit under $16m across 3 years", one-off (seed MDF0004; MDF0169/0172; MDP0035/0145/0152/0501); run-rate ~$13m (MDF0465 audit of superseded MDF0002; MDP0036/0059); runway 12–16 months (MDT0034; MDF0466; MDP0037/0060); end-2025 goal (MDP0060). statement.
- 2025-09-29 supporter paragraph reworded, no names (MDT0427) page_version. 2025-09-30 RAND FY2025 990 (MDS0476).
- 2025-10-20 Stratechery: Moskovitz self-described board observer (MDT0238). 2025-10-23 gpt-oss-120b review (MDQ0025/0026/0029/0106; MDS0631). 2025-10-28 Anthropic sabotage-report review (MDS0640).
- **2025-11-10 Forbes Australia, Cari Tuna quoted: stake (est. $500M) moved to a nonprofit vehicle "in early 2025"** (seed MDT0004; MDT0240). First donation statement in the pack; vehicle unnamed.
- 2025-11-16 METR FY2024 990 ReturnTs (MDF0410 note). 2025-11-19 GPT-5.1-Codex-Max (MDQ0010/0104/0120). 2025-11-26 Apollo CoI norms (MDP0228). 2025-11-28 TED notice 864574-2025 published (MDP0281) PAGE; Dylan Field Form 4 gift to unnamed DAF (MDP0007/0476). 2025-11-30 Tepper FYE (MDT0211).
- 2025-12 Coefficient Giving: METR not a grantee (MDP0053/0519).
- **2025-12-03 → 2025-12-07 about paragraph adds Schmidt Sciences, Astralis, Expa.org, AISI, Longview, Effektiv Spenden, SFF, Geoff Ralston; "individuals directly" appears** (MDT0074–0089; MDT0428; MDT0012/0021/0022/0223/0224) page_version.
- 2025-12-04 AEF-1 Version 1 (MDP0206–0221; MDQ0012/0013/0087/0088). policy.
- **2025-12-07 → 2025-12-16 about paragraph adds Sijbrandij, La Centra-Sumerlin, David Farhi, Dylan Field** (MDT0090–0097; MDT0429; MDT0011/0013/0015/0020/0226/0227) page_version.
- **2025-12-15 EU AI Office contract 4500137790 (TED LOT-0003), EUR 1,167,484 lot total to EquiStamp (leader) + METR + Epoch; METR share undisclosed** (seed MDF0017; MDF0150/0151/0236; MDP0051/0132/0282/0517). contract, seed+lane. Notice 2025-11-28 (MDP0281); criteria row 2025-12-23 (MDP0291).
- **2025-12-18 Alexander Berger on X: "He's since donated his stake (and not to us)"** (seed MDT0006; MDT0239). 2025-12-19 RAND Europe CF award (MDS0535). 2025-12-31 calendar-year 2025 closes; Tsai/Oak TY2025 already posted (MDT0197/0200); Transluce FY2025 (MDP0233).

### 2026
- **2026-01-27 → 2026-02-02 about page first European AI Office sentence; "Funding" heading** (MDT0068/0069).
- **2026-02-05 → 2026-02-11 donate compensation footnote disappears** (MDT0110/0111; MDT0129).
- 2026-02-14 Forbes India restatement (MDT0243). **Derived window start ≈2026-02-14** (commitment_reconciliation.csv; MDP0484 note) — a lane derivation, not a METR date.
- **2026-02-16 FRR assessment window starts** (to 2026-03-16); no applicable personnel CoI policy at project start (MDT0141/0143; MDQ0089; MDP0716). 2026-02-17 confidentiality post (MDQ0011); about capture: Painter "Policy Director" (MDT0145).
- **2026-03-06 → 2026-03-11 about paragraph adds The Pew Charitable Trusts and European AI Office** (MDT0098/0099; MDT0430).
- 2026-03-12 Opus 4.6 sabotage-report review (mutual NDA; general veto; one rephrase) (MDQ0023/0024/0027/0028/0041/0107/0136/0179). 2026-03-16 FRR window ends; Painter still Policy Director (MDT0144). 2026-03-25 agent-monitoring red-team (MDQ0042/0108/0140). 2026-03-27 CAISI slide (MDP0290).
- **2026-03-30 Moskovitz Bluesky 05:24:03Z / 05:28:20Z: shares "entirely in our foundation"** (seed MDT0007; MDT0234/0235/0244). 2026-04 Mythos Preview card (MDP0286). 2026-04-11 Bluesky: "$20B more in the foundation ... invested in Anthropic" (MDT0236). 2026-04-17 Washington Examiner (MDT0242). 2026-04-18 Newman X (MDS1067). **2026-04-20 Forbes: "Last year he donated ... less than 0.8%"** (seed MDT0005; MDT0241). 2026-04-30 Rippleworks FYE closes (MDT0202).
- 2026-05-08 R&D-section review (MDQ0043/0109/0138). **2026-05-15 METR FY2025 990 original due, not posted** (MDT0017; MDS0345; MDT0159); GVF FY2025 990-PF signed (MDT0218).
- **2026-05-19 Frontier Risk Report published** (JSON-LD 2026-05-19T11:00:00-07:00): AEF-1 2.3 = No; "at least 6" close personal relationships; 2.5 = Yes beside "did not run a formal recusal or disclosures process"; participants Anthropic, Google, Meta, OpenAI; Painter "President" on the day's about capture (seed MDQ0001; MDQ0002–0005, 0015–0017, 0022, 0030–0037, 0044–0045, 0048–0068, 0080–0086, 0090, 0096–0100, 0114–0115, 0177; MDP0716/0239/0240; MDT0140/0142/0144; MDS0620/0728). project, seed+lane.
- **2026-05-25 → 2026-06-01 about paragraph adds Steve Newman** (MDT0100/0101; MDT0431; MDT0014); 2026-06-01 capture still lacks "individuals from Jane Street" (MDT0225).
- 2026-06-01 Anthropic confidential draft S-1 notice (MDT0162; MDP0372). 2026-06-26 GPT-5.6 Sol evaluation (MDQ0008/0020/0105/0118).
- **2026-06-29 → 2026-07-06 about paragraph adds "the Packard Foundation"** (MDT0102/0103; MDT0432).
- 2026-06-30 FY2026 closes for GVF and June-year sponsors (MDT0193/0221/0222; MDT0023–0026/0160; CAL03/07/09); METR "Progress Report March–June 2026" (MDP0495).
- **2026-07-03 → 2026-08-04 donate page employee-direction parenthesis** (MDT0108/0109; MDT0132; seed MDT0003).
- **2026-07-06 Packard grantee page datePublished 2026-07-06T06:09:41Z** (dateModified 2026-09-14T06:08:32Z): grant 2026-79050, $350,000, award year 2026, 12 months, general support — the only identified denominator-compatible component; **catalog date, not an instrument date** (MDT0010/0122; MDP0030/0480/0496/0585/0589/0598; MDF0091/0092/0416/1031; year-only rows MDF0020/0021/0078/0090/0191–0193). Same day: Illinois P.A. 104-0538 (MDP0224; MDQ0071). 2026-07-08 RSP v3.4 §3.6.1 effective (MDP0243).
- **2026-07-14 → 2026-07-19 about page employee-direction parenthesis first appears** (seed MDT0002/0003; MDT0070/0071; MDT0123/0131; MDT0409/0410). 2026-07-15 WIRED Farhi, not a METR gift (MDS0077).
- **2026-07-19 → 2026-08-04 about paragraph restructured; "individuals from Jane Street" APPEARS; "individuals directly" REMOVED → "many others, such as"; "Note:" prefix; "free compute credits" → "free tokens"** (MDT0104/0105; MDT0114–0117; MDT0133; MDT0433; MDT0411/0412).
- 2026-07-30 Anthropic "in dialogue with METR" (MDP0244). 2026-08-01 FRR archive still no policy (MDP0710) PAGE.
- **2026-08-04 → 2026-08-18 "La Centra-Sumerlin" → "LaCentra-Sumerlin"** (MDT0072/0073; MDT0434; MDT0413).
- **2026-08-14 METR funding update: "In the last 6 months, METR raised commitments of around $71 million"** (seed MDF0001; MDF0089/0145/0463/0464/0552/0608/0926/1032; MDP0029/0055/0062/0171/0521; MDT0033/0127; MDT0435). commitment, seed+lane; statement date. Thank-you list and METR_Evals X post (MDT0009; MDT0019 "Frontier Fund" alt; MDT0252; MDP0027/0147; MDF0019/0024/0026/0028/0030).
- 2026-08-17 Dylan Field second Form 4 gift to unnamed DAF (MDP0008/0477).
- **2026-08-26 OpenAI/Hugging Face investigation post**; ~$400K API-credit estimate (in-kind); no CoI policy in force (MDQ0006/0007/0018/0019/0038/0102/0116/0178; MDP0052/0518; MDS0632). Same day Moskovitz Bluesky "GV is itself a beneficiary" (MDT0237).
- 2026-08-27 Transluce policy (MDP0227/0232); first Wayback capture of the funding update (MDT0118) PAGE; Field X post (MDS1066).
- **2026-08-28 METR Conflict of interest policy v1.0, printed "Last updated August 28, 2026"** (MDP0708/0711–0715; MDT0137–0139/0250; MDQ0014/0091/0092/0095/0113; MDP0265–0268; MDS0790). policy, lane.
- 2026-08-31 Anthropic "planning to work with METR" (MDT0151); METR "Update on Security" post (MDT0173; MDS0744).
- 2026-09 (month) Amodei essay (MDP0247). 2026-09-01 Mythos 5.1 card (MDQ0146). 2026-09-03 NIST consortium list (MDP0289).
- **2026-09-09 Anthropic–METR signed agreement; eight-week initial term** (MDT0147–0150/0152; MDP0241/0242/0245/0246/0298; MDQ0181/0142; MDS0610); CA AB 1405 chaptered (MDP0223; MDQ0070; MDS0662); Christiano joins OpenAI SSC (MDQ0039 quote).
- 2026-09-11 Business Insider Barnes (MDP0061). 2026-09-12 Greenblatt X (MDQ0094). 2026-09-13 HF footnotes added (MDQ0039/0040/0046).
- **2026-09-14 posted figure commit f64df65** (MDP0551/0553/0555/0557/0559/0561; current 17539ba MDP0552/0554/0556/0558/0560/0562; STATE.md "The image readers saw on 2026-09-14"); Packard page dateModified; **last about capture without a COI section 20260914132053** (MDT0248; MDT0423); last archived donate digest 20260914132047 (MDS0552). post/archive.
- **2026-09-15 NY Post**: six METR-attributed sentences, does not name the 2026-09-14 figure (MDP0563–0568; MDS1239/1240/1255–1258/1266/1593 — date column empty); **first about capture with the COI-policy link 20260915160044** (MDT0249; MDT0424); RSS lastBuildDate 18:37 (MDT0173).
- **2026-09-16** sitemap lastmod for coi-policy.pdf 10:34:29-07:00 (MDT0246); HTTP Date 17:35:21Z, Last-Modified absent (MDT0245); live about links "current" policy (MDP0709); live rules and supporter list (MDT0016/0124–0126/0136/0146/0251/0252); CDX 172 unique about digests (MDT0247); five request drafts registered 11:59:05Z; calendar last_checked 10:00:00Z; exhaustion gate 18:45:48Z (MDT0435). All check dates.

### Future (calendar closers; see §4)
2026-09-30 Longview Inc Ltd / FP Ltd UK accounts (MDT0059) · 2026-10-15 Tepper extended (MDT0211) · 2026-10-16 CAL05 monthly · ~2026-11-04 CAL01 (MDT0166/0178) · 2026-11-15 GVF FY2026 statutory (Sunday) and CA RRF-1 (MDT0165/0180/0217/0221/0222/0219) · 2026-11-16 observed deadlines for METR FY2025 990, CY2025 filers, June-year DAF FY2026, GVF (MDT0163/0164/0179/0181; MDT0017/0159; MDT0023–0027; MDT0160/0193; MDT0185–0215) · 2027-01-15 Someland (MDT0207) · 2027-03-15 Rippleworks (MDT0202) · 2027-03-31 EV UK (MDT0059) · 2027-04-15 Lyda Hill (MDT0198) · 2027-05-15/17 GVF extended, METR FY2026 990 original, Tsai/Oak TY2026 original (MDT0218; MDT0018; MDT0197/0200) · 2027-10-15 / 2027-11-15 extensions · 2028-01-01 Illinois audit duty · 2029-01-01 California registration.

---

## 2. About-page supporter-paragraph version history (lane MD70; C02.E1 / C09.E1 / C09.E3)

Index: Wayback TimeMap CDX collapse=digest for metr.org/about, 172 unique digests from 20240423101403 to 20260915160044 (MDT0247; MDS1653); 171 of 172 id_ bodies hashed by MD72, all 172 by MD70 (MDT0253–MDT0424, one row per capture; 119 with a supporter paragraph, 53 without; 132 distinct SHA-256 because Wayback digest ≠ body hash). Live capture 2026-09-16T17:38:37Z sha 8f2d3c6d… (MDT0251). Every timestamp below is a capture time (PAGE), never a gift date.

| v | after capture (UTC) | before capture (MD70, paragraph-distinct) | MD24 page-digest immediately before | names added | names removed | reworded | rows | after sha256 |
|---|---|---|---|---|---|---|---|---|
| 0 | 2024-04-23T10:14:03Z | — | — | (no paragraph) | — | — | MDT0425; MDT0253 | d27dee22… |
| 1 | **2025-07-14T23:17:49Z** | 2024-04-23T10:14:03Z | 2025-07-11T11:06:23Z (MDT0060/0062/0064, sha 004d75e8…) | The Audacious Project | — | paragraph APPEARED; "METR has not accepted funding from AI companies, though we make use of free compute credits" | MDT0426; MDT0306; MDT0061/0063/0065; MDT0121/0130 | a954c479… |
| 2 | **2025-09-29T23:31:29Z** | 2025-07-14T23:17:49Z | — | — | — | "significant free compute credits"; "Independent funding has been crucial" | MDT0427 | c500d892… |
| 3 | **2025-12-07T08:57:07Z** | 2025-09-29T23:31:29Z | 2025-12-03T02:45:26Z (MDT0074/76/78/80/82/84/86/88, sha 3e1016f3…) | AI Security Institute; Astralis Foundation; Effektiv Spenden; Expa.org; Geoff Ralston; Longview Philanthropy; Schmidt Sciences; Survival and Flourishing Fund | — | "a wide range of **individuals directly**, such as Geoff Ralston" ADDED | MDT0428; MDT0075/77/79/81/83/85/87/89; MDT0012/0021/0022/0223/0224 | 7c677d8f… |
| 4 | **2025-12-16T01:31:59Z** | 2025-12-07T08:57:07Z | 2025-12-07T08:57:07Z (MDT0090/92/94/96) | David Farhi; Dylan Field; La Centra-Sumerlin Foundation; Sijbrandij Foundation | — | — | MDT0429; MDT0091/93/95/97; MDT0011/0013/0015/0020/0226/0227 | afcf4bf3… |
| 5 | **2026-03-11T01:59:26Z** | 2025-12-16T01:31:59Z | 2026-03-06T07:46:01Z (MDT0098, sha a4582e12…) | European AI Office; The Pew Charitable Trusts | — | — | MDT0430; MDT0099; (EU sentence 2026-01-27→02-02 MDT0068/0069) | d35c691c… |
| 6 | **2026-06-01T23:29:33Z** | 2026-03-11T01:59:26Z | 2026-05-25T23:23:20Z (MDT0100, sha 204a7805…) | Steve Newman | — | — | MDT0431; MDT0400; MDT0101; MDT0014; MDT0225 | 27b65104… |
| 7 | **2026-07-06T23:26:41Z** | 2026-06-01T23:29:33Z | 2026-06-29T23:28:51Z (MDT0102, sha 42e57a15…) | Packard Foundation | — | — | MDT0432; MDT0408; MDT0103; MDT0122 | bb1ee497… |
| 8 | **2026-08-04T07:49:10Z** | 2026-07-06T23:26:41Z | 2026-07-19T23:27:59Z (MDT0104/0114/0116; MDT0411, sha a0cdd91a…) | **individuals from Jane Street** | — | "**individuals directly**" REMOVED; "a wide range of individuals directly, such as" → "many others, such as"; paragraph restructured ("We are grateful to METR's many supporters: from … The Audacious Project …; to individuals from Jane Street; foundations such as …"); employee rule gains "Note:"; "free compute credits" → "free tokens" | MDT0433; MDT0412; MDT0105/0115/0117; MDT0133; MDT0009 | dee43e09… |
| 9 | **2026-08-18T22:35:48Z** | 2026-08-04T07:49:10Z | 2026-08-04T07:49:10Z (MDT0072) | LaCentra-Sumerlin Foundation | La Centra-Sumerlin Foundation | spelling only (EIN 77-0416683 unchanged) | MDT0434; MDT0413; MDT0073; MDT0019 | 4a7d1d6f… |

Notes on this table:
- Version 9 is still the live text at 2026-09-16 (MDT0251); the only later about-page change in the hashed set is the COI-policy section (2026-09-15, §3), not the supporter paragraph.
- The 2026-07-14 → 2026-07-19 employee-direction parenthesis (MDT0409→MDT0410; MDT0070/0071) is a change to the funding section but not to the supporter *names*, so MD70 records no version step there; MD24 does (MDT0070/0071/0123).
- Cross-lane sha256 agreement: MD24's after-captures (a954c479, 7c677d8f, afcf4bf3, d35c691c, 27b65104, bb1ee497, dee43e09, 4a7d1d6f) equal MD70's, so the two lanes hashed the same bodies.
- Seed MDT0003 counts "64 about captures before 20260719171236"; MD70 holds 158 unique digests before that timestamp — a counting-basis difference (caution X13), not a different change window.
- First-naming rows from other lanes agree with the ladder: Ralston 2025-12-07 (MDT0012); Farhi and Field 2025-12-16 (MDT0013/0226); Newman 2026-06-01 (MDT0014); Sijbrandij 2025-12-16 (MDT0011); Astralis/Expa 2025-12-07 (MDT0021/0022/0223/0224); La Centra-Sumerlin 2025-12-16 (MDT0020).
- What the ladder does not say: any gift date, amount or vehicle for any named supporter (supporter_coverage.csv marks every name except Audacious, Packard, Longview, Effektiv, SFF and the filed-payer rows as acknowledged_no_amount).

---

## 3. Conflict-of-interest policy history (lane MD72; C09.E2 / C08.E1)

**Versions found:** exactly one hashed body — "Conflict of interest policy (version 1.0), Last updated August 28, 2026", sha256 cc31342508f82e5388f4733416ecf865eed1172a4e115cd5c7f2e5038cb6e8f9, 172,769 bytes, 7 pages (MDP0708; MDP0711; MDQ0113; MDT0138). Scope: company-identifying risk assessments, footnote examples "as of July 2026" (MDP0712); Tier 3 current direct equity/debt always externally disclosed (MDP0713); provisional/full recusal (MDP0714; MDP0266); org must not invest in frontier-lab equity, free compute credits acceptable (MDP0715; MDQ0014); board/independent-director rules (MDP0265/0267/0268; MDS0790). No second version exists to diff (MDP0711).

**Seven distinct dates that must not be collapsed** (MDT0250, D06):
1. Printed last-updated: **2026-08-28** (MDP0708).
2. sitemap.xml lastmod for /coi-policy.pdf: **2026-09-16T10:34:29-07:00** = 17:34:29Z, 47 s before the lane GET (MDT0246).
3. HTTP Date of the GET: **2026-09-16T17:35:21Z**; Last-Modified header absent; ETag 8a7ecded…-ssl-df (MDT0245).
4. pdfinfo CreationDate / ModDate: **absent** (Google Docs renderer) (MDT0245).
5. This-run fetch: 2026-09-16T17:35:21Z (MDP0708).
6. Wayback captures of the PDF: **zero** — CDX `[]` HTTP 200 (MDS1638), sparkline first_ts=null (MDS1639), timemap empty (MDS1640); earlier CDX 503 ×5 (MDS1637); available API 429 (MDS1650); MD28 sparkline check 2026-05-19 also null (MDS0728).
7. About-page link: **absent at 2026-09-14T13:20:53Z** (Wayback 20260914132053, sha 0df432f8…, MDT0248/MDT0423) and **first present at 2026-09-15T16:00:44Z** (20260915160044, sha a03b6bcd…, the only one of 171 hashed bodies with the section, MDT0249/MDT0424). Live about page links the "current" policy at 2026-09-16T17:35:22Z (MDP0709; MDP0276; MDP0230).

Related dated statements: FRR (published 2026-05-19; window 2026-02-16–03-16) "METR did not have an applicable personnel conflict of interest (CoI) policy in place at the start of this project, and as such we did not run a formal recusal or disclosures process"; AEF-1 2.3 = No (MDP0716; MDQ0080/0082/0048/0049/0061/0089/0177). The same sentence is archived unchanged with no PDF link at 2026-08-01T17:29:09Z and in all 12 FRR digests to 2026-09-16 (MDP0710; MDS1641; MDS1649). No blog, news, feed, homepage or on-site search announces the PDF (MDS1643–1649, 1651); DuckDuckGo site search empty (MDS1647/1648). The FY2024 Form 990 Part VI written-CoI-policy checkbox (period ending 2024-12-31; MDP0231/0269; MDQ0069; MDS0789) is a governance checkbox, not the personnel/project policy (MDQ0069 undetermined).

**Per-project "in force" determinations (MD72 D01–D05, with MD28/MD30/MD35/MD48 support):**

| project | engagement date(s) | in force | rows |
|---|---|---|---|
| Frontier Risk Report | window 2026-02-16/2026-03-16; published 2026-05-19 | **none** (report's own words) | MDQ0177; MDQ0089/0090/0091; MDQ0080/0082; MDT0143; MDP0716 |
| Anthropic reviews: Opus 4.6 sabotage review; R&D-section review; agent-monitoring red-team | 2026-03-12; 2026-05-08; 2026-03-25 | **none** | MDQ0179; MDQ0041/0042/0043; MDQ0107/0108/0109 |
| OpenAI evaluations: GPT-5; gpt-oss-120b; Codex-Max; GPT-5.6 Sol | 2025-08-07; 2025-10-23; 2025-11-19; 2026-06-26 | **none** | MDQ0180; MDQ0009/0025/0010/0008 |
| OpenAI / Hugging Face investigation | 2026-08-26 (footnotes added 2026-09-13) | **none** — two days before the printed date; not applied backward; the Barnes non-involvement footnote is not recorded as an application of v1.0 | MDQ0178; MDQ0046; MDQ0116; MDQ0039/0040 |
| Anthropic cybersecurity-incidents investigation | agreement 2026-09-09 | **v1.0 is the only hashed version that could apply**; no document says it was applied; about-page link still absent 2026-09-14 | MDQ0181; MDQ0095; MDQ0142/0143; MDT0148; MDP0245 |
| Earlier evaluations (GPT-4o 2024-08-07; o1 2024-09-12; Claude 3.5 Sonnet 2024-10-30; GPT-4.5 2025-02-27; o3 2025-04-16; Nova 2025-07-07; sabotage-report review 2025-10-28; Mythos 2026-04 / 2026-09-01) | 2024-08-07 … 2026-09-01 | no dated METR personnel policy identified; MD72 did not enumerate these (MD48 rows carry empty policy_version) | MDQ0132/0126/0144/0130/0128/0150/0146; MDS0640 |

Comparators dated in the pack: AEF-1 v1 2025-12-04; Apollo norms 2025-11-26; Transluce policy 2026-08-27; GAGAS 3.18 (2024-02); EU AI Act Art. 31(4) 2024-06-13; GPAI CoP 2025-07-10; Illinois P.A. 104-0538 2026-07-06 (effective 2027-01-01, audit duty 2028-01-01); California AB 1405 chaptered 2026-09-09 (operative 2029-01-01); Anthropic RSP v3.4 §3.6.1 effective 2026-07-08 (MDP0206–0228, 0232, 0243; MDQ0070/0071).

---

## 4. Future-document calendar (research/calendar.csv) and unsent records requests (REQUESTS.jsonl)

All ten closers were last checked 2026-09-16T10:00:00Z. Row ids are the MD45/MD43/MD39/MD11/MD22 rows that carry the same closer.

| id | document | claims it could settle | earliest expected | next check | state | rows |
|---|---|---|---|---|---|---|
| CAL01 | METR's Anthropic incident report if the eight-week schedule from 2026-09-09 holds (metr.org/blog + RSS) | C03; C04; C08 | ~2026-11-04 (approximate; extendable) | 2026-11-04 | future | MDT0166; MDT0178; MDT0173; MDS0744 |
| CAL02 | CY2025 Forms 990 for calendar-year intermediaries and DAF sponsors (SVCF, Coefficient entities, RAND, calendar-year Audacious partners) | C01; C02; C06; C07 | 2026-11-16 (extended; original 2026-05-15) | 2026-11-16 | future | MDT0164; MDT0171; MDT0179; MDT0027; MDT0053/0054/0058; MDT0231/0232 |
| CAL03 | Good Ventures Foundation FY2026 990-PF (FYE 2026-06-30) — tests whether a donated stake arrived after 2025-06-30 | C05; C07 | 2026-11-16 (statutory 2026-11-15 is a Sunday); extendable to 2027-05-17 | 2026-11-16 | future | MDT0165; MDT0172; MDT0180; MDT0193; MDT0217–0222 |
| CAL04 | METR's next Form 990 (CY2025) and any audited financial statement | C01; C02 | 2026-11-16 (extended; original 2026-05-15) | 2026-11-16 | future | MDT0163; MDT0170; MDT0181; MDT0017; MDT0159; MDS0345 |
| CAL05 | Anthropic registration statement / holder disclosure (EDGAR) — confidential draft S-1 announced 2026-06-01 is not a holder table | C05; C07 | as published | 2026-10-16, then monthly | future | MDT0167; MDT0174; MDT0182; MDT0162; MDP0372 |
| CAL06 | Statutory records productions (UK DSIT FOIA; NIST FOIA; Commission Reg. 1049/2001; NPT §6104(d); IRS 4506-A/5227) | C01; C02; C06; C07 | per request clock | on Kevin's approval decision | **USER_AUTHORITY_WAIT** | MDT0169; MDT0177; MDT0184 (these MD45 rows predate registration; see caution X08) |
| CAL07 | National Philanthropic Trust FY2026 Form 990 (Schedule B Part I restricted every year; expect sponsor aggregates only) | C07 | 2026-11-16; extension to 2027-05-17 | 2026-11-16 | future | MDT0160; MDT0026 |
| CAL08 | Next unfiled returns of the 28 named Audacious partners (per-partner dates) | C06 | earliest 2026-10-15 (Tepper, FYE 2025-11-30 extended); Rippleworks FYE 2026-04-30 original 2026-09-15 passed unposted (extended 2027-03-15); calendar-year partners 2026-11-16; Someland 2027-01-15 | 2026-10-15 | future | MDT0185–MDT0216 |
| CAL09 | Vanguard Charitable FY2025 990 XML in the GivingTuesday lake (absent; ProPublica render used) and Fidelity/Schwab FY2026 returns | C07 | when posted; June-year FY2026 due 2026-11-16, extension 2027-05-17 | 2026-11-16 | future | MDT0057; MDT0230; MDT0023–0025 |
| CAL10 | Overdeck Family Foundation TY2024 Statement 26 attachment as extractable text; Joe and Clara Tsai Foundation TY2025 990-PF XML (lake 404) | C06 | when posted | 2026-11-16 (with CAL02) | future | MDT0201; MDT0197 |

Also dated but not in calendar.csv: TED/Contracts Finder/NIST/AISI procurement update points (as published; MDT0168/0175/0176/0183); Longview Inc Ltd and Founders Pledge Ltd UK accounts due 2026-09-30, EV UK 2027-03-31 (MDT0059); METR FY2026 Form 990 original due 2027-05-17 (MDT0018); Lyda Hill FYE 2026-11-30 due 2027-04-15 / 2027-10-15 (MDT0198); Tsai and Oak TY2026 due 2027-05-17 / 2027-11-15 (MDT0197/0200).

**Records-request drafts** (all state USER_AUTHORITY_WAIT; approved_for_send false; drafted 2026-09-16T09:06:36Z–10:15:00Z; registered 2026-09-16T11:59:05Z; sent_utc null; deadline_utc null; no clock is running; each lane draft names the $71M, each cleaned draft does not):

| id | custodian | route | response clock | donor-side custodian | rows |
|---|---|---|---|---|---|
| REQ-MD44-UK-DSIT-FOI | Department for Science, Innovation and Technology (UK) | Freedom of Information Act 2000 | 20 working days from receipt (s.10) | no | MDT0169/0177/0184; MDP0203–0205 |
| REQ-MD44-US-NIST-FOIA | NIST FOIA Office, U.S. Department of Commerce | 5 U.S.C. §552 | 20 working days (§552(a)(6)(A)(i)) | no | MDT0169/0177/0184; MDS1595 |
| REQ-MD44-EU-EASE-1049 | European Commission, DG CNECT, via EASE | Regulation (EC) 1049/2001 | 15 working days from registration (Art. 7(1)) | no | MDT0169/0177/0184; MDF0236 |
| REQ-MD37-NPT-6104D | National Philanthropic Trust (EIN 23-7825575) | IRC §6104(d) public-inspection copy of FY2025 Form 990 | 30 days if in writing (§6104(d)(1)) | yes | MDP0370; MDP0328; MDT0160 |
| REQ-MD41-IRS-4506A-5227 | IRS RAIVS Unit (Ogden, UT) | Form 4506-A line 8, public-inspection copy of any Form 5227 (§6104) | not stated on the form; IRS processing time | yes | MDP0455; MDP0457; MDT0161 |

---

## 5. The Feb–Aug 2026 window (the six months the $71M statement covers)

METR's phrase is "In the last 6 months" as of 2026-08-14 (MDF0089). The bounds **approximately 2026-02-14 to 2026-08-14** are a lane derivation (commitment_reconciliation.csv denominator row; MDP0484 note). The JSON `window_feb_aug_2026` lists 44 entries from 2026-02-01 to 2026-08-31 with `inside_derived_window_2026-02-14_to_2026-08-14` set per entry. Inside the derived window, dated events are:

- **Money**: only the Packard $350,000 commitment, dated by the grantee-page datePublished 2026-07-06 (award year 2026; no instrument day) — the single compatible component; remainder around $70.65M is arithmetic (MDP0055/0521; MDF0089). Dylan Field's 2026-08-17 Form 4 gift is to an unnamed DAF, outside the window and not METR. HF API credits (~$400K, 2026-08-26) are in-kind and outside. Nothing else money-typed is dated inside the window.
- **Statements**: Forbes India 2026-02-14 (boundary); Moskovitz Bluesky 2026-03-30 ×2, 2026-04-11; Washington Examiner 2026-04-17; Newman X 2026-04-18; Forbes 2026-04-20; WIRED Farhi 2026-07-15; Anthropic 2026-07-30; funding update 2026-08-14 (the statement itself, at the window's end).
- **Projects**: FRR window 2026-02-16 → 03-16; confidentiality post 2026-02-17; Opus 4.6 review 2026-03-12; red-team 2026-03-25; CAISI slide 2026-03-27; Mythos Preview 2026-04; R&D review 2026-05-08; FRR published 2026-05-19; Sol 2026-06-26.
- **Policy**: Illinois P.A. 104-0538 2026-07-06; RSP v3.4 2026-07-08. (COI v1.0 2026-08-28 and Transluce 2026-08-27 fall just outside.)
- **Filings / registry**: 2026-04-30 Rippleworks FYE; 2026-05-15 METR FY2025 990 original due (not posted) and GVF FY2025 990-PF signed; 2026-06-01 confidential draft S-1; 2026-06-30 GVF and June-year sponsors' FY2026 year-end, June 2026 progress report.
- **Page versions (all PAGE dates)**: donate footnote removed 2026-02-05→02-11 (boundary); Pew + EU AI Office 2026-03-06→03-11; Newman 2026-05-25→06-01; Packard 2026-06-29→07-06; donate employee parenthesis 2026-07-03→08-04; about employee parenthesis 2026-07-14→07-19; restructure with "individuals from Jane Street" 2026-07-19→08-04; Wayback about captures MDT0361–MDT0412 (52 unique digests between 2026-02-02 and 2026-08-04).
- **Just outside**: 2026-08-18 LaCentra spelling; 2026-08-26 HF post and Moskovitz post; 2026-08-27 Transluce and first funding-update archive; 2026-08-28 COI v1.0; 2026-08-31 Anthropic/METR posts.

---

## 6. Contradictions between dates in different rows (each with row ids)

1. **GVF FY2026 due date 2026-11-15 vs 2026-11-16**: MDT0165, MDT0180, MDT0217, MDT0221, MDT0222 carry 11-15 (statutory day, a Sunday); MDT0163, MDT0193 and calendar CAL03 carry 11-16 (next business day). One deadline; label both.
2. **CAL06 state**: MDT0169 ("REQUESTS.jsonl is empty") and MDT0184 ("CAL06 state=not started") were written at 09:49Z on 2026-09-16; the five drafts were registered at 11:59:05Z and calendar.csv now reads USER_AUTHORITY_WAIT. Ordering, not conflict; the calendar and REQUESTS.jsonl are current.
3. **ARC→METR transfer**: Schedule N 2024-04-30 / $4,553,935 FMV (MDT0030/0228; MDF0007) vs Schedule I $4,477,169 + $76,766 (MDF0064/0065) vs Part III "May" (MDT0229) vs METR 990 related-org $4,501,424 (MDF0034; MDP0032). Three documents; the rows themselves say do not collapse.
4. **Packard date**: "2026" (year) on MDF0020/0021/0078/0090/0191–0193 vs "2026-07-06" (day) on MDT0122/MDP0030/MDF0091/0092/0416/1031 — the day is the catalog datePublished (MDT0010), not an award day; MD50 lists the missing instrument day as a gate correction (MDP0598). dateModified 2026-09-14 is a third page date.
5. **ARC donate page 2023-03-06 vs spin-out announcement 2023-09-19** (MDT0031 vs MDT0028): the page stamp predates the event its body describes; body sentence undated.
6. **Seed capture count "64" vs MD70 "158"** before 20260719171236 (MDT0003 vs MDT0253–0410): different indexes; same change window.
7. **Capture 20260827031343**: HTTP 200 in MD70 (MDT0414) vs connection-refused in MD72 (MDS1642). Different runs; same content conclusion.
8. **MD70 "before" vs MD24 "immediately before"** for versions 3, 5, 6, 7, 8 (e.g. 2025-09-29 vs 2025-12-03; 2025-12-16 vs 2026-03-06): paragraph-distinct vs page-digest neighbours; both correct at their own level.
9. **METR formation dates**: ruling 2024-03 (MDE0014, entities.csv) vs TaxPeriodBeginDt 2024-05-01 (MDF0410) vs "formed May 2024" (MDS0583) vs Schedule N 2024-04-30 vs announcements 2023-09-19/2023-12-04. No founding-date row exists in the listed tables; ARC's own founding date is absent everywhere (MDE0037 only says grants "between 2021 and 2024").
10. **FRR recusal**: item 2.5 "Yes" vs "did not run a formal recusal or disclosures process" on the same 2026-05-19 page (MDQ0045/0052/0064/0085) — recorded, not reconciled.
11. **Anthropic eight-week end date**: computed ~2026-11-04 by MD45 (MDT0166/0178; MDS0744) while MD29 declines to compute it (MDT0148) and Anthropic allows extension.
12. **EU AI Office contract**: 2025-11-28 notice (MDP0281) vs 2025-12-15 IssueDate/FTS start (MDF0150/0151) vs 2025-12-23 criteria row (MDP0291) vs about-page sentence 2026-01-27→02-02 (MDT0068/0069). Use 2025-12-15 for the instrument.
13. **SFF-2025 matching pledge typed both ways**: `commitment` (MDF0081/0217) vs `recommendation` (MDF0046/0197); the amount is the same $428,000 conditional pledge.
14. **Amodei essay**: month-only post-date "September 2026" (MDP0247) vs HTML Last-Published 2026-09-14; the pack correctly refuses 2026-09-12.
15. **NY Post "2022 Moskovitz donation to ARC"** (MDP0568, undetermined) vs the pack's 2022 rows, which are Open Philanthropy recommendations and GVF Part XV grants to ARC, not a personal gift.

---

## 7. Suggested figures (details in JSON `suggested_figures`)

F-TL-1 master swim-lane timeline 2021–2026 with greyed future closers · F-TL-2 supporter-paragraph version ladder with 172-capture density strip and window bars (MD24 before → MD70 after) · F-TL-3 COI policy seven-date separation axis over per-project in-force bars · F-TL-4 the derived six-month window with the single compatible component hatched as a page date and every other in-window event by category · F-TL-5 calendar closers and the five unstarted request clocks · F-TL-6 "one flow, three attestations" (recommendation / ledger / filed) for the 2022–2024 ARC–METR flows · F-TL-7 stake statements against Good Ventures fiscal years with the FY2026 closer.

Rules to print on every figure: page-appearance and capture dates are not gift, grant, payment or in-force dates; commitments, recommendations, regrants, transfers, filed grants, paid grants, contracts, in-kind estimates and equity values are never summed; the ~$70.65M remainder is arithmetic, not a list of unidentified donors; the five records requests have not been sent and no clock is running.
