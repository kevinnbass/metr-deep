<!-- casework-review lane=research/grok-out/MD28-frontier-risk-report-coi.csv -->

# Review of MD28 — frontier risk report coi

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 4e6d88dc603203152ee0ba2b76b1bb6041af70952a0e728c844cdf1e0ad2bb17; goal state complete. Checked against the lane's saved FRR HTML and PDF, the Wayback id_ captures of metr.org/about on 2026-02-17, 2026-03-16 and 2026-05-19 (the reviewer verified the Cotra, Painter and Painter-title-change cards), the Wayback sparkline/timemap for metr.org/coi-policy.pdf, the live COI policy PDF (sha256 matches the S3 locator) and the AEF-1 PDF. The none-in-force finding is bound for the assessment window and for the publication date separately; the 2.5 Yes and the no-formal-process sentence are both recorded; every dated title is taken from the capture of that date and later titles are not applied backward; the unnamed 'at least 6' are not identified.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| A01 | CONFIRMED | MDT | C08.E1;C08.E2 | {} | primary | evidence |  | FRR assessment window (2026-02-16..03-16) and publication date (2026-05-19) recorded separately from the report itself |
| A02 | CONFIRMED | MDT | C08.E1;C08.E2 | {} | primary | evidence |  | FRR assessment window (2026-02-16..03-16) and publication date (2026-05-19) recorded separately from the report itself |
| A03 | CONFIRMED | MDQ | C08.E1;C08.E2 | {} | primary | evidence |  | FRR's own statement / Table A.1 cell quoted from the saved HTML (verified); both the 2.5 Yes and the no-formal-process sentence recorded without reconciliation |
| A04 | CONFIRMED | MDQ | C08.E2 | {} | supporting | evidence |  | FRR CoI-adjacent disclosures (funding independence, social ties, Constellation co-location); unnamed staff not identified |
| A05 | CONFIRMED | MDQ | C08.E1 | {} | primary | evidence |  | FRR's own statement / Table A.1 cell quoted from the saved HTML (verified); both the 2.5 Yes and the no-formal-process sentence recorded without reconciliation |
| A06 | CONFIRMED | MDQ | C08.E2 | {} | primary | evidence |  | FRR's own statement / Table A.1 cell quoted from the saved HTML (verified); both the 2.5 Yes and the no-formal-process sentence recorded without reconciliation |
| A07 | CONFIRMED | MDQ | C08.E2 | {} | primary | evidence |  | FRR's own statement / Table A.1 cell quoted from the saved HTML (verified); both the 2.5 Yes and the no-formal-process sentence recorded without reconciliation |
| A08 | CONFIRMED | MDQ | C08.E2 | {} | primary | evidence |  | FRR's own statement / Table A.1 cell quoted from the saved HTML (verified); both the 2.5 Yes and the no-formal-process sentence recorded without reconciliation |
| A09 | CONFIRMED | MDE | C08.E2 | {} | supporting | evidence |  | named contributors on the public report (public people in public roles) |
| A10 | CONFIRMED | MDE | C08.E2 | {} | supporting | evidence |  | named contributors on the public report (public people in public roles) |
| A11 | CONFIRMED | MDE | C08.E2 | {} | supporting | evidence |  | named contributors on the public report (public people in public roles) |
| A12 | CONFIRMED | MDP | C08.E2 | {} | supporting | evidence |  | HTML vs PDF difference on footnote 65 and thanks names; both recorded, neither chosen |
| A13 | CONFIRMED | MDE | C08.E2 | {} | supporting | evidence |  | named contributors on the public report (public people in public roles) |
| A14 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | Greenblatt parenthesised as Redwood Research; fn66 no non-public access; entities separate |
| A15 | CONFIRMED | MDQ | C08.E1;C08.E2 | {} | supporting | evidence |  | AEF-1 standard identity, date and 2.3/2.4/2.5 text as context for the report's checklist answers; not METR's policy |
| A16 | CONFIRMED | MDQ | C08.E1;C08.E2 | {} | supporting | evidence |  | AEF-1 standard identity, date and 2.3/2.4/2.5 text as context for the report's checklist answers; not METR's policy |
| A17 | CONFIRMED | MDQ | C08.E1;C08.E2 | {} | supporting | evidence |  | AEF-1 standard identity, date and 2.3/2.4/2.5 text as context for the report's checklist answers; not METR's policy |
| A18 | CONFIRMED | MDP | C08.E1;C08.E2 | {} | supporting | context |  | alias URL redirect; context |
| B01 | CONFIRMED | MDQ | C08.E1 | {} | primary | evidence |  | none-in-force finding for the assessment window and for the publication date, each from the report's own statement; the 2026-08-28 policy is later |
| B02 | CONFIRMED | MDQ | C08.E1 | {} | primary | evidence |  | none-in-force finding for the assessment window and for the publication date, each from the report's own statement; the 2026-08-28 policy is later |
| B03 | CONFIRMED | MDS | C08.E1 | {} | supporting | negative |  | bounded archive negative for metr.org/coi-policy.pdf (sparkline first_ts null, empty timemap, id_ 404); not proof no unpublished policy existed |
| B04 | CONFIRMED | MDS | C08.E1 | {} | supporting | negative |  | bounded archive negative for metr.org/coi-policy.pdf (sparkline first_ts null, empty timemap, id_ 404); not proof no unpublished policy existed |
| B05 | CONFIRMED | MDS | C08.E1 | {} | supporting | negative |  | bounded archive negative for metr.org/coi-policy.pdf (sparkline first_ts null, empty timemap, id_ 404); not proof no unpublished policy existed |
| B06 | CONFIRMED | MDS | C08.E1 | {} | supporting | negative |  | bounded archive negative for metr.org/coi-policy.pdf (sparkline first_ts null, empty timemap, id_ 404); not proof no unpublished policy existed |
| B07 | CONFIRMED | MDT | C08.E1 | {} | supporting | evidence |  | proposition: the two dates each carry a none-in-force result and are not collapsed |
| C01 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated public METR title on the publication-day about capture (Wayback id_ 20260519102303, sha256 recorded; reviewer spot-checked Cotra and Painter cards); public role, no conflict inferred |
| C02 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated public METR title on the publication-day about capture (Wayback id_ 20260519102303, sha256 recorded; reviewer spot-checked Cotra and Painter cards); public role, no conflict inferred |
| C03 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated public METR title on the publication-day about capture (Wayback id_ 20260519102303, sha256 recorded; reviewer spot-checked Cotra and Painter cards); public role, no conflict inferred |
| C04 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated public METR title on the publication-day about capture (Wayback id_ 20260519102303, sha256 recorded; reviewer spot-checked Cotra and Painter cards); public role, no conflict inferred |
| C05 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated public METR title on the publication-day about capture (Wayback id_ 20260519102303, sha256 recorded; reviewer spot-checked Cotra and Painter cards); public role, no conflict inferred |
| C06 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated public METR title on the publication-day about capture (Wayback id_ 20260519102303, sha256 recorded; reviewer spot-checked Cotra and Painter cards); public role, no conflict inferred |
| C07 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated public METR title on the publication-day about capture (Wayback id_ 20260519102303, sha256 recorded; reviewer spot-checked Cotra and Painter cards); public role, no conflict inferred |
| C08 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated public METR title on the publication-day about capture (Wayback id_ 20260519102303, sha256 recorded; reviewer spot-checked Cotra and Painter cards); public role, no conflict inferred |
| C09 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated public METR title on the publication-day about capture (Wayback id_ 20260519102303, sha256 recorded; reviewer spot-checked Cotra and Painter cards); public role, no conflict inferred |
| C10 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated public METR title on the publication-day about capture (Wayback id_ 20260519102303, sha256 recorded; reviewer spot-checked Cotra and Painter cards); public role, no conflict inferred |
| C11 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated public METR title on the publication-day about capture (Wayback id_ 20260519102303, sha256 recorded; reviewer spot-checked Cotra and Painter cards); public role, no conflict inferred |
| C12 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated public METR title on the publication-day about capture (Wayback id_ 20260519102303, sha256 recorded; reviewer spot-checked Cotra and Painter cards); public role, no conflict inferred |
| C13 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated public METR title on the publication-day about capture (Wayback id_ 20260519102303, sha256 recorded; reviewer spot-checked Cotra and Painter cards); public role, no conflict inferred |
| C14 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated public METR title on the publication-day about capture (Wayback id_ 20260519102303, sha256 recorded; reviewer spot-checked Cotra and Painter cards); public role, no conflict inferred |
| C15 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated public METR title on the publication-day about capture (Wayback id_ 20260519102303, sha256 recorded; reviewer spot-checked Cotra and Painter cards); public role, no conflict inferred |
| C16 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated public METR title on the publication-day about capture (Wayback id_ 20260519102303, sha256 recorded; reviewer spot-checked Cotra and Painter cards); public role, no conflict inferred |
| C17 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated public METR title on the publication-day about capture (Wayback id_ 20260519102303, sha256 recorded; reviewer spot-checked Cotra and Painter cards); public role, no conflict inferred |
| C18 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated public METR title on the publication-day about capture (Wayback id_ 20260519102303, sha256 recorded; reviewer spot-checked Cotra and Painter cards); public role, no conflict inferred |
| C19 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated public METR title on the publication-day about capture (Wayback id_ 20260519102303, sha256 recorded; reviewer spot-checked Cotra and Painter cards); public role, no conflict inferred |
| C20 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated public METR title on the publication-day about capture (Wayback id_ 20260519102303, sha256 recorded; reviewer spot-checked Cotra and Painter cards); public role, no conflict inferred |
| C21 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated public METR title on the publication-day about capture (Wayback id_ 20260519102303, sha256 recorded; reviewer spot-checked Cotra and Painter cards); public role, no conflict inferred |
| C22 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated public METR title on the publication-day about capture (Wayback id_ 20260519102303, sha256 recorded; reviewer spot-checked Cotra and Painter cards); public role, no conflict inferred |
| C23 | CONFIRMED | MDT | C08.E2 | {} | supporting | evidence |  | Chris Painter Policy Director on the Feb 17 / Mar 16 captures and President on May 19 (verified); titles kept per date |
| C24 | CONFIRMED | MDS | C08.E2 | {} | supporting | negative |  | two names absent from assessment-window about cards, present on May 19; bounded; not proof of non-involvement |
| C25 | CONFIRMED | MDR | C08.E2 | {} | supporting | context |  | person named on the report with no dated about card or team page; employer not guessed; context |
| C26 | CONFIRMED | MDR | C08.E2 | {} | supporting | context |  | person named on the report with no dated about card or team page; employer not guessed; context |
| C27 | CONFIRMED | MDR | C08.E2 | {} | supporting | context |  | person named on the report with no dated about card or team page; employer not guessed; context |
| C28 | CONFIRMED | MDR | C08.E2 | {} | supporting | context |  | person named on the report with no dated about card or team page; employer not guessed; context |
| C29 | CONFIRMED | MDR | C08.E2 | {} | supporting | context |  | person named on the report with no dated about card or team page; employer not guessed; context |
| C30 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | Greenblatt's affiliation at report date as the report states (Redwood Research) |
| C31 | CONFIRMED | MDR | C08.E2 | {} | supporting | context |  | person named on the report with no dated about card or team page; employer not guessed; context |
| C32 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated self-statement / roster from Wayback captures at the report dates; later titles not applied backward |
| C33 | CONFIRMED | MDR | C08.E2 | {} | supporting | evidence |  | dated self-statement / roster from Wayback captures at the report dates; later titles not applied backward |
| C34 | CONFIRMED | MDT | C08.E2 | {} | supporting | evidence |  | dated self-statement / roster from Wayback captures at the report dates; later titles not applied backward |
| D01 | CONFIRMED | MDQ | C08.E1 | {} | primary | evidence |  | live COI policy v1.0 last updated 2026-08-28 (sha256 cc313425... matches the S3 locator) postdates the FRR window and publication; scope and July 2026 examples recorded; not applied retroactively |
| D02 | CONFIRMED | MDQ | C08.E1 | {} | primary | evidence |  | live COI policy v1.0 last updated 2026-08-28 (sha256 cc313425... matches the S3 locator) postdates the FRR window and publication; scope and July 2026 examples recorded; not applied retroactively |
| D03 | CONFIRMED | MDT | C08.E1;C08.E2 | {} | supporting | evidence |  | live 2026-09-16 titles / funding wording recorded so they are not silently applied backward |
| D04 | CONFIRMED | MDQ | C08.E1 | {} | supporting | evidence |  | live 2026-09-16 titles / funding wording recorded so they are not silently applied backward |
| E01 | CONFIRMED | MDS | C08.E1 | {} | supporting | context |  | archive route failure (503/429/403/400); context |
| E02 | CONFIRMED | MDS | C08.E1 | {} | supporting | context |  | archive route failure (503/429/403/400); context |
| E03 | CONFIRMED | MDS | C08.E1;C08.E2 | {} | supporting | context |  | archive route failure (503/429/403/400); context |
| E04 | CONFIRMED | MDS | C08.E2 | {} | supporting | negative |  | bounded negative (404 team slugs; May 19 cards; empty id_ body; live policy URL) with blind spots stated |
| E05 | CONFIRMED | MDS | C08.E2 | {} | supporting | negative |  | bounded negative (404 team slugs; May 19 cards; empty id_ body; live policy URL) with blind spots stated |
| E06 | CONFIRMED | MDS | C08.E2 | {} | supporting | negative |  | bounded negative (404 team slugs; May 19 cards; empty id_ body; live policy URL) with blind spots stated |
| E07 | CONFIRMED | MDS | C08.E1 | {} | supporting | context |  | archive route failure (503/429/403/400); context |
| E08 | CONFIRMED | MDS | C08.E1;C08.E2 | {} | supporting | negative |  | bounded negative (404 team slugs; May 19 cards; empty id_ body; live policy URL) with blind spots stated |
