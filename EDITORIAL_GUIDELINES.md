# Your Travel Atlas — Editorial Playbook v4

Owner's instructions consolidated 28 October 2026. This document is the editorial source of truth for the @yourtravelatlas automated publication. Existing code checks are guardrails, not a substitute for editorial judgment.

## Mission and voice
A premium-feeling, curious, original Instagram travel magazine that sparks the desire to explore. Not a sales page, affiliate funnel, destination encyclopedia, AI-photo dump, generic listicle farm or safety leaflet. Showcase places, experiences, routes and ways of travelling, whether adventurous, relaxed, urban, cultural or remote. Speak to the reader as a curious traveller, not like a tourism brochure. "WANDER FURTHER" is the consistent tagline.

## Accessibility and energy balance — HARD EDITORIAL REQUIREMENT
The publication must welcome travellers who want *easy, sociable, achievable trips*, not just physically demanding destinations. Think a weekend in a beautiful town, a gentle coastal escape, cities and neighbourhoods, good food, beaches, comfortable holidays, art, culture, easy train trips, scenic drives, spontaneous breaks and unusual low-effort discoveries as well as hardcore adventures.

Target a flexible long-run mix: approximately **40% easy exploration, 35% journeys and approachable experiences, 25% demanding adventure**. This is a portfolio balance, NOT a rigid per-post classifier or a license to force ideas into a formula. Some destinations suit a mix of easy days and more demanding options; show that range. Do not assume everyone wants to hike a mountain, surf an expert wave, spend a fortnight driving remote roads or pay for expensive excursions.

**Immediate corrective action:** issues 001–003 are predominantly active, outdoors-heavy regional collections. In the *next three fresh issues*, at least **two** must foreground low-friction, attainable travel (city/culture, seaside, relaxed food/design, rail or easy getaway), and **at most one** should centre a strenuous adventure. Avoid three consecutive geographically distant or expedition-style concepts. Preserve the brand and premium visual style. Suggestions should spark ideas the account owner might want to pursue too, not require heroics or deep pockets.

For every future issue, record **effort level** (`relaxed` / `moderate` / `adventurous`) plus an **accessibility angle** in the JSON. Explain how an ordinary traveller could enjoy it with a friend, without presenting accessible places as boring. Do not fabricate budgets or public transport access.

## Music and audio policy
- **Static image carousels:** PUBLISH WITHOUT MUSIC. Metricool/Instagram's official API cannot auto-attach music to image carousels. Never switch to manual posting just to add sound, since no routine admin is the user's goal.
- **Future authentic video Reels:** Select ambient, warm, atmospheric, understated instrumental or location-appropriate natural sounds only, consistent with the place and pace. Prefer real ambient sound when it adds meaning. No obnoxious or irrelevant viral songs, aggressive drops, comedy noises, forced pop soundtracks, or unlicensed re-uploaded "original" music.
- Only use properly cleared tracks for the Instagram account and exact usage, preferably Meta Sound Collection or demonstrably owned original sound. Never infer that "trending" means licensed.
- Metricool can add Reel audio when the connection uses Facebook Login and supported authorised audio; if unverified or unsuitable, use natural original audio or silence. No automated Reel is allowed until the rights, audio, rendered 9:16 video and auto-publish pipeline are demonstrably tested.
- Do not ask the owner to vet ordinary music choices; skip audio when confidence is not high.

## Continuous improvement without brand drift
Make modest, evidence-backed, **backward-compatible improvements** to content research, verified imagery, accessible travel variety, on-screen copy, SEO/search keywords, alt text, metadata, usability, formatting, no-repeat tracking, quality gates and shareability whenever a clear opportunity appears. Assess free GitHub, Metricool and other safe no-cost capabilities, but never assume a new integration is required or connect/install services without the user's authorisation. Avoid subscription costs and paid APIs.
Maintain the core masthead, numbered issue, WANDER FURTHER tagline, high-quality licensed photography, friendly editorial storytelling and free unattended workflow. Do not silently change fundamental account strategy, graphic identity, publishing frequency, account privileges or commercial policy.
Before modifying the production pipeline, test the new behaviour and inspect rendered media, then confirm the Metricool schedule still works. Log meaningful changes in the repo's editorial guidance or README and use account analytics when there is enough data, avoiding conclusions from tiny samples. Improvements are *not* a mandate to constantly experiment at the expense of consistency.

## Every story begins with an idea
Before browsing pictures or writing a caption, define:
- **Editorial premise / travel motivation:** What is this post inspiring — road trip, solo city weekend, hiking, rail/interrail, surf, skiing, food/culture, scenic area, unusual stay, longer itinerary, off-season escape or wider destination discovery?
- **Reader promise:** What will someone understand, imagine or discover after swiping?
- **Scope:** Is this one precise destination, a region, a route, several separate places or an open-ended collection? Do not imply disjointed scenes form a one-day itinerary.
- **Audience and moment:** Who is it especially appealing to, and is the season or travel-planning trend relevant?
- **Original angle:** How is this noticeably different from posts already published or scheduled?
Post formats, pace, number of images, amount of explanatory text, location mix, cover wording and caption treatment should follow the premise — NOT a rigid "six reasons" template.

## The imagination-to-itinerary test — NEW HARD GATE

The reader should not merely think “nice view”. They should be able to say to a friend: **“We could actually do this: here's the adventure.”** The publication exists to spark real plans and shared experiences.

For every concept, write a short unpublished editorial decision before asset sourcing:
- **Intent:** a specific trip idea, activity, city experience, journey or carefully chosen wider collection
- **Reader scenario:** who could do it together, how it might fit a weekend, day, longer trip or open-ended wishlist (never invent timings)
- **Share hook:** a genuine reason to send it to a friend, e.g., “this is our next road trip / hiking day / group trip”
- **At least three distinct concrete experiences** that can be pictured and reasonably planned, and for each, a research-backed reference
- **Originality:** what it adds to the grid that previous issues have not
- **Final editorial verdict:** publish only when it is compelling and useful, not because assets are available. REJECT a premise or a photo set that feels generic, repetitive, incoherent or low on genuine inspiration. Rework from scratch or choose an entirely different premise; don't spend effort polishing a weak concept.

**Every supporting slide needs an experience:** a particular action, route, excursion, local ritual or itinerary-building idea, not an instruction to merely “see”, “watch”, “discover” or “explore” the depicted landmark. Action verbs are fine when attached to a real, evocative, specific plan, e.g. “Ferry to Kalsoy, then walk from Trøllanes to the lighthouse”; “Take the cable car from Ortisei, then hike the Seceda ridge”; “Book a guided kayak trip on the Walvis Bay lagoon.” Avoid invented tours, travel times, operators, seasonality, route continuity or promises of sightings. Research the exact feasibility of suggestions before publishing. A page can be more general when its creative premise warrants it, but should still convey real experiences, not empty commands.

A post may be gorgeous and technically valid yet still **not good enough**. That is a reason to reject it. Neither deadline nor scheduled cadence overrides this editorial gate. Never require user approval for each post, but pause/skip if it cannot meet the standards.

## Editorial reference desk and competitive learning
Research analogous editorial accounts and sources periodically, and before planning materially new formats. Learn a principle, not copy an individual post or someone else's photograph without rights:
- **hospitality.guide** — discovery-led subjects, photogenic themed collections; improve on this by pairing them with real traveller-useful, location-specific activities.
- **Accidentally Wes Anderson** ([official](https://accidentallywesanderson.com/faqs/)) — recognisable curatorial visual signature + unusual real places; adapt consistent taste, not their signature look or photographer assets.
- **LOST iN** ([about](https://lostin.com/pages/about)) — local-character city and neighbourhood immersion, culture and design; useful model for city deep dives rather than obvious attractions.
- **Along Dusty Roads** ([about](https://www.alongdustyroads.com/about-us), [road trips](https://www.alongdustyroads.com/the-road-trip-guides)) — actionable, honest slow-travel and itinerary detail; extract the *trip design* approach without borrowing copy or implying firsthand travel.
- **Atlas Obscura** ([about](https://www.atlasobscura.com/about.html)) — genuine curiosity and unusual experiences; verify practical access and traveller appeal rather than relying on novelty alone.
- **@travelanddestinations / @beautifuldestinations** — strong photography and global discovery; never be an anonymous repost feed, and distinguish Your Travel Atlas through deeper experiences.

When reviewing a comparable account, answer: What is its post's promise? Why would someone share it with a friend? What specific info helps transform interest into an adventure? What can we do more intelligently and originally? Do not invent views, engagement statistics or social performance without reliable data.

## Cover — visual hierarchy (non-negotiable)
1. Top: **YOUR TRAVEL ATLAS** masthead.
2. Small: **ISSUE 001** (increment globally) plus compact slide count (01/06).
3. **The destination/region in its own prominent, legible bold line**, materially larger than the secondary travel-type label (e.g., NAMIBIA above WILD ROAD TRIPS). It must be instantly obvious where the post is about even when the biggest headline is an abstract travel hook.
4. **Largest typographic element**: the most compelling, concrete promise/hook. E.g., "SIX VERY DIFFERENT REASONS TO EXPLORE" big and "NAMIBIA / ROAD TRIPS" small. Do not bury the hook in a subtitle. The headline need not be a number or list.
5. Optional short, inviting supporting line that does not duplicate the headline.
6. Bottom: **WANDER FURTHER / @YOURTRAVELATLAS**.
7. Remove "FIELD NOTES" from all images.
8. Strong, authentic and beautiful hero shot; high-contrast readable type, portrait 1080×1350, safe Instagram crop margins. Do not plaster text over the main photographic subject.
All post and slide text should use correct destination names, readable type, appropriate line breaks and thoughtful spacing.

## Supporting slides
- Usually 5–8 total high-quality slides (minimum 5, Instagram maximum 10 in this pipeline). Each photo must be independently compelling and add a different place, perspective, activity or atmosphere. Choose deliberate variety, not a batch of lookalike photos.
- Each slide should explain a distinct part of the travel idea, ideally with **place/experience name** and a short, concrete, vivid, **specific experience a traveller could actually plan**, backed by research; show a plausible adventure, journey or activity, not just a generic description.
- Examples: "Walk across a white clay pan dotted with dark, skeletal trees" rather than "Check 4×4 access"; "Explore the coast where the desert meets the Atlantic" rather than "See how quickly the landscape changes"; "Hike above the valley to a dramatic limestone ridge" rather than "Plan a day for this hike."
- **No health-and-safety instructions, access restrictions, generic filler, empty 'see this / watch that' commands or scolding in the small on-image description.** Relevant material access/safety requirements belong in the researched caption or a separate practical planning note when genuinely significant.
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

## Reels — cinematic discovery with a mandatory inspirational quality gate
- **Independent series:** Reels have their own internal `reel_number` sequence separate from carousel issue numbering. Do not show a number or clip counter publicly.
- **Layout:** very small YOUR TRAVEL ATLAS at the top, legible destination at the top, and a concise **inspiring editorial hook or plausible experience** near the lower portion (but above Instagram interface controls), with elegant contrasting serif. **Do not put WANDER FURTHER on the Reel at all**; retain it for photo carousel branding only. Avoid overlaying generic lists of the available footage. Evaluate mobile contrast and keep graphic elements minimal.
- **Editorial test — hard gate:** Ask whether the Reel makes a viewer want to visit the place or send a concrete trip idea to their friends, *even without reading the caption*. The video needs a compelling beginning, independently striking moving shots and a sense of progression or experience; do not just assemble whatever free footage exists. Five genuinely different, purposeful shots minimum (normally 5–8). If the video feels routine, generic or underwhelming, **reject the entire concept** and choose another. A completed MP4 is not evidence of inspiration.
- **Music — professional and upbeat:** Use warm, positive, modern, properly recorded indie-pop, lively but tasteful instrumental, soft house, acoustic and naturally rhythmic travel music that supports the images. No sombre pads, generic MIDI-sounding synthesized backing, obnoxious or unrelated meme songs. The mood and emotional match are editorial quality gates, not satisfied by an AAC track alone. Research music choices from successful travel Reels without copying or assuming popular audio is cleared.
- **Rights and delivery:** Only use an individual track with verifiable licence terms for professional Instagram video use, genuine artist attribution and a legitimate automated download path that passes GitHub Actions (with track provenance recorded in the brief). The Mixkit Stock Music Free License does permit social videos, but the attempted direct download of “Just Keep Walking” by Michael Ramir C. returned HTTP 403 from GitHub Actions on 29 Oct 2026, so **that track's current URL is NOT approved for automation**. Do not work around access controls or silently switch to the rejected synthetic soundtrack. Claims can arise even with licensed music, so never claim zero platform risk. Find another legitimately accessible free track and test actual video and audio before considering publication.
- **Music blocker means no Reel:** If properly licensed, uplifting music cannot be accessed and evaluated automatically, leave the Reel unscheduled/draft. Photo carousels continue normally. The image/story and music must BOTH meet the editorial gate. A mediocre video is not rescued by better music.
- **Production:** research and verify actual footage source pages, locations, and all travel claims; use `content/reels/NNN-slug.json`, `scripts/render_reel.py`, and `.github/workflows/reels.yml`. GitHub Actions creates 1080×1920 H.264 + AAC genuine video, storyboard, cover and provenance manifest. **Visually inspect all scenes** and audio; mark a technically successful but creatively mediocre Reel as rejected.
- **Cadence and cost:** Target one Reel every fortnight, replacing a regular carousel slot, not increasing publication frequency. Combined hard internal ceiling 16 publications per calendar month, well below Metricool Free 20. Any missed slot due to poor content is acceptable; never compensate by forcing a weak post or spending.
- **Lisbon decision 29 October 2026:** The first Lisbon Reel met technical validation but failed the stricter inspiration standard: too many ordinary sightseeing scenes, and cool/dull final imagery with misleading golden-hour copy. It was explicitly **moved to a Metricool draft, with auto-publishing disabled**, UUID `5053010952195819165`. Keep it as an archived rejected pilot; DO NOT republish unless fully re-concepted and reviewed. Its existing source material is not automatically an approved future template.
- **Cinque Terre decision 29 October 2026:** The replacement Cinque Terre-by-train Reel also technically rendered, but several 9:16 shots cropped poorly and the final beach scene lacked visual appeal. It was **editorially rejected and never scheduled**. Its source file is marked `editorial_status: rejected`; do not revive automatically.
- **Scheduling:** Metricool `instagramData.type=REEL`, verified MP4 and cover, final original caption, accurate credits, `autoPublish=true` and `draft=false` only after all gates pass. Recheck final state. Never claim publication until actual platform status confirms it.

- **Istanbul Reel 003 decision 29 October 2026:** A fresh seven-clip city-in-motion Reel `content/reels/003-istanbul-between-continents.json` rendered successfully to `media/reels/003-istanbul-between-continents/reel.mp4`, 1080×1920, 22.1 seconds, with encoded AAC audio from Kevin MacLeod's `Protofunk` (CC BY 4.0; official source `https://incompetech.com/music/royalty-free/index.html?Search=Search&isrc=USUAN1100103`). Seven Pexels clips passed source/encoding checks. Output exists with cover, storyboard and manifest. **Technical success does not constitute editorial approval.** This run could not directly inspect actual moving frames or listen to the final mastered track in context; keep candidate `editorial_status: candidate_not_approved`, do not auto-schedule or publish until an actual visual-and-listening quality review passes. Earlier licensed-music attempts failed with HTTP 429 on Wikimedia and a certificate mismatch at static.incompetech.com; do not bypass these controls. An alternative canonical HTTPS Incompetech source worked.\n\n## Metricool Free plan — hard publishing budget
- Metricool Free permits **at most 20 actually published posts per calendar month** for this connected brand. A carousel counts as one post and a Reel counts as one post. Published content in the same month counts across connected networks, so do not cross-post through Metricool without deducting the additional network publication(s). Drafts do not count before publication, but they must be tracked to avoid double-booking.
- Enforce a more conservative **internal cap of 16 total posts per calendar month**, across all types (feed/carousel/Reels/Stories) and networks: count **already published + pending automatically scheduled + any planned new posts**, and include manual posts visible in the account or planner. This preserves four slots of buffer under the provider's 20-post limit.
- **Reels replace carousel slots; never add extra posts to the current cadence.** For a two-week trial, use five carousels and one Reel, subject to the same budget.
- Before every creation/update and after every scheduler run, query Metricool's planned posts for the **entire target month** and inspect published posts/counter or available analytics. If monthly published count cannot be verified, use the strict 16-slot allocation and avoid scheduling when any uncertainty risks exceeding the allowance. Never rely on Metricool rejecting excess posts at publication time.
- Never upgrade, pay, buy credits, or increase publication volume beyond the free entitlement. Platform limits may change; review official Metricool Free plan guidance if the connection reports discrepancies.

## Technical process and zero-extra-cost constraint
1. Inspect the connected Metricool account/queued posts and the GitHub repo content archive. Review the recent portfolio for diversity of travel energy, geography, accessibility and experience type, and consult reference publications for lessons on original ideas, shareability and usefulness.
2. Select a differentiated premise, define travel effort and an easy/approachable alternative when applicable, a friend-worthy share hook and plausible experiences, research facts, sources, photos and traveller questions before choosing design. Reject underwhelming concepts before production even when factually safe.
3. Storyboard every planned slide and write exact on-screen title, place label and a concrete, research-supported adventure/activity idea. Reconsider the entire post when the story is not inspiring, differentiated and shareable.
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
