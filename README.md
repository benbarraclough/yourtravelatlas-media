# Your Travel Atlas

An editor-led, image-led Instagram travel discovery project for [@yourtravelatlas](https://www.instagram.com/yourtravelatlas/). Content is researched, rendered and scheduled using GitHub and Metricool, with **no additional paid tools**.

> **One active operating policy:** [ATLAS_WEEKLY.md](ATLAS_WEEKLY.md). This is the first and only required publishing brief. Do not follow old multi-job instructions in the archives.

## Current workflow

- **Manual Tuesday production:** The owner prompts ChatGPT each Tuesday and may issue continuation prompts. No ChatGPT Atlas scheduled jobs run. In-session work checks Metricool, researches and verifies sources, creates/reviews finished assets via GitHub render workflows, and schedules finished content in Metricool. All seven legacy Atlas ChatGPT tasks are paused; do not create or re-enable.
- A rendered asset is not automatically QA-approved. A scheduled success requires live `PENDING`, `draft=false`, `autoPublish=true`.
- **Four posts per following week**, counting published/scheduled: **THREE manual swipe carousels** (4:5 separate portrait photographs, 8–10 slides including scenic "FILL YOUR FEED WITH WONDER." closing card), plus **ONE genuine moving-footage Reel** (9:16, ideally 7–10 licensed clips). If authentic motion isn't feasible, use a fourth carousel. **No zooming-still-photo MP4 Reels.**
- Accurate places and gripping hooks, strong licensed photographs, phone-legible covers, compact helpful captions and source/rights evidence. No music, public issue numbers, fabricated destinations, mandatory extra subscriptions, or routine owner approvals.
- Maximum **20 posts per calendar month** or any stricter Metricool limit; never duplicate or revive retired ideas. Successful GitHub rendering alone does not mean Instagram is scheduled.

## Where things live

| Path | Purpose |
| --- | --- |
| [ATLAS_WEEKLY.md](ATLAS_WEEKLY.md) | **Only live content and operations brief** |
| [CURRENT_STATE.json](CURRENT_STATE.json) | Dated planning snapshot; **Metricool is authoritative** |
| [content/production-queue.json](content/production-queue.json) | Minimal active commission ledger, not a historical to-do list |
| [content/posts/](content/posts/) | Live photo carousel briefs |
| [content/reels/](content/reels/) | Genuine moving-footage Reel briefs; older photo slideshow inputs are retired |
| [scripts/render.py](scripts/render.py) · [scripts/render_reel.py](scripts/render_reel.py) | Carousel and genuine-video Reel renderers; old still-photo slideshow capability is disabled |
| [.github/workflows/](.github/workflows/) | Rendering and source-audit helper workflows; **not** Instagram scheduling |
| [media/](media/) | Generated media, manifests and provenance; preserve links for already published/scheduled posts |
| [content/archive/](content/archive/) | Retired/replaced briefs that must not be rendered/scheduled |
| [docs/reference/](docs/reference/) | Historical benchmark and footage-source research (not production rules) |
| [docs/history/](docs/history/) | Superseded workflow documents and older records |
| [docs/reviews/ATLAS_TRIPLE_QA_2026-11-17.md](docs/reviews/ATLAS_TRIPLE_QA_2026-11-17.md) | Current seven-post visual/source/booking quality audit and complete change log |

## Final live position — 17 November 2026 after full triple QA

**Metricool brand 7717708 verified:** 7 November posts published + 7 PENDING = **14/20** used, 6 slots remain; seven upcoming media bookings preserve their original post UUID and dates, all `autoPublish=true`, `draft=false`.

- **18 Nov:** 8-slide mountain carousel, improved island-church Lake Bled photo.
- **20 Nov:** 9-slide winter carousel, clearer destination-specific caption.
- **22 Nov:** 9-slide Madeira carousel, corrected truncated headings, reordered caption.
- **23 Nov:** 8-slide Indonesia carousel, corrected elevated Padar viewpoint and photo credits.
- **25 Nov:** 8-slide desert-coast carousel, place-specific secondary angle captions and CC BY credit.
- **27 Nov:** 9-slide Vietnam carousel, upgraded Bản Giốc waterfall and Mã Pí Lèng gorge original photographs, stronger hook.
- **29 Nov:** true **eight-clip moving-footage** 25.1-second silent Cappadocia Reel with high-contrast hook and moving branded ending.

All six carousels have real 1080×1350 photographs, clear mobile text, and a source-reuse scenic `FILL YOUR FEED WITH WONDER.` final page. The video is real original licensed moving footage, never still-photo animation. Corrected renders were visually reviewed and existing Metricool bookings updated and re-fetched PENDING, with corresponding alt text and credits.

**Full annotated change log:** [Final seven-post QA](docs/reviews/ATLAS_TRIPLE_QA_2026-11-17.md). **Source of truth for actual post IDs and statuses:** [production queue](content/production-queue.json); Metricool live always overrides dated snapshots. **Original future content research:** [Travel formats & ideas](docs/reference/TRAVEL_CONTENT_IDEAS_2026-11-17.md).

All seven old Atlas ChatGPT scheduled tasks are paused. Permanent deletion requires the owner to use ChatGPT Tasks (not available via the connected task control); no replacements or autonomous ChatGPT work. **Next owner prompt: Tuesday 24 November** for 30 November–6 December, normally three distinct swipe carousels plus one genuine motion Reel (fourth carousel fallback). No paid tools required.
