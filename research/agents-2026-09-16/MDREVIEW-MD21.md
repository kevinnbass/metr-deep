<!-- casework-review lane=research/grok-out/MD21-us-public-sector-awards.csv -->

# Review of MD21 — us public sector awards

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 b85f54ede796153a0a95fe7812231c32225f1d199e27d5c54e757313b40fe3d4; goal state complete. Checked against the lane's saved USAspending API responses (recipient listing, award search, award count, subawards: all empty for the METR legal name and EIN), SAM.gov public entity index (no registration; UEI not recovered), the NIST AI Consortium member list naming METR, and the CAISI March 2026 slide listing METR under CRADAs and DTAs (access to private benchmarks). No US public-sector award exists in the checked systems; the NIST/CAISI listings are typed as membership and in-kind access, explicitly not awards.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| A01 | CONFIRMED | MDS | C06.E3 | {} | supporting | context |  | GET 405 is a method cap; context |
| A02 | CONFIRMED | MDS | C06.E3 | {} | primary | negative |  | USAspending API query returned no recipient/award/subaward for the METR legal name or EIN; bounded with the UEI caveat |
| A03 | CONFIRMED | MDS | C06.E3 | {} | primary | negative |  | USAspending API query returned no recipient/award/subaward for the METR legal name or EIN; bounded with the UEI caveat |
| A04 | CONFIRMED | MDS | C06.E3 | {} | primary | negative |  | USAspending API query returned no recipient/award/subaward for the METR legal name or EIN; bounded with the UEI caveat |
| A05 | CONFIRMED | MDS | C06.E3 | {} | primary | negative |  | USAspending API query returned no recipient/award/subaward for the METR legal name or EIN; bounded with the UEI caveat |
| A06 | CONFIRMED | MDS | C06.E3 | {} | primary | negative |  | USAspending API query returned no recipient/award/subaward for the METR legal name or EIN; bounded with the UEI caveat |
| A07 | CONFIRMED | MDS | C06.E3 | {} | supporting | context |  | four-letter token matches Metropolitan* recipients; context |
| A08 | CONFIRMED | MDS | C06.E3 | {} | supporting | negative |  | SAM.gov public entity index has no METR registration; bounded (opt-out and sign-in blind spots stated) |
| A09 | CONFIRMED | MDS | C06.E3 | {} | supporting | negative |  | SAM.gov public entity index has no METR registration; bounded (opt-out and sign-in blind spots stated) |
| A10 | CONFIRMED | MDS | C06.E3 | {} | supporting | context |  | Entity Management API requires a key; retrieval cap; context |
| B01 | CONFIRMED | MDR | C06.E3;C04.E2 | {} | primary | evidence |  | NIST AI Consortium member list names 'Model Evaluation and Threat Research (METR, formerly ARC Evals)'; membership, not an award; no value or period |
| B02 | CONFIRMED | MDI | C06.E3;C04.E1;C04.E2 | {} | primary | evidence |  | CAISI March 2026 slide lists METR under 'CRADAs and DTAs — access to private benchmarks'; an agreement/in-kind access listing with no instrument number, value or period; also relevant to lab-independent access terms |
| B03 | CONFIRMED | MDP | C06.E3 | {} | supporting | evidence |  | NIST's general consortium CRADA requirement; METR's executed instrument is not published |
| B04 | CONFIRMED | MDS | C06.E3 | {} | supporting | negative |  | named CAISI documents do not name METR; bounded |
| B05 | CONFIRMED | MDS | C06.E3 | {} | supporting | negative |  | named CAISI documents do not name METR; bounded |
| B06 | DIFFERS | MDS | C06.E3 | {"source_class": "issuer statements"} | supporting | negative |  | Federal Register quoted-phrase search count 0; class corrected (government publication) |
| C01 | CONFIRMED | MDR | C06.E3 | {} | supporting | evidence |  | METR self-statement of California Cybersecurity Task Force membership; not an award |
| C02 | CONFIRMED | MDS | C06.E3 | {} | supporting | negative |  | Cal OES CCTF pages do not name METR and state membership is volunteer; bounded |
| C03 | CONFIRMED | MDS | C06.E3 | {} | supporting | context |  | California Grants Portal keyword filter not applied in static HTML; retrieval failure, not a negative; context |
| C04 | CONFIRMED | MDS | C06.E3 | {} | supporting | negative |  | CanadaBuys / NSF awardee queries: none; bounded |
| C05 | CONFIRMED | MDS | C06.E3 | {} | supporting | negative |  | CanadaBuys / NSF awardee queries: none; bounded |
| D01 | CONFIRMED | MDS | C06.E3 | {} | supporting | negative |  | no SAM registration recovered; correctly not typed as an award; bounded |
| D02 | CONFIRMED | MDP | C06.E3 | {} | primary | evidence |  | proposition: consortium membership / CRADA-DTA listing is not a procurement award; correctly stated |
| D03 | CONFIRMED | MDP | C06.E3 | {} | primary | evidence |  | proposition: consortium membership / CRADA-DTA listing is not a procurement award; correctly stated |
| E01 | CONFIRMED | MDS | C06.E3 | {} | supporting | negative |  | class-level coverage summary with blind spots stated |
| E02 | CONFIRMED | MDS | C06.E3 | {} | supporting | negative |  | class-level coverage summary with blind spots stated |
| E03 | CONFIRMED | MDS | C06.E3 | {} | supporting | negative |  | class-level coverage summary with blind spots stated |
| E04 | CONFIRMED | MDS | C06.E3 | {} | supporting | context |  | California routes: retrieval failures and no roster; context |
| E05 | CONFIRMED | MDS | C06.E3 | {} | supporting | negative |  | class-level coverage summary with blind spots stated |
