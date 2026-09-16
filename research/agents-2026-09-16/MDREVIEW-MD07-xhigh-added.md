<!-- casework-review lane=research/rerun/MD07-xhigh-added.csv -->

# Review of MD07 — xhigh added

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 74fa74cc4d8b6430f0f4f52ae9ae651b2a20b75311942307f72f215625869fc6; goal state complete. xhigh re-run adjudication (PLAN A4/A4.1): rows of the xhigh run of MD07 were matched to the promoted medium run by content (url, prefix, money type, amount, date, subject), never by row number. Rows matching a promoted fact stay on the medium row. This file holds the rows with no medium counterpart (X-prefixed) and the candidate corrections (C-prefixed, superseding the medium row where the re-run cleared a stray money type or amount on an aggregate, entity or negative row, or filled a missing date); every added fact was read by the reviewer against the row's saved primary reference and bound by role; restatements of already promoted facts are context; medium rows with no xhigh counterpart stand as promoted.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| X4 | CONFIRMED | MDT | C02.E2 | {} | supporting | evidence |  | dated Wayback capture 2026-06-01: about page names four individuals and does not yet contain the 'individuals from Jane Street' wording |
| X7 | CONFIRMED | MDE | C05.E3 | {} | supporting | context |  | entity-separation note from a public court exhibit (natural-person purchaser on the same FTX-estate list as Jane Street Global Trading, LLC); not a METR supporter fact; context only |
| X8 | CONFIRMED | MDR | C05.E3 | {} | supporting | context |  | entity-separation note from a public court exhibit (natural-person purchaser on the same FTX-estate list as Jane Street Global Trading, LLC); not a METR supporter fact; context only |
| X12 | CONFIRMED | MDR | C05.E1;C05.E3 | {} | supporting | evidence |  | Anthropic Series H issuer release names Jane Street among investors (amount undisclosed); a firm investment is not a donation by an individual and is never merged with METR's unnamed class |
| X13 | CONFIRMED | MDP | C05.E1;C05.E3 | {} | supporting | evidence |  | Anthropic Series H issuer release names Jane Street among investors (amount undisclosed); a firm investment is not a donation by an individual and is never merged with METR's unnamed class |
| X20 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | 404 / route failures (janestreet.com/giving, USAspending 422/502, CA RCT 404, WSJ paywall); context |
| X30 | CONFIRMED | MDS | C02.E2;C05.E3 | {} | supporting | negative |  | bounded negative: no Anthropic-as-filer EDGAR document naming Jane Street; no Jane Street firm foundation locatable in ProPublica |
| X31 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | 404 / route failures (janestreet.com/giving, USAspending 422/502, CA RCT 404, WSJ paywall); context |
| X32 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | 404 / route failures (janestreet.com/giving, USAspending 422/502, CA RCT 404, WSJ paywall); context |
| X33 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | 404 / route failures (janestreet.com/giving, USAspending 422/502, CA RCT 404, WSJ paywall); context |
| X34 | CONFIRMED | MDS | C02.E2;C05.E3 | {} | supporting | negative |  | bounded negative: no Anthropic-as-filer EDGAR document naming Jane Street; no Jane Street firm foundation locatable in ProPublica |
