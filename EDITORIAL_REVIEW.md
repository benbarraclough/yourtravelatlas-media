# Mandatory editorial creation and review workflow

Owner standard, 29 October 2026. Read with EDITORIAL_GUIDELINES.md on every publishing run. This is an operating procedure, not an optional inspiration list. A filled form cannot prove good taste or factual accuracy.

## 1. Commission a specific story before collecting assets

Check the full archive and the real Metricool month first. Record the reader, trip motivation, time/scope, effort/accessibility angle, original premise and reason friends would share it. Explain the bucket-list moment in one concrete sentence. Compare with the last published and scheduled issues for geography, energy, imagery, promise and treatment. Avoid repeated European city/coast posts after the Porto/Riviera revisions.

Choose the editorial treatment explicitly: ordered itinerary, neighbourhood immersion, experience collection, event-led escape, rail journey, food/culture guide, etc. State what that treatment requires. A seven-day rail story needs day-by-day pacing and checked connections; a neighbourhood story needs specific streets and stops; a swimming collection needs exact spots and season/access context. Do not feed every story into identical headings and one-line tips.

## 2. Research the experiences and when to go

Use primary tourism bodies, organisers, transport operators, venues, museums and park agencies where possible. Look beyond the famous photograph: what precisely does the traveller do, look for, eat, ride, book or join? What nearby stop makes the experience better? What important detail would they otherwise miss?

Research festivals, special events and seasonal reasons to go, then decide whether they improve this story. Record official URLs and the checked date. Confirm edition/year, dates, exact venue and individual programme when needed. A recurring 23 June celebration is not proof of a particular 2027 concert, fireworks time or transport extension. Never present a past programme as the next one. If dates are unknown, say so or use a clearly recurring seasonal window. Avoid unsupported best-season, price, journey-time and opening claims.

Put each factual claim in a traceable slide/caption ledger. Source closure and transport decisions that materially change the plan. If official pages conflict, use the relevant current operator/venue, omit the disputed precision and document the conflict.

## 3. Storyboard and write before rendering

For every page, define its editorial job, exact place/experience, on-image detail, useful planning line when relevant, source references and photo requirements. Aim for an evocative, specific 25–50-word explanation when useful; the amount follows the story. Do not shrink typography to cram in research. Use route/planning pages for multi-step information.

Every supporting page should answer: Where exactly? What would I do? What special thing should I seek out? Why is this worth my time? Which timing/route/closure/booking detail makes it usable? Not every page needs all five answers, but the whole story must deliver them clearly.

Choose page count deliberately. Current pipeline: 6–10 total, at least five editorial pages plus one final CTA. More pages are welcome only when useful. Write `slide_count_rationale`. Never stop at five because it is easy, or expand to ten because space exists. Cut duplicated scenery, repeated neighbourhood roles and ornamental pages.

## 4. Verify every actual image

Check the original source page, photographer, reuse licence and any attribution/share-alike requirements. Record source page, actual image URL, subject, location, accurate alt text, crop focus and licence. No Unsplash+, watermarks, promotions, realistic generated scenery or copied competitor assets.

The photograph must illustrate the exact promise. A lane can illustrate a route towards a named chapel only if text makes the distinction clear; do not label the lane as the chapel. A generic firework photo is not evidence of São João. Festival imagery must be the actual festival, and old editions must be labelled archive/past edition. A summer beach photo is not a February forecast. Prefer verified event detail to a generic scenery substitute.

Record `review.reader_value`, `review.image_context`, `review.specific_detail` and `review.distinct_contribution` per image. Give real reasons, not the same stock sentence on every page. Store `fact_checks` URLs and ensure all appear in `fact_sources`. For CC images record licence URL, changes, on-image credit and caption/source links; distribute adapted CC BY-SA slides under that licence.

## 5. Challenge the story before production

Read the copy without photos. Then review photos without copy. Ask:

- Could I replace the destination name and keep this copy? If yes, rewrite it.
- Can a traveller explain a concrete plan to a friend after swiping?
- Does each page add something genuinely different and specific?
- Is the bucket-list appeal supported by the actual experience and image?
- What did we learn that a generic tourism list would not tell us?
- Are any facts, photos, event editions, routes or seasonal promises misleading?
- Does the chosen format earn its existence, or is it another interchangeable list?

Use PASS / REVISE / REJECT, with reasons. Reject a polished but uninspiring concept, low-value photo, unjustified extra slide or weak caption. Replacing one generic verb with another does not count as a revision. Return to research or choose a different concept when necessary.

## 6. Write and review the caption

Draft at least two different accurate opening hooks. Choose the one that creates the strongest travel-specific curiosity or planning promise. No generic 'discover the beauty', fake secrets, inflated superlatives, unsupported urgency or invented algorithm claims.

Deliver useful information beyond repeating the slides: meaningful sequence, route direction, what to book first, a closure/day distinction, a seasonal hook or worthwhile alternatives. Include specific names and restrained search terms. A save/share invitation should follow the value, not replace it. Keep at most 2,200 characters including every credit, licence URL and hashtag. Verify source and licence credits remain usable.

## 7. Render and inspect the actual final edition

Use editorial_version 5+. Retain the recognisable design system while selecting layouts for the story: photo-led details, clear date-led event pages and cream planning/route pages. Every new carousel ends with one standard photographic follow card: 'FILL YOUR FEED WITH WONDER.' / 'Follow @yourtravelatlas for beautiful places and the details that turn them into real plans.' Use a licensed image that supports the story and does not repeat an editorial image in the same post.

Run renderer checks and relevant layout regression checks. Inspect EVERY rendered full-size image and a mobile/contact-sheet view: exact location/subject, photographic appeal and variety, line breaks, spelling, contrast, safe margins, credits, date/edition labels and footer clearance. Re-render and re-inspect every changed page. If code changes shared behaviour, verify the published issue 001 rendering path remains unchanged. Technical success is only a technical pass.

Create `content/reviews/NNN-slug.json` with: verdict; review date; source-check date; exact render/source commit; explicit list of image paths inspected; per-slide verdict/reason; rejected/cut material; hook candidates and chosen hook; what makes the post valuable to save; caption length; date/rights checks; layout/crop checks and remaining limitations. `editorial_status=ready_for_visual_review` is never permission to schedule. An agent must actually inspect all final images, then save an approved review tied to that edition.

## 8. Schedule only the reviewed revision

Before scheduling, reread the review and compare it to the current manifest/brief and media commit. Recheck time-sensitive event facts. Check the whole month against the 16-slot internal cap / 20-post Free allowance, counting actual published and pending content. Reuse the existing UUID when replacing a scheduled post; do not create duplicates. Pause a weak existing post as a draft while rebuilding.

Import all final media, the complete final caption and matching alt text into Metricool. Confirm PENDING, autoPublish=true, draft=false, correct date/timezone, exact media count/order and full caption. Compare the Istanbul Reel to the original when it is outside scope. Record verified scheduling ID/UUID and final media revision in the review. Do not claim live publication before platform confirmation.

## 9. Improve from evidence, keep the standard

Compare strong editorial publishers periodically, documenting exact accessible examples and what was actually inspected. Separate inference from observation; no invented engagement statistics. Do not imply a visual Instagram review when access was blocked. See EDITORIAL_BENCHMARKS.md.

Use saves, shares, reach and follows only when there is enough data for a defensible comparison. Preserve useful learning in this process, not just in chat. Do not reduce research, slide value or visual checks to meet cadence. Skip the slot if standards cannot be met within the existing free workflow.
