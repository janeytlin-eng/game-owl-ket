## 2026-11-07 — #148 *Ninox rumseyi* v3: sex direction and brow length must be independently constrained

- **Observed failure:** the first generation obeyed male-larger direction but exaggerated it, and rendered “short separate supercilia” as broad arcs.
- **Evidence:** primary field measurements imply only a modest direction and species diagnosis says short whitish supercilia.
- **Applied change:** targeted only adult brow length and relative scale; preserved juvenile, text, environment and plumage.
- **Verified result:** edited full plate and two crops show shorter separate marks, a reduced male/female contrast, supported feet, and no new juvenile claim. PASS_WITH_LIMITATIONS.
- **Reusable rule:** prompts must separate (a) direction of dimorphism from (b) magnitude; for *Ninox* brow marks, specify spatial extent relative to the eye, then inspect a face crop.

undefined

## 2026-11-07 — #162 *Aegolius acadicus* v2: do not copy adult spot fields onto a formed juvenile wing

- **Observed failure:** v1 correctly showed a late cavity nestling with a formed wing, but added conspicuous pale spots that made the wing read as adult-patterned.
- **Evidence:** institutional ageing guidance and curated juvenile/adult field photographs distinguish plain chocolate juvenal upperparts from adult white crown streaks and upperpart spots.
- **Applied change:** retained a short rounded juvenal wing and cavity support while removing the adult spot field; added the documented cinnamon belly and white facial V.
- **Verified result:** the full plate and juvenile crop show a functional-looking but unspotted juvenile wing, supported feet/belly and no flight claim. PASS_WITH_LIMITATIONS.
- **Reusable rule:** “formed juvenile flight feathers” does not license adult body/wing pattern. Prompt structure, pattern and action ability as three separate constraints, then inspect a stage-specific crop.


## 2026-11-07 — range conflicts and age-unknown pygmy-owl immatures
- **Observed problem:** original type accounts and later species summaries can disagree on countable markings; pygmy-owl generators also tend to adultify unknown immatures through bright yellow eyes, hard layered wings and exposed barred tails.
- **Evidence:** #171 Nelson type states five tail-spot series, while later western-Mexico summaries report six/seven; the repository mesoptile record supports an unspotted grey crown but not age/flight.
- **Applied:** described the range, rendered a restrained midpoint only as a design inference, and explicitly prohibited a universal count; required a dark/indeterminate iris, short down-soft wing and concealed supported tail.
- **Verified effect:** #171 v3 full image and two crops passed these checks without edit. Verified for #171 v3 only; reuse must re-check each species and source conflict.


## 2026-11-07 — #172 *Tyto castanops* v3
- **Problem:** v2’s “~5-week nestling” imported exact chronology from a single nominate-subspecies growth series into *castanops*.
- **Evidence:** castanops-specific sources support strong adult female-larger/darker direction and Tasmanian hollow habitat, but not exact mesoptile week, feather sequence or flight threshold.
- **Applied change:** replace exact week with AGE-UNKNOWN MESOPTILE; require thick cream down, developed mask, wing buried by down, concealed tail and bilateral hollow-lip support; depict adult dimorphism mainly through mass and colour, not doubled standing height.
- **Validation:** first v3 render passed full-size and crop review with no edit. This validates the rule on #172 v3 only; it is not yet a universal masked-owl prompt rule. Recheck any other plate whose exact juvenile week is derived only from another taxon.


## 2026-11-07 — #179 *Otus mayottensis* v3: separate museum age class from invented chronology
- **Observed risk:** an “immature” museum label can tempt the prompt to invent a chick age, iris transition, fledging threshold or nest scene.
- **Evidence:** the primary museum catalogue confirms only an immature specimen; adult photographs calibrate adult outline but do not document juvenile chronology.
- **Applied change:** labelled the third bird AGE-UNKNOWN OLDER IMMATURE, used dark/indeterminate irides, softer less-regular coverts, a compact rounded partly formed wing, hidden short tail and bilateral branch support; made no age, flight or nest claim.
- **Verified result:** full plate, adult crop, older-immature crop and 32-colour transport all pass those bounded checks without an edit. PASS_WITH_LIMITATIONS.
- **Reusable rule:** when a specimen source confirms only age class, lock the label to that class and inspect eye, wing hardness, tail exposure, support and any implied action separately. Verified here only; re-check per species.


## 2026-11-07 — #184 *Otus spilocephalus* v2: a soft juvenile still needs an age-plausible wing
- **Problem:** fixing an adult-hard juvenile wing can overcorrect into a wingless hatchling-like ball.
- **Evidence:** the viewed juvenile photograph supports a compact partly formed wing and supported posture, but only cross-subspecies; Taiwan-race juvenile colour, exact age and flight chronology remain unknown.
- **Applied change:** after reducing the hard wing, a second edit restored one small soft rounded partly formed wing with blurred coverts, without mature primaries or flight action.
- **Verified result:** final plate plus juvenile crop pass this bounded check. PASS_WITH_LIMITATIONS.
- **Reusable rule:** review both over-maturity and over-softening after juvenile-wing edits; require a stage-plausible wing silhouette when the selected older juvenile reference shows one. Verified here only.


## 2026-11-11 — #116 *Margarobyas lawrencii* v5: “bare-legged” must be checked at the full tarsus, not inferred from the species name
- **Observed risk:** a correct-looking owl face can hide feather trousers or cropped/unsupported feet; a generic “juvenile” can also acquire adult-hard flight feathers.
- **Evidence:** the species-specific adult references and repository research record support visibly bare tarsi/toes and an untufted, dark-eyed identity, while exact juvenile chronology and flight threshold remain unknown.
- **Applied change:** required every foot and support in frame, adults near-equal, and an age-unknown older juvenile with softer compact wing and short tail near a natural cavity.
- **Verified result:** full plate plus male, female and juvenile crops show bare tarsi/toes, bilateral support and no flight claim; no image edit was required. PASS_WITH_LIMITATIONS.
- **Reusable rule:** for diagnostic leg/foot characters, inspect the entire tarsus-to-toe chain and support contact in a focused crop; separately check that a bounded older juvenile has stage-plausible softness without inventing a hatchling or flight-ready chronology. Verified here only; re-check per species.


## 2026-11-11 — #118 *Megascops cooperi* v5: do not “soften” documented fledgling flight feathers out of existence
- **Observed risk:** a rule against mature-looking juvenile wings can overcorrect a documented older fledgling into a wingless/down-only chick.
- **Evidence:** the primary Zamorano observation records a fledgling in defensive wing-spread after falling and having difficulty flying; it supports formed flight feathers and ground display, but not exact age or a universal first-flight threshold.
- **Applied change:** kept barred formed flight feathers while softening the head, body and wing-base coverts, hiding/shortening the tail and requiring bilateral ground/root support. Adult identity was separately checked at fully feathered tarsi and bristled toes.
- **Verified result:** full plate plus three role crops pass these bounded checks without an edit. PASS_WITH_LIMITATIONS.
- **Reusable rule:** when action evidence directly shows formed feathers, preserve them; judge age plausibility from the whole package—coverts/down, tail, support and action—not one “soft wing” heuristic. Verified here only.


## 2026-11-11 — #119 older cavity juvenile and anti-template check

- Problem: #119 v4 used three strongly frontal birds with repeated facial/ventral motifs, making a species-specific plate read like a copied template.
- Evidence boundary: the repository's primary-study record supports an older photographed juvenile with gray mesoptile, formed remiges and no visible tail, but not an exact age, sex, flight threshold or independence claim. Current-name checks retain *Megascops centralis* and the former *Otus guatemalae centralis* combination.
- Applied change: v5 uses asymmetric adult angles, irregular individualized plumage, near-equal displayed adult scale, and a cavity-braced juvenile whose formed wing group ends above the sill and whose feet are fully supported.
- Validation: full plate and three focused crops passed the saved checks without edit; exact text/count/order and all supports were visible. This validates the prompt/review rule for #119 only. It does not establish a universal juvenile pattern or quantitative sex-size rule.
