# #164 Desert Owl — *Strix hadorami*

- Project ID: 164
- Version: v1
- Current taxonomy: *Strix hadorami* Kirwan, Schweizer & Copete, 2015
- Historical source mapping: Mikkola (2013) `Strix butleri` account mainly describes the widespread Levant–Arabia population now assigned to *S. hadorami*; current *S. butleri* is Omani Owl.
- Production status: VERIFIED archive; scientific calibration pending
- Scientific status: pending

## Evidence facts

- Adult: round-headed and untufted; pale uniform sandy-gray disc; sandy ochre/gray upperparts; pale scapular row and restrained wing spots; barred flight feathers/tail; pale underparts with light rufous cross-barring; warm yellow to brownish-orange eyes; gray-blue bill and pale cere.
- Sex: no pronounced dimorphism in the 2015 specimen study; females average only slightly larger, so show fullness only.
- Juvenile stage selected: age-unknown very pale mesoptile, yellowish eyes and weaker talons; fully ledge-supported, no inferred flight.
- Habitat/nest context: rocky semi-desert wadi; a sheltered cliff crevice is supported by current institutional synthesis.
- Unknown: exact age, iris chronology, continuous feather sequence, wing/tail readiness, flight threshold, exact crevice geometry, quantified universal sex ratio and geographic variation.

## Design decision

Use exactly three labeled birds on one continuous sandstone ledge system. Keep adults near-equal and show the juvenile as a pale fluffy, short-winged, fully supported mesoptile. Do not import the bicolored face/long-streaked underparts of current Omani Owl *S. butleri*.

## Sources

See stable IDs `DEOW-MIKKOLA-2013-P318`, `DEOW-KIRWAN-2015`, `DEOW-IOC-2015-SPLIT`, and `DEOW-EBIRD-2026` in [SOURCE_INDEX.md](../SOURCE_INDEX.md).

## Review result

- First render failed the juvenile-wing check because it carried adult-style bars/spots and hard layered remiges.
- One targeted edit produced a short rounded down-covered wing, concealed tail and weaker supported talons; title, adult diagnosis, sex boundary and wadi context remained intact.
- Visual review: PASS; scientific verification remains pending.

## Linked production

- [Cycle 5 run](../../production/runs/2026-10-27T1335+0800-cycle-5.md)


## v2 science revision — 2026-10-28

### Problem → evidence → correction
- **Problem:** v1’s evidence table correctly marked exact juvenile iris chronology unknown, but its saved prompt nevertheless requested “yellowish eyes,” and the image rendered a conspicuous adult-like yellow-orange iris.
- **Evidence:** Ben Dov et al. (2017), *Dutch Birding* 39:285–307, supplies current-species nest shelf, first-flight and later fledgling milestones plus real plate captions, but does not establish juvenile iris colour. Mikkola printed pp.318–319 / PDF pp.320–321 remains the bounded source for a very pale mesoptile under the historical *S. butleri* account now mapped to *S. hadorami*.
- **Correction:** v2 keeps the pale, fully supported mesoptile and wadi ledge context, but changes the juvenile eyes to a neutral dark-to-gray-amber shaded uncertainty treatment; it explicitly prohibits bright adult-yellow, crisp adult wing bars and mature hard wing/tail geometry.
- **Candidate audit:** #165 *Ninox punctulata* v2 was withdrawn before generation because Mikkola explicitly says its mesoptile wing and tail feathers are as adult; that species-specific exception invalidated the initial visual concern.

### Development and action boundary
The primary study reports partly open eyes at about day 7, fully open at day 9, wing-flapping at 20–25 days, standing on the nest shelf around day 25, first flight around day 30, leaving the nest site around day 34, and body feathers appearing at 70–75 days. These observations support a natural rock-ledge setting and caution against universal flightlessness, but v2 does not assign an exact age to the Mikkola-based pale mesoptile.

### Full imagegen prompt

Create a polished 3:2 landscape zoological concept plate in the repository's established warm, painterly realistic owl-pet style. Exact title at the top: “DESERT OWL · Strix hadorami”. Exactly three birds, no extra birds. Exact small labels below birds: left “ADULT MALE”, center “PALE MESOPTILE JUVENILE”, right “ADULT FEMALE”.

Show one continuous rocky semi-desert wadi at warm dusk: sandstone cliff ledges, a sheltered natural crevice and sparse dry scrub. The three birds must share one connected ledge system with believable feet and support. Do not show eggs, a fabricated cavity interior, human objects, specimen panels or split frames.

Adults: medium-sized round-headed owls with no ear tufts; pale sandy-gray facial discs with subtle dark rims; warm yellow to brownish-orange adult irises; gray-blue bills and pale ceres; sandy ochre-gray upperparts with a restrained pale scapular row and irregular small wing marks; barred flight feathers and tail; pale underparts with light rufous-brown cross-barring. Feathered tarsi, natural toes and claws gripping rock. Male and female nearly equal in height; female only subtly fuller, never a fixed exaggerated larger ratio.

Center juvenile: an age-unknown very pale mesoptile juvenile, fluffy and distinctly softer than the adults, with a short rounded developing folded wing, concealed or very short tail, weaker smaller talons, and full belly/feet support on the rock ledge. IMPORTANT uncertainty rule: exact juvenile iris chronology is not documented in the sources read. Show the juvenile eyes softly shaded neutral dark brown to gray-amber in shadow, not bright adult-yellow and not a claim of a known fixed color. Do not give the juvenile crisp adult wing bars, long hard layered remiges, mature tail geometry, a flight pose or unsupported posture.

All three birds fully visible with complete feet/support, believable anatomy and distinct silhouettes. Natural irregular markings, no cloned symmetry, no cropped birds, no human objects, no text other than the exact title and three exact role labels, no logos or watermarks.

### Status
ARCHIVED; one targeted juvenile-wing edit passed original-resolution review. Independent commit-pinned readback is pending. Scientific verification remains false.


### v2 visual review
- First render: neutral shaded juvenile eye and rock support passed, but the juvenile carried long hard adult-barred remiges.
- Edit: only the juvenile wing/tail was changed to a short rounded down-covered wing with diffuse markings and concealed tail.
- Recheck: PASS at 1536×1024 for exact three-bird count/title/labels, adult identity, near-equal adult scale, neutral uncertainty treatment, smaller juvenile talons and continuous rock support. Science remains false.
