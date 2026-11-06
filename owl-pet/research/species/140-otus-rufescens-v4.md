# #140 *Otus rufescens* v4 research and design boundary

- Prepared: 2026-11-07T02:05:18+08:00
- Batch/cycle: `20261107T012800+0800` · 3/6
- Stage: RESEARCH_READY
- Action: SCIENCE_REVISION
- Source delta: newly indexed 3 / reused project evidence 2 / corrected 1
- Scientific verification: false

## Current name and historical names

ITIS TSN 555364 lists current valid *Otus rufescens* (Horsfield, 1821) and the original combination *Strix rufescens* Horsfield, 1821. GBIF/Catalogue of Life additionally reports *Strix mantis* as a synonym, but this v4 design does not use that database record for morphology.

## Actually read evidence

1. **RFS-MIKKOLA-2013-P178** — Heimo Mikkola, *Owls of the World: A Photographic Guide*, printed p.178 / PDF p.180, actually read from the user's uploaded file on 2026-11-07. It explicitly says there are no data on sexual size differences; describes the nominate light morph, chestnut- to amber-brown eyes, horn-white bill, feathered pale-buff feet, downy chick reddish-brown/darker on crown and mantle/paler on rump, and mesoptile adult-like but far less speckled. It also describes lowland rainforest/evergreen forest habitat. This is a secondary photographic guide, not a developmental chronology.
2. **RFS-WARAKAGODA-RASMUSSEN-2004-P102** — Warakagoda & Rasmussen, BOC 124(2):85–105, p.102, original comparative/specimen paper actually read through its PDF text. An NNM specimen supports only a nearly uniform rich rufescent-brown mesoptile, weak dark facial-disc rim, and very vague dark barring strongest on hindcrown/upper mantle. It does not establish exact age, iris, flight capacity or nest.
3. **RFS-ITIS-555364-2026** — ITIS taxonomic record actually opened/read, accessed 2026-11-07. Valid current name *Otus rufescens*; original combination *Strix rufescens*; two listed subspecies, nominate and *malayensis*. Taxonomy only.

Reused project evidence: v3 research boundary and v1 production record. Correction: v3 said four new index entries, but the current SOURCE_INDEX did not contain them; v4 adds stable, de-duplicated entries instead of counting missing historical index rows.

## Design decisions and unknowns

- Adult male and female are near-equal in apparent size. No fixed female-larger rule is allowed.
- Use the nominate light morph and do not import the more saturated/yellower *malayensis* palette.
- Use the directly documented downy-chick stage rather than inventing a newborn. The chick is supported, resting and has no mature remiges/tail.
- A shallow moss/leaf depression is an illustrative load-bearing support, not a nest-site claim.
- Exact chick day age, iris, flight ability, ear-tuft chronology, nest structure/site, sex-size ratio and complete feather chronology remain unknown. Therefore this is a concept-stage revision and not a scientific pass.

## Full imagegen prompt

Create a 3:2 horizontal 1536×1024 scientific character-concept plate in the established owl-pet warm cinematic tactile 3D natural-history style. Exactly three nominate light-morph Reddish Scops Owls (Otus rufescens) on one broad, naturally load-bearing mossy branch in humid Southeast Asian lowland evergreen rainforest: adult male left, adult female center, supported downy chick right. Full bodies, toes, claws and every contact point visible. Adults nearly equal in apparent body size because the source explicitly states no sexual-size data; use distinct poses/head angles, never clones. Adults are tiny scops owls with prominent but compact ear tufts; tawny reddish-brown upperparts; sparse irregular triangular/elongated light-fulvous spots with dark margins, larger on mantle/wing coverts and shaft-like on back/rump; ochre primaries with dark bars; yellowish-brown to dull-yellow underparts with sparse small dark-edged spots; cinnamon-buff facial discs lightening inward toward dark-brown ruffs; chestnut-brown to amber-brown irises, not yellow; horn-white bills; pale-buff legs feathered nearly to the base of yellowish toes; horn claws. Do not import the more reddish malayensis palette. Chick is much smaller and fully supported in a shallow depression of moss and leaves on the same branch: rounded reddish-brown down, visibly darker crown and mantle, paler rump/belly, eyes gently closed because chick iris is unknown; no asserted ear tufts, no mature remiges, no long adult tail, no flight pose. The moss/leaf depression is only a support, not a claimed nest site. Humid lowland evergreen forest, subdued dawn light, soft depth of field. Exact text only: top “#140 · OTUS RUFESCENS”; subtitle “REDDISH SCOPS OWL”; labels “ADULT MALE”, “ADULT FEMALE”, “DOWNY CHICK · AGE UNKNOWN”; footer “CHARACTER CONCEPT · NOT TO SCALE”. Avoid extra birds, cloned adults, fixed female-larger scaling, unsupported feet, regular polka-dot spots, oversized facial discs, yellow eyes, adult plumage on chick, invented cavity, watermark or misspelled text.
