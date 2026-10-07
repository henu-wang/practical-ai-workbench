# Practical AI Workbench — project contract

Status: proposed product contract for the replacement editorial system. Public repository, Pages URL, and deployed capabilities must be verified by the publisher before they are represented as available.

## Product and promise

Accepted project name: **Practical AI Workbench**. Repository slug: `practical-ai-workbench`. Public creation and deployment remain unverified until the publisher records them.

An open source workbench for everyday work: useful local tools, editable templates, realistic examples, and concise instructions that help an English-speaking reader finish a task. The reader arrives with a problem, gets an immediate result, and can adapt the source.

The main audience is an individual knowledge worker, freelancer, or small-business operator. Developer integrations are supporting material. The default editorial subject is the task, such as cleaning a CSV or preparing meeting notes, rather than the underlying AI framework.

The first result must not require an AI API key. AI is an optional extension for interpretation or a more complex follow-up task, not a dependency added to a deterministic conversion. User-selected files must remain in the browser; the implementation and network checks must establish this before the page makes a privacy claim.

TokRepo supplies relevant reusable assets and further exploration. A page must be useful even before the reader follows a TokRepo link. Links identify the actual contributing assets and explain their roles. Distinguish a library actually used in the tool from a related workflow offered as an optional extension.

## Four content pillars

| Pillar | Reader results | Suitable deliverables |
| --- | --- | --- |
| Documents and data | Clean a table, extract document fields, prepare information for analysis | Local utility, sample file, schema, validation checklist |
| Writing and communication | Turn rough notes into a useful email, summary, or brief | Editable template, filled example, constrained prompt, review checklist |
| Meetings and planning | Turn a transcript or notes into decisions, owners, and next actions | Structured template, sample input/output, exportable result |
| Content repurposing | Turn existing material into a new useful format | Working converter or generator, editing template, original worked example |

These pillars are a scope boundary, not a mandate to publish an equal number in each. Specific topics require current demand evidence and compatible assets. Broad terms such as “AI tools” are not automatically strong candidates: the project must serve the intent behind a query.

## Minimum usable product

The first release must include all of the following:

1. One working tool for a validated everyday task. It accepts a realistic input and produces a useful, inspectable output. If browser based, run the task locally where feasible and make input handling explicit.
2. At least two reusable templates with filled examples. Their purpose and limitations must be visible without an account or setup guide.
3. A public site with clear task navigation, working asset/source links, and download or copy actions for the deliverables.
4. A repository containing the actual tool source, examples, tests appropriate to the tool, a documented local run command, contribution instructions, and an explicit license for original project material.
5. A topic ledger and demand evidence that let a maintainer see why each page exists and which search intent it serves.

Implementation selected by the coordinator for the first product: browser-local PDF merging/page extraction, image resizing/compression, and CSV deduplication/JSON conversion, plus downloadable task templates. Each individual public task route still needs verified demand, a checked example, and a review pass; listing it here is not evidence that it exists or works. Include runnable example inputs and expected outcomes so readers and reviewers can reproduce the result without their private files.

“Open source” requires real maintained source and a license. A collection of Markdown articles, an “awesome” list, or a Pages skin is insufficient to satisfy this product contract. Use an existing repository when doing so preserves a coherent product; creating additional repositories has no editorial value by itself.

The earlier `tokrepo-guides` repository and URLs remain accessible but no longer receive daily new tutorials. Its home page can naturally direct readers to this replacement product. Do not break old routes, fabricate historical product capability, or continue a second article factory alongside the new workbench.

## Page contract

Each public page must contain:

- A clear result and an accurate description of who it helps.
- An immediately useful deliverable: working tool, editable template, complete original example, or runnable workflow. A prompt alone needs a filled example and an output-checking method.
- The minimum steps needed to reproduce or adapt that result.
- One realistic input/output pair that is identified as tested, manually checked, or illustrative. Never blur those categories.
- Checks that help a reader spot a wrong output, plus relevant failure cases and limits.
- Exact TokRepo asset URLs, with a short role for each; upstream technical references where needed.

Prefer two to four assets when the combination contributes distinct capabilities. One asset plus original glue is acceptable when it is the honest design. Do not pad asset counts or invent integration work.

## Outcomes and constraints

The daily cap is six new pages per Beijing calendar day. A cap is not a quota. Publish fewer or none when research, product usefulness, or review does not pass. Improvements to an existing intent page are usually better than title variants.

Measure organic discovery separately from publication: confirmed live pages, search indexing, impressions/clicks, engaged use of the deliverable, and outbound visits to relevant TokRepo assets. Do not claim traffic before it is measured, and do not treat GitHub views as search traffic.

No public credentials, private logs, copied third-party assets without permission, fabricated benchmarks, invented search volumes, paid model executions, or unrelated social outreach. Publishing this project does not authorize modifications to the TokRepo production application.
