<!-- casework-review lane=research/grok-out/MD01-metr-recipient-baseline.csv -->

# Review of MD01 — metr recipient baseline

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 4624ac6524d51366cb46b242b077bd7ebf345d2685325c280058eb3ad5a4e0df; goal state complete. Checked against the lane's saved IRS e-file XML (object 202523209349300367: period 2024-05-01 to 2024-12-31, total revenue 13639155, contributions 13603035, program service revenue 0, net assets 5404631, related-organization contributions 4501424, all other contributions 9101611, accrual, DE domicile, binaryAttachmentCnt 0, FSAuditedInd 1, Schedule B contributor fields RESTRICTED) and the live metr.org pages. Recipient-side revenue totals are not typed as grants; the ARC transfer is typed as a transfer; locator rows, calendar closers and blocked routes are context.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| 1 | DIFFERS | MDF | C02.E4;C01.E3 | {"money_type": "", "ledger": "", "quantity_or_value": "CYTotalRevenueAmt 13639155; CYContributionsGrantsAmt 13603035", "payment_status": "filed on the recipient's own Form 990", "subject": "METR FY2024 Form 990 initial short-year total revenue and contributions (2024-05-01 to 2024-12-31)"} | primary | evidence |  | saved primary irs-bulk-2025-TEOS-XML-11C-202523209349300367 rechecked locally 2026-09-16: both totals match; a recipient-side revenue total is not a grant, so money_type is cleared; not comparable with the 2026 commitment statement |
| 2 | CONFIRMED | MDF | C02.E4 | {} | primary | evidence |  | saved primary irs-bulk-2025-TEOS-XML-11C-202523209349300367 rechecked locally 2026-09-16: NetAssetsOrFundBalancesEOYAmt 5404631 matches; no donor-restriction tag on the return |
| 3 | CONFIRMED | MDF | C02.E4 | {} | primary | evidence |  | saved primary irs-bulk-2025-TEOS-XML-11C-202523209349300367 rechecked locally 2026-09-16: CYProgramServiceRevenueAmt 0 matches; no government-grant element |
| 4 | CONFIRMED | MDS | C02.E4 | {} | primary | negative |  | saved primary irs-bulk-2025-TEOS-XML-11C-202523209349300367 rechecked locally 2026-09-16: binaryAttachmentCnt=0 and FSAuditedInd=1 both present; bounded negative on the public e-file only |
| 5 | CONFIRMED | MDS | C02.E4 | {} | supporting | negative |  | metr.org pages saved; no 990 or audited statement posted; bounded to the pages named |
| 6 | CONFIRMED | MDS | C02.E4 | {} | supporting | context |  | the California download is the May-Not-Operate list, not a registrant dump; absence is a route limitation, bound as context |
| 7 | CONFIRMED | MDS | C02.E4 | {} | supporting | context |  | index_2025 locator row for OBJECT_ID 202523209349300367; a locator, not a finding |
| 8 | DIFFERS | MDF | C02.E3;C02.E4;C06.E1 | {"ledger": "transfers_regrants", "date_precision": "day"} | primary | evidence |  | saved primary irs-bulk-2025-TEOS-XML-11C-202523209349300367 rechecked locally 2026-09-16: RelatedOrganizationsAmt 4501424 matches; recipient-side view of the ARC program transfer; ledger typed |
| 9 | CONFIRMED | MDS | C02.E3;C02.E4 | {} | primary | negative |  | saved primary irs-bulk-2025-TEOS-XML-11C-202523209349300367 rechecked locally 2026-09-16: Schedule B contributor fields RESTRICTED; verification boundary correctly stated |
| 10 | DIFFERS | MDF | C02.E3;C02.E4 | {"money_type": "", "ledger": "", "payment_status": "filed as AllOtherContributionsAmt on the recipient's Form 990; payers not named"} | primary | evidence |  | saved primary irs-bulk-2025-TEOS-XML-11C-202523209349300367 rechecked locally 2026-09-16: AllOtherContributionsAmt 9101611 matches; an unnamed aggregate is not a grant row, money_type cleared |
| 11 | CONFIRMED | MDR | C02.E4 | {} | primary | evidence |  | saved primary irs-bulk-2025-TEOS-XML-11C-202523209349300367 rechecked locally 2026-09-16: IdRelatedTaxExemptOrgGrp names Alignment Research Center as the related organisation |
| 12 | CONFIRMED | MDE | C02.E4 | {} | primary | evidence |  | EO BMF CA extract row for EIN 991219864 saved; ruling 202403, subsection 03 |
| 13 | CONFIRMED | MDE | C02.E4 | {} | primary | evidence |  | saved primary irs-bulk-2025-TEOS-XML-11C-202523209349300367 rechecked locally 2026-09-16: MethodOfAccountingAccrualInd X and LegalDomicileStateCd DE present |
| 14 | CONFIRMED | MDE | C02.E4 | {} | supporting | evidence |  | EIN 99-1219864 on metr.org/donate saved page |
| 15 | CONFIRMED | MDT | C02.E4;C01.E3 | {} | supporting | context |  | calendar closer for the FY2025 Form 990, not a negative; next check after 2026-11-16 |
| 16 | CONFIRMED | MDT | C02.E4 | {} | supporting | context |  | calendar closer for the FY2026 Form 990; period not closed |
| 17 | CONFIRMED | MDS | C02.E4 | {} | supporting | context |  | route failure (TEOS 403), not a content negative; bound as context |
| 18 | CONFIRMED | MDS | C02.E4 | {} | supporting | negative |  | index_2024 contains no METR row; bounded to that posting-year index |
| 19 | CONFIRMED | MDS | C02.E4 | {} | supporting | negative |  | index_2026 contains no METR row at check time; bounded |
| 20 | CONFIRMED | MDS | C02.E4 | {} | supporting | context |  | route failure (JavaScript portal), not a content negative; bound as context |
| 21 | CONFIRMED | MDS | C02.E4 | {} | supporting | context |  | route failure (legacy search URL failed), bound as context |
| 22 | CONFIRMED | MDS | C02.E4 | {} | supporting | context |  | path note: per-object XML is not hosted; the zip route worked; context |
| 23 | CONFIRMED | MDS | C02.E4 | {} | supporting | negative |  | BMF state file follows filing address; the CA row exists; bounded |
