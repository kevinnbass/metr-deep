<!-- casework-review lane=research/grok-out/MD20-eu-ai-office-contract.csv -->

# Review of MD20 — eu ai office contract

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 070d4e58b609a48f8d9ae791c9037438c5957cd4491f25d12966da33e00ea107; goal state complete. Checked against the lane's saved TED 864574-2025 XML (LOT-0003 PayableAmount 1,167,484 EUR; tenderers EquiStamp Inc. (group lead), Model Evaluation and Threat Research, Inc., Epoch Artificial Intelligence, Inc.; contract 4500137790; conclusion 2025-12-15) and the saved FTS 2025 excerpt (EquiStamp as invoicing party). The award is typed as a contract in EUR with METR's share explicitly undisclosed; unpublished underlying documents are named with the Commission access-to-documents route and no request was filed.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| A01 | DIFFERS | MDF | C06.E3 | {"quantity_or_value": "1,167,484 EUR (LOT-0003 consortium total; METR share not disclosed)"} | primary | evidence |  | saved TED 864574-2025 XML rechecked locally: LOT-0003 PayableAmount 1167484 EUR; award to the EquiStamp-led consortium including Model Evaluation and Threat Research, Inc.; contract 4500137790; conclusion 2025-12-15; EUR kept as EUR; consortium total, not METR's share |
| A02 | CONFIRMED | MDE | C06.E3 | {} | primary | evidence |  | buyer identity from the notice: European Commission DG CNECT, AI Office department |
| A03 | CONFIRMED | MDF | C06.E3 | {} | primary | evidence |  | FTS 2025 row for 4500137790 names EquiStamp Inc. only (invoicing party); same EUR 1,167,484; not an additional amount; ledger in_kind_contracts |
| A04 | CONFIRMED | MDP | C06.E3 | {} | supporting | evidence |  | metr.org/about names the contract without amount; recipient statement |
| A05 | CONFIRMED | MDS | C06.E3 | {} | primary | evidence |  | TED expert search: one notice for the METR legal name; coverage receipt |
| B01 | CONFIRMED | MDP | C06.E3 | {} | primary | evidence |  | consortium composition and METR's non-lead role from the XML; share not disclosed; do not infer one-third |
| B02 | CONFIRMED | MDP | C06.E3 | {} | supporting | evidence |  | subcontracting flagged with unknown value/percentage; not METR's share |
| B03 | CONFIRMED | MDP | C06.E3 | {} | primary | evidence |  | FTS lists the invoicing party only; METR share undisclosed; correctly bounded |
| C01 | CONFIRMED | MDS | C06.E3 | {} | supporting | evidence |  | archived primary with sha256; coverage receipt |
| C02 | CONFIRMED | MDS | C06.E3 | {} | supporting | evidence |  | archived primary with sha256; coverage receipt |
| C03 | CONFIRMED | MDS | C06.E3 | {} | supporting | evidence |  | archived primary with sha256; coverage receipt |
| C04 | CONFIRMED | MDS | C06.E3 | {} | supporting | evidence |  | archived primary with sha256; coverage receipt |
| C05 | CONFIRMED | MDS | C06.E3 | {} | supporting | context |  | related procedure notices returned WAF 202; route failure; context |
| D01 | CONFIRMED | MDP | C06.E3 | {} | supporting | context |  | unpublished underlying document named with the Commission access-to-documents route; no request filed or sent; MD44 owns any draft; context |
| D02 | CONFIRMED | MDP | C06.E3 | {} | supporting | context |  | unpublished underlying document named with the Commission access-to-documents route; no request filed or sent; MD44 owns any draft; context |
| D03 | CONFIRMED | MDP | C06.E3 | {} | supporting | context |  | unpublished underlying document named with the Commission access-to-documents route; no request filed or sent; MD44 owns any draft; context |
| E01 | CONFIRMED | MDS | C06.E3 | {} | primary | negative |  | FTS 2025 has no METR-named beneficiary; bounded with the invoicing-party caveat |
| E02 | CONFIRMED | MDS | C06.E3 | {} | supporting | negative |  | FTS 2024 none; bounded (contract concluded 2025-12-15) |
| E03 | CONFIRMED | MDS | C06.E3 | {} | supporting | negative |  | TED winner-name ARC/ARC Evals none; bounded |
| E04 | CONFIRMED | MDS | C06.E3 | {} | supporting | context |  | four-letter token matches unrelated operators; legal-name search is the responsive query; context |
| E05 | CONFIRMED | MDS | C06.E3 | {} | supporting | context |  | route failure or scope note, not a content negative; context |
| E06 | CONFIRMED | MDS | C06.E3 | {} | supporting | context |  | route failure or scope note, not a content negative; context |
| E07 | CONFIRMED | MDS | C06.E3 | {} | supporting | evidence |  | source-coverage receipt |
