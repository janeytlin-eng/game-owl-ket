## 2026-11-07 — #149 *Ninox odiosa* v3 historic text corrected a modern-summary simplification

**Problem:** v2 translated general summaries into a broad full-width dark upper-breast band.
**Evidence:** the sexed 1879 adult male account instead describes a white, narrowly brown-streaked underside with chocolate breast sides mottled white.
**Applied rule:** when a full specimen account becomes available, prefer its localized pattern map over a generalized secondary summary; preserve field-photo color range but do not transfer unsupported sex/juvenile traits.
**Validation state:** applied to v3 prompt; pixel review pending.

## 2026-11-07 — #148 *Ninox rumseyi* v3 sex-size correction

**Problem:** v2 treated the adults as near-equal because the species description lacked a quantified sex ratio.

**Evidence:** Jakosalem et al. measured nine adults; four brood-patch birds were consistently smaller and assumed female, while five were assumed male (wing 175–181 vs 184–190 mm; tail 91–99 vs 100–109 mm). The sex assignment remains inferential.

**Applied rule:** when species-specific primary measurements give a direction, use it cautiously even when it reverses a common owl stereotype; encode a subtle male-larger direction and record the sexing method. Do not generalize across taxa.

**Validation state:** applied and visually checked after one targeted edit. The corrected plate retains a subtle male-larger direction; PASS_WITH_LIMITATIONS, not scientific verification. Juvenile chronology remains unknown.

#147 卡米金鹰鸮 / Camiguin Boobook

- Scientific name: *Ninox leventisi*
- Taxonomy: Rasmussen et al. 2012; historically included in the Philippine hawk-owl complex.
- Scope: Camiguin Island endemic; treated as a full species in the current 251-species production scope.
- Concepts: [v1](../../design/concepts/147-ninox-leventisi-v1.png) · [v2 science revision](../../design/concepts/147-ninox-leventisi-v2.png)
- Scientific verification: false

## Evidence actually read

- CAM-EBIRD-2026: Cornell/eBird identification page. Medium-sized, earless Camiguin endemic of remnant broadleaf forest; warm brown, uniformly finely barred plumage, pale shoulder bar, long facial whiskers, white throat, pale yellow eyes.
- CAM-BIRDLIFE-2026: BirdLife Data Zone species account. Confirms restricted Camiguin distribution and conservation context; dynamically rendered page did not expose detailed breeding or juvenile data.
- CAM-RASMUSSEN-2012-LEAD: Rasmussen et al., *Forktail* 28:1–20. Search/abstract and diagnosis excerpt read; full PDF retrieval timed out in this run. Supports species split and diagnostic gray to very pale yellow-green iris, but is retained as a partial-read source, not complete verification.

## Design boundary

Adults are shown with near-equal scale because no reliable visual sexual dimorphism or sexed linear ratio was established. Diagnostic pale gray-green eyes, white throat, pale shoulder bar, warm brown fine barring, yellowish-olive bill and mustard bare toes are retained. The juvenile sequence and nesting are undocumented in accessible species-specific evidence, so v1 uses an explicitly age-unknown older juvenile: fluffy, shorter rounded wing/tail, reduced crisp barring, alert two-foot branch support. No hatchling, flight, nest cavity interior or exact age claim.

## Review

Final image viewed after two targeted juvenile-wing edits. The first image had adult-like long layered remiges; v2 softened them, and the final edit shortened the folded wing further and removed crisp adult spot rows. Three birds, labels, anatomy, support and habitat are intact. Exact juvenile feather sequence, sex ratio, bill/toe variation and breeding ecology remain unknown.

## 2026-11-01 v2 science-revision evidence and review

- Primary Rasmussen et al. 2012 diagnosis (printed pp.15–16) was read in full for this taxon. It corrects v1 toward large, full/lax adults with long deep bills, no pale supercilium, gray/whitish to very pale yellow-green irides, extensive white throat, bold upperpart bars, broad irregular underpart bars, mustard/olive bare parts and mostly pale claws with dark tips.
- The paper combines sexes for analysis and explicitly defers sexual-size work; v2 therefore keeps near-equal adult scale. It also excludes immatures from diagnoses because data are sparse, allowing only the general boundary “fluffier and less well marked.”
- Adult field-photo pixels and metadata (Cheta Chua 2025, Wikimedia Commons) were viewed as a secondary appearance check; ITIS TSN 1063268 and BirdLife were used only for current-name/range context.
- Built-in ImageGen generated v2, then one targeted edit corrected mostly dark adult claws and shortened/softened the older immature wing. Full image and two crops were actually viewed.
- Result: `PASS_WITH_LIMITATIONS`, scientific verification false. The age-unknown older immature keeps eyes closed, tail hidden and both feet supported; exact age, iris development, flight, nest, sex-size direction and continuous feather sequence remain unknown.
- Detailed evidence and complete prompts: [research record](../../research/species/147-ninox-leventisi-v2.md) · [run](../../production/runs/20261101T002622+0800-cycle-1.md).


## v3 — 2026-11-07 science revision

- Rasmussen et al. 2012 pp.15–16 re-read; ZOBODAT 2014 p.108 added for type metadata. Adults remain near equal because types are female and no sex-size ratio is established.
- Full plate and two crops passed: long deep bills, pale irides, white throats, barred coverts, pale claws/dark tips, and all supports visible. Juvenile remains AGE UNKNOWN with wing/tail concealed.
- PASS_WITH_LIMITATIONS; scientifically_verified=false; edit_count=0.
- Research: `research/species/147-ninox-leventisi-v3.md`; review: `research/reviews/147-ninox-leventisi-v3-review.md`; concept: `design/concepts/147-ninox-leventisi-v3.png`.


## v3 verification

- Immutable archive `26db941a0a53cc277fcd41ac86aba0311153eca8` / tree `ef17a4abc2fff919376524e2e004d2bd99c41727` read back by exact paths; concept/generated/reviewed resolve to `cdf02e5446f1372027db00bc0b7e9aabc652790c`; crop and text paths resolved.
- PASS_WITH_LIMITATIONS; science false; ledger pending.


## v3 ledger

- Verification `4d0273366ec170d90b45b0820cdf029396acbf8d` read back after archive `26db941a0a53cc277fcd41ac86aba0311153eca8` / tree `ef17a4abc2fff919376524e2e004d2bd99c41727`.
- Cycle 3 credited once; batch 3/6, next 4; unique 176/251; science false.


## #149 *Ninox odiosa* v3 — 2026-11-07 science revision

- Gould & Sharpe 1884 sexed-male specimen account was read and corrects the generalized dark chest-band shorthand: underbody is predominantly pale with narrow brown shaft-streaks and chocolate breast sides mottled white; separate white brows, yellow iris and irregular scapular/covert white marks are retained.
- ITIS TSN 555491 records the current name. IUCN and an adult field photograph were reused for range/appearance context.
- Female size/plumage and the juvenile sequence remain unknown; adults were kept near equal and the juvenile age is not assigned.
- Initial generated juvenile wing was too long, crisp and adult-spotted. One targeted edit shortened and softened it; edited full image and two crops were viewed.
- Result: PASS_WITH_LIMITATIONS; scientifically_verified=false; edit_count=1.
- Research: `research/species/149-ninox-odiosa-v3.md`; review: `research/reviews/149-ninox-odiosa-v3-review.md`.


## #149 v3 verification

- Immutable archive `7176fb71b2990e89b73582ada698b40853b87f6d` / tree `7270e082effd7f0f906a3b9f8cabcd312cb38326` resolved 16 required paths; five image paths matched exact expected blobs and the three manifests parsed at 757/758/748.
- PASS_WITH_LIMITATIONS; scientifically_verified=false; ledger credit pending.


## #149 v3 ledger

- Verification `a0ef5804bea7730c21a105ce93a626a0d9f51b04` was read back after immutable archive `7176fb71b2990e89b73582ada698b40853b87f6d` / tree `7270e082effd7f0f906a3b9f8cabcd312cb38326`.
- Cycle 5 credited once; batch 5/6, next 6; unique 176/251; revision +1; scientifically_verified=false.


## #150 *Ninox variegata* v3 research-ready — 2026-11-07

- Voisin & Voisin 2011 printed p.25 was read: the type series contains two New Ireland syntypes, MNHN 2010-278 and 2010-279, not one. MNHN 2010-278 metadata records sex and age as indeterminate.
- Adult visual boundary reuses the secondary barred/short-tailed/heavy-tarsus synthesis, but type records do not justify sex direction or juvenile traits.
- Adults therefore remain near equal. Juvenile is AGE UNKNOWN, closed-eyed, supported, with mature wing/tail topology suppressed.
- Full prompt: `production/PROMPTS_FULL.md`; research: `research/species/150-ninox-variegata-v3.md`.


## #150 v3 visual review

- Full 1536×1024 plate plus juvenile and adults/support crops were viewed. Adult barred identity, near-equal scale, exact labels/count and all six support contacts passed.
- Juvenile is AGE UNKNOWN, eyes closed, down-soft, short-winged/body-blended and tail-concealed. No edit required.
- PASS_WITH_LIMITATIONS; scientifically_verified=false; edit_count=0.


## #150 v3 verification

- Immutable archive `99735154d84ff945a4c9ab5d21b59bb80434156a` / tree `f20fbb806bf8e03b04880371edae46205cfc265e` resolved 16 required paths; five image blobs matched and manifests parsed 758/759/749.
- PASS_WITH_LIMITATIONS; scientifically_verified=false; ledger credit pending.


## #150 v3 ledger

- Verification `92df887e6da967619a4b6aa9780627e99bbdd7d6` read back after archive `99735154d84ff945a4c9ab5d21b59bb80434156a` / tree `f20fbb806bf8e03b04880371edae46205cfc265e`.
- Cycle 6 credited once; batch 6/6 COMPLETE; unique 176/251; revision +1; scientifically_verified=false.


## 2026-11-07 — #151 *Athene jacquinoti* v3: type photograph corrects “plain belly” simplification

**Problem:** v2 compressed secondary descriptions into a nearly plain cream belly.
**Evidence:** the actual male holotype image (MNHN-ZO-2010-270, age indeterminate) visibly retains substantial irregular brown barring across cream-white underparts; a living eBird image supports orange eyes and compact support but has no sex/age metadata.
**Applied rule:** specimen photographs can correct zone and irregularity of adult pattern, but museum mounts and unsexed field images cannot establish live posture, sex contrast or development.
**Validation state:** applied to the v3 prompt; pixel review pending. Scientific verification remains false.


## #151 v3 immutable archive verification

- Archive `ae92217d2c5028fe76a0dfef7257b0fbec35fbb9` / tree `f9fb81d80f500381e8e13e2159c103cf24b95be6` resolved 17 required paths; six binary paths matched exact expected Git blobs. The juvenile crop required a full base64 retry after metadata-only read omission, then matched `dbf7e990f82a09403eb9b95291e78f123d0e06a4`.
- Manifests parsed 759/760/750 with one #151 v3 entry each. PASS_WITH_LIMITATIONS; scientifically_verified=false; ledger credit pending.


## #151 v3 ledger

- Verification `a1324392ee72514fc053f0bcf09e60e349c53d2e` / tree `d2790e4d373c0ea58f15e393b5ff1db6195f68bc` read back after archive `ae92217d2c5028fe76a0dfef7257b0fbec35fbb9`.
- Cycle 1 credited once; batch 1/6, next 2; unique 176/251; revision +1; scientifically_verified=false.
