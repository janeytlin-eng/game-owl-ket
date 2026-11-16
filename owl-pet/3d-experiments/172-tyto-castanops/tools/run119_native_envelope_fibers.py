#!/usr/bin/env python3
"""Run119 experimental anatomical envelope and physical strand ablation on real TRELLIS source.
Research only: no primitive owl body, no SVG, no release, no rights assertion.
"""
import sys, argparse, hashlib, math, random, bisect, json, pathlib
import bpy
from mathutils import Vector, Matrix
from math import sin, cos, radians, pi

p=argparse.ArgumentParser()
p.add_argument("--source",required=True);p.add_argument("--out",required=True)
a=p.parse_args(sys.argv[sys.argv.index("--")+1:])
src=pathlib.Path(a.source); out=pathlib.Path(a.out);out.mkdir(parents=True,exist_ok=True)
sha=lambda f:hashlib.sha256(pathlib.Path(f).read_bytes()).hexdigest()
SOURCE_SHA="2893e95965a9c6e6fd3af5779c1ebf3b65a16b6cdaebf7c2f743e047b9fa78de"
assert src.is_file() and src.read_bytes()[:4]==b"glTF" and sha(src)==SOURCE_SHA
bpy.ops.object.select_all(action="SELECT");bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=str(src))
meshes=[o for o in bpy.context.scene.objects if o.type=="MESH"]
assert len(meshes)==1, "No new procedural owl proxy permitted"
obj=meshes[0]; original_verts=len(obj.data.vertices);original_faces=len(obj.data.polygons)
assert original_faces>30000
world=obj.matrix_world.copy()
pts=[world@v.co for v in obj.data.vertices]
obj.parent=None;obj.matrix_world=Matrix.Identity(4)
lo=Vector(tuple(min(q[i] for q in pts) for i in range(3)))
hi=Vector(tuple(max(q[i] for q in pts) for i in range(3)))
c=(lo+hi)*.5;d=hi-lo;s=max(d)
assert min(d)>.4 and max(d)<2,tuple(d)
# Correct the specific volume problem: posterior long adult-flight-feather sack, not the heart front.
posterior_changed=0
for v,q in zip(obj.data.vertices,pts):
    rz=(q.z-lo.z)/d.z
    aft=max(0., min(1.,(q.y-c.y)/(.5*d.y)))
    lower=math.exp(-.5*((rz-.49)/.34)**2)
    q.y=c.y+(q.y-c.y)*(1.-.33*aft*lower)
    q.x=c.x+(q.x-c.x)*(1.+.095*lower)
    if aft>.01 and lower>.2:posterior_changed+=1
    v.co=q
obj.data.update()
# Smooth only the wing/posterior and belly, preserving the already-recognizable heart.
g=obj.vertex_groups.new(name="rear_wing_and_body_only")
for v in obj.data.vertices:
    q=v.co;rz=(q.z-lo.z)/d.z
    front=(c.y-q.y)/d.y
    facial=rz>.61 and front>.09 and abs(q.x-c.x)<d.x*.45
    rear=max(0.,min(1.,(q.y-c.y)/(.23*d.y)+.55))
    wt=0.0 if facial else max(.40, min(1.0,.62+.42*rear))
    if rz<.15:wt=.10
    g.add([v.index],wt,"REPLACE")
bpy.context.view_layer.objects.active=obj
obj.select_set(True)
sm=obj.modifiers.new("continuous_existing_geometry_scale_softening","SMOOTH")
sm.factor=.79;sm.iterations=42;sm.vertex_group=g.name
bpy.ops.object.modifier_apply(modifier=sm.name)
# Rebuild native polygon topology to avoid glTF custom attribute export errors.
raw=obj.data
clean=bpy.data.meshes.new("real_source_3d_topology_after_nonrigid_sculpt")
clean.from_pydata([tuple(v.co) for v in raw.vertices],[],[tuple(f.vertices) for f in raw.polygons])
clean.update()
obj.data=clean
if raw.users==0:bpy.data.meshes.remove(raw)
obj.name="real_TRELLIS_source_nonrigid_juvenile_attempt_RESEARCH"
for f in obj.data.polygons:f.use_smooth=True

def mat(name,color,rough=.93):
    m=bpy.data.materials.new(name)
    m.diffuse_color=(*color,1)
    m.use_nodes=True
    b=m.node_tree.nodes.get("Principled BSDF")
    b.inputs["Base Color"].default_value=(*color,1)
    b.inputs["Metallic"].default_value=0
    b.inputs["Roughness"].default_value=rough
    return m
cream=mat("matte_cream_chick_down_undercoat",(0.91,.847,.748))
warmface=mat("integrated_warm_ivory_facial_surface",(.94,.858,.724))
crown=mat("sunlit_cream_crown",(.96,.914,.843))
foot=mat("muted_gray_toe",(.26,.23,.20))
pupil=mat("refractive_dark_brown_eye",(.022,.014,.009),.14)
glint=mat("small_corneal_glint",(.95,.91,.83),.20)
fibermat=mat("real_sculpt_surface_cream_down_fibers",(.986,.928,.815))
obj.data.materials.clear()
for m in [cream,warmface,crown,foot]:obj.data.materials.append(m)
for poly in obj.data.polygons:
    q=poly.center
    rz=(q.z-lo.z)/d.z
    yf=(c.y-q.y)/d.y
    if rz<.17: poly.material_index=3
    elif rz>.79 and yf>.07: poly.material_index=2
    elif rz>.60 and yf>.13 and abs(q.x-c.x)<d.x*.43:poly.material_index=1
    else:poly.material_index=0
# Physical eye surfaces on actual 3D raycast sockets, not image overlay.
bpy.context.view_layer.update()
eyes=[]; ornaments=[]
for sign in [-1,1]:
    x=c.x+sign*d.x*.118
    z=lo.z+d.z*.71
    origin=Vector((x,lo.y-.5*s,z))
    hit,pos,norm,face,hit_obj,matrix=bpy.context.scene.ray_cast(
        bpy.context.evaluated_depsgraph_get(),origin,Vector((0,1,0)),distance=3*s)
    eyes.append(dict(sign=sign,hit=bool(hit),point=list(pos) if hit else None))
    if not hit or hit_obj!=obj:continue
    r=s*.041
    bpy.ops.mesh.primitive_uv_sphere_add(segments=22,ring_count=12,radius=r,
        location=(pos.x,pos.y-s*.007,pos.z))
    eye=bpy.context.object;eye.name="registered_open_chick_eye_"+str(sign)
    eye.scale=(.90,.28,.92);eye.data.materials.append(pupil)
    for f in eye.data.polygons:f.use_smooth=True
    ornaments.append(eye)
    bpy.ops.mesh.primitive_uv_sphere_add(segments=10,ring_count=8,radius=r*.14,
        location=(pos.x-sign*r*.20,pos.y-s*.016,pos.z+r*.24))
    sparkle=bpy.context.object;sparkle.name="true_3D_eye_highlight_"+str(sign)
    sparkle.data.materials.append(glint);ornaments.append(sparkle)
assert all(e["hit"] for e in eyes),"Socket raycast failed: reject and investigate"
# Actual curved and tapered fibers on true mesh triangles, not floating mesh impostor:
mesh=obj.data;mesh.calc_loop_triangles()
verts=mesh.vertices
tris=mesh.loop_triangles
cdf=[];area=0.
for t in tris:
    x,y,z=[verts[k].co for k in t.vertices]
    area+=(y-x).cross(z-x).length*.5
    cdf.append(area)
assert area>0
rng=random.Random(172119)
curve=bpy.data.curves.new("Fine_Airy_3D_Down_Over_True_Neural_Sculpt","CURVE")
curve.dimensions="3D";curve.resolution_u=1
curve.bevel_depth=s*.00060;curve.bevel_resolution=1
curve.use_fill_caps=False
nstrands=0;attempts=0
while nstrands<4700 and attempts<45000:
    attempts+=1
    t=tris[min(len(tris)-1,bisect.bisect_left(cdf,rng.random()*area))]
    x,y,z=[verts[k].co for k in t.vertices]
    u=rng.random();v=rng.random()
    if u+v>1:u=1-u;v=1-v
    q=x+(y-x)*u+(z-x)*v
    n=(y-x).cross(z-x).normalized()
    rz=(q.z-lo.z)/d.z
    if rz<.23:continue
    # Keep the eyes, facial disc and its large heart clear for the original silhouette.
    if q.y<c.y-.08*d.y and rz>.58 and abs(q.x-c.x)<d.x*.49:continue
    if n.z<-.73:continue
    length=s*rng.uniform(.018,.040)
    direction=(n*.79+Vector((rng.uniform(-.19,.19),rng.uniform(-.13,.13),-.28))).normalized()
    bend=Vector((rng.uniform(-1,1),rng.uniform(-1,1),rng.uniform(-.4,.4))).normalized()
    root=q+n*s*.0014
    mid=root+direction*length*.5+n*length*.11
    tip=root+direction*length+bend*length*.23
    spline=curve.splines.new("POLY");spline.points.add(2)
    for j,(co,rad) in enumerate([(root,.90),(mid,.72),(tip,.04)]):
        spline.points[j].co=(*co,1.0);spline.points[j].radius=rad
    nstrands+=1
coat=bpy.data.objects.new("4700_real_curved_down_fibers",curve)
bpy.context.scene.collection.objects.link(coat)
coat.data.materials.append(fibermat)
# Convert evaluated physical curves to ordinary mesh for honest glTF/WebGL compatibility.
bpy.ops.object.select_all(action="DESELECT");coat.select_set(True)
bpy.context.view_layer.objects.active=coat
bpy.ops.object.convert(target="MESH")
coat=bpy.context.object;coat.name="GLB_baked_native_curve_down_mesh"
assert len(coat.data.polygons)>10000
models=[obj,coat]+ornaments
glb=out/"run119_real_neural_sculpt_with_true_curved_fibers_ART_UNAPPROVED.glb"
bpy.ops.object.select_all(action="DESELECT")
for m in models:m.select_set(True)
bpy.context.view_layer.objects.active=obj
bpy.ops.export_scene.gltf(filepath=str(glb),export_format="GLB",use_selection=True,
    export_materials="EXPORT")
assert glb.read_bytes()[:4]==b"glTF" and glb.stat().st_size>200000
# Verify actual GLB is importable, never equate export success with import success.
bpy.ops.object.select_all(action="DESELECT")
before=set(bpy.context.scene.objects)
bpy.ops.import_scene.gltf(filepath=str(glb))
reimports=[m for m in bpy.context.scene.objects if m not in before and m.type=="MESH"]
assert len(reimports)>=3
triangles=sum(len(m.data.loop_triangles) for m in reimports)
assert triangles>original_faces,"Mesh geometry vanished on export"
for m in reimports:bpy.data.objects.remove(m,do_unlink=True)
# Native multiview cycles on exactly the exported 3D composition.
scene=bpy.context.scene;scene.render.engine="CYCLES";scene.cycles.samples=22
scene.render.resolution_x=480;scene.render.resolution_y=480
scene.render.resolution_percentage=100
scene.render.image_settings.file_format="PNG"
scene.view_settings.view_transform="Standard"
scene.world.color=(.20,.19,.18)
def area_light(name,offset,energy,size):
    ld=bpy.data.lights.new(name,"AREA");ld.energy=energy;ld.shape="DISK";ld.size=size*s
    o=bpy.data.objects.new(name,ld);scene.collection.objects.link(o)
    o.location=c+Vector(offset)*s
    o.rotation_euler=(c-o.location).to_track_quat("-Z","Y").to_euler()
area_light("large_soft_key",(-2.6,-3.1,2.8),450,4)
area_light("neutral_fill",(2.2,-1.9,1.2),280,3)
area_light("warm_backlight",(2.0,2.8,2.4),350,3)
cam=bpy.data.objects.new("run119_true_spatial_camera",bpy.data.cameras.new("run119_true_spatial_camera"))
scene.collection.objects.link(cam);scene.camera=cam;cam.data.type="ORTHO"
cam.data.ortho_scale=s*1.66
center=c+Vector((0,0,-.03*s))
for label,theta in [("front",0),("quarter",45),("side",90),("back",180)]:
    t=radians(theta)
    cam.location=center+Vector((3.6*sin(t),-3.6*cos(t),1.0))*s
    cam.rotation_euler=(center-cam.location).to_track_quat("-Z","Y").to_euler()
    scene.render.filepath=str(out/("run119_"+label+"_actual_cycles_ART_UNAPPROVED.png"))
    bpy.ops.render.render(write_still=True)
stats={"run":"119","outcome":"ART_REJECTED_pending_independent_multiview_visual_review",
  "actual_source_sha256":sha(src),"original_faces":original_faces,
  "original_vertices":original_verts,"posterior_vertices_modified":posterior_changed,
  "real_mesh_3d_fiber_count":nstrands,"baked_fiber_polygons":len(coat.data.polygons),
  "actual_import_meshes":len(reimports),"actual_import_triangles":triangles,
  "source_dims":list(d),"real_GLb_bytes":glb.stat().st_size,"real_GLb_sha256":sha(glb),
  "eye_raycasts":eyes,
  "all_quality_gates":"NOT APPROVED: real phone GPU, anatomy, fur, bark support, worldwide rights"}
(out/"run119_native_geometry_metrics.json").write_text(json.dumps(stats,indent=2))
print("RUN119_EXPERIMENT_REAL_GEOMETRY_EXPORTED_ART_UNAPPROVED",json.dumps(stats))
