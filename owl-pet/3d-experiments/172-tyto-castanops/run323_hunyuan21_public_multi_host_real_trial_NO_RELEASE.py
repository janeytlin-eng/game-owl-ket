#!/usr/bin/env python3
"""Run323 – actual, no-extra-fee public Hunyuan3D-2.1 UI attempts.
Research ONLY; use only publicly displayed site controls/downloads, never infer a
GLB from a preview. Stop on payment/login/quota/security challenge. NO RELEASE.
"""
import hashlib, json, re, time, traceback, io
from pathlib import Path
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright
OUT=Path('owl172-run323-evidence');OUT.mkdir(exist_ok=True)
REF=Path('owl172-run295-evidence/young-isolated-white-background-input-NO_3D.png')
REF_SHA='6ec346e5b02411f9509fd364db748c23a58075aeec461ef7424adcc4d893bc77'
SITES=[
  ('tencent-official-hunyuan21','https://tencent-hunyuan3d-2-1.hf.space/'),
  ('mfurkanyener-hunyuan3d','https://mfurkanyener-hunyuan3d-demo.hf.space/'),
  ('dylanebert-hunyuan21','https://dylanebert-hunyuan3d-2-1.hf.space/'),
]
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2,default=str)+'\n',encoding='utf8')
def body(page):
  try:return page.locator('body').inner_text(timeout=6500)[-3000:]
  except Exception:return ''
def controls(page):
  try:return page.evaluate("""() => ({
    buttons:[...document.querySelectorAll('button')].filter(x=>x.getClientRects().length)
      .map(x=>({text:(x.innerText||x.getAttribute('aria-label')||'').trim().slice(0,80),disabled:x.disabled})).slice(0,65),
    files:[...document.querySelectorAll('input[type=file]')].map(x=>({accept:x.accept,multiple:x.multiple})),
    anchors:[...document.querySelectorAll('a[href]')].filter(x=>x.getClientRects().length)
      .map(x=>({label:(x.innerText||'').slice(0,50),href:x.href.slice(0,180)})).slice(0,28)
  })""")
  except Exception as e:return {'error':str(e)[:200]}
def snap(page,name):
  try:page.screenshot(path=str(OUT/name),timeout=22000,full_page=False)
  except Exception:pass
def discover(page):
  try:return page.evaluate("""() => [...document.querySelectorAll('a[href],gradio-model3d,model-viewer,[src]')]
    .map(e=>e.href||e.getAttribute('src')||e.getAttribute('value')||'')
    .filter(Boolean).filter(u=>/\.(glb|gltf|obj|zip)(\?|$)|\/file=/.test(u)).slice(0,35)""")
  except Exception:return []
def eligible(url):
  u=urlparse(url)
  return u.scheme=='https' and (u.hostname or '').endswith('.hf.space')
def try_glb(page,urls,record):
  import trimesh
  for url in urls:
    if url in record['attempted_model_urls']:continue
    record['attempted_model_urls'].append(url)
    if not eligible(url):continue
    try:
      rsp=page.request.get(url,timeout=30000)
      if rsp.status!=200:continue
      data=rsp.body()
      if len(data)<1000 or len(data)>80_000_000 or data[:4]!=b'glTF':continue
      scene=trimesh.load(file_obj=io.BytesIO(data),file_type='glb',force='scene',process=False)
      tris=sum(len(m.faces) for m in scene.geometry.values())
      if tris<1000:continue
      out=OUT/(record['name']+'_ACTUAL-UNREVIEWED-NO_RELEASE.glb')
      out.write_bytes(data)
      record['native_model']={'filename':out.name,'bytes':len(data),
                              'sha256':sha(data),'triangles':tris,'geometry_count':len(scene.geometry)}
      return True
    except Exception as e:
      record.setdefault('model_errors',[]).append(str(e)[:230])
  return False

def main():
  if not REF.is_file():raise FileNotFoundError('Exact rightmost reference not reconstructed')
  if sha(REF.read_bytes())!=REF_SHA:raise ValueError('Original #172 rightmost source reference SHA changed')
  report={'run':323,'target':'#172 Tyto castanops v3 rightmost cream-white age-unknown mesoptile chick',
     'reference_sha256':REF_SHA,'run_context':'public browser only, no accounts or paid credit',
     'paid_usd':0,'art_approved':False,'physical_phone_tested':False,'rights_approved':False,
     'production_251_untouched':True,'release':False,'providers':[],'native_models':0}
  dump(OUT/'report.json',report)
  with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True,args=['--no-sandbox','--disable-dev-shm-usage',
      '--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader'])
    for name,site in SITES:
      rec={'name':name,'url':site,'status':'PENDING','generation_clicked':False,
           'uploaded_reference':False,'attempted_model_urls':[],'observations':[]}
      report['providers'].append(rec);dump(OUT/'report.json',report)
      page=None
      raw_urls=[]
      try:
        page=browser.new_page(viewport={'width':1170,'height':810},accept_downloads=True)
        def capture(r):
          try:
            if r.status==200 and re.search(r'\.(glb|gltf)(?:\?|$)|/file=',r.url,re.I):
              if eligible(r.url):raw_urls.append(r.url)
          except Exception:pass
        page.on('response',capture)
        rsp=page.goto(site,wait_until='domcontentloaded',timeout=60000)
        rec['http_status']=rsp.status if rsp else None
        page.wait_for_timeout(7000)
        rec['initial_text']=body(page)[-1800:]
        rec['initial_controls']=controls(page)
        snap(page,name+'_initial.png')
        if rec['http_status']!=200:
          rec['status']='PUBLIC_HOST_HTTP_NOT_200';continue
        if re.search('checking your browser|verify you are human|security verification|captcha|cloudflare',rec['initial_text'],re.I):
          rec['status']='SECURITY_CHALLENGE_STOP';continue
        if re.search('out of credits|quota exceeded|zeroGPU quota|payment required|login to continue',rec['initial_text'],re.I):
          rec['status']='PUBLIC_QUOTA_OR_PAYMENT_STOP';continue
        inputs=page.locator('input[type=file]')
        if inputs.count()==0:
          # one additional chance for Gradio to hydrate without login or private APIs
          page.wait_for_timeout(9000)
          inputs=page.locator('input[type=file]')
        if inputs.count()==0:
          rec['status']='NO_PUBLIC_IMAGE_UPLOAD_CONTROL';continue
        inputs.first.set_input_files(str(REF.resolve()),timeout=20000)
        rec['uploaded_reference']=True
        page.wait_for_timeout(6000)
        rec['post_upload_text']=body(page)[-1400:]
        rec['post_upload_controls']=controls(page)
        snap(page,name+'_uploaded.png')
        if re.search('out of credits|quota exceeded|zeroGPU quota|payment required|login to continue',rec['post_upload_text'],re.I):
          rec['status']='PUBLIC_QUOTA_OR_PAYMENT_STOP';continue
        # ONLY a real visible enabled public generate control, never hidden API probing.
        loc=page.get_by_role('button',name=re.compile(r'^(Generate|Generate 3D|Generate Shape|Generate Mesh|Gen Shape|Gen Textured Shape|Create 3D|Submit)$',re.I))
        clicked=False
        for i in range(min(20,loc.count())):
          btn=loc.nth(i)
          if btn.is_visible() and btn.is_enabled():
            label=btn.inner_text().strip()[:100]
            if 'pro' in label.lower() or 'credit' in label.lower():continue
            btn.click(timeout=18000);rec['clicked_button']=label;clicked=True;break
        rec['generation_clicked']=clicked
        if not clicked:
          rec['status']='NO_ENABLED_PUBLIC_GENERATE_BUTTON';continue
        rec['status']='FREE_PUBLIC_GENERATION_CLICKED'
        start=time.monotonic()
        while time.monotonic()-start<210:
          page.wait_for_timeout(7500)
          txt=body(page)
          rec['observations'].append({'seconds':round(time.monotonic()-start,1),
            'body_tail':re.sub(r'\s+',' ',txt)[-700:],'model_url_count':len(raw_urls)})
          all_urls=raw_urls+discover(page)
          if try_glb(page,all_urls,rec):
            rec['status']='GENUINE_NATIVE_GLB_ACQUIRED_UNREVIEWED';report['native_models']+=1;break
          if re.search('exceeded your ZeroGPU|quota exceeded|out of credits|insufficient quota|need to login|sign in to|not enough GPU|runtime error|internal server error|error generating',txt,re.I):
            rec['status']='FREE_PROVIDER_RUNTIME_OR_QUOTA_BLOCK';break
        if rec['status']=='FREE_PUBLIC_GENERATION_CLICKED':
          rec['status']='NO_OBSERVED_NATIVE_GLB_WITHIN_TEST_WINDOW'
        rec['final_text']=body(page)[-1500:]
        snap(page,name+'_final.png')
      except Exception as e:
        rec['status']='ACCESS_OR_SCRIPT_ERROR';rec['error']=str(e)[:900]
        rec['traceback']=traceback.format_exc()[-1000:]
        if page:snap(page,name+'_exception.png')
      finally:
        if page:page.close()
        dump(OUT/'report.json',report)
    browser.close()
  (OUT/'STRICT_NO_RELEASE.txt').write_text(
    'Research only. No release. No representation as successful juvenile sculpt until genuine '
    'heart face, soft real volumetric down, tucked wings and back, feet/contact, rights, '
    'multi-view artistic approval and real mobile performance all verified.\n',encoding='utf8')
  dump(OUT/'report.json',report)
  print(json.dumps({'provider_statuses':[(x['name'],x['status']) for x in report['providers']],
                    'native_models':report['native_models'],'release':False},indent=2))

if __name__=='__main__':main()
