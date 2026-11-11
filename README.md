# Your Travel Atlas

An autonomous, image-led Instagram travel discovery project for [@yourtravelatlas](https://www.instagram.com/yourtravelatlas/). Content is researched, rendered and scheduled using GitHub and Metricool, with **no additional paid tools**.

> **One active operating policy:** [ATLAS_WEEKLY.md](ATLAS_WEEKLY.md). This is the first and only required publishing brief. Do not follow old multi-job instructions in the archives.

## Current workflow

- **One enabled Atlas Weekly Publisher task**, Thursday **08:00 Europe/London**, configured to read `ATLAS_WEEKLY.md`.
- Each run checks the **actual Metricool calendar first**, creates and reviews finished content, schedules via Metricool, then re-fetches to verify **PENDING**, `draft=false`, `autoPublish=true`.
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

## Current position (snapshot: 11 November 2026, morning UK)

Published in November: Porto, French Riviera, Iceland Reel and Japan. The older Faroe Islands carousel is also published.

The three posts confirmed auto-publishing **PENDING** during the morning check were New Zealand (11 Nov 12:00), Philippines (13 Nov 19:00) and Amalfi Coast (16 Nov 19:00). Status may change after this snapshot; **re-fetch Metricool before making decisions**.

The next Thursday run (12 November) should fill the **remaining three slots for 16–22 November**: **one strong curiosity-led carousel POST + one slideshow REEL + one genuine moving-footage REEL**, or a **second slideshow REEL** if genuine footage is not viable. Amalfi counts as the already booked destination discovery. The sole-job process has not yet proven a full end-to-end run.

**Retired and replaced:** Namibia, European wildlife, the original Istanbul Reel, and the original Amalfi photo-MP4. This does **not** prohibit creating new, purposeful photo-slideshow Reels under the current plan. Their briefs and old multi-job operating documents are archived to prevent accidental reuse. All prior material remains recoverable through Git history.

For publishing status and analytics, inspect the connected **Metricool brand 7717708**. Never store credentials in this public repository.
