<!-- casework-review lane=research/grok-out/MD45-calendar-monitor.csv -->

# Review of MD45 — calendar monitor

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 f6a38ae98f3fedf228b386795afa33a473a9b85d8f8a6fb8d55a5d8d0fb1a919; goal state complete. Checked against the lane's saved IRS instructions and index_2026 hit files, the metr.org blog HTML and RSS, the EDGAR responses, the Contracts Finder JSON, the NIST and AISI pages and the DSIT releases search. Every calendar entry carries an earliest-expected date derived from the statute, instructions or announced term and an official release point; every now-check is dated and explicitly a check rather than a finding of absence; every future document is an N/A-with-reason closer with a next-check date; nothing was drafted or sent.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| A01 | CONFIRMED | MDT | C01.E5;C02.E3 | {} | supporting | evidence |  | calendar entry: earliest expected date derived from the statute/instructions or the announced term, official release point named; approximate where the source is approximate |
| A02 | CONFIRMED | MDT | C01.E5;C02.E3 | {} | supporting | evidence |  | calendar entry: earliest expected date derived from the statute/instructions or the announced term, official release point named; approximate where the source is approximate |
| A03 | CONFIRMED | MDT | C07.E3 | {} | supporting | evidence |  | calendar entry: earliest expected date derived from the statute/instructions or the announced term, official release point named; approximate where the source is approximate |
| A04 | CONFIRMED | MDT | C01.E5;C02.E3;C07.E3 | {} | supporting | evidence |  | calendar entry: earliest expected date derived from the statute/instructions or the announced term, official release point named; approximate where the source is approximate |
| A05 | CONFIRMED | MDT | C07.E3 | {} | supporting | evidence |  | calendar entry: earliest expected date derived from the statute/instructions or the announced term, official release point named; approximate where the source is approximate |
| A06 | CONFIRMED | MDT | C01.E5;C02.E3 | {} | supporting | evidence |  | calendar entry: earliest expected date derived from the statute/instructions or the announced term, official release point named; approximate where the source is approximate |
| A07 | CONFIRMED | MDT | C01.E5;C02.E3;C07.E3 | {} | supporting | evidence |  | calendar entry: earliest expected date derived from the statute/instructions or the announced term, official release point named; approximate where the source is approximate |
| B01 | CONFIRMED | MDT | C01.E5;C02.E3 | {} | supporting | evidence |  | dated now-check at the official release point: not posted as of 2026-09-16 (index_2026 rows, metr.org/blog RSS, EDGAR, CF/NIST/AISI, DSIT releases); a check, not a finding of absence |
| B02 | CONFIRMED | MDT | C01.E5;C02.E3 | {} | supporting | evidence |  | dated now-check at the official release point: not posted as of 2026-09-16 (index_2026 rows, metr.org/blog RSS, EDGAR, CF/NIST/AISI, DSIT releases); a check, not a finding of absence |
| B03 | CONFIRMED | MDT | C07.E3 | {} | supporting | evidence |  | dated now-check at the official release point: not posted as of 2026-09-16 (index_2026 rows, metr.org/blog RSS, EDGAR, CF/NIST/AISI, DSIT releases); a check, not a finding of absence |
| B04 | CONFIRMED | MDT | C01.E5;C02.E3;C07.E3 | {} | supporting | evidence |  | dated now-check at the official release point: not posted as of 2026-09-16 (index_2026 rows, metr.org/blog RSS, EDGAR, CF/NIST/AISI, DSIT releases); a check, not a finding of absence |
| B05 | CONFIRMED | MDT | C07.E3 | {} | supporting | evidence |  | dated now-check at the official release point: not posted as of 2026-09-16 (index_2026 rows, metr.org/blog RSS, EDGAR, CF/NIST/AISI, DSIT releases); a check, not a finding of absence |
| B06 | CONFIRMED | MDT | C01.E5;C02.E3 | {} | supporting | evidence |  | dated now-check at the official release point: not posted as of 2026-09-16 (index_2026 rows, metr.org/blog RSS, EDGAR, CF/NIST/AISI, DSIT releases); a check, not a finding of absence |
| B07 | CONFIRMED | MDT | C01.E5;C02.E3 | {} | supporting | evidence |  | dated now-check at the official release point: not posted as of 2026-09-16 (index_2026 rows, metr.org/blog RSS, EDGAR, CF/NIST/AISI, DSIT releases); a check, not a finding of absence |
| B08 | CONFIRMED | MDT | C01.E5;C02.E3;C07.E3 | {} | supporting | evidence |  | dated now-check at the official release point: not posted as of 2026-09-16 (index_2026 rows, metr.org/blog RSS, EDGAR, CF/NIST/AISI, DSIT releases); a check, not a finding of absence |
| C01 | CONFIRMED | MDS | C01.E5;C02.E3;C07.E3 | {} | supporting | context |  | first monitor pass: nothing newly available to route; context |
| C02 | CONFIRMED | MDS | C01.E5;C02.E3;C07.E3 | {} | supporting | context |  | first monitor pass: nothing newly available to route; context |
| C03 | CONFIRMED | MDS | C07.E3 | {} | supporting | context |  | first monitor pass: nothing newly available to route; context |
| C04 | CONFIRMED | MDS | C01.E5;C02.E3 | {} | supporting | context |  | first monitor pass: nothing newly available to route; context |
| C05 | CONFIRMED | MDS | C01.E5;C02.E3;C07.E3 | {} | supporting | context |  | first monitor pass: nothing newly available to route; context |
| D01 | CONFIRMED | MDT | C01.E5;C02.E3;C07.E3 | {} | supporting | evidence |  | N/A-with-reason calendar closer with next-check date; explicitly not a negative finding |
| D02 | CONFIRMED | MDT | C01.E5;C02.E3 | {} | supporting | evidence |  | N/A-with-reason calendar closer with next-check date; explicitly not a negative finding |
| D03 | CONFIRMED | MDT | C07.E3 | {} | supporting | evidence |  | N/A-with-reason calendar closer with next-check date; explicitly not a negative finding |
| D04 | CONFIRMED | MDT | C01.E5;C02.E3 | {} | supporting | evidence |  | N/A-with-reason calendar closer with next-check date; explicitly not a negative finding |
| D05 | CONFIRMED | MDT | C07.E3 | {} | supporting | evidence |  | N/A-with-reason calendar closer with next-check date; explicitly not a negative finding |
| D06 | CONFIRMED | MDT | C01.E5;C02.E3 | {} | supporting | evidence |  | N/A-with-reason calendar closer with next-check date; explicitly not a negative finding |
| D07 | CONFIRMED | MDT | C01.E5;C02.E3;C07.E3 | {} | supporting | evidence |  | N/A-with-reason calendar closer with next-check date; explicitly not a negative finding |
| E01 | CONFIRMED | MDS | C01.E5;C02.E3;C07.E3 | {} | supporting | negative |  | class-level bounded negative at the official release point with blind spots stated; future documents deferred to Task D closers |
| E02 | CONFIRMED | MDS | C01.E5;C02.E3;C07.E3 | {} | supporting | negative |  | class-level bounded negative at the official release point with blind spots stated; future documents deferred to Task D closers |
| E03 | CONFIRMED | MDS | C07.E3 | {} | supporting | negative |  | class-level bounded negative at the official release point with blind spots stated; future documents deferred to Task D closers |
| E04 | CONFIRMED | MDS | C01.E5;C02.E3 | {} | supporting | negative |  | class-level bounded negative at the official release point with blind spots stated; future documents deferred to Task D closers |
| E05 | CONFIRMED | MDS | C01.E5;C02.E3;C07.E3 | {} | supporting | negative |  | class-level bounded negative at the official release point with blind spots stated; future documents deferred to Task D closers |
| E06 | CONFIRMED | MDS | C01.E5;C02.E3 | {} | supporting | negative |  | class-level bounded negative at the official release point with blind spots stated; future documents deferred to Task D closers |
| E07 | CONFIRMED | MDS | C07.E3;C02.E3 | {} | supporting | negative |  | class-level bounded negative at the official release point with blind spots stated; future documents deferred to Task D closers |
| E08 | CONFIRMED | MDS | C01.E5;C02.E3;C07.E3 | {} | supporting | negative |  | class-level bounded negative at the official release point with blind spots stated; future documents deferred to Task D closers |
| E09 | CONFIRMED | MDS | C01.E5;C02.E3 | {} | supporting | context |  | TEOS 403 cap; context |
