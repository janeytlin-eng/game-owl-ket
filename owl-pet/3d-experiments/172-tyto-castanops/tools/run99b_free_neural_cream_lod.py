#!/usr/bin/env python3
"""Run99B: real Hunyuan3D generated mesh -> separately archived cream-PBR mobile LOD tests.
NOT artist-approved; no procedural replacement of species art, no primitives or SVG.
Blender 4.x Python CLI: blender -b --python script.py -- SOURCE DEST
"""
import bpy,sys,json,pathlib,hashlib,math
from mathutils import Vector

def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
argv=sys.argv[sys.argv.index("--")+1:]
source,out=pathlib.Path(argv[0]),pathlib.Path(argv[1])
out.mkdir(parents=True,exist_ok=True)
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=str(source))
source_meshes=[o for o in bpy.context.scene.objects if o.type=="MESH"]
assert len(source_meshes)==1,[(o.name,o.type) for o in source_meshes]
original=source_meshes[0]
source_triangles=sum(len(poly.vertices)-2 for poly in original.data.polygons)
source_vertices=len(original.data.vertices)
metrics={"source_sha256":sha(source),"source_meshes":len(source_meshes),
    "original_triangles":source_triangles,"original_vertices":source_vertices,
    "variants":[],"rejected_default":True,
    "mobile_hardware_fps":"NOT_TESTED","source":"Run99 public anonymous Hunyuan3D-2 ZeroGPU"}
def make_pbr(name,color):
    mat=bpy.data.materials.new(name);mat.use_nodes=True
    nodes=mat.node_tree.nodes
    bsdf=nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value=(*color,1.0)
    bsdf.inputs["Metallic"].default_value=0
    bsdf.inputs["Roughness"].default_value=0.87
    bsdf.inputs["Specular IOR Level"].default_value=0.14
    return mat
cream=make_pbr("creamy_mesh_rough_pbr",(0.88,0.765,0.625))
for target in [72000,32000]:
    bpy.ops.object.select_all(action="DESELECT")
    bpy.context.view_layer.objects.active=original;original.select_set(True)
    obj=original.copy();obj.data=original.data.copy()
    bpy.context.scene.collection.objects.link(obj)
    obj.name=f"run99b_retopo_{target}_PBR_UNAPPROVED"
    bpy.ops.object.select_all(action="DESELECT")
    bpy.context.view_layer.objects.active=obj
    obj.select_set(True)
    d=obj.modifiers.new(f"decimate_to_{target}_faces","DECIMATE")
    d.decimate_type="COLLAPSE"
    d.ratio=min(1, target/source_triangles)
    d.use_collapse_triangulate=True
    bpy.ops.object.modifier_apply(modifier=d.name)
    obj.data.materials.clear()
    obj.data.materials.append(cream)
    for poly in obj.data.polygons:poly.material_index=0
    triangles=sum(len(f.vertices)-2 for f in obj.data.polygons)
    filename=f"run99b_cream_{target}_ART_UNAPPROVED.glb"
    destination=out/filename
    bpy.ops.export_scene.gltf(filepath=str(destination),export_format="GLB",
        use_selection=True,export_materials="EXPORT")
    # Validate by an actual Blender reimport of the generated GLB.
    obj.select_set(False)
    before={o.name for o in bpy.data.objects}
    bpy.ops.import_scene.gltf(filepath=str(destination))
    imported=[o for o in bpy.context.scene.objects if o.name not in before and o.type=="MESH"]
    imp_tris=sum(sum(len(poly.vertices)-2 for poly in o.data.polygons) for o in imported)
    imp_pbr=[m.name for o in imported for m in o.data.materials if m]
    assert imp_tris > 0 and 0 <= triangles - imp_tris <= max(25, int(triangles * 0.001)), (imp_tris,triangles) # Skip numerically degenerate post-decimation triangles, transparently report discrepancy.
    assert imported and imp_pbr
    metrics["variants"].append({"name":filename,"file_bytes":destination.stat().st_size,
        "sha256":sha(destination),"triangle_count":triangles,
        "vertices":len(obj.data.vertices),"reimport_triangles":imp_tris,"triangles_dropped_by_gltf_export":triangles-imp_tris,
        "reimport_materials":imp_pbr,"artist_gate":"UNAPPROVED"})
    for i in imported: bpy.data.objects.remove(i,do_unlink=True)
    bpy.data.objects.remove(obj,do_unlink=True)
(out/"run99b_mesh_metrics.json").write_text(json.dumps(metrics,indent=2))
print("RUN99B_LOD_REIMPORT_METRICS",json.dumps(metrics),flush=True)
