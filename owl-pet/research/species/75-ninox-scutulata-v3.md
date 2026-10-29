# #75 *Ninox scutulata* v3 research note

- Batch/cycle: `2026-10-29T0835+0800` 4/6
- Run: `20261029T0930+0800-cycle-4`
- Research completed: 2026-10-29T09:34:00+08:00
- Action: SCIENCE_REVISION; v1–v2 retained.
- Scientific status: `false`; exact Singapore subspecies, exact juvenile age, quantitative sex ratio and tract chronology remain unknown.

## Sources actually read

1. **SCU-BESG-2024** — Andy Chew, Bird Ecology Study Group, “Brown Hawk Owl juveniles”, 14 June 2024, https://besgroup.org/2024/06/14/brown-hawk-owl-juveniles/ . Text and gallery landing page read. Windsor Nature Park on 13 June: four birds including two juveniles perched high; juveniles disturbed a parent and performed varied “stunts”. Direct Singapore field observation; supports branch dependency and active movement, not exact age, sex or feather chronology.
2. **SCU-NPARKS-2025** — Charlyn Ng / National Parks Board Singapore, “In the Lonely ‘Owl’”, 6 February 2025, Brown Hawk-Owl section, https://www.nparks.gov.sg/publications-resources/articles/in-the-lonely--owl . About 30 cm; rounded head without ear tufts; yellow eyes; dark-brown upperparts; whitish, heavily brown-streaked underparts; rainforest/central catchment and canopy insect hunting. Institutional synthesis; no sex/juvenile series.
3. **SCU-ITIS-2025** — ITIS TSN 555481, *Ninox scutulata* (Raffles, 1822), taxonomy/nomenclature and subordinate-taxa sections, https://www.itis.gov/servlet/SingleRpt/SingleRpt?search_topic=TSN&search_value=555481 . Valid species; synonym *Strix scutulata*; current English name Brown Boobook. Supports name mapping only.
4. **SCU-FUKAI-2016** — Norio Fukai, “Age determination of Brown Hawk-Owl (*Ninox scutulata*)”, *Bulletin of the Japanese Bird Banding Association* 28(1):22–28, DOI 10.14491/jbba.ms073. Abstract and bibliographic page actually read via CiNii/J-STAGE. Japanese Tochigi/Niigata specimens; juvenile/adult rectrix criteria and molt boundary. **Excluded from direct v3 design transfer** because the Japanese population is not evidence for the present Singapore taxon after modern splits.
5. **SCU-MIZOTA-2020** — Mizota, Funo & Ohtani, “Changes in feeding patterns of Brown Hawk-Owls *N. s. japonica* during the nestling period”, *Japanese Journal of Ornithology* 69(2):223–234, DOI 10.3838/jjo.69.223. Abstract actually read. Feeding ecology only; explicitly Japanese *japonica*. **Excluded from plumage/stage design transfer**.
6. Reused **WHSO-MIKKOLA-2013**, printed pp.464–465 / PDF pp.466–467, and **SCU-OWLPAGES-2021**. Their opposite unquantified sex-size directions remain unresolved; adults therefore remain near-equal rather than enforcing a direction.

## Evidence → design boundaries

- Direct: adult identity and rainforest setting follow NParks; active, supported branch-dependent juvenile follows the Windsor observation.
- Inference: juvenile shown with pale fluffy/less-organized body feathering and developed dark growing folded wings/tail, consistent with existing card and field images, but no exact age is claimed.
- Prohibited transfer: no Japanese rectrix-fringe criterion, no Japanese nestling feeding-stage timing, no Morepork-like white-dot rows.
- Sex: near-equal adults; female may be only subtly fuller. This is uncertainty handling, not a biological claim.

## Problem → modification → validation target

- Problem: v2 retained residual pale dot/crown leakage and did not make the taxonomic transfer boundary explicit.
- Modification: v3 removes repeated white crown/back spot rows, constrains the white area to forehead/restrained scapular accents, and selects a fully supported active branch-dependent juvenile.
- Validation: inspect exact three-bird count/text, adult eyes/bill/forehead/streak direction, near-equal scale, juvenile wing/tail/down/action/support, and high-branch humid-forest setting.

## Full imagegen prompt

```text
Create a single polished 3:2 horizontal natural-history character concept plate for the owl electronic-pet project, 1536×1024. Show exactly three full-body BROWN BOOBOOKS, Ninox scutulata, in a cohesive humid Singapore native-forest branch setting, in this left-to-right order: adult male, adult female, branch-dependent juvenile. Use the project’s established softly lit painterly-realistic wildlife illustration style: tactile layered feathers, gentle rounded electronic-pet appeal without chibi distortion, natural anatomy, restrained warm forest palette, subtle depth of field, no UI frame.

Exact visible typography:
Top title: “BROWN BOOBOOK · Ninox scutulata”
Small labels under each bird: “ADULT MALE”, “ADULT FEMALE”, “BRANCH-DEPENDENT JUVENILE”
No other text, no misspellings.

Adult male and female:
- compact medium boobook silhouette, rounded head, absolutely no ear tufts;
- staring round bright yellow irises; blue-black hooked bill with a small pale horn tip; modest white forehead patch, not a broad white crown;
- chocolate to dark-brown crown and upperparts, mostly plain; do NOT create rows of tiny white dots over crown, mantle or wing coverts and do not make them look like Moreporks;
- only restrained, anatomically plausible pale scapular accents;
- whitish throat and underparts with many strong lengthwise brown drop-shaped streaks, not horizontal bars;
- yellow-green toes gripping the branch;
- adults nearly equal in size because published sex-size direction conflicts; female only subtly fuller in body, never an exaggerated larger female or male.
Pose male alert and slightly forward, female calm and three-quarter turned; both feet naturally supported.

Branch-dependent juvenile:
- clearly younger and somewhat smaller, with a fluffy pale cream/off-white head and body, softer round facial outline and less organized/less dense streaking than adults;
- dark growing folded wings and a visible short growing tail, with soft irregular feather edges; developed enough for branch activity but not mature adult wing rows, not wing buds, no invented hatchling features;
- active natural preening/turning pose inspired by observed Windsor Nature Park juveniles, with both feet gripping a forked branch and body weight fully supported;
- preserve juvenile dependency and softness; no adult-like regular white spotting, no spread flight pose, no unsupported floating feet.

Environment: high mossy branch/fork in Windsor-style humid Singapore rainforest, soft green canopy bokeh, restrained natural litter and lichen, no nest cavity interior, no water patch, no prey, no extra birds. Keep all birds unobscured and fully inside frame. Scientific concept art, not a taxonomic plate certification.
```
