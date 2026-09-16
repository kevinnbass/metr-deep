<!-- casework-review lane=research/grok-out/MD11-daf-filed-grants.csv -->

# Review of MD11 — daf filed grants

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 ee886453e18ec4644ff02443110ededa16be2f8c8473299c0952d55004ac3056; goal state complete. Checked against the lane's saved Schedule I excerpts under research/primary/MD11-daf-filed-grants/ (SVCF TY2024: METR 20000 and ARC 50450; SVCF TY2023 ARC 1401000; Fidelity FY2024 ARC 100000; Vanguard FY2023 ARC 201000 and FY2024 ARC 1000000) and the saved ProPublica render of Vanguard FY2025 Schedule I (METR 4,000,000; ARC 1,500,000). Per-year negatives for periods that cover METR's existence rest on the lane's reproducible scan of the named object ids (the saved excerpts hold only matched rows), so they are bound as supporting negatives; pre-existence years are structurally empty. ARC grants are context; 'no account principal' rows have their money fields cleared; calendar rows and blocked routes are context.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| 1 | DIFFERS | MDF | C02.E3;C02.E5;C03.E3 | {"ledger": "paid_filed", "date_precision": "day"} | primary | evidence |  | saved SVCF TY2024 Schedule I excerpt rechecked locally: RecipientEIN 991219864, CashGrantAmt 20000; sponsor names no account principal; ledger typed |
| 2 | DIFFERS | MDF | C02.E3;C02.E5;C03.E3 | {"ledger": "paid_filed", "date_precision": "day"} | primary | evidence |  | saved ProPublica render of Vanguard FY2025 Schedule I row 15424 rechecked locally: METR CashGrantAmt 4,000,000; the e-file XML object is absent from the lake and the IRS zip (row 67), so the sponsor's rendered public copy is the working primary; ledger typed |
| 3 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period ends before METR existed (formed May 2024); structurally empty, bounded |
| 4 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period ends before METR existed (formed May 2024); structurally empty, bounded |
| 5 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period ends before METR existed (formed May 2024); structurally empty, bounded |
| 6 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period ends before METR existed (formed May 2024); structurally empty, bounded |
| 7 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period covers METR's existence; the lane's saved excerpt holds only matched rows, so this negative rests on the lane's reproducible scan of the named object id (result_count 0), not on a local re-scan; bounded |
| 8 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period covers METR's existence; the lane's saved excerpt holds only matched rows, so this negative rests on the lane's reproducible scan of the named object id (result_count 0), not on a local re-scan; bounded |
| 9 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period ends before METR existed (formed May 2024); structurally empty, bounded |
| 10 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | context |  | two-day return with no recipient table; context |
| 11 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period ends before METR existed (formed May 2024); structurally empty, bounded |
| 12 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period ends before METR existed (formed May 2024); structurally empty, bounded |
| 13 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period covers METR's existence; the lane's saved excerpt holds only matched rows, so this negative rests on the lane's reproducible scan of the named object id (result_count 0), not on a local re-scan; bounded |
| 14 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period covers METR's existence; the lane's saved excerpt holds only matched rows, so this negative rests on the lane's reproducible scan of the named object id (result_count 0), not on a local re-scan; bounded |
| 15 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period ends before METR existed (formed May 2024); structurally empty, bounded |
| 16 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period ends before METR existed (formed May 2024); structurally empty, bounded |
| 17 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period ends before METR existed (formed May 2024); structurally empty, bounded |
| 18 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period covers METR's existence; the lane's saved excerpt holds only matched rows, so this negative rests on the lane's reproducible scan of the named object id (result_count 0), not on a local re-scan; bounded |
| 19 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period ends before METR existed (formed May 2024); structurally empty, bounded |
| 20 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period ends before METR existed (formed May 2024); structurally empty, bounded |
| 21 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period ends before METR existed (formed May 2024); structurally empty, bounded |
| 22 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period covers METR's existence; the lane's saved excerpt holds only matched rows, so this negative rests on the lane's reproducible scan of the named object id (result_count 0), not on a local re-scan; bounded |
| 23 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period covers METR's existence; the lane's saved excerpt holds only matched rows, so this negative rests on the lane's reproducible scan of the named object id (result_count 0), not on a local re-scan; bounded |
| 24 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period ends before METR existed (formed May 2024); structurally empty, bounded |
| 25 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period ends before METR existed (formed May 2024); structurally empty, bounded |
| 26 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | negative |  | period ends before METR existed (formed May 2024); structurally empty, bounded |
| 27 | DIFFERS | MDF | C02.E5;C06.E1 | {"ledger": "paid_filed", "date_precision": "day"} | supporting | context |  | filed grant to Alignment Research Center, not METR; kept on ARC and bound as context for the pooled-route and ARC-provenance elements; ledger typed |
| 28 | DIFFERS | MDF | C02.E5;C06.E1 | {"ledger": "paid_filed", "date_precision": "day"} | supporting | context |  | filed grant to Alignment Research Center, not METR; kept on ARC and bound as context for the pooled-route and ARC-provenance elements; ledger typed |
| 29 | DIFFERS | MDF | C02.E5;C06.E1 | {"ledger": "paid_filed", "date_precision": "day"} | supporting | context |  | filed grant to Alignment Research Center, not METR; kept on ARC and bound as context for the pooled-route and ARC-provenance elements; ledger typed |
| 30 | DIFFERS | MDF | C02.E5;C06.E1 | {"ledger": "paid_filed", "date_precision": "day"} | supporting | context |  | filed grant to Alignment Research Center, not METR; kept on ARC and bound as context for the pooled-route and ARC-provenance elements; ledger typed |
| 31 | DIFFERS | MDF | C02.E5;C06.E1 | {"ledger": "paid_filed", "date_precision": "day"} | supporting | context |  | filed grant to Alignment Research Center, not METR; kept on ARC and bound as context for the pooled-route and ARC-provenance elements; ledger typed |
| 32 | DIFFERS | MDF | C02.E5;C06.E1 | {"ledger": "paid_filed", "date_precision": "day"} | supporting | context |  | filed grant to Alignment Research Center, not METR; kept on ARC and bound as context for the pooled-route and ARC-provenance elements; ledger typed |
| 33 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | per-year sponsor Schedule I negative versus ARC; bounded |
| 34 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | per-year sponsor Schedule I negative versus ARC; bounded |
| 35 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | per-year sponsor Schedule I negative versus ARC; bounded |
| 36 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | per-year sponsor Schedule I negative versus ARC; bounded |
| 37 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | per-year sponsor Schedule I negative versus ARC; bounded |
| 38 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | per-year sponsor Schedule I negative versus ARC; bounded |
| 39 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | per-year sponsor Schedule I negative versus ARC; bounded |
| 40 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | per-year sponsor Schedule I negative versus ARC; bounded |
| 41 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | per-year sponsor Schedule I negative versus ARC; bounded |
| 42 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | per-year sponsor Schedule I negative versus ARC; bounded |
| 43 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | per-year sponsor Schedule I negative versus ARC; bounded |
| 44 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | per-year sponsor Schedule I negative versus ARC; bounded |
| 45 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | per-year sponsor Schedule I negative versus ARC; bounded |
| 46 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | per-year sponsor Schedule I negative versus ARC; bounded |
| 47 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | per-year sponsor Schedule I negative versus ARC; bounded |
| 48 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | per-year sponsor Schedule I negative versus ARC; bounded |
| 49 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | per-year sponsor Schedule I negative versus ARC; bounded |
| 50 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | per-year sponsor Schedule I negative versus ARC; bounded |
| 51 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | per-year sponsor Schedule I negative versus ARC; bounded |
| 52 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | per-year sponsor Schedule I negative versus ARC; bounded |
| 53 | DIFFERS | MDS | C02.E3;C03.E3 | {"money_type": "", "amount_usd": "", "currency": ""} | supporting | negative |  | structural verification boundary: Schedule I carries no account-principal or adviser field; money fields cleared on a source-coverage row (the grant itself is its own MDF row) |
| 54 | DIFFERS | MDS | C02.E3;C03.E3 | {"money_type": "", "amount_usd": "", "currency": ""} | supporting | negative |  | structural verification boundary: Schedule I carries no account-principal or adviser field; money fields cleared on a source-coverage row (the grant itself is its own MDF row) |
| 55 | DIFFERS | MDS | C02.E3;C03.E3 | {"money_type": "", "amount_usd": "", "currency": ""} | supporting | negative |  | structural verification boundary: Schedule I carries no account-principal or adviser field; money fields cleared on a source-coverage row (the grant itself is its own MDF row) |
| 56 | DIFFERS | MDS | C02.E3;C03.E3 | {"money_type": "", "amount_usd": "", "currency": ""} | supporting | negative |  | structural verification boundary: Schedule I carries no account-principal or adviser field; money fields cleared on a source-coverage row (the grant itself is its own MDF row) |
| 57 | DIFFERS | MDS | C02.E3;C03.E3 | {"money_type": "", "amount_usd": "", "currency": ""} | supporting | negative |  | structural verification boundary: Schedule I carries no account-principal or adviser field; money fields cleared on a source-coverage row (the grant itself is its own MDF row) |
| 58 | DIFFERS | MDS | C02.E3;C03.E3 | {"money_type": "", "amount_usd": "", "currency": ""} | supporting | negative |  | structural verification boundary: Schedule I carries no account-principal or adviser field; money fields cleared on a source-coverage row (the grant itself is its own MDF row) |
| 59 | DIFFERS | MDS | C02.E3;C03.E3 | {"money_type": "", "amount_usd": "", "currency": ""} | supporting | negative |  | structural verification boundary: Schedule I carries no account-principal or adviser field; money fields cleared on a source-coverage row (the grant itself is its own MDF row) |
| 60 | DIFFERS | MDS | C02.E3;C03.E3 | {"money_type": "", "amount_usd": "", "currency": ""} | supporting | negative |  | structural verification boundary: Schedule I carries no account-principal or adviser field; money fields cleared on a source-coverage row (the grant itself is its own MDF row) |
| 61 | CONFIRMED | MDT | C02.E3;C02.E5 | {} | supporting | context |  | calendar closer: next unfiled sponsor return and the date it becomes available; context |
| 62 | CONFIRMED | MDT | C02.E3;C02.E5 | {} | supporting | context |  | calendar closer: next unfiled sponsor return and the date it becomes available; context |
| 63 | CONFIRMED | MDT | C02.E3;C02.E5 | {} | supporting | context |  | calendar closer: next unfiled sponsor return and the date it becomes available; context |
| 64 | CONFIRMED | MDT | C02.E3;C02.E5 | {} | supporting | context |  | calendar closer: next unfiled sponsor return and the date it becomes available; context |
| 65 | CONFIRMED | MDT | C02.E3;C02.E5 | {} | supporting | context |  | calendar closer: next unfiled sponsor return and the date it becomes available; context |
| 66 | CONFIRMED | MDS | C02.E3 | {} | supporting | context |  | route failure (TEOS 403); context |
| 67 | CONFIRMED | MDS | C02.E3;C02.E5 | {} | supporting | context |  | route note: Vanguard FY2025 XML object absent from the lake and from the IRS 05A zip at check time; rendered copy used; context |
| 68 | CONFIRMED | MDS | C02.E3 | {} | supporting | context |  | scope note, not a search: community-foundation sponsors beyond the named set are deferred to MD22/MD38; context |
