"""Release gate for reviewed, demand-backed TokRepo asset recipes."""
import hashlib,json,re
from pathlib import Path
from collections import Counter
from datetime import datetime
from html.parser import HTMLParser
from urllib.parse import urlparse,parse_qs,unquote
from source_hash import ROOT,source_hash

def read(name):return json.loads((ROOT/name).read_text())
recipes=read('recipes.json')['recipes'];slugs={x['slug'] for x in recipes}
assert len(slugs)==len(recipes), 'Duplicate canonical recipe'
reviews=[]
review_packets=[]
for p in (ROOT/'team/reviews').glob('recipes-review-*.json'):
 packet=json.loads(p.read_text())
 stamp=packet.get('reviewed_at') or packet.get('observed_at')
 assert stamp, 'Missing independent review timestamp: '+str(p)
 observed=datetime.fromisoformat(stamp)
 assert observed.tzinfo is not None, 'Review timestamp must include timezone: '+str(p)
 review_packets.append((observed,p.name,packet))
for _,_,packet in sorted(review_packets):reviews.extend(packet['pages'])
by_slug={x['slug']:x for x in reviews}
demand={}
packets=[ROOT/'team/research/redirect-demand.json']+sorted((ROOT/'team/research').glob('demand-????-??-??.json'))
for packet in packets:
 for topic in json.loads(packet.read_text())['recipes']:
  assert topic['slug'] not in demand, 'Duplicate demand brief: '+topic['slug']
  demand[topic['slug']]=topic
for recipe in recipes:
 slug=recipe['slug'];review=by_slug[slug]
 assert review['verdict']=='PASS' and not review['blockers'], 'Unresolved editor blocker: '+slug
 assert review['author']!=review['reviewer'], 'Self review: '+slug
 expected_files={str(p.relative_to(ROOT)) for p in (ROOT/'templates'/slug).rglob('*') if p.is_file()}
 expected_files.add('recipes/'+slug+'.md')
 assert set(review.get('file_sha256',{}))==expected_files, 'Incomplete final source/template review: '+slug
 for name,digest in review.get('file_sha256',{}).items():
  assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest, 'Stale reviewed template: '+name
 assert review['content_sha256']==hashlib.sha256((ROOT/'recipes'/f'{slug}.md').read_bytes()).hexdigest(), 'Stale content review: '+slug
 topic=demand[slug]
 assert topic['autocomplete'] and len({q['url'] for q in topic['questions']})>=2, 'Missing demand evidence: '+slug
 assert 2<=len(recipe['assets'])<=4, 'Missing real asset combination: '+slug
 assert all(a['url'].startswith('https://tokrepo.com/en/workflows/') and a['role'] for a in recipe['assets'])
 assert (ROOT/'templates'/slug).is_dir(), 'Missing original usable example: '+slug
receipt=read('team/reviews/recipes-browser.json')
assert receipt['status']=='PASS' and receipt['source_sha256']==source_hash(), 'Missing/stale browser verification'
assert not receipt['page_errors']
ledger=read('team/ledger.json')['entries']
active=[x for x in ledger if x.get('program')=='asset_search' and x.get('action')=='new_topic']
assert all(n<=6 for n in Counter(x['published_on'] for x in active).values()), 'Daily new-topic cap exceeded'
assert len({x['dedupe_key'] for x in active})==len(active), 'Duplicate topic ledger entry'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1':self.h1+=1
  for key in ['href','src']:
   if key in a:self.links.append(a[key])
for path in [ROOT/'docs/index.html']+list((ROOT/'docs/workflows').glob('*/index.html')):
 text=path.read_text();p=Page();p.feed(text)
 assert p.h1==1 and '<html lang="en">' in text and 'rel="canonical"' in text
 for link in p.links:
  if link.startswith(('#','https:','http:','data:')):continue
  dest=(path.parent/unquote(urlparse(link).path)).resolve()
  assert dest.is_relative_to(ROOT/'docs'), 'Local path escapes site'
  if dest.is_dir():dest=dest/'index.html'
  assert dest.is_file(), f'Broken local link: {path}: {link}'
for recipe in recipes:
 path=ROOT/'docs/workflows'/recipe['slug']/'index.html';p=Page();p.feed(path.read_text())
 asset_links=[link for link in p.links if link.startswith('https://tokrepo.com/en/workflows/')]
 for link in asset_links:
  q=parse_qs(urlparse(link).query)
  assert q=={'utm_source':['github_pages'],'utm_medium':['referral'],'utm_campaign':['tokrepo_search'],'utm_content':[recipe['slug']]}, 'Wrong attribution: '+link
 assert {urlparse(x).path for x in asset_links}>={urlparse(a['url']).path for a in recipe['assets']}
for required in ['LICENSE','README.md','AGENTS.md','docs/vendor/pdf-lib.LICENSE.md','docs/vendor/papaparse.LICENSE']:
 assert (ROOT/required).stat().st_size>0
print('PASS: independent recipe review, demand evidence, asset combinations, original downloads, browser receipt, internal links, UTM and daily cap.')
