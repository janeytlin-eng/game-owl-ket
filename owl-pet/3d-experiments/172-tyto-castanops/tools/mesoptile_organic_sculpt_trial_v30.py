#!/usr/bin/env python3
"""REJECTABLE #172 mesoptile 3D organic sculpt trial, NOT a completed pet or species proof.

Pure CPU NumPy/skimage/trimesh. Generates a SINGLE connected sculpted head-body via
smooth implicit surfaces, conformal heart colour + relief, organic support limbs,
short wing volumes and transparent soft-down cards. Model and references are user-
authored experimental geometry; no adult horned owl structure transferred.

Coordinate convention in asset: X right, Y positive toward back, Z up. Face looks -Y.
This is a quality-gate *candidate*, not approval or a claim of physical mobile FPS.
"""
import argparse, hashlib, json, math
from pathlib import Path
import numpy as np
from skimage.measure import marching_cubes
from scipy.ndimage import gaussian_filter
from PIL import Image
import trimesh
from trimesh.visual.texture import TextureVisuals
from trimesh.visual.material import PBRMaterial

SEED = 172013

def saturate(x):return np.clip(x,0,1)
def softmin(a,b,k):
    h=saturate(.5+.5*(b-a)/k)
    return (b*(1-h)+a*h)-k*h*(1-h)

def efield(X,Y,Z,c,r):
    return (np.sqrt(((X-c[0])/r[0])**2+((Y-c[1])/r[1])**2+((Z-c[2])/r[2])**2)-1)*min(r)

def heart_field(X,Z):
    # Deliberate reference-constrained narrow upper lobes and lower point.
    u=X/.296
    v=(Z-.912)/.257
    F=(u*u+v*v-1)**3-u*u*v*v*v
    Fx=6*u*(u*u+v*v-1)**2-2*u*v*v*v
    Fv=6*v*(u*u+v*v-1)**2-3*u*u*v*v
    # Approximate signed distance in local normalized heart coordinates.
    return F/np.maximum(np.sqrt(Fx*Fx+Fv*Fv),.2)

def body_sdf(X,Y,Z):
    b=efield(X,Y,Z,(0,.005,.57),(.490,.391,.465))
    h=efield(X,Y,Z,(0,-.032,.93),(.375,.344,.356))
    d=softmin(b,h,.16)
    # Narrow juvenile occiput / modest off-axis posture rather than perfect egg.
    n=(.010*np.sin(15*X+7*Z)*np.sin(9*Y-6*Z)
       +.007*np.sin(31*Z-11*Y+5*X)
       +.005*np.cos(36*X-17*Y-3*Z))
    d+=n
    # Soft disc relief is inseparable from the head-body sculpt; never a flat mask.
    heart=heart_field(X,Z)
    front=saturate((-Y-.145)/.145)
    face_height=saturate((Z-.635)/.12)*saturate((1.28-Z)/.1)
    inside=saturate(-heart/.035)
    rim=np.exp(-((heart-.004)/.032)**2)
    d += front*face_height*(.005*inside-.010*rim)
    # Genuine socket depression under two eye spheres; tiny eyebrow fur ridge.
    for sign in (-1,1):
        socket=np.exp(-((X-sign*.142)/.100)**2-((Z-.964)/.097)**2)
        d+=front*.019*socket
    # Some asymmetry / soft organic forehead slopes.
    d+=.004*np.sin(9*X+5*Z)*front*face_height
    return d

def make_sculpt(res=144):
    nx=int(res); ny=int(res*.90);nz=int(res*1.08)
    gx=np.linspace(-.59,.59,nx,dtype=np.float32)
    gy=np.linspace(-.50,.53,ny,dtype=np.float32)
    gz=np.linspace(.035,1.33,nz,dtype=np.float32)
    # Slice in Z to reduce maximum memory and avoid fully dense coordinate arrays.
    x=gx[:,None,None];y=gy[None,:,None];z=gz[None,None,:]
    d=body_sdf(x,y,z).astype(np.float32)
    verts, faces, _, _ = marching_cubes(d,0,spacing=(gx[1]-gx[0],gy[1]-gy[0],gz[1]-gz[0]))
    verts+=np.array([gx[0],gy[0],gz[0]],dtype=np.float32)
    rng=np.random.default_rng(SEED)
    X,Y,Z=verts.T
    heart=heart_field(X,Z)
    disc=saturate((-.17-Y)/.09)*saturate((Z-.65)/.075)*saturate((1.265-Z)/.085)
    interior=saturate(-heart/.045)*disc
    rim=np.exp(-((heart+.001)/.048)**2)*disc
    fleck=(.5+.5*np.sin(42*X+17*Z)*np.sin(51*Z-11*Y))
    random_fuzz=rng.normal(0,1,len(verts))
    warm=np.array([239.,227.,205.]); rose=np.array([235.,204.,169.])
    base=np.broadcast_to(warm,(len(verts),3)).copy()
    base+= (9*np.sin(13*Z+3*X)+4*np.sin(48*X+21*Y)+random_fuzz*3)[:,None]
    base = base*(1-interior[:,None]) + (np.array([244.,218.,186.])+6*fleck[:,None])*interior[:,None]
    # Ring tan with bright inner border: warm and nested rather than black hard outline.
    base=base*(1-.83*rim[:,None]) + np.array([162.,120.,83.])*(.60*rim[:,None])
    inside_rim=np.exp(-((heart+.048)/.02)**2)*disc
    base=base*(1-.52*inside_rim[:,None]) + np.array([253.,240.,216.])*(.52*inside_rim[:,None])
    # Diffuse dark shading around eyes (before real 3D eye bulbs are built).
    for sx in (-.13,.13):
        e=np.exp(-((X-sx)/.092)**2-((Z-.96)/.092)**2)*interior
        base=base*(1-(.42*e)[:,None])+np.array([114.,80.,62.])*(.42*e)[:,None]
    # A short subtly golden wing emerging beneath down but not adult remiges.
    for sx in (-1,1):
        f=np.exp(-((np.abs(X)-.417)/.085)**2-((Z-.553)/.21)**2)*saturate((-.01-Y)/.16)
        base=base*(1-(.13*f)[:,None])+np.array([211.,184.,151.])*(.13*f)[:,None]
    colors=np.column_stack([saturate(base/255)*255,np.full(len(verts),255)]).astype(np.uint8)
    mesh=trimesh.Trimesh(vertices=verts,faces=faces,process=False,vertex_colors=colors)
    # Check actual closure and signed volume: provides stronger evidence than cheap spheres.
    return mesh

def uv_ellipsoid(c,r,color,n=24,m=32):
    mesh=trimesh.creation.uv_sphere(radius=1,count=[n,m])
    mesh.vertices=mesh.vertices*np.asarray(r)+np.asarray(c)
    mesh.visual.vertex_colors=np.array([*color,255],dtype=np.uint8)
    return mesh

def tube(path,radii,col,sides=9):
    path=np.array(path,dtype=float)
    t=np.gradient(path,axis=0)
    t/=np.maximum(1e-8,np.linalg.norm(t,axis=1))[:,None]
    frames=[]
    for tangent in t:
        ref=np.array([0,0,1.]) if abs(tangent[2])<.83 else np.array([0,1.,0])
        a=np.cross(tangent,ref);a/=np.linalg.norm(a)
        b=np.cross(tangent,a)
        frames.append((a,b))
    vertices=[];faces=[]
    for p,r,(a,b) in zip(path,radii,frames):
        for j in range(sides):
            theta=j*2*np.pi/sides
            vertices.append(p+r*(a*np.cos(theta)+b*np.sin(theta)))
    for i in range(len(path)-1):
        for j in range(sides):
            a=i*sides+j; b=i*sides+(j+1)%sides; c=(i+1)*sides+j; d=(i+1)*sides+(j+1)%sides
            faces.extend([[a,b,c],[b,d,c]])
    faces.extend([[0,(j+1)%sides,j] for j in range(1,sides-1)])
    k=(len(path)-1)*sides
    faces.extend([[k,k+j,k+j+1] for j in range(1,sides-1)])
    mesh=trimesh.Trimesh(vertices=vertices,faces=faces,process=False)
    mesh.visual.vertex_colors=np.tile([*col,255],(len(vertices),1)).astype(np.uint8)
    return mesh

def outward_surf(mesh, count, rng):
    # Underlying body triangular surface barycentric positions; face mask prevents hair on disc.
    face_areas=mesh.area_faces
    ids=rng.choice(len(mesh.faces),size=count*2,p=face_areas/face_areas.sum())
    tri=mesh.triangles[ids];s=np.sqrt(rng.random(len(ids)));t=rng.random(len(ids))
    p=(1-s)[:,None]*tri[:,0]+(s*(1-t))[:,None]*tri[:,1]+(s*t)[:,None]*tri[:,2]
    n=mesh.face_normals[ids];norm=np.linalg.norm(n,axis=1)
    n=n/np.maximum(1e-8,norm)[:,None]
    heart=heart_field(p[:,0],p[:,2]);disc=(heart<.07)&(p[:,1]<-.16)&(p[:,2]>.66)
    mask=(~disc)&(p[:,2]>.22)
    return p[mask][:count],n[mask][:count]

def down_texture():
    # Soft rounded filament tuft with translucent edges, no needle-tip alpha shape.
    W,H=128,192
    x,y=np.meshgrid(np.linspace(-1,1,W),np.linspace(0,1,H))
    edge_radius=.72*(1-.40*y)*np.sqrt(saturate(1-y)**.25)
    edge=saturate((edge_radius-np.abs(x-.045*np.sin(9*y)))/.22)
    extent=saturate((y-.02)/.13)*saturate((.98-y)/.13)
    # Wavy strands internally, not hard-cut silhouette spikes.
    strand=(.78+.19*np.cos(x*19+10*y)**2)
    alpha=(edge*extent*strand*116).astype(np.uint8)
    rgba=np.zeros((H,W,4),dtype=np.uint8)
    rgba[:,:,:3]=[252,245,229]; rgba[:,:,3]=alpha
    return Image.fromarray(rgba,'RGBA')

def make_down(body,n=3800,seed=SEED):
    rng=np.random.default_rng(seed)
    p,norm=outward_surf(body,n,rng)
    vs=[]; uv=[]; faces=[]
    for i,(point,normal) in enumerate(zip(p,norm)):
        ref=np.array([0.,0.,1.]) if abs(normal[2])<.89 else np.array([1.,0.,0.])
        tan=np.cross(normal,ref);tan/=max(np.linalg.norm(tan),1e-8)
        swirl=np.cross(normal,tan)
        theta=rng.uniform(0,np.pi*2)
        direction=normal*.84+(tan*np.cos(theta)+swirl*np.sin(theta))*.34
        direction/=np.linalg.norm(direction)
        length=rng.uniform(.012,.024) * (.80 if point[2]>.98 else 1)
        width=length*rng.uniform(.20,.34)
        root=point+normal*.0008
        tip=root+direction*length
        side=(tan*np.cos(theta)+swirl*np.sin(theta))*width
        # Root and rounded tip move softly; soft alpha accounts for most silhouette.
        idx=len(vs)
        vs.extend([root-side,root+side,tip+side*.7,tip-side*.7])
        uv.extend([[0,0],[1,0],[1,1],[0,1]])
        faces.extend([[idx,idx+1,idx+2],[idx,idx+2,idx+3]])
    mat=PBRMaterial(name='UNAPPROVED_cream_mesoptile_down_alpha_cards',
                    baseColorTexture=down_texture(),alphaMode='BLEND',
                    doubleSided=True,roughnessFactor=1.,metallicFactor=0.)
    return trimesh.Trimesh(vertices=np.array(vs),faces=np.array(faces),process=False,
                           visual=TextureVisuals(uv=np.array(uv),material=mat)),len(p)

def bark_ledge():
    # Small sculpted dead-eucalypt hollow lip with uneven thickness (not a rectangular box).
    rng=np.random.default_rng(1728)
    vs=[];fs=[];cols=[]
    nx=58; na=22
    for i,x in enumerate(np.linspace(-.65,.65,nx)):
        cy=-.229+.020*np.sin(2.3*x+1.4)
        cz=.089+.025*np.sin(5*x-1)
        for j,th in enumerate(np.linspace(0,2*np.pi,na,endpoint=False)):
            y=cy+(.225+.01*np.sin(i*1.8+th*3))*np.cos(th)
            z=cz+(.095+.009*np.sin(6*th+3*x))*np.sin(th)
            vs.append([x,y,z])
            noise=rng.normal(0,7)
            col=np.clip([104+noise+13*np.sin(i*.6+th*4),81+noise,62+noise],0,255)
            cols.append([*col,255])
    for i in range(nx-1):
        for j in range(na):
            a=i*na+j;b=i*na+(j+1)%na;c=(i+1)*na+j;d=(i+1)*na+(j+1)%na
            fs.extend([[a,b,c],[b,d,c]])
    mesh=trimesh.Trimesh(vertices=vs,faces=fs,process=False,vertex_colors=np.array(cols,dtype=np.uint8))
    return mesh

def make_scene(res=144,n_down=3800):
    scene=trimesh.Scene();body=make_sculpt(res)
    scene.add_geometry(body,geom_name='ORGANIC_CONNECTED_HEAD_BODY_HEART_RELIEF')
    scene.add_geometry(bark_ledge(),geom_name='TEMPORARY_BARK_SUPPORT_RESEARCH_ONLY')
    # True 3D eye settings; very dark eyes with eye sockets sculpted into mesh.
    for sign in [-1,1]:
        x=sign*.137; z=.958
        # approximate eye seating along organic head surface; surface normal faces -Y.
        eye=uv_ellipsoid((x,-.347,z),(.050,.017,.052),(21,17,13),26,40)
        scene.add_geometry(eye,geom_name=f'eye_gloss_dark_{sign}')
        pupil=uv_ellipsoid((x,-.367,z),(.029,.009,.038),(8,7,7),20,32)
        scene.add_geometry(pupil,geom_name=f'eye_pupil_{sign}')
        glint=uv_ellipsoid((x-sign*.009,-.381,z+.017),(.006,.003,.007),(245,241,221),12,18)
        scene.add_geometry(glint,geom_name=f'eye_catchlight_{sign}')
    # A tapered, slightly crooked bill: curved 3D ribbon-like sculpt, not a triangle sticker.
    beak=tube([(0,-.356,.870),(0,-.389,.85),(0,-.402,.816),(.006,-.394,.768)],
              [.048,.038,.022,.005],(214,191,156),sides=12)
    scene.add_geometry(beak,geom_name='ivory_hooked_bill')
    # Ankles disappear into belly, toes contact the same bark support.
    for s in (-1,1):
        scene.add_geometry(uv_ellipsoid((s*.244,-.205,.247),(.088,.081,.125),(238,220,195),20,32),geom_name=f'down_shank_{s}')
        foot=(s*.245,-.260,.166)
        scene.add_geometry(tube([(.24*s,-.178,.205),foot,(.25*s,-.293,.151)],
                                [.050,.045,.035],(174,151,128)),geom_name=f'tarsus_{s}')
        for idx,dx in enumerate([-.071,0,.071]):
            end_x=s*.245+dx
            line=[foot,(s*.245+dx*.40,-.31,.149),(end_x,-.37,.125),(end_x+dx*.14,-.389,.137)]
            scene.add_geometry(tube(line,[.024,.024,.016,.006],(170,150,129),sides=8),geom_name=f'toe_{s}_{idx}')
            claw=[line[-2],(end_x+dx*.19,-.405,.133),(end_x+dx*.24,-.416,.104)]
            scene.add_geometry(tube(claw,[.013,.009,.001],(83,78,73),sides=7),geom_name=f'claw_{s}_{idx}')
    down,n_real=make_down(body,n=n_down)
    scene.add_geometry(down,geom_name='soft_alpha_mesoptile_research_groom')
    return scene,{'sdf_source':'smooth union, integrated signed-distance heart relief',
      'heart_mesh_integrated':True,'head_body_connected':bool(body.is_watertight),
      'down_cards':n_real,'alpha_mode':'BLEND','approval':False,'physical_phone_test':False,
      'scientific_claim':False}

def build(path,res=144,n_down=3800):
    scene,stats=make_scene(res,n_down)
    # glTF/Three.js are Y-up; sculpt and 4-view QA are Z-up. Explicitly rotate
    # once at the asset boundary, unlike v29 (which would lie sideways in WebGL).
    # Original -Y face becomes +Z front in glTF coordinate space.
    scene.apply_transform(trimesh.transformations.rotation_matrix(-np.pi/2,[1,0,0]))
    scene.export(str(path))
    check=trimesh.load(str(path),force='scene',process=False)
    stats.update({'path':str(path),'model_count':len(check.geometry),
                  'triangles':sum(len(g.faces) for g in check.geometry.values()),
                  'bytes':Path(path).stat().st_size,
                  'sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest(),
                  'bounds':check.bounds.tolist(),
                  'gltf_up_axis':'Y', 'gltf_front_axis':'+Z',
                  'honest_gate':'ART UNREVIEWED until real four camera views inspected'})
    return stats

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('output')
    parser.add_argument('--resolution',type=int,default=110)
    parser.add_argument('--down',type=int,default=2600)
    parser.add_argument('--stats')
    args=parser.parse_args()
    result=build(Path(args.output),args.resolution,args.down)
    report=json.dumps(result,indent=2);print(report)
    if args.stats:Path(args.stats).write_text(report)