# #66 *Tyto capensis* v4 — mature wetland-patch boundary

- Run: `20261030T233010+0800-cycle-4`; batch `2026-10-30T2158+0800`; cycle 4/6.
- Action: SCIENCE_REVISION; v1–v3 retained; unique species increment 0.
- Status: VERIFIED_ARCHIVE at 2026-10-30T23:43:30+08:00; science false.

## Sources actually read

### AGO-PRETORIUS-ETAL-2026-P110 — new
- Pretorius, M. D. et al. (2026), “African Grass Owl nest site use and nest survival in fragmented grassland landscapes”, *African Journal of Wildlife Research* 56:110–124. DOI: https://doi.org/10.3957/056.056.0110
- Full author-posted article text read on 2026-10-30, including abstract, methods/results and reported patch metrics.
- Species/stage: *Tyto capensis* breeding patches and nesting females; 41 nests in Gauteng/Mpumalanga, 2009–2017.
- Facts: nest patches averaged 3.6 ha versus 1.9 ha random patches and 2.9 versus 2.3 years old; more *Imperata cylindrica* nearby; more wetland and less developed land cover. Development reduced daily nest survival.
- Limits: the study addresses nest-patch selection/survival, not juvenile plumage, exact chamber geometry, day-age or first-flight thresholds.
- Design use: dense old *Imperata* wetland interior, concealed runway/platform, no developed edge. It does not justify a neat visible cave mouth.

### Reused sources
- AGO-WHITTINGTON-2012: Whittington-Jones et al. (2011), GABAR 22:19–25, actually read pp.19–25. Six nestlings in two active nests; literature-based fledging about six weeks; tall rank grass/sedges along drainage/wetland. The paper explicitly rejects tawny-buff face as a reliable age key. It does not provide chick feather chronology.
- AGO-BLSA-RDB-2025: BirdLife South Africa 2025 account, Identification/Biology lines 122–130. Adults: white heart face, dark eyes, pale bill, dark olive-brown upperparts with tiny white tips, pale spotted underparts; fledglings darker and without adult white dorsal spots.
- SEO-OSTRICH-RSD-2008: Ansara-Ross et al., *Ostrich* 79:83–86, DOI 10.2989/OSTRICH.2008.79.1.11.366. Female mass/body-length direction in a Gauteng carcass sample; no fixed standing-height ratio.

## Conflict and correction

- Existing v3 used a visually explicit grass-tunnel/cave opening. The new 41-nest study supports mature dense wetland patches and *Imperata* proximity but does not document a neat cave-shaped mouth.
- V4 therefore keeps the recent-fledgling plumage boundary already supported by BirdLife, while replacing the conspicuous cave mouth with a concealed runway and low supported platform beneath arching mature grass.
- Current *Tyto capensis* retained. Do not borrow *Tyto longimembris* juvenile timing even though some taxonomies historically group them.

## Unknowns

Exact individual age, feather-tract sequence, first-flight threshold, range-wide sex scaling, geographic variation and fine nest-chamber geometry remain unknown. PASS_WITH_LIMITATIONS only; scientific verification remains false.

## Complete imagegen prompt

```text
Use case: scientific-educational.
Asset type: owl-pet species concept plate.
Primary request: Create a polished 3:2 science-revision plate in the repository’s established realistic-cute natural-history game concept style for African Grass Owl. Show exactly three owls and the complete readable title and labels.
Text (verbatim): title “AFRICAN GRASS OWL”; italic scientific name “Tyto capensis”; bottom labels “ADULT MALE”, “RECENT FLEDGLING”, “ADULT FEMALE”.
Adults: no ear tufts; dense white heart-shaped facial disc with a subtle dark-speckled/buff border; dark teardrop eyes; whitish to pale-gray bill; dark olive-brown upperparts with tiny white terminal spots; white to pale-buff underparts with scattered dark spots; long buff-feathered legs and grayish feet. Sexes share plumage. Show the female only modestly fuller/longer-bodied than the male, never a fixed or exaggerated standing-height ratio.
Juvenile: recent fledgling at the learning-to-fly period, fully feathered but grounded with folded wings, stable feet and no flight pose. It is darker than the adults and lacks the adults’ tiny white dorsal spots. Keep the face buff-neutral rather than forcing rufous, because face color is unreliable for ageing. Do not show white natal down, baby wing buds, adult white dorsal spotting, crisp adult covert rows, or an exact day-age.
Environment: interior of a mature, tall, dense African wetland patch dominated by old cotton-wool grass / Imperata cylindrica and sedges. Show a concealed trampled grass runway and stable low grass platform under arching stems. Do not show a neat cave mouth, tree hollow, rock ledge, open exposed nest, eggs, roads, buildings or developed edges. The 2026 field study supports large old wetland patches and Imperata proximity, not a visible cave-shaped chamber.
Composition: three full birds clearly separated, all feet naturally supported with correct perspective; juvenile central and slightly lower; adults flanking it at near-equal visual height.
Constraints: exact three birds; correct species identity; no extra chicks, text, logos, borders or watermark; no unsupported sex-size exaggeration; no mature juvenile wing pattern.
```


## Production check and iteration

- First render issue: center fledgling showed conspicuous pale dorsal speckles and an overly adult-regular folded-wing panel.
- Evidence applied: BirdLife's fledgling distinction (darker, lacking adult white dorsal spots); the 2026 patch study changes habitat geometry only and does not fill plumage chronology.
- Edit: center bird only; removed dorsal white spotting and softened/compacted the folded wing while preserving adults, text, scale, grass structure and foot support.
- Recheck: edited 1536x1024 master, 620x760 juvenile crop and 680x453 derivative opened; PASS_WITH_LIMITATIONS. Exact age, feather chronology, first-flight threshold, range-wide sex scale and chamber geometry remain unknown; science false.
- Archive paths: `design/concepts/66-tyto-capensis-v4.png`, `production/generated/66-tyto-capensis-v4-generated-master.png`, `production/reviewed/66-tyto-capensis-v4-reviewed-master.png`; fixed readback pending.


## Fixed archive verification

- Commit: `0a6e36a7cc30840727a0ad98a8b0f66c63a6b1f0`; recursive tree non-truncated (2,112 entries).
- Exact concept/generated/reviewed blob SHAs and sizes matched; manifests 572/571/562 each contained exactly one v4 entry; support records matched.
- Archive verification is complete, but scientific acceptance remains false because the listed chronology/sex/chamber unknowns are unresolved.
