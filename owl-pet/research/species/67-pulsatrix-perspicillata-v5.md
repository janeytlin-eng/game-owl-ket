# #67 *Pulsatrix perspicillata* v5 — cavity training / overlapping adult scale boundary

- Current name: *Pulsatrix perspicillata* (Spectacled Owl).
- Historical name: *Strix perspicillata* Latham, 1790.
- Action: SCIENCE_REVISION; unique increment 0; v1–v4 preserved.
- Research ready: 2026-11-05T16:50:00+08:00.
- Uploaded Mikkola file: not accessible in this execution; repository page extraction was reused, not claimed as newly read.

## Sources actually read

1. New `SPO-GOMES-ETAL-2011-P4-5`: Gomes, Santos, Machado & Moura (2011), “Acompanhamento do desenvolvimento de ninhego de *Pulsatrix perspicillata* ...”, *Atualidades Ornitológicas* 163:4–5. The two-page report monitored one chick in a dead-tree cavity every three days. The cavity was 2.20 m high, 60 cm diameter and 80 cm deep. The chick remained inside during all monitoring for about 50 days; from early November it stretched its wings upward and flapped but did not take off. Figures caption it at about 20, 23, 44 and 51 days. One individual/site does not define all nests or an exact universal day-stage.
2. New `SPO-CORREA-2016-P55-56-179-187`: Corrêa (2016), University of São Paulo MSc thesis, pp.55–56, 179 and 186–187. Adult specimen tests show female wing, tail and culmen lengths significantly larger, while tarsus and supercilium were not; observed ranges overlap. The thesis also documents white juvenile plumage, a dark facial disc through about six months, adult-like flight feathers plus first-generation barred coverts, and geographic/age/sex variation in barring.
3. Reused `SPO-WETMORE-1968-P164`: species-specific first-stage description: buffy-white body down and dark face can coexist with formed brown barred wings/tail and barred pale coverts/back. This blocks the generic “erase all formed juvenile wings” rule.
4. Reused `SPO-BOUGLOUAN-2026` and `SPO-PEREGRINE-2026` for adult identity and the broad white-bodied/dark-mask juvenile appearance only. Their generalized branch-leaving statement does not override the directly observed no-takeoff behavior of the selected cavity-stage individual.

## Fact / inference / unknown boundary

- **Fact:** one monitored chick stayed inside its cavity for roughly 50 days and practised wing stretching/flapping without takeoff. **Design inference:** depict an age-unknown older cavity-stage chick on the cavity floor/rim, one wing modestly lifted for practice, both feet/body supported; no branch-perching, jump or flight claim.
- **Fact:** species-specific juvenile evidence supports white down/dark face with formed barred wing/tail feathers. **Design inference:** retain soft brown transverse bars and formed compact flight feathers; do not turn the chick into a newborn with white wing buds, and do not use adult-regular hard spots.
- **Fact:** museum morphometrics support female-longer wing/tail/culmen directions with overlapping ranges, but not a fixed standing-height ratio. **Design inference:** adult female modestly fuller/longer, close crown height, same plumage identity.
- **Unknown:** exact depicted age, sex and subspecies; continuous feather sequence; first takeoff/competent flight; range-wide standing-height ratio; universality of this cavity; precise relation between photographed day and Wetmore's first-stage description. Science remains false.

## Complete imagegen prompt

```text
Create one polished horizontal 3:2 owl electronic-pet concept plate in the established semi-realistic hand-painted natural-history game-art style of the owl-pet series: warm painterly texture, anatomically credible and gently charming, no photorealism, no pixel art, no split panels and no border. One coherent humid Neotropical forest scene around a natural dead-tree cavity. Exactly three Spectacled Owls (*Pulsatrix perspicillata*), clearly separated and naturally supported. Add a small clean title “SPECTACLED OWL”, italic subtitle “Pulsatrix perspicillata”, and unobtrusive labels “ADULT MALE”, “CAVITY-STAGE JUVENILE — AGE UNKNOWN”, and “ADULT FEMALE”; no other text.

Adults flank the cavity at similar camera distance, untufted, bright yellow eyes, creamy horn bills, dark chocolate-brown head/back, bold pale cream spectacles and white throat, dark broad upper-breast bib, warm buff unbarred belly, brown barred wings and tail. Based on adult specimen morphometrics, make the female only modestly fuller and slightly longer-winged/tailed than the male while keeping crown height close; do not invent a fixed standing-height ratio or sex-linked colour. Both adults grip separate mossy branches with both feet visibly supported.

Central juvenile is low at the floor/rim of a deep natural dead-tree cavity, an older cavity-stage bird of exact age unknown. White to buffy-white soft body down, dark chocolate heart-shaped facial disc, bright yellow eyes and pale bill. Preserve the species-specific exception: compact formed brown wing and tail feathers with soft irregular transverse pale bars, plus barred first-generation coverts transitioning into white down. Do not erase the wings into newborn buds and do not use round polka dots, hard adult-perfect spot rows or an adult dark body. Show one compact wing modestly lifted in a documented practice stretch while both feet/body remain firmly supported inside the cavity; no takeoff, hovering, branch-perching, jumping or implied competent flight.

Environment: humid lowland/gallery forest with a dead tree cavity, moss, vines and soft filtered light. Use the documented cavity only as one monitored example, not a universal nest blueprint. No eggs, prey remains, logging machinery, road, humans, extra animals or extra birds. Exact three birds, correct labels, all support contacts anatomically plausible, no watermark or logo.
```

## Review and iteration rules

- Preserve the barred-wing first-stage exception; “juvenile = short white wing buds” is wrong for this selected stage.
- Correct v4's branch-perching implication: selected juvenile remains in-cavity and wing practice never becomes takeoff.
- Female may be modestly fuller/longer but never a fixed giant. Labels, not plumage, encode sex.
- Verify exactly three birds, readable text, adult spectacles/bib, juvenile white body/dark face, transverse bars rather than spots, and all feet/body supports.

## Actual image review — 2026-11-05

- Generated master: `owl-pet/production/generated/67-pulsatrix-perspicillata-v5-generated-master.png`; 1536×1024; 3,237,058 bytes; SHA-256 `71222f42b9dd27f2f16af32007cd4ac0979c1cd665d958a33b7fa8ae1e97406a`; imagegen wait 68.6 s; edit count 0.
- Opened full frame and adult/juvenile crops. All three birds and their supports are present. Adult identity and overlapping-scale direction pass. The cavity juvenile is white/dark-faced, fully supported and raising one transversely barred formed wing without takeoff.
- The mature-looking wing was not edited into generic white buds because Wetmore and Corrêa specifically support formed barred juvenile wings in this species. The exact age-stage synthesis remains uncertain, so this is `PASS_WITH_LIMITATIONS`, not scientific approval.
- Review record: `owl-pet/research/reviews/67-pulsatrix-perspicillata-v5-review.md`.
- Immutable archive verification: commit `a462f51b1ff42f80f673ab9faa835b641e9ef23c`, tree `e2a5bc2bf29abda4a77f58858069e744bcc16186`; non-truncated 3,068-entry readback matched all 16 required paths and exact full/crop blobs and byte sizes.
