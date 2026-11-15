"""Run89 - RESEARCH ONLY. Bake a subset of Run88 real groom parent curves to
tapered GLB triangle ribbons and compare with native hair Cycles views.
The inherited adult horned owl anatomy is scientifically wrong for #172.
Never publish this artifact or call browser/mobile GPU pass.
"""
import bpy, sys, os, json, hashlib, math
from mathutils import Vector

src,out=sys.argv[sys.argv.index("--")+1:sys.argv.index("--")+3]
os.makedirs(out,exist_ok=True)
bpy.ops.wm.open_mainfile(filepath=src)
body=next(o for o in bpy.data.objects if o.type=="MESH" and o.particle_systems)
scene=bpy.context.scene
ps=body.particle_systems[0]
pm=next(m for m in body.modifiers if m.type=="PARTICLE_SYSTEM")
scene.frame_set(scene.frame_current)
dg=bpy.context.evaluated_depsgraph_get()
dg.update()
evaluated_body=body.evaluated_get(dg)
eval_ps=evaluated_body.particle_systems[0]
print("RUN89_PSYS_DIAG",ps.settings.type,ps.settings.count,
      "raw",len(ps.particles),"evaluated",len(eval_ps.particles),
      "child",len(eval_ps.child_particles),flush=True)
if len(ps.particles)<1000 and len(eval_ps.particles)>1000:
    ps=eval_ps
    body=evaluated_body
    pm=next(m for m in body.modifiers if m.type=="PARTICLE_SYSTEM")
assert ps.settings.type=="HAIR" and len(ps.particles)>1000, "No evaluated hair data"
assert len([o for o in bpy.data.objects if o.type=="MESH"])>40
bpy.context.view_layer.update()

# Sample native parent curves; do not replace them with imaginary radial spines.
# co_object returns object-space coordinates from the original particle modifier.
all_points=[]
root_diag=[]
for idx,p in enumerate(ps.particles):
    if idx%2: continue    # half-resolution first WebGL transfer test
    coords=[]
    for k in p.hair_keys:
        try:
            local=k.co_object(body,pm,p)
            v=body.matrix_world @ Vector(local)
        except Exception:
            v=body.matrix_world @ Vector(k.co)
        if all(math.isfinite(float(a)) for a in v):
            coords.append(v)
    if len(coords)<3 or (coords[-1]-coords[0]).length<0.0002:
        # Alternative documented particle-hair sampling; count fallback separately.
        coords=[]
        for j in range(0,17,4):
            try:
                v=Vector(ps.co_hair(body,idx,j))
                if all(math.isfinite(float(a)) for a in v): coords.append(v)
            except Exception: pass
    if len(coords)<3: continue
    length=(coords[-1]-coords[0]).length
    if not 0.00015<length<0.10: continue
    all_points.append(coords)
    root_diag.append((idx,round(length,6),len(coords)))
assert len(all_points)>250, "No valid hair guide curves; no fake GLB will be issued"
print("ACTUAL_NATIVE_GUIDE_SAMPLES",len(all_points),"examples",root_diag[:8],flush=True)

# Tapered fine ribbons are made from actual bent guide curves, not a new
# procedural owl silhouette. Alpha ribbons are only a portability ablation.
verts, faces, uvs=[],[],[]
for j,coords in enumerate(all_points):
    n=len(coords)
    for k,pt in enumerate(coords):
        prev=coords[max(0,k-1)]
        following=coords[min(n-1,k+1)]
        tang=(following-prev)
        if tang.length<1e-8: tang=Vector((0,0,1))
        tang.normalize()
        axis=Vector((0,0,1))
        if abs(tang.dot(axis))>.90: axis=Vector((0,1,0))
        side=tang.cross(axis).normalized()
        width=.00032*(max(.035,1-k/max(1,n-1))**.7)
        verts.extend([tuple(pt-side*width),tuple(pt+side*width)])
    start=len(verts)-2*n
    for k in range(n-1):
        a=start+2*k
        faces.extend([(a,a+1,a+2),(a+1,a+3,a+2)])
mesh=bpy.data.meshes.new("Run89BakedGuideRibbonsMesh")
mesh.from_pydata(verts,[],faces)
mesh.update()
fur=bpy.data.objects.new("Run89RealGuidesToMesh NOT APPROVED",mesh)
bpy.context.collection.objects.link(fur)
mat=bpy.data.materials.new("Run89 CreamDown Baked Alpha NOT APPROVED")
mat.use_nodes=True
mat.blend_method="BLEND"
mat.use_backface_culling=False
bs=next(n for n in mat.node_tree.nodes if n.type=="BSDF_PRINCIPLED")
bs.inputs["Base Color"].default_value=(.90,.79,.66,1)
bs.inputs["Roughness"].default_value=.93
bs.inputs["Alpha"].default_value=.78
mesh.materials.append(mat)
print("BAKED_RIBBONS",len(verts),len(faces),flush=True)

# Paired native hair and low-cost GLB ribbons, same camera/light/color.
scene.render.engine="CYCLES"
scene.cycles.samples=12
scene.render.resolution_x=420
scene.render.resolution_y=420
scene.render.resolution_percentage=100
scene.render.image_settings.file_format="PNG"
meshes=[o for o in bpy.data.objects if o.type=="MESH"]
worldpts=[o.matrix_world@v.co for o in meshes if o != fur for v in o.data.vertices[:2000]]
center=Vector(tuple((min(p[i] for p in worldpts)+max(p[i] for p in worldpts))/2 for i in range(3)))
cams=[("front",(2,0,.4)),("threequarter",(1.65,-1.5,.43)),("side",(0,-2,.37)),("back",(-2,0,.37))]
rendered=[]
for native in (True,False):
    pm.show_render=native
    pm.show_viewport=native
    fur.hide_render=native
    for name,pos in cams:
        scene.camera.location=center+Vector(pos)
        scene.camera.rotation_euler=(center-scene.camera.location).to_track_quat("-Z","Y").to_euler()
        fn=f"run89_{'native' if native else 'baked'}_{name}.png"
        scene.render.filepath=os.path.join(out,fn)
        bpy.ops.render.render(write_still=True)
        assert os.path.getsize(scene.render.filepath)>10000
        rendered.append(fn)
pm.show_render=False
pm.show_viewport=False
fur.hide_render=False
for o in bpy.data.objects: o.select_set(False)
for o in meshes: o.select_set(True)
bpy.context.view_layer.objects.active=fur
glb=os.path.join(out,"owl172_run89_real_guide_baked_GLTF_ART_REJECTED.glb")
bpy.ops.export_scene.gltf(filepath=glb,export_format="GLB",use_selection=True,
                          export_animations=False,export_apply=False)
assert os.path.getsize(glb)>1000000
glb_sha=hashlib.sha256(open(glb,"rb").read()).hexdigest()
# Actual fresh glTF re-import, not just a Blender render.
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=glb)
reimported=[o for o in bpy.data.objects if o.type=="MESH"]
fur_reimport=[o for o in reimported if "Run89RealGuides" in o.name]
assert fur_reimport and sum(len(o.data.polygons) for o in fur_reimport)>3000
metrics={
"decision":"ART_REJECTED_TEST_ONLY",
"source":"Run88B true Blender particle native hair atop Run87B wrong-adult-owl transfer",
"actual_native_guides_sampled":len(all_points),"baked_vertices":len(verts),
"baked_triangles":len(faces),"glb_bytes":os.path.getsize(glb),
"glb_sha256":glb_sha,"reimport_meshes":len(reimported),
"baked_mesh_reimport_triangles":sum(len(o.data.polygons) for o in fur_reimport),
"paired_native_and_exportable_cycles_views":rendered,
"true_mobile_GPU_test":False,"PBR_parity_test":False,"animation_test":False,
"species_and_infant_anatomy_quality_pass":False,"approved_release":False,
"no_payment":True
}
with open(os.path.join(out,"metrics.json"),"w") as f: json.dump(metrics,f,indent=2)
print("RUN89_GLTF_BAKED_NATIVE_GUIDES_BUT_ART_REJECTED",json.dumps(metrics),flush=True)
