# #146 *Ninox mindorensis* v2 research and design boundary

- Batch / cycle: `20261031T2128+0800` / 6 of 6
- Action: `SCIENCE_REVISION`
- Research ready: 2026-10-31T23:48:00+08:00
- Current name: *Ninox mindorensis* Ogilvie-Grant, 1896 (Mindoro Boobook)
- Historical crosswalk: *Ninox philippensis mindorensis*; original protonym *Ninox mindorensis*.
- Existing v1 is preserved. Its bright-eyed “older juvenile” has long crisp adult-like barred remiges/tail unsupported by any species-specific developmental source read here.

## Sources actually read

### LZBO-RASMUSSEN-2012-LEAD — reused, species section freshly read

Rasmussen et al. 2012, “Vocal Divergence and New Species in the Philippine Hawk Owl *Ninox philippensis* Complex,” *Forktail* 28:1–20, https://www.asianscientist.com/wp-content/uploads/2012/08/Vocal-divergence-and-new-species.pdf . Complete PDF reopened 2026-10-31; *mindorensis* diagnosis on printed p.13 / PDF p.13, relationship text p.17 and habitat discussion p.18 read. Adults are small, with small bill and mostly feathered tarsus; small short white supercilia; pale-brown small facial disk with short filamentous auricular extensions; crown/nape finely broken-barred dark brown and buff/whitish; extensive white scapular patches; extensively finely barred wing coverts; tawny-buff underparts with especially narrow fine dark bars; mustard-yellow inner iris ring and lemon-yellow outer ring; pale dull-yellow/greenish bill/cere; dull olive-yellow tarsi/toes and black claws. The paper does not give a species-specific immature diagnosis, age, iris chronology, locomotor ability or feather sequence. It locates the species in Mindoro forest, including lowland Sablayan and Mt Halcon at 1,150–1,250 m.

### MINDBOO-ITIS-2025 — new

ITIS standard report TSN 1063265, https://www.itis.gov/servlet/SingleRpt/SingleRpt?search_topic=TSN&search_value=1063265 , opened 2026-10-31. It treats *Ninox mindorensis* as valid and maps synonym *Ninox philippensis mindorensis*. Used only for current/old-name crosswalk.

### MINDBOO-CLEMENTS-2013 — new

Cornell/eBird Clements 2013 update, https://www.birds.cornell.edu/clementschecklist/introduction/updateindex/overview-august-2013/updates-and-corrections-august-2013/ , lines around the Philippine boobook split read 2026-10-31. It follows Rasmussen et al., elevates Mindoro Boobook and maps former *N. philippensis mindorensis* to Mindoro. Used for checklist crosswalk/range, not plumage or development.

### MINDBOO-OGILVIE-1896-LEAD — unverified primary lead

Avibase/ITIS link the original description to Ogilvie-Grant 1896, *Ibis* 7(2):457–477, p.463, BHL https://www.biodiversitylibrary.org/item/55020#page/519/mode/1up . BHL returned 403 in this run, so the original page was not counted as read. Rasmussen's paper quotes its adult comparison, but no juvenile claim is taken from the inaccessible original.

## Evidence boundary and design decisions

- Adults are near equal in displayed skeletal height; no quantified sex-size direction was found.
- Adult identity follows the narrow, broken fine bars and speckled head, short white supercilia, white scapular patches, two-tone yellow iris and mostly feathered tarsi. Avoid the v1 wallpaper-like horizontal barring.
- Because no species-specific juvenile stage was found after active searches under current and historical names, the center bird is explicitly `JUVENILE · AGE UNKNOWN`. It is smaller/softer, rests low with closed or downcast eyes, and keeps wing and tail largely hidden by soft contours. This is a conservative design inference, not a scientific developmental reconstruction.
- Both juvenile feet grip one continuous mossy branch. No nest, eggs, flight, day age, bright iris claim, long mature remiges or adult tail bands.
- Scientific status remains `false`; target review result is `PASS_WITH_LIMITATIONS`.

## Full ImageGen prompt

```text
Create a 1536×1024 landscape three-character scientific concept plate in the same warm, softly rounded, semi-realistic electronic-pet style as the verified #144 v5 plate. Humid Mindoro forest at warm natural light; one continuous mossy branch; exactly three owls. Bottom title exactly “146 MINDORO BOOBOOK · Ninox mindorensis”. Bottom labels exactly “ADULT MALE”, “JUVENILE · AGE UNKNOWN”, “ADULT FEMALE”.

Adult male left and adult female right: near-equal skeletal height and mass because no quantified sex-size direction is available. Small compact earless boobooks, small pale dull-yellow bills/cere tinged greenish at the sides, small pale-brown facial disks with short subtle filamentous cheek/auricular extensions but no ear tufts. Irides have a mustard-yellow inner ring and brighter lemon-yellow outer ring. Crown and nape are dark brown with narrow broken buff-to-whitish bars that read as irregular speckling, not stripes. Upper mantle mostly plain dark brown after the speckling fades. Scapular patches extensively white but naturally broken by irregular dark margins and tiny dark spots. Wing coverts have dense narrow irregular fine bars with dark bands predominating; outer larger coverts have broken white patches containing tiny dark scrawls. Tawny-buff throat/chest/belly are covered by especially narrow, fine, irregular transverse dark bars, never broad repeated wallpaper stripes. Tarsi mostly feathered; dull olive-yellow toes and black claws grip the branch.

Center juvenile, exact age and locomotor stage unknown: smaller, rounder, softer and lower than adults, eyes closed or downcast so no juvenile iris colour is claimed. Use a plain softly mottled brown-buff contour with only diffuse, nonrepeating hints of the adult palette. Keep the compact developing wing mostly hidden under soft body plumage, with no long crisp barred remiges and no adult covert rows; tail very short and almost entirely hidden. Both feet clearly grip the same branch. Quiet resting pose only; no flight, no nest, no egg, no invented day age.

Keep all six feet anatomically clear and supported. No extra birds, no duplicate limbs, no horn-like tufts, no white adult chest patch, no mature juvenile wing/tail, no unsupported body, no watermark, no extra text. Prioritize species diagnosis and evidence-bounded juvenile uncertainty over decorative detail.
```

## Source delta

- New verified source IDs: 2 (`MINDBOO-ITIS-2025`, `MINDBOO-CLEMENTS-2013`)
- Reused source IDs: 1 (`LZBO-RASMUSSEN-2012-LEAD`)
- Corrected design issue: 1 (v1 juvenile maturity/iris overclaim)
- Unverified lead: 1 (`MINDBOO-OGILVIE-1896-LEAD`)

## Problem — evidence — edit — recheck

- Problem found in the first generated master: both adult underparts still read as regularly repeated horizontal ladders and the crowns as round dots.
- Evidence applied: Rasmussen et al. 2012 printed p.13 describes especially narrow fine bars below and finely broken bars/speckling on crown and nape.
- Edit1: restricted imagegen edit to the two adults, breaking the ventral marks into finer, shorter, irregularly interrupted bars and changing crown/nape marks to broken bars/speckling. The juvenile, branch support, title and labels were explicitly preserved.
- Recheck: full plate plus two original-resolution crops were viewed. Exactly three birds remain; title/labels are exact; all three birds have natural branch support; juvenile has closed/downcast eyes, mostly hidden wing/tail and both feet supported. Adult markings are less repetitive and closer to the read diagnosis.
- Remaining unknowns: species-specific juvenile age, iris progression, locomotor stage and feather sequence. The plate therefore remains `PASS_WITH_LIMITATIONS` and `scientifically_verified=false`.
- Reusable rule actually applied and visually verified here: when a source diagnoses “fine/narrow bars,” the image prompt must also require unequal lengths, breaks, variable spacing and asymmetry; “fine” alone still produced wallpaper-like repetition.

## Full ImageGen edit1 prompt

```text
Edit this exact scientific concept plate; preserve the 1536×1024 landscape layout, warm humid Mindoro forest, continuous mossy branch, exactly three owls, all labels and title text exactly unchanged, and preserve the center juvenile completely unchanged. Modify only the plumage pattern of the two adult Mindoro Boobooks. On both adult breasts and bellies, replace the overly regular continuous horizontal ladder-like stripes with much narrower, finer, irregularly interrupted dark-brown bars on tawny-buff: unequal lengths, variable spacing, small breaks, slight asymmetry, subtly different from feather to feather, with the dark marks remaining delicate rather than bold. On both adult crowns and napes, replace the round polka-dot look with finely broken short dark-brown and buff/whitish bars and natural speckling. Keep the adults' short white supercilia, small pale-brown facial discs, extensive white scapular patches with dark margins, finely barred wing coverts with dark bands predominant, yellow irises, pale dull yellow-green bills, olive-yellow feet and black claws. Do not change body size, feet, perch contact, eye direction, juvenile, environment, typography, title, or labels. Keep the same warm softly rounded semi-realistic electronic-pet rendering, not a field-guide plate and not photorealistic.
```
