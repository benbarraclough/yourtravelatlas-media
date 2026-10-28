#!/usr/bin/env python3
"""Render curated travel carousels into publication-ready 1080x1350 JPEGs.

This is a DESIGN renderer, not a photo researcher or an accuracy verifier.
Only feed it reviewed manifests whose photo source pages and facts were checked.
It never publishes posts, pays for APIs, or uses generated landscape images.
"""
import hashlib
import io
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

import requests
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "content" / "posts"
OUTPUT = ROOT / "media"
SIZE = (1080, 1350)
ALLOWED_HOSTS = {"images.unsplash.com", "images.pexels.com", "upload.wikimedia.org"}
SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "YourTravelAtlasMediaRenderer/1.0 (public travel magazine)"})
REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"


def font(size, path=BOLD):
    return ImageFont.truetype(path, size)


def lines_to_fit(draw, message, face, width, max_lines=4):
    words = str(message).strip().split()
    lines, line = [], ""
    for word in words:
        candidate = f"{line} {word}".strip()
        if draw.textbbox((0, 0), candidate, font=face)[2] <= width:
            line = candidate
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    if len(lines) > max_lines:
        raise ValueError(f"Text too long to fit cleanly: {message!r}")
    return lines


def text_block(draw, text, xy, face, max_width, spacing=12, max_lines=4):
    x, y = xy
    result = lines_to_fit(draw, text, face, max_width, max_lines)
    ascent, descent = face.getmetrics()
    row_height = ascent + descent + spacing
    for part in result:
        draw.text((x + 2, y + 3), part, font=face, fill=(0, 0, 0, 110), stroke_width=0)
        draw.text((x, y), part, font=face, fill=(251, 249, 243, 255))
        y += row_height
    return y


def gradient_overlay(image):
    overlay = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    layer = ImageDraw.Draw(overlay)
    for y in range(SIZE[1]):
        top = round(132 * max(0, 1 - y / 370))
        bottom = round(215 * max(0, (y - 640) / 710))
        layer.line(((0, y), (SIZE[0], y)), fill=(9, 18, 20, max(top, bottom)))
    return Image.alpha_composite(image.convert("RGBA"), overlay)


def acquire_photo(item):
    url = item["image_url"]
    if urlsplit(url).scheme != "https" or urlsplit(url).hostname not in ALLOWED_HOSTS:
        raise ValueError("Image URL must use HTTPS from a supported photo host")
    if not item.get("source_page", "").startswith("https://"):
        raise ValueError("Missing inspectable original photo page")
    if item.get("license") not in ("Unsplash License", "Pexels License", "CC BY 4.0", "CC BY-SA 4.0"):
        raise ValueError("Unverified or unsupported image licence")
    if not item.get("photographer") or not item.get("alt") or not item.get("subject"):
        raise ValueError("Missing photographer, description, or independently labelled subject")
    response = SESSION.get(url, timeout=45, stream=True)
    response.raise_for_status()
    if not response.headers.get("Content-Type", "").startswith("image/"):
        raise ValueError("Photo URL did not return an image")
    blob = response.raw.read(22_000_001)
    if len(blob) > 22_000_000:
        raise ValueError("Photo file too large")
    original = ImageOps.exif_transpose(Image.open(io.BytesIO(blob)))
    original.load()
    if original.width < 1000 or original.height < 850:
        raise ValueError(f"Source image too small: {original.size} ({url})")
    return original.convert("RGB"), hashlib.sha256(blob).hexdigest()


def draw_slide(source, post, item, index, count):
    crop_y = min(1.0, max(0.0, float(item.get("focus_y", 0.5))))
    img = ImageOps.fit(source, SIZE, method=Image.Resampling.LANCZOS, centering=(0.5, crop_y))
    canvas = gradient_overlay(img)
    d = ImageDraw.Draw(canvas)
    cream = (252, 248, 235, 255)
    muted = (215, 218, 211, 255)
    d.text((72, 62), "YOUR TRAVEL ATLAS", font=font(30), fill=cream)
    d.line((72, 117, 1008, 117), fill=cream, width=2)
    d.text((72, 145), f"FIELD NOTES   /   ISSUE {post['issue']:03d}", font=font(23, REGULAR), fill=cream)
    d.text((905, 145), f"{index+1:02d}/{count:02d}", font=font(22), fill=cream)

    if index == 0:
        d.text((72, 810), post["category"].upper(), font=font(28), fill=muted)
        text_y = text_block(d, post["headline"].upper(), (68, 870), font(75, SERIF), 945, spacing=7, max_lines=3)
        if text_y > 1165:
            raise ValueError("Cover headline doesn't fit")
        d.text((72, text_y + 3), post["dek"], font=font(29, REGULAR), fill=cream)
    else:
        d.text((72, 990), item["kicker"].upper(), font=font(25), fill=muted)
        y = text_block(d, item["heading"].upper(), (68, 1040), font(62, SERIF), 935, spacing=6, max_lines=2)
        text_block(d, item["tip"], (72, y + 10), font(27, REGULAR), 915, spacing=5, max_lines=2)

    d.line((72, 1276, 1008, 1276), fill=(245, 242, 233, 170), width=2)
    d.text((72, 1293), "WANDER FURTHER   /   @YOURTRAVELATLAS", font=font(17), fill=cream)
    return canvas.convert("RGB")


def build(path):
    post = json.loads(path.read_text(encoding="utf-8"))
    required = ("issue", "slug", "headline", "dek", "category", "caption", "slides", "fact_sources")
    for key in required:
        if not post.get(key):
            raise ValueError(f"Missing {key} in {path}")
    if not isinstance(post["issue"], int) or not re.fullmatch(r"[0-9]{3}-[a-z0-9-]+", post["slug"]):
        raise ValueError("Invalid issue number or slug")
    if not 5 <= len(post["slides"]) <= 10:
        raise ValueError("Each carousel must contain 5–10 intentional slides")
    if len(post["fact_sources"]) < 2:
        raise ValueError("Fact-check provenance needs at least two credible source URLs")
    urls = [x["image_url"].split("?")[0] for x in post["slides"]]
    subjects = [x["subject"].strip().casefold() for x in post["slides"]]
    if len(set(urls)) != len(urls) or len(set(subjects)) != len(subjects):
        raise ValueError("Duplicate image or slide subject")
    out = OUTPUT / post["slug"]
    out.mkdir(parents=True, exist_ok=True)
    evidence = []
    print(f"Rendering {post['slug']}: {len(post['slides'])} slides", flush=True)
    hashes = set()
    for i, item in enumerate(post["slides"]):
        if i > 0 and not all(item.get(k) for k in ("kicker", "heading", "tip")):
            raise ValueError(f"Slide {i+1} has no purposeful on-image text")
        photo, sha = acquire_photo(item)
        if sha in hashes:
            raise ValueError("Source photo reused in carousel")
        hashes.add(sha)
        slide = draw_slide(photo, post, item, i, len(post["slides"]))
        filename = f"{i+1:02d}.jpg"
        slide.save(out / filename, "JPEG", quality=91, optimize=True, subsampling=0)
        evidence.append({k: item[k] for k in ("subject", "source_page", "photographer", "license", "alt")})
        evidence[-1].update({"file": filename, "source_sha256": sha, "size": list(SIZE)})
        print(f"  {filename} - {item['subject']}", flush=True)
    manifest = {
        "issue": post["issue"], "slug": post["slug"], "status": "rendered-not-published",
        "caption": post["caption"], "fact_sources": post["fact_sources"],
        "slides": evidence,
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main():
    files = sorted(INPUT.glob("*.json"))
    if len(sys.argv) > 1:
        files = [INPUT / f"{name}.json" for name in sys.argv[1:]]
    if not files:
        print("No post JSON found; no media generated.")
        return
    for path in files:
        build(path)


if __name__ == "__main__":
    main()
