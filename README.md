# Your Travel Atlas — Media Pipeline

**Editorial source of truth:** [Your Travel Atlas — Editorial Playbook (latest)](EDITORIAL_GUIDELINES.md). Read it before creating or changing issues.

A **£0-extra-cost** editorial image renderer for [@yourtravelatlas](https://www.instagram.com/yourtravelatlas/).

**GitHub Actions renders artwork. ChatGPT + Metricool handles editorial research and publishing.** This repository does **not** store Instagram credentials or publish directly.

## How it works

1. Research a travel story with a specific editorial purpose. Check every factual claim against primary tourism, park or transport sources. Choose **5–10** different, independently compelling photographs from verified, free-to-reuse licence pages. Never use Unsplash+ images. Maintain correct creator attribution and image-specific alternative text.
2. Add a JSON brief to `content/posts/NNN-topic.json`. Each slide declares its `image_url` (supported hosts: Unsplash, Pexels and Wikimedia), original `source_page`, `photographer`, `license`, `subject`, and on-slide copy. The issue number must be unique.
3. The free GitHub Actions [Render travel carousels](.github/workflows/render.yml) workflow automatically creates 1080×1350 JPEG slides, using Pillow and open-source system fonts, under `media/<slug>/`. It rejects too-small, missing or duplicate photos, missing attribution, unknown licensing, duplicate issue numbers, missing caption, missing source list and absent overlay copy.
4. **Inspect the actual rendered slides** before scheduling, including visual distinctiveness, accuracy, cropping, readability, absence of promotions, and source provenance. The renderer cannot prove that a declared licence is genuine; editorial research must establish that from the original source.
5. Schedule or update the existing draft with Metricool using publicly accessible URLs such as:
   `https://raw.githubusercontent.com/benbarraclough/yourtravelatlas-media/main/media/003-dolomites/01.jpg`
   Include all slide URLs, image alt text, caption and `autoPublish: true`, and use `draft: false` only after the finished carousel passes every check.

## Launch issues

- **001** Faroe Islands: five different places for an Atlantic exploration story.
- **002** Namibia: six distinct experiences from the desert to wildlife.
- **003** Dolomites: six photographs exploring contrasting mountain experiences.

Sources, photographer names and fact-check references are stored in each JSON brief; generated `manifest.json` files provide the image provenance and output list.

## Editorial standards

- Every post must be a genuine travel idea, not a photodump; vary formats and geography.
- Cover text includes the **Your Travel Atlas** masthead, a destination/trip hook and an issue identifier. Every subsequent slide has context-appropriate, legible on-image text.
- Images must be real, location-accurate, visually different, high resolution and appropriately licensed. The photo host and file existing do **not** validate the licence.
- Captions focus on memorable experiences and practical travel advice, not unhelpful trivia; they are checked, searchable and free of promotions.
- Do not reuse photos or issue numbers. Check existing published content as well as this repository for repeated editorial concepts.
- Avoid paid API services, paid add-ons and unapproved third-party promotions. The GitHub Actions workflow uses only standard public-repository runner minutes and free Python libraries.
- If anything fails, keep the associated Metricool entry as a **draft**. Never publish a faulty or incomplete image set.

## Automated task

The recurring ChatGPT task **Your Travel Atlas Publishing** should check the Metricool queue and this repository's content history, research and create next issue briefs via the GitHub connector, confirm that the Actions run succeeded, review the rendered media, then schedule eligible posts through the Metricool connector. If output has not yet rendered, leave the draft unpublished until verified in a later run.

This README and generated media are public. Do not add passwords, private data or credentials.

## Reels — original footage and original sound

Reels use a dedicated internal series, **independent** of numbered carousel issues, and **do not show a public sequence or clip counter**.

The zero-extra-cost Reel workflow:

1. Research a concrete, genuinely shareable trip idea, verify five or more distinct and actually moving free-licensed video clips against original Pexels pages, and check official source information for travel activities.
2. Create `content/reels/NNN-slug.json`; see [Lisbon Reel 001](content/reels/001-lisbon-weekend.json) for a working example. The file has `reel_number`, not a carousel `issue` number.
3. [GitHub Actions Reel renderer](.github/workflows/reels.yml) calls `scripts/render_reel.py`, producing 1080×1920 H.264 and playable AAC original synthesized ambient audio. Results: `media/reels/<slug>/reel.mp4`, `cover.jpg`, `storyboard.jpg` and `manifest.json`.
4. Visually inspect each frame and check media properties, exact footage/licensing, text contrast, correct location, original soundtrack and whether the sound actually suits the travel story. The render passing only confirms technical checks, not human-level quality.
5. Update the existing scheduled Reel (if revising), or fill one eligible future Reel slot with Metricool. Use real video-only public pinned-commit media URLs, a proper Reel cover and `instagramData.type=REEL`, `autoPublish=true`, `draft=false`. Read the queue again and check.
6. Start with about **one Reel per fortnight** (two per month). Reels **replace** an ordinary carousel slot. The conservative **16-publication per month** cap covers all formats, with zero paid services.

**First Reel:** *A Lisbon Weekend Without Rushing* — five actual Lisbon moving scenes, separate internal Reel no. 001, original instrumental ambience, and 16.3 seconds of video. Scheduled for Thursday 5 November 2026 at 09:00 Europe/London via existing Metricool UUID `5053010952195819165`. Publication is pending, not yet proven. Carousel Issue 004 is not used by this Reel.
