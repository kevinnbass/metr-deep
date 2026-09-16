<!-- casework-review lane=research/rerun/MD01-xhigh-added.csv -->

# Review of MD01 — xhigh added

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 039e5313f59feea81a284eea85bed9789ebf90b195d69c01c6efa3c59a534987; goal state complete. xhigh re-run adjudication (PLAN A4/A4.1): rows of the xhigh run of MD01 were matched to the promoted medium run by content (url, prefix, money type, amount, date, subject), never by row number. Rows matching a promoted fact stay on the medium row. This file holds the rows with no medium counterpart (X-prefixed) and the candidate corrections (C-prefixed, superseding the medium row where the re-run cleared a stray money type or amount on an aggregate, entity or negative row, or filled a missing date); every added fact was read by the reviewer against the row's saved primary reference and bound by role; restatements of already promoted facts are context; medium rows with no xhigh counterpart stand as promoted.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| X6 | CONFIRMED | MDS | C02.E4 | {} | supporting | negative |  | bounded negative (issuer annual report is an activities report stating a $10 million 2024 budget, not a financial statement; Schedule A names no substantial contributor; no predecessor or parent stated; CA professional-fundraiser CSV) |
| X12 | CONFIRMED | MDS | C02.E3;C02.E4 | {} | supporting | negative |  | bounded negative (issuer annual report is an activities report stating a $10 million 2024 budget, not a financial statement; Schedule A names no substantial contributor; no predecessor or parent stated; CA professional-fundraiser CSV) |
| X17 | CONFIRMED | MDS | C02.E4 | {} | supporting | negative |  | bounded negative (issuer annual report is an activities report stating a $10 million 2024 budget, not a financial statement; Schedule A names no substantial contributor; no predecessor or parent stated; CA professional-fundraiser CSV) |
| X25 | CONFIRMED | MDS | C02.E4 | {} | supporting | negative |  | bounded negative (issuer annual report is an activities report stating a $10 million 2024 budget, not a financial statement; Schedule A names no substantial contributor; no predecessor or parent stated; CA professional-fundraiser CSV) |
| X28 | CONFIRMED | MDS | C02.E4 | {} | supporting | context |  | secondary locator / proxy route failure; context |
| X29 | CONFIRMED | MDS | C02.E4 | {} | supporting | context |  | secondary locator / proxy route failure; context |
| C1 | CONFIRMED | MDF | C02.E4;C01.E3 | {} | primary | evidence | MDF0031 | correction: METR FY2024 total revenue line (CYTotalRevenueAmt 13,639,155) re-typed with money_type cleared; the superseded medium row carried the same amount typed filed_grant with the contributions-line quote; CYContributionsGrantsAmt 13,603,035 is the separate contributions line |
| C11 | CONFIRMED | MDF | C02.E3;C02.E4 | {} | primary | evidence | MDF0035 | correction: AllOtherContributionsAmt 9,101,611 is the recipient's own unnamed-contributions aggregate; money_type cleared so it is never summed with funder filed grants |
