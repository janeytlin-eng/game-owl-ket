#!/usr/bin/env python3
"""Run319: real no-fee PUBLIC Hunyuan3D-2mini Turbo UI trial; no release.
Only use model URLs directly observed from user's own generated UI session.
Never solve CAPTCHAs, request private tokens, create paid jobs or invent geometry.
"""
import hashlib, json, os, re, time, traceback
from pathlib import Path
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright

OUT=Path('owl172-run319-evidence');OUT.mkdir(exist_ok=True)
SOURCE=Path('owl172-run295-evidence/young-REAL-PHOTO-PIXELS-transparent-input-NO_3D.png')
EXPECTED= '37e2b3c96da31c558f511ee172b43bec4c721186a074327ec6cb791c9d2c5ed8'
HOST='tencent-hunyuan3d-2mini-turbo.hf.space'
SITE='https://'+HOST+'/'
def digest(b):return hashlib.sha256(b).hexdigest()
def save(name,data): (OUT/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
def snap(page,name):
    try:page.screenshot(path=str(OUT/name),timeout=18000)
    except Exception as e: report.setdefault('screenshot_errors',[]).append(str(e)[:160])
def body(page):
    try:return page.locator('body').inner_text(timeout=4000)[-6000:]
    except Exception:return ''
def controls(page):
    return page.evaluate("""() => ({
       buttons: [...document.querySelectorAll('button')].filter(x=>x.getClientRects().length)
                  .map(x=>({label:(x.innerText||x.getAttribute('aria-label')||'').trim().slice(0,95),disabled:x.disabled})).slice(0,70),
       files:[...document.querySelectorAll('input[type=file]')].map(x=>({accept:x.accept,multiple:x.multiple})),
       links:[...document.querySelectorAll('a[href]')].filter(x=>x.getClientRects().length).map(x=>({text:x.innerText.slice(0,45),href:x.href.slice(0,140)})).slice(0,20)
    })""")
report={'run':'319','date_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
        'target':'#172 Tyto castanops v3 concept rightmost cream mesoptile',
        'source':'Original repository v3 plate, no edits',
        'service':'Tencent Hunyuan3D-2mini-Turbo public free Hugging Face Space',
        'provider_url':SITE,'used_free_public_ui':True,'paid_or_authenticated':False,
        'generation_clicked':False,'valid_native_glb':False,'webgl2_qa_pass':False,
        'natural_down_art_pass':False,'rights_cleared':False,'physical_phone_tested':False,
        'release':False,'status':'INITIAL','observations':[]}
events=[]
def persist():
    save('result.json',report)
    save('public_network_observations.json',events[-120:])
def record_response(r):
    try:
        u=r.url
        if any(q in u for q in ('queue','/upload','/file=','.glb','.obj','.zip','.gltf','.ply')):
            events.append({'url_path':urlparse(u).path[:190],'status':r.status,'mime':r.headers.get('content-type','')[:100]})
    except Exception:pass
def candidate_urls(page):
    links=page.evaluate("""() => [...document.querySelectorAll('a[href],gradio-model3d,model-viewer,[src]')]
       .map(e=>e.href||e.getAttribute('src')||e.getAttribute('value')||'').filter(Boolean)
       .filter(u=>/\.(glb|gltf|obj|zip)(\?|$)|\/file=/.test(u)).slice(0,50)""")
    # DOM-advertised model urls only, never guess hidden server paths
    return links
def get_native_from_observed(page):
    import trimesh
    items=[]
    for r in raw_model_responses:
        items.append(('actually_loaded_response',r))
    for u in candidate_urls(page):
        if u.startswith('/'):u=SITE.rstrip('/')+u
        items.append(('DOM_download_link',u))
    seen=set()
    for where,url in items:
        if url in seen:continue
        seen.add(url)
        try:
            hostname=urlparse(url).hostname or ''
            if not url.startswith('https://') or not (hostname.endswith('.hf.space') or hostname=='huggingface.co'):continue
            rsp=page.request.get(url,timeout=35000)
            buf=rsp.body()
            if rsp.status!=200 or len(buf)>80_000_000 or len(buf)<1000 or buf[:4]!=b'glTF':continue
            scene=trimesh.load(file_obj=__import__('io').BytesIO(buf),file_type='glb',force='scene',process=False)
            faces=sum(len(g.faces) for g in scene.geometry.values())
            if faces<1500:continue
            name='hunyuan-mini-ORIGINAL-UNREVIEWED-NO_RELEASE.glb'
            (OUT/name).write_bytes(buf)
            report['native_glb']={'filename':name,'bytes':len(buf),'sha256':digest(buf),
                 'triangle_count':faces,'geometry_count':len(scene.geometry),'origin':where}
            report['valid_native_glb']=True
            return True
        except Exception as e:report.setdefault('native_errors',[]).append(str(e)[:150])
    return False
raw_model_responses=[]
assert SOURCE.is_file(), 'missing original rightmost chick source'
actual=digest(SOURCE.read_bytes());report['reference_sha256']=actual
assert actual==EXPECTED, 'original reference unexpectedly changed'
persist()
try:
    with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True,args=['--no-sandbox','--disable-dev-shm-usage',
                                  '--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader'])
        page=browser.new_page(viewport={'width':1280,'height':850},accept_downloads=True)
        page.on('response',record_response)
        def observe_model(r):
            try:
                if re.search(r'\.(glb|gltf)(\?|$)|/file=',r.url,re.I) and r.status==200:
                    raw_model_responses.append(r.url)
            except Exception:pass
        page.on('response',observe_model)
        try:
            rsp=page.goto(SITE,wait_until='domcontentloaded',timeout=65000)
            report['initial_http']=rsp.status if rsp else None
            page.wait_for_timeout(7000)
            report['initial_controls']=controls(page); report['initial_body']=body(page)[-2200:]
            snap(page,'initial_public_ui.png');persist()
            if report['initial_http']!=200:raise RuntimeError('PUBLIC_SPACE_HTTP_NOT_200')
            if re.search('checking your browser|verify you are human|cloudflare|security verification',report['initial_body'],re.I):
                raise RuntimeError('CAPTCHA_OR_CLOUDFLARE_BLOCKED')
            files=page.locator('input[type=file]')
            if files.count()<1:raise RuntimeError('NO_PUBLIC_UPLOAD_WIDGET')
            files.first.set_input_files(str(SOURCE.resolve()),timeout=16000)
            page.wait_for_timeout(6000)
            report['post_upload_controls']=controls(page);report['post_upload_text']=body(page)[-2200:]
            snap(page,'rightmost_chick_uploaded.png')
            if re.search('sign in|log in|authentication required|quota exceeded',report['post_upload_text'],re.I):
                report['account_or_quota_warning']=True
            generate=page.get_by_role('button',name=re.compile(r'^(Gen Shape|Gen Textured Shape|Generate Shape|Generate 3D|Generate)$',re.I))
            for i in range(generate.count()):
                if generate.nth(i).is_visible() and generate.nth(i).is_enabled():
                    report['clicked_button']=generate.nth(i).inner_text()[:120]
                    generate.nth(i).click(timeout=13000)
                    report['generation_clicked']=True
                    break
            if not report['generation_clicked']:raise RuntimeError('NO_ENABLED_PUBLIC_GENERATE_BUTTON')
            report['status']='PUBLIC_GENERATION_CLICKED';persist()
            started=time.monotonic()
            while time.monotonic()-started<210:
                page.wait_for_timeout(9000)
                txt=body(page)
                report['observations'].append({'seconds':int(time.monotonic()-started),'body_tail':re.sub(r'\s+',' ',txt)[-580:],
                    'real_file_links':len(candidate_urls(page))})
                if get_native_from_observed(page):
                    report['status']='GENUINE_NATIVE_GLB_ACQUIRED_UNREVIEWED'
                    break
                if re.search('quota exceeded|exceeded your ZeroGPU|insufficient quota|no GPU available|unauthorized|error while generating|runtime error|not enough credits',txt,re.I):
                    report['status']='PROVIDER_QUOTA_OR_RUNTIME_ERROR'
                    break
            if not report['valid_native_glb'] and report['status']=='PUBLIC_GENERATION_CLICKED':
                report['status']='PUBLIC_GENERATION_NO_NATIVE_GLB'
            report['final_body']=body(page)[-3000:]
            report['final_controls']=controls(page)
            snap(page,'final_public_UI.png')
        finally:
            persist(); page.close();browser.close()
except Exception as e:
    report['error']=repr(e)
    report['traceback']=traceback.format_exc()[-1600:]
    if not report['valid_native_glb']:report['status']='PUBLIC_UI_BLOCKED_OR_TEST_ERROR'
finally:
    (OUT/'STRICT_NO_RELEASE.txt').write_text(
      'Research only; 3D can be art-unacceptable. No release until soft down, heart face, side/back, '
      'feet, legal rights and physical phone WebGL validated.\n',encoding='utf8')
    report['finished_utc']=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())
    persist()
    print(json.dumps({'status':report['status'],'initial_http':report.get('initial_http'),
      'generation_clicked':report['generation_clicked'],'native_glb':report.get('native_glb'),
      'error':report.get('error')},ensure_ascii=False,indent=2))
