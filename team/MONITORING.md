# Publication, indexing and TokRepo attribution review

The business journey is English search intent → public recipe/template → matching TokRepo asset → supported use. A GitHub commit or HTTP 200 is not indexing, ranking, a visit or asset use. Record each state separately; unavailable account data stays unknown.

## Repeatable daily public checks

Run from the repository:

    python3 scripts/monitor_public.py --output /tmp/tokrepo-public-monitor.json

Without --output, the script creates a unique JSON receipt in the system temporary directory, outside the repository. --manifest, --site-url, --timeout, --workers and --recipe-prefix support deployed hosts or local QA fixtures. Do not commit account exports, tokens or private analytics to this public repository.

The script reads recipes.json, requests the home page and every canonical workflow URL, checks self-canonical and meta/X-Robots directives, checks sitemap membership, and requests template links actually present in public HTML. An attachment returning HTML instead of its advertised file is flagged. Records include UTC times, original/final URLs, HTTP status, safe public headers and exceptions.

Exit codes: 0 technical pass; 1 failure; 2 needs review because effective robots state is unknown or a recipe has no discoverable template link. Missing template links never get an invented PASS. Indexing and GSC fields remain unknown/null. Attachment HTTP 200 still requires editorial validation that the file opens and matches its example.

On a project Pages URL such as https://henu-wang.github.io/practical-ai-workbench/, the effective robots file is **https://henu-wang.github.io/robots.txt**, not /practical-ai-workbench/robots.txt. The latter is informational and cannot grant crawling permission. Host-root 404 is recorded as missing; Google's documented behavior assumes no crawl restrictions for 4xx other than 429, but this establishes neither a Googlebot visit nor an indexed URL. Network errors, 429 and 5xx stay unknown because this script cannot see Google's cached robots state. See [Google's robots interpretation](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec).

Daily action: investigate changed failures, compare the last receipt and deployed revision, make a scoped fix and repeat the affected check. Do not narrate an unchanged all-green receipt or infer traffic improved.

## D3, D7 and D14 URL Inspection

Anchor D0 to each URL's verified public release date, not draft or commit date. At D3, D7 and D14, inspect canonical home/recipe URLs through authorized GSC access when available. Record inspection time and URL, stored indexing/coverage state, last crawl, crawl/index permission, declared canonical, Google-selected canonical and sitemap association. Missing fields stay unknown; report permission/connector gaps precisely.

A live inspection test means current fetchability; indexed URL results describe Google's stored state. Do not substitute one for the other. Crawled-but-not-indexed and discovered-but-not-indexed require different diagnoses. Investigate technical blockers first, then intent fit, duplication and distinct reader value. A correction receives an action record and dated follow-up inspection. Request indexing only through an available authorized tool; record its actual response, never invented submission or success.

## Weekly settled GSC and TokRepo attribution

Use reporting periods GSC shows as complete. Record property, timezone, report dates, search type, country filters, page scope, completeness/freshness and extraction time. Compare like-for-like seven-day periods; incomplete rows are not settled. Inspect:

- Page: impressions, clicks, CTR, average position, and indexing state as separate measurements.
- Query: actual matched intent, impressions/clicks/CTR/position; withheld or anonymized queries are not zero.
- Country: US, UK, Canada, Australia and relevant English-speaking markets separately, then total. Country is not a language detector.
- Position: preserve GSC's aggregate metric/context; it is not a fixed manual rank.

Do not sum detailed query rows as if they necessarily equal headline totals. Record privacy filtering, truncation and row limits. Zero observed clicks is a valid result; unavailable rows are unknown. When connectors are inaccessible, continue public technical work and identify exactly which indexing/performance fields could not be verified.

Outbound asset URLs use:

    utm_source=github_pages
    utm_medium=referral
    utm_campaign=tokrepo_search
    utm_content=<canonical-recipe-slug>

In available TokRepo inbound analytics, inspect attributed sessions/users and asset destinations by that UTM tuple and recipe slug. Record date range, source system, metric definitions, filters and freshness. Tagged links enable potential attribution; they do not prove analytics captures it. An asset visit is not installation/use. Count supported use only when an actual product event/receipt establishes it; otherwise asset_use remains unknown.

Keep GSC clicks, page availability and TokRepo sessions in different columns. Consent, blockers, redirect stripping and differing counting windows can cause discrepancies; use observable evidence before assigning causes. The script never authenticates to GSC/GA4/TokRepo and contains no token or invented account measurements.

## D28 queue review

At D28 for the cohort, review settled evidence for each recipe and corresponding TokRepo destinations. Decide whether to improve the same canonical page, merge overlapping intents, hold a weak draft, or pursue a demonstrably different task. Impressions without clicks suggest inspecting query/title/intent; arrivals without asset visits suggest inspecting CTA relevance; asset visits without a supported use event leave that outcome unknown.

Do not promise ranking within 28 days or delete a page solely for no early clicks. Sparse evidence and delayed indexing limit decisions. Maximum six qualified new intents per Beijing day is a cap, not a quota.

## Evidence and action record

Private inspection/analytics receipts stay outside this public repository. Public technical receipts may be intentionally included after checking they contain no credentials/private account data. Every correction records:

|Field|Required content|
|---|---|
|Observed at / URL / revision|UTC timestamp, canonical URL, verified source/deployed revision|
|Evidence|Technical receipt or restricted inspection/report reference; exact state and period|
|Diagnosis|Observation versus inference; missing data and alternatives|
|Before|Relevant status, title/canonical/CTA or measurement with source/window|
|Action|Scoped change and independent reviewer when editorial content changes|
|After|Verified technical/functional outcome or comparable settled metric; pending is acceptable|
|Follow-up|Specific retest/inspection date, expected observation and owner|

Example: D7 inspection selects a different canonical → investigate overlap/internal links → revise the appropriate existing page → verify public canonical/sitemap → inspect again D14. Technical correction and Google's eventual indexed canonical remain separate outcomes. Date retests; content/input changes invalidate affected old PASS reports.
