# #132 *Strix davidi* v5 review

- Review time: 2026-11-12T05:36:00+08:00–2026-11-12T05:40:00+08:00
- Image: `owl-pet/production/reviewed/132-strix-davidi-v5-reviewed-master.png`
- Result: **PASS_WITH_LIMITATIONS**
- Scientifically verified: **false**
- Imagegen invocations: 1
- Edits: 0

## Actual views

1. Full 1536×1024 plate.
2. Adult-male crop.
3. Approximately-four-week young crop.
4. Adult-female crop.

## Evidence comparison

| Check | Evidence boundary | Observed result | Verdict |
|---|---|---|---|
| Identity | Scherzinger et al. 2014: dark adult, long tail, radial face; no bold concentric target rings | Both adults are dark, long-tailed and radially faced; no target-like concentric rings | PASS_WITH_LIMITATIONS — concept cannot prove taxonomic rank |
| Sex display | No defensible universal female-larger ratio in the sources read | Adults are near-equal in structural size but use different head/body poses | PASS_WITH_LIMITATIONS |
| Young stage | Primary Fig. 11/table supports about four weeks: dull gray fluffy mesoptile, fine pale-brown undulation, tawny/rusty mask, dark-brown eyes, pinkish lids, pale face border | Center young is visibly down-rich, gray-brown and tawny masked; wing and tail remain compact and down-obscured | PASS_WITH_LIMITATIONS — exact individual age cannot be independently verified from a concept image |
| Action/support | At this stage, supported standing/perching is defensible; no flight claim | Both feet rest on the box sill; no flight, stretched wing or unsupported pose | PASS |
| Nest context | 2009 study used bare artificial boxes 4–6 m high with no nest material; not a universal natural-nest claim | Rough artificial box with bare sill in montane conifer forest; no fabricated nest lining | PASS_WITH_LIMITATION |
| Count/text/order | Exact #132 title, scientific name and three roles required | Exact title/name/labels; one male, one approximately-four-week young, one female | PASS |

## Problem → evidence → change → recheck

- Prior recurring risk: bold facial-disc rings and exaggerated sexual dimorphism. Evidence: 2014 primary comparison and absence of quantitative sex-size direction. Change in v5 prompt: radial face, restrained pale drops, near-equal adults, non-mirrored poses. Recheck: both adult crops pass; no edit required.
- Prior recurring risk: generic fluffy chick with adult wing/tail or unsupported action. Evidence: photographed/table-described approximately-four-week mesoptile. Change in v5 prompt: compact hidden wing/tail and two-foot sill support. Recheck: young crop passes; no edit required.
- No evidence-backed defect remained after full/crop inspection, so the initial original was retained as final. This is a deliberate zero-edit result, not an assumption that generation equals review.

## Remaining unknowns

- Exact sex of the depicted reference individuals and population-level quantitative sex-size direction.
- Complete hatch-to-flight chronology beyond the evidenced approximately-four-week stage.
- Frequency and substrate of natural nest sites outside the study-box context.
- Whether a current checklist treats the Sichuan form as species or `Strix uralensis davidi` subspecies.

## Iteration rule applied and checked

When a primary source supports a photographed age while taxonomic rank and sex-size direction remain disputed, anchor the young only to that age and keep adults near-equal. Do not turn uncertainty into a larger female, mature juvenile wing or unsupported action. This rule was actually applied to v5 and verified on all three role crops.
