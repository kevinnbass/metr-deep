<!-- casework-review lane=research/grok-out/MD08-named-individual-donors.csv -->

# Review of MD08 — named individual donors

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 e5a257965f025f5c52b17d6b76f37f21675c6efa011eec16b1f740fe1676b797; goal state complete. Checked against the saved Wayback id_ captures (2025-12-07 names Ralston only; 2025-12-16 adds Farhi and Field; 2026-06-01 adds Newman; the 'individuals directly' wording is on the 2025 captures), the live metr.org pages, the saved Form 4 XMLs and the FEC receipt. Acknowledgments are typed with amount, date and vehicle undisclosed; person-role rows are retargeted from MDE to MDR; the Figma-share DAF gifts are MDP propositions with no onward transaction to METR; undated window rows are MDS negatives.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| 1 | DIFFERS | MDF | C02.E2 | {"payment_status": "acknowledged as a supporter; amount, date, vehicle and money type not disclosed by the source", "date_precision": "day"} | primary | evidence |  | metr.org/about live-checked 2026-09-16 names David Farhi among 'many others'; acknowledgment typed; the date is the check date not a gift date |
| 2 | DIFFERS | MDF | C02.E2 | {"payment_status": "acknowledged as a supporter; amount, date, vehicle and money type not disclosed by the source", "date_precision": "day"} | supporting | evidence |  | 2026-08-14 funding update names David Farhi; second document for the same acknowledgment |
| 3 | DIFFERS | MDF | C02.E2 | {"payment_status": "acknowledged as a supporter; amount, date, vehicle and money type not disclosed by the source", "date_precision": "day"} | primary | evidence |  | metr.org/about live-checked 2026-09-16 names Geoff Ralston among 'many others'; acknowledgment typed; the date is the check date not a gift date |
| 4 | DIFFERS | MDF | C02.E2 | {"payment_status": "acknowledged as a supporter; amount, date, vehicle and money type not disclosed by the source", "date_precision": "day"} | supporting | evidence |  | 2026-08-14 funding update names Geoff Ralston; second document for the same acknowledgment |
| 5 | DIFFERS | MDF | C02.E2 | {"payment_status": "acknowledged as a supporter; amount, date, vehicle and money type not disclosed by the source", "date_precision": "day"} | primary | evidence |  | metr.org/about live-checked 2026-09-16 names Dylan Field among 'many others'; acknowledgment typed; the date is the check date not a gift date |
| 6 | DIFFERS | MDF | C02.E2 | {"payment_status": "acknowledged as a supporter; amount, date, vehicle and money type not disclosed by the source", "date_precision": "day"} | supporting | evidence |  | 2026-08-14 funding update names Dylan Field; second document for the same acknowledgment |
| 7 | DIFFERS | MDF | C02.E2 | {"payment_status": "acknowledged as a supporter; amount, date, vehicle and money type not disclosed by the source", "date_precision": "day"} | primary | evidence |  | metr.org/about live-checked 2026-09-16 names Steve Newman among 'many others'; acknowledgment typed; the date is the check date not a gift date |
| 8 | DIFFERS | MDF | C02.E2 | {"payment_status": "acknowledged as a supporter; amount, date, vehicle and money type not disclosed by the source", "date_precision": "day"} | supporting | evidence |  | 2026-08-14 funding update names Steve Newman; second document for the same acknowledgment |
| 9 | CONFIRMED | MDT | C02.E2;C09.E1 | {} | primary | evidence |  | Wayback id_ 2025-12-07 capture names Ralston only among these four |
| 10 | CONFIRMED | MDT | C02.E2;C09.E1 | {} | primary | evidence |  | Wayback id_ 2025-12-16 capture adds Farhi and Field |
| 11 | CONFIRMED | MDT | C02.E2;C09.E1 | {} | primary | evidence |  | Wayback id_ 2026-06-01 capture adds Newman |
| 12 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | supporting | negative |  | WIRED 2026-07-15 first-person quote is about AI regulation, not a METR gift; bounded |
| 13 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | no first-person METR gift statement found; capped searches stated |
| 14 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | X from:geoffralston search none; capped |
| 15 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | X from:zoink search none; capped |
| 16 | CONFIRMED | MDS | C02.E2 | {} | supporting | negative |  | X from:snewmanpv search none; capped |
| 17 | DIFFERS | MDT | C02.E2;C03.E3;C09.E1 | {"relationship_type": "recipient page wording 'a wide range of individuals directly' on the 2025-12-16 capture; live page says 'many others, such as'"} | supporting | evidence |  | retargeted from MDF to MDT: a wording change is a timeline fact, not a funding event |
| 18 | DIFFERS | MDP | C02.E2;C03.E3 | {"edge_type": "stock gift to an unnamed donor-advised fund; no onward transaction to METR documented", "documented_transaction": "yes, to a donor-advised fund; not to METR", "to_entity": "unnamed donor-advised fund"} | supporting | context |  | retargeted from MDF to MDP: Form 4 2025-11-28 gift to a DAF does not name METR; adviser not identified |
| 19 | DIFFERS | MDP | C02.E2;C03.E3 | {"edge_type": "stock gift to an unnamed donor-advised fund; no onward transaction to METR documented", "documented_transaction": "yes, to a donor-advised fund; not to METR", "to_entity": "unnamed donor-advised fund"} | supporting | context |  | retargeted from MDF to MDP: Form 4 2026-08-17 gift to a DAF does not name METR |
| 20 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | supporting | negative |  | no Farhi-named vehicle found; bounded |
| 21 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | supporting | negative |  | no Ralston-named 990-PF; SAIF is a VC fund; bounded |
| 22 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | supporting | negative |  | Form 4 DAF gifts do not name METR; no Field-named filer; bounded |
| 23 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | supporting | negative |  | homonym foundations excluded; bounded |
| 24 | CONFIRMED | MDE | C02.E2 | {} | supporting | context |  | SAIF is a for-profit fund, not a METR vehicle; context |
| 25 | DIFFERS | MDR | C02.E2 | {"relationship_type": "named among AVERI's funders on averi.org/about; not a METR vehicle", "to_entity": "AVERI"} | supporting | context |  | retargeted from MDF to MDR: an acknowledgment by a different organisation is a relationship, not a METR funding event |
| 26 | DIFFERS | MDR | C03.E3;C02.E2 | {"relationship_type": "former OpenAI research manager; left summer 2025 per WIRED 2026-07-15", "to_entity": "OpenAI"} | supporting | evidence |  | retargeted from MDE to MDR: person-role fact; press-reported departure |
| 27 | DIFFERS | MDR | C03.E3 | {"relationship_type": "self-reported employer SELF EMPLOYED, occupation RESEARCH MANAGER on a 2026-06-16 FEC Schedule A receipt", "to_entity": "Guardrails Alliance (political committee; not METR)"} | primary | evidence |  | retargeted from MDE to MDR; FEC used only to corroborate employment on a dated record, as the brief allows; the $3,000 is a political receipt |
| 28 | DIFFERS | MDR | C03.E3 | {"relationship_type": "third-party profile title 'Technical Lead, OpenAI', undated and stale-prone", "to_entity": "OpenAI"} | supporting | context |  | retargeted to MDR; context only |
| 29 | DIFFERS | MDR | C03.E3 | {"relationship_type": "historical contributor credit on OpenAI's o1 page", "to_entity": "OpenAI"} | supporting | context |  | retargeted to MDR; context only |
| 30 | DIFFERS | MDR | C02.E2;C03.E3 | {"relationship_type": "President & CEO of Figma, Inc. per Form 4 2026-08-17", "to_entity": "Figma, Inc."} | supporting | evidence |  | retargeted from MDE to MDR; employer distinct from any DAF and from METR |
| 31 | DIFFERS | MDR | C02.E2 | {"relationship_type": "former Y Combinator president; SAIF founder per TechCrunch 2025-04-17", "to_entity": "Safe Artificial Intelligence Fund"} | supporting | evidence |  | retargeted to MDR |
| 32 | DIFFERS | MDR | C02.E2 | {"relationship_type": "self-described chairman and president of Golden Gate Institute for AI", "to_entity": "Golden Gate Institute for AI"} | supporting | evidence |  | retargeted to MDR |
| 33 | DIFFERS | MDR | C02.E2 | {"relationship_type": "listed on Epoch AI board of directors", "to_entity": "Epoch AI"} | supporting | evidence |  | retargeted to MDR; board role, not a gift |
| 34 | CONFIRMED | MDS | C03.E3;C02.E2 | {} | supporting | negative |  | employment at gift date undeterminable because no gift date is disclosed; bounded |
| 35 | CONFIRMED | MDS | C03.E3;C02.E2 | {} | supporting | negative |  | as row 34 |
| 36 | CONFIRMED | MDS | C03.E3;C02.E2 | {} | supporting | negative |  | as row 34 |
| 37 | CONFIRMED | MDS | C03.E3;C02.E2 | {} | supporting | negative |  | as row 34 |
| 38 | DIFFERS | MDS | C02.E2;C01.E3 | {"result": "gift date not disclosed; cannot be placed inside or outside the February-August 2026 window"} | supporting | negative |  | retargeted from MDT to MDS: an undated fact is source coverage, not a timeline event |
| 39 | DIFFERS | MDS | C02.E2;C01.E3 | {"result": "gift date not disclosed; cannot be placed inside or outside the February-August 2026 window"} | supporting | negative |  | retargeted to MDS |
| 40 | DIFFERS | MDS | C02.E2;C01.E3 | {"result": "gift date not disclosed; cannot be placed inside or outside the February-August 2026 window"} | supporting | negative |  | retargeted to MDS |
| 41 | DIFFERS | MDS | C02.E2;C01.E3 | {"result": "gift date not disclosed; cannot be placed inside or outside the February-August 2026 window"} | supporting | negative |  | retargeted to MDS |
| 42 | CONFIRMED | MDT | C03.E1;C03.E3 | {} | supporting | evidence |  | employee-donation rule present on live about and donate pages 2026-09-16; wording matches the live check |
| 43 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | primary | negative |  | Schedule B RESTRICTED on the saved FY2024 XML; verification boundary |
| 44 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | supporting | negative |  | ProPublica org search none; locator negative |
| 45 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | supporting | negative |  | ProPublica org search none; locator negative |
| 46 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | supporting | negative |  | ProPublica org search none; locator negative |
| 47 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | supporting | negative |  | homonym filers excluded; locator negative |
| 48 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | supporting | negative |  | structural boundary: Schedule I carries no adviser field; bounded |
| 49 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | supporting | context |  | route failure (TEOS 403); context |
| 50 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | supporting | context |  | entity registry, not a donor ledger; context |
| 51 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | supporting | negative |  | no SEC filing names METR; bounded |
| 52 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | supporting | negative |  | CourtListener 0 results; bounded |
| 53 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | supporting | context |  | route failure (redirect to a job page); context |
| 54 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | supporting | context |  | GET 405 on a POST endpoint; individuals outside procurement scope; context |
| 55 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | supporting | context |  | EA Forum search is a JS shell; context |
| 56 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | primary | negative |  | METR pages give no per-person amount, date or vehicle; bounded |
| 57 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | supporting | context |  | search path 404; context |
| 58 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | supporting | context |  | homepage is not a member directory; context |
| 59 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | supporting | context |  | record that this lane sent nothing (embargo); not a source check; context |
| 60 | CONFIRMED | MDS | C02.E2;C03.E3 | {} | supporting | negative |  | press class bounded negative |
