# Your Travel Atlas — Editorial Playbook v2

Owner's instructions consolidated 28 October 2026. This document is the editorial source of truth for the @yourtravelatlas automated publication. Existing code checks are guardrails, not a substitute for editorial judgment.

## Mission and voice
A premium-feeling, curious, original Instagram travel magazine that sparks the desire to explore. Not a sales page, affiliate funnel, destination encyclopedia, AI-photo dump, generic listicle farm or safety leaflet. Showcase places, experiences, routes and ways of travelling, whether adventurous, relaxed, urban, cultural or remote. Speak to the reader as a curious traveller, not like a tourism brochure. "WANDER FURTHER" is the consistent tagline.

## Every story begins with an idea
Before browsing pictures or writing a caption, define:
- **Editorial premise / travel motivation:** What is this post inspiring — road trip, solo city weekend, hiking, rail/interrail, surf, skiing, food/culture, scenic area, unusual stay, longer itinerary, off-season escape or wider destination discovery?
- **Reader promise:** What will someone understand, imagine or discover after swiping?
- **Scope:** Is this one precise destination, a region, a route, several separate places or an open-ended collection? Do not imply disjointed scenes form a one-day itinerary.
- **Audience and moment:** Who is it especially appealing to, and is the season or travel-planning trend relevant?
- **Original angle:** How is this noticeably different from posts already published or scheduled?
Post formats, pace, number of images, amount of explanatory text, location mix, cover wording and caption treatment should follow the premise — NOT a rigid "six reasons" template.

## Cover — visual hierarchy (non-negotiable)
1. Top: **YOUR TRAVEL ATLAS** masthead.
2. Small: **ISSUE 001** (increment globally) plus compact slide count (01/06).
3. Small contextual label: location/region/country and the genre of travel. It must be immediately clear where the post is about.
4. **Largest typographic element**: the most compelling, concrete promise/hook. E.g., "SIX VERY DIFFERENT REASONS TO EXPLORE" big and "NAMIBIA / ROAD TRIPS" small. Do not bury the hook in a subtitle. The headline need not be a number or list.
5. Optional short, inviting supporting line that does not duplicate the headline.
6. Bottom: **WANDER FURTHER / @YOURTRAVELATLAS**.
7. Remove "FIELD NOTES" from all images.
8. Strong, authentic and beautiful hero shot; high-contrast readable type, portrait 1080×1350, safe Instagram crop margins. Do not plaster text over the main photographic subject.
All post and slide text should use correct destination names, readable type, appropriate line breaks and thoughtful spacing.

## Supporting slides
- Usually 5–8 total high-quality slides (minimum 5, Instagram maximum 10 in this pipeline). Each photo must be independently compelling and add a different place, perspective, activity or atmosphere. Choose deliberate variety, not a batch of lookalike photos.
- Each slide should explain a distinct part of the travel idea, ideally with **place/experience name** and a short, concrete, evocative **what it is / what you can see or do** description.
- Examples: "Walk across a white clay pan dotted with dark, skeletal trees" rather than "Check 4×4 access"; "Explore the coast where the desert meets the Atlantic" rather than "See how quickly the landscape changes"; "Hike above the valley to a dramatic limestone ridge" rather than "Plan a day for this hike."
- **No health-and-safety instructions, access restrictions, generic filler or scolding in the small on-image description.** Relevant material access/safety requirements belong in the researched caption or a separate practical planning note when genuinely significant.
- Information should paint a travel experience, not mainly list facts such as elevation, dates or foreign language place names unless unusually relevant. Do not imply wildlife is guaranteed.
- Vary slide structure intelligently when the premise calls for maps, timelines, itinerary stops, practical planning panels or city/neighbourhood details; these must be accurate and aesthetically consistent.
- Never use promotional images, logos, watermarks or near-duplicate scenes.

## Caption
- Open with a reason to care, a sensory detail, useful idea or intriguing observation.
- Give a meaningful overview: what someone might do, what a realistic trip feels like, whether to base in one place or move around, any substantive considerations such as timing, transport or travel effort.
- No unnecessary history, Wikipedia excerpts, mountain elevations, local-language trivia, inflated claims or generic travel fluff.
- Avoid repeating the carousel verbatim. The images should inspire; the caption should enrich or enable that idea.
- A *natural*, non-demanding invitation to save, share, follow or discuss only when it fits the post. No repeated formula, spam or misleading engagement bait.
- Searchable location, specific terms, proper names and restrained relevant hashtags, accurate alt text. Image text is useful for readers, while keywords in the caption and profile remain the main deliberate search surfaces.

## Editorial diversity / trend sensitivity
Alternate continents, environments, budget styles, trip lengths, traveller types, season and formats. Mix city deep-dives, hiking, unusual experiences, cultural stories, rail, surfing, scenic road trips, skiing, hidden corners and broader picture-book inspiration.
Occasionally draw on genuine contemporary travel conversations and seasonally timely trip-planning interests, only when supported by current, credible sources. Never chase silly viral gimmicks.
Consider Instagram Reels when there is verified, properly licensed and accurately located video, lawful audio, a designed hook, useful story, and an *actually tested free* rendering-to-publishing route. A static carousel is not a Reel.

## Research and provenance gates (must pass before scheduling)
- Verify all factual assertions against reputable current sources, preferably official tourism bodies, transport operators, park agencies, official destination information and primary evidence. Make no unverifiable price, route duration, legal access, seasonality, permit or opening-hour claims.
- Validate **each actual photo**: real destination and activity, visually appropriate to its exact label, accurate source page, author and explicit reusable licence (no Unsplash+), suitable 4:5 crop, resolution and independent impact. A declared licence string or successful JPEG download alone does **not** prove these things.
- No realistic AI-generated fake scenery passed off as authentic. No watermarks, brands, promotions or affiliation without specific authorisation.
- Check the full content archive for previously used location angles, photographic subjects, photo IDs, misleadingly similar photos, concept duplication and issue-number collisions.
- Validate the entire rendered output visually: especially cover headline hierarchy, text legibility, spelling, photography, crop, on-screen relevance, no warning captions. Correct and regenerate if it falls short.
- Prefer not publishing to publishing inaccurate, inappropriate, repetitive or low-quality material.

## Technical process and zero-extra-cost constraint
1. Inspect the connected Metricool account/queued posts and the GitHub repo content archive.
2. Select a differentiated premise and research facts, sources, photos and traveller questions before choosing design.
3. Storyboard every planned slide and write exact on-screen title, place label and useful descriptive copy.
4. Prepare the issue JSON in \`content/posts/\` following existing examples, using unique issue number and distinct 5–10 high-resolution licensed photos.
5. GitHub Actions renders actual JPEGs through \`scripts/render.py\` into \`media/<slug>/\` and writes \`manifest.json\`. Diagnose failures; never publish from a manifest alone.
6. Inspect all actual images, check that facts and licences remain credible, then publish through existing Metricool draft UUID or create next slot. Use final public raw GitHub image URLs; media-alt-text matches images, \`draft: false\`, \`autoPublish: true\`.
7. Re-fetch Metricool queue, confirm posted dates, new media count, full caption, alt text, pending status, no duplicate; never claim post is live before confirmed.
8. Measure saves/shares/follows/reach and Reels watch time once available. Test Monday evenings, Wednesday noon, Thursday mornings as starting UK slots, optimise later based on real account metrics. Maximum 20 posts/month on free plan.
9. Maintain existing recurring ChatGPT automation; fail closed if a required free tool, reliable licence, accuracy check or rendering step is unavailable. Zero additional spending beyond the existing ChatGPT subscription.

## Examples for current launch issues
- Issue 001: **FIVE PLACES FOR A WILD ATLANTIC ESCAPE** [large] / **FAROE ISLANDS** [small]
- Issue 002: **SIX VERY DIFFERENT REASONS TO EXPLORE** [large] / **NAMIBIA** [small]
- Issue 003: **SIX SCENES WORTH THE JOURNEY** [large] / **THE ITALIAN DOLOMITES** [small]
This is an example hierarchy, **not** a repeating formula required for new stories.
