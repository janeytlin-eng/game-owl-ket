# #61 Buffy Fish Owl — *Ketupa ketupu* — v4 research and design boundary

- **Accessed:** 2026-10-30
- **Action:** SCIENCE_REVISION; v1–v3 preserved.
- **Current / historical names:** current *Ketupa ketupu*; historical combination *Bubo ketupu*; protonym *Strix ketupu*.
- **Target:** early Sungei Buloh bird's-nest-fern nestling, age estimated around two weeks; science false.

## Sources actually read

### BFOW-NPARKS-BIODIVERSITYSG-2026 — new
- **Title / institution / date:** “Buffy Fish Owl” / BiodiversitySG, National Parks Board Singapore / updated 29 May 2026.
- **URL:** https://biodiversitysg.nparks.gov.sg/our-biodiversity/birds/raptors/buffy-fish-owl/
- **Sections read:** identifying features; habitat and ecology; no page numbers on the web page.
- **Facts:** warm buffy-brown plumage, thick dark vertical chest streaks, bright yellow eyes, prominent outward-pointing ear tufts; mangroves, forested streams and reservoir edges; bare featherless legs with fish-gripping soles.
- **Limits:** adult-oriented institutional synthesis; no sexed measurements or juvenile feather chronology.
- **Design use:** adults have fully bare lower legs/toes and near-equal display scale; no invented adult sex ratio.

### BFOW-BESG-NEST-2016 — reused and reopened
- **URL:** https://besgroup.org/2016/05/03/buffy-fish-owl-nesting-in-a-birds-nest-fern/
- **Sections read:** complete photo-sequence text and captions; no page numbers.
- **Facts:** one chick in a living *Asplenium nidus* at Sungei Buloh; the 25 March chick rested and sometimes shifted position, was covered in down; adults watched from nearby trees.
- **Limits:** hatch date and exact age unknown; photographs are one sequence, not a population-wide feather series.

### BFOW-BESG-FLEDGE-2016 — reused and reopened
- **URL:** https://besgroup.org/2016/05/13/buffy-fish-owl-the-chick-has-fledged/
- **Sections read:** article text and captions; no page numbers.
- **Facts:** early chick between fern-frond bases was estimated about two weeks and covered with white down; a separately described roughly six-week branch bird had adult-like feathers and preflight wing-stretch behavior.
- **Limits:** ages are retrospective estimates relying partly on secondary incubation/fledging figures; exact hatch day and continuous chronology are not measured.

### BFOW-SBG-BREED-2016 — reused and reopened
- **URL:** https://singaporebirdgroup.wordpress.com/2016/04/30/first-nesting-record-of-the-buffy-fish-owl/
- **Sections read:** full dated field account; no page numbers.
- **Facts:** 25 March chick approximately two weeks after discovery; one month later fully feathered; on 25 April it was outside the fern and perched on a nearby branch, with wobbly steps reported.
- **Limits:** “about two weeks” is time since discovery, not a known hatch age; the short flight is inferred from relocation.

### Uploaded-guide check
No page-numbered Heimo Mikkola extract for #61 was accessible in this execution context; no page fact was invented.

## Corrected inference and design boundary

- V3's early-versus-late separation is retained. V4 adds an official adult bare-leg gate and does not transfer the later branch bird's adult-like plumage or movement ability into the early chick.
- Adults: warm buff-brown, yellow eyes, outward tousled tufts, pale brows, thick vertical chest streaks, barred wings/tails, fully bare yellowish legs/toes. Sexes near-equal because no quantified display ratio was verified.
- Juvenile: one unsexed, age-estimated early nestling deep between bird's-nest-fern frond bases; loose white/cream down, no ear tufts, only tucked down-covered wing buds, hidden tail, low resting/slightly shifting posture, full substrate and frond support.
- Unknown: exact hatch age, continuous feather geometry, first-flight threshold, sexed measurements and subspecies transfer.
- Target result: PASS_WITH_LIMITATIONS; scientifically_verified=false.

## Full imagegen prompt

```
Create one polished landscape 3:2 natural-history concept plate for an owl electronic-pet prototype. Exact top title: “61 · BUFFY FISH OWL · Ketupa ketupu”. Exactly three birds in one coherent Sungei Buloh mangrove/stream-edge scene: adult male on the left, early nestling in the center, adult female on the right. No extra birds and no other text.

Adults: Buffy Fish Owls, warm buff-brown, bright yellow eyes, black bills, prominent outward-pointing tousled ear tufts, pale brows, thick dark vertical chest streaks, barred folded wings and tails. Legs and toes clearly bare and yellowish with strong dark claws; do not feather the legs. Adults near-equal in apparent height and bulk; no conspicuous female enlargement.

Juvenile: one unsexed early nestling based on the 25 March 2016 Sungei Buloh bird's-nest-fern sequence, estimated around two weeks but exact age unknown. Loose white-to-cream natal down dominates the whole body; round downy head with no ear tufts; tiny tucked down-covered wing buds only, no formed remiges, no dark structured wing panel, no adult barring and no visible long tail. The chick rests very low deep between the bases of living bird's-nest-fern (*Asplenium nidus*) fronds in trapped leaf litter/humus; body and both feet fully supported and mostly nestled, not standing upright, not on a branch, not flying. Alert but calm, perhaps a slight weight shift.

Environment: living bird's-nest fern mounted high in a rain tree in humid Sungei Buloh wetland forest, mangrove/stream edge suggested behind; adults on separate sturdy nearby branches watching the fern. Natural overcast tropical light, richly textured painterly realism matching prior owl-pet concept plates; identifying anatomy crisp, not chibi.

Preserve scientific uncertainty: do not add day-age labels, sex callouts, explanatory boxes, leader lines or arrows. Do not show the later six-week adult-feathered branch bird, adult-like juvenile wings, ear tufts, long tail, unsupported pose, exaggerated adult sex size, orange eyes, feathered legs, prey, watermark, border or extra typography.
```

## Iteration hypothesis

The recurring failure mode is that an early down-dominant chick receives ear-like projections and a dark structured wing. The prompt therefore binds the juvenile to deep fern support and explicitly forbids both features while separately specifying the adults' official bare-leg diagnostic. Effect must be verified by opening the generated original and derivative; this is a production hypothesis until then.


## Actual production review — 2026-10-30

- IMAGE_GENERATED: 50.6 s. The 1536×1024 original was opened; exact title/count, adult diagnostics and bare legs, low white-down chick, absent juvenile tufts/formed wing/tail, fern support and wetland context passed.
- REVIEWED: same original and 680×453 derivative opened; no edit required. PASS_WITH_LIMITATIONS; exact hatch age and continuous feather/flight chronology remain unknown.

## Iteration rule result

- **Hypothesis:** explicit deep-fern support plus prohibitions on juvenile ear tufts and structured wings would prevent the recurring early-chick maturity drift.
- **Applied:** full prompt separated the early chick from the later branch bird and independently gated adult bare legs.
- **Verified:** the first render passed at full and derivative sizes without editing. This verifies the prompt control for this plate only; it does not establish exact plumage chronology. Science false.

- **Fixed readback:** archive `d1c49366e7bd9746bd91a91383619d531f23663f` returned exact image paths, blobs and sizes, a non-truncated tree and 567/566/557 manifests. Batch 5/6; science false.
