<!-- casework-review lane=research/grok-out/MD04-schmidt-sciences.csv -->

# Review of MD04 — schmidt sciences

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 d20be334a1c586cc8f657226b6a371185ea6dee4e8c725654d5cf126666113f0; goal state complete. Checked against the four saved Schmidt-entity 990-PF XMLs (46-3460261: 379 paid/50 approved groups; 20-4170342: 695/165; 99-5077186: 0/0 short year; 26-4562328: 19/3; the only METR substrings are an address and a stock name) and the live metr.org/about page. The Schmidt Sciences acknowledgment is typed as an acknowledgment with the paying legal entity unstated; client-rendered awardee search and blocked registries are context.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| 1 | CONFIRMED | MDE | C05.E3;C02.E2 | {} | primary | evidence |  | FAQ names the LLC as a 501(c)(3) subsidiary of EIN 46-3460261; kept distinct from the Fund |
| 2 | CONFIRMED | MDE | C05.E3;C02.E2 | {} | supporting | evidence |  | brand/redirect; not a separate filer |
| 3 | CONFIRMED | MDE | C05.E3;C02.E2 | {} | primary | evidence |  | Fund for Strategic Innovation EIN 46-3460261 from the filer header |
| 4 | CONFIRMED | MDE | C05.E3;C02.E2 | {} | supporting | evidence |  | Hillspire LLC identified from the Schmidt Family Foundation 990-PF contractor block; family office, not a filer |
| 5 | CONFIRMED | MDE | C05.E3;C02.E2 | {} | primary | evidence |  | Schmidt Family Foundation EIN 20-4170342 |
| 6 | CONFIRMED | MDE | C05.E3;C02.E2 | {} | supporting | evidence |  | Operating Foundation EIN 99-5077186, initial short year 2024 |
| 7 | CONFIRMED | MDE | C02.E2 | {} | supporting | context |  | Schmidt Ocean Institute is not named by METR; context only |
| 8 | DIFFERS | MDF | C02.E2 | {"payment_status": "acknowledged as a supporter; amount, date, vehicle, money type and paying legal entity not disclosed by the source"} | primary | evidence |  | metr.org/about live-checked 2026-09-16 names Schmidt Sciences among foundations; acknowledgment only; which Schmidt legal entity paid is not stated |
| 9 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | awardees search is client-rendered and returned identical HTML for three queries: route limitation, bound as context |
| 10 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | primary | negative |  | saved TY2024 990-PF for 46-3460261 rechecked locally: 379 paid and 50 approved groups, no METR/ARC grantee; the one METR substring is an address |
| 11 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | primary | negative |  | saved TY2024 990-PF for 20-4170342 rechecked locally: 695 paid and 165 approved groups, no METR/ARC grantee; METR substring is a stock name |
| 12 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | saved TY2024 990-PF for 99-5077186: initial short year with 0 grant groups; bounded but weak |
| 13 | CONFIRMED | MDS | C02.E2 | {} | primary | negative |  | saved TY2024 990-PF for 26-4562328 rechecked locally: 19 paid and 3 approved groups, none METR/ARC |
| 14 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | the LLC has no separate Nonprofit Explorer identity; locator negative |
| 15 | CONFIRMED | MDR | C05.E1;C05.E3 | {} | primary | evidence |  | Anthropic Series A page names Eric Schmidt the individual; amount undisclosed; issuer statement |
| 16 | CONFIRMED | MDR | C05.E1;C05.E3 | {} | supporting | evidence |  | archived CNBC 2025-01-21 names Hillspire as an Anthropic backer; press, amount undisclosed |
| 17 | CONFIRMED | MDS | C02.E2;C05.E1 | {} | supporting | context |  | issuer-class summary; context |
| 18 | CONFIRMED | MDS | C02.E2;C01.E5 | {} | primary | negative |  | funder-filings class summary across four EINs TY2024 with the unfiled-year blind spot |
| 19 | CONFIRMED | MDS | C02.E2 | {} | supporting | context |  | self-statements class summary; context |
| 20 | CONFIRMED | MDS | C05.E1 | {} | supporting | context |  | press class summary; context |
| 21 | CONFIRMED | MDS | C02.E2;C05.E1 | {} | supporting | context |  | archives class note; context |
| 22 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | philanthropy.org who-funds secondary aggregate (through FY2024 filings) shows no Schmidt entity; locator negative only |
| 23 | CONFIRMED | MDS | C02.E2;C05.E3 | {} | supporting | context |  | route failure (TEOS 403); context |
| 24 | CONFIRMED | MDS | C05.E3 | {} | supporting | context |  | route failure (CA SOS Incapsula); context |
