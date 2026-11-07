# #177 *Otus hartlaubi* v3 research and design boundary

- **Current name:** *Otus hartlaubi* (Giebel, 1872), São Tomé Scops-owl.
- **Historical synonym:** *Athene hartlaubi* Giebel, 1872.
- **Action:** SCIENCE_REVISION; unique increment 0.
- **Access date:** 2026-11-07.
- **Science status:** false / PASS_WITH_LIMITATIONS target.

## Sources actually read

### STSO-MELO-ETAL-2022-P7-P27 — reused original specimen measurements
- **URL/ID:** https://pmc.ncbi.nlm.nih.gov/articles/PMC9836643/ ; ZooKeys 1126.
- **Read:** Table 1 and diagnosis.
- **Facts:** five São Tomé birds; visible wing 130–136 mm and tail 67–69 mm, diagnosis wing range 130–139 mm. Table entries unsexed.
- **Decision/limit:** extremely small compact silhouette; no statistical sex-size rule.

### STSO-IUCN-2018-ID — re-read institutional identification account
- **URL/DOI:** https://doi.org/10.2305/IUCN.UK.2018-2.RLTS.T22688620A131460770.en
- **Read:** identification information in the indexed account.
- **Facts:** 16–19 cm, tiny ear tufts, light rufous-brown facial disc, black-shaft-streaked warm upperparts, black-tipped white scapular spots, narrow buff tail bars, yellow bill/eyes; juvenile only “paler.”
- **Decision/limit:** adult identity and direction only; does not establish juvenile age, wing maturity or iris.

### STSO-COMMONS-INAT-2018-12933236 — new verified adult photograph
- **Credit/date:** thibaudaronson / iNaturalist observation, 1 Jan 2018; Commons file reviewed 26 Dec 2019.
- **URL:** https://commons.wikimedia.org/wiki/File:Otus_hartlaubi_12933236.jpg
- **Read:** full image page, original 1600×1200 metadata and licence lines 102–152.
- **Fact/use:** adult *O. hartlaubi* field appearance; compact outline and low tuft calibration.
- **Limit:** sex unknown; adult only; CC BY-SA 4.0 image not copied into repository.

### STSO-AFRICANBIRDCLUB-SINEUX-2020-ADULT — new verified adult photograph
- **Institution/credit/date:** African Bird Club image database; Lionel Sineux; São Tomé; Feb 2020.
- **URL:** https://africanbirdclub.org/afbid/search/birddetails/birder/805/37008
- **Read:** image page lines 33–78.
- **Fact/use:** explicitly adult *O. hartlaubi*, location/date verified; compact adult visual cross-check.
- **Limit:** sex not supplied; no young or sex comparison.

### STSO-MIKKOLA-2013-P136 — reused repository transcription
- **Facts retained:** very small owl, very small tufts, deep yellow adult eyes, yellow bill/cere, distal quarter of tarsus unfeathered; paler finely barred mesoptile; downy chick undescribed.
- **Access note:** uploaded guide unavailable this execution; only existing page-verified repository transcription reused.
- **Limit:** exact young age, iris and feather/flight chronology unknown.

### STSO-IUCN-JONES-ETAL-1991-P72-73 / STSO-ITIS-555374-2026 — reused
- **Facts:** primary/secondary humid forest and middle-altitude secondary forest records; October fledglings without plumage/mobility detail; ITIS valid name and *Athene hartlaubi* synonym.
- **Decision:** forest context; no nest/flight reconstruction.

## Evidence-to-design boundary
- Adults near-equal height/body; no default female enlargement. A subtly fuller female is allowed only as a non-quantified guide direction.
- Same grey-brown morph for both sexes; no sex-coded morph.
- Yellow adult eyes/bill/cere, low tufts, pale scapular patches, fine barring and compact tail.
- Young is an **age-unknown mesoptile**: paler, finely barred, dark/indeterminate iris, short soft rounded wings, short supported tail; no hatchling or flight claim.
- No nest/cavity/eggs because evidence does not establish geometry.

## Unknowns
Exact mesoptile age/sex, iris chronology, remex/tail sequence, flight threshold, nest geometry, downy chick appearance and quantified sex-size difference.

## Full ImageGen prompt

```text
Use case: scientific-educational.
Asset: premium tactile naturalistic 3D maquette owl-pet triptych, v3 science revision.
Species: #177 SÃO TOMÉ SCOPS-OWL — Otus hartlaubi (Giebel, 1872); historical synonym Athene hartlaubi only.
Canvas: 1536×1024 landscape, warm humid São Tomé middle-altitude forest, restrained moss and broad leaves, museum-quality hand-modelled feather planes, readable but natural. Exactly three complete birds on one broad living branch, all feet supported. Title exactly "177 SÃO TOMÉ SCOPS-OWL" with italic "Otus hartlaubi". Labels exactly: "ADULT MALE" left, "ADULT FEMALE" center, "AGE-UNKNOWN MESOPTILE" right. No other text or birds.

Adults: extremely small compact short-tailed scops-owls in the same controlled grey-brown morph; tiny low ear tufts nearly absent at rest, deep yellow eyes, small yellow bill/cere partly masked by facial bristles, light brown facial disc darker close to eyes, dark grey-brown upperparts with subtle rufous/brown vermiculation and narrow dark shaft streaks, broken conspicuous pale scapular patches, pale underparts with fine brown/rufous barring and restrained darker streaks, narrow buff tail bars. Distal quarter of tarsus only lightly feathered; no long bare legs. Adults near-equal in height and body scale. Female may be only subtly fuller, not taller/larger; do not encode morph or colour as sex. The two newly read adult photographs calibrate compact outline only because sex is not supplied.

Young: AGE-UNKNOWN MESOPTILE, not hatchling and not claimed fledgling. Paler than adults, soft fluffy contour with fine light-brown barring across upper- and underparts, round head with tiny low tufts or none, dark/indeterminate iris, short soft partly formed rounded wings mostly dissolved into fluff, no long adult-hard layered remiges, short partly hidden tail. Calm low stationary posture with both feet gripping the broad branch and belly naturally supported. Do not claim age, sex, flight ability or adult eye chronology.

No nest, cavity, eggs, prey, flight, begging, spread wing, cliff or savanna. Exact young age, iris/wing/tail/flight chronology, nest geometry and robust sex-size ratio remain unknown. Target PASS_WITH_LIMITATIONS; scientifically_verified=false.
```
