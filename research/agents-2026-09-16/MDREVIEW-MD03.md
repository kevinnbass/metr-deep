<!-- casework-review lane=research/grok-out/MD03-pew.csv -->

# Review of MD03 — pew

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 a1450b52051eb548b4214e8e7cbdea78c3d45a1b8377dbc9690baeb38c305f42; goal state complete. Checked against the lane's five saved Pew Charitable Trusts Form 990 Schedule I XMLs (FY2021-FY2025, recipient counts 439/407/401/391/535, 0 METR/ARC strings; FY2025 lines to Pew Research Center EIN 200881724 of 38100000, 2500000, 701292, 206887) and the live metr.org/about page. The lane's source_class 'public grant listings' is corrected to the config vocabulary; JavaScript-rendered search misses are context, not negatives; the Pew Research Center grant is context for the entity distinction only.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| 1 | DIFFERS | MDS | C02.E2;C01.E5 | {"source_class": "public grant databases"} | primary | negative |  | pew.org sitemap index plus 3 shards (20932 loc) enumerated; source_class corrected to config vocabulary |
| 2 | DIFFERS | MDS | C02.E2 | {"source_class": "public grant databases"} | supporting | context |  | JS-rendered search returned chrome only: route failure, bound as context; class corrected |
| 3 | DIFFERS | MDS | C02.E2 | {"source_class": "public grant databases"} | supporting | context |  | JS-rendered search, route failure, context; class corrected |
| 4 | DIFFERS | MDS | C02.E2 | {"source_class": "public grant databases"} | supporting | context |  | JS-rendered search, route failure, context; class corrected |
| 5 | DIFFERS | MDS | C02.E2 | {"source_class": "public grant databases"} | supporting | context |  | JS-rendered search, route failure, context; class corrected |
| 6 | DIFFERS | MDS | C02.E2 | {"source_class": "public grant databases"} | supporting | negative |  | program-specific listing, weak but bounded; class corrected |
| 7 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | news room checked; bounded |
| 8 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | accountability page and linked FY2025 990/financials checked; bounded |
| 9 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | consolidated financial statements do not itemise grantees; bounded |
| 10 | DIFFERS | MDS | C02.E2 | {"source_class": "public grant databases"} | supporting | context |  | summary of Task B routes; context; class corrected |
| 11 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | primary | negative |  | five saved Schedule I XMLs rechecked locally 2026-09-16: FY2021-FY2025 recipient counts 439/407/401/391/535 and 0 METR/ARC strings |
| 12 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | issuer-posted FY2025 990 PDF has no METR/ARC line; bounded |
| 13 | CONFIRMED | MDP | C02.E2 | {} | supporting | evidence |  | proposition correctly stated: named on metr.org/about without amount; not an award record |
| 14 | CONFIRMED | MDS | C02.E2 | {} | primary | negative |  | FY2021 Schedule I none; verified locally (439 recipients) |
| 15 | CONFIRMED | MDS | C02.E2 | {} | primary | negative |  | FY2022 Schedule I none; verified locally (407) |
| 16 | CONFIRMED | MDS | C02.E2 | {} | primary | negative |  | FY2023 Schedule I none; verified locally (401) |
| 17 | CONFIRMED | MDS | C02.E2 | {} | primary | negative |  | FY2024 Schedule I none; verified locally (391) |
| 18 | CONFIRMED | MDS | C02.E2 | {} | primary | negative |  | FY2025 Schedule I none; verified locally (535) |
| 19 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | calendar closer for the FYE 2026-06-30 return; context |
| 20 | CONFIRMED | MDE | C02.E2 | {} | primary | evidence |  | filer identity from the saved FY2025 XML: EIN 562307147, FYE June |
| 21 | CONFIRMED | MDE | C02.E2 | {} | supporting | evidence |  | Pew Research Center kept distinct (EIN 20-0881724 per lane); subsidiary is not the payer named by METR |
| 22 | CONFIRMED | MDF | C02.E2 | {} | supporting | context |  | verified locally: FY2025 Schedule I lines to Pew Research Center EIN 200881724 of 38100000, 2500000, 701292, 206887; not a METR payment; bound as context for the entity distinction |
| 23 | CONFIRMED | MDE | C02.E2 | {} | supporting | context |  | supporting trusts distinct from the filer; context |
| 24 | DIFFERS | MDS | C02.E2;C01.E5 | {"source_class": "public grant databases"} | supporting | negative |  | class-level bounded negative; class corrected |
| 25 | DIFFERS | MDS | C02.E2 | {"source_class": "public grant databases"} | supporting | context |  | JS search route failure; context; class corrected |
| 26 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | financial statements bounded negative |
| 27 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | accountability page bounded negative |
| 28 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | primary | negative |  | class-level summary for funder filings FY2021-FY2025 with blind spots stated |
| 29 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | Wayback capture of the legacy search UI only; context |
