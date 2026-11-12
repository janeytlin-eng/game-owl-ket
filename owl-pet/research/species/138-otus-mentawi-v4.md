# #138 *Otus mentawi* v4 — research and design boundary

- batch: `20261107T012800+0800`, cycle `1/6`
- run: `20261107T012800+0800-cycle-1`
- accessed: 2026-11-07
- action: SCIENCE_REVISION / complete-image archive repair
- prior concepts preserved: v1, v2, v3
- target: v4
- scientific approval: false

## Why this revision is selected

The current main tree is complete and non-truncated, but the v3 concept, generated master and reviewed master are each exactly 700,000 bytes. That repeated hard boundary is treated as evidence of historical connector truncation, so v3 is not reused as a complete image asset. v4 must be regenerated, viewed and archived with an exact blob/byte readback.

## Taxonomy

Current valid name: *Otus mentawi* Chasen & Kloss, 1926. ITIS TSN 555383 lists historical *Otus bakkamoena mentawi* as a synonym. The repository roster ID and 251-species scope do not change.

## Evidence actually read

1. `MEN-TAUFIQURRAHMAN-2018-P31-32`: complete BirdingASIA printed pp.31–32, including dated juvenile photographs/captions and text.
2. `MEN-MIKKOLA-2013-P166-167`: user-uploaded Heimo Mikkola guide, PDF pages 168–169 / printed pp.166–167.
3. `MEN-ITIS-555383-2026`: current-name and synonym record.
4. `MEN-CHASEN-KLOSS-1926-DOI`: publisher metadata only; full species text unavailable, therefore not used for morphology.

## Source facts and design boundary

- Adult identity: compact rufous-morph owl about 20 cm; modest ear tufts; dark reddish-brown/chestnut adults; no pale nuchal collar; whitish-and-black scapular row; mottled coverts; herringbone/white-ocellus underparts; brown eyes selected from a documented brown-or-yellow range; yellowish-horn bill; tarsi feathered to toe bases; bare flesh-grey toes and dark claws.
- Sex: Mikkola explicitly reports no data on sexual size differences. Both adults stay near-equal in apparent standing height; pose asymmetry is allowed, a fixed female-larger rule is not.
- Juvenile stage: use the dated 18–21 May 2017 branch-using stage, not an unseen newborn. Slightly smaller; pale greyish-brown thin-streaked below, darker above, reddish-brown face/eyes, pale greyish-horn bill/toes, short dark tail and formed folded wings projecting beyond it with faint narrow bars.
- Behaviour/support: the field paper reports juveniles calling from lower branches, sometimes 2–3 m above ground. The plate may show secure low-branch support, but must not infer continuous flight competence.
- Environment: lowland rainforest and village/secondary-growth edge are supported. No nest or eggs are asserted.
- Unknown: exact hatch date, independent flight ability, complete feather chronology, population sex ratio, pair-specific size ratio and universal nest type.

## Complete imagegen prompt

Use case: scientific-educational
Asset type: owl-pet species concept plate, landscape 1536×1024
Primary request: Create a warm, tactile, hand-sculpted 3D game-character concept plate for #138 Mentawai Scops Owl, Otus mentawi, matching the established owl-pet diorama style.
Scene/backdrop: humid lowland village-edge rainforest on Siberut with natural rambutan branches, soft moss and foliage; no nest, no eggs.
Subject: exactly three owls and no extra birds. Left “ADULT MALE”, center “ADULT FEMALE”, right “JUVENILE · AGE UNKNOWN”.
Adults: compact ~20 cm rufous-morph scops owls with modest dark mottled ear tufts, dark reddish-brown/chestnut upperparts, no pale nuchal collar, distinct whitish-and-black outer scapular row, mottled dark-brown wing coverts, reddish-brown/chestnut underparts with fine herringbone markings and scattered paired white ocelli, subtly paler belly, warm brown irises, yellowish-horn bills, tarsi fully feathered to the toe bases, bare flesh-grey toes and dark horn claws. Keep male and female near-equal standing height because no sex-size direction is documented; distinguish them by natural pose only.
Juvenile: use the photographed 18–21 May 2017 branch-using stage, slightly smaller than adults and securely supported on a lower branch with both feet visible. Pale greyish-brown underparts with thin dark streaks, darker upperparts, reddish-brown face and eyes, pale greyish-horn bill/toes, short dark tail, formed folded wings visibly projecting beyond the tail with faint narrow bars. It is not a down-only hatchling and is not a miniature fully mature adult.
Composition/framing: one coherent landscape character sheet, adults left/center and juvenile right, all feet naturally supported, readable anatomy, no overlapping characters that hides the juvenile wing-to-tail relation.
Lighting/mood: warm diffuse humid-forest light, friendly but scientifically restrained.
Text (verbatim): “#138 MENTAWAI SCOPS OWL”; “Otus mentawi”; “ADULT MALE”; “ADULT FEMALE”; “JUVENILE · AGE UNKNOWN”.
Constraints: preserve exact three-character count and labels; no fixed female-larger claim; no exact juvenile day age; no flight-skill claim; no nest claim; no mature adult herringbone/ocelli transferred wholesale to the juvenile; no unsupported yellow juvenile iris.
Avoid: extra birds, eggs, nest cavity, human objects, unsupported size dimorphism, floating feet, long fully adult juvenile tail, adult-length heavily patterned juvenile remiges, white periocular goggles, grey adult bills, watermark or extra text.

## Review checklist

- exact title, subtitle, three role labels and exactly three owls
- adult brown eyes and yellowish-horn bills; no grey-bill regression
- adults near-equal; no unsupported sex-size claim
- feathered adult tarsi, bare toes, natural two-foot support
- juvenile slightly smaller, branch-supported and not a generic miniature adult
- juvenile pale thin-streaked underparts, darker upperparts and reddish face/eyes
- formed folded wing beyond short dark tail, but no adult-heavy herringbone/ocelli
- no exact age, flight claim, nest, eggs or extra birds
- open full image and juvenile/adults-support crops after generation
