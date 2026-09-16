<!-- casework-review lane=research/grok-out/MD42-anthropic-securities-filings.csv -->

# Review of MD42 — anthropic securities filings

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 5d36db035b2b70586331b09a1c9f004b7a8c78dd0e6b31b5181d06940cb9106b; goal state complete. Checked against the lane's saved EDGAR company-browse, CIK directory, EFTS JSON and Form D results, the eCFR/GovInfo Item 403 text and the Form S-1 PDF, Anthropic's support article (transfer-restriction sentence verified) and confidential-draft-S-1 notice, and the Delaware/Florida/California registry responses. No public Anthropic, PBC registration statement, CIK or holder table exists on EDGAR; the 'Anthropic'-named Form D filers are distinct series vehicles; a future S-1 would disclose only >5% holders and management; the issuer's bylaws restriction is recorded as the issuer's own statement; the public S-1 is a calendar closer with a next-check date, never a finding of no holders.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| 1 | CONFIRMED | MDS | C07.E3;C05.E1 | {} | supporting | negative |  | bounded negative: no public Anthropic, PBC registration statement, CIK or holder table on EDGAR (verified 'No matching companies'); name-collision series vehicles and third-party mentions are not the issuer |
| 2 | CONFIRMED | MDS | C07.E3;C05.E1 | {} | supporting | negative |  | bounded negative: no public Anthropic, PBC registration statement, CIK or holder table on EDGAR (verified 'No matching companies'); name-collision series vehicles and third-party mentions are not the issuer |
| 3 | CONFIRMED | MDS | C07.E3;C05.E1 | {} | supporting | negative |  | bounded negative: no public Anthropic, PBC registration statement, CIK or holder table on EDGAR (verified 'No matching companies'); name-collision series vehicles and third-party mentions are not the issuer |
| 4 | CONFIRMED | MDS | C07.E3;C05.E1 | {} | supporting | context |  | cik_lookup tool returned 0 despite directory hits; route quirk; context |
| 5 | CONFIRMED | MDS | C07.E3;C05.E1 | {} | supporting | negative |  | bounded negative: no public Anthropic, PBC registration statement, CIK or holder table on EDGAR (verified 'No matching companies'); name-collision series vehicles and third-party mentions are not the issuer |
| 6 | CONFIRMED | MDS | C07.E3;C05.E1 | {} | supporting | negative |  | bounded negative: no public Anthropic, PBC registration statement, CIK or holder table on EDGAR (verified 'No matching companies'); name-collision series vehicles and third-party mentions are not the issuer |
| 7 | CONFIRMED | MDS | C07.E3;C05.E1 | {} | supporting | negative |  | bounded negative: no public Anthropic, PBC registration statement, CIK or holder table on EDGAR (verified 'No matching companies'); name-collision series vehicles and third-party mentions are not the issuer |
| 8 | CONFIRMED | MDE | C07.E3 | {} | supporting | evidence |  | distinct Form D filer with 'Anthropic' in its name (series/co-invest vehicle), kept apart from Anthropic, PBC |
| 9 | CONFIRMED | MDE | C07.E3 | {} | supporting | evidence |  | distinct Form D filer with 'Anthropic' in its name (series/co-invest vehicle), kept apart from Anthropic, PBC |
| 10 | CONFIRMED | MDE | C07.E3 | {} | supporting | evidence |  | distinct Form D filer with 'Anthropic' in its name (series/co-invest vehicle), kept apart from Anthropic, PBC |
| 11 | CONFIRMED | MDP | C07.E3;C05.E1 | {} | supporting | evidence |  | Regulation S-K Item 403 / Form S-1 Item 11(m): a public S-1 would disclose only >5% holders and management, not a full cap table |
| 12 | CONFIRMED | MDP | C07.E3;C05.E1 | {} | supporting | evidence |  | Regulation S-K Item 403 / Form S-1 Item 11(m): a public S-1 would disclose only >5% holders and management, not a full cap table |
| 13 | CONFIRMED | MDP | C07.E3;C05.E1 | {} | supporting | evidence |  | issuer's own statement of its bylaws transfer restriction (unapproved transfers void; SPVs barred) verified in the saved page; how a holding could be held or moved, naming no holder |
| 14 | CONFIRMED | MDP | C07.E3 | {} | supporting | evidence |  | issuer's own statement of its bylaws transfer restriction (unapproved transfers void; SPVs barred) verified in the saved page; how a holding could be held or moved, naming no holder |
| 15 | CONFIRMED | MDS | C07.E3 | {} | supporting | context |  | Delaware ICIS public GET is a search form; context |
| 16 | CONFIRMED | MDS | C07.E3 | {} | supporting | negative |  | Florida foreign annual report has no charter/bylaws text; bounded |
| 17 | CONFIRMED | MDT | C07.E3;C05.E1 | {} | supporting | evidence |  | calendar closer CAL05: public S-1 is as-published; next check 2026-10-16; confidential draft is not a holder table |
| 18 | CONFIRMED | MDS | C07.E3;C05.E1 | {} | supporting | negative |  | bounded negative: no public Anthropic, PBC registration statement, CIK or holder table on EDGAR (verified 'No matching companies'); name-collision series vehicles and third-party mentions are not the issuer |
| 19 | CONFIRMED | MDS | C07.E3 | {} | supporting | negative |  | anthropic.com/company hosts no charter or bylaws; bounded |
| 20 | CONFIRMED | MDS | C07.E3 | {} | supporting | context |  | CA Bizfile Incapsula; context |
| 21 | CONFIRMED | MDS | C07.E3;C05.E1 | {} | supporting | negative |  | bounded negative: no public Anthropic, PBC registration statement, CIK or holder table on EDGAR (verified 'No matching companies'); name-collision series vehicles and third-party mentions are not the issuer |
| 22 | CONFIRMED | MDS | C07.E3;C05.E1 | {} | supporting | negative |  | bounded negative: no public Anthropic, PBC registration statement, CIK or holder table on EDGAR (verified 'No matching companies'); name-collision series vehicles and third-party mentions are not the issuer |
