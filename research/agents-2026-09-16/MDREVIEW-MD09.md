<!-- casework-review lane=research/grok-out/MD09-sff-tallinn.csv -->

# Review of MD09 — sff tallinn

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 39aa1a9baefe936f13e283bb51ef54d83962d5eee34482336472fbb09d12f51f; goal state complete. Checked against the lane's saved SFF round pages, the saved Founders Pledge TY2022/TY2023 990-PF and TY2024 990 XMLs (2179000, 1846000, 184000 METR and 147000 ARC), the saved SVCF TY2024 XML, and a live fetch of jaan.online/philanthropy/donations.csv on 2026-09-16T06:38Z (sha256 57ebf17c5a48ad24184942b81d39685aa34df9ae2b37b39aa39d7cc149f48b8e) whose METR and ARC lines match rows 18-24 verbatim. Speculation annotations are retargeted to MDP with amounts cleared so no annotation becomes a second funding event; ledger payments are typed paid_filed; ARC-recipient rows are context. Row 53's index_2025 none-found is contradicted by MD01's saved hit (the lane's index copy was a truncated 24.3 MB download) and is corrected to the positive locator.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| 1 | CONFIRMED | MDF | C02.E2;C02.E5 | {} | primary | evidence |  | saved sff-recommendations and 2025 pages show the METR row: $120,000 with a separately printed $428,000 matching pledge |
| 2 | CONFIRMED | MDF | C02.E2;C02.E5 | {} | primary | evidence |  | saved 2025 recommendations page: $428,000 matching pledge at 1x through 2026-09-30; conditional, not a payment |
| 3 | DIFFERS | MDP | C02.E5 | {"amount_usd": "", "money_type": "", "edge_type": "annotation on the SFF-2025 track total: speculation ($120,000)† is not additional dollars"} | supporting | context |  | retargeted from MDF to MDP and amount cleared so the annotation is not a second $120,000 funding event |
| 4 | CONFIRMED | MDF | C02.E2;C02.E5 | {} | primary | evidence |  | saved sff-2024 pages show $204,000 to Model Evaluation and Threat Research, Inc., General support |
| 5 | DIFFERS | MDP | C02.E5 | {"amount_usd": "", "money_type": "", "edge_type": "annotation: SFF-2024 ($20,000)† speculation inside the $204,000, not additional dollars"} | supporting | context |  | retargeted from MDF to MDP; amount cleared |
| 6 | CONFIRMED | MDF | C02.E5;C06.E1 | {} | supporting | context |  | SFF-2024 recommendation to Alignment Research Center, a separate legal recipient; context for ARC provenance |
| 7 | DIFFERS | MDP | C06.E1 | {"amount_usd": "", "money_type": "", "edge_type": "annotation: SFF-2024 ARC ($50,000)† speculation inside the $197,000"} | supporting | context |  | retargeted to MDP; amount cleared |
| 8 | CONFIRMED | MDF | C06.E1;C02.E5 | {} | supporting | context |  | SFF-2023-H1 recommendation to Alignment Research Center (Evals Team); ARC, not METR; context |
| 9 | CONFIRMED | MDF | C06.E1;C02.E5 | {} | supporting | context |  | SFF-2022-H2 recommendation to Alignment Research Center; context |
| 10 | CONFIRMED | MDP | C02.E5 | {} | supporting | evidence |  | metr.org/about names SFF recommendations as a route; live-checked |
| 11 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | negative |  | older SFF round page saved; no METR/ARC/ARC Evals row; bounded to that page |
| 12 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | negative |  | older SFF round page saved; no METR/ARC/ARC Evals row; bounded to that page |
| 13 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | negative |  | older SFF round page saved; no METR/ARC/ARC Evals row; bounded to that page |
| 14 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | negative |  | older SFF round page saved; no METR/ARC/ARC Evals row; bounded to that page |
| 15 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | negative |  | older SFF round page saved; no METR/ARC/ARC Evals row; bounded to that page |
| 16 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | negative |  | older SFF round page saved; no METR/ARC/ARC Evals row; bounded to that page |
| 17 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | negative |  | older SFF round page saved; no METR/ARC/ARC Evals row; bounded to that page |
| 18 | DIFFERS | MDF | C02.E2;C02.E5 | {"ledger": "paid_filed"} | primary | evidence |  | live jaan.online/philanthropy/donations.csv fetched 2026-09-16T06:38Z (sha256 57ebf17c…) shows this line verbatim; ledger typed paid_filed (self-reported payment) |
| 19 | DIFFERS | MDF | C02.E2;C02.E5 | {"ledger": "paid_filed"} | primary | evidence |  | live jaan.online/philanthropy/donations.csv fetched 2026-09-16T06:38Z (sha256 57ebf17c…) shows this line verbatim; ledger typed paid_filed (self-reported payment) |
| 20 | DIFFERS | MDF | C02.E2;C02.E5 | {"ledger": "paid_filed"} | primary | evidence |  | live jaan.online/philanthropy/donations.csv fetched 2026-09-16T06:38Z (sha256 57ebf17c…) shows this line verbatim; ledger typed paid_filed (self-reported payment) |
| 21 | DIFFERS | MDF | C06.E1;C02.E5 | {"ledger": "paid_filed"} | supporting | context |  | live jaan.online/philanthropy/donations.csv fetched 2026-09-16T06:38Z (sha256 57ebf17c…) shows this line verbatim; ledger typed paid_filed (self-reported payment); payment to Alignment Research Center, not METR; context |
| 22 | DIFFERS | MDF | C06.E1;C02.E5 | {"ledger": "paid_filed"} | supporting | context |  | live jaan.online/philanthropy/donations.csv fetched 2026-09-16T06:38Z (sha256 57ebf17c…) shows this line verbatim; ledger typed paid_filed (self-reported payment); payment to Alignment Research Center, not METR; context |
| 23 | DIFFERS | MDF | C06.E1;C02.E5 | {"ledger": "paid_filed"} | supporting | context |  | live jaan.online/philanthropy/donations.csv fetched 2026-09-16T06:38Z (sha256 57ebf17c…) shows this line verbatim; ledger typed paid_filed (self-reported payment); payment to Alignment Research Center, not METR; context |
| 24 | DIFFERS | MDF | C06.E1;C02.E5 | {"ledger": "paid_filed"} | supporting | context |  | live jaan.online/philanthropy/donations.csv fetched 2026-09-16T06:38Z (sha256 57ebf17c…) shows this line verbatim; ledger typed paid_filed (self-reported payment); payment to Alignment Research Center, not METR; context |
| 25 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | primary | negative |  | live ledger fetched 2026-09-16: no METR line after 2024-12-06; last disbursed date 2025-03-31; bounded |
| 26 | CONFIRMED | MDS | C06.E1 | {} | supporting | negative |  | no second ARC Evals Team line on the ledger; bounded |
| 27 | CONFIRMED | MDE | C02.E5 | {} | primary | evidence |  | Founders Pledge Inc EIN 37-1795297 as the FP-US legal payer |
| 28 | CONFIRMED | MDF | C02.E2;C02.E5 | {} | primary | evidence |  | saved FP TY2024 Schedule I XML: CashGrantAmt 184000 to METR EIN 99-1219864; ledger paid_filed |
| 29 | CONFIRMED | MDF | C06.E1;C02.E5 | {} | supporting | context |  | FP TY2024 filed $147,000 to ARC; context |
| 30 | CONFIRMED | MDF | C06.E1;C02.E5 | {} | supporting | context |  | FP TY2023 990-PF $1,846,000 general support of ARC Evals Team; context |
| 31 | CONFIRMED | MDF | C06.E1;C02.E5 | {} | supporting | context |  | FP TY2022 990-PF $2,179,000 to ARC; context |
| 32 | CONFIRMED | MDE | C02.E5 | {} | supporting | evidence |  | SVCF EIN 20-5205488 as DAF-sponsor filer; adviser not identified |
| 33 | CONFIRMED | MDF | C02.E2;C02.E5 | {} | primary | evidence |  | SVCF TY2024 $20,000 to METR verified in MD11; the row records a dollar match to two ledger lines as an observation only and does not identify an adviser |
| 34 | CONFIRMED | MDF | C06.E1;C02.E5 | {} | supporting | context |  | SVCF TY2024 $50,450 to ARC; context |
| 35 | CONFIRMED | MDE | C02.E5 | {} | supporting | context |  | Survival and Flourishing Corp kept distinct as a PBC; context |
| 36 | CONFIRMED | MDS | C02.E5 | {} | supporting | negative |  | SFC has no 990 identity; locator negative |
| 37 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | negative |  | TY2025 FP/SVCF returns not yet indexed; calendar-bounded negative |
| 38 | CONFIRMED | MDS | C06.E1 | {} | supporting | negative |  | no second ARC Evals amount in FP TY2023; FLI filing not retrieved; bounded |
| 39 | CONFIRMED | MDR | C05.E1;C05.E2 | {} | primary | evidence |  | Anthropic Series A page names Tallinn as lead; amount undisclosed; issuer statement |
| 40 | CONFIRMED | MDE | C05.E1;C05.E3 | {} | supporting | evidence |  | Metaplanet named as Tallinn's investment vehicle in a press-quoted statement; entity distinction |
| 41 | CONFIRMED | MDR | C05.E1 | {} | supporting | evidence |  | Semafor 2023: declined a board seat; press |
| 42 | CONFIRMED | MDR | C05.E1 | {} | supporting | evidence |  | Postimees 2026: press reports an observer role and quotes Tallinn; press, not issuer |
| 43 | CONFIRMED | MDS | C05.E1 | {} | supporting | negative |  | anthropic.com/company board list does not name Tallinn; observer seats are not on that list; bounded |
| 44 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | primary | negative |  | METR Schedule B RESTRICTED; verification boundary |
| 45 | CONFIRMED | MDS | C05.E1;C05.E2 | {} | supporting | negative |  | SEC EFTS: no Anthropic filing naming Tallinn's amount or role; bounded |
| 46 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | negative |  | CourtListener 0; bounded |
| 47 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | context |  | GET 405; route note; context |
| 48 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | context |  | legacy RCT 404; context |
| 49 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | context |  | Candid DNS failure; context |
| 50 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | context |  | archives not needed (live 200); context |
| 51 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | negative |  | no published SFF grant letter naming the check-writing entity; bounded |
| 52 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | context |  | record that nothing was sent; context |
| 53 | DIFFERS | MDS | C02.E2;C02.E5 | {"result": "index_2025.csv does list METR EIN 991219864 (OBJECT_ID 202523209349300367, batch 2025_TEOS_XML_11C) per MD01's saved hit file; this lane's copy of the index missed it, so its none-found is withdrawn", "limitation": "the lane's saved index_2025 copy is 24,346,943 bytes / 195,937 lines and contains no 991219864 row, i.e. a truncated download; MD01's hit file from the complete index lists the METR row (batch 2025_TEOS_XML_11C); MD01 row 7 is the authoritative locator"} | supporting | context |  | contradicted by MD01's saved index_2025 hit; the lane's index copy was truncated (24.3 MB); corrected to the positive locator and bound as context |
