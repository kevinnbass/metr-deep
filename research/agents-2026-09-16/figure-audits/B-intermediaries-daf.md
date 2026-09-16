# Figure audit B — Intermediary and pooled money routes, and where public verification stops

Subject: METR (Model Evaluation and Threat Research, Inc., EIN 99-1219864).
Pack: `/mnt/f/projects/anthropic/metr_deep` (read-only). Tables read: `research/funding_events.csv` (MDF), `provenance.csv` (MDP), `source_coverage.csv` (MDS), `timeline.csv` (MDT), `relationships.csv` (MDR), `entities.csv` (MDE); cross-checked against `commitment_reconciliation.csv`, `CLAIMS.md` and `STATE.md` line 313. Companion machine file: `B-intermediaries-daf.json` (same directory) carries every fact/negative row with url, strength, lane and seed-vs-new flags.

Rules applied: no sums across money types; a commitment is not a payment; every legal entity separate (sponsor vs account vs adviser vs donor); no DAF principal inferred; no motive language; only public people in public roles.

---

## 0. How to read the tables before drawing anything

The six CSVs mix five row classes. A figure pipeline must separate them or it will double-count every amount 2–7×.

| Class | How to recognise | What it is |
|---|---|---|
| Seed (S0-seed-import) | note contains `lane=research/grok-out/S0-seed-import.csv`; `checked_utc=2026-09-14T00:00:00Z` | Transcriptions from the 10-metr pack; role=context. Every seed amount used below has an MDnn re-verification row beside it. |
| Lineage import (S2) | note contains `S2-lineage-import` | Transcriptions from the `/anthropic/lineage` pack (e.g. MDF0094–MDF0144 GVF/DAF lines to RAND, FP, EV). |
| Investigation rows (MD01–MD72) | lane `MDnn-...` with a saved primary | This-run live fetches; the facts to cite. |
| MD50 "audit of promoted MDxxxx" | subject begins `audit of promoted` (MDF0467–MDF0925, MDS12xx) | Exact duplicates re-verified 2026-09-16 12:34–13:34Z. Not new facts. |
| MD47 edge-classification | lane `MD47-entity-edge-audit` (MDF0930–MDF1029, MDR0141–MDR0181, MDE0132–MDE0140) | Group promoted row ids under "documented transaction" / "adjacency"; from/to/amount usually blank. Not fact rows. |
| Superseded | note contains `superseded by MDxxxx` | Skip: MDS0001, MDS0006, MDS0007, MDS0008, MDS0214–MDS0221, MDF0068, MDF0076, MDF0077, MDF0155, MDS0151. Caution: the superseding rows MDS1270/1275/1276/1277 are MD50 "unbounded in form" attack records, not fresh negatives; the bounded negatives are MDS0434–0436 (TED Foundation), MDS0186–0190 (NPT), MDS1011–1016 (GVF), MDS1283 (Coefficient). |

`review_verdict=DIFFERS` on many rows (MDF0037, MDF0038, MDF0051–0057, MDF0070, MDF0072, MDF0188–0190, MDP0043 …) records an audit note on one field (`ledger`, `date_precision`, `money_type`), visible as `audit-n 2026-09-16: lane said …` in the note. It is not a disagreement on the amount.

---

## 1. Route: The Audacious Project (housed at TED) → "Canary" (RAND + METR)

Legal entities kept separate: The Audacious Project (a funding initiative, not a Form 990 filer — MDS0980); TED Foundation Inc EIN 82-1934592 (host foundation); TED Conferences LLC; RAND Corporation EIN 95-1958142; METR EIN 99-1219864; "Canary" (a project name, not a legal recipient — MDE0047); Valhalla Foundation EIN 20-0478828; High Tide Foundation EIN 20-1164239; Open Philanthropy EIN 81-0737472 (later brand Coefficient Giving — MDT0215); Good Ventures Foundation EIN 46-1008520 (not "Good Ventures" EIN 45-2757586 — MDT0193).

### 1.1 Proposition P1 — Membership (documented as membership only)

- The Audacious Project is housed at TED; **TED itself does not provide funding for grantees**: Audacious FAQ, live and on the 2024-10-09 Wayback capture (MDP0064, MDP0143). The FAQ does *not* say "partners pay grantees directly" (MDS0366).
- Finalist projects "are presented privately to groups of donors" — not a statement that the whole partner list funds each project (MDP0067).
- Partner list: **46 names** on the 2024-10-09T22:05:22Z capture of audaciousproject.org/about (MDE0041; Webflow Last Published 2024-10-09 13:12 GMT); **60 names** live on 2026-09-16 (MDE0042; Last Published 2026-04-17). No join dates (MDP0129). 14 names were added between the two captures (MDT0038–MDT0051): 10X Better Foundation, AKO Foundation, Arrow Impact, Cheryl and Jahm Najafi Family, Dovetail Impact Foundation, **Good Ventures**, Growald Climate Fund, Jay and Michaela (Mikey) Hoag, Jeff and Marieke Rothschild, Molly and Bill Ford, Skip Foundation, The Just Trust, The Patchwork Collective, The Tepper Foundation. Display-name change Bill & Melinda Gates Foundation → Gates Foundation (MDT0036). Worked example: Good Ventures is listed now and absent from the announcement-day capture (MDP0130).
- The RAND press and METR blog both recite six names as the "funding collective … including the Bill & Melinda Gates Foundation, ELMA Philanthropies, Emerson Collective, MacKenzie Scott, Skoll Foundation, Valhalla Foundation, and more" — cohort-generally, not Canary-specific (MDP0070, MDP0140, MDP0141). High Tide Foundation is on the partners page but not in that boilerplate (MDP0142).
- Per-partner rows MDP0071–MDP0128 (one per live name) each record "membership only; none found in Audacious/TED/RAND/METR Canary issuer pages tying <name> to Canary specifically" and an `On 2024-10-09 capture: True/False` flag (full table in the JSON).
- Bounded negatives for any Canary-specific partner naming: Audacious Canary page (MDS0356), RAND Canary page (MDS0357), TED blog cohort post (MDS0358), METR post (MDS0359), RAND CAST funding page (MDS0360), TED about (MDS0365), sitemap (MDS0364).

Settling document: a per-project partner allocation (grant letters / partners-by-project table) from Audacious/TED — none is published (MDS0364, MDS0418, MDS0420).

### 1.2 Proposition P2 — Project funding (documented as a commitment only)

- RAND press 2024-10-09 (JSON-LD datePublished 2024-10-09T12:00:00Z): "has committed approximately $38 million to RAND and METR for Canary" — MDF0167 (live), MDF0173 (MD17 re-fetch), MDF0194 (MD23), MDP0149 (Wayback 20241009132212id_, unchanged), seed MDF0005, lineage MDF0125.
- METR blog 2024-10-09: "catalyzed approximately $38 million of funding for Canary" — verb is *catalyzed*, not *committed* — MDF0165; Wayback 20241103120028id_ unchanged except "Project Canary" → "Canary" (MDP0148, MDT0119).
- Audacious's own grantee page: collaboration listing, tag 2024, **no dollar amount** (MDF0087, MDP0139, MDS0418, MDS0443, MDS0493, MDS1009); the 2024-11-06 archive likewise (MDP0493). TED blog cohort post: no amount (MDP0492). RAND CAST Canary page: "major philanthropic commitment from The Audacious Project … funding for RAND and METR to jointly pursue"; no amount, no term (MDP0156, MDF0208, MDP0491).
- No term is stated on any announcement page; no split (MDS0419, MDS0420).
- Recon: excluded as a joint-project commitment incompatible with a METR-only denominator (MDP0033, MDP0184, MDP0499); MD50 double-count attack MDP0586.

Settling document: the Audacious/partner grant agreements with RAND and METR (amount, term, payer) — not public.

### 1.3 Proposition P3 — Recipient allocation (documented as METR's quoted allocation; not a payment)

- METR blog 2024-10-09: "Approximately $17 million of this will support work at METR" — MDF0166, MDF0168 (labelled "quoted allocation, not a subtraction"), MDF0170 (MD18), seed MDF0006. Same-day X post 1844005567532245136 (2024-10-09T13:22:41Z): "$17M in new funding" — MDF0171 (fxtwitter mirror of the exact status).
- Beth Barnes, 2025-09-28 (GreaterWrong 200; LessWrong GraphQL postedAt 2025-09-28T20:34:12.755Z): "Audacious funding: This ended up being a bit under $16m, and is a commitment across 3 years" — MDF0169, MDF0172, seed MDF0004; same comment: "The audacious funding was a one-off" (MDP0145) and "Our fundraising goal for the end of 2025 is to raise $10M" (MDP0060).
- RAND never quotes a share (MDS0419); Audacious never quotes a split (MDS0420); the ~$21M remainder is a **subtraction, not a quoted allocation** (MDP0144). METR's about page and 2026-08-14 funding update restate "first institutional-scale funding through The Audacious Project" without amount or term (MDP0146, MDP0147, MDS0449, MDS0450, MDF0223, MDE0069).
- Recon: MDP0034, MDP0035, MDP0500, MDP0501 excluded (date and subset).

Settling document: the Audacious-to-METR grant letter or METR audited financial statements. METR's FY2025 Form 990 (original due 2026-05-15; extended 2026-11-16 — MDS0432 next_document) will aggregate contributions; its Schedule B is RESTRICTED on the public copy.

### 1.4 Proposition P4 — Payment (documented to RAND; bounded negative to METR)

Filed Canary-purpose payments, all to RAND Corporation:

| Payer | Filing | Amount | Purpose as filed | Rows |
|---|---|---|---|---|
| Valhalla Foundation (EIN 20-0478828) | 990-PF TY2024, object 202502559349100000 | $10,000,000 | "PROJECT CANARY, AN ARTIFICIAL INTELLIGENCE SAFETY INITIATIVE"; paid to RAND, 1776 Main Street Santa Monica | MDF0174 (MD17), MDF0149 (MD15), MDF0297 (MD43), seed MDP0001, MDP0046, MDP0158, MDP0467, MDP0512, MDS0437 |
| High Tide Foundation (EIN 20-1164239; ProPublica label "Overlook International Foundation Inc") | 990-PF TY2024, object 202503179349100135 | $333,334 | "To support tTHE PROJECT CANARY" (as filed) — only two paid grants on the return | MDF0175, MDF0148, MDF0298, seed MDP0002, MDP0047, MDP0159, MDP0468, MDP0513, MDS0438 |

Do not infer a three-year $1M pledge from 333,334 (MDF0175 limitation).

Commitment to RAND: Open Philanthropy "gave a gift of $10 million over three years to the RAND Corporation in support of Canary" (award date September 2025) — archived openphilanthropy.org page via Wayback 20251025225511id_; live coefficientgiving.org URL HTTP 404; payment vehicle not named (MDF0176, MDP0160, MDP0489, MDS0808, MDS0488, MDS1010). If paid through Good Ventures Foundation it would appear on GVF FY2026 990-PF (due 2026-11-16, ext. 2027-05-17 — MDT0193) or on OP TY2025 Form 990 (MDT0214).

To METR — none found in every checked filing:
- METR FY2024 Form 990 (short year 2024-05-01 to 2024-12-31; object 202523209349300367): no CANARY/AUDACIOUS string; `AllOtherContributionsAmt` 9,101,611 with no public payer names; `RelatedOrganizationsAmt` 4,501,424 = ARC; Schedule B RESTRICTED (MDS0432). Absence of the string is not proof no Canary dollar sits inside the unnamed remainder.
- TED Foundation Inc 990-PF Part XV TY2022/TY2023/TY2024: no METR, RAND or Canary grant (MDS0436, MDS0435, MDS0434, MDS0479; TY2024 = two grants totalling 100,253). Seed MDS0008 (TY2021–TY2024) is superseded by the MD50 attack MDS1277 ("unbounded in form"); TY2021 is not separately re-checked in a bounded MDS row.
- Valhalla and High Tide TY2024: no METR line (MDS0361, MDS0362); TY2023: no RAND/Canary line (MDS0477, MDS0478).
- Founders Pledge $184,000, SVCF $20,000 and Vanguard $4,000,000 to METR are not Canary-attributed (MDS0439, MDS0440, MDS0441).
- Gates TY2024 990-PF: no METR line (MDS0806, MDS1004); Skoll TY2024: no METR/RAND/Canary (MDS0807, MDS0482).
- RAND Form 990 FY2023/FY2024/FY2025: Canary never named; contributions aggregated; Schedule B RESTRICTED (MDS0474–0476, MDS0485); RAND Schedule I FY2023–FY2025 lists only fellowship grants to individuals — **no onward passage to METR** (MDS0486); every MD17 row carries "Onward passage to METR: none found in this document as of 2026-09-16T07:26:30Z".
- Candid public search (MDS0444), ProPublica org search and full-text search (MDS0447, MDS0448): nothing.
- CAST-list names as Canary payers: Longview USA (MDS1131), Ergo Impact (MDS1138), Fathom Family Foundation — a same-word candidate, not merged (MDS1139), Sentinel Bio (MDS1140), Pew FY2025 no RAND line (MDS0481), Hewlett/Waking Up lines not Canary (MDF0184, MDF0185); ELMA/Emerson not 990 filers under the listed names (MDS0494, MDS1132).

RAND's aggregated contribution lines exist as context only (MDF0188 FY2025: AllOtherContributionsAmt 139,947,770; MDF0189 FY2024: 88,755,931, year-end nine days before the announcement; MDF0190 FY2023: 116,365,040) — never Canary amounts.

Settling document: a partner 990-PF/990 grant line naming METR with a Canary purpose (next TY2025 990-PFs of Valhalla, High Tide, Gates, Skoll: original due 2026-05-15, extended 2026-11-16 — MDT0212, MDT0195, MDT0192, MDT0206; CAL08 MDS1582), or a METR-side receipt (audited FS; an unredacted Schedule B is not a public e-file field).

### 1.5 Proposition P5 — Named partners and their filings

Filings with Canary purpose: **only Valhalla and High Tide, both to RAND** (above).

Other partner filings recovered (none to METR, none Canary):
- Gates Foundation TY2024 990-PF: six paid RAND lines 1,050,000 / 2,368,896 / 564,628 / 273,036 / 700,000 / 99,726 (education/health purposes) — MDF0178–MDF0183 (MD17), duplicated as MDF0299–MDF0304 (MD43); plus an approved-for-future RAND line 1,300,000 K-12 EDUCATION with blank money_type (MDF0305; MD47 classes it adjacency, MDF0994). Bounded negative on Canary purpose: MDS0480.
- Skoll Foundation TY2024 990-PF: 650,000 paid to **TED FOUNDATION INC**, purpose AUDACIOUS PROJECT (MDF0311; MDP0469) and an expenditure-responsibility grant 2,250,000 to TED FOUNDATION INC dated 2022-11-04 (MDF0312; MDP0474) — payments to the host foundation, not to Canary/RAND/METR.
- Samueli Foundation 450,000 to CLEAN SLATE INITIATIVE "PART OF AUDACIOUS PROJECT" (MDF0313); Rippleworks 5,000,000 to INKOMOKO "TO BE USED AS PART OF THE AUDACIOUS PROJECT" (MDF0316) — other Audacious grantees.
- MacArthur 300,000 to CANARY MEDIA INC and 50,000 to Business Capacity Development Alliance "IN SUPPORT OF THE CANARY IMPACT FUND" (MDF0314, MDF0315) — different legal entities with "Canary" in the name; SVCF and Vanguard schedules also carry "Canary Fund", "Canary Media Inc", "Canary Impact Lab Inc" recipients (MDS0440, MDS0441).
- Latest retrieved 990/990-PF grant schedules with no Canary/METR/RAND/Audacious line: 10X Better (MDS0981), Additional Ventures (0982), Anne Wojcicki Foundation (0983), Arrow Impact (0984), Climate Lead (0985), Crankstart (0986), Dovetail (0987), Growald (0988), James Family (0989), Lyda Hill (0990), Oak (0991), Robertson (0992), Science Philanthropy Alliance (0993), Seadream (0994), Someland (0995), Bridgespan (0996), Just Trust (0997), Tepper (0998), Virgin Unite (0999), Open Philanthropy TY2024 (no Schedule I; MDS1000), Overdeck (MDS1001). Joe and Clara Tsai Foundation TY2025 XML in index but not retrievable (MDS1002 — search failure). Good Ventures FY2025 XML unreadable in MD17 (MDS0484, MDS1003) but readable from IRS bulk zip in MD39 (MDS1016: 565 rows, no METR).
- Not 990 filers under the listed name: MacKenzie Scott, Novogratz, Ford, Blecharczyk, Simons/Baxter-Simons, Hastings/Quillin, Jurvetson (MDS0960–0966); Acton Family Giving, AKO, Ballmer Group, CIFF, Dalio, Delta, ELMA, Emerson Collective, Pivotal Ventures, Quadrature, Sea Grape, Skip, Patchwork Collective, The Audacious Project itself (MDS0967–0980). The pack does not deanonymize vehicles.

### 1.6 Figure notes for this route

Four panels, four source classes; commitment arrows never become payment arrows. Show ~$38M (joint, 2024-10-09), ~$17M (METR-quoted, 2024-10-09) and "a bit under $16m / 3 years" (2025-09-28) as three dated statements, never summed or substituted; label the ~$21M as a subtraction if drawn at all. Payments: $10,000,000 Valhalla and $333,334 High Tide (filed, to RAND); $10,000,000 OP (commitment, to RAND). METR panel: bounded negative with the checked-filings list and calendar closers. Partner panel: set diagram 46 → 60 names, 14 adds, six boilerplate names, two names with Canary filings (both to RAND).

---

## 2. Route: Donor-advised fund sponsors

Sponsors (legal payers): Vanguard Charitable Endowment Program (EIN 23-2888152, June FYE); Silicon Valley Community Foundation (EIN 20-5205488, calendar); Fidelity Investments Charitable Gift Fund (EIN 11-0303001, June); National Philanthropic Trust (EIN 23-7825575, June; public charity — MDE0093); Donor Advised Charitable Giving Inc (EIN 31-1640316, June; Schwab Charitable Fund / DAFgiving360). Kept separate from any DAF account, adviser or account principal (MDE0135) and from the recipient charities METR (99-1219864) and Alignment Research Center (86-3605182).

### 2.1 What each sponsor filed to METR

| Sponsor | Years checked (Schedule I) | METR line | Rows |
|---|---|---|---|
| Vanguard Charitable | FY2021–FY2025 | **FY2025 (2024-07-01 to 2025-06-30): $4,000,000, RecipientTable[15424], MODEL EVALUATION AND THREAT RESEARCH, EIN 99-1219864, "FOR RECIPIENT'S EXEMPT PURPOSE"** | MDF0038, MDF0154, MDF0206, MDF0211, seed MDF0012; MDP0043, MDP0482, MDP0509; negatives MDS0182–0185, MDS0394–0397, MDS1093, MDS1094 |
| SVCF | TY2020–TY2024 | **TY2024: $20,000, Model Evaluation and Threat Research, EIN 99-1219864, purpose "Sciences"** | MDF0037, MDF0062, MDF0153, MDF0205, MDF0212, MDF0220, MDF0418, seed MDF0011; MDP0042, MDP0508; negatives MDS0191–0193, MDS0398–0400, MDS1095, MDS1146 |
| Fidelity Charitable | FY2021–FY2025 (+ FY2022 amended) | none | MDS0170–MDS0175 |
| National Philanthropic Trust | FY2021–FY2025 | none | MDS0186–MDS0190 (seed MDS0007 superseded by attack MDS1276) |
| Donor Advised Charitable Giving Inc (Schwab) | FY2020–FY2025 (+ TY2021 two-day return) | none | MDS1092, MDS0176–MDS0181 |

Purpose classification: Vanguard "unrestricted" (MDP0180; MDS0514 — still a filed_grant outside the commitment type); SVCF "programme-restricted" (Sciences is a Schedule I category, not a project title — MDP0179, MDF0205). Neither is Canary-attributed (MDS0440, MDS0441). METR names neither sponsor on its about page (MDP0167, MDP0168).

Provenance caveat on the Vanguard $4,000,000: XML object 202621329349306657 is absent from the GivingTuesday lake (HTTP 404: MDS0223, MDS1118, MDS1183) and from IRS zip 2026_TEOS_XML_05A although index_2026 lists it; ProPublica download-xml returns 403 (MDS1119); the live Schedule I page was a JS shell in one fetch (MDP0043) and the METR row was re-verified on the ~105 MB full_text stream in another (MDP0509, SHA-256 e1abfc49…). MD50 records this as an open gate correction: "Vanguard Charitable FY2025 $4,000,000 XML was not recovered from GT/IRS zip; recon still cites a seed-held amount" (MDP0593, MDP0600). A figure should carry the flag.

Sponsor grants to Alignment Research Center (not METR; adjacency per MDP0614): SVCF TY2023 $1,401,000 and TY2024 $50,450 (MDF0040, MDF0041/MDF0063); Vanguard FY2023 $201,000, FY2024 $1,000,000, FY2025 $1,500,000 (MDF0042–MDF0044); Fidelity FY2024 $100,000 (MDF0039). Principal undisclosed on each (MDS1106–MDS1111).

Sponsor grants to RAND (not METR; not Canary — Route 5): NPT FY2025 $61,646,790 "CULTURE & ARTS" (MDF0186/MDF0118), FY2023 $11,000 (MDF0108); Fidelity FY2025 $18,202,491, FY2024 $269,475, FY2023 $423,764 (MDF0187/0119, MDF0115, MDF0110); Schwab FY2025 $4,858,600, FY2024 $581,200, FY2023 $575,700 (MDF0417/0120, MDF0116, MDF0106); Vanguard FY2025 $12,000, FY2024 $48,000, FY2023 $175,500 (MDF0121, MDF0113, MDF0109); SVCF TY2024 $2,000,000 (MDF0117); Goldman Sachs Philanthropy Fund and American Endowment Foundation small lines (MDF0107, MDF0112, MDF0111, MDF0114).

### 2.2 Sponsor-to-sponsor flows (NOT METR money)

MD38 collected 56 Schedule I lines in which one of the five sponsors grants to another (MDF0240–MDF0295; each has an MD50 duplicate at row id + 463). The filing names the recipient sponsor and `CashGrantAmt`; it has no account-principal, donor or adviser field, so a grant that moves an account family is not labelled as such (MDF0240 limitation). Fiscal periods differ (SVCF calendar; the others July–June), so any matrix must be labelled per filer period.

| From → To | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| SVCF → Fidelity | 153,756,594 (MDF0240, TY2023) | 51,869,044 (MDF0244, TY2024) | — |
| SVCF → NPT | 7,196,356 (MDF0241) | **1,591,322,838** (MDF0245) | — |
| SVCF → DACG | 27,471,026 (MDF0242) | 5,824,989 (MDF0246) | — |
| SVCF → Vanguard | 1,102,097 (MDF0243) | 786,994 (MDF0247) | — |
| Vanguard → Fidelity | 59,069,369 (MDF0248) | 25,171,927 (MDF0252) | 87,288,229 (MDF0292) |
| Vanguard → NPT | 1,414,505 (MDF0249) | 8,594,628 (MDF0253) | 31,579,852 (MDF0293) |
| Vanguard → DACG | 15,205,207 (MDF0250) | 29,603,374 (MDF0254) | 46,308,571 (MDF0294) |
| Vanguard → SVCF | 1,448,500 (MDF0251) | 453,000 (MDF0255) | 81,000 (MDF0295) |
| Fidelity → NPT | 194,975,525 (MDF0256) | 153,263,488 (MDF0260) | 346,816,520 (MDF0265) |
| Fidelity → DACG | 183,131,878 (MDF0257) | 100,913,919 (MDF0261) | 117,840,716 (MDF0267) |
| Fidelity → SVCF | 15,669,854 (MDF0258) | 29,017,360 (MDF0262) | 147,537,286 (MDF0266) |
| Fidelity → Vanguard | 10,634,088 (MDF0259) | 21,738,778 (MDF0263) | 480,068,133 (MDF0264) |
| DACG → Fidelity | 120,864,512 (MDF0268) | 127,700,997 (MDF0273) | 976,570,217 (MDF0276) |
| DACG → Vanguard | 26,383,102 (MDF0269) | 4,051,608 (MDF0274) | 8,657,300 (MDF0278) |
| DACG → NPT | 14,713,511 (MDF0270) | 249,117,686 (MDF0272) | 161,539,525 (MDF0277) |
| DACG → SVCF | 992,325 (MDF0271) | 519,200 (MDF0275) | 2,402,317 (MDF0279) |
| NPT → Fidelity | 63,245,404 (MDF0280) | 242,538,360 (MDF0285) | 284,919,786 (MDF0289) |
| NPT → DACG | 76,791,161 (MDF0281) | 72,074,515 (MDF0284) | 43,578,702 (MDF0288) |
| NPT → SVCF | 257,077,976 (MDF0282) | 366,362,375 (MDF0286) | 265,751,500 (MDF0290) |
| NPT → Vanguard | 1,347,243 (MDF0283) | 17,680,162 (MDF0287) | 3,447,704 (MDF0291) |

SVCF's audited statements describe the movement generically: grants of $1,667,000,000 (2024) and $207,000,000 (2023) "transferred to other donor-advised fund sponsors" (MDF0237, MDF0238) and gifts of $500,000,000 (2024) and $325,000,000 (2023) "transferred from other donor-advised fund providers" (MDF0239; MDP0447). These are a different money_type (`transfer`, rounded to millions) from the Schedule I `filed_grant` lines and must not be summed with them. Receiving/sending sponsor and account family are unnamed.

### 2.3 The explicit statement: no public filing discloses the account principal

- IRS Schedule I Part II columns are (a) name/address (b) EIN (c) IRC section (d) cash (e) non-cash (f) valuation method (g) description (h) purpose — no donor/adviser/account-principal column; "public verification stops at the DAF sponsor legal entity and the recipient row" (MDS0594, quoting irs.gov f990si.pdf).
- Schedule B Part I names contributors *to the sponsor*, is RESTRICTED on every public e-file checked (SVCF MDS1150; Vanguard MDS1151, MDS0593; NPT FY2021–FY2025 MDP0329–0333, MDS0840–0844), and even unredacted would not name the account that recommended a listed grant (MDS0886–MDS0890, one row per sponsor, each with the "document that would identify a principal if it existed" named: an unredacted DAF account ledger/statement or a Schedule I adviser column that does not exist).
- No adviser name on any sponsor Schedule I for a METR grant (MDS0099, MDS1082); the SVCF $20,000 must not be identified with the Tallinn ledger's two $10,000 lines by amount-matching (MDS1082, MDE0028, MDF0062, MDF0220).
- NPT is a public charity; 26 U.S.C. §6104(d)(1) opens its return, §6104(d)(3)(A) excepts contributor names/addresses (MDP0320, MDP0321); NPT's Schedule O says the 990 is available on request (MDP0328); an unsent §6104(d) draft exists, `approved_for_send=false`, USER_AUTHORITY_WAIT (MDP0370; MDS0899).
- MD47/MD50 standing corrections: "Sponsor filing identity is not the account principal; advisers and private donors are not deanonymized" (MDE0135); "Public Schedule B contributor identities are restricted; DAF sponsor Schedule I has no adviser/principal field" (MDP0606). STATE.md line 313: "A DAF sponsor's return never names an account principal".
- Posted figure metr-17 ("The Vanguard channel: … grew from $8M to $66M … no filing says whose it is") is adjudicated defective (MDP0542: sponsor adjacency used as a channelled flow from an unidentified principal) and incomplete (MDP0580: cluster totals are not promoted rows).

### 2.4 DAF sponsors as payers into other intermediaries (context, transfers)

Founders Pledge Inc 990-PF Schedule B institutional contributors: SVCF $1,702,000 (TY2023, MDF0421) and $1,000,000 (TY2020, MDF0435); Fidelity $511,736 / $1,440,450 / $483,750 / $175,000 / $6,000 / $40,000 / $50,000 (MDF0156, MDF0424, MDF0432, MDF0436, MDF0438–0440); Vanguard $34,273 / $177,685 / $325,000 (MDF0419, MDF0426, MDF0430); Schwab $114,101 / $14,079 (MDF0420, MDF0428); Bank of America Charitable Gift Fund $7,500 (MDF0423). Every.org 990-PF contributors: Fidelity $1,014,836 (TY2023, MDF0161), $425,000 (TY2024, MDF0442), $158,314 (TY2021, MDF0448); Schwab $210,115 / $56,600 (MDF0443, MDF0449); Vanguard $50,075 / $31,480 / $5,500 (MDF0444, MDF0450, MDF0453). Every.org's TY2023 Part XV has no METR line (MDF0161 limitation); METR's donate page says every.org donations are re-granted as batched unrestricted donations (MDP0168) — a recipient-channel statement, not Vanguard's purpose. None of these chain to METR (MDP0613 classes 280 such rows as adjacency).

### 2.5 Calendar closers

Vanguard, Fidelity, NPT, DACG FY2026 (FYE 2026-06-30) due 2026-11-16 (MDT0024–MDT0026, MDT0057, MDT0230, MDS1581, MDS1583); SVCF TY2025 absent from index_2026, treat as extended to 2026-11-16 (MDT0027, MDS0948, MDT0179).

---

## 3. Route: Coefficient Giving / Open Philanthropy / Good Ventures Foundation / Alignment Research Center

Entities: Open Philanthropy (files as OPEN PHILANTHROPY, EIN 81-0737472; brand now Coefficient Giving; not merged with Coefficient Giving Advisors Inc EIN 99-2255770, Action Fund 81-2644663, Policy Fund 39-4232601 — MDT0215); Good Ventures Foundation (EIN 46-1008520, June FYE — MDE0114); "Good Ventures" EIN 45-2757586 (different, 0 index rows — MDT0193); Dustin Moskovitz (individual) and DUSTIN A MOSKOVITZ REMAINDER INTEREST TRUST (GVF Schedule B contributor) — not merged with any foundation (MDE0139, MDE0140); Alignment Research Center (EIN 86-3605182) — a related tax-exempt organisation on METR's Schedule R with ControlledOrganizationInd=0, not a parent (MDR0020, MDE0132, MDP0537).

### 3.1 Bounded negative: no grant to METR

- GVF 990-PF Part XV `GrantOrContributionPdDurYrGrp`, one bounded row per year: FY2020 (108 rows, MDS1011), FY2021 (MDS1012), FY2022 (MDS1013), FY2023 (MDS1014), FY2024 (493 rows, MDS1015), FY2025 (565 rows, from IRS bulk zip 2026_TEOS_XML_05B, MDS1016; ProPublica render MDS1165). Zero METR name/EIN hits. METR formed May 2024, so years ending before 2024-05-01 cannot list its EIN.
- Open Philanthropy TY2024 Form 990 (object 202503209349301300): no Schedule I (MDS1000).
- Coefficient grants catalog: `/grants` redirects to a closed Grants Associate job posting; `/grants/` HTTP 404; grant permalinks 404; CDX for `coefficientgiving.org/grants/*metr*` empty; legacy `openphilanthropy.org/grants/?q=METR` redirects to Coefficient Funds (MDS0021, MDS0299, MDS0309, MDS0335, MDS0340, MDS1120, MDS1173, MDS1180, MDS1283, MDS1629, MDS1634, MDS0104). Seed MDS0001 (local-path snapshot, 2,911 rows) superseded by MDS1283 (public URL).
- Coefficient staff donor-suggestions page (2025): "Note: This organization is not a Coefficient Giving grantee." (MDP0053, MDP0519).
- Alexander Berger (CEO, Coefficient Giving) on X, 2025-12-18: "Open Phil never invested in Anthropic, dustin did early on … He's since donated his stake (and not to us)" (MDT0006 seed; MDT0239 live).
- Posted figure metr-18 ("no direct Coefficient grant to METR in checked index/filings; ARC program transfer and Coefficient award to RAND partner exist") adjudicated **accurate** (MDP0581).
- Closers: GVF FY2026 990-PF (FYE 2026-06-30) due 2026-11-16, extension 2027-05-17 (MDT0193, MDT0165, MDT0180, MDT0221, MDS1577, MDS0947); OP TY2025 990 due 2026-05-15, ext. 2026-11-16 (MDT0214, MDT0215).

### 3.2 ARC-era awards (2022) — to ARC, not METR

| Money type | From | To | Amount | Date/period | Rows |
|---|---|---|---|---|---|
| recommendation | Open Philanthropy | Alignment Research Center | $265,000 general support | March 2022 | MDF0066 (Wayback 20240620191457id_ of withdrawn OP page), MDP0485 |
| filed_grant | Good Ventures Foundation | ALIGNMENT RESEARCH CENTER | $265,000 GENERAL SUPPORT | FY2022 (2021-07-01 to 2022-06-30) | MDF0335 |
| recommendation | Open Philanthropy | Alignment Research Center | $1,250,000 over two years, general support | November 2022 | MDF0067, MDP0486 |
| filed_grant | Good Ventures Foundation | ALIGNMENT RESEARCH CENTER | $1,250,000 RESEARCH RELATED TO AI ALIGNMENT | FY2023 (2022-07-01 to 2023-06-30) | MDF0337 |
| paid_grant | FTX Foundation | ARC | $1.25M received 2022; set aside; returned to the FTX estate in 2024 | 2022 / 2024 | MDF0069, MDP0019, MDT0032, MDP0487 |

The pack keeps each OP recommendation and each same-dollar GVF filed line on separate money_types and explicitly says the filed line "is not this recommendation" (MDF0335/MDF0337 notes); a figure may pair them as columns but must not merge them. The live OP grant URL redirects to a Coefficient fund page (MDS0257). Other ARC funders on record (all ARC, not METR; MDP0614 adjacency): SFF-2022-H2 $2,179,000 and SFF-2023-H1 $3,247,000 recommendations (MDF0050/0415, MDF0049/0088/0210), FLI $1,401,000 (MDF0084), LTFF $72,000 (MDF0085), FP 990-PF $2,179,000 (TY2022) and $1,846,000 (TY2023) and Schedule I $147,000 (TY2024) (MDF0061, MDF0060, MDF0059), Tallinn ledger lines to ARC (MDF0054–MDF0057), DAF sponsor lines (§2.1). ARC Schedule B identities RESTRICTED (MDS0249).

### 3.3 The 2024-04-30 spin-out transfer ARC → METR (documented; one event, three filed figures)

- ARC FY2024 Form 990 (EIN 86-3605182; object 202513219349323246; extracted from IRS zip 2025_TEOS_XML_11D; GT copy sha256-identical), Schedule I to MODEL EVALUATION AND THREAT RESEARCH INC, EIN 99-1219864: `CashGrantAmt` **4,477,169** (MDF0064, MDF0207) and `NonCashAssistanceAmt` **76,766** COMPUTERS at BOOK (MDF0065, typed in_kind_estimate); `PurposeOfGrantTxt` PROGRAM SPIN-OFF; no restriction text (MDP0016); Part I line 2: "ENTITY GRANTED TO IS THE SPIN-OFF OF ARC'S EVALUATIONS PROGRAM AND ASSOCIATED GRANTS ARE DECIDED UPON AND TRANSFERRED ACCORDING TO A GRANT AGREEMENT" — agreement not attached, binaryAttachmentCnt=0 (MDP0014).
- Schedule N: `DistributionDt` **2024-04-30**, `FairMarketValueOfAssetAmt` 4,553,935 (= cash + non-cash; "PROGRAM ASSETS AND LIABILITIES AS ON BOOKS ON THE DATE OF TRANSFER"), successor EIN 99-1219864 (MDT0030, MDT0228); Schedule R type B InvolvedAmt 4,553,935 and Part III GrantAmt 4,553,935 are the same disposition (MDT0229). Seed MDF0007 carries 4,553,935.
- Part III narrative: "PRIOR TO COMPLETING THE SPIN OUT IN MAY" — a different filed string from Schedule N (MDT0229).
- METR FY2024 Form 990 (short year 2024-05-01 to 2024-12-31): `RelatedOrganizationsAmt` **4,501,424**; Schedule R type C InvolvedAmt 4,501,424 FAIR MARKET VALUE from ALIGNMENT RESEARCH CENTER; also loan-type D 325,431 and type E 490,182 (not grants) (MDF0034, MDP0032, MDS0587); METR has no Schedule I (MDS1112); DonorRstrOrQuasiEndowmentsInd=0 (MDP0169).
- ARC donor-restricted net assets 1,146,000 → 0 in FY2024; the return does not tie this to the transfer and 1,146,000 is not the FTX 1,250,000 (MDP0017). AllOtherContributionsAmt 5,219,333 with no named payer; the transfer "cannot be attributed to any single ARC funder" (MDP0015).
- Organisational-separation dates are distinct from the distribution date: 2023-09-19 spin-out announcement (MDT0028), 2023-12-04 METR named (MDT0029), ARC donate page stamp 2023-03-06 (MDT0031); ARC FY2023 Schedule I has no METR line (MDS0262).
- Double-count attack MDP0587: 4,501,424 vs 4,477,169 + 76,766 "are different filed figures, not two payments". The posted "$4.55M" is the cash + in-kind sum the pack's rule forbids (MDP0570).
- **Note defect**: MDF0064's note says "the $47,511 difference is not attributed"; the actual differences are 4,501,424 − 4,477,169 = 24,255 and 4,553,935 − 4,501,424 = 52,511.

### 3.4 The "firewall" claim — undetermined

MDP0568 (CLAIMS.md B16): New York Post, 2026-09-15 — "In the case of Moskovitz's donation to ARC in 2022, the official said the funding was firewalled and not used for METR's operations." Status: undetermined. No promoted row states a firewall. The 2022 ARC money on record is the OP recommendations / GVF filed grants above, not a personal Moskovitz gift (entity unmerge MDE0139/MDE0140). The journalist's $1,515,000 (265,000 + 1,250,000) is not the official's sentence and is not summed by the pack. Schedule I purpose PROGRAM SPIN-OFF carries no restriction text (MDP0016); METR's return shows no donor-restricted endowments (MDP0169); ARC's restricted net assets fell 1,146,000 → 0 in the transfer year without an explanatory line (MDP0017).

**What would settle it**: an ARC or METR instrument stating that the 2022 Open Philanthropy/Good Ventures awards to ARC were excluded from METR operations and from the 2024-04-30 program transfer — the ARC–METR spin-out grant agreement named in ARC Schedule I Part I line 2 (not in the e-file), an OP/GVF grant letter with a use restriction, or an ARC audited-statement note explaining the FY2024 change in donor-restricted net assets.

### 3.5 Coefficient/OP award to METR's Canary partner

OP $10,000,000 over three years to RAND "in support of Canary" (award date September 2025) — commitment, not a filed line; page names METR only as collaborator, not payee (MDF0176, MDP0160, MDP0489, MDS0808, MDE0137 — the archived text continues "This gift was recommended by Trevor…", a public program-officer role). GVF FY2023/FY2024 RAND lines (four and five) are all GENERAL SUPPORT, none Canary (MDS0483; amounts MDF0094–MDF0102, triplicated as MDF0359–0362/0388–0392 and MDF0306–0310); FY2025 RAND lines (MDF0103–0105; MDF0407–0409) purpose text unread in MD17 (MDS0484) but the FY2025 return was later grant-scanned for METR (MDS1016).

### 3.6 Moskovitz stake statements (context only; not a METR route)

Forbes 2025-11-10: Anthropic stake "moved into a nonprofit vehicle in early 2025" (MDT0004); Forbes 2026-04-20: "less than 0.8%" donated "last year" (MDT0005); Moskovitz on Bluesky 2026-03-30: "Our Anthropic shares are entirely in our foundation" (MDT0007; also MDT0234–MDT0237); Berger 2025-12-18 (MDT0239). GVF Schedule B FY2020–FY2025 lists only PUBLICLY TRADED SECURITIES as non-cash property (MDF0317–MDF0333; MDT0008). Posted figure metr-01b's "$7.7B" is a ceiling, adjudicated incomplete (MDP0572). These do not touch METR's money routes; posted figures that pipe Moskovitz/Coefficient "through" ARC/RAND/pooled funds to METR are adjudicated defective (MDP0532, MDP0536, MDP0537, MDP0538, MDP0539, MDP0543).

---

## 4. Route: Longview Philanthropy, Effektiv Spenden, Survival and Flourishing Fund, Founders Pledge

Entities: SFF (recommendation vehicle; not a payer — MDR0029) vs Survival and Flourishing Corp (PBC; for-profit grants — MDE0029, MDE0066) vs Jaan Tallinn (individual; funder column; public ledger jaan.online); Founders Pledge Inc (US filer EIN 37-1795297) vs Founders Pledge Ltd (UK 08565148) vs Founders Pledge gGmbH (MDE0046, MDF0159, MDF0422); Longview brand vs Longview Philanthropy USA Inc (EIN 93-2664730; first US return TY2024) vs Longview Inc. Ltd (UK 14444004) (MDE0131, MDE0032, MDE0045); Giving What We Can (donation processor for the Emerging Challenges Fund — MDR0027, MDE0031); Effektiv Spenden brand vs UES – Gemeinnützige GmbH für effektives Spenden / Effektiv Spenden Schweiz (MDE0034, MDR0028). The 2023 Longview and Effektiv Spenden lines name ARC Evals, a project of Alignment Research Center, before METR Inc existed (formed May 2024) (MDE0035, MDE0132).

### 4.1 Three columns, kept apart

| Route / round | Recommendation | Paid (funder self-statement) | Filed (990) |
|---|---|---|---|
| SFF-2024 (funder Jaan Tallinn; recipient Model Evaluation and Threat Research, Inc.; general support) | **$204,000**, of which ($20,000)† is a speculation-grant annotation inside the total, not extra (MDF0047, MDF0075, MDF0079, MDF0198, MDF0215, seed MDF0008; MDP0011) | Tallinn ledger: **$10,000** 2024-07-23 and **$10,000** 2024-07-24 via "SFF-spec" (MDF0051, MDF0052, MDF0221, MDF0222, MDF0412); **$184,000** 2024-12-06 via "FP-US" (MDF0053, MDF0218; MDF0199) | Founders Pledge Inc TY2024 Schedule I **$184,000** to MODEL EVALUATION AND THREAT RESEARCH INC, "FUND CHARITABLE ACTIVITIES" (MDF0058, MDF0152, MDF0203, MDF0219, seed MDF0010) |
| SFF-2025 | **$120,000** remainder (MDF0045, MDF0074, MDF0080, MDF0196, MDF0216) **+ {$428,000}‡ matching pledge** at 1x, conditional on outside donations through 2026-09-30 (MDF0046, MDF0197, MDP0185 typed recommendation; MDF0081, MDF0217 typed commitment); track total $548,000; ($120,000)† speculation is an annotation (MDP0010); seed MDF0009 stores "120000 + 428000 matching pledge" | none on the ledger for the remainder or the match (MDS0232) | none yet; FP/SVCF TY2025 returns are calendar closers (MDS0235) |
| SFF-2025 further-opportunities page (Last Published 2025-02-15) | METR row with $220,000 and $1,210,000 columns — a different SFF figure, not summed, excluded (MDF0093, MDP0040) | — | — |
| Longview public fund 2023 | **$220,000** "from its public fund in 2023" to ARC Evals (now METR): GWWC-hosted Longtermism Fund August 2023 grants report (MDF0070, MDF0200), GWWC charity page quote (MDF0082, MDF0071, MDF0201, seed MDF0013); Longview's own catalog object slug arc-evaluations dated 2023-09-25 has no amount (MDP0478); ECF page: "All funds are disbursed based on recommendations by Longview Philanthropy" (MDP0022); Dec-2023 ECF report does not list METR (MDP0025) | none recovered | none: Longview USA Inc TY2024 Schedule I five domestic grantees, none METR/ARC (MDS0266, MDS1083); Schedule F three unnamed Europe grants 504,714 / 262,000 / 126,000 (MDS0267, MDS1084); Longview Inc. Ltd accounts image-only (MDS0268, MDS0403); no US e-file before TY2024 (MDS1147); GWWC USA TY2024 pays Longview USA $843,128, not METR (MDS1088, MDR0135) |
| Effektiv Spenden Giving Fund "Safeguarding the future", H1/2023 | — | **128.000 EUR** regrant to METR (formerly ARC Evals), "Grants were made in August 2023" (MDF0072, MDF0202, MDF0461, seed MDF0014; German blog: ARC Evals 128.000 € following Longview's recommendation — MDF0073); typed regrant per the fund's own words (MDP0024); never converted to USD (MDP0045, MDP0483) | none: UES gGmbH Jahresabschluss 2023/2024 reports aggregate "Weitergeleitete Spenden" −11,765,151.77 EUR with no grantee names (MDS1085); live site Cloudflare 403 (MDS0273, MDS0314, MDS0520, MDS1178) |
| Comparison (to ARC, not METR): SFF-2022-H2 | $2,179,000 (MDF0050, MDF0415) | Tallinn 2022-12-20 FP-US $2,179,000 (MDF0057) | FP TY2022 990-PF $2,179,000 to ARC (MDF0061) — the cleanest rec→paid→filed triple in the pack |

Arithmetic the pack notes but does not merge: $184,000 = $204,000 − $20,000 (the speculation lines already disbursed) (MDF0053). Seven promoted rows carry 184000 across filed_grant and paid_grant; adding the ledger line to the 990 line counts one dollar amount twice (MDP0588; MDP0484).

Founders Pledge grantee page: METR "first funded April 2024", programme purpose ("development of autonomous capability evaluations … time horizons"), no amount, incomplete-list disclaimer (MDF0086 typed paid_grant; MDF0204 typed filed_grant; MDP0494). See contradiction C1.

Founders Pledge as regrantor: named institutional payers-in on its 990-PF years — DAF sponsors (§2.4), Every.org $1,246,087 / $525,370 / $586,327 (MDF0157, MDF0425, MDF0431), Effective Ventures Foundation $1,060,136 (MDF0158), Founders Pledge Ltd $3,138,047 / $69,524 and gGmbH $449,412 / $6,981 (MDF0159, MDF0427, MDF0422, MDF0433), OPEN PHILANTHROPY PROJECT $1,000,000 (2021, MDF0429), GOOD VENTURES FOUNDATION $1,000,000 (2021) and $1,500,000 (2020) (MDF0434, MDF0437); GVF Part XV filed grants to FP $1,500,000 FY2021, $1,000,000 FY2022, $250,000 FY2025 (MDF0126/MDF0334, MDF0127/MDF0336, MDF0406/MDF0457). FP TY2024 total revenue $144,636,466 (MDF0459; supersedes MDF0155). None of these chain to METR (MDP0613). FP also filed $1,000,000 to THE RAND CORPORATION in TY2024 (MDF0177/MDF0122) and $147,000 to ARC (MDF0059/MDF0413). FP TY2020–TY2023 have no METR line (MDS1143, MDS0390–0392); TY2025 absent from index (MDS0417; MDT0053).

Tallinn → RAND (SFF-2025): $1,000,000 recommendation + $22,000 matching pledge, "General support of Technology and Security Policy Center" (CAST's predecessor) — not Canary, not a payment (MDF0124, MDF0123, MDS0495).

### 4.2 How METR names these routes

metr.org/about: "pooled funds such as those of Longview Philanthropy and Effektiv Spenden; recommendations by the Survival and Flourishing Fund" — no amounts (MDP0020, MDP0013, MDF0230, MDF0231, MDP0727–MDP0729). First appearance of the three names in the about-page funding paragraph: capture window 2025-12-03 to 2025-12-07 (MDT0082–MDT0087) — page appearance, not a payment date.

### 4.3 Bounded negatives specific to this route

SFF older rounds (2019–2023-H2) name no METR/ARC recommendation beyond those above (MDS0225–0231); SFF-2026 not published (MDS0337, MDS1121, MDS1176, MDS1073); no SFC/FLI/court/USAspending/California registry/GuideStar/press record of an SFF payment to METR (MDS0234, MDS0236, MDS1074, MDS0240–0243, MDS1075–1081); METR FY2024 Schedule B names no SFF/Tallinn/Longview/FP/Every.org/EV contributor (MDS0238, MDS0270, MDS0415, MDS0769); ARC TY2023 names no Longview/ES/GWWC payer (MDS1086); Longview Frontier AI Fund (private) aggregates 18 organisations Dec 2024–Sep 2025, METR not named (MDS0265); Tallinn ledger has no METR disbursement in the Feb–Aug 2026 window (MDS1117).

Settling documents: SFF-2025 — a TY2025 Schedule I line from the legal payer (FP Inc, SVCF or other sponsor) naming METR, or SFF's grant letter (MDS0245); the match outcome after 2026-09-30. Longview — a Longview USA Inc / Longview Inc. Ltd grant-schedule line, GWWC payment record, or METR/ARC receipt (MDP0022). Effektiv Spenden — a UES gGmbH grant schedule/agreement naming METR/ARC Evals and EUR 128,000, or a receipt in EUR for August 2023 (MDP0024).

---

## 5. Route: RAND Corporation as Canary co-recipient

- Legal recipients named by RAND and METR: RAND and METR, unmerged; Ella Guest (RAND) and Beth Barnes (METR) named as Canary leads in public roles; "will each contribute" is not a dollar split (MDR0030, MDR0205, MDE0047). RAND CAST operates Canary; CAST was formed by merging the Technology and Security Policy Center and the Meselson Center; CAST has no separate EIN — receipts stay with RAND Corporation (MDR0033, MDR0178).
- CAST funding page: three funder lists, no amounts or terms; the "directed grants" list names The Audacious Project, Chris Anderson and Jacqueline Novogratz, Coefficient Giving, DALHAP Investments Ltd., Ergo Impact, Fathom, Good Ventures, High Tide, Valhalla, Hewlett, Li Lu Humanitarian Foundation, Pew, Sea Grape, and others — a centre-wide list; Canary is not tagged (MDP0157, MDP0490, MDS0360).
- Canary-tagged money to RAND: Valhalla $10,000,000 and High Tide $333,334 (filed, TY2024); OP $10,000,000 (commitment, Sept 2025). Everything else filed to RAND in the pack carries a non-Canary purpose: Gates six lines + one future line; Hewlett $300,000; Waking Up $250,000; FP $1,000,000; GVF twelve GENERAL SUPPORT lines FY2023–FY2025; NPT, Fidelity, Schwab, Vanguard, SVCF, Goldman Sachs Philanthropy Fund, American Endowment Foundation lines (§2.1); Pew FY2025 no RAND line (MDS0481); Longview USA no RAND line (MDS1131); Ergo Impact / Fathom Family Foundation / Sentinel Bio / DALHAP / Charlottes och Fredriks Stiftelse none found (MDS1133–1140). MD47 reclassified all 170 RAND-bound rows as adjacency for METR (MDP0612).
- RAND Form 990: FY2023 (2022-10-01 to 2023-09-30), FY2024 (to 2024-09-30, nine days before the announcement), FY2025 (to 2025-09-30, the first year that could carry Canary money): aggregated contributions (§1.4), Canary never named, Schedule B RESTRICTED, Schedule I fellowships only — no METR line (MDF0188–0190, MDS0474–0476, MDS0485, MDS0486); annual-report URL 404 (MDS0489); giving page generic (MDS0490).
- RAND Europe is three legal entities and not RAND Corporation (MDE0138); the UK AISI Contracts Finder award "CNI Monitoring" (RAND Europe, 348,959 GBP) names no consortium with METR (MDS0535).

---

## 6. Contradictions between rows (exact ids)

1. **Founders Pledge "first funded April 2024" vs one TY2024 line.** MDF0086/MDF0204 (grantee card: first funded 2024-04, amount undisclosed) vs MDF0058/MDF0152 (FP TY2024 Schedule I: a single METR line, $184,000) vs MDF0053/MDF0218 (Tallinn ledger 2024-12-06 $184,000 via FP-US). If FP paid METR in April 2024, either that payment is inside the $184,000 line (then the FP-US $184,000 is not the whole line) or it is outside Schedule I reporting. The pack records the dollar match as "noted, not merged" (MDF0058) and does not resolve the April event. Settling: FP's grant record / TY2025 return.
2. **ARC → METR figures and date.** 4,477,169 + 76,766 (MDF0064/MDF0065) vs 4,553,935 (MDF0007, MDT0030) vs 4,501,424 (MDF0034); 2024-04-30 (MDT0030/MDT0228) vs "May" (MDT0229) vs page stamp 2023-03-06 (MDT0031). Explained as one event with different filed bases (MDP0587); MDF0064's note mis-states the difference as $47,511.
3. **SFF-2025 $428,000 matching pledge typed both ways.** recommendation (MDF0046, MDF0197, MDP0185) vs commitment (MDF0081, MDF0217).
4. **Audacious METR share restated.** ~$17M (MDF0166/0168/0170/0171, 2024-10-09) vs "a bit under $16m … across 3 years" and "one-off" (MDF0169/0172, MDP0145, 2025-09-28). Two dated statements; the pack forbids replacing one with the other.
5. **"Moskovitz's donation to ARC in 2022" vs pack entities.** MDP0568 (official's phrasing) vs MDF0066/MDF0067 (OP recommendations) and MDF0335/MDF0337 (GVF filed grants) with MDE0139/MDE0140 unmerging Moskovitz from GVF/OP/Coefficient. No personal Moskovitz gift to ARC is on record; the firewall claim is undetermined.
6. **Seed TED Foundation negative vs its superseding attack.** MDS0008 (TY2021–TY2024 none found) → MDS1277 ("unbounded in form"); bounded rows MDS0434–0436/MDS0479 cover TY2022–TY2024 only.
7. **Posted-figure wording vs pack rows.** "~$21M RAND" (MDP0584) vs subtraction (MDP0144); "$4.55M" (MDP0570) vs no cash+in-kind sum; metr-17 "Vanguard channel" (MDP0542, MDP0580) vs sponsor-level only; person-for-organisation and adjacency-as-flow defects (MDP0532, MDP0533, MDP0536–MDP0539, MDP0543).
8. **Two $220,000 figures.** Longview 2023 (MDF0013/MDF0070/MDF0082) vs SFF-2025 further-opportunities METR column (MDF0093/MDP0040).
9. **Longview named as a "pooled fund" supporter (MDP0020/MDF0230) vs no legal-filer payment found (MDS0266/MDS1083/MDS0267/MDS1084/MDS0268).** Not a contradiction — a thank-you is not a payment record and a UK or pre-2024 payment would not appear on the US TY2024 return — but the payment is unrecovered.
10. **Seed note vs standing rule.** MDF0011's seed note says the SVCF $20,000 "Matches Jaan Tallinn's public donation ledger to the dollar" (and continues "Tallinn is an Anthropic Series B investor and boa…", truncated); MDS1082, MDE0028, MDF0062 and MDF0220 forbid adviser identification by amount-matching. Cite MDF0037/MDF0153, not the seed note.

---

## 7. Table defects found

- **D1 Non-numeric `amount_usd`**: MDF0004 `<16000000 ("a bit under $16m")`, MDF0169 `<16000000`, MDF0009 `120000 + 428000 matching pledge`, MDF0014 `EUR 128,000` (currency EUR in a USD column). MDF0172 (same Barnes statement) leaves the field blank while MDF0169 carries a string.
- **D2 Duplicate fact rows across lanes** — 44 groups in these routes with identical (money_type, amount, from, to, period), e.g. SVCF $20,000 ×7 (MDF0037, 0062, 0153, 0205, 0212, 0220, 0418); GVF→RAND FY2024 $2,500,000 ×6 (MDF0098, 0102, 0306, 0310, 0388, 0392 — two genuine lines recorded three times each); Tallinn $10,000 ×5 (MDF0051, 0052, 0221, 0222, 0412 — two genuine lines); Vanguard $4,000,000 ×4 (MDF0038, 0154, 0206, 0211); FP→METR $184,000 ×4 (MDF0058, 0152, 0203, 0219); Valhalla $10,000,000 ×3 (MDF0149, 0174, 0297); High Tide $333,334 ×3 (MDF0148, 0175, 0298); NPT/Fidelity/Schwab→RAND FY2025 ×2 (MDF0118/0186, 0119/0187, 0120/0417); FP→RAND ×2 (MDF0122/0177); ARC→METR cash ×2 (MDF0064/0207); Audacious ~$38M/~$17M ×2–3 each. Plus MD50 exact duplicates (MDF0467–MDF0925) and MD47 edge rows (MDF0930–MDF1029). Any sum or count over `funding_events.csv` is inflated 2–7× unless deduped on (from, to, amount, period, source object id).
- **D3 Entity alias inconsistency** in from/to: Good Ventures Foundation / GOOD VENTURES FOUNDATION / "Good Ventures" (MDF0306–0310 — the last collides with the distinct legal entity "Good Ventures" EIN 45-2757586 flagged in MDT0193); Fidelity Investments Charitable Gift Fund / FIDELITY CHARITABLE / Fidelity Charitable; Vanguard Charitable Endowment Program / VANGUARD CHARITABLE / Vanguard Charitable; Donor Advised Charitable Giving Inc / Schwab Charitable (DAFgiving360) / SCHWAB CHARITABLE FUND / SCHWAB CHARITABLE; RAND Corporation / THE RAND CORPORATION / RAND CORPORATION / RAND and METR / RAND Corporation [Technology and Security Policy Center]; The Audacious Project / The Audacious Project (TED); Canary (METR and RAND) / Canary (RAND + METR); Alignment Research Center / ALIGNMENT RESEARCH CENTER / "ARC Evals (…)" variants; Founders Pledge Inc / Founders Pledge / FOUNDERS PLEDGE INC / FOUNDERS PLEDGE INCORPORATED; Survival and Flourishing Fund / Survival and Flourishing Fund (Jaan Tallinn) / "Jaan Tallinn (funder named on the SFF table)". `entities.csv` gives the separations (MDE0027–0035, MDE0132–0140) but no spelling map.
- **D4 Inconsistent `money_type` for one fact**: SFF-2025 match (recommendation vs commitment, above); FP grantee card (paid_grant with no amount MDF0086 vs filed_grant MDF0204); MDF0305 future grant and MDF0454/0455/0456/0459 revenue totals have blank money_type by design.
- **D5 Arithmetic error in a note**: MDF0064 "$47,511 difference" (actual 24,255 / 52,511).
- **D6 Seed note carries a forbidden inference**: MDF0011 (see contradiction 10).
- **D7 Superseding rows that are audit records, not replacements**: MDS1270 (attack on MDS0001) cites `metr.org/blog/2026-08-14-funding-update/` as its url — unrelated to the Coefficient index; MDS1275/1276/1277 are "unbounded in form" records; following `superseded by` pointers lands on audit rows rather than evidence.
- **D8 Heterogeneous date encodings**: `SFF-2024`, `2024`, `2024-12-31`, `FY2025 (2024-07-01 to 2025-06-30)` in the date column (MDF0012, MDP0043), `2024-10-09/2026-09-16` (listing windows), `2024 (TY2024 990-PF Part XV)` (MDP0001).
- **D9 Three dates for the Longview $220,000**: `2023` (MDF0013), `2023-08` (MDF0070/0200), `2023-09-25` (MDP0478).
- **D10 Blank from/to/amount on edge rows** (MDF0955, 0956, 0962, 0986 …) and on MDF0162 (Longview revenue; no supersede pointer to its replacement MDF0454, whereas MDF0155 → MDF0459 is marked).

---

## 8. Cautions for anyone drawing figures from this pack

1. Never sum across money types; every row in these routes is excluded from the ~$71M commitment denominator in `commitment_reconciliation.csv` (MDP0032–0047, MDP0053, MDP0481–0489).
2. A commitment is not a payment: ~$38M, ~$17M, <$16M (Audacious), $10M OP→RAND, $428,000 SFF match are commitments/announcements.
3. The only filed Canary-purpose payments are to RAND; METR has no Canary-attributed line in any checked filing; its FY2024 990 aggregates $9,101,611 of unnamed contributions plus $4,501,424 from ARC.
4. DAF sponsor filings never disclose the account principal; no amount-matching, hinting or "likely" labels.
5. Sponsor-to-sponsor flows are account-family moves, not METR money; do not sum Schedule I lines with the SVCF audit figures.
6. Keep every legal entity separate (the lists at the head of each route).
7. ARC is a related organisation, not a parent; one spin-off edge with three filed labels; never sum cash with in-kind.
8. The firewall claim is undetermined; name the settling document, do not assert either way.
9. Recommendation / paid / filed are three columns; $184,000 appears in two of them for one dollar amount.
10. EUR stays EUR; the two $220,000 figures are unrelated; 2023 Longview/Effektiv Spenden recipients were ARC Evals (ARC), not METR Inc.
11. Page-appearance and archive-capture dates are never transaction dates; DIFFERS verdicts are field audit notes, not amount disputes.
12. Filter MD50 "audit of promoted" and MD47 edge rows before counting; flag the Vanguard $4,000,000 provenance (XML not recovered; gate correction MDP0600 open).
13. Calendar closers, not negatives: METR FY2025 990 (ext 2026-11-16); SVCF/FP/Longview USA/OP TY2025 (ext 2026-11-16); Vanguard/Fidelity/NPT/DACG FY2026 (2026-11-16); GVF FY2026 (2026-11-16 / 2027-05-17); partner TY2025 990-PFs (ext 2026-11-16); Tepper FYE 2025-11-30 extended (CAL08).
14. Only public people in public roles (Barnes, Guest, Berger, Moskovitz and Tallinn as named funders/investors, "Trevor" as OP program officer on the archived page); no adviser, pooled-fund donor or private individual named or inferred.
15. No motive language; "channel", "reach METR through", "firewalled" framings from posted figures are adjudicated defects, not pack facts.

---

## 9. Suggested figures

- **B1 Canary: four propositions, four kinds of source** — four stacked panels (membership 46→60 names, 14 adds, six boilerplate names, TED does not fund; project funding ~$38M commitment with Audacious page showing no amount; allocation ~$17M / <$16M-3y / RAND unquoted / ~$21M labelled subtraction; payment $10,000,000 Valhalla + $333,334 High Tide filed to RAND, $10,000,000 OP commitment to RAND, METR bounded negative with checked-filings list and closers).
- **B2 Where public verification stops for a donor-advised grant** — [account principal: undisclosed] ✕ [sponsor legal entity] → [Schedule I recipient row (a)–(h)] → [METR]; Vanguard FY2025 $4,000,000 (provenance flag) and SVCF TY2024 $20,000; Fidelity/NPT/DACG bounded negatives by year; Schedule B redaction bar; stop statement from MDS0594/STATE.md line 313.
- **B3 Sponsor-to-sponsor transfer matrix FY2023–FY2025** — 5×5 directed heatmap per filer period from §2.2, log scale, SVCF audit figures as a footnote, "not METR money" in the title.
- **B4 ARC → METR: one spin-off, three filed figures** — dated edge (Schedule N 2024-04-30; Part III "May") with labels 4,477,169 + 76,766 / 4,553,935 / 4,501,424; ARC-side column of 2022 OP recommendations paired with GVF filed lines, FTX received/returned, SFF/FLI/LTFF/FP/DAF ARC lines; firewall text box "undetermined" with settling document.
- **B5 Recommendation vs paid vs filed** — the §4.1 three-column ledger (SFF-2024, SFF-2025, Longview 2023, Effektiv Spenden 2023, SFF-2022-H2 comparison to ARC); no column sums; $184,000 marked once.
- **B6 RAND receipts by purpose** — bars grouped by payer, coloured Canary-tagged / commitment / not Canary; dashed RAND→METR edge "none found (Schedule I FY2023–FY2025; Schedule B RESTRICTED)"; RAND Europe kept off the chart.
- **B7 Coefficient / OP / GVF → METR checked-years strip** — GVF Part XV FY2020–FY2025 with row counts scanned; OP TY2024 (no Schedule I); catalog 404 (2026-09-16); staff note (2025); Berger 2025-12-18; closers GVF FY2026 and OP TY2025; cite MDS1011–1016/MDS1283, not the MD50 attack rows.
