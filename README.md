# metr_deep: a public-records reconstruction of METR's funding, in-kind support and project independence

This repository is an investigation pack. It reconstructs, from public records only, what money, in-kind resources, access, personnel relationships and governance conditions support METR (Model Evaluation and Threat Research, Inc., EIN 99-1219864), which of those have documented Anthropic investor or company connections, and how far each statement about them can be taken on the documents that exist.

The pack was built on 16 September 2026 by a plan-driven pipeline (`PLAN.md`) of 59 research lanes, two adversarial audits, seven figure audits and a claim gate. Every fact lives in a row of `research/*.csv`, carries its source URL, an exact quote, the lane that found it and a review verdict, and is bound to one or more elements of the ten claims in `case.json`. Nothing enters the tables except through a reviewed promotion, and rows are never deleted; corrections append a note.

## The posted figure and the current one

On 14 September 2026 a figure about METR's funding was posted publicly (repository `kevinnbass/metr-money-figure`, commit `f64df65`). This pack treats that figure as a set of claims under adjudication, never as evidence. Of its sixteen claims, two are accurate as stated, eleven are incomplete (they say more than the documents support, and the exact missing document is named for each) and three are undetermined. The scorecard is `figures/metr-deep-09-posted-claims-scorecard.html`, and the framing defects the audit found in the posted figure are listed in `research/agents-2026-09-16/AUDIT-FRAMING.md`. The six figures under `figures/metr-deep-01…06` are the current, corrected versions of the posted set; figures 07 to 30 are a second series covering everything the pack holds.

## The strongest statement the documents support

METR's 14 August 2026 funding update says it raised commitments of around $71 million in the previous six months. Public records identify exactly one commitment compatible with that sentence in money type, period and currency: a $350,000 Packard Foundation grant listed in July 2026. The remaining roughly $70.65 million of commitments has no public source: no donor, vehicle, amount or date for it appears in any filing, database, archive or statement the pack checked. Every other known amount to METR (the 2024 ARC spin-out transfer of about $4.5 million, the 2024 Audacious/Canary commitment of about $17 million later restated as "a bit under $16m", Vanguard Charitable's $4,000,000 filed grant for the year to June 2025, and the smaller filed, recommended and regranted amounts) is earlier or of a different money type and is set aside with its reason recorded (`research/commitment_reconciliation.csv`).

METR's only filed Form 990 (May to December 2024) reports $13.6 million of revenue, of which $4.5 million came from Alignment Research Center and $9.1 million from contributors the public copy does not name. No payment or contract from Anthropic, OpenAI, Google DeepMind, Meta or Amazon to METR appears in any checked filing; lab support is in-kind access, tokens and credits, quantified in only two of METR's own statements. One conflict-of-interest policy version exists (dated 28 August 2026); every named METR assessment before that date ran with none in force.

## The strongest statement the documents do not support

That any identified person or organisation composed the $71 million, or that any Anthropic-connected supporter's money reached METR through a documented transaction. The pack finds no transaction into METR from Good Ventures Foundation, Open Philanthropy, Coefficient Giving, the individual Dustin Moskovitz, or any vehicle that might hold his donated Anthropic stake. The two donor-advised lines to METR (Vanguard $4,000,000; SVCF $20,000) have no identifiable principal, by the structure of those filings. Statements about the donated stake name no legal entity, share class, amount or transfer date. Each of these is a bounded negative over the sources named on the rows, not a finding that nothing was given.

## What could still change the picture

`research/calendar.csv` lists the ten documents not yet published (METR's CY2025 Form 990 and any audited statement; Good Ventures Foundation's FY2026 990-PF; the DAF sponsors' next returns; any Anthropic registration statement; the Audacious partners' next filings) with their earliest expected dates. Five public-record requests (UK DSIT FOI, US NIST FOIA, EU access to documents, an NPT public-inspection request and an IRS Form 4506-A) were drafted and not sent; a single consolidated request to METR for the unresolved cells was drafted and not sent. The drafts are held outside this repository until a decision to send is taken. `research/EXHAUSTION-GATE.json` records the state of the public frontier with its 22 exceptions.

## How to read the pack

- `research/CLAIMS.md`: verdict per claim and per element, with counts of evidence, primary-strength rows and bounded negatives.
- `research/FIGURES.md`: index of the thirty figures, each self-contained HTML under `figures/` with a PNG under `figures/png/`. Every figure cites row ids, carries an unknown block, keeps money types on separate axes and names only public people in public roles.
- `research/*.csv`: the eight tables (entities, funding events, in-kind and access, provenance propositions, project conflicts, relationships, source coverage and bounded negatives, timeline). Money types (commitment, paid grant, filed grant, transfer, recommendation, regrant, contract, in-kind estimate, equity value) are never summed across type.
- `research/agents-2026-09-16/`: per-lane review records, the money and framing audits with their resolution states, and the seven figure audits.
- `research/PRIMARY-MANIFEST.csv`: path, size and SHA-256 of all 11,583 saved primary documents (3.6 GB, kept outside this repository).
- `LEDGER.jsonl`, `CHANGELOG.md`, `research/LANES.csv`, `research/receipts/`: the append-only record of every lane, review, promotion and slice closure.

## Rules the pack follows

Legal entities are kept separate (a person, an employer, an investment vehicle, a foundation, a donor-advised sponsor and an account are never merged because they are connected). A page or archive date bounds when a page changed, never when money moved. No private donor, donor-advised adviser or Jane Street individual is identified by inference. No motive vocabulary appears in any figure. A claim under adjudication is never evidence.

## Verification

```
cd <casework engine> && python3 -m casework verify --pack metr_deep
python3 scripts/lint_figures.py
python3 scripts/check_s6.py
```

The engine used is the `casework` package; the pack's `casework.json` and `case.json` define the claims, elements, source classes and banned vocabulary.
