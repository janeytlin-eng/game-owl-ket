#!/usr/bin/env python3
"""Run155: actual unauthenticated public-UI test of NEW juvenile 3D sources.

Never bypass access controls. Never purchase, login, click checkout, scrape private APIs,
or conflate a photorealistic preview with a GLB. Source CC0 statements are provisional.
ART is unreviewed and NO_RELEASE even if valid native mesh is obtained.
"""
import sys, os, re, json, time, hashlib, struct, pathlib, traceback
from datetime import datetime, timezone

ROOT=pathlib.Path("owl-pet/3d-experiments/172-tyto-castanops")
OUT=ROOT/"research-evidence-run155-MESHY-CC0-JUVENILE-NO_RELEASE"
OUT.mkdir(parents=True,exist_ok=True)
SOURCES={
 "meshy_sunlit_owlet": "https://www.meshy.ai/posts/Sunlit-Owlet-01a00f65-b940-70c9-817a-255fff4654d8",
 "meshy_heartfaced_barnowl_tag": "https://www.meshy.ai/tags/heartshape",
}
BLOCK=["login","log in","sign in","signup","sign up","purchase","buy now",
       "checkout","credit card","subscribe","payment","captcha","verify you are human"]
def save_json(p, obj): (OUT/p).write_text(json.dumps(obj,indent=2,ensure_ascii=False,default=str))
def sha(b): return hashlib.sha256(b).hexdigest()
def legal_preview(data):
    return (data or "")[:5000]
def check_glb(b):
    out={"bytes":len(b),"sha256":sha(b),"valid_glb":False}
    if len(b)<20 or b[:4]!=b"glTF":return out
    magic,ver,total=struct.unpack_from("<4sII",b,0)
    out.update({"glb_version":ver,"declared_length":total})
    if ver!=2 or total!=len(b):return out
    chunklen,tag=struct.unpack_from("<II",b,12)
    if tag!=0x4E4F534A or 20+chunklen>len(b):return out
    try:
        gltf=json.loads(b[20:20+chunklen].decode("utf-8").rstrip(" \x00"))
        acc=gltf.get("accessors",[])
        tris=0
        for mesh in gltf.get("meshes",[]):
            for prim in mesh.get("primitives",[]):
                if prim.get("mode",4)!=4:continue
                idx=prim.get("indices")
                if isinstance(idx,int) and idx<len(acc):tris+=int(acc[idx].get("count",0))//3
        out.update({"valid_glb":True,"mesh_count":len(gltf.get("meshes",[])),
                    "material_count":len(gltf.get("materials",[])),
                    "image_count":len(gltf.get("images",[])),"primitive_triangles":tris})
    except Exception as e:out["parse_error"]=repr(e)
    return out

def probe():
    records={"run":"155","target":"#172 rightmost cream mesoptile, not adult",
      "date_utc":datetime.now(timezone.utc).isoformat(),
      "preflight":["owl-pet/AGENTS.md","owl-pet/README.md",
          "owl-pet/research/species/172-tyto-castanops-v3.md",
          "owl-pet/prototype/index.html",
          str(ROOT/"2026-11-18-run154-real-glb-groom-transport-NO_RELEASE.md"),
          str(ROOT/"known_rejected_asset_sha256_registry.json")],
      "sources":{}, "downloaded_valid_new_glb":[], "payment_usd":0,
      "status":"NO_RELEASE / UNREVIEWED"}
    for fn in records["preflight"]:
        if not pathlib.Path(fn).exists():raise FileNotFoundError(fn)
    rejected=(ROOT/"known_rejected_asset_sha256_registry.json").read_text(errors="replace")
    import requests
    from playwright.sync_api import sync_playwright,TimeoutError as PWT
    ss=requests.Session()
    ss.headers.update({"User-Agent":"Mozilla/5.0 Owl172 research, public no-fee/no-login source QA"})
    for key,url in SOURCES.items():
        rec={"url":url,"http":{},"browser":{},"downloads":[]}
        records["sources"][key]=rec
        try:
            resp=ss.get(url,timeout=35)
            rec["http"]={"status":resp.status_code,"final_url":resp.url,
              "content_type":resp.headers.get("content-type"),"bytes":len(resp.content),
              "sha256":sha(resp.content)}
            (OUT/f"{key}_public_http_excerpt.txt").write_text(resp.text[:9000],encoding="utf-8",errors="replace")
        except Exception as e:rec["http_error"]=repr(e)
    save_json("run155_partial.json",records)
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,args=["--no-sandbox","--disable-dev-shm-usage"])
        for key,url in SOURCES.items():
            rec=records["sources"][key]
            ctx=browser.new_context(viewport={"width":1380,"height":820},accept_downloads=True)
            page=ctx.new_page()
            try:
                resp=page.goto(url,wait_until="domcontentloaded",timeout=50000)
                page.wait_for_timeout(2300)
                rec["browser"]["initial_status"]=resp.status if resp else None
                rec["browser"]["initial_url"]=page.url
                rec["browser"]["title"]=page.title()
                body=page.locator("body").inner_text(timeout=10000)
                rec["browser"]["body_excerpt"]=legal_preview(body)
                rec["browser"]["anchors"]=[]
                for link in page.locator("a[href]").all()[:220]:
                    try:
                        a=link.get_attribute("href") or ""
                        t=(link.inner_text(timeout=800) or "").strip()[:110]
                        if any(x in (a+" "+t).lower() for x in ("download","owl","owlet",".glb")):
                            rec["browser"]["anchors"].append({"href":a[:300],"text":t})
                    except Exception:pass
                page.screenshot(path=str(OUT/f"{key}_initial_actual_browser.png"))
                # Resolve a linked community post from the public tag page, without API or login.
                if key=="meshy_heartfaced_barnowl_tag":
                    matches=[x for x in rec["browser"]["anchors"] if "heart" in (x["text"]+" "+x["href"]).lower()]
                    rec["browser"]["heart_matches"]=matches[:20]
                    try:
                        term=page.get_by_text("Heart-faced Barn Owl",exact=True)
                        rec["browser"]["heart_title_visible"]=term.count()>0
                        if term.count()>0:
                            a=term.first.locator("xpath=ancestor::a[1]")
                            if a.count(): rec["browser"]["heart_post_link"]=a.first.get_attribute("href")
                    except Exception as e:rec["browser"]["heart_lookup_error"]=repr(e)
                if any(x in page.url.lower() for x in ("login","signin","checkout","captcha","challenge")):
                    rec["browser"]["access_block"]="already on authentication or challenge";continue
                # Only click explicitly visible public download controls. No registration or checkout.
                download_locs=page.get_by_role("button",name=re.compile(r"download|下载",re.I))
                if download_locs.count()==0:
                    download_locs=page.get_by_role("link",name=re.compile(r"download|下载",re.I))
                rec["browser"]["download_controls"]=download_locs.count()
                if download_locs.count():
                    chosen=download_locs.first
                    try:
                        label=chosen.inner_text(timeout=1500)
                        rec["browser"]["clicked_label"]=label[:160]
                        if any(x in label.lower() for x in ("buy","purchase","pay","subscribe")):
                            rec["browser"]["access_block"]="payment labelled";continue
                        with page.expect_download(timeout=9000) as evt:
                            chosen.click(timeout=6000)
                        dl=evt.value
                        suggestion=dl.suggested_filename
                        destination=OUT/(key+"_download_quarantine.tmp")
                        dl.save_as(destination)
                        b=destination.read_bytes(); destination.unlink()
                        info=check_glb(b)
                        info.update({"suggested_name":suggestion,"ui_download":True})
                        rec["downloads"].append(info)
                        if info["valid_glb"]:
                            if info["sha256"] in rejected:
                                info["previously_rejected"]=True
                            else:
                                fn=key+"_genuine_3d_SOURCE_UNAPPROVED.glb"
                                (OUT/fn).write_bytes(b)
                                records["downloaded_valid_new_glb"].append({"name":fn,**info})
                    except PWT:
                        page.wait_for_timeout(1000)
                        page.screenshot(path=str(OUT/f"{key}_after_download_click.png"))
                        txt=page.locator("body").inner_text(timeout=10000)[:3000].lower()
                        rec["browser"]["after_click_url"]=page.url
                        rec["browser"]["after_click_excerpt"]=txt[:2500]
                        if any(x in page.url.lower() for x in ("login","signin","checkout","captcha","challenge")) or any(x in txt for x in BLOCK):
                            rec["browser"]["access_block"]="download requires login/verification/purchase; not bypassed"
                        else:
                            rec["browser"]["download_event"]="none during bounded 9s; not a downloaded model"
                    except Exception as e:rec["browser"]["download_error"]=repr(e)
                else:rec["browser"]["access_block"]="no public download control; cannot claim local model"
            except Exception as e:
                rec["browser"]["error"]=repr(e)
                try:page.screenshot(path=str(OUT/f"{key}_error_actual_browser.png"))
                except Exception:pass
            finally:
                save_json("run155_partial.json",records)
                ctx.close()
        browser.close()
    save_json("run155_actual_public_ui_probe.json",records)
    (OUT/"NO_RELEASE.flag").write_text(
      "No art approval. No purchase, no private source access, no mobile device verified. "
      "Any source model stays quarantined pending 4-view human art review and rights checks.\n")
    print("RUN155_ACTUAL_PUBLIC_UI_FINISHED",json.dumps({
      "valid_new_GLBS":len(records["downloaded_valid_new_glb"]),
      "states":{k:v.get("browser",{}).get("access_block",v.get("browser",{}).get("error","checked"))
          for k,v in records["sources"].items()}},ensure_ascii=False))

if __name__=="__main__":
    try:probe()
    except Exception:
        (OUT/"RUN155_ERROR.txt").write_text(traceback.format_exc())
        raise
