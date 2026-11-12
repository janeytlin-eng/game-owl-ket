

## 2026-11-08 — never stream >786 KiB binary through one shell-output result

**Problem:** #31's first archive commit preserved paths but truncated five large bodies near 786 KiB. Git path existence and blob equality to the upload response were insufficient because the upload input itself had been truncated.

**Fix applied:** split local files into 600000-byte chunks (divisible by 3), base64 each chunk, concatenate, then create the Git blob. Verify immutable tree blob *and exact size* before credit.

**Status:** applied to #31 repair; final verification is a separate required stage.


## 2026-11-08 — “fully feathered immature” still requires a wing/tail contour check

**Problem:** #31 v5 correctly used a dated fully feathered immature reference, yet the first render retained a long mature-looking folded wing and tail.

**Evidence/application:** the dated reference supports the stage, yellow eyes and branch support, while the morphology synthesis supports weaker lower barring and browner tail bars; neither licenses a fully mature wing/tail contour. A center-bird-only edit compacted and softened the wing and shortened/browned the tail.

**Verified visual result:** the edited full plate, transport master and three subject crops were opened; the immature correction held without material drift in adults, text, cavity context or support. Apply this as a review trigger for older immatures, not as an exact feather-age rule.


## 2026-11-08 — juvenile crown evidence does not license adult wing organization

**Problem:** #30 v5 initially rendered the evidence-supported spotted juvenile crown correctly but paired it with a long folded wing and neat adult-like white covert rows.

**Evidence/application:** the sources support a juvenile/fledgling stage and yellow iris, not adult-complete wing organization or a flight threshold. A targeted edit shortened and softened only the center bird's wing and removed neat adult-style rows while retaining full branch support.

**Verified result:** edited full plate, archival master and juvenile crop were opened; the correction held without material drift in adults, labels or habitat. Apply this as a review trigger, not a universal claim about exact feather timing.


## 2026-11-08 — stage-specific action can be added without inventing age

**Problem:** juvenile plates can become static, while forcing an exact day-age from a field narrative would overclaim.

**Evidence/application:** BirdLife South Africa's directly observed African Barred Owlet sequence reports newly fledged chicks staying near the nest, making short hops and stretching flight muscles. #29 v5 therefore uses a fully supported one-wing stretch and explicitly avoids airborne flight or exact age.

**Verified result:** the full plate and three crops passed review without mature juvenile wing/tail anatomy. This rule is validated for this evidence pattern, not generalized to species lacking comparable direct observation.


## 2026-11-06 — conflict rule applied to #135 v4

**Problem:** a prior revision translated a one-pair specimen direction into an explicit female-larger visual ratio. **Evidence:** Mees has only one adult per sex; Mikkola explicitly states there are no sexual-size data. **Change applied:** retain pose asymmetry but keep adults at comparable apparent scale. **Observed validation:** the new plate was opened in full and crop; poses remain distinct without a size claim. This is a verified prompt/review rule application, not population-level science verification.


## 2026-11-06 — #136 v4 verified application

For taxa diagnosed by absence of white, write the negative as a whole-body identity rule and inspect facial, scapular and belly crops; warm-buff highlights must not drift to white. #136 v4 applied and visually passed this rule, without upgrading science status.


## 2026-11-07 — #138 v4 wing–tail relation verified application

**Problem:** a first render inverted a primary juvenile field mark by extending the tail beyond the folded wing; a first edit then hid the tail too completely to review the relation. **Evidence:** the dated 2017 field account says formed wings projected beyond a short dark tail. **Change applied:** use a relation-specific edit—retain a small short dark tail fringe ending before the folded wing tip—then open both the full frame and juvenile crop. **Observed validation:** the long-tail inversion is removed and natural branch support remains. Because the boundary is partly occluded, record PASS_WITH_LIMITATIONS and keep scientific status false. This is a verified production/checking rule: relational morphology needs a dedicated crop, and “not visibly wrong” is not the same as “fully verified.”


## 2026-11-07 — #139 v4 single-specimen juvenile cue

**Problem:** an image model expanded “retained juvenile feathers on one specimen” into a generally mature, long-winged small adult. **Evidence:** the primary description supports only scattered pale juvenile crown/nape feathers; the guide explicitly says juvenile undescribed. **Change applied:** constrain the figure to an age-unknown older immature, close the eyes, shorten/soften the formed wing, conceal most of the tail, and inspect a dedicated crop. **Observed validation:** the long hard wing/tail impression was reduced while natural support and the one evidenced juvenile cue remained. Rule validated for production: a single specimen cue must remain local to its feather tract and must not be generalized into an invented whole-stage plumage.


## 2026-11-07 — #140 *Otus rufescens* v4
- **Problem observed across earlier versions:** juvenile descriptions often establish color/texture but not day age, flight capacity or full feather chronology.
- **Evidence rule:** when a source explicitly documents a downy chick and color zones but not chronology, select a fully supported resting pose, conceal mature remiges/tail, and label age unknown; do not infer a cavity or fixed sex-size direction.
- **Applied:** #140 v4 used near-equal adults and a moss/leaf-supported downy chick with no mature wing/tail claim.
- **Verified in this image:** full plate plus adult/support and chick crops were opened; all contacts and juvenile boundaries passed without edit. This validates the prompt/check rule for this case only, not all owl species.


## 2026-11-07 — #141 partial-tarsus and juvenile-wing correction

**Problem:** the initial model expanded “distal 6–9 mm bare” into a mostly bare adult tarsus and gave an age-unknown juvenile a long hard adult-like folded wing. **Evidence:** Mikkola restricts the bare adult portion to the distal tarsus and describes the juvenile only as fluffy/adult-like with narrow head/crown/neck bars. **Change applied:** extend adult leg feathering almost to the toes, leave only a narrow distal band bare, shorten/soften the juvenile wing and conceal most of its tail. **Observed validation:** the full plate and dedicated adult/support and juvenile crops were opened; both overclaims were removed while all feet remained supported. Production rule validated for this case: numeric partial-feathering limits must be stated as a visible anatomical boundary, and unknown flight stage requires soft short wing language plus crop review.


## 2026-11-07 — #142 down-remnant juvenile boundary

**Problem:** the model translated a down-remnant juvenile into a fluffy bird carrying a long, hard, adult-barred wing. **Evidence:** the guide documents down remnants and juvenile colour zones but not flight stage; the photographic comparator shows a compact mostly hidden wing/tail. **Change applied:** a juvenile-only edit shortened/softened and mostly concealed the wing, concealed the tail, and normalized dark-neutral eye alignment while retaining two-foot fork support. **Observed validation:** full plate plus juvenile and adult/support crops were opened; the unsupported maturity claim was removed. Rule validated for this case: “fluffy” alone does not prevent adult-wing leakage; explicitly combine compact/hidden wing, concealed tail and crop review.


## 2026-11-07 — #170 prepared-skin immature boundary: tail maturity needs its own check

- **Problem:** even when an age-unknown immature is prompted with a short soft wing, ImageGen may still give it a long, fully exposed, regularly barred adult tail.
- **Evidence:** Lowery & Newman 1949 pp.2–3 describe prepared immature material but do not supply exact age, flight ability or a continuous wing/tail growth series.
- **Applied:** edit the immature only; end the wing high above the feet, hide nearly all of the tail, retain bilateral branch support and keep the adult sex-palette comparison unchanged.
- **Verified in this asset:** the edited full-colour plate, 64-colour transport plate and immature crop were opened; the adult-style long tail was removed and support preserved.
- **Reuse boundary:** for sparse skin-based immature evidence, prompt and inspect wing maturity **and tail exposure separately**. This is one validated application, not a universal owl development schedule.

## 2026-11-07 — Calendar-age evidence is not a nest-stage clock (applied and visually verified)

- Problem: a banding study's HY/juvenal-plumage category was previously converted into a precise cavity-threshold stage.
- Evidence boundary: Pyle et al. 2004 gives calendar-age plumage characters, not exact day, nest position, first-flight ability or a universal iris timetable.
- Applied change: #26 *Glaucidium siju* v5 moved the juvenile to a broad living branch, kept it low and fully supported, and made wing/tail cues soft and subordinate; no nest-stage or flight claim.
- Validation: original, transport and juvenile crop reopened; the juvenile retained the documented unmarked-back/streaked-underpart direction without adult wing rows or a long adult tail. Rule is verified for this plate only, not universal across owl species.

## 2026-11-07T22:59:17.142+08:00 — Flight evidence does not require a flight pose

When primary sources say a recent fledgling can fly but lands poorly, that evidence does not justify depicting flight. If feather sequence and landing ability are not individually documented, use a fully supported low perch and keep wings compact. For adult sexual dimorphism reported as overlapping linear measurements, show only a modest directional difference rather than categorical female gigantism. Applied and visually rechecked on #27 *Glaucidium passerinum* v5; effectiveness is limited to this plate until later cross-species review.


## 2026-11-07 — Behavioural-age intervals are not visual day-age calibrations

- **Finding:** independent secondary sources may agree on a 27–32-day cavity-departure interval without providing a primary daily feather or iris sequence.
- **Applied:** #28 v5 replaced “approximately 31-day appearance” with an age-unknown recent fledgling; kept only supported behaviour (near nest, parent-dependent, low support) and conservative juvenile directions already indexed.
- **Verified:** the generated plate passed whole-image and crop review without an edit: short/soft wing, short/mostly hidden tail, dim indeterminate iris, six-foot support, no flight claim.
- **Rule:** never translate a behavioural fledging interval into exact visual age unless a readable age-linked growth/photographic series supports it. Record the applied life stage and unresolved chronology separately.

## 2026-11-11 — Archive transport must be verified as bytes, not inferred from a successful ref update

- **Problem:** the #102 archive commit moved `main`, but two large PNG objects were only about 786 KB and four JSON files contained unescaped/truncated content; a successful commit/ref update therefore did not prove a valid production archive.
- **Applied:** preserved the old commit for audit, restored the last valid ledger/manifests, regenerated the asset from the persisted full prompt, opened the full plate and three role crops, and uploaded binary content in 300,000-byte raw chunks with an exact expected base64-length check before blob creation.
- **Validation required:** compare remote Git blob SHA and byte size for every image alias, parse every canonical JSON manifest from the immutable commit, and only then write `VERIFIED` and ledger credit.
- **Reusable rule:** connector success is only a transport event. Production success requires immutable path, blob, byte and parse evidence; a scratch path or ref update alone is not archival proof.

## 2026-11-11 — Preserve source conflicts instead of averaging them into invented traits

- **Finding:** #106 *Strix albitarsis* has two accessible institutional accounts describing dark eyes, while a blocked prior guide snippet and a secondary account point toward orange/yellow eyes.
- **Applied:** v4 uses very dark brown adult irides with restrained warm reflections, documents the conflicting material, and remains scientifically unverified. No speculative second edit was made merely to blend contradictory color claims.
- **Validation:** full plate plus adult and juvenile crops were opened; the result preserves the selected evidence boundary without bright iris discs, clone adults, adult-hard juvenile wings or nest-like geometry.
- **Reusable rule:** when sources conflict, select the best actually read evidence for the concept, retain the conflict and confidence limit in the record, and never present an aesthetic compromise as a resolved scientific fact.

## 2026-11-12 — “Non-flying but moves among branches” requires a contact-specific pose

- **Problem:** a field report that a young owl moves among branches can be over-expanded into flight, wing-flapping, fledged remiges or an unstable one-foot pose.
- **Evidence boundary:** Brosset & Erard 1986 p.226 explicitly document about-50-day and other non-flying *Ketupa leucosticta* young moving among branches, and state that the nest was not found; no daily feather sequence is supplied.
- **Applied:** #168 v4 uses a low supported step with one foot on each connected branch surface, short rounded soft wing, hidden short tail, no airborne gap and no invented nest.
- **Verified in this asset:** full plate plus dedicated young crop were opened; bilateral support and conservative wing/tail maturity passed without edit.
- **Reuse rule:** translate locomotion evidence into the least capable evidenced action and specify visible contact geometry; do not infer flight, a nest or a complete age-linked plumage from locomotion alone.


## 2026-11-13 — local diagnostic marks need tract-specific placement checks

- **Problem:** #169 v3 omitted a museum-account posterior-crown white patch while its age-unknown mesoptile still carried a long adult-hard wing and exposed tail.
- **Evidence boundary:** Bouet 1961 p.619 places the white patch specifically on the posterior crown, not the scapulars; the mesoptile record supports formed remiges/rectrices but not adult-complete proportions or flight.
- **Applied:** #169 v4 adds only a small crown patch behind/between the tufts, explicitly forbids white shoulder migration, compacts/softens the mesoptile wing and hides most of the tail while preserving two-foot branch support.
- **Verified in this asset:** the full plate and three role crops were opened; crown location, absence of white shoulders, compact young wing/tail and support all passed without edit.
- **Reuse rule:** when evidence names a small feather tract, prompt its anatomical location and inspect both the target tract and common leakage sites; separately review wing and tail maturity even when a source says juvenile feathers are “adult-like”.


## 2026-11-13 — mass dimorphism and downy emergence need separate visual translations

- **Problem:** a large male–female mass difference can leak into an exaggerated height ratio, while a report that downy young leave a nest hole can leak into unsupported flight.
- **Evidence boundary:** Debus 1993 pp.171–172 reports Tasmanian mean masses of 525 g male and 850 g female and a 12.8 dimorphism index; p.187 says young may leave the hole while still downy. Neither passage supplies a body-height ratio, exact young age or first-flight threshold.
- **Applied:** #172 v4 expresses the adult difference mainly through female body fullness/darker tone with only moderate height difference, and shows the young taking one low two-foot supported step at the hollow lip.
- **Verified in this asset:** full plate plus three role crops were opened; no giant-height caricature, airborne gap, mature young wing or exposed mature tail was found. Reuse this as a prompt/review rule, not as a universal Tytonidae growth schedule.


## 2026-11-13 — recurring morphology defects belong in generation constraints and crop gates

- **Problem:** #173 v3 required an edit because short-tuft evidence leaked into tall theatrical ear tufts and an age-unknown older immature acquired adult-hard wing/tail layering.
- **Evidence boundary:** western-form sources support very short low tufts; the immature evidence supports only local uppertail-coverts/rectrix-tip cues, not adult-complete remiges, exact age or flight.
- **Applied:** #173 v4 states tuft height and compact diffuse immature wing/tail as whole-image prohibitions and requires three role crops before accepting the first render.
- **Verified in this asset:** the full plate and all three crops passed those gates without an edit. This validates the prompt/check combination for this asset, not a universal *Otus* development schedule.

## 2026-11-13 — #174 `Strix sartorii` v4 (applied, review-validated; archive pending)

- Problem: the first render converted “unringed pale face” into conspicuous target-like facial circles and rendered the directly flight-observed fledgling with crisp adult-style wing rows.
- Evidence boundary: the 2015 field record supports an age-unknown begging fledgling able to fly out of sight, not a downy nestling or exact first-flight age; it allows formed flight feathers but not adult-like crisp patterning.
- Applied change: targeted edit softened the adults' facial framing and shortened/softened the fledgling's wing pattern while preserving flight capability and bilateral branch support.
- Validation: edited full plate and three fresh crops were reopened; role count/labels, near-equal adults, support and evidence-bounded fledgling stage passed with limitations.
- Reusable check: for a flight-capable age-unknown fledgling, do not automatically remove all formed remiges; instead compare feather length, edge softness and pattern crispness against the adults. Treat “unringed face” as a specific anti-target review gate.
- Archive lesson: a persistent Git blob is recoverable evidence but is not an archived repository file. Do not advance ARCHIVED/VERIFIED until the blob is attached to a main-tree path and read back.


### 2026-11-13 — “juvenile resembles adult” is not a licence for adult wing geometry (applied and crop-verified)

- **Problem:** #175 initial generation followed adult resemblance too literally: the juvenile wing rows were too crisp, while adult ear-tufts were exaggerated.
- **Evidence:** Mikkola printed p.134/PDF p.136 gives small ear-tufts, no evidence of sexual size difference, and only the broad statement that juvenile resembles adult; it does not provide feather chronology or flight ability.
- **Applied change:** keep adults near-equal, reduce tufts, and render the age-unknown fledgling with a shorter rounded softer folded wing plus bilateral support; do not infer nest or flight.
- **Verified result:** edit1 full plate and all three crops passed these gates. This is an applied visual rule, not new biological evidence; science remains false.
## 2026-11-13 — “mesoptile described” does not license a visible mature wing

**Problem:** #176 v4's first render respected the broad pale mesoptile description but exposed a long, organized adult-like wing.

**Evidence/application:** the directly read guide supports whitish down with vague yellow-brown barring, a white-barred crown and somewhat banded tail, but gives no exact age, flight threshold or feather chronology. The edit therefore shortened and softened the wing, retained a short supported tail and labelled the stage age-unknown.

**Observed validation:** the edited full plate and three subject crops were opened; the wing correction held without adult identity, label, support or habitat drift. Apply this as a review trigger only when the source describes a mesoptile without flight/age evidence; it is not a universal claim about owl development.

# 2026-11-13 — juvenile evidence may hide in older primary monographs

- **Problem:** a modern guide summary for #177 only supported a generic paler mesoptile, encouraging an age-unknown juvenile and leaving wing maturity unresolved.
- **Evidence found:** de Naurois (1975) directly describes two juvenile colour phases, a non-flying late-November stage and one younger chick with remiges only half-grown; it also states the nest was not discovered.
- **Applied change:** #177 v4 replaces the generic mesoptile with a documented still-downy, non-flying grey-brown young and short half-grown remiges; no cavity is shown. The initial generated adult-like wing was edited and reopened at native size plus crop.
- **Validated scope:** visually validated for #177 v4 only. For rare species, search older species monographs in original-language terms for `juvenile`, `poussin`, `jeune`, `rémiges`, `nest` before accepting a modern-guide summary as the developmental evidence ceiling.


## 2026-11-13 — a documented juvenile eye option is not an age rule

- **Problem:** #178 v3 muted the juvenile iris as if eye colour tracked age, while the first v4 render also gave the recent fledgling an adult-hard wing.
- **Evidence boundary:** Currie et al. 2002 pp.16–18 report bright yellow in some fledglings and found no age relationship; Currie et al. 2004 pp.126–130 define a fluffy barred c.8–12-week recent-fledgling category but not a complete feather chronology.
- **Applied change:** v4 uses the directly observed bright-yellow option without calling it universal, and one edit shortened/softened the juvenile wing while retaining bilateral support.
- **Verified scope:** edited full plate plus three role crops passed. Reuse the rule only to separate a documented soft-part option from an unsupported age code; it does not establish universal iris or wing development.


## 2026-11-13 — #179 short distal tarsus boundary

- **Problem:** A generic handbook-style phrase can be over-expanded into “feathered to the toes,” even when a specimen source documents a short bare terminal segment.
- **Evidence:** Marshall 1978 printed p.19 states the distal c.5 mm of *O. r. mayottensis* is bare.
- **Applied:** Prompted feathered upper tarsi plus a short visible bare terminal segment, then reopened both adult crops.
- **Validated:** The v4 image shows the bounded segment without turning the species into a long bare-legged owl. Treat this as species-specific; do not generalize to other scops owls.
