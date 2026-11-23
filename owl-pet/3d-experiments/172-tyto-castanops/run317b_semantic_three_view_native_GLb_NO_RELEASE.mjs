#!/usr/bin/env node
/** #172 Run317b: real GLB WebGL2 three-camera 390x780 browser QA. TECH ONLY, ART REJECTED. */
import fs from 'node:fs';
import path from 'node:path';
import http from 'node:http';
import crypto from 'node:crypto';
import { chromium } from 'playwright-core';
import { PNG } from 'pngjs';
const inputs=process.argv.slice(2).filter(p=>fs.existsSync(p));
if(!inputs.length)throw new Error('Missing real 3D GLB inputs');
const out=path.resolve('owl172-run317b-browser-evidence');fs.mkdirSync(out,{recursive:true});
const root=path.resolve('.');
const html=path.resolve('owl-pet/3d-experiments/172-tyto-castanops/run317b_semantic-front-negZ_viewer_NO_RELEASE.html');
let activeModel='';
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const server=http.createServer((req,res)=>{
 try{
  const u=new URL(req.url,'http://localhost');
  let file='';
  if(u.pathname==='/model.glb')file=activeModel;
  else if(u.pathname==='/')file=html;
  else if(u.pathname.startsWith('/node_modules/three/'))file=path.resolve(root,'.'+u.pathname);
  if(!file || !fs.existsSync(file) || (u.pathname.startsWith('/node_modules')&&!file.startsWith(path.join(root,'node_modules','three')))){res.writeHead(404).end();return;}
  const stat=fs.statSync(file);
  res.writeHead(200,{'content-type':file.endsWith('.glb')?'model/gltf-binary':file.endsWith('.html')?'text/html':'text/javascript','content-length':stat.size,'cache-control':'no-store'});
  if(req.method==='HEAD'){res.end();return;}fs.createReadStream(file).pipe(res);
 }catch(e){res.writeHead(500).end(String(e));}
});
await new Promise(ok=>server.listen(0,'127.0.0.1',ok));
const url='http://127.0.0.1:'+server.address().port+'/';
const report={run:'317b',date:new Date().toISOString(),environment:'390x780 emulated browser Chrome/SwiftShader WebGL2; NOT physical Android/iOS',inputs:[]};
function occupancy(buf){
 const p=PNG.sync.read(buf);let count=0;
 for(let i=0;i<p.data.length;i+=4)if(Math.abs(p.data[i]-237)+Math.abs(p.data[i+1]-230)+Math.abs(p.data[i+2]-221)>52)count++;
 return Number((100*count/(p.width*p.height)).toFixed(3));
}
let browser;
try{
 browser=await chromium.launch({executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',headless:true,args:['--no-sandbox','--disable-dev-shm-usage','--enable-webgl','--ignore-gpu-blocklist','--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader','--disable-gpu-sandbox']});
 for(let i=0;i<inputs.length;i++){
  const file=inputs[i],buf=fs.readFileSync(file);
  const item={path:file,sha256:sha(buf),bytes:buf.length,pass:false,views:[]};report.inputs.push(item);
  if(buf.subarray(0,4).toString()!=='glTF'){item.error='Not a native GLB';continue;}
  activeModel=path.resolve(file);
  const page=await browser.newPage({viewport:{width:390,height:780},deviceScaleFactor:1,isMobile:true,hasTouch:true});
  const logs=[];page.on('pageerror',e=>logs.push(String(e)));page.on('console',m=>{if(m.type()==='error')logs.push(m.text());});
  try{
   await page.goto(url,{waitUntil:'load',timeout:30000});
   await page.waitForFunction(()=>window.__owlStatus==='ready'||window.__owlStatus==='error',null,{timeout:90000});
   const status=await page.evaluate(()=>({status:window.__owlStatus,error:window.__owlError,stats:window.__stats}));
   item.browser=status;
   if(status.status!=='ready')throw Error('WebGL2 or GLTFLoader error: '+status.error);
   for(const direction of ['front','right','back']){
    await page.evaluate(v=>window.__setView(v),direction);await page.waitForTimeout(250);
    const png=await page.locator('#view').screenshot();const name='model'+(i+1)+'_'+direction+'.png';
    fs.writeFileSync(path.join(out,name),png);
    item.views.push({direction,file:name,sha256:sha(png),occupancyPct:occupancy(png)});
   }
   if(new Set(item.views.map(v=>v.sha256)).size!==3)throw Error('Identical 3D views');
   if(item.views.some(v=>v.occupancyPct<.8))throw Error('Empty/too small canvas');
   item.pass=true;
  }catch(e){item.error=String(e);}item.consoleErrors=logs.slice(0,12);
  await page.close();
 }
}finally{
 if(browser)await browser.close();
 await new Promise(ok=>server.close(ok));
 fs.writeFileSync(path.join(out,'report.json'),JSON.stringify(report,null,2));
 const lines=fs.readdirSync(out).sort().filter(p=>p!=='SHA256SUMS.txt').map(p=>sha(fs.readFileSync(path.join(out,p)))+'  '+p);
 fs.writeFileSync(path.join(out,'SHA256SUMS.txt'),lines.join('\n')+'\n');
 console.log(JSON.stringify(report,null,2));
}
if(report.inputs.some(i=>!i.pass))process.exitCode=1;
