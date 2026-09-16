<!-- casework-review lane=research/grok-out/MD99-71m-allocation-request.csv -->

# Review of MD99 — 71m allocation request

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 d38634a5e9a97a04eeced65bc245be6bc83e62e2bbd8e09e6ea6d6ff8a95a255; goal state complete. Outreach-drafting lane. Checked the lane's saved copy of the exhaustion gate (sha256 6f8887d9… matches the live file), its reconciliation copy, its this-run fetches of the funding update, about page and Packard catalog, and the unsent draft (sha256 3bdc9403…). The draft asks only the six residual cells for the unresolved remainder, states the denominator and the Packard component as already established, links reconciliation cells, contains no allegation, no compound question and no banned motive word, and carries approved_for_send false with USER_AUTHORITY_WAIT; research/outreach/receipts is empty and nothing was transmitted. All fact rows restate promoted facts or enumerate questions and are bound as context; the remainder row's money type and amount are cleared (arithmetic, not a commitment); two bounded negatives stand.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| A01 | CONFIRMED | MDP | C01.E4 | {} | supporting | context |  | gate state as read by the lane (gate_pass true with listed exceptions); journal context |
| A02 | CONFIRMED | MDP | C01.E4;C02.E2 | {} | supporting | context |  | residual cell enumerated from the exhaustion gate; a question to ask, not a fact; no amount |
| A03 | DIFFERS | MDP | C01.E4;C02.E2 | {"money_type": ""} | supporting | context |  | residual cell enumerated from the exhaustion gate; money_type cleared because the row states a question, not a commitment |
| A04 | CONFIRMED | MDT | C01.E4;C02.E2 | {} | supporting | context |  | residual cell enumerated from the exhaustion gate; a question to ask, not a fact; no amount |
| A05 | CONFIRMED | MDF | C01.E4;C02.E2 | {} | supporting | context |  | residual cell enumerated from the exhaustion gate; a question to ask, not a fact; no amount |
| A06 | CONFIRMED | MDP | C01.E4;C02.E2 | {} | supporting | context |  | residual cell enumerated from the exhaustion gate; a question to ask, not a fact; no amount |
| A07 | CONFIRMED | MDI | C01.E4 | {} | supporting | context |  | residual cell enumerated from the exhaustion gate; a question to ask, not a fact; no amount |
| A08 | CONFIRMED | MDF | C01.E4;C02.E2 | {} | supporting | context |  | restates the promoted Packard $350,000 commitment (MDP0030 / packard.org catalog re-fetched this run); duplicate of a promoted fact |
| A09 | DIFFERS | MDP | C01.E4 | {"money_type": "", "amount_usd": ""} | supporting | context |  | the unresolved remainder is arithmetic on the reconciliation, not a commitment by anyone; money_type and amount cleared so no table carries a $70.65M 'commitment' row; the figure lives in commitment_reconciliation.csv |
| A10 | CONFIRMED | MDP | C01.E4 | {} | supporting | context |  | restates the five S4 drafts' USER_AUTHORITY_WAIT state; journal context |
| A11 | CONFIRMED | MDF | C01.E4 | {} | supporting | context |  | restates the promoted denominator sentence (MDF0089), re-fetched this run; duplicate of a promoted fact |
| A12 | DIFFERS | MDP | C01.E4 | {"money_type": ""} | supporting | context |  | aggregate of one compatible component; money_type cleared per the aggregate convention |
| B01 | CONFIRMED | MDP | C01.E4;C02.E2 | {} | supporting | context |  | journal: the unsent lane draft exists (sha256 3bdc9403…); the reviewed cleaned copy is research/outreach/MD99-71m-allocation.md |
| C01 | CONFIRMED | MDP | C01.E4;C02.E2 | {} | supporting | context |  | journal: the draft links the reconciliation cells rather than a theory; reviewer confirmed no banned motive word and no compound question in the lane draft |
| D01 | CONFIRMED | MDP | C01.E4;C02.E2 | {} | supporting | context |  | journal: approved_for_send false, USER_AUTHORITY_WAIT, nothing transmitted; reviewer confirmed research/outreach/receipts is empty |
| E01 | CONFIRMED | MDS | C01.E4;C02.E2 | {} | supporting | negative |  | bounded negative: the funding update and about page (this-run hashes) give none of the six remainder cells |
| E02 | CONFIRMED | MDS | C01.E4;C02.E2 | {} | supporting | negative |  | bounded negative: the Packard grantee catalog page gives no cash-paid-versus-approved figure for the $350,000 listing |
