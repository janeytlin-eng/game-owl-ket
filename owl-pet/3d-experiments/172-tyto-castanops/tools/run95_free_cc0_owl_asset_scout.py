#!/usr/bin/env python3
"""Run95: no-fee search for genuine CC0 owl source meshes; quarantine only.
This is NOT an art-approved model-generation service.
Do not access authentication, billing, the 251-species pipeline, or live pet.
"""
import hashlib, json, os, pathlib, re, sys, time, urllib.parse, urllib.request
from urllib.error import HTTPError,URLError

OUT=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else 'qa95').resolve()
OUT.mkdir(parents=True,exist_ok=True)
API='https://3dassets.dev/api/v1/assets'
QUERIES=['barn owl','masked owl','owlet','baby owl','owl']
agent='Owl172-CC0-3D-research/Run95 (no-auth read-only)'
raw_search={}; seen={}; errors=[]

def request(url,limit=3_000_000):
    req=urllib.request.Request(url,headers={'User-Agent':agent,'Accept':'application/json'})
    with urllib.request.urlopen(req,timeout=30) as resp:
        data=resp.read(limit+1)
        if len(data)>limit: raise ValueError('response too big')
        return data

def score(a):
    title=str(a.get('title') or a.get('name') or a.get('slug') or '').lower()
    desc=str(a.get('description') or '').lower()
    if 'owl' not in title and 'owlet' not in title: return -100
    s=10
    for term,bonus in [('barn owl',100),('masked owl',95),('owlet',90),
                       ('baby owl',85),('owl chick',85),('nestling',60),
                       ('juvenile',50),('tyto',85),('fluffy',20)]:
        if term in title:s+=bonus
        elif term in desc:s+=bonus//4
    for term,minus in [('horned',35),('eagle owl',25),('statue',25),
                       ('low poly',25),('low-poly',25),('cartoon',20)]:
        if term in title:s-=minus
    return s

for query in QUERIES:
    url=API+'?'+urllib.parse.urlencode({'q':query,'limit':30})
    try:
        doc=json.loads(request(url))
        data=doc.get('data',[])
        if not isinstance(data,list):data=[]
        raw_search[query]={'returned':len(data),'source':url}
        for v in data:
            if not isinstance(v,dict):continue
            key=str(v.get('slug') or v.get('id') or '')
            if key and key not in seen:seen[key]=v
    except Exception as e:
        errors.append({'query':query,'error':repr(e)})
        raw_search[query]={'error':repr(e)}
    time.sleep(.15)

candidates=sorted((a for a in seen.values() if score(a)>0),
                  key=lambda a:(-score(a),str(a.get('slug'))))
manifest={'kind':'Run95 CC0 free public adult/juvenile owl mesh scout',
          'target':'#172 Tyto castanops v3 RIGHT cream mesoptile',
          'generation_cost_usd':0,'user_model_ready':False,
          'verdict':'ART_REJECTED_PENDING_TRUE_ART_AND_MOBILE_GPU',
          'api_queries':raw_search,'errors':errors,
          'candidate_summaries':[],'downloaded':[]}
for a in candidates[:18]:
    manifest['candidate_summaries'].append({
        'slug':a.get('slug'),'name':a.get('name') or a.get('title'),
        'score':score(a),'cdnUrl':a.get('cdnUrl'),
        'license':a.get('license'),'triangles':a.get('triangles'),
        'description':str(a.get('description') or '')[:240]})
    if len(manifest['downloaded'])>=4:continue
    url=a.get('cdnUrl') or a.get('cdn_url') or a.get('modelUrl')
    if not isinstance(url,str) or not url.startswith('https://cdn.3dassets.dev/'):
        continue
    lic=json.dumps(a.get('license') or '',ensure_ascii=False).lower()
    if lic and ('cc0' not in lic and 'public domain' not in lic):
        errors.append({'slug':a.get('slug'),'error':'license not recognized as CC0'})
        continue
    try:
        raw=request(url,25_000_000)
        if len(raw)<1000 or raw[:4]!=b'glTF':
            raise ValueError('not a genuine GLB')
        slug=re.sub('[^a-zA-Z0-9_-]','_',str(a.get('slug') or 'owl'))[:70]
        path=OUT/f'CC0_original_{slug}.glb'
        path.write_bytes(raw)
        manifest['downloaded'].append({
            'slug':a.get('slug'),'display_name':a.get('name') or a.get('title'),
            'score':score(a),'file':path.name,'bytes':len(raw),
            'sha256':hashlib.sha256(raw).hexdigest(),'source_url':url,
            'licence':'CC0 claimed by origin site; independent provenance unverified',
            'claimed_species':str(a.get('name') or a.get('title') or ''),
            'original_art_approved':False,'age_and_taxon_verified':False})
    except Exception as e: errors.append({'slug':a.get('slug'),'error':repr(e)})
    time.sleep(.3)

(OUT/'run95_candidates.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False))
(OUT/'ART_REJECTED_DO_NOT_PUBLISH.txt').write_text(
    'Research-only unapproved mesh source study. All original external meshes remain unattributed candidates, not the target Tyto castanops juvenile.\n'
    'No authentic age verification, true soft cream down, correct multi-view anatomy, or physical mobile WebGL GPU pass.\n'
    'No public demo or production use. No charges or billing API.\n')
print(json.dumps({'candidates':len(candidates),
  'downloaded':manifest['downloaded'],
  'errors':errors},indent=2),flush=True)
# Zero matches is a valid negative research outcome, not success.
