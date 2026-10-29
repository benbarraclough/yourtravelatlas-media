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
ALLOWED_HOSTS = {"images.unsplash.com", "images.pexels.com", "upload.wikimedia.org", "thumb.wikimedia.org"}
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
    if item.get("license") not in ("Unsplash License", "Pexels License", "CC BY 2.0", "CC BY 4.0", "CC BY-SA 4.0", "CC0 1.0"):
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


def editorial_text(draw, message, xy, face, width, fill, max_lines=5, gap=8):
    """Measured editorial text; never shrink body text to squeeze in weak copy."""
    x, y = xy
    rows = lines_to_fit(draw, message, face, width, max_lines)
    a, b = face.getmetrics()
    for row in rows:
        draw.text((x, y), row, font=face, fill=fill)
        y += a + b + gap
    return y


def draw_editorial(source, post, item, index, count):
    cream, ink, accent = (248, 244, 233), (22, 43, 43), (149, 85, 53)
    layout = item.get("layout", "story")
    photo_height = 430 if layout == "itinerary" else 780
    focus = (float(item.get("focus_x", .5)), float(item.get("focus_y", .5)))
    if layout == "cta":
        canvas = gradient_overlay(ImageOps.fit(source, SIZE, centering=focus)).convert("RGB")
        d = ImageDraw.Draw(canvas)
        d.text((72, 62), "YOUR TRAVEL ATLAS", font=font(30), fill=cream)
        d.line((72, 117, 1008, 117), fill=cream, width=2)
        d.text((72, 145), f"ISSUE {post['issue']:03d}  /  {index+1:02d}/{count:02d}", font=font(22, REGULAR), fill=cream)
        d.text((72, 825), "KEEP YOUR CURIOSITY CLOSE", font=font(24), fill=cream)
        y = editorial_text(d, "FILL YOUR FEED WITH WONDER.", (68, 885), font(78, SERIF), 936, cream, 3)
        y = editorial_text(d, "Follow @yourtravelatlas for beautiful places and the details that turn them into real plans.", (72, y + 25), font(30, REGULAR), 920, cream, 3)
        if y > 1252:
            raise ValueError("Closing-card text overlaps footer")
    else:
        canvas = Image.new("RGB", SIZE, cream)
        pic = ImageOps.fit(source, (1080, photo_height), method=Image.Resampling.LANCZOS, centering=focus)
        canvas.paste(pic, (0, 0))
        shade = Image.new("RGBA", SIZE, (0, 0, 0, 0))
        sd = ImageDraw.Draw(shade)
        for y in range(260):
            sd.line((0, y, 1080, y), fill=(8, 24, 24, round(145 * (1-y/260))))
        canvas = Image.alpha_composite(canvas.convert("RGBA"), shade).convert("RGB")
        d = ImageDraw.Draw(canvas)
        d.text((72, 62), "YOUR TRAVEL ATLAS", font=font(30), fill=cream)
        d.line((72, 117, 1008, 117), fill=cream, width=2)
        d.text((72, 145), f"ISSUE {post['issue']:03d}", font=font(22, REGULAR), fill=cream)
        d.text((905, 145), f"{index+1:02d}/{count:02d}", font=font(22), fill=cream)
        if item.get("date_label"):
            label = item["date_label"].upper()
            f = font(26)
            w = d.textbbox((0, 0), label, font=f)[2]
            if w > 904:
                raise ValueError("Event date label is too long")
            d.rectangle((72, 210, 104+w, 264), fill=cream)
            d.text((88, 219), label, font=f, fill=ink)
        if item.get("photo_note"):
            note = item["photo_note"]
            nf = font(19, REGULAR)
            if d.textbbox((0,0), note, font=nf)[2] > 936:
                raise ValueError("Historical/context photo note is too long")
            d.rectangle((0, photo_height-49, 1080, photo_height), fill=ink)
            d.text((72, photo_height-36), note, font=nf, fill=cream)
        y = photo_height + 24
        d.text((72, y), item["kicker"].upper(), font=font(23), fill=accent)
        y += 42
        title = item["heading"].upper()
        for size in (54, 50, 46, 42):
            face = font(size, SERIF)
            if d.textbbox((0, 0), title, font=face)[2] <= 936:
                break
        else:
            raise ValueError("Editorial heading must fit on one readable line")
        y = editorial_text(d, title, (68, y), face, 936, ink, 1) + 15
        if layout == "itinerary":
            for stop in item["stops"]:
                d.line((72, y, 1008, y), fill=(196, 191, 177), width=1)
                y += 18
                y = editorial_text(d, stop["label"].upper(), (72, y), font(23), 936, accent, 1) + 7
                y = editorial_text(d, stop["text"], (72, y), font(29, REGULAR), 936, ink, 3) + 19
        else:
            y = editorial_text(d, item["body"], (72, y), font(30, REGULAR), 936, ink, 5)
        if item.get("detail"):
            y += 17
            y = editorial_text(d, item["detail"], (72, y), font(24), 936, accent, 2, 5)
        limit = 1225 if item.get("credit_line") else 1250
        if y > limit:
            raise ValueError(f"Editorial slide {index+1} overlaps credit/footer: {y} > {limit}")
        if item.get("credit_line"):
            editorial_text(d, item["credit_line"], (72, 1238), font(17, REGULAR), 936, ink, 1)
    d.line((72, 1276, 1008, 1276), fill=cream if layout == "cta" else ink, width=2)
    d.text((72, 1293), "WANDER FURTHER   /   @YOURTRAVELATLAS", font=font(17), fill=cream if layout == "cta" else ink)
    return canvas


def visible_words(item):
    """Count all editorial overlay words, excluding discreet brand/issue marks."""
    return " ".join(str(item.get(k, "")) for k in
                    ("heading", "body", "date_label", "photo_note", "detail", "kicker")).split()


def draw_discovery(source, post, item, index, count):
    """Photo-first v6: one promise; concise specific copy; no brochure panels."""
    cream = (252, 249, 241)
    focus = tuple(float(item.get(k, .5)) for k in ("focus_x", "focus_y"))
    canvas = ImageOps.fit(source, SIZE, method=Image.Resampling.LANCZOS, centering=focus).convert("RGBA")
    overlay = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    shade = ImageDraw.Draw(overlay)
    for y in range(1350):
        top = round(65 * max(0, 1-y/180))
        bottom = round(225 * max(0, min(1, (y-730)/590)))
        shade.line((0,y,1080,y), fill=(8,17,20,max(top,bottom)))
    canvas = Image.alpha_composite(canvas, overlay).convert("RGB")
    d = ImageDraw.Draw(canvas)
    if index == 0:
        title = post["headline"]
        face = font(86, SERIF)
        rows = lines_to_fit(d,title,face,936,3)
        a,b = face.getmetrics(); h=a+b+5
        y=1198-len(rows)*h
        if y < 800: raise ValueError("Cover hook obscures too much of the photograph")
        editorial_text(d,title,(72,y),face,936,cream,3,5)
    elif item.get("layout") == "cta":
        y=editorial_text(d,"Fill your feed with wonder.",(72,885),font(74,SERIF),936,cream,2,5)
        y=editorial_text(d,"Follow @yourtravelatlas for beautiful places and the details that turn them into real plans.",(72,y+24),font(30,REGULAR),900,cream,3,6)
        if y > 1234: raise ValueError("Closing-card text overlaps brand mark")
    else:
        if len(visible_words(item)) > 30:
            raise ValueError("Supporting slides have an absolute 30-word overlay maximum")
        bodyface=font(34,REGULAR); titleface=font(56,SERIF)
        rows=lines_to_fit(d,item["body"],bodyface,936,4)
        titles=lines_to_fit(d,item["heading"],titleface,936,2)
        a,b=bodyface.getmetrics(); ta,tb=titleface.getmetrics()
        note=" · ".join(item.get(k,"") for k in ("date_label","photo_note") if item.get(k))
        block=len(rows)*(a+b+7)+len(titles)*(ta+tb+5)+17+(38 if note else 0)
        y=1210-block
        if y < 830: raise ValueError("Supporting copy obscures too much of the photograph")
        if note:
            y=editorial_text(d,note,(72,y),font(20),936,cream,1,4)+10
        y=editorial_text(d,item["heading"],(72,y),titleface,936,cream,2,5)+17
        y=editorial_text(d,item["body"],(72,y),bodyface,936,cream,4,7)
        if y > 1220: raise ValueError("Discovery copy overlaps brand mark")
    d.text((72,1270),"@yourtravelatlas",font=font(20,REGULAR),fill=cream)
    issue=f"ISSUE {post['issue']:03d}"
    width=d.textbbox((0,0),issue,font=font(17,REGULAR))[2]
    d.text((1008-width,1273),issue,font=font(17,REGULAR),fill=cream)
    if item.get("credit_line"):
        editorial_text(d,item["credit_line"],(72,1305),font(16,REGULAR),936,cream,1)
    return canvas


def validate_editorial(post):
    if post.get("editorial_version", 0) < 6:
        if post.get("issue") == 1:
            return  # Preserve the already published, frozen launch issue.
        raise ValueError("New/unpublished carousels require editorial_version >= 6")
    if not post.get("format") or not post.get("slide_count_rationale"):
        raise ValueError("Missing format-specific treatment or slide-count decision")
    if not 5 <= len(post["slides"]) <= 10:
        raise ValueError("New carousels need 5–10 intentional pages including a closing card")
    if len(post["caption"]) > 2200:
        raise ValueError("Instagram caption exceeds 2200 characters")
    if post["slides"][-1].get("layout") != "cta" or sum(s.get("layout") == "cta" for s in post["slides"]) != 1:
        raise ValueError("Exactly one standard closing card must finish the carousel")
    for i, slide in enumerate(post["slides"]):
        if 0 < i < len(post["slides"])-1 and len(visible_words(slide)) > 30:
            raise ValueError("Supporting slides have an absolute 30-word overlay maximum")
        for field in ("reader_value", "image_context", "specific_detail", "distinct_contribution"):
            if len(slide.get("review", {}).get(field, "").strip()) < 35:
                raise ValueError(f"Slide {i+1} lacks substantive {field} review")
        refs = slide.get("fact_checks", [])
        if not refs or any(ref not in post["fact_sources"] for ref in refs):
            raise ValueError(f"Slide {i+1} has no valid claim-source ledger")
        if 0 < i < len(post["slides"])-1 and slide.get("layout") != "itinerary" and not slide.get("body"):
            raise ValueError("Supporting slides require valuable on-image detail")
        if slide.get("event_status") and (not slide.get("event_status") or not slide.get("date_label")):
            raise ValueError("Events require dates and confirmed/recurring status")
        if slide["license"].startswith("CC ") and not all(slide.get(k) for k in ("license_url", "credit_line", "changes")):
            raise ValueError("Creative Commons images require attribution, licence and changes")


def draw_slide(source, post, item, index, count):
    if post.get("editorial_version", 0) >= 6:
        return draw_discovery(source, post, item, index, count)
    if post.get("editorial_version", 0) >= 5 and index > 0:
        return draw_editorial(source, post, item, index, count)
    crop_y = min(1.0, max(0.0, float(item.get("focus_y", 0.5))))
    img = ImageOps.fit(source, SIZE, method=Image.Resampling.LANCZOS, centering=(0.5, crop_y))
    canvas = gradient_overlay(img)
    d = ImageDraw.Draw(canvas)
    cream = (252, 248, 235, 255)
    muted = (215, 218, 211, 255)
    d.text((72, 62), "YOUR TRAVEL ATLAS", font=font(30), fill=cream)
    d.line((72, 117, 1008, 117), fill=cream, width=2)
    d.text((72, 145), f"ISSUE {post['issue']:03d}", font=font(23, REGULAR), fill=cream)
    d.text((905, 145), f"{index+1:02d}/{count:02d}", font=font(22), fill=cream)

    if index == 0:
        # Hero hierarchy: small location, BIG inspirational promise, small supporting line.
        # Anchor the bottom of the hook to the same visual baseline for short and long titles.
        headline = post["headline"].upper()
        for size in (78, 74, 70, 66, 62, 58):
            face = font(size, SERIF)
            try:
                title_lines = lines_to_fit(d, headline, face, 945, max_lines=3)
                break
            except ValueError:
                continue
        else:
            raise ValueError(f"Cover headline too long for a beautiful layout: {headline}")
        ascent, descent = face.getmetrics()
        line_height = ascent + descent + 8
        title_y = 1172 - (len(title_lines) * line_height)
        # Location must be immediately legible in the mobile feed: an explicit
        # large destination line above a smaller trip-type / regional label.
        category_y = title_y - 110
        if category_y < 685:
            raise ValueError("Cover typography collides with the hero image")
        location, _, genre = post["category"].partition("/")
        location = location.strip().upper()
        genre = genre.strip().upper()
        location_face = None
        for dest_size in (46, 43, 40, 37, 34, 31):
            candidate = font(dest_size)
            if d.textbbox((0, 0), location, font=candidate)[2] <= 935:
                location_face = candidate
                break
        if location_face is None:
            raise ValueError(f"Destination label is too long: {location}")
        d.text((72, category_y), location, font=location_face, fill=cream)
        if genre:
            if d.textbbox((0, 0), genre, font=font(25, REGULAR))[2] > 935:
                raise ValueError(f"Trip-type label is too long: {genre}")
            d.text((72, category_y + 54), genre, font=font(25, REGULAR), fill=muted)
        title_end = text_block(d, headline, (68, title_y), face, 945, spacing=8, max_lines=3)
        if title_end > 1173:
            raise ValueError("Cover headline exceeds its allocated space")
        dek = lines_to_fit(d, post["dek"], font(27, REGULAR), 935, max_lines=2)
        if len(dek) > 1:
            raise ValueError("Cover supporting line should be concise and one line")
        d.text((72, 1189), dek[0], font=font(27, REGULAR), fill=cream)
    else:
        d.text((72, 990), item["kicker"].upper(), font=font(25), fill=muted)
        y = text_block(d, item["heading"].upper(), (68, 1040), font(62, SERIF), 935, spacing=6, max_lines=2)
        text_block(d, item["tip"], (72, y + 10), font(34, REGULAR), 915, spacing=8, max_lines=2)

    d.line((72, 1276, 1008, 1276), fill=(245, 242, 233, 170), width=2)
    d.text((72, 1293), "WANDER FURTHER   /   @YOURTRAVELATLAS", font=font(17), fill=cream)
    return canvas.convert("RGB")


def build(path):
    post = json.loads(path.read_text(encoding="utf-8"))
    validate_editorial(post)
    required = ("issue", "slug", "headline", "dek", "category", "caption", "slides", "fact_sources", "editorial_intent", "share_reason")
    for key in required:
        if not post.get(key):
            raise ValueError(f"Missing {key} in {path}")
    if not isinstance(post["issue"], int) or not re.fullmatch(r"[0-9]{3}-[a-z0-9-]+", post["slug"]):
        raise ValueError("Invalid issue number or slug")
    if not 5 <= len(post["slides"]) <= 10:
        raise ValueError("Each carousel must contain 5–10 intentional slides")
    if len(post["fact_sources"]) < 2:
        raise ValueError("Fact-check provenance needs at least two credible source URLs")
    if len(post["editorial_intent"].strip()) < 45 or len(post["share_reason"].strip()) < 45:
        raise ValueError("An issue needs a specific editorial intent and reason friends would share it")
    if any(not url.startswith("https://") for url in post["fact_sources"]):
        raise ValueError("Fact sources must have inspectable HTTPS URLs")
    urls = [x["image_url"].split("?")[0] for x in post["slides"]]
    subjects = [x["subject"].strip().casefold() for x in post["slides"]]
    if len(set(urls)) != len(urls) or len(set(subjects)) != len(subjects):
        raise ValueError("Duplicate image or slide subject")
    out = OUTPUT / post["slug"]
    out.mkdir(parents=True, exist_ok=True)
    # A shorter remake must not leave obsolete numbered pages in its output folder.
    for stale in out.glob("[0-9][0-9].jpg"):
        if int(stale.stem) > len(post["slides"]):
            stale.unlink()
    evidence = []
    print(f"Rendering {post['slug']}: {len(post['slides'])} slides", flush=True)
    hashes = set()
    for i, item in enumerate(post["slides"]):
        if i > 0 and post.get("editorial_version", 0) < 5 and not all(item.get(k) for k in ("kicker", "heading", "tip")):
            raise ValueError(f"Slide {i+1} has no purposeful on-image text")
        if not item.get("activity_source", "").startswith("https://") or item["activity_source"] not in post["fact_sources"]:
            raise ValueError(f"Slide {i+1} lacks a traceable, verified activity source")
        # Supporting-slide space is for the experience, not logistics/safety notices.
        if i > 0 and re.search(
            r"\b(check (?:local|current|seasonal|paid|trail|access|road|rules)|keep your distance|keep back|stay in your vehicle|access restrictions?|permits?|safety warnings?)\b",
            item.get("tip", ""), flags=re.IGNORECASE,
        ):
            raise ValueError(f"Slide {i+1}: move safety or access warnings to caption: {item['tip']}")
        photo, sha = acquire_photo(item)
        if sha in hashes:
            raise ValueError("Source photo reused in carousel")
        hashes.add(sha)
        slide = draw_slide(photo, post, item, i, len(post["slides"]))
        filename = f"{i+1:02d}.jpg"
        slide.save(out / filename, "JPEG", quality=91, optimize=True, subsampling=0)
        evidence.append({k: item[k] for k in ("subject", "source_page", "photographer", "license", "alt", "activity_source")})
        evidence[-1].update({"file": filename, "source_sha256": sha, "size": list(SIZE)})
        for key in ("layout", "body", "detail", "date_label", "event_status", "photo_note", "license_url", "credit_line", "changes", "review", "fact_checks"):
            if key in item:
                evidence[-1][key] = item[key]
        print(f"  {filename} - {item['subject']}", flush=True)
    manifest = {
        "issue": post["issue"], "slug": post["slug"], "status": "rendered-not-published",
        "caption": post["caption"], "fact_sources": post["fact_sources"],
        "editorial_intent": post["editorial_intent"], "share_reason": post["share_reason"],
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
    # Prevent reusing photographs between issues, not only inside one carousel.
    all_paths = sorted(INPUT.glob("*.json"))
    used_images = {}
    used_issues = {}
    for path in all_paths:
        post = json.loads(path.read_text(encoding="utf-8"))
        number = post.get("issue")
        if number in used_issues:
            raise ValueError(f"Issue {number} duplicated by {path} and {used_issues[number]}")
        used_issues[number] = path
        for slide in post.get("slides", []):
            src = slide.get("image_url", "").split("?")[0]
            if src in used_images:
                raise ValueError(f"Photo reused between issues: {path} and {used_images[src]}")
            used_images[src] = path
    for path in files:
        build(path)


if __name__ == "__main__":
    main()
