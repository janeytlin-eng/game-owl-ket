# #70 *Ninox strenua* v5 — RESEARCH_READY

- Batch/run: `20261105T153530+0800` / `20261105T173620+0800-cycle-6`
- Action: SCIENCE_REVISION; v1–v4 and historical confirmation records preserved; unique increment 0.
- Research completed: 2026-11-05T17:44:00+08:00.
- New verified source: 1; re-read verified sources: 3; reused verified sources: 2; corrected design boundaries: 3.
- Uploaded Mikkola guide: unavailable in this execution. Repository-verified extraction `WHSO-MIKKOLA-2013`, printed pp.450–451 / PDF pp.452–453, is reused without claiming a fresh page read.
- Target status: PASS_WITH_LIMITATIONS; `scientifically_verified=false`.

## Source facts

### New: POWERFUL-COOKE-ETAL-2020

- Cooke, Rendall, Weston, Porch, Bradsworth & White (2020), “Photography can determine the sex of a predator with limited sexual dimorphism: A case study of the powerful owl,” *Global Ecology and Conservation* 22:e00959. DOI: https://doi.org/10.1016/j.gecco.2020.e00959 . Full open article text and Figs.1–6 read 2026-11-05.
- The authors call overall sexual dimorphism extremely limited. In 63 known-sex forward-facing alert images, the head-width/inter-nostril ratio separated sexes; males had the larger ratio. In 82 assessable images, female facemask feathers reached or slightly exceeded the horizontal head edge, whereas male facemask feathers stopped short. The paper cautions that posture and camera angle matter and that the male gap can be small.
- Design support: do not encode sex as a large height gap. Use comparable crown/support height, a subtly broader/full-bodied male, and a restrained front-view facial-mask boundary: female mask feathers reach the contour edge; male mask stops slightly short.
- Limits: this photographic method depends on direct forward alert posture and ratios; it is not a licence to invent exact pixel ratios in a stylised plate or to sex a sideways/slouched bird.

### Re-read: POWERFUL-MO-WATERHOUSE-2015

- Mo & Waterhouse (2015), *Australian Field Ornithology* 32:143–153, printed pp.143–153; pp.145–146 and Fig.1 re-read 2026-11-05 from author-uploaded full text.
- Two young left the hollow on 5 and 14 August; the second was observed flying out, crashed into a shrub, and was with the adults in treetops the next night. Both were first seen flying on 17 August and stayed in the gully until mid-October.
- Design support: a recent fledgling may carry developed folded wings/tail and be flight-capable, but should be shown perched with full two-foot support. The observed crash prevents converting fledging into polished flight competence.

### Re-read: POWERFUL-ABSA-2019 and POWERFUL-NSWSC-2008

- ABSA/HANZAB p.1: male/female wing, tail, bill, tarsus and toe ranges overlap; females are marginally smaller; post-juvenile adult-like change starts about 3–4 months after fledging.
- NSW Scientific Committee report pp.1–2: narrow pale dorsal bars, coarse V-shaped ventral chevrons, yellow-orange eyes, feathered legs and large yellow feet; initially whiter/downier young; large old-tree hollows, about two-month nestling period and months of post-fledging dependence.

### Reused: POWERFUL-MV-2026 and WHSO-MIKKOLA-2013

- Museums Victoria supports small broad head, yellow eyes, light-grey bill, narrow dorsal bars, coarse V-marks, feathered legs/large talons and white-headed lightly streaked young.
- Mikkola repository extraction supports the male-larger direction and white face/dark eye patches with barred growing wings in young birds, but not an exact age or fixed standing-height ratio.

## Evidence boundary and design decision

Problem in v4: the adult scale direction was restrained, but the plate did not apply the newly verified front-view facemask boundary that permits sex distinction without exaggerating height. V5 therefore keeps near-equal adult crown/support height, adds only a subtle broader male head/body direction, and differentiates the female by facemask feathers reaching the head contour while the male mask stops just short. This is the actual new evidence application.

The juvenile stage remains a recent fledgling immediately after hollow departure: white/downier crown and underparts, dark eye patches, sparse dark streaks, developed but softer barred folded wings and a short-to-moderate rounded tail. It can fly according to the selected field stage, but the image must show no launch, prey handling or unsupported action; both feet grip a stable hollow lip/adjacent branch.

Unknown: exact hatch age, the depicted bird’s sex, day-by-day feather-tract chronology, universal flight competence at first exit, stylised-image transfer of photographic facial ratios, and individual/population variation. These keep scientific status false.

## Complete imagegen prompt

```text
Use case: scientific-educational.
Asset type: owl-pet species concept plate, revision v5.
Primary request: Create a polished landscape 3:2 comparison plate in the established realistic-cute natural-history game concept style for the Powerful Owl.
Scene/backdrop: moist eastern Australian eucalypt gully, a huge old living eucalypt with a deep natural hollow, stable broad hollow lip and adjacent mossy branch, soft natural daylight.
Subject: exactly three Powerful Owls: adult male on the left, recent fledgling in the center, adult female on the right.
Composition/framing: full bodies, all feet visible and naturally supported, balanced triangular group. Both adults face almost straight forward in alert upright posture so the facial-mask boundary can be compared. The center fledgling sits slightly lower at the hollow lip, not flying.
Adult identity: no ear tufts; small broad head; prominent yellow-orange eyes; pale blue-grey bill; dark grey-brown upperparts with narrow irregular off-white bars, never round polka dots or broad zebra bands; white underparts with coarse dark grey-brown V-shaped chevrons, never horizontal waves; rounded barred tail; feathered legs; very large yellow feet and dark claws.
Adult sex evidence: sexual dimorphism is extremely limited. Keep adult crown heights and supports comparable. Male only subtly broader-headed and fuller-bodied; his facemask feathers stop slightly short of the outer horizontal head contour. Female is not taller; her facemask feathers reach or just meet the horizontal head contour. Do not create contrasting colour morphs.
Recent fledgling: newly out of the hollow and capable of short flight in the selected field stage, but quietly perched with both feet gripping. White/downier crown, face and underparts; dark patches around the eyes; sparse dark streaks; pale grey bill; developed folded wings with softer broader pale bars than adults; short-to-moderate rounded barred tail; residual fluffy down around head and shoulders. No adult chevron density.
Text, verbatim: title “POWERFUL OWL”; italic subtitle “Ninox strenua”; bottom labels “ADULT MALE”, “RECENT FLEDGLING”, “ADULT FEMALE”.
Constraints: exactly three owls; front-alert adult heads; subtle facial-mask-edge distinction; true adult V-chevrons and narrow irregular upperpart bars; juvenile remains white/downier and fully supported; natural eucalypt hollow context.
Avoid: extra birds, eggs, prey, ear tufts, large adult height gap, female-larger template, broad zebra bars, round wing spots, horizontal belly waves, adult-like juvenile chevrons, launch or flight pose, dangling or fused feet, invented exact age, decorative border, watermark, extra text.
```
