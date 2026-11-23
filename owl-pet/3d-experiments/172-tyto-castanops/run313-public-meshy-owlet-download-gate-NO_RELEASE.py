#!/usr/bin/env python3
"""Run313 real public download gate for a Meshy community owlet, research-only.
No paid calls, login bypass, account creation, private endpoint probing, or release.
"""
import hashlib, json, os, pathlib, re, time, traceback, urllib.parse
import requests
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

DEST=pathlib.Path(os.getenv("OWL_RESEARCH_OUT","/tmp/owl172_run313_evidence"))
DEST.mkdir(parents=True,exist_ok=True)
URL="https://www.meshy.ai/zh/posts/Sunlit-Owlet-01a00f65-b940-70c9-817a-255fff4654d8"
INDEX="https://www.meshy.ai/tags/babybird"
result={"run":"313","utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),
        "candidate":URL,"index":INDEX,
        "target":"#172 Tyto castanops v3 rightmost AGE-UNKNOWN MESOPTILE only",
        "candidate_claim":"Meshy7 geometry + Meshy6 textures; 1986946 triangles; community CC0 publisher claim",
        "candidate_not_same_as_target":True,
        "access":"NOT_CHECKED","download":"NOT_CHECKED","model":None,"browser_webgl2":"NOT_TESTED",
        "physical_phone":"NOT_TESTED","juvenile_art":"NOT_APPROVED",
        "rights":"UPSTREAM_LICENSE_AND_ORIGINALITY_UNVERIFIED",
        "payment_usd":0,"release":False}
events=[]
def persist():
    (DEST/"source_diagnostic.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    (DEST/"network_diagnostic.json").write_text(json.dumps(events[-200:],ensure_ascii=False,indent=2)+"\n")
persist()
try:
    for name,url in [("index",INDEX),("candidate",URL)]:
        try:
            rsp=requests.get(url,timeout=30,headers={"User-Agent":"Mozilla/5.0"})
            result[name+"_http"]=rsp.status_code
            result[name+"_bytes"]=len(rsp.content)
            result[name+"_sha256"]=hashlib.sha256(rsp.content).hexdigest()
            # Retain a short textual excerpt, not a copy of the publisher's copyrighted page.
            txt=re.sub(r"<[^>]*>"," ",rsp.text)
            result[name+"_page_excerpt"]=re.sub(r"\s+"," ",txt)[:1500]
        except Exception as e:result[name+"_http_error"]=repr(e)
    persist()
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,args=["--no-sandbox","--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader"])
        context=browser.new_context(viewport={"width":1240,"height":900},device_scale_factor=1,accept_downloads=True)
        page=context.new_page()
        def onresponse(response):
            url=response.url
            if len(events)>600:return
            if any(z in url for z in (".glb",".gltf","download","mesh","model")):
                events.append({"status":response.status,"url":url[:550],"type":response.headers.get("content-type","")})
        page.on("response",onresponse)
        try:
            response=page.goto(URL,wait_until="domcontentloaded",timeout=65000)
            result["browser_http"]=response.status if response else None
            page.wait_for_timeout(6500)
            page.screenshot(path=str(DEST/"browser_initial_desktop.png"),full_page=False)
            result["browser_title"]=page.title()
            result["visible_text"]=page.locator("body").inner_text(timeout=20000)[:8500]
            result["controls"]=page.evaluate("""() => [...document.querySelectorAll('button,a,[role=button]')].map(x=>({
                tag:x.tagName, label:(x.innerText||x.getAttribute('aria-label')||x.title||'').trim().slice(0,110),
                href:x.tagName==='A'?x.href:null, disabled:x.disabled||x.getAttribute('aria-disabled')==='true'
            })).filter(x=>x.label||x.href).slice(0,130)""")
            result["access"]="VISIBLE_PUBLIC_PAGE" if "Sunlit Owlet" in result["visible_text"] else "PUBLIC_BROWSER_NOT_CONFIRMED"
            # Normal visible download control. No spoofed auth, no private API calls.
            patterns=re.compile(r"^(download|下载|免费下载|下载模型|download model|free download|立即下载|indirmek|herunterladen)",re.I)
            candidates=[]
            controls=page.locator("button,a,[role=button]")
            for i in range(min(controls.count(),160)):
                el=controls.nth(i)
                try:
                    title=(el.inner_text(timeout=1000) or el.get_attribute("aria-label") or "").strip()
                    if patterns.search(title) and el.is_visible(timeout=500):
                        candidates.append({"index":i,"title":title[:110]})
                except Exception:pass
            result["public_download_controls"]=candidates
            if not candidates:
                result["download"]="NO_VISIBLE_PUBLIC_DOWNLOAD_CONTROL"
            else:
                clicked=False
                for c in candidates[:3]:
                    el=controls.nth(c["index"])
                    try:
                        with page.expect_download(timeout=16000) as dl_info:
                            el.click(timeout=5000)
                        dl=dl_info.value
                        clicked=True
                        filename=pathlib.Path(dl.suggested_filename).name
                        suffix=pathlib.Path(filename).suffix.lower()
                        result["clicked_control"]=c
                        result["download_filename"]=filename
                        if suffix not in [".glb",".gltf",".zip"]:
                            result["download"]="NON_MODEL_DOWNLOAD_"+suffix
                        else:
                            output=DEST/("unreviewed_juvenile_candidate"+suffix)
                            dl.save_as(str(output))
                            blob=output.read_bytes()
                            result["download_bytes"]=len(blob)
                            result["download_sha256"]=hashlib.sha256(blob).hexdigest()
                            if suffix==".glb" and blob[:4]==b"glTF":
                                result["download"]="NATIVE_GLB_BYTES_ACQUIRED_UNREVIEWED"
                                result["model"]=str(output.name)
                            else:result["download"]="DOWNLOAD_FILE_REQUIRES_VALIDATION"
                        break
                    except PWTimeout:
                        clicked=True
                        result["clicked_control"]=c
                        page.wait_for_timeout(2300)
                        text=page.locator("body").inner_text()[:8500]
                        if re.search(r"sign.?in|log.?in|登录|註冊|注册|需要登录",text,re.I):
                            result["download"]="PUBLIC_BUTTON_LOGIN_GATE"
                        else:result["download"]="CLICK_NO_BROWSER_DOWNLOAD"
                        break
                    except Exception as e:
                        result["button_click_error"]=repr(e)
                if not clicked:result["download"]="VISIBLE_BUTTON_CLICK_FAILED"
            page.screenshot(path=str(DEST/"browser_after_public_download_attempt.png"),full_page=False)
            result["after_click_visible_text"]=page.locator("body").inner_text(timeout=15000)[:6000]
            # A clearly visible direct .glb anchor is a normal public download.
            if not result["model"]:
                anchors=[c for c in result["controls"] if c.get("href") and re.search(r"\.(glb|gltf)(\?|$)",c["href"],re.I)]
                result["public_direct_glb_anchors"]=anchors[:10]
                for a in anchors[:2]:
                    url=a["href"]
                    if not url.startswith("https://"):continue
                    try:
                        rr=requests.get(url,timeout=60,stream=True)
                        if rr.status_code!=200:continue
                        chunks=[];size=0
                        for part in rr.iter_content(1<<18):
                            size+=len(part)
                            if size>125_000_000:raise ValueError("125MB limit")
                            chunks.append(part)
                        blob=b"".join(chunks)
                        if blob[:4]!=b"glTF":continue
                        output=DEST/"unreviewed_juvenile_candidate.glb"
                        output.write_bytes(blob)
                        result.update(download="DIRECT_PUBLIC_GLB_ACQUIRED_UNREVIEWED",
                                      model=output.name,download_bytes=len(blob),
                                      download_sha256=hashlib.sha256(blob).hexdigest())
                        break
                    except Exception as e:result.setdefault("direct_download_errors",[]).append(repr(e))
            # Also confirm phone-sized page UI / WebGL2 environment (NOT a physical phone).
            phone=context.new_page(viewport={"width":390,"height":780})
            try:
                phone.goto(URL,wait_until="domcontentloaded",timeout=45000)
                phone.wait_for_timeout(1700)
                phone.screenshot(path=str(DEST/"browser_mobile_viewport.png"))
                result["phone_viewport_http"]="loaded"
            except Exception as e:result["phone_viewport_error"]=repr(e)
            phone.close()
        except Exception as e:
            result["browser_error"]=repr(e)
            result["access"]="BROWSER_BLOCKED"
            try:page.screenshot(path=str(DEST/"browser_failure.png"))
            except Exception:pass
        browser.close()
    if result["model"]:
        try:
            import trimesh
            modelpath=DEST/result["model"]
            model=trimesh.load(str(modelpath),force="scene",process=False)
            geometry={
                "file_sha256":hashlib.sha256(modelpath.read_bytes()).hexdigest(),
                "genuine_glb_magic":modelpath.read_bytes()[:4]==b"glTF",
                "mesh_count":len(model.geometry),
                "triangles":int(sum(len(g.faces) for g in model.geometry.values())),
                "bounds":model.bounds.tolist(),
                "materials":sum(getattr(getattr(g.visual,"material",None),"image",None) is not None for g in model.geometry.values()),
                "art":"NOT_REVIEWED, NEVER APPROVED BY GEOMETRY METRICS",
                "phone":"NOT_TESTED",
                "release":False
            }
            (DEST/"native_model_geometry.json").write_text(json.dumps(geometry,indent=2))
            result["model_geometry"]=geometry
        except Exception as e:result["model_parse_error"]=repr(e)
except Exception as e:
    result["exception"]=repr(e)
    result["traceback"]=traceback.format_exc()[-4500:]
finally:
    result["release"]=False
    result["payment_usd"]=0
    persist()
    (DEST/"STRICT_NO_RELEASE.txt").write_text(
        "Run313 / #172 / community owlet source access research only.\n"
        "NOT the target Tasmanian masked owl juvenile. DO NOT deploy, redistribute or claim finished.\n"
        "Native model, proper mask, short down-covered wing, real side/back, rights and phone QA ALL required.\n")
    print(json.dumps(result,ensure_ascii=False,indent=2))
