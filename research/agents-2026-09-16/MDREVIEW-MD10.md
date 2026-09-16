<!-- casework-review lane=research/grok-out/MD10-longview-pooled-regrants.csv -->

# Review of MD10 — longview pooled regrants

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 21bb881931f4cc1890cf03c6cd30336011e276081cfa80216a44e347824a035f; goal state complete. Checked against the lane's saved Longview Philanthropy USA Inc TY2024 Form 990 XML (Schedule I grantees Players Philanthropy Fund, Rethink Priorities, AI Objectives Institute, Pacific Forum International, Horizon Institute; Schedule F Europe grants 504714, 262000, 126000; no METR/ARC), live checks on 2026-09-16 of the GWWC August 2023 grants report ('ARC Evals (now called METR) — 20,000', Longview decided the grants) and the Effektiv Spenden fund page (METR formerly ARC Evals, 128.000 €, August 2023), and the saved Companies House record for Longview Inc. Ltd. Recommendations and the EUR regrant are typed and kept unconverted; route identifications are retargeted from MDF to MDE/MDP/MDS so no non-amount row sits in the money ledger; blocked routes are context.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| 1 | DIFFERS | MDP | C02.E5 | {"money_type": "", "ledger": "", "edge_type": "recipient names pooled and recommendation routes without amounts"} | supporting | evidence |  | retargeted from MDE to MDP; money_type cleared |
| 2 | DIFFERS | MDP | C02.E5;C06.E1 | {"money_type": "", "edge_type": "route profiles the grantee without an amount"} | supporting | context |  | retargeted from MDF to MDP; not a funding event |
| 3 | DIFFERS | MDE | C02.E5;C06.E1 | {"money_type": "", "subject": "Emerging Challenges Fund (public fund managed by Longview Philanthropy; donations handled by Giving What We Can)"} | supporting | context |  | retargeted from MDF to MDE: fund identity, not a funding event |
| 4 | DIFFERS | MDF | C02.E5;C06.E1 | {"ledger": "commitments"} | primary | evidence |  | GWWC August 2023 grants report live-checked 2026-09-16: 'ARC Evals (now called METR) — $220,000'; Longview made the grantmaking decisions; recommendation, not a filed grant |
| 5 | CONFIRMED | MDF | C02.E5 | {} | supporting | context |  | GWWC charity page restates the same $220,000; context so one recommendation is one row |
| 6 | DIFFERS | MDS | C02.E5;C06.E1 | {"money_type": "", "result": "Frontier AI Fund public page reports an aggregate of 18 organisations Dec 2024-Sep 2025; METR not named; amounts not public"} | supporting | negative |  | retargeted from MDF to MDS: a private fund's aggregate is source coverage |
| 7 | DIFFERS | MDF | C02.E5;C06.E1 | {"ledger": "transfers_regrants", "quantity_or_value": "128,000 EUR"} | primary | evidence |  | Effektiv Spenden fund page live-checked 2026-09-16 (via this reviewer's fetch): METR (formerly ARC Evals) 128.000 €, grants made August 2023; EUR kept as EUR |
| 8 | CONFIRMED | MDF | C02.E5;C06.E1 | {} | supporting | context |  | German H1/2023 blog restates the same EUR 128,000 and names Longview as recommender; context |
| 9 | CONFIRMED | MDF | C02.E5 | {} | supporting | context |  | SFF-2025 METR row; owned and promoted by MD09; context |
| 10 | CONFIRMED | MDF | C02.E5 | {} | supporting | context |  | SFF-2024 METR row; owned by MD09; context |
| 11 | CONFIRMED | MDE | C02.E5;C06.E1 | {} | primary | evidence |  | Longview Philanthropy USA Inc EIN 93-2664730 distinct from the brand |
| 12 | DIFFERS | MDE | C02.E5;C06.E1 | {"source_class": "state registries"} | supporting | evidence |  | Companies House record for Longview Inc. Ltd 14444004; class corrected |
| 13 | DIFFERS | MDS | C06.E1 | {"money_type": "", "result": "none found in Longview Philanthropy USA Inc TY2024 Form 990 Schedule I (domestic grantees: Players Philanthropy Fund, Rethink Priorities, AI Objectives Institute, Pacific Forum International, Horizon Institute) as of 2026-09-16T06:06:36Z"} | primary | negative |  | saved gt-xml-longview-usa-2024 rechecked locally: those five grantees, no METR/ARC; retargeted from MDF to MDS |
| 14 | DIFFERS | MDS | C06.E1 | {"money_type": "", "result": "none found in Longview USA Inc TY2024 Schedule F (three unnamed Europe grants 504714, 262000, 126000) as of 2026-09-16T06:06:36Z"} | primary | negative |  | saved XML rechecked locally: Schedule F amounts match; foreign grantees unnamed; retargeted to MDS |
| 15 | CONFIRMED | MDS | C06.E1 | {} | supporting | context |  | Companies House accounts are a scanned image without extractable text; route limitation; context |
| 16 | CONFIRMED | MDE | C02.E5;C06.E1 | {} | supporting | evidence |  | UES gGmbH für effektives Spenden as the German legal filer; from a Wayback impressum capture |
| 17 | CONFIRMED | MDS | C06.E1 | {} | supporting | context |  | Charity Commission search UI is JS and the API is 401; context |
| 18 | CONFIRMED | MDS | C06.E1 | {} | primary | negative |  | METR Schedule B RESTRICTED; boundary |
| 19 | CONFIRMED | MDS | C06.E1 | {} | supporting | context |  | ProPublica locator; context |
| 20 | CONFIRMED | MDP | C02.E5;C06.E1 | {} | supporting | evidence |  | the recovered $220,000 is a recommendation; ECF disburses on Longview recommendations |
| 21 | CONFIRMED | MDP | C06.E1 | {} | supporting | context |  | FAIF aggregate proposition; context |
| 22 | CONFIRMED | MDS | C06.E1 | {} | supporting | context |  | ECF 2025 annual report PDF not recovered; route failure; context |
| 23 | CONFIRMED | MDP | C06.E1 | {} | supporting | evidence |  | Effektiv Spenden states the grant was made; the German filer's accounts were not recovered; bounded |
| 24 | CONFIRMED | MDP | C02.E5 | {} | supporting | negative |  | December 2023 ECF report lists FAR AI and Blueprint, not METR; bounded |
| 25 | CONFIRMED | MDR | C02.E5;C06.E1 | {} | supporting | evidence |  | donors to GWWC/ECF are not METR donors; entity separation |
| 26 | CONFIRMED | MDR | C02.E5;C06.E1 | {} | supporting | evidence |  | Effektiv Spenden fund donors are not METR donors; entity separation |
| 27 | CONFIRMED | MDE | C02.E5;C06.E1 | {} | supporting | evidence |  | ARC distinct from METR at the 2023 grant date |
| 28 | CONFIRMED | MDR | C02.E5 | {} | supporting | evidence |  | SFF recommender not merged into METR's donor identity |
| 29 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | context |  | live Effektiv Spenden 403; Wayback used; context |
| 30 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | context |  | r.jina.ai 403; context |
| 31 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | longview.org/grants 404 and no archived copies; bounded |
| 32 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | Longview site search and wp-json grant search: no METR amount; bounded |
| 33 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | context |  | TEOS 403; context |
| 34 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | context |  | AWS yearly index 404; context |
| 35 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | context |  | BMF DE extract 404 at that path; context |
| 36 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | SEC EFTS 0 hits; bounded |
| 37 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | SEC EFTS 0 hits; bounded |
| 38 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | CourtListener 0; bounded |
| 39 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | context |  | USAspending JS shell; context |
| 40 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | context |  | GWWC /charities/metr 404; METR sits under /charities/arc-evals; context |
| 41 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | context |  | Bundesanzeiger search chrome only; context |
| 42 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | context |  | Charity Commission API 401; context |
| 43 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | context |  | record that nothing was sent; context |
| 44 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | context |  | scope note: DAF-sponsor sweep belongs to MD11/MD22; context |
