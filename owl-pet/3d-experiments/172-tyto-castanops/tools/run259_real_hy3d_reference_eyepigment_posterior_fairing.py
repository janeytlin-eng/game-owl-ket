#!/usr/bin/env python3
"""Run259 independent research-only experiment on real Run258p 20k triangle neural GLB.
Compare ORIGINAL native geometry with reference-derived color to the SAME geometry
with posterior-only mesh Laplacian smoothing. No fake 2-D turntable, primitive owl,
unlicensed source, extra API use or publication. Art must be separately reviewed.
"""
import bpy, hashlib, json, math, pathlib, struct, time
from mathutils import Vector

R=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
O=R/"research-evidence-run259-REAL-HY3D-PROJECTED-PIGMENT-POSTERIOR-ART_UNAPPROVED"
O.mkdir(parents=True,exist_ok=True)
SOURCE=O/"run259_from_run258p_actual_native.glb"
REF=R/"research-evidence-run117-FREE-TRELLIS-QUOTA-RECHECK-ART_REJECTED/rightmost_baby_owl_512_rgba.png"
PIN="4b74b8d045b50ad2075ccf262647824e06d1d51e440c7634c864651800a5541e"
REFPIN="e439928a9ef08d3be266106cb5f2766b6f5a9f2c414d44e8da55ba81732153b8"
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def clamp(x):return max(0.,min(1.,x))
assert SOURCE.is_file() and sha(SOURCE)==PIN,"Not exact real source GLB"
assert REF.is_file() and sha(REF)==REFPIN,"Not original far-right reference"
assert SOURCE.read_bytes()[:4]==b"glTF"
assert bpy.app.version >= (4,0,0)
data=json.loads(SOURCE.read_bytes()[20:20+struct.unpack_from("<I",SOURCE.read_bytes(),12)[0]])
assert sum(data["accessors"][p["indices"]]["count"]//3
           for m in data["meshes"] for p in m["primitives"])==20000

def xy_texture():
    image=bpy.data.images.load(str(REF.resolve()),check_existing=True)
    w,h=image.size
    raw=list(image.pixels[:])
    xvals=[];yvals=[]
    for y in range(h):
        for x in range(w):
            if raw[4*(y*w+x)+3]>.5:
                xvals.append(x);yvals.append(y)
    assert xvals and yvals
    crop=(min(xvals),min(yvals),max(xvals),max(yvals))
    def bilinear(x,y):
        x=clamp(x)*(crop[2]-crop[0])+crop[0]
        y=clamp(y)*(crop[3]-crop[1])+crop[1]
        ix=min(int(x),w-2);iy=min(int(y),h-2)
        dx=x-ix;dy=y-iy
        def pix(a,b):
            j=4*(b*w+a);return raw[j:j+4]
        p=[pix(ix,iy),pix(ix+1,iy),pix(ix,iy+1),pix(ix+1,iy+1)]
        return tuple((1-dy)*((1-dx)*p[0][k]+dx*p[1][k])+dy*((1-dx)*p[2][k]+dx*p[3][k]) for k in range(4))
    return bilinear,crop
def geometry_and_material(name,do_fair):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(SOURCE.resolve()))
    meshes=[v for v in bpy.context.scene.objects if v.type=="MESH"]
    assert len(meshes)==1 and len(meshes[0].data.polygons)==20000
    ob=meshes[0]
    bpy.ops.object.select_all(action="DESELECT");ob.select_set(True)
    bpy.context.view_layer.objects.active=ob
    ob.data.update()
    old=[v.co.copy() for v in ob.data.vertices]
    wverts=[ob.matrix_world@v.co for v in ob.data.vertices]
    bot=Vector(tuple(min(p[i] for p in wverts) for i in range(3)))
    top=Vector(tuple(max(p[i] for p in wverts) for i in range(3)))
    size=top-bot
    # Camera fronts are y-negative according to previous 4-view real Blender QA.
    # Vertex group affects only rear silhouette, never eyes, bill, heart disc or toes.
    if do_fair:
        vg=ob.vertex_groups.new(name="REAR_ONLY_LONG_SPINE_FAIRING")
        for v,p in zip(ob.data.vertices,wverts):
            d=clamp((p.y-(bot.y+.43*size.y))/(.40*size.y))
            # Deform mainly the back upper torso. Leave feet & forward face alone.
            z=clamp((p.z-(bot.z+.18*size.z))/(.35*size.z))
            weight=d*z
            if weight>.001:vg.add([v.index],weight,"REPLACE")
        mod=ob.modifiers.new("REAR_NATIVE_TRIANGLE_SURFACE_SMOOTH","SMOOTH")
        mod.factor=.67;mod.iterations=17;mod.vertex_group=vg.name
        bpy.ops.object.modifier_apply(modifier=mod.name)
    new=[v.co.copy() for v in ob.data.vertices]
    changed=sum(1 for a,b in zip(old,new) if (a-b).length>1e-5)
    maxmove=max((a-b).length for a,b in zip(old,new))
    for p in ob.data.polygons:p.use_smooth=True
    ob.data.update()
    interp,crop=xy_texture()
    attr=ob.data.color_attributes.new(name="OWL172_ORIGINAL_REFERENCE_PIGMENT",type="FLOAT_COLOR",domain="CORNER")
    lower=Vector(tuple(min((ob.matrix_world@v.co)[i] for v in ob.data.vertices) for i in range(3)))
    upper=Vector(tuple(max((ob.matrix_world@v.co)[i] for v in ob.data.vertices) for i in range(3)))
    extent=upper-lower
    front_count=0;dark_count=0
    for poly in ob.data.polygons:
        for li in poly.loop_indices:
            vert=ob.data.vertices[ob.data.loops[li].vertex_index]
            p=ob.matrix_world@vert.co
            # Individual vertex normal: true 3D front-facing geometry only.
            n=vert.normal
            frontal=clamp((-n.y-.08)/.62)
            u=clamp((p.x-lower.x)/max(extent.x,1e-6))
            v=clamp((p.z-lower.z)/max(extent.z,1e-6))
            rgba=interp(u,v)
            frontal*=clamp((rgba[3]-.18)/.55)
            if frontal>.3:front_count+=1
            cream=(.80+.055*math.sin(3.3*p.z),.773+.040*math.sin(3.0*p.x),.687+.020*math.sin(2.7*p.y))
            rawrgb=tuple(clamp((1-frontal)*cream[k]+frontal*rgba[k]) for k in range(3))
            if min(rawrgb)<.22:dark_count+=1
            # Image pixels and material color values are linear in Blender image buffers.
            attr.data[li].color=(*rawrgb,1.0)
    # Blender glTF exporter only exports vertex colors actually consumed by a material.
    mat=bpy.data.materials.new("Run259 source-projected actual mesh PBR - ART_UNAPPROVED")
    mat.use_nodes=True
    nodes=mat.node_tree.nodes
    nodes.clear()
    output=nodes.new("ShaderNodeOutputMaterial")
    bsdf=nodes.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Roughness"].default_value=.96
    bsdf.inputs["Metallic"].default_value=0.
    color=nodes.new("ShaderNodeVertexColor")
    color.layer_name=attr.name
    mat.node_tree.links.new(color.outputs["Color"],bsdf.inputs["Base Color"])
    mat.node_tree.links.new(bsdf.outputs["BSDF"],output.inputs["Surface"])
    ob.data.materials.clear();ob.data.materials.append(mat)
    dst=O/("run259_"+name+"_TRUE_NATIVE_REF_COLOR_ART_UNAPPROVED.glb")
    bpy.ops.export_scene.gltf(filepath=str(dst.resolve()),export_format="GLB",
        use_selection=True,export_normals=True,export_materials="EXPORT",export_apply=True)
    glb=dst.read_bytes()
    assert glb[:4]==b"glTF" and struct.unpack_from("<I",glb,8)[0]==len(glb)
    njson=struct.unpack_from("<I",glb,12)[0]
    gltf=json.loads(glb[20:20+njson])
    triangles=sum(gltf["accessors"][p["indices"]]["count"]//3
        for m in gltf["meshes"] for p in m["primitives"])
    assert triangles==20000
    has_color=all("COLOR_0" in p["attributes"] for m in gltf["meshes"] for p in m["primitives"])
    if not has_color:raise AssertionError("GLB did NOT export real COLOR_0 vertex pigment")
    if not all("NORMAL" in p["attributes"] for m in gltf["meshes"] for p in m["primitives"]):
        raise AssertionError("GLB normal attributes missing")
    return dict(variant=name,source_sha256=PIN,reference_sha256=REFPIN,
        reference_alpha_crop_bottom_up=list(crop),face_direction="Y-negative",
        original_triangles=20000,export_triangles=triangles,mesh_count=len(gltf["meshes"]),
        native_color_attributes=has_color,actual_painted_corners=front_count,
        dark_pigment_corners=dark_count,vertex_count=len(new),
        modified_real_vertices=changed,max_vertex_change=float(maxmove),
        output_file=dst.name,output_bytes=len(glb),output_sha256=sha(dst))
def real_views(record):
    name=record["variant"]
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str((O/record["output_file"]).resolve()))
    m=[o for o in bpy.context.scene.objects if o.type=="MESH"]
    assert m and sum(len(o.data.polygons) for o in m)==20000
    pts=[o.matrix_world@Vector(v) for o in m for v in o.bound_box]
    lower=Vector(tuple(min(p[i] for p in pts) for i in range(3)))
    upper=Vector(tuple(max(p[i] for p in pts) for i in range(3)))
    center=(lower+upper)*.5
    ext=max(upper-lower)
    scene=bpy.context.scene
    scene.render.engine="CYCLES";scene.cycles.samples=16
    scene.render.resolution_x=450;scene.render.resolution_y=450
    scene.render.resolution_percentage=100
    scene.render.film_transparent=False
    scene.world.color=(.50,.50,.50)
    def light(pos,power):
        data=bpy.data.lights.new("Run259 light","AREA")
        data.energy=power;data.size=ext*3.
        obj=bpy.data.objects.new("Run259 light",data)
        scene.collection.objects.link(obj)
        obj.location=center+Vector(pos)*ext
        obj.rotation_euler=(center-obj.location).to_track_quat("-Z","Y").to_euler()
    light((-3,-3,4),440);light((3,2,2),260)
    camera=bpy.data.objects.new("Run259 real camera",bpy.data.cameras.new("Run259 real camera"))
    scene.collection.objects.link(camera);scene.camera=camera
    camera.data.type="ORTHO";camera.data.ortho_scale=ext*1.70
    views=[]
    for label,deg in (("front",0),("quarter",45),("side",90),("back",180)):
        a=math.radians(deg)
        camera.location=center+Vector((4*math.sin(a),-4*math.cos(a),1.2))*ext
        camera.rotation_euler=(center-camera.location).to_track_quat("-Z","Y").to_euler()
        fp=O/("run259_"+name+"_"+label+"_REAL_BLENDER_ART_UNAPPROVED.png")
        scene.render.filepath=str(fp)
        bpy.ops.render.render(write_still=True)
        views.append(dict(view=label,file=fp.name,sha256=sha(fp)))
    record["blender_true_orbit_views"]=views
    record["blender_reimport_triangles"]=sum(len(o.data.polygons) for o in m)
    return record

results=[]
for name,sm in (("A_reference_only",False),("B_posterior_smooth",True)):
    record=geometry_and_material(name,sm)
    record=real_views(record)
    results.append(record)
report=dict(run=259,run_started_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),
    actual_original_neural_3d=True,license_for_generated_model_cleared=False,
    user_authorized_paid_service=False,additional_external_payment_usd=0,
    original_reference=REF.name,input_provider_real_glb_sha256=PIN,
    source_model_triangles=20000,variants=results,
    geometry_artifact_only=True,physical_mobile_GPU_tested=False,
    color_from_source_is_not_3D_down=True,
    art_approved=False,release="NO_RELEASE",
    note="Source color projection cannot invent physical down. Rear smoothing cannot create natural anatomically correct chick wings. Independent visual review mandatory.")
(O/"run259_real_3d_machine_report.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
print("RUN259_TRUE_REAL_GEOMETRY_AND_PIGMENT_REPORT",json.dumps(report,ensure_ascii=False))
