#!/usr/bin/env python3
"""Run282c research only: authentic reference-bound TripoSR neural mesh ->
connected-component cleanup -> voxel level-set organic retopology -> textured
true 3D glTF. Neither a primitive stand-in nor a production-approved model.
"""
import json,sys,pathlib
import numpy as np
import trimesh
from PIL import Image
from scipy.ndimage import gaussian_filter,binary_closing,binary_fill_holes
from skimage.measure import marching_cubes
from run281_triposr_cpu_juvenile_reference_NO_RELEASE import qa,sha
SOURCE='46f22943806075ec749d96f1bafa630fee256a02e6048839c428101fc9c12e12'
REFERENCE='8eee63bf0b8650c390d4c4bba6a07a0c2dd05dd7fc2e90e00a896ec3ab51c641'

def main(src,ref,out):
    src=pathlib.Path(src);ref=pathlib.Path(ref);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True)
    assert sha(src)==SOURCE and sha(ref)==REFERENCE, 'Verified previous real 3D mesh and actual source photo ONLY'
    obj=next(iter(trimesh.load(src,force='scene').geometry.values()))
    assert len(obj.faces)==103084 and len(obj.vertices)==51795, 'Never substitute fake primitives'
    components=sorted(obj.split(only_watertight=False),key=lambda m:len(m.faces),reverse=True)
    base=components[0];assert len(base.faces)==100534
    vox=base.voxelized(.007).fill()
    assert vox.matrix.sum()>100000
    grid=np.pad(vox.matrix,4)
    field=binary_fill_holes(binary_closing(grid,iterations=2)).astype('float32')
    back=np.empty((512,512,3),dtype=np.uint8)
    rng=np.random.default_rng(172282)
    n=gaussian_filter(rng.normal(size=(512,512)),7);n/=n.std()
    back[:]=np.clip(np.array([233,220,202])[None,None,:]+n[:,:,None]*2.4,0,255).astype('uint8')
    atlas=Image.new('RGB',(1024,512));atlas.paste(Image.open(ref).convert('RGB'),(0,0));atlas.paste(Image.fromarray(back),(512,0))
    atlas.save(out/'original_front_neutral_back_atlas_RESEARCH.png')
    report={'source_sha256':sha(src),'source_image_sha256':sha(ref),'source_faces':len(obj.faces),
            'kept_connected_component_faces':len(base.faces),'removed_artifact_faces':len(obj.faces)-len(base.faces),
            'volumetric_method':'authentic TripoSR surface voxel .007, fill, close, gaussian, marching cubes',
            'variants':{},'art':'UNREVIEWED_NO_RELEASE','mobile_gpu':'NOT_TESTED','rights':'SOURCE_CONCEPT_REVIEW_REQUIRED'}
    for sigma in [1.5,3.0]:
        smooth=gaussian_filter(field,sigma)
        vertices,faces,_,_=marching_cubes(smooth,.47)
        vertices=trimesh.transform_points(vertices-4,vox.transform)
        mesh=trimesh.Trimesh(vertices=vertices,faces=faces,process=False)
        if mesh.volume<0:mesh.invert()
        assert mesh.is_watertight and len(mesh.faces)>50000
        v=mesh.vertices;norm=mesh.vertex_normals
        xp=np.clip((250+390*v[:,0])/512,.005,.995)
        yp=np.clip((257-450*v[:,1])/512,.005,.995)
        # Known artistic limitation: normal-based continuous atlas transition
        # may produce a colored seam across side views. Never conceal this.
        t=1/(1+np.exp(-np.clip(15*(norm[:,2]-.03),-25,25)))
        t*=1/(1+np.exp(-np.clip(20*(v[:,2]+.01),-25,25)))
        uv=np.stack([xp*.5*t+(.5+.5*xp)*(1-t),1-yp],axis=1)
        mat=trimesh.visual.material.PBRMaterial(baseColorTexture=atlas,baseColorFactor=[255]*4,
                   metallicFactor=0,roughnessFactor=.92,doubleSided=True)
        mesh.visual=trimesh.visual.TextureVisuals(uv=uv,material=mat)
        scene=trimesh.Scene();scene.add_geometry(mesh,geom_name='actual_neural_volumetric_retopology')
        stem=f'neural_levelset_sigma_{sigma:.1f}_REAL3D_NO_RELEASE'
        path=out/(stem+'.glb');path.write_bytes(trimesh.exchange.gltf.export_glb(scene))
        views=out/(stem+'_six_views');qa(path,views)
        ret=trimesh.load(path,force='scene');geom=next(iter(ret.geometry.values()))
        assert geom.is_watertight and len(geom.faces)==len(mesh.faces)
        report['variants'][stem]={'sha256':sha(path),'bytes':path.stat().st_size,
             'vertices':len(mesh.vertices),'triangles':len(mesh.faces),
             'true_3D':True,'watertight':True,'texture':geom.visual.kind=='texture',
             'six_spatial_camera_images':len(list(views.glob('axis_*.png'))),
             'art':'PENDING_MANUAL_VISUAL_REJECTION_OR_PASS'}
    (out/'run282c_native_volumetric_gltf_QA.json').write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))
if __name__=='__main__':main(*sys.argv[1:])
