#!/usr/bin/env python3
"""Run113: actual third-party CC0 owl 3D asset ingestion + native Blender mobile LOD.
Source is an adult great horned owl (NOT Tyto, NOT a juvenile). This is a
rights/provenance, topology and PBR pipeline benchmark only. ART_REJECTED always.
Never overwrite owl-pet prototype, 251-species producer or original #172 image.
"""
import argparse
import bpy
import hashlib
import json
import math
import pathlib
import struct
import sys
from mathutils import Vector

p=argparse.ArgumentParser()
p.add_argument("--source",required=True)
p.add_argument("--out",required=True)
p.add_argument("--manifest",required=True)
p.add_argument("--license",required=True)
args=p.parse_args(sys.argv[sys.argv.index("--")+1:])
src=pathlib.Path(args.source)
dest=pathlib.Path(args.out)
dest.mkdir(parents=True,exist_ok=True)
def digest(f):
    h=hashlib.sha256()
    with open(f,"rb") as inp:
        for chunk in iter(lambda:inp.read(1048576),b""):h.update(chunk)
    return h.hexdigest()
head=src.open("rb").read(12)
assert len(head)==12 and head[:4]==b"glTF", "Not a real GLB"
glb_len=struct.unpack("<I",head[8:12])[0]
assert glb_len==src.stat().st_size,(glb_len,src.stat().st_size)
manifest=json.loads(pathlib.Path(args.manifest).read_text())
expected=manifest["files"]["glb_light"]["bytes"]
assert src.stat().st_size==expected,(src.stat().st_size,expected)
license_text=pathlib.Path(args.license).read_text()
assert "CC0 1.0" in license_text and "AI-assisted" in license_text
scene=bpy.context.scene
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=str(src))
parts=[o for o in bpy.context.scene.objects if o.type=="MESH"]
assert parts, "No real mesh in source"
def faces(objects):
    return sum(max(0,len(f.vertices)-2) for o in objects for f in o.data.polygons)
def bounds(objects):
    points=[o.matrix_world@Vector(v) for o in objects for v in o.bound_box]
    return (Vector(tuple(min(q[i] for q in points) for i in range(3))),
            Vector(tuple(max(q[i] for q in points) for i in range(3))))
original_faces=faces(parts)
assert original_faces>10000,(original_faces,"source too small")
original_bounds=bounds(parts)
mats=len({mat.name for o in parts for mat in o.data.materials if mat})
images=[{"name":img.name,"w":img.size[0],"h":img.size[1]} for img in bpy.data.images
        if img.size[0]>0 and img.size[1]>0]
scene.render.engine="CYCLES"
scene.cycles.samples=12
scene.cycles.use_denoising=False
scene.render.resolution_x=440
scene.render.resolution_y=440
scene.render.resolution_percentage=100
scene.view_settings.view_transform="Standard"
scene.view_settings.look="Medium High Contrast"
scene.view_settings.exposure=-0.15
scene.world.color=(.22,.22,.22)
camera=bpy.data.objects.new("RUN113_ACTUAL_SOURCE_ORBIT",bpy.data.cameras.new("RUN113_ACTUAL_SOURCE_ORBIT"))
scene.collection.objects.link(camera)
scene.camera=camera
camera.data.type="ORTHO"
def make_light(name,energy):
    data=bpy.data.lights.new(name,"AREA")
    data.energy=energy
    data.shape="DISK"
    ob=bpy.data.objects.new(name,data)
    scene.collection.objects.link(ob)
    return ob
key=make_light("source_key",350)
fill=make_light("source_fill",200)
def four_views(stage,objects):
    lo,hi=bounds(objects)
    c=(lo+hi)*.5
    size=max(hi-lo)
    assert size>0
    camera.data.ortho_scale=size*1.55
    for lamp,offset,mult in [(key,Vector((-2.2,-3.2,2.5)),3.8),
                             (fill,Vector((2.5,2.0,2.5)),3.0)]:
        lamp.location=c+offset*size
        lamp.rotation_euler=(c-lamp.location).to_track_quat("-Z","Y").to_euler()
        lamp.data.size=size*mult
    outputs=[]
    for label,angle in (("orbit000",0),("orbit090",90),("orbit180",180),("orbit270",270)):
        a=math.radians(angle)
        camera.location=c+Vector((4*math.sin(a),-4*math.cos(a),1.2))*size
        camera.rotation_euler=(c-camera.location).to_track_quat("-Z","Y").to_euler()
        f=dest/("run113_"+stage+"_"+label+"_ACTUAL_3D.png")
        scene.render.filepath=str(f)
        bpy.ops.render.render(write_still=True)
        assert f.is_file() and f.stat().st_size>5000
        outputs.append(f.name)
    return outputs
source_renders=four_views("cc0_adult_source",parts)
# Real mesh decimation only, no fake sphere, no SVG, no unrelated surrogate owl.
# Keep small separated submeshes intact; preserve UV/materials where possible.
per_mesh=[]
for o in sorted(parts,key=lambda o:len(o.data.polygons),reverse=True):
    before=faces([o])
    if before>=3000:
        ratio=.23 if before>20000 else .45
        bpy.context.view_layer.objects.active=o
        bpy.ops.object.select_all(action="DESELECT")
        o.select_set(True)
        modifier=o.modifiers.new("RUN113_LOD_real_geometry","DECIMATE")
        modifier.ratio=ratio
        bpy.ops.object.modifier_apply(modifier=modifier.name)
    after=faces([o])
    per_mesh.append({"object":o.name,"triangles_before":before,"triangles_after":after})
lod_faces=faces(parts)
assert 10000<lod_faces<original_faces,{"src":original_faces,"lod":lod_faces}
bpy.ops.object.select_all(action="DESELECT")
for o in parts:o.select_set(True)
bpy.context.view_layer.objects.active=parts[0]
glb=dest/"run113_cc0_adult_anatomy_LOD_NOT_A_JUVENILE_ART_REJECTED.glb"
bpy.ops.export_scene.gltf(filepath=str(glb),export_format="GLB",use_selection=True,
                          export_materials="EXPORT")
assert glb.open("rb").read(4)==b"glTF"
existing=set(bpy.context.scene.objects)
bpy.ops.import_scene.gltf(filepath=str(glb))
reimported=[o for o in bpy.context.scene.objects if o not in existing and o.type=="MESH"]
assert reimported and faces(reimported)==lod_faces,(faces(reimported),lod_faces)
for ob in reimported:bpy.data.objects.remove(ob,do_unlink=True)
lod_renders=four_views("cc0_adult_lod",parts)
report={
 "run":"113",
 "result":"ART_REJECTED",
 "source_url":"https://grab3d.com/dl/owl/owl-light.glb",
 "license_url":"https://grab3d.com/dl/owl/LICENSE.txt",
 "manifest_url":"https://grab3d.com/dl/owl/manifest.json",
 "source_license_claim":"CC0 1.0; origin AI-assisted Meshy claimed by distributor; upstream rights not separately verified",
 "source_subject":"ADULT great horned owl with ear tufts; NOT Tyto castanops juvenile",
 "source_glb_bytes":src.stat().st_size,
 "source_sha256":digest(src),
 "native_blender":bpy.app.version_string,
 "original_triangle_count":original_faces,
 "original_mesh_parts":len(parts),
 "original_materials":mats,
 "original_texture_images":images,
 "original_bounds_m":[list(original_bounds[0]),list(original_bounds[1])],
 "lod_triangle_count":lod_faces,
 "lod_glb_bytes":glb.stat().st_size,
 "lod_sha256":digest(glb),
 "lod_reimport_triangles":faces(parts),
 "lod_mesh_parts":len(parts),
 "part_reductions":per_mesh,
 "native_cycles_render_source":source_renders,
 "native_cycles_render_lod":lod_renders,
 "actual_phone_gpu_tested":False,
 "art_approved":False,
 "why_rejected":"Wrong species/age/morphology: adult horned owl ear tufts, adult full wing/tail, no cream mesoptile down, no Tyto heart facial disc or eucalypt hollow support. Source is benchmark only; no design claims.",
 "next":"Use evidence to assess a truly juvenile Tyto rights-cleared sculpture, not as a final pet or production asset."
}
(dest/"run113_actual_source_and_LOD_metrics.json").write_text(json.dumps(report,indent=2,ensure_ascii=False))
print("RUN113_ACTUAL_SOURCE_AND_LOD",json.dumps(report,ensure_ascii=False),flush=True)
