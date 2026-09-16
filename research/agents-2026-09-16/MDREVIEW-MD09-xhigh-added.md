<!-- casework-review lane=research/rerun/MD09-xhigh-added.csv -->

# Review of MD09 — xhigh added

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 63d4deb0a571f6f9fd81c72fa5a436e617974a56e65e8f9bd729a50f1ac93604; goal state complete. xhigh re-run adjudication (PLAN A4/A4.1): rows of the xhigh run of MD09 were matched to the promoted medium run by content (url, prefix, money type, amount, date, subject), never by row number. Rows matching a promoted fact stay on the medium row. This file holds the rows with no medium counterpart (X-prefixed) and the candidate corrections (C-prefixed, superseding the medium row where the re-run cleared a stray money type or amount on an aggregate, entity or negative row, or filled a missing date); every added fact was read by the reviewer against the row's saved primary reference and bound by role; restatements of already promoted facts are context; medium rows with no xhigh counterpart stand as promoted.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| X18 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | context |  | 404 / restated negative (MDS0236, MDS0244) / route shells; context |
| X39 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | context |  | 404 / restated negative (MDS0236, MDS0244) / route shells; context |
| X51 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | context |  | 404 / restated negative (MDS0236, MDS0244) / route shells; context |
| X52 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | context |  | 404 / restated negative (MDS0236, MDS0244) / route shells; context |
| X54 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | context |  | 404 / restated negative (MDS0236, MDS0244) / route shells; context |
| X55 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | context |  | 404 / restated negative (MDS0236, MDS0244) / route shells; context |
| X58 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | context |  | 404 / restated negative (MDS0236, MDS0244) / route shells; context |
| X59 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | negative |  | bounded negative (FLI TY2024 Schedule I no ARC/METR; press states no SFF grant amount; SVCF Schedule I names no adviser or account principal) |
| X60 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | negative |  | bounded negative (FLI TY2024 Schedule I no ARC/METR; press states no SFF grant amount; SVCF Schedule I names no adviser or account principal) |
| X61 | CONFIRMED | MDS | C02.E2;C02.E5 | {} | supporting | negative |  | bounded negative (FLI TY2024 Schedule I no ARC/METR; press states no SFF grant amount; SVCF Schedule I names no adviser or account principal) |
| C20 | CONFIRMED | MDF | C02.E2;C02.E5 | {} | supporting | evidence |  | second $10,000 SFF-spec ledger line dated 2024-07-24 (the 2024-07-23 line is MDF0051); together they match the $20,000 speculation annotation; paid_grant, not summed |
| C30 | CONFIRMED | MDF | C02.E2;C02.E5 | {} | supporting | evidence |  | Founders Pledge Inc TY2024 Schedule I filed grant of $147,000 to Alignment Research Center (EIN 86-3605182), a different legal entity from METR; the $184,000 METR line is MDF0058 |
