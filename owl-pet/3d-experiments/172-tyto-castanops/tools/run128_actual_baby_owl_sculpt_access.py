#!/usr/bin/env python3
"""Run128: publisher-page-only $0 access test for genuine juvenile owl sculpt bases.

Does not sign up, log in, pay, retry a CAPTCHA, scrape private download URLs,
or publish a third-party mesh. Every result has a negative release gate.
"""
import hashlib
import json
import os
import re
import sys
import time
import zipfile
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

from playwright.sync_api import sync_playwright, TimeoutError as BrowserTimeout

TARGETS = [
    ("artistfrog_sculpt", "https://www.cgtrader.com/free-3d-models/animal/bird/free-baby-owl-sculpt"),
    ("richardshaw_barn_owl_kid", "https://www.cgtrader.com/free-3d-models/character/man/baby-owl-animated-black"),
]
MAX_DOWNLOAD = 130 * 1024 * 1024
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/run128"); OUT.mkdir(parents=True,exist_ok=True)
report = {"date_utc":time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
          "task":"#172 cream-white downy masked-owl juvenile professional sculpt source access",
          "sources":[], "art_gate":"ART_UNREVIEWED", "release":"NO_RELEASE", "payment_usd":0}

def redact_url(u):
    p=urlsplit(u or "")
    return urlunsplit((p.scheme,p.netloc,p.path,"",""))

def record_file(path):
    s=path.stat().st_size
    h=hashlib.sha256()
    with path.open("rb") as f:
        while True:
            b=f.read(4*1024*1024)
            if not b:break
            h.update(b)
    ans={"download_bytes":s,"sha256":h.hexdigest(),"filename":path.name,
         "format":"unknown", "archive_entries":[]}
    with path.open("rb") as f: magic=f.read(32)
    if magic[:4] == b"glTF": ans["format"]="GLB"
    elif magic.startswith(b"BLENDER"): ans["format"]="BLEND"
    elif magic.startswith(b"Kaydara FBX Binary"): ans["format"]="FBX"
    elif magic.startswith(b"PK\x03\x04"):
        ans["format"]="ZIP"
        try:
            with zipfile.ZipFile(path) as z:
                names=z.namelist()
                ans["archive_entries"]=[{"name":n[:180],"size":z.getinfo(n).file_size} for n in names[:80]]
                ans["archive_entry_count"]=len(names)
                ans["zip_test"]=z.testzip() is None
        except Exception as e:ans["zip_error"]=str(e)[:150]
    elif path.suffix.lower()==".obj":ans["format"]="OBJ_UNCONFIRMED"
    return ans

with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,args=["--no-sandbox"])
    for tag,url in TARGETS:
        item={"id":tag,"source_url":url,"source_kind":"artist listing (not rights clearance)",
              "model_download":False,"rights_cleared":False}
        ctx=browser.new_context(accept_downloads=True,viewport={"width":1240,"height":900},
                                user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36")
        page=ctx.new_page()
        try:
            response=page.goto(url,wait_until="domcontentloaded",timeout=50000)
            page.wait_for_timeout(2600)
            item["http_status"]=response.status if response else None
            item["final_url"]=redact_url(page.url)
            item["page_title"]=page.title()[:220]
            txt=page.locator("body").inner_text(timeout=12000)
            item["public_text_excerpt"]=txt[:1800]
            item["listing_has_free_label"]=bool(re.search(r"Free Download|Download for Free|Free 3D model",txt,re.I))
            item["listing_license_no_ai"]=bool(re.search(r"Royalty Free License\s*\(no AI\)",txt,re.I))
            item["login_gate_text"]=bool(re.search(r"Log in to download|Login to download|Sign in to download",txt,re.I))
            page.screenshot(path=str(OUT/(tag+"_listing.png")),full_page=False)
            # Interact only with visibly free download controls on the publisher's own page.
            # Never interact with cart, paid offers, account logins or CAPTCHA.
            if not item["listing_has_free_label"]:
                item["access"]="NO_VERIFIABLE_FREE_LISTING"
            else:
                candidates = [
                    page.get_by_role("button",name=re.compile(r"^Free Download$",re.I)),
                    page.get_by_role("link",name=re.compile(r"^Free Download$",re.I)),
                    page.get_by_text("Free Download",exact=True),
                    page.get_by_role("button",name=re.compile(r"^Download for Free$",re.I)),
                    page.get_by_role("link",name=re.compile(r"^Download for Free$",re.I)),
                ]
                found=None
                for candidate in candidates:
                    if candidate.count():
                        el=candidate.first
                        if el.is_visible() and el.is_enabled():
                            found=el; break
                if found is None:
                    item["access"]="VISIBLE_FREE_BUTTON_NOT_FOUND"
                else:
                    item["access"]="CLICKED_OFFICIAL_FREE_DOWNLOAD"
                    # The file is genuine only if Chromium actually emits a download event.
                    try:
                        with page.expect_download(timeout=18000) as download_info:
                            found.click(timeout=9000)
                        d=download_info.value
                        src=Path(d.path())
                        item["suggested_filename"]=d.suggested_filename
                        item.update(record_file(src))
                        item["model_download"]=item["format"] in ("GLB","BLEND","FBX","OBJ_UNCONFIRMED") or (
                            item["format"]=="ZIP" and item.get("zip_test") is True and
                            any(re.search(r"\.(blend|fbx|obj|glb|gltf)$",v["name"],re.I) for v in item.get("archive_entries",[]))
                        )
                        # Do not redistribute a third-party raw file under royalty-free/no-AI terms.
                        item["raw_file_archived"]=False
                        item["access"]="DOWNLOADED_OFFICIAL_BUT_RIGHTS_NOT_CLEARED" if item["model_download"] else "DOWNLOADED_NON_MODEL_FILE"
                    except BrowserTimeout:
                        item["access"]="NO_DOWNLOAD_EVENT_OR_LOGIN_GATE"
                        item["after_click_url"]=redact_url(page.url)
                        item["after_click_body_excerpt"]=page.locator("body").inner_text(timeout=10000)[:1500]
                    except Exception as e:
                        item["access"]="OFFICIAL_FREE_CLICK_ERROR"
                        item["click_error"]=str(e)[:400]
                    page.wait_for_timeout(1000)
                    page.screenshot(path=str(OUT/(tag+"_after_click.png")),full_page=False)
        except Exception as e:
            item["access"]="PAGE_ACCESS_ERROR"
            item["error"]=str(e)[:450]
            try:page.screenshot(path=str(OUT/(tag+"_error.png")))
            except Exception:pass
        finally:
            report["sources"].append(item);ctx.close()
    browser.close()
(OUT/"run128_source_access.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
(OUT/"NO_RELEASE.flag").write_text("ART_UNREVIEWED/NO_RELEASE: publisher listing or source-file access cannot establish #172 professional sculpt, four-view juvenile anatomy, global redistribution rights, real phone GPU performance.\n")
print(json.dumps({"result":[{"id":v["id"],"access":v.get("access"),"http":v.get("http_status"),"model":v["model_download"],"license_cleared":v["rights_cleared"]} for v in report["sources"]],"release":"NO_RELEASE"},ensure_ascii=False))
