#!/usr/bin/env node
// Run260: genuine FREE (no signup, no card) image-to-GLB PBR provider experiment.
// Not production, never identify generated model as accepted without human multi-angle review.
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const root='owl-pet/3d-experiments/172-tyto-castanops';
const out=root+'/research-evidence-run260-FREE-PBR-PROVIDER-ART_UNAPPROVED-NO_RELEASE';
const reference=root+'/research-evidence-run117-FREE-TRELLIS-QUOTA-RECHECK-ART_REJECTED/rightmost_baby_owl_512_rgba.png';
const expected='e439928a9ef08d3be266106cb5f2766b6f5a9f2c414d44e8da55ba81732153b8';
const provider='https://hunyuan3d.dev/en';
fs.mkdirSync(out,{recursive:true});
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const write=(n,v)=>fs.writeFileSync(path.join(out,n),typeof v==='string'?v:JSON.stringify(v,null,2)+'\n');
const log=[], network=[], errors=[], captures=[];
const state={run:'260',provider,started:new Date().toISOString(),reference_sha:expected,
 status:'NOT_YET_SUBMITTED',actual_native_glb:false,art_approved:false,phone_tested:false,fee_usd:0,
 provider_rights_not_cleared:true,release:'NO_RELEASE'};
if(!fs.existsSync(reference)||sha(fs.readFileSync(reference))!==expected) throw Error('Reference identity mismatch');
write('NO_RELEASE.flag','Research only: art unapproved; no commercial rights or physical phone QA; no release.\n');
let browser;
function maybeGLB(buf,tag){
  if(buf.length<256 || buf.toString('ascii',0,4)!=='glTF')return false;
  if(buf.readUInt32LE(8)!==buf.length)return false;
  const len=buf.readUInt32LE(12);
  try{
   const obj=JSON.parse(buf.toString('utf8',20,20+len));
   const tris=(obj.meshes||[]).flatMap(x=>x.primitives||[]).reduce((n,p)=>{
     const a=(obj.accessors||[])[p.indices];return n+(a?Math.floor(a.count/3):0);
   },0);
   if(tris<300){log.push('native glb too small: '+tris);return false;}
   const fp=path.join(out,'run260_FREE_PBR_PROBE_NATIVE_ART_UNAPPROVED.glb');
   fs.writeFileSync(fp,buf);
   Object.assign(state,{actual_native_glb:true,status:'REAL_NATIVE_GLB_RETURNED_ART_UNAPPROVED',native_file:path.basename(fp),
      native_sha256:sha(buf),native_bytes:buf.length,triangles:tris,
      mesh_count:(obj.meshes||[]).length,materials:(obj.materials||[]).length,
      textures:(obj.textures||[]).length,images:(obj.images||[]).length,
      source_response:tag});
   return true;
  }catch(e){log.push('Malformed gltf JSON '+String(e));return false;}
}
try{
  browser=await chromium.launch({headless:true,args:['--no-sandbox','--use-gl=angle','--use-angle=swiftshader']});
  const page=await browser.newPage({viewport:{width:1350,height:950},deviceScaleFactor:1,acceptDownloads:true});
  page.on('console',m=>{if(['error','warning'].includes(m.type()))errors.push(m.type()+':'+m.text().slice(0,300));});
  page.on('pageerror',e=>errors.push('pageerror:'+String(e).slice(0,350)));
  page.on('response',async r=>{
     const url=r.url(),ct=(r.headers()['content-type']||'').toLowerCase();
     if(network.length<300)network.push({code:r.status(),mime:ct.slice(0,85),url:url.slice(0,240)});
     if(state.actual_native_glb)return;
     if(/\.glb(?:$|[?#])|gltf-binary|model\/gltf|3d-model.*download/i.test(url+' '+ct)){
       try{const b=await r.body();maybeGLB(b,'network_response:'+url.slice(0,200));}
       catch(e){log.push('binary network '+String(e).slice(0,200));}
     }
  });
  page.on('download',async d=>{
    try{
      const p=await d.path();
      if(p){const b=fs.readFileSync(p);maybeGLB(b,'browser_download:'+d.suggestedFilename());}
    }catch(e){log.push('download '+String(e).slice(0,200));}
  });
  const result=await page.goto(provider,{waitUntil:'domcontentloaded',timeout:65000});
  state.initial_status=result?.status();
  await page.waitForTimeout(2800);
  await page.screenshot({path:path.join(out,'run260_initial_site_REAL_BROWSER.png'),fullPage:false});
  write('initial_dom_summary.json',{
    title:await page.title(), url:page.url(),
    inputs:await page.locator('input').evaluateAll(ns=>ns.map(n=>({type:n.type,accept:n.accept,name:n.name,outer:n.outerHTML.slice(0,260)}))),
    buttons:await page.locator('button').evaluateAll(ns=>ns.slice(0,50).map(n=>({text:n.innerText.slice(0,140),disabled:n.disabled,html:n.outerHTML.slice(0,240)}))),
    body:(await page.locator('body').innerText()).slice(0,3500)
  });
  const files=page.locator('input[type=file]');
  if(await files.count()===0){
    state.status='NO_NATIVE_INPUT_CONTROL';log.push('No upload file input on live page');}
  else{
    await files.first().setInputFiles(reference);
    state.status='REFERENCE_UPLOADED';
    await page.waitForTimeout(1400);
    await page.screenshot({path:path.join(out,'run260_after_original_upload_REAL_BROWSER.png'),fullPage:false});
    write('pre_submit_buttons.json',await page.locator('button').evaluateAll(ns=>ns.slice(0,60).map(n=>({text:n.innerText.slice(0,150),disabled:n.disabled,html:n.outerHTML.slice(0,200)}))));
    const btn=page.getByRole('button',{name:/Generate My 3D Model|Generate 3D|Generate Model|Generate/i}).first();
    if(await btn.count()===0){state.status='NO_FREE_GENERATE_CONTROL';}
    else{
      const buttonText=await btn.innerText();
      const body=await page.locator('body').innerText();
      if(/(payment required|checkout|credit card required|buy credits to continue|no free credits|subscribe to generate)/i.test(body)){
        state.status='PAID_OR_NO_CREDIT_BOUNDARY';log.push('Observed paywall; did not submit');
      }else if(await btn.isDisabled()){
        state.status='GENERATION_BUTTON_DISABLED';log.push('Free generation button disabled after valid input');
      }else{
        // Only free clearly marked generation, never click paid checkout, credit or subscription.
        state.status='FREE_GENERATE_CLICKED';
        log.push('clicked '+buttonText.slice(0,160));
        await btn.click({timeout:12000});
        for(let i=0;i<27;i++){
          await page.waitForTimeout(6500);
          if(i===2 || i===8 || i===20){
            await page.screenshot({path:path.join(out,'run260_progress_'+i+'_REAL_BROWSER.png'),fullPage:false}).catch(()=>{});
            write('run260_progress_'+i+'_text.txt',(await page.locator('body').innerText()).slice(0,6500));
          }
          if(state.actual_native_glb)break;
          const b=(await page.locator('body').innerText()).slice(0,9000);
          if(/(insufficient credits|payment required|subscribe to|sign in to|login required|daily limit exceeded|generation failed|internal server error)/i.test(b)){
             state.status='PROVIDER_AUTH_QUOTA_OR_ERROR';log.push('blocker:'+b.slice(-650));break;
          }
          const dl=page.getByRole('button',{name:/download.*(glb|3d|model)|download/i}).first();
          if(await dl.count() && await dl.isVisible() && await dl.isEnabled()){
             const txt=await dl.innerText();
             if(!/paid|premium|subscribe|pro plan/i.test(txt)){
               await dl.click({timeout:5000}).catch(e=>log.push('download button '+String(e).slice(0,200)));
             }
          }
          const hrefs=await page.locator('a[href$=".glb"],a[download],a[href*=".glb?"]').evaluateAll(ns=>ns.slice(0,5).map(n=>({href:n.href,download:n.download}))).catch(()=>[]);
          for(const h of hrefs){
             if(state.actual_native_glb)break;
             if(!/^https?:/.test(h.href)||!/\.glb|download/i.test(h.href))continue;
             // browser request remains in the same origin and cookie session.
             try{
               const res=await page.request.get(h.href,{timeout:18000});
               const bb=await res.body();maybeGLB(bb,'download_href:'+h.href.slice(0,200));
             }catch(e){log.push('GLB href '+String(e).slice(0,160));}
          }
        }
      }
    }
  }
  if(!state.actual_native_glb && state.status==='FREE_GENERATE_CLICKED')state.status='NO_NATIVE_GLB_WITHIN_OBSERVATION_WINDOW';
  state.final_url=page.url();
  state.final_body_excerpt=(await page.locator('body').innerText()).slice(-6500);
  await page.screenshot({path:path.join(out,'run260_final_REAL_BROWSER.png'),fullPage:false}).catch(()=>{});
}catch(e){
  state.status='EXPERIMENT_EXCEPTION';errors.push(String(e)+'\n'+(e?.stack||'').slice(0,2500));
}finally{
 await browser?.close().catch(()=>{});
 state.ended=new Date().toISOString();
 write('run260_machine_report.json',state);
 write('run260_browser_network.json',network);
 write('run260_browser_console_errors.json',errors);
 write('run260_experiment_log.txt',log.join('\n')+'\n');
 console.log('RUN260_REAL_PROVIDER_REPORT '+JSON.stringify(state));
}