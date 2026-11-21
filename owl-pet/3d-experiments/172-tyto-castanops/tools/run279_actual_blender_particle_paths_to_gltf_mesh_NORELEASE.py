"""#172 Run279. Convert actual Run278 Blender particle-hair paths into native glTF-compatible ribbons.
A *technical*, noncommercial research experiment: not a finished or accepted 3D pet.
Never touch species-production or the old WebGL prototype. No external paid services.
"""
import bpy, math, os, json, hashlib, traceback
from pathlib import Path
from mathutils import Vector

OUT=Path(os.environ.get("OWL172_OUT", "/tmp/owl172-run279"))
SOURCE=Path(os.environ["OWL172_BLEND_INPUT"])
OUT.mkdir(parents=True,exist_ok=True)
sha=lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
report={"run":279,"source":str(SOURCE),"source_sha256":sha(SOURCE),
        "source_rights":"HUNYUAN_NONCOMMERCIAL_ONLY",
        "aesthetic":"UNREVIEWED_NO_RELEASE","phone":"UNTESTED",
        "status":"EXPERIMENT_FAILED_NO_RELEASE"}
try:
    bpy.ops.wm.open_mainfile(filepath=str(SOURCE))
    meshes=[obj for obj in bpy.data.objects if obj.type=="MESH"]
    base=max(meshes,key=lambda obj:len(obj.data.polygons))
    assert len(base.particle_systems)>0,"Original Blender hair groom absent"
    bpy.context.view_layer.objects.active=base
    bpy.context.view_layer.update()
    sys=base.particle_systems[0]
    dep=bpy.context.evaluated_depsgraph_get()
    dep.update()
    eval_base=base.evaluated_get(dep)
    eval_ps=eval_base.particle_systems[0]
    print("RUN279 source particles",len(sys.particles),"evaluated",len(eval_ps.particles),flush=True)
    verts=[Vector(v.co) for v in base.data.vertices]
    low=Vector(tuple(min(v[i] for v in verts) for i in range(3)))
    high=Vector(tuple(max(v[i] for v in verts) for i in range(3)))
    center=(low+high)*0.5
    diag=(high-low).length
    report["donor_mesh"]={"vertices":len(verts),"faces":len(base.data.polygons),
      "bounds_min":list(low),"bounds_max":list(high),"diag":diag}
    assert diag>0 and len(verts)>10000
    # Extract *actual simulated/artist generated hair trajectories*, do not invent a new
    # sphere, fur cloud, or a rotating silhouette image. Convert paths to true glTF mesh.
    samples=[]
    hist=[]
    collection=eval_ps.particles if len(eval_ps.particles)>0 else sys.particles
    for i,part in enumerate(collection):
        hk=part.hair_keys
        if len(hk)<3: continue
        coords=[Vector(key.co) for key in hk]
        if i<4: hist.append({"index":i,"keys":len(hk),
              "first":list(coords[0]),"last":list(coords[-1])})
        # Use four sub-sampled actual hair trajectory points.
        pts=[coords[round((len(coords)-1)*j/3)] for j in range(4)]
        span=(pts[-1]-pts[0]).length
        if span<diag*0.00015 or span>diag*0.55:continue
        if any(not math.isfinite(x) for p in pts for x in p):continue
        samples.append(pts)
    report["particle_data"]={"count":len(collection),"valid_trajectories":len(samples),"examples":hist}
    assert len(samples)>2200,"Particle path extraction failed, do not substitute random geometry"
    within=sum(1 for pts in samples if all(low[k]-diag*0.25<=pts[0][k]<=high[k]+diag*0.25 for k in range(3)))
    report["particle_data"]["roots_near_source_fraction"]=within/len(samples)
    assert within/len(samples)>0.90,"Hair paths do not share source mesh coordinates; fail closed"
    # Build narrow 3D ribbons following extracted real hair paths, with 3 tapering
    # intervals and physically distinct spatial orientation. This is genuine mesh
    # export research, not an art-release claim; strips may appear harsh.
    mat=bpy.data.materials.new("warm_cream_down_paths_TRUE_GLTFRIBBON_NO_RELEASE")
    mat.diffuse_color=(0.94,0.89,0.79,1)
    mat.use_nodes=True
    principled=mat.node_tree.nodes.get("Principled BSDF")
    if principled:
        principled.inputs["Base Color"].default_value=(0.94,0.89,0.79,1)
        principled.inputs["Roughness"].default_value=0.88
    def make_cards(count,tag):
        positions=[];faces=[]
        step=max(1,len(samples)//count)
        chosen=samples[::step][:count]
        for idx,pts in enumerate(chosen):
            tang=(pts[-1]-pts[0]).normalized()
            ref=Vector((0,0,1))
            if abs(tang.dot(ref))>0.85:ref=Vector((1,0,0))
            side=tang.cross(ref).normalized()
            width=diag*0.0014
            vstart=len(positions)
            for j,p in enumerate(pts):
                shape=max(0.09,(1-j/3)**1.25)
                positions.extend([p-side*width*shape,p+side*width*shape])
            for k in range(3):
                a=vstart+2*k
                faces.extend([(a,a+1,a+2),(a+1,a+3,a+2)])
        mesh=bpy.data.meshes.new(tag+"_authentic_particle_strand_mesh")
        mesh.from_pydata(positions,[],faces)
        mesh.update()
        ob=bpy.data.objects.new(tag+"_gltf_strand_matte_mesh",mesh)
        bpy.context.scene.collection.objects.link(ob)
        mesh.materials.append(mat)
        return ob,len(chosen)
    # Disable true renderer-only particle hair while exporting ribbons.
    # Both variants retain original organic donor body.
    bpy.ops.object.select_all(action="DESELECT")
    base.select_set(True)
    bpy.context.view_layer.objects.active=base
    bpy.ops.object.particle_system_remove()
    report["native_path_to_geometry"]="Blender particle hair_keys -> curved tapered real triangle ribbons"
    results={}
    full,fcount=make_cards(3200,"run279_full")
    def export(name,body,fur):
        bpy.ops.object.select_all(action="DESELECT")
        body.select_set(True);fur.select_set(True)
        bpy.context.view_layer.objects.active=body
        path=OUT/name
        bpy.ops.export_scene.gltf(filepath=str(path),export_format="GLB",use_selection=True,
                                   export_normals=True,export_materials="EXPORT")
        assert path.exists() and path.stat().st_size>200000
        return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha(path),
                "fur_faces":len(fur.data.polygons),"body_faces":len(body.data.polygons)}
    results["full"]=export("run279_real_particle_hair_mesh_full_RESEARCH_NO_RELEASE.glb",base,full)
    bpy.data.objects.remove(full,do_unlink=True)
    # Create truly distinct lower-detail mobile candidate, not just a smaller GLB ZIP.
    bpy.ops.object.select_all(action="DESELECT")
    base.select_set(True);bpy.context.view_layer.objects.active=base
    mod=base.modifiers.new("research_mobile_continuous_mesh_decimation","DECIMATE")
    mod.ratio=0.42
    bpy.ops.object.modifier_apply(modifier=mod.name)
    lowfur,lcount=make_cards(1600,"run279_lod")
    results["mobile_candidate"]=export("run279_real_particle_hair_mesh_lod_RESEARCH_NO_RELEASE.glb",base,lowfur)
    report["mesh_exports"]=results
    report["extracted_groom_trajectories"]={"full":fcount,"lod":lcount}
    # Render actual mobile candidate using Blender pathtracer from four spatial cameras.
    scene=bpy.context.scene
    for obj in list(scene.objects):
        if obj.type=="LIGHT" or obj.type=="CAMERA":
            bpy.data.objects.remove(obj,do_unlink=True)
    scene.render.engine="CYCLES";scene.cycles.device="CPU";scene.cycles.samples=4
    scene.cycles.use_denoising=False
    for layer in scene.view_layers:
        if hasattr(layer,"cycles"):layer.cycles.use_denoising=False
    scene.render.resolution_x=420;scene.render.resolution_y=420
    scene.render.resolution_percentage=100
    scene.render.film_transparent=True
    world=bpy.data.worlds.new("run279_world")
    world.use_nodes=True
    world.node_tree.nodes["Background"].inputs["Strength"].default_value=0.65
    scene.world=world
    for name,xyz,energy in [("key",(-1.4,-1.6,2),700),("fill",(1.4,1.2,1.2),300)]:
        light=bpy.data.lights.new(name,"AREA")
        ob=bpy.data.objects.new(name,light)
        scene.collection.objects.link(ob)
        ob.location=center+Vector(xyz)*diag
        ob.rotation_euler=(center-ob.location).to_track_quat("-Z","Y").to_euler()
        light.energy=energy;light.shape="DISK";light.size=diag*2
    cdata=bpy.data.cameras.new("research_orthographic_camera")
    cam=bpy.data.objects.new("research_orthographic_camera",cdata)
    scene.collection.objects.link(cam);scene.camera=cam
    cdata.type="ORTHO";cdata.ortho_scale=diag*1.3
    scene.render.image_settings.file_format="PNG"
    shots=[]
    for degrees in (0,45,90,180):
        a=math.radians(degrees)
        cam.location=center+Vector((math.sin(a)*2.3,-math.cos(a)*2.3,0.5))*diag
        cam.rotation_euler=(center-cam.location).to_track_quat("-Z","Y").to_euler()
        dst=OUT/("run279_lod_true3d_azimuth_%03d.png"%degrees)
        scene.render.filepath=str(dst)
        bpy.ops.render.render(write_still=True)
        shots.append({"azimuth":degrees,"file":dst.name,"sha256":sha(dst),"bytes":dst.stat().st_size})
    report["native_rendered_views"]=shots
    bpy.ops.wm.save_as_mainfile(filepath=str(OUT/"run279_editable_true_particle_path_gltf_mesh_lod_NORELEASE.blend"))
    report["status"]="ACTUAL_GLTF_GROOM_MESH_EXPORTED_AND_RENDERED_ART_UNREVIEWED_NO_RELEASE"
except Exception as e:
    report["error"]=repr(e);report["traceback"]=traceback.format_exc()
    print("RUN279 FAILURE",traceback.format_exc(),flush=True)
    raise
finally:
    (OUT/"run279_machine_report.json").write_text(json.dumps(report,indent=2,default=str)+"\n")
    print("RUN279_MACHINE_REPORT",json.dumps(report,default=str),flush=True)
