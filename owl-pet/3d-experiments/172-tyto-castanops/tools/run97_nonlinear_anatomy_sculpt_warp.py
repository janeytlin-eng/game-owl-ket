#!/usr/bin/env python3
"""Run97 research-only NONLINEAR shape-control ablation over real Run96B 3D geometry.
Repositions each of the *existing* 220k-triangle model's 3D vertices with a smooth
measured-proportion field. It does NOT draw an impostor or assemble primitive
geometry. It does NOT imply artistic acceptance.
"""
import bpy,math,json,hashlib,sys
from pathlib import Path
from mathutils import Vector
args=sys.argv[sys.argv.index("--")+1:]
source,out,variant=args
out=Path(out);out.parent.mkdir(parents=True,exist_ok=True)
assert variant in ("mild","broad")
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=source)
objs=[o for o in bpy.context.scene.objects if o.type=="MESH"]
assert len(objs)>12, len(objs)
# Internal coordinates: after GLB import Y up, bird faces -Z as per source
# mesh source. Preserve the natural tree hollow prop (no scaling to fake fit).
def fld(y,loc=.99,spread=.65):
    return math.exp(-((y-loc)/spread)**2)
def warp(v):
    x,y,z=v
    belly=fld(y,1.34,.59)
    shoulder=fld(y,1.74,.36)
    h=fld(y,2.43,.46)
    # More rotund mesoptile compared with previous narrow upright pill:
    # all connected body, coat, toes and bill transform coherently in 3D.
    strength={"mild":.18,"broad":.33}[variant]
    x=x*(1+strength*belly+.045*shoulder-.05*h)
    z=z*(1+.10*belly)
    # Lower thorax compresses gently; head crown stays intact.
    s={"mild":.95,"broad":.89}[variant]
    if .52<y<2.00:
        t=math.sin(math.pi*(y-.52)/1.48)**2
        y+=-(1-s)*.34*t
    return Vector((x,y,z))
counter=0
bounds_before=[]
bounds_after=[]
moved_names=[]
for o in objs:
    n=o.name.lower()
    prop=( "lip" in n or "hollow" in n or "shadow" in n )
    if prop:continue
    m=o.matrix_world
    inv=m.inverted_safe()
    touched=0
    for v in o.data.vertices:
        p=m@v.co
        new=warp(p)
        if (new-p).length>1e-6:
            counter+=1;touched+=1
        v.co=inv@new
    if touched:moved_names.append({"object":o.name,"vertices":touched})
    o.data.update()
assert counter>40000,counter
bpy.ops.export_scene.gltf(filepath=str(out),export_format="GLB",
                           export_apply=True,export_colors=True)
assert out.exists() and out.stat().st_size>100000
# Round-trip the exported file in a new scene to ensure actual glTF data.
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(out))
imported=[o for o in bpy.context.scene.objects if o.type=="MESH"]
for o in imported:o.data.calc_loop_triangles()
tris=sum(len(o.data.loop_triangles) for o in imported)
assert tris>50000,(len(imported),tris)
metrics={
  "verdict":"PENDING_VISUAL_QA_NOT_APPROVED",
  "experiment":"nonrigid geometry sculpt warp over previously generated *real* 3D GLB",
  "source":"Run96B ART_REJECTED GLB from its isolated research branch",
  "variant":variant,
  "mesh_count":len(imported),"triangles":tris,
  "changed_vertices":counter,
  "byte_size":out.stat().st_size,
  "sha256":hashlib.sha256(out.read_bytes()).hexdigest(),
  "new_primitives_created":0,
  "real_mobile_gpu_benchmarked":False,
  "production_changed":False
}
(out.parent/(out.stem+"-metrics.json")).write_text(json.dumps(metrics,indent=2))
print("RUN97_TRUE_GLTF_REIMPORT_VERIFIED",json.dumps(metrics),flush=True)
