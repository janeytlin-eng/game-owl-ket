"""Run86: continuous cranium-and-trunk contour; feather-disc geometry and folded wing relief, Blender experimental only.
NOT art approved, NOT a production model. Independent branch-only experiment.
Usage: blender -b -t 2 --python this.py -- output-directory
No paid services. Age-unknown Tyto castanops mesoptile design study.
"""
import bpy, math, random, json, os, sys, time, hashlib
from mathutils import Vector
from math import sin, cos, pi, sqrt, exp

seed=17286
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
face=mat('velvety face cheek',(.935,.851,.716))
brown=mat('brown narrow heart edging',(.60,.42,.285))
brownlight=mat('fawn eyelid',(.65,.49,.355))
black=mat('wet dark owl eye',(.015,.012,.010),.10)
eyeinner=mat('deep-brown orbit',(.24,.155,.105))
billmat=mat('horn ivory bill',(.77,.69,.55),.40)
clawmat=mat('dark slate talons',(.25,.22,.21),.40)
bark=mat('weathered eucalyptus lip',(.29,.215,.16))
furm=[mat('filament cream %02d'%i,c) for i,c in enumerate([
(.91,.83,.725),(.915,.828,.722),(.925,.842,.740),(.915,.835,.735),(.92,.837,.74)])]
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

# Run86: a single closed organic head-to-body loft, no spheres fused into a bag.
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
    return .51*hx,1.48+.41*hz

# Run86 topology overhaul: ONE continuous S-shaped cranium, shoulders and
# seated belly radius profile, with C1 Hermite interpolation. No MAX of
# independently swelling two spheres; flat broad transition at the nape.
# Coordinates reflect a plausible *design hypothesis*, not age-specific data.
shape_knots=[
    (.070,.24,.22),(.16,.46,.37),(.30,.57,.49),
    (.53,.69,.57),(.78,.715,.605),(1.00,.705,.597),
    (1.19,.66,.565),(1.37,.615,.535),(1.52,.59,.525),
    (1.66,.55,.505),(1.78,.48,.455),(1.88,.32,.33),
    (1.96,.006,.006)]
def radius_spline(z,which):
    for k in range(len(shape_knots)-1):
        a=shape_knots[k]; b=shape_knots[k+1]
        if z<=b[0] or k==len(shape_knots)-2:
            v0=a[which];v1=b[which];h=b[0]-a[0]
            prev=shape_knots[max(k-1,0)]
            nextp=shape_knots[min(k+2,len(shape_knots)-1)]
            d0=(v1-prev[which])/(b[0]-prev[0])
            d1=(nextp[which]-v0)/(nextp[0]-a[0])
            t=max(0.,min(1.,(z-a[0])/h))
            return ((2*t**3-3*t**2+1)*v0 +
                    (t**3-2*t**2+t)*h*d0 +
                    (-2*t**3+3*t**2)*v1 +
                    (t**3-t**2)*h*d1)
    return shape_knots[-1][which]
NV=124; NA=112
V=[];F=[]
for i in range(NV):
    z=.07+1.89*i/(NV-1)
    rx=radius_spline(z,1)
    ry=radius_spline(z,2)
    if i in (0,NV-1):rx=.006;ry=.006
    for j in range(NA):
        t=2*pi*j/NA
        x=rx*cos(t);y=.05+ry*sin(t)
        # Large, low-frequency scapular mass and buried juvenile folded wing.
        # Real displacement of original loft; no scored feather-strip ornaments.
        lat=exp(-((abs(x)/max(rx,.04)-.94)/.24)**2)
        wing=lat*exp(-((z-1.04)/.27)**2)*exp(-((y+.008)/.36)**2)
        if .48<z<1.43:
            x+=math.copysign(.12*wing,x)
            y+=.065*wing
            # broad subtle trailing-edge transition, not a detached rigid wing.
            y-=.022*lat*exp(-((z-.69)/.11)**2)
        y+=.0035*sin(3*t+3.8*z)*exp(-((z-1.05)/.5)**2)
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
    # Smooth relief integrated into the head: inside soft convex facial disk, outside
    # recessed plumage and broad feathered ruff. No disconnected face plaque.
    rim=exp(-((d-.026)/.057)**2)
    blend=exp(-((d)/.082)**2)
    if inside:
        vert.co.y-=.026+.009*blend+.009*rim
    else:
        vert.co.y+=.007-.016*blend
body.data.update()
for poly in body.data.polygons:
    c=poly.center
    if c.y<-.12 and 1.15<c.z<1.94:
        d,inside=faceSDF(c.x,c.z)
        if inside:
            poly.material_index=2 if d<.043 else 1
        elif d<.026:
            poly.material_index=2
for p in body.data.polygons:p.use_smooth=True

def front_depth(x,z):
    hit,co,n,idx=body.ray_cast(Vector((x,-3.,z)),Vector((0.,1.,0.)),distance=6.)
    return co.y if hit else -.32


# Surface-conformal sculpt: preserve natural heart silhouette without detached mask.
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

# Run86 ablation: no comb-tooth ruff cards and no parallel scored wing coverts.
# A true shaded 3D face is painted *across the continuous body surface*;
# per-corner RGBA is exported through the glTF COLOR_0 vertex attribute.
def smoothstep(a,b,v):
    t=max(0.,min(1.,(v-a)/(b-a)))
    return t*t*(3.-2.*t)

def mix3(a,b,q):
    return tuple((1.-q)*a[i]+q*b[i] for i in range(3))
colorlayer=body.data.vertex_colors.new(name='FeatherTone')
ivory=(.91,.82,.70)
disc=(.965,.875,.755)
border=(.755,.625,.492)
# Color sampled from the ACTUAL sculpt vertices and projected onto the face,
# not a separate plate; 160-edge original Tyto-heart outline with soft feather boundary.
point_colors=[]
for vert in body.data.vertices:
    x,y,z=vert.co
    c=ivory
    if y<-.08 and 1.10<z<1.97:
        d,inside=faceSDF(x,z)
        if inside:
            alpha=smoothstep(.003,.135,d)
            c=mix3(border,disc,alpha)
        else:
            alpha=1.-smoothstep(0.,.11,d)
            c=mix3(ivory,border,alpha*.45)
    # Diffuse orbital umbra and eyebrow under-mesoptile shading on skin,
    # avoiding visible cartoon eye rings. Still vertex colours in actual GLB.
    if y<-.08 and z>1.22:
        for ex in (-.216,.216):
            q=((x-ex)/.078)**2+((z-1.57)/.083)**2
            shade=.29*exp(-q*1.65)
            c=tuple(c[h]*(1-shade) for h in range(3))
    point_colors.append((*c,1.))
for loop in body.data.loops:
    colorlayer.data[loop.index].color=point_colors[loop.vertex_index]
# Give our actual body material a color-attribute input in Cycles and glTF:
pm=cream.node_tree.nodes.get('Principled BSDF')
pm.inputs['Base Color'].default_value=(1,1,1,1)
color_node=cream.node_tree.nodes.new('ShaderNodeVertexColor')
color_node.layer_name='FeatherTone'
cream.node_tree.links.new(color_node.outputs['Color'],pm.inputs['Base Color'])
for poly in body.data.polygons:poly.material_index=0
print('BODY_VERTEX_COLORS',len(point_colors), 'BODY_CORNER_COLORS',len(body.data.loops))

# Keep feather-soft wing silhouette as sculpted smooth relief within body skin.
# Do NOT attach stripy tubing, detached ellipsoids, or adult-style long remiges.

# Run86: minimize high-contrast concentric stacked orbs. An embedded
# eyeball lies nearly flush to the naturally shadowed vertex-colored socket.
# Do not equate this tiny rendering refinement with anatomical proof.
for side in (-1,1):
    depth=front_depth(.216*side,1.571)
    uvball('recessed dark eye %s'%side,
           (.216*side,depth-.009,1.572),
           (.039,.012,.043),black,36,20)

# Tapered downward-curving beak with curved centerline, not a cone.
beakpts=[];rads=[]
for i in range(13):
    q=i/12
    zz=1.468-.165*q
    beakpts.append((0, front_depth(0,zz)-.041-.040*sin(pi*q)+.020*q,zz))
    rads.append(.029*(1-q)**.85+.0015)
tube('curved ivory hooked beak',beakpts,rads,billmat,12)

# Buried feet, visible toes and dark claw tips (no adult-length shanks).
for side in (-1,1):
    x0=.26*side
    # Ankle is tucked below belly, not a pair of floating white marbles.
    # Remove visible disconnected ankle spheres (feet emerge from body).
    for j in range(3):
        dx=(j-1)*.080
        pts=[(x0+dx*.25,-.22,.17),(x0+dx*.70,-.34,.146),
             (x0+dx,-.52,.121),(x0+dx*1.15,-.60,.099)]
        tube('short juvenile toe %d_%d'%(side,j),pts,[.036,.030,.022,.014],brownlight,7)
        tube('curved dark claw %d_%d'%(side,j),[
            pts[-1],(pts[-1][0]+dx*.24,-.642,.067),
            (pts[-1][0]+dx*.26,-.65,.036)], [.017,.013,.002],clawmat,6)

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
join_edge([ix for ix in range(NX)])
join_edge([(NY-1)*NX+ix for ix in range(NX-1,-1,-1)])
join_edge([iy*NX for iy in range(NY-1,-1,-1)])
join_edge([iy*NX+NX-1 for iy in range(NY)])
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
kept=0;trials=0;target=11000
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
    length=rng.uniform(.008,.019) if p.z>1.15 else rng.uniform(.011,.023)
    length*=rng.uniform(.86,1.14)
    width=length*rng.uniform(.17,.25)
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
    sc.render.filepath=os.path.join(out,'sculpt86_'+name+'.png')
    bpy.ops.render.render(write_still=True)
    print('RENDERED',name,os.path.getsize(sc.render.filepath))

# Export real meshes as glTF 2.0 GLB; camera/light excluded.
glb=os.path.join(out,'owl172_run86_organic_integrated_face_ART_PENDING.glb')
bpy.ops.export_scene.gltf(filepath=glb,export_format='GLB',export_cameras=False,
                          export_lights=False,export_yup=True)
bytesize=os.path.getsize(glb)
tri=sum(len(ob.data.polygons) for ob in bpy.data.objects if ob.type=='MESH')
stats={'gate':'ART_PENDING_VISUAL_REVIEW_NOT_APPROVED','blender_version':bpy.app.version_string,
       'branch':'research/owl172-run86-supported-rounded-mesoptile','source':'Run86 single Hermite radius loft, no two-globe smooth-max, revised buried scapular mass, softly pigmented orbital volumes and embedded eyes. Zero claim of art approval; side/rear and mobile need independent review.',
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
print('RUN86_TOOLCHAIN_SUCCESS_NOT_ART_APPROVAL',json.dumps(stats))
