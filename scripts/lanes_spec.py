#!/usr/bin/env python3
"""The frozen metr_deep lane map (PLAN.md §6). IDs, slugs, slices and element bindings are immutable.

Each entry: lane id -> (slice, wave, title, slug, routes, elements, tasks A-D).
Task E is the standard bounded-negative task and is appended by scripts/materialize_briefs.py.
A lane is never renumbered or repurposed; a correction adds a successor lane in MD70-MD89.
"""
from __future__ import annotations

NEG = ("Record a bounded negative for every source class named in this lane that returned no responsive "
       "record: the exact query, endpoint or document, the filters, the result count, the UTC check time and "
       "the known blind spot. Write one row per source checked with target_prefix=MDS. Never write an "
       "unbounded negative and never leave a task silent.")

LANES: dict[str, dict] = {}


def lane(lid, sl, wave, title, slug, routes, elements, tasks):
    assert len(tasks) == 4, lid
    LANES[lid] = dict(slice=sl, wave=wave, title=title, slug=slug, routes=routes,
                      elements=elements, tasks=list(tasks) + [NEG])


# ---------------------------------------------------------------- Wave 1 / S1
lane("MD01", "S1", 1,
     "METR recipient-side financial baseline",
     "metr-recipient-baseline",
     "IRS TEOS and e-file index; IRS bulk 990 XML; California registry; METR's own site and reports",
     ["C02.E3", "C02.E4", "C01.E3"],
     ["Recover every Form 990 and any public audited financial statement filed by Model Evaluation and Threat "
      "Research (EIN 99-1219864) through the current IRS index. For each return record the fiscal period, total "
      "revenue, contributions and grants, program service revenue, government grants, net assets, and any "
      "restricted-fund line, each with the exact XML field or page.",
      "List every payer named on the recipient side of those returns (Schedule B is redacted for a public charity; "
      "use Part VIII, Schedule A public-support schedules and any grantor named in narrative parts) with amount, "
      "fiscal year and the field it came from.",
      "Record METR's related entities, predecessor or parent relationships, state registrations and any group "
      "exemption, with the document that states each. Record the ruling date and the accounting method.",
      "Record which fiscal periods are not yet filed and the earliest date each becomes available, as a calendar "
      "row rather than a negative finding."])

lane("MD02", "S1", 1,
     "Packard Foundation grant to METR",
     "packard-grant",
     "packard.org grantee pages and grant database; Packard Form 990-PF; Wayback",
     ["C02.E2", "C01.E2", "C01.E3"],
     ["Reproduce the Packard Foundation grant record for Model Evaluation and Threat Research from packard.org: "
      "amount, award date, duration, program area and purpose text, with the canonical grantee or grant URL and a "
      "verbatim quote. Record the page's own metadata fields and the response hash.",
      "Enumerate the Packard grant database by its canonical index, sitemap or API as well as by keyword, and list "
      "every Packard award to METR or to any METR alias, with the enumeration route used.",
      "Find the same grant in Packard's Form 990-PF Part XV if it is filed, and record whether it appears as paid "
      "or approved for future payment; type it in money_type accordingly.",
      "Capture the grant page history from Wayback and record when the record first appeared, stating explicitly "
      "that first appearance is not the grant date."])

lane("MD03", "S1", 1,
     "Pew grants to METR or ARC",
     "pew",
     "Pew Charitable Trusts grant listings and disclosures; Pew Form 990; Wayback",
     ["C02.E2"],
     ["Search every Pew Charitable Trusts public grant listing, annual report and disclosure route for Model "
      "Evaluation and Threat Research, METR, Alignment Research Center, ARC Evals and any other alias, by canonical "
      "index and by keyword. Record each route and result count.",
      "For any award found, record amount, date, purpose, the legal Pew entity that made it and the legal recipient, "
      "with the exact document.",
      "Check Pew's Form 990 grant schedules for the same recipient names and record the filing year checked.",
      "Distinguish the Pew Charitable Trusts from the Pew Research Center and from any other Pew entity, and record "
      "which entity each result belongs to."])

lane("MD04", "S1", 1,
     "Schmidt Sciences and related Schmidt entities",
     "schmidt-sciences",
     "schmidtsciences.org and related sites; Schmidt entity Forms 990 and 990-PF; issuer and press records",
     ["C02.E2", "C05.E1", "C05.E3"],
     ["Identify every Schmidt-associated legal entity that could be the payer to METR (Schmidt Sciences, Schmidt "
      "Futures, Eric and Wendy Schmidt Fund for Strategic Innovation, Hillspire, Schmidt Family Foundation and any "
      "other), with EIN or registration identifier for each, and keep them separate.",
      "Record the amount, date, purpose and legal payer of any Schmidt support to METR from the entity's own "
      "announcement or grant listing, quoted verbatim.",
      "Find the same support in the paying entity's Form 990 or 990-PF grant schedule and record whether it is paid "
      "or approved for future payment.",
      "Record separately, and without merging it with the grant, any documented Schmidt investment or governance "
      "connection to Anthropic, naming the exact investing entity or individual."])

lane("MD05", "S1", 1,
     "Sijbrandij Foundation",
     "sijbrandij-foundation",
     "Sijbrandij Foundation site and grant listings; Form 990-PF; state registry",
     ["C02.E2"],
     ["Record every Sijbrandij Foundation grant, commitment or pledge naming METR, with amount, date, duration, "
      "restriction and the document that states it.",
      "Recover the foundation's Forms 990-PF for the years that could carry a METR line and record the Part XV "
      "entries, distinguishing paid grants from amounts approved for future payment.",
      "Record the foundation's legal name, EIN, state registration and any related vehicle or donor-advised account "
      "named in its own materials, keeping each entity separate.",
      "Record the grant purpose and any restriction verbatim, and whether the amount falls inside METR's stated "
      "February to August 2026 commitment window."])

lane("MD06", "S1", 1,
     "LaCentra-Sumerlin, Astralis and Expa.org",
     "lacentra-astralis-expa",
     "entity sites; Forms 990 and 990-PF; state registries; IRS index",
     ["C02.E2"],
     ["For each of the LaCentra-Sumerlin, Astralis and Expa.org supporters METR names, identify the exact legal "
      "entity: full legal name, EIN or registration number, jurisdiction, and whether it is a private foundation, a "
      "public charity, a donor-advised account or an operating company.",
      "Record any grant, commitment or gift from each to METR with amount, date, vehicle and purpose from the "
      "entity's own materials.",
      "Recover each entity's filings that could carry a METR line and record the grant schedule entries and the "
      "years checked.",
      "Where an entity has no public filing route, say exactly why (for example a 990-N filer, a foreign entity or a "
      "donor-advised account) and name the document that would show a grant if one existed."])

lane("MD07", "S1", 1,
     "Individuals from Jane Street, as publicly acknowledged only",
     "jane-street-individuals",
     "METR's own acknowledgments; donor self-statements; filings that name a donor",
     ["C02.E2", "C05.E1", "C05.E3"],
     ["Record METR's own wording about individuals associated with Jane Street, with the dated capture and the "
      "verbatim quote, and record whether METR names the firm or only individuals.",
      "Record separately every documented Jane Street Capital firm position in Anthropic, with the round, date and "
      "source, and state explicitly that a firm investment is not a donation by an individual.",
      "Record any first-person public statement by a named individual acknowledging a gift to METR, quoted "
      "verbatim, and only where the individual has made it public themselves.",
      "Do not attempt to identify an unnamed donor. Record as a bounded limit that METR names no individual and "
      "that no public filing checked discloses a natural-person donor to a public charity."])

lane("MD08", "S1", 1,
     "Named individual donors: Farhi, Ralston, Field and Newman",
     "named-individual-donors",
     "donor self-statements; DAF and stock-gift filings; recipient acknowledgments; FEC only to corroborate employment",
     ["C02.E2", "C03.E3"],
     ["For each named individual supporter, record METR's own acknowledgment with its dated capture, and any "
      "first-person public statement by that individual about the gift, quoted verbatim.",
      "Record the vehicle used where a source names one (personal gift, donor-advised account, stock transfer, "
      "family foundation) and keep the individual, the vehicle and any employer separate.",
      "Record each individual's employment status at the gift date from a dated public source; use an FEC record "
      "only to corroborate a self-reported employer on a dated contribution, never as evidence of a gift to METR.",
      "Record whether the gift falls inside METR's stated February to August 2026 commitment window, or that the "
      "date is not disclosed."])

lane("MD09", "S1", 1,
     "Survival and Flourishing Fund and Jaan Tallinn",
     "sff-tallinn",
     "SFF round tables; Tallinn's public donation ledger; recipient and grantor filings",
     ["C02.E2", "C02.E5", "C05.E1", "C05.E2"],
     ["Recover every SFF recommendation naming METR, ARC or ARC Evals from the SFF round pages, with round, year, "
      "amount, the legal recipient named and any conditional or matching component stated separately.",
      "Record the corresponding entries in Jaan Tallinn's public donation ledger with amount and date, and mark "
      "where the ledger amount differs from the recommendation; never sum a recommendation with a payment.",
      "Identify the legal payer for each recommendation (the recommending fund, a regrantor or a donor-advised "
      "sponsor) and find the payment in a grantor filing where one exists.",
      "Record separately Tallinn's documented Anthropic investment and any stated board-observer role, with the "
      "exact source, and do not treat either as evidence about the grant."])

lane("MD10", "S1", 1,
     "Longview, Effektiv Spenden and pooled or regrant routes",
     "longview-pooled-regrants",
     "grant pages; annual reports; Forms 990 and foreign charity filings",
     ["C02.E5", "C06.E1"],
     ["For each pooled or regranting route METR names, record what the route's own materials say it gave to METR: "
      "amount, date, fund name and whether the figure is a recommendation, a disbursement or undisclosed.",
      "Recover the route's filings that could carry a METR line and record the grant schedule entries and years "
      "checked, distinguishing the legal filer from the fund brand.",
      "Where a route reports only an aggregate or a recommendation, record that explicitly and name the document "
      "that would show a payment.",
      "Keep the pooled fund's own donors separate from METR's donors: a donor to the fund is not a donor to METR "
      "unless a document ties the specific money."])

lane("MD11", "S1", 1,
     "Filed donor-advised-fund grants to METR",
     "daf-filed-grants",
     "DAF sponsor Form 990 Schedule I; IRS bulk e-files; recipient aliases",
     ["C02.E3", "C02.E5", "C03.E3"],
     ["Search every major donor-advised-fund sponsor's filed Form 990 Schedule I for grants to METR and to each "
      "METR alias and EIN, for every fiscal year available, and record amount, fiscal year, sponsor and the exact "
      "filing object id.",
      "Record for each hit that the sponsor discloses no account principal, and name the schedule and line that "
      "would carry more detail if it existed.",
      "Repeat the search for the Alignment Research Center and its aliases so that pre-spinout money is not "
      "attributed to METR.",
      "Record which sponsors file on a calendar year and which on a June year, and the next date each sponsor's "
      "unfiled year becomes available."])

lane("MD12", "S1", 1,
     "ARC spin-out and restricted-fund provenance",
     "arc-spinout-provenance",
     "ARC and METR Forms 990; transfer documents; announcements",
     ["C02.E3", "C06.E1"],
     ["Record the ARC to METR program transfer from ARC's own Form 990 Schedule I: cash amount, non-cash amount, "
      "purpose text, distribution date and the exact fields.",
      "Record the separation and spin-out events with their own dated sources, keeping the organisational "
      "separation date and the asset distribution date as different events.",
      "Record ARC's own funders for the years that produced the transferred assets, and state explicitly that the "
      "transfer cannot be attributed to any single ARC funder.",
      "Record any restriction carried by the transferred funds, or that no restriction is stated in the checked "
      "document."])

lane("MD13", "S1", 1,
     "Universal public grant-database sweep",
     "grant-database-sweep",
     "official grantmaker databases enumerated by canonical page, sitemap or API; Candid used only to locate a primary",
     ["C01.E5", "C02.E2"],
     ["Build the alias list first: METR, Model Evaluation and Threat Research, METR Inc, ARC Evals, Alignment "
      "Research Center Evals, and the EIN, and record it as a row so later lanes reuse it.",
      "For each named supporter's grant database and for the major independent AI-safety grant databases, "
      "enumerate the canonical index, sitemap or API rather than relying on keyword search alone, and record the "
      "enumeration route, the record count seen and any cap hit.",
      "Record every award found with payer, recipient alias matched, amount, date, purpose and the canonical record "
      "URL.",
      "Record a bounded negative for each database enumerated with no METR record, naming the enumeration route and "
      "the record count, so the Packard-style miss cannot recur."])

lane("MD14", "S1", 1,
     "Six-month window chronology and denominator compatibility",
     "six-month-chronology",
     "METR blog and archives; all Wave 1 rows; fiscal and payment dates",
     ["C01.E1", "C01.E2", "C01.E3", "C01.E4"],
     ["Capture METR's own statement of the approximately $71 million total with its URL, verbatim sentence, the "
      "period it names, the response hash and the UTC check time, and record the money type it uses.",
      "Build the dated chronology of every public funding event between the window's start and end, one row per "
      "event, with money type and payment status.",
      "For each known amount, record whether it is compatible with the denominator's period, entity and money type, "
      "and give the reason for every exclusion.",
      "State the identified compatible total and the unresolved remainder or range arithmetically from the rows, "
      "with no imputed allocation and no forced equality."])

# ---------------------------------------------------------------- Wave 2 / S2
lane("MD15", "S2", 2,
     "Audacious partner list by date and project-funder rules",
     "audacious-partners",
     "Audacious Project and TED live pages plus Wayback; partner descriptions",
     ["C06.E2", "C09.E1"],
     ["Capture the Audacious Project partner list as it stood on the Canary announcement date and as it stands now, "
      "each from a dated archive or live capture with a hash, and record every name added or removed between them.",
      "Record what the Audacious Project's own materials say about how partners fund projects: whether partners pay "
      "grantees directly, whether membership implies participation in a given project, and the exact wording.",
      "Record for each partner whether any public document ties it to the Canary project specifically, and mark "
      "every partner with no such document as membership only.",
      "Record explicitly that a partner's appearance on a current list is not evidence of the date it joined, and "
      "date each listing change from the archive capture instead."])

lane("MD16", "S2", 2,
     "Canary award structure and project-specific funder disclosures",
     "canary-award-structure",
     "METR, RAND and Audacious announcements and their archives",
     ["C06.E2"],
     ["Record the Canary award as each announcing organisation states it: total commitment, term, the legal "
      "recipients named, and each organisation's own wording, quoted verbatim with the dated capture.",
      "Record every project-specific funder disclosure: which funders are named for Canary as opposed to for the "
      "Audacious cohort generally.",
      "Record the stated split between the recipients and mark clearly any figure that is a subtraction rather than "
      "a quoted allocation.",
      "Record every later restatement of the amount or term with its date, and keep commitment, allocation and "
      "payment as separate propositions."])

lane("MD17", "S2", 2,
     "RAND-side Canary receipts and directed grants",
     "rand-canary-receipts",
     "RAND reports, funding pages and Forms 990; funder filings",
     ["C06.E1", "C06.E2"],
     ["Record every RAND disclosure naming Canary or the centre that houses it: funder names, amounts, terms and "
      "the dated document.",
      "Find filed payments to RAND from Audacious partners and other named funders in grantor filings, with amount, "
      "fiscal year, purpose text and filing object id.",
      "Record RAND's own Form 990 lines that could carry the Canary money and the years checked.",
      "State explicitly for each RAND receipt that a payment to RAND is not a payment to METR, and record whether "
      "any document shows onward passage."])

lane("MD18", "S2", 2,
     "METR-side Canary commitment, payments and term changes",
     "metr-canary-commitment",
     "METR statements and archives; METR Form 990; funder filings",
     ["C06.E1", "C06.E2", "C01.E2", "C01.E3"],
     ["Record METR's own statements of its Canary share across time, each with date and verbatim quote, including "
      "any later revision of the amount or term.",
      "Record whether any filing shows a payment into METR attributable to Canary, and the exact schedule and year "
      "checked if none does.",
      "Record the restricted-revenue treatment of the commitment in METR's own filings if it is visible, with the "
      "field.",
      "Record whether the Canary commitment is inside or outside METR's stated February to August 2026 commitment "
      "window, with the reason."])

lane("MD19", "S2", 2,
     "UK AI Security Institute grants, contracts and in-kind arrangements",
     "uk-aisi-contracts",
     "Contracts Finder; Find a Tender; UK AISI publications and transparency data",
     ["C06.E3", "C04.E1"],
     ["Search the official UK procurement systems for every award or contract naming METR or an alias, record the "
      "award notice id, contracting authority, legal supplier, value, currency and period, and archive the notice.",
      "Search UK AI Security Institute publications and transparency releases for any grant, contract, "
      "collaboration or in-kind arrangement with METR, quoted verbatim.",
      "Where an award is to a consortium, record the consortium ceiling separately from METR's share, and record "
      "that the share is not disclosed if the document does not give it.",
      "Record which contract documents exist but are not published, and name the exact public-record route that "
      "would produce each one, for a later slice to consider."])

lane("MD20", "S2", 2,
     "EU AI Office technical-assistance contract and consortium share",
     "eu-ai-office-contract",
     "TED; EU Financial Transparency System; Commission documents",
     ["C06.E3"],
     ["Search TED and the EU Financial Transparency System for every contract or grant naming METR or an alias, and "
      "record the reference number, contracting authority, legal contractor, value, currency and period.",
      "Record the consortium composition where the award is to a consortium, with METR's role as the document "
      "states it and its share only where a document gives one.",
      "Archive each notice and award document and record its response hash and check time.",
      "Record which underlying contract documents are unpublished and name the Commission access-to-documents route "
      "that would produce each, for a later slice to consider."])

lane("MD21", "S2", 2,
     "US and other public-sector awards or agreements",
     "us-public-sector-awards",
     "USAspending; SAM.gov; NIST and CAISI publications; state records",
     ["C06.E3"],
     ["Search USAspending and SAM.gov by recipient name, alias and UEI for every award, subaward or registration "
      "naming METR, and record award id, awarding agency, legal recipient, obligated and potential value, and "
      "period.",
      "Search NIST, CAISI and other federal publications for any agreement, CRADA, cooperative agreement or "
      "in-kind arrangement with METR, quoted verbatim.",
      "Record any state or non-US public-sector award found outside the UK and EU routes, with the same fields.",
      "Distinguish a registration or a solicitation response from an award, and record explicitly where only a "
      "registration exists."])

lane("MD22", "S2", 2,
     "Intermediary recipient and payer returns",
     "intermediary-returns",
     "IRS e-files for intermediaries and sponsors; foreign charity filings",
     ["C02.E3", "C02.E5", "C06.E1"],
     ["For each intermediary that could carry money to METR, recover its filings for every available year and "
      "record each grant schedule line naming METR or an alias, with amount, year, purpose and object id.",
      "Record the intermediary's own reported revenue and the named payers into it where its filing discloses them, "
      "keeping payer-into-intermediary and intermediary-to-METR as separate propositions.",
      "For a foreign intermediary, find the equivalent national charity filing and record the fields it gives.",
      "Record the fiscal-year basis of each intermediary and the next date each unfiled year becomes available."])

lane("MD23", "S2", 2,
     "Restrictions and grant purposes across all identified support",
     "restrictions-and-purposes",
     "grant letters and pages; filings; recipient disclosures",
     ["C02.E2", "C01.E3"],
     ["For every identified item of support, record the stated purpose and any restriction verbatim from the "
      "funder's own document.",
      "Record the same purpose as the recipient states it where both exist, and mark any difference between the two "
      "statements.",
      "Classify each item as unrestricted, programme-restricted, project-restricted or undisclosed, using only the "
      "document's own words.",
      "Record which restrictions would make an amount incompatible with the approximately $71 million commitment "
      "denominator, and why."])

lane("MD24", "S2", 2,
     "Funding-page and donor-rule chronology",
     "funding-page-chronology",
     "Wayback and CDX; live page hashes",
     ["C09.E1", "C09.E3", "C03.E1"],
     ["Enumerate every archived capture of METR's about, funding, donor and support pages through the CDX index, "
      "and record the capture timestamps and count.",
      "Diff consecutive captures and record the exact date range in which each supporter name and each funding rule "
      "first appeared or changed, with the verbatim before and after text.",
      "Capture the live pages now with their response hashes and UTC time, and record any difference from the last "
      "archived capture.",
      "Record explicitly for every appearance date that it bounds when the page changed, not when a transaction "
      "occurred, and note any case where a separate document gives the transaction date."])

lane("MD25", "S2", 2,
     "Revenue, commitments, runway, headcount and expenditure reconciliation",
     "revenue-runway-reconciliation",
     "recipient filings; METR's own budget statements; public job data",
     ["C01.E3", "C01.E4", "C02.E4"],
     ["Record every public statement by METR or its officers about its budget, run rate, runway or headcount, with "
      "date and verbatim quote.",
      "Record the filed revenue and expenditure figures for every available fiscal year from METR's own returns, "
      "with the fields.",
      "Set the commitment statements beside the filed revenue without summing them, and state which periods do and "
      "do not overlap.",
      "Record what the difference between committed and filed amounts can and cannot establish, in one explicit "
      "bounded statement."])


# ---------------------------------------------------------------- Wave 3 / S3
lane("MD26", "S3", 3,
     "Tokens, credits, compute and engineering help by lab and project",
     "tokens-credits-compute",
     "METR reports and acknowledgments; lab statements and system cards",
     ["C04.E1"],
     ["For every METR assessment or report naming a lab, record the acknowledgment of tokens, credits, compute or "
      "engineering support verbatim, with the report, its date and the provider named.",
      "Record a quantity or estimated value only where a source states one, with the source's own wording; leave "
      "the value empty rather than estimating.",
      "Record each lab's own statement about resources given to METR from the lab's documents, and mark any "
      "difference from METR's wording.",
      "Record explicitly that free resources are not cash, and never carry an in-kind figure into a money total."])

lane("MD27", "S3", 3,
     "Model access, safe harbor, publication, redaction and exit rights",
     "access-and-project-terms",
     "assessment reports; published agreements; policies",
     ["C04.E2", "C04.E3", "C08.E3"],
     ["For each engagement, record the model access granted as the documents describe it: level of access, "
      "transcripts, sampling, internal materials, and the dates access applied.",
      "Record the stated safe harbor, non-disclosure, publication and pre-publication review terms, quoted "
      "verbatim from the document that states them.",
      "Record whether the provider holds any redaction right or any authority to end the engagement before "
      "publication, and the document that grants or withholds it.",
      "Where a term is not disclosed, record that explicitly with the exact documents checked, rather than "
      "inferring it from another engagement."])

lane("MD28", "S3", 3,
     "February to March 2026 Frontier Risk Report team and conflict process",
     "frontier-risk-report-coi",
     "the report itself; AEF-1; the dated conflict-of-interest policy",
     ["C08.E1", "C08.E2"],
     ["Record the report's own disclosure section verbatim: who worked on it, what conflicts were disclosed and "
      "what recusals were applied.",
      "Record which conflict-of-interest policy version was in force on the report's dates, with the dated capture "
      "and hash of that version.",
      "Record each named team member's public affiliations at the report date from dated public sources only.",
      "Record explicitly any later policy version that did not apply at the time, so no policy is applied "
      "retroactively without saying so."])

lane("MD29", "S3", 3,
     "September 2026 Anthropic incident engagement",
     "anthropic-incident-engagement",
     "Anthropic and METR announcements; subcontractor statements; the responsible-scaling policy and trust documents",
     ["C08.E2", "C08.E3", "C08.E4", "C04.E2"],
     ["Record every dated statement by Anthropic and by METR about the engagement: scope, access, term and any "
      "stated compensation, each quoted verbatim, and mark where the two differ.",
      "Record how METR was selected for the engagement and by whom, from the documents, and whether any published "
      "policy provision is cited as governing the selection.",
      "Record every subcontractor whose own statements place it inside the engagement, with its wording and the "
      "terms it discloses or withholds.",
      "Record whether compensation, redaction authority and publication control are disclosed, and by which "
      "document, or that they are not disclosed."])

lane("MD30", "S3", 3,
     "Project staff conflicts, disclosures and recusals",
     "project-staff-conflicts",
     "report disclosures; public bios; the conflict policy; public statements only",
     ["C08.E2", "C05.E1"],
     ["For each material project, list the staff the documents name and record each person's disclosed conflicts "
      "exactly as the document states them.",
      "Separate, for each person, direct equity, recent lab employment, simultaneous lab work, a stated close "
      "personal relationship, a board role and mere ecosystem adjacency; never merge two categories.",
      "Record only what the person or the organisation has made public; record no inference about a private "
      "relationship and no unpublished personal information.",
      "Record each disclosed recusal and each case where a document states that no recusal was applied."])

lane("MD31", "S3", 3,
     "Board, advisers and institutional governance safeguards",
     "board-and-governance",
     "METR filings, site and board bios; the conflict policy",
     ["C08.E1", "C02.E4"],
     ["Record METR's board and adviser roster with dated sources, and each member's other public roles at the date "
      "recorded.",
      "Record the governance provisions the organisation's own filings and policy state: conflict procedures, "
      "recusal rules, independent-director requirements and review bodies.",
      "Record the officers and directors listed in each available Form 990 with the fiscal year, and note any "
      "change between years.",
      "Record any governance safeguard that is asserted publicly but not documented in a filing or policy, and mark "
      "it as an assertion."])

lane("MD32", "S3", 3,
     "Direct lab payment and employee-directed donation negative sweep",
     "lab-money-negative-sweep",
     "lab disclosures; METR filings and pages; donor-advised sponsor rules",
     ["C03.E1", "C03.E2", "C03.E3"],
     ["Record METR's stated rule on funding from AI companies and on employee-directed donations, in each dated "
      "version, quoted verbatim.",
      "Search each named frontier lab's own disclosures, grant lists and filings for any payment, contract, "
      "sponsorship or donation to METR, and record each source checked with its result.",
      "Search METR's own filings and pages for any lab-sourced revenue line, and record the fields checked.",
      "Record the exact point at which public verification stops for a donation routed through a donor-advised "
      "account, naming the schedule that would show it if sponsors disclosed principals."])

lane("MD33", "S3", 3,
     "Donor and investor map with strict entity resolution",
     "donor-investor-map",
     "issuer announcements; SEC; court-supervised sales; donor records; state registries",
     ["C05.E1", "C05.E2", "C05.E3"],
     ["Build one row per legal entity or natural person involved, with full legal name, type, jurisdiction and "
      "identifier, and an explicit note on what distinguishes it from any similarly named entity.",
      "Record each documented Anthropic investment with the round, date, investing entity as the source names it, "
      "and the amount or share only where a document gives one.",
      "Record each documented governance role, including any self-described observer role, with the person's own "
      "dated words.",
      "Record each documented donation separately from each investment, and never let a shared person merge two "
      "entities into one actor."])

lane("MD34", "S3", 3,
     "Comparison of terms and treatment across labs",
     "cross-lab-project-terms",
     "METR reports and provider statements",
     ["C08.E3", "C08.E4", "C04.E2"],
     ["Build one row per project covering provider, date, compensation, access, disclosure, redaction authority and "
      "exit rights, with each cell sourced to a document or marked undisclosed.",
      "Record differences between providers as observations with their sources, never as evidence of motive or "
      "favouritism.",
      "Record where a difference is explained by the document itself, quoting the explanation.",
      "Record which cells cannot be compared because the underlying documents differ in kind, and why."])

lane("MD35", "S3", 3,
     "External-evaluator independence standards compared with METR practice",
     "evaluator-standards",
     "AEF-1; government evaluator standards; other published evaluator policies",
     ["C08.E5"],
     ["Record the requirements each published external-evaluator standard states, quoted verbatim, with its "
      "publisher and date.",
      "Record METR's own self-assessment answers against those requirements, quoted verbatim with the date.",
      "Record other evaluators' published independence policies for comparison, with source and date.",
      "Record for each requirement whether the public record shows METR meeting it, not meeting it, or leaves it "
      "undetermined, and which document would determine it."])

lane("MD36", "S3", 3,
     "Evaluator-selection market and who selected METR for each role",
     "evaluator-selection",
     "procurement and request-for-information records; company and government documents",
     ["C08.E5", "C06.E3"],
     ["For each role METR holds, record who selected or endorsed it and by what documented process, with the "
      "document and date.",
      "Record the alternatives named in the same document or process, without ranking them.",
      "Record any published criteria for selection and whether independence is among them, quoted verbatim.",
      "Record where no selection process is published, naming the documents checked."])

# ---------------------------------------------------------------- Wave 4 / S4
lane("MD37", "S4", 4,
     "National Philanthropic Trust public Schedule B route",
     "npt-schedule-b",
     "section 6104(d) public-inspection rules; NPT and Pennsylvania filings",
     ["C07.E2", "C07.E3"],
     ["Record exactly which parts of the sponsor's Form 990 are open to public inspection under section 6104(d) "
      "and which are redacted, citing the instruction text.",
      "Recover every already-posted copy of the sponsor's return for the relevant years and record what its "
      "Schedule B Parts I and II disclose and withhold.",
      "Record the non-cash contribution and closely held or other equity lines for the relevant years with their "
      "exact fields and amounts.",
      "Draft, without sending, the narrowest possible request for the existing public parts of an existing return, "
      "and record it as a draft with approved_for_send false. Ask for a record, never for an explanation."])

lane("MD38", "S4", 4,
     "Other donor-advised-fund sponsor schedules and account-transfer evidence",
     "daf-sponsor-schedules",
     "sponsor Forms 990 and audited statements",
     ["C07.E2", "C07.E3", "C02.E3"],
     ["For each sponsor named by a primary document as relevant, record the non-cash contribution schedule lines by "
      "year with the exact field names, keeping publicly traded stock, closely held stock and partnership or "
      "limited-liability interests on their own lines.",
      "Record any sponsor-to-sponsor grant that moves an account family, with amount, year and the filing field.",
      "Record what each sponsor's audited statement adds beyond the return, where one is public.",
      "Record for each sponsor that it discloses no account principal, and name the document that would if any "
      "existed."])

lane("MD39", "S4", 4,
     "Good Ventures fiscal-2026 return and the later-arrival test",
     "good-ventures-fy2026",
     "IRS index; California registry; Form 990-PF",
     ["C07.E2", "C07.E4", "C02.E3"],
     ["Record the filer's fiscal year end, its filing due date and any extension, and the earliest date the "
      "relevant return becomes available.",
      "Record from the returns already available every contribution schedule line and every grant line that could "
      "bear on the question, with fields and amounts.",
      "Record whether any METR line appears in any available year, with the schedule and year checked.",
      "Record the unavailable year as a calendar closer with its next check date, never as a negative finding."])

lane("MD40", "S4", 4,
     "Named investment vehicles and family entities",
     "moskovitz-vehicles",
     "state business registries; SEC filings; issuer records",
     ["C07.E3"],
     ["For each vehicle named by a primary document, record its exact legal name, jurisdiction, registration "
      "number, status and registered agent from the state registry.",
      "Record every securities filing in which the vehicle appears as a holder or seller, with the filing, date "
      "and the exact table entry.",
      "Record any issuer document that names a purchaser or transferee of the shares in question.",
      "Record explicitly that identifying a vehicle would not by itself establish any payment to METR, and what "
      "document would."])

lane("MD41", "S4", 4,
     "Remainder-interest trust type and the records route",
     "remainder-interest-trust",
     "IRS public files; SEC filings; public trust records",
     ["C07.E2", "C07.E3"],
     ["Record every public document that names the trust, with the exact wording about its type, trustee and "
      "beneficiaries.",
      "Record which IRS return a trust of each candidate type would file and which parts of it are open to public "
      "inspection, citing the instruction text.",
      "Record the result of searching the applicable IRS public indexes for the trust, with the index, the query "
      "and the result count.",
      "Draft, without sending, the request for the specific existing return if that is the only remaining route, "
      "with approved_for_send false."])

lane("MD42", "S4", 4,
     "Anthropic securities filings and holder disclosure",
     "anthropic-securities-filings",
     "EDGAR full-text and issuer search; issuer charter and bylaws where public",
     ["C07.E3", "C05.E1"],
     ["Search EDGAR by issuer, by central index key and by full text for any Anthropic registration statement or "
      "holder disclosure, and record the query, the result count and the UTC check time.",
      "Record what a registration statement would and would not disclose about holders, citing the rule or "
      "instruction, so that absence is correctly bounded.",
      "Record any public transfer restriction in the issuer's charter or bylaws that bears on how a holding could "
      "be held or moved, quoted verbatim.",
      "Record the filing as a calendar closer with its next check date if it does not yet exist."])

lane("MD43", "S4", 4,
     "Audacious partner and Canary funder calendar closers",
     "partner-calendar-closers",
     "partner Forms 990-PF and annual reports for the most recent years",
     ["C06.E1", "C06.E2"],
     ["For each partner and named Canary funder, record the filer, fiscal year basis, the latest available return "
      "and the next unfiled year with its due date.",
      "Record every grant line naming the project, either recipient, or an alias, in every available return.",
      "Record which partners have no available return for the relevant year and why.",
      "Record each finding as a payment to the recipient actually named in the filing, never as a payment to the "
      "project as a whole."])

lane("MD44", "S4", 4,
     "Public-record request drafts for contract amounts and terms",
     "public-record-requests",
     "UK freedom-of-information; US freedom-of-information; Commission access to documents",
     ["C06.E3"],
     ["Record, for each unresolved contract element, the exact authority that holds the record and the statutory "
      "route that would produce it, with the citation and the response clock.",
      "Confirm first that the document is not already published, recording the publication routes checked.",
      "Draft each request as a narrow ask for a specific existing record, never as a question for an explanation "
      "and never as any form of allocation question, and save it with approved_for_send false.",
      "Record each draft in the requests journal with its state, and send nothing."])

lane("MD45", "S4", 4,
     "Calendar monitor for filings and reports",
     "calendar-monitor",
     "official release points only",
     ["C01.E5", "C02.E3", "C07.E3"],
     ["Build one calendar row per expected document: the document, the issuer, the earliest expected date, the "
      "official release point and the claim elements it would bear on.",
      "For each row, record the check performed now, the result and the UTC time.",
      "Record any document that has become available since the last check and route it to the lane that owns it.",
      "Record explicitly that a document not yet due is a calendar closer, not a negative finding."])

# ---------------------------------------------------------------- Wave 5 / S5
lane("MD46", "S5", 5,
     "Full typed funding reconciliation",
     "funding-reconciliation",
     "promoted rows only",
     ["C01.E2", "C01.E3", "C01.E4"],
     ["Rebuild the reconciliation from promoted rows only: the denominator, each compatible component with the "
      "reason it is compatible, and each excluded amount with the reason it is not.",
      "Record the identified compatible total and the unresolved remainder or range as arithmetic over those rows.",
      "Record every money type present and confirm that no two types, periods or currencies were summed.",
      "List the exact residual cells that remain unknown after the reconciliation, in the form a later request "
      "would need."])

lane("MD47", "S5", 5,
     "Entity and causal-edge audit",
     "entity-edge-audit",
     "promoted rows only",
     ["C06.E4", "C05.E3"],
     ["Classify every edge asserted anywhere in the pack as a documented transaction, a role, an access "
      "arrangement or an adjacency, and record the document that supports its class.",
      "Record every case where two legal entities have been treated as one and correct it, keeping the original "
      "value in an audit note.",
      "Record every edge that would imply onward passage of money without a documented transaction, and reclassify "
      "it.",
      "Record the final edge inventory by class so a figure can be built without a false pipe."])

lane("MD48", "S5", 5,
     "Project independence synthesis",
     "independence-synthesis",
     "promoted rows only",
     ["C08.E1", "C08.E2", "C08.E3", "C08.E4", "C08.E5"],
     ["Build one row per project with money, in-kind resources, access, disclosure, redaction authority, personnel "
      "and policy version as separate columns.",
      "Record for every cell the row id that supports it, and leave a cell empty rather than filling it from "
      "affiliation.",
      "Record the strongest supported reading and the strongest unsupported reading of the result, each as an "
      "explicit statement.",
      "Record which cells would change if a named pending document arrived."])

lane("MD49", "S5", 5,
     "Claim-by-claim adjudication of the post and the response",
     "claim-adjudication",
     "the frozen public clone; the public response; promoted rows",
     ["C10.E1", "C10.E2", "C10.E3"],
     ["Record the posted version and the current version of each disputed figure separately, each with its commit "
      "and hash, and never let a later correction stand in for what was posted.",
      "Adjudicate each sentence of the public response against the promoted rows: accurate, incomplete, incorrect "
      "or undetermined, with the row ids and the reason.",
      "Adjudicate each claim of the underlying post the same way.",
      "For every verdict short of accurate, name the exact document that would settle it."])

lane("MD50", "S5", 5,
     "Money and provenance adversarial audit",
     "audit-money",
     "promoted rows and their primaries",
     ["C01.E4", "C02.E2", "C06.E1"],
     ["Check every promoted money row against its primary and assign a verdict, listing every row whose amount, "
      "date, entity or money type does not match.",
      "Attack the reconciliation: find every amount that could be double counted, every period mismatch and every "
      "money type used as evidence of another.",
      "Attack every bounded negative: find any that is unbounded in fact, or whose named source would not have "
      "carried the record anyway.",
      "State whether the exhaustion gate can be approved on the money side, and list every correction required "
      "first."])

lane("MD51", "S5", 5,
     "Framing, entity and causality adversarial audit",
     "audit-framing",
     "promoted rows, figures and written synthesis",
     ["C05.E3", "C06.E4", "C10.E2"],
     ["Find every place where two legal entities are merged, where a person stands in for an organisation, or "
      "where an employer stands in for an individual.",
      "Find every place where adjacency, shared employment, friendship, office space or investor status is used as "
      "if it were a money flow.",
      "Find every motive, coordination or dependence conclusion whose required elements are not independently "
      "supported, and every use of motive vocabulary in figure text.",
      "State whether the exhaustion gate can be approved on the framing side, and list every correction required "
      "first."])

lane("MD52", "S5", 5,
     "Frontier-driven gap generation",
     "frontier-gap-generation",
     "the engine frontier and open elements",
     ["C01.E5", "C02.E2", "C04.E3", "C07.E3"],
     ["Run the engine frontier and list every untouched source class and every open element with its claim.",
      "For each, decide whether a currently available public route exists, and record the route or the reason "
      "none exists.",
      "Write one targeted successor brief in the MD70 to MD89 range for each real gap, citing the finding that "
      "created it, and create none for an element that merely lacks detail.",
      "Record every class that is not applicable with its reason, and every future document with its next check "
      "date."])

lane("MD53", "S5", 5,
     "Figures, bibliography, verdicts and release lint",
     "figures-and-release",
     "promoted rows only; local artifacts only",
     ["C10.E1", "C10.E2", "C10.E3"],
     ["Render only figures whose claims are ready, and record for each the rows it cites and the unknown block it "
      "shows.",
      "Build the evidence bibliography so that every number on a figure resolves to a promoted row id.",
      "Write the verdict summary: the strongest supported thesis, the strongest unsupported thesis, the posted "
      "and current version distinction, and every outstanding document.",
      "Run the release lint and record its result; publish nothing and push nothing."])

# ---------------------------------------------------------------- Terminal / S6
lane("MD99", "S6", 6,
     "Single consolidated request for the unresolved allocation",
     "71m-allocation-request",
     "the exhaustion gate and the residual unknown matrix only",
     ["C01.E4", "C02.E2"],
     ["Read the exhaustion gate and list the residual cells it enumerates; ask about nothing already established.",
      "Draft one short request asking, for the unresolved portion only, the donor or vehicle, the committed "
      "amount, the commitment date, the cash paid to date, the restriction or purpose, and whether in-kind "
      "support is counted inside the total.",
      "Attach or link the public-source reconciliation so the recipient can correct specific cells rather than "
      "answer a theory; include no allegation and no compound rhetorical question.",
      "Save the draft with approved_for_send false and record the state as awaiting the user's authority. Send "
      "nothing."])


# ---------------------------------------------------------------- Successors (MD52 Task C, 2026-09-16)
lane("MD70", "S5", 5,
     "Named-supporter list capture with dated page versions",
     "named-supporter-list-capture",
     "live metr.org/about with response hash; Wayback CDX and raw id_ captures of metr.org/about and the funding pages",
     ["C02.E1", "C09.E1", "C09.E3"],
     ["Capture the live https://metr.org/about page now with its HTTP status, byte length, SHA-256 and UTC time, and "
      "quote verbatim the complete supporter paragraph (every foundation, pooled fund, government body, unnamed class "
      "and individual named), so the row is METR's own named-supporter list with the capture date and page version it "
      "was taken from (C02.E1). Do the same for the 2026-08-14 funding update and metr.org/donate.",
      "Enumerate every archived capture of metr.org/about through the Wayback CDX index (retry if the index is offline "
      "and record each attempt), fetch the raw id_ body of each distinct digest, and quote its supporter paragraph "
      "verbatim with the capture timestamp, so each dated version of the list is its own row.",
      "Record the exact differences between consecutive versions of the supporter paragraph (names added, removed or "
      "reworded, the 'individuals from Jane Street' wording, the 'directly' wording), citing the before and after "
      "capture timestamps; a version difference bounds when the page changed, never when a gift occurred.",
      "For each supporter name on the live list, state which promoted rows already give an amount, date or vehicle "
      "and which have only bounded negatives, citing row ids; add no amount that a source does not give."])

lane("MD71", "S5", 5,
     "Dated public statements about the donated Anthropic stake, quoted exactly",
     "donation-statements-quoted",
     "Bluesky and X posts by the named public speakers; Stratechery and other published interviews; Good Ventures, "
     "Open Philanthropy and Coefficient Giving statements; Wayback id_ captures",
     ["C07.E1", "C07.E3", "C05.E2"],
     ["Collect every public statement by Dustin Moskovitz in his public role about donating Anthropic shares or "
      "holding them in a foundation (the Bluesky post 3miawblqk7224, the Stratechery interview, any X post or "
      "reply, any Good Ventures page), quoting each exactly with its URL, date, speaker, venue, response hash and UTC "
      "fetch time; one statement per row bound to C07.E1.",
      "Collect every statement by Good Ventures Foundation, Open Philanthropy, Coefficient Giving or Anthropic about "
      "the donated stake or the foundation's Anthropic holding, quoted exactly and dated the same way, and every "
      "third-party press restatement kept as press, not as the speaker's words.",
      "For each statement record exactly what it does and does not say: the vehicle named or unnamed, the timing, the "
      "share class or amount, and whether 'our foundation' is identified as a legal entity; label every inference "
      "the statement would need as not stated.",
      "Record the separation between the donation statements (C07) and the Series A investment statements (C05.E2) "
      "with their separate dates, and cite the promoted rows for each; assert no motive."])

lane("MD72", "S5", 5,
     "Dated versions of the conflict-of-interest policy with hashes",
     "coi-policy-versions-hashed",
     "live metr.org/coi-policy.pdf and the pages that link it; Wayback CDX and raw id_ captures; METR blog posts that "
     "announce or cite the policy",
     ["C09.E2", "C08.E1", "C09.E3"],
     ["Fetch the live https://metr.org/coi-policy.pdf and record its SHA-256, byte length, HTTP headers, PDF metadata "
      "dates, the version string and 'last updated' date printed in the document, and the UTC fetch time; quote the "
      "version line exactly.",
      "Enumerate every archived capture of coi-policy.pdf and of every metr.org page that links or announces the "
      "policy through the Wayback CDX index (retry on 503 and record each attempt), fetch each distinct digest's raw "
      "id_ body, hash it, and record the earliest capture of each version.",
      "Record the exact textual differences between versions (scope, disclosure, recusal, equity rules), citing the "
      "capture timestamps, and record any dated METR statement that a policy existed before 2026-08-28 or that none "
      "did (the FRR Table A.1 answer), quoted exactly.",
      "For each named engagement already promoted (FRR, HF investigation, Anthropic reviews, OpenAI evaluations, the "
      "2026-09 Anthropic investigation), state which policy version was in force on its dates by citing the "
      "capture evidence, and label 'none in force' where the evidence says so; apply no version backward."])


# ---------------------------------------------------------------- California registries (Kevin, 2026-09-16T19:40Z; created by route failures MDS0658/MDS1063/MDS0920: the AG registry Search.aspx URL returned 404 on all 27 attempts and SOS bizfile was a JS shell, so neither registry was ever searched)
lane("MD73", "S5", 5,
     "California Attorney General charity registry: METR registration, RRF-1 renewals, 990 copies and audited statements",
     "ca-ag-charity-registry",
     "the current California Attorney General Registry of Charities and Fundraisers search tool and document viewer "
     "(rct.doj.ca.gov, oag.ca.gov/charities), its bulk registry CSV downloads, and the Wayback id_ captures of any "
     "registry page; the legacy Search.aspx URL is known to be 404 and must not be the only route tried",
     ["C02.E4", "C02.E3", "C01.E5", "C05.E3"],
     ["Find the registry's current public search endpoint (follow oag.ca.gov/charities links, the registry landing page, "
      "its JavaScript bundle's API paths, or the bulk CSV downloads) and record every endpoint tried with HTTP status, "
      "UTC time and saved body; then locate the registration record for Model Evaluation and Threat Research (EIN "
      "99-1219864), and for Alignment Research Center as its predecessor, recording registry number, status, "
      "registration date, fiscal year end and every listed document with its type and filing date.",
      "Download every document the registry publishes for METR (CT-1 initial registration with attachments, each "
      "RRF-1 annual renewal, each Form 990 copy, each audited financial statement, any correspondence or delinquency "
      "notice), save each with SHA-256 and UTC fetch time, and quote exactly the lines that state total revenue, "
      "contributions, restricted versus unrestricted net assets, related-party transactions, and any named contributor "
      "or grantor; bind one row per stated amount with its money type and period and never sum across type.",
      "Do the same for Alignment Research Center's registry documents for the fiscal years covering the 2024-04-30 "
      "spin-out (the transfer to METR, any restriction on it, and the audited-statement note on the program spin-off).",
      "Record what each audited statement says about donor concentration, conditional or unconditional promises to "
      "give, in-kind contributions and government contracts, quoting exactly; where the statements name no donor, "
      "record that as a bounded negative naming the note and page checked; if the registry is a search UI this lane "
      "cannot drive without a browser, record the exact API call attempted and its response."])

lane("MD74", "S5", 5,
     "California Secretary of State bizfile: METR and ARC corporate records, statements of information and officers",
     "ca-sos-bizfile-corporate",
     "the California Secretary of State bizfile Online search and its document download endpoints "
     "(bizfileonline.sos.ca.gov, including its JSON API paths), the SOS business-search bulk data, Delaware Division "
     "of Corporations entity search for the home-state record, and Wayback id_ captures",
     ["C05.E3", "C02.E4", "C08.E1"],
     ["Find bizfile Online's current public search endpoint (the site is a JavaScript shell; identify the JSON API "
      "the page calls and record every endpoint tried with HTTP status, UTC time and saved body), then locate the "
      "entity records for Model Evaluation and Threat Research, Inc. and Alignment Research Center, recording entity "
      "number, type, jurisdiction of formation, registration date in California, status, agent for service and "
      "principal address, each quoted exactly.",
      "Download every filed document bizfile publishes for each entity (foreign registration or articles, every "
      "Statement of Information, amendments, conversions), save each with SHA-256 and UTC fetch time, and record the "
      "officers and directors named on each Statement of Information with the filing date, keeping each person as a "
      "public officer in a public role and adding nothing about them from other sources.",
      "Check the home-state record (Delaware Division of Corporations entity search or the state named in the "
      "California filing) for formation date, entity type and registered agent, quoted exactly, and keep the "
      "California and home-state records as separate documents.",
      "Record the dated officer and director roster changes between consecutive Statements of Information as timeline "
      "rows, and separately note any officer who is also named on a promoted funder, lab or intermediary row, citing "
      "the promoted row id and asserting nothing beyond the two documents."])


# ---------------------------------------------------------------- MD75 (Kevin, 2026-09-16T21:05Z): when did the COI policy PDF first exist? Created by MD72's bound (about-page link absent 2026-09-14T13:20:53Z, present 2026-09-15T16:00:44Z; PDF never archived)
lane("MD75", "S5", 5,
     "First public existence of metr.org/coi-policy.pdf: archived sitemaps, third-party indexes and inbound links",
     "coi-policy-first-existence",
     "Wayback CDX and raw id_ captures of metr.org/sitemap.xml and every metr.org page between 2026-08-20 and 2026-09-16; "
     "Common Crawl index API (CC-MAIN-2026 crawls) for the PDF URL; archive.today; search-engine result dates; any third-party "
     "page, post or report that linked the PDF before 2026-09-15",
     ["C09.E2", "C09.E3", "C08.E1"],
     ["Enumerate every Wayback capture of https://metr.org/sitemap.xml from 2026-08-01 to 2026-09-16 (CDX, retry on 503, record each "
      "attempt), fetch each distinct digest raw with id_, and record for each whether it lists /coi-policy.pdf and with what lastmod; "
      "the earliest sitemap that lists the PDF bounds its existence from above and the latest that does not bounds it from below.",
      "Query the Common Crawl index API for every 2026 crawl (index list at index.commoncrawl.org/collinfo.json) for url=metr.org/coi-policy.pdf "
      "and for metr.org/about, recording crawl id, timestamp, status and digest; fetch any WARC record found and hash it; do the same on "
      "archive.today (archive.ph) and on the Wayback CDX for metr.org/*.pdf with matchType=prefix.",
      "Search for inbound links to the PDF dated before 2026-09-15: DuckDuckGo html, Bing, Bluesky and X search pages, Hacker News "
      "and LessWrong search, the AI Evaluator Forum and Transluce pages, and METR's own posts and reports from 2026-08-20 onward "
      "(raw id_ captures where live pages are JS shells); quote any page that links or names the policy with its date and hash.",
      "State the resulting bound in one row: the earliest date at which the PDF is documented to exist and the latest date at which it "
      "is documented not to be linked, with the exact capture or index record for each end; distinguish existence of the file from "
      "appearance of the link; assert nothing about why the policy appeared when it did."])
