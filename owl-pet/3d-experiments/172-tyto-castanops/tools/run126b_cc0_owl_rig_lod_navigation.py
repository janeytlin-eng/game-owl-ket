#!/usr/bin/env python3
"""Run126B: real zero-dollar official itch.io CC0 sample flow / actual GLB geometry check.
No paid tier, no login circumvent, no fake success. Asset is a toy anatomy donor ONLY.
"""
import datetime as dt, hashlib, json, pathlib, re, struct, sys, zipfile
from playwright.sync_api import sync_playwright, TimeoutError as BrowserTimeout
ROOT=pathlib.Path(sys.argv[1]); ROOT.mkdir(parents=True, exist_ok=True)
SOURCE="https://vuena.itch.io/blocky-pets-free"
PURCHASE=SOURCE+"/purchase"
EXPECTED="Cute-Pets-Wildlife-FREE-Sample-CC0-v3.1.zip"
log={"run":"126B","date_utc":dt.datetime.now(dt.timezone.utc).isoformat(),"source":SOURCE,
     "download_page":PURCHASE,"expected_free_archive":EXPECTED,
     "target":"#172 Tyto castanops v3 RIGHTMOST age-unknown mesoptile",
     "purpose":"inspect real CC0 rig+mobile LOD as engineering donor, NEVER art approval",
     "purchase_authorized":False,"amount_spent_usd":0,"no_auth_bypass":True,
     "status":"NO_MODEL","art_gate":"NOT_ASSESSED_NO_RELEASE","events":[]}
def emit(stage,**kw):
    record={"stage":stage,**kw}; log["events"].append(record)
    print(json.dumps(record,ensure_ascii=False),flush=True)
def sha(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for chunk in iter(lambda:f.read(262144),b""):h.update(chunk)
    return h.hexdigest()
def inspect_glb(path):
    b=path.read_bytes()
    d={"file":path.name,"bytes":len(b),"sha256":sha(path),"magic":b[:4].decode("latin-1","replace")}
    if len(b)<20 or b[:4]!=b"glTF":
        d["error"]="not a glTF binary";return d
    magic,version,total=struct.unpack_from("<4sII",b,0)
    d.update(version=version,declared_bytes=total)
    if version!=2 or total!=len(b):d["error"]="invalid GLB byte length/version";return d
    jlen,jtype=struct.unpack_from("<I4s",b,12)
    if jtype!=b"JSON" or jlen>len(b)-20:d["error"]="missing or invalid GLB JSON chunk";return d
    obj=json.loads(b[20:20+jlen].decode())
    meshes=obj.get("meshes",[]);nodes=obj.get("nodes",[])
    a=obj.get("accessors",[])
    tri=0;prims=0
    for mesh in meshes:
        for prim in mesh.get("primitives",[]):
            prims+=1
            ac=prim.get("indices")
            n=a[ac].get("count",0) if isinstance(ac,int) and ac<len(a) else 0
            if prim.get("mode",4)==4:tri+=n//3
    d.update(mesh_count=len(meshes),mesh_primitives=prims,nodes=len(nodes),
             triangles_indexed=tri,skins=len(obj.get("skins",[])),
             animations=len(obj.get("animations",[])),
             clips=[z.get("name","") for z in obj.get("animations",[])],
             materials=len(obj.get("materials",[])),
             image_count=len(obj.get("images",[])),
             node_names=[z.get("name","") for z in nodes[:120]],
             mesh_names=[z.get("name","") for z in meshes[:120]],
             model_source="artist-created downloadable GLB; CC0 as stated on official itch page",
             art_status="NOT_ASSESSED; child likeness and real phone GPU NOT verified")
    return d
try:
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True, args=["--no-sandbox"])
        context=browser.new_context(accept_downloads=True,viewport={"width":1000,"height":760})
        network=[]
        context.on("response",lambda response: network.append({"status":response.status,"url":response.url[:260]}) if len(network)<60 and any(x in response.url for x in ("itch.io","itch.zone")) else None)
        page=context.new_page()
        try:
            resp=page.goto(SOURCE,wait_until="domcontentloaded",timeout=35000)
            emit("listing",http_status=resp.status if resp else None,title=page.title(),url=page.url,
                 has_CC0=bool(re.search("CC0",page.locator("body").inner_text()[:25000])),
                 has_free_zip=EXPECTED in page.locator("body").inner_text()[:25000])
            page.screenshot(path=str(ROOT/"run126b_listing.png"),full_page=False)
            response=page.goto(PURCHASE,wait_until="domcontentloaded",timeout=35000)
            emit("official_purchase_page",status=response.status if response else None,url=page.url,
                 text_excerpt=page.locator("body").inner_text()[:1500])
            page.screenshot(path=str(ROOT/"run126b_official_free_purchase_page.png"))
            # Only click the site's own $0 "No thanks" route; no Pay/checkout.
            free=page.get_by_text("No thanks, just take me to the downloads",exact=False)
            if free.count()==0:
                free=page.locator("a[href*='/download']").first
            if free.count()==0:emit("blocked",reason="official zero-dollar route not exposed")
            else:
                href=free.first.get_attribute("href")
                emit("official_free_route",element=free.first.evaluate("(e)=>e.tagName"),href=href,outer_html=free.first.evaluate("(e)=>e.outerHTML")[:650])
                free.first.click(timeout=15000)
                page.wait_for_timeout(4500)
                try:
                    page.wait_for_url(lambda url: "/purchase" not in url,timeout=17000)
                except BrowserTimeout:
                    emit("free_route_navigation_timeout",url=page.url)
                emit("network_after_click",responses=network[-35:],
                     frames=[f.url for f in page.frames],tabs=[pg.url for pg in context.pages])
                if len(context.pages)>1:
                    page=context.pages[-1]
                    page.wait_for_load_state("domcontentloaded",timeout=20000)
                emit("download_listing",url=page.url,text_excerpt=page.locator("body").inner_text()[:3500])
                page.screenshot(path=str(ROOT/"run126b_official_download_listing.png"))
                # Only accept exact official free filename. Never download paid STARTER pack.
                links=page.locator("a")
                matches=[]
                for i in range(min(links.count(),250)):
                    e=links.nth(i); txt=(e.inner_text() or "")[:120]
                    href=e.get_attribute("href")
                    if href and (EXPECTED in txt or ("download" in txt.lower() and "STARTER" not in txt.upper()) or "download" in (href or "").lower()):
                        matches.append((i,txt,href))
                emit("download_buttons",matched=matches[:20],visible_links=links.count(),body_tail=page.locator("body").inner_text()[-2200:])
                clicked=False
                for i,txt,href in matches:
                    if "STARTER" in txt.upper() or "starter" in href.lower():continue
                    try:
                        with page.expect_download(timeout=25000) as info:links.nth(i).click(timeout=12000)
                        dl=info.value
                        emit("download_event",suggested_filename=dl.suggested_filename,url=dl.url[:300])
                        if EXPECTED.lower() not in dl.suggested_filename.lower():
                            emit("rejected_download",reason="unexpected filename; avoid paid pack");break
                        dest=ROOT/EXPECTED;dl.save_as(str(dest))
                        emit("actual_zip_saved",bytes=dest.stat().st_size,sha256=sha(dest))
                        clicked=True
                        if not zipfile.is_zipfile(dest):
                            emit("not_zip",reason="download payload was not a valid ZIP");break
                        with zipfile.ZipFile(dest) as z:
                            entries=[{"name":x.filename,"bytes":x.file_size} for x in z.infolist()]
                            emit("zip_entries",entries=entries[:100],total=len(entries))
                            birds=[x for x in z.infolist() if x.filename.lower().endswith(".glb") and "owl" in x.filename.lower() and x.file_size<25000000]
                            for num,x in enumerate(birds[:5]):
                                glbpath=ROOT/("source_cc0_owl_"+str(num)+".glb")
                                glbpath.write_bytes(z.read(x))
                                info=inspect_glb(glbpath)
                                (ROOT/("run126b_glb_inspection_"+str(num)+".json")).write_text(json.dumps(info,ensure_ascii=False,indent=2)+"\n")
                                emit("true_glb_inspected",**{k:info.get(k) for k in ("bytes","sha256","triangles_indexed","skins","animations","mesh_count","error")})
                                log["status"]="OBTAINED_CC0_GLTF_UNREVIEWED"
                        break
                    except Exception as exc:
                        emit("download_failed",error=type(exc).__name__+": "+str(exc)[:400])
                if not clicked:
                    emit("blocked",reason="no approved free ZIP downloaded via exact official link")
        except Exception as exc:
            emit("exception",type=type(exc).__name__,message=str(exc)[:500],url=page.url)
        finally:
            browser.close()
except Exception as exc:
    emit("browser_setup_failure",type=type(exc).__name__,message=str(exc)[:500])
finally:
    # This source is designer-toy / NOT an anatomically credible Tyto mesoptile.
    log["art_gate"]="UNAPPROVED_TOY_DONOR_NO_RELEASE" if log["status"].startswith("OBTAINED_") else "NO_GEOMETRY_NO_RELEASE"
    (ROOT/"run126b_actual_source_and_glb_status.json").write_text(json.dumps(log,ensure_ascii=False,indent=2)+"\n")
    (ROOT/"NO_RELEASE.flag").write_text(log["art_gate"]+
         " — source-only rig reference, not #172 Tyto castanops rightmost chick. No preview release.\n")
    print("FINAL",log["status"],log["art_gate"],flush=True)
