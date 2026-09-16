<!-- casework-review lane=research/rerun/MD12-xhigh-added.csv -->

# Review of MD12 — xhigh added

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 df6cc64192493ab38919c1349387a2f3a59cfaf6da983354c2a64e7e109485f5; goal state complete. xhigh re-run adjudication (PLAN A4/A4.1): rows of the xhigh run of MD12 were matched to the promoted medium run by content (url, prefix, money type, amount, date, subject), never by row number. Rows matching a promoted fact stay on the medium row. This file holds the rows with no medium counterpart (X-prefixed) and the candidate corrections (C-prefixed, superseding the medium row where the re-run cleared a stray money type or amount on an aggregate, entity or negative row, or filled a missing date); every added fact was read by the reviewer against the row's saved primary reference and bound by role; restatements of already promoted facts are context; medium rows with no xhigh counterpart stand as promoted.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| X4 | CONFIRMED | MDT | C02.E3;C06.E1 | {} | primary | evidence |  | ARC FY2024 Schedule N DistributionDt 2024-04-30 for the program spin-off to METR (successor EIN 99-1219864); the same disposition as Schedule I, not a second transfer |
| X9 | CONFIRMED | MDT | C02.E3;C06.E1 | {} | supporting | evidence |  | ARC Part III narrative states the spin-out completed in May; kept distinct from the Schedule N date |
| X37 | CONFIRMED | MDS | C02.E3;C06.E1 | {} | supporting | negative |  | bounded negative: METR's own short-year FY2024 990 has no Schedule I |
| C14 | CONFIRMED | MDF | C02.E3;C06.E1 | {} | supporting | evidence | MDF0068 | correction: ARC Schedule A gift totals with the stray filed_grant money type cleared; an unnamed aggregate carries no money type |
