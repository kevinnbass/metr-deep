# S3 adversarial entity-distinction check (2026-09-16)

Pairs of legal entities that must never be merged were searched across the promoted MDE/MDR/MDQ/MDF/MDI rows; a row is flagged when it names both members of a pair without an explicit separation statement in its own text or note.

FLAGGED: 28

| row_id | table | pair | text |
|---|---|---|---|
| MDE0035 | entities.csv | Alignment Research Center|ARC Evals vs METR|Model Evaluation and Threat Research | Alignment Research Center is a distinct legal recipient from METR Inc Longview public fund / Effektiv Spenden Giving Fund ARC Evals project of Alignment Research Center (2023); later METR Inc   2023 money was described a |
| MDR0020 | relationships.csv | Alignment Research Center|ARC Evals vs METR|Model Evaluation and Threat Research | related tax-exempt organization Alignment Research Center Alignment Research Center Model Evaluation and Threat Research Inc   one related tax-exempt org related organization related tax-exempt organization (Schedule R); |
| MDR0035 | relationships.csv | Alignment Research Center|ARC Evals vs METR|Model Evaluation and Threat Research | Frontier AI Taskforce second progress report lists ARC Evals among announced partnerships — still no value Frontier AI Taskforce ARC Evals  Frontier AI Taskforce ARC Evals remains in the partnership list; no METR/ARC Eva |
| MDR0047 | relationships.csv | Redwood vs METR | Ryan Greenblatt (Redwood Research) thanks line and non-public-access footnote Ryan Greenblatt Redwood Research   Ryan Greenblatt parenthesized as Redwood Research; fn66: did not have non-public access; program restricted |
| MDR0075 | relationships.csv | Redwood vs METR | Ryan Greenblatt affiliation at report date as parenthesized in the report: Redwood Research Ryan Greenblatt Redwood Research   Dated public affiliation at publication is Redwood Research per the report. fn66: no non-publ |
| MDR0079 | relationships.csv | Redwood vs METR | Redwood Research @redwood_ai 2026-09-12: own statement that several Redwood staff have been subcontracted by METR onto this investigation Redwood Research Anthropic, PBC Model Evaluation and Threat Research, Inc. Anthrop |
| MDQ0018 | project_coi.csv | Redwood vs METR | HF: OpenAI held a redaction right over any non-public information in METR's post    OpenAI OpenAI held a redaction right on this public METR/Redwood post   |
| MDQ0040 | project_coi.csv | Redwood vs METR | Ryan Greenblatt / Beth Barnes disclosed close personal relationship (HF blog footnote 2, added 2026-09-13) Ryan Greenblatt Beth Barnes  OpenAI METR public footnote; Greenblatt is Redwood staff contracting with METR; Barn |
| MDF0007 | funding_events.csv | Alignment Research Center|ARC Evals vs METR|Model Evaluation and Threat Research |  Alignment Research Center METR      |
| MDF0013 | funding_events.csv | Alignment Research Center|ARC Evals vs METR|Model Evaluation and Threat Research |  Longview Philanthropy (public fund) METR (then ARC Evals, division of ARC)      |
| MDF0014 | funding_events.csv | Alignment Research Center|ARC Evals vs METR|Model Evaluation and Threat Research |  Effektiv Spenden (Giving Fund: Safeguarding the future) ARC Evals / METR      |
| MDF0034 | funding_events.csv | Alignment Research Center|ARC Evals vs METR|Model Evaluation and Threat Research | Alignment Research Center contribution from related organization (Part VIII / Schedule R type C) Alignment Research Center Model Evaluation and Threat Research Inc   named related-organization contribution  related tax-e |
| MDF0065 | funding_events.csv | Alignment Research Center|ARC Evals vs METR|Model Evaluation and Threat Research | ARC FY2024 Schedule I non-cash assistance to METR (computers) Alignment Research Center Model Evaluation and Threat Research Inc   Schedule I non-cash assistance filed   |
| MDF0070 | funding_events.csv | Alignment Research Center|ARC Evals vs METR|Model Evaluation and Threat Research | Longview Aug 2023 public-fund grant report: ARC Evals / METR $220,000 Longview Philanthropy (public fund / Longtermism Fund later ECF) ARC Evals (now called METR), then a project of Alignment Research Center Giving What  |
| MDF0071 | funding_events.csv | Alignment Research Center|ARC Evals vs METR|Model Evaluation and Threat Research | GWWC ARC Evals locator restating Longview $220,000 recommendation Longview Philanthropy (public fund) METR (then ARC Evals)   GWWC restates Longview recommended $220,000 from its public fund in 2023  third-party locator  |
| MDF0072 | funding_events.csv | Alignment Research Center|ARC Evals vs METR|Model Evaluation and Threat Research | Effektiv Spenden Giving Fund: Safeguarding the future — 128.000 € to METR/ARC Evals Effektiv Spenden Giving Fund: Safeguarding the future (brand/fund) METR (formerly ARC Evals)   128.000 EUR; August 2023; fund name Safeg |
| MDF0076 | funding_events.csv | Alignment Research Center|ARC Evals vs METR|Model Evaluation and Threat Research | Giving What We Can charities sitemap enumeration Longview Philanthropy METR (formerly called ARC Evals)   GWWC sitemap-0 has 1489 loc; charities/arc-evals present; charities/metr HTTP 404. Charity page titles METR (forme |
| MDF0077 | funding_events.csv | Alignment Research Center|ARC Evals vs METR|Model Evaluation and Threat Research | Future of Life Institute grant-sitemap enumeration Future of Life Institute Alignment Research Center   FLI grant-sitemap n=154; one Alignment Research Center loc; zero METR/Model Evaluation loc. WP REST /wp/v2/grant 404 |
| MDF0082 | funding_events.csv | Alignment Research Center|ARC Evals vs METR|Model Evaluation and Threat Research | Longview public-fund recommendation of $220,000 in 2023 as quoted on GWWC Longview Philanthropy METR (formerly called ARC Evals)   GWWC records a 2023 Longview public-fund recommendation of $220,000 to METR/ARC Evals   |
| MDF0085 | funding_events.csv | Alignment Research Center|ARC Evals vs METR|Model Evaluation and Threat Research | EA Funds LTFF 2022 Q4 grant to Alignment Research Center Long-Term Future Fund Alignment Research Center   One LTFF CSV row: Alignment Research Center $72,000 in 2022 Q4. No METR Inc row.   |
| MDF0186 | funding_events.csv | DAF sponsor|National Philanthropic Trust|Silicon Valley Community Foundation|Vanguard Charitable vs adviser|account principal|donor-advised account | National Philanthropic Trust FY2025 Schedule I cash grant to RAND (held amount; purpose not Canary) National Philanthropic Trust RAND Corporation   1 RAND RecipientTable; CashGrantAmt=61646790; purpose CULTURE & ARTS (do |
| MDF0187 | funding_events.csv | DAF sponsor|National Philanthropic Trust|Silicon Valley Community Foundation|Vanguard Charitable vs adviser|account principal|donor-advised account | Fidelity Investments Charitable Gift Fund FY2025 Schedule I cash grant to RAND (held amount; purpose not Canary) Fidelity Investments Charitable Gift Fund RAND Corporation   1 RAND RecipientTable; CashGrantAmt=18202491;  |
| MDF0201 | funding_events.csv | Alignment Research Center|ARC Evals vs METR|Model Evaluation and Threat Research | GWWC locator restating Longview $220,000 recommendation Longview Philanthropy (public fund) METR (then ARC Evals)   GWWC restates Longview recommended $220,000 with quoted purpose   |
| MDF0202 | funding_events.csv | Alignment Research Center|ARC Evals vs METR|Model Evaluation and Threat Research | Effektiv Spenden Safeguarding-the-future regrant purpose (Wayback id_ of funder page) Effektiv Spenden Giving Fund: Safeguarding the future METR (formerly ARC Evals)   128.000 EUR August 2023; purpose Evaluation of state |
| MDF0211 | funding_events.csv | DAF sponsor|National Philanthropic Trust|Silicon Valley Community Foundation|Vanguard Charitable vs adviser|account principal|donor-advised account | Vanguard Charitable FY2025 Schedule I cash grant to METR (DAF sponsor, principal undisclosed) Vanguard Charitable Endowment Program Model Evaluation and Threat Research   1 METR RecipientTable; CashGrantAmt displayed 4,0 |
| MDI0004 | in_kind_access.csv | Alignment Research Center|ARC Evals vs METR|Model Evaluation and Threat Research | AISI approach-to-evaluations (GOV.UK) quotes working with METR (formerly ARC Evals), including unpublished METR work at the Summit — unquantified AI Safety Institute / AI Security Institute METR  AI Safety Institute (UK) |
| MDI0009 | in_kind_access.csv | Redwood vs METR | OpenAI/Hugging Face investigation: message-board dump, transcripts, Sol credits, on-premises days OpenAI METR Redwood Research (Ryan Greenblatt contracting with METR) OpenAI access as described; credits are in_kind_estim |
| MDI0056 | in_kind_access.csv | Redwood vs METR | OpenAI Hugging Face technical report: worked with METR and Redwood; no credit amount OpenAI METR  OpenAI verbatim; continues 'Redwood Research to conduct a third-party assessment'   |

ADJUDICATION (reviewer; persisted in S3-ENTITY-ADJUDICATIONS.json; a flagged row without an entry is unresolved until the reviewer adds one):
MDE0035 -> resolved: the row is itself the separation statement (ARC a distinct legal recipient from METR Inc)
MDR0020 -> resolved: Schedule R related-organization relationship between two distinct EINs (ARC 86-3605182; METR 99-1219864); relationship, not merger
MDR0035 -> resolved: ARC Evals named as METR's historical alias by the UK taskforce; note keeps ARC the 501(c)(3) unmerged
MDR0047 -> resolved: Greenblatt's employer Redwood Research recorded as distinct from METR; fn66 states no non-public access
MDR0075 -> resolved: note says do not treat Redwood Research and METR as the same legal entity
MDR0079 -> resolved: Redwood's own statement that its staff are subcontracted by METR; subcontract is a relationship between separate entities
MDQ0018 -> resolved: OpenAI redaction right over a METR/Redwood joint post; entities named as co-authors, not merged
MDQ0040 -> resolved: METR's own footnote names Greenblatt as Redwood staff contracting with METR and Barnes as METR CEO; personal relationship between people, entities separate
MDF0007 -> resolved: seed context row for an ARC->METR transfer between two EINs; role context
MDF0013 -> resolved: recipient alias 'METR (then ARC Evals, division of ARC)' is the recipient's own history; ARC the 501(c)(3) kept separate in the note
MDF0014 -> resolved: same alias statement (Effektiv Spenden regrant to the ARC Evals project, later METR); context row
MDF0034 -> resolved: METR 990 Part VIII/Schedule R contribution from related organization ARC (EIN stated); typed transfer between separate entities
MDF0065 -> resolved: ARC FY2024 Schedule I non-cash assistance to METR (computers); two EINs, separate
MDF0070 -> resolved: Longview 2023 grant to 'ARC Evals (now called METR), then a project of ARC'; alias history stated on the row
MDF0071 -> resolved: GWWC locator restating the same alias; context
MDF0072 -> resolved: Effektiv Spenden regrant to METR (formerly ARC Evals); alias stated; regrant typed
MDF0076 -> resolved: GWWC sitemap enumeration naming 'METR (formerly called ARC Evals)'; alias
MDF0077 -> resolved: FLI grant to Alignment Research Center recorded as an ARC award (C06), METR none-found separately; not merged
MDF0082 -> resolved: Longview recommendation naming the alias; alias
MDF0085 -> resolved: LTFF grant to Alignment Research Center explicitly 'not a METR Inc award'
MDF0186 -> resolved: NPT->RAND grant; note states a payment to RAND is not a payment to METR; DAF adviser not identified
MDF0187 -> resolved: Fidelity Charitable->RAND grant; same separation; adviser not identified
MDF0201 -> resolved: GWWC locator restating the alias; context
MDF0202 -> resolved: Effektiv Spenden regrant purpose row; alias; regrant typed
MDF0211 -> resolved: Vanguard Charitable Schedule I grant to METR with 'principal undisclosed' stated; sponsor and account kept separate
MDI0004 -> resolved: AISI/GOV.UK text 'METR (formerly ARC Evals)'; alias quoted from the source
MDI0009 -> resolved: OpenAI in-kind to METR with a Redwood contractor on premises; Redwood named as a separate contracting entity
MDI0056 -> resolved: OpenAI technical report 'worked with METR and Redwood'; two named counterparties, not merged

UNRESOLVED: 0
