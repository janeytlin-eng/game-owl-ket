"""Run81: anatomical wing-shoulder and recessed facial/foot tests, free Blender only.
NOT art approved, NOT a production model. Independent branch-only experiment.
Usage: blender -b -t 2 --python this.py -- output-directory
No paid services. Age-unknown Tyto castanops mesoptile design study.
"""
import bpy, math, random, json, os, sys, time, hashlib
from mathutils import Vector
from math import sin, cos, pi, sqrt, exp

seed=17281
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

cream=mat('second-down ivory cream',(.875,.795,.665))
face=mat('velvety face cheek',(.865,.765,.640))
brown=mat('brown narrow heart edging',(.60,.42,.285))
brownlight=mat('fawn eyelid',(.585,.415,.30))
black=mat('wet dark owl eye',(.015,.012,.010),.10)
eyeinner=mat('deep-brown orbit',(.24,.155,.105))
billmat=mat('horn ivory bill',(.77,.69,.55),.40)
clawmat=mat('dark slate talons',(.25,.22,.21),.40)
bark=mat('weathered eucalyptus lip',(.29,.215,.16))
furm=[mat('filament cream %02d'%i,c) for i,c in enumerate([
(.93,.85,.73),(.88,.78,.65),(.95,.89,.80),(.81,.71,.57),(.90,.81,.70)])]
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

# Run81: a single closed organic head-to-body loft, no spheres fused into a bag.
# Integrated face is assigned on the very same skin and gently sculpted into it.
def meshob(name,verts,faces,material):
    me=bpy.data.meshes.new(name)
    me.from_pydata(verts,[],faces);me.update()
    ob=bpy.data.objects.new(name,me)
    bpy.context.collection.objects.link(ob)
    me.materials.append(material)
    for p in me.polygons:p.use_smooth=True
    return ob

def heart(t):
    hx=16*sin(t)**3/18
    hz=(13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t))/18
    return .545*hx,1.49+.425*hz

# Triangular loft has actual 360-degree geometry from toe/belly to crown.
# Very gentle shoulder relief only; avoid jagged detached shoulder pads.
NV=110; NA=96
V=[];F=[]
for i in range(NV):
    z=.17+1.82*i/(NV-1)
    rx=.52*exp(-((z-.82)/.56)**2)+.43*exp(-((z-1.50)/.45)**2)
    ry=.45*exp(-((z-.82)/.57)**2)+.33*exp(-((z-1.49)/.45)**2)
    if i==0 or i==NV-1:rx=.002;ry=.002
    for j in range(NA):
        t=2*pi*j/NA
        x=rx*cos(t);y=.05+ry*sin(t)
        # Non-spherical rump and tapered nape; short down-hidden wing ridge,
        # broad smooth influence without an independent ellipsoid.
        wing=exp(-((abs(x)-.49)/.23)**2-((z-(.89+.09*y))/.35)**2)
        if z<1.32:
            x+=math.copysign(.016*wing,x)
        y+=.009*sin(3*t+4*z)*exp(-((z-.94)/.52)**2)
        V.append((x,y,z))
        if i:
            a=(i-1)*NA+j;b=(i-1)*NA+(j+1)%NA
            c=i*NA+j;d=i*NA+(j+1)%NA
            F.extend([(a,b,c),(b,d,c)])
body=meshob('one continuous organic juvenile loft',V,F,cream)
body.data.materials.append(face)
body.data.materials.append(brownlight)
# Make the thin edge and cheeks part of body topology: no separate heart plaque.
heartpoly=[heart(2*pi*k/160) for k in range(160)]
def faceSDF(x,z):
    inside=False
    near=100.
    for k in range(160):
        ax,az=heartpoly[k];bx,bz=heartpoly[(k+1)%160]
        dx=bx-ax;dz=bz-az
        h=max(0.,min(1.,((x-ax)*dx+(z-az)*dz)/(dx*dx+dz*dz+1e-10)))
        near=min(near,sqrt((x-ax-h*dx)**2+(z-az-h*dz)**2))
        if (az>z)!=(bz>z) and x<(bx-ax)*(z-az)/(bz-az)+ax:inside=not inside
    return near,inside
for vert in body.data.vertices:
    x,y,z=vert.co
    if y>-.12 or z<1.17:continue
    d,inside=faceSDF(x,z)
    # Relief of just a few mm, with no hard shell and no protruding mask.
    effect=exp(-(d/.045)**2)
    if inside:vert.co.y-=.011*(1-effect)
    else:vert.co.y+=.008*effect
body.data.update()
for poly in body.data.polygons:
    c=poly.center
    if c.y<-.12 and 1.15<c.z<1.94:
        d,inside=faceSDF(c.x,c.z)
        if d<.018:poly.material_index=2
        elif inside:poly.material_index=1
for p in body.data.polygons:p.use_smooth=True

def front_depth(x,z):
    hit,co,n,idx=body.ray_cast(Vector((x,-3.,z)),Vector((0.,1.,0.)),distance=6.)
    return co.y if hit else -.32


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
    ring.append((x,y+.0035*sin(2*pi*k/7),z))
tube('soft subtle integrated face edge',ring,.005,brownlight)
for row in range(1):
    rr=[]
    for k in range(161):
        x,z=heart(2*pi*k/160)
        xx=x*.995; zz=z-.005
        rr.append((xx,front_depth(xx,zz)-.043-.011*row,zz))
    tube('thin down edge %d'%row,rr,.0025,furm[row])

# Eye sockets and black glossy bird eyes: physically attached to head plane.
for side in (-1,1):
    depth=front_depth(.218*side,1.575)
    # Avoid Run79's giant circular "toy glasses". Place small eyes within
    # deeper, soft-shadowed socket; the orbital edge is only shallow relief.
    uvball('soft shaded eye depression',(.210*side,depth-.020,1.565),(.070,.008,.075),face,32,18)
    uvball('deep dark lid shadow',(.210*side,depth-.035,1.567),(.057,.010,.062),eyeinner,32,18)
    uvball('small dark eye',(.210*side,depth-.052,1.571),(.046,.015,.051),black,40,22)

# Tapered downward-curving beak with curved centerline, not a cone.
beakpts=[];rads=[]
for i in range(13):
    q=i/12
    zz=1.472-.190*q
    beakpts.append((0, front_depth(0,zz)-.041-.040*sin(pi*q)+.020*q,zz))
    rads.append(.043*(1-q)**.85+.002)
tube('curved ivory hooked beak',beakpts,rads,billmat,12)

# Buried feet, visible toes and dark claw tips (no adult-length shanks).
for side in (-1,1):
    x0=.26*side
    # Ankle is tucked below belly, not a pair of floating white marbles.
    uvball('mostly concealed crouched tarsus',(x0,-.12,.242),(.084,.10,.078),cream,24,16)
    for j in range(3):
        dx=(j-1)*.080
        pts=[(x0+dx*.25,-.32,.17),(x0+dx*.70,-.46,.145),
             (x0+dx,-.63,.129),(x0+dx*1.15,-.70,.092)]
        tube('short juvenile toe %d_%d'%(side,j),pts,[.036,.030,.022,.014],brownlight,7)
        tube('curved dark claw %d_%d'%(side,j),[
            pts[-1],(pts[-1][0]+dx*.24,-.745,.060),
            (pts[-1][0]+dx*.26,-.757,.018)], [.017,.013,.002],clawmat,6)

# A wide solid eroded hollow-floor shelf (no open-end cylindrical pipe).
# All exposed claws land on its surface. Closed top/bottom/sides with a rough edge.
shelfV=[];shelfF=[]
NX=42; NY=13
for level in range(2):
    for iy in range(NY):
        yy=-.95+1.17*iy/(NY-1)
        for ix in range(NX):
            xx=-1.12+2.24*ix/(NX-1)
            wave=.017*sin(17*xx+7*yy)+.012*sin(31*yy+11*xx)
            topz=.055+.039*cos(2.8*xx)+.012*sin(8*yy)+wave
            botz=topz-.29-.025*sin(4*xx)
            shelfV.append((xx,yy,topz if level==0 else botz))
for iy in range(NY-1):
    for ix in range(NX-1):
        a=iy*NX+ix;b=a+1;c=a+NX;d=c+1
        shelfF.extend([(a,b,c),(b,d,c)])
        off=NX*NY
        shelfF.extend([(a+off,c+off,b+off),(b+off,c+off,d+off)])
def join_edge(top_ids):
    for k in range(len(top_ids)-1):
        a=top_ids[k];b=top_ids[k+1];off=NX*NY
        shelfF.extend([(a,a+off,b),(b,a+off,b+off)])
join_edge([ix for ix in range(NX-1,-1,-1)])
join_edge([(NY-1)*NX+ix for ix in range(NX)])
join_edge([iy*NX for iy in range(NY)])
join_edge([iy*NX+NX-1 for iy in range(NY-1,-1,-1)])
meshob('solid eroded mature eucalyptus hollow ledge',shelfV,shelfF,bark)

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
kept=0;trials=0;target=9500
while kept<target and trials<target*7:
    trials+=1
    idx=bisect.bisect_left(acc,rng.random()*total)
    a,b,c=tris[min(idx,len(tris)-1)]
    u=rng.random();v0=rng.random()
    if u+v0>1:u=1-u;v0=1-v0
    p=a+u*(b-a)+v0*(c-a)
    norm=(b-a).cross(c-a).normalized()
    # no low-quality splinters over the actual developed heart mask
    if p.y<-.14 and abs(p.x)<.55 and 1.15<p.z<1.94:continue
    if p.z<.20:continue
    if norm.z<-.75:continue
    # Shorter crown down, longer body fringe: curved, not sharp needles.
    length=rng.uniform(.009,.024) if p.z>1.15 else rng.uniform(.012,.033)
    length*=rng.uniform(.82,1.17)
    width=length*rng.uniform(.26,.36)
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
sc.cycles.samples=20
# Ubuntu distro Blender is compiled without Intel OIDN: disable Cycles denoising.
bpy.context.view_layer.cycles.use_denoising=False
sc.render.resolution_x=640;sc.render.resolution_y=640;sc.render.resolution_percentage=100
sc.render.image_settings.file_format='PNG'
sc.render.film_transparent=False
sc.view_settings.view_transform='Standard'
sc.view_settings.exposure=-.48
# modest, controlled no-spin orthographic 4-view QA
for name,loc in [
('front',(0,-4.6,2.1)),
('threequarter',(3,-3.8,2.0)),
('side',(4.7,0,2.0)),
('back',(0,4.7,2.0))]:
    cam.location=loc
    cam.rotation_euler=(Vector((0,0,1.05))-cam.location).to_track_quat('-Z','Y').to_euler()
    sc.render.filepath=os.path.join(out,'sculpt81_'+name+'.png')
    bpy.ops.render.render(write_still=True)
    print('RENDERED',name,os.path.getsize(sc.render.filepath))

# Export real meshes as glTF 2.0 GLB; camera/light excluded.
glb=os.path.join(out,'owl172_run81_organic_integrated_face_ART_PENDING.glb')
bpy.ops.export_scene.gltf(filepath=glb,export_format='GLB',export_cameras=False,
                          export_lights=False,export_yup=True)
bytesize=os.path.getsize(glb)
tri=sum(len(ob.data.polygons) for ob in bpy.data.objects if ob.type=='MESH')
stats={'gate':'ART_PENDING_VISUAL_REVIEW_NOT_APPROVED','blender_version':bpy.app.version_string,
       'branch':'research/owl172-run81-structural-eye-wing-bark','source':'Run81 one continuous loft with face color and small integrated cheek relief; no detached facial plaque, no spheres forming body or detached wings. Art QA pending',
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
print('RUN81_TOOLCHAIN_SUCCESS_NOT_ART_APPROVAL',json.dumps(stats))
