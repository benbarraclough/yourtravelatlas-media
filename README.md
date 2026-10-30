<!-- Owner update 30 October 2026: supersedes earlier public-numbering rules. -->

**Current owner direction:** remove public issue numbers from ALL formats. Keep internal IDs for tracking/removal only. Destination guides must include the essential sights and signature experiences before optional discoveries; record covered and omitted essentials with reasons. Rail/road/activity concepts must visibly show the train/road/activity in at least one meaningful image. Preserve the successful Japan editorial direction. Iceland discovery Reel text: smaller, horizontally centred, in the lower middle of the frame (48px at 1080-wide; first line y=1280), with no footage/content changes. Retire Protofunk as the default: research contemporary travel-page audio and verify a lawful publishing route before using a replacement.

# Your Travel Atlas — media and editorial workflow

**Start here:** [Three-format creation process and flowcharts](CONTENT_PROCESS.md).

Read [Editorial Guidelines v7](EDITORIAL_GUIDELINES.md), [mandatory approval gates](EDITORIAL_REVIEW.md), [reference evidence](EDITORIAL_BENCHMARKS.md) and, for video, [Footage Sources](FOOTAGE_SOURCES.md) on every production run. The three formats coexist: formal **Travel Discovery Collection** destination guides, attention-grabbing **Discovery carousels**, and informative authentic-video **Travel Reels**. No format displays a public issue number. Internal IDs remain for tracking and deletion.

£0 additional cost. GitHub Actions renders assets; ChatGPT researches/reviews and Metricool schedules. This public repository contains no Instagram credentials and does not publish directly. The recurring task reads current policy rather than relying on chat memory.

## Production paths and capability boundary

- Photo briefs: content/posts/NNN-slug.json; scripts/render.py; .github/workflows/render.yml; 1080×1350 JPEGs and provenance manifests in media/<slug>/.
- Reel briefs: content/reels/NNN-slug.json; scripts/render_reel.py; .github/workflows/reels.yml; 1080×1920 H.264/AAC MP4, cover, storyboard, caption and provenance manifest in media/reels/<slug>/.
- Research and exact-edition approval records: content/research/ and content/reviews/. Pin reviewed media commits before importing to Metricool.
- V7 photo briefs require content_type=collection or discovery. Collection additionally requires a unique collection_number >= 2 (Faroe is Collection 001); issue remains the internal asset ID. Collection uses the formal photo-led masthead; Discovery hides public numbers. Both retain the 30-word supporting-copy cap and final follow card. Default batch renders preserve legacy briefs; explicit legacy renders are for recovery only. See CONTENT_PROCESS.md for the complete handoff.
- Current photo pipeline supports 5–10 total pages. Numerical promises must fit honestly; expand/test the pipeline and verify delivery constraints before larger formats. Do not omit promised items.
- Reel rendering now rejects fewer than five distinct shots, including the former four-shot exception. V7 briefs additionally require substantive location_evidence, reader_value and distinct_contribution for each clip, and contextual overlays on at least three shots. Editorial review must still assess their quality. revision_required briefs are skipped in batch production. Additional footage hosts/licences and music tracks require individual verification and tested support.
- Renderer tests: python scripts/test_editorial_renderer.py and python -m unittest discover -s tests. Tests do not replace inspection of all actual images, complete video playback or listening to the mastered track.

## Current editions — status reference as of 29 October 2026

Always re-fetch Metricool and current review records before acting; this table is not a live queue.

| Edition | State | UK schedule / handling |
| --- | --- | --- |
| Faroe Islands, internal carousel 001 | Published; frozen formal design reference | Collection 001 reference; do not alter/re-render to adopt new branding. |
| Porto, internal carousel 002 | Owner-approved v6 discovery | 2 November 19:00; UUID -1686861758455201569. |
| French Riviera, internal carousel 003 | Owner-approved v6 discovery | 4 November 12:00; UUID -4032844728941590495. |
| Japan beyond the big cities, internal carousel 004 | Internally approved v6 discovery | 9 November 19:00; UUID -1638283085571405156. |
| Istanbul, internal Reel 003 | Previously owner-approved and scheduled; replacement requested | 5 November 09:00; UUID 5053010952195819165. Keep until a replacement passes review and receives owner approval. |
| Seljalandsfoss, internal Reel 004 | Owner feedback: requires improvement; NOT approved | New five-shot, 23-second v7 draft prepared 30 October. Full playback/listening and owner approval remain open; no scheduling approval inferred. |

All schedule times use Europe/London. Existing approved artwork, including legacy public numbers, is preserved until intentionally revised and re-reviewed. New Discovery carousels have no public issue number. Internal IDs remain unique and stable; public Collection numbers are a separate sequence. Derive the next internal ID from current history, not a hardcoded instruction.

Lisbon Reel 001 and Cinque Terre Reel 002 are rejected historical pilots. The former Lisbon Metricool UUID now contains Istanbul; never revive Lisbon from an old status note. Namibia/Dolomites and superseded Porto/Riviera variants are historical. Do not reschedule or delete history indiscriminately.

## Scheduling discipline

Retain the existing cadence and16-publication monthly internal ceiling across formats/networks. A Reel replaces a carousel slot. Check the entire month and available published/manual counts. Use exact reviewed media, full caption/credits/alt text and the appropriate POST/REEL type. Re-fetch to verify imports, count/order, caption, date/timezone, PENDING, draft=false and autoPublish=true. Never claim publication from scheduling success.

Routine content proceeds through calibrated internal review. Owner review requests remain binding, including the current Istanbul replacement. If required evidence or media/playback/audio checks are unavailable, leave the new edition unapproved. Do not degrade quality, buy tools or force a post to fill a slot.

Final cleanup remains conditional on owner satisfaction with the finished schedule. Preserve all live/queued media dependencies, source/licence evidence and necessary recovery history.
