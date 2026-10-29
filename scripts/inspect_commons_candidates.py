#!/usr/bin/env python3
"""Research Commons photographs via its PUBLIC API. Never bypass blocked access."""
import io,json,html,re
from pathlib import Path
from urllib.parse import urlsplit
import requests
from PIL import Image,ImageOps
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"review"/"candidates"/"004-japan-beyond-the-cities"
API="https://commons.wikimedia.org/w/api.php"
QUERIES=["Shirakawa-go snow","Shirakawago winter village","Kamikochi Azusa river mountains","Tottori Sand Dunes"]
def strip_html(s):return re.sub("<[^>]+>"," ",html.unescape(s or "")).strip()
def main():
    OUT.mkdir(parents=True,exist_ok=True)
    session=requests.Session();session.headers["User-Agent"]="YourTravelAtlasEditorial/1.0 (educational travel research; contact via repository)"
    all_results=[]
    for term in QUERIES:
        try:
            r=session.get(API,params={"action":"query","generator":"search","gsrsearch":term,"gsrnamespace":6,"gsrlimit":8,"prop":"imageinfo","iiprop":"url|size|extmetadata","iiurlwidth":800,"format":"json","formatversion":2},timeout=35)
            r.raise_for_status()
            pages=r.json().get("query",{}).get("pages",[])
            print("QUERY",term,"RESULTS",len(pages),flush=True)
            for p in pages:
                infos=p.get("imageinfo") or []
                if not infos:continue
                inf=infos[0]; meta=inf.get("extmetadata",{})
                lic=strip_html(meta.get("LicenseShortName",{}).get("value",""))
                if lic not in ("CC BY 4.0","CC BY-SA 4.0","CC BY 2.0"):
                    all_results.append({"query":term,"title":p.get("title"),"status":"license_not_supported","license":lic,"width":inf.get("width"),"height":inf.get("height")})
                    continue
                url=inf.get("thumburl") or inf.get("url")
                if not url or urlsplit(url).hostname not in ("upload.wikimedia.org",):
                    all_results.append({"query":term,"title":p.get("title"),"status":"image_url_not_supported","license":lic,"url":url})
                    continue
                if inf.get("width",0)<1200 or inf.get("height",0)<1000:
                    all_results.append({"query":term,"title":p.get("title"),"status":"too_small","license":lic,"width":inf.get("width"),"height":inf.get("height")})
                    continue
                record={"query":term,"title":p.get("title"),"page_url":inf.get("descriptionurl"),"file_url":inf.get("url"),"license":lic,"license_url":strip_html(meta.get("LicenseUrl",{}).get("value","")),"author":strip_html(meta.get("Artist",{}).get("value",""))[:250],"description":strip_html(meta.get("ImageDescription",{}).get("value",""))[:400],"width":inf.get("width"),"height":inf.get("height")}
                try:
                    blob=session.get(url,timeout=30);blob.raise_for_status()
                    img=ImageOps.exif_transpose(Image.open(io.BytesIO(blob.content))).convert("RGB")
                    img.thumbnail((800,1000))
                    name="commons-"+str(len(all_results)+1).zfill(2)
                    img.save(OUT/(name+".jpg"),quality=83,optimize=True)
                    record["preview_file"]=str((OUT/(name+".jpg")).relative_to(ROOT))
                    record["status"]="downloaded"
                except Exception as exc:record["status"]="image_failed";record["reason"]=str(exc)[:160]
                all_results.append(record)
        except Exception as exc:
            all_results.append({"query":term,"status":"search_failed","reason":str(exc)[:240]})
    (OUT/"commons-manifest.json").write_text(json.dumps(all_results,ensure_ascii=False,indent=2)+"\n")
    print("Total",len(all_results),flush=True)
if __name__=="__main__":main()
