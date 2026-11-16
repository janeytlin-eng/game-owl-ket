#!/usr/bin/env python3
"""Run122: actual no-charge sculpt ablation on Run121's *real re-importable GLB*.
NOT a released owl. The intervention tests continuous facial/shoulder soft sculpt,
inset eyes, slender actual crossed-strand geometry, and a deeper hollow base.
Always re-import GLB for true four-view render; art approval is manual and separate.
"""
import bpy, sys, pathlib, random, math, hashlib, json, traceback
from mathutils import Vector
from math import sin, cos, pi, exp
random.seed(172122)
assert "--" in sys.argv
root=pathlib.Path(sys.argv[sys.argv.index("--")+1])
src=pathlib.Path(sys.argv[sys.argv.index("--")+2])
root.mkdir(parents=True,exist_ok=True)
assert src.is_file() and src.stat().st_size > 1000000
assert src.open("rb").read(4)==b"glTF"
bpy.ops.object.select_all(action="SELECT");bpy.ops.object.delete(use_global=False)
bpy.ops.import_scene.gltf(filepath=str(src))
meshes=[o for o in bpy.context.scene.objects if o.type=="MESH"]
body=max((o for o in meshes if "CONTINUOUS" in o.name.upper()),key=lambda o:len(o.data.vertices))
hair=[o for o in meshes if "CROSSFIBERS" in o.name.upper() or "MESOPTILE CROSS" in o.name.upper()]
print("RUN122_SOURCE",src.name,"body",body.name,"vertices",len(body.data.vertices),"hair",[o.name for o in hair])
assert len(body.data.vertices)>10000 and hair,"Expected original real Run121 sculpt and original fiber mesh"
for o in hair:bpy.data.objects.remove(o,do_unlink=True)
# A/B: keep adult/egg proportions auditable. Small continuous sculpt, no new toy-sphere owl.
for v in body.data.vertices:
    p=v.co; x,y,z=p.x,p.y,p.z
    front=max(0.0,(-y-.24)/.57)
    if front>0 and z>1.23:
        lobes=exp(-((abs(x)-.275)/.20)**2-((z-1.86)/.16)**2)
        valley=exp(-(x/.115)**2-((z-1.94)/.13)**2)
        cheek=exp(-(x/.42)**2-((z-1.39)/.19)**2)
        p.y-=front*(.042*lobes-.020*valley)
        p.x*=1.0+front*(.042*exp(-((z-1.82)/.20)**2)-.065*cheek)
    # Shallow shoulders with no long exposed flight feathers; leaves continuous volume.
    for side in (-1,1):
        w=exp(-((x-side*.59)/.22)**2-((z-1.10)/.30)**2)*exp(-((y+.04)/.65)**2)
        p.x+=side*.025*w
body.data.update()
# Recess eye geometry and tiny catchlights, keeping their relationship with the eyelid.
inset_names=[]
for o in bpy.context.scene.objects:
    if o.type!="MESH":continue
    name=o.name.lower()
    if "deep inset expressive glossy eye" in name:
        o.location.y+=.061
        o.scale*=.82
        inset_names.append(o.name)
    elif "tiny wet eye catchlight" in name:o.location.y+=.075
    elif "small naturally curved horn beak" in name:o.location.y+=.04
# Change overbright white paper hue to warm natural creamy down without a new fake texture.
for m in bpy.data.materials:
    if "layered cream mesoptile" in m.name:
        node=m.node_tree.nodes.get("Principled BSDF") if m.use_nodes else None
        if node:
            col=node.inputs["Base Color"].default_value
            node.inputs["Base Color"].default_value=(col[0]*.92,col[1]*.94,col[2]*.92,1)
            node.inputs["Roughness"].default_value=.99
        m.diffuse_color=(m.diffuse_color[0]*.92,m.diffuse_color[1]*.94,m.diffuse_color[2]*.92,1)
# Hair MUST be real 3D geometry in exported GLB. Slender two-plane cross, not spike ribbons.
downmats=[m for m in bpy.data.materials if "layered cream mesoptile" in m.name]
assert len(downmats)>=4
body.data.calc_loop_triangles()
tri=[t for t in body.data.loop_triangles if .10 < sum(body.data.vertices[i].co.z for i in t.vertices)/3 < 2.13]
assert len(tri)>10000
vlist=[];faces=[];mi=[];hairs=0
for sample in range(10800):
    t=random.choice(tri)
    av=[body.data.vertices[i].co for i in t.vertices]
    a=math.sqrt(random.random());b=random.random()
    q=av[0]*(1-a)+av[1]*(a*(1-b))+av[2]*(a*b)
    if q.y<-.27 and q.z>1.29 and abs(q.x)<.56:continue
    # Avoid burying underneath the tree or directly across eye/lid.
    if q.z<.20:continue
    n=t.normal.normalized()
    if n.length<.5:continue
    if n.z < -.42 and q.z<.35:continue
    L=random.uniform(.014,.041)
    if q.z>1.92:L*=1.05
    d=(n*.80+Vector((random.uniform(-.40,.40),random.uniform(-.40,.40),random.uniform(-.38,.25)))*.42).normalized()
    tan=d.cross(Vector((0,0,1)))
    if tan.length<.08:tan=d.cross(Vector((0,1,0)))
    tan.normalize();tan2=d.cross(tan).normalized()
    fiber_root=q-n*.0025
    radius=random.uniform(.00052,.00122)
    mat_idx=random.choices(range(len(downmats)),weights=[4,7,10,9,8][:len(downmats)])[0]
    for cross in (tan,tan2):
        ids=[]
        for j in range(4):
            u=j/3
            bend=tan2*(.006*sin(pi*u)*random.uniform(.80,1.15))
            center=fiber_root+d*(L*u)+bend+Vector((0,0,-.004*u*u))
            width=radius*(1-u)**.75 + .00006
            ids.extend((len(vlist),len(vlist)+1))
            vlist.extend((tuple(center-cross*width),tuple(center+cross*width)))
        for j in range(3):
            k=ids[2*j]
            faces.append((k,k+1,k+3,k+2));mi.append(mat_idx)
    hairs+=1
me=bpy.data.meshes.new("real glTF cross-silk-down-mesh");me.from_pydata(vlist,[],faces);me.update()
ob=bpy.data.objects.new("run122_actual_soft_tapered_crossfilaments_not_image",me)
bpy.context.collection.objects.link(ob)
for m in downmats:me.materials.append(m)
for i,f in enumerate(me.polygons):f.material_index=mi[i]
print("RUN122_HAIR_COUNT",hairs,"4-quad strands",len(faces))
# Remove run121 pancake ring; reconstruct continuous bark wall / hollow load bearing geometry.
for o in list(bpy.context.scene.objects):
    if o.type=="MESH" and "aged eucalypt tree hollow" in o.name.lower():
        bpy.data.objects.remove(o,do_unlink=True)
barkm=[m for m in bpy.data.materials if "weathered eucalypt" in m.name]
bv=[];bf=[];bm=[]
n=136
profiles=[(.70,.78,.205),(.75,.83,.18),(.77,.85,.08),
          (.77,.88,-.17),(.79,.91,-.39),(.90,1.02,-.53)]
# Knit continuous inner+outer sides, rim at top: real hollow depth, not flat torus.
for ir,(inner,outer,z0) in enumerate(profiles):
    for side,r in enumerate((inner,outer)):
        for k in range(n):
            a=2*pi*k/n
            noise=.016*sin(11*a+ir*.40)+.011*sin(27*a+ir*.23)+.013*sin(19*a)
            r0=r+noise
            bv.append((r0*cos(a),.82*r0*sin(a),z0+.021*sin(8*a)+.013*sin(23*a+ir*.7)))
def idx(row,side,k):return (row*2+side)*n+(k%n)
for row in range(len(profiles)-1):
    for side in (0,1):
        for k in range(n):
            bf.append((idx(row,side,k),idx(row,side,k+1),idx(row+1,side,k+1),idx(row+1,side,k)))
            bm.append((k//8+row+side)%len(barkm))
for row in (0,len(profiles)-1):
    for k in range(n):
        bf.append((idx(row,0,k),idx(row,1,k),idx(row,1,k+1),idx(row,0,k+1)));bm.append(k//8%len(barkm))
wood=bpy.data.meshes.new("sculpted deep eucalypt timber mesh")
wood.from_pydata(bv,[],bf);wood.update()
bark=bpy.data.objects.new("run122_deep_open_tree_hollow_walls_and_rim",wood)
bpy.context.collection.objects.link(bark)
for m in barkm:wood.materials.append(m)
for i,p in enumerate(wood.polygons):p.material_index=bm[i];p.use_smooth=True
# Actual exported GLB, not curve-only Blender beauty render.
objects=[o for o in bpy.context.scene.objects if o.type=="MESH"]
bpy.ops.object.select_all(action="DESELECT")
for o in objects:o.select_set(True)
bpy.context.view_layer.objects.active=body
path=root/"run122_continuous_sculpt_silkdown_organic_juvenile_ART_UNAPPROVED.glb"
bpy.ops.export_scene.gltf(filepath=str(path),export_format="GLB",use_selection=True,export_materials="EXPORT")
assert path.open("rb").read(4)==b"glTF" and path.stat().st_size>500000
for o in objects:bpy.data.objects.remove(o,do_unlink=True)
bpy.ops.import_scene.gltf(filepath=str(path))
real=[o for o in bpy.context.scene.objects if o.type=="MESH"]
tri_count=sum(len(o.data.loop_triangles) for o in real)
assert len(real)>5 and 50000<tri_count<320000
sc=bpy.context.scene;sc.render.engine="CYCLES";sc.cycles.samples=20
for lay in sc.view_layers:lay.cycles.use_denoising=False
sc.render.resolution_x=520;sc.render.resolution_y=520;sc.render.resolution_percentage=100
sc.render.image_settings.file_format="PNG";sc.view_settings.view_transform="Standard"
sc.world.color=(.27,.26,.27)
def area(name,xyz,power,size):
    l=bpy.data.lights.new(name,"AREA");l.energy=power;l.size=size
    o=bpy.data.objects.new(name,l);sc.collection.objects.link(o);o.location=xyz
    o.rotation_euler=(Vector((0,0,1.10))-o.location).to_track_quat("-Z","Y").to_euler()
area("soft key",(-3,-4.5,4.5),450,4.5)
area("gentle fill",(3,-3,3),220,3.5)
area("back rim",(2,3.5,3),320,2.6)
camera=bpy.data.cameras.new("actual imported GLB orbit camera")
ca=bpy.data.objects.new("actual imported GLB orbit camera",camera);sc.collection.objects.link(ca)
sc.camera=ca;camera.type="ORTHO";camera.ortho_scale=2.90
for name,degrees in (("front",0),("quarter",45),("side",90),("back",180)):
    th=math.radians(degrees)
    ca.location=(4.8*sin(th),-4.8*cos(th),1.98)
    ca.rotation_euler=(Vector((0,0,1.02))-ca.location).to_track_quat("-Z","Y").to_euler()
    sc.render.filepath=str(root/("run122_reimported_glb_"+name+"_actual_cycles_ART_REVIEW.png"))
    bpy.ops.render.render(write_still=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
metrics={"run":122,"status":"ART_UNAPPROVED_NO_RELEASE","source":str(src),"source_sha256":sha(src),
"source_type":"real Run121 actual GLB, not SVG, adult owl or still image","new_glb":path.name,
"glb_bytes":path.stat().st_size,"glb_sha256":sha(path),"blender":bpy.app.version_string,
"imported_meshes":len(real),"imported_triangles":tri_count,
"original_spiky_fur_mesh_removed":True,"new_cross_silkdown_strands":hairs,
"eyes_inset":inset_names,"new_deeper_hollow":True,
"soft_groom_vs_image_reference":"NOT_YET_HUMAN_ART_REVIEWED",
"real_phone_test":False,"worldwide_distribution_rights":"original experiment geometry; no commercial deployment review",
"four_true_reimported_glb_views":["front","quarter","side","back"]}
(root/"run122_geometry_run_metrics.json").write_text(json.dumps(metrics,indent=2))
(root/"NO_RELEASE.flag").write_text("ART_UNAPPROVED / NO RELEASE. This is a real GLB but requires manual art judgement, real physical mobile, and future production permission checks.\n")
print("RUN122_REAL_GLB_AND_FOUR_REIMPORT_RENDER_PASS_NO_ART_APPROVAL",json.dumps(metrics))
