#!/usr/bin/env python3
"""Run139 genuine alternative free public-browser image-to-3D attempt for #172.
No auth/captcha bypass, paid calls, inferred output, automatic art approval, or
publication of provider output. Original source crop pinned by SHA256.
"""
import sys,os,json,hashlib,pathlib,shutil,traceback,struct,time,math,re
R=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
SRC=R/"research-evidence-run117-FREE-TRELLIS-QUOTA-RECHECK-ART_REJECTED/rightmost_baby_owl_512_rgba.png"
O=R/"research-evidence-run139-ALTERNATE-PUBLIC-NO_RELEASE"
O.mkdir(parents=True,exist_ok=True)
PIN="e439928a9ef08d3be266106cb5f2766b6f5a9f2c414d44e8da55ba81732153b8"
REJECTED={
 "c11c94db20065c6c6f252e768e8c748f22dc69ef9b4e7199110b96de0625c12e",
 "339a2eafd291fe1c2352d93d0755ca10a1c34d0b83b560a91cdca73053db3685",
 "b65fe7ca77aee54806792f473f15282000a5adc1f3798283a83c1b9bc928630d",
}
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def save(name,obj):(O/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2,default=str)+"\n")
def gltf_info(p):
    b=pathlib.Path(p).read_bytes()
    if len(b)<1024 or b[:4]!=b"glTF":raise ValueError("Not valid binary GLB magic/size")
    if struct.unpack_from("<I",b,8)[0]!=len(b):raise ValueError("GLB reported total length mismatch")
    n,ty=struct.unpack_from("<I4s",b,12)
    if ty!=b"JSON" or n>len(b)-20:raise ValueError("Missing GLB JSON chunk")
    d=json.loads(b[20:20+n].decode("utf8").strip(" \t\r\n\x00"))
    triangles=0
    for m in d.get("meshes",[]):
      for prim in m.get("primitives",[]):
        mode=prim.get("mode",4)
        if mode!=4:continue
        if "indices" in prim:count=d["accessors"][prim["indices"]]["count"]
        else:count=d["accessors"][prim["attributes"]["POSITION"]]["count"]
        triangles+=count//3
    return dict(bytes=len(b),sha256=sha(p),triangles=triangles,meshes=len(d.get("meshes",[])),
      nodes=len(d.get("nodes",[])),images=len(d.get("images",[])),textures=len(d.get("textures",[])),
      materials=len(d.get("materials",[])),animations=len(d.get("animations",[])),
      known_rejected_sha=sha(p) in REJECTED,glb_header_valid=True)

PROVIDERS=[
 dict(name="3dvalley",url="https://3dvalley.com/tools/create/image-to-3d",
      buttons=["Make 3D model","Generate 3D","Generate model","Generate","Create 3D"]),
]

def browse():
    from PIL import Image
    from playwright.sync_api import sync_playwright
    assert SRC.is_file() and sha(SRC)==PIN,"Do not submit wrong or altered reference image"
    im=Image.open(SRC)
    assert im.size==(512,512) and im.mode=="RGBA","Expected original rightmost owl matte"
    shutil.copyfile(SRC,O/"run139_pinned_rightmost_juvenile_RGBA.png")
    state=dict(run=139,source=str(SRC),source_sha256=PIN,source_actual_dims=list(im.size),
      species="Tyto castanops v3, rightmost age-unknown cream mesoptile",
      prior_run137="real 20k triangle grey untextured GLB art rejected",
      exact_mode="free public browser controls only",extra_payment=0,license_verified=False,
      physical_mobile_tested=False,art_approved=False,status="NO_RELEASE",
      results=[],glb_saved=False,free_provider_research=True)
    save("run139_status.json",state)
    with sync_playwright() as pw:
      browser=pw.chromium.launch(headless=True,args=["--use-gl=angle","--use-angle=swiftshader"])
      ctx=browser.new_context(viewport={"width":1366,"height":860},accept_downloads=True,locale="en-US")
      for pr in PROVIDERS:
        r=dict(name=pr["name"],url=pr["url"],status="PENDING",screenshots=[],network=[],actual_public_ui=True,
          fees_paid=0,auth_bypassed=False,generation_clicked=False)
        state["results"].append(r);save("run139_status.json",state)
        page=ctx.new_page(); collected=[]
        def on_resp(resp):
          try:
            typ=resp.headers.get("content-type","").lower();u=resp.url.lower()
            if ".glb" not in u and "model/gltf-binary" not in typ and "application/octet-stream" not in typ:
              return
            r["network"].append(dict(url=resp.url[:350],status=resp.status,content_type=typ[:100]))
            if resp.status!=200 or len(collected)>3:return
            b=resp.body()
            if 1024<len(b)<50_000_000 and b[:4]==b"glTF":
              p=O/("run139_"+pr["name"]+"_response_RESEARCH_ONLY.glb")
              p.write_bytes(b);collected.append(p)
          except Exception as e:r["network_hook_error"]=str(e)[:400]
        page.on("response",on_resp)
        try:
          page.goto(pr["url"],wait_until="domcontentloaded",timeout=60000)
          page.wait_for_timeout(4000)
          b=O/("run139_"+pr["name"]+"_initial.png")
          page.screenshot(path=str(b),timeout=25000)
          r["screenshots"].append(b.name)
          visible=page.locator("body").inner_text(timeout=15000)
          (O/("run139_"+pr["name"]+"_initial_visible.txt")).write_text(visible[:10000])
          r["title"]=page.title()
          r["file_inputs"]=page.locator("input[type=file]").count()
          if re.search(r"Generation (is )?paused|Rendering capacity unavailable",visible,re.I):
            r["status"]="PROVIDER_GENERATION_PAUSED";continue
          if page.locator("iframe[src*='turnstile'],iframe[src*='captcha']").count() or page.locator("input[name*='captcha']").count():
            r["status"]="CAPTCHA_PRESENT_NO_BYPASS";continue
          if not r["file_inputs"]:r["status"]="NO_VISIBLE_PUBLIC_FILE_INPUT";continue
          page.locator("input[type=file]").first.set_input_files(str(SRC.resolve()))
          page.wait_for_timeout(1700)
          (O/("run139_"+pr["name"]+"_post_upload_visible.txt")).write_text(page.locator("body").inner_text()[:10000])
          button=None
          for name in pr["buttons"]:
            loc=page.get_by_role("button",name=name,exact=False)
            if loc.count() and loc.first.is_visible():
              button=loc.first;r["chosen_button"]=name;break
          if button is None:r["status"]="NO_GENERATE_BUTTON";continue
          if not button.is_enabled():r["status"]="GENERATION_DISABLED";continue
          r["generation_clicked"]=True
          try:
            with page.expect_download(timeout=5000) as di:button.click(timeout=15000)
            d=di.value
            p=O/("run139_"+pr["name"]+"_button_download"+pathlib.Path(d.suggested_filename).suffix)
            d.save_as(str(p));collected.append(p)
            r["immediate_download"]=p.name
          except Exception as e:
            r["initial_async_click_or_no_immediate_download"]=str(e)[:280]
          start=time.monotonic()
          while time.monotonic()-start<155 and not any(p.suffix.lower()==".glb" and p.stat().st_size>1024 for p in collected):
            links=page.get_by_role("button",name=re.compile(r"(download|export).*(glb|model|3d)",re.I))
            if not links.count():links=page.get_by_role("link",name=re.compile(r"(download|export).*(glb|model|3d)",re.I))
            if not links.count():links=page.locator("a[download]")
            if links.count() and links.first.is_visible():
              try:
                with page.expect_download(timeout=11000) as ev:links.first.click(timeout=5000)
                d=ev.value
                p=O/("run139_"+pr["name"]+"_download"+pathlib.Path(d.suggested_filename).suffix)
                d.save_as(str(p));collected.append(p)
              except Exception as e:r["download_err"]=str(e)[:300]
            page.wait_for_timeout(7500)
          r["status"]="PUBLIC_UI_REQUEST_FINISHED_NO_VALID_GLB"
          for p in collected:
            try:
              info=gltf_info(p)
              r.setdefault("candidates",[]).append(info)
              if info["known_rejected_sha"] or info["triangles"]<1000:continue
              r["status"]="REAL_GLTF_QUARANTINED_FOR_ART_RIGHTS_QA"
              if not state["glb_saved"] or info["images"]>state["chosen_glb"]["images"]:
                shutil.copyfile(p,O/"run139_original_RESEARCH_ONLY.glb")
                state["chosen_glb"]=info;state["chosen_provider"]=pr["name"];state["glb_saved"]=True
            except Exception as e:
              r.setdefault("invalid",[]).append(dict(name=p.name,reason=str(e)[:300]))
        except Exception as e:
          r["status"]="ACTUAL_PUBLIC_BROWSER_ERROR";r["error"]=traceback.format_exc(limit=4)[-1800:]
        finally:
          try:
            s=O/("run139_"+pr["name"]+"_final.png")
            page.screenshot(path=str(s),timeout=20000)
            r["screenshots"].append(s.name)
            (O/("run139_"+pr["name"]+"_final_visible.txt")).write_text(page.locator("body").inner_text()[:10000])
          except Exception as e:r["final_capture_error"]=str(e)[:250]
          r["ended_utc"]=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())
          save("run139_status.json",state);page.close()
      browser.close()
    save("run139_status.json",state)
    print("REAL_BROWSER_RESULT",json.dumps(state,ensure_ascii=False))

def render():
    import bpy
    from mathutils import Vector
    p=O/"run139_original_RESEARCH_ONLY.glb"
    if not p.is_file():raise RuntimeError("No source mesh; do not create imitation")
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(p))
    meshes=[o for o in bpy.context.scene.objects if o.type=="MESH"]
    assert meshes,"Nothing imported: never claim rendering"
    points=[o.matrix_world@Vector(v) for o in meshes for v in o.bound_box]
    lo=Vector(tuple(min(q[i] for q in points) for i in range(3)))
    hi=Vector(tuple(max(q[i] for q in points) for i in range(3)))
    center=(lo+hi)*.5; extent=max(hi-lo)
    assert extent>0,"Degenerate imported geometry"
    scene=bpy.context.scene
    if not scene.world:scene.world=bpy.data.worlds.new("Run139 studio")
    scene.world.color=(.6,.6,.6)
    scene.render.engine="CYCLES";scene.cycles.samples=12
    scene.view_layers[0].cycles.use_denoising=False
    scene.render.resolution_x=500;scene.render.resolution_y=500
    scene.render.resolution_percentage=100
    def light(pos,power):
      ld=bpy.data.lights.new("run139_area","AREA")
      ld.energy=power;ld.size=extent*4
      ob=bpy.data.objects.new("run139_area",ld);scene.collection.objects.link(ob)
      ob.location=center+Vector(pos)*extent
      ob.rotation_euler=(center-ob.location).to_track_quat("-Z","Y").to_euler()
    light((-3,-3,4),360);light((3,2,2),200)
    cam=bpy.data.objects.new("run139_cam",bpy.data.cameras.new("run139_cam"))
    scene.collection.objects.link(cam);scene.camera=cam
    cam.data.type="ORTHO";cam.data.ortho_scale=extent*1.7
    for name,deg in (("front",0),("quarter",45),("side",90),("back",180)):
      a=math.radians(deg)
      cam.location=center+Vector((4*math.sin(a),-4*math.cos(a),1.2))*extent
      cam.rotation_euler=(center-cam.location).to_track_quat("-Z","Y").to_euler()
      scene.render.filepath=str(O/("run139_"+name+"_ACTUAL_CYCLES_UNAPPROVED.png"))
      bpy.ops.render.render(write_still=True)
    save("run139_native_mesh_info.json",dict(blender=bpy.app.version_string,mesh_count=len(meshes),
      polygons=sum(len(ob.data.polygons) for ob in meshes),bbox=list(hi-lo),native_four_views=True,
      art_approved=False,physical_phone_tested=False,status="NO_RELEASE"))
if __name__=="__main__":
  mode=sys.argv[-1]
  if mode=="browse":browse()
  elif mode=="render":render()
  else:raise SystemExit("usage: browse or render")
