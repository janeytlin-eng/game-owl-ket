#!/usr/bin/env python3
"""Blender Cycles native GLB/glTF COLOR_0 four-view validation for run101; NOT release."""
import bpy,sys,math,json,pathlib
from mathutils import Vector
a=sys.argv[sys.argv.index("--")+1:] if "--" in sys.argv else []
assert len(a)==2,"Blender -- FILE.glb OUT"
source,out=pathlib.Path(a[0]),pathlib.Path(a[1]);out.mkdir(parents=True,exist_ok=True)
bpy.ops.object.select_all(action="SELECT");bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=str(source))
objs=[o for o in bpy.context.scene.objects if o.type=="MESH"]
assert len(objs)==1 and len(objs[0].data.polygons)>79000
for o in objs:
    colors=o.data.color_attributes
    if not colors:raise RuntimeError("GLB has no imported COLOR_0: cannot claim colored PBR")
    material=bpy.data.materials.new("run101_embedded_real_mesh_COLOR_0")
    material.use_nodes=True
    nodes=material.node_tree.nodes
    shader=nodes.get("Principled BSDF")
    shader.inputs["Metallic"].default_value=0.0
    shader.inputs["Roughness"].default_value=.91
    color=nodes.new("ShaderNodeVertexColor")
    color.layer_name=colors[0].name
    material.node_tree.links.new(color.outputs["Color"],shader.inputs["Base Color"])
    o.data.materials.clear();o.data.materials.append(material)
    for poly in o.data.polygons:poly.use_smooth=True
bounds=[o.matrix_world@Vector(c) for o in objs for c in o.bound_box]
lo=Vector(tuple(min(p[i] for p in bounds) for i in range(3)))
hi=Vector(tuple(max(p[i] for p in bounds) for i in range(3)))
center=(lo+hi)*.5;scale=max(hi-lo)
scene=bpy.context.scene
scene.render.engine="CYCLES";scene.cycles.samples=16
scene.cycles.use_denoising=False
scene.render.resolution_x=448;scene.render.resolution_y=448
scene.render.resolution_percentage=100
scene.render.image_settings.file_format="PNG"
scene.render.film_transparent=False
scene.world.color=(.45,.45,.45)
scene.view_settings.view_transform="Standard"
scene.view_settings.look="Medium High Contrast"
def area(name,offset,power,size):
    data=bpy.data.lights.new(name,"AREA");data.energy=power;data.size=size*scale
    lamp=bpy.data.objects.new(name,data);scene.collection.objects.link(lamp)
    lamp.location=center+Vector(offset)*scale
    lamp.rotation_euler=(center-lamp.location).to_track_quat("-Z","Y").to_euler()
area("key",(-2.3,-3,3),450,4.0)
area("fill",(2,-2,1.5),155,3.4)
area("rim",(1.5,2,3),220,3.0)
camdata=bpy.data.cameras.new("run101_360deg_qa")
cam=bpy.data.objects.new("run101_360deg_qa",camdata)
scene.collection.objects.link(cam);scene.camera=cam
cam.data.type="ORTHO";cam.data.ortho_scale=1.62*scale
for name,deg in (("front",0),("quarter",45),("side",90),("back",180)):
    angle=math.radians(deg)
    cam.location=center+Vector((4*math.sin(angle),-4*math.cos(angle),1.3))*scale
    cam.rotation_euler=(center-cam.location).to_track_quat("-Z","Y").to_euler()
    scene.render.filepath=str(out/(name+"_native_cycles.png"))
    bpy.ops.render.render(write_still=True)
print("RUN101_NATIVE_3D",json.dumps({"source":source.name,"polygon_count":sum(len(o.data.polygons) for o in objs),"material_color_attribute":objs[0].data.color_attributes[0].name,"views":4}),flush=True)
