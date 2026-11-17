#!/usr/bin/env python3
"""Run141: native mesh sculpt ablation on REAL Run139 textured neural GLB.
No replacement of owl with primitives; input SHA pinned; no art/rights approval.
Two variants: topology-preserving juvenile tail/wing tuck, then SMALL true
3D eye-surface ablation on that same original real PBR geometry.
"""
import bpy, math, json, pathlib, hashlib, sys
from mathutils import Vector
R=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
O=R/"research-evidence-run141-NATIVE-PBR-EYE-WING-NO_RELEASE"
O.mkdir(parents=True, exist_ok=True)
SRC=O/"run139_original_RESEARCH_ONLY.glb"
PIN="9a154c9e3aeebb34ebcd6f209760e1d9e21e2f544f2b690dae406d9c8bf878e8"
def sha(path):return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()
assert SRC.is_file() and sha(SRC)==PIN, "Source must be exact real Run139 PBR GLB, not imitation or duplicate"
report={"experiment":"Run141 #172 native actual PBR geometry","input_sha256":PIN,
        "original_source":"Run139 3DValley TRELLIS.2 free public output",
        "license_cleared":False,"art_approved":False,"physical_mobile_tested":False,
        "release":"NO_RELEASE","variants":[],"blender":bpy.app.version_string}

def open_scene(source):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(source))
    ms=[ob for ob in bpy.context.scene.objects if ob.type=="MESH"]
    if len(ms)!=1:raise RuntimeError("Expected exactly 1 genuine PBR neural source mesh; got %s"%len(ms))
    ob=ms[0]
    if len(ob.data.polygons)<180000:raise RuntimeError("PBR original mesh topology unexpectedly absent")
    return ob

def bbox(ob):
    ps=[ob.matrix_world@v.co for v in ob.data.vertices]
    lo=Vector(tuple(min(p[i] for p in ps) for i in range(3)))
    hi=Vector(tuple(max(p[i] for p in ps) for i in range(3)))
    return lo,hi

def render_views(tag):
    ms=[ob for ob in bpy.context.scene.objects if ob.type=="MESH"]
    all_pts=[ob.matrix_world@Vector(c) for ob in ms for c in ob.bound_box]
    lo=Vector(tuple(min(p[i] for p in all_pts) for i in range(3)))
    hi=Vector(tuple(max(p[i] for p in all_pts) for i in range(3)))
    c=(lo+hi)*.5; extent=max(hi-lo)
    sc=bpy.context.scene
    if not sc.world:sc.world=bpy.data.worlds.new("Run141 neutral world")
    sc.world.color=(.55,.55,.55)
    sc.render.engine="CYCLES";sc.cycles.samples=12
    sc.view_layers[0].cycles.use_denoising=False
    sc.render.resolution_x=460;sc.render.resolution_y=460
    sc.render.resolution_percentage=100
    sc.view_settings.view_transform="Standard"
    sc.view_settings.look="Medium High Contrast"
    for pos,power in ((Vector((-3,-3,4)),400),(Vector((3,1,2)),220)):
        ld=bpy.data.lights.new("Run141 softbox","AREA");ld.energy=power;ld.size=extent*4
        light=bpy.data.objects.new("Run141 softbox",ld);sc.collection.objects.link(light)
        light.location=c+pos*extent
        light.rotation_euler=(c-light.location).to_track_quat("-Z","Y").to_euler()
    cam=bpy.data.objects.new("Run141 camera",bpy.data.cameras.new("Run141 camera"))
    sc.collection.objects.link(cam);sc.camera=cam
    cam.data.type="ORTHO";cam.data.ortho_scale=extent*1.58
    shots=[]
    for name,deg in (("front",0),("quarter",45),("side",90),("back",180)):
        a=math.radians(deg)
        cam.location=c+Vector((4*math.sin(a),-4*math.cos(a),1.2))*extent
        cam.rotation_euler=(c-cam.location).to_track_quat("-Z","Y").to_euler()
        path=O/("run141_"+tag+"_"+name+"_ACTUAL_CYCLES_NO_RELEASE.png")
        sc.render.filepath=str(path);bpy.ops.render.render(write_still=True)
        assert path.exists() and path.stat().st_size>10000
        shots.append(path.name)
    return shots

def shape_real_neural_mesh(ob):
    lo,hi=bbox(ob);c=(lo+hi)*.5;d=hi-lo
    assert min(d)>.1
    inv=ob.matrix_world.inverted()
    changed=0;sum_delta=0.;max_delta=0.
    for v in ob.data.vertices:
        p=ob.matrix_world@v.co
        t=(p.z-lo.z)/d.z
        top=math.exp(-.5*((t-.785)/.145)**2)
        chest=math.exp(-.5*((t-.48)/.21)**2)
        # Alter the true continuous native surface rather than attaching
        # toy egg/sphere/flat billboard geometry.
        q=p.copy()
        q.x=c.x+(p.x-c.x)*(1.+.15*top+.055*chest)
        back=max(0.,min(1.,(p.y-c.y)/max(hi.y-c.y,.0001)))
        low=max(0.,min(1.,(.81-t)/.56))
        q.y=c.y+(p.y-c.y)*(1.-.30*back*low-.08*chest)
        # Gently lift drooping long rear low feather mass, but preserve toes.
        q.z=p.z+d.z*.055*back*back*math.exp(-.5*((t-.27)/.19)**2)
        delta=(q-p).length
        if delta>1e-6:changed+=1;sum_delta+=delta;max_delta=max(max_delta,delta)
        v.co=inv@q
    ob.data.update()
    return {"input_bbox":list(d),"native_vertices_moved":changed,
            "mean_vertex_displacement":sum_delta/max(changed,1),
            "max_vertex_displacement":max_delta,"post_bbox":list(bbox(ob)[1]-bbox(ob)[0])}

def test_eye_surface(ob):
    lo,hi=bbox(ob);c=(lo+hi)*.5;d=hi-lo
    inv=ob.matrix_world.inverted()
    fixes=[]
    for sign in (-1,1):
        hit=None
        for zt in (.79,.77,.75,.81,.73):
            for xt in (.12,.10,.08,.14):
                x=c.x+sign*d.x*xt
                z=lo.z+d.z*zt
                start=Vector((x,lo.y-d.y*.7,z))
                direction=Vector((0,1,0))
                yes,loc,nrm,face=ob.ray_cast(inv@start,inv.to_3x3()@direction)
                if yes:
                    hit=(ob.matrix_world@loc,sign,face,zt,xt)
                    break
            if hit:break
        if hit is None:
            fixes.append({"side":sign,"status":"NO_SURFACE_HIT"});continue
        pt,_,face,zt,xt=hit
        # Tiny genuine convex eye insert is anatomical detail on a complete
        # 192k triangle neural owl, NEVER an owl assembled from basic shapes.
        bpy.ops.mesh.primitive_uv_sphere_add(segments=24,ring_count=12,location=pt+Vector((0,-.003,0)))
        eye=bpy.context.object
        eye.name="Run141_Sculpted_inset_black_eye_"+str(sign)
        eye.scale=(d.x*.054,d.y*.021,d.z*.057)
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        for f in eye.data.polygons:f.use_smooth=True
        mat=bpy.data.materials.get("Run141 dark iris material")
        if mat is None:
            mat=bpy.data.materials.new("Run141 dark iris material")
            mat.diffuse_color=(.023,.018,.013,1.)
            mat.use_nodes=True
            node=mat.node_tree.nodes.get("Principled BSDF")
            if node:
                node.inputs["Base Color"].default_value=(.023,.018,.013,1)
                node.inputs["Roughness"].default_value=.18
        eye.data.materials.append(mat)
        fixes.append({"side":sign,"status":"NATIVE_SURFACE_HIT","face_index":face,
                     "hit_world":list(pt),"zt":zt,"xt":xt,"eye_mesh_polygons":len(eye.data.polygons)})
    return fixes

def export_variant(tag):
    selected=[ob for ob in bpy.context.scene.objects if ob.type=="MESH"]
    bpy.ops.object.select_all(action="DESELECT")
    for ob in selected:ob.select_set(True)
    bpy.context.view_layer.objects.active=selected[0]
    out=O/("run141_"+tag+"_RESEARCH_ONLY.glb")
    bpy.ops.export_scene.gltf(filepath=str(out),export_format="GLB",use_selection=True,
       export_materials="EXPORT",export_texcoords=True,export_normals=True)
    assert out.is_file() and out.stat().st_size>1000000 and out.read_bytes()[:4]==b"glTF"
    before_faces=sum(len(ob.data.polygons) for ob in selected)
    # Export must be independently reopenable, not just an Blender object.
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(out))
    reopened=[ob for ob in bpy.context.scene.objects if ob.type=="MESH"]
    after_faces=sum(len(ob.data.polygons) for ob in reopened)
    assert after_faces>=before_faces*.99,(tag,before_faces,after_faces)
    shots=render_views(tag)
    return {"glb_name":out.name,"bytes":out.stat().st_size,"sha256":sha(out),
       "native_polygons":before_faces,"reimport_polygons":after_faces,
       "reimport_mesh_count":len(reopened),"real_cycles_views":shots}

base=open_scene(SRC)
report["original"]={"mesh_faces":len(base.data.polygons),"bbox":list(bbox(base)[1]-bbox(base)[0]),
                  "sha256":sha(SRC),"original_views":render_views("source")}
(O/"run141_metrics.json").write_text(json.dumps(report,indent=2))
for tag,eyes in (("native_tuck_only",False),("native_tuck_eyes",True)):
    ob=open_scene(SRC)
    rec={"variant":tag,"real_native_original_sha":sha(SRC)}
    rec["continuous_sculpt"]=shape_real_neural_mesh(ob)
    if eyes:rec["eye_surface_ablation"]=test_eye_surface(ob)
    rec.update(export_variant(tag))
    report["variants"].append(rec)
    (O/"run141_metrics.json").write_text(json.dumps(report,indent=2)+"\n")
print("RUN141_REAL_MODEL_ABLATIONS",json.dumps(report,ensure_ascii=False))
