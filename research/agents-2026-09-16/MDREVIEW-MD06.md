<!-- casework-review lane=research/grok-out/MD06-lacentra-astralis-expa.csv -->

# Review of MD06 — lacentra astralis expa

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 52214cf84cbfe3f6bdaa8f0d3061c8699bb1366270f72194d2114d42b5e130b9; goal state complete. Checked against the lane's saved LaCentra-Sumerlin 990-PF XMLs (FYE Nov 2021-2024: 59/19/52/46 paid groups, 0 METR/ARC/Frontier strings), Expa.org 990-PF XMLs (TY2021-2024: 1/2/3/1 groups, 0), the Companies House record and accounts for UK company 15917880, the foundation sites, the saved Wayback captures and the live metr.org pages; the 'LaCentra-Sumerlin Foundation Frontier Fund' alt text is confirmed in the saved funding-update HTML. Acknowledgment rows are typed as acknowledgments; none-found rows typed MDF are retargeted to MDS; blocked registries are context.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| 1 | CONFIRMED | MDE | C02.E2 | {} | primary | evidence |  | LA CENTRA-SUMERLIN FOUNDATION EIN 77-0416683 from the saved FYE Nov 2024 990-PF |
| 2 | CONFIRMED | MDE | C02.E2 | {} | supporting | evidence |  | EO BMF CA row for 770416683; private non-operating foundation |
| 3 | CONFIRMED | MDE | C02.E2 | {} | primary | evidence |  | Stiftelsen Astralis org.nr 802482-2317 from the foundation's own site footer |
| 4 | CONFIRMED | MDE | C02.E2 | {} | primary | evidence |  | UK company 15917880 from Companies House; company limited by guarantee, not a charity |
| 5 | CONFIRMED | MDE | C02.E2 | {} | primary | evidence |  | EXPAORG EIN 83-2856275 from the saved TY2024 990-PF |
| 6 | CONFIRMED | MDE | C02.E2 | {} | supporting | context |  | expa.com studio kept distinct from the Expa.org foundation; context |
| 7 | DIFFERS | MDR | C02.E2 | {"relationship_type": "acknowledged supporter on the recipient's own list; amount, date, vehicle and purpose not disclosed"} | primary | evidence |  | metr.org/about live-checked 2026-09-16 names LaCentra-Sumerlin Foundation; acknowledgment typed |
| 8 | DIFFERS | MDR | C02.E2 | {"relationship_type": "acknowledged supporter on the recipient's own list; amount, date, vehicle and purpose not disclosed"} | primary | evidence |  | metr.org/about names Astralis Foundation; acknowledgment typed |
| 9 | DIFFERS | MDR | C02.E2 | {"relationship_type": "acknowledged supporter on the recipient's own list; amount, date, vehicle and purpose not disclosed"} | primary | evidence |  | metr.org/about names Expa.org; acknowledgment typed |
| 10 | CONFIRMED | MDT | C02.E2 | {} | supporting | evidence |  | funding-update image alt names 'LaCentra-Sumerlin Foundation Frontier Fund'; a sub-fund of the same EIN per lcsf.org |
| 11 | DIFFERS | MDS | C02.E2 | {"result": "none found in https://www.lcsf.org/frontier as of 2026-09-16T05:40:32Z"} | supporting | negative |  | retargeted from MDF to MDS: a none-found row is source coverage |
| 12 | DIFFERS | MDS | C02.E2 | {"result": "none found in https://astralisfoundation.org/ as of 2026-09-16T05:40:36Z"} | supporting | negative |  | retargeted from MDF to MDS |
| 13 | DIFFERS | MDS | C02.E2 | {"result": "none found in https://www.expa.org/ as of 2026-09-16T05:35:24Z"} | supporting | negative |  | retargeted from MDF to MDS |
| 14 | DIFFERS | MDS | C02.E2;C01.E5 | {"money_type": ""} | primary | negative |  | four saved LaCentra 990-PF XMLs FYE Nov 2021-2024 rechecked locally: 59/19/52/46 paid groups, 0 METR/ARC/Frontier strings; money_type cleared on a negative |
| 15 | DIFFERS | MDS | C02.E2;C01.E5 | {"money_type": ""} | primary | negative |  | four saved Expa 990-PF XMLs TY2021-2024 rechecked locally: 1/2/3/1 paid groups, 0 METR/ARC; money_type cleared |
| 16 | CONFIRMED | MDS | C02.E2 | {} | primary | negative |  | Companies House accounts YE 2025-08-31 saved; no grants-paid detail, P&L not filed; bounded |
| 17 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | ProPublica search returns three near-miss US filers, none the METR-named Astralis; locator negative |
| 18 | CONFIRMED | MDT | C02.E2;C09.E1 | {} | supporting | evidence |  | Wayback 2025-12-16 about capture names La Centra-Sumerlin; appearance not transaction |
| 19 | CONFIRMED | MDT | C02.E2;C09.E1 | {} | supporting | evidence |  | Wayback 2025-12-07 about capture names Astralis |
| 20 | CONFIRMED | MDT | C02.E2;C09.E1 | {} | supporting | evidence |  | Wayback 2025-12-07 about capture names Expa.org |
| 21 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | filing route exists; FYE Nov 2025 return not yet posted; calendar; context |
| 22 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | filing route exists; TY2025 not yet posted; calendar; context |
| 23 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | foreign foundation plus UK company: no US 990 route; bounded with the registry blind spots stated |
| 24 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | route failure (TEOS 403); context |
| 25 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | route failure (legacy RCT 404); context |
| 26 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | route failure (JS portal); context |
| 27 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | Charity Commission search UI is JS; no result card; context |
| 28 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | commercial Swedish registry mirror blocked; context |
| 29 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | Länsstyrelsen path 404; context |
| 30 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | astralisfoundation.org has no grants page (404); bounded |
| 31 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | lcsf.org grants page names no grantees; bounded |
| 32 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | expa.org one-line site; bounded |
| 33 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | primary | negative |  | LaCentra funder-filings class summary with the post-FYE blind spot |
| 34 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | primary | negative |  | Expa funder-filings class summary |
| 35 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | Astralis UK accounts summary; grants-received not grants-paid; bounded |
| 36 | CONFIRMED | MDE | C02.E2 | {} | supporting | evidence |  | lcsf.org self-description: three funds including the Frontier Fund |
