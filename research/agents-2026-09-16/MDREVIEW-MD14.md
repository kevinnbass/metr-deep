<!-- casework-review lane=research/grok-out/MD14-six-month-chronology.csv -->

# Review of MD14 — six month chronology

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 b6653b8b950218211b46b5fb05ce2f86fdd49c83979cb24d21501e9d1f7f6529; goal state complete. Denominator and reconciliation lane. The approximately $71 million sentence was live-checked on 2026-09-16; the Packard award compatibility rests on the 2026 award year and the July catalog listing, stated as such; every exclusion proposition (C03-C26) was checked against the row already promoted by its owning lane (MD01, MD07, MD08, MD09, MD10, MD11) or the seed context; SFF further-opportunities and Effektiv Spenden pages were live-checked; the identified compatible total is $350,000 and the unresolved remainder is around $70.65 million (D01), typed as an arithmetic residual, not a donor list. Duplicate Packard rows are context; C04's quote is corrected to the RelatedOrganizationsAmt tag; C15's url, which the rewrite pointed at the pack's seed file, is corrected to the sponsor's rendered Schedule I; route failures are context.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| A01 | CONFIRMED | MDF | C01.E1 | {} | primary | evidence |  | live page checked 2026-09-16: sentence verbatim; the denominator row for C01 |
| A02 | CONFIRMED | MDT | C01.E1;C09.E3 | {} | supporting | evidence |  | JSON-LD datePublished 2026-08-14; statement date, not a transaction date |
| A03 | CONFIRMED | MDP | C01.E1;C01.E3 | {} | supporting | evidence |  | correctly separates the over-the-years thank-you from the six-month total |
| A04 | DIFFERS | MDP | C01.E3 | {"subject": "about-page supporter list is not a dated funding event and not an allocation of the total", "edge_type": "acknowledgment list; no amounts or dates"} | supporting | context |  | retargeted from MDE to MDP: a proposition about the list, not an entity |
| B01 | DIFFERS | MDF | C01.E2;C01.E3 | {"date": "2026", "date_precision": "year", "period": "award year 2026; catalog listing published 2026-07-06T06:09:41Z (page metadata, not the instrument date)"} | supporting | context |  | same award as MD02 row A01 (already promoted); the listing timestamp is moved out of the date field so a page date is not read as the commitment date; bound as context so one award is one funding event |
| B02 | CONFIRMED | MDF | C01.E2 | {} | supporting | context |  | same award as MD02 A01; context |
| B03 | CONFIRMED | MDF | C01.E2 | {} | supporting | context |  | same award, API enumeration; context |
| B04 | DIFFERS | MDF | C01.E3;C02.E5 | {"ledger": "commitments", "date_precision": "day", "quantity_or_value": "$220,000 in the $5M-additional column; $1,210,000 in the $15M-additional column; not summed"} | supporting | evidence |  | live page checked 2026-09-16: METR row shows $220,000 and $1,210,000 under the two scenario columns; the lane's saved copy carries 'Last Published: Sat Feb 15 2025', confirming the 2025-02-15 page date; retargeted from MDT to MDF as a recommendation-type row |
| C01 | CONFIRMED | MDP | C01.E3 | {} | supporting | context |  | the denominator is not one of its own components; context |
| C02 | CONFIRMED | MDP | C01.E2 | {} | primary | evidence |  | Packard $350,000 is the only identified compatible component; compatibility of period rests on the 2026 award year and the July listing, not on an instrument date, as the row states |
| C03 | CONFIRMED | MDP | C01.E3 | {} | primary | evidence |  | filed FY2024 revenue excluded: not a commitment, period before the window; amount verified in MD01 |
| C04 | DIFFERS | MDP | C01.E3 | {"url": "https://apps.irs.gov/pub/epostcard/990/xml/2025/2025_TEOS_XML_11C.zip", "quote_300": "<RelatedOrganizationsAmt>4501424</RelatedOrganizationsAmt>"} | primary | evidence |  | the lane's quote was the revenue total; the transfer amount is the RelatedOrganizationsAmt tag verified in MD01's saved XML; exclusion reasoning stands |
| C05 | CONFIRMED | MDP | C01.E3 | {} | supporting | evidence |  | Audacious ~$38M joint-project commitment excluded; amount from the seed context, re-collection owned by MD16 |
| C06 | CONFIRMED | MDP | C01.E3 | {} | supporting | evidence |  | ~$17M METR share excluded; subset of the joint commitment; MD16/MD18 own the re-collection |
| C07 | CONFIRMED | MDP | C01.E3 | {} | supporting | evidence |  | 'a bit under $16m' restatement excluded; MD18 owns the re-collection |
| C08 | CONFIRMED | MDP | C01.E3 | {} | supporting | evidence |  | run rate is not an inbound amount |
| C09 | CONFIRMED | MDP | C01.E3 | {} | supporting | evidence |  | runway is not a funding event |
| C10 | CONFIRMED | MDP | C01.E3 | {} | supporting | evidence |  | SFF-2024 recommendation excluded; MD09 owns the re-collection |
| C11 | CONFIRMED | MDP | C01.E3 | {} | supporting | evidence |  | SFF-2025 recommendation excluded; two figures not summed |
| C12 | CONFIRMED | MDP | C01.E3 | {} | primary | evidence |  | further-opportunities figures excluded; verified live 2026-09-16 |
| C13 | CONFIRMED | MDP | C01.E3 | {} | supporting | evidence |  | Founders Pledge 2024 filed grant excluded; 2024 period |
| C14 | CONFIRMED | MDP | C01.E3 | {} | primary | evidence |  | SVCF $20,000 TY2024 excluded; verified in MD11 |
| C15 | DIFFERS | MDP | C01.E3 | {"url": "https://projects.propublica.org/nonprofits/full_text/202621329349306657/IRS990ScheduleI", "quote_300": "RecipientTable[15424]/CashGrantAmt[1]\">4,000,000"} | primary | evidence |  | the revised lane row cites the pack's own seed-import file as its url; corrected to the sponsor's rendered Schedule I (verified in MD11); exclusion reasoning stands: FY ends 2025-06-30, before the window, and the sponsor discloses no account principal |
| C16 | CONFIRMED | MDP | C01.E3 | {} | primary | evidence |  | Longview 2023 recommendation excluded; verified live in MD07 review |
| C17 | CONFIRMED | MDP | C01.E3 | {} | primary | evidence |  | Effektiv Spenden EUR 128,000 August 2023 excluded; verified live by this reviewer 2026-09-16; the revised lane row cites the Wayback 2025-01-26 capture, which is a valid archive URL; EUR never converted |
| C18 | CONFIRMED | MDP | C01.E3;C06.E1 | {} | supporting | evidence |  | Valhalla $10M to RAND excluded; a payment to RAND is not a payment to METR |
| C19 | CONFIRMED | MDP | C01.E3;C06.E1 | {} | supporting | evidence |  | High Tide $333,334 to RAND excluded |
| C20 | CONFIRMED | MDP | C01.E3;C01.E2 | {} | primary | evidence |  | Jane Street individuals: no public amount or date; not an addend; verified in MD07 |
| C21 | CONFIRMED | MDP | C01.E3 | {} | primary | evidence |  | named individuals: no public amounts; verified in MD08 |
| C22 | CONFIRMED | MDP | C01.E3;C06.E3 | {} | supporting | evidence |  | UK AISI arrangement undisclosed; MD19 owns the procurement search |
| C23 | CONFIRMED | MDP | C01.E3;C06.E3 | {} | supporting | evidence |  | EU AI Office contract, EUR, consortium share undisclosed; MD20 owns the TED notice |
| C24 | CONFIRMED | MDP | C01.E3 | {} | supporting | evidence |  | API credits are an in-kind estimate dated after the statement; excluded |
| C25 | CONFIRMED | MDP | C01.E3 | {} | supporting | evidence |  | the lane's saved copy of the Coefficient staff page contains 'not a Coefficient Giving grantee.' (live page returned 403 to this reviewer); no Coefficient amount to add |
| C26 | CONFIRMED | MDP | C01.E3 | {} | primary | evidence |  | named foundations other than Packard have no public in-window amount; verified in MD03-MD06 |
| D01 | CONFIRMED | MDP | C01.E4 | {} | primary | evidence |  | identified compatible total $350,000 (Packard only) against a denominator of around $71,000,000; unresolved remainder around $70,650,000; arithmetic over the C rows; no imputed allocation |
| D02 | DIFFERS | MDP | C01.E4 | {"edge_type": "arithmetic residual of the commitment statement; not an unidentified donor list", "documented_transaction": "no"} | supporting | evidence |  | retargeted from MDT to MDP: the remainder is a proposition, not a dated event; asking for its composition is embargoed to S6 |
| E01 | CONFIRMED | MDS | C01.E2;C01.E3 | {} | supporting | context |  | route failure (/grants 404, redirect to a job page); MD13 owns the index enumeration; context |
| E02 | CONFIRMED | MDS | C01.E3 | {} | supporting | negative |  | index_2026 has no METR return; bounded to the posting-year index |
| E03 | CONFIRMED | MDS | C01.E2 | {} | supporting | negative |  | no published SFF-2026 recommendations page at check time; bounded |
| E04 | CONFIRMED | MDS | C01.E2;C06.E3 | {} | supporting | negative |  | USAspending grants-only keyword POST returned no results for the window; keyword not UEI search, as stated |
| E05 | CONFIRMED | MDS | C01.E2 | {} | supporting | context |  | grants.gov JS shell; route failure; context |
| E06 | CONFIRMED | MDS | C01.E2 | {} | supporting | context |  | legacy Open Philanthropy grants query redirects to a funds page; context |
| E07 | CONFIRMED | MDS | C01.E3 | {} | supporting | context |  | TED notice fetch returned 202 empty; route failure; MD20 owns it; context |
| E08 | CONFIRMED | MDS | C01.E2 | {} | supporting | context |  | Packard search endpoint empty body; the award was found by enumeration; context |
| E09 | CONFIRMED | MDS | C01.E1;C09.E1 | {} | supporting | evidence |  | Wayback CDX shows three 200 captures of the funding-update URL (2026-08-27, 08-30, 09-14); archive coverage of the statement |
