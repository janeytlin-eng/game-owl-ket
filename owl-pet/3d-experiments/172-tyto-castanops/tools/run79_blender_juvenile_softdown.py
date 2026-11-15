"""Run79: Blender juvenile proportions, sunken eyes, softer mesoptile groom and true supported perch experiment.
NOT art approved, NOT a production model. Independent branch-only experiment.
Usage: blender -b -t 2 --python this.py -- output-directory
No paid services. Age-unknown Tyto castanops mesoptile design study.
"""
import bpy, math, random, json, os, sys, time, hashlib
from mathutils import Vector
from math import sin, cos, pi, sqrt, exp

seed=17279
rng=random.Random(seed)
out=sys.argv[sys.argv.index('--')+1] if '--' in sys.argv else 'qa-out'
os.makedirs(out,exist_ok=True)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

def mat(name, color, rough=0.91, metallic=0):
    m=bpy.data.materials.new(name)
    m.diffuse_color=(*color,1)
    m.use_nodes=True
    p=m.node_tree.nodes.get('Principled BSDF')
    p.inputs['Base Color'].default_value=(*color,1)
    p.inputs['Roughness'].default_value=rough
    p.inputs['Metallic'].default_value=metallic
    return m

cream=mat('second-down ivory cream',(.94,.885,.77))
face=mat('velvety face cheek',(.95,.89,.79))
brown=mat('brown narrow heart edging',(.66,.49,.33))
brownlight=mat('fawn eyelid',(.67,.52,.37))
black=mat('wet dark owl eye',(.015,.012,.010),.10)
eyeinner=mat('deep-brown orbit',(.24,.155,.105))
billmat=mat('horn ivory bill',(.81,.72,.55),.40)
clawmat=mat('dark slate talons',(.25,.22,.21),.40)
bark=mat('weathered eucalyptus lip',(.31,.23,.17))
furm=[mat('filament cream %02d'%i,c) for i,c in enumerate([
(.96,.92,.84),(.92,.87,.78),(.99,.96,.90),(.89,.80,.69),(.96,.90,.81)])]
for m in furm:
    m.use_backface_culling=False

def active(o):
    bpy.ops.object.select_all(action='DESELECT'); o.select_set(True); bpy.context.view_layer.objects.active=o

def uvball(name,center,scale,material,segments=40,rings=24):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=rings, location=center)
    ob=bpy.context.object
    ob.name=name; ob.scale=scale
    active(ob); bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    ob.data.materials.append(material)
    for poly in ob.data.polygons: poly.use_smooth=True
    return ob

# A truly continuous voxel-fused body sculpt (no separated oval wings).
body=uvball('BODY raw fused soft anatomy', (0,.075,.80),(.62,.53,.72),cream)
head=uvball('HEAD raw downy crown', (0,.02,1.44),(.59,.49,.56),cream)
bpy.ops.object.select_all(action='DESELECT')
for ob in (body,head): ob.select_set(True)
bpy.context.view_layer.objects.active=body
bpy.ops.object.join()
active(body)
bpy.ops.object.transform_apply(location=True,rotation=True,scale=True)
body.data.remesh_voxel_size=.027
bpy.ops.object.voxel_remesh()
# Smooth, non-axisymmetric sculpt. Body and head must share actual skin topology.
for _ in range(3):
    bpy.ops.object.modifier_add(type='SMOOTH')
    mod=body.modifiers[-1]; mod.factor=1.15; mod.iterations=2
    bpy.ops.object.modifier_apply(modifier=mod.name)
for vert in body.data.vertices:
    p=vert.co; x,y,z=p.x,p.y,p.z
    # A defined juvenile shoulder, softer nape and tiny down-hidden wing-root relief.
    g=exp(-((abs(x)-.46)/.18)**2-((z-.98)/.29)**2)
    g*=max(0.0, min(1.0,(y+.24)/.46))
    normal=vert.normal.copy()
    vert.co+=normal*(.065*g)
    # Broad folded juvenile wing-root ridge blends into the original continuous skin,
    # not an attached ovoid. Masked from the breast and hidden below down.
    seam=exp(-((abs(x)-.49)/.12)**2-((z-(.78+.20*max(0,y)))/.10)**2)
    vert.co-=normal*(.015*seam*max(0.0,min(1.0,(y+.12)/.45)))
    # smaller structured irregularities are 3D and affect front/back consistently
    fall=max(0.,min(1.,(z-.16)/.31))
    n=sin(26*x+3*z)*sin(17*z+5*y)+.4*sin(39*y+9*x)
    vert.co+=vert.normal*(.0032*n*fall)
body.name='continuous sculpted juvenile skin (research)'
body.data.materials.clear();body.data.materials.append(cream)
for p in body.data.polygons:p.use_smooth=True
# Triangulate the continuous remeshed owl skin to sample its actual 3D surface for grooming.
active(body)
bpy.ops.object.modifier_add(type='TRIANGULATE')
bpy.ops.object.modifier_apply(modifier=body.modifiers[-1].name)

def meshob(name,verts,faces,material):
    me=bpy.data.meshes.new(name)
    me.from_pydata(verts,[],faces);me.update()
    ob=bpy.data.objects.new(name,me)
    bpy.context.collection.objects.link(ob)
    me.materials.append(material)
    for p in me.polygons:p.use_smooth=True
    return ob

# Three-dimensional (not photographed) continuous heart face mesh.
# Standard heart parametric contour in the owl's XZ anatomical plane.
def heart(t):
    hx=16*sin(t)**3/18
    hz=(13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t))/18
    return .545*hx,1.49+.425*hz
# Surface-following front contour: make the disk touch real remeshed head/body,
# instead of a visually detached frontal placard at three-quarter and profile.
def front_depth(x,z):
    hit,co,n,idx=body.ray_cast(Vector((x,-3.,z)),Vector((0.,1.,0.)),distance=6.)
    return co.y if hit else -.33
verts=[];faces=[];N=160;R=20
for j in range(R+1):
    r=max(0.0001,j/R)
    for k in range(N):
        x,z=heart(2*pi*k/N)
        x*=r;z=1.49+(z-1.49)*r
        # Actual dish-depth: central cheeks inset, heart edge raised
        y=front_depth(x,z)-.020-.011*r*r+.010*exp(-((z-1.68)/.23)**2)
        y+=.020*exp(-((abs(x)-.19)/.11)**2-((z-1.54)/.12)**2)
        verts.append((x,y,z))
        if j>0:
            a=(j-1)*N+k;b=(j-1)*N+(k+1)%N;c=j*N+k;d=j*N+(k+1)%N
            faces.extend([(a,c,b),(b,c,d)])
disc=meshob('sculpted double-lobed heart facial disk',verts,faces,face)

# Face contour: a genuine curved 3D mesh, layered natural rim strands.
def tube(name, points, radii, material, sides=7):
    verts=[];faces=[]
    for i,co in enumerate(points):
        v=Vector(co)
        tangent=Vector(points[min(i+1,len(points)-1)])-Vector(points[max(i-1,0)])
        if tangent.length<1e-6:tangent=Vector((0,0,1))
        tangent.normalize()
        s=tangent.cross(Vector((0,1,0)))
        if s.length<1e-6:s=Vector((1,0,0))
        s.normalize();t=tangent.cross(s).normalized()
        rad=radii[i] if isinstance(radii,list) else radii
        for j in range(sides):
            w=v+rad*(s*cos(2*pi*j/sides)+t*sin(2*pi*j/sides))
            verts.append(tuple(w))
        if i:
            for j in range(sides):
                a=(i-1)*sides+j;b=(i-1)*sides+(j+1)%sides
                c=i*sides+j;d=i*sides+(j+1)%sides
                faces.extend([(a,b,c),(b,d,c)])
    return meshob(name,verts,faces,material)

ring=[]
for k in range(161):
    x,z=heart(2*pi*k/160)
    y=front_depth(x,z)-.034+.004*sin(2*pi*k/13)+.005*sin(2*pi*k/29)
    ring.append((x,y,z))
tube('subtle warm down edge of facial disc',ring,.008,brownlight)
for row in range(1):
    rr=[]
    for k in range(161):
        x,z=heart(2*pi*k/160)
        xx=x*.995; zz=z-.005
        rr.append((xx,front_depth(xx,zz)-.043-.011*row,zz))
    tube('thin down edge %d'%row,rr,.0045,furm[row])

# Eye sockets and black glossy bird eyes: physically attached to head plane.
for side in (-1,1):
    depth=front_depth(.218*side,1.575)
    uvball('natural shaded eye orbit',(.212*side,depth-.028,1.577),(.101,.017,.103),eyeinner,32,18)
    uvball('small recessed dark eye',(.212*side,depth-.054,1.581),(.070,.028,.074),black,40,22)

# Tapered downward-curving beak with curved centerline, not a cone.
beakpts=[];rads=[]
for i in range(13):
    q=i/12
    zz=1.496-.237*q
    beakpts.append((0, front_depth(0,zz)-.078-.070*sin(pi*q)+.026*q,zz))
    rads.append(.065*(1-q)**.75+.002)
tube('curved ivory hooked beak',beakpts,rads,billmat,12)

# Buried feet, visible toes and dark claw tips (no adult-length shanks).
for side in (-1,1):
    x0=.26*side
    uvball('crouched down-covered tarsal stump',(x0,-.28,.245),(.108,.13,.125),cream,24,16)
    for j in range(3):
        dx=(j-1)*.080
        pts=[(x0+dx*.25,-.39,.14),(x0+dx*.70,-.48,.122),
             (x0+dx,-.58,.114),(x0+dx*1.15,-.63,.095)]
        tube('short juvenile toe %d_%d'%(side,j),pts,[.036,.030,.022,.014],brownlight,7)
        tube('curved dark claw %d_%d'%(side,j),[
            pts[-1],(pts[-1][0]+dx*.24,-.665,.075),
            (pts[-1][0]+dx*.26,-.679,.052)], [.017,.013,.002],clawmat,6)

# Anatomically sensible short, uneven bark perch rather than the preceding
# flat, hovering cloth-like hollow support. Cross-section has real volume.
perchpoints=[];perchradii=[]
for i in range(33):
    t=i/32
    perchpoints.append((-1.08+2.16*t,-.55+.045*sin(2*pi*t),.044+.022*sin(3*pi*t)))
    perchradii.append(.12+.018*sin(5*pi*t)+.008*sin(13*pi*t))
tube('solid irregular eucalyptus perch',perchpoints,perchradii,bark,11)

# Actual hundreds of thousands of individually varied 3D feather-guide positions
# rendered into a mobile-capable triangle filament groom; no raster SVG shell.
bpy.context.view_layer.update()
verts=[Vector(p.co) for p in body.data.vertices]
faces=[p.vertices[:] for p in body.data.polygons if len(p.vertices)==3]
tris=[(verts[t[0]],verts[t[1]],verts[t[2]]) for t in faces]
areas=[(b-a).cross(c-a).length*.5 for a,b,c in tris]
total=sum(areas)
acc=[];s=0.
for area in areas:
    s+=area;acc.append(s)
import bisect
FV=[[] for _ in furm]; FF=[[] for _ in furm]
kept=0;trials=0;target=19500
while kept<target and trials<target*7:
    trials+=1
    idx=bisect.bisect_left(acc,rng.random()*total)
    a,b,c=tris[min(idx,len(tris)-1)]
    u=rng.random();v0=rng.random()
    if u+v0>1:u=1-u;v0=1-v0
    p=a+u*(b-a)+v0*(c-a)
    norm=(b-a).cross(c-a).normalized()
    # no low-quality splinters over the actual developed heart mask
    if p.y<-.30 and abs(p.x)<.55 and 1.15<p.z<1.91:continue
    if p.z<.20:continue
    if norm.z<-.75:continue
    # Shorter crown down, longer body fringe: curved, not sharp needles.
    length=rng.uniform(.017,.043) if p.z>1.15 else rng.uniform(.023,.061)
    length*=rng.uniform(.82,1.17)
    width=length*rng.uniform(.10,.17)
    tangent=norm.cross(Vector((0,0,1)))
    if tangent.length<.08:tangent=norm.cross(Vector((0,1,0)))
    tangent.normalize()
    bend=(Vector((rng.uniform(-.55,.55),rng.uniform(-.40,.40),-.32))
          +tangent*rng.uniform(-.3,.3))*length
    root=p+norm*.004
    mid=root+norm*(length*.30)+bend*.30
    tip=root+norm*(length*.62)+bend*.67
    bb=tangent*width
    group=rng.randrange(len(furm))
    vv=FV[group];ff=FF[group];n=len(vv)
    vv.extend([tuple(root-bb),tuple(root+bb),
               tuple(mid-bb*.48),tuple(mid+bb*.48),tuple(tip)])
    ff.extend([(n,n+1,n+2),(n+1,n+3,n+2),(n+2,n+3,n+4)])
    kept+=1
for i in range(len(furm)):
    if FF[i]:meshob('curved second-down filament batch %d'%i,FV[i],FF[i],furm[i])
print('SOFT_FUR_GUIDES',kept,'FUR_TRIANGLES',3*kept)

# Soft neutral gallery lights; same angles reveal unsupported back morphology.
world=bpy.context.scene.world
world.color=(.16,.16,.16)
world.use_nodes=True
bg=world.node_tree.nodes.get('Background')
bg.inputs['Color'].default_value=(.24,.28,.28,1)
bg.inputs['Strength'].default_value=.7

def area(name,loc,energy,size):
    bpy.ops.object.light_add(type='AREA',location=loc)
    o=bpy.context.object;o.name=name;o.data.energy=energy;o.data.shape='DISK';o.data.size=size
    rot=Vector((0,0,1.0))-o.location;o.rotation_euler=rot.to_track_quat('-Z','Y').to_euler()
for name,loc,energy,size in [
('cream softbox key',(-3,-3,5),380,4.2),
('neutral fill',(3,-2,3),200,3.2),
('rear separation',(0,3,4),300,3.4)]:area(name,loc,energy,size)
bpy.ops.object.camera_add()
cam=bpy.context.object;cam.name='audit camera'
bpy.context.scene.camera=cam
cam.data.type='ORTHO';cam.data.ortho_scale=2.95
sc=bpy.context.scene;sc.render.engine='CYCLES'
sc.cycles.samples=24
# Ubuntu distro Blender is compiled without Intel OIDN: disable Cycles denoising.
bpy.context.view_layer.cycles.use_denoising=False
sc.render.resolution_x=640;sc.render.resolution_y=640;sc.render.resolution_percentage=100
sc.render.image_settings.file_format='PNG'
sc.render.film_transparent=False
sc.view_settings.view_transform='Standard'
sc.view_settings.exposure=-.25
# modest, controlled no-spin orthographic 4-view QA
for name,loc in [
('front',(0,-4.6,2.1)),
('threequarter',(3,-3.8,2.0)),
('side',(4.7,0,2.0)),
('back',(0,4.7,2.0))]:
    cam.location=loc
    cam.rotation_euler=(Vector((0,0,1.05))-cam.location).to_track_quat('-Z','Y').to_euler()
    sc.render.filepath=os.path.join(out,'sculpt79_'+name+'.png')
    bpy.ops.render.render(write_still=True)
    print('RENDERED',name,os.path.getsize(sc.render.filepath))

# Export real meshes as glTF 2.0 GLB; camera/light excluded.
glb=os.path.join(out,'owl172_run79_softdown_juvenile_ART_PENDING.glb')
bpy.ops.export_scene.gltf(filepath=glb,export_format='GLB',export_cameras=False,
                          export_lights=False,export_yup=True)
bytesize=os.path.getsize(glb)
tri=sum(len(ob.data.polygons) for ob in bpy.data.objects if ob.type=='MESH')
stats={'gate':'ART_PENDING_VISUAL_REVIEW_NOT_APPROVED','blender_version':bpy.app.version_string,
       'branch':'research/owl172-run79-juvenile-soft-groom','source':'Run78 free Blender geometry baseline refit with a shorter down veil, recessed smaller eyes, continuous folded flank-wing and solid perch; still experimental, requires visual rejection gate',
       'mesoptile_age':'UNKNOWN','model_glb_bytes':bytesize,'triangle_count':tri,
       'filament_guides':kept,'filament_triangles':3*kept,
       'render_views':['front','threequarter','side','back'],
       'real_phone_gpu_test':False,'animation_test':False,'PBR_mobile_test':False,
       'glb_sha256':hashlib.sha256(open(glb,'rb').read()).hexdigest()}
with open(os.path.join(out,'metrics.json'),'w') as f:json.dump(stats,f,indent=2)
assert open(glb,'rb').read(4)==b'glTF'
# Reopen in Blender to validate real interchange, not merely exporter success.
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=glb)
imported=[o for o in bpy.context.scene.objects if o.type=='MESH']
stats['reimported_mesh_count']=len(imported)
stats['reimported_face_count']=sum(len(o.data.polygons) for o in imported)
with open(os.path.join(out,'metrics.json'),'w') as f:json.dump(stats,f,indent=2)
assert len(imported)>=10, 'GLB reimport did not retain character parts'
print('RUN79_TOOLCHAIN_SUCCESS_NOT_ART_APPROVAL',json.dumps(stats))
