"""Fail publication on stale review, missing demand, broken links, or unverified tools."""
import hashlib,json,re,subprocess
from collections import Counter
from pathlib import Path
from html.parser import HTMLParser
from source_hash import ROOT,source_hash

def read(name):return json.loads((ROOT/name).read_text())
review=read('team/reviews/content-review.json')
browser=read('team/reviews/browser-local.json')
assert review['verdict']=='PASS', 'Independent content review is not PASS'
assert review['reviewed_source_sha256']==source_hash(), 'Content review is stale'
assert browser['reviewed_source_sha256']==source_hash(), 'Browser verification is stale'
assert browser['status']=='PASS' and not browser['external_requests'] and not browser['page_errors']
assert review.get('reviewer') and review.get('author') and review['reviewer']!=review['author'], 'Review must be independent'
tasks=read('tasks.json')['tasks'];slugs={x['slug'] for x in tasks}
assert len(slugs)==len(tasks), 'Duplicate canonical task'
ledger=read('team/ledger.json')['entries'];assert len({x['dedupe_key'] for x in ledger})==len(ledger)
assert all(n<=6 for n in Counter(x['published_on'] for x in ledger).values()), 'Daily publication cap exceeded'
assert review['demand_evidence_sha256']==hashlib.sha256((ROOT/'team/research/demand.json').read_bytes()).hexdigest(), 'Demand review is stale'
demand=read('team/research/demand.json');seeds={x['seed']:x for x in demand['demand']}
for topic in demand['first_batch']:
 assert topic['slug'] in slugs
 assert topic['exact_observed_suggestion'] in seeds[topic['seed']]['suggestions'], 'Missing exact observed search intent'
 questions=demand['user_questions'][topic['slug']]
 assert len({q['url'] for q in questions})>=2 and all(q.get('question_intent') for q in questions), 'Missing independent public questions'
 assert topic['monthly_search_volume'] is None or topic['monthly_search_volume']>0
pages={x['slug']:x for x in review['pages']};assert set(pages)==slugs
for slug,page in pages.items():
 assert page['verdict']=='PASS' and not page['blockers'], 'Unresolved page blocker: '+slug
 scores=list(page['scores'].values());assert len(scores)==6 and min(scores)>=3 and sum(scores)>=24, 'Low editorial score: '+slug
cases={x['slug']:x for x in browser['cases']};assert set(cases)==slugs
for row in cases.values():
 for key in ['sample_download','empty_input','valid_variant','reset_and_error_recovery','mobile_viewport']:assert row[key]=='PASS'
 assert row['output_bytes']>0 and row['sha256']
assets=read('team/research/asset-registry.json');byurl={a['url']:a for a in assets}
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1':self.h1+=1
  for key in ['href','src']:
   if key in a:self.links.append(a[key])
for page in (ROOT/'docs').rglob('*.html'):
 text=page.read_text();parsed=Links();parsed.feed(text)
 assert parsed.h1==1 and '<html lang="en">' in text and 'rel="canonical"' in text
 for link in parsed.links:
  if link.startswith(('#','https:','http:','blob:','data:')):continue
  destination=(page.parent/link.split('#')[0]).resolve()
  if destination.is_dir():destination=destination/'index.html'
  assert destination.is_file(),f'Broken local link in {page.name}: {link}'
for task in tasks:
 text=(ROOT/'content'/f"{task['slug']}.md").read_text()
 links=re.findall(r'https://tokrepo\.com/en/workflows/[^)\s]+',text)
 assert links, 'No exact asset backlink: '+task['slug']
 for link in links:
  assert link in byurl and byurl[link]['public_status']==200 and byurl[link]['slug_in_page'], 'Unverified asset: '+link
for required in ['LICENSE','README.md','CONTRIBUTING.md','AGENTS.md','docs/vendor/pdf-lib.LICENSE.md','docs/vendor/papaparse.LICENSE']:
 assert (ROOT/required).stat().st_size>0
subprocess.run(['npm','test'],cwd=ROOT,check=True,stdout=subprocess.DEVNULL)
print('PASS: independent source-bound review, qualitative demand, 6 usable tasks, asset links, privacy scope, license, daily cap and local references.')
