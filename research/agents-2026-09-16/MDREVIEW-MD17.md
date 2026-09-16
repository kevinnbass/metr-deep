<!-- casework-review lane=research/grok-out/MD17-rand-canary-receipts.csv -->

# Review of MD17 — rand canary receipts

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 ddbe6d46fae2645ff1eb7cd13a68cc7589ed1764715c431785f3fb7b7a1ed0c9; goal state complete. Checked against the lane's saved RAND Forms 990 (FY2023-FY2025 aggregates; Schedule B RESTRICTED; Schedule I with no METR grant), the saved partner and sponsor XMLs, and the archived Open Philanthropy grant page (Wayback 20251025225511; 'Award Date: September 2025' verified in the saved capture). New evidence: Open Philanthropy's $10 million over three years to RAND in support of Canary (a commitment to RAND, not METR). Non-Canary RAND grants and lineage-held amounts are context; onward-passage propositions are evidence; every payment to RAND is explicitly not a payment to METR. The worker's second rewrite expanded quotes cosmetically; re-pinned.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| 1 | CONFIRMED | MDF | C06.E1;C06.E2 | {} | supporting | context |  | Audacious ~$38M joint commitment; MD16 A04 is the promoted RAND-side row; context |
| 2 | CONFIRMED | MDP | C06.E1;C06.E2 | {} | primary | evidence |  | RAND CAST Canary project page: Audacious named as the philanthropic commitment; no amount or term; additional discretionary support unnamed |
| 3 | CONFIRMED | MDR | C06.E1;C06.E2 | {} | supporting | evidence |  | CAST houses Canary; not a separate legal entity |
| 4 | CONFIRMED | MDP | C06.E1;C06.E2 | {} | primary | evidence |  | RAND CAST funding page: three funder lists with no amounts, dates or Canary tagging; correctly kept as names only |
| 5 | CONFIRMED | MDS | C06.E1;C06.E2 | {} | supporting | negative |  | RAND FY2023/FY2024 returns end before the Canary announcement; bounded |
| 6 | CONFIRMED | MDS | C06.E1;C06.E2 | {} | supporting | negative |  | RAND FY2023/FY2024 returns end before the Canary announcement; bounded |
| 7 | CONFIRMED | MDS | C06.E1;C06.E2 | {} | primary | negative |  | RAND FY2025 return (2024-10-01 to 2025-09-30) does not name Canary or METR; Schedule B RESTRICTED; a Canary gift would sit in AllOtherContributionsAmt 139947770 unnamed |
| 8 | CONFIRMED | MDF | C06.E1;C06.E2 | {} | supporting | context |  | Valhalla $10,000,000 to RAND for Project Canary; already held from S0/lineage (MDP0001); context |
| 9 | CONFIRMED | MDS | C06.E1;C06.E2 | {} | supporting | negative |  | Valhalla TY2023 no RAND/Canary; bounded |
| 10 | CONFIRMED | MDF | C06.E1;C06.E2 | {} | supporting | context |  | High Tide $333,334 to RAND; already held (MDP0002); context |
| 11 | CONFIRMED | MDS | C06.E1;C06.E2 | {} | supporting | negative |  | High Tide TY2023 none; bounded |
| 12 | CONFIRMED | MDS | C06.E1;C06.E2 | {} | primary | negative |  | TED Foundation 990-PFs TY2023/TY2024 have no RAND/METR/Canary grant; consistent with the FAQ |
| 13 | CONFIRMED | MDF | C06.E1;C06.E2 | {} | primary | evidence |  | NEW: archived Open Philanthropy grant page (Wayback 20251025225511, 'Award Date: September 2025' verified in the saved capture): $10 million over three years to RAND 'in support of Canary'; live Coefficient URL 404; a commitment to RAND, not to METR; payment vehicle unnamed |
| 14 | CONFIRMED | MDF | C06.E1;C06.E2 | {} | supporting | context |  | Founders Pledge $1,000,000 to RAND, purpose FUND CHARITABLE ACTIVITIES; already held from lineage (FN1369); not Canary-attributed; context |
| 15 | CONFIRMED | MDF | C06.E1;C06.E2 | {} | supporting | context |  | Gates Foundation TY2024 grant to RAND with an education/health purpose; not Canary; context for the 'named in the collective' point only |
| 16 | CONFIRMED | MDF | C06.E1;C06.E2 | {} | supporting | context |  | Gates Foundation TY2024 grant to RAND with an education/health purpose; not Canary; context for the 'named in the collective' point only |
| 17 | CONFIRMED | MDF | C06.E1;C06.E2 | {} | supporting | context |  | Gates Foundation TY2024 grant to RAND with an education/health purpose; not Canary; context for the 'named in the collective' point only |
| 18 | CONFIRMED | MDF | C06.E1;C06.E2 | {} | supporting | context |  | Gates Foundation TY2024 grant to RAND with an education/health purpose; not Canary; context for the 'named in the collective' point only |
| 19 | CONFIRMED | MDF | C06.E1;C06.E2 | {} | supporting | context |  | Gates Foundation TY2024 grant to RAND with an education/health purpose; not Canary; context for the 'named in the collective' point only |
| 20 | CONFIRMED | MDF | C06.E1;C06.E2 | {} | supporting | context |  | Gates Foundation TY2024 grant to RAND with an education/health purpose; not Canary; context for the 'named in the collective' point only |
| 21 | CONFIRMED | MDS | C06.E1;C06.E2 | {} | primary | negative |  | Gates TY2024 RAND lines: none names Canary; bounded |
| 22 | CONFIRMED | MDF | C06.E1;C06.E2 | {} | supporting | context |  | Hewlett TY2024 RAND grant for a school-district survey; not Canary; context |
| 23 | CONFIRMED | MDS | C06.E1;C06.E2 | {} | supporting | negative |  | Pew FY2025 Schedule I has no RAND line (Canary Media Inc is a different entity); bounded |
| 24 | CONFIRMED | MDS | C06.E1;C06.E2 | {} | primary | negative |  | Skoll TY2024 990-PF (157 groups) has no RAND/Canary line; bounded |
| 25 | CONFIRMED | MDF | C06.E1;C06.E2 | {} | supporting | context |  | Waking Up Foundation $250,000 to RAND, mission-language purpose; not Canary; context |
| 26 | CONFIRMED | MDS | C06.E1;C06.E2 | {} | primary | negative |  | Good Ventures FY2023/FY2024 RAND lines are all GENERAL SUPPORT; none names Canary; amounts held from lineage |
| 27 | CONFIRMED | MDS | C06.E1;C06.E2 | {} | supporting | context |  | GVF FY2025 XML not available from any route; image-only PDF; route note and calendar; context |
| 28 | CONFIRMED | MDF | C06.E1;C06.E2 | {} | supporting | context |  | NPT FY2025 $61,646,790 to RAND, purpose CULTURE & ARTS; already held from lineage (FN2519); not Canary; context |
| 29 | CONFIRMED | MDF | C06.E1;C06.E2 | {} | supporting | context |  | Fidelity FY2025 $18,202,491 to RAND, generic purpose; already held (FN2533); context |
| 30 | DIFFERS | MDF | C06.E1;C06.E2 | {"money_type": ""} | supporting | context |  | RAND Part VIII aggregate contribution lines; not a Canary amount; MDF row without an amount to a Canary line is context |
| 31 | DIFFERS | MDF | C06.E1;C06.E2 | {"money_type": ""} | supporting | context |  | RAND Part VIII aggregate contribution lines; not a Canary amount; MDF row without an amount to a Canary line is context |
| 32 | DIFFERS | MDF | C06.E1;C06.E2 | {"money_type": ""} | supporting | context |  | RAND Part VIII aggregate contribution lines; not a Canary amount; MDF row without an amount to a Canary line is context |
| 33 | CONFIRMED | MDS | C06.E1;C06.E2 | {} | primary | negative |  | RAND Schedule B RESTRICTED FY2023-FY2025; verification boundary |
| 34 | CONFIRMED | MDS | C06.E1;C06.E2 | {} | primary | negative |  | RAND Schedule I FY2023-FY2025 shows no grant to METR (FY2025: fellowship grants to individuals only); no onward passage documented |
| 35 | CONFIRMED | MDP | C06.E1;C06.E2 | {} | primary | evidence |  | onward-passage proposition: payment/commitment to RAND with no document showing passage to METR; correctly bounded |
| 36 | CONFIRMED | MDP | C06.E1;C06.E2 | {} | primary | evidence |  | onward-passage proposition: payment/commitment to RAND with no document showing passage to METR; correctly bounded |
| 37 | CONFIRMED | MDP | C06.E1;C06.E2 | {} | primary | evidence |  | onward-passage proposition: payment/commitment to RAND with no document showing passage to METR; correctly bounded |
| 38 | CONFIRMED | MDS | C06.E1;C06.E2 | {} | supporting | context |  | TEOS 403; context |
| 39 | CONFIRMED | MDS | C06.E1;C06.E2 | {} | supporting | context |  | live Coefficient grant URL 404; archived copy used; context |
| 40 | CONFIRMED | MDS | C06.E1;C06.E2 | {} | supporting | context |  | RAND annual-report path 404; context |
| 41 | CONFIRMED | MDS | C06.E1;C06.E2 | {} | supporting | negative |  | RAND giving page has no Canary ledger; bounded |
| 42 | CONFIRMED | MDS | C06.E1;C06.E2 | {} | supporting | negative |  | no 990 filer named Sea Grape Foundation located; the Dobson Foundation hit is not treated as Sea Grape; bounded |
| 43 | CONFIRMED | MDS | C06.E1;C06.E2 | {} | supporting | negative |  | no filer located for The Li Lu Humanitarian Foundation; bounded |
| 44 | CONFIRMED | MDS | C06.E1;C06.E2 | {} | supporting | negative |  | Audacious grantee page has no amount or receipt; bounded |
| 45 | CONFIRMED | MDS | C06.E1;C06.E2 | {} | supporting | negative |  | ELMA/Emerson locator searches: no Canary/RAND filer; bounded with the legal-name caveat |
| 46 | CONFIRMED | MDS | C06.E1;C06.E2 | {} | supporting | negative |  | SFF-2025 RAND recommendation names the Technology and Security Policy Center, not Canary; amounts held from lineage; bounded |
