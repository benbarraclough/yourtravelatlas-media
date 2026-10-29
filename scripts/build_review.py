#!/usr/bin/env python3
"""Build a portable, photo-exact owner review from current rendered carousels."""
import base64
import html
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'review'

def build():
    OUT.mkdir(exist_ok=True)
    sections=[]
    captions=['# Your Travel Atlas — captions for approval\n\nBoth v6 remakes await owner approval. These are the exact candidate captions.\n']
    for path in sorted((ROOT/'content/posts').glob('*.json')):
        post=json.loads(path.read_text())
        if post.get('editorial_version',0)<6: continue
        slug=post['slug']; images=[]; n=len(post['slides'])
        sheet=Image.new('RGB',(1080,((n+2)//3)*475),(245,242,234)); pen=ImageDraw.Draw(sheet)
        for i,item in enumerate(post['slides']):
            file=ROOT/'media'/slug/f'{i+1:02d}.jpg'
            encoded=base64.b64encode(file.read_bytes()).decode('ascii')
            images.append(f'<figure><img src="data:image/jpeg;base64,{encoded}" alt="{html.escape(item["alt"],quote=True)}"><figcaption>Slide {i+1} of {n}</figcaption></figure>')
            im=Image.open(file).resize((348,435)); x=i%3*360+6;y=i//3*475;sheet.paste(im,(x,y));pen.text((x+5,y+442),f'{i+1:02d}',fill=(20,30,30),font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',20))
        sheet.save(OUT/(slug+'-preview.jpg'),quality=94)
        sections.append(f'<section id="issue{post["issue"]}"><h2>{html.escape(post["headline"])}</h2><p class="meta">Issue {post["issue"]:03d} · {n} slides · awaiting your approval</p><div class="review"><div><p class="hint">Swipe or scroll sideways to see every slide →</p><div class="carousel">{"".join(images)}</div></div><div class="caption"><h3>Full Instagram caption</h3><div class="copy">{html.escape(post["caption"])}</div></div></div></section>')
        captions.append(f'## {post["headline"]}\n\n{post["caption"]}\n')
    style='''*{box-sizing:border-box}body{margin:0;background:#f7f4eb;color:#203331;font:16px/1.55 system-ui,sans-serif}main{max-width:1180px;margin:auto;padding:32px 24px 80px}header{border-bottom:1px solid #c9cbbf;padding-bottom:24px}h1{font:42px/1.1 Georgia,serif;margin:12px 0}h2{font:32px/1.2 Georgia,serif;margin-bottom:5px}h3{font-size:16px;margin-top:0}nav a{color:#203331;margin-right:20px}.meta,.hint{font-size:13px;color:#596d65}section{padding-top:26px;margin-bottom:48px}.review{display:grid;grid-template-columns:minmax(0,480px) minmax(0,1fr);gap:36px;align-items:start}.carousel{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:16px;padding-bottom:12px}figure{margin:0;flex:0 0 100%;scroll-snap-align:start}figure img{width:100%;height:auto;display:block;border-radius:3px}figcaption{font-size:13px;padding-top:6px}.caption{padding-top:44px}.copy{white-space:pre-wrap}.status{display:inline-block;background:#e3e9db;color:#354b32;border-radius:20px;padding:5px 12px;font-size:13px}@media(max-width:800px){main{padding:20px 16px 50px}.review{grid-template-columns:1fr;gap:12px}.carousel{max-width:480px}.caption{padding-top:12px}h1{font-size:34px}}'''
    page='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Your Travel Atlas — carousel approval</title><style>'+style+'</style><main><header><span class="status">Ready for your review</span><h1>Your Travel Atlas</h1><p>Two photo-led remakes. Every image and complete caption below is part of the proposed edition.</p><nav><a href="#issue2">Porto</a><a href="#issue3">French Riviera</a></nav></header>'+''.join(sections)+'</main></html>'
    (OUT/'index.html').write_text(page)
    (OUT/'captions.md').write_text('\n'.join(captions))
    print('Built portable approval page, exact captions and two contact sheets.')

if __name__=='__main__': build()
