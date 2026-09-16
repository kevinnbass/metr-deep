<!-- casework-review lane=research/grok-out/MD05-sijbrandij-foundation.csv -->

# Review of MD05 — sijbrandij foundation

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 68d92997b252954462a634c716205dcdeab092b4e1011bc2cef6dd4b58e27001; goal state complete. Checked against the five saved Sijbrandij Foundation 990-PF XMLs TY2020-TY2024 (paid totals 0 / 5000000 / 7395162 / 10790127 / 5435593; approved-for-future 0; 0 METR/ARC strings) and the live metr.org pages. The GitLab Foundation entity row has its money figures moved out of the money columns; identity and calendar rows are context.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| MD05-001 | CONFIRMED | MDP | C02.E2 | {} | supporting | evidence |  | named on metr.org/about (live-checked 2026-09-16); acknowledgment without amount |
| MD05-002 | CONFIRMED | MDP | C02.E2 | {} | supporting | evidence |  | named in the 2026-08-14 funding update thank-you; the row correctly separates the thank-you from the approximately $71M sentence |
| MD05-003 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | foundation grants page saved; no METR; bounded |
| MD05-004 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | foundation site pages saved; no METR; bounded |
| MD05-005 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | primary | negative |  | saved TY2024 990-PF rechecked locally: paid 5435593, approved-for-future 0, 0 METR/ARC strings |
| MD05-006 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | primary | negative |  | saved TY2023 990-PF rechecked locally: paid 10790127, future 0, 0 METR/ARC |
| MD05-007 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | primary | negative |  | saved TY2022 990-PF rechecked locally: paid 7395162, future 0, 0 METR/ARC |
| MD05-008 | CONFIRMED | MDS | C02.E2 | {} | primary | negative |  | saved TY2021 990-PF rechecked locally: paid 5000000, future 0, 0 METR/ARC |
| MD05-009 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | saved TY2020 990-PF rechecked locally: paid 0, future 0 |
| MD05-010 | CONFIRMED | MDE | C02.E2 | {} | primary | evidence |  | legal name and EIN 85-4270305 from the saved TY2024 XML |
| MD05-011 | CONFIRMED | MDE | C02.E2 | {} | supporting | evidence |  | Delaware file 4428228, CA CT0273494 from the foundation's own bylaws page; not from a live registry |
| MD05-012 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | DonorAdvisedFundInd 0 on the TY2024 return; bounded as stated |
| MD05-013 | DIFFERS | MDE | C02.E2 | {"money_type": "", "amount_usd": "", "payment_status": "", "relationship_type": "990-PF grantee of the Sijbrandij Foundation (TY2023 four lines of 1675000; TY2022 one line of 4000000)"} | supporting | context |  | entity kept distinct; the money figures are moved out of an entity row into the relationship note so no non-METR grant sits in a money column |
| MD05-014 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | no grant letter or restriction published; bounded |
| MD05-015 | CONFIRMED | MDP | C02.E2;C01.E3 | {} | supporting | evidence |  | amount undisclosed, so window membership cannot be decided; correctly bounded |
| MD05-016 | CONFIRMED | MDT | C02.E2;C09.E1 | {} | supporting | evidence |  | Wayback id_ 2025-12-16 about capture names the foundation; appearance date not a transaction date |
| MD05-017 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | route failure (TEOS 403); context |
| MD05-018 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | index_2026 has no TY2025 990-PF yet; calendar-bounded negative |
| MD05-019 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | May-Not-Operate list is not a registrant dump; context |
| MD05-020 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | Delaware SOS search errored; route failure; context |
| MD05-021 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | ProPublica full-text none; locator negative |
| MD05-022 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | Grantmakers.io profile none; locator negative |
| MD05-023 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | BMF is not a grant register; identity hit only; context |
| MD05-024 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | no TY2025 990-PF posted; calendar; context |
