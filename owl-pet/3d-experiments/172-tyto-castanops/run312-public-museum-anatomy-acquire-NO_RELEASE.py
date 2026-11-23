#!/usr/bin/env python3
"""Run312: attempt public-URL acquisition of a museum CC0 Tyto alba anatomy reference.
NO RELEASE: adult taxidermy cannot substitute the target #172 juvenile sculpt.
Normal requests / rendered public click only; never bypass access controls or spend.
"""
import hashlib, json, os, pathlib, re, time, urllib.parse
import requests
from bs4 import BeautifulSoup

ROOT=pathlib.Path(os.environ.get("OWL_RESEARCH_OUT","/tmp/owl172_run312_evidence"))
ROOT.mkdir(parents=True,exist_ok=True)
PAGE="https://doc.ayootech.com/galeri"
UPSTREAM="https://sketchfab.com/3d-models/barn-owl-0e65de5934db4f0eae02835ba7227dcc"
out={"run":"312","utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),
     "source":PAGE,"upstream":UPSTREAM,"intent":"adult Tyto alba surface/facial disc morphology REFERENCE ONLY",
     "target":"#172 Tyto castanops v3 rightmost downy chick",
     "release":False,"payment_usd":0,"rights":"CC0 claimed by museum Sketchfab source; not independently proven for mirrored file",
     "art":"NOT_A_CANDIDATE; adult specimen cannot pass juvenile art gate"}
def record():
    (ROOT/"source_diagnostic.json").write_text(json.dumps(out,indent=2,ensure_ascii=False))
record()
try:
    resp=requests.get(PAGE,headers={"User-Agent":"Owl172Research/1.0 public model provenance"},timeout=50)
    out["page_http"]=resp.status_code
    out["page_content_bytes"]=len(resp.content)
    out["page_sha256"]=hashlib.sha256(resp.content).hexdigest()
    resp.raise_for_status()
    soup=BeautifulSoup(resp.text,"html.parser")
    nodes=soup.find_all(string=lambda s:s and s.strip()=="Barn owl")
    out["matching_text_nodes"]=len(nodes)
    cards=[]
    for node in nodes:
        p=node.parent
        for level in range(1,9):
            if p is None: break
            a=[{"text":x.get_text(" ",strip=True)[:120],"href":x.get("href"),"download":x.get("download")} for x in p.find_all("a")]
            cards.append({"level":level,"tag":p.name,"classes":p.get("class"),"links":a[:15],
                          "excerpt":str(p)[:3000]})
            p=p.parent
    (ROOT/"public_card_dom_excerpt.json").write_text(json.dumps(cards[:12],indent=2,ensure_ascii=False))
    links=[]
    for c in cards:
        for l in c["links"]:
            h=l.get("href")
            if h and ("Unduh" in (l.get("text") or "") or re.search(r"\\.glb(?:[?#]|$)",h,re.I) or l.get("download") is not None):
                url=urllib.parse.urljoin(PAGE,h)
                if url.startswith("https://") and url not in links:
                    links.append(url)
    out["public_download_candidates"]=links[:12]
    record()
    if not links:
        out["status"]="NO_PUBLIC_DIRECT_LINK_IN_HTML"
        # A real browser can identify dynamically attached link only if visible publicly.
        try:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as p:
                browser=p.chromium.launch(headless=True,args=["--no-sandbox"])
                page=browser.new_page(viewport={"width":1200,"height":800})
                page.goto(PAGE,wait_until="domcontentloaded",timeout=60000)
                page.wait_for_timeout(3000)
                matches=page.get_by_text("Barn owl",exact=True)
                out["browser_matches"]=matches.count()
                if matches.count():
                    e=matches.first.evaluate("""el=>{
                      let a=el,rows=[];
                      for(let i=0;i<8&&a;i++,a=a.parentElement){
                        rows.push({depth:i,html:a.outerHTML.slice(0,4000),
                        anchors:[...a.querySelectorAll('a')].slice(0,12).map(x=>({text:x.textContent.trim(),href:x.href,download:x.download}))});
                      }
                      return rows;
                    }""")
                    (ROOT/"browser_card_dom_excerpt.json").write_text(json.dumps(e,indent=2,ensure_ascii=False))
                    for r in e:
                        for a in r["anchors"]:
                            u=a["href"]
                            if u.startswith("https://") and ("Unduh" in a["text"] or ".glb" in u.lower() or a["download"]):
                                if u not in links: links.append(u)
                    out["public_download_candidates"]=links[:12]
                browser.close()
        except Exception as ex:
            out["browser_diagnostic_error"]=repr(ex)
    # Only follow normal, public download link; avoid any login / special API.
    accepted=[]
    for url in links[:5]:
        if "sketchfab.com" in urllib.parse.urlparse(url).hostname: continue
        try:
            r=requests.get(url,stream=True,timeout=90,headers={"User-Agent":"Mozilla/5.0"})
            status=r.status_code; ctype=r.headers.get("Content-Type","")
            note={"url":url,"status":status,"type":ctype}
            if status!=200:
                accepted.append(note);r.close();continue
            p=ROOT/"museum_tyto_alba_CC0_CLAIM_REFERENCE_ONLY.glb"
            h=hashlib.sha256(); size=0
            with p.open("wb") as f:
                for ch in r.iter_content(chunk_size=1<<18):
                    if not ch:continue
                    size+=len(ch)
                    if size>100_000_000:raise ValueError("size_cap_exceeded")
                    h.update(ch);f.write(ch)
            note["bytes"]=size;note["sha256"]=h.hexdigest()
            if size<10000 or p.open("rb").read(4)!=b"glTF":
                note["invalid_glb_magic"]=True;p.unlink(missing_ok=True)
                accepted.append(note);continue
            accepted.append(note);out["model"]=note;break
        except Exception as ex:
            accepted.append({"url":url,"error":repr(ex)})
    out["download_attempts"]=accepted
    if out.get("model"):
        out["status"]="GENUINE_GLB_BYTES_ACQUIRED_NOT_ART_APPROVED"
        import trimesh
        model=ROOT/"museum_tyto_alba_CC0_CLAIM_REFERENCE_ONLY.glb"
        try:
            s=trimesh.load(str(model),force="scene",process=False)
            im=0
            for geom in s.geometry.values():
                mat=getattr(getattr(geom,"visual",None),"material",None)
                im+=sum(getattr(mat,a,None) is not None for a in ("baseColorTexture","normalTexture","metallicRoughnessTexture"))
            audit={"scene_geometries":len(s.geometry),"total_triangles":sum(len(g.faces) for g in s.geometry.values()),
                   "material_texture_slots":im,"bounds":s.bounds.tolist(),
                   "source_type":"genuine museum adult scan (NOT juvenile)", "webgl2":"NOT_TESTED",
                   "art":"NOT_ELIGIBLE_MISMATCHED_AGE_AND_TARGET_SPECIES","release":False}
            (ROOT/"native_mesh_qa.json").write_text(json.dumps(audit,indent=2))
            out["mesh_qa"]=audit
        except Exception as ex:
            out["mesh_parse_error"]=repr(ex)
    else:out["status"]="PUBLIC_DOWNLOAD_NOT_RETRIEVED"
except Exception as ex:
    out["status"]="FETCH_OR_PARSE_BLOCKED"
    out["error"]=repr(ex)
finally:
    record()
    (ROOT/"STRICT_NO_RELEASE.txt").write_text("Run312 | museum adult barn owl / source access research ONLY | art candidate: NO | release: NO | physical phone: NOT TESTED.\n")
    print(json.dumps(out,indent=2,ensure_ascii=False))
