# #05 *Strix aluco* v4 research and design record

- Species: Tawny Owl — *Strix aluco*
- Catalogue action: `SCIENCE_REVISION`; unique-species increment `0`
- Existing versions preserved: v1–v3; the 2026-10-10 user approval remains attached to v1 only.
- Research checkpoint: 2026-10-30T00:36:00+08:00
- Science status: `false` pending external expert review; this is a concept-calibration revision.

## Evidence actually read

1. `TAO-MIKKOLA-2013-P315` — Heimo Mikkola, *Owls of the World: A Photographic Guide*, 2nd ed. (2013), printed pp. 315–317 / uploaded PDF pp. 317–319. Adults are round-headed and untufted, with blackish-brown eyes and an ivory-yellow bill. Brown/grey/rufous morph is not a sex marker. Juvenile mesoptile is pale brownish- or greyish-white with diffuse dense barring; eye rims/soft parts can be pale fleshy-pink.
2. `TAO-COLES-PETTY-1997` — Coles & Petty (1997), GTR NC-190 pp. 111–118. In one Kielder Forest sample, 22 young from 11 broods were tagged at 22–31 d and left nests at 29–36 d (mean 32.1 d). Nest departure is not evidence of confident flight and is not universal timing.
3. `TAO-OVERSKAUG-1999` — Overskaug et al. (1999), *The Condor* 101(1):169–174, abstract. Telemetry sample n=53 in central Norway; mortality peaked during the first ten days after nest-box departure, when young were small and had poorly developed locomotion. Dense forest and concealed roosts were preferred. This supports a low, fully supported, cautious recent-fledgling pose; it does not provide plumage chronology.
4. `TAO-SUNDE-NAUNDRUP-2016` — Sunde & Naundrup (2016), *Journal of Ornithology* 157:961–970, abstract. In 41 broods, movement increased during the first 20–30 d after fledging; only after that interval did juveniles range across the natal territory, indicating near-full flying ability. This supports portraying a first-week fledgling as not yet a confident flyer.
5. Reused `TAO-BTO-FACTS` — BTO BirdFacts. Sexed mass/wing samples overlap; adult female is heavier on average but this is not a universal standing-height ratio. Nest records support cavity use and altricial young.

## Design boundary and uncertainty

Source facts: recent fledglings can have developed folded wings while locomotion is still poor; early post-departure concealment and full support are biologically plausible. Adults must share the same brown morph because morph is not sex-linked. Design inference: a first-week post-departure juvenile crouches and side-steps on a broad low mossy log, with both feet and lower body supported and one folded wing slightly away for balance. No flight or exposed high-branch pose.

Unknown and not depicted as known: exact day, sex, subspecies, wing/tail measurements, first-flight threshold, iris transition, universal female:male displayed-size ratio, and universal cavity geometry. A formed folded wing is retained because the chosen stage is post-fledging; it must remain soft, diffuse-barred and less orderly than adult remiges rather than being shortened to a generic nestling stub.

## Full image-generation prompt

Create one 1536×1024 horizontal cinematic 3D animated scientific comparison board in the exact established owl-pet concept style. Use the supplied #05 Tawny Owl v3 only as layout, lighting, material and typography reference, while rendering a clearly new evidence-led scene.

Header must read exactly: `05 · TAWNY OWL · Strix aluco`. Place exactly three Tawny Owls in one coherent temperate broadleaf woodland scene and label them exactly `ADULT MALE`, `ADULT FEMALE`, `JUVENILE`. No other bird.

Adult male and adult female: same brown morph; round head with no ear tufts; very dark blackish-brown eyes; ivory-yellow bill; warm brown upperparts with irregular darker vermiculation and whitish scapular marks; pale facial discs with darker rims. They are sexually similar in plumage. Show only a modest average female fullness, with nearly equal displayed head height; do not make the female a giant and do not use morph colour as sex difference. Both adults perch naturally with gripping feet and complete branch support.

Juvenile: a recent fledgling in roughly the first week after leaving the cavity, not a newborn and not a capable adult-like flyer. Pale greyish-white to light brown mesoptile with dense soft diffuse barring, pinkish/fleshy eyelid rims, dark eyes, short incomplete tail, developed but fully folded wings. The juvenile wing pattern must be soft, irregular and down-softened, never crisp adult rows or regular spotted coverts. Pose it cautiously crouching and side-stepping on a broad low mossy log under dense cover: both feet plus lower breast/belly visibly supported, one folded wing held only slightly away for balance, no spread wing, no takeoff, no flight, no unsupported high perch. The log must visibly support the body.

Environment: shaded deciduous woodland, ivy/moss and a plausible dark tree hollow behind the family, dry woody substrate, concealed low understory. Keep the background quiet enough for scientific comparison. Warm dusk rim light, soft volumetric depth, tactile feathers, expressive but anatomically credible owl proportions. No prey, eggs, water, snow, ropes, text errors, extra captions, watermark or logo.

## Expected review checklist

- exact title, labels and count;
- untufted adults, dark eyes, yellow bill, same morph;
- no exaggerated sex-size rule;
- juvenile formed folded wings but diffuse non-adult pattern, short tail and fleshy eye rims;
- cautious low locomotion with complete natural support and no flight claim;
- cavity woodland environment; no fabricated newborn detail.


## Image review and iteration

- Initial 1536×1024 render and 600×760 juvenile crop were actually opened. Exact title/labels/count, untufted dark-eyed adults, same brown morph, restrained size difference, gripping feet, low juvenile support and cavity woodland passed.
- Problem: the juvenile folded wing had crisp white spots and orderly adult-like remige rows.
- Evidence: Mikkola supports diffuse juvenile mesoptile; the telemetry studies support poor early locomotion, not deletion of a formed post-fledging wing.
- Modification: one targeted imagegen edit removed regular spots/rows and softened the wing texture while preserving its folded formed structure.
- Recheck: full edited image and crop reopened; irregular down-softened wing, short tail, fleshy eye rims, both feet/lower body support and no flight pose pass. Result `PASS_WITH_LIMITATIONS`; science false.
- Transfer error caught before credit: initial generated JPEG blob was shorter than the local file; archive replaces it with a complete 674881-byte JPEG and fixed readback remains mandatory.

## Archive verification

Fixed commit `afa285df8c801b83605af9038a16a03ecd8fa45e` was read back as a non-truncated 1794-entry tree. Concept, complete repaired generated JPEG, reviewed JPEG and juvenile crop matched exact paths, blobs and byte sizes; the source-index blob and all required text records were reopened. Cycle result: VERIFIED; scientific verification remains false.
