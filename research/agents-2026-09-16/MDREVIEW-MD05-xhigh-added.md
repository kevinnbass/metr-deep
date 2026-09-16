<!-- casework-review lane=research/rerun/MD05-xhigh-added.csv -->

# Review of MD05 — xhigh added

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 a94486d336202033932805e3e327045978419bfffc01810b34e1ba3b031e9e0e; goal state complete. xhigh re-run adjudication (PLAN A4/A4.1): rows of the xhigh run of MD05 were matched to the promoted medium run by content (url, prefix, money type, amount, date, subject), never by row number. Rows matching a promoted fact stay on the medium row. This file holds the rows with no medium counterpart (X-prefixed) and the candidate corrections (C-prefixed, superseding the medium row where the re-run cleared a stray money type or amount on an aggregate, entity or negative row, or filled a missing date); every added fact was read by the reviewer against the row's saved primary reference and bound by role; restatements of already promoted facts are context; medium rows with no xhigh counterpart stand as promoted.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| XMD05-013 | CONFIRMED | MDE | C02.E2 | {} | supporting | evidence |  | issuer label (Sijbrandij Foundation LLC og:site_name; ANBI RSIN) kept as its own row, not merged with the 990-PF filer |
| XMD05-014 | CONFIRMED | MDE | C02.E2 | {} | supporting | evidence |  | issuer label (Sijbrandij Foundation LLC og:site_name; ANBI RSIN) kept as its own row, not merged with the 990-PF filer |
| XMD05-025 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | bounded negative in ProPublica full-text and Grantmakers.io for a METR line |
| XMD05-026 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | bounded negative in ProPublica full-text and Grantmakers.io for a METR line |
| XMD05-027 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | BMF identity hit / no FY2025 filing yet; context |
| XMD05-028 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | BMF identity hit / no FY2025 filing yet; context |
| CMD05-016 | CONFIRMED | MDE | C02.E2 | {} | supporting | evidence | MDE0012 | correction: GitLab Foundation entity row with the paid_grant amount cleared; the amounts belong on the funding-event rows, an entity row carries no money type |
