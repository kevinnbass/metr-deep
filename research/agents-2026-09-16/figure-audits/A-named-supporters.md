# Audit A: every named supporter of METR and every documented direct-money fact

Pack: `/mnt/f/projects/anthropic/metr_deep` (read-only). Built 2026-09-16 from the promoted tables; role/strength are the case.json bindings; rows whose note says "superseded by" are marked DEAD and must not be drawn. Money types are never summed across type. Amounts are quoted exactly as the row carries them; the currency column governs.

## How to read this audit

- **ANCHOR** rows are the ones a figure should cite for an amount; restatement rows (MD50 re-verifications, MD47 edge classifications, MD53 figure bibliography, MD70 live-list, MD46 recon re-run) are listed separately so they are not mistaken for new facts.
- "SEED" marks the S0 baseline transcribed from the earlier 10-metr pack (context strength); "new_vs_seed" in the JSON is false for those rows.
- Negatives are the pack's own `supporter_coverage.csv` attribution (plus a few strict additions for ARC and the EU contract), each with source class, query and result, and flagged if dead.

## Summary table

| supporter | status | identified amount(s) (type) | anchor rows | primary-strength negatives |
|---|---|---|---|---|
| The Audacious Project (TED) | amount identified (commitment, joint); no payment filed | ~38,000,000 USD joint RAND+METR 2024-10-09; ~17,000,000 USD METR share 2024-10-09; <16,000,000 USD over 3 years (2025-09-28) | MDF0167, MDF0165, MDF0166, MDF0170, MDF0169, MDF0172 | MDS0432, MDS0434-0436, MDS0437, MDS0438, MDS0419 |
| individuals from Jane Street | acknowledged, no amount (class) | none | MDF0018, MDF0019, MDP0003 | MDS0009, MDS0022 |
| Sijbrandij Foundation | acknowledged, no amount | none | MDP0004, MDP0005 | MDS0062-0065 |
| The Pew Charitable Trusts | acknowledged, no amount | none | MDP0009 | MDS0134, MDS0136-0140, MDS0146, MDS0124 |
| Schmidt Sciences | acknowledged, no amount; payer entity unknown | none | MDF0022 | MDS0047, MDS0048, MDS0050, MDS0053 |
| Packard Foundation | amount identified (commitment) | 350,000 USD, award year 2026, 12 months, general support | MDF0020, MDP0030 | MDS0034-0037, MDS0041, MDS0029 |
| LaCentra-Sumerlin Foundation | acknowledged, no amount | none | MDR0021 | MDS0167 (MDS0151 dead) |
| Astralis Foundation | acknowledged, no amount | none | MDR0022 | MDS0153 |
| Expa.org | acknowledged, no amount | none | MDR0023 | MDS0152, MDS0168 |
| AI Security Institute (UK) | acknowledged, no amount (contract undisclosed) | none (programme ceilings only, GBP) | MDP0197, MDP0200 | MDS0523-0526, MDS0532, MDS0534, MDS0535 |
| Longview Philanthropy | amount identified (recommendation) | 220,000 USD, Aug 2023, to ARC Evals (then ARC) | MDF0070 | MDS0266, MDS0267, MDS0270, MDS0415 |
| Effektiv Spenden | amount identified (regrant, EUR) | 128,000 EUR, Aug 2023, to METR (formerly ARC Evals) | MDF0072 | MDS0270 |
| Survival and Flourishing Fund / Jaan Tallinn | amounts identified (recommendation; matching pledge; paid_grant) | rec 204,000 (SFF-2024); rec 120,000 + match 428,000 conditional (SFF-2025); paid 10,000 + 10,000 (Jul 2024) + 184,000 (2024-12-06) | MDF0047, MDF0045, MDF0046, MDF0051, MDF0052, MDF0053 | MDS0232, MDS0238 |
| David Farhi | acknowledged, no amount | none | MDF0023, MDF0024 | MDS0077-0106 set |
| Geoff Ralston | acknowledged, no amount | none | MDF0025, MDF0026 | MDS0079-0103 set |
| Dylan Field | acknowledged, no amount | none | MDF0027, MDF0028 | MDS0080-0103 set |
| Steve Newman | acknowledged, no amount | none | MDF0029, MDF0030 | MDS0081-0103 set |
| European AI Office | acknowledged; consortium amount only (contract, EUR) | 1,167,484 EUR lot total, 2025-12-15, METR share undisclosed, consumed 0.00 | MDF0150, MDF0151, MDP0132 | MDS0373, MDS0834 |
| [not named] Alignment Research Center | amount identified (transfer + in_kind_estimate) | 4,477,169 + 76,766 = 4,553,935 USD (ARC return, 2024-04-30) vs 4,501,424 USD (METR return FY2024) | MDF0064, MDF0065, MDT0030, MDF0034 | MDS1112, MDS0587 |
| [not named] Founders Pledge Inc | amount identified (filed_grant) | 184,000 USD TY2024 | MDF0058 | MDS0401, MDS0415, MDS0390-0392 |
| [not named] Silicon Valley Community Foundation | amount identified (filed_grant; DAF) | 20,000 USD TY2024 | MDF0037, MDF0062 | MDS0191-0193, MDS1150 |
| [not named] Vanguard Charitable | amount identified (filed_grant; DAF) | 4,000,000 USD FY2025 | MDF0038 | MDS0182-0185, MDS0441 |


# Named supporters (metr.org/about, MD70 capture)


## The Audacious Project (housed at TED)

**How METR names it:** metr.org/about: 'from METR's first institutional-scale funding through The Audacious Project (a funding initiative housed at TED)'; 2026-08-14 funding update: 'The Audacious Project, through which we received our first institutional-scale funding'

**Status:** public amount identified: commitment (joint Canary award to RAND and METR, three dated public statements); no payment to METR documented in any filing

### Facts (draw only from these)

- **MDF0167** [evidence/primary; lane MD16] commitment 38000000 USD | 2024-10-09 | The Audacious Project -> RAND and METR | status: committed; payment not stated | purpose: n/a
  - ANCHOR (joint): RAND press 2024-10-09: Audacious committed approximately $38 million to RAND and METR for Canary. Joint, approximate, term not stated, payment not stated.
  - url: https://www.rand.org/news/press/2024/10/09.html
- **MDF0165** [evidence/primary; lane MD16] commitment 38000000 USD | 2024-10-09 | The Audacious Project -> Canary (METR and RAND) | status: committed; payment not stated | purpose: n/a
  - METR blog 2024-10-09 restates the same approximately $38 million ('catalyzed'); same document also gives the METR share sentence.
  - url: https://metr.org/blog/2024-10-09-new-support-through-the-audacious-project/
- **MDF0166** [evidence/primary; lane MD16] commitment 17000000 USD | 2024-10-09 | The Audacious Project -> METR | status: committed; payment not stated | purpose: will support work at METR
  - ANCHOR (METR share): approximately $17 million of the Canary funding will support work at METR (METR blog 2024-10-09). Subset of the ~$38M; never additive with it.
  - url: https://metr.org/blog/2024-10-09-new-support-through-the-audacious-project/
- **MDF0170** [evidence/primary; lane MD18] commitment 17000000 USD | 2024-10-09 | The Audacious Project (TED) -> Model Evaluation and Threat Research Inc | status: committed; payment not stated | purpose: n/a
  - MD18 re-fetch of the same ~$17 million METR-share sentence (same primary as MDF0166).
  - url: https://metr.org/blog/2024-10-09-new-support-through-the-audacious-project/
- **MDF0171** [evidence/supporting; lane MD18] commitment 17000000 USD | 2024-10-09 | The Audacious Project (TED) -> Model Evaluation and Threat Research Inc | status: committed; payment not stated | purpose: n/a
  - METR X post 2024-10-09: $17M in new funding (same-day restatement of the share; no term).
  - url: https://x.com/METR_Evals/status/1844005567532245136
- **MDF0169** [evidence/primary; lane MD16] commitment <16000000 USD | 2025-09-28 | The Audacious Project -> METR | status: committed; payment not stated | purpose: n/a
  - ANCHOR (restatement): Beth Barnes 2025-09-28 comment: Audacious funding 'ended up being a bit under $16m, and is a commitment across 3 years'. Not an integer; not additive with ~$17M; only source for the 3-year term.
  - url: https://www.greaterwrong.com/posts/yrephKDBFL6h9zAFv/beth-barnes-s-shortform/comment/w3e6cbHeozQJaJH5c
- **MDF0172** [evidence/primary; lane MD18] commitment (no amount) USD | 2025-09-28 | The Audacious Project (TED) -> Model Evaluation and Threat Research Inc | status: committed; payment not stated | purpose: n/a
  - MD18 re-fetch of the same 2025-09-28 restatement (same primary as MDF0169).
  - url: https://www.greaterwrong.com/posts/yrephKDBFL6h9zAFv/beth-barnes-s-shortform/comment/w3e6cbHeozQJaJH5c
- **MDP0145** [evidence/supporting; lane MD16] commitment (no amount)  | 2025-09-28 | The Audacious Project -> METR | status: n/a | purpose: n/a
  - Same 2025-09-28 comment: the Audacious funding was 'a one-off'.
  - url: https://www.greaterwrong.com/posts/yrephKDBFL6h9zAFv/beth-barnes-s-shortform/comment/w3e6cbHeozQJaJH5c
- **MDP0139** [evidence/supporting; lane MD16] untyped (no amount)  | 2024 | The Audacious Project -> METR; RAND | status: n/a | purpose: n/a
  - Audacious Project grantee page (tag 2024) states no dollar amount and no award term.
  - url: https://www.audaciousproject.org/grantees/project-canary-a-collaboration-between-metr-and-rand
- **MDP0144** [context/supporting; lane MD16] commitment 21000000 USD | 2024-10-09 | The Audacious Project -> not quoted | status: n/a | purpose: n/a
  - Arithmetic remainder ~$21M (38 minus 17) is a subtraction, not a quoted RAND allocation. Do not chart as a RAND share.
  - url: https://metr.org/blog/2024-10-09-new-support-through-the-audacious-project/
- **MDP0156** [evidence/primary; lane MD17] commitment (no amount)  | undated | The Audacious Project -> RAND and METR | status: not stated as paid on this page | purpose: n/a
  - RAND CAST Canary project page names Audacious support; no amount, term or payment date.
  - url: https://www.rand.org/global-and-emerging-risks/centers/ai-security-and-technology/projects/canary.html
- **MDP0148** [evidence/supporting; lane MD16] commitment 38000000 USD | 2024-11-03 | The Audacious Project -> Canary (METR and RAND) | status: n/a | purpose: n/a
  - Wayback 2024-11-03 of the METR post: figures unchanged; name Project Canary -> Canary.
  - url: https://web.archive.org/web/20241103120028id_/https://metr.org/blog/2024-10-09-new-support-through-the-audacious-project/
- **MDP0149** [evidence/supporting; lane MD16] commitment 38000000 USD | 2024-10-09 | The Audacious Project -> RAND and METR | status: n/a | purpose: n/a
  - Wayback 2024-10-09 of the RAND press: figure unchanged.
  - url: https://web.archive.org/web/20241009132212id_/https://www.rand.org/news/press/2024/10/09.html
- **MDP0033** [evidence/supporting; lane MD14] commitment 38000000 USD | 2024-10-09 | The Audacious Project (TED) -> Canary (RAND + METR) | status: n/a | purpose: n/a
  - Commitment reconciliation: ~$38M excluded from the ~$71M denominator (2024 date; joint recipients).
  - url: https://www.rand.org/news/press/2024/10/09.html
- **MDP0034** [evidence/supporting; lane MD14] commitment 17000000 USD | 2024-10-09 | The Audacious Project (TED) -> METR | status: n/a | purpose: n/a
  - Commitment reconciliation: ~$17M excluded (2024 date; subset).
  - url: https://metr.org/blog/2024-10-09-new-support-through-the-audacious-project/
- **MDP0035** [evidence/supporting; lane MD14] commitment <16000000 USD | 2025-09-28 | The Audacious Project (TED) -> METR | status: n/a | purpose: n/a
  - Commitment reconciliation: <$16M restatement excluded (2025 date; not an integer).
  - url: https://www.greaterwrong.com/posts/yrephKDBFL6h9zAFv/beth-barnes-s-shortform/comment/w3e6cbHeozQJaJH5c
- **MDP0151** [evidence/primary; lane MD18] commitment 17000000 USD | 2024-10-09 | The Audacious Project (TED) -> Model Evaluation and Threat Research Inc | status: committed; payment not stated | purpose: n/a
  - MD18: METR-share commitment is outside the Feb-Aug 2026 window.
  - url: https://metr.org/blog/2024-10-09-new-support-through-the-audacious-project/
- **MDP0152** [evidence/supporting; lane MD18] commitment (no amount) USD | 2025-09-28 | The Audacious Project (TED) -> Model Evaluation and Threat Research Inc | status: committed; payment not stated | purpose: n/a
  - MD18: 2025-09-28 restatement is outside the window.
  - url: https://www.greaterwrong.com/posts/yrephKDBFL6h9zAFv/beth-barnes-s-shortform/comment/w3e6cbHeozQJaJH5c
- **MDP0586** [evidence/supporting; lane MD50] commitment 38000000 USD | 2024-10-09 | The Audacious Project (TED) -> METR | status: n/a | purpose: n/a
  - MD50 double-count attack: $38M, $17M and <$16M are one award seen three ways; never separate inbound amounts.
  - url: https://www.rand.org/news/press/2024/10/09.html
- **MDP0001** [context/supporting; lane S0; SEED] filed_grant 10000000  | 2024 (TY2024 990-PF Part XV) | Valhalla Foundation (Scott Cook and Signe Ostby; EIN 20-0478828; Audacious partner) -> RAND Corporation (Project Canary) | status: n/a | purpose: "PROJECT CANARY, AN ARTIFICIAL INTELLIGENCE SAFETY INITIATIVE"; paid direct to RAND, Santa Monica
  - NOT A METR PAYMENT: Valhalla Foundation TY2024 990-PF $10,000,000 to RAND Corporation for Project Canary (seed context). Shows Audacious partner money reaching RAND, not METR.
  - url: https://projects.propublica.org/nonprofits/organizations/200478828/202502559349100000/full (XML copy research/990pf-valhalla-ty2024-202502559349100000.xml); research/audacious-partners.csv AP06
- **MDP0002** [context/supporting; lane S0; SEED] filed_grant 333334  | 2024 (TY2024 990-PF Part XV) | High Tide Foundation (EIN 20-1164239; Audacious partner on the 2024-10-09 list) -> RAND Corporation (Project Canary) | status: n/a | purpose: "To support tTHE PROJECT CANARY" (as filed); no METR line
  - NOT A METR PAYMENT: High Tide Foundation TY2024 990-PF $333,334 to RAND 'To support tTHE PROJECT CANARY' (seed context).
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202503179349100135_public.xml
- **MDF0005** [context/supporting; lane S0; SEED] commitment 38000000  | 2024-10-09 | The Audacious Project (TED) -> Canary (RAND + METR) | status: n/a | purpose: Canary: evaluations of frontier AI for dangerous capabilities
  - SEED BASELINE (context): ~$38M joint commitment as transcribed from the 10-metr pack.
  - url: https://www.rand.org/news/press/2024/10/09.html
- **MDF0006** [context/supporting; lane S0; SEED] commitment 17000000  | 2024-10-09 | The Audacious Project (TED) -> METR | status: n/a | purpose: METR share of Canary
  - SEED BASELINE (context): ~$17M METR share.
  - url: https://metr.org/blog/2024-10-09-new-support-through-the-audacious-project/
- **MDF0004** [context/supporting; lane S0; SEED] commitment <16000000 ("a bit under $16m")  | 2025-09-28 | The Audacious Project (TED) -> METR | status: committed; payment not stated | purpose: n/a
  - SEED BASELINE (context): 'a bit under $16m' across 3 years.
  - url: https://www.greaterwrong.com/posts/yrephKDBFL6h9zAFv/beth-barnes-s-shortform/comment/w3e6cbHeozQJaJH5c
- **MDF0125** [context/supporting; lane S2] commitment 38000000 USD | 2024-10-09 | The Audacious Project -> RAND Corporation and METR (Canary collaboration) | status: committed; payment not stated | purpose: n/a
  - S2 lineage import (context): ~$38M joint commitment.
  - url: https://www.rand.org/news/press/2024/10/09.html
- **MDF0223** [context/supporting; lane MD33] untyped (no amount)  | undated | The Audacious Project -> METR (Model Evaluation and Threat Research) | status: n/a | purpose: n/a
  - MD33: named on metr.org/about; amount not on that page.
  - url: https://metr.org/about

### Restatement / locator rows (do not cite as new facts)

MDF0087, MDF0168, MDF0173, MDF0194, MDF0195, MDF0208, MDF0467, MDF0468, MDF0469, MDF0550, MDF0588, MDF0628, MDF0629, MDF0630, MDF0631, MDF0632, MDF0633, MDF0634, MDF0635, MDF0636, MDF0657, MDF0658, MDF0671, MDF0686, MDF0955, MDF0986, MDF1023, MDF1024, MDP0142, MDP0146, MDP0147, MDP0162, MDP0173, MDP0184, MDP0490, MDP0491, MDP0492, MDP0493, MDP0499, MDP0500, MDP0501, MDP0642, MDP0643, MDP0655, MDP0656, MDP0686, MDP0717

### Timeline rows

MDT0119, MDT0121, MDT0038, MDT0039, MDT0040, MDT0041, MDT0042, MDT0043, MDT0044, MDT0045, MDT0046, MDT0047, MDT0048, MDT0049, MDT0050, MDT0051, MDT0062, MDT0063

### Bounded negatives

Counts (live): 55 rows; by source class: archives 8, funder filings 22, issuer statements 16, project documents 3, public grant databases 5, recipient filings 1
- MDS0302: public grant databases | GET https://www.audaciousproject.org/sitemap.xml (244 loc) filter metr|canary => Sitemap n=244; one METR loc: Project Canary collaboration between METR and RAND. No METR-only grantee loc and no dollar amount on the grantee page. | n=244 | role=evidence strength=supporting lane=MD1
- MDS0355: issuer statements | GET https://www.ted.com/about/programs-initiatives/audacious-project => none found in https://www.ted.com/about/programs-initiatives/audacious-project as of 2026-09-16T07:18:36Z | n=0 | role=context strength=supporting lane=MD15
- MDS0356: project documents | GET https://www.audaciousproject.org/grantees/project-canary-a-collaboration-between-metr-and-rand ; filter partner/funder names => none found in Audacious Canary grantee page for a named partner as Canary funder as of 2026-09-16T07:18:36Z | n=0 | role=negative strength=supporting lane=MD15
- MDS0357: issuer statements | GET https://www.rand.org/global-and-emerging-risks/centers/ai-security-and-technology/projects/canary.html ; Funding heading => none found in RAND Canary project page for an individual Audacious partner named as a Canary funder as of 2026-09-16T07:18:36Z | n=0 | role=negative strength=supporting lane=MD15
- MDS0359: issuer statements | GET https://metr.org/blog/2024-10-09-new-support-through-the-audacious-project/ ; partner names as Canary payers => none found in METR 2024-10-09 Audacious post for an individual partner named as a Canary payer as of 2026-09-16T07:18:36Z | n=0 | role=negative strength=supporting lane=MD15
- MDS0364: public grant databases | GET https://www.audaciousproject.org/sitemap.xml ; filter metr|canary|partner => sitemap has the Canary collaboration loc; none found in sitemap for a partner-by-project funder table as of 2026-09-16T07:18:36Z | n=1 | role=negative strength=supporting lane=MD15
- MDS0365: issuer statements | GET https://www.ted.com/about ; filter Audacious partners => none found in https://www.ted.com/about for an Audacious partner list as of 2026-09-16T07:21:20Z | n=0 | role=context strength=supporting lane=MD15
- MDS0366: issuer statements | GET https://www.audaciousproject.org/faq ; string partners pay grantees directly OR pay directly => none found in Audacious FAQ for the string partners pay grantees directly as of 2026-09-16T07:18:36Z | n=0 | role=context strength=supporting lane=MD15
- MDS0418: issuer statements | GET https://www.audaciousproject.org/grantees/project-canary-a-collaboration-between-metr-and-rand ; search Gates|ELMA|Valhalla|funder|million|$ => none found in www.audaciousproject.org/grantees/project-canary-a-collaboration-between-metr-and-rand as of 2026-09-16T07:19:01Z | n=0 | role=negative strength=supporting lane=MD16
- MDS0419: issuer statements | GET https://www.rand.org/news/press/2024/10/09.html ; search million of this|METR share|split|17 million => none found in www.rand.org/news/press/2024/10/09.html for a per-recipient dollar split as of 2026-09-16T07:19:01Z | n=0 | role=negative strength=primary lane=MD16
- MDS0420: issuer statements | GET https://www.audaciousproject.org/grantees/project-canary-a-collaboration-between-metr-and-rand ; search 17 million|38 million|split|share => none found in www.audaciousproject.org/grantees/project-canary-a-collaboration-between-metr-and-rand for a recipient dollar split as of 2026-09-16T07:19:01Z | n=0 | role=negative strength=supporting l
- MDS0425: issuer statements | GET www.audaciousproject.org/grantees/project-canary-a-collaboration-between-metr-and-rand ; /about ; /faq ; /news ; /sitemap.xml ; www.ted.com/about/programs-initiatives/the-audac => Audacious Canary grantee page responsive (no dollar); sitemap n=244 with 1 Canary loc; TED program page has no Canary amount | n=1 | role=evidence strength=supporting lane=MD16
- MDS0426: issuer statements | GET https://www.audaciousproject.org/news ; search Canary|METR|38 million => none found in www.audaciousproject.org/news for a Canary amount or term as of 2026-09-16T07:20:25Z | n=0 | role=negative strength=supporting lane=MD16
- MDS0428: issuer statements | GET https://www.audaciousproject.org/ideas/project-canary-a-collaboration-between-metr-and-rand => none found in www.audaciousproject.org/ideas/project-canary-a-collaboration-between-metr-and-rand as of 2026-09-16T07:19:01Z | n=0 | role=context strength=supporting lane=MD16
- MDS0429: archives | GET https://r.jina.ai/http://www.audaciousproject.org/grantees/project-canary-a-collaboration-between-metr-and-rand => none found in r.jina.ai proxy of www.audaciousproject.org/grantees/project-canary-a-collaboration-between-metr-and-rand as of 2026-09-16T07:19:18Z | n=0 | role=context strength=supporting lane=MD16
- MDS0431: archives | CDX url=metr.org/blog/2024-10-09-new-support-through-the-audacious-project/ ; url=www.rand.org/news/press/2024/10/09.html ; url=www.audaciousproject.org/grantees/project-canary-a-collaborat => RAND CDX 5 captures from 20241009; Audacious CDX many 2024-2026 captures; METR CDX first GET 503 then retry 200 with first capture 20241103120028 | n=5 | role=evidence strength=supporting lane=MD16
- MDS0432: recipient filings | GET S3 EfileData/XmlFiles/202523209349300367_public.xml; grep CANARY|AUDACIOUS|PROJECT CANARY; Part VIII RelatedOrganizationsAmt/AllOtherContributionsAmt; Schedule B ContributorInf => none found in METR FY2024 Form 990 object 202523209349300367 (Part VIII, Schedule B, Schedule R) as of 2026-09-16T07:22:52Z | n=0 | role=negative strength=primary lane=MD18
- MDS0443: public grant databases | GET https://www.audaciousproject.org/grantees/project-canary-a-collaboration-between-metr-and-rand ; r.jina.ai same URL; filter dollar amount / million / METR share => none found in The Audacious Project Canary grantee page as of 2026-09-16T07:20:59Z | n=0 | role=negative strength=supporting lane=MD18
- MDS0450: issuer statements | GET https://metr.org/blog/2026-08-14-funding-update/ ; filter 17 million|16m|Canary => none found in metr.org/blog/2026-08-14-funding-update/ as a restatement of METR's Canary share amount or term as of 2026-09-16T07:20:59Z | n=0 | role=negative strength=supporting lane=MD18
- MDS0493: public grant databases | GET https://www.audaciousproject.org/grantees/project-canary-a-collaboration-between-metr-and-rand => none found in audaciousproject.org/grantees/project-canary-a-collaboration-between-metr-and-rand for a dollar amount or RAND receipt as of 2026-09-16T07:18:22Z | n=0 | role=negative strength=supportin
- MDS0550: archives | https://web.archive.org/cdx/search/cdx?url=metr.org/blog/2024-10-09-new-support-through-the-audacious-project/&output=json&fl=timestamp,original,statuscode,mimetype,digest,length => 17 CDX rows; 17 status=200; 17 unique digest among status=200; first 20241103120028 last 20260915160045 | n=17 | role=evidence strength=supporting lane=MD24
- MDS0554: issuer statements | GET https://metr.org/blog/2024-10-09-new-support-through-the-audacious-project/ => live HTTP 200 sha256=2901b4015e28e138c6ca3b2b4c6533309bc8bcdce7cc4f24a09b6c4cf55b25e5; last archive 20260915160045 sha256=d651593df393f5395ec9221291238ce1c3a5a2eae43b487cdec68c09190e3152; bytes_equal=
- MDS0682: project documents | GET https://metr.org/blog/2024-10-09-new-support-through-the-audacious-project/ ; search free token|API credit|compute grant|access and tokens|provided us with|engineering support => none found in https://metr.org/blog/2024-10-09-new-support-through-the-audacious-project/ as of 2026-09-16T09:24:09Z | n=0 | role=negative strength=supporting lane=MD26
- MDS0776: issuer statements | GET anthropic.com Series A, E, F, G, H and /company; HTML search those supporter names => none found in Anthropic Series A/E/F/G/H and /company pages as of 2026-09-16T09:37:25Z for Packard, Pew, Sijbrandij, Audacious, LaCentra-Sumerlin, Astralis, Expa.org, Longview, Effektiv Spenden, David
- MDS0804: archives | GET https://r.jina.ai/http://www.audaciousproject.org/about and GET https://r.jina.ai/https://www.audaciousproject.org/about => none found in r.jina.ai proxy of http://www.audaciousproject.org/about as of 2026-09-16T09:57:25Z (HTTP 403 Cloudflare challenge) | n=0 | role=context strength=supporting lane=MD15
- MDS0809: archives | GET https://web.archive.org/cdx/search/cdx?url=metr.org/blog/2024-10-09-new-support-through-the-audacious-project/&output=json ; retry same URL later this window => none found in Wayback CDX for metr.org Audacious post as of 2026-09-16T09:48:39Z (HTTP 503 Temporarily Offline); retry also 503/0 bytes | n=0 | role=context strength=supporting lane=MD18
- MDS0980: public grant databases | search.json?q=The Audacious Project => none found in search.json?q=The Audacious Project / IRS e-file index_2024-2026 under the listed name as of 2026-09-16T09:44:36Z | n=0 | role=negative strength=supporting lane=MD43
- MDS0981: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202542519349101034_public.xml ; GrantOrContributionPdDurYrGrp / GrantOrContriApprvForFutGrp / ExpenditureResponsi => none found in 10X Better Foundation Form 990PF object 202542519349101034 grant schedule as of 2026-09-16T09:47:43Z | n=0 | role=negative strength=supporting lane=MD43
- MDS0982: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202503189349103400_public.xml ; GrantOrContributionPdDurYrGrp / GrantOrContriApprvForFutGrp / ExpenditureResponsi => none found in Additional Ventures Form 990PF object 202503189349103400 grant schedule as of 2026-09-16T09:47:43Z | n=0 | role=negative strength=supporting lane=MD43
- MDS0983: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202543189349103279_public.xml ; GrantOrContributionPdDurYrGrp / GrantOrContriApprvForFutGrp / ExpenditureResponsi => none found in Anne Wojcicki Foundation Form 990PF object 202543189349103279 grant schedule as of 2026-09-16T09:47:43Z | n=0 | role=negative strength=supporting lane=MD43
- MDS0984: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202543219349104089_public.xml ; GrantOrContributionPdDurYrGrp / GrantOrContriApprvForFutGrp / ExpenditureResponsi => none found in Arrow Impact Form 990PF object 202543219349104089 grant schedule as of 2026-09-16T09:47:43Z | n=0 | role=negative strength=supporting lane=MD43
- MDS0985: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202503149349303480_public.xml ; GrantOrContributionPdDurYrGrp / GrantOrContriApprvForFutGrp / ExpenditureResponsi => none found in Climate Lead Form 990 object 202503149349303480 grant schedule as of 2026-09-16T09:47:43Z | n=0 | role=negative strength=supporting lane=MD43
- MDS0986: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202543179349103724_public.xml ; GrantOrContributionPdDurYrGrp / GrantOrContriApprvForFutGrp / ExpenditureResponsi => none found in Crankstart Form 990PF object 202543179349103724 grant schedule as of 2026-09-16T09:47:43Z | n=0 | role=negative strength=supporting lane=MD43
- MDS0987: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202523189349100212_public.xml ; GrantOrContributionPdDurYrGrp / GrantOrContriApprvForFutGrp / ExpenditureResponsi => none found in Dovetail Impact Foundation Form 990PF object 202523189349100212 grant schedule as of 2026-09-16T09:47:43Z | n=0 | role=negative strength=supporting lane=MD43
- MDS0988: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202512549349101116_public.xml ; GrantOrContributionPdDurYrGrp / GrantOrContriApprvForFutGrp / ExpenditureResponsi => none found in Growald Climate Fund Form 990PF object 202512549349101116 grant schedule as of 2026-09-16T09:47:43Z | n=0 | role=negative strength=supporting lane=MD43
- MDS0989: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202611689349100131_public.xml ; GrantOrContributionPdDurYrGrp / GrantOrContriApprvForFutGrp / ExpenditureResponsi => none found in James Family Charitable Foundation Form 990PF object 202611689349100131 grant schedule as of 2026-09-16T09:47:43Z | n=0 | role=negative strength=supporting lane=MD43
- MDS0990: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202630909349100628_public.xml ; GrantOrContributionPdDurYrGrp / GrantOrContriApprvForFutGrp / ExpenditureResponsi => none found in Lyda Hill Philanthropies Form 990PF object 202630909349100628 grant schedule as of 2026-09-16T09:47:43Z | n=0 | role=negative strength=supporting lane=MD43
- MDS0991: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202612039349100951_public.xml ; GrantOrContributionPdDurYrGrp / GrantOrContriApprvForFutGrp / ExpenditureResponsi => none found in Oak Foundation Form 990PF object 202612039349100951 grant schedule as of 2026-09-16T09:47:43Z | n=0 | role=negative strength=supporting lane=MD43
- MDS0992: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202503219349104680_public.xml ; GrantOrContributionPdDurYrGrp / GrantOrContriApprvForFutGrp / ExpenditureResponsi => none found in Robertson Foundation Form 990PF object 202503219349104680 grant schedule as of 2026-09-16T09:47:43Z | n=0 | role=negative strength=supporting lane=MD43
- MDS0993: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202512689349301556_public.xml ; GrantOrContributionPdDurYrGrp / GrantOrContriApprvForFutGrp / ExpenditureResponsi => none found in Science Philanthropy Alliance Form 990 object 202512689349301556 grant schedule as of 2026-09-16T09:47:43Z | n=0 | role=negative strength=supporting lane=MD43
- MDS0994: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202503169349103550_public.xml ; GrantOrContributionPdDurYrGrp / GrantOrContriApprvForFutGrp / ExpenditureResponsi => none found in Seadream Family Foundation Form 990PF object 202503169349103550 grant schedule as of 2026-09-16T09:47:43Z | n=0 | role=negative strength=supporting lane=MD43
- MDS0995: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202513509349100511_public.xml ; GrantOrContributionPdDurYrGrp / GrantOrContriApprvForFutGrp / ExpenditureResponsi => none found in Someland Foundation Form 990PF object 202513509349100511 grant schedule as of 2026-09-16T09:47:43Z | n=0 | role=negative strength=supporting lane=MD43
- MDS0996: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202513189349311961_public.xml ; GrantOrContributionPdDurYrGrp / GrantOrContriApprvForFutGrp / ExpenditureResponsi => none found in The Bridgespan Group Form 990 object 202513189349311961 grant schedule as of 2026-09-16T09:47:43Z | n=0 | role=negative strength=supporting lane=MD43
- MDS0997: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202513219349309271_public.xml ; GrantOrContributionPdDurYrGrp / GrantOrContriApprvForFutGrp / ExpenditureResponsi => none found in The Just Trust Form 990 object 202513219349309271 grant schedule as of 2026-09-16T09:47:43Z | n=0 | role=negative strength=supporting lane=MD43
- MDS0998: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202502379349100610_public.xml ; GrantOrContributionPdDurYrGrp / GrantOrContriApprvForFutGrp / ExpenditureResponsi => none found in The Tepper Foundation Form 990PF object 202502379349100610 grant schedule as of 2026-09-16T09:47:43Z | n=0 | role=negative strength=supporting lane=MD43
- MDS0999: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202533189349302518_public.xml ; GrantOrContributionPdDurYrGrp / GrantOrContriApprvForFutGrp / ExpenditureResponsi => none found in Virgin Unite Form 990 object 202533189349302518 grant schedule as of 2026-09-16T09:47:43Z | n=0 | role=negative strength=supporting lane=MD43
- MDS1000: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202503209349301300_public.xml ; GrantOrContributionPdDurYrGrp / GrantOrContriApprvForFutGrp / ExpenditureResponsi => none found in Open Philanthropy Form 990 object 202503209349301300 grant schedule as of 2026-09-16T09:47:43Z | n=0 | role=negative strength=supporting lane=MD43
- MDS1008: issuer statements | GET https://www.audaciousproject.org/about ; /faq ; gatesfoundation.org/about/financials ; valhallafoundation.org ; skoll.org/about/the-skoll-foundation/ ; macfound.org/about/finan => Audacious about HTTP 200 (60 partner names present, including High Tide Foundation and Valhalla Foundation); issuer annual-report/financials pages fetched as calendar context, not as grant ledgers | n
- MDS1009: project documents | GET https://www.audaciousproject.org/grantees/project-canary-a-collaboration-between-metr-and-rand ; filter million|$|funder => none found in www.audaciousproject.org/grantees/project-canary-a-collaboration-between-metr-and-rand for a dollar amount or named partner as Canary payer as of 2026-09-16T09:44:42Z | n=0 | role=negati
- MDS1125: issuer statements | GET https://www.ted.com/talks?q=Canary+Audacious => none found in www.ted.com/talks?q=Canary+Audacious for a Canary/METR/RAND/Beth Barnes talk as of 2026-09-16T09:42:50Z | n=0 | role=context strength=supporting lane=MD16
- MDS1127: archives | CDX url=metr.org/blog/2024-10-09-new-support-through-the-audacious-project/ ; url=www.rand.org/news/press/2024/10/09.html ; url=www.audaciousproject.org/grantees/project-canary-a-collaborat => none found in web.archive.org CDX for www.rand.org/news/press/2024/10/09.html as of 2026-09-16T09:46:43Z | n=0 | role=context strength=supporting lane=MD16
- MDS1129: archives | id_ 20241009132212 RAND, 20241103120028 METR, 20241106023027 Audacious => id_ captures HTTP 200 for RAND, METR and Audacious 2024 snapshots; CDX index was 503/504 this fetch (E14) | n=3 | role=context strength=supporting lane=MD16
- MDS1277: funder filings | Form 990-PF Part XV, TY2021-TY2024 => unbounded in form: result is not 'none found in <exact source> as of <UTC date>' | n=0 | role=context strength=supporting lane=MD50
- MDS1582: funder filings | GET IRS TEOS; earliest remaining statutory date 2026-10-15 => future document CAL08 is N/A-with-reason until availability; not searched-and-absent | n=0 | role=evidence strength=supporting lane=MD52
- MDS1676: archives | https://web.archive.org/cdx/search/cdx?url=metr.org/blog/2024-10-09-new-support-through-the-audacious-project/&output=json&fl=timestamp,original,statuscode,mimetype,digest,length => CDX query returned HTTP 503 HTML as of 2026-09-16T17:45:38Z; not treated as an empty index. 503/504 HTML is a cap. | n=0 | role=context strength=supporting lane=MD70

### Contradictions, duplicates and defects

- Three public figures for the same award: ~$38,000,000 joint to RAND and METR (RAND press and METR blog, 2024-10-09: MDF0167, MDF0165); ~$17,000,000 METR share (METR blog and X, 2024-10-09: MDF0166, MDF0170, MDF0171); a bit under $16,000,000 across 3 years (Beth Barnes, 2025-09-28: MDF0169, MDF0172). RAND never states a split (MDS0419). These are one commitment restated, not three amounts.
- The ~$21M non-METR remainder (MDP0144) is a subtraction, not a quoted RAND allocation; do not chart it as a RAND commitment.
- No document records any Audacious or partner payment to METR: METR FY2024 Form 990 has no Canary/Audacious payer (MDS0432); TED Foundation Inc 990-PF TY2022-TY2024 has no METR/RAND/Canary line (MDS0434-MDS0436); filed Canary payments went to RAND (Valhalla $10,000,000 MDP0001/MDS0437; High Tide $333,334 MDP0002/MDS0438).
- from_entity spelling varies across rows: The Audacious Project (TED) (seed/MD18) vs The Audacious Project (MD16/MD17). Same entity; TED is the host, not a payer (MDS0434-0436).
- The same ~$38M / ~$17M / <$16M figures appear on roughly 40 promoted MDF/MDP rows (listed under restatement_row_ids); sum nothing across them.

### Figure notes
Draw one commitment with three dated statements (2024-10-09 joint ~$38M; 2024-10-09 METR share ~$17M; 2025-09-28 METR share a bit under $16M, 3-year term). Label 'approximately'. Mark payment status as 'not stated in any public document' and show the RAND-side filed payments (Valhalla $10M; High Tide $333,334) on a RAND node, never on METR. Excluded from the ~$71M Feb-Aug 2026 commitment total (MDP0033/0034/0035). Primary-strength anchors: MDF0165, MDF0166, MDF0167, MDF0169, MDF0170, MDF0172.


## individuals from Jane Street (a class; no person named)

**How METR names it:** metr.org/about: 'to individuals from Jane Street'; 2026-08-14 update and METR_Evals X post: 'individuals from Jane Street'

**Status:** acknowledged, no public amount; METR names a class of natural persons, not the firm, and names no individual

### Facts (draw only from these)

- **MDF0018** [evidence/primary; lane MD07] untyped (no amount)  | undated | individuals from Jane Street -> METR (Model Evaluation and Threat Research) | status: acknowledged as a supporter; amount, date, vehicle and money type not disclosed by the source | purpose: n/a
  - ANCHOR: live metr.org/about names the class; amount, date, vehicle not disclosed. Audit cleared the seed money_type=commitment (see audit notes on the row).
  - url: https://metr.org/about
- **MDF0019** [evidence/primary; lane MD07] untyped (no amount)  | 2026-08-14 | individuals from Jane Street -> METR (Model Evaluation and Threat Research) | status: acknowledged as a supporter; amount, date, vehicle and money type not disclosed by the source | purpose: n/a
  - ANCHOR: 2026-08-14 funding update names the class; the ~$71M sentence on the same page is not an amount for this class.
  - url: https://metr.org/blog/2026-08-14-funding-update/
- **MDP0003** [negative/primary; lane MD07] untyped (no amount)  | undated | individuals from Jane Street -> METR | status: n/a | purpose: n/a
  - Bounded limit (negative, primary): no individual named by METR; no public filing checked discloses a natural-person Jane Street donor; METR Schedule B is RESTRICTED.
  - url: https://metr.org/about
- **MDP0048** [evidence/primary; lane MD14] commitment undisclosed  | undated | individuals from Jane Street -> METR | status: n/a | purpose: n/a
  - Commitment reconciliation: excluded (no public amount, no public date).
  - url: https://metr.org/about
- **MDP0475** [evidence/supporting; lane MD07] untyped (no amount)  | undated | Jane Street Global Trading, LLC / Jane Street (issuer-named) -> Anthropic PBC | status: n/a | purpose: n/a
  - A firm investment in Anthropic (Jane Street / Jane Street Global Trading, LLC) is not a METR gift by an individual; keep off any METR supporter figure.
  - url: https://www.anthropic.com/news/series-h
- **MDP0535** [evidence/supporting; lane MD51] untyped (no amount)  | undated | individuals from Jane Street -> Jane Street (firm) | status: n/a | purpose: n/a
  - MD51 defect record: the posted figure metr-11 put the firm's Anthropic stakes on the individuals row; do not repeat.
  - url: https://api.github.com/repositories/1370599694/contents/figures/metr-11-same-donors-both-sides-of-the-table.html?ref=f64df65a16400fd88a77536111851695acc9a928
- **MDT0009** [context/supporting; lane MD07] untyped (no amount)  | 2026-08-14 | individuals from Jane Street -> METR | status: n/a | purpose: n/a
  - METR_Evals X post 2026-08-14 restates the thank-you naming the class.
  - url: https://x.com/METR_Evals/status/2088403780551442683
- **MDT0225** [evidence/supporting; lane MD07] untyped (no amount)  | 2026-06-01 | ? -> METR | status: n/a | purpose: n/a
  - Wayback 2026-06-01 about page lacks the wording 'individuals from Jane Street'.
  - url: https://web.archive.org/web/20260601232933id_/https://metr.org/about
- **MDT0105** [evidence/primary; lane MD24] untyped (no amount)  | 2026-08-04 | ? -> METR | status: n/a | purpose: n/a
  - About-page first appearance of the class wording bounded 2026-07-19 to 2026-08-04 (page change, not a gift date).
  - url: https://web.archive.org/web/20260804074910id_/https://metr.org/about
- **MDF0015** [context/supporting; lane S0; SEED] commitment undisclosed  | undated | individuals from Jane Street -> METR | status: n/a | purpose: general support
  - SEED BASELINE (context): seed typed this class as money_type=commitment, amount 'undisclosed', purpose 'general support'. The lane rows carry no money type; treat the seed typing as superseded in substance.
  - url: https://metr.org/about
- **MDF0213** [context/supporting; lane MD33] untyped (no amount)  | undated | individuals from Jane Street -> METR (Model Evaluation and Threat Research) | status: acknowledged as a supporter class; no individual, amount, date or vehicle disclosed | purpose: n/a
  - MD33: named; amount, date, vehicle not stated.
  - url: https://metr.org/about

### Restatement / locator rows (do not cite as new facts)

MDF0478, MDF0481, MDF0482, MDF0676, MDP0514, MDP0599, MDP0622, MDP0718, MDE0055, MDE0133, MDT0104

### Timeline rows

MDT0009, MDT0104, MDT0105, MDT0225

### Bounded negatives

Counts (live): 20 rows; by source class: SEC 3, court dockets 1, funder filings 1, issuer statements 3, press 2, public grant databases 4, recipient filings 1, self-statements 3, state registries 2
- MDS0009: self-statements | X Latest keyword search: ("Jane Street" OR janestreet) (METR OR "ARC Evals" OR "Alignment Research Center"); also "individuals from Jane Street"; from:METR_Evals ("Jane Street" OR "i => none found in X Latest keyword search for a named individual first-person METR gift as of 2026-09-16T05:48:00Z | n=0 | role=negative strength=primary lane=MD07
- MDS0010: self-statements | GET https://forum.effectivealtruism.org/search?query=Jane%20Street%20METR ; GraphQL POST same host returned HTTP 400 => none found in EA Forum search page/GraphQL as of 2026-09-16T05:34:01Z | n=0 | role=negative strength=supporting lane=MD07
- MDS0012: public grant databases | GET https://projects.propublica.org/nonprofits/api/v2/search.json?q=Jane%20Street => none found in ProPublica org search q=Jane Street as of 2026-09-16T05:34:01Z for a Jane Street Capital/Group private foundation that could name a METR grant | n=3 | role=negative strength=supporting l
- MDS0018: self-statements | GET https://survivalandflourishing.com/ and https://survivalandflourishing.fund/ ; search Jane Street => none found in SFC/SFF public pages as of 2026-09-16T05:34:01Z for a first-person METR gift by a named Jane Street individual | n=0 | role=negative strength=supporting lane=MD07
- MDS0020: public grant databases | GET https://candid.org/search/?query=Jane%20Street%20METR => none found in Candid public search page as of 2026-09-16T05:48:00Z (login wall; no grant rows in recovered HTML) | n=0 | role=context strength=supporting lane=MD07
- MDS0312: public grant databases | GET https://www.janestreet.com/ ; GET /giving ; GET /the-latest/impact/ ; GET graduate-research-fellowship => none found in Jane Street /giving as of 2026-09-16T06:14:50Z (HTTP 404); no public grant index, sitemap or API for firm grants to METR | n=0 | role=context strength=supporting lane=MD13
- MDS0508: issuer statements | GET https://metr.org/about funding paragraph (recipient naming only; no Jane Street the firm grant page) => none found in Jane Street the firm or any named-individual funder document for a purpose/restriction on this class as of 2026-09-16T07:21:32Z | n=0 | role=negative strength=supporting lane=MD23
- MDS0762: court dockets | GET https://www.courtlistener.com/api/rest/v4/search/?q="Jane Street" Anthropic&type=o => none found in CourtListener REST v4 search q="Jane Street" Anthropic type=o (count=0) as of 2026-09-16T09:37:47Z | n=0 | role=negative strength=supporting lane=MD33
- MDS0763: state registries | GET https://bizfileonline.sos.ca.gov/ => none found in California SOS bizfileonline.sos.ca.gov as of 2026-09-16T09:38:24Z (Incapsula challenge page, no entity record returned) | n=0 | role=context strength=supporting lane=MD33
- MDS0765: state registries | GET https://opencorporates.com/companies?q=Jane+Street+Global+Trading+LLC&jurisdiction_code=us_de => none found in OpenCorporates companies?q=Jane+Street+Global+Trading+LLC as of 2026-09-16T09:38:36Z (captcha challenge; no entity record returned) | n=0 | role=context strength=supporting lane=MD33
- MDS0769: recipient filings | IRS e-file XML 202523209349300367 IRS990ScheduleB ContributorInformationGrp => none found in METR FY2024 public 990 Schedule B as of 2026-09-16T09:37:58Z: contributor fields are RESTRICTED | n=0 | role=negative strength=supporting lane=MD33
- MDS0772: funder filings | GET https://projects.propublica.org/nonprofits/api/v2/search.json?q=Jane%20Street => none found in ProPublica org search q=Jane Street as of 2026-09-16T09:37:59Z for a Jane Street Capital/Group private foundation that could name a METR grant | n=3 | role=negative strength=supporting l
- MDS0777: SEC | SEC EFTS LATEST/search-index q="Jane Street" Anthropic file_date 2020-01-01..2026-09-16 => none found in SEC EFTS q="Jane Street" Anthropic for an Anthropic, PBC issuer filing as of 2026-09-16T09:37:51Z (214 hits were fund NPORT/N-CSR/N-CSRS plus CoreWeave, Inc. 8-K; none Anthropic, PBC) | 
- MDS1061: SEC | GET https://efts.sec.gov/LATEST/search-index?q="Jane Street" Anthropic&dateRange=custom&startdt=2023-01-01&enddt=2026-09-16 => none found in first 100 of 214 SEC EDGAR hits as of 2026-09-16T09:57:48Z for an Anthropic PBC issuer filing that names Jane Street as an investor | n=214 | role=negative strength=supporting lane=MD07
- MDS1064: press | GET https://www.wsj.com/tech/ai/jane-street-ai-wall-street-bdfcc81a => route failure: HTTP 401 / JS-challenge from WSJ as of 2026-09-16T09:57:48Z; article body unread | n= | role=context strength=supporting lane=MD07
- MDS1065: public grant databases | GET https://projects.propublica.org/nonprofits/api/v2/search.json?q=Jane%20Street%20Capital => none found in ProPublica org search q=Jane Street Capital as of 2026-09-16T09:57:48Z | n=0 | role=negative strength=supporting lane=MD07
- MDS1166: issuer statements | GET https://www.janestreet.com/ and https://www.janestreet.com/culture/ text search METR|Model Evaluation|philanthropy grant => none found in https://www.janestreet.com/ or https://www.janestreet.com/culture/ as of 2026-09-16T09:58:24Z for a METR purpose/restriction (0 METR strings) | n=0 | role=negative strength=supporting la
- MDS1219: SEC | GET https://efts.sec.gov/LATEST/search-index?q=%22Jane%20Street%20Global%20Trading%22%20Anthropic&dateRange=all ; match_phrase Jane Street Global Trading AND Anthropic => none found in SEC EDGAR full-text search (Jane Street Global Trading AND Anthropic) as of 2026-09-16T12:27:12Z | n=0 | role=negative strength=supporting lane=MD51
- MDS1226: press | GET https://www.businessinsider.com/metr-beth-barnes-ai-talent-shortage-safety-research-openai-2026-8 ; r.jina.ai of the same URL; filter Jane Street, Coefficient, Good Ventures, Moskovitz, Sc => none found in Business Insider METR profile (Council, 2026-09-11) as of 2026-09-16T12:33:54Z of Jane Street, Coefficient, Good Ventures, Moskovitz or Schmidt used as a METR money-path or entity merge 
- MDS1687: issuer statements | GET https://metr.org/about funding paragraph; scan for a Jane Street natural-person name => none found in https://metr.org/about as of 2026-09-16T17:38:37Z: METR names the class 'individuals from Jane Street' and does not name a Jane Street natural person. This lane does not deanonymize by p

### Contradictions, duplicates and defects

- Seed MDF0015 carries money_type=commitment and purpose=general support for the class; MD07 re-verification (MDF0018/MDF0019) cleared the money type (audit notes: lane said money_type=commitment; ledger=commitments). No money type is supportable.
- The class wording appears on the live about page and the 2026-08-14 post but is absent from the 2026-06-01 capture (MDT0225); the first-appearance window is 2026-07-19 to 2026-08-04 (MDT0104/MDT0105). This dates METR wording, not any gift.

### Figure notes
Show as 'acknowledged, no public amount'. Never place a person's name on this row; never place Jane Street firm Anthropic investments (MDR0004-MDR0008, MDR0083-MDR0087) on it. Anchors: MDF0018, MDF0019; negative anchor MDP0003.


## Sijbrandij Foundation (EIN 85-4270305)

**How METR names it:** metr.org/about: 'foundations such as the Sijbrandij Foundation ...'; 2026-08-14 update: 'foundations like the Sijbrandij Foundation ...'

**Status:** acknowledged, no public amount

### Facts (draw only from these)

- **MDP0004** [evidence/supporting; lane MD05] untyped (no amount)  | undated | Sijbrandij Foundation -> METR | status: n/a | purpose: n/a
  - ANCHOR: named on metr.org/about; amount, date, duration, restriction not stated.
  - url: https://metr.org/about
- **MDP0005** [evidence/supporting; lane MD05] untyped (no amount)  | 2026-08-14 | Sijbrandij Foundation -> METR | status: n/a | purpose: n/a
  - ANCHOR: thanked in the 2026-08-14 update as a supporter over the years; no amount.
  - url: https://metr.org/blog/2026-08-14-funding-update/
- **MDP0006** [evidence/supporting; lane MD05] untyped (no amount)  | 2026-08-14 | Sijbrandij Foundation -> METR | status: n/a | purpose: n/a
  - The thank-you is over the years; not classifiable inside or outside the Feb-Aug 2026 window.
  - url: https://metr.org/blog/2026-08-14-funding-update/
- **MDE0010** [evidence/primary; lane MD05] untyped (no amount)  | undated | ? -> ? | status: n/a | purpose: n/a
  - Legal entity: SIJBRANDIJ FOUNDATION EIN 85-4270305 (TY2024 990-PF filer block).
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202513179349103921_public.xml
- **MDT0011** [evidence/supporting; lane MD05] untyped (no amount)  | 2025-12-16 | Sijbrandij Foundation -> METR | status: n/a | purpose: n/a
  - Already named on the 2025-12-16 about capture (page version, not a payment).
  - url: https://web.archive.org/web/20251216013159id_/https://metr.org/about
- **MDT0091** [evidence/primary; lane MD24] untyped (no amount)  | 2025-12-16 | ? -> METR | status: n/a | purpose: n/a
  - About-page first appearance bounded 2025-12-07 to 2025-12-16.
  - url: https://web.archive.org/web/20251216013159id_/https://metr.org/about
- **MDF0224** [context/supporting; lane MD33] untyped (no amount)  | undated | Sijbrandij Foundation -> METR (Model Evaluation and Threat Research) | status: n/a | purpose: n/a
  - MD33: named; amount not on page.
  - url: https://metr.org/about
- **MDP0054** [evidence/primary; lane MD14] untyped undisclosed  | undated | The Pew Charitable Trusts; Schmidt Sciences; Sijbrandij Foundation; LaCentra-Sumerlin Foundation; Astralis Foundation; Expa.org -> METR | status: n/a | purpose: n/a
  - Commitment reconciliation: excluded as addend (no public amount) with Pew, Schmidt Sciences, LaCentra-Sumerlin, Astralis, Expa.org.
  - url: https://metr.org/about

### Restatement / locator rows (do not cite as new facts)

MDF0687, MDP0183, MDP0520, MDP0599, MDP0719, MDE0011, MDE0070, MDE0123, MDE0124, MDE0125, MDT0090

### Timeline rows

MDT0011, MDT0090, MDT0091

### Bounded negatives

Counts (live): 27 rows; by source class: IRS TEOS and e-file index 4, funder filings 10, issuer statements 3, public grant databases 6, self-statements 2, state registries 2
- MDS0060: self-statements | GET https://sijbrandijfoundation.org/grants ; full-page text search METR OR 'Model Evaluation' OR 'Alignment Research' => none found in Sijbrandij Foundation grants page as of 2026-09-16T05:34:17Z | n=0 | role=negative strength=supporting lane=MD05
- MDS0061: self-statements | GET https://sijbrandijfoundation.org/ plus /team /investments /projects /fcct /sitemap.xml ; text search METR OR 'Model Evaluation' OR 'Alignment Research' => none found in Sijbrandij Foundation home and related site pages as of 2026-09-16T05:34:17Z | n=0 | role=negative strength=supporting lane=MD05
- MDS0062: funder filings | Form 990-PF tax year 2024 XML object_id=202513179349103921; grep METR|Model Evaluation|Alignment Research; read GrantOrContributionPdDurYrGrp and TotalGrantOrContriApprvFutAmt (990-PF => none found in Sijbrandij Foundation Form 990-PF TY2024 grant schedule (object_id 202513179349103921) as of 2026-09-16T05:35:24Z | n=0 | role=negative strength=primary lane=MD05
- MDS0063: funder filings | Form 990-PF tax year 2023 XML object_id=202423189349101777; grep METR|Model Evaluation|Alignment Research; read GrantOrContributionPdDurYrGrp and TotalGrantOrContriApprvFutAmt (990-PF => none found in Sijbrandij Foundation Form 990-PF TY2023 grant schedule (object_id 202423189349101777) as of 2026-09-16T05:35:24Z | n=0 | role=negative strength=primary lane=MD05
- MDS0064: funder filings | Form 990-PF tax year 2022 XML object_id=202333179349102443; grep METR|Model Evaluation|Alignment Research; read GrantOrContributionPdDurYrGrp and TotalGrantOrContriApprvFutAmt (990-PF => none found in Sijbrandij Foundation Form 990-PF TY2022 grant schedule (object_id 202333179349102443) as of 2026-09-16T05:35:24Z | n=0 | role=negative strength=primary lane=MD05
- MDS0065: funder filings | Form 990-PF tax year 2021 XML object_id=202233189349100703; grep METR|Model Evaluation|Alignment Research; read GrantOrContributionPdDurYrGrp and TotalGrantOrContriApprvFutAmt (990-PF => none found in Sijbrandij Foundation Form 990-PF TY2021 grant schedule (object_id 202233189349100703) as of 2026-09-16T05:35:24Z | n=0 | role=negative strength=primary lane=MD05
- MDS0066: funder filings | Form 990-PF tax year 2020 XML object_id=202113159349103831; grep METR|Model Evaluation|Alignment Research; read GrantOrContributionPdDurYrGrp and TotalGrantOrContriApprvFutAmt (990-PF => none found in Sijbrandij Foundation Form 990-PF TY2020 grant schedule (object_id 202113159349103831) as of 2026-09-16T05:35:24Z | n=0 | role=negative strength=supporting lane=MD05
- MDS0067: funder filings | 990-PF TY2020-TY2024 DonorAdvisedFundInd; text search donor advised|DAF => none found in Sijbrandij Foundation 990-PF DonorAdvisedFundInd/own materials for a named DAF account as of 2026-09-16T05:35:24Z | n=0 | role=negative strength=supporting lane=MD05
- MDS0068: issuer statements | GET https://metr.org/about and https://metr.org/blog/2026-08-14-funding-update/ ; search purpose, restriction, grant terms for Sijbrandij => none found in METR about page for a Sijbrandij grant purpose or restriction as of 2026-09-16T05:34:17Z | n=0 | role=negative strength=supporting lane=MD05
- MDS0069: IRS TEOS and e-file index | GET https://apps.irs.gov/app/eos/detailsPage?ein=854270305 => none found in IRS TEOS detailsPage for EIN 854270305 as of 2026-09-16T05:37:44Z (HTTP 403) | n=0 | role=context strength=supporting lane=MD05
- MDS0070: IRS TEOS and e-file index | stream grep EIN 854270305 in https://apps.irs.gov/pub/epostcard/990/xml/2026/index_2026.csv (full index; not truncated download) => none found in IRS 2026 Form 990 e-file index for EIN 854270305 as of 2026-09-16T05:42:05Z | n=0 | role=negative strength=supporting lane=MD05
- MDS0071: state registries | GET https://rct.doj.ca.gov/Verification/Web/Search.aspx?facility=Y ; GET https://ca-rcf.evokeplatform.com/app/publicPortal/verification ; grep CA may-not-operate list for SIJBRANDIJ => none found in California May Not Operate or Solicit list for Sijbrandij/854270305/CT0273494 as of 2026-09-16T05:43:20Z | n=0 | role=context strength=supporting lane=MD05
- MDS0072: state registries | POST https://icis.corp.delaware.gov/ecorp/entitysearch/NameSearch.aspx Entity Name=SIJBRANDIJ FOUNDATION File Number=4428228 => none found in Delaware Division of Corporations NameSearch live result set as of 2026-09-16T05:46:00Z | n=0 | role=context strength=supporting lane=MD05
- MDS0073: public grant databases | GET https://projects.propublica.org/nonprofits/full_text_search?q=METR+organization_id:854270305 => none found in ProPublica Nonprofit Explorer full-text search q=METR organization_id:854270305 as of 2026-09-16T05:37:48Z | n=0 | role=negative strength=supporting lane=MD05
- MDS0074: public grant databases | GET https://www.grantmakers.io/profiles/v1/854270305-sijbrandij-foundation/ ; in-page search METR|Model Evaluation|Alignment Research => none found in Grantmakers.io Sijbrandij Foundation profile grant names for METR as of 2026-09-16T05:37:48Z | n=0 | role=negative strength=supporting lane=MD05
- MDS0075: IRS TEOS and e-file index | stream grep EIN 854270305 in https://www.irs.gov/pub/irs-soi/eo_ca.csv => none found in IRS EO BMF CA extract for a METR grant line as of 2026-09-16T05:42:43Z | n=1 | role=context strength=supporting lane=MD05
- MDS0076: funder filings | GET https://projects.propublica.org/nonprofits/organizations/854270305 and API v2 same EIN; list tax years => none found in ProPublica org page for a TY2025 990-PF as of 2026-09-16T05:34:17Z | n=0 | role=context strength=supporting lane=MD05
- MDS0293: public grant databases | GET https://sijbrandijfoundation.org/sitemap.xml (7 loc including /grants) then GET /grants ; text search METR|Model Evaluation|Alignment Research => none found in Sijbrandij Foundation sitemap (7 loc) or grants page as of 2026-09-16T06:07:15Z for METR/ARC | n=7 | role=negative strength=supporting lane=MD13
- MDS0307: public grant databases | sitemap.xml 7 loc + GET /grants text search METR|Model Evaluation|Alignment Research => none found in Sijbrandij Foundation grants page as of 2026-09-16T06:07:15Z | n=0 | role=negative strength=supporting lane=MD13
- MDS0496: issuer statements | GET https://sijbrandijfoundation.org/grants ; text search METR|Model Evaluation|Alignment Research => none found in Sijbrandij Foundation grants page as of 2026-09-16T07:21:38Z | n=0 | role=negative strength=supporting lane=MD23
- MDS0497: funder filings | GET XML 202513179349103921 RecipientTable/GrantOrContributionPdDurYrGrp filter METR|991219864|Alignment Research => none found in Sijbrandij Foundation Form 990-PF TY2024 grant schedule (object 202513179349103921) as of 2026-09-16T07:24:42Z | n=0 | role=negative strength=supporting lane=MD23
- MDS0776: issuer statements | GET anthropic.com Series A, E, F, G, H and /company; HTML search those supporter names => none found in Anthropic Series A/E/F/G/H and /company pages as of 2026-09-16T09:37:25Z for Packard, Pew, Sijbrandij, Audacious, LaCentra-Sumerlin, Astralis, Expa.org, Longview, Effektiv Spenden, David
- MDS1043: public grant databases | GET https://projects.propublica.org/nonprofits/full_text_search?q=METR+organization_id:854270305 => none found in ProPublica Nonprofit Explorer full-text search q=METR organization_id:854270305 as of 2026-09-16T09:55:35Z | n=0 | role=negative strength=supporting lane=MD05
- MDS1044: public grant databases | GET https://www.grantmakers.io/profiles/v1/854270305-sijbrandij-foundation/ ; in-page search METR|Model Evaluation|Alignment Research => none found in Grantmakers.io Sijbrandij Foundation profile grant names for METR as of 2026-09-16T09:55:35Z | n=0 | role=negative strength=supporting lane=MD05
- MDS1045: IRS TEOS and e-file index | stream grep EIN 854270305 in https://www.irs.gov/pub/irs-soi/eo_ca.csv => none found in IRS EO BMF CA extract for a METR grant line as of 2026-09-16T09:57:37Z | n=1 | role=context strength=supporting lane=MD05
- MDS1046: funder filings | GET https://projects.propublica.org/nonprofits/organizations/854270305 and API v2 same EIN; list tax years => none found in ProPublica org page for a TY2025 990-PF as of 2026-09-16T09:55:35Z | n=0 | role=context strength=supporting lane=MD05
- MDS1274: funder filings | Form 990-PF Part XV, 2021-2024 => unbounded in form: result is not 'none found in <exact source> as of <UTC date>' | n=0 | role=context strength=supporting lane=MD50

### Contradictions, duplicates and defects

- None on amounts (none exists). MDE0012 (GitLab Foundation as a Sijbrandij 990-PF grantee, mis-typed paid_grant) is DEAD, superseded by MDE0125; neither is a METR fact.

### Figure notes
Acknowledged only. Bounded negatives at primary strength: 990-PF TY2021-TY2024 grant schedules (MDS0062-MDS0065) plus TY2020 (MDS0066); no TY2025 return yet (MDS0070). Anchors: MDP0004, MDP0005.


## The Pew Charitable Trusts (EIN 56-2307147)

**How METR names it:** metr.org/about: 'The Pew Charitable Trusts'; 2026-08-14 update: 'The Pew Charitable Trusts'

**Status:** acknowledged, no public amount

### Facts (draw only from these)

- **MDP0009** [evidence/supporting; lane MD03] untyped (no amount)  | undated | The Pew Charitable Trusts -> Model Evaluation and Threat Research | status: n/a | purpose: n/a
  - ANCHOR: named on metr.org/about without an award figure; no Pew award document found.
  - url: https://metr.org/about
- **MDE0017** [evidence/primary; lane MD03] untyped (no amount)  | undated | ? -> ? | status: n/a | purpose: n/a
  - Legal entity: The Pew Charitable Trusts EIN 56-2307147 (Form 990 filer, FYE June); distinct from Pew Research Center.
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202620849349301332_public.xml
- **MDF0036** [context/supporting; lane MD03] filed_grant 38100000 USD | 2025-06-30 | The Pew Charitable Trusts -> Pew Research Center | status: filed as granted | purpose: Information
  - NOT A METR AMOUNT: Pew Charitable Trusts FY2025 Schedule I $38,100,000 to Pew Research Center; recorded only to keep recipients unmerged. A from_entity filter on 'Pew' will pull this row; exclude it from any METR figure.
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202620849349301332_public.xml
- **MDT0099** [evidence/primary; lane MD24] untyped (no amount)  | 2026-03-11 | ? -> METR | status: n/a | purpose: n/a
  - About-page first appearance bounded 2026-03-06 to 2026-03-11 (page change, not a grant date).
  - url: https://web.archive.org/web/20260311015926id_/https://metr.org/about
- **MDF0225** [context/supporting; lane MD33] untyped (no amount)  | undated | The Pew Charitable Trusts -> METR (Model Evaluation and Threat Research) | status: n/a | purpose: n/a
  - MD33: named; amount not on page.
  - url: https://metr.org/about

### Restatement / locator rows (do not cite as new facts)

MDF0499, MDF0688, MDF1011, MDP0054, MDP0183, MDP0520, MDP0599, MDP0720, MDE0018, MDE0019, MDE0071, MDT0098

### Timeline rows

MDT0098, MDT0099

### Bounded negatives

Counts (live): 37 rows; by source class: IRS TEOS and e-file index 1, funder filings 12, issuer statements 8, public grant databases 16
- MDS0124: public grant databases | GET https://www.pew.org/site-map (sitemapindex, 3 shards); enumerate <loc>; filter loc for METR|Alignment Research Center|ARC Evals|Model Evaluation and Threat Research as who => none found in pew.org sitemapindex and 3 shard sitemaps (20932 loc URLs) as of 2026-09-16T05:39:22Z | n=0 | role=negative strength=primary lane=MD03
- MDS0125: public grant databases | GET https://www.pew.org/search?q=METR ; also r.jina.ai proxy of same URL; filters: none (site search) => none found in pew.org/search?q=METR as of 2026-09-16T05:37:30Z | n=0 | role=context strength=supporting lane=MD03
- MDS0126: public grant databases | GET https://www.pew.org/search?q=Model%20Evaluation%20and%20Threat%20Research via r.jina.ai; filters: query string => none found in pew.org/search?q=Model Evaluation and Threat Research as of 2026-09-16T05:39:22Z | n=0 | role=context strength=supporting lane=MD03
- MDS0127: public grant databases | GET https://www.pew.org/search?q=Alignment%20Research%20Center ; r.jina.ai proxy; filters: none => none found in pew.org/search?q=Alignment Research Center as of 2026-09-16T05:39:22Z | n=0 | role=context strength=supporting lane=MD03
- MDS0128: public grant databases | GET https://www.pew.org/search?q=ARC%20Evals ; r.jina.ai proxy; filters: none => none found in pew.org/search?q=ARC Evals as of 2026-09-16T05:39:22Z | n=0 | role=context strength=supporting lane=MD03
- MDS0129: public grant databases | GET https://www.pew.org/en/projects/pew-biomedical-scholars ; in-page text search for METR|Alignment Research Center|ARC Evals|Model Evaluation and Threat Research as whole to => none found in Pew Biomedical Scholars project page as of 2026-09-16T05:41:18Z | n=0 | role=negative strength=supporting lane=MD03
- MDS0130: issuer statements | GET https://www.pew.org/en/about/news-room ; whole-token search METR|Alignment Research Center|ARC Evals|Model Evaluation => none found in pew.org/en/about/news-room as of 2026-09-16T05:41:18Z | n=0 | role=negative strength=supporting lane=MD03
- MDS0131: issuer statements | GET https://www.pew.org/en/about/accountability ; follow linked FY2025 Form 990 PDF and FY2025 financial statements PDF; grep METR/ARC aliases => none found in pew.org/en/about/accountability or the linked FY2025 Form 990 PDF / FY2025 audited financial statements as of 2026-09-16T05:37:30Z | n=0 | role=negative strength=supporting lane=MD03
- MDS0132: issuer statements | GET https://www.pew.org/-/media/assets/2025/12/financialstatements_2025.pdf ; pdftotext; grep METR|Alignment Research Center|ARC Evals|Model Evaluation => none found in The Pew Charitable Trusts consolidated financial statements June 30, 2025 and 2024 as of 2026-09-16T05:37:30Z | n=0 | role=negative strength=supporting lane=MD03
- MDS0133: public grant databases | canonical sitemap + keyword aliases + Pew Biomedical Scholars + news-room; filters: aliases Model Evaluation and Threat Research, METR, Alignment Research Center, ARC Evals => none found in pew.org sitemap, keyword search, Biomedical Scholars listing, or news-room as of 2026-09-16T05:41:18Z | n=0 | role=context strength=supporting lane=MD03
- MDS0134: funder filings | grep RecipientBusinessName/RecipientEIN/text of five IRS 990 XMLs for METR, Model Evaluation and Threat Research, Alignment Research Center, ARC Evals, EIN 99-1219864 => none found in The Pew Charitable Trusts Form 990 Schedule I XML FY2021-FY2025 (FYE 2021-06-30 through 2025-06-30) as of 2026-09-16T05:37:30Z | n=0 | role=negative strength=primary lane=MD03
- MDS0135: issuer statements | pdftotext pew-990-fy2025.pdf and financialstatements_2025.pdf; grep aliases => none found in Pew issuer FY2025 Form 990 PDF as of 2026-09-16T05:37:30Z | n=0 | role=negative strength=supporting lane=MD03
- MDS0136: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202221029349301247_public.xml ; grep Schedule I RecipientBusinessName/RecipientEIN for METR, Model Evaluation and => none found in The Pew Charitable Trusts Form 990 Schedule I FY2021 (tax period 2020-07-01 to 2021-06-30) as of 2026-09-16T05:37:30Z | n=0 | role=negative strength=primary lane=MD03
- MDS0137: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202340889349301359_public.xml ; grep Schedule I RecipientBusinessName/RecipientEIN for METR, Model Evaluation and => none found in The Pew Charitable Trusts Form 990 Schedule I FY2022 (tax period 2021-07-01 to 2022-06-30) as of 2026-09-16T05:37:30Z | n=0 | role=negative strength=primary lane=MD03
- MDS0138: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202440829349300334_public.xml ; grep Schedule I RecipientBusinessName/RecipientEIN for METR, Model Evaluation and => none found in The Pew Charitable Trusts Form 990 Schedule I FY2023 (tax period 2022-07-01 to 2023-06-30) as of 2026-09-16T05:37:30Z | n=0 | role=negative strength=primary lane=MD03
- MDS0139: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202520859349300727_public.xml ; grep Schedule I RecipientBusinessName/RecipientEIN for METR, Model Evaluation and => none found in The Pew Charitable Trusts Form 990 Schedule I FY2024 (tax period 2023-07-01 to 2024-06-30) as of 2026-09-16T05:37:30Z | n=0 | role=negative strength=primary lane=MD03
- MDS0140: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202620849349301332_public.xml ; grep Schedule I RecipientBusinessName/RecipientEIN for METR, Model Evaluation and => none found in The Pew Charitable Trusts Form 990 Schedule I FY2025 (tax period 2024-07-01 to 2025-06-30) as of 2026-09-16T05:37:30Z | n=0 | role=negative strength=primary lane=MD03
- MDS0141: funder filings | ProPublica API GET /nonprofits/api/v2/organizations/562307147.json locator; organization.tax_period=2025-06-01 latest_object_id=202620849349301332; no later object_id => none found in IRS e-file index / ProPublica locator for a Pew Form 990 with tax period after 2025-06 as of 2026-09-16T05:33:05Z | n=0 | role=context strength=supporting lane=MD03
- MDS0142: public grant databases | GET pew.org/site-map + 3 shards (20932 loc); Biomedical Scholars; news-room; filters: aliases METR / Model Evaluation and Threat Research / Alignment Research Center / ARC Eva => none found in Pew public grant listings as of 2026-09-16T05:41:18Z | n=0 | role=negative strength=supporting lane=MD03
- MDS0143: public grant databases | GET /search?q=METR ; /search?q=Model Evaluation and Threat Research ; /search?q=Alignment Research Center ; /search?q=ARC Evals ; r.jina.ai of each; filters: query string only => none found in pew.org keyword search (extractable HTML) as of 2026-09-16T05:39:22Z | n=0 | role=context strength=supporting lane=MD03
- MDS0144: issuer statements | GET financialstatements_2025.pdf; pdftotext; grep aliases; filters: FY2024 and FY2025 consolidated statements => none found in Pew consolidated financial statements June 30, 2025 and 2024 as of 2026-09-16T05:37:30Z | n=0 | role=negative strength=supporting lane=MD03
- MDS0145: issuer statements | GET https://www.pew.org/en/about/accountability and linked FY2025 990 PDF; grep aliases => none found in Pew accountability disclosures as of 2026-09-16T05:37:30Z | n=0 | role=negative strength=supporting lane=MD03
- MDS0146: funder filings | five XML object_ids 202221029349301247, 202340889349301359, 202440829349300334, 202520859349300727, 202620849349301332; filters: Schedule I/F text and EIN 99-1219864; filing years FY2 => none found in The Pew Charitable Trusts Form 990 Schedule I FY2021-FY2025 as of 2026-09-16T05:37:30Z | n=0 | role=negative strength=primary lane=MD03
- MDS0291: public grant databases | GET https://www.pew.org/robots.txt Sitemap=https://www.pew.org/site-map ; then GET the three sitemapfiles shards; filter loc for model-evaluation|threat-research|arc-evals|ali => none found in Pew canonical sitemap shards (10000+10000+remaining locs) as of 2026-09-16T06:16:51Z for a METR/ARC grant page; metr substring hits are metro/metropolitan/biometrics URLs | n=20932 | rol
- MDS0305: public grant databases | Pew site-map + three sitemapfiles shards; loc filter model-evaluation|threat-research|arc-evals => none found in Pew canonical sitemap shards as of 2026-09-16T06:16:51Z for a METR/ARC grant URL | n=0 | role=negative strength=supporting lane=MD13
- MDS0481: funder filings | GET gt990datalake XmlFiles/202620849349301332_public.xml; Schedule I RecipientEIN 951958142 or BusinessName RAND CORPORATION => none found in The Pew Charitable Trusts Form 990 Schedule I object 202620849349301332 (FY2025) for RAND Corporation EIN 95-1958142 as of 2026-09-16T07:21:12Z | n=0 | role=negative strength=supporting 
- MDS0498: funder filings | GET XML 202620849349301332 RecipientTable filter METR|991219864|Alignment Research => none found in The Pew Charitable Trusts Form 990 Schedule I FY2025 (object 202620849349301332) as of 2026-09-16T07:24:42Z | n=0 | role=negative strength=supporting lane=MD23
- MDS0521: issuer statements | GET https://www.pew.org/en/about/accountability ; text search METR|Model Evaluation|Alignment Research => none found in https://www.pew.org/en/about/accountability as of 2026-09-16T07:21:39Z | n=0 | role=negative strength=supporting lane=MD23
- MDS0776: issuer statements | GET anthropic.com Series A, E, F, G, H and /company; HTML search those supporter names => none found in Anthropic Series A/E/F/G/H and /company pages as of 2026-09-16T09:37:25Z for Packard, Pew, Sijbrandij, Audacious, LaCentra-Sumerlin, Astralis, Expa.org, Longview, Effektiv Spenden, David
- MDS1032: public grant databases | GET https://www.pew.org/en/projects/pew-latin-american-fellows ; in-page whole-token search METR|Alignment Research Center|ARC Evals|Model Evaluation and Threat Research => none found in Pew Latin American Fellows project page as of 2026-09-16T09:58:53Z | n=0 | role=negative strength=supporting lane=MD03
- MDS1033: public grant databases | GET https://www.pew.org/en/projects/pew-stewart-scholars-for-cancer-research ; in-page whole-token alias search => none found in Pew-Stewart Scholars for Cancer Research project page as of 2026-09-16T09:58:54Z | n=0 | role=negative strength=supporting lane=MD03
- MDS1034: public grant databases | GET https://www.pew.org/en/projects/marine-fellows ; in-page whole-token alias search => none found in Pew Marine Fellows project page as of 2026-09-16T09:58:56Z | n=0 | role=negative strength=supporting lane=MD03
- MDS1035: public grant databases | GET https://www.pew.org/en/projects/pew-biomedical-scholars/directory-of-pew-scholars (directory page, not the robots-disallowed /search path); in-page whole-token alias searc => none found in Pew Biomedical Scholars directory-of-pew-scholars page as of 2026-09-16T09:58:58Z | n=0 | role=negative strength=supporting lane=MD03
- MDS1036: public grant databases | GET https://www.pew.org/en/about/current-contract-and-grant-opportunities ; in-page whole-token alias search => none found in Pew current contract and grant opportunities page as of 2026-09-16T09:54:48Z | n=0 | role=negative strength=supporting lane=MD03
- MDS1037: funder filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202111059349301696_public.xml ; grep Schedule I RecipientBusinessName/RecipientEIN and Schedule F for METR, Model => none found in The Pew Charitable Trusts Form 990 Schedule I FY2020 (tax period 2019-07-01 to 2020-06-30) as of 2026-09-16T09:58:53Z | n=0 | role=negative strength=supporting lane=MD03
- MDS1038: IRS TEOS and e-file index | GET https://apps.irs.gov/pub/epostcard/990/xml/2026/index_2026.csv filter EIN=562307147; ProPublica API GET /nonprofits/api/v2/organizations/562307147.json locator; organiz => none found in IRS e-file index / ProPublica locator for a Pew Form 990 with tax period after 2025-06 as of 2026-09-16T09:58:49Z | n=0 | role=context strength=supporting lane=MD03
- MDS1272: funder filings | Form 990 Schedule I, FY2021-FY2025 => unbounded in form: result is not 'none found in <exact source> as of <UTC date>' | n=0 | role=context strength=supporting lane=MD50

### Contradictions, duplicates and defects

- MDF0036 / MDF0499 / MDF1011 carry a $38,100,000 filed_grant with from_entity The Pew Charitable Trusts; the recipient is Pew Research Center, not METR. Not a contradiction in the pack, but a trap for any query keyed on payer name.

### Figure notes
Acknowledged only. Primary-strength negatives: Form 990 Schedule I FY2021-FY2025 (MDS0134, MDS0136-MDS0140, MDS0146) plus FY2020 (MDS1037); FY2025 audited statements and 990 PDF (MDS0131/MDS0132/MDS0144). Anchor: MDP0009.


## Schmidt Sciences (brand; paying legal entity not stated)

**How METR names it:** metr.org/about: 'Schmidt Sciences'; 2026-08-14 update: 'Schmidt Sciences'

**Status:** acknowledged, no public amount; which Schmidt legal entity paid is not stated by any source

### Facts (draw only from these)

- **MDF0022** [evidence/primary; lane MD04] untyped (no amount)  | undated | Schmidt Sciences -> Model Evaluation and Threat Research (METR) | status: acknowledged as a supporter; amount, date, vehicle, money type and paying legal entity not disclosed by the source | purpose: n/a
  - ANCHOR (primary): named on metr.org/about; amount, date, purpose, payment status and paying legal entity (LLC vs Fund EIN 46-3460261) not disclosed.
  - url: https://metr.org/about
- **MDE0003** [evidence/primary; lane MD04] untyped (no amount)  | undated | ? -> ? | status: n/a | purpose: n/a
  - Schmidt Sciences, LLC is a 501(c)(3) subsidiary of The Eric and Wendy Schmidt Fund for Strategic Innovation (EIN 46-3460261); no separate 990 filing identity.
  - url: https://www.schmidtsciences.org/faq/
- **MDE0005** [evidence/primary; lane MD04] untyped (no amount)  | undated | ? -> ? | status: n/a | purpose: n/a
  - The Eric and Wendy Schmidt Fund for Strategic Innovation EIN 46-3460261 (990-PF filer).
  - url: https://projects.propublica.org/nonprofits/organizations/463460261
- **MDE0134** [evidence/supporting; lane MD47] untyped (no amount)  | undated | ? -> ? | status: n/a | purpose: n/a
  - Entity separation: Eric Schmidt (individual), Schmidt Sciences LLC, the Fund, Hillspire LLC kept distinct.
  - url: https://www.schmidtsciences.org/faq/
- **MDP0534** [evidence/supporting; lane MD51] untyped (no amount)  | undated | Eric Schmidt -> Schmidt Sciences | status: n/a | purpose: n/a
  - MD51 defect record: posted figure metr-11 merged Schmidt Sciences with Eric Schmidt; Anthropic Series A names the individual, METR names the brand.
  - url: https://api.github.com/repositories/1370599694/contents/figures/metr-11-same-donors-both-sides-of-the-table.html?ref=f64df65a16400fd88a77536111851695acc9a928
- **MDT0075** [evidence/primary; lane MD24] untyped (no amount)  | 2025-12-07 | ? -> METR | status: n/a | purpose: n/a
  - About-page first appearance bounded 2025-12-03 to 2025-12-07.
  - url: https://web.archive.org/web/20251207085707id_/https://metr.org/about
- **MDF0214** [context/supporting; lane MD33] untyped (no amount)  | undated | Schmidt Sciences -> Model Evaluation and Threat Research (METR) | status: n/a | purpose: n/a
  - MD33: named; paying entity unstated.
  - url: https://metr.org/about

### Restatement / locator rows (do not cite as new facts)

MDF0485, MDF0677, MDP0054, MDP0183, MDP0520, MDP0599, MDP0721, MDE0004, MDE0006, MDE0007, MDE0008, MDE0009, MDE0059, MDE0060, MDE0061, MDE0062, MDE0118, MDE0120, MDT0074

### Timeline rows

MDT0074, MDT0075

### Bounded negatives

Counts (live): 19 rows; by source class: SEC 2, funder filings 9, issuer statements 4, public grant databases 2, recipient filings 1, state registries 1
- MDS0046: issuer statements | GET https://www.schmidtsciences.org/awardees/?search=METR filters=search string METR; renderer=r.jina.ai plus live HTML; also search=Alignment Research and search=Model Evaluation; => none found in schmidtsciences.org/awardees/?search=METR as of 2026-09-16T05:37:01Z | n=0 | role=context strength=supporting lane=MD04
- MDS0047: funder filings | grep GrantOrContributionPdDurYrGrp (n=379) and GrantOrContriApprvForFutGrp (n=50) in XML 202543219349108364 for METR|MODEL EVALUATION|ALIGNMENT RESEARCH|99-1219864|86-3605182 => none found in Form 990-PF Part XV of EIN 46-3460261 TY2024 object 202543219349108364 as of 2026-09-16T05:33:57Z | n=0 | role=negative strength=primary lane=MD04
- MDS0048: funder filings | grep GrantOrContributionPdDurYrGrp (n=695) and GrantOrContriApprvForFutGrp (n=165) in XML 202513219349104316 for METR|MODEL EVALUATION|ALIGNMENT RESEARCH|THREAT RESEARCH => none found in Form 990-PF Part XV of EIN 20-4170342 TY2024 object 202513219349104316 as of 2026-09-16T05:40:52Z | n=0 | role=negative strength=primary lane=MD04
- MDS0049: funder filings | GrantOrContributionPdDurYrGrp count and GrantOrContriApprvForFutGrp count in XML 202512279349100406 => none found in Form 990-PF Part XV of EIN 99-5077186 TY2024 object 202512279349100406 as of 2026-09-16T05:40:52Z | n=0 | role=negative strength=supporting lane=MD04
- MDS0050: funder filings | grep 19 paid GrantOrContributionPdDurYrGrp and GrantOrContriApprvForFutGrp in XML 202513199349101171 for METR|MODEL EVALUATION|ALIGNMENT RESEARCH => none found in Form 990-PF Part XV of EIN 26-4562328 TY2024 object 202513199349101171 as of 2026-09-16T05:40:52Z | n=0 | role=negative strength=primary lane=MD04
- MDS0051: funder filings | GET https://projects.propublica.org/nonprofits/api/v2/search.json?q=Schmidt%20Sciences%20LLC => none found in ProPublica Nonprofit Explorer search.json?q=Schmidt Sciences LLC as of 2026-09-16T05:43:51Z | n=0 | role=negative strength=supporting lane=MD04
- MDS0292: public grant databases | GET https://www.schmidtsciences.org/wp-json/wp/v2/types then GET /wp-json/wp/v2/profile_2025?per_page=100 (X-WP-Total=35); also GET /wp-json/wp/v2/profile_2025?search=METR (to => none found in Schmidt Sciences profile_2025 CPT (n=35) as of 2026-09-16T06:16:44Z for METR/ARC/Model Evaluation and Threat Research | n=35 | role=negative strength=supporting lane=MD13
- MDS0306: public grant databases | WP REST profile_2025 n=35 plus search=METR total=0 => none found in Schmidt Sciences profile_2025 search=METR as of 2026-09-16T06:16:47Z | n=0 | role=negative strength=supporting lane=MD13
- MDS0499: issuer statements | GET https://www.schmidtsciences.org/awardees/?search=METR ; in-HTML search Model Evaluation|Alignment Research => none found in schmidtsciences.org/awardees/?search=METR as of 2026-09-16T07:21:39Z | n=0 | role=context strength=supporting lane=MD23
- MDS0500: funder filings | GET XML 202543219349108364 GrantOrContributionPdDurYrGrp/ApprvForFut filter METR|991219864|Alignment Research => none found in Form 990-PF Part XV of EIN 46-3460261 object 202543219349108364 as of 2026-09-16T07:24:42Z | n=0 | role=negative strength=supporting lane=MD23
- MDS0756: issuer statements | GET https://www.anthropic.com/company Governance / Board of Directors => none found in https://www.anthropic.com/company Board of Directors list naming Jaan Tallinn, Dustin Moskovitz, Eric Schmidt, or an observer seat as of 2026-09-16T09:37:25Z | n=0 | role=negative streng
- MDS0758: SEC | SEC EFTS LATEST/search-index q="Eric Schmidt" Anthropic file_date 2020-01-01..2026-09-16 => none found in SEC EFTS q="Eric Schmidt" Anthropic 2020-01-01..2026-09-16 as of 2026-09-16T09:37:52Z | n=0 | role=negative strength=supporting lane=MD33
- MDS0763: state registries | GET https://bizfileonline.sos.ca.gov/ => none found in California SOS bizfileonline.sos.ca.gov as of 2026-09-16T09:38:24Z (Incapsula challenge page, no entity record returned) | n=0 | role=context strength=supporting lane=MD33
- MDS0769: recipient filings | IRS e-file XML 202523209349300367 IRS990ScheduleB ContributorInformationGrp => none found in METR FY2024 public 990 Schedule B as of 2026-09-16T09:37:58Z: contributor fields are RESTRICTED | n=0 | role=negative strength=supporting lane=MD33
- MDS0770: funder filings | grep GrantOrContributionPdDurYrGrp and GrantOrContriApprvForFutGrp in XML 202543219349108364 for METR|MODEL EVALUATION|ALIGNMENT RESEARCH|99-1219864|86-3605182 => none found in Form 990-PF Part XV of EIN 46-3460261 TY2024 object 202543219349108364 as of 2026-09-16T09:38:17Z | n=0 | role=negative strength=supporting lane=MD33
- MDS0774: funder filings | GET https://projects.propublica.org/nonprofits/api/v2/search.json?q=Schmidt%20Sciences%20LLC => none found in ProPublica Nonprofit Explorer search.json?q=Schmidt Sciences LLC as of 2026-09-16T09:38:00Z | n=0 | role=negative strength=supporting lane=MD33
- MDS1040: issuer statements | GET https://www.schmidtsciences.org/wp-json/wp/v2/profile_2025?search=METR&per_page=20 => none found in schmidtsciences.org/wp-json/wp/v2/profile_2025?search=METR as of 2026-09-16T10:02:41Z | n=0 | role=negative strength=supporting lane=MD04
- MDS1221: SEC | GET https://efts.sec.gov/LATEST/search-index?q=%22Schmidt%20Sciences%22%20METR&dateRange=all => none found in SEC EDGAR full-text search (Schmidt Sciences AND METR) as of 2026-09-16T12:30:16Z | n=0 | role=negative strength=supporting lane=MD51
- MDS1273: funder filings | Form 990-PF Part XV, 2021-2024 => unbounded in form: result is not 'none found in <exact source> as of <UTC date>' | n=0 | role=context strength=supporting lane=MD50

### Contradictions, duplicates and defects

- Anthropic Series A participation by Eric Schmidt the individual (MDR0009, MDR0081) and Hillspire LLC press-reported Anthropic investment (MDR0010, MDR0088) are C05 facts about different legal persons; they are not Schmidt Sciences money and must not sit on a METR supporter row.

### Figure notes
Acknowledged only. Primary-strength negatives: 990-PF TY2024 Part XV of the Fund 46-3460261 (MDS0047), Schmidt Family Foundation 20-4170342 (MDS0048), Schmidt Ocean Institute (MDS0050), combined (MDS0053); LLC not a 990 filer (MDS0051). Anchor: MDF0022.


## The David and Lucile Packard Foundation (EIN 94-2278431)

**How METR names it:** metr.org/about: 'the Packard Foundation'; 2026-08-14 update: 'the Packard Foundation'

**Status:** public amount identified: commitment $350,000, award year 2026, 12-month term, for general support (grant 2026-79050); paid vs approved-for-future-payment not determinable until Packard TY2025/TY2026 990-PF is filed

### Facts (draw only from these)

- **MDF0020** [evidence/primary; lane MD02] commitment 350000 USD | 2026 | The David and Lucile Packard Foundation -> Model Evaluation and Threat Research | status: awarded per Packard's catalog; paid or approved-for-future-payment status not determinable until the TY2025 or TY2026 990-PF is posted | purpose: for general support
  - ANCHOR (primary; NEW vs seed): Packard grantee catalog: 1 grant, year 2026, term 12, $350,000, 'for general support'. JSON-LD datePublished 2026-07-06 is a CMS listing timestamp, not the instrument date.
  - url: https://www.packard.org/grantee/model-evaluation-and-threat-research/
- **MDF0021** [context/supporting; lane MD02] commitment 350000 USD | 2026 | The David and Lucile Packard Foundation -> Model Evaluation and Threat Research | status: n/a | purpose: for general support
  - Grant permalink 2026-79050: $350,000, for general support (same award).
  - url: https://www.packard.org/grant/2026-79050/
- **MDF0092** [context/supporting; lane MD14] commitment 350000 USD | 2026-07-06 | The David and Lucile Packard Foundation -> Model Evaluation and Threat Research | status: n/a | purpose: n/a
  - Packard grant-directory-pro API grantee object: total_grants=1, total_grants_amount=350000 (same award; date field here is the API post date 2026-07-06, not a grant day).
  - url: https://www.packard.org/wp-json/grant-directory-pro/v1/grantees
- **MDF0416** [context/supporting; lane MD14] commitment 350000 USD | 2026-07-06 | The David and Lucile Packard Foundation -> Model Evaluation and Threat Research | status: not stated on this page | purpose: n/a
  - API grant object grant_id 2026-79050 grant_amount 350000.00 award_term 12 grant_fiscal_year 2026 (same award).
  - url: https://www.packard.org/wp-json/grant-directory-pro/v1/grants
- **MDP0030** [evidence/primary; lane MD14] commitment 350000 USD | 2026-07-06 | The David and Lucile Packard Foundation -> Model Evaluation and Threat Research | status: not stated on this page | purpose: for general support
  - ANCHOR (primary, C01.E2): the only publicly identified component compatible with the ~$71M Feb-Aug 2026 commitment window, on the basis of the 2026-07-06 listing date, not a signed-grant day.
  - url: https://www.packard.org/grantee/model-evaluation-and-threat-research/
- **MDP0172** [evidence/primary; lane MD23] commitment 350000 USD | undated | The David and Lucile Packard Foundation -> METR | status: n/a | purpose: unrestricted
  - Purpose classification: unrestricted ('for general support').
  - url: https://www.packard.org/grantee/model-evaluation-and-threat-research/
- **MDP0161** [evidence/supporting; lane MD23] untyped (no amount)  | undated | The David and Lucile Packard Foundation -> METR | status: n/a | purpose: funder: for general support; recipient: no Packard-specific purpose on about/funding-update
  - Recipient (metr.org/about) is silent on the Packard purpose; funder states general support.
  - url: https://metr.org/about
- **MDP0589** [evidence/supporting; lane MD50] commitment 350000 USD | 2026-07-06 | The David and Lucile Packard Foundation -> Model Evaluation and Threat Research | status: n/a | purpose: n/a
  - MD50 period-mismatch attack: if the instrument day is before 2026-02-14, Packard is not a window component.
  - url: https://www.packard.org/grantee/model-evaluation-and-threat-research/
- **MDP0591** [evidence/supporting; lane MD50] commitment 350000 USD | undated | The David and Lucile Packard Foundation -> ? | status: n/a | purpose: n/a
  - MD50 cross-type attack: a catalog award listing is typed commitment; paid vs approved waits on the 990-PF.
  - url: https://www.packard.org/grantee/model-evaluation-and-threat-research/
- **MDP0585** [evidence/supporting; lane MD50] commitment 350000 USD | 2026-07-06 | The David and Lucile Packard Foundation -> Model Evaluation and Threat Research | status: n/a | purpose: n/a
  - MD50 double-count attack: the same $350,000 sits on MDF0020, MDF0021, MDF0078, MDF0090, MDF0091, MDF0092, MDF0191, MDF0192, MDF0193, MDF0416 and three recon lines; count once.
  - url: https://www.packard.org/grantee/model-evaluation-and-threat-research/
- **MDP0056** [evidence/supporting; lane MD14] commitment 70650000 USD | the last 6 months as of 2026-08-14 | ? -> METR | status: n/a | purpose: n/a
  - Commitment reconciliation remainder: ~$71,000,000 minus $350,000 = ~$70,650,000 unresolved (arithmetic gap, not a donor list).
  - url: https://metr.org/blog/2026-08-14-funding-update/
- **MDT0010** [evidence/supporting; lane MD02] untyped (no amount)  | 2026-07-06 | The David and Lucile Packard Foundation -> Model Evaluation and Threat Research | status: n/a | purpose: n/a
  - Packard page metadata: datePublished 2026-07-06T06:09:41Z; dateModified 2026-09-14T06:08:32Z.
  - url: https://www.packard.org/grantee/model-evaluation-and-threat-research/
- **MDT0103** [evidence/primary; lane MD24] untyped (no amount)  | 2026-07-06 | ? -> METR | status: n/a | purpose: n/a
  - About-page first appearance of the Packard name bounded 2026-06-29 to 2026-07-06.
  - url: https://web.archive.org/web/20260706232641id_/https://metr.org/about
- **MDE0002** [evidence/primary; lane MD02] untyped (no amount)  | undated | ? -> Model Evaluation and Threat Research | status: n/a | purpose: n/a
  - Packard lists the grantee as Model Evaluation and Threat Research, website metr.org.
  - url: https://www.packard.org/grantee/model-evaluation-and-threat-research/
- **MDF0226** [context/supporting; lane MD33] untyped (no amount)  | undated | The David and Lucile Packard Foundation -> METR (Model Evaluation and Threat Research) | status: n/a | purpose: n/a
  - MD33: named on metr.org/about; amount not on that page.
  - url: https://metr.org/about

### Restatement / locator rows (do not cite as new facts)

MDF0078, MDF0090, MDF0091, MDF0191, MDF0192, MDF0193, MDF0483, MDF0484, MDF0541, MDF0553, MDF0554, MDF0555, MDF0654, MDF0655, MDF0656, MDF0689, MDF0879, MDF0963, MDF0967, MDF0989, MDF1022, MDF1030, MDF1031, MDP0480, MDP0496, MDP0520, MDP0527, MDP0598, MDP0603, MDP0634, MDP0635, MDP0653, MDP0654, MDP0677, MDP0692, MDP0722, MDP0741, MDP0743, MDE0072, MDT0102, MDT0122

### Timeline rows

MDT0010, MDT0102, MDT0103, MDT0122

### Bounded negatives

Counts (live): 33 rows; by source class: IRS TEOS and e-file index 2, archives 5, funder filings 8, issuer statements 3, public grant databases 15
- MDS0024: public grant databases | GET https://www.packard.org/sitemap_index.xml then GET grantee-sitemap.xml and grantee-sitemap2.xml; filter loc contains model-evaluation-and-threat-research => METR grantee slug present in grantee-sitemap2.xml (278 loc, lastmod 2026-09-14T06:08:32Z); absent from grantee-sitemap.xml (1001 loc) | n=1 | role=evidence strength=supporting lane=MD02
- MDS0025: public grant databases | GET https://www.packard.org/grantee-sitemap.xml; filter loc=https://www.packard.org/grantee/model-evaluation-and-threat-research/ => none found in https://www.packard.org/grantee-sitemap.xml (1001 loc) as of 2026-09-16T05:33:23Z; METR loc is on sitemap2 | n=0 | role=negative strength=supporting lane=MD02
- MDS0026: public grant databases | GET https://www.packard.org/wp-json/grant-directory-pro/v1/grantees and GET https://www.packard.org/wp-json/grant-directory-pro/v1/grants; match post_name=model-evaluation-and => grant-directory-pro/v1 full catalog: 1278 grantees, 2557 grants; exactly one METR grantee (ID 2703989) and one grant 2026-79050 at 350000.00 | n=1 | role=evidence strength=primary lane=MD02
- MDS0027: public grant databases | GET https://www.packard.org/grantees/search-our-grants/?grant_keyword=Model%20Evaluation filters: funding_area empty (All Funding Areas) => keyword grant_keyword=Model Evaluation returns 1 grantee | n=1 | role=context strength=supporting lane=MD02
- MDS0028: public grant databases | GET https://www.packard.org/grantees/search-our-grants/?grant_keyword=Model%20Evaluation%20and%20Threat%20Research filters: funding_area empty => keyword grant_keyword=Model Evaluation and Threat Research returns 1 grantee | n=1 | role=context strength=supporting lane=MD02
- MDS0029: public grant databases | GET https://www.packard.org/grantees/search-our-grants/?grant_keyword=METR filters: funding_area empty => none found in Packard search-our-grants grant_keyword=METR as of 2026-09-16T05:36:05Z for Model Evaluation and Threat Research; 3 substring hits are Black Lives Matter Phoenix Metro, Fresno Metropolit
- MDS0030: public grant databases | GET https://www.packard.org/grantees/search-our-grants/?grant_keyword=Alignment%20Research%20Center filters: funding_area empty => none found in Packard search-our-grants grant_keyword=Alignment Research Center as of 2026-09-16T05:36:05Z | n=0 | role=negative strength=supporting lane=MD02
- MDS0031: public grant databases | GET https://www.packard.org/grantees/search-our-grants/?grant_keyword=ARC%20Evals filters: funding_area empty => none found in Packard search-our-grants grant_keyword=ARC Evals as of 2026-09-16T05:37:37Z | n=0 | role=negative strength=supporting lane=MD02
- MDS0032: public grant databases | GET https://www.packard.org/grantees/search-our-grants/?grant_keyword=ARC filters: funding_area empty => 91 grantee substring hits including Model Evaluation and Threat Research (token ARC inside Research); not a distinct Alignment Research Center award | n=91 | role=context strength=supporting lane=MD02
- MDS0034: funder filings | IRS e-file index EIN 942278431 -> GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202533209349100148_public.xml ; search RecipientBusinessName/BusinessNameLine1T => none found in Packard Form 990-PF TY2024 OBJECT_ID=202533209349100148 Part XV GrantOrContributionPdDurYrGrp (n=2058) and GrantOrContriApprvForFutGrp (n=366) as of 2026-09-16T05:40:37Z | n=0 | role=neg
- MDS0035: funder filings | IRS e-file index EIN 942278431 -> GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202433199349102603_public.xml ; search RecipientBusinessName/BusinessNameLine1T => none found in Packard Form 990-PF TY2023 OBJECT_ID=202433199349102603 Part XV GrantOrContributionPdDurYrGrp (n=2194) and GrantOrContriApprvForFutGrp (n=256) as of 2026-09-16T05:40:37Z | n=0 | role=neg
- MDS0036: funder filings | IRS e-file index EIN 942278431 -> GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202303149349102680_public.xml ; search RecipientBusinessName/BusinessNameLine1T => none found in Packard Form 990-PF TY2022 OBJECT_ID=202303149349102680 Part XV GrantOrContributionPdDurYrGrp (n=2316) and GrantOrContriApprvForFutGrp (n=378) as of 2026-09-16T05:40:37Z | n=0 | role=neg
- MDS0037: funder filings | IRS e-file index EIN 942278431 -> GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202223199349107432_public.xml ; search RecipientBusinessName/BusinessNameLine1T => none found in Packard Form 990-PF TY2021 OBJECT_ID=202223199349107432 Part XV GrantOrContributionPdDurYrGrp (n=2800) and GrantOrContriApprvForFutGrp (n=372) as of 2026-09-16T05:40:37Z | n=0 | role=neg
- MDS0038: IRS TEOS and e-file index | GET https://apps.irs.gov/pub/epostcard/990/xml/2026/index_2026.csv streamed; grep -F ,942278431, ; Content-Length=47506032 => none found in IRS e-file index_2026.csv for EIN 942278431 as of 2026-09-16T05:40:37Z | n=0 | role=negative strength=supporting lane=MD02
- MDS0039: archives | GET https://web.archive.org/cdx/search/cdx?url=www.packard.org/grantee/model-evaluation-and-threat-research/&output=json&fl=timestamp,original,statuscode,digest,length&filter=statuscode:200 => none found in Wayback CDX for the grantee URL as of 2026-09-16T05:37:37Z (0 rows) | n=0 | role=negative strength=supporting lane=MD02
- MDS0040: archives | GET https://web.archive.org/cdx/search/cdx?url=www.packard.org/grant/2026-79050/&output=json&fl=timestamp,original,statuscode,digest,length&filter=statuscode:200&collapse=digest => none found in Wayback CDX for https://www.packard.org/grant/2026-79050/ as of 2026-09-16T05:37:37Z | n=0 | role=negative strength=supporting lane=MD02
- MDS0041: funder filings | Part XV RecipientBusinessName search of OBJECT_IDs 202223199349107432, 202303149349102680, 202433199349102603, 202533209349100148 => none found in Packard Form 990-PF Part XV TY2021-TY2024 as of 2026-09-16T05:40:37Z | n=0 | role=negative strength=primary lane=MD02
- MDS0042: IRS TEOS and e-file index | GET https://apps.irs.gov/app/eos/input?ein=942278431 => none found in IRS TEOS HTML input?ein=942278431 as of 2026-09-16T05:37:37Z (HTTP 403 Access Denied) | n=0 | role=context strength=supporting lane=MD02
- MDS0043: archives | Wayback CDX for grantee and grant permalinks; GET https://web.archive.org/web/2026*/https://www.packard.org/grantee/model-evaluation-and-threat-research/ => none found in Wayback CDX/calendar for the Packard METR grantee and grant URLs as of 2026-09-16T05:37:37Z | n=0 | role=negative strength=supporting lane=MD02
- MDS0045: public grant databases | GET https://www.packard.org/grantees/search-our-grants/?grant_keyword=Alignment%20Research filters: funding_area empty => none found in Packard search-our-grants grant_keyword=Alignment Research as of 2026-09-16T05:37:37Z | n=0 | role=negative strength=supporting lane=MD02
- MDS0289: public grant databases | GET https://www.packard.org/wp-json/grant-directory-pro/v1/grantees and GET .../v1/grants ; match post_name=model-evaluation-and-threat-research and grant_id=2026-79050 => grant-directory-pro/v1 full catalog re-enumerated: 1278 grantees, 2557 grants; exactly one METR grantee and one grant 2026-79050 at 350000.00; no ARC grantee | n=2557 | role=evidence strength=supporti
- MDS0290: public grant databases | GET https://www.packard.org/sitemap_index.xml then GET grantee-sitemap.xml (1001 loc) and grantee-sitemap2.xml (278 loc); filter loc contains model-evaluation-and-threat-resea => Canonical sitemap index lists grantee-sitemap.xml (1001 loc, METR slug absent) and grantee-sitemap2.xml (278 loc, METR slug present). Combined grantee loc excluding index = 1278, matching API grantee 
- MDS0342: public grant databases | GET https://www.packard.org/wp-json/grant-directory-pro/v1/search?s=METR => none found in https://www.packard.org/wp-json/grant-directory-pro/v1/search?s=METR as of 2026-09-16T06:05:27Z | n=0 | role=context strength=supporting lane=MD14
- MDS0513: issuer statements | GET https://www.packard.org/grantee/model-evaluation-and-threat-research/ => none found in the Packard grantee/grant documents as of 2026-09-16T07:21:33Z of a restriction that would make the $350,000 incompatible with a METR general-support commitment; incompatibility if any w
- MDS0771: funder filings | GET https://www.packard.org/grants-and-investments/grants-database/ HTML search METR|Model Evaluation => none found in packard.org/grants-and-investments/grants-database/ live HTML for METR or Model Evaluation as of 2026-09-16T09:38:41Z | n=0 | role=negative strength=supporting lane=MD33
- MDS0776: issuer statements | GET anthropic.com Series A, E, F, G, H and /company; HTML search those supporter names => none found in Anthropic Series A/E/F/G/H and /company pages as of 2026-09-16T09:37:25Z for Packard, Pew, Sijbrandij, Audacious, LaCentra-Sumerlin, Astralis, Expa.org, Longview, Effektiv Spenden, David
- MDS0811: archives | GET https://web.archive.org/cdx/search/cdx?url=www.packard.org/grantee/model-evaluation-and-threat-research/&output=json&fl=timestamp,original,statuscode,digest,length&filter=statuscode:200 => none found in Wayback CDX for https://www.packard.org/grantee/model-evaluation-and-threat-research/ as of 2026-09-16T09:51:35Z (HTTP 503 Temporarily Offline; not a capture list) | n=0 | role=context s
- MDS1031: archives | GET https://web.archive.org/__wb/sparkline?url=https://www.packard.org/grantee/model-evaluation-and-threat-research/&output=json => none found in Wayback sparkline for https://www.packard.org/grantee/model-evaluation-and-threat-research/ as of 2026-09-16T09:57:58Z (first_ts=null last_ts=null years empty) | n=0 | role=negative stre
- MDS1177: public grant databases | GET https://www.packard.org/wp-json/grant-directory-pro/v1/search?s=METR => none found in https://www.packard.org/wp-json/grant-directory-pro/v1/search?s=METR as of 2026-09-16T12:22:15Z | n=0 | role=context strength=supporting lane=MD46
- MDS1271: funder filings | Form 990-PF Part XV, 2021-2024 => unbounded in form: result is not 'none found in <exact source> as of <UTC date>'; 2021-2024 Packard 990-PF Part XV would not have carried the 2026 catalog award later promoted as the compatible compon
- MDS1602: issuer statements | GET https://metr.org/about ; filter dollar amounts next to named supporters other than the Packard catalog (separate URL) => none found in https://metr.org/about as of 2026-09-16T16:45:13Z of a public amount, vehicle or gift date for individuals from Jane Street, Sijbrandij Foundation, The Pew Charitable Trusts, Schmidt Sci
- MDS1603: funder filings | GET https://www.packard.org/grantee/model-evaluation-and-threat-research/ ; filter signed-grant day, paid vs approved, 2026-79050 => none found in https://www.packard.org/grantee/model-evaluation-and-threat-research/ as of 2026-09-16T16:45:13Z of a signed-grant day, paid-versus-approved status, or the string 2026-79050 | n=0 | role
- MDS1613: public grant databases | GET Packard grantee catalog (live) as the public grant-database re-verify of the compatible component => none found in https://www.packard.org/grantee/model-evaluation-and-threat-research/ as of 2026-09-16T16:45:13Z of a second METR grant line besides 1 Grants / $350,000 | n=0 | role=negative strength=su

### Contradictions, duplicates and defects

- Date field differs by row for one award: '2026' (year precision) on MDF0020/MDF0021/MDF0078/MDF0191-0193/MDF0483; '2026-07-06' (day precision) on MDF0091/MDF0092/MDF0416/MDP0030/MDP0496/MDT0122. The day is the catalog listing datePublished, not a signed-grant date; a figure must not present 2026-07-06 as the grant date.
- Payment status text differs: MDF0020 says awarded per catalog, paid-vs-approved not determinable; MDF0090/MDF0091 say not stated on this page. Consistent in substance: no payment status is public.
- Review verdicts: MDF0020 and MDF0090 are DIFFERS (reviewer changed fields), MDF0021/MDF0078/MDF0091/MDF0092 CONFIRMED. Amount is identical on all.

### Figure notes
One $350,000 commitment, award year 2026, term 12 months, general support; listing published 2026-07-06; payment unknown. It is the sole identified compatible component of METR's ~$71M (MDP0030) and the seed baseline did not contain it (new information from MD02). Primary-strength negatives: Packard 990-PF Part XV TY2021-TY2024 (MDS0034-MDS0037, MDS0041); index_2026 no TY2025 (MDS0038); catalog search METR none (MDS0029); paid-vs-approved not on page (MDS1603, MDS1690).


## LaCentra-Sumerlin Foundation (EIN 77-0416683; FYE 30 Nov)

**How METR names it:** metr.org/about: 'LaCentra-Sumerlin Foundation' (earlier captures 'La Centra-Sumerlin Foundation'); 2026-08-14 update image alt: 'LaCentra-Sumerlin Foundation Frontier Fund'

**Status:** acknowledged, no public amount

### Facts (draw only from these)

- **MDR0021** [evidence/primary; lane MD06] untyped (no amount)  | undated | LaCentra-Sumerlin Foundation -> METR | status: n/a | purpose: n/a
  - ANCHOR (primary): acknowledged on the recipient list; amount, date, vehicle, purpose not disclosed.
  - url: https://metr.org/about
- **MDE0020** [evidence/primary; lane MD06] untyped (no amount)  | undated | ? -> ? | status: n/a | purpose: n/a
  - Legal entity: LA CENTRA-SUMERLIN FOUNDATION EIN 77-0416683, private non-operating foundation, FYE 2024-11-30.
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202502889349100435_public.xml
- **MDE0026** [evidence/supporting; lane MD06] untyped (no amount)  | undated | ? -> ? | status: n/a | purpose: n/a
  - Frontier Fund is an invitation-only sub-fund of the same EIN, not a separate legal entity.
  - url: https://www.lcsf.org/
- **MDT0019** [evidence/supporting; lane MD06] untyped (no amount)  | 2026-08-14 | LaCentra-Sumerlin Foundation Frontier Fund -> METR | status: n/a | purpose: n/a
  - 2026-08-14 update image alt labels the supporter 'LaCentra-Sumerlin Foundation Frontier Fund'; no amount.
  - url: https://metr.org/blog/2026-08-14-funding-update/
- **MDT0020** [evidence/supporting; lane MD06] untyped (no amount)  | 2025-12-16 | LaCentra-Sumerlin Foundation -> METR | status: n/a | purpose: n/a
  - Named on the 2025-12-16 about capture; absent on 2025-12-07 (explains why FYE Nov 2024 990-PF has no METR line without implying a gift date).
  - url: https://web.archive.org/web/20251216013159/https://metr.org/about
- **MDT0093** [evidence/primary; lane MD24] untyped (no amount)  | 2025-12-16 | ? -> METR | status: n/a | purpose: n/a
  - About-page first appearance bounded 2025-12-07 to 2025-12-16.
  - url: https://web.archive.org/web/20251216013159id_/https://metr.org/about
- **MDT0073** [context/supporting; lane MD24] untyped (no amount)  | 2026-08-18 | ? -> METR | status: n/a | purpose: n/a
  - Spelling change La Centra -> LaCentra between 2026-08-04 and 2026-08-18 captures (not a new gift).
  - url: https://web.archive.org/web/20260818223548id_/https://metr.org/about
- **MDF0227** [context/supporting; lane MD33] untyped (no amount)  | undated | LaCentra-Sumerlin Foundation -> METR (Model Evaluation and Threat Research) | status: n/a | purpose: n/a
  - MD33: named; amount not on page.
  - url: https://metr.org/about

### Restatement / locator rows (do not cite as new facts)

MDF0690, MDP0054, MDP0183, MDP0520, MDP0599, MDP0723, MDE0021, MDE0073, MDT0072, MDT0092

### Timeline rows

MDT0019, MDT0020, MDT0072, MDT0073, MDT0092, MDT0093

### Bounded negatives

Counts (live): 17 rows; by source class: IRS TEOS and e-file index 2, funder filings 4, issuer statements 3, public grant databases 2, self-statements 3, state registries 3; DEAD cited: MDS0151
- MDS0148: self-statements | GET https://www.lcsf.org/frontier => none found in https://www.lcsf.org/frontier as of 2026-09-16T05:40:32Z | n=0 | role=negative strength=supporting lane=MD06
- MDS0151 (DEAD): funder filings | grep METR|Model Evaluation|Threat Research|Alignment Research|ARC EVALS|99-1219864|86-3605182 in object_ids 202202909349100745, 202311029349102446, 202402889349101005, 202502889349100 => none found in LaCentra-Sumerlin Foundation Forms 990-PF FYE Nov 2021, Nov 2022, Nov 2023, and Nov 2024 XML grant schedules as of 2026-09-16T05:37:38Z | n=0 | role=negative strength=primary lane=MD06 |
- MDS0155: funder filings | ProPublica org page filings list; GET /nonprofits/organizations/770416683/202511 => Public filing route exists: US Form 990-PF (private foundation). Latest object 202502889349100435 (FYE Nov 2024). GET .../202511 returned HTTP 404 as of 2026-09-16T05:41:32Z. | n=1 | role=context stre
- MDS0158: IRS TEOS and e-file index | GET https://apps.irs.gov/app/eos/details/?Ein=770416683 => none found in IRS TEOS interactive details page for EIN 770416683 as of 2026-09-16T05:35:40Z (HTTP 403 Access Denied) | n=0 | role=context strength=supporting lane=MD06
- MDS0159: state registries | GET https://rct.doj.ca.gov/Verification/Web/Search.aspx?facility=Y => none found in https://rct.doj.ca.gov/Verification/Web/Search.aspx?facility=Y as of 2026-09-16T05:39:22Z (HTTP 404) | n=0 | role=context strength=supporting lane=MD06
- MDS0165: self-statements | GET https://www.lcsf.org/grants ; text search METR|Model Evaluation|ARC => none found in https://www.lcsf.org/grants as of 2026-09-16T05:37:48Z for METR/ARC | n=0 | role=negative strength=supporting lane=MD06
- MDS0167: funder filings | Form 990-PF Part XV XML grep METR/ARC aliases, object_id 202502889349100435 and three prior years => none found in LaCentra-Sumerlin Foundation 990-PF XML grant schedules FYE Nov 2021-Nov 2024 as of 2026-09-16T05:37:38Z | n=0 | role=negative strength=primary lane=MD06
- MDS0294: public grant databases | GET https://www.lcsf.org/sitemap.xml (7 loc: /home /carpinteria /hea /frontier /grants /loi /application) then GET /grants and /frontier ; text search METR|ARC => none found in LaCentra-Sumerlin sitemap (7 loc) or grants/frontier pages as of 2026-09-16T06:07:21Z for METR/ARC | n=7 | role=negative strength=supporting lane=MD13
- MDS0308: public grant databases | sitemap.xml 7 loc + /grants + /frontier => none found in https://www.lcsf.org/grants as of 2026-09-16T06:07:20Z for METR/ARC | n=0 | role=negative strength=supporting lane=MD13
- MDS0501: issuer statements | GET https://www.lcsf.org/frontier ; text search METR|Model Evaluation|ARC => none found in https://www.lcsf.org/frontier as of 2026-09-16T07:21:40Z | n=0 | role=negative strength=supporting lane=MD23
- MDS0502: funder filings | GET XML 202502889349100435 filter METR|991219864|Alignment Research => none found in LaCentra-Sumerlin Foundation Form 990-PF FYE 2024-11-30 grant schedule as of 2026-09-16T07:24:42Z | n=0 | role=negative strength=supporting lane=MD23
- MDS0522: issuer statements | GET https://www.lcsf.org/grants ; text search METR|Model Evaluation|ARC => none found in https://www.lcsf.org/grants as of 2026-09-16T07:21:40Z | n=0 | role=negative strength=supporting lane=MD23
- MDS0776: issuer statements | GET anthropic.com Series A, E, F, G, H and /company; HTML search those supporter names => none found in Anthropic Series A/E/F/G/H and /company pages as of 2026-09-16T09:37:25Z for Packard, Pew, Sijbrandij, Audacious, LaCentra-Sumerlin, Astralis, Expa.org, Longview, Effektiv Spenden, David
- MDS1047: self-statements | GET https://www.lcsf.org/frontier ; text search METR|Model Evaluation|ARC => none found in https://www.lcsf.org/frontier as of 2026-09-16T10:01:13Z | n=0 | role=negative strength=supporting lane=MD06
- MDS1048: IRS TEOS and e-file index | GET https://apps.irs.gov/pub/epostcard/990/xml/2026/index_2026.csv streamed; filter EIN 770416683 or 832856275 => none found in IRS e-file index_2026.csv for EIN 770416683 or 832856275 as of 2026-09-16T10:01:32Z | n=0 | role=context strength=supporting lane=MD06
- MDS1050: state registries | GET https://rct.doj.ca.gov/Verification/Web/Search.aspx?facility=Y => none found in https://rct.doj.ca.gov/Verification/Web/Search.aspx?facility=Y as of 2026-09-16T10:01:20Z (HTTP 404) | n=0 | role=context strength=supporting lane=MD06
- MDS1057: state registries | GET https://bizfileonline.sos.ca.gov/search/business => none found in CA SOS bizfileonline search/business as of 2026-09-16T10:01:20Z (JS/iframe challenge; no EIN lookup possible in this fetch) | n=0 | role=context strength=supporting lane=MD06
- MDS1059: funder filings | Form 990-PF Part XV XML grep METR/ARC aliases, object_id 202502889349100435 and three prior years => none found in LaCentra-Sumerlin Foundation 990-PF XML grant schedules FYE Nov 2021-Nov 2024 as of 2026-09-16T10:01:25Z | n=0 | role=negative strength=supporting lane=MD06

### Contradictions, duplicates and defects

- DEFECT: supporter_coverage.csv (lacentra negative_rows) and MDP0723 cite MDS0151, which is DEAD (superseded by MDS1059). Use MDS1059 and MDS0167 for the 990-PF FYE Nov 2021-Nov 2024 negative.

### Figure notes
Acknowledged only; the FYE Nov 2025 990-PF is the calendar closer. Primary-strength negative: MDS0167 (990-PF FYE Nov 2021-Nov 2024 grant schedules); index_2026 none (MDS1048). Anchor: MDR0021.


## Astralis Foundation (Stiftelsen Astralis 802482-2317, Sweden; ASTRALIS FOUNDATION UK company 15917880)

**How METR names it:** metr.org/about: 'Astralis Foundation'; 2026-08-14 update image alt: 'Astralis Foundation'

**Status:** acknowledged, no public amount; no US Form 990 route exists

### Facts (draw only from these)

- **MDR0022** [evidence/primary; lane MD06] untyped (no amount)  | undated | Astralis Foundation -> METR | status: n/a | purpose: n/a
  - ANCHOR (primary): acknowledged on the recipient list; no amount, date, vehicle or purpose.
  - url: https://metr.org/about
- **MDE0022** [evidence/primary; lane MD06] untyped (no amount)  | undated | ? -> ? | status: n/a | purpose: n/a
  - Swedish foundation Stiftelsen Astralis, org.nr 802482-2317 (avkastningsstiftelse).
  - url: https://astralisfoundation.org/
- **MDE0023** [evidence/primary; lane MD06] untyped (no amount)  | undated | ? -> ? | status: n/a | purpose: n/a
  - UK company ASTRALIS FOUNDATION 15917880, incorporated 2024-08-27, company limited by guarantee; not a registered charity.
  - url: https://find-and-update.company-information.service.gov.uk/company/15917880
- **MDE0126** [evidence/supporting; lane MD06] untyped (no amount)  | undated | ? -> ? | status: n/a | purpose: n/a
  - Swedish stiftelseregister record ID 1032015 (identity only, no grant schedule).
  - url: https://stiftelser.lansstyrelsen.se/Öppendata/Json
- **MDT0021** [evidence/supporting; lane MD06] untyped (no amount)  | 2025-12-07 | Astralis Foundation -> METR | status: n/a | purpose: n/a
  - Named on the 2025-12-07 about capture (appearance, not a transaction).
  - url: https://web.archive.org/web/20251207085707/https://metr.org/about
- **MDT0077** [evidence/primary; lane MD24] untyped (no amount)  | 2025-12-07 | ? -> METR | status: n/a | purpose: n/a
  - About-page first appearance bounded 2025-12-03 to 2025-12-07.
  - url: https://web.archive.org/web/20251207085707id_/https://metr.org/about
- **MDF0228** [context/supporting; lane MD33] untyped (no amount)  | undated | Astralis Foundation -> METR (Model Evaluation and Threat Research) | status: n/a | purpose: n/a
  - MD33: named; amount not on page.
  - url: https://metr.org/about

### Restatement / locator rows (do not cite as new facts)

MDF0691, MDP0054, MDP0183, MDP0520, MDP0724, MDE0074, MDE0127, MDT0076, MDT0223

### Timeline rows

MDT0021, MDT0076, MDT0077, MDT0223

### Bounded negatives

Counts (live): 18 rows; by source class: IRS TEOS and e-file index 1, funder filings 2, issuer statements 2, public grant databases 2, self-statements 3, state registries 8
- MDS0149: self-statements | GET https://astralisfoundation.org/ => none found in https://astralisfoundation.org/ as of 2026-09-16T05:40:36Z | n=0 | role=negative strength=supporting lane=MD06
- MDS0153: funder filings | Companies House AA Total exemption full accounts made up to 31 August 2025; iXBRL transaction MzUyMzA0OTE1M2FkaXF6a2N4 => none found in ASTRALIS FOUNDATION UK accounts for the period ended 2025-08-31 as of 2026-09-16T05:43:08Z | n=0 | role=negative strength=primary lane=MD06
- MDS0154: IRS TEOS and e-file index | ProPublica API v2 search.json?q=Astralis Foundation => none found in ProPublica Nonprofit Explorer search 'Astralis Foundation' as of 2026-09-16T05:35:33Z for an exact Astralis Foundation US filer | n=0 | role=negative strength=supporting lane=MD06
- MDS0157: state registries | no US 990; UK P&L withheld; Swedish stiftelseregister URL this fetch => none found in US Form 990/990-PF index (ProPublica search 'Astralis Foundation') as of 2026-09-16T05:35:33Z. Reason: foreign Swedish foundation plus UK company limited by guarantee; neither is a US 99
- MDS0161: state registries | Charity Commission register search q=Astralis (r.jina.ai extract) => none found in Charity Commission register search 'Astralis' as of 2026-09-16T05:41:15Z | n=0 | role=context strength=supporting lane=MD06
- MDS0162: state registries | GET https://www.bolagsfakta.se/8024822317-STIFTELSEN_ASTRALIS via r.jina.ai => none found in bolagsfakta.se/8024822317-STIFTELSEN_ASTRALIS as of 2026-09-16T05:40:46Z (HTTP 403 Cloudflare) | n=0 | role=context strength=supporting lane=MD06
- MDS0163: state registries | GET https://www.lanstyrelsen.se/stockholm/naringsliv-och-foreningar/stiftelser/ => none found in https://www.lanstyrelsen.se/stockholm/naringsliv-och-foreningar/stiftelser/ as of 2026-09-16T05:43:21Z (HTTP 404) | n=0 | role=context strength=supporting lane=MD06
- MDS0164: self-statements | GET https://astralisfoundation.org/grants => none found in https://astralisfoundation.org/grants as of 2026-09-16T05:35:23Z (HTTP 404) | n=0 | role=negative strength=supporting lane=MD06
- MDS0169: funder filings | UK accounts iXBRL YE 2025-08-31; no P&L; grep METR/ARC => none found in ASTRALIS FOUNDATION UK accounts YE 2025-08-31 as of 2026-09-16T05:43:08Z for a METR/ARC grant payable | n=0 | role=negative strength=supporting lane=MD06
- MDS0295: public grant databases | GET https://astralisfoundation.org/grants ; GET /robots.txt ; GET /sitemap.xml => none found in https://astralisfoundation.org/grants as of 2026-09-16T06:07:23Z (HTTP 404); robots 404; sitemap HTTP 500 | n=0 | role=negative strength=supporting lane=MD13
- MDS0503: issuer statements | GET https://astralisfoundation.org/ ; text search METR|Model Evaluation|ARC => none found in https://astralisfoundation.org/ as of 2026-09-16T07:21:40Z | n=0 | role=negative strength=supporting lane=MD23
- MDS0776: issuer statements | GET anthropic.com Series A, E, F, G, H and /company; HTML search those supporter names => none found in Anthropic Series A/E/F/G/H and /company pages as of 2026-09-16T09:37:25Z for Packard, Pew, Sijbrandij, Audacious, LaCentra-Sumerlin, Astralis, Expa.org, Longview, Effektiv Spenden, David
- MDS1049: state registries | Stiftelsesök källfil record ID 1032015; text search METR|Model Evaluation|Alignment Research => none found in Länsstyrelsen Stiftelsesök källfil record for Stiftelsen Astralis (ORGNR 802482-2317) as of 2026-09-16T10:01:36Z for a METR/ARC grant line | n=0 | role=context strength=supporting lane=M
- MDS1052: state registries | Charity Commission register search q=Astralis => none found in Charity Commission register search 'Astralis' as of 2026-09-16T10:01:21Z | n=0 | role=negative strength=supporting lane=MD06
- MDS1053: state registries | GET https://www.lansstyrelsen.se/stockholm/naringsliv-och-foreningar/stiftelser/ => none found in https://www.lansstyrelsen.se/stockholm/naringsliv-och-foreningar/stiftelser/ as of 2026-09-16T10:01:23Z (HTTP 404) | n=0 | role=context strength=supporting lane=MD06
- MDS1055: self-statements | GET https://r.jina.ai/https://astralisfoundation.org/ => none found in r.jina.ai proxy of https://astralisfoundation.org/ as of 2026-09-16T10:01:14Z (HTTP 403) | n=0 | role=context strength=supporting lane=MD06
- MDS1056: state registries | GET https://opencorporates.com/companies/gb/15917880 => none found in OpenCorporates company gb/15917880 as of 2026-09-16T10:01:23Z (hCaptcha / HAProxy Challenge) | n=0 | role=context strength=supporting lane=MD06
- MDS1058: public grant databases | GET https://projects.propublica.org/nonprofits/full_text_search?q="Astralis Foundation"+METR => none found in ProPublica full_text_search 'Astralis Foundation METR' as of 2026-09-16T10:01:17Z (HTTP 429) | n=0 | role=context strength=supporting lane=MD06

### Contradictions, duplicates and defects

- None on amounts. Two legal entities operate under one brand (MDE0022 vs MDE0023); the pack keeps them separate and neither publishes a grant schedule.

### Figure notes
Acknowledged only. Primary-strength negative: UK accounts YE 2025-08-31 contain no METR/ARC line and no P&L (MDS0153, MDS0169). No US 990 (MDS0154). Swedish annual accounts were not retrieved. Anchor: MDR0022.


## Expa.org (EXPAORG / EXPA ORG, EIN 83-2856275)

**How METR names it:** metr.org/about: 'Expa.org'; 2026-08-14 update image alt: 'Expa.org'

**Status:** acknowledged, no public amount

### Facts (draw only from these)

- **MDR0023** [evidence/primary; lane MD06] untyped (no amount)  | undated | Expa.org -> METR | status: n/a | purpose: n/a
  - ANCHOR (primary): acknowledged on the recipient list; no amount, date, vehicle or purpose.
  - url: https://metr.org/about
- **MDE0024** [evidence/primary; lane MD06] untyped (no amount)  | undated | ? -> ? | status: n/a | purpose: n/a
  - Legal entity: EXPAORG EIN 83-2856275, California private non-operating foundation, TY2024 990-PF.
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202523219349106192_public.xml
- **MDE0025** [context/supporting; lane MD06] untyped (no amount)  | undated | ? -> ? | status: n/a | purpose: n/a
  - expa.com (startup studio) is a separate operating company; METR names Expa.org.
  - url: https://expa.com/
- **MDT0022** [evidence/supporting; lane MD06] untyped (no amount)  | 2025-12-07 | Expa.org -> METR | status: n/a | purpose: n/a
  - Named on the 2025-12-07 about capture.
  - url: https://web.archive.org/web/20251207085707/https://metr.org/about
- **MDT0079** [evidence/primary; lane MD24] untyped (no amount)  | 2025-12-07 | ? -> METR | status: n/a | purpose: n/a
  - About-page first appearance bounded 2025-12-03 to 2025-12-07.
  - url: https://web.archive.org/web/20251207085707id_/https://metr.org/about
- **MDF0229** [context/supporting; lane MD33] untyped (no amount)  | undated | Expa.org -> METR (Model Evaluation and Threat Research) | status: n/a | purpose: n/a
  - MD33: named; amount not on page.
  - url: https://metr.org/about

### Restatement / locator rows (do not cite as new facts)

MDF0692, MDP0054, MDP0183, MDP0520, MDP0725, MDE0075, MDT0078, MDT0224

### Timeline rows

MDT0022, MDT0078, MDT0079, MDT0224

### Bounded negatives

Counts (live): 12 rows; by source class: funder filings 5, issuer statements 2, public grant databases 1, self-statements 2, state registries 2
- MDS0150: self-statements | GET https://www.expa.org/ => none found in https://www.expa.org/ as of 2026-09-16T05:35:24Z | n=0 | role=negative strength=supporting lane=MD06
- MDS0152: funder filings | grep METR|Model Evaluation|Threat Research|Alignment Research|ARC EVALS|99-1219864|86-3605182 in object_ids 202243199349105784, 202333189349106013, 202513219349106941, 202523219349106 => none found in EXPA ORG Forms 990-PF TY2021-TY2024 XML grant schedules as of 2026-09-16T05:37:41Z | n=0 | role=negative strength=primary lane=MD06
- MDS0156: funder filings | ProPublica org page; latest_object_id 202523219349106192 => Public filing route exists: US Form 990-PF for EXPA ORG. Latest is TY2024 object 202523219349106192. TY2025 not yet on the index. | n=1 | role=context strength=supporting lane=MD06
- MDS0160: state registries | GET https://ca-rcf.evokeplatform.com/app/publicPortal/verification => none found in CA Registry Search Tool publicPortal/verification as of 2026-09-16T05:43:16Z (JS-only; no EIN lookup possible in this fetch) | n=0 | role=context strength=supporting lane=MD06
- MDS0166: self-statements | GET https://www.expa.org/ => none found in https://www.expa.org/ as of 2026-09-16T05:35:24Z for a METR/ARC grant, amount, or date | n=0 | role=negative strength=supporting lane=MD06
- MDS0168: funder filings | Form 990-PF Part XV XML grep METR/ARC aliases, object_id 202523219349106192 and three prior years => none found in EXPA ORG 990-PF XML grant schedules TY2021-TY2024 as of 2026-09-16T05:37:41Z | n=0 | role=negative strength=primary lane=MD06
- MDS0296: public grant databases | GET https://www.expa.org/ ; no /grants path, no robots sitemap advertised on this host => none found in https://www.expa.org/ as of 2026-09-16T06:07:25Z for a METR/ARC grant listing, amount or date | n=0 | role=negative strength=supporting lane=MD13
- MDS0504: issuer statements | GET https://www.expa.org/ ; text search METR|Model Evaluation => none found in https://www.expa.org/ as of 2026-09-16T07:21:40Z | n=0 | role=negative strength=supporting lane=MD23
- MDS0505: funder filings | GET XML 202523219349106192 filter METR|991219864|Alignment Research => none found in EXPA ORG Form 990-PF TY2024 grant schedule as of 2026-09-16T07:24:42Z | n=0 | role=negative strength=supporting lane=MD23
- MDS0776: issuer statements | GET anthropic.com Series A, E, F, G, H and /company; HTML search those supporter names => none found in Anthropic Series A/E/F/G/H and /company pages as of 2026-09-16T09:37:25Z for Packard, Pew, Sijbrandij, Audacious, LaCentra-Sumerlin, Astralis, Expa.org, Longview, Effektiv Spenden, David
- MDS1051: state registries | GET https://ca-rcf.evokeplatform.com/app/publicPortal/verification => none found in CA Registry Search Tool publicPortal/verification as of 2026-09-16T10:01:20Z (JS-only; no EIN lookup possible in this fetch) | n=0 | role=context strength=supporting lane=MD06
- MDS1054: funder filings | Form 990-PF Part XV XML grep METR/ARC aliases, object_id 202523219349106192 and three prior years => none found in EXPA ORG 990-PF XML grant schedules TY2021-TY2024 as of 2026-09-16T10:01:25Z | n=0 | role=negative strength=supporting lane=MD06

### Contradictions, duplicates and defects

- None.

### Figure notes
Acknowledged only. Primary-strength negatives: EXPA ORG 990-PF TY2021-TY2024 grant schedules (MDS0152, MDS0168); TY2024 re-check (MDS0505, MDS1054). Anchor: MDR0023.


## AI Security Institute (UK; DSIT)

**How METR names it:** metr.org/about funding paragraph: 'the AI Security Institute'; same page: 'partnering with the AI Security Institute'

**Status:** acknowledged, no public amount; typed contract (seed) with amount undisclosed; no award instrument naming METR found on any UK procurement or spend record

### Facts (draw only from these)

- **MDP0197** [evidence/supporting; lane MD19] untyped (no amount)  | undated | AI Security Institute (UK) -> METR | status: acknowledged as a supporter and partner; amount, date, vehicle and award id not disclosed | purpose: n/a
  - ANCHOR: metr.org/about names AISI as supporter and partner; no award id, value, period or share.
  - url: https://metr.org/about
- **MDP0200** [evidence/primary; lane MD19] untyped (no amount) GBP | undated | DSIT / AI Security Institute -> METR | status: n/a | purpose: n/a
  - ANCHOR (primary): Challenge Fund notice 4113c27b programme ceiling GBP 50,000-200,000 per project; METR not named as supplier; awards[] empty; METR share undisclosed.
  - url: https://www.contractsfinder.service.gov.uk/Notice/4113c27b-11c1-4489-a7ac-c87a57b216e6
- **MDP0196** [evidence/supporting; lane MD19] untyped (no amount) GBP | 2025-03-05 | Department for Science, Innovation and Technology (DSIT) / AI Security Institute -> ? | status: Closed opportunity; awards array empty | purpose: AISI priority research areas / safe and secure AI systems
  - Contracts Finder notice 4113c27b (DSIT, GRANT, valueLow 50000 valueHigh 200000 GBP; awards empty).
  - url: https://www.contractsfinder.service.gov.uk/Notice/4113c27b-11c1-4489-a7ac-c87a57b216e6
- **MDP0201** [evidence/supporting; lane MD19] untyped (no amount) GBP | undated | AI Security Institute -> ? | status: n/a | purpose: n/a
  - Alignment Project programme ceiling GBP 15m then 27m; METR absent from the 60-awardee PDF.
  - url: https://www.aisi.gov.uk/blog/funding-60-projects-to-advance-ai-alignment-research
- **MDP0202** [evidence/supporting; lane MD19] untyped (no amount) GBP | undated | AI Security Institute -> METR | status: n/a | purpose: n/a
  - Alignment Project 2026 Grants PDF: METR share not disclosed; Alignment Research Center (Jacob Hilton) is listed and is not METR.
  - url: https://cdn.prod.website-files.com/68752402cd25ead7e36d7373/699c54b61461caad7130683c_f3052ca4341dfc41646ed7155aaee5fd_The%20Alignment%20Project%202026%20-%20Grants%20%281%29.pdf
- **MDR0034** [evidence/primary; lane MD19] untyped (no amount)  | 2023-09-07 | Frontier AI Taskforce (UK government; later AISI) -> ARC Evals | status: n/a | purpose: n/a
  - Frontier AI Taskforce first progress report 2023-09-07 names ARC Evals as a partnership; no value.
  - url: https://www.gov.uk/government/publications/frontier-ai-taskforce-first-progress-report/frontier-ai-taskforce-first-progress-report
- **MDR0121** [evidence/supporting; lane MD36] untyped (no amount)  | 2024-02-09 | UK AI Safety Institute (DSIT) -> METR (formerly ARC Evals) | status: n/a | purpose: n/a
  - AISI approach-to-evaluations page 2024-02-09 names METR (formerly ARC Evals) as an external partner; no value.
  - url: https://www.gov.uk/government/publications/ai-safety-institute-approach-to-evaluations/ai-safety-institute-approach-to-evaluations
- **MDP0050** [evidence/supporting; lane MD14] contract undisclosed  | undated | AI Security Institute (UK) -> METR | status: n/a | purpose: n/a
  - Commitment reconciliation: excluded (contract, undisclosed).
  - url: https://metr.org/about
- **MDP0311** [context/supporting; lane MD44] untyped (no amount)  | undated | DSIT / AI Security Institute -> ? | status: n/a | purpose: n/a
  - MD44 re-check: notice 4113c27b awards[] still empty; no METR string.
  - url: https://www.contractsfinder.service.gov.uk/api/rest/2/get_published_notice/json/4113c27b-11c1-4489-a7ac-c87a57b216e6
- **MDP0314** [context/supporting; lane MD44] untyped (no amount)  | undated | Department for Science, Innovation and Technology -> Model Evaluation and Threat Research, Inc. | status: n/a | purpose: n/a
  - Unsent UK FOIA draft to DSIT (approved_for_send false).
  - url: https://www.gov.uk/make-a-freedom-of-information-request/how-to-make-an-foi-request
- **MDT0067** [evidence/primary; lane MD24] untyped (no amount)  | 2025-02-15 | ? -> METR | status: n/a | purpose: n/a
  - About-page first partnership mention bounded 2025-02-11 to 2025-02-15.
  - url: https://web.archive.org/web/20250215024028id_/https://metr.org/about
- **MDT0081** [evidence/primary; lane MD24] untyped (no amount)  | 2025-12-07 | ? -> METR | status: n/a | purpose: n/a
  - Funding-paragraph first appearance bounded 2025-12-03 to 2025-12-07.
  - url: https://web.archive.org/web/20251207085707id_/https://metr.org/about
- **MDF0016** [context/supporting; lane S0; SEED] contract undisclosed  | undated | AI Security Institute (UK) -> METR | status: n/a | purpose: general support
  - SEED BASELINE (context): money_type=contract, amount 'undisclosed', purpose 'general support' (purpose is a seed default, not a document).
  - url: https://metr.org/about

### Restatement / locator rows (do not cite as new facts)

MDF0479, MDP0183, MDP0199, MDP0203, MDP0204, MDP0205, MDP0280, MDP0288, MDP0297, MDP0302, MDP0305, MDP0307, MDP0315, MDP0317, MDP0516, MDP0607, MDP0726, MDR0031, MDR0120, MDR0176, MDE0076, MDE0091, MDT0066, MDT0080, MDT0168, MDT0175, MDT0176, MDT0177

### Timeline rows

MDT0066, MDT0067, MDT0080, MDT0081, MDT0168, MDT0176

### Bounded negatives

Counts (live): 31 rows; by source class: issuer statements 11, procurement records 10, project documents 2, public grant databases 7, statutory records requests 1
- MDS0321: public grant databases | GET https://www.aisi.gov.uk/robots.txt Sitemap=https://www.aisi.gov.uk/sitemap.xml (206 loc) then GET /grants and /grants/example-projects; filter loc /grants => Canonical sitemap n=206 with 2 grant locs (/grants and /grants/example-projects). /grants is a Challenge Fund / Alignment Fund programme page (applications closed), not a grantee dump. | n=206 | role=
- MDS0322: public grant databases | GET /grants and /grants/example-projects and blog/funding-60-projects-to-advance-ai-alignment-research and https://alignmentproject.aisi.gov.uk/ ; text search METR|Model Evalu => none found in AISI /grants, /grants/example-projects, funding-60-projects blog, or alignmentproject.aisi.gov.uk as of 2026-09-16T06:57:35Z for a METR/Model Evaluation and Threat Research award | n=0 |
- MDS0461: issuer statements | GET https://www.nist.gov/news-events/news/2026/03/announcement-caisi-signs-crada-openmined-enable-secure-ai-evaluations ; filter METR => none found in CAISI OpenMined CRADA announcement for METR as of 2026-09-16T07:27:14Z | n=0 | role=negative strength=supporting lane=MD21
- MDS0462: issuer statements | GET https://www.nist.gov/caisi ; filter METR / Model Evaluation and Threat Research => none found in https://www.nist.gov/caisi body for the string METR or Model Evaluation and Threat Research as of 2026-09-16T07:27:09Z | n=0 | role=negative strength=supporting lane=MD21
- MDS0471: issuer statements | GET nist.gov/caisi; nist.gov/search?s=METR and s=Model Evaluation and Threat Research; AISIC/NIST AI Consortium members; join-CRADA page; CAISI March 2026 PDF; OpenMined CRADA news => NIST member list and CAISI March PDF name METR as consortium/CRADA-DTA class; no published award id, obligated/potential value, or period in the checked NIST/CAISI documents | n=2 | role=negative stre
- MDS0506: procurement records | GET https://www.aisi.gov.uk/grants ; text search METR|Model Evaluation|ARC Evals => none found in https://www.aisi.gov.uk/grants as of 2026-09-16T07:21:41Z | n=0 | role=negative strength=supporting lane=MD23
- MDS0519: procurement records | GET https://www.aisi.gov.uk/grants filter METR|Model Evaluation|ARC Evals => none found in https://www.aisi.gov.uk/grants as of 2026-09-16T07:21:41Z | n=0 | role=negative strength=supporting lane=MD23
- MDS0523: procurement records | POST https://www.contractsfinder.service.gov.uk/api/rest/2/search_notices/json {"searchCriteria":{"keyword":"METR"},"size":100} => none found in Contracts Finder v2 search_notices/json keyword=METR as of 2026-09-16T08:26:38Z | n=0 | role=negative strength=primary lane=MD19
- MDS0524: procurement records | POST search_notices/json {"searchCriteria":{"keyword":"\"Model Evaluation and Threat Research\""},"size":100} => none found in Contracts Finder v2 search_notices/json keyword="Model Evaluation and Threat Research" as of 2026-09-16T08:26:41Z | n=0 | role=negative strength=primary lane=MD19
- MDS0525: procurement records | POST search_notices/json {"searchCriteria":{"keyword":"\"ARC Evals\""},"size":100} => none found in Contracts Finder v2 search_notices/json keyword="ARC Evals" as of 2026-09-16T08:26:45Z | n=0 | role=negative strength=primary lane=MD19
- MDS0526: procurement records | POST search_notices/json {"searchCriteria":{"keyword":"\"AISI\""},"size":100} and keyword="\"AI Security Institute\"" => none found in Contracts Finder v2 quoted-AISI dump (n=34) or quoted 'AI Security Institute' (n=5) as of 2026-09-16T08:27:16Z for awardedSupplier METR / Model Evaluation and Threat Research / ARC Evals
- MDS0527: procurement records | GET https://www.find-tender.service.gov.uk/Search/Results?keywords=METR and keywords=%22AI%20Security%20Institute%22; GET /API/1.0/ocdsReleasePackages (404) => none found in Find a Tender Search/Results?keywords=METR as of 2026-09-16T08:27:31Z (HTML is a JS shell with no notice rows and no METR string; unauthenticated /API/1.0/ocdsReleasePackages HTTP 404; r
- MDS0528: public grant databases | GET https://www.aisi.gov.uk/grants ; sitemap loc filter /grants => none found in AISI /grants as of 2026-09-16T08:27:44Z for a METR / Model Evaluation and Threat Research / ARC Evals grantee name | n=0 | role=negative strength=supporting lane=MD19
- MDS0529: public grant databases | GET https://www.aisi.gov.uk/blog/funding-60-projects-to-advance-ai-alignment-research => none found in AISI blog/funding-60-projects-to-advance-ai-alignment-research HTML as of 2026-09-16T08:27:48Z for METR / Model Evaluation and Threat Research / ARC Evals as an awardee | n=0 | role=nega
- MDS0530: public grant databases | GET https://www.aisi.gov.uk/grants/example-projects ; text search METR|ARC Evals|Model Evaluation and Threat Research => none found in AISI /grants/example-projects as of 2026-09-16T08:27:45Z for METR / Model Evaluation and Threat Research / ARC Evals | n=0 | role=negative strength=supporting lane=MD19
- MDS0531: issuer statements | GET https://www.gov.uk/api/search.json?q=%22ARC%20Evals%22&count=50 (total=8); q=METR tokenises to metre => 8 GOV.UK documents match quoted ARC Evals; none is a Contracts Finder award or a GBP payment line. q=METR is unusable (7363 hits on metre/metric). | n=8 | role=evidence strength=supporting lane=MD19
- MDS0533: project documents | GET https://www.aisi.gov.uk/blog/our-approach-to-evaluations ; text search METR|ARC Evals|Model Evaluation and Threat Research => none found in recovered HTML of aisi.gov.uk/blog/our-approach-to-evaluations as of 2026-09-16T08:27:48Z for METR / Model Evaluation and Threat Research / ARC Evals (GOV.UK HTML of the same publication
- MDS0534: public grant databases | GET Full list of awardees PDF linked from aisi.gov.uk/blog/funding-60-projects-to-advance-ai-alignment-research; pdftotext -layout; text search METR|Model Evaluation and Threa => none found in Alignment Project 2026 Grants PDF (Full list of awardees) as of 2026-09-16T09:04:43Z for METR / Model Evaluation and Threat Research / ARC Evals | n=0 | role=negative strength=primary la
- MDS0535: procurement records | GET get_published_notice/json/ce97f158-727e-43d2-8169-452b2b48b6f7 => none found in the 34 quoted-AISI Contracts Finder notices as of 2026-09-16T08:27:16Z for a consortium award naming METR as a member. Closest AISI award is RAND Europe (legal supplier RAND Europe; awar
- MDS0537: public grant databases | GET aisi.gov.uk/grants, /grants/example-projects, blog/funding-60-projects-to-advance-ai-alignment-research, alignmentproject.aisi.gov.uk/ and /awardees /projects; GET Alignme => none found in AISI /grants, /grants/example-projects, funding-60-projects blog, alignmentproject.aisi.gov.uk (/awardees HTTP 404, /projects HTTP 404) as of 2026-09-16T08:27:51Z, or in Alignment Projec
- MDS0538: procurement records | DSIT departmental spending over £25,000 collection + 21 monthly CSVs 2024-2025; GOV.UK search filter_organisations=ai-security-institute filter_format=transparency (total=1: Ian  => none found in DSIT spending-over-25000 CSVs (n=21 files) as of 2026-09-16T08:28:42Z for payee METR / Model Evaluation and Threat Research / ARC Evals; none found in AISI-organisation transparency sear
- MDS0648: issuer statements | GET https://www.aisi.gov.uk/about ; filter: independence policy / conflict of interest for evaluators => none found in https://www.aisi.gov.uk/about as of 2026-09-16T09:25:37Z of a published independence or CoI policy for third-party evaluators. Case-insensitive search of the saved HTML found no 'indepen
- MDS0649: issuer statements | GET https://www.nist.gov/caisi ; filter: evaluator independence / conflict of interest policy => none found in https://www.nist.gov/caisi as of 2026-09-16T09:25:37Z of a published independence or CoI policy for third-party evaluators. Page uses the phrase 'independent evaluators' in a generic eva
- MDS0812: issuer statements | GET https://scale.com/blog/first-independent-model-evaluator-for-the-usaisi ; JSON-LD BlogPosting => none found in https://scale.com/blog/first-independent-model-evaluator-for-the-usaisi JSON-LD/headline as of 2026-09-16T09:36:09Z for the string METR or Model Evaluation and Threat Research; Scale is 
- MDS0816: procurement records | POST https://www.contractsfinder.service.gov.uk/api/rest/2/search_notices/json searchCriteria.keyword METR | "Model Evaluation and Threat Research" | "ARC Evals" size=100; GET No => none found in Contracts Finder v2 search_notices/json keyword=METR as of 2026-09-16T09:37:40Z (hitCount=0); none found for quoted Model Evaluation and Threat Research as of 2026-09-16T09:37:44Z; none 
- MDS0819: issuer statements | GET https://www.aisi.gov.uk/about and https://www.aisi.gov.uk/grants ; filter METR / Model Evaluation => none found in https://www.aisi.gov.uk/about as of 2026-09-16T09:35:26Z for the string METR or Model Evaluation and Threat Research. Responsive AISI naming of METR is the GOV.UK approach-to-evaluations
- MDS0825: issuer statements | GET OpenAI GPT-4/o1/GPT-5 PDFs and GPT-4o HTML; Anthropic Claude 2/3.5/Mythos PDFs, RSP, cyber-incidents; Amazon arXiv 2507.06260 and 2601.19134; GDM FSF v3.1; NIST members/join/CA => Issuer documents recovered METR/ARC roles for OpenAI, Anthropic, Amazon, NIST/CAISI, UK Taskforce/AISI, and EU AI Office (via TED+FAR.AI). GDM FSF did not select METR. Scale US AISI blog did not name 
- MDS0827: project documents | pdftotext/layout of OpenAI GPT-4/o1/GPT-5 cards; Anthropic Claude 2/3.5/Mythos cards; Amazon arXiv PDFs; GDM FSF; CAISI March PDF; FR 2026-10779; TED ContractAwardNotice XML 864574 => Project documents recovered METR/ARC as named evaluator/tenderer/auditor. FR 2026-10779 does not name METR. GDM FSF only a metr.org URL. Mythos Preview names METR and Epoch. | n=12 | role=context stre
- MDS0830: statutory records requests | GET https://www.gov.uk/search/transparency-and-freedom-of-information-releases?keywords=METR&organisations[]=department-for-science-innovation-and-technology ; filter Mode => none found in DSIT FOI releases keywords=METR as of 2026-09-16T08:57:37Z for Model Evaluation and Threat Research (0 in static HTML). Search title contains the query token METR. Document still unpubli
- MDS0832: issuer statements | GET https://www.nist.gov/news-events/news/2026/03/announcement-caisi-signs-crada-openmined-enable-secure-ai-evaluations ; filter METR legal name => Page documents a CRADA with OpenMined, a different legal entity. It is not the unpublished METR instrument. | n=0 | role=context strength=supporting lane=MD44
- MDS0833: issuer statements | GET https://www.aisi.gov.uk/grants ; filter Model Evaluation and Threat Research | METR | ARC Evals => none found in https://www.aisi.gov.uk/grants as of 2026-09-16T08:58:13Z for Model Evaluation and Threat Research as an awardee. Programme ceiling is not METR's share. | n=0 | role=negative strength=su

### Contradictions, duplicates and defects

- Seed MDF0016 carries purpose_restriction 'general support' for an undisclosed contract; no document states a purpose. Treat as a seed default.
- Programme ceilings (GBP 50k-200k per project; GBP 15m/27m Alignment Project) are not METR amounts; the pack records them with METR share blank. Do not convert GBP.

### Figure notes
Acknowledged only. Primary-strength negatives: Contracts Finder v2 keyword METR / quoted legal name / ARC Evals / AISI (MDS0523-MDS0526, MDS0535), DSIT spend-over-GBP25k CSVs 2024-2025 (MDS0532), Alignment Project awardee PDF (MDS0534). Anchors: MDP0197, MDP0200.


## Longview Philanthropy (pooled funds: public fund / Longtermism Fund, later Emerging Challenges Fund; legal filers Longview Philanthropy USA Inc EIN 93-2664730 and Longview Inc. Ltd UK 14444004)

**How METR names it:** metr.org/about: 'pooled funds such as those of Longview Philanthropy and Effektiv Spenden' (earlier: 'the pooled funds of many other donors, including through Longview Philanthropy and Effektiv Spenden's funds')

**Status:** public amount identified as a recommendation only: $220,000 from the Longview public fund, August 2023 grants report, to ARC Evals (now METR), then a project of Alignment Research Center; no payment document; no Longview filing names METR

### Facts (draw only from these)

- **MDF0070** [evidence/primary; lane MD10] recommendation 220000 USD | 2023-08 | Longview Philanthropy (public fund / Longtermism Fund later ECF) -> ARC Evals (now called METR), then a project of Alignment Research Center | status: recommendation (report does not show a bank payment) | purpose: General support of ARC Evals evaluations project
  - ANCHOR (primary): Longview August 2023 public-fund grants report (hosted by GWWC): ARC Evals (now called METR) $220,000. Recommendation, not a bank payment; recipient at the time a project of ARC.
  - url: https://www.givingwhatwecan.org/en-GB/charities/longtermism-fund/longtermism-fund-august-2023-grants-report
- **MDF0071** [context/supporting; lane MD10] recommendation 220000 USD | 2023 | Longview Philanthropy (public fund) -> METR (then ARC Evals) | status: recommendation | purpose: n/a
  - GWWC charity page restates the $220,000 recommendation in 2023 (third-party locator).
  - url: https://www.givingwhatwecan.org/charities/arc-evals
- **MDF0200** [context/supporting; lane MD23] recommendation 220000 USD | 2023-08 | Longview Philanthropy (public fund / Longtermism Fund later ECF) -> ARC Evals (now called METR), then a project of Alignment Research Center | status: n/a | purpose: evaluations project at the Alignment Research Center (ARC Evals) works on assessing whether cutting-edge AI systems could pose catastrophic risks to civilization
  - Purpose per the report: evaluations project assessing catastrophic risks (programme-restricted per MDP0175).
  - url: https://www.givingwhatwecan.org/en-GB/charities/longtermism-fund/longtermism-fund-august-2023-grants-report
- **MDP0022** [evidence/supporting; lane MD10] recommendation 220000 USD | 2023 | Longview Philanthropy public fund / ECF -> ARC Evals / METR | status: recommendation only in recovered documents | purpose: n/a
  - Explicit: the recovered Longview-to-METR figure is a recommendation; ECF page says funds are disbursed on Longview recommendations, but no wire document.
  - url: https://www.longview.org/fund/emerging-challenges-fund/
- **MDP0044** [evidence/primary; lane MD14] recommendation 220000 USD | 2023 | Longview Philanthropy (public fund) -> METR (then ARC Evals, division of ARC) | status: n/a | purpose: n/a
  - Commitment reconciliation: excluded (recommendation; 2023; recipient then a division of ARC).
  - url: https://www.givingwhatwecan.org/charities/arc-evals
- **MDP0478** [evidence/supporting; lane MD10] untyped (no amount)  | 2023-09-25 | Longview Philanthropy (brand grant CPT) -> Model Evaluation & Threat Research | status: undisclosed on public REST payload | purpose: n/a
  - Longview WP grant CPT object 1577 (slug arc-evaluations) titled Model Evaluation & Threat Research dated 2023-09-25; no amount in the public JSON.
  - url: https://www.longview.org/wp-json/wp/v2/grant?slug=arc-evaluations
- **MDP0021** [context/supporting; lane MD10] untyped (no amount)  | undated | Longview Philanthropy (brand) -> METR | status: undisclosed | purpose: n/a
  - Longview AI page profiles METR; no amount.
  - url: https://www.longview.org/artificial-intelligence/
- **MDP0023** [context/supporting; lane MD10] recommendation (no amount)  | 2024-12/2025-09 | Frontier AI Fund -> ? | status: aggregate / private disbursement report | purpose: n/a
  - Frontier AI Fund (private) reports an aggregate of 18 organisations; METR not listed.
  - url: https://www.longview.org/fund/frontier-ai-fund/
- **MDP0025** [negative/supporting; lane MD10] recommendation (no amount)  | 2023-12 | Emerging Challenges Fund -> ? | status: n/a | purpose: n/a
  - December 2023 ECF grants report does not list METR.
  - url: https://www.longview.org/fund/emerging-challenges-fund-december-2023-grants-report/
- **MDR0135** [evidence/supporting; lane MD10] filed_grant 843128 USD | 2024 | Giving What We Can USA Inc -> Longview Philanthropy USA Inc | status: n/a | purpose: SAFEGUARD THE LONG-TERM FUTURE BY PROVIDING FUNDING TO HIGHLY-EFFECTIVE ORGANISATIONS THAT SEEK TO REDUCE EXISTENTIAL AND CATASTROPHIC RISKS
  - NOT A METR PAYMENT: GWWC USA TY2024 $843,128 filed to Longview USA Inc; Longview USA Schedule I the same year has no METR line.
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202533179349308523_public.xml
- **MDR0027** [evidence/supporting; lane MD10] transfer (no amount)  | undated | unnamed donors to Giving What We Can / ECF -> Emerging Challenges Fund / Longview-recommended grantees | status: n/a | purpose: n/a
  - GWWC/ECF donors are not METR donors.
  - url: https://www.longview.org/fund/emerging-challenges-fund/
- **MDE0032** [evidence/primary; lane MD10] untyped (no amount)  | undated | Longview Philanthropy USA Inc -> ? | status: n/a | purpose: n/a
  - Longview Philanthropy USA Inc EIN 93-2664730 (legal filer, first 990 TY2024).
  - url: https://www.longview.org/organisational-structure/
- **MDE0033** [evidence/supporting; lane MD10] untyped (no amount)  | undated | Longview Inc. Ltd -> ? | status: n/a | purpose: n/a
  - Longview Inc. Ltd UK company 14444004.
  - url: https://find-and-update.company-information.service.gov.uk/company/14444004
- **MDT0083** [evidence/primary; lane MD24] untyped (no amount)  | 2025-12-07 | ? -> METR | status: n/a | purpose: n/a
  - About-page first appearance bounded 2025-12-03 to 2025-12-07.
  - url: https://web.archive.org/web/20251207085707id_/https://metr.org/about
- **MDF0013** [context/supporting; lane S0; SEED] recommendation 220000  | 2023 | Longview Philanthropy (public fund) -> METR (then ARC Evals, division of ARC) | status: n/a | purpose: General support
  - SEED BASELINE (context): $220,000 recommendation 2023 (from GWWC page).
  - url: https://www.givingwhatwecan.org/charities/arc-evals
- **MDF0230** [context/supporting; lane MD33] untyped (no amount)  | undated | Longview Philanthropy -> METR (Model Evaluation and Threat Research) | status: n/a | purpose: n/a
  - MD33: named; amount not on page.
  - url: https://metr.org/about
- **MDF0076** [context/supporting; lane MD13; DEAD] recommendation 220000 USD | 2023 | Longview Philanthropy -> METR (formerly called ARC Evals) | status: n/a | purpose: n/a
  - DEAD ROW (superseded by MDF0539) still cited by supporter_coverage.csv positive_rows and MDP0727. Do not cite.
  - url: https://www.givingwhatwecan.org/sitemap-0.xml

### Restatement / locator rows (do not cite as new facts)

MDF0082, MDF0201, MDF0476, MDF0533, MDF0534, MDF0539, MDF0545, MDF0663, MDF0664, MDF0693, MDF0961, MDF0988, MDF1026, MDF1029, MDP0020, MDP0164, MDP0175, MDP0189, MDP0190, MDP0191, MDP0192, MDP0510, MDP0615, MDP0650, MDP0657, MDP0727, MDE0031, MDE0035, MDE0045, MDE0077, MDE0129, MDE0130, MDE0131, MDT0082

### Timeline rows

MDT0054, MDT0059, MDT0082, MDT0083

### Bounded negatives

Counts (live): 34 rows; by source class: DAF sponsor filings 1, IRS TEOS and e-file index 4, SEC 1, archives 1, court dockets 1, funder filings 10, issuer statements 2, procurement records 1, public grant databases 7, recipient filings 3, state registries 3
- MDS0017: public grant databases | GET https://www.longview.org/artificial-intelligence/ and https://www.longview.org/about/ ; HTML search for Jane Street => none found in Longview /artificial-intelligence and /about as of 2026-09-16T05:34:01Z for a named Jane Street individual as METR donor | n=0 | role=negative strength=supporting lane=MD07
- MDS0265: issuer statements | GET https://www.longview.org/frontier-ai-fund/ (redirects to /fund/frontier-ai-fund/) => Frontier AI Fund public page reports an aggregate of 18 organisations Dec 2024-Sep 2025; METR not named; amounts not public | n=0 | role=negative strength=supporting lane=MD10
- MDS0266: funder filings | GET GivingTuesday S3 XML 202503179349304265_public.xml ; IRS990ScheduleI RecipientTable => none found in Longview Philanthropy USA Inc TY2024 Form 990 Schedule I (domestic grantees: Players Philanthropy Fund, Rethink Priorities, AI Objectives Institute, Pacific Forum International, Horizon 
- MDS0267: funder filings | GET same XML IRS990ScheduleF GrantsToOrgOutsideUSGrp => none found in Longview USA Inc TY2024 Schedule F (three unnamed Europe grants 504714, 262000, 126000) as of 2026-09-16T06:06:36Z | n=0 | role=negative strength=primary lane=MD10
- MDS0268: funder filings | GET https://find-and-update.company-information.service.gov.uk/company/14444004/filing-history/MzQ4MzcxMjE5OGFkaXF6a2N4/document?format=pdf&download=0 => none found in Longview Inc. Ltd total exemption full accounts made up to 31 December 2024 (Companies House PDF MzQ4MzcxMjE5OGFkaXF6a2N4) as of 2026-09-16T06:14:00Z | n=0 | role=context strength=suppor
- MDS0269: state registries | GET https://register-of-charities.charitycommission.gov.uk/en/charity-search/-/charity-details/search?q=Longview+Philanthropy => none found in Charity Commission for England and Wales register search q=Longview Philanthropy as of 2026-09-16T06:06:36Z | n=0 | role=context strength=supporting lane=MD10
- MDS0270: recipient filings | GET GivingTuesday S3 XML 202523209349300367_public.xml ; search LONGVIEW|EFFEKTIV|SPENDEN => none found in METR FY2024 Form 990 XML as of 2026-09-16T06:12:00Z for a Longview or Effektiv Spenden named payer | n=0 | role=negative strength=primary lane=MD10
- MDS0271: IRS TEOS and e-file index | GET https://projects.propublica.org/nonprofits/api/v2/organizations/932664730.json => locator hit: latest_object_id 202503179349304265 TY2024; filings_with_data empty on API | n=1 | role=context strength=supporting lane=MD10
- MDS0274: archives | GET https://r.jina.ai/http://effektiv-spenden.org/en/safeguarding-the-future/ (and Longview/GWWC/METR jina URLs) => none found in r.jina.ai proxy of effektiv-spenden.org/en/safeguarding-the-future/ as of 2026-09-16T06:12:00Z | n=0 | role=context strength=supporting lane=MD10
- MDS0275: public grant databases | GET https://www.longview.org/grants/ ; CDX url=longview.org/grants/ filter statuscode:200 => none found in https://www.longview.org/grants/ as of 2026-09-16T06:06:36Z | n=0 | role=negative strength=supporting lane=MD10
- MDS0276: public grant databases | GET https://www.longview.org/?s=METR => none found in Longview site search ?s=METR as of 2026-09-16T06:06:36Z for a METR grant amount | n=0 | role=negative strength=supporting lane=MD10
- MDS0280: SEC | GET https://efts.sec.gov/LATEST/search-index?q=%22Longview%20Philanthropy%22%20METR&dateRange=custom&startdt=2022-01-01&enddt=2026-09-16 => none found in SEC EFTS search-index q="Longview Philanthropy" METR (file_date 2022-01-01..2026-09-16) as of 2026-09-16T06:18:00Z | n=0 | role=negative strength=supporting lane=MD10
- MDS0282: court dockets | GET https://www.courtlistener.com/?type=o&q=%22Longview%20Philanthropy%22%20METR => none found in CourtListener opinion search q="Longview Philanthropy" METR as of 2026-09-16T06:18:00Z | n=0 | role=negative strength=supporting lane=MD10
- MDS0283: procurement records | GET https://www.usaspending.gov/search/?hash=none&q=METR%20Longview => none found in USAspending.gov search page q=METR Longview as of 2026-09-16T06:18:00Z | n=0 | role=context strength=supporting lane=MD10
- MDS0286: state registries | GET https://api.charitycommission.gov.uk/register/api/searchCharityName/Longview%20Philanthropy => none found in Charity Commission API searchCharityName/Longview Philanthropy as of 2026-09-16T06:06:36Z | n=0 | role=context strength=supporting lane=MD10
- MDS0288: DAF sponsor filings | not a Schedule I sweep (MD11/MD22); this lane checked GWWC as ECF processor only => none found in this lane's DAF-sponsor filing sweep as of 2026-09-16T06:18:00Z (no sponsor 990 opened for a Longview earmark to METR) | n=0 | role=context strength=supporting lane=MD10
- MDS0297: public grant databases | GET https://www.longview.org/wp-json/wp/v2/types (type=grant) then GET /wp-json/wp/v2/grant?per_page=100 (X-WP-Total=23); search=METR total=0; search=Model Evaluation total=1  => Longview WP grant CPT (n=23) contains one object titled Model Evaluation & Threat Research (slug arc-evaluations, dated 2023-09-25); the public REST payload does not expose an amount; keyword search=M
- MDS0320: public grant databases | GET https://www.longview.org/grants/ and /grants (HTTP 404); catalog is WP /wp-json/wp/v2/grant => none found in https://www.longview.org/grants/ as of 2026-09-16T06:07:35Z (HTTP 404); grant CPT dump is B09 | n=0 | role=context strength=supporting lane=MD13
- MDS0380: funder filings | GET GT XML 202503179349304265; IRS990ScheduleI RecipientTable and Schedule F GrantsToOrgOutsideUSGrp; filter METR|991219864|MODEL EVALUATION|ARC EVALS => none found in Longview Philanthropy USA Inc TY2024 Form 990 Schedule I object 202503179349304265 as of 2026-09-16T07:27:52Z | n=0 | role=negative strength=supporting lane=MD22
- MDS0403: funder filings | GET https://find-and-update.company-information.service.gov.uk/company/14444004/filing-history/MzQ4MzcxMjE5OGFkaXF6a2N4/document?format=pdf&download=0 ; pdftotext/strings METR|grant => none found in Longview Inc. Ltd total exemption full accounts made up to 31 December 2024 (Companies House PDF MzQ4MzcxMjE5OGFkaXF6a2N4) as of 2026-09-16T07:27:52Z | n=0 | role=context strength=suppor
- MDS0404: state registries | GET https://register-of-charities.charitycommission.gov.uk/en/charity-search/-/charity-details/search?q=Longview+Philanthropy => none found in Charity Commission for England and Wales register search q=Longview Philanthropy as of 2026-09-16T07:27:52Z for a named Longview Philanthropy charity (search UI is a JS shell; no charity
- MDS0415: recipient filings | GET GT XML 202523209349300367; search LONGVIEW|FOUNDERS PLEDGE|EVERY ORG|EFFECTIVE VENTURES|ContributorNum => none found in METR FY2024 Form 990 XML object 202523209349300367 as of 2026-09-16T07:27:52Z for a named Longview, Founders Pledge, Every Org, or Effective Ventures contributor | n=0 | role=negative st
- MDS0417: IRS TEOS and e-file index | stream https://apps.irs.gov/pub/epostcard/990/xml/2026/index_2026.csv filter EIN in {371795297,932664730,611913297,333737390,205205488} => none found in IRS e-file index_2026.csv as of 2026-09-16T07:27:52Z for EIN 371795297, 932664730, 611913297, 333737390, or 205205488 | n=0 | role=negative strength=supporting lane=MD22
- MDS0776: issuer statements | GET anthropic.com Series A, E, F, G, H and /company; HTML search those supporter names => none found in Anthropic Series A/E/F/G/H and /company pages as of 2026-09-16T09:37:25Z for Packard, Pew, Sijbrandij, Audacious, LaCentra-Sumerlin, Astralis, Expa.org, Longview, Effektiv Spenden, David
- MDS1083: funder filings | GET GivingTuesday S3 XML 202503179349304265_public.xml ; IRS990ScheduleI RecipientTable => none found in Longview Philanthropy USA Inc TY2024 Form 990 Schedule I as of 2026-09-16T09:53:47Z | n=0 | role=context strength=supporting lane=MD10
- MDS1084: funder filings | GET same XML IRS990ScheduleF GrantsToOrgOutsideUSGrp => none found in Longview Philanthropy USA Inc TY2024 Form 990 Schedule F as of 2026-09-16T09:53:47Z for a named METR/ARC grantee | n=0 | role=context strength=supporting lane=MD10
- MDS1086: recipient filings | GET GT XML 202403209349312630_public.xml ; search LONGVIEW|EFFEKTIV|GIVING WHAT WE CAN|220000 => none found in Alignment Research Center TY2023 Form 990 XML object 202403209349312630 as of 2026-09-16T09:53:47Z for a named Longview, Effektiv Spenden, or GWWC payer | n=0 | role=negative strength=su
- MDS1088: funder filings | GET GT XML 202533179349308523_public.xml ; RecipientTable filter METR|991219864|ALIGNMENT RESEARCH|863605182 => none found in Giving What We Can USA Inc TY2024 Form 990 Schedule I as of 2026-09-16T09:53:47Z for a METR or ARC grant line | n=0 | role=negative strength=supporting lane=MD10
- MDS1089: public grant databases | GET https://www.longview.org/wp-json/wp/v2/grant?search=METR&per_page=100 => none found in Longview wp-json /grant?search=METR as of 2026-09-16T09:53:47Z for a METR grant amount | n=0 | role=context strength=supporting lane=MD10
- MDS1091: IRS TEOS and e-file index | stream https://apps.irs.gov/pub/epostcard/990/xml/2026/index_2026.csv filter EIN 932664730|991219864|863605182 => none found in IRS e-file index_2026.csv as of 2026-09-16T09:53:47Z for EIN 932664730, 991219864, or 863605182 | n=0 | role=context strength=supporting lane=MD10
- MDS1113: public grant databases | GET https://www.longview.org/grant-sitemap.xml (discovered from sitemap_index.xml); compare locs to WP grant CPT n=23 => grant-sitemap.xml n=3 locs (perry-world-house, council-on-strategic-risks, massachusetts-institute-of-technology); arc-evaluations / METR absent. CPT dump (B09) n=23 is the complete public catalog. | 
- MDS1131: funder filings | GET gt990datalake XmlFiles/202503179349304265_public.xml; Schedule I RecipientEIN 951958142 or RAND|CANARY => none found in Longview Philanthropy USA Inc Form 990 Schedule I object 202503179349304265 (TY2024) for RAND Corporation / Canary as of 2026-09-16T09:50:30Z | n=0 | role=negative strength=supporting la
- MDS1147: IRS TEOS and e-file index | stream index_2021.csv through index_2026.csv filter EIN 932664730 => none found in IRS e-file indexes for EIN 932664730 other than the TY2024 object(s) recovered this fetch as of 2026-09-16T10:12:54Z | n=1 | role=context strength=supporting lane=MD22
- MDS1148: funder filings | GET GT XML 202503179349304265; IRS990ScheduleB ContributorInformationGrp ContributorNum => none found in Longview Philanthropy USA Inc TY2024 (2024-01-01 to 2024-12-31) Form 990 Schedule B public copy object 202503179349304265 as of 2026-09-16T10:07:53Z for a named payer (ContributorNum=RES

### Contradictions, duplicates and defects

- Date precision varies for the same $220,000: '2023' (MDF0013, MDF0071, MDF0082, MDF0201) vs '2023-08' (MDF0070, MDF0200); the report is the August 2023 grants report; Longview's own catalog object is dated 2023-09-25 (MDP0478). One recommendation.
- Recipient naming varies: 'METR (then ARC Evals, division of ARC)' (seed) vs 'ARC Evals (now called METR), then a project of Alignment Research Center' (MD10). Legal recipient in 2023 was ARC, not METR Inc (MDE0035).
- DEFECT: MDF0076 is DEAD (superseded by MDF0539) but is listed in supporter_coverage.csv positive_rows for longview and in MDP0727.
- Good Ventures 990-PF lines to Effective Ventures for Longview costs (MDF0356, MDF0373, MDF0376, MDF0386) are payer-into-intermediary rows; MDP0538 records the posted-figure defect of treating them as METR money.

### Figure notes
Show $220,000 as a 2023 recommendation to ARC Evals (recipient then ARC), no payment found; never as a payment to METR Inc. Primary-strength negatives: Longview USA TY2024 Schedule I and F (MDS0266, MDS0267), METR FY2024 990 no Longview payer (MDS0270, MDS0415). Anchor: MDF0070.


## Effektiv Spenden (Giving Fund: Safeguarding the future; legal filer UES gGmbH HRB 204815 B, Berlin)

**How METR names it:** metr.org/about: 'pooled funds such as those of Longview Philanthropy and Effektiv Spenden'

**Status:** public amount identified as a regrant in EUR: 128,000 EUR, August 2023, to METR (formerly ARC Evals); never converted to USD; no legal-filer grant line recovered

### Facts (draw only from these)

- **MDF0072** [evidence/primary; lane MD10] regrant 128,000 EUR EUR | 2023-08 | Effektiv Spenden Giving Fund: Safeguarding the future (brand/fund) -> METR (formerly ARC Evals) | status: grants were made (route's words); not a bank statement | purpose: Evaluation of state-of-the-art AI systems to identify and minimize risks
  - ANCHOR (primary): fund page: METR (formerly ARC Evals), Evaluation of state-of-the-art AI systems to identify and minimize risks (128.000 EUR); 'Grants were made in August 2023'. amount_usd is blank on this row; the EUR figure sits in quantity_or_value.
  - url: https://effektiv-spenden.org/en/safeguarding-the-future/
- **MDF0073** [context/supporting; lane MD10] regrant (no amount) EUR | 2023 | Effektiv Spenden Giving Fund (H1/2023) -> ARC Evals (Alignment Research Center evaluations project) | status: fund-mittel allocated (~128.000 €) | purpose: ARC Evals evaluation project
  - German H1/2023 fund blog: the same ~128.000 EUR to ARC Evals following Longview's recommendation (Longview named as recommender, not payer).
  - url: https://effektiv-spenden.org/blog/fonds-zukunft-bewahren-h1-2023/
- **MDP0024** [evidence/supporting; lane MD10] regrant (no amount) EUR | 2023-08 | Effektiv Spenden Giving Fund: Safeguarding the future -> METR / ARC Evals | status: route says grants were made; filer Jahresabschluss not in hand | purpose: n/a
  - Disbursement language on the fund page; UES gGmbH accounts not in hand.
  - url: https://effektiv-spenden.org/en/safeguarding-the-future/
- **MDP0045** [evidence/primary; lane MD14] regrant 128000 EUR | 2023-08 | Effektiv Spenden (Giving Fund: Safeguarding the future) -> ARC Evals / METR | status: n/a | purpose: n/a
  - Commitment reconciliation: excluded (EUR; regrant; 2023). WARNING: amount_usd column holds 128000 with currency=EUR.
  - url: https://web.archive.org/web/20250126120532/https://effektiv-spenden.org/en/safeguarding-the-future/
- **MDP0176** [evidence/primary; lane MD23] regrant (no amount) EUR | undated | Effektiv Spenden -> METR | status: n/a | purpose: programme-restricted
  - Purpose classification: programme-restricted.
  - url: https://effektiv-spenden.org/en/safeguarding-the-future/
- **MDR0028** [evidence/supporting; lane MD10] transfer (no amount)  | undated | unnamed donors to Giving Fund: Safeguarding the future -> Giving Fund: Safeguarding the future | status: n/a | purpose: n/a
  - Fund donors are not METR donors (no deanonymization).
  - url: https://effektiv-spenden.org/en/safeguarding-the-future/
- **MDE0034** [evidence/supporting; lane MD10] untyped (no amount)  | undated | UES – Gemeinnützige GmbH für effektives Spenden -> ? | status: n/a | purpose: n/a
  - Legal filer UES gGmbH für effektives Spenden, HRB 204815 B.
  - url: https://effektiv-spenden.org/impressum/
- **MDT0085** [evidence/primary; lane MD24] untyped (no amount)  | 2025-12-07 | ? -> METR | status: n/a | purpose: n/a
  - About-page first appearance bounded 2025-12-03 to 2025-12-07.
  - url: https://web.archive.org/web/20251207085707id_/https://metr.org/about
- **MDF0014** [context/supporting; lane S0; SEED] regrant EUR 128,000 EUR | 2023-08 | Effektiv Spenden (Giving Fund: Safeguarding the future) -> ARC Evals / METR | status: n/a | purpose: Evaluation of state-of-the-art AI systems to identify and minimize risks
  - SEED BASELINE (context): amount_usd literally 'EUR 128,000', currency EUR.
  - url: https://effektiv-spenden.org/en/safeguarding-the-future/
- **MDF0231** [context/supporting; lane MD33] untyped (no amount)  | undated | Effektiv Spenden -> METR (Model Evaluation and Threat Research) | status: n/a | purpose: n/a
  - MD33: named; amount not on page.
  - url: https://metr.org/about

### Restatement / locator rows (do not cite as new facts)

MDF0202, MDF0461, MDF0477, MDF0535, MDF0536, MDF0665, MDF0694, MDF0924, MDF1000, MDF1020, MDP0020, MDP0165, MDP0188, MDP0483, MDP0511, MDP0651, MDP0658, MDP0728, MDR0141, MDE0035, MDE0078, MDT0084

### Timeline rows

MDT0084, MDT0085

### Bounded negatives

Counts (live): 11 rows; by source class: SEC 1, archives 1, funder filings 2, issuer statements 4, public grant databases 1, recipient filings 2
- MDS0270: recipient filings | GET GivingTuesday S3 XML 202523209349300367_public.xml ; search LONGVIEW|EFFEKTIV|SPENDEN => none found in METR FY2024 Form 990 XML as of 2026-09-16T06:12:00Z for a Longview or Effektiv Spenden named payer | n=0 | role=negative strength=primary lane=MD10
- MDS0273: issuer statements | GET https://effektiv-spenden.org/en/safeguarding-the-future/ and sibling paths (about, impressum, transparenz, blogs) => none found in live GET https://effektiv-spenden.org/en/safeguarding-the-future/ as of 2026-09-16T06:06:36Z | n=0 | role=context strength=supporting lane=MD10
- MDS0281: SEC | GET https://efts.sec.gov/LATEST/search-index?q=%22Effektiv%20Spenden%22%20METR => none found in SEC EFTS search-index q="Effektiv Spenden" METR as of 2026-09-16T06:18:00Z | n=0 | role=negative strength=supporting lane=MD10
- MDS0285: funder filings | GET https://www.bundesanzeiger.de/pub/en/search?search[fulltext]=Effektiv%20Spenden => none found in Bundesanzeiger search fulltext=Effektiv Spenden as of 2026-09-16T06:12:00Z for a METR grant line | n=0 | role=context strength=supporting lane=MD10
- MDS0314: public grant databases | GET https://www.effektiv-spenden.org/ and /en/ and /en/recommendations and /sitemap.xml ; r.jina.ai of the same hosts => none found in https://www.effektiv-spenden.org/ as of 2026-09-16T06:07:40Z (HTTP 403 from this host; r.jina.ai returned a robot-challenge screen) | n=0 | role=context strength=supporting lane=MD13
- MDS0520: issuer statements | GET https://effektiv-spenden.org/en/safeguarding-the-future/ => none found in live effektiv-spenden.org/en/safeguarding-the-future/ as of 2026-09-16T07:21:37Z (HTTP 403) | n=0 | role=context strength=supporting lane=MD23
- MDS0776: issuer statements | GET anthropic.com Series A, E, F, G, H and /company; HTML search those supporter names => none found in Anthropic Series A/E/F/G/H and /company pages as of 2026-09-16T09:37:25Z for Packard, Pew, Sijbrandij, Audacious, LaCentra-Sumerlin, Astralis, Expa.org, Longview, Effektiv Spenden, David
- MDS1085: funder filings | GET https://effektiv-spenden.org/wp-content/uploads/2024/07/Jahresabschluss-UES-–-Gemeinnuetzige-GmbH-fuer-effektives-Spenden-2023.pdf ; pdftotext; search METR|ARC|128.000 => none found in UES gGmbH Jahresabschluss zum 31. Dezember 2023 as of 2026-09-16T09:53:47Z for a named METR/ARC grant line | n=0 | role=negative strength=supporting lane=MD10
- MDS1086: recipient filings | GET GT XML 202403209349312630_public.xml ; search LONGVIEW|EFFEKTIV|GIVING WHAT WE CAN|220000 => none found in Alignment Research Center TY2023 Form 990 XML object 202403209349312630 as of 2026-09-16T09:53:47Z for a named Longview, Effektiv Spenden, or GWWC payer | n=0 | role=negative strength=su
- MDS1090: archives | GET https://web.archive.org/cdx/search/cdx?url=effektiv-spenden.org/en/safeguarding-the-future/&output=json&filter=statuscode:200 => none found in Wayback CDX search for effektiv-spenden.org/en/safeguarding-the-future/ statuscode:200 as of 2026-09-16T09:53:47Z (endpoint HTTP 503 this fetch) | n=0 | role=context strength=supporting 
- MDS1178: issuer statements | GET https://effektiv-spenden.org/en/safeguarding-the-future/ => none found in https://effektiv-spenden.org/en/safeguarding-the-future/ as of 2026-09-16T12:23:00Z | n=0 | role=context strength=supporting lane=MD46

### Contradictions, duplicates and defects

- FIELD DEFECT: the EUR amount is stored three ways: amount_usd='EUR 128,000' (MDF0014), amount_usd blank with quantity_or_value='128,000 EUR' (MDF0072), amount_usd=128000 with currency=EUR (MDP0045, MDP0483, MDP0511, MDP0651, MDP0658). Any figure must read the currency column and label EUR.
- Recipient naming varies: 'METR (formerly ARC Evals)' (MDF0072) vs 'ARC Evals (Alignment Research Center evaluations project)' (MDF0073) vs 'ARC Evals / METR' (seed). In August 2023 the recipient was ARC's project.
- Date precision: 2023-08 (MDF0072) vs 2023 / H1/2023 (MDF0073).

### Figure notes
Show 128,000 EUR regrant, August 2023, programme-restricted, recipient then ARC Evals; keep in EUR. MD50 re-verification MDF0477 reported 'amount EUR 128,000 not found in primary' for the seed row only (string-format mismatch), while MDF0535 matched the MD10 row. Negatives: METR FY2024 990 no Effektiv payer (MDS0270); UES Jahresabschluss 2023 aggregate only (MDS1085). Anchor: MDF0072.


## Survival and Flourishing Fund (recommendations; funder named on the SFF tables: Jaan Tallinn) and Jaan Tallinn public donation ledger

**How METR names it:** metr.org/about: 'recommendations by the Survival and Flourishing Fund'. METR does not name Jaan Tallinn; his name is on SFF's public tables and his own public ledger (jaan.online).

**Status:** public amounts identified in three distinct money types (recommendation; conditional matching pledge; paid_grant on the donor's own ledger); none summed; SFF-2025 remainder not shown paid

### Facts (draw only from these)

- **MDF0047** [evidence/primary; lane MD09] recommendation 204000 USD | SFF-2024 | Jaan Tallinn (funder named on the SFF table) -> Model Evaluation and Threat Research, Inc. | status: recommendation; not a payment | purpose: General support
  - ANCHOR (primary): SFF-2024 recommendation $204,000 to Model Evaluation and Threat Research, Inc., general support; funder column Jaan Tallinn; includes a ($20,000) speculation annotation (MDP0011), not extra money.
  - url: https://survivalandflourishing.fund/recommendations
- **MDF0045** [evidence/primary; lane MD09] recommendation 120000 USD | SFF-2025 | Jaan Tallinn (funder named on the SFF table) -> Model Evaluation and Threat Research, Inc. | status: recommendation; not a payment | purpose: General support
  - ANCHOR (primary): SFF-2025 recommendation $120,000 (non-matching remainder), general support.
  - url: https://survivalandflourishing.fund/recommendations
- **MDF0046** [evidence/primary; lane MD09] recommendation 428000 USD | SFF-2025 | Jaan Tallinn (funder named on the SFF matching table) -> Model Evaluation and Threat Research, Inc. | status: conditional on outside donations by 2026-09-30 | purpose: General support
  - ANCHOR (primary): SFF-2025 matching pledge $428,000 at 1x through 2026-09-30, conditional on outside donations. Typed recommendation on this row.
  - url: https://survivalandflourishing.fund/2025/recommendations
- **MDP0185** [evidence/primary; lane MD23] recommendation 428000 USD | undated | Jaan Tallinn (SFF matching table) -> Model Evaluation and Threat Research, Inc. | status: n/a | purpose: Matching Pledge: match outside donations up to the pledged amount (conditional)
  - Matching-pledge condition makes the $428,000 incompatible with an unconditional commitment total.
  - url: https://survivalandflourishing.fund/2025/recommendations
- **MDF0093** [evidence/supporting; lane MD14] recommendation 220000 USD | 2025-02-15 | Survival and Flourishing Fund -> Model Evaluation and Threat Research, Inc. | status: recommendation, not a payment | purpose: n/a
  - SFF-2025 further-opportunities page (last published 2025-02-15): METR row $220,000 (in the $5M-additional column) and $1,210,000 (in the $15M-additional column); recommendations of further funding, not summed, not a commitment (MDP0040 excluded).
  - url: https://survivalandflourishing.fund/2025/further-opportunities
- **MDF0051** [evidence/primary; lane MD09] paid_grant 10000 USD | 2024-07-23 | Jaan Tallinn -> Model Evaluation and Threat Research | status: disbursed as recorded on jaan.online ledger | purpose: For general operating support
  - ANCHOR (primary, paid_grant): Jaan Tallinn public ledger 2024-07-23 $10,000 via SFF-spec to METR, 'For general operating support'.
  - url: https://jaan.online/philanthropy/donations.csv
- **MDF0052** [evidence/primary; lane MD09] paid_grant 10000 USD | 2024-07-24 | Jaan Tallinn -> Model Evaluation and Threat Research | status: disbursed as recorded on jaan.online ledger | purpose: For general operating support
  - ANCHOR (primary, paid_grant): ledger 2024-07-24 $10,000 via SFF-spec to METR. With MDF0051 equals the SFF-2024 ($20,000) speculation annotation and the SVCF TY2024 $20,000 filed line (dollar match noted, not merged).
  - url: https://jaan.online/philanthropy/donations.csv
- **MDF0053** [evidence/primary; lane MD09] paid_grant 184000 USD | 2024-12-06 | Jaan Tallinn -> Model Evaluation and Threat Research | status: disbursed as recorded on jaan.online ledger | purpose: General support
  - ANCHOR (primary, paid_grant): ledger 2024-12-06 $184,000 via FP-US to METR, general support. Equals Founders Pledge Inc TY2024 Schedule I $184,000 (MDF0058); differs from the $204,000 recommendation by the $20,000 speculation lines. Same money seen twice; never add.
  - url: https://jaan.online/philanthropy/donations.csv
- **MDF0412** [evidence/supporting; lane MD09] paid_grant 10000 USD | 2024-07-24 | Jaan Tallinn -> Model Evaluation and Threat Research | status: disbursed as recorded on jaan.online ledger | purpose: For general operating support
  - DUPLICATE of MDF0052 (2024-07-24 $10,000). Its note claims to correct MDF0051 (row 18) but reproduces row 19; it does not supersede anything. Cite MDF0052.
  - url: https://jaan.online/philanthropy/donations.csv
- **MDP0484** [evidence/supporting; lane MD14] paid_grant 184000 USD | 2024-12-06 | Jaan Tallinn -> Model Evaluation and Threat Research | status: n/a | purpose: n/a
  - Commitment reconciliation: the three 2024 ledger paid_grants excluded (paid_grant; 2024).
  - url: https://jaan.online/philanthropy/donations.csv
- **MDP0038** [evidence/supporting; lane MD14] recommendation 204000 USD | SFF-2024 | Survival and Flourishing Fund (Jaan Tallinn) -> Model Evaluation and Threat Research, Inc. | status: recommendation, not a payment | purpose: General support
  - Commitment reconciliation: SFF-2024 $204,000 excluded.
  - url: https://survivalandflourishing.fund/
- **MDP0039** [evidence/supporting; lane MD14] recommendation 120000 + 428000 matching pledge USD | SFF-2025 | Survival and Flourishing Fund (Jaan Tallinn) -> Model Evaluation and Threat Research, Inc. | status: recommendation incl. a matching pledge, not a payment | purpose: General support
  - Commitment reconciliation: SFF-2025 excluded. FIELD DEFECT: amount_usd holds two figures '120000 + 428000 matching pledge'.
  - url: https://survivalandflourishing.fund/
- **MDP0010** [context/supporting; lane MD09] untyped (no amount) USD | SFF-2025 | Jaan Tallinn -> Model Evaluation and Threat Research, Inc. | status: annotated as already awarded as Speculation Grant; not a second recommendation | purpose: General support
  - SFF-2025 track total $548,000 = $120,000 remainder + $428,000 matching; speculation ($120,000) is an annotation, not a third amount.
  - url: https://survivalandflourishing.fund/2025/recommendations
- **MDP0011** [context/supporting; lane MD09] untyped (no amount) USD | SFF-2024 | Jaan Tallinn -> Model Evaluation and Threat Research, Inc. | status: annotated as Speculation Grant within the $204,000 recommendation | purpose: General support
  - SFF-2024 $204,000 includes a ($20,000) speculation annotation; do not add.
  - url: https://survivalandflourishing.fund/2024/recommendations
- **MDP0013** [evidence/supporting; lane MD09] untyped (no amount)  | 2026-09-16 | Survival and Flourishing Fund -> METR (Model Evaluation and Threat Research, Inc.) | status: n/a | purpose: n/a
  - METR names SFF recommendations as a route; no amounts.
  - url: https://metr.org/about
- **MDR0029** [evidence/supporting; lane MD10] recommendation (no amount)  | undated | Survival and Flourishing Fund (recommendation vehicle) -> Model Evaluation and Threat Research, Inc. | status: n/a | purpose: n/a
  - The recommender named on SFF tables is not merged into METR donor identity.
  - url: https://survivalandflourishing.fund/recommendations
- **MDE0065** [evidence/supporting; lane MD33] untyped (no amount)  | undated | ? -> ? | status: n/a | purpose: n/a
  - SFF tables name Jaan Tallinn as funder and METR Inc as receiving charity; SFF is the recommending process.
  - url: https://survivalandflourishing.fund/recommendations
- **MDT0087** [evidence/primary; lane MD24] untyped (no amount)  | 2025-12-07 | ? -> METR | status: n/a | purpose: n/a
  - About-page first appearance of SFF bounded 2025-12-03 to 2025-12-07.
  - url: https://web.archive.org/web/20251207085707id_/https://metr.org/about
- **MDF0008** [context/supporting; lane S0; SEED] recommendation 204000  | SFF-2024 | Survival and Flourishing Fund (Jaan Tallinn) -> Model Evaluation and Threat Research | status: recommendation, not a payment | purpose: General support
  - SEED BASELINE (context): SFF-2024 $204,000 recommendation.
  - url: https://survivalandflourishing.fund/sff-2024-recommendations
- **MDF0009** [context/supporting; lane S0; SEED] recommendation 120000 + 428000 matching pledge  | SFF-2025 | Survival and Flourishing Fund (Jaan Tallinn) -> Model Evaluation & Threat Research (METR) | status: recommendation incl. a matching pledge, not a payment | purpose: General support
  - SEED BASELINE (context): SFF-2025 amount cell '120000 + 428000 matching pledge' (two figures in one cell).
  - url: https://survivalandflourishing.fund/
- **MDF0081** [context/supporting; lane MD13] commitment 428000 USD | SFF-2025 | Survival and Flourishing Fund -> Model Evaluation and Threat Research, Inc. | status: matching pledge, not a payment | purpose: General support
  - MD13 row typing the $428,000 matching pledge as money_type=commitment (inconsistent with MDF0046/MDF0197/MDP0185 = recommendation).
  - url: https://survivalandflourishing.fund/
- **MDF0217** [context/supporting; lane MD33] commitment 428000 USD | SFF-2025 | Jaan Tallinn (funder named on the SFF matching table) -> Model Evaluation and Threat Research, Inc. | status: conditional matching pledge; not a payment | purpose: General support
  - MD33 row typing the $428,000 matching pledge as commitment (same inconsistency).
  - url: https://survivalandflourishing.fund/recommendations
- **MDF0199** [context/supporting; lane MD23] paid_grant (no amount) USD | undated | Jaan Tallinn -> Model Evaluation and Threat Research | status: n/a | purpose: For general operating support / General support (ledger purpose column)
  - MD23: the three ledger purpose lines to METR (2 x For general operating support; General support).
  - url: https://jaan.online/philanthropy/donations.csv

### Restatement / locator rows (do not cite as new facts)

MDF0074, MDF0075, MDF0079, MDF0080, MDF0196, MDF0197, MDF0198, MDF0215, MDF0216, MDF0218, MDF0221, MDF0222, MDF0471, MDF0472, MDF0508, MDF0509, MDF0510, MDF0514, MDF0515, MDF0516, MDF0537, MDF0538, MDF0542, MDF0543, MDF0544, MDF0556, MDF0659, MDF0660, MDF0661, MDF0662, MDF0678, MDF0679, MDF0680, MDF0681, MDF0684, MDF0685, MDF0875, MDF0932, MDF0984, MDF1014, MDF1016, MDP0020, MDP0040, MDP0163, MDP0174, MDP0504, MDP0505, MDP0506, MDP0533, MDP0588, MDP0615, MDP0647, MDP0648, MDP0649, MDP0659, MDP0660, MDP0661, MDP0665, MDP0666, MDP0667, MDP0681, MDP0682, MDP0683, MDP0729, MDE0029, MDE0030, MDE0063, MDE0064, MDE0066, MDT0086

### ARC-side rows (not METR)

MDF0050, MDF0049, MDF0048, MDF0088, MDF0083, MDF0415, MDF0210, MDF0057, MDF0056, MDF0054, MDF0055, MDF0061, MDF0060, MDF0059, MDF0413, MDF0063, MDP0012, MDF0123, MDF0124

### Timeline rows

MDT0086, MDT0087

### Bounded negatives

Counts (live): 34 rows; by source class: IRS TEOS and e-file index 1, archives 2, court dockets 1, funder filings 4, issuer statements 12, press 1, procurement records 1, project documents 1, public grant databases 3, recipient filings 1, self-statements 3, state registries 3, statutory records requests 1
- MDS0018: self-statements | GET https://survivalandflourishing.com/ and https://survivalandflourishing.fund/ ; search Jane Street => none found in SFC/SFF public pages as of 2026-09-16T05:34:01Z for a first-person METR gift by a named Jane Street individual | n=0 | role=negative strength=supporting lane=MD07
- MDS0225: issuer statements | GET https://survivalandflourishing.fund/sff-2023-h2-recommendations filter organization name contains METR OR Model Evaluation OR Alignment Research Center OR ARC Evals => none found in SFF-2023-H2 recommendations page as of 2026-09-16T06:04:57Z | n=0 | role=negative strength=supporting lane=MD09
- MDS0226: issuer statements | GET https://survivalandflourishing.fund/sff-2022-h1-recommendations filter organization name contains METR OR Model Evaluation OR Alignment Research Center OR ARC Evals => none found in SFF-2022-H1 recommendations page as of 2026-09-16T06:04:57Z | n=0 | role=negative strength=supporting lane=MD09
- MDS0227: issuer statements | GET https://survivalandflourishing.fund/sff-2021-h2-recommendations filter organization name contains METR OR Model Evaluation OR Alignment Research Center OR ARC Evals => none found in SFF-2021-H2 recommendations page as of 2026-09-16T06:04:57Z | n=0 | role=negative strength=supporting lane=MD09
- MDS0228: issuer statements | GET https://survivalandflourishing.fund/sff-2021-h1-recommendations filter organization name contains METR OR Model Evaluation OR Alignment Research Center OR ARC Evals => none found in SFF-2021-H1 recommendations page as of 2026-09-16T06:04:57Z | n=0 | role=negative strength=supporting lane=MD09
- MDS0229: issuer statements | GET https://survivalandflourishing.fund/sff-2020-h2-recommendations filter organization name contains METR OR Model Evaluation OR Alignment Research Center OR ARC Evals => none found in SFF-2020-H2 recommendations page as of 2026-09-16T06:04:57Z | n=0 | role=negative strength=supporting lane=MD09
- MDS0230: issuer statements | GET https://survivalandflourishing.fund/sff-2020-h1-recommendations filter organization name contains METR OR Model Evaluation OR Alignment Research Center OR ARC Evals => none found in SFF-2020-H1 recommendations page as of 2026-09-16T06:04:57Z | n=0 | role=negative strength=supporting lane=MD09
- MDS0231: issuer statements | GET https://survivalandflourishing.fund/sff-2019-q4-recommendations filter organization name contains METR OR Model Evaluation OR Alignment Research Center OR ARC Evals => none found in SFF-2019 recommendations page as of 2026-09-16T06:04:57Z | n=0 | role=negative strength=supporting lane=MD09
- MDS0232: self-statements | GET https://jaan.online/philanthropy/donations.csv filter recipient contains Model Evaluation or METR and disbursed>=2025-01-01 => none found in jaan.online/philanthropy/donations.csv METR/Model Evaluation rows after 2024-12-06 as of 2026-09-16T06:04:57Z | n=0 | role=negative strength=primary lane=MD09
- MDS0233: self-statements | GET https://jaan.online/philanthropy/donations.csv filter recipient Alignment Research Center purpose ARC Evals => none found in jaan.online/philanthropy/donations.csv for a second ARC Evals Team line that would close the $3,247,000 recommendation as of 2026-09-16T06:04:57Z | n=0 | role=negative strength=supportin
- MDS0234: funder filings | ProPublica API v2 search.json?q=Survival%20and%20Flourishing and q=Survival%20and%20Flourishing%20Corp => none found in ProPublica API v2 search q=Survival and Flourishing (total_results=0) as of 2026-09-16T06:04:57Z | n=0 | role=negative strength=supporting lane=MD09
- MDS0235: funder filings | IRS e-file index_2026.csv EIN 371795297 or 205205488 object later than TY2024; FP TY2024 XML has no 2025 METR amount other than $184,000 => none found in IRS e-file index_2026.csv for EIN 371795297 or 205205488 as of 2026-09-16T06:04:57Z | n=0 | role=negative strength=supporting lane=MD09
- MDS0236: funder filings | This lane checked Founders Pledge TY2023 XML (ARC Evals $1,846,000 only) not a FLI XML; remainder not in Tallinn ledger => none found in Founders Pledge Inc TY2023 990-PF XML 202402359349100515 for a second ARC Evals amount that would total $3,247,000 as of 2026-09-16T06:04:57Z | n=0 | role=negative strength=supporting la
- MDS0238: recipient filings | GET IRS e-file XML 202523209349300367 IRS990ScheduleB => none found in METR FY2024 Form 990 XML 202523209349300367 Schedule B (ContributorNum RESTRICTED) as of 2026-09-16T06:04:57Z | n=0 | role=negative strength=primary lane=MD09
- MDS0240: court dockets | CourtListener REST v4 search q="Jaan Tallinn" METR type=o => none found in CourtListener REST v4 search q="Jaan Tallinn" METR type=o (count=0) as of 2026-09-16T06:04:57Z | n=0 | role=negative strength=supporting lane=MD09
- MDS0241: procurement records | GET https://api.usaspending.gov/api/v2/search/spending_by_award/ (POST endpoint) => none found in USAspending spending_by_award GET (HTTP 405) as of 2026-09-16T06:04:57Z | n=0 | role=context strength=supporting lane=MD09
- MDS0242: state registries | GET https://rct.doj.ca.gov/Verification/Web/Search.aspx?facility=Y => none found in CA OAG RCT Search.aspx?facility=Y (HTTP 404) as of 2026-09-16T06:04:57Z | n=0 | role=context strength=supporting lane=MD09
- MDS0243: public grant databases | GET https://lab.candid.org/ => none found in lab.candid.org (DNS failure) as of 2026-09-16T06:04:57Z | n=0 | role=context strength=supporting lane=MD09
- MDS0244: archives | Live GET survivalandflourishing.fund round pages 2019–2025; Wayback not required => none found in Wayback fallback because live SFF round pages returned HTTP 200 as of 2026-09-16T06:04:57Z | n=0 | role=context strength=supporting lane=MD09
- MDS0245: project documents | SFF round pages and matching-pledges page (public HTML); no grant-letter PDF linked for METR => none found in SFF matching-pledges page for a METR/ARC grant letter naming the check-writing entity as of 2026-09-16T06:04:57Z | n=0 | role=negative strength=supporting lane=MD09
- MDS0246: statutory records requests | This lane sends nothing (embargo); no FOIA/CPRA/state charity request was filed => none found in this lane for a statutory records request (lane embargo: send nothing) as of 2026-09-16T06:04:57Z | n=0 | role=context strength=supporting lane=MD09
- MDS0298: public grant databases | GET https://survivalandflourishing.fund/ (home table) and GET /recommendations ; count <tr> and filter recipient cells => SFF home/recommendations table enumerated: 472 data rows SFF-2019-Q3 to SFF-2025; METR Inc rows SFF-2025 $120,000 + $428,000 matching pledge and SFF-2024 $204,000; ARC rows separate | n=472 | role=evi
- MDS0337: issuer statements | GET https://survivalandflourishing.fund/sff-2026-recommendations => none found in https://survivalandflourishing.fund/sff-2026-recommendations as of 2026-09-16T06:05:27Z | n=0 | role=negative strength=supporting lane=MD14
- MDS0495: issuer statements | Re-read held lineage quote from https://survivalandflourishing.fund/recommendations ; not recollected as a new amount => none found in the held SFF-2025 recommendation text for Canary as of 2026-09-16T07:26:30Z | n=0 | role=negative strength=supporting lane=MD17
- MDS1073: issuer statements | GET https://survivalandflourishing.fund/2026/recommendations => none found in SFF-2026 recommendations page (HTTP 404 Not Found) as of 2026-09-16T09:49:22Z | n=0 | role=context strength=supporting lane=MD09
- MDS1074: funder filings | GET IRS e-file XML 202521139349301937 (FLI EIN 471052538 TY2023) RecipientEIN 863605182 or 991219864 or name Alignment Research / METR / Evals => none found in Future of Life Institute TY2023 Form 990 XML 202521139349301937 for Alignment Research Center / METR / EIN 863605182 or 991219864 as of 2026-09-16T09:49:22Z | n=0 | role=context strength
- MDS1075: state registries | GET https://oag.ca.gov/sites/all/files/agweb/pdfs/charities/reports/charities-may-not-operate.csv filter FEIN=991219864 => none found in California Attorney General May Not Operate or Solicit CSV for FEIN 991219864 or MODEL EVALUATION as of 2026-09-16T09:49:22Z | n=0 | role=context strength=supporting lane=MD09
- MDS1076: state registries | GET https://ca-rcf.evokeplatform.com/app/publicPortal/verification => none found in CA Registry Search Tool machine-readable GET (ca-rcf.evokeplatform.com EVOKE SPA shell) as of 2026-09-16T09:49:22Z | n=0 | role=context strength=supporting lane=MD09
- MDS1077: public grant databases | GET https://www.guidestar.org/search?q=METR => none found in GuideStar/Candid search page q=METR for an SFF or Tallinn grant to METR as of 2026-09-16T09:49:22Z | n=0 | role=context strength=supporting lane=MD09
- MDS1078: archives | Live GET survivalandflourishing.fund round pages 2019–2025; Wayback CDX as archive class => none found in Wayback CDX for survivalandflourishing.fund/recommendations (HTTP 504); live SFF round pages returned HTTP 200 as of 2026-09-16T09:49:22Z | n=0 | role=context strength=supporting lane=MD
- MDS1079: IRS TEOS and e-file index | GET https://apps.irs.gov/app/eos/ => none found in IRS TEOS interactive app apps.irs.gov/app/eos (HTTP 403 Access Denied) as of 2026-09-16T09:49:22Z | n=0 | role=context strength=supporting lane=MD09
- MDS1081: press | GET Semafor 2023-04-28 and Postimees 2026-02-22; filter for SFF or METR or ARC grant amount => none found in Semafor 2023-04-28 interview and Postimees 2026-02-22 article for an SFF/METR/ARC grant amount as of 2026-09-16T09:49:22Z | n=0 | role=negative strength=supporting lane=MD09
- MDS1121: issuer statements | GET https://survivalandflourishing.fund/2026/further-opportunities => none found in https://survivalandflourishing.fund/2026/further-opportunities as of 2026-09-16T09:43:26Z | n=0 | role=context strength=supporting lane=MD14
- MDS1176: issuer statements | GET https://survivalandflourishing.fund/sff-2026-recommendations => none found in https://survivalandflourishing.fund/sff-2026-recommendations as of 2026-09-16T12:22:35Z | n=0 | role=context strength=supporting lane=MD46

### Contradictions, duplicates and defects

- TYPE CONFLICT: the SFF-2025 $428,000 matching pledge is money_type=recommendation on MDF0046 (MD09 primary), MDF0197 (MD23), MDP0185 (MD23 primary), seed MDF0009, MDP0039, MDP0505 and MD53 rows, but money_type=commitment on MDF0081 (MD13), MDF0217 (MD33), MDF0544 and MDF0680 (MD50 audits of those). supporter_coverage.csv therefore lists money_types_seen commitment; paid_grant; recommendation. A figure must pick one label; the primary MD09 row says recommendation (conditional matching pledge).
- PAYER PLACEMENT CONFLICT: for the same recommendations, from_entity is 'Jaan Tallinn (funder named on the SFF table)' with SFF as intermediary (MD09/MD23/MD33), 'Survival and Flourishing Fund' with Jaan Tallinn as intermediary (MD13: MDF0079/MDF0080/MDF0081), or 'Survival and Flourishing Fund' alone (MD10: MDF0074/MDF0075; seed 'Survival and Flourishing Fund (Jaan Tallinn)'). No row is a payment by either.
- DUPLICATE/LINEAGE DEFECT: MDF0412 reproduces MDF0052 while its note says 'candidate correction of medium row 18 (promoted MDF0051)' (off by one); MDF0413 reproduces MDF0059 (ARC $147,000) while its note says 'candidate correction of medium row 28 (promoted MDF0058)' (METR $184,000). Neither carries 'supersedes'; MDF0051/MDF0052/MDF0058/MDF0059 remain live.
- TWO FIGURES IN ONE CELL: seed MDF0009 and MDP0039 amount_usd='120000 + 428000 matching pledge'.
- Recommendation vs ledger: SFF-2024 $204,000 recommended; ledger shows $184,000 (FP-US, 2024-12-06) + $10,000 + $10,000 (SFF-spec, July 2024) = the same total by arithmetic, but the pack does not merge them and no payment for the SFF-2025 $120,000 or $428,000 appears on the ledger through 2026-08-14 (MDS0232, MDS1117).
- Date fields: SFF rows use round labels (SFF-2024, SFF-2025) with date_precision=interval; MD10 rows put 2024 / 2025 in the date column; MDF0093 uses the page last-published date 2025-02-15. None is a payment date.

### Figure notes
Draw as three separate money types: recommendation (SFF-2024 $204,000; SFF-2025 $120,000), conditional matching pledge (SFF-2025 $428,000, deadline 2026-09-30, drawn-status unknown), paid_grant on the donor's public ledger (2024-07-23 $10,000; 2024-07-24 $10,000; 2024-12-06 $184,000). Mark the $184,000 ledger line and Founders Pledge Inc filed $184,000 (MDF0058) as the same money seen from two documents, and the 2 x $10,000 and SVCF $20,000 (MDF0037) as a dollar match the pack does not merge. Never sum. Jaan Tallinn's Anthropic Series A role (MDR0024) belongs to C05, not to a funding figure. Primary anchors: MDF0045, MDF0046, MDF0047, MDF0051, MDF0052, MDF0053; primary negatives MDS0232, MDS0238.


## David Farhi

**How METR names it:** metr.org/about: 'and many others, such as David Farhi, Geoff Ralston, Dylan Field and Steve Newman'; 2026-08-14 update: 'many others, including David Farhi, ...'

**Status:** acknowledged, no public amount, date or vehicle

### Facts (draw only from these)

- **MDF0023** [evidence/primary; lane MD08] untyped (no amount)  | 2026-09-16 | David Farhi -> METR (Model Evaluation and Threat Research, Inc.) | status: acknowledged as a supporter; amount, date, vehicle and money type not disclosed by the source | purpose: n/a
  - ANCHOR (primary): named on the live metr.org/about (fetched 2026-09-16) among 'many others, such as'; no amount, date or vehicle. The date on this row is the fetch date, not a gift date.
  - url: https://metr.org/about
- **MDF0024** [evidence/supporting; lane MD08] untyped (no amount)  | 2026-08-14 | David Farhi -> METR (Model Evaluation and Threat Research, Inc.) | status: acknowledged as a supporter; amount, date, vehicle and money type not disclosed by the source | purpose: n/a
  - ANCHOR: named on the 2026-08-14 funding update as a supporter 'over the years'; the ~$71M sentence is not this person's gift.
  - url: https://metr.org/blog/2026-08-14-funding-update/
- **MDP0049** [evidence/primary; lane MD14] commitment undisclosed  | undated | David Farhi; Geoff Ralston; Dylan Field; Steve Newman -> METR | status: n/a | purpose: n/a
  - Commitment reconciliation: the four named individuals excluded as addends (no public amounts).
  - url: https://metr.org/blog/2026-08-14-funding-update/
- **MDF0232** [context/supporting; lane MD33] untyped (no amount)  | undated | David Farhi -> METR (Model Evaluation and Threat Research) | status: n/a | purpose: n/a
  - MD33: named; amount not on page.
  - url: https://metr.org/about
- **MDT0013** [evidence/primary; lane MD08] untyped (no amount)  | 2025-12-16 | David Farhi; Dylan Field -> METR (Model Evaluation and Threat Research, Inc.) | status: n/a | purpose: n/a
  - First recovered about-page naming of Farhi and Field: 2025-12-16 capture (appearance, not a gift date).
  - url: https://web.archive.org/web/20251216013159id_/https://metr.org/about
- **MDR0013** [evidence/primary; lane MD08] untyped (no amount)  | 2026-06-16 | David Farhi -> Guardrails Alliance (political committee; not METR) | status: n/a | purpose: n/a
  - NOT METR MONEY: FEC Schedule A $3,000 to Guardrails Alliance 2026-06-16 (self-reported employer Self Employed). Recorded for C03; keep off any METR funding figure.
  - url: https://api.open.fec.gov/v1/schedules/schedule_a/?contributor_name=farhi%2C+david&two_year_transaction_period=2026&per_page=20&sort=-contribution_receipt_date&api_key=DEMO_KEY
- **MDR0012** [evidence/supporting; lane MD08] untyped (no amount)  | 2026-07-15 | David Farhi -> OpenAI | status: n/a | purpose: n/a
  - NOT METR MONEY: WIRED 2026-07-15 reports departure from OpenAI in summer 2025; gift date to METR unknown, so employment at gift date cannot be stated.
  - url: https://www.wired.com/story/openai-employees-donations-guardrails-alliance-leading-the-future/

### Restatement / locator rows (do not cite as new facts)

MDF0486, MDF0487, MDF0695, MDP0183, MDP0515, MDP0730, MDR0014, MDR0015, MDR0127, MDR0128, MDR0129, MDR0130, MDR0155, MDR0156, MDR0172, MDR0183, MDR0184, MDE0079

### Timeline rows

MDT0013, MDT0015, MDT0094, MDT0095, MDT0227

### Bounded negatives

Counts (live): 13 rows; by source class: DAF sponsor filings 1, SEC 1, court dockets 1, funder filings 2, issuer statements 5, press 1, self-statements 2
- MDS0077: press | GET WIRED Guardrails Alliance article => first-person statement recovered; it addresses AI regulation, not a gift to METR | n=1 | role=negative strength=supporting lane=MD08
- MDS0078: self-statements | WIRED 2026-07-15 Farhi statement plus X/EA Forum name search for a METR gift => none found in WIRED 2026-07-15 Farhi statement plus X/EA Forum name search for a METR gift as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0082: funder filings | ProPublica API v2 org search q=David Farhi => none found in ProPublica API v2 org search q=David Farhi as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0086: issuer statements | METR about and funding-update for a gift date, then dated employer records at that date => none found in METR about page and 2026-08-14 funding update for a per-person gift date as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0090: issuer statements | METR funding update ~$71M six-month commitments; about-page first naming => gift date not disclosed; cannot be placed inside or outside the February-August 2026 window | n=0 | role=negative strength=supporting lane=MD08
- MDS0095: funder filings | GET /nonprofits/api/v2/search.json?q=David Farhi => none found in ProPublica API v2 search.json q=David Farhi as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0099: DAF sponsor filings | Vanguard Charitable / other sponsor Schedule I rows identify recipient EIN not adviser; Field Form 4 DAF unnamed => none found in DAF sponsor public filings for an adviser name on a METR grant as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0102: SEC | Field Form 4s fetched (DAF, METR not named); no Farhi/Ralston/Newman Form 4 METR path => none found in SEC Form 4/gift filings for Farhi, Ralston, or Newman that name METR as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0103: court dockets | GET courtlistener.com type=o METR+(Farhi|Ralston|Field|Newman) => none found in CourtListener opinions query METR+(Farhi|Ralston|Field|Newman) as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0106: self-statements | GET https://forum.effectivealtruism.org/search?query=David Farhi METR => none found in EA Forum search query=David Farhi METR for a first-person METR gift statement as of 2026-09-16T05:33:55Z | n=0 | role=context strength=supporting lane=MD08
- MDS0509: issuer statements | GET https://metr.org/about ; David Farhi is named by the recipient only => none found in a funder-issued grant letter or filing for David Farhi as of 2026-09-16T07:21:32Z | n=0 | role=negative strength=supporting lane=MD23
- MDS0776: issuer statements | GET anthropic.com Series A, E, F, G, H and /company; HTML search those supporter names => none found in Anthropic Series A/E/F/G/H and /company pages as of 2026-09-16T09:37:25Z for Packard, Pew, Sijbrandij, Audacious, LaCentra-Sumerlin, Astralis, Expa.org, Longview, Effektiv Spenden, David
- MDS1068: issuer statements | METR funding update ~$71M six-month commitments; about-page first naming => date of this individual's gift is not disclosed | n=0 | role=context strength=supporting lane=MD08

### Contradictions, duplicates and defects

- METR's wording changed from 'a wide range of individuals directly, such as ...' (2025-12 to 2026-06 captures: MDT0015/MDT0227) to 'many others, such as ...' (live); 'directly' was METR's list wording, not a vehicle disclosure.
- The $3,000 political contribution (MDR0013/MDR0128) is the only dollar figure attached to this name in the pack and it is not a METR gift.

### Figure notes
Acknowledged only. Anchors MDF0023, MDF0024. Do not import FEC or employment rows into a money figure.


## Geoff Ralston

**How METR names it:** metr.org/about: 'many others, such as ... Geoff Ralston ...'; 2026-08-14 update; first named on the 2025-12-07 capture ('a wide range of individuals directly, such as Geoff Ralston')

**Status:** acknowledged, no public amount, date or vehicle

### Facts (draw only from these)

- **MDF0025** [evidence/primary; lane MD08] untyped (no amount)  | 2026-09-16 | Geoff Ralston -> METR (Model Evaluation and Threat Research, Inc.) | status: acknowledged as a supporter; amount, date, vehicle and money type not disclosed by the source | purpose: n/a
  - ANCHOR (primary): named on the live metr.org/about (fetched 2026-09-16) among 'many others, such as'; no amount, date or vehicle. The date on this row is the fetch date, not a gift date.
  - url: https://metr.org/about
- **MDF0026** [evidence/supporting; lane MD08] untyped (no amount)  | 2026-08-14 | Geoff Ralston -> METR (Model Evaluation and Threat Research, Inc.) | status: acknowledged as a supporter; amount, date, vehicle and money type not disclosed by the source | purpose: n/a
  - ANCHOR: named on the 2026-08-14 funding update as a supporter 'over the years'; the ~$71M sentence is not this person's gift.
  - url: https://metr.org/blog/2026-08-14-funding-update/
- **MDP0049** [evidence/primary; lane MD14] commitment undisclosed  | undated | David Farhi; Geoff Ralston; Dylan Field; Steve Newman -> METR | status: n/a | purpose: n/a
  - Commitment reconciliation: the four named individuals excluded as addends (no public amounts).
  - url: https://metr.org/blog/2026-08-14-funding-update/
- **MDF0233** [context/supporting; lane MD33] untyped (no amount)  | undated | Geoff Ralston -> METR (Model Evaluation and Threat Research) | status: n/a | purpose: n/a
  - MD33: named; amount not on page.
  - url: https://metr.org/about
- **MDT0012** [evidence/primary; lane MD08] untyped (no amount)  | 2025-12-07 | Geoff Ralston -> METR (Model Evaluation and Threat Research, Inc.) | status: n/a | purpose: n/a
  - First recovered about-page naming: 2025-12-07 capture (only individual named then).
  - url: https://web.archive.org/web/20251207085707id_/https://metr.org/about
- **MDR0011** [context/supporting; lane MD08] untyped (no amount)  | undated | Geoff Ralston -> AVERI | status: n/a | purpose: n/a
  - NOT METR MONEY: AVERI names Geoff Ralston among its funders; METR not named; vehicle not stated.
  - url: https://www.averi.org/about
- **MDR0017** [evidence/supporting; lane MD08] untyped (no amount)  | 2025-04-17 | Geoff Ralston -> Safe Artificial Intelligence Fund | status: n/a | purpose: n/a
  - NOT METR MONEY: former Y Combinator president; SAIF founder (TechCrunch 2025-04-17); SAIF is a VC vehicle, not a METR payer.
  - url: https://techcrunch.com/2025/04/17/former-y-combinator-president-geoff-ralston-launches-new-ai-safety-fund/

### Restatement / locator rows (do not cite as new facts)

MDF0488, MDF0489, MDF0696, MDP0183, MDP0515, MDP0731, MDR0126, MDR0132, MDR0158, MDR0169, MDE0013, MDE0080

### Timeline rows

MDT0012, MDT0015, MDT0088, MDT0089, MDT0227

### Bounded negatives

Counts (live): 11 rows; by source class: DAF sponsor filings 1, SEC 1, court dockets 1, funder filings 2, issuer statements 5, self-statements 1
- MDS0079: self-statements | X from:geoffralston METR/donate => none found in X from:geoffralston METR/donate as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0083: funder filings | ProPublica API v2 org search q=Geoff Ralston; SAIF is a VC fund not a 990-PF => none found in ProPublica API v2 org search q=Geoff Ralston; SAIF is a VC fund not a 990-PF as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0087: issuer statements | METR about and funding-update for a gift date, then dated employer records at that date => none found in METR about page and 2026-08-14 funding update for a per-person gift date as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0092: issuer statements | METR funding update ~$71M six-month commitments; about-page first naming => gift date not disclosed; cannot be placed inside or outside the February-August 2026 window | n=0 | role=negative strength=supporting lane=MD08
- MDS0096: funder filings | GET /nonprofits/api/v2/search.json?q=Geoff Ralston => none found in ProPublica API v2 search.json q=Geoff Ralston as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0099: DAF sponsor filings | Vanguard Charitable / other sponsor Schedule I rows identify recipient EIN not adviser; Field Form 4 DAF unnamed => none found in DAF sponsor public filings for an adviser name on a METR grant as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0102: SEC | Field Form 4s fetched (DAF, METR not named); no Farhi/Ralston/Newman Form 4 METR path => none found in SEC Form 4/gift filings for Farhi, Ralston, or Newman that name METR as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0103: court dockets | GET courtlistener.com type=o METR+(Farhi|Ralston|Field|Newman) => none found in CourtListener opinions query METR+(Farhi|Ralston|Field|Newman) as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0510: issuer statements | GET https://metr.org/about ; Geoff Ralston is named by the recipient only => none found in a funder-issued grant letter or filing for Geoff Ralston as of 2026-09-16T07:21:32Z | n=0 | role=negative strength=supporting lane=MD23
- MDS0776: issuer statements | GET anthropic.com Series A, E, F, G, H and /company; HTML search those supporter names => none found in Anthropic Series A/E/F/G/H and /company pages as of 2026-09-16T09:37:25Z for Packard, Pew, Sijbrandij, Audacious, LaCentra-Sumerlin, Astralis, Expa.org, Longview, Effektiv Spenden, David
- MDS1069: issuer statements | METR funding update ~$71M six-month commitments; about-page first naming => date of this individual's gift is not disclosed | n=0 | role=context strength=supporting lane=MD08

### Contradictions, duplicates and defects

- METR's wording changed from 'a wide range of individuals directly, such as ...' (2025-12 to 2026-06 captures: MDT0015/MDT0227) to 'many others, such as ...' (live); 'directly' was METR's list wording, not a vehicle disclosure.
- MDE0013 carries '$100,000' as SAIF's planned per-company check size; it is not a METR amount.

### Figure notes
Acknowledged only. Anchors MDF0025, MDF0026.


## Dylan Field

**How METR names it:** metr.org/about: 'many others, such as ... Dylan Field ...'; 2026-08-14 update

**Status:** acknowledged, no public amount, date or vehicle

### Facts (draw only from these)

- **MDF0027** [evidence/primary; lane MD08] untyped (no amount)  | 2026-09-16 | Dylan Field -> METR (Model Evaluation and Threat Research, Inc.) | status: acknowledged as a supporter; amount, date, vehicle and money type not disclosed by the source | purpose: n/a
  - ANCHOR (primary): named on the live metr.org/about (fetched 2026-09-16) among 'many others, such as'; no amount, date or vehicle. The date on this row is the fetch date, not a gift date.
  - url: https://metr.org/about
- **MDF0028** [evidence/supporting; lane MD08] untyped (no amount)  | 2026-08-14 | Dylan Field -> METR (Model Evaluation and Threat Research, Inc.) | status: acknowledged as a supporter; amount, date, vehicle and money type not disclosed by the source | purpose: n/a
  - ANCHOR: named on the 2026-08-14 funding update as a supporter 'over the years'; the ~$71M sentence is not this person's gift.
  - url: https://metr.org/blog/2026-08-14-funding-update/
- **MDP0049** [evidence/primary; lane MD14] commitment undisclosed  | undated | David Farhi; Geoff Ralston; Dylan Field; Steve Newman -> METR | status: n/a | purpose: n/a
  - Commitment reconciliation: the four named individuals excluded as addends (no public amounts).
  - url: https://metr.org/blog/2026-08-14-funding-update/
- **MDF0234** [context/supporting; lane MD33] untyped (no amount)  | undated | Dylan Field -> METR (Model Evaluation and Threat Research) | status: n/a | purpose: n/a
  - MD33: named; amount not on page.
  - url: https://metr.org/about
- **MDT0013** [evidence/primary; lane MD08] untyped (no amount)  | 2025-12-16 | David Farhi; Dylan Field -> METR (Model Evaluation and Threat Research, Inc.) | status: n/a | purpose: n/a
  - First recovered about-page naming of Farhi and Field: 2025-12-16 capture.
  - url: https://web.archive.org/web/20251216013159id_/https://metr.org/about
- **MDP0007** [context/supporting; lane MD08] transfer 1250000 Class B Common Stock; transactionPricePerShare 0; code G  | 2025-11-28 | Dylan Field -> unnamed donor-advised fund | status: n/a | purpose: n/a
  - NOT A METR GIFT: SEC Form 4 2025-11-28 bona fide gift of 1,250,000 Figma Class B shares to an unnamed donor-advised fund; METR not named; shares not converted to USD.
  - url: https://www.sec.gov/Archives/edgar/data/1579878/000207358625000010/form4-12032025_121217.xml
- **MDP0008** [context/supporting; lane MD08] transfer 1250000 Class B Common Stock; transactionPricePerShare 0; code G  | 2026-08-17 | Dylan Field -> unnamed donor-advised fund | status: n/a | purpose: n/a
  - NOT A METR GIFT: SEC Form 4 2026-08-17 bona fide gift of 1,250,000 Figma Class B shares to an unnamed DAF; METR not named.
  - url: https://www.sec.gov/Archives/edgar/data/1579878/000207358626000012/form4-08192026_100818.xml
- **MDR0016** [evidence/supporting; lane MD08] untyped (no amount)  | 2026-08-17 | Dylan Field -> Figma, Inc. | status: n/a | purpose: n/a
  - Employment: President and CEO of Figma, Inc. on the dated Form 4s; METR gift date unknown.
  - url: https://www.sec.gov/Archives/edgar/data/1579878/000207358626000012/form4-08192026_100818.xml

### Restatement / locator rows (do not cite as new facts)

MDF0490, MDF0491, MDF0697, MDP0183, MDP0476, MDP0477, MDP0515, MDP0732, MDR0131, MDR0170, MDE0081

### Timeline rows

MDT0013, MDT0015, MDT0096, MDT0097, MDT0226, MDT0227

### Bounded negatives

Counts (live): 11 rows; by source class: SEC 1, court dockets 1, funder filings 2, issuer statements 4, self-statements 3
- MDS0080: self-statements | X from:zoink METR/donate => none found in X from:zoink METR/donate as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0084: funder filings | Form 4 DAF gifts do not name METR; ProPublica API v2 q=Dylan Field total_results=0 => none found in Form 4 DAF gifts do not name METR; ProPublica API v2 q=Dylan Field total_results=0 as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0088: issuer statements | METR about and funding-update for a gift date, then dated employer records at that date => none found in METR about page and 2026-08-14 funding update for a per-person gift date as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0091: issuer statements | METR funding update ~$71M six-month commitments; about-page first naming => gift date not disclosed; cannot be placed inside or outside the February-August 2026 window | n=0 | role=negative strength=supporting lane=MD08
- MDS0097: funder filings | GET /nonprofits/api/v2/search.json?q=Dylan Field => none found in ProPublica API v2 search.json q=Dylan Field as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0103: court dockets | GET courtlistener.com type=o METR+(Farhi|Ralston|Field|Newman) => none found in CourtListener opinions query METR+(Farhi|Ralston|Field|Newman) as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0108: self-statements | GET https://givingpledge.org/search?q=Dylan Field (404) => none found in Giving Pledge search URL for Dylan Field as a pledger as of 2026-09-16T05:33:55Z | n=0 | role=context strength=supporting lane=MD08
- MDS0511: issuer statements | GET https://metr.org/about ; Dylan Field is named by the recipient only => none found in a funder-issued grant letter or filing for Dylan Field as of 2026-09-16T07:21:32Z | n=0 | role=negative strength=supporting lane=MD23
- MDS0761: SEC | SEC EFTS LATEST/search-index q="Dylan Field" Anthropic file_date 2020-01-01..2026-09-16 => none found in SEC EFTS q="Dylan Field" Anthropic for an Anthropic, PBC issuer filing as of 2026-09-16T09:37:55Z (6 hits were Figma, Inc. CIK 0001579878) | n=0 | role=negative strength=supporting lane=
- MDS1066: self-statements | X keyword search from:zoink (METR OR donate OR donation OR donor OR fund) => post recovered; it praises a METR report and does not state a gift, vehicle, amount, or date | n=1 | role=context strength=supporting lane=MD08
- MDS1070: issuer statements | METR funding update ~$71M six-month commitments; about-page first naming => date of this individual's gift is not disclosed | n=0 | role=context strength=supporting lane=MD08

### Contradictions, duplicates and defects

- METR's wording changed from 'a wide range of individuals directly, such as ...' (2025-12 to 2026-06 captures: MDT0015/MDT0227) to 'many others, such as ...' (live); 'directly' was METR's list wording, not a vehicle disclosure.
- The two Form 4 DAF gifts (MDP0007/MDP0008, typed transfer with share counts only) name no grantee; they must not be drawn as METR money or as a METR-bound DAF.

### Figure notes
Acknowledged only. Anchors MDF0027, MDF0028.


## Steve Newman

**How METR names it:** metr.org/about: 'many others, such as ... Steve Newman'; 2026-08-14 update; first named on the 2026-06-01 capture

**Status:** acknowledged, no public amount, date or vehicle

### Facts (draw only from these)

- **MDF0029** [evidence/primary; lane MD08] untyped (no amount)  | 2026-09-16 | Steve Newman -> METR (Model Evaluation and Threat Research, Inc.) | status: acknowledged as a supporter; amount, date, vehicle and money type not disclosed by the source | purpose: n/a
  - ANCHOR (primary): named on the live metr.org/about (fetched 2026-09-16) among 'many others, such as'; no amount, date or vehicle. The date on this row is the fetch date, not a gift date.
  - url: https://metr.org/about
- **MDF0030** [evidence/supporting; lane MD08] untyped (no amount)  | 2026-08-14 | Steve Newman -> METR (Model Evaluation and Threat Research, Inc.) | status: acknowledged as a supporter; amount, date, vehicle and money type not disclosed by the source | purpose: n/a
  - ANCHOR: named on the 2026-08-14 funding update as a supporter 'over the years'; the ~$71M sentence is not this person's gift.
  - url: https://metr.org/blog/2026-08-14-funding-update/
- **MDP0049** [evidence/primary; lane MD14] commitment undisclosed  | undated | David Farhi; Geoff Ralston; Dylan Field; Steve Newman -> METR | status: n/a | purpose: n/a
  - Commitment reconciliation: the four named individuals excluded as addends (no public amounts).
  - url: https://metr.org/blog/2026-08-14-funding-update/
- **MDF0235** [context/supporting; lane MD33] untyped (no amount)  | undated | Steve Newman -> METR (Model Evaluation and Threat Research) | status: n/a | purpose: n/a
  - MD33: named; amount not on page.
  - url: https://metr.org/about
- **MDT0014** [evidence/primary; lane MD08] untyped (no amount)  | 2026-06-01 | Steve Newman -> METR (Model Evaluation and Threat Research, Inc.) | status: n/a | purpose: n/a
  - First recovered about-page naming: 2026-06-01 capture (Farhi, Field, Ralston already present).
  - url: https://web.archive.org/web/20260601232933id_/https://metr.org/about
- **MDR0018** [evidence/supporting; lane MD08] untyped (no amount)  | undated | Steve Newman -> Golden Gate Institute for AI | status: n/a | purpose: n/a
  - NOT METR MONEY: self-described chairman and president of Golden Gate Institute for AI.
  - url: https://secondthoughts.ai/about
- **MDR0019** [evidence/supporting; lane MD08] untyped (no amount)  | undated | Steve Newman -> Epoch AI | status: n/a | purpose: n/a
  - NOT METR MONEY: listed on the Epoch AI board of directors.
  - url: https://epoch.ai/about/team

### Restatement / locator rows (do not cite as new facts)

MDF0492, MDF0493, MDF0698, MDP0183, MDP0515, MDP0733, MDR0133, MDR0134, MDR0164, MDR0167, MDE0082

### Timeline rows

MDT0014, MDT0015, MDT0100, MDT0101, MDT0227

### Bounded negatives

Counts (live): 9 rows; by source class: court dockets 1, funder filings 2, issuer statements 4, self-statements 2
- MDS0081: self-statements | X from:snewmanpv METR/donate => none found in X from:snewmanpv METR/donate as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0085: funder filings | ProPublica API v2 q=Steve Newman returns unrelated homonym foundations => none found in ProPublica API v2 q=Steve Newman returns unrelated homonym foundations as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0089: issuer statements | METR about and funding-update for a gift date, then dated employer records at that date => none found in METR about page and 2026-08-14 funding update for a per-person gift date as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0093: issuer statements | METR funding update ~$71M six-month commitments; about-page first naming => gift date not disclosed; cannot be placed inside or outside the February-August 2026 window | n=0 | role=negative strength=supporting lane=MD08
- MDS0098: funder filings | GET /nonprofits/api/v2/search.json?q=Steve Newman => none found in identity-confirmed 990-PF of the METR-named Steve Newman in ProPublica API v2 q=Steve Newman (3 homonym orgs excluded) as of 2026-09-16T05:33:55Z | n=3 | role=negative strength=supportin
- MDS0103: court dockets | GET courtlistener.com type=o METR+(Farhi|Ralston|Field|Newman) => none found in CourtListener opinions query METR+(Farhi|Ralston|Field|Newman) as of 2026-09-16T05:33:55Z | n=0 | role=negative strength=supporting lane=MD08
- MDS0512: issuer statements | GET https://metr.org/about ; Steve Newman is named by the recipient only => none found in a funder-issued grant letter or filing for Steve Newman as of 2026-09-16T07:21:32Z | n=0 | role=negative strength=supporting lane=MD23
- MDS1067: self-statements | X keyword search from:snewmanpv (METR OR donate OR donation OR donor OR fund) => posts recovered; they discuss METR time-horizon graphs and do not state a gift | n=1 | role=context strength=supporting lane=MD08
- MDS1071: issuer statements | METR funding update ~$71M six-month commitments; about-page first naming => date of this individual's gift is not disclosed | n=0 | role=context strength=supporting lane=MD08

### Contradictions, duplicates and defects

- METR's wording changed from 'a wide range of individuals directly, such as ...' (2025-12 to 2026-06 captures: MDT0015/MDT0227) to 'many others, such as ...' (live); 'directly' was METR's list wording, not a vehicle disclosure.

### Figure notes
Acknowledged only. Anchors MDF0029, MDF0030. First-appearance window 2026-05-25 to 2026-06-01 (MDT0100/MDT0101) is inside the Feb-Aug 2026 window but is a page change, not a gift date (MDS0093).


## European AI Office (European Commission DG CNECT, CNECT.A.3) technical-assistance contract

**How METR names it:** metr.org/about: 'Additionally, a small part of our income is from a technical assistance contract with the European AI Office, supporting their approach and technical methods for assessing loss of control risks.'

**Status:** acknowledged; amount identified only at consortium level (contract 4500137790, TED 864574-2025 LOT-0003, payable 1,167,484 EUR to an EquiStamp-led consortium of three); METR share undisclosed; FTS 2025 consumed amount 0.00

### Facts (draw only from these)

- **MDF0150** [evidence/primary; lane MD20] contract 1167484 EUR | 2025-12-15 | European Commission, DG CNECT - Communications Networks, Content and Technology (CNECT.A Artificial Intelligence Office / CNECT.A.3 Artificial Intelligence Safety) -> EquiStamp Inc. (ORG-0009, group leader); Model Evaluation and Threat Research, Inc. (ORG-0010); Epoch Artificial Intelligence, Inc. (ORG-0011) | status: awarded; FTS 2025 consumed amount 0.00; a commitment is not a payment | purpose: Loss of Control Risk Modelling and Evaluation; AI Act technical assistance for AI safety
  - ANCHOR (primary): TED contract award notice 864574-2025 LOT-0003: payable amount 1,167,484 EUR; contract id 4500137790; award 2025-11-28; conclusion 2025-12-15; 36 months; tenderers EquiStamp Inc (group leader), Model Evaluation and Threat Research, Inc., Epoch Artificial Intelligence, Inc. WARNING: amount_usd column holds the EUR figure.
  - url: https://ted.europa.eu/en/notice/864574-2025/xml
- **MDF0151** [evidence/primary; lane MD20] contract 1167484 EUR | 2025-12-15 | CNECT - Directorate-General for Communications Networks, Content and Technology -> EQUISTAMP INC. | status: commitment total 1,167,484.00 EUR; commitment consumed amount 0.00 | purpose: AI SAFETY TOOLS: LOSS OF CONTROL RISK MODELLING AND EVALUATION
  - ANCHOR (primary): Commission FTS 2025 names EQUISTAMP INC. only as beneficiary of legal commitment 4500137790, 1,167,484.00 EUR, consumed 0.00; FTS shows the invoicing party only.
  - url: https://ec.europa.eu/budget/financial-transparency-system/download/2025_FTS_dataset_en.csv
- **MDP0132** [evidence/primary; lane MD20] contract 1167484 EUR | 2025-12-15 | European Commission, DG CNECT -> tendering party TPA-0009 (three legal entities, unmerged) | status: n/a | purpose: n/a
  - Consortium composition; METR GroupLeadIndicator=false; share not disclosed; do not infer one third.
  - url: https://ted.europa.eu/en/notice/864574-2025/xml
- **MDP0131** [evidence/supporting; lane MD20] contract (no amount)  | undated | European AI Office -> METR | status: n/a | purpose: n/a
  - METR's own words: contract class only; no TED number, no EUR figure, no share; 'a small part of our income' is not an amount.
  - url: https://metr.org/about
- **MDP0051** [evidence/supporting; lane MD14] contract undisclosed share of EUR 1167484 EUR | 2025-12-15 | European AI Office -> METR | status: n/a | purpose: n/a
  - Commitment reconciliation: excluded (contract; 2025-12-15; EUR; share undisclosed).
  - url: https://metr.org/about
- **MDP0182** [evidence/primary; lane MD23] contract (no amount)  | undated | European AI Office -> METR | status: n/a | purpose: programme-restricted
  - Purpose classification: programme-restricted (loss-of-control methods).
  - url: https://metr.org/about
- **MDR0109** [evidence/primary; lane MD36] untyped (no amount)  | 2025-11-28 | European Commission, DG CNECT - Communications Networks, Content and Technology (CNECT.A Artificial Intelligence Office / CNECT.A.3 Artificial Intelligence Safety) -> Model Evaluation and Threat Research, Inc. | status: n/a | purpose: n/a
  - Selection record: open procurement EC-CNECT/2025/OP/0032; METR named ORG-0010 tenderer.
  - url: https://ted.europa.eu/en/notice/864574-2025/xml
- **MDP0291** [evidence/primary; lane MD36] untyped (no amount)  | 2025-12-23 | European Commission, DG CNECT -> ? | status: n/a | purpose: n/a
  - Award criteria on the notice: quality 65 / price 35.
  - url: https://ted.europa.eu/en/notice/864574-2025/xml
- **MDP0316** [context/supporting; lane MD44] untyped 1167484 EUR lot payable amount on TED; METR share requested as a copy of an existing annex, not as a calculation EUR | undated | European Commission, DG CNECT -> EquiStamp Inc.-led consortium including Model Evaluation and Threat Research, Inc. | status: n/a | purpose: n/a
  - Unsent Commission access-to-documents draft for the signed contract and any share annex (approved_for_send false).
  - url: https://www.ec.europa.eu/transparency/documents-request
- **MDT0069** [evidence/primary; lane MD24] untyped (no amount)  | 2026-02-02 | ? -> METR | status: n/a | purpose: n/a
  - About-page first appearance of the EU AI Office sentence bounded 2026-01-27 to 2026-02-02.
  - url: https://web.archive.org/web/20260202230601id_/https://metr.org/about
- **MDF0017** [context/supporting; lane S0; SEED] contract undisclosed share of EUR 1,167,484 (LOT-0003 joint tender by 3 firms; EUR as written in TED)  | 2025-12-15 | European AI Office -> METR | status: n/a | purpose: technical assistance on assessing loss-of-control risks
  - SEED BASELINE (context): 'undisclosed share of EUR 1,167,484'.
  - url: https://ted.europa.eu/en/notice/-/detail/864574-2025;https://ted.europa.eu/en/notice/864574-2025/xml;https://metr.org/about
- **MDF0236** [context/supporting; lane MD44] contract 1167484 EUR lot payable amount; METR share not disclosed EUR | 2025-12-15 | European Commission, DG CNECT -> EquiStamp Inc. (group leader); Model Evaluation and Threat Research, Inc.; Epoch Artificial Intelligence, Inc. | status: n/a | purpose: n/a
  - MD44 re-check: notice still published; signed contract and share unpublished.
  - url: https://ted.europa.eu/en/notice/864574-2025/xml

### Restatement / locator rows (do not cite as new facts)

MDF0462, MDF0480, MDF0613, MDF0614, MDF0699, MDF0925, MDF0998, MDF0999, MDF1028, MDP0134, MDP0135, MDP0136, MDP0137, MDP0170, MDP0187, MDP0280, MDP0281, MDP0282, MDP0299, MDP0309, MDP0313, MDP0517, MDP0670, MDP0734, MDR0144, MDE0043, MDT0068, MDT0168, MDT0175

### Timeline rows

MDT0068, MDT0069

### Bounded negatives

Counts (live): 8 rows; by source class: procurement records 8
- MDS0341: procurement records | GET https://ted.europa.eu/en/notice/-/detail/864574-2025 => none found in https://ted.europa.eu/en/notice/-/detail/864574-2025 as of 2026-09-16T06:09:43Z | n=0 | role=context strength=supporting lane=MD14
- MDS0507: procurement records | GET https://ted.europa.eu/en/notice/-/detail/864574-2025 and /xml and udl DATA:EN:XML => none found in TED notice 864574-2025 as of 2026-09-16T07:21:41Z (HTTP 202 empty body) | n=0 | role=context strength=supporting lane=MD23
- MDS1179: procurement records | GET https://ted.europa.eu/en/notice/-/detail/864574-2025 => none found in https://ted.europa.eu/en/notice/-/detail/864574-2025 as of 2026-09-16T12:23:14Z | n=0 | role=context strength=supporting lane=MD46
- MDS0373: procurement records | GET 2025_FTS_dataset_en.csv; filters Name of beneficiary / any field regex Model Evaluation and Threat Research | \bMETR\b | Epoch Artificial Intelligence | Alignment Research Ce => none found in 2025_FTS_dataset_en.csv as of 2026-09-16T07:21:26Z for METR legal name, METR word, Epoch Artificial Intelligence, Alignment Research Center, or ARC Evals (0 rows); EquiStamp hits=2 recor
- MDS0834: procurement records | GET https://ted.europa.eu/en/notice/864574-2025/xml ; filters: attachment/binary contract text; fields share, percentage of ORG-0010, PayableAmount belonging to METR => none found in TED XML https://ted.europa.eu/en/notice/864574-2025/xml as of 2026-09-16T09:00:07Z for signed contract 4500137790 full text or a METR share/percentage (0). Award notice itself is present
- MDS0375: procurement records | POST https://api.ted.europa.eu/v3/notices/search winner-name="Alignment Research Center" ; winner-name="ARC Evals" ; FT~"Alignment Research Center" => none found in TED API winner-name/FT Alignment Research Center or ARC Evals as of 2026-09-16T07:20:11Z (totalNoticeCount=0) | n=0 | role=negative strength=supporting lane=MD20
- MDS0377: procurement records | GET https://ted.europa.eu/en/search/result?query=%22Model%20Evaluation%20and%20Threat%20Research%22 => none found in https://ted.europa.eu/en/search/result?query=%22Model%20Evaluation%20and%20Threat%20Research%22 as of 2026-09-16T07:18:32Z: HTTP 202 empty body (0 bytes) | n=0 | role=context strength=su
- MDS0378: procurement records | GET https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/tender-details/EC-CNECT/2025/OP/0032 ; GET https://etendering.ted.europa.eu/cft/cft-search => none found in Funding & Tenders tender-details EC-CNECT/2025/OP/0032 as of 2026-09-16T07:19:44Z (HTTP 404); eTendering cft-search HTTP 404 as of 2026-09-16T07:22:51Z | n=0 | role=context strength=supp

### Contradictions, duplicates and defects

- FIELD DEFECT: amount_usd=1167484 with currency=EUR on MDF0150, MDF0151, MDP0132, MDP0134 (and MD50/MD53 restatements); seed MDF0017 puts the text 'undisclosed share of EUR 1,167,484' in amount_usd. Read the currency column.
- from_entity naming varies: 'European AI Office' (seed/METR wording) vs 'European Commission, DG CNECT ... (CNECT.A Artificial Intelligence Office / CNECT.A.3)' (TED) vs 'CNECT - Directorate-General ...' (FTS). One contracting authority.
- Recipient differs by document: TED names three tenderers; FTS names EquiStamp Inc only; METR names itself. The 1,167,484 EUR is the lot total, not a METR receipt.

### Figure notes
Show one consortium contract of 1,167,484 EUR (lot total) with METR as a non-lead member and share undisclosed; consumed 0.00 as of FTS 2025. Keep EUR. Primary-strength negative: FTS 2025 has no beneficiary named METR (MDS0373). Anchors: MDF0150, MDF0151, MDP0132.


# Payers and aggregates METR does not name as supporters


## Alignment Research Center (EIN 86-3605182): program spin-off transfer to METR

**How METR names it:** Not named as a supporter. Appears as a related tax-exempt organization on METR's FY2024 Form 990 Schedule R (MDR0020) and as the payer of a PROGRAM SPIN-OFF grant on ARC's FY2024 Form 990 Schedule I / Schedule N.

**Status:** public amount identified: transfer (intra-group program spin-off), three filed figures that describe one event: 4,477,169 cash + 76,766 non-cash = 4,553,935 (ARC return) vs 4,501,424 (METR return); not attributable to any single ARC funder

### Facts (draw only from these)

- **MDF0064** [evidence/primary; lane MD12] transfer 4477169 USD | 2024-04-30 | Alignment Research Center -> Model Evaluation and Threat Research Inc | status: filed as cash grant on Schedule I | purpose: PROGRAM SPIN-OFF (no donor-restriction text on this line)
  - ANCHOR (primary): ARC FY2024 Schedule I CashGrantAmt 4,477,169 to MODEL EVALUATION AND THREAT RESEARCH INC, purpose PROGRAM SPIN-OFF; date 2024-04-30 taken from Schedule N DistributionDt. NOTE DEFECT: the row note says 'the $47,511 difference is not attributed'; 4,553,935 - 4,501,424 = 52,511 and 4,501,424 - 4,477,169 = 24,255; 47,511 matches neither.
  - url: https://apps.irs.gov/pub/epostcard/990/xml/2025/2025_TEOS_XML_11D.zip
- **MDF0065** [evidence/primary; lane MD12] in_kind_estimate 76766 USD | 2024-04-30 | Alignment Research Center -> Model Evaluation and Threat Research Inc | status: filed as non-cash assistance on Schedule I | purpose: PROGRAM SPIN-OFF (no donor-restriction text on this line)
  - ANCHOR (primary): ARC FY2024 Schedule I NonCashAssistanceAmt 76,766 (COMPUTERS, BOOK value), typed in_kind_estimate; do not add to cash.
  - url: https://apps.irs.gov/pub/epostcard/990/xml/2025/2025_TEOS_XML_11D.zip
- **MDT0030** [evidence/primary; lane MD12] untyped FairMarketValueOfAssetAmt=4553935 (Schedule N FMV; not an additional money flow)  | 2024-04-30 | Alignment Research Center -> Model Evaluation and Threat Research Inc | status: n/a | purpose: PROGRAM SPIN-OFF: EVALUATIONS PROGRAM SPUN-OFF AS A SEPARATE 501(C)(3) CALLED MODEL EVALUATION AND THREAT RESEARCH
  - ARC Schedule N: DistributionDt 2024-04-30; FairMarketValueOfAssetAmt 4,553,935 = cash + non-cash; Schedule R type B InvolvedAmt 4,553,935; not a third transfer.
  - url: https://apps.irs.gov/pub/epostcard/990/xml/2025/2025_TEOS_XML_11D.zip
- **MDT0229** [evidence/supporting; lane MD12] untyped (no amount)  | 2024-05 | Alignment Research Center -> Model Evaluation and Threat Research Inc | status: n/a | purpose: n/a
  - ARC Part III narrative says the spin-out completed 'in May'; ProgSrvcAccomActy2Grp GrantAmt 4,553,935 (same total).
  - url: https://apps.irs.gov/pub/epostcard/990/xml/2025/2025_TEOS_XML_11D.zip
- **MDF0034** [evidence/primary; lane MD01] transfer 4501424 USD | 2024-12-31 | Alignment Research Center -> Model Evaluation and Threat Research Inc | status: filed as contribution from related organizations | purpose: n/a
  - ANCHOR (primary, METR side): METR FY2024 Form 990 Part VIII RelatedOrganizationsAmt 4,501,424; Schedule R type C InvolvedAmt 4,501,424 (FAIR MARKET VALUE) for ALIGNMENT RESEARCH CENTER. Differs from both ARC-side figures.
  - url: https://apps.irs.gov/pub/epostcard/990/xml/2025/2025_TEOS_XML_11C.zip
- **MDP0587** [evidence/supporting; lane MD50] transfer 4501424 USD | undated | Alignment Research Center -> Model Evaluation and Threat Research Inc | status: n/a | purpose: n/a
  - MD50 double-count attack: 4,501,424 (METR) and 4,477,169 + 76,766 (ARC) describe the same program transfer; never add.
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202523209349300367_public.xml
- **MDP0015** [evidence/primary; lane MD12] untyped (no amount)  | 2024-04-30 | Alignment Research Center -> Model Evaluation and Threat Research Inc | status: n/a | purpose: n/a
  - Explicit non-attribution: the transfer cannot be attributed to any single ARC funder; ARC Schedule B RESTRICTED.
  - url: https://apps.irs.gov/pub/epostcard/990/xml/2025/2025_TEOS_XML_11D.zip
- **MDP0014** [evidence/primary; lane MD12] untyped (no amount)  | undated | Alignment Research Center -> Model Evaluation and Threat Research Inc | status: n/a | purpose: PROGRAM SPIN-OFF
  - Schedule I Part I line 2: grant agreement named but not attached (binaryAttachmentCnt=0).
  - url: https://apps.irs.gov/pub/epostcard/990/xml/2025/2025_TEOS_XML_11D.zip
- **MDP0016** [evidence/primary; lane MD12] untyped (no amount)  | 2024-04-30 | Alignment Research Center -> Model Evaluation and Threat Research Inc | status: n/a | purpose: no restriction stated in Schedule I PurposeOfGrantTxt (PROGRAM SPIN-OFF)
  - No donor restriction stated on the Schedule I line; agreement unattached.
  - url: https://apps.irs.gov/pub/epostcard/990/xml/2025/2025_TEOS_XML_11D.zip
- **MDP0032** [evidence/primary; lane MD14] transfer 4501424 USD | 2024-12-31 | Alignment Research Center -> Model Evaluation and Threat Research Inc | status: n/a | purpose: n/a
  - Commitment reconciliation: excluded (transfer; FY2024).
  - url: https://apps.irs.gov/pub/epostcard/990/xml/2025/2025_TEOS_XML_11C.zip
- **MDP0481** [evidence/supporting; lane MD14] transfer 4477169 USD | 2024-04-30 | Alignment Research Center -> Model Evaluation and Threat Research Inc | status: n/a | purpose: n/a
  - Commitment reconciliation: ARC-side cash and non-cash excluded; not summed.
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202513219349323246_public.xml
- **MDP0181** [evidence/primary; lane MD23] transfer 4477169 USD | undated | Alignment Research Center -> METR | status: n/a | purpose: programme-restricted
  - Purpose classification: programme-restricted (PROGRAM SPIN-OFF).
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202513219349323246_public.xml
- **MDR0020** [evidence/primary; lane MD01] untyped (no amount)  | undated | Alignment Research Center -> Model Evaluation and Threat Research Inc | status: n/a | purpose: n/a
  - METR Schedule R: ARC is a related tax-exempt organization, not a controlled organization; METR InitialReturnInd=X, FormationYr 2024.
  - url: https://apps.irs.gov/pub/epostcard/990/xml/2025/2025_TEOS_XML_11C.zip
- **MDT0029** [evidence/primary; lane MD12] untyped (no amount)  | 2023-12-04 | Alignment Research Center -> Model Evaluation and Threat Research Inc | status: n/a | purpose: n/a
  - METR announcement 2023-12-04: 'spinning off into our own standalone nonprofit' (organisational event, no amount).
  - url: https://metr.org/blog/2023-12-04-metr-announcement/
- **MDF0007** [context/supporting; lane S0; SEED] transfer 4553935  | 2024-04-30 | Alignment Research Center -> METR | status: filed as distributed | purpose: Program spin-off: assets and liabilities of the evaluations program
  - SEED BASELINE (context): transfer 4,553,935 dated 2024-04-30 from the ARC XML (Schedule I cash + non-cash and Schedule N).
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202513219349323246_public.xml
- **MDF0066** [context/supporting; lane MD12] recommendation 265000 USD | 2022-03 | Open Philanthropy -> Alignment Research Center | status: recommended; payment not stated on this page | purpose: general support
  - ARC's own funders (context, not METR payers): Open Philanthropy recommended $265,000 to ARC, March 2022.
  - url: https://web.archive.org/web/20240620191457id_/https://www.openphilanthropy.org/grants/alignment-research-center-general-support/
- **MDF0067** [context/supporting; lane MD12] recommendation 1250000 USD | 2022-11 | Open Philanthropy -> Alignment Research Center | status: recommended; payment not stated on this page | purpose: general support
  - ARC's own funders (context): Open Philanthropy recommended $1,250,000 over two years to ARC, November 2022.
  - url: https://web.archive.org/web/20240620191457id_/https://www.openphilanthropy.org/grants/alignment-research-center-general-support-november-2022/
- **MDF0069** [context/supporting; lane MD12] paid_grant 1250000 USD | 2022 | FTX Foundation -> Alignment Research Center | status: received (ARC issuer statement) | purpose: set aside and not spent (later returned; see Task D)
  - ARC's own funders (context): ARC states it received $1.25M from the FTX Foundation in 2022 (set aside, later returned).
  - url: https://www.alignment.org/funding-from-ftx/

### Restatement / locator rows (do not cite as new facts)

MDF0207, MDF0470, MDF0497, MDF0527, MDF0528, MDF0670, MDF0936, MDF0974, MDP0169, MDP0186, MDP0498, MDP0537, MDP0570, MDP0640, MDP0641, MDP0662, MDP0663, MDP0678, MDP0679, MDR0175, MDT0031, MDT0228, MDF0414

### ARC-side rows (not METR)

MDF0039, MDF0040, MDF0041, MDF0063, MDF0042, MDF0043, MDF0044, MDF0048, MDF0049, MDF0050, MDF0054, MDF0055, MDF0056, MDF0057, MDF0059, MDF0060, MDF0061

### Timeline rows

MDT0028, MDT0029, MDT0030, MDT0031, MDT0032, MDT0228, MDT0229

### Bounded negatives

Counts (live): 41 rows; by source class: DAF sponsor filings 28, IRS TEOS and e-file index 1, issuer statements 1, procurement records 2, public grant databases 4, recipient filings 4, self-statements 1
- MDS0030: public grant databases | GET https://www.packard.org/grantees/search-our-grants/?grant_keyword=Alignment%20Research%20Center filters: funding_area empty => none found in Packard search-our-grants grant_keyword=Alignment Research Center as of 2026-09-16T05:36:05Z | n=0 | role=negative strength=supporting lane=MD02
- MDS0127: public grant databases | GET https://www.pew.org/search?q=Alignment%20Research%20Center ; r.jina.ai proxy; filters: none => none found in pew.org/search?q=Alignment Research Center as of 2026-09-16T05:39:22Z | n=0 | role=context strength=supporting lane=MD03
- MDS0194: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202221339349302787_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Fidelity Investments Charitable Gift Fund Form 990 Schedule I object 202221339349302787 (FY2021) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0195: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202321309349304807_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Fidelity Investments Charitable Gift Fund Form 990 Schedule I object 202321309349304807 (FY2022) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0196: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202430459349302913_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Fidelity Investments Charitable Gift Fund Form 990 Schedule I object 202430459349302913 (FY2022 amended) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0197: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202441369349301334_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Fidelity Investments Charitable Gift Fund Form 990 Schedule I object 202441369349301334 (FY2023) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0198: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202601389349301700_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Fidelity Investments Charitable Gift Fund Form 990 Schedule I object 202601389349301700 (FY2025) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0199: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202230499349301028_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Schwab Charitable Fund Form 990 Schedule I object 202230499349301028 (FY2021) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0200: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202201119349300745_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Schwab Charitable Fund Form 990 Schedule I object 202201119349300745 (TY2021 two-day return) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0201: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202330939349300403_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Schwab Charitable Fund Form 990 Schedule I object 202330939349300403 (FY2022) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0202: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202411039349301716_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Schwab Charitable Fund Form 990 Schedule I object 202411039349301716 (FY2023) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0203: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202541069349300729_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Donor Advised Charitable Giving Inc Form 990 Schedule I object 202541069349300729 (FY2024) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0204: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202611199349300601_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Donor Advised Charitable Giving Inc Form 990 Schedule I object 202611199349300601 (FY2025) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0205: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202211339349310116_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Vanguard Charitable Endowment Program Form 990 Schedule I object 202211339349310116 (FY2021) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0206: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202331359349303108_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Vanguard Charitable Endowment Program Form 990 Schedule I object 202331359349303108 (FY2022) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0207: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202231339349309863_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in National Philanthropic Trust Form 990 Schedule I object 202231339349309863 (FY2021) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0208: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202311359349313966_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in National Philanthropic Trust Form 990 Schedule I object 202311359349313966 (FY2022) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0209: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202431429349301368_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in National Philanthropic Trust Form 990 Schedule I object 202431429349301368 (FY2023) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0210: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202511339349301311_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in National Philanthropic Trust Form 990 Schedule I object 202511339349301311 (FY2024) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0211: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202601289349302480_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in National Philanthropic Trust Form 990 Schedule I object 202601289349302480 (FY2025) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0212: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202223199349318287_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Silicon Valley Community Foundation Form 990 Schedule I object 202223199349318287 (TY2021) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0213: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202333189349318948_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Silicon Valley Community Foundation Form 990 Schedule I object 202333189349318948 (TY2022) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0256: public grant databases | GET https://coefficientgiving.org/grants/ ; GET /grants/?_search=Alignment+Research+Center ; GET wp-json/wp/v2/grant and /grants search; sitemap_index.xml => none found in Coefficient Giving /grants or wp/v2/grant as of 2026-09-16T06:10:58Z | n=0 | role=context strength=supporting lane=MD12
- MDS0324: public grant databases | GET https://aisecurityandsafety.org/grants/arc-evals-research-grants/ => Directory lists an active grant programme funded by Alignment Research Center / ARC Evals; it is not an award paying METR Inc | n=1 | role=context strength=supporting lane=MD13
- MDS0373: procurement records | GET 2025_FTS_dataset_en.csv; filters Name of beneficiary / any field regex Model Evaluation and Threat Research | \bMETR\b | Epoch Artificial Intelligence | Alignment Research Ce => none found in 2025_FTS_dataset_en.csv as of 2026-09-16T07:21:26Z for METR legal name, METR word, Epoch Artificial Intelligence, Alignment Research Center, or ARC Evals (0 rows); EquiStamp hits=2 recor
- MDS0375: procurement records | POST https://api.ted.europa.eu/v3/notices/search winner-name="Alignment Research Center" ; winner-name="ARC Evals" ; FT~"Alignment Research Center" => none found in TED API winner-name/FT Alignment Research Center or ARC Evals as of 2026-09-16T07:20:11Z (totalNoticeCount=0) | n=0 | role=negative strength=supporting lane=MD20
- MDS0587: recipient filings | IRS990 RelatedOrganizationsAmt; Schedule R IdRelatedTaxExemptOrgGrp => none found in RelatedOrganizationsAmt as a lab-sourced line as of 2026-09-16T09:20:12Z; the named related organization is Alignment Research Center, not Anthropic, OpenAI, Google DeepMind, Meta or Ama
- MDS1096: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202601389349301700_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Fidelity Investments Charitable Gift Fund Form 990 Schedule I object 202601389349301700 (FY2025) as of 2026-09-16T09:56:17Z | n=0 | role=negative strength=supporting lane=MD11
- MDS1097: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202140489349301804_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Schwab Charitable Fund Form 990 Schedule I object 202140489349301804 (FY2020) as of 2026-09-16T09:56:17Z | n=0 | role=negative strength=supporting lane=MD11
- MDS1098: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202330939349300403_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Schwab Charitable Fund Form 990 Schedule I object 202330939349300403 (FY2022) as of 2026-09-16T09:56:17Z | n=0 | role=negative strength=supporting lane=MD11
- MDS1099: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202121459349300307_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in National Philanthropic Trust Form 990 Schedule I object 202121459349300307 (FY2020) as of 2026-09-16T09:56:17Z | n=0 | role=negative strength=supporting lane=MD11
- MDS1100: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202431429349301368_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in National Philanthropic Trust Form 990 Schedule I object 202431429349301368 (FY2023) as of 2026-09-16T09:56:17Z | n=0 | role=negative strength=supporting lane=MD11
- MDS1101: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202511339349301311_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in National Philanthropic Trust Form 990 Schedule I object 202511339349301311 (FY2024) as of 2026-09-16T09:56:17Z | n=0 | role=negative strength=supporting lane=MD11
- MDS1102: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202601289349302480_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in National Philanthropic Trust Form 990 Schedule I object 202601289349302480 (FY2025) as of 2026-09-16T09:56:17Z | n=0 | role=negative strength=supporting lane=MD11
- MDS1103: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202103199349327615_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Silicon Valley Community Foundation Form 990 Schedule I object 202103199349327615 (TY2020) as of 2026-09-16T09:56:17Z | n=0 | role=negative strength=supporting lane=MD11
- MDS1112: recipient filings | GET GT lake XML object 202523209349300367; grep IRS990ScheduleI / RecipientEIN 863605182 / ALIGNMENT RESEARCH CENTER grant table => none found in METR FY2024 Form 990 Schedule I as of 2026-09-16T09:52:40Z | n=0 | role=negative strength=supporting lane=MD12
- MDS0252: IRS TEOS and e-file index | index_2026.csv filter EIN=863605182 OR name ALIGNMENT RESEARCH CENTER => none found in IRS e-file index_2026.csv as of 2026-09-16T06:05:03Z | n=0 | role=negative strength=supporting lane=MD12
- MDS0258: issuer statements | GET https://metr.org/about ; text search Schedule I, spin-off amount, restriction, Alignment Research Center transfer => none found in metr.org/about for the ARC Schedule I transfer amount or restriction as of 2026-09-16T06:05:56Z | n=0 | role=negative strength=supporting lane=MD12
- MDS0260: self-statements | GET https://www.alignment.org/blog/rss/ ; filter item title/description for METR spin-off amount, Schedule I, restriction, transfer => none found in alignment.org/blog/rss/ for a dated asset-distribution amount or transfer restriction as of 2026-09-16T06:13:45Z | n=0 | role=negative strength=supporting lane=MD12
- MDS1112: recipient filings | GET GT lake XML object 202523209349300367; grep IRS990ScheduleI / RecipientEIN 863605182 / ALIGNMENT RESEARCH CENTER grant table => none found in METR FY2024 Form 990 Schedule I as of 2026-09-16T09:52:40Z | n=0 | role=negative strength=supporting lane=MD12
- MDS0587: recipient filings | IRS990 RelatedOrganizationsAmt; Schedule R IdRelatedTaxExemptOrgGrp => none found in RelatedOrganizationsAmt as a lab-sourced line as of 2026-09-16T09:20:12Z; the named related organization is Alignment Research Center, not Anthropic, OpenAI, Google DeepMind, Meta or Ama

### Contradictions, duplicates and defects

- THREE FIGURES, ONE EVENT: (a) 4,553,935 = ARC FY2024 Schedule N FairMarketValueOfAssetAmt, Schedule R type B InvolvedAmt and Part III GrantAmt (MDT0030, MDT0228, MDT0229; seed MDF0007); (b) 4,477,169 cash (ARC Schedule I CashGrantAmt, MDF0064) + 76,766 non-cash computers at book (ARC Schedule I NonCashAssistanceAmt, MDF0065), which sum exactly to 4,553,935; (c) 4,501,424 = METR FY2024 Form 990 Part VIII line 1d RelatedOrganizationsAmt and Schedule R type C InvolvedAmt at fair market value (MDF0034). METR-side is 52,511 below the ARC total and 24,255 above ARC cash. No filing reconciles the gap; the pack does not attribute it.
- NOTE ARITHMETIC DEFECT: MDF0064's note cites a '$47,511 difference'; no pair of the filed figures differs by 47,511.
- DATE: ARC Schedule N says 2024-04-30 (MDT0030/MDT0228); ARC Part III narrative says May (MDT0229); METR-side row MDF0034 is dated 2024-12-31 (fiscal year end, precision 'day' though it is a period end). Use 2024-04-30 as the distribution date and label the METR figure as the FY2024 return total.
- money_type: ARC cash = transfer; ARC non-cash = in_kind_estimate; METR-side = transfer. supporter_coverage lists 'in_kind_estimate; transfer'.

### Figure notes
Draw a two-sided reconciliation: ARC return (cash 4,477,169 + non-cash 76,766 = 4,553,935, distributed 2024-04-30, purpose PROGRAM SPIN-OFF) vs METR return (4,501,424 related-organization contribution, FY2024). Label as an intra-group program transfer, not new outside money and not attributable to any ARC funder; excluded from the ~$71M. ARC's own funders (Open Philanthropy recommendations, FTX Foundation, SFF/Tallinn/Founders Pledge/DAF lines to ARC) stay on an ARC node.


## Founders Pledge Inc (EIN 37-1795297; regrantor)

**How METR names it:** Not named by METR. Appears as a filed Schedule I payer on Founders Pledge Inc's TY2024 Form 990 and as 'FP-US' on Jaan Tallinn's public ledger; Founders Pledge's own grantee page lists METR (first funded April 2024) without an amount.

**Status:** public amount identified: filed_grant $184,000 TY2024 (calendar 2024) to METR EIN 99-1219864, purpose FUND CHARITABLE ACTIVITIES; equals the Tallinn ledger 2024-12-06 $184,000 via FP-US (same money, two documents)

### Facts (draw only from these)

- **MDF0058** [evidence/primary; lane MD09] filed_grant 184000 USD | 2024 | Founders Pledge Inc -> MODEL EVALUATION AND THREAT RESEARCH INC | status: filed as granted | purpose: FUND CHARITABLE ACTIVITIES
  - ANCHOR (primary): Founders Pledge Inc TY2024 Form 990 Schedule I CashGrantAmt 184,000 to MODEL EVALUATION AND THREAT RESEARCH INC EIN 99-1219864, FUND CHARITABLE ACTIVITIES.
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202523079349303352_public.xml
- **MDF0152** [context/supporting; lane MD22] filed_grant 184000 USD | 2024-12-31 | Founders Pledge Inc -> MODEL EVALUATION AND THREAT RESEARCH INC | status: filed as granted | purpose: FUND CHARITABLE ACTIVITIES
  - MD22 re-fetch of the same Schedule I line (context).
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202523079349303352_public.xml
- **MDP0177** [evidence/primary; lane MD23] filed_grant 184000 USD | undated | Founders Pledge Inc -> METR | status: n/a | purpose: unrestricted
  - Purpose classification from the 990: unrestricted (FUND CHARITABLE ACTIVITIES).
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202523079349303352_public.xml
- **MDF0086** [context/supporting; lane MD13] paid_grant (no amount)  | 2024-04 | Founders Pledge -> METR | status: n/a | purpose: Funding METR's development of autonomous capability evaluations and their research on AI task-completion time horizons
  - Founders Pledge grantee card: METR first funded April 2024; amount not on the page. Typed paid_grant on this row (inconsistent with filed_grant on MDF0058; it is a website listing, not a payment record).
  - url: https://www.founderspledge.com/grantees/metr
- **MDF0204** [evidence/supporting; lane MD23] filed_grant (no amount)  | undated | Founders Pledge -> METR | status: n/a | purpose: Funding METR's development of autonomous capability evaluations and their research on AI task-completion time horizons
  - Grantee-page purpose: 'Funding METR's development of autonomous capability evaluations and their research on AI task-completion time horizons' (programme-restricted per MDP0178); differs in specificity from the 990 text.
  - url: https://www.founderspledge.com/grantees/metr
- **MDP0041** [evidence/supporting; lane MD14] filed_grant 184000 USD | 2024 | Founders Pledge Inc -> METR | status: n/a | purpose: n/a
  - Commitment reconciliation: excluded (filed_grant; TY2024).
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202523079349303352_public.xml
- **MDP0588** [evidence/supporting; lane MD50] filed_grant 184000 USD | undated | Founders Pledge Inc -> Model Evaluation and Threat Research | status: n/a | purpose: n/a
  - MD50 double-count attack: 7 promoted rows carry 184000 across Founders Pledge filed_grant and Tallinn ledger paid_grant; same money, never add.
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202523079349303352_public.xml
- **MDF0053** [evidence/primary; lane MD09] paid_grant 184000 USD | 2024-12-06 | Jaan Tallinn -> Model Evaluation and Threat Research | status: disbursed as recorded on jaan.online ledger | purpose: General support
  - Same money, donor side: Jaan Tallinn ledger 2024-12-06 $184,000 via FP-US to METR (paid_grant).
  - url: https://jaan.online/philanthropy/donations.csv
- **MDE0027** [evidence/primary; lane MD09] untyped (no amount)  | undated | Founders Pledge Inc -> Model Evaluation and Threat Research, Inc. / Alignment Research Center | status: n/a | purpose: n/a
  - Founders Pledge Inc EIN 37-1795297 identified as the FP-US legal payer class (regrantor).
  - url: https://projects.propublica.org/nonprofits/api/v2/search.json?q=Founders%20Pledge
- **MDP0166** [evidence/supporting; lane MD23] untyped (no amount)  | undated | Founders Pledge Inc -> METR | status: n/a | purpose: funder website: autonomous capability evaluations / time horizons; 990: FUND CHARITABLE ACTIVITIES; recipient silent on FP
  - METR does not name Founders Pledge; recipient silent on purpose.
  - url: https://metr.org/about
- **MDF0010** [context/supporting; lane S0; SEED] filed_grant 184000  | 2024 | Founders Pledge Inc -> METR | status: filed as granted | purpose: FUND CHARITABLE ACTIVITIES
  - SEED BASELINE (context): $184,000 filed grant TY2024.
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202523079349303352_public.xml
- **MDF0177** [context/supporting; lane MD17] filed_grant 1000000 USD | 2024-12-31 | Founders Pledge Inc -> RAND Corporation | status: filed as granted | purpose: FUND CHARITABLE ACTIVITIES
  - NOT A METR PAYMENT: same FP TY2024 return: $1,000,000 to THE RAND CORPORATION, FUND CHARITABLE ACTIVITIES (does not name Canary).
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202523079349303352_public.xml
- **MDF0059** [context/supporting; lane MD09] filed_grant 147000 USD | 2024 | Founders Pledge Inc -> ALIGNMENT RESEARCH CENTER | status: filed as granted | purpose: FUND CHARITABLE ACTIVITIES
  - NOT A METR PAYMENT: same FP TY2024 return: $147,000 to ALIGNMENT RESEARCH CENTER.
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202523079349303352_public.xml

### Restatement / locator rows (do not cite as new facts)

MDF0203, MDF0219, MDF0413, MDF0473, MDF0521, MDF0549, MDF0615, MDF0666, MDF0667, MDF0682, MDF0934, MDF0987, MDP0178, MDP0494, MDP0507, MDP0613, MDP0645, MDP0664, MDP0680, MDE0046, MDE0067, MDT0053, MDT0059, MDT0164

### Payer-into-Founders-Pledge rows (not METR)

MDF0126, MDF0127, MDF0334, MDF0336, MDF0406, MDF0457, MDF0156, MDF0157, MDF0158, MDF0159, MDF0419, MDF0420, MDF0421, MDF0422, MDF0423, MDF0424, MDF0425, MDF0426, MDF0427, MDF0428, MDF0429, MDF0430, MDF0431, MDF0432, MDF0433, MDF0434, MDF0435, MDF0436, MDF0437, MDF0438, MDF0439, MDF0440, MDF0459, MDF0060, MDF0061, MDF0122

### Bounded negatives

Counts (live): 17 rows; by source class: IRS TEOS and e-file index 1, SEC 1, court dockets 1, funder filings 9, public grant databases 2, recipient filings 1, self-statements 1, statutory records requests 1
- MDS0015: public grant databases | GET https://www.founderspledge.com/grantees/metr ; HTML search for Jane Street => none found in Founders Pledge METR grantee page as of 2026-09-16T05:34:01Z for a named Jane Street individual donor | n=0 | role=negative strength=supporting lane=MD07
- MDS0109: self-statements | GET https://www.founderspledge.com/ exact-name strings => none found in Founders Pledge homepage HTML for David Farhi, Geoff Ralston, Dylan Field, or Steve Newman as of 2026-09-16T05:33:55Z | n=0 | role=context strength=supporting lane=MD08
- MDS0235: funder filings | IRS e-file index_2026.csv EIN 371795297 or 205205488 object later than TY2024; FP TY2024 XML has no 2025 METR amount other than $184,000 => none found in IRS e-file index_2026.csv for EIN 371795297 or 205205488 as of 2026-09-16T06:04:57Z | n=0 | role=negative strength=supporting lane=MD09
- MDS0246: statutory records requests | This lane sends nothing (embargo); no FOIA/CPRA/state charity request was filed => none found in this lane for a statutory records request (lane embargo: send nothing) as of 2026-09-16T06:04:57Z | n=0 | role=context strength=supporting lane=MD09
- MDS0300: public grant databases | GET https://www.founderspledge.com/sitemap.xml (444 loc) then GET /grantees/metr ; also GET /programs/global-catastrophic-risk-grantees => Founders Pledge grantee card: METR first funded April 2024; amount not published; sitemap (444 loc) omits /grantees/metr, so the canonical URL had to be fetched directly | n=444 | role=evidence streng
- MDS0390: funder filings | GET GT XML 202402359349100515; GrantOrContributionPdDurYrGrp filter METR|991219864|MODEL EVALUATION AND THREAT RESEARCH => none found in Founders Pledge Inc TY2023 990-PF XML object 202402359349100515 as of 2026-09-16T07:27:52Z for a METR grant line | n=0 | role=negative strength=supporting lane=MD22
- MDS0391: funder filings | GET GT XML 202301999349100115; GrantOrContributionPdDurYrGrp filter METR|991219864|MODEL EVALUATION AND THREAT RESEARCH => none found in Founders Pledge Inc TY2022 990-PF XML object 202301999349100115 as of 2026-09-16T07:27:52Z for a METR grant line | n=0 | role=negative strength=supporting lane=MD22
- MDS0392: funder filings | GET GT XML 202232349349100823; GrantOrContributionPdDurYrGrp filter METR|991219864|MODEL EVALUATION AND THREAT RESEARCH => none found in Founders Pledge Inc TY2021 990-PF XML object 202232349349100823 as of 2026-09-16T07:27:52Z for a METR grant line | n=0 | role=negative strength=supporting lane=MD22
- MDS0401: funder filings | GET GT XML 202523079349303352; IRS990ScheduleB ContributorInformationGrp ContributorNum => none found in Founders Pledge Inc TY2024 Form 990 Schedule B public copy object 202523079349303352 as of 2026-09-16T07:27:52Z for a named payer (ContributorNum=RESTRICTED) | n=0 | role=negative streng
- MDS0410: SEC | GET https://efts.sec.gov/LATEST/search-index?q=%22Founders%20Pledge%22%20METR => none found in SEC EFTS search-index q="Founders Pledge" METR as of 2026-09-16T07:27:52Z | n=0 | role=negative strength=supporting lane=MD22
- MDS0411: court dockets | GET https://www.courtlistener.com/?q=%22Founders%20Pledge%22%20METR&type=o => none found in CourtListener opinion search q="Founders Pledge" METR as of 2026-09-16T07:27:52Z (HTTP 403) | n=0 | role=context strength=supporting lane=MD22
- MDS0415: recipient filings | GET GT XML 202523209349300367; search LONGVIEW|FOUNDERS PLEDGE|EVERY ORG|EFFECTIVE VENTURES|ContributorNum => none found in METR FY2024 Form 990 XML object 202523209349300367 as of 2026-09-16T07:27:52Z for a named Longview, Founders Pledge, Every Org, or Effective Ventures contributor | n=0 | role=negative st
- MDS0417: IRS TEOS and e-file index | stream https://apps.irs.gov/pub/epostcard/990/xml/2026/index_2026.csv filter EIN in {371795297,932664730,611913297,333737390,205205488} => none found in IRS e-file index_2026.csv as of 2026-09-16T07:27:52Z for EIN 371795297, 932664730, 611913297, 333737390, or 205205488 | n=0 | role=negative strength=supporting lane=MD22
- MDS0439: funder filings | GET S3 EfileData/XmlFiles/202523079349303352_public.xml ; RecipientTable EIN 991219864; PurposeOfGrantTxt => none found in Founders Pledge Inc Form 990 Schedule I object 202523079349303352 (TY2024) as a Canary-attributed payment into METR as of 2026-09-16T07:22:52Z | n=0 | role=negative strength=primary lane
- MDS1143: funder filings | GET GT XML 202131059349101903; Schedule I RecipientTable / 990-PF GrantOrContributionPdDurYrGrp filter RecipientEIN 991219864 OR BusinessNameLine1Txt MODEL EVALUATION AND THREAT RESEA => none found in Founders Pledge Inc TY2020 (2020-01-01 to 2020-12-31) XML object 202131059349101903 as of 2026-09-16T10:04:42Z for a METR/EIN 99-1219864 grant line | n=0 | role=negative strength=support
- MDS1163: funder filings | GET https://find-and-update.company-information.service.gov.uk/company/08565148/filing-history/MzQ4MzQyNDk1N2FkaXF6a2N4/document?format=pdf&download=0 ; pdftotext/strings METR|Model E => none found in Founders Pledge Ltd group accounts made up to 31 December 2024 (Companies House PDF MzQ4MzQyNDk1N2FkaXF6a2N4) as of 2026-09-16T10:12:54Z for a METR grant line | n=0 | role=context streng
- MDS1164: funder filings | GET https://find-and-update.company-information.service.gov.uk/company/08565148/filing-history/MzQyNzgwOTcyOGFkaXF6a2N4/document?format=pdf&download=0 ; pdftotext/strings METR|Model E => none found in Founders Pledge Ltd group accounts made up to 31 December 2023 (Companies House PDF MzQyNzgwOTcyOGFkaXF6a2N4) as of 2026-09-16T10:12:54Z for a METR grant line | n=0 | role=context streng

### Contradictions, duplicates and defects

- money_type conflict for the same payer: MDF0058/MDF0152/MDF0203/MDF0219 filed_grant (990 line) vs MDF0086 paid_grant (grantee card with no amount). supporter_coverage lists filed_grant; paid_grant. Only the filed_grant carries an amount.
- Purpose conflict between two funder documents: 990 'FUND CHARITABLE ACTIVITIES' (unrestricted, MDP0177) vs website programme text (programme-restricted, MDP0178).
- Same-money: the $184,000 equals the Tallinn ledger FP-US line to the dollar (MDF0053); the pack notes the match but does not merge payer identity (Founders Pledge Inc is the legal payer; the ledger is the donor's self-statement).
- Lineage defect: MDF0413 (ARC $147,000) claims to be a candidate correction of MDF0058 (METR $184,000).
- Date fields: 2024 (year) on MDF0058/MDF0203/MDF0219; 2024-12-31 (interval) on MDF0152; the Schedule I line has no payment date. MDF0155 (FP total revenue) is DEAD, superseded by MDF0459.

### Figure notes
One filed grant $184,000, TY2024, unrestricted per 990; show side by side with the Tallinn ledger $184,000 (2024-12-06 via FP-US) as the same money. The dozens of payer-into-Founders-Pledge transfer rows (Fidelity, EveryOrg, EV, SVCF, Vanguard, Schwab, Good Ventures, Open Philanthropy Project, FP Ltd/gGmbH) are not METR facts and must not be chained to METR. Primary-strength negatives: FP TY2024 Schedule B restricted (MDS0401); METR FY2024 990 has no named Founders Pledge payer (MDS0415); FP TY2020-TY2023 no METR (MDS0390-MDS0392, MDS1143).


## Silicon Valley Community Foundation (DAF sponsor; EIN 20-5205488)

**How METR names it:** Not named by METR. Filed Schedule I payer on SVCF's TY2024 Form 990; the DAF account principal/adviser is not disclosed on any public schedule.

**Status:** public amount identified: filed_grant $20,000 TY2024 (calendar 2024) to Model Evaluation and Threat Research EIN 99-1219864, purpose Sciences; principal undisclosed

### Facts (draw only from these)

- **MDF0037** [evidence/primary; lane MD11] filed_grant 20000 USD | 2024-12-31 | Silicon Valley Community Foundation -> Model Evaluation and Threat Research | status: filed as granted | purpose: Sciences
  - ANCHOR (primary): SVCF TY2024 Form 990 Schedule I: RecipientEIN 991219864, CashGrantAmt 20000, PurposeOfGrantTxt 'Sciences'; 3,576 recipient rows scanned; no account-principal field exists on Schedule I.
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202543149349305759_public.xml
- **MDF0062** [evidence/primary; lane MD09] filed_grant 20000 USD | 2024 | Silicon Valley Community Foundation -> Model Evaluation and Threat Research | status: filed as granted | purpose: Sciences
  - MD09 independent recovery of the same $20,000 line; dollar match to the Tallinn ledger 2024-07-23 + 2024-07-24 SFF-spec $10,000 + $10,000 noted, adviser not identified.
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202543149349305759_public.xml
- **MDP0042** [evidence/primary; lane MD14] filed_grant 20000 USD | 2024 | Silicon Valley Community Foundation -> METR | status: n/a | purpose: n/a
  - Commitment reconciliation: excluded (filed_grant; TY2024; DAF sponsor is not the account principal).
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202543149349305759_public.xml
- **MDP0179** [evidence/primary; lane MD23] filed_grant 20000 USD | undated | Silicon Valley Community Foundation -> METR | status: n/a | purpose: programme-restricted
  - Purpose classification: programme-restricted ('Sciences' is a Schedule I category, not a project title).
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202543149349305759_public.xml
- **MDP0167** [evidence/supporting; lane MD23] untyped (no amount)  | undated | Silicon Valley Community Foundation -> METR | status: n/a | purpose: funder: Sciences; recipient silent on SVCF
  - METR does not name SVCF; recipient silent.
  - url: https://metr.org/about
- **MDF0011** [context/supporting; lane S0; SEED] filed_grant 20000  | 2024 | Silicon Valley Community Foundation -> METR | status: filed as granted | purpose: Sciences
  - SEED BASELINE (context): $20,000 TY2024.
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202543149349305759_public.xml
- **MDF0041** [context/supporting; lane MD11] filed_grant 50450 USD | 2024-12-31 | Silicon Valley Community Foundation -> Alignment Research Center | status: filed as granted | purpose: Sciences
  - NOT A METR PAYMENT: same SVCF TY2024 return: $50,450 to Alignment Research Center (MDF0063 duplicate recovery by MD09; $450 above the Tallinn $50,000 speculation line).
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202543149349305759_public.xml
- **MDF0040** [context/supporting; lane MD11] filed_grant 1401000 USD | 2023-12-31 | Silicon Valley Community Foundation -> Alignment Research Center | status: filed as granted | purpose: Sciences
  - NOT A METR PAYMENT: SVCF TY2023: $1,401,000 to Alignment Research Center.
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202413129349304911_public.xml

### Restatement / locator rows (do not cite as new facts)

MDF0153, MDF0205, MDF0212, MDF0220, MDF0418, MDF0474, MDF0500, MDF0525, MDF0616, MDF0668, MDF0675, MDF0683, MDF0881, MDP0508, MDF0063, MDF0421, MDF0435, MDF0455, MDT0027, MDT0231

### Bounded negatives

Counts (live): 17 rows; by source class: DAF sponsor filings 17; DEAD cited: MDS0214, MDS0217, MDS0218
- MDS0191: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202223199349318287_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Silicon Valley Community Foundation Form 990 Schedule I object 202223199349318287 (TY2021) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0192: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202333189349318948_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Silicon Valley Community Foundation Form 990 Schedule I object 202333189349318948 (TY2022) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0193: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202413129349304911_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Silicon Valley Community Foundation Form 990 Schedule I object 202413129349304911 (TY2023) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0212: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202223199349318287_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Silicon Valley Community Foundation Form 990 Schedule I object 202223199349318287 (TY2021) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0213: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202333189349318948_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Silicon Valley Community Foundation Form 990 Schedule I object 202333189349318948 (TY2022) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0214 (DEAD): DAF sponsor filings | Schedule I Part II columns; Schedule B ContributorNum on object 202543149349305759 => none found in Schedule I Part II or public Schedule B of object 202543149349305759 for a DAF account principal as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11 | DEAD (su
- MDS0217 (DEAD): DAF sponsor filings | Schedule I Part II columns; Schedule B ContributorNum on object 202413129349304911 => none found in Schedule I Part II or public Schedule B of object 202413129349304911 for a DAF account principal as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11 | DEAD (su
- MDS0218 (DEAD): DAF sponsor filings | Schedule I Part II columns; Schedule B ContributorNum on object 202543149349305759 => none found in Schedule I Part II or public Schedule B of object 202543149349305759 for a DAF account principal as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11 | DEAD (su
- MDS0398: DAF sponsor filings | GET GT XML 202413129349304911; Schedule I RecipientTable filter 991219864|MODEL EVALUATION AND THREAT RESEARCH => none found in Silicon Valley Community Foundation TY2023 990 XML object 202413129349304911 as of 2026-09-16T07:27:52Z for a METR grant line | n=0 | role=negative strength=supporting lane=MD22
- MDS0399: DAF sponsor filings | GET GT XML 202333189349318948; Schedule I RecipientTable filter 991219864|MODEL EVALUATION AND THREAT RESEARCH => none found in Silicon Valley Community Foundation TY2022 990 XML object 202333189349318948 as of 2026-09-16T07:27:52Z for a METR grant line | n=0 | role=negative strength=supporting lane=MD22
- MDS0400: DAF sponsor filings | GET GT XML 202223199349318287; Schedule I RecipientTable filter 991219864|MODEL EVALUATION AND THREAT RESEARCH => none found in Silicon Valley Community Foundation TY2021 990 XML object 202223199349318287 as of 2026-09-16T07:27:52Z for a METR grant line | n=0 | role=negative strength=supporting lane=MD22
- MDS0440: DAF sponsor filings | GET S3 EfileData/XmlFiles/202543149349305759_public.xml ; RecipientTable EIN 991219864; PurposeOfGrantTxt; Canary Fund and Canary Media Inc are unrelated names on the same schedu => none found in Silicon Valley Community Foundation Form 990 Schedule I object 202543149349305759 (TY2024) as a Canary-attributed payment into METR as of 2026-09-16T07:22:52Z | n=0 | role=negative stren
- MDS0886: DAF sponsor filings | Schedule I Part II columns a–h; Schedule B contributor name fields on object 202543149349305759 / public 990 => none found in Silicon Valley Community Foundation public Form 990 Schedule I or public Schedule B object 202543149349305759 (TY2024) for a DAF account principal as of 2026-09-16T10:21:56Z | n=0 | role
- MDS1095: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202103199349327615_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Silicon Valley Community Foundation Form 990 Schedule I object 202103199349327615 (TY2020) as of 2026-09-16T09:56:17Z | n=0 | role=negative strength=supporting lane=MD11
- MDS1103: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202103199349327615_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Silicon Valley Community Foundation Form 990 Schedule I object 202103199349327615 (TY2020) as of 2026-09-16T09:56:17Z | n=0 | role=negative strength=supporting lane=MD11
- MDS1105: DAF sponsor filings | Schedule I Part II columns; Schedule B ContributorNum on object 202543149349305759 => none found in Schedule I Part II or public Schedule B of object 202543149349305759 for a DAF account principal as of 2026-09-16T09:56:17Z | n=0 | role=negative strength=supporting lane=MD11
- MDS1110: DAF sponsor filings | Schedule I Part II columns; Schedule B ContributorNum on object 202413129349304911 => none found in Schedule I Part II or public Schedule B of object 202413129349304911 for a DAF account principal as of 2026-09-16T09:56:17Z | n=0 | role=negative strength=supporting lane=MD11
- MDS1111: DAF sponsor filings | Schedule I Part II columns; Schedule B ContributorNum on object 202543149349305759 => none found in Schedule I Part II or public Schedule B of object 202543149349305759 for a DAF account principal as of 2026-09-16T09:56:17Z | n=0 | role=negative strength=supporting lane=MD11
- MDS1146: DAF sponsor filings | GET GT XML 202103199349327615; Schedule I RecipientTable / 990-PF GrantOrContributionPdDurYrGrp filter RecipientEIN 991219864 OR BusinessNameLine1Txt MODEL EVALUATION AND THREAT  => none found in Silicon Valley Community Foundation TY2020 (2020-01-01 to 2020-12-31) XML object 202103199349327615 as of 2026-09-16T10:04:32Z for a METR/EIN 99-1219864 grant line | n=0 | role=negative 
- MDS1150: DAF sponsor filings | GET GT XML 202543149349305759; IRS990ScheduleB ContributorInformationGrp ContributorNum => none found in Silicon Valley Community Foundation TY2024 (2024-01-01 to 2024-12-31) Form 990 Schedule B public copy object 202543149349305759 as of 2026-09-16T10:07:40Z for a named payer (ContributorN

### Contradictions, duplicates and defects

- DEFECT: supporter_coverage.csv (svcf negative_rows) cites MDS0214, MDS0217 and MDS0218, all DEAD (superseded by MDS1105, MDS1110, MDS1111).
- Date fields: 2024 (year) on MDF0062/MDF0205/MDF0220; 2024-12-31 with precision 'day' on MDF0037 (audit note: lane said interval) and 'interval' on MDF0153/MDF0418. The Schedule I line has no payment date.
- Dollar match to the Tallinn ledger 2 x $10,000 SFF-spec lines (MDF0051/MDF0052) is recorded as a match only; the pack does not identify the DAF adviser and neither should a figure.

### Figure notes
One filed grant $20,000, TY2024, purpose Sciences, principal undisclosed. Show the 2 x $10,000 ledger lines as a dollar match, not as an identification. Primary-strength negatives: SVCF TY2020-TY2023 Schedule I no METR (MDS0191-MDS0193, MDS1095, MDS1146); Schedule B restricted (MDS1150); not Canary-attributed (MDS0440).


## Vanguard Charitable Endowment Program (DAF sponsor; EIN 23-2888152)

**How METR names it:** Not named by METR. Filed Schedule I payer on Vanguard Charitable's FY2025 (2024-07-01 to 2025-06-30) Form 990; account principal undisclosed.

**Status:** public amount identified: filed_grant $4,000,000 FY2025 to MODEL EVALUATION AND THREAT RESEARCH EIN 99-1219864, purpose FOR RECIPIENT'S EXEMPT PURPOSE; the largest single filed grant to METR in the pack; provenance rests on rendered ProPublica Schedule I captures because the XML is not yet on GivingTuesday/IRS bulk and the live page later became a JS shell

### Facts (draw only from these)

- **MDF0038** [evidence/primary; lane MD11] filed_grant 4000000 USD | 2025-06-30 | Vanguard Charitable Endowment Program -> Model Evaluation and Threat Research | status: filed as granted | purpose: FOR RECIPIENT'S EXEMPT PURPOSE
  - ANCHOR (primary): ProPublica rendered Schedule I (object 202621329349306657) RecipientTable[15424]: MODEL EVALUATION AND THREAT RESEARCH, EIN 99-1219864, CashGrantAmt 4,000,000, FOR RECIPIENT'S EXEMPT PURPOSE. Saved capture 2026-09-16T06:09Z. XML not on GivingTuesday; not in 2026_TEOS_XML_05A.zip; download-xml HTTP 403.
  - url: https://projects.propublica.org/nonprofits/full_text/202621329349306657/IRS990ScheduleI
- **MDF0154** [context/supporting; lane MD22] filed_grant 4000000 USD | 2025-06-30 | Vanguard Charitable Endowment Program -> MODEL EVALUATION AND THREAT RESEARCH | status: filed as granted | purpose: FOR RECIPIENT'S EXEMPT PURPOSE
  - MD22 re-fetch: same row 15424 recovered (excerpt saved 2026-09-16T07:19Z).
  - url: https://projects.propublica.org/nonprofits/full_text/202621329349306657/IRS990ScheduleI
- **MDF0206** [context/supporting; lane MD23] filed_grant 4000000 USD | 2025-06-30 | Vanguard Charitable Endowment Program -> MODEL EVALUATION AND THREAT RESEARCH | status: filed as granted | purpose: FOR RECIPIENT'S EXEMPT PURPOSE
  - MD23 re-fetch: same row and purpose recovered.
  - url: https://projects.propublica.org/nonprofits/full_text/202621329349306657/IRS990ScheduleI
- **MDF0211** [context/supporting; lane MD32] filed_grant 4000000 USD | 2025-06-30 | Vanguard Charitable Endowment Program -> Model Evaluation and Threat Research | status: filed as granted | purpose: FOR RECIPIENT'S EXEMPT PURPOSE
  - MD32 re-fetch: same row recovered; no donor/adviser/principal column.
  - url: https://projects.propublica.org/nonprofits/full_text/202621329349306657/IRS990ScheduleI
- **MDP0180** [evidence/primary; lane MD23] filed_grant 4000000 USD | undated | Vanguard Charitable Endowment Program -> METR | status: n/a | purpose: unrestricted
  - Purpose classification: unrestricted (FOR RECIPIENT'S EXEMPT PURPOSE).
  - url: https://projects.propublica.org/nonprofits/full_text/202621329349306657/IRS990ScheduleI
- **MDP0043** [evidence/primary; lane S0] filed_grant 4000000 USD | FY2025 (2024-07-01 to 2025-06-30) | Vanguard Charitable Endowment Program -> METR | status: n/a | purpose: n/a
  - Commitment reconciliation: excluded (filed_grant; FY2025). PROVENANCE GAP: this MD14 row could not re-fetch the grant line (JS shell / XML 404) and quotes the seed CSV cell; MDP0593 (MD50) records the gap.
  - url: https://projects.propublica.org/nonprofits/full_text/202621329349306657/IRS990ScheduleI
- **MDP0593** [evidence/supporting; lane MD50] filed_grant 4000000 USD | undated | Vanguard Charitable Endowment Program -> Model Evaluation and Threat Research | status: n/a | purpose: n/a
  - MD50 provenance attack: the recon line relies on a seed-held amount; live ProPublica HTML is a JS shell; GT XML 404. The MD11/MD18/MD22/MD23/MD32 captures are the working primaries.
  - url: https://projects.propublica.org/nonprofits/full_text/202621329349306657/IRS990ScheduleI
- **MDP0168** [evidence/supporting; lane MD23] untyped (no amount)  | undated | Vanguard Charitable Endowment Program -> METR | status: n/a | purpose: funder: FOR RECIPIENT'S EXEMPT PURPOSE; recipient donate page: every.org re-grants as unrestricted donations (channel, not this DAF)
  - METR does not name Vanguard Charitable; the every.org unrestricted sentence on metr.org/donate is a different channel.
  - url: https://metr.org/donate
- **MDF0012** [context/supporting; lane S0; SEED] filed_grant 4000000  | FY2025 (2024-07-01 to 2025-06-30) | Vanguard Charitable Endowment Program -> METR | status: filed as granted | purpose: FOR RECIPIENT'S EXEMPT PURPOSE
  - SEED BASELINE (context): $4,000,000 FY2025, Schedule I row 15424.
  - url: https://projects.propublica.org/nonprofits/organizations/232888152/202621329349306657/IRS990ScheduleI
- **MDF0044** [context/supporting; lane MD11] filed_grant 1500000 USD | 2025-06-30 | Vanguard Charitable Endowment Program -> Alignment Research Center | status: filed as granted | purpose: FOR RECIPIENT'S EXEMPT PURPOSE
  - NOT A METR PAYMENT: same Vanguard FY2025 return: $1,500,000 to Alignment Research Center (row 547).
  - url: https://projects.propublica.org/nonprofits/full_text/202621329349306657/IRS990ScheduleI
- **MDF0043** [context/supporting; lane MD11] filed_grant 1000000 USD | 2024-06-30 | Vanguard Charitable Endowment Program -> Alignment Research Center | status: filed as granted | purpose: FOR RECIPIENT'S EXEMPT PURPOSE
  - NOT A METR PAYMENT: Vanguard FY2024: $1,000,000 to Alignment Research Center.
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202511349349313096_public.xml
- **MDF0042** [context/supporting; lane MD11] filed_grant 201000 USD | 2023-06-30 | Vanguard Charitable Endowment Program -> Alignment Research Center | status: filed as granted | purpose: FOR RECIPIENT'S EXEMPT PURPOSE
  - NOT A METR PAYMENT: Vanguard FY2023: $201,000 to Alignment Research Center.
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202441359349309439_public.xml

### Restatement / locator rows (do not cite as new facts)

MDF0475, MDF0501, MDF0617, MDF0669, MDF0674, MDF1013, MDP0482, MDP0509, MDP0600, MDP0644, MDF0419, MDF0426, MDF0430, MDF0444, MDF0450, MDF0453, MDF0456, MDT0025, MDT0057, MDT0230

### Bounded negatives

Counts (live): 26 rows; by source class: DAF sponsor filings 26; DEAD cited: MDS0215, MDS0219, MDS0220, MDS0221
- MDS0182: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202211339349310116_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Vanguard Charitable Endowment Program Form 990 Schedule I object 202211339349310116 (FY2021) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0183: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202331359349303108_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Vanguard Charitable Endowment Program Form 990 Schedule I object 202331359349303108 (FY2022) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0184: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202441359349309439_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Vanguard Charitable Endowment Program Form 990 Schedule I object 202441359349309439 (FY2023) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0185: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202511349349313096_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Vanguard Charitable Endowment Program Form 990 Schedule I object 202511349349313096 (FY2024) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0205: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202211339349310116_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Vanguard Charitable Endowment Program Form 990 Schedule I object 202211339349310116 (FY2021) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0206: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202331359349303108_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Vanguard Charitable Endowment Program Form 990 Schedule I object 202331359349303108 (FY2022) as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11
- MDS0215 (DEAD): DAF sponsor filings | Schedule I Part II columns; Schedule B ContributorNum on object 202621329349306657 => none found in Schedule I Part II or public Schedule B of object 202621329349306657 for a DAF account principal as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11 | DEAD (su
- MDS0219 (DEAD): DAF sponsor filings | Schedule I Part II columns; Schedule B ContributorNum on object 202441359349309439 => none found in Schedule I Part II or public Schedule B of object 202441359349309439 for a DAF account principal as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11 | DEAD (su
- MDS0220 (DEAD): DAF sponsor filings | Schedule I Part II columns; Schedule B ContributorNum on object 202511349349313096 => none found in Schedule I Part II or public Schedule B of object 202511349349313096 for a DAF account principal as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11 | DEAD (su
- MDS0221 (DEAD): DAF sponsor filings | Schedule I Part II columns; Schedule B ContributorNum on object 202621329349306657 => none found in Schedule I Part II or public Schedule B of object 202621329349306657 for a DAF account principal as of 2026-09-16T06:16:31Z | n=0 | role=negative strength=supporting lane=MD11 | DEAD (su
- MDS0223: DAF sponsor filings | GET GT .../202621329349306657_public.xml; GET s3.amazonaws.com/irs-form-990/202621329349306657_public.xml; unzip -l 2026_TEOS_XML_05A.zip member 202621329349306657_public.xml => none found in GivingTuesday XML and IRS 2026_TEOS_XML_05A.zip for object 202621329349306657 as of 2026-09-16T06:08:26Z | n=0 | role=context strength=supporting lane=MD11
- MDS0394: DAF sponsor filings | GET GT XML 202511349349313096; Schedule I RecipientTable filter 991219864|MODEL EVALUATION AND THREAT RESEARCH => none found in Vanguard Charitable Endowment Program FY2024 990 XML object 202511349349313096 as of 2026-09-16T07:27:52Z for a METR grant line | n=0 | role=negative strength=supporting lane=MD22
- MDS0395: DAF sponsor filings | GET GT XML 202441359349309439; Schedule I RecipientTable filter 991219864|MODEL EVALUATION AND THREAT RESEARCH => none found in Vanguard Charitable Endowment Program FY2023 990 XML object 202441359349309439 as of 2026-09-16T07:27:52Z for a METR grant line | n=0 | role=negative strength=supporting lane=MD22
- MDS0396: DAF sponsor filings | GET GT XML 202331359349303108; Schedule I RecipientTable filter 991219864|MODEL EVALUATION AND THREAT RESEARCH => none found in Vanguard Charitable Endowment Program FY2022 990 XML object 202331359349303108 as of 2026-09-16T07:27:52Z for a METR grant line | n=0 | role=negative strength=supporting lane=MD22
- MDS0397: DAF sponsor filings | GET GT XML 202211339349310116; Schedule I RecipientTable filter 991219864|MODEL EVALUATION AND THREAT RESEARCH => none found in Vanguard Charitable Endowment Program FY2021 990 XML object 202211339349310116 as of 2026-09-16T07:27:52Z for a METR grant line | n=0 | role=negative strength=supporting lane=MD22
- MDS0441: DAF sponsor filings | GET https://projects.propublica.org/nonprofits/full_text/202621329349306657/IRS990ScheduleI ; RecipientTable[15424] EIN 99-1219864; PurposeOfGrantTxt; S3 XML 404 => none found in Vanguard Charitable Endowment Program Form 990 Schedule I object 202621329349306657 (FY2025) as a Canary-attributed payment into METR as of 2026-09-16T07:25:19Z | n=0 | role=negative str
- MDS0514: DAF sponsor filings | ProPublica Schedule I RecipientTable[15424] => none found in the Vanguard Schedule I purpose line as of 2026-09-16T07:25:41Z of a project restriction; the amount remains a FY2025 filed_grant, which is a different money_type from the $71 million co
- MDS0593: DAF sponsor filings | GET ProPublica full_text/202621329349306657/IRS990ScheduleB => none found in public Schedule B of Vanguard object 202621329349306657 as of 2026-09-16T09:20:14Z for a DAF account principal on the METR grant | n=0 | role=negative strength=supporting lane=MD32
- MDS0887: DAF sponsor filings | Schedule I Part II columns a–h; Schedule B contributor name fields on object 202621329349306657 / public 990 => none found in Vanguard Charitable Endowment Program public Form 990 Schedule I or public Schedule B object 202621329349306657 (FY2025) for a DAF account principal as of 2026-09-16T10:21:56Z | n=0 | ro
- MDS1093: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202441359349309439_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Vanguard Charitable Endowment Program Form 990 Schedule I object 202441359349309439 (FY2023) as of 2026-09-16T09:56:17Z | n=0 | role=negative strength=supporting lane=MD11
- MDS1094: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202511349349313096_public.xml; Schedule I <RecipientTable>; filters RecipientEIN in {991219864,863605182} OR => none found in Vanguard Charitable Endowment Program Form 990 Schedule I object 202511349349313096 (FY2024) as of 2026-09-16T09:56:17Z | n=0 | role=negative strength=supporting lane=MD11
- MDS1104: DAF sponsor filings | Schedule I Part II columns; Schedule B ContributorNum on object 202621329349306657 => none found in Schedule I Part II or public Schedule B of object 202621329349306657 for a DAF account principal as of 2026-09-16T09:56:17Z | n=0 | role=negative strength=supporting lane=MD11
- MDS1107: DAF sponsor filings | Schedule I Part II columns; Schedule B ContributorNum on object 202441359349309439 => none found in Schedule I Part II or public Schedule B of object 202441359349309439 for a DAF account principal as of 2026-09-16T09:56:17Z | n=0 | role=negative strength=supporting lane=MD11
- MDS1108: DAF sponsor filings | Schedule I Part II columns; Schedule B ContributorNum on object 202511349349313096 => none found in Schedule I Part II or public Schedule B of object 202511349349313096 for a DAF account principal as of 2026-09-16T09:56:17Z | n=0 | role=negative strength=supporting lane=MD11
- MDS1109: DAF sponsor filings | Schedule I Part II columns; Schedule B ContributorNum on object 202621329349306657 => none found in Schedule I Part II or public Schedule B of object 202621329349306657 for a DAF account principal as of 2026-09-16T09:56:17Z | n=0 | role=negative strength=supporting lane=MD11
- MDS1118: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202621329349306657_public.xml => none found in gt990datalake S3 object 202621329349306657_public.xml as of 2026-09-16T09:43:37Z | n=0 | role=context strength=supporting lane=MD14
- MDS1119: DAF sponsor filings | GET https://projects.propublica.org/nonprofits/download-xml?object_id=202621329349306657 => none found in ProPublica download-xml?object_id=202621329349306657 as of 2026-09-16T09:47:03Z | n=0 | role=context strength=supporting lane=MD14
- MDS1151: DAF sponsor filings | GET GT XML 202511349349313096; IRS990ScheduleB ContributorInformationGrp ContributorNum => none found in Vanguard Charitable Endowment Program FY2024 (2023-07-01 to 2024-06-30) Form 990 Schedule B public copy object 202511349349313096 as of 2026-09-16T10:07:54Z for a named payer (Contributo
- MDS1183: DAF sponsor filings | GET https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202621329349306657_public.xml => none found in gt990datalake S3 XML 202621329349306657_public.xml as of 2026-09-16T12:22:53Z | n=0 | role=context strength=supporting lane=MD46
- MDS1583: DAF sponsor filings | when posted; next check 2026-11-16 with June-year sponsors => future document CAL09 is N/A-with-reason until availability; not searched-and-absent | n=0 | role=evidence strength=supporting lane=MD52

### Contradictions, duplicates and defects

- PROVENANCE: MD50 re-verification rows MDF0475, MDF0501, MDF0617, MDF0669, MDF0674 report 'mismatch: amount 4000000 not found in primary' because the live ProPublica Schedule I page returned a JS shell at 12:33Z; the amount was recovered from the rendered page by MD11 (06:09Z), MD18 (MDS0441, 07:25Z), MD22, MD23 and MD32. The figure rests on those saved captures until the FY2025 XML is published (calendar closer MDS1583).
- DEFECT: supporter_coverage.csv (vanguard negative_rows) cites MDS0215, MDS0219, MDS0220, MDS0221, all DEAD (superseded by MDS1104, MDS1107, MDS1108, MDS1109).
- Date field on seed MDF0012 is the text 'FY2025 (2024-07-01 to 2025-06-30)'; MDF0038 uses 2025-06-30 (fiscal year end) with precision 'day' (audit note: lane said interval). No payment date is filed.

### Figure notes
One filed grant $4,000,000, FY2025 (Jul 2024-Jun 2025), unrestricted, principal undisclosed; mark provenance as 'rendered ProPublica Schedule I row 15424 (saved captures); XML not yet public'. Do not deanonymize the DAF adviser. Primary-strength negatives: Vanguard FY2021-FY2024 Schedule I no METR (MDS0182-MDS0185, MDS0394-MDS0397); not Canary-attributed (MDS0441); Schedule B/Schedule I disclose no principal (MDS0593, MDS0887, MDS1104, MDS1109).


## METR's own filed aggregates and statements (denominators, not payers)

**How METR names it:** METR's FY2024 Form 990 (initial short year 2024-05-01 to 2024-12-31) and the 2026-08-14 funding update ('In the last 6 months, METR raised commitments of around $71 million.')

**Status:** recipient-side totals and an organisation-wide commitment statement; never a supporter amount and never summed with supporter rows

### Facts (draw only from these)

- **MDF0089** [evidence/primary; lane MD14] commitment 71000000 USD | 2026-08-14 | not stated in this source -> METR | status: committed; payment not stated | purpose: n/a
  - ANCHOR (primary): 2026-08-14: 'In the last 6 months, METR raised commitments of around $71 million.' money_type commitment; composition and payment not stated; working integer 71,000,000.
  - url: https://metr.org/blog/2026-08-14-funding-update/
- **MDF0410** [evidence/primary; lane MD01] untyped 13639155 USD | 2024-12-31 | ? -> Model Evaluation and Threat Research Inc | status: filed on the recipient's own Form 990 | purpose: n/a
  - ANCHOR (primary): METR FY2024 Form 990 CYTotalRevenueAmt 13,639,155; CYContributionsGrantsAmt 13,603,035 (8-month initial year). money_type blank by design.
  - url: https://apps.irs.gov/pub/epostcard/990/xml/2025/2025_TEOS_XML_11C.zip
- **MDF0411** [evidence/primary; lane MD01] untyped 9101611 USD | 2024-12-31 | ? -> Model Evaluation and Threat Research Inc | status: filed as AllOtherContributionsAmt on the recipient's Form 990; payers not named | purpose: n/a
  - METR FY2024 AllOtherContributionsAmt 9,101,611: unnamed payers (Schedule B RESTRICTED). Supersedes MDF0035.
  - url: https://apps.irs.gov/pub/epostcard/990/xml/2025/2025_TEOS_XML_11C.zip
- **MDF0034** [evidence/primary; lane MD01] transfer 4501424 USD | 2024-12-31 | Alignment Research Center -> Model Evaluation and Threat Research Inc | status: filed as contribution from related organizations | purpose: n/a
  - METR FY2024 RelatedOrganizationsAmt 4,501,424 (ARC; see ARC entry).
  - url: https://apps.irs.gov/pub/epostcard/990/xml/2025/2025_TEOS_XML_11C.zip
- **MDF0147** [evidence/primary; lane MD25] untyped 8234524 USD | 2024-12-31 | ? -> Model Evaluation and Threat Research Inc | status: filed on the recipient's own Form 990 (CYTotalExpensesAmt); recipient-side aggregate, not a funding event | purpose: n/a
  - METR FY2024 CYTotalExpensesAmt 8,234,524.
  - url: https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202523209349300367_public.xml
- **MDF0032** [evidence/primary; lane MD01] untyped 5404631 USD | 2024-12-31 | ? -> Model Evaluation and Threat Research Inc | status: n/a | purpose: n/a
  - METR FY2024 NetAssetsOrFundBalancesEOYAmt 5,404,631; no donor-restricted net-asset tags.
  - url: https://apps.irs.gov/pub/epostcard/990/xml/2025/2025_TEOS_XML_11C.zip
- **MDF0033** [evidence/primary; lane MD01] untyped 0 USD | 2024-12-31 | ? -> Model Evaluation and Threat Research Inc | status: n/a | purpose: n/a
  - METR FY2024 program service revenue 0; government grants element absent.
  - url: https://apps.irs.gov/pub/epostcard/990/xml/2025/2025_TEOS_XML_11C.zip
- **MDP0055** [evidence/primary; lane MD14] commitment 350000 USD | 2026-08-14 | ? -> METR | status: n/a | purpose: n/a
  - Reconciliation remainder statement: identified compatible total $350,000 (Packard).
  - url: https://metr.org/blog/2026-08-14-funding-update/
- **MDP0056** [evidence/supporting; lane MD14] commitment 70650000 USD | the last 6 months as of 2026-08-14 | ? -> METR | status: n/a | purpose: n/a
  - Reconciliation remainder: ~$70,650,000 unresolved (arithmetic; composition unknown from public sources).
  - url: https://metr.org/blog/2026-08-14-funding-update/
- **MDP0062** [evidence/primary; lane MD25] untyped (no amount)  | 2026-08-14 | ? -> Model Evaluation and Threat Research Inc | status: n/a | purpose: n/a
  - Do not add ~$71M commitments to FY2024 filed revenue 13,639,155 or to the 2024 annual-report budget.
  - url: https://metr.org/blog/2026-08-14-funding-update/
- **MDP0053** [evidence/supporting; lane MD14] paid_grant (no amount)  | 2025-12 | Coefficient Giving -> METR | status: n/a | purpose: n/a
  - Coefficient Giving staff note (2025-12): 'This organization is not a Coefficient Giving grantee.' No Coefficient amount exists.
  - url: https://www.coefficientgiving.org/research/suggestions-for-individual-donors-from-coefficient-giving-staff-2025/
- **MDP0052** [evidence/supporting; lane MD14] in_kind_estimate 400000 USD | 2026-08-26 | ? -> ? | status: n/a | purpose: n/a
  - Lab in-kind (out of scope for this audit): METR estimated ~$400K of API credits spent over six days of the 2026-08-26 investigation (in_kind_estimate; not a cash supporter).
  - url: https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/
- **MDF0001** [context/supporting; lane S0; SEED] commitment 71000000  | 2026-08-14 | not stated in this source -> METR | status: committed; payment not stated | purpose: not stated in this source
  - SEED BASELINE (context): the ~$71M sentence.
  - url: https://metr.org/blog/2026-08-14-funding-update/

### Restatement / locator rows (do not cite as new facts)

MDF0031 (DEAD), MDF0035 (DEAD), MDF0145, MDF0146, MDF0463, MDF0464, MDF0494, MDF0495, MDF0496, MDF0498, MDF0552, MDF0608, MDF0609, MDF0610, MDF0873, MDF0874, MDF0926, MDF1032, MDP0031, MDP0590, MDP0592, MDP0741, MDF0002 (DEAD), MDF0003 (DEAD), MDF0465, MDF0466

### Bounded negatives

Counts (live): 6 rows; by source class: recipient filings 6
- MDS0769: recipient filings | IRS e-file XML 202523209349300367 IRS990ScheduleB ContributorInformationGrp => none found in METR FY2024 public 990 Schedule B as of 2026-09-16T09:37:58Z: contributor fields are RESTRICTED | n=0 | role=negative strength=supporting lane=MD33
- MDS0238: recipient filings | GET IRS e-file XML 202523209349300367 IRS990ScheduleB => none found in METR FY2024 Form 990 XML 202523209349300367 Schedule B (ContributorNum RESTRICTED) as of 2026-09-16T06:04:57Z | n=0 | role=negative strength=primary lane=MD09
- MDS0432: recipient filings | GET S3 EfileData/XmlFiles/202523209349300367_public.xml; grep CANARY|AUDACIOUS|PROJECT CANARY; Part VIII RelatedOrganizationsAmt/AllOtherContributionsAmt; Schedule B ContributorInf => none found in METR FY2024 Form 990 object 202523209349300367 (Part VIII, Schedule B, Schedule R) as of 2026-09-16T07:22:52Z | n=0 | role=negative strength=primary lane=MD18
- MDS0415: recipient filings | GET GT XML 202523209349300367; search LONGVIEW|FOUNDERS PLEDGE|EVERY ORG|EFFECTIVE VENTURES|ContributorNum => none found in METR FY2024 Form 990 XML object 202523209349300367 as of 2026-09-16T07:27:52Z for a named Longview, Founders Pledge, Every Org, or Effective Ventures contributor | n=0 | role=negative st
- MDS0270: recipient filings | GET GivingTuesday S3 XML 202523209349300367_public.xml ; search LONGVIEW|EFFEKTIV|SPENDEN => none found in METR FY2024 Form 990 XML as of 2026-09-16T06:12:00Z for a Longview or Effektiv Spenden named payer | n=0 | role=negative strength=primary lane=MD10
- MDS1112: recipient filings | GET GT lake XML object 202523209349300367; grep IRS990ScheduleI / RecipientEIN 863605182 / ALIGNMENT RESEARCH CENTER grant table => none found in METR FY2024 Form 990 Schedule I as of 2026-09-16T09:52:40Z | n=0 | role=negative strength=supporting lane=MD12

### Contradictions, duplicates and defects

- Seed MDF0002 (run rate ~$13M p.a.) and MDF0003 (12-16 months runway) were typed commitment; both are DEAD (superseded by MDF0465/MDF0466, which clear the type). Do not chart them as inbound money.
- MDF0031 and MDF0035 (filed revenue / all-other contributions) were typed filed_grant in the medium run; both are DEAD, superseded by MDF0410/MDF0411 with money_type cleared.

### Figure notes
Use MDF0089 for the ~$71M denominator (commitment, last 6 months to 2026-08-14) and MDF0410/MDF0411/MDF0034 for the FY2024 filed composition (13,603,035 contributions = 4,501,424 related-organization + 9,101,611 unnamed). Never place these on the same axis as supporter amounts.


# Cautions (apply to every figure)

- Money types are never summed across type (pack rule; MDP0592). The identified supporter amounts are of six types: commitment (Audacious, Packard, METR's ~$71M), recommendation (Longview, SFF), regrant (Effektiv, EUR), paid_grant (Tallinn ledger), filed_grant (Founders Pledge, SVCF, Vanguard), transfer/in_kind_estimate (ARC), contract (EU AI Office, EUR).
- The amount_usd column holds non-USD figures on EUR rows: MDP0045, MDP0483, MDP0511, MDP0651, MDP0658 (128000 EUR), MDF0150, MDF0151, MDP0132, MDP0134, MDF0613, MDF0614, MDP0670 (1167484 EUR); seed MDF0014 and MDF0017 hold text. Always read the currency column.
- Restatement lanes are not new facts: MD50 rows subject 'audit of promoted MDFxxxx' (re-verification), MD47 rows 'documented transaction edges' (edge classification), MD53 rows 'number on figure resolves to' (figure bibliography), MD70 rows 'Live about-list supporter ...' (coverage), MD46 rows 'Excluded: ...' (recon re-run), MD99 rows (request-form cells). Cite the originating row ids listed under facts.
- Dead rows still cited by derived tables: MDF0076 (longview positive_rows; MDP0727), MDS0151 (lacentra negative_rows; MDP0723), MDS0214/MDS0217/MDS0218 (svcf negative_rows), MDS0215/MDS0219/MDS0220/MDS0221 (vanguard negative_rows). Seed negatives MDS0002-MDS0008 are dead ('unbounded in form', superseded by MDS1271-MDS1277). commitment_reconciliation.csv cites no dead rows.
- Off-by-one lineage notes: MDF0412 duplicates MDF0052 but claims to correct MDF0051; MDF0413 duplicates MDF0059 (ARC $147,000) but claims to correct MDF0058 (METR $184,000). Neither supersedes; treat both as duplicates.
- Type conflict: SFF-2025 $428,000 matching pledge is recommendation on MDF0046/MDF0197/MDP0185 (primary) and commitment on MDF0081/MDF0217/MDF0544/MDF0680.
- Arithmetic defect in a note: MDF0064 says 'the $47,511 difference is not attributed'; the filed differences are 52,511 (4,553,935 vs 4,501,424) and 24,255 (4,501,424 vs 4,477,169).
- Vanguard $4,000,000 provenance: the live ProPublica Schedule I became a JS shell; the amount rests on saved rendered-row captures (MD11 06:09Z, MD18 07:25Z, MD22, MD23, MD32). MD50 'mismatch' rows MDF0475/0501/0617/0669/0674 reflect the shell, not a changed filing.
- Page-appearance dates (all MDT 'first appearance' rows from MD24/MD06/MD08/MD07) bound when METR's page changed; they are never gift, grant or payment dates.
- Packard: award year 2026, term 12 months; 2026-07-06 is the catalog datePublished, not a signed-grant day; paid vs approved unknown until Packard TY2025/TY2026 990-PF.
- Audacious/Canary: no filing shows any payment to METR; the only filed Canary payments (Valhalla $10,000,000; High Tide $333,334, both TY2024) are to RAND Corporation.
- Same-money pairs the pack notes but does not merge: Founders Pledge filed $184,000 (MDF0058) = Tallinn ledger 2024-12-06 $184,000 via FP-US (MDF0053); SVCF filed $20,000 (MDF0037) = Tallinn ledger 2 x $10,000 via SFF-spec (MDF0051/MDF0052); ARC 4,477,169 + 76,766 = 4,553,935 vs METR 4,501,424. Draw as equalities, not as additional money and not as adviser identification.
- Individuals: METR names the class 'individuals from Jane Street' and four persons (Farhi, Ralston, Field, Newman). Name no other natural person. Jane Street firm Anthropic investments (MDR0004-MDR0008, MDR0083-MDR0087), Field's Form 4 DAF gifts (MDP0007/MDP0008), Farhi's FEC receipt (MDR0013), Ralston's AVERI/SAIF rows and Newman's board roles are not METR money.
- Seed baseline vs new: the S0 seed already held Audacious (~38M/17M/<16M), ARC 4,553,935, SFF-2024/2025 recommendations, Founders Pledge $184,000, SVCF $20,000, Vanguard $4,000,000, Longview $220,000, Effektiv 128,000 EUR, EU consortium 1,167,484 EUR, AISI undisclosed, Jane Street class, and the ~$71M sentence. Added by lanes: Packard $350,000 (MD02), the Tallinn ledger paid_grants and the SFF-2025 remainder/matching split (MD09), the ARC cash/non-cash split and METR-side 4,501,424 (MD01/MD12), the EU contract id/FTS detail (MD20), AISI programme ceilings (MD19), Founders Pledge grantee card (MD13), the Longview August 2023 report (MD10), legal-entity EINs (MD03-MD06), first-appearance windows (MD24), and the reconciliation (MD14/MD46).
- Recipient identity at the time: Longview (Aug 2023) and Effektiv Spenden (Aug 2023) money went to ARC Evals, then a project of Alignment Research Center (EIN 86-3605182), before METR Inc (EIN 99-1219864, formed 2024) existed; SFF-2022-H2 and SFF-2023-H1 recommendations and the 2022-2023 Founders Pledge/Tallinn payments were to ARC, not METR.
- Contract amounts in GBP (AISI ceilings) and EUR (EU lot total) are programme or consortium ceilings, never METR receipts; do not convert or divide.

# Suggested figures

- **A1 Named-supporter ledger**: One row per name on metr.org/about: status (amount identified vs acknowledged only), money type, amount and currency, date/period, payment status, primary row id. Rows: {"Audacious": ["MDF0167", "MDF0166", "MDF0169"], "Jane Street individuals": ["MDF0018", "MDP0003"], "Sijbrandij": ["MDP0004"], "Pew": ["MDP0009"], "Schmidt Sciences": ["MDF0022"], "Packard": ["MDF0020", "MDP0030"], "LaCentra-Sumerlin": ["MDR0021"], "Astralis": ["MDR0022"], "Expa.org": ["MDR0023"], "AISI": ["MDP0197", "MDP0200"], "Longview": ["MDF0070"], "Effektiv Spenden": ["MDF0072"], "SFF": ["MDF0047", "MDF0045", "MDF0046"], "Farhi": ["MDF0023"], "Ralston": ["MDF0025"], "Field": ["MDF0027"], "Newman": ["MDF0029"], "EU AI Office": ["MDF0150", "MDF0151"]}
- **A2 Audacious/Canary: one award, three statements**: Timeline of ~$38M joint (2024-10-09), ~$17M METR share (2024-10-09), a bit under $16M over 3 years (2025-09-28); RAND-side filed payments (Valhalla $10M, High Tide $333,334) on a RAND node; METR payment status: none filed. Rows: ["MDF0167", "MDF0165", "MDF0166", "MDF0170", "MDF0171", "MDF0169", "MDF0172", "MDP0001", "MDP0002", "MDS0432", "MDS0437", "MDS0438", "MDS0419"]
- **A3 ARC spin-off reconciliation**: ARC return: 4,477,169 cash + 76,766 non-cash = 4,553,935 (2024-04-30) vs METR return: 4,501,424; gap 52,511 unexplained; not attributable to any ARC funder. Rows: ["MDF0064", "MDF0065", "MDT0030", "MDF0034", "MDP0587", "MDP0015"]
- **A4 Filed payers METR does not name**: Founders Pledge $184,000 (TY2024), SVCF $20,000 (TY2024), Vanguard Charitable $4,000,000 (FY2025), ARC transfer; with the same-money equalities to the Tallinn ledger shown as links, not sums. Rows: ["MDF0058", "MDF0037", "MDF0038", "MDF0064", "MDF0053", "MDF0051", "MDF0052", "MDP0588"]
- **A5 SFF / Tallinn: recommendation vs matching pledge vs paid**: SFF-2024: $204,000 recommended; ledger $184,000 (FP-US) + $10,000 + $10,000 (SFF-spec). SFF-2025: $120,000 recommended + $428,000 conditional match (to 2026-09-30); no ledger payment found through 2026-08-14. Rows: ["MDF0047", "MDP0011", "MDF0053", "MDF0051", "MDF0052", "MDF0045", "MDF0046", "MDP0010", "MDS0232", "MDS1117"]
- **A6 Bounded-negatives matrix**: Supporter x source class, counting live (non-dead) MDS negatives; from the negatives arrays in this JSON. Rows: "negatives arrays"
- **A7 When each name first appeared on metr.org/about**: Page-change windows from MD24/MD06/MD07/MD08 (not gift dates). Rows: ["MDT0083", "MDT0085", "MDT0087", "MDT0075", "MDT0077", "MDT0079", "MDT0089", "MDT0091", "MDT0093", "MDT0095", "MDT0097", "MDT0099", "MDT0101", "MDT0103", "MDT0105", "MDT0067", "MDT0081", "MDT0069", "MDT0073"]
- **A8 Commitment reconciliation of the ~$71M**: Denominator MDF0089; sole compatible component Packard $350,000 (MDP0030); remainder ~$70.65M (MDP0056); every other known amount excluded with its reason (MDP0031-MDP0054, MDP0481-MDP0489). Rows: ["MDF0089", "MDP0030", "MDP0055", "MDP0056", "MDP0062", "MDP0033", "MDP0034", "MDP0035", "MDP0038", "MDP0039", "MDP0040", "MDP0041", "MDP0042", "MDP0043", "MDP0044", "MDP0045", "MDP0048", "MDP0049", "MDP0050", "MDP0051", "MDP0054", "MDP0481", "MDP0484"]

# Integrity

Row ids cited: 1285; missing from tables: none; dead rows cited (all flagged): MDF0002, MDF0003, MDF0031, MDF0035, MDF0076, MDS0151, MDS0214, MDS0215, MDS0217, MDS0218, MDS0219, MDS0220, MDS0221

# Table defects found (consolidated)

- Dead rows still cited in research/supporter_coverage.csv: longview positive_rows MDF0076; lacentra negative_rows MDS0151; svcf negative_rows MDS0214, MDS0217, MDS0218; vanguard negative_rows MDS0215, MDS0219, MDS0220, MDS0221. Also cited by MD70 rows MDP0727 (MDF0076) and MDP0723 (MDS0151).
- Wrong-type rows: the SFF-2025 $428,000 matching pledge is commitment on MDF0081, MDF0217 (and MD50 audits MDF0544, MDF0680) but recommendation on the MD09 primary MDF0046, MDF0197, MDP0185; Founders Pledge grantee card MDF0086 is paid_grant with no amount while the 990 line MDF0058 is filed_grant; seed MDF0015 (Jane Street class) and MDF0016 (AISI) carry seed-default money types and purposes not supported by any document; seed MDF0002/MDF0003 (run rate, runway) were typed commitment and are dead.
- Duplicated amounts with wrong lineage notes: MDF0412 duplicates MDF0052 (note says corrects MDF0051); MDF0413 duplicates MDF0059 (note says corrects MDF0058). Neither supersedes.
- Two figures in one amount cell: MDF0009 (seed) and MDP0039 '120000 + 428000 matching pledge'.
- EUR values in amount_usd: MDP0045, MDP0483, MDP0511, MDP0651, MDP0658, MDF0150, MDF0151, MDP0132, MDP0134, MDF0613, MDF0614, MDP0670; text amounts in MDF0014 ('EUR 128,000'), MDF0017 ('undisclosed share of EUR 1,167,484'), MDF0004/MDF0169 ('<16000000 ...'), MDF0002 (dead).
- Arithmetic slip in MDF0064 note ('$47,511 difference'); filed differences are 52,511 and 24,255.
- Date-precision inconsistencies for one fact: Packard 2026 vs 2026-07-06; Longview 2023 vs 2023-08; SVCF 2024 vs 2024-12-31 (precision 'day' on MDF0037 for a period end); Vanguard seed MDF0012 date is a text string; MDF0034 dated 2024-12-31 with precision 'day' for a fiscal-year total.
- Provenance gap: MDP0043 (Vanguard recon line) cites the seed CSV as its url/quote; MDP0593 records it; MD50 mismatch rows MDF0475/0501/0617/0669/0674 reflect the ProPublica JS shell.
- Pew from_entity trap: MDF0036/MDF0499/MDF1011 ($38,100,000 to Pew Research Center) will match a payer filter on 'Pew'.
