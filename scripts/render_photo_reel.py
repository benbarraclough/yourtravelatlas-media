#!/usr/bin/env python3
"""Silent editorial photo Reels from verified real licensed stills (no synthetic travel imagery)."""
import hashlib, json, re, shutil, subprocess, tempfile
from pathlib import Path
from urllib.parse import urlsplit
import requests
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"media"/"reels"
SIZE=(1080,1920)
VALID_HOSTS={"images.unsplash.com","images.pexels.com","upload.wikimedia.org"}
FREE_LICENSES={"Unsplash License","Pexels License","CC0 1.0","Public Domain"}
REG="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SERIF="/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"

def command(*args):
    r=subprocess.run([str(a) for a in args],capture_output=True,text=True)
    if r.returncode: raise RuntimeError("ffmpeg failure: "+r.stderr[-1600:])
    return r.stdout

def lines(draw, s, font, width, max_lines):
    if len(str(s))>120: raise ValueError("Overlay too long")
    out=[]; line=""
    for word in str(s).split():
        test=(line+" "+word).strip()
        if draw.textbbox((0,0),test,font=font)[2]<=width: line=test
        else:
            if line: out.append(line)
            if draw.textbbox((0,0),word,font=font)[2]>width: raise ValueError("Overlay word too wide")
            line=word
    if line: out.append(line)
    if len(out)>max_lines: raise ValueError("Overlay too dense for phone")
    return out

def frame_from_photo(photo,shot,brief,first):
    if min(photo.size)<1000 or photo.width<900 or photo.height<1150:
        raise ValueError("Source photo lacks sufficient original detail for 9:16 Reel")
    # Explicit location-specific image already verified by the editor; not a generic stock substitute.
    focus=(max(0,min(1,float(shot.get("focus_x",0.5)))),max(0,min(1,float(shot.get("focus_y",0.5)))))
    im=ImageOps.fit(photo.convert("RGB"),SIZE,method=Image.Resampling.LANCZOS,centering=focus).convert("RGBA")
    # Restrained contrast backing, no banners.
    shade=Image.new("RGBA", SIZE,(0,0,0,0))
    q=ImageDraw.Draw(shade)
    for y in range(1150,1920,4):
        alpha=round(180*(y-1150)/770)
        q.rectangle((0,y,1080,y+4),fill=(0,0,0,alpha))
    im=Image.alpha_composite(im,shade)
    d=ImageDraw.Draw(im)
    d.text((72,155),"@yourtravelatlas",font=ImageFont.truetype(REG,29),fill="white",stroke_width=1,stroke_fill="#25313a")
    heading=brief["hook"] if first else shot["overlay"]
    # A subtle country label prevents regional titles from hiding the destination country.
    country=str(brief.get("country_label","")).strip().upper()
    if first and country:
        if len(country)>34: raise ValueError("Country label too long")
        d.text((76,1362),country,font=ImageFont.truetype(REG,32),fill="white",stroke_width=1,stroke_fill="#333333")
    # Match the actual size of words rather than killing the render for an ordinary sentence.
    wrapped=None
    for size in ((72,67,62,58) if first else (65,60,56,52,48)):
        f=ImageFont.truetype(SERIF,size)
        try:
            wrapped=lines(d,heading,f,936,3)
            break
        except ValueError:
            continue
    if wrapped is None: raise ValueError("Overlay cannot fit legibly at minimum font size")
    step=size+13
    y=1430 if first else 1510
    for line in wrapped:
        d.text((72,y),line,font=f,fill="white",stroke_width=2,stroke_fill="#333333")
        y+=step
    if first:
        caption=brief["destination"]
        d.text((76,1762),caption[:45],font=ImageFont.truetype(REG,37),fill="white",stroke_width=1,stroke_fill="#333333")
    return im.convert("RGB")

def download_image(shot):
    url=shot["image_url"]
    if urlsplit(url).scheme!="https" or urlsplit(url).hostname not in VALID_HOSTS:
        raise ValueError("Unsupported public original photo CDN")
    r=requests.get(url,timeout=(12,50),headers={"User-Agent":"YourTravelAtlas-photo-reel/1.0"})
    r.raise_for_status()
    if len(r.content)>24*1024*1024: raise ValueError("Source image too large")
    from io import BytesIO
    im=Image.open(BytesIO(r.content))
    im.load()
    if im.width<900 or im.height<1150: raise ValueError("Source resolution insufficient")
    return im, hashlib.sha256(r.content).hexdigest()

def render(path):
    brief=json.loads(path.read_text(encoding="utf-8"))
    images=brief.get("images",[])
    if brief.get("treatment")!="photo_slideshow_v1": raise ValueError("Not a photo Reel brief")
    if len(images)<5 or len(images)>10: raise ValueError("Photo Reels require 5-10 real different photographs")
    if len(brief.get("caption",""))>2200: raise ValueError("Caption too long")
    if brief.get("audio_policy")!="no_music": raise ValueError("No music or audio")
    if len({s["image_url"].split("?")[0] for s in images})!=len(images):raise ValueError("Duplicated image")
    if len({s["source_page"] for s in images})!=len(images):raise ValueError("Duplicated source")
    for s in images:
        if s.get("license") not in FREE_LICENSES: raise ValueError("Unverified or unsupported reuse licence")
        if not s.get("location_evidence") or len(s["location_evidence"])<30: raise ValueError("Missing exact location verification")
        if not str(s.get("source_page","")).startswith("https://"): raise ValueError("Missing image source page")
        if not s.get("photographer") or s["photographer"].casefold() not in brief.get("caption","").casefold():
            raise ValueError("Missing correct photographer in public caption")
        if not s.get("overlay"): raise ValueError("Every still needs a short specific on-screen description")
    folder=OUT/brief["slug"]
    folder.mkdir(parents=True,exist_ok=True)
    records=[]
    previews=[]
    with tempfile.TemporaryDirectory() as td:
        tmp=Path(td); pieces=[]
        for i,s in enumerate(images):
            pic,rawhash=download_image(s)
            img=frame_from_photo(pic,s,brief,i==0)
            previews.append(img.resize((360,640),Image.Resampling.LANCZOS))
            frame=tmp/f"{i:02d}.png";img.save(frame)
            if i==0:img.save(folder/"cover.jpg",quality=91)
            piece=tmp/f"piece{i:02d}.mp4"
            # Slow Ken Burns crop creates genuine video from stills, not a mislabeled image carousel.
            filt="scale=1200:2134,zoompan=z='min(pzoom+0.00045,1.055)':d=1:x='(iw-iw/zoom)/2':y='(ih-ih/zoom)/2':s=1080x1920:fps=30,format=yuv420p"
            command("ffmpeg","-hide_banner","-loglevel","error","-y","-loop","1","-framerate","30","-i",frame,
                    "-frames:v","87","-vf",filt,"-an","-c:v","libx264","-threads","2","-preset","veryfast","-crf","23",
                    "-pix_fmt","yuv420p","-movflags","+faststart",piece)
            pieces.append(piece)
            records.append({"source_page":s["source_page"],"photographer":s["photographer"],"license":s["license"],
                            "subject":s.get("subject"),"overlay":s["overlay"],"source_sha256":rawhash,
                            "location_evidence":s["location_evidence"]})
        listing=tmp/"list.txt"
        listing.write_text("".join("file '"+str(p)+"'\n" for p in pieces),encoding="utf-8")
        file=folder/"reel.mp4"
        command("ffmpeg","-hide_banner","-loglevel","error","-y","-f","concat","-safe","0","-i",listing,
                "-map","0:v:0","-an","-c","copy","-movflags","+faststart",file)
    sheet=Image.new("RGB",(1080,640*((len(previews)+2)//3)),(24,24,24))
    for k,small in enumerate(previews):sheet.paste(small,((k%3)*360,(k//3)*640))
    sheet.save(folder/"storyboard.jpg",quality=87,optimize=True)
    stream=json.loads(command("ffprobe","-v","error","-show_streams","-show_format","-of","json",file))
    if any(s.get("codec_type")=="audio" for s in stream["streams"]):raise ValueError("Unexpected audio stream")
    video=[s for s in stream["streams"] if s.get("codec_type")=="video"]
    if len(video)!=1 or int(video[0]["width"])!=1080 or int(video[0]["height"])!=1920:
        raise ValueError("Wrong output size")
    if file.stat().st_size>70*1024*1024:raise ValueError("Output too large for host")
    manifest={"status":"rendered-not-scheduled","type":"photo_slideshow_v1","video":"reel.mp4",
              "cover":"cover.jpg","source_brief":str(path.relative_to(ROOT)),
              "brief_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
              "video_sha256":hashlib.sha256(file.read_bytes()).hexdigest(),"audio_streams":0,
              "image_count":len(images),"duration_seconds":float(stream["format"]["duration"]),
              "caption":brief["caption"],"images":records}
    (folder/"manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print("PHOTO REEL RENDERED",brief["slug"],len(images),"stills",manifest["duration_seconds"],"s / silent",flush=True)

if __name__=="__main__":
    import sys
    for f in sys.argv[1:]:
        render(ROOT/"content"/"reels"/(f+".json"))
