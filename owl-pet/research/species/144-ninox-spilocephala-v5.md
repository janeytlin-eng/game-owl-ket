# #144 *Ninox spilocephala* v5 research and design boundary

- Batch / cycle: `20261031T2128+0800` / 5 of 6
- Action: `ARCHIVE_REPAIR_AND_SCIENCE_REVISION`
- Research ready: 2026-10-31T22:54:00+08:00
- Current name: *Ninox spilocephala* Tweeddale, 1879 (Mindanao Boobook)
- Historical crosswalk: *Ninox philippensis spilocephala*
- Recoverable visual base: intact v3 blob `ae4dc3a63da40c8c3d4af13003ed2f3be76dd4b0`; current-main v4 blob is only 786,444 bytes and is not treated as a complete original.

## Sources actually read or reused

### LZBO-RASMUSSEN-2012-LEAD — reused and fully refreshed

Rasmussen et al., “Vocal Divergence and New Species in the Philippine Hawk Owl *Ninox philippensis* Complex,” *Forktail* 28 (2012):1–20, https://www.asianscientist.com/wp-content/uploads/2012/08/Vocal-divergence-and-new-species.pdf . The complete PDF was opened and the specimen methods, diagnosis and range text were read. The study examined 177 specimens, including 43 *spilocephala*. Because most key specimens were not sexed, the authors combined sexes and explicitly left sexual dimorphism for future study. For adults the diagnosis supports a small, compact, short-tailed owl; a tiny or absent white patch between eye and supercilium; long filamentous auricular extensions; buff spotting strong on crown/nape/upper mantle and weaker down the mantle; large white spots or narrow buff bars on wing coverts; a narrow whitish throat with dark shafts; weak bars/spots on neck and breast with the central breast mostly streaked; pale lower underparts with irregular longitudinal dark marks and chevron tips; pale-yellow irides, pale-olive bill/cere and bright-yellow feet with mostly black claws. The immature diagnosis is limited to an unspotted brown crown and a weak pale-buff-spotted upper-mantle collar. The paper does not give exact age, independent flight ability or a complete feather sequence. Current range in the diagnosis is Mindanao, Dinagat, Siargao and Basilan.

### MINBOO-ITIS-2025 — new taxonomy crosswalk

Integrated Taxonomic Information System, standard report for *Ninox spilocephala*, live record opened 2026-10-31: https://www.itis.gov/servlet/SingleRpt/SingleRpt?search_topic=TSN&search_value=1178395 . The record treats *Ninox spilocephala* Tweeddale, 1879 as valid and maps the historical synonym *Ninox philippensis spilocephala*. This source is used only for the current/old-name crosswalk, not morphology or development.

### MINBOO-EBIRD-ID-2026 and MINBOO-AVIBASE-TAXON-2026 — reused project records

The existing project records were reused only as secondary adult identification and name/range checks. They do not close the juvenile-age, locomotor or sex-dimorphism gaps.

### PH-REDLIST-MINBOO-LEAD — unverified lead, not evidence credit

A search result located the Philippine Red List account, but the original PDF timed out during this cycle. Its search snippet is not counted as verified evidence and is not used to assert morphology, sex, development or habitat.

## Evidence boundary and design decisions

- Adult male and female are displayed at near-equal skeletal height. No fixed female-larger or male-larger rule is asserted.
- Adults retain the species-specific compact, short-tailed outline, pale-yellow irides, pale-olive bill/cere, yellow feet, dark claws, adult crown/nape spotting and mixed streak/bar underpart diagnosis.
- The central young bird is explicitly “older immature · age unknown.” Only the plain brown crown and weak buff-spotted upper-mantle collar are diagnostic evidence. Its compact formed wing is kept mostly covered; it grips one continuous branch with both feet. No flight claim, day age, nest, iris chronology or mature juvenile remiges are asserted.
- Long auricular filaments are cheek/ear-covert feathers, not ear tufts.
- v5 repairs the incomplete current v4 original and corrects v3's adults, where white rises too high on the chest, plus the too-adult-looking central bird.
- Scientific status remains `false`; review target is `PASS_WITH_LIMITATIONS`.

## Full ImageGen edit prompt

```text
Use case: precise-object-edit / stylized scientific concept. Edit the supplied intact landscape #144 Mindanao Boobook plate into version 5 while preserving the established soft rounded 3D electronic-pet style, 1536×1024 landscape layout, humid Mindanao forest lighting, exactly three birds, one continuous mossy support branch, and the title “144 MINDANAO BOOBOOK · Ninox spilocephala”. Keep labels ADULT MALE at left, OLDER IMMATURE · AGE UNKNOWN in the center, and ADULT FEMALE at right.

Adult male and female: show near-equal skeletal height and mass; do not impose a female-larger rule. Both are small compact earless owls with short tails. Long fine filamentous auricular/ear-covert extensions may feather outward beside the facial disc like subtle whiskery cheek feathers, but they must NOT become ear tufts or horns. Irides pale yellow; bill and cere pale olive, slightly yellower along the culmen; feet bright yellow with mostly black claws. Adult crown, nape and upper mantle have many small evenly distributed buff spots that weaken farther down the mantle. Wing coverts show naturally irregular large white spots and narrow buff bars. The upper chest must remain reddish-brown with weak disorganized bars, mottling and longitudinal shaft marks; do NOT place a clean white chest patch. Restrict whitish ground to the lower belly and flanks, overlaid by irregular longitudinal reddish-brown/dark marks with occasional broken or chevron-like tips, never a repeated wallpaper pattern. Preserve secure natural branch grip.

Center older immature, exact age and flight ability unknown: keep it smaller and softer, with an unspotted plain brown crown and only a weak collar of pale-buff spots on the upper mantle; no adult crown spots and no adult chest pattern. Give it a compact short rounded formed wing mostly covered by soft body plumage and foliage, and a short mostly hidden tail, avoiding crisp mature remiges or a miniature-adult silhouette. Show both feet naturally gripping the same continuous mossy branch so the body is visibly supported. It may rest quietly with closed or downcast eyes, but do not claim a particular iris stage. No hatchling anatomy, no flight action, no nest, eggs or invented age.

Preserve readable text and the three-character composition. No extra birds, no duplicated limbs, no floating feet, no watermarks, no invented cavity or nest material. Adult diagnostic correction and juvenile evidence-bounded support are more important than decorative detail.
```

## Source delta

- New verified source IDs: 1 (`MINBOO-ITIS-2025`)
- Reused source IDs: 3 (`LZBO-RASMUSSEN-2012-LEAD`, `MINBOO-EBIRD-ID-2026`, `MINBOO-AVIBASE-TAXON-2026`)
- Corrected records: 1 archive-integrity correction (v4 current blob is incomplete; no biological source fact overwritten)
- Unverified leads: 1 (`PH-REDLIST-MINBOO-LEAD`)

