#!/usr/bin/env python3
"""Inspect PUBLIC Unsplash candidate pages; do not scrape login-only material."""
import io, json, re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, parse_qsl, urlencode, urlunsplit
import requests
from PIL import Image, ImageOps
ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/"content"/"research"/"004-photo-candidate-pages.json"
OUT=ROOT/"review"/"candidates"/"004-japan-beyond-the-cities"
class Metadata(HTMLParser):
    def __init__(self): super().__init__();self.tags={}
    def handle_starttag(self,tag,attrs):
        if tag=="meta":
            a=dict(attrs);key=a.get("property") or a.get("name")
            if key in ("og:image","twitter:image","og:title"):self.tags[key]=a.get("content","")
def run():
    OUT.mkdir(parents=True,exist_ok=True)
    result=[]
    sess=requests.Session()
    sess.headers.update({"User-Agent":"Mozilla/5.0 (compatible; YourTravelAtlasResearch/1.0)"})
    for entry in json.loads(INPUT.read_text()):
        name,url=entry["name"],entry["page_url"]
        rec={"name":name,"page_url":url}
        try:
            r=sess.get(url,timeout=25);r.raise_for_status()
            parser=Metadata();parser.feed(r.text)
            original=parser.tags.get("og:image") or parser.tags.get("twitter:image")
            if not original:
                m=re.search(r"https://images\.unsplash\.com/photo-[0-9a-z-]+",r.text)
                if m:original=m.group(0)
            if not original or urlsplit(original).hostname!="images.unsplash.com":
                raise ValueError("No public first-party Unsplash image link on original page")
            base=original.split("?")[0]
            image_url=base+"?auto=format&fit=crop&w=2000&q=88"
            preview_url=base+"?auto=format&fit=crop&w=1000&q=85"
            p=sess.get(preview_url,timeout=40);p.raise_for_status()
            img=ImageOps.exif_transpose(Image.open(io.BytesIO(p.content))).convert("RGB")
            img.thumbnail((800,1000))
            img.save(OUT/(name+".jpg"),quality=84,optimize=True)
            rec.update({"status":"downloaded","image_url":image_url,"preview_file":str((OUT/(name+".jpg")).relative_to(ROOT)),"preview_size":list(img.size),"title":parser.tags.get("og:title","")})
        except Exception as exc:
            rec.update({"status":"failed","reason":str(exc)[:250]})
        print(rec,flush=True);result.append(rec)
    (OUT/"manifest.json").write_text(json.dumps(result,indent=2)+"\n")
if __name__=="__main__":run()
