# Editorial team and execution contract

This is a working editorial system, not a claim that agents were already run or that pages have passed review. Logical roles can run sequentially when concurrency is limited. Keep handoffs compact and tied to actual artifacts.

## Read the context before acting

Each role reads `context/PROJECT.md`, `context/AUDIENCE.md`, and `context/ASSET-POLICY.md`, then the current topic ledger and its assigned topic packet. Read the public project's README and the relevant implementation before drafting instructions. User steering overrides these contracts; record substantive accepted steering in project context, without writing personal memory.

A topic packet must travel with the draft and implementation. The publisher must not infer missing demand or execution evidence from an author's confident prose.

## Five roles, bounded responsibilities

| Role | Owns | Required handoff |
| --- | --- | --- |
| Demand researcher | Candidate evidence and intent clustering | Qualified brief or explicit rejection, exact demand sources, search-intent observations |
| Product editor | Deliverable choice, reader promise, asset combination | Useful result, page outline, asset roles, acceptance examples |
| Author/builder | Original prose, working tool/template, examples | Draft plus source, expected outputs, test or manual-check evidence |
| Independent reviewer | Reader usefulness, demand traceability, technical and attribution checks | Pass or concrete revision requests with evidence |
| Publisher/maintainer | Atomic release, live verification, ledger, concise run report | Public URLs, release identifier, actual deployment status, corrected failures |

An author must not approve their own work. A separately invoked reviewer checks the actual draft and deliverable, not just the author's summary. The publisher may combine orchestration and maintenance; neither can bypass an unresolved review failure.

## Topic packet

Use a structured file such as `team/research/<intent-id>.json` with these fields:

```json
{
  "intent_id": "stable-task-slug",
  "status": "candidate",
  "reader": "specific reader",
  "task": "input and useful output",
  "pillar": "Documents and data",
  "primary_query": "observed query",
  "related_queries": [],
  "market": {"country": "US", "language": "en"},
  "demand_evidence": [
    {"kind": "suggestion-or-quantitative-or-question", "url": "exact source", "observed_at": "ISO date/time", "observation": "what was actually seen", "limitations": "what it cannot prove"}
  ],
  "intent_assessment": "why the proposed result fits these queries",
  "assets": [
    {"id": "stable ID", "url": "exact TokRepo asset URL", "role": "concrete contribution", "verified_at": "ISO date/time", "license_note": "link-only or permitted reuse"}
  ],
  "deliverable": {"kind": "tool-or-template-or-workflow", "source_paths": [], "sample_input": "path", "expected_output": "path"},
  "canonical_path": "proposed public route",
  "duplicate_check": {"overlaps": [], "decision": "new intent or update existing page"},
  "verification": {"level": "illustrative", "checks": [], "limitations": []},
  "review": {"reviewer": null, "decision": "pending", "report_path": null}
}
```

The exact schema can evolve with the implementation. Required evidence and truthful status must remain. Store only public research and synthetic examples in public paths.

## Hard publishing gates

A reviewer passes a page only when all applicable gates pass:

1. **Demand:** evidence satisfies `AUDIENCE.md`, is tied to the exact intent, and contains no invented volume or guaranteed ranking.
2. **Usefulness:** the page delivers its promised result. The reader can access the tool/template/example immediately; instructions describe the actual implementation.
3. **Accuracy:** consequential technical statements have current primary support; outputs match checks; execution claims use the correct verification label.
4. **Originality:** the content is original and specific to the example. No copied articles, stock introductions, generic filler, or lightly renamed variants.
5. **Asset fit:** exact TokRepo links resolve to the intended assets, roles are real, dependencies and permitted reuse are checked.
6. **Intent ownership:** no existing canonical page already serves the task. Overlap is resolved by an update or a justified separate deliverable.
7. **Product quality:** examples, downloads, copy actions, relevant mobile layout, internal navigation, and tool behavior work. No broken placeholder routes or misleading buttons.
8. **Public hygiene:** no credentials or private input, honest data-handling claims, correct project/third-party licenses, and no unapproved external actions.

A pass must point to the reviewed files and checks. Vague praise is not a review. Record `revise` with the smallest actionable correction set or `reject` with the unmet gate. Fixes return to the independent reviewer only for the changed or previously failing checks; avoid ceremonial full restarts.

## Release and daily operation

Read the canonical ledger first. Research more candidates than the publishing cap so weak topics can be discarded. Select only qualified intents whose deliverables can be completed. Build and review with scoped ownership when using agents; do not revert other collaborators' changes.

Publish at most six new canonical pages per Beijing date, across all runs. Keep a durable per-date ledger with public path, intent ID, source commit, review report, and deployment result. Re-running a day must resume or improve the existing batch rather than duplicate it.

Use GitHub tools to publish the public repository content. Use a permitted CLI only where a needed GitHub capability is absent from the available connector, such as initial Pages configuration. Do not assume a push means deployment: verify the live HTML, linked deliverables, exact asset links, and deployment status. A missing live release is an incomplete release.

Corrections to existing pages do not consume the six-new-page limit, but they still require proportionate checks. Prefer repairing a broken or misleading page over adding another page. A failed public build should preserve the previous usable release when feasible and produce a concrete failure report.

Report meaningful batch completion with the public project link, number of new/updated pages, demand basis, and material limits. Remain quiet when there is no qualified new work and no actionable problem. Never fill the cap with unsupported topics, automatically archive the chat, or expand into other promotional channels.
