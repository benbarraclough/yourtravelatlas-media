# Your Travel Atlas

Editorial standards v8 (1 November 2026); **autonomous operations v9 (8 November 2026)**. @yourtravelatlas uses existing GitHub and Metricool connections at £0 additional cost. **Read [the live multi-job production pipeline](AUTOMATION_PIPELINE.md) first for operating cadence, handoffs, catch-up, 20-post monthly ceiling, tasks and delivery checks.** It supersedes older single-Thursday/three-posts-per-week/16-post policy. All existing editorial standards and approvals remain in force.

Read in order: [current state](CURRENT_STATE.json), [outstanding work](OUTSTANDING_WORK.md), [creation flows](CONTENT_PROCESS.md), [guidelines](EDITORIAL_GUIDELINES.md), [approval gates](EDITORIAL_REVIEW.md). [Audit](PROJECT_AUDIT.md) maps project decisions to implementation and weekly ownership. Current policy supersedes historical snapshots.

Three audience-facing strategies coexist in a flexible initial ~40/40/20 mix: destination discovery (Faroe, Japan, Porto), compelling honest list/trend posts, and silent real-video Reels. These use the technical renderers below, but strategy and renderer category are distinct. An additional weekly [growth-insights job](GROWTH_LOG.md) audits opportunities, experiments and account value. Every scheduled job is explicitly instructed to return a brief completion report, including when it made no schedule changes (actual push/email delivery requires user notification settings and has not yet been verified).

Three formats coexist: formal Faroe-style Travel Discovery Collection guides, hook-led Discovery carousels, and informative authentic-video Reels. No public issue numbers on any format. No music on any content. Keep internal IDs, small handle, clear hooks, concise useful overlays and rich specific captions. Destination guides need meaningful essential-place imagery, not caption-only expansion.

## Live status verified1 November

- Porto: nine-page visual remake,2 November19:00 UK; automatic publishing enabled.
- Riviera: eight-page rail edition including a real 2016 archive train,4 November12:00 UK; automatic publishing enabled.
- All four scheduled entries are PENDING with draft=false;17 revised imported carousel files exactly match reviewed SHA-256 hashes.
- Iceland: silent23-second five-shot Reel replaces Istanbul at5 November09:00 UK.
- Japan: successful six-image content retained; public numbers removed;9 November19:00 UK.
- Faroe: published design reference, frozen.
-28 obsolete files removed; source evidence and recovery history retained.

Always re-fetch Metricool; this is a dated snapshot. Updates change post IDs; UUIDs remain stable.

## Automation — operations v9

Five **enabled** specialised ChatGPT jobs (the four production/publishing stages plus Monday-evening Growth & Strategy) coordinate through the [GitHub production-stage ledger](content/production-queue.json): Research & Commission; Media Production; Quality, Revision & Scheduling; and Recovery, Capacity & Learning. Their precise task IDs/schedules are logged in [CURRENT_STATE.json](CURRENT_STATE.json) and [AUTOMATION_PIPELINE.md](AUTOMATION_PIPELINE.md). Each task must deliver actual stage artefacts or a concrete technical fix; a completed status-only run does not count as publishing success. First catch-up prioritises the empty 11 and 13 November slots after Japan.

The repository's GitHub helper workflows render media but do not themselves schedule Instagram; Metricool publishes approved content after scheduling. Owner approval is delegated for routine editions, with all quality and rights gates retained.


## Production

Photo briefs: content/posts/; scripts/render.py;1080×1350 JPEGs. content_type=collection/discovery for v7+; internal issue is only an asset ID. No public Collection sequence. Current total5–10 pages including follow card. Supporting overlays at most30 editorial words.

Reel briefs: content/reels/; scripts/render_reel.py;1080×1920 H.264 MP4 without audio. At least five distinct purposeful shots. Verify zero audio streams and full motion/text quality. Iceland approved discovery text uses48px centred lines starting y1280 at1080-wide.

Evidence: content/research/, content/reviews/, media manifests. Pin reviewed commits and hashes; keep full caption/rights/alt text. Appropriate renderer checks: python scripts/test_editorial_renderer.py and python -m unittest discover -s tests. Tests are not visual approval.

Operations v9: aim for four strong evenly spread posts per week, with a fifth only where quality and remaining monthly capacity permit; maximum 20 known calendar-month publications/reservations and any stricter free account constraints. Monday 19:00, Wednesday 12:00, Friday 19:00, Sunday 17:00 UK are default candidate slots; previously scheduled posts are preserved. A Reel replaces a slot; weak content is rejected, never filled for quota. Never store credentials in this public repo.
