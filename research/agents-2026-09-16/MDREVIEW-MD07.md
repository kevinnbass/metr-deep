<!-- casework-review lane=research/grok-out/MD07-jane-street-individuals.csv -->

# Review of MD07 — individuals from Jane Street

Reviewing agent: Claude (parent session), 2026-09-16. Every row was checked against the lane's saved primaries under research/primary/MD07-jane-street-individuals/ and, for the METR pages, Founders Pledge and GWWC, against the live page on 2026-09-16. Lane CSV sha256 ca15810dab59556490d9aec61ba9a255d35a77bbccc395e27e028674bffcda5a; goal state complete. DIFFERS rows correct vocabulary (source_class) or clear an unsupported money_type; route failures (403/429/login wall/redirect) are bound as context, not as negatives; one wrong-host row is UNVERIFIABLE.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| 1 | DIFFERS | MDF | C02.E2 | {"money_type": "", "ledger": "", "payment_status": "acknowledged as a supporter; amount, date, vehicle and money type not disclosed by the source"} | primary | evidence |  | primary checked live 2026-09-16: metr.org/about lists 'individuals from Jane Street' among supporters; the source acknowledges support and gives no amount, date, vehicle or money type, so money_type is cleared rather than typed as a commitment |
| 2 | DIFFERS | MDF | C02.E2;C01.E2 | {"money_type": "", "ledger": "", "payment_status": "acknowledged as a supporter; amount, date, vehicle and money type not disclosed by the source", "date_precision": "day"} | primary | evidence |  | primary checked live 2026-09-16: the 2026-08-14 funding update's thank-you sentence matches verbatim; the date is the post date, not a gift date; the same post carries the approximately $71M sentence (C01.E1 is owned by MD14) |
| 3 | CONFIRMED | MDT | C02.E2 | {} | supporting | context |  | same thank-you text as row 2 republished on X; bound as context so the one statement is not counted twice |
| 4 | DIFFERS | MDE | C05.E1;C05.E3 | {"source_class": "court dockets", "entity_type": "investment entity (limited liability company)", "identifier": "purchaser named in Case 22-11068-JTD Doc 10241-1 Exhibit 1"} | primary | evidence |  | saved primary court-ftx-10241-1 p.1 lists 'Jane Street Global Trading, LLC 3,332,833 $99,999,988'; source_class corrected from 'government filings' to the config vocabulary; the LLC is the purchasing entity, not the firm's employees |
| 5 | DIFFERS | MDR | C05.E1;C05.E3 | {"source_class": "court dockets", "quantity_or_value": "3,332,833 shares for $99,999,988", "relationship_type": "court-documented share purchase from the FTX estate"} | primary | evidence |  | figures match the saved exhibit exactly; filed 03/22/24; a firm-entity purchase is not a donation and is kept separate from any METR gift |
| 6 | CONFIRMED | MDR | C05.E1;C05.E3 | {} | primary | evidence |  | saved Series E page names Jane Street among participants; amount and share undisclosed |
| 7 | CONFIRMED | MDR | C05.E1;C05.E3 | {} | primary | evidence |  | saved Series F page names Jane Street among participants |
| 8 | CONFIRMED | MDR | C05.E1;C05.E3 | {} | primary | evidence |  | saved Series G page names Jane Street among participants |
| 9 | CONFIRMED | MDR | C05.E1;C05.E3 | {} | primary | evidence |  | saved Series H page names Jane Street among participants |
| 10 | CONFIRMED | MDS | C02.E2 | {} | primary | negative |  | bounded negative: X Latest keyword search, capped page; the quote_300 reproduces METR's own thank-you, which is the only hit |
| 11 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | bounded negative with the GraphQL 400 limitation stated; the saved search HTML is the record |
| 12 | CONFIRMED | MDP | C02.E2;C05.E3 | {} | primary | negative |  | bounded limit stated correctly: METR names no individual and a public charity's public Schedule B copy is redacted; this is the verification boundary, not a finding of absence |
| 13 | CONFIRMED | MDS | C02.E2;C02.E3 | {} | primary | negative |  | saved metr-990-fy2024 XML shows Schedule B contributor fields RESTRICTED (8 occurrences); bounded correctly |
| 14 | CONFIRMED | MDS | C02.E2;C05.E3 | {} | supporting | negative |  | ProPublica org search returns only unrelated 'Jane Street' civic organizations; used as a locator only |
| 15 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | janestreet.com site search saved; no METR hit; the firm's own site is not where an individual's gift would appear, so this is weak but bounded |
| 16 | CONFIRMED | MDS | C02.E2;C05.E3 | {} | primary | negative |  | six saved BEMC 990-PF XMLs (TY2020-TY2024) contain no METR or Alignment Research string; rechecked locally |
| 17 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | negative |  | live page checked 2026-09-16: METR grantee page shows 'First funded: April 2024', no amount, no donor names; the 'July 2026' fragment in quote_300 belongs to other grantees on the same page |
| 18 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | negative |  | live page checked 2026-09-16: Longview $220,000 public-fund recommendation in 2023 sentence matches; no individual donor named |
| 19 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | negative |  | Longview public pages do not name a Jane Street individual; pooled-fund principals are undisclosed by design |
| 20 | DIFFERS | MDS | C02.E2 | {"source_class": "self-statements"} | supporting | negative |  | source_class corrected to the config vocabulary; the row correctly refuses to treat a former-employment bio as a gift acknowledgment |
| 21 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | route failure, not a content negative: IRS TEOS returned HTTP 403; bound as context so it does not count as a searched source |
| 22 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | route failure, not a content negative: Candid login wall; bound as context |
| 23 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | route failure: live /grants redirected to a closed job posting; the grantmaker index enumeration belongs to MD13; bound as context |
| 24 | CONFIRMED | MDS | C02.E2;C03.E1 | {} | primary | negative |  | metr.org/donate saved; names no Jane Street person; the employee-donation sentence is present and is evidence for C03.E1 wording as of 2026-09-16 |
| 25 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | route failure, not a content negative: every.org HTTP 429; bound as context |
| 26 | UNVERIFIABLE | MDS | C02.E2 | {} | primary | evidence |  | route tried: intercept.bio, which the lane itself identifies as a biology-equipment directory unrelated to any AI entity; the row establishes nothing about METR and stays in immutable lane output only |
