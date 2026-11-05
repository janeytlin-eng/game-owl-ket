# #78 *Asio capensis* v5 research and design boundary

- Run: `20261106T003403+0800-cycle-2`; batch `20261105T233209+0800`, cycle 2/6.
- Action: `SCIENCE_REVISION`; v1–v4 preserved.
- Current name: *Asio capensis* (Smith, 1834). Original combination *Otus capensis* is retained as a historical-name mapping, not substituted in the title.
- Selected stage: age-unknown down-rich owlet documented in a directly opened species-identified photograph. No exact hatch age, juvenile sex, flight ability or daily feather chronology is inferred.
- Scientific status: false.

## Sources actually opened and read on 2026-11-06

### MAR-COMMONS-MURRAY-2020 — new visual source

Danelle Murray, “Baby Marsh Owls,” photograph dated 18 April 2020, Wikimedia Commons file page and original image opened at full size: https://commons.wikimedia.org/wiki/File:Baby_Marsh_Owls.jpg

Facts visible in the source: two Marsh Owl young sit low in tall grass. Both have buff-brown woolly down, very dark facial masks/discs, dark irides and black bills. Darker emerging feather areas are visible around the shoulders/back, while the wings and tails are mostly concealed by down, body position and vegetation.

Limits: the file provides no age, locality, sex, scale, measured feather sequence or action test. Grass hides parts of the feet and wings. It supports an age-unknown down-rich, naturally grass-supported young, not an exact day label, adult-style wing geometry or a flight claim.

### MAR-ANSARA-ROSS-2008 — primary morphometrics re-read

Ansara-Ross, Waller, Hockey & Oatley, “Sexing Marsh Owls *Asio capensis* using morphological measurements,” *Ostrich* 79(1), DOI `10.2989/OSTRICH.2008.79.1.11.366`. Publisher abstract and indexed full-text table/method excerpt re-read.

Facts: in the Gauteng sample, males averaged 297.59 g and 148.8 mm tail (n=21); females 329.07 g and 156.3 mm tail (n=11). Mass and tail differed, while mean flattened wing length was almost identical; no dichromatic sex distinction was found.

Boundary: encode only a restrained female fullness and subtly longer tail direction. Do not impose a fixed standing-height ratio, universal female-larger rule or sex-specific colour.

### MARSH-BIOEXP-2026 and MARSH-OWLPAGES-2020 — development/habitat re-read

The Biodiversity Explorer/Roberts synthesis and Owl Pages species account were opened. They converge that young leave the ground depression around 14–18 days while still downy and move/crawl into nearby cover before later fledging around 29–35 days. The Owl Pages account also states full feathering much later, around 70 days.

Boundary: these summaries support ground/grass dependence and a long transition, but do not assign the Commons owlets an age. V5 therefore uses the photograph-controlled “AGE-UNKNOWN OWLET” and a low, fully supported posture; no walking, wing exercise, flight or day-specific plumage is claimed.

### WHSO-MIKKOLA-2013 — repository extraction reused

The repository's earlier extraction records printed pp.518–519 / PDF pp.520–521 for adult and juvenile appearance. The uploaded guide itself was not mounted in this run, so no fresh page transcription is claimed. It is used only as a prior morphology cross-check.

## Design decision

- Adults: dark brown eyes; pale buff facial disc with dark rim; blackish horn bill; tiny ear tufts; plain earth-brown upperparts; buff underparts with fine dark vertical streaking. Adults remain comparable in crown height; female only subtly fuller with a slightly longer visible tail.
- Juvenile: age-unknown down-rich owlet based on the opened Commons photograph—buff-brown woolly down, very dark face/disc, dark eyes and black bill, with restrained darker emerging shoulder/back feather areas. Wings and tail remain mostly concealed and must not display mature layered remiges or repeated adult pattern rows.
- Support/action: juvenile sits low in tall grass with both feet/ground contact naturally supported, partly obscured by vegetation if necessary. No takeoff, walking, wing display or flight claim.
- Habitat: open wet grassland/marsh edge with tall grass and shallow water in the middle distance; no nest, eggs or prey.

## Full imagegen prompt

```text
Use case: scientific-educational
Asset type: owl-pet species concept plate, horizontal 3:2
Input image: Image 1 is the v4 style, adult-identity and layout reference. Preserve its painterly-realistic, gently rounded owl-pet finish, warm natural light and readable three-subject composition, but replace the central older juvenile with the evidence-bounded down-rich owlet described below.
Primary request: exactly three full-body Marsh Owls: left adult male, center age-unknown down-rich owlet, right adult female.
Scene/backdrop: open African wet grassland/marsh edge with tall tawny-green grass, a narrow shallow-water band in the middle distance and soft muted sky; no nest, eggs or prey. Adults and young must have coherent natural support.
Text (verbatim): top line “78 MARSH OWL”; second italic serif line “Asio capensis”; bottom labels “ADULT MALE”, “AGE-UNKNOWN OWLET”, “ADULT FEMALE”. No other text.
Adults: dark brown irises, pale buff facial discs with clear dark rims, blackish horn bills, tiny subtle ear tufts, earth-brown upperparts and buff underparts with fine dark vertical streaking. Keep adult crown heights comparable; the female may be only subtly fuller with a slightly longer visible tail, not generically much larger. Give the two adults distinct calm head/stance directions. Both feet of each adult must be visibly and anatomically supported on low natural earth/grass hummocks.
Central owlet: reproduce the directly photographed age-unknown visual stage without assigning a day: compact low body in tall grass, buff-brown woolly down, very dark facial mask/disc, dark irises and black bill, with only restrained darker emerging feather patches around shoulders and upper back. Keep wings and tail mostly concealed by down/body/grass; do not show long layered remiges, a mature barred tail or repeated adult-perfect pattern rows. The owlet is resting/sitting low, both feet and abdomen naturally supported by the ground and grass, not walking or displaying wings.
Constraints: exact number/title/order; exactly three owls; no generic female-much-larger rule; no orange/yellow adult eyes; no adult-perfect juvenile wing; no exact-age label; no hovering, airborne pose or unsupported feet; no extra birds, prey, eggs, logo, border or watermark.
```

## Review gates and unknowns

- Verify exact three birds/text/order; adult dark eyes/tiny tufts/dark-rimmed pale discs; comparable adult height; restrained female fullness/tail; juvenile dark face/dark eyes/down-rich body/concealed wings and tail; continuous ground/grass support.
- Unknown: photographed juveniles' age, sex, location, exact feather geometry and action ability; universal sex ratio; subspecies-specific proportions; daily developmental sequence. These prevent scientific approval.

## Production result

- Initial generation passed the count/text, adult identity and restrained sex-direction gates. The central `AGE-UNKNOWN OWLET` is down-rich and dark-faced with mostly concealed wing/tail and bilateral ground/grass support.
- Full image and juvenile/support crops were actually opened. No edit was scientifically necessary; edit count 0.
- Concept/reviewed master: 1536×1024 RGB PNG, 2,922,411 bytes; SHA-256 `ad3ed1912b94bb58bf27a1230843c2aeef50ccb0579ac4a319dd0dd106793461`.
- Review: `research/reviews/78-asio-capensis-v5-review.md`; result `PASS_WITH_LIMITATIONS`; scientific status remains false.

