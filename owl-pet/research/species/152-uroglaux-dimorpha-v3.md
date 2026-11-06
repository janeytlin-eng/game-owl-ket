# #152 *Uroglaux dimorpha* v3 research card

- Prepared: 2026-11-04T18:37:36.228+08:00
- Action: archive repair and science revision
- Current name: *Uroglaux dimorpha*
- Old names mapped: *Athene dimorpha* (original combination); *Ninox dimorpha* (historical combination/plate)
- Mikkola upload accessible: no

## Verified source facts

1. **PHO-BEEHLER-PRATT-2016-P373-374** — Beehler & Pratt, *Birds of New Guinea*, 2nd ed., pp.373–374. Adult 30–33 cm, small-headed and long-tailed; streaked breast and profusely barred upperparts. Downy juvenile has white face and underparts. Read in the available page extract; no exact juvenile age or flight threshold supplied.
2. **PHO-MIMIKA-GUIDE-2015-P143** — Freeport Indonesia, *A Guide to the Birds of the Mimika Region*, p.143. Medium (32 cm), hawk-like, small head, longish tail, heavily streaked/barred; rainforest and gallery forest to 1,500 m; rare in Mimika lowlands.
3. **PHO-BIRDLIFE-2026-ECOLOGY** — BirdLife DataZone species factsheet, accessed 2026-11-04. New Guinea lowland forest, generally 0–1,000 m and locally 1,500 m; gallery forest; broad prey categories. No juvenile description.
4. **PHO-ITIS-1063560-2026** — ITIS TSN 1063560, accessed 2026-11-04. Accepted *Uroglaux dimorpha* and original combination *Athene dimorpha*. Taxonomy only.
5. **PHO-SHANY-1995-P74-UNVERIFIED** — Noem Shany, “Juvenile Papuan Hawk-Owl *Uroglaux dimorpha* near Vanimo”, *Muruk* 7(2):74. Title/page verified in issue metadata; full article subscription-blocked, so no biological detail is treated as verified.

## Design boundaries

- Adults share the diagnostic small head/long tail and barred/streaked pattern. Yellow adult iris is retained.
- Sex-size direction is **unknown/conflicted**: adults are near-equal; neither is deliberately enlarged.
- Juvenile is the directly described downy stage: white face/underparts, soft brown-gray upper down, low supported crouch. No mature remiges, long projecting tail, bright adult iris, flight pose or invented nest.
- Scene is generic New Guinea lowland rainforest with a natural support, not a claimed nest site.
- Concept remains a stylized scientific design and must retain `scientifically_verified: false`.

## Problem → evidence → change → review target

- v2 raw display is top-strip-only/gray-body → direct repository visual inspection → preserve v2, create v3 → verify full 1536×1024 render and all three complete birds.
- prior sex-size direction not supportable → conflicting secondary summaries → near-equal adults → check crown height and body mass visually.
- juvenile development incomplete → Beehler & Pratt only support white-faced/white-underpart downy juvenile → remove adult-hard wing/tail → inspect juvenile wing, tail, support and eye colour.

## Complete generation prompt

```text
Use case: scientific-educational
Asset type: full-resolution owl-pet scientific concept plate for repository archive
Primary request: polished 1536×1024 landscape plate titled exactly “152 PAPUAN HAWK-OWL · Uroglaux dimorpha”.
Scene/backdrop: New Guinea lowland rainforest in neutral daylight; one broad mossy branch/trunk-base support; no nest, cavity or eggs because breeding site is unknown.
Subject: exactly three birds: left “ADULT MALE”, center “DOWNY JUVENILE · AGE UNKNOWN”, right “ADULT FEMALE”.
Adults: same plumage and near-equal crown height because sex-size direction conflicts/unknown; medium owl with proportionately small head, sleek hawk-like profile, long tail, short rounded folded wings; pale indistinct facial disc with narrow pale brows and dark streaks; bright yellow eyes, gray-dark bill; pale buff/gray-brown upperparts profusely barred dark; breast and underparts strongly longitudinally streaked with brown; barred long tail; feathered tarsi and gripping feet.
Juvenile: source-supported downy juvenile only: white face and underparts, soft brown-gray down above with faint irregular bars; low crouched fully supported, dark/neutral indeterminate eyes; short down-covered wing buds, no layered adult remiges, no projecting long tail, no flight pose. Exact age and flight ability unknown.
Style: refined stylized 3D owl-pet maquette matching recent plates; fine feather texture, rounded anatomy, distinct natural poses, neutral light.
Constraints: exact title and exact labels; current name Uroglaux dimorpha; old names Athene dimorpha and Ninox dimorpha only in metadata; preserve small-head/long-tail adult proportion; visible natural two-foot support; exactly three birds.
Avoid: huge round heads, adult-like juvenile long wings or tail, bright yellow juvenile iris, exaggerated female or male size, identical cloned poses, ear tufts, eggs, nest, cavity, prey, extra birds, cropped feet, orange cast, watermark, border, extra text.
```
