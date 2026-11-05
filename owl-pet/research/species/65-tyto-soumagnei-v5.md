# #65 *Tyto soumagnei* v5 — no-visible-sex-dimorphism / down-only nestling boundary

- Current name: *Tyto soumagnei* (A. Grandidier, 1878)
- Historical name: *Heliodilus soumagnei* Milne-Edwards, 1877 (MNHN holotype record)
- Common name: Madagascar Red Owl
- Action: SCIENCE_REVISION; unique increment 0; v1–v4 preserved.
- Research ready: 2026-11-05T15:40:00+08:00

## Sources actually read

1. New `MRO-RAMAMONJISOA-2014-P56-57-75-77`: doctoral field thesis, printed pp.56–57, 75–77 and Annex I. Eight sexed adults show nearly equal mean wingspan but different mean mass; the author states no visually detectable size/colour/form dimorphism. Three Bemanevika nests were tree holes. Two 2014 nestlings were still covered only in down and unable to escape the cavity when they disappeared; exact age and feather details are absent.
2. New `MRO-MNHN-HOLOTYPE-2026`: institutional holotype record maps original *Heliodilus soumagnei* to current *Tyto soumagnei*; adult sex unknown.
3. Reused `MRO-NHM-2003-P1112` and `MRO-THORSTROM-NEST-1996` only to separate earlier/later documented stages; no stage facts are merged.

## Fact / inference / unknown boundary

- **Fact:** adult sexes are not visually distinguishable by size, colour or form in the thesis description; mean wingspans of the small samples are nearly equal, while mean female mass is higher.
- **Design inference:** show equal crown height and essentially the same adult silhouette; any mass difference is not encoded as a visible scale ratio.
- **Fact:** the 2014 chicks were covered only in down and could not escape their tree cavity; three nest entrances measured 16–20 m high and cavities were 45–117 cm deep.
- **Design inference:** one low, fully supported, down-covered nestling can be shown inside a deep cavity with folded wing area concealed by down and no tail/flight pose.
- **Unknown:** exact chick age, sex, bare-part colour, wing-pin geometry, feather chronology, first climb/flight threshold and fate; individual adult colour variation; universality of the Bemanevika nest geometry.

## Complete imagegen prompt

Create one 3:2 horizontal owl electronic-pet concept plate in the established semi-realistic hand-painted natural-history game-art style of the owl-pet series: warm painterly texture, anatomically credible and gently charming, no photorealism, no pixel art, no split panels, no borders. One coherent humid highland-forest scene at dusk around a deep natural tree cavity in Bemanevika, Madagascar. Exactly three Madagascar Red Owls (*Tyto soumagnei*), fully visible and naturally supported. Add a small clean title “Madagascar Red Owl” and unobtrusive labels “Adult male”, “Adult female”, and “Downy nestling — age unknown” near the correct birds; no other text.

Adult male and adult female: same crown height and essentially the same silhouette, because the primary field thesis states that sex is not visually distinguishable by size, colour or form and the measured mean wingspans were nearly equal. Do not make the female taller, broader, darker or paler as a sex code. Both adults are rich red-ochre to yellow-ochre, untufted, with a pale cream heart-shaped facial disc outlined warm brown, dark sooty eyes, pale grey bill, fine dark spotting on body and larger dark marks on wings/tail, and smoky-grey toes. Both grip separate stable branches with both feet, at comparable camera distance beside the cavity.

Central juvenile: one age-unknown nestling low inside the deep dry tree cavity, explicitly based only on the thesis statement that the 2014 chicks were still covered exclusively in down and could not escape the nest. Show abundant soft pale cream-to-warm-buff down over the body and wing area, a softly forming heart-shaped face with dark eyes, a compact crouched posture and visible bilateral floor/body support on dry cavity material. No exact day label, no bare pink hatchling skin, no invented pin-feather rows, no long remiges, no barred or spotted adult wing panel, no visible long tail, no branch-perching, climbing, hopping or flight pose.

Environment: a documented Bemanevika tree-hole nest example with a visibly deep shaded cavity, moist highland forest outside and dry debris inside. Do not imply that all nests share this geometry. No eggs, prey, humans, duplicate owls, floating feet or extra animals. Keep all six adult toes/feet anatomically plausible and all three birds clearly separated.

## Review gates

- Exactly three owls and correct labels; no extra text.
- Adults equal in display height and silhouette; sex is not encoded as colour or scale.
- Both adults untufted, dark-eyed, red-ochre, pale heart faces; both feet supported.
- Nestling remains down-only/age-unknown, low in the cavity, bilaterally supported, with no mature wing panel or tail.
- Deep tree cavity is an example, not universal; no flight or escape claim.

## Iteration rule

Problem: earlier prompts converted a population mean mass difference into visible female size. Evidence: the same primary thesis reports higher mean female mass but nearly equal mean wingspan and no visually detectable size/colour/form difference. Change: display adults at equal height/silhouette and retain sex only in labels. This rule is applied to #65 v5 and is not considered verified until the generated full frame and adult crop are inspected.

## Visual review — 2026-11-05T15:46:30+08:00

Full master, adult/support crop and juvenile/cavity crop opened. Exactly three owls, correct labels, equal adult silhouette, all support contacts, down-only age-unknown nestling and deep-cavity boundary pass. No edit required. PASS_WITH_LIMITATIONS; science false.

## Fixed-commit verification — 2026-11-05T15:54:00+08:00

Archive `3db4bde798c5d362917f574162abaee6da68e9e9`, tree `13e2cb4deaaef57677ed122ad6da69e9632c2e08`, returned all 13 required paths with exact full-size blobs and byte sizes in a non-truncated 3,052-entry tree. Manifests parse at 688/689/679. PASS_WITH_LIMITATIONS; science false.
