"""Run182: actually import CC0 adult owl GLB into Blender and render 4 real camera orbits.
Native source is an adult Great Horned Owl and is NOT an acceptable #172 young owl.
"""
import bpy, pathlib, json, math, traceback
from mathutils import Vector
R=pathlib.Path(__file__).resolve().parent.parent
OUT=R/"research-evidence-run182-HIGHDETAIL-CC0-SOURCE-NO_RELEASE"
GLB=OUT/"grab3d_adult_horned_owl_light_UNAPPROVED.glb"
metrics={"run":182,"status":"BLENDER_NOT_STARTED","art":"NOT_APPROVED","release":False,"actual_phone_gpu":"NOT_TESTED"}
def save():
 (OUT/"run182_blender_metrics.json").write_text(json.dumps(metrics,indent=2))
try:
 if not GLB.is_file():raise RuntimeError("NO_ACTUAL_GLB_DOWNLOADED")
 bpy.ops.wm.read_factory_settings(use_empty=True)
 bpy.ops.import_scene.gltf(filepath=str(GLB))
 objects=[o for o in bpy.context.scene.objects if o.type=="MESH"]
 if not objects:raise RuntimeError("NO_IMPORTED_MESH")
 vert=sum(len(o.data.vertices) for o in objects)
 tris=sum(sum(len(p.vertices)-2 for p in o.data.polygons) for o in objects)
 coords=[o.matrix_world@Vector(v) for o in objects for v in o.bound_box]
 lo=Vector([min(p[i] for p in coords) for i in range(3)])
 hi=Vector([max(p[i] for p in coords) for i in range(3)])
 center=(lo+hi)/2
 extent=hi-lo
 max_dim=max(extent)
 metrics.update(import_status="GLTF_NATIVE_IMPORT_SUCCESS",mesh_objects=len(objects),
  vertices=vert,triangles=tris,bbox_world=list(extent),center_world=list(center))
 if tris<1000:raise RuntimeError("TRIVIAL_MESH_SOURCE")
 scene=bpy.context.scene
 opts={v.identifier for v in bpy.types.RenderSettings.bl_rna.properties["engine"].enum_items}
 if "BLENDER_EEVEE_NEXT" in opts:scene.render.engine="BLENDER_EEVEE_NEXT"
 elif "BLENDER_EEVEE" in opts:scene.render.engine="BLENDER_EEVEE"
 else:scene.render.engine="CYCLES"
 if scene.render.engine=="CYCLES":
  scene.cycles.samples=12
 scene.render.resolution_x=384
 scene.render.resolution_y=384
 scene.render.resolution_percentage=100
 scene.render.image_settings.file_format="PNG"
 scene.view_settings.view_transform="Standard"
 scene.render.film_transparent=False
 if scene.world is None:scene.world=bpy.data.worlds.new("soft neutral world")
 scene.world.use_nodes=True
 scene.world.node_tree.nodes.get("Background").inputs["Color"].default_value=(0.38,0.4,0.44,1)
 scene.world.node_tree.nodes.get("Background").inputs["Strength"].default_value=.75
 def area(name,location,energy,size):
  data=bpy.data.lights.new(name,"AREA");data.energy=energy;data.shape="DISK";data.size=size
  obj=bpy.data.objects.new(name,data);scene.collection.objects.link(obj)
  obj.location=center+Vector(location)*max_dim
  obj.rotation_euler=(center-obj.location).to_track_quat("-Z","Y").to_euler()
  return obj
 area("key",(2,-3,4),650,max_dim*4)
 area("fill",(-2,2,1.8),420,max_dim*3)
 camd=bpy.data.cameras.new("real_native_orbit")
 cam=bpy.data.objects.new("real_native_orbit",camd)
 scene.collection.objects.link(cam);scene.camera=cam
 camd.type="ORTHO"
 camd.ortho_scale=max_dim*1.65
 count=0
 for name,angle in [("axis_minusY",0),("axis_plusX",90),("axis_plusY",180),("axis_minusX",270)]:
  a=math.radians(angle)
  cam.location=center+Vector((math.sin(a)*max_dim*2.9,-math.cos(a)*max_dim*2.9,max_dim*.42))
  cam.rotation_euler=(center-cam.location).to_track_quat("-Z","Y").to_euler()
  scene.render.filepath=str(OUT/("run182_"+name+"_GENUINE_NATIVE_ADULT_NOT_TYTO.png"))
  bpy.ops.render.render(write_still=True)
  count+=1
 metrics["native_renders"]=count
 if count==4:
  bpy.ops.wm.save_as_mainfile(filepath=str(OUT/"run182_real_cc0_adult_donor_UNAPPROVED.blend"))
 metrics["status"]="NATIVE_ADULT_GLTF_FOUR_VIEWS_COMPLETE_NOT_JUVENILE"
except Exception as e:
 metrics["status"]="BLENDER_NATIVE_ERROR"
 metrics["error"]=repr(e)
 metrics["traceback"]=traceback.format_exc()[-4000:]
finally:
 metrics["release"]=False
 save()
 print("RUN182_BLENDER_FINAL",metrics["status"],metrics.get("triangles",0),metrics.get("native_renders",0),flush=True)
