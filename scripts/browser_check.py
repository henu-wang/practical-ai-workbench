"""Exercise actual downloads in an isolated Chrome browser against a local or public site."""
import csv, hashlib, io, json, os, subprocess, sys, tempfile, time
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image
from source_hash import source_hash
from playwright.sync_api import sync_playwright, expect
ROOT=Path(__file__).resolve().parent.parent
local=len(sys.argv)<2
BASE=sys.argv[1].rstrip('/') if not local else 'http://127.0.0.1:8792'
server=None
if local:
 server=subprocess.Popen([sys.executable,'-m','http.server','8792','--bind','127.0.0.1','--directory',str(ROOT/'docs')],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 time.sleep(.4)
records=[]; external=[]; errors=[]
def pdf_widths(path):
 code="const fs=require('fs');const {PDFDocument}=require('./docs/vendor/pdf-lib-1.17.1.min.js');PDFDocument.load(fs.readFileSync(process.argv[1])).then(p=>console.log(JSON.stringify(p.getPages().map(x=>x.getWidth()))));"
 return json.loads(subprocess.check_output(['node','-e',code,str(path)],cwd=ROOT))
try:
 with tempfile.TemporaryDirectory() as tmp, sync_playwright() as p:
  browser=p.chromium.launch(channel='chrome',headless=True)
  context=browser.new_context(accept_downloads=True)
  context.on('request',lambda request: external.append(request.url) if not request.url.startswith(BASE+'/') and not request.url.startswith(('blob:','data:')) else None)
  page=context.new_page();page.on('pageerror',lambda error:errors.append(str(error)))
  def run(slug,filename):
   with page.expect_download() as event:
    page.locator('#run').click();page.locator('#download').click()
   download=event.value;target=Path(tmp)/filename;download.save_as(target)
   assert target.stat().st_size>0
   return target
  for slug in ['merge-pdf','extract-pdf-pages','compress-image','resize-image','remove-duplicate-csv-rows','csv-to-json']:
   response=page.goto(BASE+'/'+slug+'/',wait_until='networkidle')
   assert response.status==200, (slug,response.status,page.url)
   print('Checking',slug,flush=True)
   page.locator('#run').click();assert page.locator('#status').get_attribute('class')=='status error'
   page.locator('#try-sample').click();page.wait_for_function("document.getElementById('status').textContent.startsWith('Example ready')")
   target=run(slug,slug+'.out')
   if slug=='merge-pdf':assert pdf_widths(target)==[300,350,420]
   elif slug=='extract-pdf-pages':assert pdf_widths(target)==[350,300]
   elif slug in ['compress-image','resize-image']:
    with Image.open(target) as image:
     expected=(1200,800) if slug=='compress-image' else (600,400)
     assert image.size==expected and image.format=='JPEG'
    assert target.stat().st_size < (ROOT/'docs/samples/sample-image.png').stat().st_size
   elif slug=='remove-duplicate-csv-rows':
    rows=list(csv.reader(io.StringIO(target.read_text())))
    assert len(rows)==4 and rows[1][2]=='hello, world' and rows[3][2]=='line one\nline two'
   else:
    rows=json.loads(target.read_text());assert len(rows)==4 and rows[0]['note']=='hello, world'
   summary=page.locator('#result-summary').inner_text()
   records.append({'slug':slug,'sample_download':'PASS','empty_input':'PASS','download_name':page.locator('#download').get_attribute('download'),'output_bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'summary':summary})
   if slug=='merge-pdf':
    page.locator('#file-list li').nth(1).get_by_role('button',name='Move up',exact=True).click()
    assert pdf_widths(run(slug,'reordered.pdf'))==[420,300,350]
   if slug=='extract-pdf-pages':
    page.locator('#pages').fill('0');page.locator('#run').click();expect(page.locator('#status')).to_contain_text('between 1 and 2');assert not page.locator('#result').is_visible()
    page.locator('#pages').fill('1');assert pdf_widths(run(slug,'one-page.pdf'))==[300]
   if slug in ['compress-image','resize-image']:
    page.locator('#format').select_option('image/webp');output=run(slug,'image.webp')
    with Image.open(output) as image:assert image.format=='WEBP'
    page.locator('#width').fill('0');page.locator('#run').click();expect(page.locator('#status')).to_contain_text('positive')
   if slug=='remove-duplicate-csv-rows':
    page.locator('#csv-text').fill('name,email\nAda,a@x.test\nBob,b@x.test\nAda New,A@x.test')
    page.locator('#key-column').fill('email');page.locator('#ignore-case').check();page.locator('#keep').select_option('last')
    data=list(csv.reader(io.StringIO(run(slug,'last.csv').read_text())));assert [r[0] for r in data[1:]]==['Bob','Ada New']
   if slug=='csv-to-json':
    page.locator('#csv-text').fill('id,note\n001,"hello, world"');data=json.loads(run(slug,'zeros.json').read_text());assert data[0]['id']=='001'
    page.locator('#csv-text').fill('id,id\n1,2');page.locator('#run').click();assert 'unique' in page.locator('#status').inner_text()
   page.locator('#reset').click();assert not page.locator('#result').is_visible()
   records[-1]['valid_variant']='PASS';records[-1]['reset_and_error_recovery']='PASS'
   page.set_viewport_size({'width':390,'height':844});page.goto(BASE+'/'+slug+'/',wait_until='networkidle')
   assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),slug+' horizontal overflow'
   page.locator('#try-sample').click();page.wait_for_function("document.getElementById('status').textContent.startsWith('Example ready')")
   page.locator('#run').click();page.locator('#download').wait_for(state='visible')
   records[-1]['mobile_viewport']='PASS';page.set_viewport_size({'width':1280,'height':900})
  print('All task cases passed; capture homepage.',flush=True)
  page.goto(BASE+'/',wait_until='networkidle');page.screenshot(path=str(ROOT.parent/('homepage-public.png' if not local else 'homepage-local.png')),full_page=True)
  version=browser.version
  assert not errors,errors
  assert not external,external
  out={'verified_at':datetime.now(timezone.utc).isoformat(),'base_url':BASE,'reviewed_source_sha256':source_hash(),'browser':'Chrome '+version,'status':'PASS','tested_page_count':len(records),'file_content_uploads':'none observed; no third-party network requests during tasks','external_requests':external,'page_errors':errors,'cases':records}
  (ROOT/'team/reviews').mkdir(parents=True,exist_ok=True)
  (ROOT/'team/reviews'/('browser-local.json' if local else 'browser-public.json')).write_text(json.dumps(out,indent=2)+'\n')
  print(f"PASS: {len(records)} browser task pages; real downloads, errors, variants, mobile and network checks.",flush=True)
  print('Closing isolated browser.',flush=True)
  browser.close()
finally:
 if server:server.terminate();server.wait(timeout=5)
