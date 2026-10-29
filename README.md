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

## Reels (licensed moving video)

The video workflow uses only no-cost GitHub Actions, FFmpeg and real free licensed footage:

1. Research an original, experience-led **video** concept; verify actual footage pages, licence, credited creators and traveller claims.
2. Create `content/reels/NNN-slug.json` using the Lisbon pilot `content/reels/004-lisbon-weekend.json` as a reference.
3. [Render licensed travel Reels](.github/workflows/reels.yml) automatically uses `scripts/render_reel.py` to create `media/reels/<slug>/reel.mp4`, a portrait `cover.jpg`, a complete `storyboard.jpg` of actual frames, and a detailed provenance manifest.
4. Inspect storyboard and verify H.264 MP4, 1080×1920 portrait, actual moving footage, readable overlay labels, editing quality and silent audio policy before scheduling.
5. Schedule through Metricool as Instagram `REEL` with the final public video URL, optional custom cover URL, `autoPublish: true`, `draft: false`, `showReelOnFeed: true`. Re-fetch planner and verify `PENDING` without claiming live publication.
6. A Reel takes an existing publication slot; **never exceed 16 total monthly posts** across all formats under our safety budget.

**Pilot:** Issue 004, *A Lisbon Weekend Without Rushing*, four distinct Pexels clips and an authentic 14-second 1080×1920 video, scheduled for Thursday 5 November 2026 at 09:00 Europe/London. Metricool planner UUID: `5053010952195819165`. This confirms the production and scheduling handoff; publication needs separate verification when due. Default audio is silence until a genuinely approved and suitably licensed soundtrack pipeline exists.
