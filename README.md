# Your Travel Atlas

An editor-led, image-led Instagram travel discovery project for [@yourtravelatlas](https://www.instagram.com/yourtravelatlas/). Content is researched, rendered and scheduled using GitHub and Metricool, with **no additional paid tools**.

> **One active operating policy:** [ATLAS_WEEKLY.md](ATLAS_WEEKLY.md). This is the first and only required publishing brief. Do not follow old multi-job instructions in the archives.

## Current workflow

- **Manual Tuesday production:** The owner prompts ChatGPT each Tuesday and may issue continuation prompts. No ChatGPT Atlas scheduled jobs run. In-session work checks Metricool, researches and verifies sources, creates/reviews finished assets via GitHub render workflows, and schedules finished content in Metricool. All seven legacy Atlas ChatGPT tasks are paused; do not create or re-enable.
- A rendered asset is not automatically QA-approved. A scheduled success requires live `PENDING`, `draft=false`, `autoPublish=true`.
- **Four posts per following week in total, including posts already booked:** **2 swipeable carousel POSTS (4:5, 1080×1350 JPGs), 1 still-photo slideshow REEL (9:16, 1080×1920 MP4), and 1 genuine moving-footage REEL (9:16, 1080×1920 MP4)**. If suitable real video footage cannot be sourced and rendered, publish **another slideshow REEL** in its place. Slideshow Reels autoplay; carousels are manually swipeable, never interchange them.
- Accurate places and gripping hooks, strong licensed photographs, phone-legible covers, compact helpful captions and source/rights evidence. No music, public issue numbers, fabricated destinations, mandatory extra subscriptions, or routine owner approvals.
- Maximum **20 posts per calendar month** or any stricter Metricool limit; never duplicate or revive retired ideas. Successful GitHub rendering alone does not mean Instagram is scheduled.

## Where things live

| Path | Purpose |
| --- | --- |
| [ATLAS_WEEKLY.md](ATLAS_WEEKLY.md) | **Only live content and operations brief** |
| [CURRENT_STATE.json](CURRENT_STATE.json) | Dated planning snapshot; **Metricool is authoritative** |
| [content/production-queue.json](content/production-queue.json) | Minimal active commission ledger, not a historical to-do list |
| [content/posts/](content/posts/) | Live photo carousel briefs |
| [content/reels/](content/reels/) | Live still-photo slideshow and genuine moving-footage Reel briefs |
| [scripts/render.py](scripts/render.py) · [scripts/render_reel.py](scripts/render_reel.py) · [scripts/render_photo_reel.py](scripts/render_photo_reel.py) | Carousel, true-video Reel and slideshow Reel renderers |
| [.github/workflows/](.github/workflows/) | Rendering and source-audit helper workflows; **not** Instagram scheduling |
| [media/](media/) | Generated media, manifests and provenance; preserve links for already published/scheduled posts |
| [content/archive/](content/archive/) | Retired/replaced briefs that must not be rendered/scheduled |
| [docs/reference/](docs/reference/) | Historical benchmark and footage-source research (not production rules) |
| [docs/history/](docs/history/) | Superseded workflow documents, audits and older records |

## Current verified position (Tuesday 17 November 2026, after manual session)

Metricool shows **7 November posts PUBLISHED + 7 PENDING = 14/20 allowance used; 6 slots remain**. Weeks 16–22 and 23–29 November each have exactly four bookings. The new Sunday 29 November post is a **genuine five-clip Pexels moving-video Reel** about Cappadocia, not a photo slideshow. The 22 November Madeira slideshow was revised with stronger image sources and credits in its existing Metricool slot. All future bookings have `autoPublish=true`, `draft=false`.

All seven Atlas ChatGPT automations are **paused**. There is no delete action in the available Automations connector; the user can permanently delete them in ChatGPT **Scheduled**. Do not create replacements. Owner prompts each **Tuesday**, next on **24 Nov**, to produce the following four-post week. A candidate South America carousel is parked in `content/archive/` for future approval only, not booked. The 23 Nov Indonesia carousel was improved again: a stronger Simon Spring original Pink Beach aerial photograph replaced the earlier image within the SAME Metricool booking, new id 431514077; live caption credits and alt text were reconciled and verified PENDING.

Follow [ATLAS_WEEKLY.md](ATLAS_WEEKLY.md) and [content/production-queue.json](content/production-queue.json) for live operating policy/next actions, but **Metricool brand 7717708** is authoritative for real posting. Never put credentials in this public repository.
