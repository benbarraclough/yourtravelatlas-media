# Your Travel Atlas

Current policy v8 ·30 October2026. @yourtravelatlas uses existing GitHub and Metricool connections at £0 additional cost.

Read in order: [current state](CURRENT_STATE.json), [outstanding work](OUTSTANDING_WORK.md), [creation flows](CONTENT_PROCESS.md), [guidelines](EDITORIAL_GUIDELINES.md), [approval gates](EDITORIAL_REVIEW.md). [Audit](PROJECT_AUDIT.md) maps project decisions to implementation and weekly ownership. Current policy supersedes historical snapshots.

Three formats coexist: formal Faroe-style Travel Discovery Collection guides, hook-led Discovery carousels, and informative authentic-video Reels. No public issue numbers on any format. No music on any content. Keep internal IDs, small handle, clear hooks, concise useful overlays and rich specific captions. Destination guides need meaningful essential-place imagery, not caption-only expansion.

## Live status verified30 October

- Porto and Riviera: held as drafts, auto-publishing off, pending visual revisions and owner preview.
- Iceland: silent23-second five-shot Reel replaces Istanbul at5 November09:00 UK.
- Japan: successful six-image content retained; public numbers removed;9 November19:00 UK.
- Faroe: published design reference, frozen.
-28 obsolete files removed; source evidence and recovery history retained.

Always re-fetch Metricool; this is a dated snapshot. Updates change post IDs; UUIDs remain stable.

## Automation

One enabled ChatGPT task found: Your Travel Atlas Publishing, Thursday15:00 Europe/London, ID6ae251260af881919e1d2042f46e1ff2. Its service timing mode is flexible_schedule, so15:00 is configured timing rather than a minute-exact guarantee. No second ChatGPT task was found.

The repository has three GitHub helper workflows: render.yml, reels.yml and photo-audit.yml. They run on matching pushes/manual dispatch, with no cron schedules. They render/research; they do not schedule Instagram posts. Metricool executes individual approved publication dates.

The weekly task reads current policy/backlog, resolves outstanding work first, verifies the whole month's publishing allowance, researches and creates varied content, applies review gates, schedules only approved editions, re-fetches imports/status, learns from available real analytics and reports material outcomes/blockers. Held posts never become publishable merely because their date arrives.

## Production

Photo briefs: content/posts/; scripts/render.py;1080×1350 JPEGs. content_type=collection/discovery for v7+; internal issue is only an asset ID. No public Collection sequence. Current total5–10 pages including follow card. Supporting overlays at most30 editorial words.

Reel briefs: content/reels/; scripts/render_reel.py;1080×1920 H.264 MP4 without audio. At least five distinct purposeful shots. Verify zero audio streams and full motion/text quality. Iceland approved discovery text uses48px centred lines starting y1280 at1080-wide.

Evidence: content/research/, content/reviews/, media manifests. Pin reviewed commits and hashes; keep full caption/rights/alt text. Appropriate renderer checks: python scripts/test_editorial_renderer.py and python -m unittest discover -s tests. Tests are not visual approval.

Approximately three publishing slots/week: Monday19:00, Wednesday12:00, Thursday09:00 UK; a fortnightly Reel replaces a carousel. Internal ceiling16 monthly publications across networks/formats, subject to actual free account constraints. Skip weak/unapproved content; no compensatory volume. Never store credentials in this public repo.
