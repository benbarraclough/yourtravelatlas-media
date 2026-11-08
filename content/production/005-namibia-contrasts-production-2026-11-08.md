# Namibia contrasts — actual Stage 2 production work, 8 November 2026

**Status: IN_PROGRESS / MEDIA_REVISE. NOT RENDERED, NOT QA APPROVED, NOT SCHEDULED.**
**Owner:** Atlas Content Production. **Strategy:** destination discovery (distinct real places in Namibia; no itinerary). **Renderer:** discovery carousel. **Target:** first eligible future vacancy after Japan, but never bypass QA.

## Real production finding: the initial visual candidates fail the editorial premise

I opened actual original image URLs and checked named Commons file pages, authors, pixel dimensions, and licence types. Critically, the **proposed Sandwich Harbour cover** `Sandwich Harbour 08.jpg` by Lidine Mia (4288×2848, CC BY-SA 4.0) **shows a scrubby inland dune with NO ocean visible**. It CANNOT illustrate the headline 'dunes that touch the ocean'. Reject as cover rather than label a false visual. Source: https://commons.wikimedia.org/wiki/File:Sandwich_Harbour_08.jpg .

Other actual originals inspected:
- **Deadvlei** `Deadvlei Tree (49186683317).jpg`, Mark Fischer, 6000×4000, CC BY-SA 2.0: authentic tree, white pan and dunes; **strong enough to consider**, but renderer currently rejects CC BY-SA 2.0; only after rights-preserving renderer support or another photo. https://commons.wikimedia.org/wiki/File:Deadvlei_Tree_(49186683317).jpg
- **Spitzkoppe** `Spitzkoppe Rock Arch Viewpoint.jpg`, Daniel Kraft, 4600×3456, CC BY-SA 3.0: file description explicitly says **peak seen from rock arch viewpoint**, NOT an image of an arch itself. Never caption it as an arch. Original >13 MB could not be displayed in this inspection. Requires actual pixels and rights-supported image; **unapproved**. https://commons.wikimedia.org/wiki/File:Spitzkoppe_Rock_Arch_Viewpoint.jpg
- **Kolmanskop** `Kolmanskop hospital, Lüderitz (Namibia).jpg`, Olga Ernst, 4928×3264, CC BY-SA 4.0: original visibly shows a fairly ordinary building exterior, **NOT sand-filled interior**; reject for promised reveal. https://commons.wikimedia.org/wiki/File:Kolmanskop_hospital,_L%C3%BCderitz_(Namibia).jpg
- **Cape Cross** `Seals at Cape Cross, Namibia (3045814005).jpg`, Joachim Huber, 3008×2000, CC BY-SA 2.0: original depicts many seals, but dull grey/foggy flat composition and weaker portrait crop. **Reject for this premium visual edition**; renderer also does not yet support BY-SA 2.0. https://commons.wikimedia.org/wiki/File:Seals_at_Cape_Cross,_Namibia_(3045814005).jpg
- **Etosha** `Namibia Etosha-Nationalpark Elefanten 1.jpg`, Zairon, 4536×2685, CC BY-SA 4.0: actual elephant is tiny in distant bland grassland, not a compelling wildlife/waterhole reveal. **Reject**. https://commons.wikimedia.org/wiki/File:Namibia_Etosha-Nationalpark_Elefanten_1.jpg
- **Alternative Etosha** `Elephants at Etosha National Park04.JPG`, Vberger, 2048×1536, public domain per author; Commons file page verified, but final visual and portrait composition not yet reviewed. Renderer currently does not accept this PD licence label. https://commons.wikimedia.org/wiki/File:Elephants_at_Etosha_National_Park04.JPG
- **Alternative Kolmanskop** `Kolmanskop Ghost Town.jpg`, SkyPixels, 4000×2250, CC BY-SA 4.0; original not yet inspected for interior promise, requires visual confirmation before selection. https://commons.wikimedia.org/wiki/File:Kolmanskop_Ghost_Town.jpg
- **Closing card:** no approved distinct Namibia scenic original yet. Do not reuse cover or filler.

**Implementation check:** the live `scripts/render.py` `ALLOWED_HOSTS` includes upload.wikimedia.org and thumb.wikimedia.org, but accepted licence strings are `Unsplash License`, `Pexels License`, `CC BY 2.0`, `CC BY 4.0`, `CC BY-SA 4.0`, `CC0 1.0`. BY-SA 2.0 and BY-SA 3.0 (and PD as a label) are NOT supported. Never falsify licence strings to make the renderer pass. If expanding supported licences, update tests, ensure attribution and compatible derivative/share-alike conditions, then rerun both suites.

## Editorially complete draft: seven-page storyboard (NOT an asset-approved manifest)

1. **Cover — Sandwich Harbour**. Headline A: “Namibia has dunes that touch the ocean. That's only the beginning.” Alternate B: “An abandoned diamond town. A desert beside the Atlantic. This is Namibia.” Must show BOTH dunes AND actual ocean in one authenticated striking frame; current lead fails.
2. **Deadvlei — a white pan, dark trees, red dunes.** Overlay: “Deadvlei / Walk among dark tree silhouettes standing against a pale clay pan and towering red dunes.” Distinct geometric high-contrast scene. Existing candidate promising, BY-SA 2.0 compatibility unresolved.
3. **Spitzkoppe — granite and scale.** Overlay: “Spitzkoppe / Explore sculptural granite formations beneath Namibia's dramatic desert peaks.” Use an image clearly showing actual formation/arch, not generic mountain.
4. **Kolmanskop — sand inside abandoned houses.** Overlay: “Kolmanskop / Step into a former diamond settlement where desert sand has reclaimed empty rooms.” Must show real sand-filled room; exterior candidate rejected.
5. **Cape Cross — seal colony.** Overlay: “Cape Cross / See Cape fur seals gathering along the Atlantic coast at a protected breeding reserve.” Choose compelling identifiable seal/coast frame; no guaranteed count.
6. **Etosha National Park — wildlife in an open salt-pan landscape.** Overlay: “Etosha / Look for wildlife around waterholes in a vast national park shaped by its salt pan.” Use a real visibly compelling animal/waterhole image, no guaranteed sighting.
7. **Distinct scenic CTA**. Exactly: “Fill your feed with wonder.” / “Follow @yourtravelatlas for beautiful places and the details that turn them into real plans.” Requires distinct, properly licensed exceptional Namibia scene, not a recycled support photo.

All overlays under 30 words including heading. One photo per slide. Cover/CTA scenic; 7 total pages. Avoid public issue numbers, Wander Further and music. Maintain crop/focus coordinates and small handle once actual photos selected.

## Two researched caption hooks

A. “Where dunes meet the Atlantic, deserted rooms fill with sand and ancient-looking tree silhouettes stand against red dunes. Namibia is full of places that deserve a second look. 🇳🇦”
B. “A coast that looks like a desert cliff, a town reclaimed by sand and a pan filled with dark trees. These are six different reasons to discover Namibia. 🇳🇦”
Prefer **A** unless the final selected cover fails to show the sea, in which case change both image and premise rather than falsely claim it.

## Draft complete caption — awaiting exact image credits

Where dunes meet the Atlantic, deserted rooms fill with sand and dark tree silhouettes stand against red dunes. Namibia is full of places that deserve a second look. 🇳🇦

📍 Sandwich Harbour — dunes rise beside the Atlantic south of Walvis Bay. This is challenging coastal 4WD terrain: use an experienced local guide rather than treating it as a normal self-drive beach stop.

📍 Deadvlei — walk across a pale clay pan scattered with long-dead camel-thorn trees, framed by the red dunes of the Sossusvlei area.

📍 Spitzkoppe — explore granite rock formations and wide desert views; confirm access arrangements locally.

📍 Kolmanskop — visit the abandoned diamond-era settlement near Lüderitz, where sand has invaded historic buildings. Check tour/permit arrangements before visiting.

📍 Cape Cross — a protected Atlantic-coast reserve known for its Cape fur seal breeding colony. Observe wildlife from the designated visitor areas.

📍 Etosha National Park — look for wildlife along permitted roads and at waterholes near the enormous salt pan. Sightings are never guaranteed.

These are discoveries spread across a huge country, not a weekend route or one-day drive. Save the places that excite you, then build a realistic trip around the regions you want to explore.

**PHOTO CREDITS AND LICENCE LINKS TO BE INSERTED FROM THE EXACT FINAL SEVEN FILES BEFORE RENDER OR PUBLICATION.** Current copy is NOT final deliverable and MUST fit 2,200 chars with all required creator/source/licence/change notices; move lengthy full attribution to an accessible companion credits page only if legally compliant and clearly linked.

## Primary factual references checked at commission

https://nfc.na/locations/sandwich-harbour ; https://nfc.na/locations/spitzkoppe ; https://nfc.na/locations/kolmanskop ; https://nfc.na/locations/etosha-national-park ; https://meft.gov.na/national-parks/cape-cross-seal-reserve/214 . These were inspected in Stage 1, not independently reopened this Stage 2 run; before final claim QA independently recheck exact live text and current access requirements.

## Concrete next action (production, not owner)

1. Source **four or more replacements** from actually inspectable, free commercially reusable exact-location original files: Sandwich Harbour with sea visible, sand-filled Kolmanskop interior, visually powerful Cape Cross seals, prominent Etosha wildlife, plus a distinct scenic CTA and verified Spitzkoppe landmark.
2. Confirm full-size pixels and portrait crops, author, original URL, derivative permissions, attribution and licence compatibility; replace BY-SA 2.0/3.0 candidates or properly extend renderer/tests.
3. Only then write `content/posts/005-namibia-contrasts.json` with valid schema and exact seven-image manifest, launch `render.yml`, inspect output, errors and hashes. Never create a misleading fake “complete” manifest.
4. Independent QA inspects all seven actual final 1080×1350 images at full/phone size; only then may scheduling be considered.

**Stage 2 verdict:** IN_PROGRESS / MEDIA_REVISE — meaningful full-size photo audit and complete seven-page creative draft performed, but quality/rights and CTA gaps prevent responsible render. **0 renders, 0 QA passes, 0 new posts scheduled.**
