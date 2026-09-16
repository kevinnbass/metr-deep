<!-- casework-review lane=research/grok-out/MD18-metr-canary-commitment.csv -->

# Review of MD18 — metr canary commitment

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 5c5a8a30ed548ece02196fe0274e0387abf963a0aa6ece658f15237c7471bc6b; goal state complete. Checked against the saved METR blog and X post (via fxtwitter), the saved GreaterWrong comment, the METR FY2024 990 XML, and the saved TED Foundation / Valhalla / High Tide / Founders Pledge / SVCF / Vanguard filings. METR-side Canary statements are evidence; no filing shows a Canary-attributed payment into METR; the FASB 117 note is retargeted from MDF to MDP; window propositions match MD14. Re-pinned after a cosmetic rewrite.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| A01 | CONFIRMED | MDF | C06.E2 | {} | primary | evidence |  | saved blog verified; METR-side $17M commitment; MD16 A02 is the same statement, both lanes own it; keep as evidence primary for C06.E2 (MD18 is the METR-side lane) |
| A02 | CONFIRMED | MDF | C06.E2 | {} | supporting | evidence |  | X post 1844005567532245136 via fxtwitter mirror: '$17M in new funding'; same-day restatement; evidence supporting |
| A03 | CONFIRMED | MDF | C06.E2 | {} | primary | evidence |  | Barnes 2025-09-28 restatement; saved GreaterWrong comment verified; amount_usd left blank because 'a bit under $16m' is not an integer |
| B01 | CONFIRMED | MDS | C06.E1 | {} | primary | negative |  | bounded: no Canary-attributed line on the FY2024 return / FY2025 not posted |
| B02 | CONFIRMED | MDS | C06.E1 | {} | supporting | negative |  | bounded: no Canary-attributed line on the FY2024 return / FY2025 not posted |
| B03 | CONFIRMED | MDS | C06.E1 | {} | primary | negative |  | TED Foundation 990-PF Part XV has no METR/RAND/Canary grant (consistent with the FAQ that TED does not fund grantees) |
| B04 | CONFIRMED | MDS | C06.E1 | {} | primary | negative |  | TED Foundation 990-PF Part XV has no METR/RAND/Canary grant (consistent with the FAQ that TED does not fund grantees) |
| B05 | CONFIRMED | MDS | C06.E1 | {} | primary | negative |  | TED Foundation 990-PF Part XV has no METR/RAND/Canary grant (consistent with the FAQ that TED does not fund grantees) |
| B06 | CONFIRMED | MDS | C06.E1 | {} | primary | negative |  | Valhalla $10,000,000 to RAND for Project Canary; a payment to RAND, not METR; the lineage/S0 context already holds it; bound as negative for 'payment into METR' |
| B07 | CONFIRMED | MDS | C06.E1 | {} | primary | negative |  | High Tide $333,334 to RAND; same treatment |
| B08 | CONFIRMED | MDS | C06.E1 | {} | primary | negative |  | the filed METR grant exists (promoted by MD09/MD11) but its purpose does not name Canary; bounded negative for Canary attribution |
| B09 | CONFIRMED | MDS | C06.E1 | {} | primary | negative |  | the filed METR grant exists (promoted by MD09/MD11) but its purpose does not name Canary; bounded negative for Canary attribution |
| B10 | CONFIRMED | MDS | C06.E1 | {} | primary | negative |  | the filed METR grant exists (promoted by MD09/MD11) but its purpose does not name Canary; bounded negative for Canary attribution |
| C01 | DIFFERS | MDP | C06.E2 | {"money_type": ""} | primary | evidence |  | FY2024 return does not follow FASB 117 net-asset split; DonorRstrOrQuasiEndowmentsInd 0; restricted-revenue treatment of Canary not visible; correctly bounded; MDF row without amount retargeted to MDP |
| C02 | CONFIRMED | MDS | C06.E2 | {} | supporting | context |  | FY2025 return calendar closer; context |
| D01 | CONFIRMED | MDP | C01.E3 | {} | primary | evidence |  | Canary METR-share commitment is outside the Feb-Aug 2026 window; consistent with MD14 C06 |
| D02 | CONFIRMED | MDP | C01.E3 | {} | supporting | evidence |  | restatement also outside the window; consistent with MD14 C07 |
| E01 | CONFIRMED | MDS | C06.E2 | {} | supporting | negative |  | Audacious page no share; bounded |
| E02 | CONFIRMED | MDS | C06.E1 | {} | supporting | negative |  | bounded negative as stated |
| E03 | CONFIRMED | MDS | C06.E1 | {} | supporting | context |  | route failure or scope note, not a content negative; context |
| E04 | CONFIRMED | MDS | C06.E1 | {} | supporting | context |  | route failure or scope note, not a content negative; context |
| E05 | CONFIRMED | MDS | C06.E1 | {} | supporting | context |  | route failure or scope note, not a content negative; context |
| E06 | CONFIRMED | MDS | C06.E1 | {} | supporting | negative |  | bounded negative as stated |
| E07 | CONFIRMED | MDS | C06.E2 | {} | supporting | negative |  | about page no share restatement; bounded |
| E08 | CONFIRMED | MDS | C06.E2;C01.E3 | {} | supporting | negative |  | funding update no share restatement; bounded |
