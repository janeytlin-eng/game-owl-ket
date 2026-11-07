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


## 2026-11-07 — #173 v3 — older immature evidence must bound visible remiges
- **Problem found:** generation followed an “older immature” label but still exposed a long, hard, adult-layered folded wing and tail.
- **Evidence:** repository Mikkola p.145 transcription supports tail/coverts differences but supplies no exact wing-feather chronology; René de Roland & Thorstrom 2009 observed no hatching and cannot fill that gap.
- **Rule derived:** when age is unknown and remex chronology is absent, request a shorter, softer folded wing with fewer exposed hard layers and a partly concealed tail; do not convert adult-like face into mature flight plumage.
- **Applied:** one targeted edit to #173 v3.
- **Verified:** crop recheck shows a visibly softer, shorter wing and concealed tail while preserving supported feet and adult-only details. The improvement is verified for this image only; broader back-check remains future work.
