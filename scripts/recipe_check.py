"""Validate actual rendered guides, downloaded template bytes and mobile layout."""
import hashlib,json,threading,http.server,socketserver,functools
from pathlib import Path
from datetime import datetime,timezone
from urllib.parse import urlparse,unquote
from playwright.sync_api import sync_playwright
from source_hash import ROOT,source_hash
recipes=json.loads((ROOT/'recipes.json').read_text())['recipes']
handler=functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(ROOT/'docs'))
class Quiet(handler.func):
 def log_message(self,*args):pass
with socketserver.TCPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(ROOT/'docs'))) as server:
 threading.Thread(target=server.serve_forever,daemon=True).start();base=f'http://127.0.0.1:{server.server_address[1]}/'
 report={'recorded_at':datetime.now(timezone.utc).isoformat(),'source_sha256':source_hash(),'status':'PASS','scope':'Rendered guide and original downloadable templates; no claim that third-party models ran','page_errors':[],'pages':[]}
 with sync_playwright() as p:
  browser=p.chromium.launch(channel='chrome',headless=True)
  page=browser.new_page(viewport={'width':1280,'height':800})
  page.on('pageerror',lambda error:report['page_errors'].append(str(error)))
  for recipe in recipes:
   slug=recipe['slug'];response=page.goto(base+'workflows/'+slug+'/',wait_until='networkidle');assert response.status==200
   assert page.locator('h1').count()==1 and page.locator('h1').inner_text()==recipe['title']
   assert page.locator('link[rel=canonical]').get_attribute('href')==json.loads((ROOT/'recipes.json').read_text())['site_url']+'workflows/'+slug+'/'
   assert page.locator('.asset-card').count()==len(recipe['assets'])
   assert page.locator('.page-title a.primary').get_attribute('href').startswith(recipe['assets'][0]['url']+'?')
   downloads=[]
   hrefs=page.locator('article a[href*="templates/"]').evaluate_all('(nodes)=>nodes.map(n=>n.href)')
   assert hrefs, 'No discoverable template download: '+slug
   for href in dict.fromkeys(hrefs):
    result=page.request.get(href);assert result.status==200 and len(result.body())>0
    local=ROOT/'docs'/unquote(urlparse(href).path).lstrip('/')
    assert local.read_bytes()==result.body(), 'Wrong template bytes'
    downloads.append({'path':str(local.relative_to(ROOT/'docs')),'bytes':len(result.body()),'sha256':hashlib.sha256(result.body()).hexdigest()})
   page.set_viewport_size({'width':390,'height':844})
   assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth'), 'Mobile horizontal page overflow: '+slug
   report['pages'].append({'slug':slug,'render':'PASS','primary_cta':'PASS','mobile':'PASS','template_downloads':downloads})
   page.set_viewport_size({'width':1280,'height':800})
  page.goto(base,wait_until='networkidle');assert page.locator('#workflows .card').count()==len(recipes)
  page.screenshot(path='/tmp/tokrepo-workflows-home.png',full_page=True)
  browser.close()
 server.shutdown()
assert not report['page_errors']
(ROOT/'team/reviews/recipes-browser.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS:',len(recipes),'rendered recipes, actual template bytes, asset CTAs and mobile layouts. Model runtime not tested.')
