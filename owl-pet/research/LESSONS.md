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


## 2026-11-11 — separate feather-development evidence from action ability (#120 v5)

- A primary description of “considerably developed” primaries/secondaries/tertials can justify formed barred remiges under residual down, but it does not by itself justify a long rigid adult wing or flight.
- When the same record documents only slight wing opening and bill-clapping, render a compact partially lifted wing with belly and both feet supported; keep first-flight threshold and independence unknown.
- If a paper gives different estimated age ranges in its results and discussion (here 20–30 versus 25–30 d), do not collapse them into an exact-age design label.
- Applied and visually verified for #120 *Megascops ingens* v5 after one edit; broader effectiveness is not claimed.


## 2026-11-12 — #140 *Otus rufescens* v5: an evidence-management pose is not a species fact

- **Observed risk:** v4 used a closed-eye downy chick to avoid inventing an unknown juvenile iris, but later reuse could silently turn that cautionary pose into an asserted developmental character.
- **Evidence:** the reopened primary description supports an age-unknown mesoptile that is almost uniform rich rufescent-brown, with a weak dark facial-disc rim and vague barring strongest on hindcrown/upper mantle; it does not state that the bird's eyes were closed, its iris colour, exact age, flight ability or nest position.
- **Applied change:** v5 selects the directly described mesoptile, renders open eyes with a dark/non-diagnostic iris, a compact formed soft wing, short/hidden tail and bilateral branch support, while retaining all missing chronology as unknown.
- **Verified result:** the full plate and three role crops passed without edit. PASS_WITH_LIMITATIONS; science=false.
- **Reusable rule:** record why a conservative pose was chosen, and never promote that pose into an observed developmental fact on the next revision. Prefer the best directly described stage, then neutralize only the unsupported feature. Verified here only.
## 2026-11-12 — #141 *Otus magicus* v5: inspect an apparent defect before editing it

- **Observed risk:** the full plate made the obliquely posed adult female's far eye look like a possible extra-eye artifact; an immediate image edit could have damaged otherwise coherent anatomy and typography.
- **Evidence:** the dedicated female crop shows exactly two irides aligned across the turned facial disc. Separately, Finsch's 94-specimen series supports variable tarsal feathering and fine crossbars on developing juvenile remiges, but not exact age, flight or one universal pattern count.
- **Applied change:** no pixel edit was made after the crop falsified the suspected defect. The evidence-level change instead occurred in the prompt: keep a short partly down-veiled barred juvenile wing and variable near-toe tarsal feathering, while withholding exact age, iris and action ability.
- **Verified result:** full plate plus male, downy-young and female crops pass support, count, label and bounded-plumage checks. `PASS_WITH_LIMITATIONS`; science=false.
- **Reusable rule:** when a perspective cue resembles duplicated anatomy, inspect a focused native-resolution crop before editing. Record a rejected defect hypothesis explicitly; do not count it as an image revision. Verified here only.


## 2026-11-12 — #142 *Asio grammicus* v4

- **Problem:** correcting v3's adult-hard juvenile wing had over-corrected the bird into an almost wingless uniform down ball.
- **Evidence:** Gosse's two downy immature observations show individual variation in immediate movement after disturbance but do not define a universal age or flight threshold; Mikkola and the retained photographic comparator support a down-remnant older juvenile.
- **Applied rule:** distinguish wing development from action ability. A supported older juvenile may show a compact, soft, partly formed folded wing without being posed flying or assigned a precise flight capacity.
- **Verification:** full plate plus male, juvenile and female crops passed this rule with no edit. This is verified for #142 v4 only; it is not a universal owl timetable.

## 2026-11-12 — #143 *Asio solomonensis* v4: preserve the documented rescue support without turning it into a nest

- **Observed risk:** a documented older young on a railing can be converted either into an unsupported forest chick or into an invented species-typical nest scene.
- **Evidence:** Loyn & Debus directly support a lively, long-down older young on a rescue railing with emerging barred dorsal/wing feathers; Woxvold & Novera independently support adult occurrence in Bougainville lower-montane forest. Neither source establishes exact age, flight threshold or a universal nest structure.
- **Applied change:** use a broad bilateral rail support inside lower-montane forest, label the bird OLDER YOUNG — AGE UNKNOWN, keep only a compact down-veiled barred wing patch, and state that the rail is an art translation of rescue support rather than a nest claim.
- **Verified result:** the full plate and three focused crops pass support, stage and adult-identity checks without an edit. `PASS_WITH_LIMITATIONS`; science=false.
- **Reusable rule:** preserve the evidentiary function of a human-made rescue support when it is the best direct stage record, but never promote it into a natural nest or universal life-history fact. Verified here only.

## 2026-11-12 — juvenile evidence boundary from #145

- A pre-split nestling mention without a preserved specimen or description is taxonomy/history evidence, not juvenile morphology evidence.
- Do not inherit adult iris colour into an age-unknown young bird when the stage source is silent; keep it dark/uncalibrated and record the unknown.
- A historical note that quills are formed does not license an adult-perfect long wing silhouette: retain compact, rounded, supported posture unless age/action evidence says more.
- Applied and visually verified on #145 *Ninox philippensis* v4; broader back-check remains a future review task.

### 2026-11-12 — Prevent adjacent-taxon juvenile transfer

- Finding: an “immature” sentence can belong to the next taxon even when adjacent to a target diagnosis.
- Evidence: Rasmussen et al. (2012) places the explicit immature description under *Ninox spilocephala*, after the complete *N. mindorensis* diagnosis.
- Applied: #146 v4 excluded that description, kept an age-unknown supported placeholder, and changed only adult markings from Mindoro-specific evidence.
- Validation: full plate and three role crops passed; science remains false because the juvenile stage is unresolved.


## 2026-11-12 — #147 *Ninox leventisi* v4: use documented behavior to diversify poses, but keep it separate from sex and breeding inference

- **Observed problem:** V3 adult poses were visually redundant, while sex-specific appearance and juvenile development were not evidenced.
- **Evidence:** Rasmussen et al. (2012) documents a face-to-face song display with puffed/pulsating white throat and drooped wings, but cannot establish sexual dichromatism; immatures were scarce and excluded.
- **Applied:** V4 keeps adults near equal, varies only one adult through that documented song-display cue, and retains an age-unknown supported juvenile placeholder. A conflicting secondary search snippet was explicitly quarantined because the PDF could not be read.
- **Validation:** full plate and three role crops pass; the rule improved pose differentiation without adding sex or nest claims. Science remains false because Camiguin juvenile chronology is unresolved.


## 2026-11-12 — Separate mobility evidence from plumage/flight claims (#148)

- **Problem:** a field paper can prove that a juvenile moved through a home range while still leaving exact age, wing development and flight threshold undescribed.
- **Evidence:** the Cebu Boobook telemetry study explicitly included one juvenile and mapped its nightly movements; it does not describe a feather sequence or say that the bird flew.
- **Applied change:** use an open-eyed, fully supported sidestep/perch action; keep the wing short, rounded and down-obscured; do not create a spread-wing or airborne pose.
- **Verified effect:** the full plate and independent juvenile crop preserve support and mobility without visually asserting flight. This rule is now verified for #148 v4 only; future species require their own evidence.
