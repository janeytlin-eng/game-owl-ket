# #129 *Megascops hoyi* v5 — visual/scientific review

- Run: `20261112T024500+0800-cycle-5`
- Reviewed: 2026-11-12T03:33:00+08:00
- Result: `PASS_WITH_LIMITATIONS`
- Scientific verification: false
- Initial: `owl-pet/production/generated/129-megascops-hoyi-v5-initial-original.png`
- Final: `owl-pet/production/generated/129-megascops-hoyi-v5-final-original.png`
- Reviewed master: `owl-pet/production/reviewed/129-megascops-hoyi-v5-reviewed-master.png`

## Actual views

The v4 plate, v5 initial full plate, edited full plate, and separate adult-male, fledged-juvenile and adult-female crops were actually opened. The final plate is a 1536×1024 RGB PNG; each crop is 512×1024.

## Issue — evidence — modification — recheck

The initial central juvenile had a clearly adult-yellow iris. No source used in this cycle establishes the species' juvenile iris chronology, so that colour was an unsupported claim. One targeted imagegen edit changed only the visible juvenile iris to a dark, shadowed, non-diagnostic colour while preserving the eye anatomy, title, labels, count, body proportions, plumage, cavity, support and lighting. The edited full plate and all three final crops were re-opened: the juvenile iris can no longer be confidently assigned a colour, and no collateral change was found.

## Final checks

- Identity: `PASS_WITH_LIMITATION` — compact brown-morph screech-owls, short low ear tufts on adults, pale-yellow adult irises, irregular shaft marks, broken pale scapular band, barred wing/tail and muted soft-parts are present; this remains an illustration rather than a diagnostic specimen plate.
- Adult sex treatment: `PASS_WITH_LIMITATION` — adults are near equal; the two type specimens are not generalized into a species-wide female-larger rule.
- Juvenile stage: `PASS_WITH_LIMITATIONS` — label is `FLEDGED JUVENILE · AGE UNKNOWN`; residual loose fluff, no visible ear tufts and formed but soft/irregular folded wing and short tail read as later fledged young without claiming a day age.
- Juvenile action/capability: `PASS` — stationary supported perch only; no flight, jump or unsupported locomotor claim.
- Support/anatomy: `PASS` — exactly three complete birds and all six feet are visibly supported; no duplicated limb or extra bird.
- Text/order: `PASS` — exact title, subtitle and left/centre/right role labels are present.
- Habitat/nest: `PASS_WITH_LIMITATION` — the Yungas/laurel cavity is consistent with the single Chasquivil record, but its geometry and feather lining are not treated as universal.
- Taxonomy: `PASS` — current *Megascops hoyi* and old/original *Otus hoyi* mapping retained.

## Remaining unknowns

Exact juvenile age and sex; juvenile iris and bill chronology; continuous feather sequence; first-flight threshold; independence timing; population-level adult sex-size direction; universality of the recorded tree species, cavity geometry and feather lining.

## File evidence

- Final SHA-256: `39ad4e0c90552eaf81a97b7c556981b7ad18c0c2d0f58a80cc7abbed6710b0ce`; 2,817,626 bytes; Git blob `eb568ce25c589b2aa2e08b23752238a7caf2a738`.
- Adult male crop: 970,643 bytes; Git blob `1fb6d7348c0c43d493af0d24947f4885c82ce9ee`.
- Fledged juvenile crop: 988,209 bytes; Git blob `8e3f208199b875b4311409e4b5a012e69003f1f4`.
- Adult female crop: 866,078 bytes; Git blob `7b088609dbfae85429064a2f5499b6124f2ca756`.
- Imagegen invocations: 2 (one initial generation, one targeted edit); edit count: 1.

