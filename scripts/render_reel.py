#!/usr/bin/env python3
"""Produce editorial 9:16 Reels from PRE-VERIFIED, free licensed footage.
Uses standard Ubuntu FFmpeg only; never adds copyrighted/trending music.
Fails closed on missing or invalid real video inputs.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import urlsplit
import requests

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"content"/"reels"
OUTPUT=ROOT/"media"/"reels"
WIDTH, HEIGHT, FPS = 720, 1280, 30
FONT_REG="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_SERIF="/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
S=requests.Session()
S.headers.update({"User-Agent":"Mozilla/5.0 (YourTravelAtlas editorial media renderer)"})
MAX_MB=110

def run(*cmd):
    p=subprocess.run([str(x) for x in cmd],capture_output=True,text=True)
    if p.returncode:
        raise RuntimeError(f"Command failed: {p.args[:3]}:\n{p.stderr[-3500:]}")
    return p.stdout

def esc(s):
    # Text in drawtext is supplied through a UTF-8 file to avoid filtergraph
    # escaping problems and interpolation of third-party content.
    return str(s).replace("\\","\\\\").replace(":","\\:").replace("'","\\'").replace("%","\\%").replace(",","\\,")

def probe(path):
    p=json.loads(run("ffprobe","-v","error","-show_streams","-show_format","-of","json",path))
    streams=[x for x in p.get("streams",[]) if x.get("codec_type")=="video"]
    if not streams: raise ValueError("Video file has no video stream")
    v=streams[0]
    width,height=int(v.get("width",0)),int(v.get("height",0))
    duration=float(p.get("format",{}).get("duration") or 0)
    if width<650 or height<650 or duration<2.5:
        raise ValueError(f"Unusable source clip: {width}x{height}, {duration:.2f}s")
    return {"width":width,"height":height,"duration":duration}

def download(clip,tmp):
    url=clip["download_url"]
    parsed=urlsplit(url)
    if parsed.scheme!="https" or parsed.hostname not in ("www.pexels.com","videos.pexels.com","cdn.pixabay.com","upload.wikimedia.org"):
        raise ValueError("Only public, supported licensed video download hosts")
    result=S.get(url,timeout=(15,100),stream=True,allow_redirects=True)
    result.raise_for_status()
    if result.url.startswith("http:"): raise ValueError("Unencrypted final download")
    ct=result.headers.get("Content-Type","")
    if any(x in ct for x in ("text/html","application/json")):
        raise ValueError(f"Video download gave non-media response {ct} ({result.url})")
    count=0
    with open(tmp,"wb") as f:
        for chunk in result.iter_content(128*1024):
            if not chunk:continue
            count+=len(chunk)
            if count>MAX_MB*1024*1024:raise ValueError("Video source exceeds 110MB")
            f.write(chunk)
    if count<40_000:raise ValueError("Video source too small")
    data=probe(tmp)
    return {"source_sha256":hashlib.sha256(Path(tmp).read_bytes()).hexdigest(),"source_bytes":count,**data}

def text_file(tmp_dir,name,value):
    filename=tmp_dir/(name+".txt")
    filename.write_text(value,encoding="utf-8")
    return filename

def textfilter(path,size,y,color="white",font=FONT_BOLD,center=False):
    # drawtext textfile and precise fixed margins maintain accessibility and safe framing
    x="(w-text_w)/2" if center else "60"
    return f"drawtext=fontfile={font}:textfile={path}:fontsize={size}:fontcolor={color}:x={x}:y={y}:shadowcolor=black@0.65:shadowx=2:shadowy=3"

def main(postfile):
    brief=json.loads(postfile.read_text(encoding="utf-8"))
    required=("issue","slug","destination","hook","caption","editorial_intent","share_reason","clips","fact_sources")
    for key in required:
        if not brief.get(key):raise ValueError(f"Missing {key}")
    if not re.fullmatch(r"[0-9]{3}-[a-z0-9-]+",brief["slug"]):raise ValueError("Bad slug")
    clips=brief["clips"]
    if len(clips)<3 or len(clips)>6:raise ValueError("Reels require 3-6 independent moving shots")
    if len(set(x["page_url"] for x in clips))!=len(clips):raise ValueError("Duplicate footage")
    for clip in clips:
        for k in ("page_url","photographer","license","description","overlay","download_url","activity_source"):
            if not clip.get(k):raise ValueError(f"Missing source field {k}")
        if clip["license"] not in ("Pexels License","CC BY 4.0","CC BY-SA 4.0"):
            raise ValueError("Unsupported/unverified video license")
        if clip["activity_source"] not in brief["fact_sources"]:
            raise ValueError("No independent activity/fact source")
        if "pexels.com/video/" not in clip["page_url"] and "commons.wikimedia.org/" not in clip["page_url"]:
            raise ValueError("Video page URL must point at inspectable source")
        if len(clip["overlay"])>68:raise ValueError("Text too long for 9:16 Reel overlay")
    if brief.get("audio_policy")!="silent":
        raise ValueError("Reel audio not cleared, default to silent")

    output=OUTPUT/brief["slug"]
    output.mkdir(parents=True,exist_ok=True)
    temp=output/"_work"
    if temp.exists(): shutil.rmtree(temp)
    temp.mkdir()
    pieces=[]
    evidence=[]
    try:
        for i,clip in enumerate(clips):
            src=temp/f"source{i:02d}.mp4"
            meta=download(clip,src)
            seconds=min(float(clip.get("seconds",3.4)),meta["duration"]-0.3)
            if seconds<2.5 or seconds>6:raise ValueError("Clip segment duration out of bounds")
            txt=text_file(temp,f"caption{i}",clip["overlay"])
            destination=text_file(temp,f"destination{i}",brief["destination"].upper())
            brand=text_file(temp,f"brand{i}","YOUR TRAVEL ATLAS")
            progress=text_file(temp,f"progress{i}",f"{i+1:02d} / {len(clips):02d}")
            tagline=text_file(temp,f"tagline{i}","WANDER FURTHER  /  @YOURTRAVELATLAS")
            # 9:16 full bleed, intentional text only in safe bands.
            filters=[
                "scale=720:1280:force_original_aspect_ratio=increase",
                "crop=720:1280",
                "setsar=1",
                "format=yuv420p",
                textfilter(brand,27,95),
                textfilter(progress,21,140),
                textfilter(destination,30,785),
                textfilter(txt,37,850),
                textfilter(tagline,18,1135),
            ]
            piece=temp/f"piece{i:02d}.mp4"
            run("ffmpeg","-hide_banner","-loglevel","error","-y",
                "-ss",clip.get("start",0),"-i",src,"-t",str(seconds),
                "-vf",",".join(filters),"-an","-r",str(FPS),
                "-c:v","libx264","-preset","veryfast","-crf","24",
                "-pix_fmt","yuv420p","-movflags","+faststart",
                str(piece))
            pieces.append(piece)
            evidence.append({
                "page_url":clip["page_url"],"photographer":clip["photographer"],
                "license":clip["license"],"description":clip["description"],
                "activity_source":clip["activity_source"],"overlay":clip["overlay"],
                "clip_seconds":round(seconds,2),**meta,
            })
            print(f"  {i+1}/{len(clips)} {clip['description']} ({seconds:.2f}s)",flush=True)
        concat=temp/"files.txt"
        concat.write_text("".join(f"file '{p.absolute()}'\n" for p in pieces),encoding="utf-8")
        final=output/"reel.mp4"
        run("ffmpeg","-hide_banner","-loglevel","error","-y","-f","concat","-safe","0",
            "-i",concat,"-c","copy","-movflags","+faststart",str(final))
        final_meta=probe(final)
        if final.stat().st_size>38*1024*1024:
            raise ValueError("Final Reel file exceeds GitHub upload quality/size cap")
        if final_meta["width"]!=WIDTH or final_meta["height"]!=HEIGHT:
            raise ValueError("Unexpected output dimensions")
        duration=final_meta["duration"]
        if duration<9 or duration>50:raise ValueError("Unexpected output duration")
        # Silent audio is an intentional editorial default, not unlicensed music.
        manifest={
            "issue":brief["issue"],"slug":brief["slug"],"destination":brief["destination"],
            "hook":brief["hook"],"status":"rendered-not-published",
            "editorial_intent":brief["editorial_intent"],"share_reason":brief["share_reason"],
            "caption":brief["caption"],"fact_sources":brief["fact_sources"],
            "audio_policy":"silent","video":"reel.mp4",
            "width":WIDTH,"height":HEIGHT,"fps":FPS,
            "duration_seconds":round(duration,2),"size_bytes":final.stat().st_size,
            "clips":evidence
        }
        (output/"manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
        # Unique video cover thumbnail from first video frame, intended to be visually reviewed
        run("ffmpeg","-hide_banner","-loglevel","error","-y","-ss","1.0","-i",str(final),
            "-frames:v","1",str(output/"cover.jpg"))
        print("WROTE",final,f"{duration:.2f}s",flush=True)
    finally:
        shutil.rmtree(temp,ignore_errors=True)

if __name__=="__main__":
    files=[SOURCE/(arg+".json") for arg in sys.argv[1:]] if len(sys.argv)>1 else sorted(SOURCE.glob("*.json"))
    if not files:
        print("No Reel briefs found; no videos rendered")
    for p in files: main(p)
