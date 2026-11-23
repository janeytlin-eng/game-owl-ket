#!/usr/bin/env node
/** Run322: actually load the unmodified native GLB through Chromium/Three.js WebGL2 and capture eight orbit angles.
 * Desktop software GPU with mobile dimensions is NOT physical phone validation. NO_RELEASE.
 */
import fs from 'node:fs';
import http from 'node:http';
import path from 'node:path';
import crypto from 'node:crypto';
import {chromium} from 'playwright-core';
import {PNG} from 'pngjs';
const model=path.resolve(process.argv[2]||'');
const dir=path.resolve(process.argv[3]||'owl172-run322-evidence/webgl2');
const html=path.resolve('owl-pet/3d-experiments/172-tyto-castanops/run322_native_orbit_research_NO_RELEASE.html');
if(!fs.existsSync(model)||fs.readFileSync(model).subarray(0,4).toString()!=='glTF')throw Error('A real native GLB is required');
fs.mkdirSync(dir,{recursive:true});
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const root=path.resolve('.');
const report={source:model,source_sha256:sha(fs.readFileSync(model)),viewport:[390,780],
  declared_environment:'Chromium/SwiftShader software WebGL2, emulated mobile viewport only; NOT physical phone QA',
  views:[],technicallyLoaded:false,artApproved:false,release:false};
const server=http.createServer((req,res)=>{
 let fp;
 if(req.url==='/model.glb')fp=model;
 else if(req.url==='/')fp=html;
 else if(req.url.startsWith('/node_modules/three/'))fp=path.resolve(root,'.'+req.url.split('?')[0]);
 else {res.writeHead(404).end();return;}
 if(!fs.existsSync(fp)||!fs.statSync(fp).isFile()){res.writeHead(404).end();return;}
 let ct=fp.endsWith('.glb')?'model/gltf-binary':fp.endsWith('.html')?'text/html':'text/javascript';
 res.writeHead(200,{'content-type':ct,'cache-control':'no-store'});
 fs.createReadStream(fp).pipe(res);
});
await new Promise(done=>server.listen(0,'127.0.0.1',done));
let browser=null;
try {
 browser=await chromium.launch({executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',
  headless:true,args:['--no-sandbox','--disable-dev-shm-usage','--enable-webgl','--ignore-gpu-blocklist',
  '--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader','--disable-gpu-sandbox']});
 const page=await browser.newPage({viewport:{width:390,height:780},deviceScaleFactor:1,isMobile:true,hasTouch:true});
 const errors=[];page.on('pageerror',e=>errors.push(String(e)));page.on('console',m=>{if(m.type()==='error')errors.push(m.text());});
 await page.goto('http://127.0.0.1:'+server.address().port+'/',{waitUntil:'load',timeout:30000});
 await page.waitForFunction(()=>window.__status==='ready'||window.__status==='error',null,{timeout:90000});
 const st=await page.evaluate(()=>({status:window.__status,error:window.__error,stats:window.__stats}));
 report.browser=st;if(st.status!=='ready')throw Error(st.error||'Model load failed');
 for(const yaw of [0,45,90,135,180,225,270,315]){
  await page.evaluate(y=>window.__setYaw(y),yaw);
  await page.waitForTimeout(140);
  const png=await page.locator('#view').screenshot();
  const decoded=PNG.sync.read(png);
  let count=0;
  for(let i=0;i<decoded.data.length;i+=4){
   let r=decoded.data[i],g=decoded.data[i+1],b=decoded.data[i+2];
   if(Math.abs(r-237)+Math.abs(g-231)+Math.abs(b-223)>56)count++;
  }
  const file='yaw_'+String(yaw).padStart(3,'0')+'.png';
  fs.writeFileSync(path.join(dir,file),png);
  report.views.push({yaw,file,bytes:png.length,sha256:sha(png),
    occupiedPercent:Number((100*count/(decoded.width*decoded.height)).toFixed(3))});
 }
 report.browser.stats=await page.evaluate(()=>window.__stats);
 report.consoleErrors=errors.slice(0,20);
 report.technicallyLoaded=report.views.length===8&&new Set(report.views.map(x=>x.sha256)).size>=6;
 await page.close();
} catch(e){report.error=String(e);}
finally{
 if(browser)await browser.close();
 await new Promise(done=>server.close(done));
 fs.writeFileSync(path.join(dir,'browser-report.json'),JSON.stringify(report,null,2));
 console.log(JSON.stringify(report,null,2));
}
if(!report.technicallyLoaded)process.exitCode=1;