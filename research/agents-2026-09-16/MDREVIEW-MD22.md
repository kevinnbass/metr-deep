<!-- casework-review lane=research/grok-out/MD22-intermediary-returns.csv -->

# Review of MD22 — intermediary returns

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 61225511e2c11dd6dee2677abb350bb20f5b8e70fc895d217a9f114f67c4c313; goal state complete. Checked against the lane's saved intermediary and sponsor XMLs (Every Org 990-PF TY2021-TY2024, EV USA 990 FY2021-FY2025, Founders Pledge 990-PF TY2021-TY2023 and 990 TY2024, Vanguard FY2021-FY2024, SVCF TY2021-TY2023, Longview USA TY2024) and Companies House / findthatcharity records. Filed METR grants already promoted elsewhere are context; payer-into-intermediary Schedule B lines from 990-PF filers are evidence; intermediaries' own revenue totals are retyped out of the money ledger; calendar rows are context.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| 1 | CONFIRMED | MDF | C02.E3;C02.E5;C06.E1 | {} | supporting | context |  | same filed METR grant already promoted (MD09/MD11); context so one event is one row |
| 2 | CONFIRMED | MDF | C02.E3;C02.E5;C06.E1 | {} | supporting | context |  | same filed METR grant already promoted (MD09/MD11); context so one event is one row |
| 3 | CONFIRMED | MDF | C02.E3;C02.E5;C06.E1 | {} | supporting | context |  | same filed METR grant already promoted (MD09/MD11); context so one event is one row |
| 4 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | negative |  | per-year intermediary or sponsor return with no METR line; ARC-only lines kept on ARC; bounded |
| 5 | CONFIRMED | MDS | C02.E3;C02.E5;C06.E1 | {} | supporting | negative |  | per-year intermediary or sponsor return with no METR line; ARC-only lines kept on ARC; bounded |
| 6 | CONFIRMED | MDS | C02.E3;C02.E5;C06.E1 | {} | supporting | negative |  | per-year intermediary or sponsor return with no METR line; ARC-only lines kept on ARC; bounded |
| 7 | CONFIRMED | MDS | C02.E3;C02.E5;C06.E1 | {} | supporting | negative |  | per-year intermediary or sponsor return with no METR line; ARC-only lines kept on ARC; bounded |
| 8 | CONFIRMED | MDS | C02.E3;C02.E5;C06.E1 | {} | supporting | negative |  | per-year intermediary or sponsor return with no METR line; ARC-only lines kept on ARC; bounded |
| 9 | CONFIRMED | MDS | C02.E3;C06.E1 | {} | supporting | negative |  | per-year intermediary or sponsor return with no METR line; ARC-only lines kept on ARC; bounded |
| 10 | CONFIRMED | MDS | C02.E3;C06.E1 | {} | supporting | negative |  | per-year intermediary or sponsor return with no METR line; ARC-only lines kept on ARC; bounded |
| 11 | CONFIRMED | MDS | C02.E3;C06.E1 | {} | supporting | negative |  | per-year intermediary or sponsor return with no METR line; ARC-only lines kept on ARC; bounded |
| 12 | CONFIRMED | MDS | C02.E3;C06.E1 | {} | supporting | negative |  | per-year intermediary or sponsor return with no METR line; ARC-only lines kept on ARC; bounded |
| 13 | CONFIRMED | MDS | C02.E3;C06.E1 | {} | supporting | negative |  | FY2021 short period filed under the CEA USA name; METR not formed; bounded |
| 14 | CONFIRMED | MDS | C02.E3;C06.E1 | {} | supporting | negative |  | per-year intermediary or sponsor return with no METR line; ARC-only lines kept on ARC; bounded |
| 15 | CONFIRMED | MDS | C02.E3;C06.E1 | {} | supporting | negative |  | per-year intermediary or sponsor return with no METR line; ARC-only lines kept on ARC; bounded |
| 16 | CONFIRMED | MDS | C02.E3;C06.E1 | {} | supporting | negative |  | per-year intermediary or sponsor return with no METR line; ARC-only lines kept on ARC; bounded |
| 17 | CONFIRMED | MDS | C02.E3;C06.E1 | {} | supporting | negative |  | EIN 33-3737390 has no e-file in the 2022-2026 indexes; distinct from EV USA; bounded |
| 18 | CONFIRMED | MDS | C02.E3;C06.E1 | {} | supporting | negative |  | per-year intermediary or sponsor return with no METR line; ARC-only lines kept on ARC; bounded |
| 19 | CONFIRMED | MDS | C02.E3;C06.E1 | {} | supporting | negative |  | per-year intermediary or sponsor return with no METR line; ARC-only lines kept on ARC; bounded |
| 20 | CONFIRMED | MDS | C02.E3;C06.E1 | {} | supporting | negative |  | per-year intermediary or sponsor return with no METR line; ARC-only lines kept on ARC; bounded |
| 21 | CONFIRMED | MDS | C02.E3;C06.E1 | {} | supporting | negative |  | per-year intermediary or sponsor return with no METR line; ARC-only lines kept on ARC; bounded |
| 22 | CONFIRMED | MDS | C02.E3;C06.E1 | {} | supporting | negative |  | per-year intermediary or sponsor return with no METR line; ARC-only lines kept on ARC; bounded |
| 23 | CONFIRMED | MDS | C02.E3;C06.E1 | {} | supporting | negative |  | per-year intermediary or sponsor return with no METR line; ARC-only lines kept on ARC; bounded |
| 24 | CONFIRMED | MDS | C02.E3;C06.E1 | {} | supporting | negative |  | per-year intermediary or sponsor return with no METR line; ARC-only lines kept on ARC; bounded |
| 25 | DIFFERS | MDF | C06.E1 | {"money_type": "", "ledger": ""} | supporting | context |  | Founders Pledge Inc's own TY2024 revenue; not a funding event to METR; money_type cleared; context |
| 26 | CONFIRMED | MDS | C06.E1 | {} | primary | negative |  | FP TY2024 Schedule B RESTRICTED; named payers unrecoverable; boundary |
| 27 | CONFIRMED | MDF | C02.E5;C06.E1 | {} | supporting | evidence |  | named contributor into an intermediary from a private-foundation 990-PF Schedule B (public for a 990-PF filer); payer-into-intermediary, never a payment to METR; entities unmerged |
| 28 | CONFIRMED | MDF | C02.E5;C06.E1 | {} | supporting | evidence |  | named contributor into an intermediary from a private-foundation 990-PF Schedule B (public for a 990-PF filer); payer-into-intermediary, never a payment to METR; entities unmerged |
| 29 | CONFIRMED | MDF | C02.E5;C06.E1 | {} | supporting | evidence |  | named contributor into an intermediary from a private-foundation 990-PF Schedule B (public for a 990-PF filer); payer-into-intermediary, never a payment to METR; entities unmerged |
| 30 | CONFIRMED | MDF | C06.E1 | {} | supporting | evidence |  | named contributor into an intermediary from a private-foundation 990-PF Schedule B (public for a 990-PF filer); payer-into-intermediary, never a payment to METR; entities unmerged |
| 31 | DIFFERS | MDF | C06.E1 | {"money_type": "", "ledger": ""} | supporting | context |  | intermediary's own revenue total; not a funding event; money_type cleared; context |
| 32 | CONFIRMED | MDF | C02.E5;C06.E1 | {} | supporting | evidence |  | named contributor into an intermediary from a private-foundation 990-PF Schedule B (public for a 990-PF filer); payer-into-intermediary, never a payment to METR; entities unmerged |
| 33 | DIFFERS | MDF | C06.E1 | {"money_type": "", "ledger": ""} | supporting | context |  | intermediary's own revenue total; not a funding event; money_type cleared; context |
| 34 | DIFFERS | MDF | C06.E1 | {"money_type": "", "ledger": ""} | supporting | context |  | intermediary's own revenue total; not a funding event; money_type cleared; context |
| 35 | CONFIRMED | MDF | C02.E5;C06.E1 | {} | supporting | context |  | Good Ventures FY2024 grant to EV USA; held from lineage as context; representative line; context |
| 36 | CONFIRMED | MDP | C02.E5;C06.E1 | {} | supporting | evidence |  | metr.org/donate states every.org re-grants batched unrestricted donations; processor description |
| 37 | CONFIRMED | MDE | C06.E1 | {} | supporting | evidence |  | EV Foundation (UK) charity 1149828 / company 07962181 via the findthatcharity locator; distinct from EV USA |
| 38 | CONFIRMED | MDS | C06.E1 | {} | supporting | negative |  | Companies House overview has no grant list; bounded |
| 39 | CONFIRMED | MDE | C02.E5;C06.E1 | {} | supporting | context |  | Longview Inc. Ltd already promoted by MD10; context |
| 40 | CONFIRMED | MDS | C06.E1 | {} | supporting | context |  | scanned accounts without text; route limitation; context |
| 41 | CONFIRMED | MDE | C06.E1 | {} | supporting | evidence |  | Founders Pledge Ltd UK company 08565148, distinct from Founders Pledge Inc |
| 42 | CONFIRMED | MDS | C06.E1 | {} | supporting | context |  | Charity Commission JS search; context |
| 43 | CONFIRMED | MDT | C06.E1 | {} | supporting | context |  | fiscal-year basis and next unfiled return; calendar closer; context |
| 44 | CONFIRMED | MDT | C06.E1 | {} | supporting | context |  | fiscal-year basis and next unfiled return; calendar closer; context |
| 45 | CONFIRMED | MDT | C06.E1 | {} | supporting | context |  | fiscal-year basis and next unfiled return; calendar closer; context |
| 46 | CONFIRMED | MDT | C06.E1 | {} | supporting | context |  | fiscal-year basis and next unfiled return; calendar closer; context |
| 47 | CONFIRMED | MDT | C06.E1 | {} | supporting | context |  | fiscal-year basis and next unfiled return; calendar closer; context |
| 48 | CONFIRMED | MDT | C06.E1 | {} | supporting | context |  | fiscal-year basis and next unfiled return; calendar closer; context |
| 49 | CONFIRMED | MDT | C06.E1 | {} | supporting | context |  | fiscal-year basis and next unfiled return; calendar closer; context |
| 50 | CONFIRMED | MDS | C06.E1 | {} | supporting | context |  | route failure or scope note, not a content negative; context |
| 51 | CONFIRMED | MDS | C06.E1 | {} | supporting | context |  | route failure or scope note, not a content negative; context |
| 52 | CONFIRMED | MDS | C06.E1 | {} | supporting | context |  | route failure or scope note, not a content negative; context |
| 53 | CONFIRMED | MDS | C02.E5;C06.E1 | {} | supporting | context |  | route failure or scope note, not a content negative; context |
| 54 | CONFIRMED | MDS | C06.E1 | {} | supporting | context |  | route failure or scope note, not a content negative; context |
| 55 | CONFIRMED | MDS | C06.E1 | {} | supporting | negative |  | bounded negative as stated |
| 56 | CONFIRMED | MDS | C06.E1 | {} | supporting | context |  | route failure or scope note, not a content negative; context |
| 57 | CONFIRMED | MDS | C06.E1 | {} | supporting | context |  | route failure or scope note, not a content negative; context |
| 58 | CONFIRMED | MDS | C06.E1 | {} | supporting | context |  | route failure or scope note, not a content negative; context |
| 59 | CONFIRMED | MDS | C06.E1 | {} | supporting | negative |  | bounded negative as stated |
| 60 | CONFIRMED | MDS | C02.E3;C06.E1 | {} | primary | negative |  | METR Schedule B RESTRICTED; boundary |
| 61 | CONFIRMED | MDS | C06.E1 | {} | supporting | context |  | route failure or scope note, not a content negative; context |
| 62 | CONFIRMED | MDS | C06.E1 | {} | supporting | negative |  | index_2026 has no TY2025 returns for FP, Longview USA, Every Org, CEA Inc or SVCF; calendar-bounded negative |
