<!-- casework-review lane=research/grok-out/MD13-grant-database-sweep.csv -->

# Review of MD13 — grant database sweep

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 1b94249243676609095ccbe0c46c2387103335f75bf145ad9ab10d59dad9d698; goal state complete. Enumeration-route lane. Positive hits (Packard API and sitemap, Longview grant CPT, SFF table, Founders Pledge card, GWWC sitemap, FLI sitemap, Audacious sitemap) are retargeted from MDF to MDS as enumeration receipts because every amount they surface is already a promoted funding event in MD02, MD09 or MD10; amounts for ARC are context; catalog negatives (Pew, Schmidt, Sijbrandij, LaCentra, Astralis, Expa, EA Funds CSV n=1663, FLI, Manifund, Coefficient permalinks and CDX, AISI grant pages, AI Safety Directory) are bounded negatives; blocked or dead catalogs (Candid, every.org 429, macroscopic.fund 404, vipulnaik 404, Effektiv Spenden 403) are route notes. Three source_class labels corrected to the config vocabulary.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| A01 | CONFIRMED | MDE | C02.E2;C01.E5 | {} | primary | evidence |  | metr.org/donate publishes legal name and EIN 99-1219864; alias list is the sweep universe |
| A02 | CONFIRMED | MDE | C02.E2 | {} | supporting | evidence |  | ARC EIN 86-3605182 kept distinct; secondary locator only |
| A03 | DIFFERS | MDP | C02.E2 | {"edge_type": "recipient supporter list; not a grant database and not a transaction date"} | supporting | context |  | retargeted from MDE to MDP |
| B01 | DIFFERS | MDS | C01.E5;C02.E2 | {"result": "grant-directory-pro/v1 full catalog re-enumerated: 1278 grantees, 2557 grants; exactly one METR grantee and one grant 2026-79050 at 350000.00; no ARC grantee", "money_type": "", "amount_usd": ""} | supporting | evidence |  | retargeted from MDF to MDS: second independent enumeration of the Packard catalog; the award itself is MD02 row A01 |
| B02 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | evidence |  | sitemap enumeration: 1001 + 278 loc = 1278, matching the API grantee count; METR only in part 2 |
| B03 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | negative |  | Pew sitemap shards (20932 loc) have no METR/ARC grant page; bounded |
| B04 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | negative |  | Schmidt Sciences profile_2025 CPT (n=35) has no METR; bounded |
| B05 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | negative |  | Sijbrandij sitemap (7 loc) and grants page: none; bounded |
| B06 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | negative |  | LaCentra sitemap (7 loc) and grants pages: none; bounded |
| B07 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | negative |  | Astralis has no grants path (404); bounded |
| B08 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | negative |  | Expa.org has no grant index; bounded |
| B09 | DIFFERS | MDS | C02.E5;C01.E5 | {"money_type": "", "result": "Longview WP grant CPT (n=23) contains one object titled Model Evaluation & Threat Research (slug arc-evaluations, dated 2023-09-25); the public REST payload does not expose an amount; keyword search=METR misses it, the catalog dump finds it"} | supporting | evidence |  | retargeted from MDF to MDS: a catalog hit without an amount is source coverage; the $220,000 figure is MD10 row 4 |
| B10 | DIFFERS | MDS | C01.E5;C02.E2 | {"money_type": "", "result": "SFF home/recommendations table enumerated: 472 data rows SFF-2019-Q3 to SFF-2025; METR Inc rows SFF-2025 $120,000 + $428,000 matching pledge and SFF-2024 $204,000; ARC rows separate"} | supporting | evidence |  | retargeted from MDF to MDS: enumeration receipt; the amounts are MD09 rows 1, 2 and 4 |
| B11 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | context |  | live Coefficient/Open Philanthropy grants catalog is withdrawn (/grants is a job page, no grant CPT, permalinks 404); route limitation, context |
| B12 | DIFFERS | MDS | C02.E5;C02.E2 | {"money_type": "", "result": "Founders Pledge grantee card: METR first funded April 2024; amount not published; sitemap (444 loc) omits /grantees/metr, so the canonical URL had to be fetched directly"} | supporting | evidence |  | retargeted from MDF to MDS; the filed amount is MD09 row 28 |
| B13 | CONFIRMED | MDF | C02.E5 | {} | supporting | context |  | GWWC sitemap hit restating the Longview $220,000; the figure is MD10 row 4; context |
| B14 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | primary | negative |  | EA Funds /api/grants CSV (n=1663) has no METR Inc grantee; canonical dump; bounded with the 2026 coverage caveat |
| B15 | CONFIRMED | MDF | C06.E1 | {} | supporting | context |  | FLI grant page: $1,401,000 recommended to Alignment Research Center (Evals Team); ARC, not METR; context |
| B16 | CONFIRMED | MDS | C06.E2;C01.E5 | {} | supporting | evidence |  | Audacious sitemap (244 loc): one Project Canary loc for the METR-RAND collaboration; no amount on the page; MD15/MD16 own the project |
| B17 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | negative |  | Manifund projects query: none; bounded via the rendered listing |
| B18 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | context |  | Candid login wall; locator only; context |
| C01 | CONFIRMED | MDF | C02.E2 | {} | supporting | context |  | Packard award; same as MD02 row A01; context |
| C02 | CONFIRMED | MDF | C02.E2 | {} | supporting | context |  | SFF-2024 $204,000; same as MD09 row 4; context |
| C03 | CONFIRMED | MDF | C02.E2 | {} | supporting | context |  | SFF-2025 $120,000; same as MD09 row 1; context |
| C03b | CONFIRMED | MDF | C02.E2 | {} | supporting | context |  | SFF-2025 $428,000 matching pledge; same pledge as MD09 row 2 (typed there as a conditional recommendation); context |
| C04 | DIFFERS | MDF | C02.E5 | {"source_class": "press"} | supporting | context |  | GWWC quotation of Longview's $220,000; same figure as MD10 row 4; class corrected; context |
| C05 | CONFIRMED | MDF | C06.E1 | {} | supporting | context |  | SFF-2024 ARC $197,000; same as MD09 row 6; context |
| C06 | CONFIRMED | MDF | C06.E1 | {} | supporting | context |  | FLI $1,401,000 to ARC Evals Team; same as B15; context |
| C07 | CONFIRMED | MDF | C06.E1 | {} | supporting | context |  | LTFF 2022 Q4 $72,000 to Alignment Research Center; ARC, not METR; context |
| C08 | CONFIRMED | MDF | C02.E5 | {} | supporting | context |  | Founders Pledge card; same as B12; context |
| C09 | CONFIRMED | MDF | C06.E2 | {} | supporting | context |  | Audacious Canary listing without an amount; MD16 owns the award structure; context |
| C10 | CONFIRMED | MDF | C06.E1 | {} | supporting | context |  | SFF-2023-H1 ARC Evals Team $3,247,000; same as MD09 row 8; context |
| D01 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | negative |  | Pew sitemap negative; bounded |
| D02 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | negative |  | Schmidt CPT negative; bounded |
| D03 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | negative |  | Sijbrandij negative; bounded |
| D04 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | negative |  | LaCentra negative; bounded |
| D05 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | negative |  | Coefficient permalinks 404 and CDX []; bounded with the paginated-archive caveat |
| D06 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | negative |  | EA Funds CSV negative; bounded |
| D07 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | negative |  | FLI grant-sitemap has no METR Inc loc; bounded |
| D08 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | context |  | Jane Street public site is not a grant database; context |
| D09 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | negative |  | Lightspeed Grants has no enumerable catalog (404); bounded |
| D10 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | context |  | Effektiv Spenden 403 wall; route failure; context |
| E01 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | context |  | Candid wall; context |
| E02 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | negative |  | Wayback CDX for Coefficient grant permalinks: []; bounded with the 504 caveat |
| E03 | DIFFERS | MDS | C01.E5;C02.E2 | {"source_class": "procurement records"} | supporting | context |  | scope note: procurement and IRS classes were outside this lane's routes; class corrected; context |
| E04 | DIFFERS | MDS | C01.E5;C02.E2 | {"source_class": "press"} | supporting | context |  | scope note: press not used as an award source; class corrected; context |
| E05 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | context |  | grantmakers.io profile 404; locator only; context |
| E06 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | longview.org/grants/ 404; the catalog is the CPT (B09); context |
| B19 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | supporting | context |  | AISI grants pages are a Challenge/Alignment Fund programme description, not an awardee register; route note; MD19 owns the AISI arrangement; context |
| D11 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | negative |  | AISI /grants, example-projects, 60-projects post and the Alignment Project site: no METR award string; bounded; MD19 owns the contract route |
| B20 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | supporting | evidence |  | AI Safety Directory sitemap (4546 loc, 98 grant cards): METR has an organisation page and no grant card; enumeration receipt |
| C11 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | directory card for an ARC-funded programme, not a METR receipt; context |
| D12 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | negative |  | directory grant cards: none paying METR Inc; bounded |
| B21 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | supporting | context |  | funder-landscape explainer, not an award index; context |
| D13 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | negative |  | explainer page has no award row; weak but bounded |
| B22 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | supporting | context |  | macroscopic.fund/grants 404 shell; route failure; context |
| D14 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | context |  | 404 on the grants path; route failure, not a negative about the organisation; context |
| B23 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | supporting | context |  | every.org 429 checkpoint; route failure; context |
| D15 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | context |  | every.org 429; route failure; context |
| B24 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | supporting | context |  | donations.vipulnaik.com organization page 404; route failure; context |
| D16 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | context |  | 404 on that path; context |
| E07 | CONFIRMED | MDS | C01.E5;C02.E2 | {} | supporting | context |  | every.org search 429; route failure; context |
