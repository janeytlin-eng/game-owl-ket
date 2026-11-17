#!/usr/bin/env python3
"""Run149: real external CC0 GLB acquisition, Blender mesh deformation and honest four-view evidence.
Absolutely no low-quality geometry replacement; NO_RELEASE until actual aesthetic approval."""
import sys,json,hashlib,datetime,struct
from pathlib import Path
ROOT=Path("owl-pet/3d-experiments/172-tyto-castanops")
OUT=ROOT/"research-evidence-run149-BARNOWL-HOLLOW-TRUE-CC0-MESH-NO_RELEASE"
SOURCES={
  "owl":{"url":"https://cdn.3dassets.dev/assets/28079/v1/model.glb",
         "page":"https://3dassets.dev/assets/birds-and-reptiles-hd-barn-owl-b51d286f",
         "description":"Adult Tyto alba; NOT Tyto castanops cream-down juvenile"},
  "hollow":{"url":"https://cdn.3dassets.dev/assets/28115/v1/model.glb",
         "page":"https://3dassets.dev/assets/birds-and-reptiles-hd-tree-stump-with-hollow-5ad1c3f4",
         "description":"Generic hollow-stump prop, NOT verified old Tasmanian eucalypt"}}
def fetch():
    import urllib.request
    OUT.mkdir(parents=True,exist_ok=True)
    records={}
    for key,desc in SOURCES.items():
        state=dict(desc)
        try:
            req=urllib.request.Request(desc["url"],headers={"User-Agent":"Mozilla/5.0 (owl172 independent noncommercial QA)"})
            with urllib.request.urlopen(req,timeout=50) as r:
                buf=r.read(12000000)
                state.update(http_status=r.status,content_type=r.headers.get("Content-Type"),final_url=r.url,byte_length=len(buf))
            valid=(len(buf)>20 and buf[:4]==b"glTF" and struct.unpack_from("<I",buf,8)[0]==len(buf))
            state.update(valid_glb=valid,sha256=hashlib.sha256(buf).hexdigest())
            if valid:(OUT/("run149_CC0_"+key+"_ORIGINAL_RESEARCH_ONLY.glb")).write_bytes(buf)
        except Exception as e:
            state.update(valid_glb=False,error=type(e).__name__+": "+str(e))
        records[key]=state
    records["source_license"]="Publisher asset pages assert CC0 1.0 Universal; underlying creator rights not independently warranted."
    records["target"]="Rightmost Tyto castanops v3: AGE-UNKNOWN MESOPTILE with natural cream down and short hidden wings."
    records["timestamp_utc"]=datetime.datetime.now(datetime.timezone.utc).isoformat()
    records["extra_payment_usd"]=0
    (OUT/"run149_actual_fetch_provenance.json").write_text(json.dumps(records,indent=2,ensure_ascii=False),encoding="utf8")
    print(json.dumps(records,ensure_ascii=False),flush=True)

def native():
    import bpy,math
    from mathutils import Vector
    OUT.mkdir(parents=True,exist_ok=True)
    source=OUT/"run149_CC0_owl_ORIGINAL_RESEARCH_ONLY.glb"
    if not source.is_file():
        (OUT/"run149_native_skipped.txt").write_text("NO_SOURCE_GLTF: no fake rendering")
        return
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    bpy.ops.import_scene.gltf(filepath=str(source.resolve()))
    meshes=[o for o in bpy.context.scene.objects if o.type=="MESH"]
    assert meshes,"No genuine source mesh on import"
    def bounds():
        pts=[o.matrix_world @ Vector(b) for o in meshes for b in o.bound_box]
        return [min(p[k] for p in pts) for k in range(3)],[max(p[k] for p in pts) for k in range(3)]
    mn,mx=bounds()
    stats={"source_meshes":len(meshes),"source_polygons":sum(len(o.data.polygons) for o in meshes),"bbox_min":mn,"bbox_max":mx}
    (OUT/"run149_actual_source_mesh_stats.json").write_text(json.dumps(stats,indent=2))
    s=bpy.context.scene
    s.world=bpy.data.worlds.new("Neutral audit environment") if not s.world else s.world
    s.world.use_nodes=True
    s.world.node_tree.nodes["Background"].inputs["Color"].default_value=(.62,.63,.66,1)
    s.world.node_tree.nodes["Background"].inputs["Strength"].default_value=.5
    s.render.engine="CYCLES"
    s.cycles.samples=18
    if hasattr(bpy.context.view_layer.cycles,"use_denoising"):bpy.context.view_layer.cycles.use_denoising=False
    s.render.resolution_x=480;s.render.resolution_y=480;s.render.resolution_percentage=100
    s.render.image_settings.file_format="PNG"
    h=max(mx[2]-mn[2],.1)
    mid=Vector(((mn[0]+mx[0])/2,(mn[1]+mx[1])/2,(mn[2]+mx[2])/2))
    for offset,power in [(Vector((-2,-3,4)),400),(Vector((3,1,2)),230)]:
        lamp=bpy.data.lights.new("Softbox","AREA");lamp.energy=power;lamp.shape="DISK";lamp.size=h*2.5
        ob=bpy.data.objects.new("QA Softbox",lamp);s.collection.objects.link(ob)
        ob.location=mid+offset*h;ob.rotation_euler=(mid-ob.location).to_track_quat("-Z","Y").to_euler()
    cam=bpy.data.cameras.new("Orbit camera");camob=bpy.data.objects.new("QA orbit",cam)
    s.collection.objects.link(camob);s.camera=camob;cam.type="ORTHO"
    def render_four(prefix):
        a,b=bounds()
        center=Vector(tuple((a[i]+b[i])/2 for i in range(3)))
        rad=max(b[i]-a[i] for i in range(3))
        cam.ortho_scale=rad*1.32
        for label,angle in (("front",0),("quarter",math.pi/4),("side",math.pi/2),("back",math.pi)):
            camob.location=center+Vector((rad*3*math.sin(angle),-rad*3*math.cos(angle),rad*.45))
            camob.rotation_euler=(center-camob.location).to_track_quat("-Z","Y").to_euler()
            s.render.filepath=str((OUT/(prefix+"_"+label+"_ACTUAL_CYCLES_UNAPPROVED.png")).resolve())
            bpy.ops.render.render(write_still=True)
    render_four("run149_source")

    # Explicit adult-source proportion A/B: genuine high-fidelity mesh deformed in 3D.
    # This intentionally does NOT create a fake juvenile or pretend plumage has been solved.
    cx,cy=(mn[0]+mx[0])/2,(mn[1]+mx[1])/2
    bottom=mn[2];hh=mx[2]-mn[2]
    for obj in meshes:
        inverse=obj.matrix_world.inverted_safe()
        for v in obj.data.vertices:
            p=obj.matrix_world@v.co
            height=max(0,min(1,(p.z-bottom)/hh))
            crown=max(0,min(1,(height-.53)/.4))
            q=Vector((cx+(p.x-cx)*(1.10+.16*crown),
                      cy+(p.y-cy)*(1.12+.12*crown),
                      bottom+(p.z-bottom)*(.76+.06*crown)))
            v.co=inverse@q
        obj.data.update()
    bpy.ops.object.select_all(action="DESELECT")
    for obj in meshes:obj.select_set(True)
    bpy.context.view_layer.objects.active=meshes[0]
    derivative=OUT/"run149_actual_adult_mesh_proportion_ablation_NO_RELEASE.glb"
    bpy.ops.export_scene.gltf(filepath=str(derivative.resolve()),export_format="GLB",use_selection=True)
    render_four("run149_ablation")
    (OUT/"run149_ablation_metadata.json").write_text(json.dumps({
      "changed_geometry":"True vertex-space deformation of imported organic barn-owl source; no geometric toy stand-in",
      "quality":"UNREVIEWED; still adult anatomy with unknown face and down. Not publishable.",
      "mesh_count":len(meshes),"polygon_count":sum(len(o.data.polygons) for o in meshes)
    },indent=2))
    bpy.ops.object.select_all(action="SELECT");bpy.ops.object.delete(use_global=False)
    bpy.ops.import_scene.gltf(filepath=str(derivative.resolve()))
    re=[o for o in bpy.context.scene.objects if o.type=="MESH"]
    count=sum(len(o.data.polygons) for o in re)
    assert count>1000,"Derivative failed genuine GLB reimport"
    (OUT/"run149_actual_reimport.json").write_text(json.dumps({"mesh_count":len(re),"faces":count,"art_approved":False,"physical_phone_tested":False},indent=2))
if __name__=="__main__":
    if len(sys.argv)>1 and sys.argv[1]=="fetch":fetch()
    elif "--" in sys.argv and "render" in sys.argv[sys.argv.index("--")+1:]:native()
    else:raise SystemExit("expected fetch or -- render")
