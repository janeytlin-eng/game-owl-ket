#!/usr/bin/env python3
"""#172 RUN257C: genuinely execute two independent NO-COST text-to-3D routes.
One zero-fee provider retry days after Run143; text-anatomy control only, NOT reference-faithful art.
No provider paid API, login, wallet, CAPTCHA bypass, or publishing.
"""
from __future__ import annotations
import sys, os, json, time, re, pathlib, traceback, hashlib, struct, urllib.parse, shutil, math
R=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
O=R/"research-evidence-run257c-FREE-TEXT-3D-CHICK-STRICT-NO_RELEASE"
O.mkdir(parents=True,exist_ok=True)
PROMPT=("One realistic juvenile masked barn owl chick, compact crouching baby with thick airy cream-white "
"second-down fluff over the entire rounded body. Broad soft integrated heart-shaped facial disc "
"with subtle warm-buff rim, two clearly OPEN round dark brown-black eyes and tiny pale curved bill. "
"Very short juvenile wings entirely hidden in dense down, tail entirely hidden, no ear tufts, "
"no layered long flight feathers, feet tucked close and weight resting low. Three-quarter front "
"view, faithful natural owl anatomy, detailed physically soft feathers, plain studio background, "
"one bird only, not a wooden toy or figurine.")
def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def dump(name, obj):
    (O/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2,default=str)+"\n", encoding="utf-8")
def glb_info(p):
    b=pathlib.Path(p).read_bytes()
    assert len(b)>10000 and b[:4]==b"glTF","Not a real binary GLB"
    assert struct.unpack_from("<I",b,8)[0]==len(b),"Invalid GLB length"
    n,typ=struct.unpack_from("<I4s",b,12)
    assert typ==b"JSON" and n<len(b)-20
    j=json.loads(b[20:20+n].decode("utf-8").rstrip(" \t\r\n\x00"))
    tris=0
    for mesh in j.get("meshes",[]):
        for prim in mesh.get("primitives",[]):
            if prim.get("mode",4)!=4:continue
            a=j["accessors"]
            tris+=(a[prim["indices"]]["count"] if "indices" in prim else a[prim["attributes"]["POSITION"]]["count"])//3
    return dict(bytes=len(b),sha256=sha(p),triangles=tris,meshes=len(j.get("meshes",[])),
      materials=len(j.get("materials",[])),textures=len(j.get("textures",[])),
      images=len(j.get("images",[])),animations=len(j.get("animations",[])),valid_glb_header=True)
def accept_binary(path,payload):
    path.write_bytes(payload)
    inf=glb_info(path)
    assert 1000<inf["triangles"]<1500000,"Geometry absent or unreasonable"
    return inf
def three_ws():
    import requests
    t=time.time()
    out={"source":"https://three.ws/3d","fee":"free draft only, no key or payment","prompt":PROMPT,
         "provider":"three.ws keyless free draft; do not use paid tier", "requests":[], "status":"STARTED"}
    dump("run257c_three_ws_status.json",out)
    try:
        url="https://three.ws/api/3d/generate"
        resp=requests.post(url,json={"prompt":PROMPT},timeout=105,headers={"content-type":"application/json","user-agent":"owl172 research noncommercial no-pay QA"})
        out["requests"].append(dict(url=url,status_code=resp.status_code,content_type=resp.headers.get("content-type"),
                 body=resp.text[:4500],duration=round(time.time()-t,2)))
        (O/"run257c_three_ws_initial_response.txt").write_text(resp.text[:30000])
        if resp.status_code in (402,403,429):
            out["status"]="PAYMENT_ACCESS_OR_QUOTA_BLOCK_NO_BYPASS";return out
        if not resp.ok:
            out["status"]="FREE_API_REJECTED";return out
        data=resp.json()
        for attempt in range(22):
            if isinstance(data,dict) and (data.get("glbUrl") or data.get("modelUrl")):break
            if isinstance(data,dict) and data.get("status") in ("failed","error"):break
            poll=data.get("poll") if isinstance(data,dict) else None
            job=data.get("job") if isinstance(data,dict) else None
            if not poll and job: poll="/api/3d/generate?job="+urllib.parse.quote(str(job),safe="")
            if not poll:
                out["status"]="NO_POLL_OR_DOWNLOAD_URL";break
            if poll.startswith("/"):poll="https://three.ws"+poll
            host=urllib.parse.urlsplit(poll).hostname
            if host!="three.ws":out["status"]="UNEXPECTED_POLL_HOST";break
            time.sleep(8)
            rp=requests.get(poll,timeout=60)
            out["requests"].append(dict(url=poll[:280],status_code=rp.status_code,
                                     body=rp.text[:1200],attempt=attempt))
            if rp.status_code in (402,403,429):
                out["status"]="FREE_QUOTA_OR_ACCESS_BLOCK";break
            if not rp.ok:
                out["status"]="POLL_HTTP_ERROR";break
            data=rp.json()
        dump("run257c_three_ws_full_request_record.json",out)
        glburl=(data.get("glbUrl") or data.get("modelUrl")) if isinstance(data,dict) else None
        if glburl and isinstance(glburl,str):
            parsed=urllib.parse.urlsplit(glburl)
            if parsed.scheme!="https" or not parsed.netloc:raise ValueError("Reject non-HTTPS model download URL")
            rr=requests.get(glburl,timeout=120)
            out["download_status"]=rr.status_code
            out["download_bytes"]=len(rr.content)
            if rr.ok:
                inf=accept_binary(O/"run257c_three_ws_unapproved.glb",rr.content)
                out["model"]=inf;out["status"]="REAL_GLTF_QUARANTINED_FOR_FOUR_VIEW"
            else:out["status"]="DOWNLOAD_FAIL"
        else:
            if out.get("status")=="STARTED": out["status"]="NO_MODEL_RETURNED"
    except Exception:
        out["status"]="ACTUAL_FREE_ENDPOINT_EXCEPTION"
        out["error"]=traceback.format_exc()[-3500:]
    finally:
        out["end_utc"]=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())
        dump("run257c_three_ws_status.json",out)
    return out

def three_d_valley():
    from playwright.sync_api import sync_playwright
    out={"source":"https://3dvalley.com/tools/create/text-to-3d","fee":"public no-signup free daily only",
         "prompt":PROMPT,"status":"STARTED", "captures":[],"responses":[],"generate_clicked":False}
    dump("run257c_valley_status.json",out)
    with sync_playwright() as pw:
        b=pw.chromium.launch(headless=True,args=["--use-gl=angle","--use-angle=swiftshader"])
        ctx=b.new_context(viewport={"width":1400,"height":900},accept_downloads=True,locale="en-US")
        page=ctx.new_page()
        collection=[]
        def on_response(resp):
            try:
                ct=resp.headers.get("content-type","").lower()
                if not (".glb" in resp.url.lower() or "model/gltf-binary" in ct or "application/octet-stream" in ct):return
                row=dict(url=resp.url[:350],status=resp.status,content_type=ct[:80]);out["responses"].append(row)
                if resp.status!=200:return
                body=resp.body()
                if 10000<len(body)<100_000_000 and body[:4]==b"glTF":
                    p=O/"run257c_valley_captured_unapproved.glb"
                    p.write_bytes(body);collection.append(p)
            except Exception as e:out.setdefault("network_errors",[]).append(str(e)[:250])
        page.on("response",on_response)
        try:
            page.goto(out["source"],wait_until="domcontentloaded",timeout=55000)
            page.wait_for_timeout(3500)
            page.screenshot(path=str(O/"run257c_valley_initial.png"))
            out["captures"].append("run257c_valley_initial.png")
            visible=page.locator("body").inner_text(timeout=18000)
            (O/"run257c_valley_initial_visible.txt").write_text(visible[:14000])
            if re.search(r"daily limit|out of credits|GPU.*busy|generation paused|limit reached",visible,re.I):
                out["status"]="PUBLIC_FREE_QUOTA_OR_AVAILABILITY_BLOCK";return out
            # Text-to-3D has one single-object description input; never click a paid checkout.
            fields=[]
            for sel in ("textarea","input[type=text]","input:not([type])"):
                fields.extend(page.locator(sel).all())
            out["visible_text_fields"]=[dict(tag=f.evaluate("(e)=>e.tagName"),
               placeholder=f.get_attribute("placeholder"),visible=f.is_visible()) for f in fields]
            field=next((f for f in fields if f.is_visible()),None)
            if field is None:out["status"]="NO_VISIBLE_TEXT_INPUT";return out
            field.fill(PROMPT,timeout=13000)
            page.wait_for_timeout(700)
            (O/"run257c_valley_post_prompt_visible.txt").write_text(page.locator("body").inner_text()[:14000])
            btn=page.get_by_role("button",name="Generate model",exact=False)
            if not btn.count():btn=page.get_by_role("button",name=re.compile("generate|create|make",re.I))
            if not btn.count() or not btn.first.is_enabled():
                out["status"]="NO_FREE_GENERATE_BUTTON";return out
            out["generate_clicked"]=True
            btn.first.click(timeout=12000)
            started=time.monotonic()
            while time.monotonic()-started<230 and not collection:
                page.wait_for_timeout(6000)
                body=page.locator("body").inner_text(timeout=10000)
                if re.search(r"daily limit|out of credits|free quota|try again tomorrow",body,re.I):
                    out["status"]="FREE_DAILY_QUOTA_EXHAUSTED";break
                # A model may be available behind an explicit GLB download button.
                for sel in [page.get_by_role("button",name=re.compile("download.*glb",re.I)),
                            page.get_by_role("link",name=re.compile("download.*glb",re.I))]:
                    if sel.count() and sel.first.is_visible():
                        try:
                            with page.expect_download(timeout=8000) as di:sel.first.click(timeout=6000)
                            d=di.value
                            p=O/"run257c_valley_download_unapproved.glb";d.save_as(str(p))
                            collection.append(p)
                        except Exception as e:
                            out["download_click_error"]=str(e)[:350]
                        break
            out["elapsed_after_generation"]=round(time.monotonic()-started,2)
            for p in collection:
                try:
                    inf=glb_info(p)
                    out.setdefault("candidates",[]).append(inf)
                    if inf["triangles"]>1000 and not (O/"run257c_valley_unapproved.glb").exists():
                        shutil.copyfile(p,O/"run257c_valley_unapproved.glb")
                        out["status"]="REAL_GLTF_QUARANTINED_FOR_FOUR_VIEW"
                except Exception as e:out.setdefault("invalid",[]).append(str(e)[:500])
            if out["status"]=="STARTED":out["status"]="NO_VALID_GLTF_AFTER_PUBLIC_GENERATION"
        except Exception:
            out["status"]="ACTUAL_PUBLIC_BROWSER_EXCEPTION"
            out["error"]=traceback.format_exc()[-4000:]
        finally:
            try:
                page.screenshot(path=str(O/"run257c_valley_final.png"),timeout=25000,full_page=True)
                out["captures"].append("run257c_valley_final.png")
                (O/"run257c_valley_final_visible.txt").write_text(page.locator("body").inner_text()[:14000])
            except Exception as e:out["final_capture_err"]=str(e)[:200]
            dump("run257c_valley_status.json",out)
            b.close()
    return out

def render():
    import bpy
    from mathutils import Vector
    results=[]
    for name in ("three_ws","valley"):
        p=O/("run257c_"+name+"_unapproved.glb")
        if not p.is_file():continue
        try:
            bpy.ops.wm.read_factory_settings(use_empty=True)
            bpy.ops.import_scene.gltf(filepath=str(p))
            meshes=[ob for ob in bpy.context.scene.objects if ob.type=="MESH"]
            assert meshes
            pts=[ob.matrix_world@Vector(v) for ob in meshes for v in ob.bound_box]
            lo=Vector(tuple(min(x[i] for x in pts) for i in range(3)))
            hi=Vector(tuple(max(x[i] for x in pts) for i in range(3)))
            cen=(lo+hi)*.5;scale=max(hi-lo)
            assert scale>0
            sc=bpy.context.scene
            if sc.world is None:sc.world=bpy.data.worlds.new("run257c studio")
            sc.world.color=(.55,.55,.55)
            sc.render.engine="CYCLES";sc.cycles.samples=12
            sc.view_layers[0].cycles.use_denoising=False
            sc.render.resolution_x=sc.render.resolution_y=500
            sc.render.resolution_percentage=100
            for offset,power in (((-3,-3,4),400),((3,2,2),230)):
                lamp=bpy.data.lights.new("run257c area","AREA");lamp.energy=power;lamp.size=scale*3
                ob=bpy.data.objects.new("run257c area",lamp);sc.collection.objects.link(ob)
                ob.location=cen+Vector(offset)*scale
                ob.rotation_euler=(cen-ob.location).to_track_quat("-Z","Y").to_euler()
            camera=bpy.data.objects.new("run257c camera",bpy.data.cameras.new("run257c camera"))
            sc.collection.objects.link(camera);sc.camera=camera
            camera.data.type="ORTHO";camera.data.ortho_scale=scale*1.65
            views=[]
            for v,angle in (("front",0),("quarter",45),("side",90),("back",180)):
                ang=math.radians(angle)
                camera.location=cen+Vector((4*math.sin(ang),-4*math.cos(ang),1.1))*scale
                camera.rotation_euler=(cen-camera.location).to_track_quat("-Z","Y").to_euler()
                filename=O/("run257c_"+name+"_"+v+"_NATIVE_UNAPPROVED.png")
                sc.render.filepath=str(filename)
                bpy.ops.render.render(write_still=True)
                views.append(filename)
            metrics={"source":name,"mesh_count":len(meshes),
                     "triangles":sum(len(m.data.polygons) for m in meshes),
                     "bbox":list(hi-lo),"four_actual_blender_views":len(views),
                     "blender":bpy.app.version_string, "art_review":"PENDING_HUMAN_ACTUAL_IMAGE_INSPECTION",
                     "real_phone_webgl":"NOT_TESTED","product_release":False}
            dump("run257c_"+name+"_native_metrics.json",metrics)
            try:
                from PIL import Image,ImageDraw
                contact=Image.new("RGB",(1000,1000),(238,238,238))
                draw=ImageDraw.Draw(contact)
                for i,shot in enumerate(views):
                    tile=Image.open(shot).convert("RGB").resize((500,500))
                    x,y=i%2*500,i//2*500
                    contact.paste(tile,(x,y))
                    draw.text((x+18,y+16),("front","quarter","side","back")[i],fill=(0,0,0))
                contact.save(O/("run257c_"+name+"_four_native_views_NO_RELEASE.jpg"),quality=89)
            except Exception as e:metrics["contact_sheet_error"]=str(e)
            results.append(metrics)
        except Exception:
            results.append({"source":name,"failure":traceback.format_exc()[-4000:],
                            "render_pass":False,"product_release":False})
    dump("run257c_render_results.json",results)
    return results

if __name__=="__main__":
    mode=sys.argv[-1]
    if mode=="probe":
        print("three.ws",json.dumps(three_ws(),ensure_ascii=False))
        print("3dvalley","SKIPPED_TO_AVOID_REPEATING_PRIOR_DAILY_QUOTA_AND_BROWSER_PROBE")
    elif mode=="render":print("blender",render())
    else:raise SystemExit("Call with probe or render")
