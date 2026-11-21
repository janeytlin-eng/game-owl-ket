#!/usr/bin/env node
/** Run276: seven real GLTFLoader/WebGL2 spatial views. NOT art or mobile hardware acceptance. */
import {chromium} from 'playwright';
import {createServer} from 'node:http';
import {readFileSync,statSync,writeFileSync,mkdirSync} from 'node:fs';
import {resolve,join} from 'node:path';
import {createHash} from 'node:crypto';

const model=resolve(process.env.OWL172_GLB_INPUT||'');
const evidence=resolve(process.env.OWL172_QA_DIR||'run276-browser-evidence');
const viewer=resolve('owl-pet/3d-experiments/172-tyto-castanops/run256_real_threejs_viewer_RESEARCH_NO_RELEASE.html');
const expected=process.env.OWL172_EXPECTED_SHA;
const name=process.env.OWL172_RUN_LABEL||'Run276';
mkdirSync(evidence,{recursive:true});
const hash=b=>createHash('sha256').update(b).digest('hex');
const record=f=>({bytes:statSync(f).size,sha256:hash(readFileSync(f))});
let srv=null,browser=null;
const report={
 run:'276',name,lowpoly_scaffold_only:true,art_approved:false,release:'NO_RELEASE',phone_hardware:'UNTESTED',
 paid_usd:0,views:[],gates:{},started:new Date().toISOString()
};
try {
 const bin=readFileSync(model);
 if(bin.subarray(0,4).toString()!=='glTF'||!expected||hash(bin)!==expected)
  throw Error('Source is not SHA-matched native GLB');
 report.input=record(model);
 srv=createServer((req,res)=>{
   let path;
   if(req.url==='/viewer.html')path=viewer;
   else if(req.url==='/model.glb')path=model;
   else if(req.url?.startsWith('/node_modules/three/')){
     const rel=req.url.slice('/node_modules/three/'.length);
     if(/^[a-zA-Z0-9_./-]+$/.test(rel)&&!rel.split('/').includes('..'))
       path=resolve('node_modules/three',rel);
   }
   if(!path){res.writeHead(404);res.end();return;}
   try {
     const bytes=readFileSync(path);
     const mime=path.endsWith('.glb')?'model/gltf-binary':
       path.endsWith('.html')?'text/html; charset=utf-8':'text/javascript; charset=utf-8';
     res.writeHead(200,{'Content-Type':mime,'Cache-Control':'no-store'});res.end(bytes);
   } catch(e){res.writeHead(404);res.end('not found')}
 });
 await new Promise((ok,bad)=>srv.listen(0,'127.0.0.1',err=>err?bad(err):ok()));
 browser=await chromium.launch({headless:true,args:[
   '--no-sandbox','--use-angle=swiftshader','--enable-unsafe-swiftshader','--enable-webgl'
 ]});
 const page=await browser.newPage({viewport:{width:390,height:780},deviceScaleFactor:1});
 const errors=[];
 page.on('pageerror',e=>errors.push(String(e)));
 await page.goto('http://127.0.0.1:'+srv.address().port+'/viewer.html',{waitUntil:'load'});
 await page.waitForFunction(()=>window.__qa?.status!=='loading',{timeout:110000});
 const ready=await page.evaluate(()=>({status:window.__qa.status,error:window.__qa.error,stats:window.__qa.stats}));
 if(ready.status!=='ready')throw Error('Three.js GLTFLoader '+JSON.stringify(ready));
 report.browser=ready;
 for (const view of ['front','left','threequarter','right','back','top','bottom']) {
   const pose=await page.evaluate(v=>window.__qa.setView(v),view);
   await page.waitForTimeout(70);
   const target=join(evidence,view+'_ACTUAL_THREEJS_WEBGL2_ART_REJECTED.png');
   await page.locator('#stage').screenshot({path:target});
   report.views.push({view,pose,file:record(target)});
 }
 const stats=ready.stats;
 report.errors=errors;
 report.gates={
   signed_native_binary:expected===report.input.sha256,
   real_threejs_gltfloader:stats.source?.includes('GLTFLoader')===true,
   chromium_webgl2:stats.isWebGL2===true,
   authentic_meshes:stats.meshCount>=1,
   nontrivial_real_triangles:stats.triangles>=100,
   normal_attributes:stats.missingNormals===0,
   seven_spatial_views:report.views.length===7,
   distinct_screenshots:new Set(report.views.map(x=>x.file.sha256)).size===7,
   valid_aabb:stats.bounds.every(Number.isFinite)&&stats.size.every(x=>x>0),
   no_page_errors:errors.length===0
 };
 report.status=Object.values(report.gates).every(Boolean)?
    'NATIVE_WEBGL2_SOFTWARE_PASS_ART_REJECTED_PHONE_UNTESTED_NO_RELEASE':
    'NATIVE_WEBGL2_SOFTWARE_FAIL_NO_RELEASE';
 console.log(JSON.stringify({name,status:report.status,gates:report.gates,model:stats},null,2));
} catch(e) {
 report.status='FAIL_NO_RELEASE';report.error=String(e?.stack||e);
 console.error(report.error);
} finally {
 if(browser)try{await browser.close()}catch{}
 if(srv)try{await new Promise(done=>srv.close(done))}catch{}
 report.finished=new Date().toISOString();
 writeFileSync(join(evidence,'run276_browser_report.json'),JSON.stringify(report,null,2)+'\n');
}
if(!report.status.startsWith('NATIVE_WEBGL2_SOFTWARE_PASS'))process.exitCode=1;
