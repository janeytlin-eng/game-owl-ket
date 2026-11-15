#!/usr/bin/env python3
"""Run93 experimental integration of free GroomLab C++ grooming onto an ACTUAL rejected #172 3D GLB.

This is a strict exploratory proof, not approved art. Original source GLB remains unchanged.
Output is quarantined; no production, deployment, or 251-species edits.
"""
import argparse, hashlib, json, os, subprocess, sys, time, traceback
from pathlib import Path
import numpy as np
import trimesh

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

class GroomLab:
    def __init__(self, helper, log):
        self.proc=subprocess.Popen([str(helper)],stdin=subprocess.PIPE,stdout=subprocess.PIPE,
                                   stderr=open(log,'w'),text=True,bufsize=1)
        self.seq=0
    def call(self, cmd, **kw):
        self.seq+=1
        body={"id":self.seq,"cmd":cmd,**kw}
        self.proc.stdin.write(json.dumps(body,separators=(',',':'))+'\n')
        self.proc.stdin.flush()
        line=self.proc.stdout.readline()
        if not line: raise RuntimeError('helper terminated on '+cmd)
        result=json.loads(line)
        if result.get('id') != self.seq or not result.get('ok'):
            raise RuntimeError(cmd+': '+json.dumps(result)[:3000])
        return result.get('result', {})
    def close(self):
        try:self.call('shutdown')
        except Exception: pass
        try:self.proc.communicate(timeout=5)
        except Exception:self.proc.kill()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--helper',required=True,type=Path)
    ap.add_argument('--baseline',required=True,type=Path)
    ap.add_argument('--out',required=True,type=Path)
    a=ap.parse_args();a.out.mkdir(exist_ok=True,parents=True)
    metrics={'experiment':'owl172-run93-GroomLab-free-engine-multiview-probe',
      'status':'ART_REJECTED','candidate_approved':False,'physical_phone_GPU':False,
      'original_concept_side_back_verified':False,'stage':'initializing',
      'tool':'thekesslereffect/groomlab dev Apache-2.0 core (license verified in upstream)',
      'workflow_run':os.environ.get('GITHUB_RUN_ID',''),
      'baseline_sha256':sha(a.baseline),'baseline_bytes':a.baseline.stat().st_size}
    try:
        scene=trimesh.load(a.baseline,force='scene',process=False)
        ranked=sorted([(len(m.faces),n,m) for n,m in scene.geometry.items()
                       if isinstance(m,trimesh.Trimesh) and len(m.faces)>100],
                      key=lambda z:z[0],reverse=True)
        assert ranked,'baseline has no actual triangle mesh'
        body=ranked[0][2].copy()
        metrics['base_source_geometry']=ranked[0][1]
        metrics['base_source_triangles']=len(body.faces)
        # Scalp only: decimate an existing connected volumetric owl surface, do NOT invent new spheres.
        try:
            scalp=body.simplify_quadric_decimation(face_count=3200)
            metrics['scalp_simplification']='quadric'
        except Exception as e:
            metrics['decimation_error']=repr(e)
            # Contiguous subset is sufficient for a tooling compatibility probe, NOT a finished scalp.
            scalp=body.submesh([np.arange(min(2700,len(body.faces)))],append=True,repair=False)
            metrics['scalp_simplification']='contiguous_face_subset_research_only'
        assert len(scalp.faces)>250
        vertices=np.asarray(scalp.vertices,dtype=np.float64)
        faces=np.asarray(scalp.faces,dtype=np.int32)
        uv=np.column_stack(((vertices[:,0]-vertices[:,0].min())/(np.ptp(vertices[:,0])+1e-8),
                            (vertices[:,2]-vertices[:,2].min())/(np.ptp(vertices[:,2])+1e-8)))
        corner_uv=uv[faces.reshape(-1)].round(6).tolist()
        metrics['scalp_vertices']=len(vertices);metrics['scalp_triangles']=len(faces)
        metrics['stage']='engine_handshake'
        g=GroomLab(a.helper,a.out/'helper.stderr.log')
        try:
            metrics['hello']=g.call('hello',protocol=1)
            new=g.call('new_session',space={'upAxis':'Y','metersPerUnit':1.0},fps=24)
            sid=new['session']
            metrics['session']=sid
            scalp_result=g.call('set_scalp',session=sid,points=vertices.round(7).tolist(),
                                faceCounts=[3]*len(faces),faceIndices=faces.reshape(-1).tolist(),
                                uvs=corner_uv)
            metrics['scalp_result']=scalp_result
            metrics['stage']='groom_creation'
            created=g.call('new_groom',session=sid,followScalp=True)
            metrics['groom_created']=True
            metrics['groom_summary']=str(created)[:900]
            metrics['stage']='groom_evaluation'
            evaluation=g.call('evaluate',session=sid,density=.13)
            metrics['eval_summary']=str(evaluation)[:1200]
            # Genuine failure diagnosis from Run93A: exporting hair without Cards node
            # returns state/"the graph has no Cards node". Insert card node and rebake.
            metrics['stage']='cards_graph_insertion'
            try:
                added=g.call('edit_graph',session=sid,op='add_node',type='Cards',
                             name='owl_cream_down_mobile_cards')
                metrics['cards_node_added']=str(added)[:800]
                metrics['cards_connect_from_resample']=str(g.call('edit_graph',
                    session=sid,op='connect',**{'from':'resample',
                    'to':'owl_cream_down_mobile_cards','input':'strands'}))[:800]
                metrics['cards_connect_to_output']=str(g.call('edit_graph',
                    session=sid,op='connect',**{'from':'owl_cream_down_mobile_cards',
                    'to':'output','input':'strands'}))[:800]
                try:
                    metrics['cream_color_material']=str(g.call('set_param',
                        session=sid,node='color',param='color',
                        value=[.94,.88,.75]))[:500]
                    metrics['cream_color_mode']=str(g.call('set_param',
                        session=sid,node='color',param='mode',value='color'))[:500]
                except Exception as e:
                    metrics['cream_color_warning']=str(e)
                try:
                    metrics['cards_preset']=str(g.call('cards_preset',session=sid,lod='mid'))[:1100]
                except Exception as e:
                    metrics['cards_preset_warning']=str(e)
                try:
                    baked=g.call('bake_cards',session=sid,directory=str(a.out.absolute()),
                                 name='owl_cream_down_research_cards',resolution=256)
                    metrics['cards_baked']=str(baked)[:1600]
                except Exception as e:
                    metrics['cards_bake_warning']=str(e)
            except Exception as e:
                metrics['cards_graph_error']=str(e)
            target=a.out/'owl172_run93_GROOMLAB_MESH_DOWN_ART_REJECTED.glb'
            metrics['stage']='gltf_cards_export'
            try:
                exported=g.call('export',session=sid,format='gltfCards',path=str(target.absolute()),
                                name='owl172_run93',lods=['low'],resolution=256,
                                cap=False,scale=.01,alphaMode='mask',alphaCutoff=.5)
                metrics['export_result']=str(exported)[:1400]
                if target.is_file() and target.stat().st_size>2000:
                    parsed=trimesh.load(target,force='scene',process=False)
                    triangles=sum(len(m.faces) for m in parsed.geometry.values())
                    metrics['exported_down_glb']={'bytes':target.stat().st_size,'sha256':sha(target),
                        'meshes':len(parsed.geometry),'triangles':triangles}
                    assert triangles>0,'GroomLab output contained no triangles'
                    # Diagnostic real scene combining mesh groom and existing true 3D owl; not publication.
                    all_scene=trimesh.Scene()
                    for name,m in scene.geometry.items():
                        if isinstance(m,trimesh.Trimesh):all_scene.add_geometry(m.copy(),geom_name='baseline_'+name)
                    for name,m in parsed.geometry.items():
                        if isinstance(m,trimesh.Trimesh):all_scene.add_geometry(m.copy(),geom_name='groomlab_'+name)
                    combo=a.out/'owl172_run93_combined_TOOL_PROBE_ART_REJECTED.glb'
                    all_scene.export(combo)
                    reloaded=trimesh.load(combo,force='scene',process=False)
                    metrics['combined']={'bytes':combo.stat().st_size,'sha256':sha(combo),
                        'meshes':len(reloaded.geometry),
                        'triangles':sum(len(m.faces) for m in reloaded.geometry.values())}
                    metrics['stage']='real_GLBS_written_but_not_art_approved'
                else:
                    metrics['export_did_not_create_glb']=True
            except Exception as e:
                metrics['gltf_export_failure']=str(e)
            groom=a.out/'owl172_run93_UNAPPROVED.groom'
            try:
                metrics['save_groom']=g.call('save_groom',session=sid,path=str(groom.absolute()),upAxis='Y')
                if groom.is_file():metrics['groom_bytes']=groom.stat().st_size
            except Exception as e:metrics['groom_save_error']=str(e)
        finally:g.close()
    except Exception as e:
        metrics['failure']=str(e)
        metrics['traceback']=traceback.format_exc()[-4000:]
        metrics['stage']='tooling_blocked'
    finally:
        (a.out/'probe_metrics.json').write_text(json.dumps(metrics,indent=2,ensure_ascii=False))
        (a.out/'ART_REJECTED_DO_NOT_PUBLISH.txt').write_text(
          'GroomLab new open-source 3D hair-card engine probe only. No physical mobile GPU test.\n'
          'No artistic approval; do not show as a sample or deploy. Original ref side/back unknown.\n'
          'This tooling probe may fail or produce cards but cannot establish correct juvenile owl anatomy.\n')
        print(json.dumps(metrics,indent=2,ensure_ascii=False))
if __name__=='__main__': main()
