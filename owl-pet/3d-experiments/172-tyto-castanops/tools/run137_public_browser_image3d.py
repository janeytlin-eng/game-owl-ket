#!/usr/bin/env python3
"""Run137: one real, no-signup, no-payment image-to-3D browser attempt per
publicly advertised free service. #172 v3 RIGHTMOST owl only.
Third-party rights, geometry, 4-view art and phone GPU MUST be separately
approved; all output is RESEARCH_ONLY / NO_RELEASE. Not an automated pet.
"""
import os,sys,json,time,hashlib,traceback,struct,pathlib,shutil,math
R=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
SRC=R/"research-evidence-run117-FREE-TRELLIS-QUOTA-RECHECK-ART_REJECTED/rightmost_baby_owl_512_rgba.png"
OUT=R/"research-evidence-run137-PUBLIC-BROWSER-REAL-GLB-STRICT-NO_RELEASE"
OUT.mkdir(parents=True,exist_ok=True)
PIN="e439928a9ef08d3be266106cb5f2766b6f5a9f2c414d44e8da55ba81732153b8"
def store(name,data):
    (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2,default=str)+"\n")
def digest(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def inspect_glb(p):
    b=pathlib.Path(p).read_bytes()
    if len(b)<1024 or b[:4]!=b"glTF" or struct.unpack_from("<I",b,8)[0]!=len(b):
        raise ValueError("Not a complete binary glTF file")
    sz,ty=struct.unpack_from("<I4s",b,12)
    if ty!=b"JSON" or sz>len(b)-20: raise ValueError("No valid GLB JSON")
    d=json.loads(b[20:20+sz].decode("utf-8").rstrip("\x00 "))
    tri=sum(d["accessors"][v["indices"]]["count"]//3 for m in d.get("meshes",[])
      for v in m.get("primitives",[]) if v.get("mode",4)==4 and "indices" in v)
    return dict(bytes=len(b),sha256=digest(p),meshes=len(d.get("meshes",[])),
      triangles=tri,images=len(d.get("images",[])),materials=len(d.get("materials",[])),
      animations=len(d.get("animations",[])),glb_header_valid=True)
def browse():
    from PIL import Image
    from playwright.sync_api import sync_playwright
    assert SRC.is_file(), "Source crop absent"
    assert digest(SRC)==PIN, "Wrong species source or modified crop"
    assert Image.open(SRC).size==(512,512), "Crop dimensions wrong"
    shutil.copy2(SRC,OUT/"run137_true_rightmost_reference_RGBA.png")
    state=dict(source=str(SRC),source_sha256=PIN,run="137",zero_payment=True,
      provenance="172 v3 rightmost real reference",providers=[],result="NO_GLB",
      art_approved=False,license_cleared=False,real_phone_tested=False,
      status="ART_UNREVIEWED / NO_RELEASE")
    store("run137_status.json",state)
    with sync_playwright() as pw:
      browser=pw.chromium.launch(headless=True,args=["--use-gl=angle","--use-angle=swiftshader"])
      ctx=browser.new_context(viewport={"width":1366,"height":860},accept_downloads=True,
        locale="en-US",user_agent=None)
      for slug,url in (("3dai","https://3dai.dev/en"),("hy3d","https://hy3d.dev/")):
        detail=dict(provider=slug,url=url,network=[],screenshots=[],status="NOT_STARTED",
                    one_off_free_attempt=True,rights_unverified=True)
        state["providers"].append(detail)
        store("run137_status.json",state)
        page=ctx.new_page()
        # Public UI only: do not spoof auth, bypass queues or use hidden endpoints.
        files=[]
        def response_hook(resp):
          try:
            ct=resp.headers.get("content-type","")
            u=resp.url
            if any(t in (u+" "+ct).lower() for t in [".glb","model/gltf-binary","application/octet-stream"]):
              detail["network"].append({"url":u[:220],"status":resp.status,
                                        "type":ct[:100]})
              if resp.ok and len(files)<2:
                body=resp.body()
                if len(body)<40_000_000 and body[:4]==b"glTF":
                  p=OUT/("run137_"+slug+"_PUBLIC_RESPONSE_RESEARCH_ONLY.glb")
                  p.write_bytes(body);files.append(p)
          except Exception as e:
            detail["network_exception"]=str(e)[:300]
        page.on("response",response_hook)
        try:
          page.goto(url,wait_until="domcontentloaded",timeout=65000)
          page.wait_for_timeout(4000)
          path=OUT/("run137_"+slug+"_before.png")
          page.screenshot(path=str(path),full_page=False,timeout=30000)
          detail["screenshots"].append(path.name)
          inputs=page.locator("input[type=file]")
          detail["file_inputs"]=inputs.count()
          if not inputs.count():
            detail["status"]="NO_PUBLIC_FILE_UPLOAD_CONTROL"
            continue
          inputs.first.set_input_files(str(SRC.resolve()))
          page.wait_for_timeout(1800)
          (OUT/("run137_"+slug+"_post_upload_text.txt")).write_text(page.locator("body").inner_text()[:7000])
          # Act once via visible, public Generate UI only, without authentication.
          buttons=page.get_by_role("button",name="Generate textured 3D")
          if not buttons.count(): buttons=page.get_by_role("button",name="GENERATE")
          if not buttons.count(): buttons=page.locator("button").filter(has_text="Generate")
          detail["generate_buttons"]=buttons.count()
          if not buttons.count(): detail["status"]="NO_PUBLIC_GENERATE_BUTTON";continue
          if not buttons.first.is_enabled(): detail["status"]="GENERATE_DISABLED";continue
          with page.expect_download(timeout=9000) as di:
            buttons.first.click(timeout=15000)
          downloaded=di.value
          dest=OUT/("run137_"+slug+"_DIRECT_RESEARCH_ONLY"+pathlib.Path(downloaded.suggested_filename).suffix)
          downloaded.save_as(str(dest))
          if dest.suffix.lower()==".glb":
            files.append(dest)
          else: detail["early_download"]=dest.name
          detail["clicked"]=True
        except Exception as exc:
          # A generation request may run asynchronously with no immediate download.
          detail["click_or_early_download"]=str(exc)[:500]
          if detail.get("generate_buttons",0)>0:detail["clicked"]=True
        try:
          if detail.get("clicked"):
            start=time.monotonic()
            while time.monotonic()-start<450 and not files:
              try:
                # Public file-download UI; neither guessing API nor bypassing restrictions.
                links=page.get_by_role("link",name="Download GLB")
                if not links.count(): links=page.get_by_role("button",name="Download GLB")
                if not links.count():links=page.locator("a[download]")
                if links.count() and links.first.is_visible():
                  try:
                    with page.expect_download(timeout=18000) as ev:
                      links.first.click(timeout=5000)
                    d=ev.value
                    p=OUT/("run137_"+slug+"_UI_RESEARCH_ONLY.glb")
                    d.save_as(str(p));files.append(p)
                  except Exception as ex: detail["download_click_error"]=str(ex)[:300]
                if not files:page.wait_for_timeout(9000)
              except Exception as ex:
                detail["poll_error"]=str(ex)[:300];break
          path=OUT/("run137_"+slug+"_after.png")
          page.screenshot(path=str(path),full_page=False,timeout=25000)
          detail["screenshots"].append(path.name)
          (OUT/("run137_"+slug+"_visible_text.txt")).write_text(page.locator("body").inner_text()[:9000])
          for p in files:
            try:
              meta=inspect_glb(p)
              detail["model_meta"]=meta
              if meta["triangles"]>=1000:
                dest=OUT/"run137_verified_raw_provider_RESEARCH_ONLY.glb"
                shutil.copy2(p,dest)
                state["glb"]=inspect_glb(dest)
                state["provider"]=slug
                state["result"]="REAL_GLB_ART_UNREVIEWED"
                detail["status"]="REAL_GLTF_REQUIRES_ART_AND_RIGHTS_QA"
                break
              else:detail["invalid_candidate"]="too few triangles"
            except Exception as e: detail["invalid_candidate"]=str(e)[:400]
          if state["result"]=="NO_GLB" and detail["status"]=="NOT_STARTED":
            detail["status"]="NO_VALID_GLTF_RETURNED"
        except Exception as e:
          detail["failure"]=traceback.format_exc(limit=6)[-1600:]
          detail["status"]="BROWSER_OR_PROVIDER_FAILED"
        finally:
          detail["elapsed_finished_utc"]=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())
          store("run137_status.json",state)
          page.close()
        if state["result"]!="NO_GLB": break
      browser.close()
    print("RUN137_STATUS",json.dumps(state,ensure_ascii=False))
def render():
    import bpy
    from mathutils import Vector
    p=OUT/"run137_verified_raw_provider_RESEARCH_ONLY.glb"
    if not p.is_file():raise RuntimeError("Never fake native renders: real GLB missing")
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(p))
    meshes=[o for o in bpy.context.scene.objects if o.type=="MESH"]
    assert meshes,"No real imported meshes"
    points=[o.matrix_world@Vector(c) for o in meshes for c in o.bound_box]
    lo=Vector(tuple(min(v[i] for v in points) for i in range(3)))
    hi=Vector(tuple(max(v[i] for v in points) for i in range(3)))
    center=(lo+hi)*.5
    extent=max(hi-lo)
    scene=bpy.context.scene
    if not scene.world:scene.world=bpy.data.worlds.new("Run137")
    scene.world.color=(.42,.42,.42)
    scene.render.engine="CYCLES";scene.cycles.samples=16
    scene.render.resolution_x=480;scene.render.resolution_y=480
    scene.render.resolution_percentage=100
    def area(xyz,power):
      ld=bpy.data.lights.new("light","AREA");ld.energy=power;ld.size=4*extent
      ob=bpy.data.objects.new("light",ld);scene.collection.objects.link(ob)
      ob.location=center+Vector(xyz)*extent
      ob.rotation_euler=(center-ob.location).to_track_quat("-Z","Y").to_euler()
    area((-3,-3,4),330);area((3,1,2),210)
    cam=bpy.data.objects.new("camera",bpy.data.cameras.new("camera"))
    scene.collection.objects.link(cam);scene.camera=cam
    cam.data.type="ORTHO";cam.data.ortho_scale=1.7*extent
    for name,angle in (("front",0),("quarter",45),("side",90),("back",180)):
      a=math.radians(angle)
      cam.location=center+Vector((4*math.sin(a),-4*math.cos(a),1.3))*extent
      cam.rotation_euler=(center-cam.location).to_track_quat("-Z","Y").to_euler()
      scene.render.filepath=str(OUT/("run137_"+name+"_ACTUAL_BLENDER_UNAPPROVED.png"))
      bpy.ops.render.render(write_still=True)
    store("run137_mesh_native_qa.json",dict(mesh_objects=len(meshes),
      blender=bpy.app.version_string,original_bbox=list(hi-lo),
      triangles=sum(len(ob.data.polygons) for ob in meshes),
      four_angle_rendered=True,approved=False,real_phone=False))
if __name__=="__main__":
    if sys.argv[-1]=="browse":browse()
    elif sys.argv[-1]=="render":render()
    else:raise SystemExit("usage browse|render")
