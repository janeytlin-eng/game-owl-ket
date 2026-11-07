# #26 *Glaucidium siju* v5 — juvenal-stage inference correction

- Research date: 2026-11-07 (Asia/Shanghai)
- Action: non-destructive science revision; v1–v4 preserved
- Scientific verification: false

## Repository issue selected

V4 is a reviewed full-size concept but fixes the young bird to a palm-cavity threshold. The directly read primary ageing paper does not establish a cavity-stage day-age, flight threshold, or nest position for its “juveniles”; it describes juvenal body plumage across hatching-year birds. Treating the plumage account as a cavity nestling is therefore an unsupported design inference. V5 removes that inference.

The three live manifests also disagree: `design/image-manifest.json` contains v4, while `design/IMAGE_MANIFEST.json` and `production/IMAGE_MANIFEST.json` stop at v3. V5 will reconcile the live manifests while preserving all prior versions.

## Sources actually read

### CUPO-PYLE-ETAL-2004-JFO — reused primary study, freshly reread
- Title: “Molt patterns and age and sex determination of selected southeastern Cuban landbirds”
- Authors: Peter Pyle et al.; Institute for Bird Populations
- Year/type: 2004; peer-reviewed primary banding/specimen study
- URL: https://www.birdpop.org/docs/pubs/Pyle_et_al_2004_Molt_Patterns_and_Age_and_Sex_Determ_of_Selected_SE_Cuban_Birds.pdf
- Pages: printed pp.136–145; *G. siju* account printed p.138 / PDF p.3
- Scope: 48 individuals, 127 captures and 41 specimens; wider methods include USNM series and recaptures.
- Facts: juveniles have downy plumage, unmarked backs, streaked underparts and indistinct crown spots; adults bright yellow-eyed versus possibly duller HY eyes is explicitly tentative. Female wing 95–101 mm and reddish brown; male 84–94 mm and grayish brown, with reddish-tinged males.
- Boundary: HY is calendar ageing, not a precise developmental day. No cavity-stage posture, juvenile sex, first-flight threshold, exact wing/tail length or definitive iris chronology.
- Design use: quiet supported age-unknown juvenile in juvenal body plumage; no nest-stage or flight claim. Adult female direction is subtle and not absolute.

### CUPO-GARRIDO-2002 — reused primary museum series, freshly reread
- Title: “Subespecie nueva de sijú platanero (*Glaucidium siju*) para Cuba”
- Author: Orlando H. Garrido
- Year/type: 2002; primary taxonomic museum study
- URL: https://caribbeanagroup.org/wp-content/uploads/2022/07/10Glaucidium.pdf
- Pages: printed pp.45–52; specimen coverage pp.47–50; measurements p.48 and Table 1
- Scope: 152 specimens across Cuba and U.S. museums.
- Facts: geographic pattern/colour variation is real; *turquinensis* is darker and less spotted, *vittatum* larger/more spotted. The paper gives adult measurement direction but no juvenile development.
- Boundary: do not mix subspecies extremes or convert museum means into a rigid displayed-height ratio.
- Design use: generic lowland species direction without assigning a race; restrained female fullness.

### CUPO-SMITHSONIAN-VITTATUM-TYPE-2024 — unverified visual lead
- Institution: Smithsonian NMNH
- URL: https://www.si.edu/es/object/glaucidium-siju-vittatum-ridgway:nmnhvz_4027353
- Search record identifies an adult male *G. s. vittatum* type specimen from Isla de la Juventud, collected 30 June 1900, with public-domain media.
- Direct page retrieval returned 404 in this run, so the media was not used as visual evidence.

## Design correction

Problem: v4’s downy young at a cavity threshold implied a precise nest stage not supported by Pyle’s calendar-age account.
Evidence: Pyle’s account supports juvenal plumage characters but not day-age, flight ability, nest location or fixed wing/tail geometry.
Modification planned: v5 shows a low, fully supported, quiet age-unknown juvenile on a broad living branch; plain back, streaked underparts and indistinct crown flecks remain, but no nest-stage or flight claim is made. Wing/tail remain soft and subordinate rather than being erased or rendered adult-hard.
Unknowns retained: exact age, sex, iris chronology, first-flight threshold, race and individual colour overlap.

## Source accounting

New verified sources: 0. Freshly reread/reused: 2. New unverified lead: 1. Corrected design inference: 1. Mikkola upload was unavailable; no new page claim is made.

## Complete imagegen prompt

Use case: scientific-educational
Asset type: owl-pet three-stage species concept plate
Primary request: create a scientifically bounded v5 concept plate for #26 Cuban Pygmy-Owl, preserving the established owl-pet visual language while correcting the unsupported v4 cavity-stage inference.
Scene/backdrop: semi-open lowland Cuban woodland edge with palms and native-looking leafy branches; a dark old cavity may appear in the distant trunk as habitat context only, but the juvenile is not at a nest and no nest contents are visible.
Subject: exactly three *Glaucidium siju*. Left ADULT MALE: small round untufted head, grayish-brown upperparts with irregular small pale spots, yellow eyes, pale greenish-horn bill/cere, off-white underparts with brown-ochre longitudinal streaks, feathered tarsi and naturally gripping toes, brown-gray barred tail. Centre JUVENILE: age and sex unknown, in juvenal body plumage, soft downy rounded contour, plain unmarked warm gray-brown back, streaked underparts, only indistinct crown flecks, dull indeterminate iris rather than adult-bright yellow; quiet low posture on a broad living branch, both feet fully supported, no begging, flight or nest-stage claim; folded wing and tail present but visually soft and subordinate, without crisp adult white spot rows or a long sharply barred adult tail. Right ADULT FEMALE: reddish-brown, subtly fuller and slightly longer-winged than the male but near the same displayed crown height; yellow eye and species pattern; three-quarter turn showing one white-bordered dark nape false-eye patch.
Style/medium: naturalistic softly painted 3D wildlife field-guide concept art, anatomically credible, realistic feather texture, consistent with prior owl-pet plates.
Composition/framing: 1536×1024 landscape; three birds fully separated and fully visible; adults flank juvenile; all feet and supports visible; calm sentinel adults, juvenile low and secure.
Lighting/mood: restrained warm filtered woodland light; clear diagnostic colour without theatrical saturation.
Text (verbatim): "26 CUBAN PYGMY-OWL" at top; italic-style subtitle "Glaucidium siju"; labels "ADULT MALE", "JUVENILE", "ADULT FEMALE" below the corresponding birds.
Constraints: exact three birds; preserve near-equal adult displayed height; female colour/size direction is population-level and not a rigid individual rule; juvenile is calendar-age-unknown and must not be presented as a hatchling or confidently flying fledgling; no precise iris-age claim.
Avoid: ear tufts, extra birds, eggs, prey, visible nest lining, invented hatchling detail, adult-like juvenile wing spot rows, long adult-barred juvenile tail, unsupported hovering, malformed or hidden support feet, vegetation intersecting bodies, extra text, watermark.
