#!/usr/bin/env python3
"""Run150: independently inspect publicly advertised zero-fee 3D owl sources.
Research ONLY. Never treats source adult owl / screenshots / glTF checks as accepted #172 chick.
The sole potential release gate is separate human visual review after genuine native four-angles.
No credentials, payments, API key, captcha bypass, or product path modifications.
"""
from __future__ import annotations
import os, sys, json, re, hashlib, traceback, pathlib, urllib.parse, time
OUT = pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops/research-evidence-run150-ARTIST-CC0-GROOM-SOURCE-NO_RELEASE")
OUT.mkdir(parents=True, exist_ok=True)
URLS = {
    "blendswap_owl_artist_feather_cc0": "https://blendswap.com/blend/7951",
    "innerscene_owl_claimed_cc0": "https://www.innerscene.com/tools/library/3d-parts/owl-d696472a",
    "cgtrader_juvenile_noai_listing_only": "https://www.cgtrader.com/free-3d-models/animal/bird/free-baby-owl-sculpt",
}
def dump(name, obj):
    (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2,default=str),encoding="utf-8")
def validate_glb(data: bytes, prefix: str):
    import struct
    if len(data)<20 or data[:4]!=b"glTF": return {"valid":False,"reason":"No glTF binary magic","bytes":len(data)}
    magic,version,length=struct.unpack_from("<4sII",data)
    valid=version==2 and length==len(data)
    record={"valid":valid,"version":version,"header_length":length,"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest()}
    if valid:
        path=OUT/f"{prefix}_UNAPPROVED_SOURCE_ONLY.glb"
        path.write_bytes(data)
        record["path"]=str(path)
    return record
def do_probe():
    import requests,bs4
    session=requests.Session()
    session.headers.update({"User-Agent":"Mozilla/5.0 Owl172-Research/1.0 (license-respecting, no-payment)"})
    logs={"scope":"#172 isolated research only","sources":{},"downloaded":[],"rights":"source-claimed CC0 is not independent distribution-rights verification",
          "no_ai_listing":"CGTrader specifically says Royalty Free License (no AI); listing inspection only, NO asset import/AI use"}
    for key,url in URLS.items():
        e={"url":url,"requests":{},"visible_download_candidates":[],"errors":[]}
        logs["sources"][key]=e
        try:
            r=session.get(url,timeout=30)
            e["requests"]={"status":r.status_code,"content_type":r.headers.get("Content-Type"),"bytes":len(r.content),"final_url":r.url,
              "sha256":hashlib.sha256(r.content).hexdigest()}
            (OUT/f"run150_{key}_http_excerpt.txt").write_text(r.text[:18000],encoding="utf-8",errors="replace")
            soup=bs4.BeautifulSoup(r.text,"html.parser")
            e["title"]=soup.title.get_text(" ",strip=True) if soup.title else None
            for a in soup.select("a[href]"):
                href=urllib.parse.urljoin(r.url,a.get("href"))
                label=a.get_text(" ",strip=True)[:120]
                if any(word in (label+" "+href).lower() for word in ["download","owl.glb",".blend","/file/"]):
                    e["visible_download_candidates"].append({"text":label,"href":href[:300]})
            e["visible_download_candidates"]=e["visible_download_candidates"][:25]
            # Only from the claimed CC0 Innerscene listing, never fetch a non-CC0/no-AI asset.
            if key=="innerscene_owl_claimed_cc0":
                for x in e["visible_download_candidates"]:
                    href=x["href"]
                    host=urllib.parse.urlsplit(href).hostname or ""
                    if ((host.endswith("innerscene.com") or host.endswith("innterscene.com")) and
                       (".glb" in href.lower() or "download" in href.lower()) and href.startswith("https://")):
                        try:
                            sr=session.get(href,timeout=90)
                            res=validate_glb(sr.content,"run150_innerscene")
                            res.update({"source_link":href,"http_status":sr.status_code,"content_type":sr.headers.get("Content-Type")})
                            e["direct_candidate"]=res
                            if res["valid"]:
                                logs["downloaded"].append(res)
                                break
                        except Exception as ex: e["errors"].append("candidate fetch "+str(ex))
        except Exception as ex: e["errors"].append(type(ex).__name__+": "+str(ex))
        dump("run150_source_probe_partial.json",logs)

    # Real browser navigation and clicking only publicly visible unauthenticated download UI.
    # Do not login, register, bypass protection, accept purchases, or use CGTrader noAI asset.
    try:
        from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout
        with sync_playwright() as p:
            browser=p.chromium.launch(headless=True,args=["--no-sandbox"])
            for key in ["blendswap_owl_artist_feather_cc0","innerscene_owl_claimed_cc0"]:
                url=URLS[key]
                rec=logs["sources"][key]; rec["browser"]={}
                page=browser.new_page(accept_downloads=True,viewport={"width":1280,"height":850})
                try:
                    response=page.goto(url,wait_until="domcontentloaded",timeout=45000)
                    page.wait_for_timeout(1700)
                    rec["browser"]["status"]=response.status if response else None
                    rec["browser"]["url"]=page.url
                    rec["browser"]["title"]=page.title()
                    rec["browser"]["body_excerpt"]=page.locator("body").inner_text(timeout=12000)[:3800]
                    page.screenshot(path=str(OUT/f"run150_{key}_ACTUAL_BROWSER.png"),full_page=False)
                    if any(x in page.url.lower() for x in ["login","signin","checkout","cart","challenge"]):
                        rec["browser"]["blocked"]="authentication/payment/verification route, no bypass"
                    else:
                        selectors=[
                           "a:has-text('Download GLB')","button:has-text('Download GLB')",
                           "a:has-text('Download')","button:has-text('Download')"
                        ]
                        for sel in selectors:
                            loc=page.locator(sel)
                            if loc.count()==0:continue
                            target=loc.first
                            try:
                                with page.expect_download(timeout=12000) as download_info:
                                    target.click(timeout=7000)
                                dl=download_info.value
                                fname=dl.suggested_filename
                                temp=OUT/("run150_browser_"+key+"_tmp")
                                dl.save_as(temp)
                                b=temp.read_bytes()
                                temp.unlink()
                                rec["browser"]["download_file_name"]=fname
                                rec["browser"]["download_bytes"]=len(b)
                                # GLB only. Blender ZIP would need explicit licence and security auditing.
                                out=validate_glb(b,"run150_"+key+"_browser")
                                rec["browser"]["glb"]=out
                                if out["valid"]:logs["downloaded"].append(out)
                                break
                            except PWTimeout:
                                rec["browser"]["download_click"]=f"{sel}: no download event (possibly login)"
                                page.screenshot(path=str(OUT/f"run150_{key}_AFTER_CLICK_BROWSER.png"),full_page=False)
                                break
                            except Exception as ex:
                                rec["browser"]["click_error"]=type(ex).__name__+": "+str(ex)
                                break
                        if any(x in page.url.lower() for x in ["login","signin","checkout","cart","challenge"]):
                            rec["browser"]["blocked"]="click led to login/payment/verification; no bypass"
                except Exception as ex:
                    rec["browser"]["error"]=type(ex).__name__+": "+str(ex)
                finally:
                    page.close()
                dump("run150_source_probe_partial.json",logs)
            browser.close()
    except Exception as ex:
        logs["browser_setup_error"]=type(ex).__name__+": "+str(ex)
    dump("run150_actual_source_probe.json",logs)
    (OUT/"NO_RELEASE.flag").write_text(
        "ART_UNREVIEWED / NO_RELEASE. Sources are NOT the rightmost #172 juvenile. No aesthetic acceptance; no product deployment, no phone GPU claims, no paid API.\n")
    print(json.dumps({"download_count":len(logs["downloaded"]),
        "sources":{k:{"http":v.get("requests",{}).get("status"),"browser":v.get("browser",{}).get("status"),"download":v.get("direct_candidate",{}).get("valid")} for k,v in logs["sources"].items()}},indent=2))

def do_render():
    import bpy, math, mathutils, struct
    from mathutils import Vector
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    candidates=list(OUT.glob("run150_*UNAPPROVED_SOURCE_ONLY.glb"))
    if not candidates:
        (OUT/"run150_blender_NOT_RUN_no_valid_glb.txt").write_text("No real GLB from openly accessible source; do not invent four-view renders.")
        return
    path=candidates[0]
    bpy.ops.import_scene.gltf(filepath=str(path.resolve()))
    meshes=[x for x in bpy.context.scene.objects if x.type=='MESH']
    if not meshes:
        (OUT/"run150_blender_NOT_RUN_no_mesh.txt").write_text("No actual mesh data despite glTF header.")
        return
    pts=[obj.matrix_world @ Vector(v) for obj in meshes for v in obj.bound_box]
    low=Vector(tuple(min(v[i] for v in pts) for i in range(3)))
    hi=Vector(tuple(max(v[i] for v in pts) for i in range(3)))
    center=(low+hi)*0.5
    dims=hi-low; radius=max(dims)*1.3
    scene=bpy.context.scene
    scene.render.engine='CYCLES'
    scene.cycles.samples=12
    scene.render.resolution_x=448
    scene.render.resolution_y=448
    scene.render.resolution_percentage=100
    scene.render.image_settings.file_format='PNG'
    scene.world.color=(0.75,0.75,0.75)
    bpy.ops.object.camera_add()
    cam=bpy.context.object
    scene.camera=cam
    cam.data.type='ORTHO'
    cam.data.ortho_scale=radius*2.35
    def look_at(obj,point):
        direction=point-obj.location
        obj.rotation_euler=direction.to_track_quat('-Z','Y').to_euler()
    lamps=[]
    for pos,power,scale in [((1,-2,4),320,3),((-3,1,3),260,4)]:
        bpy.ops.object.light_add(type='AREA',location=center+Vector(pos)*radius)
        light=bpy.context.object;light.data.energy=power;light.data.shape='DISK';light.data.size=radius*scale
        look_at(light,center)
        lamps.append(light)
    records=[]
    # Camera world-azimuth rather than unverified anatomical front/back.
    for degrees in [0,45,90,180]:
        rad=math.radians(degrees)
        cam.location=center+Vector((math.sin(rad)*radius*2.1,-math.cos(rad)*radius*2.1,radius*0.45))
        look_at(cam,center)
        dest=OUT/f"run150_native_azimuth_{degrees:03d}_UNREVIEWED.png"
        scene.render.filepath=str(dest.resolve())
        bpy.ops.render.render(write_still=True)
        records.append({"azimuth_degrees":degrees,"file":str(dest),"sha256":hashlib.sha256(dest.read_bytes()).hexdigest()})
    dump("run150_real_blender_four_azimuths.json",
         {"source":str(path),"meshes":len(meshes),"triangles":sum(len(p.vertices)-2 for m in meshes for p in m.data.polygons),
          "bounding_box":[list(low),list(hi)],"camera_not_anatomical":True,"renders":records,
          "acceptance":"UNREVIEWED / NO_RELEASE; donor could be adult/wrong species; art human review mandatory"})
    print("GENUINE_NATIVE_RENDERED",len(records))

if __name__=="__main__":
    if len(sys.argv)>1 and sys.argv[-1]=="render":do_render()
    else:do_probe()
