# Measurement and monitoring contract

## Funnel states are independent

| State | Required evidence | Does not prove |
| --- | --- | --- |
| Published | Public deployed page matches reviewed source and links work | Crawlability, indexing, visibility, visits |
| Crawlable | Reachable HTML, meaningful content, allowed robots behavior, canonical/sitemap checks | Google has indexed the URL |
| Indexed | Current GSC URL Inspection result for the exact canonical URL, with check time | Ranking, impressions, or users |
| Search visibility | GSC Search Analytics observations, date range, filters, queries/countries and positions where available | Monthly query volume or TokRepo visits |
| Search clicks | GSC reported clicks for the measured scope | GitHub page engagement or TokRepo arrival |
| TokRepo arrival | Available inbound sessions attributable to the agreed UTM campaign/content | Engaged sessions, asset use, installs |
| Useful asset follow-through | Available explicitly defined engagement/asset-use/install events | Uninstrumented behavior or overall product success |

Never substitute direct search browsing for GSC indexing evidence. GSC average position belongs to its reported query/country/device/date scope; it is not a universal fixed rank. Record impressions and clicks as returned, with aggregation and filters.

If GSC returns no rows, report “no rows returned for this scope” plus date range, filters, access status, and possible freshness/aggregation limits. Do not label that as 0, unindexed, no demand, or a tool outage without separate evidence. Numeric zero is valid only when the tool explicitly reports zero for the metric.

When inbound tracking or asset-use events are unavailable, record those funnel fields as `unknown` with the missing capability. UTM links do not establish analytics implementation. Read-only access is authorized; adding events or changing TokRepo production is outside scope.

## Review cadence and cohort ledger

The user authorized continued read-only indexing/ranking review. Use a weekly review of active pages and a separate 28-day publication cohort review. Record page age, canonical URL, publish/update dates, last inspection, measured interval, country/query scope, impressions, clicks, reported position, TokRepo UTM sessions, engaged sessions and asset-use evidence where available.

Compare equal, explicit windows for a cohort rather than mixing new and mature pages. Preserve previous observations so changes are auditable. Respect source rate/access restrictions and avoid repeated unchanged polling. Missing data triggers a concrete access/instrumentation note, not invented metrics.

## Action tree

- **Not indexed according to Inspection:** investigate this repository's reachability, canonical consistency, accidental noindex/robots, sitemap, internal links, and distinctive task content. Apply supported fixes and record the changed source. Do not promise that requesting indexing guarantees inclusion.
- **Indexed but too little observed visibility:** retain the page and gather the next appropriate window; assess intent and distribution evidence without guessing a rank or declaring failure from a tiny sample.
- **Meaningful impressions but weak clicks:** inspect observed query fit, title/description honesty, and whether the page offers the searched result. Rewrite the relevant title/intent element and compare a subsequent recorded window.
- **Search clicks but few measured TokRepo arrivals:** first verify UTM measurement coverage; then inspect CTA visibility, asset relevance and prerequisites. Improve the page's actual handoff rather than adding unrelated backlinks.
- **Measured arrivals without measured use:** check whether use events exist before drawing a conclusion. Review whether the asset instructions deliver the promised task; production instrumentation or asset changes require separate scope.
- **Insufficient observations at any branch:** defer that conclusion with a next review date. No fabricated conversion rates, universal numerical thresholds, or traffic promises.

Every change should identify the observed problem, expected reader improvement, affected page/source, and next comparison window. Report meaningful findings, completed fixes, or actionable access failures. Quiet unchanged monitoring is acceptable; do not emit repeated “still waiting” status or manufacture daily rewrites.
