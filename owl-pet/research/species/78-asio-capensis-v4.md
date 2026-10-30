# #78 Marsh Owl — *Asio capensis* — v4 research/design record

- Batch/cycle: `2026-10-31T0134+0800` · 2/6
- Action: SCIENCE_REVISION; v1–v3 retained
- Selected stage: older mobile dependent near fledging, age not asserted in the image label
- Scientific status: concept calibration only; `scientifically_verified=false`
- Stage: RESEARCH_READY at 2026-10-31T02:28:40+08:00

## Evidence actually reused

- **MAR-ANSARA-ROSS-2008** — primary sexed morphometrics. Gauteng males averaged 297.59 g and 148.8 mm tail (n=21); females 329.07 g and 156.3 mm tail (n=11). Mass and tail differed, flattened wing means were nearly identical, and no dichromatic sex distinction was found. Supports modest female fullness/tail direction, not a fixed standing-height ratio.
- **MARSH-BIOEXP-2026** — Biodiversity Explorer/Roberts synthesis, breeding section: young leave the ground depression at about 14–18 days and crawl into nearby cover before flight. Supports mobile ground dependence but not a day-specific feather geometry.
- **MARSH-OWLPAGES-2020** — species account, breeding section: expert summary gives later fledging context around 29–35 days. This is not treated as a primary daily feather series.
- **WHSO-MIKKOLA-2013** — printed pp.518–519 / PDF pp.520–521: adults have dark eyes, pale dark-rimmed face, tiny tufts and feathered legs; mesoptile described as buff-brown/barred with much darker face and black ruff. The uploaded guide was not directly exposed in this runtime; page facts were reused from the repository’s prior actual-read record.
- **MAR-BIRDLIFE-SA-2025** — official Red Data Book species account: current species-level identity, monotypic treatment, tall grass/weeds and ground-nesting ecology; no juvenile feather chronology.
- **MAR-HANANE-CHERKAOUI-2014** — primary Moroccan nest report, printed pp.46–49. Demonstrates nesting plasticity for the older `tingitanus` name but is not used to transfer southern-African juvenile plumage.

## Active research attempts this cycle

Two external search batches using current name, old named form and author combinations, plus direct opens of the Owl Pages and Biodiversity Explorer URLs, returned empty error payloads. They are logged as attempts only and add **zero** verified sources.

## V3 visual review and correction

The fixed v3 reviewed master was actually opened. Adult identity, dark eyes, grassland setting and natural support pass. The central bird reads as an older dependent juvenile, but its wing includes crisp repeated pale spots and adult-regular layered vanes, and the exact “29–35-day” image label is more precise than the accessible evidence warrants.

V4 therefore:
1. retains a developed but soft folded wing and short tail appropriate to an older mobile dependent;
2. replaces crisp adult rows with sparse irregular soft barring;
3. uses the label **OLDER DEPENDENT JUVENILE**;
4. keeps adult crown heights comparable and expresses female direction only through modest fullness/tail length;
5. retains bilateral ground/grass support and no flight pose.

Exact individual age, continuous feather-tract chronology, first-flight threshold, universal sex ratio, named-form geometry and population transfer remain unknown.

## Full imagegen prompt

```text
Use case: scientific-educational
Asset type: owl-pet species concept plate
Input image: Image 1 is the fixed v3 plate and is a style/layout reference only; do not copy its over-regular juvenile wing pattern.
Primary request: create a polished 3:2 horizontal natural-history plate in the repository's established realistic-cute style.
Text (verbatim): title “MARSH OWL”; italic scientific line “Asio capensis”; bottom labels “ADULT MALE”, “OLDER DEPENDENT JUVENILE”, “ADULT FEMALE”.
Composition: exactly three Marsh Owls, adult male left, juvenile centered and clearly lower, adult female right. Keep all feet visible and anatomically supported.
Adults: rounded head; tiny ear tufts barely visible/flattened; very dark brown eyes; dark horn bill; pale buff facial disc with distinct dark rim; plain earth-brown upperparts with subtle fine mottling; pale buff underparts with narrow dark streaks; feathered legs. Female only modestly fuller and slightly longer-tailed than male, with comparable crown height and overlapping proportions; do not invent a fixed height ratio or strong sex-linked colour difference.
Juvenile: an older mobile dependent near fledging, not a hatchling and not a miniature adult. Buff-brown barred mesoptile; distinctly darker face and blackish ruff; fluffy crown; developed but still soft folded wings; short visible tail. Wing marks are sparse, soft and irregular, without crisp adult scapular spots, repeated pale covert rows or a long fully layered adult remige fan. The juvenile takes a cautious low step through flattened grass with both feet naturally supported; no sustained flight or hunting pose.
Scene: southern African rank grassland/wetland edge; flattened grass and a shallow dry-leaf ground depression under an arched grass canopy nearby. Adults stand on stable low earth/grass supports.
Lighting/style: soft overcast natural light, muted tan/olive palette, realistic feather texture with gentle character appeal.
Constraints: exactly three birds; exact readable text; no eggs, extra birds, extra labels, border, logo or watermark. Do not show the juvenile with adult-regular wing rows, adult ear tufts or unsupported standing.
```

## Source delta

- New verified sources: 0
- Reused sources: 6
- Corrected design inference: 1
