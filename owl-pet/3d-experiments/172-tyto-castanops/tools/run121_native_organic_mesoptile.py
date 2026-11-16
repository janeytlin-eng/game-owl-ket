#!/usr/bin/env python3
"""Run121 no-charge native organic juvenile sculpt, not a production asset.
An original continuous lofted/locally sculpted body mesh, not disjoint owl
primitives or a retextured adult owl. Tangent-registered true 3D fine down
plus anatomical eyes/beak/short buried wing bulges and a separate bark hollow.
All output remains ART_UNAPPROVED until visually reviewed in four directions.
"""
import bpy, math, random, hashlib, json, sys, pathlib, traceback
from mathutils import Vector
from math import sin,cos,pi,exp,asin
random.seed(172121)
assert "--" in sys.argv
out=pathlib.Path(sys.argv[sys.argv.index("--")+1]);out.mkdir(parents=True,exist_ok=True)
bpy.ops.object.select_all(action="SELECT");bpy.ops.object.delete(use_global=False)
for m in list(bpy.data.materials):bpy.data.materials.remove(m)
def material(name,c,rough=.9,metal=0):
    m=bpy.data.materials.new(name);m.diffuse_color=(*c,1);m.use_nodes=True
    p=m.node_tree.nodes.get("Principled BSDF")
    p.inputs["Base Color"].default_value=(*c,1)
    p.inputs["Roughness"].default_value=rough
    p.inputs["Metallic"].default_value=metal
    return m
down=[material("deep layered cream mesoptile %d"%i,c) for i,c in enumerate([
    (.78,.70,.55),(.86,.80,.69),(.92,.87,.77),(.95,.91,.83),(.98,.95,.87)])]
facial=[material("warm natural integrated facial disk %d"%i,c) for i,c in enumerate([
    (.79,.58,.40),(.87,.72,.55),(.94,.85,.70),(.96,.90,.80),(.99,.94,.85)])]
featherrim=material("wispy bronze edge around facial disk",(.73,.52,.33))
darkeye=material("black brown deep glossy live eyes",(.012,.009,.009),.08)
eyelid=material("soft brown orbital eyelid",(.38,.24,.16))
beakmat=material("pale natural horn bill",(.86,.69,.49),.32)
feetmat=material("warm slate beige raptor toes",(.43,.37,.31),.74)
clawmat=material("small rounded keratin claws",(.28,.25,.23),.38)
barks=[material("old weathered eucalypt hollow wood %d"%i,c) for i,c in enumerate([
(.18,.12,.085),(.25,.17,.115),(.32,.23,.155),(.42,.31,.22)])]
def mesh_obj(name,vs,faces,materials,mis=None):
    me=bpy.data.meshes.new(name);me.from_pydata(vs,[],faces);me.update()
    ob=bpy.data.objects.new(name,me);bpy.context.collection.objects.link(ob)
    for mat in materials:me.materials.append(mat)
    for i,p in enumerate(me.polygons):
        p.use_smooth=True
        if mis:p.material_index=mis[i]
    return ob
height=2.15
def heart(x,z):
    u=x/.55;v=(z-1.58)/.345
    return (u*u+v*v-1)**3-u*u*v*v*v
def softstep(edge0,edge1,x):
    x=max(0.0,min(1.0,(x-edge0)/(edge1-edge0)))
    return x*x*(3-2*x)
def body(z,phi):
    t=max(.0001,min(.9999,z/height))
    cap=max(0,sin(pi*t))**.33
    bulge= .72 + .11*exp(-((z-.72)/.40)**2)+.12*exp(-((z-1.60)/.32)**2)-.075*exp(-((z-1.18)/.15)**2)
    rx=bulge*cap
    ry=(.56+.16*exp(-((z-.75)/.40)**2)+.075*exp(-((z-1.63)/.38)**2))*cap
    x=rx*sin(phi); y=-ry*cos(phi)
    f=heart(x,z)
    # Widened forehead and owl-heart surface are sculpted continuously into one anatomical mesh.
    front=max(0,cos(phi))**5
    inside=softstep(.15,-.20,f) if False else (1-softstep(-.18,.18,f))
    edge=exp(-((f/.13)**2))
    y-=.077*front*inside
    y+=.032*front*edge
    # Short down-covered juvenile wing bulges, not developed secondary/remige plates.
    for wing_angle in (-1.20,1.20):
        angular=math.atan2(sin(phi-wing_angle),cos(phi-wing_angle))
        ywing=exp(-((angular/.35)**2)-(((z-1.05)/.27)**2))
        x+=.027*(1 if phi>0 else -1)*ywing
        y+=.025*ywing*cos(phi)
    # Small asymmetries and smooth surface relief, no high-frequency adult feather tiles.
    wobble=.0065*sin(phi*7+z*4)*sin(z*12+phi*5)
    return Vector((x+sin(phi)*wobble,y-cos(phi)*wobble,z))
def normal(z,phi):
    dz=(body(min(height-.001,z+.001),phi)-body(max(.001,z-.001),phi))
    dp=body(z,phi+.001)-body(z,phi-.001)
    v=dp.cross(dz)
    return v.normalized()
N=160;M=156
vs=[];fs=[];mi=[]
for j in range(M+1):
    z=.015+(height-.03)*j/M
    for k in range(N):
        phi=2*pi*k/N
        vs.append(tuple(body(z,phi)))
for j in range(M):
    z=.015+(height-.03)*(j+.5)/M
    for k in range(N):
        a=j*N+k; b=j*N+(k+1)%N; c=(j+1)*N+(k+1)%N; d=(j+1)*N+k
        fs.append((a,b,c,d))
        p=body(z,2*pi*(k+.5)/N)
        f=heart(p.x,z)
        frontal=max(0,-p.y)>0 and cos(2*pi*(k+.5)/N)>.29
        if frontal and f<.18:
            if -.12<f<.09:ix=len(down)+0
            elif -.32<f<=-.12:ix=len(down)+1
            elif -.60<f<=-.32:ix=len(down)+2
            elif -1.00<f<=-.60:ix=len(down)+3
            else:ix=len(down)+4
        else:
            ix=1 if z<.68 else (2 if z<1.12 else 3)
        mi.append(ix)
# Sew actual smooth round caps using terminating center vertices.
vbottom=len(vs);vs.append(tuple(body(.001,0)))
vtop=len(vs);vs.append(tuple(body(height-.001,0)))
for k in range(N):
    fs.append((vbottom,(k+1)%N,k));mi.append(2)
    fs.append((vtop,M*N+k,M*N+(k+1)%N));mi.append(3)
body_ob=mesh_obj("ONE CONTINUOUS sculpted downy juvenile Tyto body and heart mask",vs,fs,down+facial,mi)
def orb(name,loc,scale,mat,segments=24,rings=16):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments,ring_count=rings,location=loc)
    ob=bpy.context.object;ob.name=name;ob.scale=scale;ob.data.materials.append(mat)
    for p in ob.data.polygons:p.use_smooth=True
    return ob
for side in (-1,1):
    z=1.71
    x=side*.265
    # Solve body surface cylindrical parameter; no floating eyes.
    rx=(.72+.11*exp(-((z-.72)/.40)**2)+.12*exp(-((z-1.60)/.32)**2)-.075*exp(-((z-1.18)/.15)**2))*(sin(pi*z/height)**.33)
    phi=asin(max(-.98,min(.98,x/rx)))
    p=body(z,phi);n=normal(z,phi)
    orb("deep inset expressive glossy eye %s"%side,p+n*.040,(.106,.092,.115),darkeye)
    # Curved soft eyelid at the anatomical eye socket, not random ring on face.
    center=p+n*.018
    points=[]
    tangent=Vector((n.y,-n.x,0)).normalized()
    up=Vector((0,0,1))
    for k in range(65):
        a=2*pi*k/64
        points.append(center+(.119*cos(a))*tangent+(.125*sin(a))*up+n*.020)
    def tube(name,pts,radius,mat,nseg=6):
        verts=[];polys=[]
        for i,p0 in enumerate(pts):
            tan=(pts[min(i+1,len(pts)-1)]-pts[max(i-1,0)]).normalized()
            cross=tan.cross(Vector((0,0,1)))
            if cross.length<.01:cross=tan.cross(Vector((1,0,0)))
            cross.normalize();c2=tan.cross(cross).normalized()
            r=radius*(.62+.38*sin(pi*i/max(1,len(pts)-1)))
            for j in range(nseg):
                d=cos(j*2*pi/nseg)*cross+sin(j*2*pi/nseg)*c2
                verts.append(tuple(p0+d*r))
        for i in range(len(pts)-1):
            for j in range(nseg):
                polys.append((i*nseg+j,i*nseg+(j+1)%nseg,(i+1)*nseg+(j+1)%nseg,(i+1)*nseg+j))
        return mesh_obj(name,verts,polys,[mat])
    tube("natural upper and lower eyelid %s"%side,points,.011,eyelid)
    orb("tiny wet eye catchlight %s"%side,p+n*.135+Vector((-.026,0,.040)),(.019,.012,.020),material("wet catchlight %s"%side,(.95,.90,.79),.09),16,10)
# Real organic tapered curved beak, close-set beneath eye pair.
beakpath=[Vector((0,-.75,1.54)),Vector((0,-.84,1.48)),Vector((0,-.876,1.41)),Vector((0,-.865,1.33))]
bvs=[];bfs=[];brad=[.068,.075,.045,.005]
for i,p in enumerate(beakpath):
    for k in range(12):
        a=2*pi*k/12
        bvs.append(tuple(p+Vector((brad[i]*cos(a),brad[i]*.61*sin(a),0))))
for i in range(3):
    for k in range(12):
        bfs.append((i*12+k,i*12+(k+1)%12,(i+1)*12+(k+1)%12,(i+1)*12+k))
mesh_obj("small naturally curved horn beak",bvs,bfs,[beakmat])
# Feet: two feet and compact anatomical toe paths visibly supported by old bark lip.
def tubular(name,points,r,mat,nseg=7):
    verts=[];faces=[]
    pts=[Vector(p) for p in points]
    for i,p in enumerate(pts):
        tangent=(pts[min(i+1,len(pts)-1)]-pts[max(i-1,0)]).normalized()
        axis=tangent.cross(Vector((0,0,1)))
        if axis.length<.01:axis=tangent.cross(Vector((1,0,0)))
        axis.normalize();other=tangent.cross(axis).normalized()
        for j in range(nseg):
            rr=r*(.9-.55*i/max(1,len(pts)-1))
            verts.append(tuple(p+rr*(axis*cos(2*pi*j/nseg)+other*sin(2*pi*j/nseg))))
    for i in range(len(pts)-1):
        for j in range(nseg):
            faces.append((i*nseg+j,i*nseg+(j+1)%nseg,(i+1)*nseg+(j+1)%nseg,(i+1)*nseg+j))
    return mesh_obj(name,verts,faces,[mat])
for sign in (-1,1):
    x=sign*.32
    tubular("supported tarsus %s"%sign,[(x,-.39,.36),(x,-.44,.27),(x,-.54,.20)],.065,feetmat)
    for di in (-1,0,1):
        bend=.11*di
        pts=[(x,-.55,.24),(x+.045*di,-.63,.20),(x+bend,-.76,.184),(x+bend*1.24,-.82,.171)]
        tubular("short supported toe %s-%d"%(sign,di),pts,.027,feetmat)
        tubular("tiny keratin toe tip %s-%d"%(sign,di),[pts[-2],pts[-1],(pts[-1][0],pts[-1][1]-.043,.17)],.014,clawmat)
# Hollow lip is a separate environment, not claimed to be a part of the owl.
rings=12;sections=128;bvs=[];bfs=[];bmis=[]
for k in range(rings+1):
    phase=k/rings
    for j in range(sections):
        a=j*2*pi/sections
        # hollow opening within weathered old eucalypt stump
        r=.72+.24*phase
        jitter=.022*sin(9*a+phase*6)+.014*sin(23*a)+.013*sin(17*a+phase*4)
        x=(r+jitter)*cos(a);y=(r*.74+jitter)*sin(a)+.02
        z=.19 - .12*phase+.023*sin(a*11)+.026*sin(a*19+phase*5)
        bvs.append((x,y,z))
for k in range(rings):
    for j in range(sections):
        a=k*sections+j;b=k*sections+(j+1)%sections
        c=(k+1)*sections+(j+1)%sections;d=(k+1)*sections+j
        bfs.append((a,b,c,d));bmis.append((j//5+k//3)%len(barks))
mesh_obj("aged eucalypt tree hollow load bearing lip",bvs,bfs,barks,bmis)
# Fine 3D down: tangent-registered, curved, short cross-ribbons, all positions on
# ONE actual continuous organic bird surface. No SVG, no particle billboard impostor.
fv=[];ff=[];fmi=[]
num_fibers=4800
for i in range(num_fibers):
    z=.11+1.99*random.random()
    if random.random()> max(.12,sin(pi*z/height)**.58):continue
    phi=2*pi*random.random()
    p=body(z,phi);n=normal(z,phi)
    f=heart(p.x,z)
    is_face=(cos(phi)>.28 and f<0.18)
    L=random.uniform(.035,.085)
    if is_face:L*=.33
    if z>1.94:L*=1.3
    if z<.45:L*=.76
    root=p-n*.002
    axis=Vector((random.uniform(-.5,.5),random.uniform(-.5,.5),random.uniform(-.24,.95)))
    direction=(n*.68+axis*.48).normalized()
    v1=direction.cross(Vector((0,0,1)))
    if v1.length<.05:v1=direction.cross(Vector((1,0,0)))
    v1.normalize();v2=direction.cross(v1).normalized()
    material_i=random.choices(range(5),weights=[3,6,16,22,13])[0]
    if is_face:material_i=random.choice([1,2,3,4])
    for o in (v1,v2):
        b=len(fv)
        for j in range(4):
            t=j/3
            center=root+direction*(L*t)+Vector((0,0,.009*t*t)) + v2*(.011*sin(pi*t))
            w=.0056*(1-t)**.74+.0003
            fv.extend([tuple(center-o*w),tuple(center+o*w)])
        for j in range(3):
            ff.extend([(b+j*2,b+j*2+1,b+j*2+3),(b+j*2,b+j*2+3,b+j*2+2)])
            fmi.extend([material_i,material_i])
fur=mesh_obj("fine true 3D soft curved mesoptile crossfibers",fv,ff,down,fmi)
# Verification and mobile-friendly GLB export; no publication approval assumed.
meshes=[o for o in bpy.context.scene.objects if o.type=="MESH"]
for ob in bpy.context.selected_objects:ob.select_set(False)
for ob in meshes:ob.select_set(True)
bpy.context.view_layer.objects.active=body_ob
glb=out/"run121_native_continuous_juvenile_organic_sculpt_ART_UNAPPROVED.glb"
bpy.ops.export_scene.gltf(filepath=str(glb),export_format="GLB",use_selection=True,export_materials="EXPORT")
assert glb.open("rb").read(4)==b"glTF" and glb.stat().st_size>150000
# Render the actual exported GLB, NOT a hidden non-exportable Blender groom.
for ob in meshes:bpy.data.objects.remove(ob,do_unlink=True)
before=set(bpy.context.scene.objects)
bpy.ops.import_scene.gltf(filepath=str(glb))
real=[o for o in bpy.context.scene.objects if o not in before and o.type=="MESH"]
assert len(real)>4
triangles=sum(len(o.data.loop_triangles) for o in real)
assert 10000<triangles<250000
s=bpy.context.scene;s.render.engine="CYCLES";s.cycles.samples=24
s.cycles.use_denoising=False
for layer in s.view_layers:layer.cycles.use_denoising=False
s.render.resolution_x=540;s.render.resolution_y=540;s.render.resolution_percentage=100
s.render.image_settings.file_format="PNG";s.view_settings.view_transform="Standard"
s.world.color=(.27,.28,.30)
def light(name,xyz,power,size):
    d=bpy.data.lights.new(name,"AREA");d.energy=power;d.shape="DISK";d.size=size
    ob=bpy.data.objects.new(name,d);s.collection.objects.link(ob)
    ob.location=xyz;ob.rotation_euler=(Vector((0,0,1.12))-ob.location).to_track_quat("-Z","Y").to_euler()
light("large natural sky key",(-3,-4,5),480,4)
light("front fill",(3,-3,2.8),260,3)
light("backlight",(2,3,4),450,2.5)
cd=bpy.data.cameras.new("true 3D four-angle orbit");ca=bpy.data.objects.new("true 3D four-angle orbit",cd)
s.collection.objects.link(ca);s.camera=ca;cd.type="ORTHO";cd.ortho_scale=2.91
for name,deg in (("front",0),("quarter",45),("side",90),("back",180)):
    phi=math.radians(deg)
    ca.location=(4.5*sin(phi),-4.5*cos(phi),2.03)
    ca.rotation_euler=(Vector((0,0,1.11))-ca.location).to_track_quat("-Z","Y").to_euler()
    s.render.filepath=str(out/("run121_glb_reimport_"+name+"_actual_cycles_ART_REVIEW.png"))
    bpy.ops.render.render(write_still=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
report={"run":121,"type":"original continuous organic high-resolution juvenile digital sculpt probe",
"source":"locally constructed one connected lofted body shell; separate anatomical features and hollow",
"blender":bpy.app.version_string,"exported_bytes":glb.stat().st_size,
"exported_glb_sha256":sha(glb),"imported_mesh_count":len(real),
"imported_triangles":triangles,"fine_down_generated_attempts":num_fibers,
"four_rendered_views":["front","quarter","side","back"],
"real_mobile_gpu_test":False,"global_license":"own experiment script, no external sculpt/texture licensing; no validation of biological details",
"art_status":"ART_UNREVIEWED_NOT_RELEASED","release":"NO_RELEASE"}
(out/"run121_native_sculpt_geometry_and_limits.json").write_text(json.dumps(report,indent=2))
(out/"NO_RELEASE.flag").write_text("Research only. Four-direction beauty, art anatomy, soft down, supported feet, real phone GPU and license NOT certified.\n")
print("RUN121_REAL_3D_REIMPORTED_FOUR_VIEWS_NO_ART_APPROVAL",json.dumps(report))
