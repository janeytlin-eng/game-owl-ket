#!/usr/bin/env python3
"""Run153: genuine Blender-native 3D sculpt/groom feasibility test; never a released owl pet.
All geometry is newly constructed here. No reused commercial model, third-party GLB,
reference image reproduction, or changes to 251-species production.
Requires Blender >=4.0, run: blender -b -t 2 --python this_file.py
"""
import bpy, math, random, json, os, hashlib, traceback
from mathutils import Vector
from math import sin, cos, pi
random.seed(172153)
OUT=os.environ.get("OWL153_OUT", "/tmp/owl172_run153")
os.makedirs(OUT, exist_ok=True)
scene=bpy.context.scene
bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
for data in bpy.data.materials: bpy.data.materials.remove(data)

def material(name, color, rough=0.85, subsurface=0.0):
    m=bpy.data.materials.new(name); m.diffuse_color=(*color,1)
    m.use_nodes=True; n=m.node_tree.nodes.get("Principled BSDF")
    n.inputs["Base Color"].default_value=(*color,1)
    n.inputs["Roughness"].default_value=rough
    n.inputs["Subsurface Weight"].default_value=subsurface
    return m
cream=material("warm creamy down - diffuse",(.88,.815,.685),.95,.08)
fluff=material("soft ivory down",(.96,.918,.80),.96)
fluff2=material("warm shaded fibre",(.81,.725,.58),.97)
face=material("pale heart mask",(.975,.909,.748),.93,.08)
face2=material("facial disc inset",(.90,.815,.675),.94)
rim=material("russet tan fine fringe",(.53,.34,.19),.97)
eye=material("glossy dark brown iris",(.014,.011,.008),.18)
catch=material("tiny eye catchlight",(.95,.93,.82),.1)
beakmat=material("warm horn bill",(.77,.62,.46),.46)
bark=material("eucalypt aged bark",(.29,.245,.19),.96)
bark2=material("sapwood hollow lip",(.49,.37,.24),.9)
hole=material("hollow internal shadow",(.07,.057,.043),.99)
toe=material("feathered tarsus",(.71,.62,.47),.85)

def uv(name, loc, scale, mat, seg=40, rings=24):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=seg,ring_count=rings,location=loc)
    o=bpy.context.object; o.name=name; o.scale=scale
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    o.data.materials.append(mat)
    bpy.ops.object.shade_smooth()
    return o

# Metaball -> fused and remeshed silhouette, not disconnected toy primitives.
mb=bpy.data.metaballs.new("mesoptile anatomical volume"); mb.resolution=.035; mb.render_resolution=.024
ob=bpy.data.objects.new("Anatomical sculpt initial volume",mb); scene.collection.objects.link(ob)
def metaball(x,y,z,r,scale):
    el=mb.elements.new("ELLIPSOID"); el.co=(x,y,z); el.radius=r
    el.size_x,el.size_y,el.size_z=scale
metaball(0,-.055,1.02,.88,(.79,.68,1.03))  # spherical, compact, crouched torso
metaball(0,.065,1.70,.70,(.81,.74,.77))    # disproportionately large head
metaball(-.42,-.10,.94,.44,(.58,.51,.94))   # down-buried short folded wing
metaball(.42,-.10,.94,.44,(.58,.51,.94))
bpy.context.view_layer.objects.active=ob
ob.select_set(True); bpy.ops.object.convert(target="MESH"); body=bpy.context.object
body.name="Run153 contiguous voxel juvenile clay sculpt"
body.data.materials.append(cream)
mod=body.modifiers.new("high quality smooth remesh","REMESH")
mod.mode="VOXEL"; mod.voxel_size=.021
bpy.ops.object.modifier_apply(modifier=mod.name)
sm=body.modifiers.new("surface fairing", "SMOOTH"); sm.factor=1.4;sm.iterations=5
bpy.ops.object.modifier_apply(modifier=sm.name)
bpy.ops.object.shade_smooth()
# Additional folded down-buried wing surface shape, no long remiges.
for sign in [-1,1]:
    o=uv("short buried wing volume "+str(sign),(sign*.45,-.055,.995),(.21,.31,.37),cream,48,32)
    o.rotation_euler[1]=sign*.18
# three-dimensional naturally curved heart facial disc (96 x 5 surface, not flat SVG).
def heart(t):
    return 16*sin(t)**3/16, (13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t))/17
N=128; R=7
verts=[]; faces_idx=[]; mids=[]
for j in range(R):
    rr=(j+.0001)/(R-1)
    for i in range(N):
        t=2*pi*i/N
        hx,hz=heart(t)
        x=.408*rr*hx
        z=1.735+.38*rr*hz
        y=.574+.13*(1-rr**1.5)-.01*max(0,-hz)
        verts.append((x,y,z))
for j in range(R-1):
    for i in range(N):
        k=j*N+i; kn=j*N+(i+1)%N
        faces_idx.append((k,kn,kn+N,k+N))
        mids.append(2 if j==R-2 else (1 if j==R-3 else 0))
mesh=bpy.data.meshes.new("heart-disc sculpt surface")
mesh.from_pydata(verts,[],faces_idx);mesh.update()
obface=bpy.data.objects.new("Anatomically broad heart-shaped facial disc",mesh)
scene.collection.objects.link(obface)
obface.data.materials.append(face)
obface.data.materials.append(face2)
obface.data.materials.append(rim)
for poly,j in zip(obface.data.polygons,mids):
    poly.use_smooth=True;poly.material_index=j
# sculpted dark eye cups with non-protruding sockets and small glossy eyeballs
for sign in [-1,1]:
    x=sign*.179
    uv("eye socket shadow "+str(sign),(x,.708,1.775),(.138,.033,.138),face2,64,32)
    uv("open dark eye "+str(sign),(x,.724,1.783),(.096,.040,.108),eye,64,32)
    uv("eye moist reflection "+str(sign),(x-sign*.028,.760,1.821),(.022,.009,.025),catch,24,16)
# hooked horn bill in anatomically central face, short and downward-pointing
bpy.ops.mesh.primitive_cone_add(vertices=64,radius1=.018,radius2=.072,depth=.235,location=(0,.748,1.55))
bill=bpy.context.object;bill.name="short curved tapered beak";bill.rotation_euler[0]=.2
bill.data.materials.append(beakmat)
sm=bill.modifiers.new("soft edge", "BEVEL");sm.width=.018;sm.segments=3
bpy.ops.object.modifier_apply(modifier=sm.name)
bpy.ops.object.shade_smooth()
# Subtle recessed nares
for sign in [-1,1]:
    uv("bill nostril "+str(sign),(sign*.043,.804,1.635),(.012,.005,.009),face2,16,12)

# A broad senescent eucalypt hollow lip supporting the juvenile from beneath.
bpy.ops.mesh.primitive_cylinder_add(vertices=96,radius=.83,depth=.48,location=(0,-.08,.42))
stump=bpy.context.object;stump.name="broad hollow trunk base"
stump.data.materials.append(bark)
# rim with true 3D tube torus; no floating feet
bpy.ops.mesh.primitive_torus_add(major_segments=128,minor_segments=24,
    location=(0,-.08,.688),major_radius=.71,minor_radius=.13)
lip=bpy.context.object;lip.name="supporting eucalypt hollow lip";lip.data.materials.append(bark2)
bpy.ops.object.shade_smooth()
uv("dark inner hollow", (0,-.08,.673),(.64,.64,.025),hole,64,16)
# feet tucked forward, supported on lip rather than dangling
for sign in [-1,1]:
    uv("down-covered tarsus"+str(sign),(sign*.245,.35,.748),(.10,.115,.17),toe,32,20)
    for offset in [-.045,0,.045]:
        uv("tucked digit "+str(sign)+"-"+str(offset),
           (sign*.245+offset,.57,.694),(.027,.16,.030),beakmat,20,12)

# Fiber groom: orientation follows true 3D surface normals and falls softly.
# Curves do not export as-is in GLB; this test honestly treats rendered groom
# as a proof-of-render only, NOT a usable mobile asset.
def groom(name, count, center, radius, mat, minl, maxl, exclude_face=False, seed_offset=0):
    rng=random.Random(172153+seed_offset)
    cr=bpy.data.curves.new(name,"CURVE");cr.dimensions="3D";cr.resolution_u=1
    cr.bevel_depth=.0016;cr.bevel_resolution=1
    accepted=0; trials=0
    while accepted<count and trials<count*5:
        trials+=1
        u=rng.uniform(-1,1);t=rng.uniform(-pi,pi);k=math.sqrt(max(0,1-u*u))
        n=Vector((k*math.cos(t),k*math.sin(t),u))
        px=Vector((center[0]+radius[0]*n.x,center[1]+radius[1]*n.y,
                   center[2]+radius[2]*n.z))
        if exclude_face and n.y>.51 and px.z>1.36: continue
        if name.startswith("body") and px.z>1.57: continue
        if name.startswith("head") and px.z<1.38: continue
        direction=Vector((n.x*.8,n.y*.8,n.z*.5+.2))
        direction.normalize()
        tang=Vector((rng.uniform(-1,1),rng.uniform(-1,1),rng.uniform(-1,1)))
        tang=tang-direction*tang.dot(direction);tang.normalize()
        length=rng.uniform(minl,maxl)
        s=cr.splines.new("POLY");s.points.add(3)
        coords=[px,px+direction*length*.40+tang*.006,
            px+direction*length*.78+tang*.011,px+direction*length+tang*.014]
        for p,coord in zip(s.points,coords):p.co=(*coord,1)
        accepted+=1
    o=bpy.data.objects.new(name,cr);scene.collection.objects.link(o)
    o.data.materials.append(mat)
    return accepted
# Deliberately not spiky adult flight-feather surfaces; tiny, soft dense down.
f1=groom("head mesoptile down cream",3500,(0,.065,1.70),(.55,.50,.50),fluff,.018,.052,True,1)
f2=groom("body second down ivory",5300,(0,-.055,1.02),(.68,.58,.72),fluff,.028,.064,False,2)
f3=groom("underwing shade filaments",1400,(0,-.045,.91),(.72,.56,.48),fluff2,.018,.040,False,3)
# facial fringe arranged as layered hairs around the heart contour
cr=bpy.data.curves.new("individual heart rim down filaments","CURVE")
cr.dimensions="3D";cr.resolution_u=1;cr.bevel_depth=.0012;cr.bevel_resolution=1
frng=random.Random(8271)
for i in range(1200):
    t=frng.random()*2*pi;hx,hz=heart(t)
    x=.395*hx; z=1.735+.37*hz;y=.568
    p=Vector((x,y,z))
    d=Vector((hx,.24,hz*.6));d.normalize()
    l=frng.uniform(.012,.032)
    s=cr.splines.new("POLY");s.points.add(2)
    for pt,co in zip(s.points,[p,p+d*l*.55,p+d*l]):pt.co=(*co,1)
fc=bpy.data.objects.new("delicate mask fringe",cr);scene.collection.objects.link(fc)
fc.data.materials.append(fluff2)
# Studio render
world=bpy.data.worlds.new("neutral studio");scene.world=world;world.use_nodes=True
world.node_tree.nodes["Background"].inputs["Color"].default_value=(.60,.67,.72,1)
world.node_tree.nodes["Background"].inputs["Strength"].default_value=.45
def area(name,loc,power,size):
    bpy.ops.object.light_add(type="AREA",location=loc);o=bpy.context.object;o.name=name
    o.data.energy=power;o.data.shape="DISK";o.data.size=size
    direction=Vector((0,0,1.18))-o.location;o.rotation_euler=direction.to_track_quat('-Z','Y').to_euler()
area("softbox key", (2.0,3.7,4.4),700,4.5)
area("large fill",(-2.7,1.0,3.0),360,4.0)
area("back soft rim",(-1.0,-3.7,3.7),850,3.0)
scene.render.engine="CYCLES";scene.cycles.samples=16;scene.cycles.use_denoising=False
scene.render.resolution_x=480;scene.render.resolution_y=480
scene.render.resolution_percentage=100;scene.render.image_settings.file_format="PNG"
scene.view_settings.view_transform="AgX"
focus=Vector((0,0,1.24))
def camera(name,loc):
    bpy.ops.object.camera_add(location=loc);o=bpy.context.object;o.name=name
    direction=focus-o.location;o.rotation_euler=direction.to_track_quat("-Z","Y").to_euler()
    o.data.type="ORTHO";o.data.ortho_scale=2.85
    return o
views={
 "front":(0,4.8,2.35),
 "quarter":(3.38,3.38,2.35),
 "strict_side":(4.8,0,2.35),
 "back":(0,-4.8,2.35),
}
for key,loc in views.items():
    scene.camera=camera("inspection_"+key,loc)
    scene.render.filepath=os.path.join(OUT,key+"_actual_cycles.png")
    bpy.ops.render.render(write_still=True)
    print("RENDER_OK",key,scene.render.filepath,flush=True)
# Save actual editable sculpt for independent inspection, quarantined only.
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT,"run153_original_sculpt_groom_UNAPPROVED.blend"))
# Export only mesh volumes, not curves, not cameras/lights, tree omitted.
bpy.ops.object.select_all(action="DESELECT")
models=[o for o in bpy.data.objects if o.type=="MESH" and (
 "mesoptile" in o.name or "wing volume" in o.name or "disc" in o.name or
 "eye " in o.name or "socket" in o.name or "beak" in o.name or "bill" in o.name or
 "tarsus" in o.name or "digit" in o.name)]
for o in models:o.select_set(True)
if models:bpy.context.view_layer.objects.active=models[0]
try:
    bpy.ops.export_scene.gltf(filepath=os.path.join(OUT,"run153_MESH_ONLY_NOT_FUR_UNAPPROVED.glb"),
       export_format="GLB",use_selection=True)
except Exception as e:
    print("GLB_EXPORT_FAILED",str(e),flush=True)
stats={"run":153,"result":"ART_UNREVIEWED_NO_RELEASE","camera_orientation":"face +Y, back -Y",
  "procedural_sculpt":True,"no_neural_output":True,"fur_is_curve_render_only":True,
  "glb_mobile_ready":False,"physical_phone_tested":False,"license":"new original script",
  "groom_strands":f1+f2+f3+1200, "render_views":list(views),
  "mesh_objects":len(models),"production_changes":False}
for name in os.listdir(OUT):
    p=os.path.join(OUT,name)
    if os.path.isfile(p):stats.setdefault("files",{})[name]={"bytes":os.path.getsize(p),
       "sha256":hashlib.sha256(open(p,"rb").read()).hexdigest()}
with open(os.path.join(OUT,"run153_status.json"),"w") as f:json.dump(stats,f,ensure_ascii=False,indent=2)
with open(os.path.join(OUT,"NO_RELEASE.txt"),"w") as f:f.write(
 "Run153 is sculpt/groom feasibility only. Rendered fibre curves do not survive GLB export. "
 "No unreviewed model may be published; no actual-phone WebGL validation exists.\n")
print("RUN153_COMPLETE_NO_RELEASE",json.dumps(stats,ensure_ascii=False),flush=True)
