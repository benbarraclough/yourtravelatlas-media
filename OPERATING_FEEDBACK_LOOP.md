# Atlas closed-loop production, rejection and learning policy
**Effective 9 November 2026.** Complements the canonical `AUTOMATION_PIPELINE.md`, `EDITORIAL_REVIEW.md`, `EDITORIAL_GUIDELINES.md` and `CONTENT_PROCESS.md`. Goals: unattended quality, a real 14+ day approved/scheduled buffer, no silently empty slots, no additional spend.

## What counts as success

A research brief, successful render, review report or completed ChatGPT task **is NOT a scheduled post**. A successful delivery cycle ends only after Metricool has actually received every correctly ordered finished media file and shows `providers.instagram.status=PENDING`, `draft=false`, `autoPublish=true`, correct slot/timezone/caption/media count/alt text; later confirm `PUBLISHED`. Track actual future scheduled dates, not a plan. Monthly maximum 20 known entries, and any stricter verified account cap. Aim four quality posts weekly, evenly spread; maintain >=14 days with actually approved/scheduled material plus >=3 independently prepared candidate concepts (not mislabelled as publishable).

## Shared learning across separate tasks (persistent, verifiable, not model retraining)

All research, production, QA/revision/scheduling, recovery and growth tasks MUST read:
1. Live Metricool next 30 days + month count and the current GitHub pipeline.
2. `content/production-queue.json` (shared exact-edition state).
3. `content/qa-lessons.json` (concrete reusable failures, fixes, whether a fix was proved).
4. `content/quality-feedback.json` (event-level failed gates, exact repairs, results and unresolved work; preserve evidence and link to reusable qa-lessons).
5. This document and the quality/copy standards.

Every rejection or technical failure MUST persist an entry in `content/quality-feedback.json`, and promote the proven prevention check to `content/qa-lessons.json`; each entry must be machine-readable: `edition_id`, `stage`, `observed_at`, `failure_class`, `affected_slide_or_field`, `evidence_url_or_asset_hash`, `specific_problem`, `remedy_attempted`, `next_action`, `owner_stage`, `attempt_count`, `status`. Avoid overwriting past history. When a replacement succeeds, mark the linked failure `RESOLVED` with commit/workflow/QA evidence; lessons must name the actual preventive check for FUTURE work. Do not infer performance-driven lessons from sparse engagement numbers.

Feedback flows immediately in GitHub: QA rejection becomes the top production input; source failures become research's sourceability filter; renderer failures become schema/preflight tests; eventual publication and engagement become Growth's experiment evidence. Compare every new brief against relevant failure classes so the same failure is not repeated silently. Growth reviews the log weekly, promotes a recurring issue into a concrete template/check/test instead of rewriting style on intuition.

## The closed-loop state machine

`IDEA -> SOURCEABLE_COMMISSION -> IN_PROGRESS -> RENDERED_PENDING_QA -> QA_APPROVED -> SCHEDULED -> PUBLISHED`

At any step, a failure routes to `REVISE` or `BLOCKED` with an exact prescriptive fix; an irreparable concept routes to `REJECTED` with a replacement candidate link. Never call a candidate `QA_APPROVED` until its exact version (brief hash + seven completed slides/clips) passes all seven editorial gates. The actual connected Metricool `PENDING` status is the only `SCHEDULED` success state.

1. **Sourceability before commissioning.** Validate at least the planned hero and key signature visuals against genuinely free commercial reuse terms, page identity/location and a workable portrait crop. For a difficult multi-location carousel, seek evidence for ALL required signature subject types before declaring commission ready. Search alternatives early; avoid accumulating impossible concepts.
2. **Production is a repair-or-replace loop.** Prioritise `REVISE` from QA, then highest-priority sourceable concept. Attempt a targeted fix from latest feedback. If two materially different replacement attempts cannot resolve a blocking photo/source/rights/technical issue, park that exact item with evidence and switch to a second viable concept **in the same run**, rather than using the entire execution to repeat one search. If the source page or media looks weak, reject it immediately. Produce actual assets; only advance after a real renderer workflow confirms current hashes, outputs and zero errors.
3. **Review both challenges and corrects.** Review the seven actual full-size and phone-scale carousel images (or real Reel motion and no-audio proof) and the caption; explicitly identify the weakest asset and any failed gate. Fix straightforward text/schema/source defects during that same QA execution, re-render and review changed outputs before publishing. If substantial replacement is needed, write a precise `REVISE` feedback record and make the next production run prioritise it, with a fallback concept ready. Do not give half-passes or schedule unfinished work.
4. **No endless retry of one idea.** After two failed production attempts or two unsuccessful QA revisions for the same fundamental problem, switch to a genuinely distinct viable concept; preserve the original and failure history, do not discard learned evidence. The loop continues across later automated executions until a real candidate PASSES, while observing platform/runtime/source limitations.
5. **Immediate scheduling on PASS.** Retrieve the actual current Metricool month/allowance and schedule the earliest genuine vacant, spaced slot; verify the imported exact media/caption/alt/time/date/status. If provider upload fails, retry with a corrected legitimate media URL/format; never claim success on a failed mutation. Re-fetch to avoid duplicate posts.

## Coverage watchdog and failure escalation

Every production and review job, not just Saturday recovery, measures `scheduled_days_ahead`, `next_7d_occupied_slots`, `next_14d_occupied_slots`, and `next_vacancy` using fresh Metricool data. If fewer than **seven days** have trustworthy scheduled posts ahead or any target publishing slot within **72 hours** is empty, mark the pipeline `RECOVERY_REQUIRED` and give sourceable candidate + revision first priority over commissioning extra ideas. If the next 14 days are not covered, keep building; a 14-day buffer is a minimum resilience target, not a publication-rate cap. Use actual four-per-week spacing, not one post every day simply to show coverage. A rolling empty period after a scheduled post is a warning, not automatically a full seven-day gap if the next planned slot is properly staffed.

The daily QA/scheduling job doubles as a watchdog and must never finish an empty-calendar run saying simply “all checks complete.” If it can create and verify a sound post, it should. If no exact media is approved, report **0 new posts scheduled**, exact blocking reason/owner and next retry or fallback; leave an actionable persistent `RECOVERY_REQUIRED` state. Saturday recovery independently reconciles publishing success and unresolved work. Repeated failure (two executions on the same missing future slot, blocked provider account, or zero scheduled upcoming posts) must be prominently reported to the owner in completion notifications instead of staying silent. Notifications themselves rely on user's ChatGPT notification configuration.

## Safety / guarantee boundary

The process CAN repair a documented technical error, swap source photos, reject a weak concept, pass on learnings and recheck the live calendar repeatedly. It CANNOT guarantee that high-quality legal imagery is always available, a third-party upload never fails, account entitlements remain unchanged or a run starts at exactly its configured time. In these cases, **fail safe (do not publish misleading or unlicensed content), pivot where possible, and surface an explicit operational alert**. Never lower the seven-gate standard to manufacture an apparently full schedule. No paid API, music, fake AI scenery, manual owner sign-off on routine material or concealed user costs.

## Immediate learning from 9 November Namibia recovery

- Reject hero frames that do not depict the headline premise (inland dune when text promises ocean). New Sandwich Harbour hero verified coast + dunes.
- Reject a facade if the promised reveal is a sand-filled Kolmanskop room; replace with an actual photographed interior.
- Treat a free photo page as a *lead*, not final assurance; check free vs Unsplash+ licence, photographer and named exact location, downloaded file pixels and final crop.
- Preflight each slide for `activity_source` in `fact_sources` before launching the image renderer; first run on 9 November failed specifically on this omitted field; second run fixed it and successfully produced seven JPEGs.
- Avoid Japan-style lengthy explanatory disclaimers and season-by-season distinctions in public captions; keep full research in private ledgers.
- The practical evidence of feedback efficacy is Namibia: initial unrendered media failures on 8 Nov -> new sourceable photos and repaired renderer inputs -> seven rendered images, actual seven-gate review -> Metricool-confirmed pending publication for 11 Nov.
