# 173 — *Otus madagascariensis* — v3 research and design boundary

- Batch/cycle: `20261107T140000+0800` 4/6
- Research ready: 2026-11-07T15:58:00+08:00
- Planned asset: `173-otus-madagascariensis-v3.png`
- Action: science revision; no new unique species
- Scientific status: **false** (age/sex/development gaps remain)

## Name and taxonomic mapping

The repository follows the current species treatment *Otus madagascariensis* (Grandidier, 1867). ITIS TSN 686657 and the IOC-linked record treat it as a valid species; the older combination *Scops madagascariensis* is retained as a synonym. Fuchs et al. (2007) found the western and eastern populations weakly differentiated and not reciprocally monophyletic, so the Clements/BirdLife lumping as *O. rutilus madagascariensis* remains an explicit taxonomic conflict rather than a morphology shortcut.

## Actually read evidence

### TSO-RENE-THORSTROM-2009-P87-88 — corrected from abstract-only to full paper read
- Lily-Arison René de Roland & Russell Thorstrom, 2009, “First record of a ground nest of the Madagascar Scops Owl *Otus rutilus*”, *African Bird Club Bulletin* 16(1):87–88. Full PDF read on 2026-11-07: https://www.biodiversitylibrary.org/page/56261159
- The exceptional Berenty nest was a shallow ~20 mm ground depression with four white eggs and no nesting material. The adult returned after disturbance, but the birds did not return later; hatching was not observed.
- The same paper reports ordinary natural tree-hole nests in Tsimembo at mean 5.8 ± 2.2 m (n=7), mean clutch 2.4 ± 0.9 (n=5), and mean body mass 108 g (n=8).
- Habitat context: western/southern forest and woodland; Berenty has ~500 mm annual rainfall and spiny forest plus riparian gallery forest.
- **Design use:** dry western Malagasy environment is supported; the ground nest is exceptional and must not be generalized or used to invent chick posture.
- **Limit:** no hatched young, sex comparison, plumage development or flight threshold.

### TSO-FUCHS-ETAL-2007-P408-418 — reused
- Fuchs et al., 2007, *Molecular Phylogenetics and Evolution* 44:408–418. DOI: https://doi.org/10.1016/j.ympev.2006.12.013
- Indexed full text/abstract read: 34 owls and 1,449 bp; western birds described as greyer/yellow-brown with shorter ear tufts, longer tail and smaller claws than eastern birds, but authors did not support two species.
- **Design use:** very short low ear tufts, grey/yellow-brown western morph, dry-west setting.
- **Limit:** population-level tendencies, not sex or age evidence.

### TSO-ITIS-686657-2025 — revalidated current record
- ITIS, TSN 686657, current page read 2026-11-07: https://www.itis.gov/servlet/SingleRpt/SingleRpt?search_topic=TSN&search_value=686657
- Valid *Otus madagascariensis*; synonym *Scops madagascariensis*; IOC v15.1-linked record.
- **Use/limit:** nomenclature only.

### TSO-MIKKOLA-2013-P145 — repository transcription reused
- Heimo Mikkola, 2013, printed p.145. The uploaded book was not accessible in this run; only the repository’s prior transcription was reused.
- Repository transcription supports the short-tufted grey morph, a moderate rather than extreme female-size direction, western dry habitat, and an age-unknown older immature with stronger-barred uppertail coverts and narrower pointed rectrix tips.
- **Limit:** no independent page re-open this run; no exact immature age, sex, fledging status or developmental chronology.

### TSO-GRANDIDIER-1867-P85-86-LEAD — unverified descriptive-text lead
- Alfred Grandidier, 1867, *Revue et Magasin de Zoologie*, series 2, 19:85–86; protonym *Otus Madagascariensis*. Metadata checked through Avibase/BHL on 2026-11-07: https://avibase.bsc-eoc.org/species.jsp?lang=EN&avibaseid=62279A0136D6A4B1
- BHL original returned 403 and the alternate 28.9 MB scan could not be opened by the retrieval service. The descriptive text was **not read**.
- **Use/limit:** name/date/type-locality lead only; not verified morphology evidence.

### TSO-RAMAMONJISOA-2007-THESIS-LEAD — unresolved
- Ramamonjisoa, 2007, University of Antananarivo DEA thesis, located only through bibliographic/secondary references.
- Full thesis was not located; snippets mentioning juvenile feeding were not treated as verified developmental evidence.

## Facts, inferences and unknowns

- **Source facts:** western birds trend grey/yellow-brown with short tufts; dry western/southern forest context; ordinary nests are tree holes and the reported ground nest was exceptional; the failed ground clutch yielded no chick evidence.
- **Design inference:** adults share one grey morph; female only moderately fuller and near-equal in standing height. This avoids the unsupported universal “female much larger” rule.
- **Age boundary:** use the previously bounded **age-unknown older immature**, adult-like but softer, with stronger-barred uppertail coverts and narrower pointed rectrix tips. Do not call it nestling, fledgling or flight-capable.
- **Unknown:** exact sex-size ratio, immature age/sex, iris and soft-part ontogeny, wing-feather timing, flight threshold, chick down sequence and occupied nest-interior support.

## Prompt

```text
Create a polished 1536×1024 landscape scientific owl-pet plate in the repository’s established premium stylized 3D maquette look. Title exactly “173 TOROTOROKA SCOPS OWL · Otus madagascariensis”. Exactly three complete birds in order and labels: left “ADULT MALE”, centre “ADULT FEMALE”, right “AGE-UNKNOWN OLDER IMMATURE”.

All are small compact western Malagasy scops owls in the evidence-supported grey/yellow-brown morph, with very short low ear tufts, yellow irises, restrained pinkish lids, blackish bills, feathered tarsi, light grey toes and dark horn claws. Adults share the same grey morph. The female is only moderately fuller, with near-equal standing height; do not impose a large female without species-specific measurement support. Upperparts are brownish-grey with long dark shaft streaks, a restrained pale scapular stripe, and rounded barred wings and tails. Underparts are light grey with fine dark streaks, vermiculation and whitish bars.

The right bird is explicitly an age-unknown older immature, not a hatchling: adult-like but softer and fluffier, with stronger-barred uppertail coverts and narrower pointed rectrix tips, a shorter soft folded wing, and a low stable stance with both feet naturally supported on the branch. Do not imply an exact age, sex or flight threshold.

Set all three in neutral daylight in western/southwestern Madagascar dry deciduous–spiny gallery forest, with subtle baobab and Alluaudia cues. Use distinct calm three-quarter poses and natural branch support. No nest scene: the published ground nest was exceptional and failed before hatching, while ordinary nests are tree holes.

Avoid tall theatrical ear tufts, rufous morph, huge female, newborn/downy chick, flight, adult-hard immature wing layering, ground nest, cavity interior, eggs, prey, unsupported feet, extra birds, extra text, decorative border or orange sunset grading.
```

## Review gates

1. Exactly three complete birds and exact order/labels.
2. Ear tufts very short and low; no tall theatrical tufts.
3. Adults same grey/yellow-brown morph; only moderate female fullness.
4. Older immature stays softer with bounded tail/coverts differences and supported feet; no exact age/flight claim.
5. Dry western/southwestern Madagascar habitat; no ground nest/cavity/eggs.
6. Any unresolved age or sex detail remains science=false.
