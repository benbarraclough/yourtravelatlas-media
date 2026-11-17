# Your Travel Atlas — final triple QA and change log
**17 November 2026 · Europe/London**  
Scope: all **seven upcoming scheduled posts** on 18, 20, 22, 23, 25, 27 and 29 November, not already-published content. Brand: Metricool 7717708. Source of truth: live Metricool plus finished GitHub media, not creative briefs alone.

## Three-stage review
1. **Actual visual/media review**: each rendered carousel page (including cover and branded last slide) was opened and checked at native image resolution or scaled mobile preview for visual interest, location correspondence, text clipping, contrast and typography; latest corrected images were reviewed again. Cappadocia's eight-scene contact sheet and actual cover were inspected, and video manifest verified 1080x1920, H.264 MP4, 25.1 seconds and **no audio stream**. A full continuous playback proof was not independently recorded; no such claim should be made.
2. **Editorial/source review**: compare visible place, original photo or footage link and licensed photographer; verify named places, unique experiences, coherent promise, captions matching slide order, credited authors and source ledger; check selected facts against reputable tourism/scientific publishers. All six carousels have a scenic final **FILL YOUR FEED WITH WONDER.** page and 7–8 preceding photographic scenes (8–9 total slides). No still-photo slideshow Reels remain scheduled.
3. **Actual booking review**: re-fetch Metricool after updating the **same original UUID**; assert correct 4:5 multi-image `POST` or actual moving `REEL`, expected media counts, Instagram `PENDING`, `autoPublish=true`, `draft=false`, identical latest public caption and a complete alt-text list for every carousel. No duplicate bookings or changed dates.

## Per-post results and specific changes

| UK date | Post | Review and changes made | Slides or motion clips | Current Metricool numeric ID | QA decision |
| --- | --- | --- | ---: | ---: | --- |
| Wed 18 Nov | Seven mountain views without a summit hike | Replaced the old distant, barely visible Lake Bled church with a clear, recognisable island-and-mountains photograph by **Haonan Wei**, free Unsplash original. Updated on-image detail, public caption, photographer attribution and alt text. Checked 7 meaningful views and attractive final brand triptych. | 8 slides | 431674912 | Approved |
| Fri 20 Nov | Eight winter film-set places | All eight authentic winter scenes and final card looked coherent; eliminated duplicate `#WinterTravel` and improved all eight description lines for more specific places and experiences. Booked revised caption and alt text. | 9 slides | 431684601 | Approved |
| Sun 22 Nov | Madeira cloud-top trails and lava pools | Fixed two clipped titles and standardised eight place names, caption order and rights credits; **replaced weak fog-obscured Risco shot with vivid original Véu da Noiva coastal waterfall** (Hikerwise.com/Unsplash), with named official roadside viewpoint. Checked official Madeira PR1 trail marked CLOSED on 17 Nov 2026; removed misleading walk-access implication, described summit as viewpoint and added concise current access note. Full replacement image and published text reviewed and synced to original booking. | 9 slides | 431684520 | Approved |
| Mon 23 Nov | Indonesia / Flores and Komodo | Corrected false boat-level Padar description; distinguished gold dry-season and green rainy-season ridges; **replaced repetitive second Wae Rebo image with an original licensed Labuan Bajo sunset** by Dhiemas Afif Febriyan. Now six genuine varied travel experiences in seven original photos; updated complete creator credits and alt text. Actual new sunset scene and caption visually checked and synced. | 8 slides | 431684800 | Approved |
| Wed 25 Nov | Where the desert meets the sea | Refined labels on separate Namibia views and Wikimedia CC BY 2.0 attribution; replaced dull second Dune du Pilat image with **Maspalomas golden coastal dunes / Gran Canaria** from Marco Canepa, original free Unsplash photo. Rejected two weaker Fuerteventura candidates after visual inspection because colour and geography claims did not match the images. The actual Maspalomas photo contains several people, so removed unsupported lone-person/sunset copy. Six coasts, seven unique licensed photographs, corrected six-country names and photographer credits; synced original Metricool UUID. | 8 slides | 431692248 | Approved |
| Fri 27 Nov | Vietnam caves, karsts and lantern nights | Replaced weak branch-obscured Bản Giốc waterfall with striking original **Taryn Elliott / Pexels** aerial waterfall. Replaced ordinary mist-free Hà Giang tourist shot with original **Du Tử Mộng / Pexels** Mã Pí Lèng river gorge. Changed generic cover to **“Vietnam: Caves, Karsts & Lantern Nights”**, added useful details and accurate slide-order caption, corrected all photo licences/credits and Hanoi Train Street access note. Rechecked full new renders. | 9 slides | 431694299 | Approved |
| Sun 29 Nov | Five Cappadocia experiences worth the journey | Eight genuine moving Pexels shots, original creator attribution, true moving branded outro and much stronger bold high-contrast hook were already updated. Visual storyboard, original cover, scene descriptions, video codec/length/no-audio manifest and unchanged pending booking checked again. **No new edit needed in this QA round.** | 8 actual moving clips | 431589392 | Approved within documented playback-check limits |

## Cross-cutting issues permanently fixed
- In previous workflow, editorial validators allowed text to clip because location text was manually truncated in the brief; now corrected in actual posted versions. Maintain a requirement to **open finished media rather than only trust successful CI**.
- No lazy 'more than just…' hook, no still-image zooming Reel, no music, no public issue numbers, no post without branded photo-carousel ending.
- Individual original licensed photo or Pexels footage source references are stored in the brief and manifest. Attribution text does not itself grant media rights.
- Metricool's update endpoint assigns new numeric IDs but preserves the above post UUIDs and existing posting slots.

## Factual spot-check sources
- [Madeira tourism board: Porto Moniz Atlantic-fed volcanic natural pools](https://visitmadeira.com/en/where-to-go/madeira/north-coast/porto-moniz/natural-pools-of-porto-moniz/)
- [Visit Madeira: Véu da Noiva official waterfall viewpoint](https://www.visitmadeira.com/en/where-to-go/madeira/north-coast/porto-moniz/veu-da-noiva-viewpoint/)
- [Visit Madeira: PR1 Vereda do Areeiro trail status — marked CLOSED at audit](https://visitmadeira.com/en/what-to-do/nature-seekers/activities/hiking/pr-1-vereda-do-areeiro/)
- [Vietnam Tourism: Bản Giốc waterfall in Cao Bằng](https://vietnam.travel/things-to-do/ban-gioc-waterfall-majestic-beauty-northern-border/)
- [Dune du Pilat site: Europe's tallest dune](https://ladunedupilat.com/en/i-discover/in-short/)
- [Indonesia official travel: Komodo/Pink Beach/Padar](https://www.indonesia.travel/gb/en/travel-ideas/marine/unveil-the-lands-of-dragons-firsttimers-guide-to-komodo-national-park)
- [Slovenia official visitor information: Bled](https://www.slovenia.info/en/places-to-go/regions/alpine-slovenia/bled)
- [Original Maspalomas licensed coastal-dune photo by Marco Canepa / Unsplash](https://unsplash.com/photos/a-woman-standing-on-top-of-a-sand-dune-jh5IfdfYR08)
- [Original licensed Labuan Bajo sunset photo by Dhiemas Afif Febriyan / Unsplash](https://unsplash.com/photos/the-sun-is-setting-over-a-mountain-with-clouds-in-the-sky-19mkRL4HN-I)
- Original source photo licence and actual subject for revised Lake Bled: [Haonan Wei / Unsplash](https://unsplash.com/photos/lake-with-island-church-and-distant-mountains-at-sunrise-tgGaBnsH7Cg)

## Resolution of the weak-photo opportunity
The weak repeated Dune du Pilat image was **actually replaced** by a distinct verified Maspalomas coast photograph. Two proposed alternatives were rejected after reviewing real rendered images; do not resurrect them. The final original image, credit and on-slide description were checked at full output size. This change is included in the live Metricool booking and the 20-post allowance was unaffected.

## Final scheduling audit
As of the successful live Metricool audit: **14/20 November posts**, **7 published, 7 pending, 6 unused**. The seven upcoming dates remain unchanged, with exactly **six real swipeable multi-image carousel POSTS and one authentic video REEL**, all `autoPublish=true` and `draft=false`. Owner requests the next production manually on Tuesday 24 November. No ChatGPT scheduled Atlas tasks have been created or re-enabled.
