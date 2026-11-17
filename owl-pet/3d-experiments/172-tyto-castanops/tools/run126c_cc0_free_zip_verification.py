#!/usr/bin/env python3
"""Run126C: real zero-dollar official itch.io CC0 sample flow / actual GLB geometry check.
No paid tier, no login circumvent, no fake success. Asset is a toy anatomy donor ONLY.
"""
import datetime as dt, hashlib, json, pathlib, re, struct, sys, zipfile
from playwright.sync_api import sync_playwright, TimeoutError as BrowserTimeout
ROOT=pathlib.Path(sys.argv[1]); ROOT.mkdir(parents=True, exist_ok=True)
SOURCE="https://vuena.itch.io/blocky-pets-free"
PURCHASE=SOURCE+"/purchase"
EXPECTED="Cute-Pets-Wildlife-FREE-Sample-CC0-v3.1.zip"
log={"run":"126C","date_utc":dt.datetime.now(dt.timezone.utc).isoformat(),"source":SOURCE,
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
            page.screenshot(path=str(ROOT/"run126c_listing.png"),full_page=False)
            response=page.goto(PURCHASE,wait_until="domcontentloaded",timeout=35000)
            emit("official_purchase_page",status=response.status if response else None,url=page.url,
                 text_excerpt=page.locator("body").inner_text()[:1500])
            page.screenshot(path=str(ROOT/"run126c_official_free_purchase_page.png"))
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
                page.screenshot(path=str(ROOT/"run126c_official_download_listing.png"))
                # The official listed FREE asset is a file row: inspect its DOM before clicking.
                # Do not use guessed URLs or download any paid STARTER file.
                rows=page.locator("[id^='game_download_']")
                emit("official_file_dom",rows=rows.count(),html=[rows.nth(i).evaluate("(e)=>e.outerHTML")[:2200] for i in range(min(3,rows.count()))])
                anchors=page.locator("a")
                candidates=[]
                for i in range(min(anchors.count(),200)):
                    e=anchors.nth(i)
                    if (e.inner_text() or "").strip()=="Download":
                        candidates.append(i)
                emit("official_download_buttons",indices=candidates)
                saved=[]
                for i in candidates[:3]:
                    e=anchors.nth(i)
                    try:
                        with page.expect_download(timeout=22000) as info:
                            e.click(timeout=9000)
                        dl=info.value
                        actual=dl.suggested_filename
                        emit("actual_download_event",name=actual,source_url_host=dl.url.split("/")[2] if dl.url.startswith("https://") else "unknown")
                        # Whitelist creator's FREE filename family, reject any paid pack or other title.
                        if not actual.startswith("Cute-Pets-Wildlife-FREE-Sample-CC0-v3.1") or "STARTER" in actual.upper() or not actual.endswith(".zip"):
                            emit("rejected_download",why="filename not in official CC0 free asset family",name=actual)
                            continue
                        dest=ROOT/actual
                        dl.save_as(str(dest))
                        meta={"name":actual,"size":dest.stat().st_size,"sha256":sha(dest),"is_zip":zipfile.is_zipfile(dest)}
                        saved.append(meta)
                        emit("actual_free_zip_saved",**meta)
                        if not meta["is_zip"]:continue
                        with zipfile.ZipFile(dest) as z:
                            records=[{"name":x.filename,"size":x.file_size} for x in z.infolist()]
                            emit("real_zip_entries",count=len(records),files=records[:120])
                            (ROOT/("entries_"+actual+".json")).write_text(json.dumps(records,ensure_ascii=False,indent=2)+"\n")
                            birds=[x for x in z.infolist() if x.filename.lower().endswith(".glb") and "owl" in x.filename.lower() and x.file_size<25000000]
                            if not birds and actual==EXPECTED:
                                emit("missing_owl_glb",why="main FREE zip has no named owl glb",glb_names=[x.filename for x in z.infolist() if x.filename.lower().endswith(".glb")][:30])
                            for num,x in enumerate(birds[:5]):
                                gp=ROOT/("source_cc0_owl_"+str(num)+".glb")
                                gp.write_bytes(z.read(x))
                                detail=inspect_glb(gp)
                                (ROOT/("run126c_glb_inspection_"+str(num)+".json")).write_text(json.dumps(detail,ensure_ascii=False,indent=2)+"\n")
                                emit("true_glb_inspected",**{k:detail.get(k) for k in ("bytes","sha256","triangles_indexed","skins","animations","mesh_count","error")})
                                log["status"]="OBTAINED_CC0_GLTF_UNREVIEWED"
                        # Do not place source third-party ZIP in public GitHub; metrics + extracted owl GLB (CC0) retained only.
                        dest.unlink(missing_ok=True)
                        if log["status"]=="NO_MODEL":
                            log["status"]="FREE_DOWNLOAD_NO_OWL_GLTF"
                    except Exception as exc:
                        emit("download_error",type=type(exc).__name__,message=str(exc)[:420])
                log["free_zip_metadata"]=saved
                if not saved:
                    emit("blocked",reason="the official file download produced no recognized free ZIP")

        except Exception as exc:
            emit("exception",type=type(exc).__name__,message=str(exc)[:500],url=page.url)
        finally:
            browser.close()
except Exception as exc:
    emit("browser_setup_failure",type=type(exc).__name__,message=str(exc)[:500])
finally:
    # This source is designer-toy / NOT an anatomically credible Tyto mesoptile.
    log["art_gate"]="UNAPPROVED_TOY_DONOR_NO_RELEASE" if log["status"].startswith("OBTAINED_") else "NO_GEOMETRY_NO_RELEASE"
    (ROOT/"run126c_actual_source_and_glb_status.json").write_text(json.dumps(log,ensure_ascii=False,indent=2)+"\n")
    (ROOT/"NO_RELEASE.flag").write_text(log["art_gate"]+
         " — source-only rig reference, not #172 Tyto castanops rightmost chick. No preview release.\n")
    print("FINAL",log["status"],log["art_gate"],flush=True)
