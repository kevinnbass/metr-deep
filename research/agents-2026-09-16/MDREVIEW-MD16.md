<!-- casework-review lane=research/grok-out/MD16-canary-award-structure.csv -->

# Review of MD16 — canary award structure

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 10bdc84c0a4c0703ba8aa62f86dea71253850d90594df509f37a2e95ec2e2d52; goal state complete. Checked against the lane's saved METR 2024-10-09 blog body and RAND press release (both quotes verified verbatim), the Wayback captures, and the Audacious grantee/about/FAQ pages. The joint ~$38M and METR-side ~$17M are quoted commitments; the ~$21M remainder is labelled a subtraction and bound as context; cohort boilerplate and partner lists are adjacency; Barnes's 'a bit under $16m across 3 years' is the term source. The worker's later rewrite changed one quote (A06) cosmetically; re-pinned.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| A01 | CONFIRMED | MDF | C06.E2 | {} | primary | evidence |  | saved metr-blog-2024-10-09 body verified: 'catalyzed approximately $38 million of funding for Canary, a collaboration with METR and RAND'; joint commitment; MD14 C05 and lineage FN605 hold the same figure as context |
| A02 | CONFIRMED | MDF | C06.E2 | {} | primary | evidence |  | saved body verified: 'Approximately $17 million of this will support work at METR'; METR-side quoted allocation; not additive with A01 |
| A03 | CONFIRMED | MDE | C06.E2 | {} | supporting | evidence |  | legal recipients named by METR's page: METR and RAND, unmerged |
| A04 | CONFIRMED | MDF | C06.E2 | {} | primary | evidence |  | saved rand-org press verified: 'has committed approximately $38 million to RAND and METR for Canary'; RAND's own wording of the same commitment |
| A05 | CONFIRMED | MDR | C06.E2 | {} | supporting | evidence |  | RAND names both contributors and public-role leads; not a dollar split |
| A06 | CONFIRMED | MDP | C06.E2 | {} | supporting | evidence |  | Audacious grantee page names the collaboration, no amount; correctly bounded |
| B01 | CONFIRMED | MDP | C06.E2 | {} | primary | evidence |  | cohort boilerplate correctly classified as adjacency, not a Canary-specific payer list |
| B02 | CONFIRMED | MDP | C06.E2 | {} | supporting | evidence |  | same boilerplate on METR's page; adjacency |
| B03 | CONFIRMED | MDS | C06.E2 | {} | supporting | negative |  | Audacious page names no Canary dollar funder; bounded |
| B04 | CONFIRMED | MDP | C06.E2 | {} | primary | evidence |  | partner list is membership; page appearance not a join date; adjacency |
| B05 | CONFIRMED | MDP | C06.E2 | {} | primary | evidence |  | FAQ: TED does not fund grantees; TED and Audacious unmerged |
| C01 | CONFIRMED | MDF | C06.E2 | {} | supporting | context |  | quoted METR-side allocation; same figure as A02; context so one statement is one row |
| C02 | CONFIRMED | MDS | C06.E2 | {} | primary | negative |  | RAND gives no per-recipient split; bounded |
| C03 | CONFIRMED | MDP | C06.E2 | {} | supporting | context |  | $21 million is a subtraction, not a quoted allocation; correctly labelled; bound as context so it is never read as a documented RAND commitment |
| C04 | CONFIRMED | MDS | C06.E2 | {} | supporting | negative |  | Audacious page gives no split; bounded |
| D01 | CONFIRMED | MDF | C06.E2 | {} | primary | evidence |  | Barnes 2025-09-28 restatement 'a bit under $16m ... across 3 years'; MD14 C07/MD18 A03 hold the same statement; this is the term source |
| D02 | CONFIRMED | MDP | C06.E2 | {} | supporting | evidence |  | 'one-off' nature statement on a separate row; not a payment flag |
| D03 | CONFIRMED | MDP | C06.E2 | {} | supporting | context |  | about page restates first institutional-scale funding without amount; context |
| D04 | CONFIRMED | MDP | C06.E2 | {} | supporting | context |  | funding update thank-you; context |
| D05 | CONFIRMED | MDP | C06.E2 | {} | supporting | evidence |  | Wayback 2024-11-03 capture: same figures, 'Project Canary' wording; archive evidence |
| D06 | CONFIRMED | MDP | C06.E2 | {} | supporting | evidence |  | Wayback 2024-10-09 RAND capture: same figure; archive evidence |
| E01 | CONFIRMED | MDS | C06.E2 | {} | supporting | evidence |  | METR announcement class coverage receipt |
| E02 | CONFIRMED | MDS | C06.E2 | {} | supporting | context |  | route failure or scope note, not a content negative; context |
| E03 | CONFIRMED | MDS | C06.E2 | {} | supporting | evidence |  | RAND announcement class coverage receipt |
| E04 | CONFIRMED | MDS | C06.E2 | {} | supporting | context |  | route failure or scope note, not a content negative; context |
| E05 | CONFIRMED | MDS | C06.E2 | {} | supporting | evidence |  | Audacious/TED class coverage receipt |
| E06 | CONFIRMED | MDS | C06.E2 | {} | supporting | negative |  | bounded negative as stated |
| E07 | CONFIRMED | MDS | C06.E2 | {} | supporting | context |  | route failure or scope note, not a content negative; context |
| E08 | CONFIRMED | MDS | C06.E2 | {} | supporting | context |  | route failure or scope note, not a content negative; context |
| E09 | DIFFERS | MDS | C06.E2 | {"source_class": "archives"} | supporting | context |  | jina 403; route failure; class corrected; context |
| E10 | CONFIRMED | MDS | C06.E2 | {} | supporting | context |  | route failure or scope note, not a content negative; context |
| E11 | CONFIRMED | MDS | C06.E2 | {} | supporting | evidence |  | Wayback CDX coverage receipt |
