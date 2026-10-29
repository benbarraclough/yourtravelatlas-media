#!/usr/bin/env python3
"""Produce editorial 9:16 Reels from PRE-VERIFIED, free licensed footage.
Uses standard Ubuntu FFmpeg only; never adds copyrighted/trending music.
Fails closed on missing or invalid real video inputs.
"""
import hashlib
import json
import os
import array
import math
import wave
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import urlsplit
import requests
from PIL import Image, ImageFont, ImageDraw

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"content"/"reels"
OUTPUT=ROOT/"media"/"reels"
WIDTH, HEIGHT, FPS = 1080, 1920, 30
FONT_REG="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_SERIF="/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
S=requests.Session()
S.headers.update({"User-Agent":"Mozilla/5.0 (YourTravelAtlas editorial media renderer)"})
MAX_MB=240

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
            if count>MAX_MB*1024*1024:raise ValueError("Video source exceeds 240MB")
            f.write(chunk)
    if count<40_000:raise ValueError("Video source too small")
    data=probe(tmp)
    return {"source_sha256":hashlib.sha256(Path(tmp).read_bytes()).hexdigest(),"source_bytes":count,**data}

def wrap_text(message, max_width=865, fontsize=57, max_lines=2, face_path=FONT_SERIF):
    face=ImageFont.truetype(face_path,fontsize)
    lines=[]
    buf=""
    for word in str(message).split():
        proposal=(buf+" "+word).strip()
        if face.getlength(proposal)<=max_width:
            buf=proposal
        else:
            if buf: lines.append(buf)
            if face.getlength(word)>max_width: raise ValueError(f"On-screen word exceeds safe width: {word}")
            buf=word
    if buf:lines.append(buf)
    if len(lines)>max_lines:raise ValueError(f"Overlay too long at mobile size: {message}")
    return "\n".join(lines)

def compose_original_upbeat(destination, seconds):
    """Compose an ORIGINAL, cheerful 112-BPM travel instrumental in C major.

    Entirely synthesized: lightly plucked guitar-like notes, a tuneful lead,
    warm bass and soft percussion. No samples, borrowed tunes or audio APIs.
    """
    rate = 32000
    bpm = 112
    beat = 60.0 / bpm
    chords = [
        (261.63, 329.63, 392.00, 493.88),  # Cmaj7
        (349.23, 440.00, 523.25, 659.25),  # Fmaj7
        (392.00, 493.88, 587.33, 783.99),  # Gadd
        (261.63, 329.63, 392.00, 587.33),  # Cadd9
    ]
    bass_notes = (130.81, 174.61, 196.00, 130.81)
    lead_notes = (659.25, 783.99, 880.00, 783.99, 659.25, 587.33, 523.25, 659.25,
                  698.46, 880.00, 783.99, 698.46, 659.25, 587.33, 523.25, 587.33)
    audio = array.array("h")
    for n in range(int(seconds*rate)):
        t = n/rate
        bar = int(t/(beat*4))
        chord_index = bar % 4
        chord = chords[chord_index]
        eighth = beat/2
        eighth_index = int(t/eighth)
        eighth_phase = (t % eighth)/eighth
        # A bouncy finger-picked pulse instead of the old long, sombre pad.
        pluck_note = chord[(0,2,1,3,2,1,3,1)[eighth_index % 8]]
        pluck_env = (1-math.exp(-40*eighth_phase))*math.exp(-4.1*eighth_phase)
        pluck = (math.sin(2*math.pi*pluck_note*t) +
                 0.22*math.sin(2*math.pi*2*pluck_note*t) +
                 0.08*math.sin(2*math.pi*3*pluck_note*t))*pluck_env*0.13
        # A bright but restrained, original four-bar melodic motif.
        lead_index = int(t/beat) % len(lead_notes)
        lead_phase = (t%beat)/beat
        freq = lead_notes[lead_index]
        lead_env = (1-math.exp(-30*lead_phase))*math.exp(-4.5*lead_phase)
        lead = (math.sin(2*math.pi*freq*t)+0.15*math.sin(2*math.pi*2*freq*t))*lead_env*0.067
        # Warm rhythmic bass and restrained soft percussion.
        beat_phase = t % beat
        bass = math.sin(2*math.pi*bass_notes[chord_index]*t)*math.exp(-3.0*beat_phase/beat)*0.085
        bass += 0.018*math.sin(2*math.pi*bass_notes[chord_index]*2*t)
        kick = 0.0
        if int(t/beat)%4 in (0,2) and beat_phase<0.18:
            kick = math.sin(2*math.pi*(74-35*beat_phase)*beat_phase)*math.exp(-28*beat_phase)*0.09
        # Deterministic high frequency noise is synthesized, not sampled.
        shimmer = (math.sin(2*math.pi*5033*t)*math.sin(2*math.pi*3167*t))
        hat = 0.022*shimmer*math.exp(-55*(t % eighth))
        clap_phase = (t % beat)
        clap = 0.0
        if int(t/beat)%4 in (1,3) and clap_phase<0.095:
            clap = 0.035*shimmer*math.exp(-30*clap_phase)
        # Fade in/out naturally so the clip loops with no sudden click.
        fade = min(1.0, t/0.24, max(0.0,(seconds-t)/0.6))
        value = (pluck+lead+bass+kick+hat+clap)*fade
        audio.append(int(max(-0.96,min(0.96,value))*32767))
    with wave.open(str(destination),"wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(rate)
        wav.writeframes(audio.tobytes())

def text_file(tmp_dir,name,value):
    filename=tmp_dir/(name+".txt")
    filename.write_text(value,encoding="utf-8")
    return filename

def textfilter(path,size,y,color="white",font=FONT_BOLD,center=False):
    # drawtext textfile and precise fixed margins maintain accessibility and safe framing
    x="(w-text_w)/2" if center else "90"
    return f"drawtext=fontfile={font}:textfile={path}:fontsize={size}:fontcolor={color}:x={x}:y={y}:line_spacing=12:shadowcolor=black@0.65:shadowx=2:shadowy=3"

def main(postfile):
    brief=json.loads(postfile.read_text(encoding="utf-8"))
    required=("reel_number","slug","destination","hook","caption","editorial_intent","share_reason","clips","fact_sources")
    for key in required:
        if not brief.get(key):raise ValueError(f"Missing {key}")
    if not re.fullmatch(r"[0-9]{3}-[a-z0-9-]+",brief["slug"]):raise ValueError("Bad slug")
    clips=brief["clips"]
    if len(clips)<5 or len(clips)>8:raise ValueError("Reels require 5-8 distinct moving shots")
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
    if brief.get("audio_policy")!="mixkit_stock":
        raise ValueError("The Reel must have verifiably cleared music, not unapproved AI/synth audio")
    track=brief.get("music",{})
    if track.get("source_page")!="https://mixkit.co/free-stock-music/indie-pop/" or track.get("title")!="Just Keep Walking" or track.get("artist")!="Michael Ramir C." or track.get("license")!="Mixkit Stock Music Free License":
        raise ValueError("Missing verified artist/track/music rights provenance")
    if track.get("download_url")!="https://assets.mixkit.co/active_storage/music/963/963.mp3":
        raise ValueError("Unexpected stock soundtrack URL")

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
            txt=text_file(temp,f"caption{i}",wrap_text(clip["overlay"],fontsize=57,face_path=FONT_SERIF))
            destination=text_file(temp,f"destination{i}",wrap_text(brief["destination"].split(",")[0].upper(),max_width=900,fontsize=74,face_path=FONT_SERIF))
            brand=text_file(temp,f"brand{i}","YOUR TRAVEL ATLAS")
            
            # 9:16 full bleed, intentional text only in safe bands.
            filters=[
                "scale=1080:1920:force_original_aspect_ratio=increase",
                "crop=1080:1920",
                "setsar=1",
                "format=yuv420p",
                textfilter(brand,28,153,font=FONT_REG),
                textfilter(destination,74,229,font=FONT_SERIF),
                textfilter(txt,57,1405,font=FONT_SERIF),
            ]
            # End of layout; no clip counts, no carousel issue numbers.
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
        silent=temp/"silent.mp4"
        run("ffmpeg","-hide_banner","-loglevel","error","-y","-f","concat","-safe","0",
            "-i",concat,"-c","copy","-movflags","+faststart",str(silent))
        duration_silent=probe(silent)["duration"]
        soundtrack=temp/"mixkit_stock.mp3"
        result=S.get(track["download_url"],timeout=35,stream=True)
        result.raise_for_status()
        if not result.url.startswith("https://assets.mixkit.co/"):
            raise ValueError("Music download redirected away from the licensed source")
        size=0
        with open(soundtrack,"wb") as out:
            for block in result.iter_content(128*1024):
                if not block:continue
                size+=len(block)
                if size>12_000_000:raise ValueError("Stock audio too large")
                out.write(block)
        details=json.loads(run("ffprobe","-v","error","-show_entries","format=duration:stream=codec_type,codec_name","-of","json",soundtrack))
        if float(details.get("format",{}).get("duration") or 0)<60 or not any(x.get("codec_type")=="audio" for x in details.get("streams",[])):
            raise ValueError("Licensed soundtrack not a valid longer-than-one-minute audio file")
        final=output/"reel.mp4"
        run("ffmpeg","-hide_banner","-loglevel","error","-y",
            "-i",str(silent),"-ss","18","-i",str(soundtrack),"-map","0:v:0","-map","1:a:0",
            "-c:v","copy","-c:a","aac","-b:a","128k","-ar","44100","-ac","2",
            "-af","loudnorm=I=-16:TP=-1.5:LRA=9",
            "-t",str(duration_silent),"-movflags","+faststart",str(final))
        final_meta=probe(final)
        streams=json.loads(run("ffprobe","-v","error","-show_streams","-of","json",final))["streams"]
        if not any(st.get("codec_type")=="audio" and st.get("codec_name")=="aac" for st in streams):
            raise ValueError("Final Reel missing playable AAC soundtrack")
        if final.stat().st_size>38*1024*1024:
            raise ValueError("Final Reel file exceeds GitHub upload quality/size cap")
        if final_meta["width"]!=WIDTH or final_meta["height"]!=HEIGHT:
            raise ValueError("Unexpected output dimensions")
        duration=final_meta["duration"]
        if duration<9 or duration>50:raise ValueError("Unexpected output duration")
        # Silent audio is an intentional editorial default, not unlicensed music.
        manifest={
            "reel_number":brief["reel_number"],"slug":brief["slug"],"destination":brief["destination"],
            "hook":brief["hook"],"status":"rendered-not-published",
            "editorial_intent":brief["editorial_intent"],"share_reason":brief["share_reason"],
            "caption":brief["caption"],"fact_sources":brief["fact_sources"],
            "audio_policy":"mixkit_stock",
            "soundtrack_provenance":track,
            "soundtrack_sha256":hashlib.sha256(soundtrack.read_bytes()).hexdigest(),
            "video":"reel.mp4",
            "width":WIDTH,"height":HEIGHT,"fps":FPS,
            "duration_seconds":round(duration,2),"size_bytes":final.stat().st_size,
            "clips":evidence
        }
        (output/"manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
        # Generate an opening cover and a multi-frame review contact sheet.
        thumbnails=[]
        middle=0.0
        for i,clip in enumerate(clips):
            mid=middle+evidence[i]["clip_seconds"]/2
            frame=temp/f"frame{i}.jpg"
            run("ffmpeg","-hide_banner","-loglevel","error","-y","-ss",str(mid),
                "-i",str(final),"-frames:v","1",str(frame))
            original=Image.open(frame).convert("RGB")
            thumbnails.append(original.resize((540,960),Image.Resampling.LANCZOS))
            middle += evidence[i]["clip_seconds"]
        contact=Image.new("RGB",(1080,960*((len(thumbnails)+1)//2)),(25,28,30))
        for i,frame in enumerate(thumbnails):
            contact.paste(frame,((i%2)*540,(i//2)*960))
        contact.save(output/"storyboard.jpg",quality=86,optimize=True)
        shutil.copy2(temp/"frame0.jpg",output/"cover.jpg")
        print("WROTE",final,f"{duration:.2f}s", "with licensed Mixkit AAC soundtrack",flush=True)
    finally:
        shutil.rmtree(temp,ignore_errors=True)

if __name__=="__main__":
    files=[SOURCE/(arg+".json") for arg in sys.argv[1:]] if len(sys.argv)>1 else sorted(SOURCE.glob("*.json"))
    if not files:
        print("No Reel briefs found; no videos rendered")
    for p in files:
        brief=json.loads(p.read_text(encoding="utf-8"))
        if brief.get("editorial_status")=="rejected":
            print(f"SKIP EDITORIALLY REJECTED REEL: {p.name}",flush=True)
            continue
        main(p)
