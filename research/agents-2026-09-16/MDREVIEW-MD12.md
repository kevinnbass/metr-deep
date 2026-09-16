<!-- casework-review lane=research/grok-out/MD12-arc-spinout-provenance.csv -->

# Review of MD12 — arc spinout provenance

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 1fce430421a1b2c38a894ebf8ab3c7288e7387bc4898f20d5e3b95f7efab631e; goal state complete. Checked against the lane's saved ARC FY2024 Form 990 XML (object 202513219349323246: Schedule I CashGrantAmt 4477169 and NonCashAssistanceAmt 76766 to METR, purpose PROGRAM SPIN-OFF and the grant-agreement explanation text; Schedule N DistributionDt 2024-04-30 and FairMarketValueOfAssetAmt 4553935; Schedule B RESTRICTED; binaryAttachmentCnt 0), the METR spin-out posts, and a live check of alignment.org/funding-from-ftx on 2026-09-16. The transfer is typed as a transfer with its non-cash part in the same ledger; ARC-side funders (Open Philanthropy recommendations, FTX Foundation receipt and return) are context; locator and blocked routes are context.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| 1 | CONFIRMED | MDF | C02.E3;C06.E1 | {} | primary | evidence |  | saved gt990-202513219349323246 XML rechecked locally 2026-09-16: CashGrantAmt 4477169 on Schedule I; transfer typed; date from Schedule N |
| 2 | DIFFERS | MDF | C02.E3;C06.E1 | {"ledger": "transfers_regrants"} | primary | evidence |  | saved gt990-202513219349323246 XML rechecked locally 2026-09-16: NonCashAssistanceAmt 76766; non-cash part of the same transfer, not summed |
| 3 | CONFIRMED | MDP | C02.E3;C06.E1 | {} | primary | evidence |  | saved gt990-202513219349323246 XML rechecked locally 2026-09-16: Schedule I explanation text matches verbatim |
| 4 | CONFIRMED | MDS | C02.E3 | {} | supporting | context |  | index_2025 locator; context |
| 5 | CONFIRMED | MDT | C02.E3;C06.E1;C09.E1 | {} | primary | evidence |  | 2023-09-19 spin-out announcement; organisational separation, not asset distribution |
| 6 | CONFIRMED | MDT | C02.E3;C06.E1;C09.E1 | {} | primary | evidence |  | 2023-12-04 METR naming announcement |
| 7 | CONFIRMED | MDT | C02.E3;C06.E1 | {} | primary | evidence |  | saved gt990-202513219349323246 XML rechecked locally 2026-09-16: Schedule N DistributionDt 2024-04-30 and FairMarketValueOfAssetAmt 4553935 = cash + non-cash |
| 8 | CONFIRMED | MDT | C02.E3 | {} | supporting | context |  | ARC donate page spin-off sentence, not independently dated; context |
| 9 | CONFIRMED | MDF | C06.E1 | {} | supporting | context |  | Open Philanthropy recommendation to ARC (2022-03), Wayback id_; ARC's funder, not a METR event; context for non-attribution |
| 10 | CONFIRMED | MDF | C06.E1 | {} | supporting | context |  | Open Philanthropy recommendation to ARC (2022-11); context |
| 11 | CONFIRMED | MDP | C06.E1;C02.E3 | {} | primary | evidence |  | saved gt990-202513219349323246 XML rechecked locally 2026-09-16: PurposeOfGrantTxt PROGRAM SPIN-OFF; Schedule B RESTRICTED; the transfer cannot be attributed to any single ARC funder |
| 12 | DIFFERS | MDF | C06.E1 | {"money_type": "", "ledger": ""} | supporting | context |  | Schedule A unnamed gift totals are ARC receipts, not a grant row; money_type cleared; context |
| 13 | CONFIRMED | MDS | C02.E3;C06.E1 | {} | primary | negative |  | saved gt990-202513219349323246 XML rechecked locally 2026-09-16: Schedule B contributor fields RESTRICTED (8 occurrences) |
| 14 | CONFIRMED | MDP | C06.E1 | {} | primary | evidence |  | no restriction text on the Schedule I line; bounded as stated |
| 15 | CONFIRMED | MDP | C06.E1 | {} | supporting | evidence |  | restricted net assets 1146000 to 0 in the transfer year with no stated link to the transfer; bounded |
| 16 | CONFIRMED | MDS | C06.E1 | {} | primary | negative |  | binaryAttachmentCnt 0: the named grant agreement is not attached |
| 17 | CONFIRMED | MDP | C06.E1 | {} | supporting | context |  | present-day every.org donations to ARC; not about the 2024 transfer; context |
| 18 | CONFIRMED | MDS | C02.E3 | {} | supporting | context |  | route failure (TEOS 403); context |
| 19 | CONFIRMED | MDS | C02.E3 | {} | supporting | negative |  | index_2026 has no ARC return; bounded |
| 20 | CONFIRMED | MDS | C02.E3 | {} | supporting | context |  | per-object URL not hosted; context |
| 21 | CONFIRMED | MDS | C02.E3 | {} | supporting | context |  | AWS mirror lacks the object; context |
| 22 | CONFIRMED | MDS | C02.E3 | {} | supporting | negative |  | ARC FY2021 return absent from the 2023-2026 posting indexes; bounded |
| 23 | CONFIRMED | MDS | C06.E1 | {} | supporting | context |  | Coefficient live index route failure; context |
| 24 | CONFIRMED | MDS | C06.E1 | {} | supporting | context |  | live Open Philanthropy grant URL redirects; Wayback used; context |
| 25 | CONFIRMED | MDS | C02.E3 | {} | supporting | negative |  | metr.org/about has no transfer amount; bounded |
| 26 | CONFIRMED | MDS | C02.E3 | {} | supporting | context |  | alignment.org/about 404; context |
| 27 | CONFIRMED | MDS | C02.E3 | {} | supporting | negative |  | ARC blog RSS has no transfer document; bounded |
| 28 | CONFIRMED | MDS | C02.E3 | {} | supporting | context |  | ProPublica PDF download blocked; locator only; context |
| 29 | CONFIRMED | MDS | C02.E3;C06.E1 | {} | primary | negative |  | ARC FY2023 return: CYGrantsAndSimilarPaidAmt 0, no Schedule I grant to METR; bounded |
| 30 | CONFIRMED | MDF | C06.E1 | {} | supporting | context |  | alignment.org/funding-from-ftx live-checked 2026-09-16 (page dated 2022-11-15): 'Earlier in 2022 ARC received a grant for $1.25M from the FTX Foundation'; an ARC funder receipt, not a METR event; context |
| 31 | CONFIRMED | MDP | C06.E1 | {} | supporting | context |  | live-checked: 'we will set aside the money and not spend it'; ARC's own hold, not the Schedule I transfer restriction; context |
| 32 | CONFIRMED | MDT | C06.E1 | {} | supporting | context |  | live-checked: 2024 update, grant returned to the FTX bankruptcy estate less expenses; not the METR transfer; context |
| 33 | CONFIRMED | MDS | C06.E1 | {} | supporting | context |  | CDX wildcard miss while the exact path has captures; route note; context |
| 34 | CONFIRMED | MDS | C06.E1 | {} | supporting | context |  | RSS miss for a Ghost page; route note; context |
