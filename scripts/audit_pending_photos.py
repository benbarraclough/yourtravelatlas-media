"""Small public Commons candidate audit; no auth, proxies or access-control bypass."""
import json,html,re,io
from pathlib import Path
import requests
from PIL import Image,ImageOps
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"review/candidates/porto-riviera"
def clean(s):return re.sub("<[^>]+>"," ",html.unescape(s or "")).strip()
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 session=requests.Session()
 session.headers["User-Agent"]="YourTravelAtlasEditorial/1.0 (public travel image research)"
 results=[]
 jobs=[("Porto essentials",{"titles":"File:Clérigos Church (Igreja dos Clérigos) Porto, horizontal.jpg|File:A Livraria Lello e Irmão-A ponte de encanto.jpg|File:Lello Bookshop 9 April 2026.jpg|File:Torre de los Clérigos, Oporto, Portugal, 2012-05-09, DD 01.JPG"}),("Riviera train",{"generator":"search","gsrsearch":"file: Villefranche train TER","gsrnamespace":6,"gsrlimit":8})]
 for label,query in jobs:
  try:
   r=session.get("https://commons.wikimedia.org/w/api.php",params={"action":"query","format":"json","formatversion":2,"prop":"imageinfo","iiprop":"url|size|extmetadata","iiurlwidth":1600,**query},timeout=35)
   if r.status_code in (403,429):
    results.append({"query":label,"status":"blocked","http_status":r.status_code});break
   r.raise_for_status()
   for p in r.json().get("query",{}).get("pages",[]):
    if not p.get("imageinfo"):continue
    i=p["imageinfo"][0];m=i.get("extmetadata",{})
    rec={"query":label,"title":p["title"],"source_page":i.get("descriptionurl"),"image_url":i.get("thumburl",i.get("url")),"original_url":i.get("url"),"width":i.get("width"),"height":i.get("height"),"license":clean(m.get("LicenseShortName",{}).get("value")),"license_url":clean(m.get("LicenseUrl",{}).get("value")),"photographer":clean(m.get("Artist",{}).get("value")),"description":clean(m.get("ImageDescription",{}).get("value"))}
    if rec["license"] not in ("CC BY 4.0","CC BY-SA 4.0","CC BY 2.0","CC0"):
     rec["status"]="unsupported_license";results.append(rec);continue
    try:
     d=session.get(rec["image_url"],timeout=35);d.raise_for_status()
     im=ImageOps.exif_transpose(Image.open(io.BytesIO(d.content))).convert("RGB");im.thumbnail((1000,1200))
     f=OUT/("candidate-"+str(len(results)+1).zfill(2)+".jpg");im.save(f,quality=88)
     rec.update(status="candidate_requires_visual_review",preview=str(f.relative_to(ROOT)))
    except Exception as e:rec.update(status="image_failed",reason=str(e)[:180])
    results.append(rec)
  except Exception as e:results.append({"query":label,"status":"failed","reason":str(e)[:200]})
 (OUT/"manifest.json").write_text(json.dumps(results,indent=2,ensure_ascii=False)+"\n")
 print(json.dumps(results,ensure_ascii=False))
if __name__=="__main__":main()
