<!-- casework-review lane=research/rerun/MD21-xhigh-added.csv -->

# Review of MD21 — xhigh added

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 f53eb2a6c13647e40a8f0f0328db8d8e251fc4e0f249b448692fc3cd54879df3; goal state complete. xhigh re-run adjudication (PLAN A4/A4.1): rows of the xhigh run of MD21 were matched to the promoted medium run by content (url, prefix, money type, amount, date, subject), never by row number. Rows matching a promoted fact stay on the medium row. This file holds the rows with no medium counterpart (X-prefixed) and the candidate corrections (C-prefixed, superseding the medium row where the re-run cleared a stray money type or amount on an aggregate, entity or negative row, or filled a missing date); every added fact was read by the reviewer against the row's saved primary reference and bound by role; restatements of already promoted facts are context; medium rows with no xhigh counterpart stand as promoted.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| XA11 | CONFIRMED | MDS | C06.E3 | {} | supporting | negative |  | bounded negative: SAM.gov SGS legal-name query returns only OFAC exclusion false positives; AusTender keyword search over-broad with no METR legal-name award on the first page |
| XC04 | CONFIRMED | MDS | C06.E3 | {} | supporting | context | MDS0466 | correction: the medium none-found on CanadaBuys (MDS0466) is recast as a bounded retrieval failure because the saved primary is an unfiltered tender table |
| XC06 | CONFIRMED | MDS | C06.E3 | {} | supporting | negative |  | bounded negative: SAM.gov SGS legal-name query returns only OFAC exclusion false positives; AusTender keyword search over-broad with no METR legal-name award on the first page |
