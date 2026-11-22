#!/usr/bin/env node
/**
 * Run300: test a DIFFERENT genuinely free image->3D provider's FULL-SURFACE
 * textured mode with the ORIGINAL #172 v3 right-side juvenile image.
 *
 * One normal UI submission; no signup, no paid quota, no circumventing limits.
 * Native binary + texture + Three.js + art + rights + phone are separate gates.
 * Nothing in this file ever approves the art or publishes a sample.
 */
import fs from 'node:fs';
import crypto from 'node:crypto';
import path from 'node:path';
import {chromium} from 'playwright-core';
const OUT='owl172-run300-evidence', INPUT='target-owl172-isolated-WHITE.png';
fs.mkdirSync(OUT,{recursive:true});
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const report={run:300,provider:'https://3dai.dev/en',provider_claim:'free, no signup; textured 3D with Hunyuan Paint',
  exact_input:'Run295 GrabCut of the actual repo-owned #172 v3 rightmost chick; white matte',
  source_sha256:fs.existsSync(INPUT)?sha(fs.readFileSync(INPUT)):null,
  source_bytes:fs.existsSync(INPUT)?fs.statSync(INPUT).size:0,
  tested_at:new Date().toISOString(),submissions:0,model_binary_saved:false,
  image_mode:'single-view TEXTURED requested; full-surround texture must be verified, not presumed',
  glb_2_checked:false,provider_rights_verified:false,art_approved:false,
  mobile_physical_gpu_verified:false,release_allowed:false,paid_usd:0,
  events:[],glbs:[],issues:[]};
let browser, modelSaved=false;
const allPending=[];
function inspectAndSave(buffer,url,origin){
  if(buffer.length<32 || buffer.subarray(0,4).toString('ascii')!=='glTF'||
    buffer.readUInt32LE(4)!==2||buffer.readUInt32LE(8)!==buffer.length) return null;
  const l=buffer.readUInt32LE(12), type=buffer.subarray(16,20).toString('ascii');
  if(type!=='JSON'||l<10||l>10000000||20+l>buffer.length)return null;
  const j=JSON.parse(buffer.subarray(20,20+l).toString('utf8'));
  let positions=0;
  for(const m of j.meshes||[])for(const q of m.primitives||[])
    if(q.attributes && q.attributes.POSITION!==undefined)positions++;
  if(positions===0)return null;
  const entry={origin,url,bytes:buffer.length,sha256:sha(buffer),
    mesh_count:(j.meshes||[]).length,position_primitives:positions,
    image_count:(j.images||[]).length,texture_count:(j.textures||[]).length,
    material_count:(j.materials||[]).length,
    textured:(j.images||[]).length>0&&(j.textures||[]).length>0,
    declared_extensions:j.extensionsUsed||[]};
  if(!modelSaved){
    fs.writeFileSync(path.join(OUT,'run300-native-reference-generated-RESEARCH_ONLY_NOT_APPROVED.glb'),buffer);
    modelSaved=true;report.model_binary_saved=true;
  }
  report.glbs.push(entry);return entry;
}
const pause=ms=>new Promise(r=>setTimeout(r,ms));
try{
  if(!fs.existsSync(INPUT)) throw Error('Exact original-pixel Run295 input missing');
  browser=await chromium.launch({executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',
    headless:true,args:['--no-sandbox','--disable-dev-shm-usage','--disable-gpu']});
  const page=await browser.newPage({viewport:{width:390,height:780},acceptDownloads:true});
  page.setDefaultTimeout(15000);
  page.on('pageerror',e=>report.events.push({event:'pageerror',text:String(e).slice(0,500)}));
  page.on('response',response=>{
    const url=response.url(),mime=(response.headers()['content-type']||'').toLowerCase();
    const maybe=/\.glb(?:\?|$)/i.test(url)||/model\/gltf-binary/.test(mime)||
      /\/(?:download|assets|models)\/.+(?:glb|binary)/i.test(url);
    if(!maybe||response.request().method()!=='GET')return;
    const job=(async()=>{
      try{
        if(!response.ok())return;
        const buf=await response.body();
        if(buf.length>80_000_000)return;
        inspectAndSave(buf,url,'network-GET');
      }catch(e){report.events.push({event:'glb-GET-body-failed',text:String(e).slice(0,350)})}
    })();allPending.push(job);
  });
  page.on('download',download=>{
    const job=(async()=>{
      try{
        const file=await download.path();
        if(file&&fs.existsSync(file)){
          const buf=fs.readFileSync(file);
          inspectAndSave(buf,download.url(),'browser-download');
        }
      }catch(e){report.events.push({event:'download-failed',text:String(e).slice(0,350)})}
    })();allPending.push(job);
  });
  const res=await page.goto(report.provider,{waitUntil:'domcontentloaded',timeout:60000});
  report.provider_http=res?.status()??null;
  if(report.provider_http!==200)throw Error('Provider unavailable HTTP '+report.provider_http);
  const intro=(await page.locator('body').innerText()).slice(0,2500);
  report.first_page_excerpt=intro;
  if(!/free|no.sign.up/i.test(intro))throw Error('No public zero-cost claim; do not submit');
  if(!/textured|texture/i.test(intro))throw Error('Full surface texture mode not found');
  const file=page.locator('input[type="file"]').first();
  if(await file.count()!==1)throw Error('No ordinary file upload input');
  await file.setInputFiles(INPUT);
  await pause(1000);
  // Try to explicitly choose Textured and Standard by accessible text when possible.
  // In the actual page, the default button is "Generate textured 3D".
  for(const word of ['Textured','Standard']){
    const controls=page.getByRole('radio',{name:new RegExp(word,'i')});
    if(await controls.count()>0){
      try{await controls.first().check({timeout:3500});report.events.push({event:'choice',value:word})}catch{}
    }
  }
  await page.screenshot({path:path.join(OUT,'01-source-selected.png'),fullPage:true});
  let generate=page.getByRole('button',{name:/Generate textured 3D/i}).first();
  if(await generate.count()!==1||!(await generate.isVisible())||!(await generate.isEnabled()))
    throw Error('Actual free textual generation submit unavailable');
  const before=(await generate.innerText()).trim();
  if(!/textured/i.test(before))throw Error('Site switched to white mesh; refuse stale technical route');
  report.actual_submit_label=before;
  await generate.click({timeout:15000});
  report.submissions=1;
  for(let i=0;i<90;i++){
    await pause(4000);
    if(modelSaved)break;
    const body=(await page.locator('body').innerText().catch(()=>''))||'';
    if(/processing limit reached|not enough credits|payment required|quota exceeded|rate limit|quota reached/i.test(body)){
      report.events.push({event:'provider-quota-or-payment-block',excerpt:body.slice(-650)});
      break;
    }
    if(i%15===14)report.events.push({event:'in-progress',elapsed_seconds:(i+1)*4,
      excerpt:body.slice(-500)});
    // Some sites expose a download button after finishing; it is free and does not publish.
    if(/download glb/i.test(body) && !report.download_clicked){
      const dl=page.getByRole('button',{name:/download.*glb|glb.*download/i}).first();
      if(await dl.count()>0 && await dl.isVisible()){
        try{await dl.click({timeout:5000});report.download_clicked=true;}catch(e){
          report.events.push({event:'download-ui-error',text:String(e).slice(0,220)})}
      }
    }
  }
  await Promise.allSettled(allPending);
  report.final_excerpt=(await page.locator('body').innerText().catch(()=>'')).slice(-1400);
  await page.screenshot({path:path.join(OUT,'02-provider-result.png'),fullPage:true});
}catch(e){report.issues.push(String(e).slice(0,1200));}
finally{
  try{await Promise.allSettled(allPending)}catch{}
  try{await browser?.close()}catch{}
  report.glb_2_checked=modelSaved;
  report.final_gate=report.glbs.some(x=>x.textured)?
    'TEXTURED_NATIVE_GLB_CAPTURED_ONLY_ART_RIGHTS_PHONE_UNVERIFIED_NO_RELEASE':
    modelSaved?'UN-TEXTURED_NATIVE_GLB_ONLY_ART_REJECTED_NO_RELEASE':
    'NO_NATIVE_GLB_CAPTURED_NO_RELEASE';
  fs.writeFileSync(path.join(OUT,'run300_provider_evidence.json'),JSON.stringify(report,null,2));
  console.log(JSON.stringify({final_gate:report.final_gate,submissions:report.submissions,
    models:report.glbs,issues:report.issues,events:report.events},null,2));
}
