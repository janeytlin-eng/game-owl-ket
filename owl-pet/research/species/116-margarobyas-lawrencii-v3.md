# 116 Margarobyas lawrencii v3 research-ready record

- Batch/cycle: `2026-10-27T2126+0800` · 1/6
- Prepared: 2026-10-27T21:31:00.000+08:00
- Action: SCIENCE_REVISION of existing v2; unique-species increment 0
- Target: v2 still shows faint bright ivory teardrop-like crown tips; calibrate the older juvenile toward source-bounded sienna-brown mesoptile with fewer white spots.
- Source index: [SOURCE_INDEX.md](../SOURCE_INDEX.md)
- Reused source IDs: `CBLO-MIK2013-252`, `CBLO-SHERONY-2006`, `CBLO-SHARP-2016`, `CBLO-BOUGLOUAN-CARD`, `CBLO-AOU-2013A11`
- New source IDs: 0
- Corrected source IDs: 0

## Fresh research and deduplication

Fresh external search/read covered the Smithsonian repository record for Olson & Suárez (2008), the AOS 2013-A-11 proposal, BirdsCaribbean adult account, and public photo leads. These did not add a new juvenile morphology fact beyond the existing indexed evidence, so no duplicate source entry was created. Olson & Suárez supports the current genus/old-name mapping, not juvenile appearance.

The uploaded Heimo Mikkola file was located and pages 254–255 were requested in this invocation, but the Library page reader returned no readable content. The previously actually-read and indexed transcription under `CBLO-MIK2013-252` is reused; this record makes no new page-reading claim.

## Evidence boundary

- Source fact: adult has a round untufted head, dark brown iris, pale brows/face, gray-yellow bill, completely bare long yellow-brown tarsi/toes, cream-buff belly with dark shaft marks, and brown white-tipped upperparts.
- Source fact: mesoptile is broadly adult-like but less spotted above; the specialist account describes sienna upperparts/breast and a paler belly.
- Design inference: choose an age-unknown older supported mesoptile with formed compact wings; render the crown mostly sienna-brown with only sparse low-contrast tips. “Zero spots” is not claimed biologically.
- Unknown: exact age, flight ability, continuous feather sequence, fixed sex-size ratio, and exact crown feather map. Scientific verification remains false.

## Full imagegen prompt

```text
Use case: scientific-educational
Asset type: owl electronic-pet species concept plate in the established soft natural-history illustration style
Primary request: Create one landscape three-bird concept plate for #116 Bare-legged Owl, Margarobyas lawrencii, version 3. Exactly three birds: adult male on the left, an age-unknown older juvenile in the center, adult female on the right.
Scene: shaded Cuban forest at a deep natural tree-cavity entrance; all three birds naturally supported on a continuous cavity sill/branch. No woven nest, no grass cup.
Adult identity: small compact owls with round untufted heads, dark brown irises, pale eyebrows and subtle pale facial framing, gray-yellow bills, brown upperparts with irregular distinct white spots, cream-buff lowerparts with sparse irregular dark drop-shaped shaft streaks. Long yellow-brown tarsi and toes are completely bare, with visible natural grip and claws. Sexes are visually similar and near-equal in scale; do not invent fixed color or size dimorphism.
Juvenile: one age-unknown older mesoptile juvenile, supported with both feet, calm low crouch, formed but compact folded wings and modest tail. Sienna-brown upperparts and breast, paler belly; adult-like overall but clearly fewer white spots than adults. Crown and nape predominantly continuous sienna-brown with only sparse, tiny, low-contrast pale tips. Do not create bright ivory teardrops, pearls, rows, scallops or a spotted adult crown. Formed wings are allowed by the selected older stage; do not make it a hatchling or flying bird.
Composition: male left, juvenile center, female right; exactly three birds, fully visible faces and supported feet, clean spacing.
Lighting/mood: soft filtered forest light, calm observational mood.
Text (verbatim): title "BARE-LEGGED OWL"; subtitle "Margarobyas lawrencii"; labels "ADULT MALE", "OLDER JUVENILE — AGE UNKNOWN", "ADULT FEMALE".
Constraints: exact three-bird count; readable correct text; preserve bare tarsi/toes; no ear tufts; no yellow irises; no unsupported sex dimorphism; no extra bird or egg; no watermark.
Avoid: mechanical repeated feather geometry, bright juvenile crown teardrop rows, adult-density juvenile white spots, mature oversized juvenile remiges, floating feet, decorative nest basket.
```

## Planned review checks

Exact species/text/count; untufted dark-eyed adults; bare tarsi/toes and real support; near-equal adult scale; juvenile crown free of bright repeated teardrop rows; fewer juvenile white spots without erasing legitimate formed wings; no unsupported nest or age claim.


## Actual review result

The newly generated 1536×1024 RGB master was opened at original detail. All planned visible checks passed. In particular, the juvenile crown no longer has bright repeated ivory teardrop rows; only sparse low-contrast pale tips remain on a continuous sienna-brown base, consistent with the conservative “fewer white spots” boundary. No edit was required. This is a visual correction result, not proof of exact feather mapping or biological verification.


## Archive target

- Concept: `owl-pet/design/concepts/116-margarobyas-lawrencii-v3.png`
- Durable master: `owl-pet/production/assets/2026-10-27T2126+0800-cycle-1/generated-master.png`
- Git blob: `49d4e1e15d4f9edeaf056a9016dc73e6878835e4`
- SHA-256: `6f850d6e13b9bb6414820a8f6a37509c722efa9e0f2b61cfce06d9afa6a591d5`
- Independent commit-pinned readback pending at ARCHIVED stage.


## Independent verification

At 2026-10-27T21:42:00.000+08:00, archive commit `b9667425eed465cccce15ee20bcc535182c927c5` was fetched. The commit-pinned concept and durable master paths both resolve to expected Git blob `49d4e1e15d4f9edeaf056a9016dc73e6878835e4`; manifest, run, batch, species and research records were read back. The connector did not return the binary payload a second time, so this is recorded precisely as commit/path/blob identity verification, not a second byte-for-byte download.
