<!-- casework-review lane=research/grok-out/MD25-revenue-runway-reconciliation.csv -->

# Review of MD25 — revenue runway reconciliation

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 d682d6bc729158bc84aaba02db9a2ef5c4d98cf4347812eb947e6db96660a0f0; goal state complete. Checked against the lane's saved primaries: the METR FY2024 Form 990 XML (CYTotalExpensesAmt 8234524; TotalEmployeeCnt 38; EmployeeCnt 38), the saved 2024 annual report PDF (10.7 MB; 'total 2024 budget of $10 million'; 'raise and deploy $15 million'), the saved Business Insider article (datePublished 2026-09-11; 'approximately 35-person lab'; Barnes quote), and the saved GreaterWrong comment. Budget, target, run-rate and officer statements are retargeted from MDF to MDP so no untyped figure sits in the money ledger; recipient-side expenses are typed as an aggregate; the C01/D01 propositions that set the commitment beside filed revenue without summing are evidence.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| A01 | CONFIRMED | MDF | C01.E3 | {} | supporting | context |  | the approximately $71M sentence; MD14 row A01 is the promoted denominator; context |
| A02 | DIFFERS | MDP | C01.E3;C02.E4 | {"amount_usd": "", "quantity_or_value": "$10 million total 2024 budget (issuer statement, calendar 2024)", "edge_type": "issuer budget statement; not an inbound amount and not comparable with the commitment denominator"} | supporting | evidence |  | saved 2024 annual report PDF (10.7 MB) rechecked locally: 'METR achieved this and more on a total 2024 budget of $10 million.'; retargeted from MDF to MDP so an untyped budget figure does not sit in the money ledger |
| A03 | DIFFERS | MDP | C01.E3 | {"amount_usd": "", "quantity_or_value": "$15 million 2025 raise-and-deploy target (issuer statement)", "edge_type": "issuer fundraising target; not revenue and not a commitment"} | supporting | evidence |  | saved PDF rechecked: 'In 2025, we seek to raise and deploy $15 million'; retargeted to MDP |
| A04 | DIFFERS | MDP | C01.E3 | {"edge_type": "issuer run-rate statement; not an inbound amount"} | supporting | context |  | GreaterWrong comment saved and rechecked; MD14 row C08 is the promoted exclusion; retargeted from MDF to MDP as context |
| A05 | CONFIRMED | MDT | C01.E3 | {} | supporting | context |  | runway sentence; MD14 row C09 promoted; context |
| A06 | DIFFERS | MDP | C01.E3 | {"edge_type": "issuer fundraising goal for end-2025 ($10M) and Audacious described as one-off; not revenue"} | supporting | evidence |  | saved comment rechecked; retargeted from MDF to MDP |
| A07 | CONFIRMED | MDE | C02.E4;C01.E3 | {} | primary | evidence |  | saved FY2024 XML rechecked: TotalEmployeeCnt 38 (Schedule F 63 is a different measure, as the row states) |
| A08 | CONFIRMED | MDE | C02.E4 | {} | supporting | context |  | same 38 on the Part V tag; context |
| A09 | CONFIRMED | MDE | C01.E3 | {} | supporting | context |  | saved Business Insider HTML (datePublished 2026-09-11, Stephen Council): 'approximately 35-person lab'; press characterization, not a census; context |
| A10 | DIFFERS | MDP | C01.E3 | {"edge_type": "on-record officer statement via press: fundraising not the bottleneck; qualitative, no amount"} | supporting | context |  | saved BI HTML rechecked: quote verbatim; retargeted from MDF to MDP |
| A11 | CONFIRMED | MDS | C01.E3 | {} | supporting | context |  | open roles are not a headcount; context |
| B01 | CONFIRMED | MDF | C02.E4;C01.E3 | {} | supporting | context |  | filed FY2024 total revenue; MD01 row 1 is the promoted row; context |
| B02 | DIFFERS | MDF | C02.E4 | {"payment_status": "filed on the recipient's own Form 990 (CYTotalExpensesAmt); recipient-side aggregate, not a funding event"} | primary | evidence |  | saved FY2024 XML rechecked: CYTotalExpensesAmt 8234524; typed as a recipient aggregate |
| B03 | CONFIRMED | MDS | C02.E4 | {} | supporting | context |  | FY2025 990 calendar closer (after 2026-11-16); MD01 row 15 holds it; context |
| C01 | CONFIRMED | MDP | C01.E3;C01.E4;C02.E4 | {} | primary | evidence |  | commitment and filed revenue set side by side without summing; periods do not overlap; correctly stated |
| D01 | CONFIRMED | MDP | C01.E4;C02.E4 | {} | primary | evidence |  | explicit bounded statement of what the committed-versus-filed difference cannot establish |
| E01 | CONFIRMED | MDS | C02.E4 | {} | supporting | context |  | TEOS 403; context |
| E02 | CONFIRMED | MDS | C02.E4 | {} | supporting | negative |  | index_2024 none; bounded |
| E03 | CONFIRMED | MDS | C01.E3 | {} | supporting | negative |  | no 2025 annual report at the checked paths; bounded |
| E04 | CONFIRMED | MDS | C01.E3 | {} | supporting | negative |  | Substack landing has no budget figure; bounded |
| E05 | CONFIRMED | MDS | C01.E3 | {} | supporting | context |  | LinkedIn /company/metr is a different legal entity (not merged); context |
| E06 | CONFIRMED | MDS | C01.E3 | {} | supporting | context |  | login wall; context |
| E07 | CONFIRMED | MDS | C01.E3 | {} | supporting | context |  | board lists openings, not headcount; context |
| E08 | CONFIRMED | MDS | C01.E3 | {} | supporting | context |  | EA Forum GraphQL missing document; GreaterWrong served the comment; context |
