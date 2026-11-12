# Review — #92 Northern Boobook (*Ninox japonica*) v5

- Reviewed: 2026-11-08T04:31:18.967+08:00
- Initial original: `production/generated/92-ninox-japonica-v5-initial-original.png`
- Final original: `production/generated/92-ninox-japonica-v5-final-original.png`
- Review result: **PASS_WITH_LIMITATIONS**
- Scientifically verified: **false**

## Evidence boundary

Research record `research/species/92-ninox-japonica-v5.md` and source index IDs JAP-TBN-2025-REREAD, JAP-ITIS-2026-REREAD, JAP-NTM-COLLECTION-2026-REREAD, JAP-LIN-LIN-TSENG-2012-PP164-166, JAP-TAIEOL2013 and JAP-MIK2013-466 were applied. Lin et al. 2012 does not support a significant adult sex-size difference. TBN and ITIS/IOC disagree on whether `totogo` is synonym or valid subspecies, so the plate stays species-level.

## Actual visual checks

- Exact title and three role labels: PASS.
- Exactly three birds: PASS.
- Adult identity: no ear tufts, yellow irises, dark brown upperparts, pale broad ventral streaking, white interscapular/shoulder marks, feathered tarsi and supported yellow toes: PASS_WITH_LIMITATION.
- Adult sex direction: near-equal standing scale; no unsupported fixed female-larger rule: PASS_WITH_LIMITATION.
- Fledgling: paler fluffy underparts, open begging beak, small rounded body, both feet supported beside cavity: PASS_WITH_LIMITATIONS.
- Habitat and nest context: Taiwanese orchard/woodland tree cavity, without exact nest-tree or subspecies claim: PASS_WITH_LIMITATION.

## Problem → evidence → modification → recheck

Initial crop showed a long orderly folded primary panel, which could imply mature flight ability. The species evidence does not provide an exact-age feather sequence or flight threshold. One image edit shortened and softened only the fledgling wing, concealed the tail and removed adult-like regular shoulder marks. Edited full plate plus adult-male, adult-female and recent-fledgling crops were opened again. The wing is now compact, rounded and down-softened; text, adults, scene and support remain correct.

## Remaining unknowns

Exact fledgling age and sex; iris chronology; continuous remex/rectrix sequence; first-flight threshold; degree of independence; and the current taxonomic rank of Taiwan `totogo`. These prevent scientific final approval.

## Full targeted-edit prompt

```text
Use case: precise-object-edit
Asset type: owl electronic-pet scientific concept plate revision
Primary request: Edit ONLY the right-hand bird labeled "RECENT FLEDGLING" in the existing three-panel Northern Boobook plate. Shorten and soften its folded wing so it is compact, rounded, and down-softened, with incomplete developing remiges rather than a long orderly adult primary panel. Keep the tail very short or concealed behind the body. Remove any adult-like regular shoulder spots from the fledgling. Preserve its paler fluffy underparts, open begging beak, large dark juvenile-looking eye, small rounded body, both feet firmly supported on the branch beside the natural tree cavity.
Text (verbatim): "92 · NORTHERN BOOBOOK · Ninox japonica"; "ADULT MALE"; "ADULT FEMALE"; "RECENT FLEDGLING"
Constraints: Change only the right-hand fledgling's wing/tail development. Keep both adults pixel-consistent in identity, pose, scale, plumage, eye color, feet, and branches. Preserve exact title, labels, three-panel layout, typography, orchard/cavity habitat, lighting, framing, and all foot support. Exactly three birds. No new birds or objects.
Avoid: adult-length fledgling primaries, orderly adult wing panel, adult shoulder spots on fledgling, long barred fledgling tail, unsupported feet, flight pose, newborn naked chick, altered text, misspelling, watermark.
```
