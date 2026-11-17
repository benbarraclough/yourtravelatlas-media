# Your Travel Atlas — Editor-led Tuesday Publishing Brief

Updated **17 November 2026 after recovery and live Metricool recheck**. This is the **sole active operating/creative brief**. Source of truth for real bookings and monthly capacity: **live Metricool brand 7717708**; GitHub queue is a record of evidence and next actions, not proof of publishing.

## Operating mode: MANUAL ONLY

- The owner explicitly prompts ChatGPT **each Tuesday**, starting 17 November 2026, and can prompt **“continue”** as many times as needed. No unattended ChatGPT publishing, research, monitoring or notifications.
- **All seven legacy Atlas ChatGPT tasks are disabled**, including paused historical tasks. Do not create, enable or schedule replacements. The connected Automations interface has no permanent-delete method; the owner may remove them in ChatGPT's Scheduled task UI.
- One manual session can advance multiple steps and book multiple approved posts. Keep working while tools are available, prioritize closest finished work, and leave an exact handoff if a render/QA is genuinely unfinished. Never pretend a render, upload or publication succeeded without evidence.
- GitHub Actions remain the FREE renderer triggered by file commits. They are not separate editorial or publishing automations and do not send posts to Instagram.
- Keep production rights-cleared and use **£0 extra spend**. No new paid tools, credits or subscriptions.

## Frequency, formats and size

**Target exactly FOUR high-quality publications per publication week**, respecting already booked material:

1. **THREE manually swipeable Instagram carousel POSTS** (or FOUR if no strong genuinely filmed Reel can be made), each generally **8–10 complete slides including one final scenic branded slide**, normally 7–9 genuinely different licensed photographs. Publish as separate **1080×1350 (4:5) JPEGs**, `instagramData.type=POST`, NOT as a still-image MP4. The final image on **every carousel** must be a beautiful “FILL YOUR FEED WITH WONDER.” brand slide made with licensed original scenic photos; do not discard it as filler.
2. **ONE REAL moving-footage REEL**, **1080×1920 (9:16) silent MP4**, aim for **7–10 distinct genuine moving-footage shots**, every clip independently source- and rights-verified. Show clear actual experiences; use high-contrast bold opening title with specific number/experience hook, place label, mobile-safe text and short original moving-footage branded finale. Never output a Ken Burns zoom, slideshow, or video consisting of still photographs.
3. **Format fallback**: if no worthwhile real video can actually be produced and QA-reviewed, use a **fourth photo carousel POST**, never a photo slideshow Reel. Instagram/Metricool's normal publishable swipe carousel is a POST, even though Instagram may recommend it through Reels-adjacent surfaces; do not claim that a static swipe-carousel is an actual REEL.

The Metricool allowance is **20 total posts per calendar month**, including posted and future queued, or any stricter provider/account cap. Check actual live month before any booking. Do **not** exceed the agreed four/week merely to use all remaining allowance. The requested default is 3 carousels + 1 genuine video Reel each week, or 4 carousels as a fallback; older 2-carousel + 2-Reel recipes are superseded. Reasonably spaced **Mon/Wed/Fri/Sun at 19:00 UK** are established defaults, not a compulsory template. Timezone **Europe/London**. Book only `draft=false`, `autoPublish=true`, and verify a provider `PENDING` response and no duplicate date. Existing published or pending content always counts toward four.

## Creative standards

- Lead with a captivating **specific, truthful and visually enticing hook**: a surprising natural phenomenon, compelling activity, an unusual cross-country contrast, or extraordinary place with a tangible reason to save/share. Avoid repetitive “5 amazing places in [country]” formats.
- Mix *destination discovery*, curiosity-driven *thematic collections*, practical inspiring *experience-led* ideas, scenic culture, wildlife, beaches, cities, nature and sometimes adventures. Ideally **at least two unusually specific hooks** per week; do not post four near-identical geography lists.
- Photographs must be exceptional, relevant and distinctive across all scenes. If any scene is ordinary, misidentified or repetitive, improve or replace it before booking. Aim for seven to nine genuinely different photographs and a final branded slide (8–10 pages) per carousel; do not stop at five if better scenes are available, but do not pad with repetitive or weak images. For motion Reels aim for 7–10 authentic moving shots. Support the premise visually: a hook that promises six things needs six real things.
- Every **carousel cover** has a truthful small geographic kicker immediately ABOVE the title: country for one-country posts, **WORLDWIDE / EUROPE / SOUTH AMERICA** or another accurate region for cross-border work. Other slides have the named place and a concise, interesting experience—not a caption essay.
- **Never use lazy “more than just…” or generic “amazing places” hooks**; promise distinct attractive travel experiences with specifics, and show the promised footage. Research inspiring stories and post patterns from other travel pages, Atlas Obscura, Lonely Planet, Time Out, Condé Nast and reputable destination journalism; original editorial and licensed assets only. See `docs/reference/TRAVEL_CONTENT_IDEAS_2026-11-17.md` for concrete styles and research leads.
- **Reel covers** must be instantly legible in the grid, clear destination and compelling promise. Keep overlay text within mobile-safe areas and don't cover the important scenery. Brand text small and tasteful.
- No arbitrary issue numbers on public graphics, no “Wander Further”, no unrelated filler CTA photos, no generic motivational slogans beyond the required branded closing, excessive footage-availability lists, or childish decorative boxes/icons. **“FILL YOUR FEED WITH WONDER.” is the expressly required intentional scenic final image on all carousels.**
- Captions: short hook, useful **📍 named stops** with specific rewards, optional question/save nudge and compact correctly spelled photo/footage credits. **No lengthy caveats, unneeded multi-season explanations or travel advisories**; do not conceal a material restriction if omitting it would actively mislead.
- Do not fabricate superlatives, ranked top ten claims, locations, prices, timings or facts. If title includes a number, actually deliver that many experiences. “Best” is editorial, not a made-up official ranking.
- **No music, songs or audio on any new output**, including both types of Reels.

## Legitimate source rights and factual QA

- Obtain full-resolution **original licensed** photographs from Pexels, original free Unsplash (never Unsplash+), Pixabay where allowed, exact-image Wikimedia Commons (CC0 / public domain or correct attribution), individually verified original Flickr Creative Commons and approved public archives. For clips prioritize Pexels; supported Pexels, Wikimedia or other hosts must be verified against current renderer implementation.
- For **every individual image/clip**, record exact source page (not merely search result), author, licensing allowing commercial redistribution and transformation, source-image/CDN URL, exact pictured location and independent fact/activity evidence where relevant. A caption credit does **not** grant rights.
- Never rip other social creators’ media, assume tourism-board footage permits republishing, synthesize fake real locations, or use mislabeled/obviously AI-generated travel footage. Avoid low-resolution destructive crops, dubious releases or content depicting a place it does not show.
- For CC BY include licence URL, author, changes and attribution. Match the actual posted media to the public credits **after** every replacement. If factual travel advice (for example FCDO against-all-travel) makes aspirational discovery significantly misleading, reject the concept rather than paste a safety essay.
- Keep source evidence and finished output manifests in repo. Verify accessibility and originality. Review image appearance at phone size.

## GitHub render and Metricool scheduling loop

1. **RECONCILE** live Metricool month and next 14 days; count all published and scheduled posts, check latest reach/saves/shares where available, and read `content/production-queue.json`. No duplicates.
2. **RESEARCH + SELECT** strong premise and rights-verifiable high-impact original photos/video; use reputable sources for any factual caption claims; reject weak filler.
3. **BRIEF** into `content/posts/<slug>.json` for carousel or `content/reels/<slug>.json` for Reel; assign unique identifiers, correct size, exact source pages, captions and location notes. Active briefs only in those directories. Archive unused/rejected concepts in `content/archive/`.
4. **RENDER** by GitHub Actions on commit. For carousels: `scripts/render.py` → `media/<slug>/01.jpg...` including mandatory last `layout=brand_end`; for genuine moving-footage Reels only: `scripts/render_reel.py` → `media/reels/<slug>/reel.mp4`, aim 7–10 licensed moving shots. **The old `photo_slideshow_v1` renderer is retired and MUST NOT be used or scheduled, even if legacy files remain in source for reproducibility.**
5. **INSPECT THE ACTUAL FINISHED FILES**: every output JPEG/cover and storyboard, geographic and source correspondence, captions/credits, crops and legibility. For Reels independently check playback when accessible; FFmpeg `ffprobe` metadata, dimensions, duration, codec and **zero audio**. A GitHub commit alone is not content QA.
6. **BOOK** finished media on Metricool at vacant slot, correct `POST` vs `REEL`, timezone, public media files, caption and credits, autoPublish=true/draft=false. Re-fetch and assert provider `PENDING`; preserve UUID when revising any scheduled post (its numeric post ID changes). Never create a duplicate to replace a draft or correction.
7. **REPORT** actual bookings, UK times, monthly used/20, what was truly QA-checked, exact blockers and concise next handoff. Update queue/state, not a pile of recurring tasks.

## Historical live schedule snapshot — Tuesday 17 November 2026 (before owner-requested format revisions)

**November: 14/20 used: 7 PUBLISHED, 7 PENDING, 6 unfilled.** All future entries autoPublish true, draft false. Don't infer live status from this dated snapshot next Tuesday.

| UK publication time | Real Instagram format | Topic | Metricool id | Actual state |
| --- | --- | --- | --- | --- |
| Mon 16 Nov 19:00 | Carousel POST | Amalfi / Fiordo di Furore | 429111375 | PUBLISHED |
| Wed 18 Nov 19:00 | Carousel POST | 7 Mountain Views Without the Summit Hike | 427230845 | PENDING |
| Fri 20 Nov 19:00 | Photo slideshow REEL | 8 Places That Look Like a Winter Film | 427232781 | PENDING |
| Sun 22 Nov 19:00 | Photo slideshow REEL | Madeira: Cloud Trails / Lava Pools, updated media+credits | 431506131 | PENDING |
| Mon 23 Nov 19:00 | Carousel POST | Indonesia Beyond Bali / Flores & Komodo | 431514077 | PENDING |
| Wed 25 Nov 19:00 | Carousel POST | Five Places Where the Desert Meets the Sea | 431479145 | PENDING |
| Fri 27 Nov 19:00 | Photo slideshow REEL | Six Sides of Vietnam | 431495264 | PENDING |
| Sun 29 Nov 19:00 | **TRUE MOVING VIDEO REEL** | Cappadocia Beyond Balloons — revised five-clip motion Reel and correct credits | 431510824 | PENDING |

Both publication weeks meet the FOUR posts/week target. The Sunday 29 November Reel was produced from **five real Pexels moving clips**, 18.9 seconds silent, with revised fairy-chimney and horseback-riding shots and corrected contributor credit. Earlier Sunday 22 Madeira slideshow was revised **inside its existing Metricool slot** to the strengthened Porto Moniz volcanic pool and São Lourenço path footage-free photo sequence, correctly credited. All seven legacy ChatGPT Atlas tasks remain disabled; permanent deletion requires the owner to use ChatGPT Tasks.

**Indonesia correction resolved on 17 Nov:** Mon 23 Nov carousel's second slide now contains the newly rendered licensed Simon Spring Pink Beach aerial photograph. Correct image, all five actual JPEGs, caption credits and alt text were uploaded to the SAME UUID `8356741788287969` and re-fetched as `PENDING`/autoPublish=true/draft=false; new numeric id **431514077**. No outstanding source/caption mismatch.

**Archived next-cycle candidate:** `content/archive/south-america-landscapes-next-cycle-2026-11-24.json`; intentionally removed from live `content/posts/` because it conflicted with existing issue 014 and four posts/week were already complete. Before reusing it, reassign a truly unused issue ID and check every photo. Existing historic production and retired concepts in `docs/history/` and `content/archive/` are reference only, not mandatory tasks.

**Next owner prompt:** Tuesday **24 November 2026**. Recheck actual bookings/engagement and the November/December caps, reconcile Monday 23 publication and all pending statuses, then create four excellent original posts for **30 November – 6 December**. Do not create reminders or scheduled jobs.


## 17 November — mandatory manual editorial corrections underway
- Owner rejected ALL still-photo zooming slideshow Reels. Convert Nov 20 Winter, Nov 22 Madeira and Nov 27 Vietnam in their EXISTING Metricool UUIDs to true swipeable carousel POSTS with new JPEG renders and a branded last slide. No new duplicate scheduling slots.
- Current carousel revisions: Nov 18 mountain, Nov 23 Indonesia and Nov 25 desert should all receive scenic brand endings and stronger extra photos where sourced. Never mark completed before inspecting actual output and re-fetching post `PENDING`.
- Real Cappadocia Reel for Sun 29 has been replaced in its same UUID with **eight** real moving clips, strengthened **'5 Cappadocia Experiences Worth the Journey'** hook, bold dark-backed mobile-safe font, and filmed branded outro. Updated live Metricool id **431589392**, PENDING, autoPublish true, draft false. No music/audio.
- GitHub renders of the replacement carousels may be in progress; see `content/production-queue.json` for exact latest checkpoint. This section is a dated handoff; always fetch live Metricool.
