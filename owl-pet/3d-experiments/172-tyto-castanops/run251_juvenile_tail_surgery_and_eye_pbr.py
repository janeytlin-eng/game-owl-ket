#!/usr/bin/env python3
"""Run251: actual neural mesh eye PBR repair and level-set juvenile tail surgery.
Research only. Owl is an existing learned native 3D mesh, not primitive assembly.
A = material-only control; B = authentic volumetric posterior excision.
Y up, +Z front. Original learned head, eye geometry and actual surface down retained.
"""
import argparse, hashlib, json
from pathlib import Path
import numpy as np
import scipy.ndimage as ndi
from scipy.spatial import cKDTree
from skimage.measure import marching_cubes
import trimesh

PIN='0b1d83f6b62191edbff2abc037ed3d635b73549ccffeac00c0b7bef02f1af5cc'
CORE='real_neural_owl_juvenile_core'
DOWN='real_3d_surface_following_wispy_down'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def smooth(a,b,x):
    t=np.clip((x-a)/(b-a),0.,1.)
    return t*t*(3-2*t)

def repair_real_eye_materials(scene):
    for side in (0,3):
        for k,color,roughness in [
            (0,[54,36,27,255],.29),
            (1,[9,12,15,255],.12),
            (2,[242,236,220,255],.18)
        ]:
            name=f'sculpt_anatomical_eye_detail_{side+k}'
            assert name in scene.geometry
            mesh=scene.geometry[name]
            mat=trimesh.visual.material.PBRMaterial(
                name='run251_'+('iris' if k==0 else 'dark_pupil' if k==1 else 'glint')+'_nonmetallic',
                baseColorFactor=color,metallicFactor=0.,roughnessFactor=roughness,doubleSided=True)
            mesh.visual=trimesh.visual.TextureVisuals(material=mat)

def cut_posterior_level_set(core,pitch=.019):
    """Carve actual learned 3D volume rather than compressing wings with affine edits.
    Protected upper mask/eyes and the anterior feet remain from the source neural mesh.
    """
    old=core.vertices
    voxel=core.voxelized(pitch).fill()
    pad=14
    base=np.pad(voxel.matrix.astype(np.float32),pad)
    mx=np.arange(base.shape[0],dtype=np.float32)*pitch+voxel.translation[0]-pitch*pad
    my=np.arange(base.shape[1],dtype=np.float32)*pitch+voxel.translation[1]-pitch*pad
    mz=np.arange(base.shape[2],dtype=np.float32)*pitch+voxel.translation[2]-pitch*pad
    x,y,z=np.meshgrid(mx,my,mz,indexing='ij',sparse=True)
    raw=ndi.gaussian_filter(base,1.25)
    t=smooth(-.73,-.28,y)
    z_limit=.055-.59*t
    rear_keep=smooth(z_limit-.11,z_limit+.12,z)
    lower_weight=1-smooth(-.08,.32,y)
    wing_rear=(1-smooth(.07,.39,z))*(1-smooth(.05,.34,y))*smooth(-.70,-.53,y)
    far_side=smooth(.36,.57,np.abs(x))
    keep=np.clip((1-lower_weight)+lower_weight*rear_keep,0,1)
    keep=keep*(1-.36*wing_rear*far_side)
    candidate=ndi.gaussian_filter(raw*keep.astype(np.float32),2.0)
    facial_preserve=smooth(.20,.44,y)*smooth(.27,.53,z)
    field=candidate*(1-facial_preserve)+raw*facial_preserve
    vertices,faces,_,_=marching_cubes(field,level=.45,spacing=(pitch,)*3)
    vertices+=np.array([mx[0],my[0],mz[0]])
    rebuilt=trimesh.Trimesh(vertices=vertices,faces=faces,process=False)
    comps=[g for g in rebuilt.split(only_watertight=False) if len(g.faces)>700]
    assert len(comps)==1,[(len(g.faces),g.is_watertight) for g in comps]
    rebuilt=comps[0]
    if rebuilt.volume<0:rebuilt.invert()
    assert rebuilt.is_watertight and rebuilt.volume>0
    nearest=cKDTree(old).query(rebuilt.vertices,k=1)[1]
    rebuilt.visual=trimesh.visual.TextureVisuals(material=core.visual.material.copy())
    rebuilt.visual.vertex_attributes['color']=core.visual.vertex_attributes['color'][nearest]
    return rebuilt,{
        'old_core_triangles':len(core.faces),
        'core_volume_before':float(core.volume),'core_volume_after':float(rebuilt.volume),
        'new_core_triangles':len(rebuilt.faces),
        'bounds_before':core.bounds.round(4).tolist(),
        'bounds_after':rebuilt.bounds.round(4).tolist(),
        'voxel_grid':list(base.shape),
        'learned_neural_color_vertices':len(rebuilt.vertices),
        'watertight':bool(rebuilt.is_watertight)
    }

def run(src,outdir):
    assert sha(src)==PIN,('source_SHA_mismatch',sha(src))
    outdir=Path(outdir);outdir.mkdir(exist_ok=True,parents=True)
    source=trimesh.load(src,force='scene')
    assert len(source.geometry)==9 and CORE in source.geometry and DOWN in source.geometry
    report={'run':'Run251','source_sha256':PIN,'original':'actual Hunyuan neural 3D',
            'research_only':True,'art_approved':False,'phone_gpu':'UNTESTED',
            'release':'NO_RELEASE','extra_paid_usd':0,'variants':{}}
    for variant in ('A','B'):
        scene=trimesh.load(src,force='scene')
        repair_real_eye_materials(scene)
        facts={'iris_material':'dark umber','pupil_material':'near-black',
               'original_eye_meshes_preserved':6,
               'original_incorrect_eye_material':'pure white'}
        if variant=='B':
            rebuilt,metrics=cut_posterior_level_set(scene.geometry[CORE])
            oldv=scene.geometry[CORE].vertices.copy()
            fur=scene.geometry[DOWN]
            oldfur=fur.vertices.copy()
            src_i=cKDTree(oldv).query(oldfur,k=1)[1]
            dst_i=cKDTree(rebuilt.vertices).query(oldv[src_i],k=1)[1]
            fur.vertices=rebuilt.vertices[dst_i]+np.clip(oldfur-oldv[src_i],-.028,.028)
            scene.geometry[CORE]=rebuilt
            facts.update(metrics)
            facts['actual_down_vertices_transferred']=len(oldfur)
        dst=outdir/f'run251_{variant}_authentic_neural_owl_eye_repair_tail_surgery_NO_RELEASE.glb'
        dst.write_bytes(scene.export(file_type='glb',include_normals=True))
        checked=trimesh.load(dst,force='scene')
        assert len(checked.geometry)==9
        assert len(checked.geometry['sculpt_anatomical_eye_detail_1'].faces)==320
        assert len(checked.geometry[DOWN].faces)==36651
        assert all(np.isfinite(g.vertices).all() for g in checked.geometry.values())
        pupil=checked.geometry['sculpt_anatomical_eye_detail_1'].visual.material
        assert pupil.baseColorFactor[0]<20 and pupil.baseColorFactor[1]<20
        if variant=='B':assert checked.geometry[CORE].is_watertight
        facts.update({'bytes':dst.stat().st_size,'sha256':sha(dst),
            'meshes':len(checked.geometry),
            'triangles':sum(len(g.faces) for g in checked.geometry.values()),
            'file':dst.name,'art_approved':False,'physical_phone_gpu':'UNTESTED'})
        report['variants'][variant]=facts
        print(variant,json.dumps(facts),flush=True)
    (outdir/'run251_geometry_report.json').write_text(json.dumps(report,indent=2)+'\n')

if __name__=='__main__':
    a=argparse.ArgumentParser()
    a.add_argument('--source',required=True)
    a.add_argument('--outdir',required=True)
    b=a.parse_args()
    run(b.source,b.outdir)
