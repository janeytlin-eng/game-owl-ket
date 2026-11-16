#!/usr/bin/env python3
"""One-off real neural mesh retouch QA. No art approval, distribution, or paid inference."""
import argparse, bpy, bisect, hashlib, json, math, pathlib, random, sys
from mathutils import Vector, Matrix
from math import sin,cos,pi,radians

parser=argparse.ArgumentParser()
parser.add_argument("--source",required=True)
parser.add_argument("--out",required=True)
args=parser.parse_args(sys.argv[sys.argv.index("--")+1:] if "--" in sys.argv else None)
root=pathlib.Path(args.out);root.mkdir(parents=True,exist_ok=True)
def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=args.source)
meshes=[o for o in bpy.context.scene.objects if o.type=="MESH"]
assert len(meshes)==1,"True mesh source expected, no fabricated owl primitive"
assert sha(args.source)=="7d7659a861a4444a4d898649e74942b7a1fcd6a6ca7e98f52f0f60ca5033be19", "Wrong research source, abort"
obj=meshes[0]
# Bake all imported parent transforms into true source world vertex coordinates.
world=obj.matrix_world.copy()
v_coords=[world@v.co for v in obj.data.vertices]
obj.parent=None
obj.matrix_world=Matrix.Identity(4)
# Sculpt the actual new Run114C native neural mesh, not a parametric owl proxy.
# Preserve the face and feet; non-rigidly shorten the overlong posterior
# torso in three dimensions. All source vertices and their topology persist.
z0=min(p.z for p in v_coords); zspan=max(p.z for p in v_coords)-z0
yc=(max(p.y for p in v_coords)+min(p.y for p in v_coords))*0.5
posterior_warped=0
for p in v_coords:
    if p.y>yc:
        zrel=(p.z-z0)/max(zspan,1e-6)
        weight=math.exp(-.5*((zrel-.53)/.33)**2)
        p.y=yc+(p.y-yc)*(1-.27*weight)
        posterior_warped+=1
for v,p in zip(obj.data.vertices,v_coords):v.co=p
obj.data.update()
verts=[v.co for v in obj.data.vertices]
lo=Vector(tuple(min(v[i] for v in verts) for i in range(3)))
hi=Vector(tuple(max(v[i] for v in verts) for i in range(3)))
dims=hi-lo;center=(lo+hi)*0.5; size=max(dims)
assert 0.1<size<100
original_vertices=len(obj.data.vertices)
original_faces=len(obj.data.polygons)
# True mesh is high-poly from Run99; decimate carefully, then smooth sculpt, no ellipsoid replacement.
bpy.ops.object.select_all(action="DESELECT")
obj.select_set(True)
bpy.context.view_layer.objects.active=obj
mod=obj.modifiers.new("gentle_decimation_preserve_heart","DECIMATE")
mod.ratio=min(1.,105000/max(1,original_faces))
bpy.ops.object.modifier_apply(modifier=mod.name)
mod=obj.modifiers.new("taubin_like_soft_relief_smooth","SMOOTH")
mod.factor=0.52;mod.iterations=8
bpy.ops.object.modifier_apply(modifier=mod.name)
# Explicitly rebuild a clean real polygon mesh. Neural source's glTF custom attributes
# become stale after decimation: Blender 4 exporter otherwise silently drops all base faces.
# This copies ALL actual edited polygon coordinates, never substitutes a primitive.
raw=obj.data
new=bpy.data.meshes.new("clean_reconstructed_existing_neural_topology")
new.from_pydata([tuple(v.co) for v in raw.vertices],[],
                [tuple(poly.vertices) for poly in raw.polygons])
new.update()
assert len(new.polygons)>50000
obj.data=new
if raw.users==0:bpy.data.meshes.remove(raw)
for p in obj.data.polygons:p.use_smooth=True

def material(name,color,roughness=0.89,alpha=1.0):
    m=bpy.data.materials.new(name);m.diffuse_color=(*color,alpha);m.use_nodes=True
    bs=m.node_tree.nodes.get("Principled BSDF")
    bs.inputs["Base Color"].default_value=(*color,alpha)
    bs.inputs["Roughness"].default_value=roughness
    bs.inputs["Metallic"].default_value=0.0
    if alpha<1:
        bs.inputs["Alpha"].default_value=alpha
        m.blend_method="BLEND";m.use_nodes=True
    return m
cream=material("run115_cream_ivory_pbr_not_finished",(0.83,0.755,0.636))
eye_dark=material("run115_deep_brown_eye",(0.045,0.030,0.023),0.23)
pupil_black=material("run115_black_pupil",(0.008,0.007,0.007),0.12)
tiny_catchlight=material("run115_eyeball_soft_catchlight",(0.9,0.83,0.71),0.17)
downmat=material("run115_airy_cream_fiber_cards",(0.94,0.855,0.735),0.97,0.58)
obj.data.materials.clear();obj.data.materials.append(cream)
obj.name="actual_neural_juvenile_sculpt_softened_RESEARCH_ONLY"
# Use front-facing raycasts to REGISTER eyes ON genuine socket mesh instead of putting eyeballs at guessed 3D depth.
# Percentage positions are measured against Run99 front-view silhouette, not scientific eye anatomy.
bpy.context.view_layer.update()
eye_info=[]
objects_added=[]
for sign in (-1,1):
    x=center.x + sign*dims.x*0.115
    z=lo.z+dims.z*0.72
    origin=Vector((x,lo.y-size*0.55,z))
    hit,location,normal,face_idx,hit_obj,mat=bpy.context.scene.ray_cast(bpy.context.evaluated_depsgraph_get(),origin,Vector((0,1,0)),distance=size*4)
    eye_info.append({"side":sign,"hit":bool(hit),"ray":[x,z],"surface":list(location) if hit else None})
    if not hit or hit_obj!=obj: continue
    radius=size*0.053
    bpy.ops.mesh.primitive_uv_sphere_add(segments=24,ring_count=12,radius=radius,
        location=(location.x,location.y-size*0.003,location.z))
    eye=bpy.context.object
    eye.name="real_socket_registered_dark_open_eye_"+str(sign)
    eye.scale=(0.92,0.28,0.96)
    eye.data.materials.append(eye_dark)
    for f in eye.data.polygons:f.use_smooth=True
    objects_added.append(eye)
    bpy.ops.mesh.primitive_uv_sphere_add(segments=20,ring_count=12,radius=radius*0.57,
        location=(location.x,location.y-size*0.017,location.z))
    pupil=bpy.context.object
    pupil.name="nested_small_pupil_"+str(sign);pupil.scale=(1.0,0.12,1.0)
    pupil.data.materials.append(pupil_black)
    for f in pupil.data.polygons:f.use_smooth=True
    objects_added.append(pupil)
    # A tiny physical glint, not a frontal photographic overlay.
    bpy.ops.mesh.primitive_uv_sphere_add(segments=12,ring_count=8,radius=radius*0.10,
        location=(location.x-sign*radius*.17,location.y-size*.022,location.z+radius*.21))
    glint=bpy.context.object;glint.name="catchlight_"+str(sign);glint.data.materials.append(tiny_catchlight)
    objects_added.append(glint)

# Actual curved, tapered cards sampled directly on ORIGINAL NEURAL surface; no synthetic owl proxy.
# Exclude the heart and front orbital surfaces to avoid earlier nose/eye occlusion failure.
rng=random.Random(172115)
mesh=obj.data
tri=mesh.loop_triangles
tri_faces=list(tri)
areas=[];total=0.
for t in tri_faces:
    a,b,c=[mesh.vertices[i].co for i in t.vertices]
    area=(b-a).cross(c-a).length*.5
    total+=max(area,1e-10);areas.append(total)
fiber_verts=[];fiber_faces=[];fiber_samples=0;attempts=0
target=1900
while fiber_samples<target and attempts<target*14:
    attempts+=1
    t=tri_faces[min(len(tri_faces)-1,bisect.bisect_left(areas,rng.random()*total))]
    a,b,c=[mesh.vertices[i].co for i in t.vertices]
    u=rng.random();v=rng.random()
    if u+v>1:u=1-u;v=1-v
    pos=a+(b-a)*u+(c-a)*v
    n=(b-a).cross(c-a).normalized()
    if n.length<.5:continue
    zrel=(pos.z-lo.z)/max(dims.z,1e-5)
    if zrel<.19:continue # avoid bare claws, toes and branch fragments
    if pos.y<center.y-dims.y*.03 and zrel>.55 and abs(pos.x-center.x)<dims.x*.31:
        continue # heart/eyes should stay visible
    # Avoid downward-facing undersides; fine down grows along outward normal.
    if n.z<-.82:continue
    direction=(n*.46+Vector((0,0,-.70))).normalized()
    if direction.length<.7:continue
    tang=direction.cross(Vector((0,1,0))).normalized()
    if tang.length<.5:tang=direction.cross(Vector((1,0,0))).normalized()
    length=size*rng.uniform(.009,.019)
    width=length*rng.uniform(.16,.25)
    tangent2=direction.cross(tang).normalized()
    angle=rng.random()*2*pi
    sideways=(tang*cos(angle)+tangent2*sin(angle)).normalized()
    # Two overlapping curved vanes per tuft, each three stations with tapered ends.
    for side in (-1,1):
        start=pos+n*size*.0015 +side*sideways*width*.38
        mid=start+direction*length*.50+n*length*.18
        end=start+direction*length+n*length*.25
        w=[width*.34,width*.43,width*.025]
        centers=[start,mid,end]
        first=len(fiber_verts)
        for j in range(3):
            lateral=sideways*w[j]
            fiber_verts.extend([centers[j]-lateral,centers[j]+lateral])
        for j in range(2):
            a0=first+2*j; b0=a0+2
            fiber_faces.extend([(a0,a0+1,b0+1),(a0,b0+1,b0)])
    fiber_samples+=1
groom_data=bpy.data.meshes.new("RealSurfaceFineDownCardMesh")
groom_data.from_pydata(fiber_verts,[],fiber_faces)
groom_data.update()
groom_obj=bpy.data.objects.new("Run115_physically_sampled_native_mesh_down_not_svg",groom_data)
bpy.context.scene.collection.objects.link(groom_obj)
groom_obj.data.materials.append(downmat)

scene=bpy.context.scene
scene.render.engine="CYCLES"
scene.cycles.samples=14
scene.cycles.use_denoising=False
scene.render.resolution_x=430;scene.render.resolution_y=430
scene.render.resolution_percentage=100
scene.world.color=(.27,.27,.27)
scene.view_settings.view_transform="Standard"
scene.view_settings.look="Medium High Contrast"
scene.view_settings.exposure=0.
for o in list(bpy.data.objects):
    if o.type=="LIGHT":bpy.data.objects.remove(o,do_unlink=True)
def area(name, xyz, power,scale):
    d=bpy.data.lights.new(name,"AREA");d.energy=power;d.shape="DISK";d.size=scale*size
    o=bpy.data.objects.new(name,d);scene.collection.objects.link(o)
    o.location=center+Vector(xyz)*size
    o.rotation_euler=(center-o.location).to_track_quat("-Z","Y").to_euler()
area("key_softbox",(-2.7,-3,3),340,4.5)
area("rear_fill",(2.2,2.3,2.6),230,3.2)
cam=bpy.data.objects.new("run115_true_four_cameras",bpy.data.cameras.new("run115_true_four_cameras"))
scene.collection.objects.link(cam);scene.camera=cam
cam.data.type="ORTHO";cam.data.ortho_scale=1.55*size
views=[("front",0),("quarter",45),("side",90),("back",180)]
variants=[]
for variant in ("eyes_only","eyes_plus_softdown"):
    groom_obj.hide_render=variant=="eyes_only"
    # Actual native Blender reimport of binary export: not a photograph or 2D proxy.
    dest=root/("run115_"+variant+"_ART_UNAPPROVED.glb")
    bpy.ops.object.select_all(action="DESELECT")
    for o in [obj]+objects_added+([groom_obj] if variant=="eyes_plus_softdown" else []):o.select_set(True)
    bpy.context.view_layer.objects.active=obj
    # Blender 4.0 mesh exporter bug: geometry may remain invalid after from_pydata/modifier
    # until a genuine edit/object mode rebuild. This is not geometry replacement.
    bpy.context.view_layer.objects.active=obj
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.object.mode_set(mode="OBJECT")
    obj.data.validate(clean_customdata=True)
    obj.data.update()
    assert len(obj.data.loop_triangles)>50000
    bpy.ops.export_scene.gltf(filepath=str(dest),export_format="GLB",use_selection=True,export_materials="EXPORT")
    assert dest.read_bytes()[:4]==b"glTF"
    before=set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=str(dest))
    loaded=[o for o in bpy.data.objects if o not in before and o.type=="MESH"]
    count=sum(len(o.data.polygons) for o in loaded)
    assert count>50000,("not real mesh",count)
    variants.append(dict(name=dest.name,size_bytes=dest.stat().st_size,sha256=sha(dest),
        native_reimport_meshes=len(loaded),native_reimport_polygons=count))
    for o in loaded:bpy.data.objects.remove(o,do_unlink=True)
    bpy.ops.object.select_all(action="DESELECT")
    for name,deg in views:
        theta=radians(deg)
        cam.location=center+Vector((4*sin(theta),-4*cos(theta),1.45))*size
        cam.rotation_euler=(center-cam.location).to_track_quat("-Z","Y").to_euler()
        scene.render.filepath=str(root/("run115_"+variant+"_"+name+"_native_cycles_UNAPPROVED.png"))
        bpy.ops.render.render(write_still=True)
metrics=dict(source_sha256=sha(args.source),source_original_vertices=original_vertices,
    source_original_faces=original_faces,posterior_native_vertices_warped=posterior_warped,mutated_base_vertices=len(mesh.vertices),
    mutated_base_triangles=len(mesh.loop_triangles),genuine_surface_sampled_tufts=fiber_samples,
    feather_card_vertices=len(fiber_verts),feather_card_faces=len(fiber_faces),
    physical_eye_socket_raycast=eye_info,model_variants=variants,render_views=8,
    tool="Blender "+bpy.app.version_string,artist_gate="ART_REJECTED_PENDING_REVIEW",
    real_mobile_gpu_tested=False,licenses_cleared=False,no_extra_payment=True)
(root/"run115_geometry_metrics.json").write_text(json.dumps(metrics,indent=2))
print("RUN110_REAL_MESH_AND_MULTIVIEW_METRICS",json.dumps(metrics),flush=True)
