<!-- casework-review lane=research/grok-out/MD32-lab-money-negative-sweep.csv -->

# Review of MD32 — lab money negative sweep

Reviewing agent: Claude (parent session), 2026-09-16. Lane CSV sha256 e6c63a9f07763777e83a3c9df75c946913adfdfa3f2c955ec152a95c644ced2b; goal state complete. Checked against the lane's saved live metr.org pages (about, donate, home, funding update, Hugging Face incident post; rule quotes verified verbatim), the saved METR FY2024 Form 990 XML (no named lab payer; CYProgramServiceRevenueAmt 0; RelatedOrganizationsAmt from ARC, not a lab), the OpenAI Foundation TY2024 Form 990 Schedule I XML (no METR grant), the Wayback captures already promoted from MD24, and the named-lab and foundation pages. Every lab, foundation and DAF sponsor is kept a separate legal entity; access and tokens are in-kind and never typed as payments; the DAF public-verification stop is bound as a proposition; route failures are context.

| row | verdict | target_prefix | element_ids | primary_values | strength | role | supersedes | note |
|---|---|---|---|---|---|---|---|---|
| A01 | CONFIRMED | MDT | C03.E1 | {} | primary | evidence |  | dated METR self-statement of its funding/compensation rule (quote verified in the saved live page); free tokens/access disclosed and not typed as a payment |
| A02 | CONFIRMED | MDT | C03.E1 | {} | primary | evidence |  | dated METR self-statement of its funding/compensation rule (quote verified in the saved live page); free tokens/access disclosed and not typed as a payment |
| A03 | CONFIRMED | MDT | C03.E1 | {} | primary | evidence |  | dated METR self-statement of its funding/compensation rule (quote verified in the saved live page); free tokens/access disclosed and not typed as a payment |
| A04 | CONFIRMED | MDT | C03.E1 | {} | primary | evidence |  | dated METR self-statement of its funding/compensation rule (quote verified in the saved live page); free tokens/access disclosed and not typed as a payment |
| A05 | CONFIRMED | MDT | C03.E1 | {} | supporting | context |  | re-verification of a Wayback window already promoted from MD24; context |
| A06 | CONFIRMED | MDT | C03.E1 | {} | supporting | context |  | re-verification of a Wayback window already promoted from MD24; context |
| A07 | CONFIRMED | MDT | C03.E1 | {} | supporting | context |  | re-verification of a Wayback window already promoted from MD24; context |
| A08 | CONFIRMED | MDT | C03.E1 | {} | supporting | context |  | re-verification of a Wayback window already promoted from MD24; context |
| A09 | CONFIRMED | MDT | C03.E1 | {} | supporting | context |  | re-verification of a Wayback window already promoted from MD24; context |
| A10 | CONFIRMED | MDT | C03.E1 | {} | supporting | context |  | re-verification of a Wayback window already promoted from MD24; context |
| A11 | CONFIRMED | MDT | C03.E1 | {} | supporting | context |  | re-verification of a Wayback window already promoted from MD24; context |
| A12 | CONFIRMED | MDT | C03.E1 | {} | supporting | context |  | re-verification of a Wayback window already promoted from MD24; context |
| A13 | CONFIRMED | MDT | C03.E1 | {} | primary | evidence |  | dated METR self-statement of its funding/compensation rule (quote verified in the saved live page); free tokens/access disclosed and not typed as a payment |
| B01 | CONFIRMED | MDS | C03.E2 | {} | supporting | negative |  | Anthropic page names a planned METR independent review; no consideration, invoice, grant or donation stated; bounded |
| B02 | CONFIRMED | MDS | C03.E2 | {} | supporting | negative |  | bounded negative on the named lab/foundation source with the legal entity kept distinct; blind spots stated |
| B03 | CONFIRMED | MDS | C03.E2 | {} | supporting | negative |  | bounded negative on the named lab/foundation source with the legal entity kept distinct; blind spots stated |
| B04 | CONFIRMED | MDS | C03.E2 | {} | supporting | negative |  | bounded negative on the named lab/foundation source with the legal entity kept distinct; blind spots stated |
| B05 | CONFIRMED | MDS | C03.E2 | {} | supporting | negative |  | bounded negative on the named lab/foundation source with the legal entity kept distinct; blind spots stated |
| B06 | CONFIRMED | MDS | C03.E2 | {} | supporting | negative |  | bounded negative on the named lab/foundation source with the legal entity kept distinct; blind spots stated |
| B07 | CONFIRMED | MDS | C03.E2 | {} | supporting | negative |  | bounded negative on the named lab/foundation source with the legal entity kept distinct; blind spots stated |
| B08 | CONFIRMED | MDS | C03.E2 | {} | primary | negative |  | OpenAI Foundation TY2024 Form 990 Schedule I (saved XML): no grant to METR's EIN or name; funder filing; $5,000 threshold stated |
| B09 | CONFIRMED | MDS | C03.E2 | {} | supporting | negative |  | bounded negative on the named lab/foundation source with the legal entity kept distinct; blind spots stated |
| B10 | CONFIRMED | MDS | C03.E2 | {} | supporting | negative |  | bounded negative on the named lab/foundation source with the legal entity kept distinct; blind spots stated |
| B11 | CONFIRMED | MDS | C03.E2 | {} | supporting | negative |  | bounded negative on the named lab/foundation source with the legal entity kept distinct; blind spots stated |
| B12 | CONFIRMED | MDS | C03.E2 | {} | supporting | negative |  | bounded negative on the named lab/foundation source with the legal entity kept distinct; blind spots stated |
| B13 | CONFIRMED | MDS | C03.E2 | {} | supporting | negative |  | bounded negative on the named lab/foundation source with the legal entity kept distinct; blind spots stated |
| B14 | CONFIRMED | MDS | C03.E2 | {} | supporting | negative |  | bounded negative on the named lab/foundation source with the legal entity kept distinct; blind spots stated |
| B15 | CONFIRMED | MDS | C03.E2 | {} | supporting | context |  | AmazonSmile Foundation TY2023 return predates METR's May 2024 formation; calendar fact, not a negative |
| B16 | CONFIRMED | MDS | C03.E2 | {} | supporting | negative |  | bounded negative on the named lab/foundation source with the legal entity kept distinct; blind spots stated |
| C01 | CONFIRMED | MDS | C03.E2 | {} | primary | negative |  | METR FY2024 Form 990 XML (saved): no named lab payer; recipient filing |
| C02 | CONFIRMED | MDS | C03.E2;C03.E3 | {} | supporting | context |  | public Schedule B is RESTRICTED; redaction is evidence neither way; context |
| C03 | CONFIRMED | MDS | C03.E2 | {} | supporting | negative |  | RelatedOrganizationsAmt $4,501,424 is from Alignment Research Center (EIN 86-3605182), not a lab; verified in saved XML; not re-typed |
| C04 | CONFIRMED | MDS | C03.E2 | {} | supporting | context |  | AllOtherContributionsAmt $9,101,611 is an unnamed remainder; a lab could sit inside it unidentifiably; context, not a negative |
| C05 | CONFIRMED | MDS | C03.E2 | {} | primary | negative |  | CYProgramServiceRevenueAmt 0 and no GovernmentGrantsAmt on METR's FY2024 return (verified); no lab program-service revenue in that year |
| C06 | CONFIRMED | MDS | C03.E2 | {} | supporting | negative |  | live supporter sentences name no lab as a funder; bounded |
| C07 | CONFIRMED | MDI | C03.E2 | {} | supporting | evidence |  | METR home page: labs 'provided access and tokens'; in-kind, unquantified, not a payment; entities unmerged |
| C08 | CONFIRMED | MDS | C03.E2 | {} | primary | evidence |  | METR's own 2026-08-26 incident post: 'we did not take payment from OpenAI for this independent assessment' (verified); free API credits named in a footnote and not typed as payment |
| D01 | CONFIRMED | MDS | C03.E3 | {} | supporting | evidence |  | Form 990 Schedule I Part II columns (a)-(h) have no donor/adviser/account-principal field (pdftotext of the saved form); defines the public-verification stop |
| D02 | CONFIRMED | MDF | C03.E3 | {} | supporting | context |  | re-verification of a DAF-sponsor Schedule I grant already promoted from MD11; context |
| D03 | CONFIRMED | MDF | C03.E3 | {} | supporting | context |  | re-verification of a DAF-sponsor Schedule I grant already promoted from MD11; context |
| D04 | CONFIRMED | MDS | C03.E3 | {} | supporting | negative |  | public Schedule B of the sponsor names no account principal; bounded; no deanonymization attempted |
| D05 | CONFIRMED | MDS | C03.E3 | {} | supporting | evidence |  | proposition: public verification of a DAF-routed gift stops at the sponsor entity and the recipient row; employee-directed gifts via a DAF are not publicly distinguishable |
| E01 | CONFIRMED | MDS | C03.E2 | {} | supporting | context |  | route failure (403/400/405/login wall) recorded reproducibly; context, not a negative |
| E02 | CONFIRMED | MDS | C03.E2 | {} | supporting | context |  | route failure (403/400/405/login wall) recorded reproducibly; context, not a negative |
| E03 | CONFIRMED | MDS | C03.E2 | {} | supporting | negative |  | bounded negative with blind spots stated |
| E04 | CONFIRMED | MDS | C03.E2 | {} | supporting | negative |  | bounded negative with blind spots stated |
| E05 | CONFIRMED | MDS | C03.E2 | {} | supporting | context |  | route failure (403/400/405/login wall) recorded reproducibly; context, not a negative |
| E06 | CONFIRMED | MDS | C03.E2 | {} | supporting | context |  | route failure (403/400/405/login wall) recorded reproducibly; context, not a negative |
| E07 | CONFIRMED | MDS | C03.E2 | {} | supporting | context |  | route failure (403/400/405/login wall) recorded reproducibly; context, not a negative |
| E08 | CONFIRMED | MDS | C03.E2 | {} | supporting | context |  | route failure (403/400/405/login wall) recorded reproducibly; context, not a negative |
| E09 | CONFIRMED | MDS | C03.E2 | {} | supporting | context |  | route failure (403/400/405/login wall) recorded reproducibly; context, not a negative |
| E10 | CONFIRMED | MDS | C03.E2 | {} | supporting | negative |  | bounded negative with blind spots stated |
| E11 | CONFIRMED | MDS | C03.E2 | {} | supporting | negative |  | bounded negative with blind spots stated |
| E12 | CONFIRMED | MDS | C03.E2;C03.E3 | {} | supporting | context |  | record of no request sent / press not used as a money source; context |
| E13 | CONFIRMED | MDS | C03.E2 | {} | supporting | context |  | record of no request sent / press not used as a money source; context |
| E14 | CONFIRMED | MDS | C03.E2 | {} | supporting | negative |  | bounded negative with blind spots stated |
| E15 | CONFIRMED | MDS | C03.E2 | {} | supporting | negative |  | bounded negative with blind spots stated |
