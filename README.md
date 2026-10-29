# Your Travel Atlas — Media Pipeline

**Editorial source of truth:** [Your Travel Atlas — Editorial Playbook (latest)](EDITORIAL_GUIDELINES.md). Read it before creating or changing issues.

**Mandatory production procedure:** [Editorial creation and review](EDITORIAL_REVIEW.md), with [competitive reference evidence](EDITORIAL_BENCHMARKS.md). New carousels require editorial_version 6: image-led clear hooks, discreet @yourtravelatlas/issue branding, no WANDER FURTHER, supporting overlays at most 30 words, caption location pins and relevant critical details. Varied intentions and 5–10 intentional pages; no compulsory itinerary panels. Per-slide source/value reviews and actual image inspection remain required. Porto/Riviera v6 remakes were owner-approved and scheduled on 29 October 2026; their temporary review hold is released. Future editions use the calibrated internal review. Published issue001 and the approved Istanbul Reel stay unchanged. Run both renderer test suites before production changes.

A **£0-extra-cost** editorial image renderer for [@yourtravelatlas](https://www.instagram.com/yourtravelatlas/).

**GitHub Actions renders artwork. ChatGPT + Metricool handles editorial research and publishing.** This repository does **not** store Instagram credentials or publish directly.

## How it works

1. Research a travel story with a specific editorial purpose. Check every factual claim against primary tourism, park or transport sources. Choose **5–10** different, independently compelling photographs from verified, free-to-reuse licence pages. Never use Unsplash+ images. Maintain correct creator attribution and image-specific alternative text.
2. Add a JSON brief to `content/posts/NNN-topic.json`. Each slide declares its `image_url` (supported hosts: Unsplash, Pexels and Wikimedia), original `source_page`, `photographer`, `license`, `subject`, and on-slide copy. The issue number must be unique.
3. The free GitHub Actions [Render travel carousels](.github/workflows/render.yml) workflow automatically creates 1080×1350 JPEG slides, using Pillow and open-source system fonts, under `media/<slug>/`. It rejects too-small, missing or duplicate photos, missing attribution, unknown licensing, duplicate issue numbers, missing caption, missing source list and absent overlay copy.
4. **Inspect the actual rendered slides** before scheduling, including visual distinctiveness, accuracy, cropping, readability, absence of promotions, and source provenance. The renderer cannot prove that a declared licence is genuine; editorial research must establish that from the original source.
5. Schedule or update the existing draft with Metricool using publicly accessible URLs such as:
   `https://raw.githubusercontent.com/benbarraclough/yourtravelatlas-media/<reviewed-commit>/media/002-porto-slow-weekend/01.jpg`
   Include all slide URLs, image alt text, caption and `autoPublish: true`, and use `draft: false` only after the finished carousel passes every check.

## Launch issues

- **001** Faroe Islands: five different places for an Atlantic exploration story.
- **002** Porto: a slow city weekend with Ribeira, São Bento, Gaia and Foz. Six-slide v6 remake; owner-approved and scheduled 2 November 2026 at 19:00 Europe/London.
- **003** French Riviera by train: one Nice base with separate coastal outings. Seven-slide v6 remake; owner-approved and scheduled 4 November 2026 at 12:00 Europe/London.

Sources, photographer names and fact-check references are stored in each JSON brief; generated `manifest.json` files provide the image provenance and output list.

## Editorial standards

- Every post must be a genuine travel idea, not a photodump; vary formats and geography.
- Cover text is one clear hook plus discreet @yourtravelatlas and issue. Supporting slides contain concise, specific descriptions with an absolute 30-word total overlay maximum. No WANDER FURTHER or large masthead.
- Images must be real, location-accurate, visually different, high resolution and appropriately licensed. The photo host and file existing do **not** validate the licence.
- Captions focus on memorable experiences and practical travel advice, not unhelpful trivia; they are checked, searchable and free of promotions.
- Do not reuse photos or issue numbers. Check existing published content as well as this repository for repeated editorial concepts.
- Avoid paid API services, paid add-ons and unapproved third-party promotions. The GitHub Actions workflow uses only standard public-repository runner minutes and free Python libraries.
- If anything fails, keep the associated Metricool entry as a **draft**. Never publish a faulty or incomplete image set.

## Automated task

The recurring ChatGPT task **Your Travel Atlas Publishing** should check the Metricool queue and this repository's content history, research and create eligible next issue briefs via the GitHub connector, confirm that the Actions run succeeded, review the rendered media, then schedule eligible posts through the Metricool connector. If output has not yet rendered, leave the draft unpublished until verified in a later run.

This README and generated media are public. Do not add passwords, private data or credentials.

## Reels — editorial quality before production

Read [Footage sources and feasibility checks](FOOTAGE_SOURCES.md) before every new Reel. The 29 October audit tested sample downloads from Pixabay, Coverr and Mixkit and identified additional specialist archives; it did not approve whole catalogues or expand the production downloader. Only build a Reel when enough coherent, properly licensed, visually strong real footage survives portrait/motion/audio review.

Reels are independent from numbered carousels and initially replace a carousel slot approximately once a fortnight, within the 16-publication internal monthly budget.

The existing no-cost production path uses `content/reels/NNN-slug.json`, `scripts/render_reel.py` and `.github/workflows/reels.yml` to render actual 1080 × 1920 moving footage into `media/reels/<slug>/reel.mp4`, cover, storyboard and source manifest. It can create an original upbeat soundtrack without using copyrighted music or paid APIs. It now **skips any brief containing `"editorial_status": "rejected"`**.

The first two tests — **Lisbon Reel 001** and **Cinque Terre by Train Reel 002** — were creatively rejected despite successful technical renders. Lisbon is preserved in Metricool as a **draft with automatic publishing disabled** (UUID `5053010952195819165`); Cinque Terre was never scheduled. Neither should be published without a new concept, new source footage and renewed visual/audio review.

**Mandatory Reel quality gate:** Find the travel story first; do not list locations merely because clips exist. Five or more distinct, high-quality, authentic, fully licensed moving shots must independently inspire a real trip friends would want to share. Prominent destination and small masthead at top; inspiring short serif description lower down; **no "Wander Further" line, issue number or clip counter on Reels**. Sound should be bright, positive and fitting, never dreary. For a professionally recorded song, verify exact source, track licence, professional Instagram use and no paid requirement before adding it. Review actual rendered frames, cropping and the sound before a Reel is scheduled.

After editorial approval, schedule as `instagramData.type=REEL`, with verified full MP4, optional thumbnail, `autoPublish=true`, `draft=false`, and confirm via Metricool. It is preferable to leave a slot empty than publish an uninspiring Reel.


## Music licensing test result (29 October 2026)

Mixkit's free music licence allows Instagram video posts, but a direct automated download for "Just Keep Walking" by Michael Ramir C. was **blocked with HTTP 403**. No track has been approved for unattended downloading or added to a scheduled Reel. The Lisbon and Cinque Terre Reel pilots remain **rejected**; Lisbon is an unpublished Metricool draft and must not be revived just because a new soundtrack is found.

Before the next Reel: select a professionally recorded, joyful, genuinely suitable track; independently verify its licence and actual automated delivery; assess the complete footage, sound and narrative; publish only if the finished result inspires a trip. Never force a Reel into the schedule. Regular carousels are unaffected.

## Current queue correction — 29 October 2026

The owner-requested Porto and Riviera replacements use the existing issue 002/003 Metricool slots. Old Namibia/Dolomites media are retained only as historical outputs and must never be rescheduled automatically. Current brief filenames match their new destinations. The approved Istanbul Reel remains scheduled for 5 November at 09:00 Europe/London; older pilot/audio notes above are historical and the latest Editorial Playbook decision takes precedence.
