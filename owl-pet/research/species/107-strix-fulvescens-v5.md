# #107 Fulvous Owl — *Strix fulvescens* — v5 science revision

- Accessed: 2026-11-06
- Action: targeted science revision; v1–v4 preserved
- Current / older name: *Strix fulvescens*; protonym and ITIS synonym *Syrnium fulvescens*
- Selected young stage: directly photographed fledgling, exact age and flight threshold unknown
- Scientific verification: false

## Evidence actually read

### FVO-EISERMANN-AVENDANO-2018-P177-F20 — new primary-image record

- Title/authors/year: “An updated checklist of the birds of Guatemala” — Knut Eisermann & Claudia Avendaño, 2018.
- Source/type: *Bulletin of the British Ornithologists’ Club* 138(3), open-access article with dated field photograph.
- URL: https://boc-online.org/bulletins/downloads/BBOC1383-PDFa.pdf
- Location: printed p.177, Fig.20; web extraction lines 1197–1205.
- Facts: Fulvous Owl is fairly common in cloud forest above 1,800 m; the nest was still undescribed; a fledgling photographed at Finca El Pilar on 26 April 2017 beside an adult was the second documented Guatemalan breeding record.
- Boundary: the photograph identifies a fledgling and adult, but provides no hatch date, sex, measured feather sequence or sustained-flight test. It supports a branch-supported, formed-but-still-soft fledgling; it does not support an invented nest, eggs or exact age.
- Confidence: high for the dated photograph/caption and explicit “nest undescribed” statement.

### FVO-ITIS-555430-2026 — new taxonomy record

- Institution/type: Integrated Taxonomic Information System, TSN 555430.
- URL: https://itis.gov/servlet/SingleRpt/SingleRpt?print_version=PRT&search_topic=TSN&search_value=555430&source=to_print
- Location read: lines 6–33 and 47–48.
- Facts: current valid *Strix fulvescens* (Sclater & Salvin, 1868); synonym/protonym *Syrnium fulvescens*.
- Boundary: taxonomy only; no morphology or development inference.
- Confidence: high for current/older-name mapping.

### FVO-OWLPAGES-2020-L64-75 — re-read secondary morphology account

- Institution/author/year: The Owl Pages / Deane Lewis, updated 2020.
- URL: https://www.owlpages.com/owls/species.php?s=1730
- Location read: lines 64–75.
- Facts used: blackish-brown eyes, corn-yellow bill, dark rufous-brown upperparts with pale flecks/short bars, fulvous-ochre underparts with barred upper breast and broadly streaked lower body, barred flight/tail feathers, feathered tarsi and basal toe feathering.
- Conflict excluded: its generic cavity, 2–5 egg and 28–30 day paragraph is explicitly probabilistic/secondary and conflicts with the 2018 article’s “nest undescribed”; no nest, eggs or exact chronology will be drawn.
- Confidence: moderate for adult synthesis; low/excluded for the generic breeding paragraph.

## Reused repository evidence

- `FVO-EISERMANN-FIELD2026` / `S107-CAYAYA-2026`: direct field photographs of adult and age-unknown juvenile.
- Existing v4 correctly avoided a fixed female-larger ratio and hid the young bird’s long tail.
- Uploaded Mikkola guide was not mounted in this execution; no fresh page claim is made.

## V4 audit and change decision

The actual v4 PNG was opened. Count, title, labels, cloud-forest habitat, near-equal adult scale, juvenile support and compact down-softened wing all pass. However both adults’ irises read light gray/amber rather than the blackish-brown adult iris supported by the re-read account. V5 therefore makes one narrow evidence-led edit: darken only the two adult irises to deep blackish-brown while preserving pupils/catchlights and every other pixel-level design intention. The juvenile iris remains unresolved and is not recolored from adult evidence.

## Complete imagegen edit prompt

Use case: precise-object-edit
Asset type: owl electronic-pet natural-history concept plate revision
Input image: `owl-pet/design/concepts/107-strix-fulvescens-v4.png` — edit target and established style/composition reference
Primary request: change only the irises of the left ADULT MALE and right ADULT FEMALE from light gray/amber to deep blackish-brown, retaining small natural catchlights and dark pupils.
Constraints: preserve exactly three birds, exact title “FULVOUS OWL · Strix fulvescens”, exact labels, every bird’s pose, body proportions, plumage, bill, feet, branch support, juvenile appearance, cloud-forest background, 3:2 framing and semi-realistic painterly natural-history style. Adults remain near-equal in visible height; juvenile remains an exact-age-unknown supported fledgling with compact down-softened wing and concealed tail. Change no other color, feather, anatomy, text or background element.
Avoid: bright orange/yellow/gray adult irises, recoloring the juvenile eye, added birds, nest, eggs, prey, ear tufts, long juvenile remiges/tail, unsupported feet, text drift, watermark.

## Design limits to recheck

- Adult sex-size direction remains unknown; near-equal display is a neutral composition, not a measured ratio.
- The young is a dated photographed fledgling but exact age, continuous feather chronology and sustained-flight ability remain unknown.
- The branch is support, not a nest. Nest site and construction remain unknown.
- Scientific verification remains false.

## Review result

The generated plate was opened at full resolution plus fledgling and adults/support crops. The renderer changed more than eye pixels, so every identity, stage, proportion, text and support invariant was rechecked. Adult irises now pass as deep dark brown; exactly three supported birds, near-equal adult scale, compact down-softened fledgling wings, concealed juvenile tail and non-nest branch support all pass. No second edit was required. Result `PASS_WITH_LIMITATIONS`; unresolved biological fields remain unknown and science stays false.


