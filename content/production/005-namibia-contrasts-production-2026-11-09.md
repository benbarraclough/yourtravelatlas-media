# Namibia 005 — Stage 2 successful production, 9 November 2026

**RENDERED_PENDING_QA**, not yet approved or scheduled. Fixed the previous media shortcomings with seven new exact-location images individually marked free under the Unsplash License, drawn from live photographer pages.

## Completed evidence
- [Actual seven-slide manifest](../../media/005-namibia-contrasts/manifest.json) and [JPEGs](../../media/005-namibia-contrasts)
- [Successful GitHub Actions render](https://github.com/benbarraclough/yourtravelatlas-media/actions/runs/42696283143); output includes seven 1080×1350 JPEGs, source and output SHA-256 per slide, brief SHA-256 and empty `review/render-errors.json`
- [Production brief](../posts/005-namibia-contrasts.json), compact ~701-character caption and real photo source pages + exact locations for every featured place

## Actual replacements
1. Sandwich Harbour coast and dunes — NIR HIMI, https://unsplash.com/photos/vast-sand-dunes-meet-the-ocean-under-a-clear-sky-NOx4oaU7fC0
2. Deadvlei trees and clay pan — NIR HIMI, https://unsplash.com/photos/a-solitary-dead-tree-in-a-vast-desert-landscape-mLt7b8QuQc8
3. Spitzkoppe rock arch — NIR HIMI, https://unsplash.com/photos/natural-rock-arch-framing-desert-mountains-and-sky-ssA-63h1c4o
4. Kolmanskop sand-filled interior — Francesco Ungaro, https://unsplash.com/photos/sand-floods-an-abandoned-room-with-sunlight-LfymQDuUXoc
5. Cape Cross fur seals — Wietse Jongsma, https://unsplash.com/photos/a-large-group-of-animals-laying-on-top-of-a-beach-eolDN8CCeso
6. Etosha elephant herd at waterhole — Nadine Marfurt, https://unsplash.com/photos/a-herd-of-elephants-gathered-at-a-watering-hole-a1ifB4-gECQ
7. Sandwich Harbour sunset dune walkers CTA — Nathalie Lays, https://unsplash.com/photos/people-walking-on-sand-dunes-at-sunset-WrVcWCADrtY

Full seven actual final images have been viewed at 1080x1350 during Stage 2. **No automatic QA PASS**: the separate Stage 3 editorial reviewer must independently challenge weak slide, rights, truthful locations, cover/copy contrast and spacing. The cover now visibly includes sea, and Kolmanskop shows sand-filled interior rather than a facade. Cape Cross shot has backlit grey spray; review whether dramatic enough. Footer and source credits legible in full resolution. No public numbers/music.

First render run https://github.com/benbarraclough/yourtravelatlas-media/actions/runs/42696108756 failed because new brief omitted `activity_source` references required by the renderer; corrected and rerun successfully. Preserve this as an actionable schema preflight failure. The actual photo images are free licensed and accessible to renderer; old invalid BY-SA/weak candidates are abandoned.

**Handoff:** QA full seven gates, then schedule and re-fetch Metricool. Only label SCHEDULED when confirmed PENDING.
