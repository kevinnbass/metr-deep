# Audit E — The donated Anthropic stake and the Anthropic ties of METR's supporters

Pack: `/mnt/f/projects/anthropic/metr_deep` (read-only). Tables read: `research/relationships.csv` (MDR), `provenance.csv` (MDP), `funding_events.csv` (MDF), `source_coverage.csv` (MDS), `timeline.csv` (MDT), `entities.csv` (MDE); element text from `research/CLAIMS.md`. Rows whose note contains "superseded by" were skipped (9 MDF, 18 MDS, 2 MDT, 1 MDE); where a superseded row matters it is named as such. Companion JSON: `E-stake-and-anthropic-ties.json` (same directory).

Elements covered: C05.E1 (supporter's Anthropic investment/governance role attached to the exact person or entity), C05.E2 (donation event and investment event separately sourced and dated), C05.E3 (entities kept distinct), C06.E4 (adjacency labelled not a money flow), C07.E1–E4 (statements quoted exactly; vehicles excluded; vehicles possible; no transaction into METR).

Seed vs lane: rows whose note carries `lane=research/grok-out/S0-seed-import.csv` are the 2026-09-14 transcription from the 10-metr pack (role=context). Every seed fact used here was re-collected by a 2026-09-16 lane (MD09, MD33, MD39, MD40, MD41, MD42, MD47, MD71); the lane row is the evidence row and is the one to cite.

---

## 1. Each supporter's documented Anthropic link, attached to the person or entity the source names (C05.E1, C05.E2)

Rule applied throughout: the investment row and the donation row are different rows, different sources, different dates, different money types; they are never summed and never drawn on the same axis.

### 1.1 Jaan Tallinn (METR names "recommendations by the Survival and Flourishing Fund", not the person)

| Fact | Row(s) | Source class / date | New vs seed |
|---|---|---|---|
| "The Series A round was led by Jaan Tallinn, technology investor and co-founder of Skype." Amount and share count not disclosed; $124M is the round | **MDR0080** (MD33), MDR0024 (MD09), MDE0063; seed MDR0001 | issuer statement, 2021-05-28 | lane |
| Declined a board seat, own words (Semafor): "I was looking for someone I felt was a good representative of the things that I'm worried about," | **MDR0091** (self-statement); MDR0025 (press paraphrase) | 2023-04-28 | lane |
| Declined board membership, own words in Estonian (Postimees quoting January Äripäev radio); the surrounding sentence, not Tallinn, says observer | **MDR0090** (self-statement); MDR0026 (press: "reported board observer"); MDR0165/MDR0171 (MD47 role edges, not a money flow) | 2026-02-22 | lane |
| Metaplanet is "Jaan Tallinnale kuuluv investeerimisettevõte" (his investment company); share count undisclosed; not a US 990 filer | MDE0064, MDE0030, MDS0773, MDS0778 | press, 2025-09 | lane |
| Anthropic /company board list: none found for Tallinn (directors only; observers not listed) | MDS0237, MDS0756 | issuer, 2026-09-16 | lane |
| SEC EFTS "Jaan Tallinn" and Tallinn+Anthropic: 0 Anthropic-issuer hits | MDS0239, MDS0757, MDS0778 | SEC | lane |
| Donation side (unsummed): SFF-2024 recommendation $204,000 (MDF0215); SFF-2025 recommendation $120,000 (MDF0216) and matching pledge $428,000 typed commitment (MDF0217); ledger paid_grant $184,000 on 2024-12-06 via FP-US (MDF0218); Founders Pledge Inc TY2024 filed_grant $184,000 (MDF0219); ledger SFF-spec $10,000 on 2024-07-23 and $10,000 on 2024-07-24 (MDF0221, MDF0222); SVCF TY2024 filed_grant $20,000, adviser not named (MDF0220) | seeds MDF0008–MDF0011 | issuer/self/funder filings | lane |

Contradiction to carry into any caption: the posted figure metr-01b said "two of them its board observers by their own account"; MD49 adjudicated this as incomplete because Tallinn's own words decline a board seat and the observer label is press (MDP0571). Moskovitz is the only self-described observer.

### 1.2 Dustin Moskovitz (not a METR-named supporter)

| Fact | Row(s) | Date | New vs seed |
|---|---|---|---|
| "The round included participation from James McClave, Dustin Moskovitz, the Center for Emerging Risk Research, Eric Schmidt, and others." Issuer names the person, not a foundation, DAF, trust or LLC | **MDR0082** (MD33), **MDR0207** (MD71), MDE0083, MDE0108, MDS1624, MDS0878; seed MDR0001 | 2021-05-28 | lane |
| "I'm a board observer at Anthropic and we are early donors to OpenAI…" (Stratechery, Ben Thompson) — self-described; no issuer document confirms | **MDR0089** (MD33), MDT0238 (MD71), MDR0168 (MD47, not a money flow); seed MDR0003 | 2025-10-20 | lane |
| Donation of the Anthropic stake: see §2. No day is stated anywhere. | MDP0707, MDT0244 | statements 2025-11-10 → 2026-08-26 | lane |
| Donation to METR: none documented (see §4) | MDS1011–MDS1016, MDS0870 | FY2020–FY2025 | lane |

MDP0707 (MD71 Task D) is the pack's explicit separation record: "Series A issuer statement is 2021-05-28 … Donation/holding statements this run begin 2025-11-10 in press and 2026-03-30 in Moskovitz's own words … Issuer Series A participation is not the donation event."

### 1.3 Schmidt Sciences (METR-named brand) vs Eric Schmidt vs Hillspire

- Anthropic names **Eric Schmidt (individual)** as a Series A participant, amount undisclosed: MDR0081 (MD33), MDR0009 (MD04), MDE0061. It does not name Hillspire, Schmidt Sciences or the Fund (MDR0081 limitation).
- **Hillspire, LLC** (family office): CNBC 2025-01-21 "has made investments in 22 private AI firms since 2019 … data provided exclusively to CNBC by Fintrx"; cheque size undisclosed: MDR0088, MDR0010, MDR0123, MDE0062. Press, not issuer.
- **Schmidt Sciences, LLC** is "a subsidiary of The Eric and Wendy Schmidt Fund for Strategic Innovation (EIN: 46-3460261)" (MDE0059, MDE0060). METR names the brand; which legal entity paid is not stated (MDF0214). EIN 46-3460261 TY2024 990-PF Part XV: none found for METR/ARC (MDS0770; "METR" substring occurs only in an address, RESTON METRO PLAZA). Next document: TY2025 Part XV.
- SEC "Eric Schmidt" Anthropic: 0 (MDS0758). Kept distinct: MDE0134.

### 1.4 "individuals from Jane Street" vs Jane Street legal entities

- METR names "individuals from Jane Street" — a class of unnamed natural persons, no amount, undated (MDF0213, MDE0055; seed MDF0015). janestreet.com search q=METR: none (MDS0775). METR FY2024 Schedule B is RESTRICTED (MDS0769).
- **Jane Street Global Trading, LLC**: court Exhibit 1, In re FTX Trading Ltd. 22-11068 Doc 10241-1, filed 2024-03-22: "Jane Street Global Trading, LLC 3,332,833 $99,999,988" (MDR0083 CONFIRMED; MDR0004 DIFFERS after field audits; MDE0058, MDE0001).
- **"Jane Street"** (legal entity not identified by the issuer): Series E 2025-03-03 (MDR0084/MDR0005), Series F 2025-09-02 (MDR0085/MDR0006), Series G 2026-02-12 (MDR0086/MDR0007), Series H 2026-05-28 (MDR0087/MDR0008/MDR0125; seed MDR0002 carries the $65B round, not a stake). Amounts undisclosed.
- SEC "Jane Street" Anthropic: 214 hits, all fund NPORT/N-CSR or CoreWeave 8-K, none Anthropic PBC (MDS0777, MDS1061, MDS1219). Kept distinct: MDE0133, MDE0056, MDE0057; reclassification MDP0622.
- MDR0124/MDE0128 record a natural-person FTX-estate purchaser named in the same exhibit; the pack does not connect that person to METR's unnamed individuals and a figure must not.

### 1.5 Farhi, Ralston, Field, Newman; Pew, Packard, Sijbrandij and the rest

- Bounded negative: "none found in Anthropic Series A/E/F/G/H and /company pages as of 2026-09-16T09:37:25Z for Packard, Pew, Sijbrandij, Audacious, LaCentra-Sumerlin, Astralis, Expa.org, Longview, Effektiv Spenden, David Farhi, Geoff Ralston, Dylan Field, or Steve Newman as an Anthropic investor or director" (MDS0776; "not a full Anthropic cap table").
- Dylan Field: SEC hits for "Dylan Field" Anthropic are Figma, Inc. filings (MDS0761); Figma role edge MDR0170.
- Adjacency only, all labelled not a money flow (C06.E4): Farhi–OpenAI (MDR0155 o1 credit; MDR0156 CHM profile; MDR0172 WIRED departure summer 2025; MDR0184 Guardrails Alliance); Ralston–AVERI funders / SAIF founder / former YC president (MDR0158, MDR0169); Newman–Golden Gate Institute for AI / Epoch AI (MDR0167, MDR0164).
- Named-supporter acknowledgment rows without amount, date or vehicle: MDF0223–MDF0235 (MDF0225 Pew, MDF0226 Packard, MDF0224 Sijbrandij, MDF0232 Farhi, MDF0233 Ralston, MDF0234 Field, MDF0235 Newman); Packard live grants-database HTML 0 METR strings (MDS0771). Amounts held in MD02/MD03/MD05 are outside this audit.

---

## 2. The donated Anthropic stake: every dated public statement, quoted exactly (C07.E1)

All this-run rows are MD71 (`research/grok-out/MD71-donation-statements-quoted.csv`, review MDREVIEW-MD71.md), fetched 2026-09-16T17:34Z with sha256 primaries. Seed locators MDT0004–MDT0007 are context only.

| Date | Speaker / venue | Exact quote (quote_300) | Says | Does not say | Rows |
|---|---|---|---|---|---|
| 2025-10-20 | Dustin Moskovitz, Stratechery | "But the harder thing has been like I'm a board observer at Anthropic and we are early donors to OpenAI and there's always this tension on if you're creating capabilities, are you also creating dangerous capabilities?" | observer at Anthropic; early donors to OpenAI | no donation, no vehicle, no foundation holding, no timing, no share class, no amount | MDT0238, MDR0089, MDP0703 |
| 2025-11-10 | Cari Tuna as quoted ("she says"), Forbes Australia | "Their Anthropic stake (worth an estimated $500 million) was moved into a nonprofit vehicle in early 2025 so they could invest any "significant financial return" back into philanthropy and "dispel any perception of conflict of interest," she says." | 'a nonprofit vehicle'; 'early 2025'; $500M is the article's estimate | legal entity; share class; GVF/Coefficient/DAF/trust — all not stated; not Moskovitz's words; press | MDT0240, MDP0705; seed MDT0004 |
| 2025-12-18 | Alexander Berger (CEO, Coefficient Giving; "Views my own"), X 2001669972171661401 | "It's not. Also: 1. Open Phil never invested in Anthropic, dustin did early on. 2. He's since donated his stake (and not to us). 3. We're called Coefficient Giving now." | OP never invested; Dustin invested early; he donated his stake; not to "us" | donee not named; "us" not expanded to a filer; share class, amount, day not stated; person statement, not an org page | MDT0239, MDP0704; seed MDT0006 (full text) |
| 2026-02-14 | Cari Tuna as quoted, Forbes India | "Their Anthropic stake (worth an estimated $500 million in mid-November) was moved into a non-profit vehicle in early 2025 …" | restatement | vehicle still unnamed | MDT0243 |
| 2026-03-30 05:24Z | Moskovitz, Bluesky 3miawblqk7224 (a reply) | "Our Anthropic shares are entirely in our foundation - no personal benefit." | shares entirely in 'our foundation'; no personal benefit | 'our foundation' not a legal entity; no transfer timing; no share class; no amount; GVF/DAF/trust/Coefficient not stated | MDT0234, MDP0699, MDS1476; seed MDT0007 |
| 2026-03-30 05:28Z | Moskovitz, Bluesky 3miawjaazyc24 | "Per the other thread all Anthropic holdings are in the foundation, dedicated to charity." | all holdings in 'the foundation' | legal entity; timing; class; amount | MDT0235, MDP0700 |
| 2026-04-11 | Moskovitz, Bluesky 3mjaq5x2pws2e | "We have given away $5B and we have about $20B more in the foundation and some more personal (you can look on bloomberg for that). The foundation is invested in Anthropic as well." | foundation is invested in Anthropic (present tense); ~$20B in the foundation | $20B is not the stake size; do not equate with GVF 990-PF assets; no donation date; no legal entity | MDT0236, MDP0701 |
| 2026-04-17 | Washington Examiner (press) | "That same year, Moskovitz transferred his stake in Anthropic, which had" [quote_300 truncated in the row] | per result field: transferred his stake, reportedly ~$500M, "to his charity" | 'his charity' unnamed; 'reportedly' via Forbes.au | MDT0242 |
| 2026-04-20 | Forbes (Durot, Peterson-Withorn), via Wayback id_ 20260421043155 | "Last year he dona­ted his early investment in AI giant Anthropic: an estimated stake of less than 0.8% that has already skyrocketed in value amid the AI boom." | 'last year' relative to 2026-04-20; <0.8% is an estimated bound | vehicle; legal entity; share class; not Moskovitz's words | MDT0241, MDP0706, MDS1630; seed MDT0005 |
| 2026-08-26 | Moskovitz, Bluesky 3mtygcpxluc2b | "GV is itself a beneficiary of that wave (via Anthropic and a number of other investments)." | names Good Ventures / GV | whether GV = Good Ventures Foundation 501(c)(3): not stated; that GV received the 2025 donation: not stated | MDT0237, MDP0702 |
| — | Bluesky 3mnnmzfh7zc27 (parent notFound) | "We literally just made a decision with the foundation to  participate in the latest round" | 'the foundation', 'the latest round' | Anthropic not named; not counted | MDS1636 |

Bounded negatives on the statement hunt: X @moskov and x.com search (MDS1619, MDS1626); goodventures.org pages and search (MDS1620, MDS1621, MDS1627); openphilanthropy.org redirect and /grants/ (MDS1622, MDS1634); coefficientgiving.org pages, search, /grants/ 404 (MDS1623, MDS1628, MDS1629); anthropic.com Series A, news, company (MDS1624, MDS1633); Bluesky searchPosts 403 and getAuthorFeed (MDS1625, MDS1635); Wayback/jina caps (MDS1631, MDS1632).

MDT0244 (MD71 D01) fixes the rule: "These are statement dates, not a filing date of a share transfer … A statement date is not a donation closing date unless the statement gives one (only B02 gives 'early 2025', still not a day)."

Quote-rendering defects to normalise before display: HTML entities (`I&#8217;m`) in MDT0238/MDP0703 vs typographic apostrophe in MDR0089 vs straight apostrophe in seed MDR0003; soft hyphen U+00AD inside "donated" in MDT0241; truncated quote in MDT0242; MDT0239's quote_300 is one sentence of the tweet (full text only in seed MDT0006 and the MDT0239 note); MDR0090 is Estonian with only a subject-line paraphrase.

---

## 3. Vehicles (C07.E2, C07.E3)

### 3.1 Excluded by a document, with the period it covers

| Vehicle | Excluding document | Period | Rows |
|---|---|---|---|
| Coefficient Giving / Open Philanthropy as donee | Berger X 2025-12-18 "donated his stake (and not to us)" — a person statement, not an org filing; only as strong as that statement | as of 2025-12-18 | MDT0239, MDT0006, MDP0704; org pages silent MDS1622, MDS1623 |
| Open Philanthropy as an Anthropic investor | same post: "Open Phil never invested in Anthropic, dustin did early on" | as of 2025-12-18 | MDT0239 |
| Good Ventures Foundation (EIN 46-1008520) as recipient of private/closely-held stock | Form 990-PF Schedule B NonCashPropertyContributionGrp: every NoncashPropertyDesc FY2020–FY2025 is "PUBLICLY TRADED SECURITIES"; contributors named (not RESTRICTED); no Anthropic, closely-held, partnership/LLC line | FY2020 (from 2019-07-01) through FY2025 (to 2025-06-30). FY2026 not covered | MDF0318, MDF0320, MDF0322, MDF0325, MDF0329, MDF0330, MDF0333; MDT0008; MDE0114 |
| Good Ventures Foundation as METR payer | Part XV GrantOrContributionPdDurYrGrp each year; FY2025 has 565 grant rows, zero METR hits | FY2020–FY2025 | MDS1011–MDS1016 |
| Remainder Interest Trust as a 990-series filer / private foundation | IRS e-file index_2022–2026 (0 hits in 656,503 / 705,156 / 728,719 / 748,906 / 385,890 rows); SOI sit-2020/2021/2022 (0); ProPublica 0; EDGAR "No matching companies."; 990-PF instructions route split-interest trusts to Form 5227 | 2020–2026 indexes | MDS0906–MDS0914, MDS0917, MDS0918, MDP0459 |
| Any vehicle via an Anthropic public registration statement | no public S-1/S-1/A for Anthropic, PBC; 35 EDGAR name matches are series/SPV funds; confidential draft S-1 (2026-06-01) is a Rule 135 notice | as of 2026-09-16 | MDS0938, MDS0931, MDS0926–MDS0928, MDS0922, MDS0924, MDS0934, MDT0162, MDP0372, MDS0868, MDS0877 |

The pack does **not** combine Tuna's "early 2025" with the FY2025 Schedule B (period 2024-07-01 to 2025-06-30, only publicly traded securities received 2025-06-30) into an inference that GVF cannot be the "nonprofit vehicle". MDF0333's limitation is deliberately narrow: "for this tax year the contribution-schedule non-cash property line does not identify a closely-held or private-stock inflow. Later-arrival of a donated private stake after 2025-06-30 is the FY2026 closer." A figure may show both facts; it must not draw the inference (reporting thresholds and characterisation of a private-stock gift on Schedule B are not stated in any row).

### 3.2 Still possible, with the exact identifying document and its expected date

| Vehicle | Identifying document | Expected date | Rows |
|---|---|---|---|
| "our foundation" if it is GVF and the stake arrived after 2025-06-30 | Good Ventures Foundation Form 990-PF TAX_PERIOD=202606 (FY2026, 2025-07-01 to 2026-06-30) Schedule B NonCashPropertyContributionGrp / Schedule M / Part XV, on IRS TEOS and the bulk e-file index (index_2026.csv currently holds only TAX_PERIOD=202506 for EIN 461008520) | original due 2026-11-15 (Sunday) → **2026-11-16**; Form 8868 extension to 2027-05-15 (Saturday) → 2027-05-17; the FY2025 return was signed 2026-05-15, i.e. on extension; CA RRF-1 same dates | MDT0165 (CAL03), MDT0217, MDT0218, MDT0219, MDT0220, MDT0221, MDT0222, MDS0947, MDS0937, MDS1021 |
| any holder in an Anthropic public S-1 | Form S-1 Item 11(m) → Reg. S-K Item 403 beneficial-owner table — lists only >5% holders of a voting class plus directors/NEOs; a stake press-estimated at "less than 0.8%" would be outside the table unless held by a director/NEO; so this is not a guaranteed closer | unknown; next web check 2026-10-16 (freshness window, not a filing date) | MDS0938, MDP0463, MDP0464, MDT0162, MDS0759 |
| a DAF account at NPT (EIN 23-7825575), Vanguard Charitable (23-2888152), SVCF (20-5205488), Fidelity Charitable (11-0303001), Donor Advised Charitable Giving (31-1640316) | none public. Sponsor Schedule M SecuritiesCloselyHeldStockGrp reports aggregates only (NPT FY2025 $1,183,079,981 MDP0337/MDP0445; Vanguard FY2025 $96,652,480 MDP0400; Fidelity FY2025 $464,187,816 MDP0415; SVCF TY2024 $2,562,398 MDP0385; DACG FY2025 $14,402,947 MDP0430); public Schedule B Part I is the token RESTRICTED (MDP0329–MDP0333); Schedule I Part II has no donor/adviser column. **A DAF sponsor's filing would not name the account principal** (MDS0886–MDS0890, MDE0135, MDS1104, MDS1105). A 6104(d) public-inspection request was drafted, unsent (MDP0329 next_document) | structural; FY2026 sponsor returns follow the same calendar | as listed |
| Dustin Moskovitz Remainder Interest Trust dated March 10, 2018 (trustee Tom Van Loben Sels; contributor of publicly traded securities to GVF: FY2024 $446,082,975; FY2025 $1,395,695,354) | if a split-interest trust (IRC 664 / 4947(a)(2)): Form 5227 via Form 4506-A line 8, public except Schedule A, K-1, trust instrument and donor attachments — draft written, approved_for_send false, unsent (MDP0461); if a grantor/family trust: Form 1041, confidential under IRC 6103, no public route (MDP0457, MDP0462). Trust type is stated by no document (MDP0454, MDP0456, MDP0460) | n/a; EIN not located; TEOS 403 (MDS0915) | MDE0109, MDE0110, MDT0161, MDP0452, MDP0453, MDP0455, MDP0458, MDF0296, MDF0326, MDF0331 |
| Moskovitz Investments LLC (Blue Owl S-1 selling holder, 96,103 Class A issuable from Operating Group Units — not Anthropic); Monster Growth Ventures LLC (Facebook 2013–2014); The CTF Trust dated 2012-12-27; Moskovitz Investment Holdings, LLC (Asana); Dustin A. Moskovitz Trust dated 2005-12-27 | an Anthropic issuer transfer ledger or public S-1 selling-stockholder table naming the vehicle; CA/DE Statements of Information (CA BizFile Incapsula, DE ICIS captcha; FL Sunbiz lists a same-name LLC L10000004438 not tied to Moskovitz by any filing). Identifying a vehicle would not establish a METR payment; that needs a 990-PF Part XIV/XV donee line or a METR Schedule B naming the vehicle (MDP0374) | n/a | MDE0095–MDE0108, MDS0853–MDS0885, MDP0373 |

---

## 4. Good Ventures Foundation Schedule B, FY2020–FY2025 (MD39), and the crucial negative (C07.E4)

Per-year lines exactly as the rows hold them. `equity_value` and `transfer` are never summed with each other or with any METR money.

| FY (period) | Contributor / line | Amount | money_type | Row |
|---|---|---|---|---|
| FY2020 (2019-07-01 to 2020-06-30) | ContributorNum 1 DUSTIN MOSKOVITZ (person) | 1,017,208,584 | equity_value | MDF0317 |
| FY2020 | NonCash #1 PUBLICLY TRADED SECURITIES, received 2020-06-26 | 1,017,208,584 | equity_value | MDF0318 |
| FY2021 (2020-07-01 to 2021-06-30) | ContributorNum 1 DUSTIN MOSKOVITZ | 269,719,012 | equity_value | MDF0319 |
| FY2021 | NonCash #1 PUBLICLY TRADED SECURITIES, received 2020-09-03 | 269,719,012 | equity_value | MDF0320 |
| FY2022 (2021-07-01 to 2022-06-30) | ContributorNum 1 DUSTIN MOSKOVITZ | 170,486,492 | equity_value | MDF0321 |
| FY2022 | NonCash #1 PUBLICLY TRADED SECURITIES, received 2022-06-03 | 168,195,798 | equity_value | MDF0322 |
| FY2023 (2022-07-01 to 2023-06-30) | ContributorNum 1 DUSTIN MOSKOVITZ | 1,911,246,067 | equity_value | MDF0323 |
| FY2023 | ContributorNum 2 FUTURE OF LIFE INSTITUTE | 161,864 | transfer | MDF0324 |
| FY2023 | NonCash #1 PUBLICLY TRADED SECURITIES, received 2023-06-15 | 1,907,189,117 | equity_value | MDF0325 |
| FY2024 (2023-07-01 to 2024-06-30) | ContributorNum 1 DUSTIN A MOSKOVITZ REMAINDER INTEREST TRUST | 446,082,975 | equity_value | MDF0326 (dup. MDE0110 amount-stripped; MDF0296 amount empty) |
| FY2024 | ContributorNum 2 DUSTIN MOSKOVITZ | 354,990,800 | equity_value | MDF0327 |
| FY2024 | ContributorNum 3 BENEFICIAL AI FOUNDATION | 164,128 | transfer | MDF0328 |
| FY2024 | NonCash #1 PUBLICLY TRADED SECURITIES, received 2024-02-05 | 446,082,975 | equity_value | MDF0329 |
| FY2024 | NonCash #2 PUBLICLY TRADED SECURITIES, received 2024-06-30 | 359,047,750 | equity_value | MDF0330 |
| FY2025 (2024-07-01 to 2025-06-30) | ContributorNum 1 DUSTIN A MOSKOVITZ REMAINDER INTEREST TRUST | 1,395,695,354 | equity_value | MDF0331 |
| FY2025 | ContributorNum 2 BENEFICIAL AI FOUNDATION | 150,027 | transfer | MDF0332 |
| FY2025 | NonCash #1 PUBLICLY TRADED SECURITIES, received 2025-06-30 | 1,395,695,354 | equity_value | MDF0333 (seed MDT0008) |
| FY2020–FY2025 | Part XV vs METR (name / EIN 99-1219864): none found each year | — | — | MDS1011, MDS1012, MDS1013, MDS1014, MDS1015, MDS1016 |
| FY2026 | not yet posted; index_2026.csv has only TAX_PERIOD=202506 | — | calendar closer | MDT0220, MDT0221, MDS0947 |

Within-year differences the rows record but do not reconcile: FY2022 170,486,492 vs 168,195,798; FY2023 1,911,246,067 vs 1,907,189,117; FY2024 contributor 2 354,990,800 vs noncash 359,047,750 (FMV exceeds the total). Every noncash row (MDF0318, 0320, 0322, 0325, 0329, 0330, 0333) has from_entity blank and is tied to its contributor only by ContributorNum in the subject; contributor rows are dated at FY end, noncash rows at ReceivedDt.

GVF's Part XV grants that do exist (Founders Pledge, ARC, Effective Ventures, RAND: MDF0334–MDF0409) are reclassified by MD47 as adjacency (MDP0612, MDP0613, MDP0614): a grant to RAND, EV, FP or ARC is not a documented transaction into METR.

### The crucial negative — no documented transaction from any candidate vehicle into METR

| Vehicle | Sources checked | Rows |
|---|---|---|
| Good Ventures Foundation | 990-PF Part XV FY2020–FY2025 (six objects); metr.org/about | MDS1011–MDS1016, MDS0870, MDS0880, MDP0569 (seed MDS0006 → MDS1275 flagged "unbounded in form") |
| Coefficient Giving / Open Philanthropy | Coefficient staff note 2025: "Note: This organization is not a Coefficient Giving grantee."; coefficientgiving.org/grants (404/redirect) and openphilanthropy.org/grants?q=METR checked 06:09Z, 09:43Z, 12:23Z on 2026-09-16 | MDP0053, MDP0519, MDS0335, MDS0340, MDS1120, MDS1173, MDS1180, MDS1283 (supersedes seed MDS0001), MDS1270, MDS1634 |
| Dustin Moskovitz (individual) | not a METR-named supporter; no payment row exists; METR's own Schedule B is RESTRICTED so nothing can be seen either way | MDR0082, MDE0083, MDS0870, MDS0769 |
| Remainder Interest Trust | not a 990 filer, not an EDGAR registrant, no court or CA registry record — there is no grants schedule to check; its only documented outflows are securities into GVF | MDS0906–MDS0910, MDS0917–MDS0920, MDP0374, MDE0110 |
| Moskovitz Investments LLC, Monster Growth Ventures, CTF Trust, Investment Holdings LLC, 2005 Trust | metr.org/about legal-name count 0; ProPublica 0; no public grants schedule exists | MDS0870, MDS0880, MDS0882, MDP0374 |
| National Philanthropic Trust | Schedule I FY2021–FY2025: none | MDS0186–MDS0190 (seed MDS0007 → MDS1276) |
| Fidelity Charitable | Schedule I FY2021–FY2025: none | MDS0170–MDS0175 |
| **Vanguard Charitable — exception** | Schedule I FY2021–FY2024 none; **FY2025 lists $4,000,000 to METR** (sponsor-level; seed MDF0012; excluded from the ~$71M denominator as filed_grant/prior period MDP0043); no account principal or adviser disclosed | MDF0012, MDP0043, MDS0182–MDS0185, MDS0394–MDS0397, MDS1093, MDS1094, MDS1104, MDS0887, MDE0135 |
| **SVCF — exception** | Schedule I TY2020–TY2023 none; **TY2024 lists $20,000 to METR EIN 99-1219864, purpose Sciences**; adviser not named; dollar match to Tallinn ledger lines noted as a coincidence, not an identification | MDF0011, MDF0220, MDS0191–MDS0193, MDS1095, MDS0398–MDS0400, MDS1146, MDS1105, MDS0886 |
| Anthropic, PBC direct | out of scope (C03.E2); the pack's Anthropic→METR edges are access arrangements, not money | MDR0147, MDR0151, MDR0174, MDP0621 |

The two DAF-sponsor grants are the only documented money into METR from any organisation in this vehicle set. Both are sponsor-level; a figure may neither attach them to any named principal nor state they are unrelated to the donated stake — both are "not stated".

---

## 5. Entity separation (C05.E3)

- Dustin Moskovitz (individual; personal CIK 0001549917, MDS0865) ≠ Good Ventures Foundation (EIN 46-1008520, June 30 FYE, MDE0114) ≠ Open Philanthropy (brand; site now redirects to Coefficient, MDS1622) ≠ Coefficient Giving (brand successor; /grants/ 404, MDS1629) ≠ "our foundation" / "the foundation" / "a nonprofit vehicle" / "his charity" (never identified as a legal entity, MDE0140) ≠ Remainder Interest Trust (trustee Van Loben Sels; not the 2005 Trust; not the Cox 2009 remainder, MDS0902) ≠ Moskovitz Investments LLC ≠ Monster Growth Ventures ≠ CTF Trust ≠ Moskovitz Investment Holdings, LLC (MDE0139). Cari Tuna appears only as a quoted speaker (MDT0240, MDT0243); MDP0536 records the defect of standing "Dustin Moskovitz and Cari Tuna" in for GVF.
- Jaan Tallinn (individual) ≠ Metaplanet (his investment company) ≠ Survival and Flourishing Fund (recommending process; "A recommendation is not a payment") ≠ Survival and Flourishing Corp (PBC; "Our primary client is philanthropist Jaan Tallinn") ≠ Founders Pledge Inc (regrantor, TY2024 990) ≠ FP-US (ledger intermediary) ≠ Silicon Valley Community Foundation (DAF sponsor; adviser not identified) — MDE0063–MDE0068, MDF0218, MDF0219.
- Eric Schmidt ≠ Schmidt Sciences, LLC ≠ The Eric and Wendy Schmidt Fund for Strategic Innovation (EIN 46-3460261) ≠ Hillspire, LLC (MDE0134, MDE0059–MDE0062).
- "individuals from Jane Street" ≠ Jane Street Group, LLC ≠ Jane Street Capital, LLC ≠ Jane Street Global Trading, LLC ≠ the issuer's bare "Jane Street" (MDE0133, MDE0055–MDE0058).
- METR (EIN 99-1219864) ≠ Alignment Research Center (EIN 86-3605182; ARC Evals was a project) ≠ Redwood Research (MDE0053, MDE0132, MDE0136). Anthropic, PBC ≠ the EDGAR name-collision series funds (MDE0054, MDE0111–MDE0113).

---

## 6. The eleven "not a money flow" labellings (C06.E4)

MD47 Task C rows MDP0612–MDP0622 (STATE.md: "eleven explicit adjacency/access labellings bound at primary strength"). Each carries `documented_transaction: no` and the result text "reclassified implied onward-money reading to adjacency [or access arrangement]; documented_transaction not yes; not a cash pipe; not a money flow (C06.E4)":

1. MDP0612 RAND-bound grants/commitments read as Canary/METR receipts (n=170)
2. MDP0613 Effective Ventures / Founders Pledge / DAF-sponsor / TED lines read as METR receipts (n=280)
3. MDP0614 ARC-bound awards read as METR receipts (n=66)
4. MDP0615 SFF / Longview / Open Philanthropy recommendations read as payments (n=73)
5. MDP0616 Audacious/Canary joint commitments read as documented METR receipts (n=78)
6. MDP0617 Anthropic equity / priced-round participation read as METR donations (n=50 — includes every Series A/E/F/G/H, FTX and Hillspire row in §1 and the GVF Schedule B rows in §4)
7. MDP0618 Named-supporter acknowledgments (no amount) read as grants (n=55)
8. MDP0619 Recipient-side unnamed 990 totals read as identified funder pipes (n=30)
9. MDP0620 Partnership/membership listings read as awards (n=165)
10. MDP0621 Lab access / tokens / credits read as cash (n=180; edge_type access arrangement)
11. MDP0622 Jane Street firm / vehicle investment read as METR "individuals from Jane Street" gifts (n=20)

Supporting person-level role edges on the Anthropic side, each labelled "not a money flow (C06.E4)": MDR0168 (Moskovitz observer), MDR0165 and MDR0171 (Tallinn), MDR0155/0156/0172/0184 (Farhi), MDR0158/0169 (Ralston), MDR0164/0167 (Newman), MDR0170 (Field); the Remainder Trust→GVF grouping MDF0991. Entity-distinction corrections MDE0132–MDE0139 are bound to the same element. Final inventory: documented transaction 863, role 103, access arrangement 180, adjacency 153 (MDP0623–MDP0626).

---

## 7. Contradictions and tensions a figure must carry, not resolve

1. "Two board observers by their own account" (posted metr-01b) vs the rows: only Moskovitz is self-described; Tallinn's own words decline a board seat and "observer" is Postimees' sentence (MDP0571, MDR0090, MDR0026).
2. "Up to $7.7B" is 0.8% × $965B — a press bound times a round valuation, a ceiling not a holding (MDP0572, MDT0005/MDT0241, MDR0087).
3. "Good Ventures has no METR grant on its books" is true only through FY2025 (2025-06-30); FY2026 is unfiled (MDP0569, MDS0947).
4. Tuna's "early 2025" sits inside GVF's FY2025 whose Schedule B shows only publicly traded securities; the pack records both and infers nothing (MDT0240, MDF0333).
5. Berger's exclusion of Coefficient/OP is a personal X post ("Views my own"); Coefficient's own pages say nothing about the stake (MDT0239, MDS1623).
6. "GV is itself a beneficiary … via Anthropic" (2026-08-26) names GV but the pack does not resolve "GV" to the 501(c)(3) filer or to the 2025 donation (MDP0702).
7. Vanguard Charitable's FY2025 $4,000,000 and SVCF's TY2024 $20,000 into METR exist; their principals are undisclosed by design (MDF0012, MDF0220, MDS1104, MDS1105).

## 8. Table defects found

- MDE0110 (MD41, entities) duplicates the FY2024 Schedule B contribution with money_type and amount_usd stripped by audit ("lane said money_type=transfer", "lane said amount_usd=446082975"), verdict DIFFERS; MDF0326 (MD39) is the clean equity_value row. MDF0296 (MD41) duplicates MDF0329 with amount deliberately empty.
- Noncash Schedule B rows have blank from_entity (MDF0318, 0320, 0322, 0325, 0329, 0330, 0333); join by ContributorNum, not by amount.
- MDT0242 quote_300 truncated mid-sentence; MDT0239 quote_300 is one sentence of the tweet; MDT0241 contains a soft hyphen; MDT0238/MDP0703 contain HTML entities; MDR0090 is Estonian only.
- MDR0004 / MDE0001 (MD07) are DIFFERS after field audits while MDR0083 / MDE0058 (MD33) are CONFIRMED for the same court line; MDF0213 lost money_type=commitment to audit-1 while seed MDF0015 keeps it.
- MDS1275 / MDS1276 (MD50) supersede seed negatives MDS0006 / MDS0007 but their result field is the audit verdict "unbounded in form", not a bounded negative; cite MDS1011–MDS1016 and MDS0186–MDS0190 instead.
- MDS0853–MDS0860 (MD40) are DIFFERS only because the lane routed source-coverage negatives to the MDE prefix.
- The Series A sentence is promoted four times for Moskovitz (MDR0001 seed, MDR0024, MDR0082, MDR0207) and quoted in MDE0061/0063/0083/0108; cite one evidence row per actor (MDR0080 Tallinn, MDR0082 Moskovitz, MDR0081 Schmidt).
- MDS0001 (seed, superseded) cites a local filesystem path as url; its replacement MDS1283 is public.

## 9. Suggested figures (details in the JSON)

E1 two-lane timeline (investment 2021-05-28 vs statements 2025-10-20 → 2026-08-26; closer 2026-11-16; no transfer marker). E2 statement × "stated / not stated" matrix. E3 vehicle × document exclusion/possibility grid with a "would it name the principal?" column. E4 GVF Schedule B FY2020–FY2025 single-field bars with a "Part XV vs METR: none" strip and an empty FY2026. E5 supporter × Anthropic-tie table naming the entity the source names. E6 entity-separation diagram with no money arrows. E7 the eleven reclassifications as a legend panel.

Standing rules for all of them: equity values are never summed with money flows; no motive language; every inference a caption would need is labelled "not stated"; only public people in public roles; nobody is deanonymised (no DAF adviser, no Jane Street individual).
