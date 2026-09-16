<!-- casework-lane {"claim_id":"C05","elements":["C05.E3","C06.E4","C10.E2"],"materializer":2,"outputs":["research/grok-out/MD51-audit-framing.csv"],"pack":"metr_deep","plan_lane":"MD51","plan_sha256":"7ff1e5a3d68d5eadfdb76c0ff002060e21ce4adbff1fa3c5c6ef52d5cad0f9e2"} -->

# MD51 — Framing, entity and causality adversarial audit

Plan directive:

Slice S5, wave 5. This lane belongs to /mnt/f/projects/anthropic/metr_deep/PLAN.md; its id, slug and scope are frozen and are never renumbered or repurposed.

Scope: Framing, entity and causality adversarial audit.
Primary routes: promoted rows, figures and written synthesis.

Embargo: this lane sends nothing and contacts nobody. It may read any public material published by METR, a funder, an intermediary, a lab or a government body, but it may not email, message, telephone, file, submit or post anything, and it may not ask anyone how the approximately $71 million commitment total was composed or allocated. A draft is not a transmission; any draft this lane writes stays unsent.

Row typing: put the target table prefix in target_prefix on every row (MDE entity, MDF funding event, MDI in-kind or access, MDP provenance proposition, MDQ project conflict, MDR relationship, MDS source coverage and bounded negative, MDT timeline event) and put the case element ids this row would support in element_ids, semicolon separated, from: C05.E3, C06.E4, C10.E2. Leave any column that does not apply to a row empty rather than guessing.

Task A — Find every place where two legal entities are merged, where a person stands in for an organisation, or where an employer stands in for an individual.
Task B — Find every place where adjacency, shared employment, friendship, office space or investor status is used as if it were a money flow.
Task C — Find every motive, coordination or dependence conclusion whose required elements are not independently supported, and every use of motive vocabulary in figure text.
Task D — State whether the exhaustion gate can be approved on the framing side, and list every correction required first.
Task E — Record a bounded negative for every source class named in this lane that returned no responsive record: the exact query, endpoint or document, the filters, the result count, the UTC check time and the known blind spot. Write one row per source checked with target_prefix=MDS. Never write an unbounded negative and never leave a task silent.

Output `research/grok-out/MD51-audit-framing.csv` with columns: `row,task,target_prefix,element_ids,subject,entity_type,aliases,identifier,from_entity,intermediary,to_entity,relationship_type,start_date,end_date,ledger,money_type,amount_usd,currency,date,date_precision,period,payment_status,purpose_restriction,project,provider,in_kind_type,quantity_or_value,terms,policy_version,disclosure_recusal,provider_authority,personnel_conflicts,edge_type,documented_transaction,source_class,query_or_endpoint,url,quote_300,checked_utc,result,result_count,next_document,limitation,note`.

Standard goal:

```text
/goal Run research/grok-briefs/MD51-audit-framing.md exactly as written; write only research/grok-out/MD51-audit-framing.csv and research/primary/MD51-audit-framing/
```

Rules: fetch and write only; no network or system changes (never nmcli, resolvectl, protonvpn, sudo, systemctl, ip, iptables, nft); never send, submit, email, post, file or publish anything, and never contact METR, a funder, a donor, an employee or a records custodian - this lane only reads public material; primary sources first (issuer, recipient and funder documents, then government filings and procurement records, then retained archives, then named on-record statements, then high-quality press; a secondary database is used only to locate a primary); every row carries url, quote_300 verbatim, source_class, checked_utc in UTC, and a note giving provenance and limits; every row must have a non-empty url naming the exact page, endpoint or document checked - a none-found row cites the URL of the source that was searched; write "none found in <exact source> as of <UTC date>" for every task with no responsive record, never "nothing more can be pulled" and never an unbounded negative; keep legal entities separate (individual, employer, investment vehicle, foundation, DAF sponsor, DAF account, grantmaker, project, recipient) and never merge two because they are connected; keep money types separate in money_type (commitment, paid_grant, filed_grant, recommendation, transfer, regrant, contract, in_kind_estimate, equity_value) and never sum across types, periods or currencies; a commitment is not a payment and an award is not a receipt; assert no motive about any person or organization and name only public people in public roles; never deanonymize a private donor, a DAF adviser or a Jane Street individual by probabilistic matching; record a search failure reproducibly (exact term, endpoint, filters, result count, UTC) rather than omitting it; do not use posts by @kevinnbass as sources, they may only point to a source located independently; where a live URL is dead use Wayback (web.archive.org/web/2024*/<url>, raw with id_) or the r.jina.ai proxy and say so in note; save every primary document relied on under research/primary/<lane>/ with the UTC fetch time in the filename; put a header comment in the CSV giving fetch window, routes used, caps hit and no_kevinnbass_sources; before adding a fact read research/STATE.md so nothing already held is recollected; write only the named output file and the named primary directory.
