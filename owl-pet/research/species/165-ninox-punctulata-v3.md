# #165 *Ninox punctulata* v3 research and correction boundary

- Batch/cycle: `20261107T103800+0800` 3/6
- Run: `20261107T113400+0800-cycle-3`
- Prior v1/v2 preserved; status at checkpoint RESEARCH_READY
- Current name: *Ninox punctulata*; old combination *Noctua punctulata*
- Science status: false

## Fresh web research and corrected interpretation

### SPBO-OCONNELL-ETAL-2022-P291-292 — re-read primary full text and figure description
D. P. O’Connell et al., “Breeding records of the birds of south-east Sulawesi, Indonesia,” *Bulletin of the British Ornithologists’ Club* 142(3), 2022:278–301; DOI 10.25226/bboc.v142i3.2022.a2.
- Open full issue: https://boc-online.org/bulletins/downloads/BBOC1423-PDFa.pdf
- Actually read 2026-11-07: printed pp.291–292, especially species paragraph and Fig.3A/caption.
- Facts: a single juvenile was observed on Buton on 8 Aug 2013, found at the base of a large tree in lowland tropical forest near Labundobundo, possibly fallen; returned to the same location. Figure 3A is explicitly a dark, fluffy juvenile. The paper warns generally that juvenile records confirm breeding but age/location timing are uncertain because travel and juvenile-plumage duration vary.
- Correction: v2 correctly used a broad root and support, but its warm cream-brown, already strongly spotted juvenile and long organized wing are too adult-like relative to the direct figure description. v3 uses dark loose down, diffuse mottling, short buried soft wing and no flight/age claim.
- Limits: exact age, flight ability, iris, nest geometry and feather sequence remain unknown; the figure was reproduced as a paper panel and not calibrated for colour.
- Confidence: high for stage darkness/fluff and found-at-tree-base context; low for exact colour values and chronology.

### SPBO-SHARPE-1875-P183 — re-read historical adult female account
R. B. Sharpe, *Catalogue of the Birds in the British Museum*, p.183; Wallace Online scan: https://wallace-online.org/converted/supplementary/specimens/1875_BMbirds_WSPEC351.2.pdf
- Actually read indexed page text on 2026-11-07.
- Facts: deep chocolate-brown above with minute dull whitish-buff spots, larger on hindneck; white superciliary circle, cheeks and throat; white body center; narrow chocolate upper-chest bar; brown flanks spotted/barred whitish; five faint pale tail bars.
- Use: preserve v2 adult identity, dark adult eyes from earlier specimen evidence, and near-equal sex scale because no quantitative direction is supplied.
- Limits: one historical adult female description; no male/juvenile/sex-ratio inference.

## Direct v2 inspection
GitHub’s full v2 board was opened. It has exactly three supported birds, near-equal dark-eyed adults and correct rainforest/root context. Its juvenile is warm brown/cream with distinct adult-like spotting and a long organized wing. The direct 2022 figure description supports a darker, fluffier and less mature rendering, so v3 is a targeted juvenile-stage correction.

## Unknowns retained
Exact age, iris chronology, flight ability, feather sequence, nest site/geometry and sex-size direction remain unknown. No claim of scientific completion.

## Complete ImageGen prompt

```text
Use case: scientific-educational.
Create a new 1536×1024 landscape owl-pet triptych for #165 SPECKLED BOOBOOK, Ninox punctulata, in the established tactile naturalistic high-detail 3D character style shown by the reference image. The reference image is style-only; do not copy its species, desert habitat or Strix proportions. Exactly three complete birds on one broad mossy buttress/root at the base of a large tree in humid Buton lowland rainforest: ADULT MALE left, ADULT FEMALE center, DARK FLUFFY JUVENILE · AGE UNKNOWN right. Title exactly “SPECKLED BOOBOOK”; italic “Ninox punctulata”; exact labels only.

Adults: small compact earless hawk-owls with weak facial discs, near-equal standing height and same plumage because no supported quantitative sex direction is available. Deep chocolate-brown crown/back/wings densely covered with minute dull whitish-buff speckles, a little larger on hindneck but not arranged in neat bars. Thin separate white brow arcs, pure white cheeks and throat, white central underparts; narrow chocolate chest bar and brown flanks spotted/barred whitish. Five faint pale tail bars. Entirely dark chocolate irises, horn-black bill with paler horn lower mandible, pale whitish feathered feet with dark claws. Do not use yellow adult eyes.

Juvenile: directly anchored to O’Connell et al. 2022 Fig. 3A, Buton, August 2013, described/visible as a dark fluffy juvenile. Show an age-unknown recent young, lower and rounder than adults, fully supported on both feet and belly/low stance on the broad root. Loose deep chocolate-to-sooty brown down with only diffuse muted buff mottling; soft pale smudges around face/underparts, not a miniature adult spot pattern. Very short rounded soft wing partly buried in down and short hidden tail; no long layered hard remiges, flight pose or precise fledging claim. Dark-indeterminate irises. The field bird was found at a tree base and possibly fell; show a natural supported ground/root stage, not a hand, cage, rescue scene or invented nest.

Environment: lowland tropical forest near Labundobundo, Buton; large trunk, moss, leaf litter, filtered humid daylight. No nest cavity, eggs, humans, prey or captivity.

Avoid ear tufts, yellow irises, strong facial disc, oversized head, adult-like juvenile wing/tail, unsupported chick, exact-age claim, exaggerated sex size difference, extra birds/limbs/text, watermark or misspelling.
```

## Iteration rule
Problem → adult-like juvenile pattern/wing in v2. Evidence → O’Connell et al. 2022 Fig.3A is a dark fluffy juvenile at a tree base. Change → dark loose down, diffuse reduced markings, short buried wing, full natural support. Recheck → reject any long hard remiges, adult spotting rows, floating feet or inferred flight.
