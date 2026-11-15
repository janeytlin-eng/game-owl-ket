"""#172 Run87B anatomical mesh transfer experiment: existing artist-made CC0
adult horned-owl mesh, *not* a new species-certified Tyto castanops model.
Remove adult flight/ear features, modify ALL retained 3D topology towards an
age-unknown mesoptile and test cream texture / face coloration. May fail art.
Do not present or deploy the result without multi-angle independent QA.
"""
import bpy, math, hashlib, json, os, sys, numpy as np
from mathutils import Vector
from math import sin,cos,pi,sqrt,exp

src=sys.argv[sys.argv.index('--')+1]
out=sys.argv[sys.argv.index('--')+2]
os.makedirs(out,exist_ok=True)
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=src)
meshes=[o for o in bpy.data.objects if o.type=='MESH']
assert len(meshes)>100
removed=[]
# Adult great-horned features are directly contradictory to the requested
# baby masked owl: remove BOTH tufts, all adult remiges and exposed adult tail.
for ob in list(meshes):
    n=ob.name.lower()
    if any(t in n for t in ['feather tuft','tail rectrix','closed flight feather','layered wing covert']):
        removed.append(ob.name)
        bpy.data.objects.remove(ob,do_unlink=True)
meshes=[o for o in bpy.data.objects if o.type=='MESH']
assert len(removed)>50
headbody=[o for o in meshes if 'great horned owl continuous thick body neck' in o.name.lower()]
assert len(headbody)==1

def morph(p):
    # Original glTF world axes as imported by Blender: +X points toward beak,
    # Z is up, Y is the transverse axis. Morph is continuous in 3D and applies
    # to source sculpt, beak, eyes and feet, rather than independent doll parts.
    x,y,z=p
    head=1./(1.+math.exp(-((z-.28)/.030)))
    trans=1.26+0.13*head
    x=(x+.010)*(.98-.07*head)-.010
    y=y*trans
    z=.830*z
    return Vector((x,y,z))
# Apply same world deformation to each 3D component, preserving placement.
for ob in meshes:
    mw=ob.matrix_world.copy()
    inv=mw.inverted()
    iswing='cambered folded wing foundation' in ob.name.lower()
    isbill=any(t in ob.name.lower() for t in ['closed descending upper hook','short lower mandible'])
    for v in ob.data.vertices:
        p=mw@v.co
        if iswing:
            # Source adult folded wing replaced by a genuinely short wing bud,
            # its structure remains a 3D mesh beneath the down-covered body.
            sign=1 if p.y>=0 else -1
            shoulder=Vector((-.025,sign*.078,.278))
            p=shoulder+(p-shoulder)*.49
        if isbill:
            base=Vector((.112,0,.365))
            p=base+(p-base)*.74
        v.co=inv@morph(p)
    ob.data.update()

# A broad facial-disc region embedded into a preexisting fully sculpted mesh,
# NOT a separate plate, ellipsoid, SVG or raster front card. The original
# artist has modelled real 3D wing folds, eyes and feet. This is only a test.
body=headbody[0]
def heart_points():
    P=[]
    for k in range(128):
        t=2*pi*k/128.
        x=16*sin(t)**3/18.
        zz=(13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t))/18.
        P.append((.121*x,.295+.085*zz))
    return P
hp=heart_points()
def proximity(y,z):
    inside=False;closest=3.
    for i in range(len(hp)):
        ay,az=hp[i];by,bz=hp[(i+1)%len(hp)]
        dy=by-ay;dz=bz-az
        t=max(0.,min(1.,((y-ay)*dy+(z-az)*dz)/(dy*dy+dz*dz+1e-12)))
        closest=min(closest,sqrt((y-ay-t*dy)**2+(z-az-t*dz)**2))
        if (az>z)!=(bz>z) and y<(by-ay)*(z-az)/(bz-az)+ay: inside=not inside
    return closest,inside
# Avoid an artificial hard forehead mask by feather-tonal variation and
# very shallow same-surface sculpt relief, declining at the rim.
mask=[]
mw=body.matrix_world.copy();inv=mw.inverted()
for v in body.data.vertices:
    p=mw@v.co
    if p.x>.06 and p.z>.20:
        d,inside=proximity(p.y,p.z)
        w=exp(-(d/.030)**2)
        if inside:p.x+=.003*w
        else:p.x-=.002*w
        v.co=inv@p
        mask.append((d,inside,p.x,p.z))
    else:mask.append((1.,False,p.x,p.z))
body.data.update()

# Keep original authored PBR normal maps and 2K high-frequency texture.
# Tint albedo images in place using NumPy (actual texture channels), rather
# than painting cream onto a colorless primitive.
color_done=[]
for image in list(bpy.data.images):
    if image.type!='IMAGE' or not image.has_data:continue
    nm=image.name.lower()
    if not any(t in nm for t in ['basecolor']):continue
    if 'normal' in nm:continue
    npx=image.size[0]*image.size[1]
    pix=np.empty(npx*4,dtype=np.float32);image.pixels.foreach_get(pix)
    px=pix.reshape(-1,4)
    g=.20*px[:,0]+.66*px[:,1]+.14*px[:,2]
    factor=np.clip(.78+.26*g,.72,1.02)
    px[:,:3]=factor[:,None]*np.array([.96,.877,.757],dtype=np.float32)
    image.pixels.foreach_set(pix)
    image.update()
    color_done.append(image.name)
# Original golden iris should NOT persist on a Tyto chick. Acknowledge that
# a material darkening cannot fix anatomical non-matching periorbital shapes.
for mat in bpy.data.materials:
    if 'golden iris' in mat.name.lower():
        bs=mat.node_tree.nodes.get('Principled BSDF') if mat.use_nodes else None
        if bs:
            for l in list(bs.inputs['Base Color'].links):
                mat.node_tree.links.remove(l)
            bs.inputs['Base Color'].default_value=(.043,.030,.021,1.)
            bs.inputs['Roughness'].default_value=.22

# Vertex color interpolation inside the source skull rather than a plaster
# heart overlay. Retain actual 3D surface, no extra face geometry generated.
vcolors=body.data.vertex_colors.new(name='Run87BabyDiscTone')
point=[]
for v,(d,inside,xx,zz) in zip(body.data.vertices,mask):
    c=np.array([1.,1.,1.],dtype=np.float32)
    if xx>.060 and zz>.195:
        if inside:
            sep=np.clip(d/.013,0.,1.)
            edge=np.array([.65,.45,.33],dtype=np.float32)
            inner=np.array([.98,.91,.82],dtype=np.float32)
            c=edge*(1-sep)+inner*sep
        elif d<.022:
            f=np.clip(d/.022,0.,1.)
            c=np.array([.76,.60,.47],dtype=np.float32)*(1-f)+c*f
    point.append(tuple(float(i) for i in c)+(1.,))
for loop in body.data.loops:vcolors.data[loop.index].color=point[loop.vertex_index]
for mat in body.data.materials:
    if not mat.use_nodes:continue
    bs=mat.node_tree.nodes.get('Principled BSDF')
    if bs is None:continue
    existing=bs.inputs['Base Color'].links[:]
    atr=mat.node_tree.nodes.new('ShaderNodeVertexColor')
    atr.layer_name='Run87BabyDiscTone'
    mix=mat.node_tree.nodes.new('ShaderNodeMixRGB')
    mix.blend_type='MULTIPLY';mix.inputs[0].default_value=1.
    if existing:
        link=existing[0]
        mat.node_tree.links.new(link.from_socket,mix.inputs[1])
        mat.node_tree.links.remove(link)
    else:mix.inputs[1].default_value=(.96,.87,.76,1.)
    mat.node_tree.links.new(atr.outputs['Color'],mix.inputs[2])
    mat.node_tree.links.new(mix.outputs[0],bs.inputs['Base Color'])

# Render true camera rotation around source artist's retained topology.
allverts=[o.matrix_world@v.co for o in meshes for v in o.data.vertices]
mn=Vector([min(q[i] for q in allverts) for i in range(3)])
mx=Vector([max(q[i] for q in allverts) for i in range(3)])
cen=(mn+mx)/2
extent=max(mx-mn)
world=bpy.context.scene.world
if not world:world=bpy.data.worlds.new('Studio');bpy.context.scene.world=world
world.use_nodes=True
world.node_tree.nodes.get('Background').inputs['Color'].default_value=(.32,.34,.35,1)
world.node_tree.nodes.get('Background').inputs['Strength'].default_value=.65
for ob in list(bpy.data.objects):
    if ob.type in {'LIGHT','CAMERA'}:bpy.data.objects.remove(ob,do_unlink=True)
for name,loc,energy,size in [
    ('key',(.7,-.8,1.2),230,1.7),
    ('fill',(.5,.9,.95),135,1.4),
    ('rim',(-.8,.5,1.),190,1.6)]:
    bpy.ops.object.light_add(type='AREA',location=loc)
    l=bpy.context.object;l.name=name;l.data.energy=energy
    l.data.shape='DISK';l.data.size=size
    l.rotation_euler=(cen-l.location).to_track_quat('-Z','Y').to_euler()
bpy.ops.object.camera_add()
cam=bpy.context.object;cam.name='run87b four-view';bpy.context.scene.camera=cam
cam.data.type='ORTHO';cam.data.ortho_scale=extent*1.50
scene=bpy.context.scene
scene.render.engine='CYCLES';scene.cycles.samples=24
bpy.context.view_layer.cycles.use_denoising=False
scene.render.resolution_x=600;scene.render.resolution_y=600
scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG'
scene.view_settings.view_transform='Standard';scene.view_settings.exposure=-.65
for name,loc in [
    ('front',(2,0,.35)),('threequarter',(1.7,-1.5,.40)),
    ('side',(0,-2,.36)),('back',(-2,0,.35))]:
    cam.location=cen+Vector(loc)
    cam.rotation_euler=(cen-cam.location).to_track_quat('-Z','Y').to_euler()
    scene.render.filepath=os.path.join(out,'transferred_juvenile_'+name+'.png')
    bpy.ops.render.render(write_still=True)
    print('RENDER_TRUE_RESHAPED_3D',name,os.path.getsize(scene.render.filepath))

glb=os.path.join(out,'owl172_run87b_cc0_anatomy_transfer_ART_REJECTED_PENDING.glb')
bpy.ops.export_scene.gltf(filepath=glb,export_format='GLB',export_cameras=False,export_lights=False)
sha=hashlib.sha256(open(glb,'rb').read()).hexdigest()
assert open(glb,'rb').read(4)==b'glTF'
nfaces=sum(len(o.data.polygons) for o in meshes)
assert len(meshes)>10 and nfaces>20000
stats={'verdict':'ART_PENDING_INDEPENDENT_REVIEW_NOT_APPROVED',
       'original_species':'great horned owl general model not target species',
       'source_license_claim':'CC0 on Innerscene; verify ownership prior to product',
       'meshes_retained':len(meshes),'removed_adult_feature_meshes':len(removed),
       'retained_original_authored_fine_mesh_3d':True,
       'textures_tinted':color_done,
       'raw_blender_faces_before_export':nfaces,
       'sha256':sha,'bytes':os.path.getsize(glb),
       'provenance_source_sha256':hashlib.sha256(open(src,'rb').read()).hexdigest(),
       'physical_mobile_gpu_test':False,'PBR_parity_test':False,'animations':False,
       'four_original_cycles_views':['front','threequarter','side','back']}
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=glb)
stats['reimport_meshes']=len([o for o in bpy.data.objects if o.type=='MESH'])
assert stats['reimport_meshes']>10
with open(os.path.join(out,'candidate_metrics.json'),'w') as f:json.dump(stats,f,indent=2)
print('RUN87B_EXPORTED_REAL_3D_NOT_ART_APPROVED',json.dumps(stats))
