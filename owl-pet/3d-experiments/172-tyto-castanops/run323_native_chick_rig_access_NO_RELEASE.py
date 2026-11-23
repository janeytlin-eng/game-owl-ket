#!/usr/bin/env python3
"""Run323: public/free native owl rig acquisition and real WebGL2 audit. NO_RELEASE."""
from __future__ import annotations
import hashlib, json, os, pathlib, shutil, struct, subprocess, threading, time, zipfile
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from functools import partial
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

ROOT=pathlib.Path.cwd()
OUT=ROOT/"run323-output"
OUT.mkdir(exist_ok=True)
REPORT={"run":"323","target":"#172 Tyto castanops v3 rightmost age-unknown cream mesoptile",
        "no_release":True,"extra_paid_usd":0,"sources":{},"quality_gate":"NOT_PASSED",
        "physical_phone_test":False}
def sha256(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for x in iter(lambda:f.read(1024*1024),b""):h.update(x)
    return h.hexdigest()
def dump():
    (OUT/"run323-results.json").write_text(json.dumps(REPORT,indent=2,ensure_ascii=False))
def safe(name): return name.replace("/","_")
def links(page):
    return page.locator("a").evaluate_all("(aa)=>aa.map(a=>({text:(a.innerText||'').trim().slice(0,100),href:a.href})).filter(a=>a.text||a.href).slice(0,80)")
def screenshot(page,name):
    page.screenshot(path=str(OUT/name),full_page=False)
def check_itch(browser):
    rec={"source":"https://vuena.itch.io/blocky-pets-free",
         "published_license":"publisher declares CC0 for free sample, non-target toy style",
         "role":"rig/animations technical baseline only, NOT juvenile art"}
    REPORT["sources"]["itch_cc0_toy_rig"]=rec
    page=browser.new_page(viewport={"width":1280,"height":800},accept_downloads=True)
    try:
        response=page.goto("https://vuena.itch.io/blocky-pets-free/purchase",wait_until="domcontentloaded",timeout=40000)
        rec["initial_http"]=response.status if response else None
        screenshot(page,"itch-purchase.png")
        rec["initial_title"]=page.title()
        locator=page.get_by_text("No thanks, just take me to the downloads",exact=False)
        rec["no_thanks_count"]=locator.count()
        if not locator.count():
            rec["status"]="free_link_not_visible";rec["links"]=links(page);return
        locator.first.click(timeout=20000)
        page.wait_for_load_state("domcontentloaded",timeout=30000)
        time.sleep(3)
        rec["download_page_url"]=page.url
        rec["download_title"]=page.title()
        screenshot(page,"itch-free-download.png")
        rec["download_links"]=links(page)
        # A public free-download only, never paid checkout, no session or challenge bypass.
        candidates=[x for x in rec["download_links"] if "Download" in x["text"] or "download" in x["text"].lower()]
        rec["candidate_count"]=len(candidates)
        matched=page.locator('a:has-text("Download")')
        if not matched.count(): matched=page.get_by_text("Download",exact=True)
        if not matched.count():
            rec["status"]="no_public_download_button";return
        try:
            with page.expect_download(timeout=55000) as obj: matched.first.click(timeout=15000)
            dl=obj.value
            name=dl.suggested_filename
            rec["suggested_name"]=name
            target=OUT/"itch-free-sample.zip"
            dl.save_as(str(target))
            rec.update(status="downloaded",bytes=target.stat().st_size,sha256=sha256(target))
        except Exception as e:
            rec["status"]="download_click_no_file"
            rec["download_error"]=str(e)[:600]
            rec["final_url"]=page.url
            screenshot(page,"itch-click-outcome.png")
    except Exception as e:
        rec["status"]="browser_failure";rec["error"]=str(e)[:800]
        try:screenshot(page,"itch-error.png")
        except Exception:pass
    finally: page.close()
def check_booth(browser):
    rec={"source":"https://booth.pm/ja/items/6643539",
         "role":"visually closer fluffy real 3D barn-owl chick, NOT licensed/released target",
         "published_price_jpy":0,"license":"VN3 site links: redistribution/use unverified"}
    REPORT["sources"]["booth_fluffy_barn_chick"]=rec
    page=browser.new_page(viewport={"width":1280,"height":800})
    try:
        r=page.goto(rec["source"],wait_until="domcontentloaded",timeout=40000)
        rec["page_http"]=r.status if r else None
        screenshot(page,"booth-official.png")
        rec["download_links"]=[x for x in links(page) if ("ダウンロード" in x["text"] or "download" in x["href"])][:8]
        possible=page.get_by_text("無料ダウンロード",exact=False)
        if possible.count():
            possible.first.click(timeout=20000)
            page.wait_for_load_state("domcontentloaded",timeout=25000)
            rec["post_click_url"]=page.url
            rec["post_click_title"]=page.title()
            screenshot(page,"booth-free-access-result.png")
            rec["status"]="login_required" if ("sign_in" in page.url or "login" in page.url) else "check_screenshot_for_access"
        else:rec["status"]="no_free_download_link_visible"
    except Exception as e:
        rec["status"]="browser_failure";rec["error"]=str(e)[:600]
    finally:page.close()
def inspect_zip():
    path=OUT/"itch-free-sample.zip"
    if not path.exists():return []
    rec=REPORT["sources"]["itch_cc0_toy_rig"]
    models=[]
    with zipfile.ZipFile(path) as z:
        entries=z.namelist()
        rec["zip_file_count"]=len(entries)
        rec["zip_crc_bad"]=z.testzip()
        rec["model_paths"]=[n for n in entries if n.lower().endswith((".glb",".gltf",".fbx",".blend"))][:100]
        for member in z.infolist():
            if not member.filename.lower().endswith(".glb"):continue
            if member.file_size>100_000_000:continue
            p=OUT/("source_"+safe(pathlib.Path(member.filename).name))
            if ".." in pathlib.PurePosixPath(member.filename).parts:continue
            p.write_bytes(z.read(member))
            models.append(p)
    rec["extracted_glbs"]=[]
    for m in models:
        entry={"name":m.name,"bytes":m.stat().st_size,"sha256":sha256(m)}
        try:
            raw=m.read_bytes()
            assert raw[:4]==b"glTF" and struct.unpack_from("<I",raw,4)[0]==2
            size,typ=struct.unpack_from("<I4s",raw,12)
            assert typ==b"JSON"
            g=json.loads(raw[20:20+size])
            entry["mesh_count"]=len(g.get("meshes",[]))
            entry["animations"]=[a.get("name") for a in g.get("animations",[])]
            entry["skins"]=len(g.get("skins",[]))
            entry["skin_joint_counts"]=[len(s.get("joints",[])) for s in g.get("skins",[])]
            entry["materials"]=len(g.get("materials",[]))
            entry["triangles"]=sum(int(g["accessors"][p["indices"]]["count"]/3) for mesh in g.get("meshes",[]) for p in mesh.get("primitives",[]) if p.get("mode",4)==4 and "indices" in p)
            entry["gltf_ok"]=True
        except Exception as e:entry["error"]=str(e)
        rec["extracted_glbs"].append(entry)
    return models
HTML='''<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<style>html,body{margin:0;height:100%;overflow:hidden;background:#75808c}canvas{display:block}</style>
<script type="importmap">{"imports":{"three":"/node_modules/three/build/three.module.js","three/addons/":"/node_modules/three/examples/jsm/"}}</script></head><body><script type="module">
import * as THREE from 'three';import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js';
const scene=new THREE.Scene();scene.background=new THREE.Color(0x748390);
const renderer=new THREE.WebGLRenderer({antialias:true,powerPreference:'low-power'});
renderer.setPixelRatio(1);renderer.setSize(390,780);renderer.outputColorSpace=THREE.SRGBColorSpace;
renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=1.5;
document.body.appendChild(renderer.domElement);
scene.add(new THREE.HemisphereLight(0xffffff,0x665c52,2.0));
const light=new THREE.DirectionalLight(0xfff2df,3);light.position.set(2,4,5);scene.add(light);
const camera=new THREE.PerspectiveCamera(35,390/780,0.01,100);
const loader=new GLTFLoader();
window.webglReport={webgl2:renderer.capabilities.isWebGL2,status:'pending'};
window.renderOwl=async function(src,angle){
  let gltf=await loader.loadAsync(src);scene.add(gltf.scene);
  const b=new THREE.Box3().setFromObject(gltf.scene),ctr=b.getCenter(new THREE.Vector3()),sz=b.getSize(new THREE.Vector3());
  const radius=Math.max(sz.x,sz.y,sz.z),d=radius*3.5;
  camera.position.set(ctr.x+Math.sin(angle)*d,ctr.y+0.12*radius,ctr.z+Math.cos(angle)*d);
  camera.lookAt(ctr);camera.updateProjectionMatrix();
  gltf.scene.traverse(x=>{if(x.isMesh){x.frustumCulled=false}});
  renderer.render(scene,camera);
  window.webglReport={webgl2:renderer.capabilities.isWebGL2,status:'loaded',meshCount:gltf.scene.getObjectsByProperty('isMesh',true).length,
  animationCount:gltf.animations.length,dims:sz.toArray(),yaw:angle,glError:renderer.getContext().getError()};
  scene.remove(gltf.scene);gltf.scene.traverse(x=>{if(x.isMesh)x.geometry.dispose()});
  return window.webglReport;
}
</script></body></html>'''
def browser_webgl(browser,glbs):
    if not glbs:return
    (ROOT/"run323-viewer.html").write_text(HTML)
    server=ThreadingHTTPServer(("127.0.0.1",8765),partial(SimpleHTTPRequestHandler,directory=str(ROOT)))
    thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
    page=browser.new_page(viewport={"width":390,"height":780})
    err=[];page.on("pageerror",lambda e:err.append(str(e)))
    try:
        page.goto("http://127.0.0.1:8765/run323-viewer.html",wait_until="domcontentloaded",timeout=30000)
        page.wait_for_function("!!window.renderOwl",timeout=30000)
        records=[]
        for path in glbs:
            for angle,label in [(0,"front"),(1.5707963268,"right"),(3.1415926536,"rear")]:
                try:
                    report=page.evaluate("""async ({src,angle})=>await window.renderOwl(src,angle)""",
                        {"src":"/run323-output/"+path.name,"angle":angle})
                    screenshot(page,"webgl-"+path.stem+"-"+label+".png")
                    records.append({"model":path.name,"view":label,**report})
                except Exception as e:records.append({"model":path.name,"view":label,"error":str(e)})
        REPORT["webgl2"]={"captures":records,"errors":err,
          "note":"390x780 desktop Chromium SwiftShader simulated phone; physical phone not tested"}
    except Exception as e:REPORT["webgl2"]={"error":str(e),"pageerrors":err}
    finally:page.close();server.shutdown()
def main():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,args=["--enable-unsafe-swiftshader","--use-gl=angle","--use-angle=swiftshader","--enable-webgl"])
        check_booth(browser);check_itch(browser)
        models=inspect_zip()
        browser_webgl(browser,models[:2])
        browser.close()
    REPORT["conclusion"]="Technology/rights source only; baby Tyto castanops anatomy, down, support, side/back and physical phone not validated. NO_RELEASE."
    dump()
if __name__=="__main__":
    try:main()
    except Exception as e:REPORT["fatal_error"]=str(e);dump();raise
