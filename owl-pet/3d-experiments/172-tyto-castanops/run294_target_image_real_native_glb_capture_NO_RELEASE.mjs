import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { chromium } from 'playwright-core';
// #172 Run294 - one actual zero-dollar image-to-3D browser run using the user's own ORIGINAL design crop.
// No external billing, no bypass, no account. Model is RESEARCH ONLY, not approved/public game art.
const out='owl172-run294-evidence';
fs.mkdirSync(out,{recursive:true});
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const report={run:294,date:new Date().toISOString(),
 source:'https://trellis2.dev/',upstream_observed_previous:'https://hy3dlab-image-to-3d.hf.space',
 input:'user-project-own-rightmost-#172-Tyto-castanops-v3-crop.png',cost_usd:0,
 webgl_phone_pass:false,art_accepted:false,redistribution_rights_checked:false,
 release_allowed:false,events:[],network_binary:[],errors:[]};
let browser;
const responses=[];
try{
 browser=await chromium.launch({executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',
 headless:true,args:['--no-sandbox','--disable-dev-shm-usage','--disable-gpu']});
 const page=await browser.newPage({viewport:{width:390,height:780},acceptDownloads:true});
 page.on('response',r=>{
  if(/\.glb(?:\?|$)/i.test(r.url())){
   const p=(async()=>{
    const e={url:r.url(),status:r.status()};
    try{
     if(!r.ok())throw Error('HTTP status '+r.status());
     const b=await r.body();
     e.bytes=b.length;e.sha256=sha(b);
     if(b.length<40||b.toString('ascii',0,4)!=='glTF'||b.readUInt32LE(4)!==2||
       b.readUInt32LE(8)!==b.length)throw Error('GLB magic/version/total length mismatch');
     const n=b.readUInt32LE(12);
     if(b.toString('ascii',16,20)!=='JSON'||n<10||n>10000000)throw Error('Invalid JSON chunk');
     const json=JSON.parse(b.subarray(20,20+n).toString('utf8'));
     e.meshes=json.meshes?.length||0;
     e.positionPrimitives=(json.meshes||[]).reduce((a,m)=>a+(m.primitives||[]).filter(p=>p.attributes?.POSITION!==undefined).length,0);
     e.textureCount=json.textures?.length||0;
     if(e.positionPrimitives===0)throw Error('No POSITION-bearing native 3D');
     const filename=path.join(out,'output-target-UNAPPROVED-native.glb');
     fs.writeFileSync(filename,b);
     e.saved_for_QA_only=true;e.valid_native_glb=true;
    }catch(x){e.error=String(x);e.valid_native_glb=false;}
    report.network_binary.push(e);
   })();
   responses.push(p);
  }
 });
 page.on('pageerror',e=>report.events.push({kind:'browser_error',text:String(e).slice(0,500)}));
 const r=await page.goto('https://trellis2.dev/',{waitUntil:'domcontentloaded',timeout:45000});
 report.site_http=r?.status();
 if(report.site_http!==200)throw Error('Source site not available: '+report.site_http);
 await page.locator('input[type=file]').first().setInputFiles('target-owl172-rightmost-crop.png');
 await page.waitForTimeout(1500);
 await page.screenshot({path:path.join(out,'01-target-upload.png')});
 const buttons=page.getByRole('button',{name:/generate/i});
 const candidates=[];
 for(let i=0;i<await buttons.count();i++){
  let b=buttons.nth(i);candidates.push({i,label:(await b.innerText()).trim().slice(0,150),
   visible:await b.isVisible(),enabled:await b.isEnabled()});
 }
 report.button_candidates=candidates;
 const correct=candidates.find(c=>c.visible&&c.enabled&&/Fast\s*&\s*Private|~50s/i.test(c.label));
 if(!correct)throw Error('Actual generation submit not available - no CTA fallback');
 report.generation_attempted=true;
 await buttons.nth(correct.i).click({timeout:10000});
 const start=Date.now();
 for(let i=0;i<25;i++){
  await page.waitForTimeout(5000);
  if(report.network_binary.some(x=>x.valid_native_glb))break;
  if(i%5===4)report.events.push({kind:'progress',elapsed_s:Math.round((Date.now()-start)/1000)});
 }
 await Promise.allSettled(responses);
 report.generation_elapsed_seconds=Math.round((Date.now()-start)/1000);
 report.page_excerpt=(await page.locator('body').innerText()).slice(0,800);
 await page.screenshot({path:path.join(out,'02-browser-result.png')});
}catch(e){report.errors.push(String(e))}
finally{
 try{await Promise.allSettled(responses)}catch{}
 try{await browser?.close()}catch{}
 report.native_glb_valid=report.network_binary.some(r=>r.valid_native_glb===true);
 report.final_gate=report.native_glb_valid?
 'ACTUAL_TARGET_NATIVE_GLB_TECH_PASS_ART_PENDING_RIGHTS_HOLD_NO_RELEASE':
 'NO_ACTUAL_NATIVE_GLB_ART_PENDING_NO_RELEASE';
 fs.writeFileSync(path.join(out,'run294_report.json'),JSON.stringify(report,null,2));
 const lines=fs.readdirSync(out).sort().filter(n=>n!=='SHA256SUMS.txt').map(n=>
 sha(fs.readFileSync(path.join(out,n)))+'  '+n);
 fs.writeFileSync(path.join(out,'SHA256SUMS.txt'),lines.join('\n')+'\n');
 console.log('RUN294',report.final_gate,'files',lines.length,'cost',$='0 USD');
}
