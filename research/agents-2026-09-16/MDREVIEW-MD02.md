<!-- casework-review lane=research/grok-out/MD02-packard-grant.csv -->

# Review of MD02 — packard grant

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 1534ba160828e518802f620e2cd81cd9a0e879803c0f883f5caf4224af7695f2; goal state complete. Checked against the saved primaries under research/primary/MD02-packard-grant/ (grant-directory-pro API record for grant 2026-79050: amount 350000.00, term 12, fiscal year 2026, 'for general support'; grantee page JSON-LD dates; four Packard 990-PF XMLs TY2021-TY2024 with 0 METR strings) and the live grantee page on 2026-09-16. DIFFERS rows type the award as a commitment with a year-precision date, and retarget enumeration and keyword-UI rows from MDF to MDS so one award is one funding event; route failures are context.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| A01 | DIFFERS | MDF | C02.E2;C01.E2;C01.E3 | {"ledger": "commitments", "date_precision": "year", "payment_status": "awarded per Packard's catalog; paid or approved-for-future-payment status not determinable until the TY2025 or TY2026 990-PF is posted"} | primary | evidence |  | saved primary packard.org_api_metr_grant json rechecked locally 2026-09-16: grant_id 2026-79050, grant_amount 350000.00, award_term 12, grant_fiscal_year 2026, content 'for general support'; grantee page live-checked; award is a commitment-type record, not a receipt |
| A02 | CONFIRMED | MDE | C02.E2 | {} | primary | evidence |  | grantee page h1 and website_url metr.org in saved API record |
| A03 | CONFIRMED | MDT | C02.E2;C09.E3 | {} | supporting | evidence |  | JSON-LD datePublished 2026-07-06T06:09:41Z and dateModified 2026-09-14T06:08:32Z match the saved page; page dates are not the grant date |
| A04 | CONFIRMED | MDF | C02.E2 | {} | supporting | context |  | same award as A01 seen on the grant permalink; bound as context so one grant is not two funding events |
| B01 | DIFFERS | MDS | C02.E2;C01.E5 | {"result": "METR grantee slug present in grantee-sitemap2.xml (278 loc, lastmod 2026-09-14T06:08:32Z); absent from grantee-sitemap.xml (1001 loc)"} | supporting | evidence |  | enumeration route, retargeted from MDF to MDS: a sitemap hit is source coverage, the award itself is row A01 |
| B02 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | supporting | negative |  | sitemap part 1 has no METR loc; bounded |
| B03 | DIFFERS | MDS | C02.E2;C01.E5 | {"result": "grant-directory-pro/v1 full catalog: 1278 grantees, 2557 grants; exactly one METR grantee (ID 2703989) and one grant 2026-79050 at 350000.00"} | primary | evidence |  | retargeted from MDF to MDS: this is the canonical-API enumeration receipt that closes the Packard-style keyword miss; the award is row A01 |
| B04 | DIFFERS | MDS | C02.E2 | {"result": "keyword grant_keyword=Model Evaluation returns 1 grantee"} | supporting | context |  | retargeted to MDS: keyword UI result, context only |
| B05 | DIFFERS | MDS | C02.E2 | {"result": "keyword grant_keyword=Model Evaluation and Threat Research returns 1 grantee"} | supporting | context |  | retargeted to MDS: keyword UI result, context only |
| B06 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | primary | negative |  | keyword METR returns three unrelated substring hits and misses the grantee; this is the documented reason keyword search alone is insufficient |
| B07 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | keyword Alignment Research Center returns 0; bounded; separate legal entity |
| B08 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | keyword ARC Evals returns 0; bounded |
| B09 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | noisy-substring note; context |
| B10 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | WP REST route absent; route note, context |
| C01 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | primary | negative |  | saved TY2024 990-PF XML rechecked locally: 0 METR strings; TotalGrantOrContriPdDurYrAmt 349965123 matches |
| C02 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | primary | negative |  | TY2023 990-PF Part XV paid and approved groups: none |
| C03 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | primary | negative |  | TY2022 990-PF Part XV paid and approved groups: none |
| C04 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | primary | negative |  | TY2021 990-PF Part XV paid and approved groups: none |
| C05 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | supporting | negative |  | index_2026 has no Packard 990-PF at check time; TY2025 return is a calendar closer for the paid-versus-approved typing of the 2026 award |
| D01 | DIFFERS | MDS | C02.E2;C09.E3 | {"result": "none found in Wayback CDX for the grantee URL as of 2026-09-16T05:37:37Z (0 rows)"} | supporting | negative |  | retargeted from MDT to MDS: a zero-capture archive result is source coverage, not a timeline event |
| D02 | CONFIRMED | MDS | C02.E2;C09.E3 | {} | supporting | negative |  | CDX 0 rows for the grant permalink; bounded |
| E01 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | primary | negative |  | summary bounded negative for the funder-filings class TY2021-TY2024 with the unfiled-year blind spot stated |
| E02 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | route failure (TEOS 403), context |
| E03 | CONFIRMED | MDS | C02.E2;C09.E3 | {} | supporting | negative |  | archives class bounded negative with the 429 cap stated |
| E04 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | API /search endpoint returns an empty body; route note, context |
| E05 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | keyword Alignment Research returns 0; bounded |
