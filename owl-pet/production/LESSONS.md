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


## 2026-11-12 — Separate mobility evidence from plumage/flight claims (#148)

- **Problem:** a field paper can prove that a juvenile moved through a home range while still leaving exact age, wing development and flight threshold undescribed.
- **Evidence:** the Cebu Boobook telemetry study explicitly included one juvenile and mapped its nightly movements; it does not describe a feather sequence or say that the bird flew.
- **Applied change:** use an open-eyed, fully supported sidestep/perch action; keep the wing short, rounded and down-obscured; do not create a spread-wing or airborne pose.
- **Verified effect:** the full plate and independent juvenile crop preserve support and mobility without visually asserting flight. This rule is now verified for #148 v4 only; future species require their own evidence.


## 2026-11-12 — Constrain sex-size direction to the actual specimen series (#149)

- **Problem:** “two males and one female” can support a direction but not a population rule or large body difference.
- **Evidence:** Gurney’s 1882 table gives both male wings as 7.40 in and the female as 7.60 in; tarsus/toe values overlap and no mass is reported.
- **Applied change:** female is only subtly longer/larger in linear silhouette (~3%), with no invented plumage difference or bulk.
- **Verified effect:** full plate and sex-specific crops show a visible but restrained direction. This rule is verified for #149 v4 only and must not be generalized.


## 2026-11-12 — Eye state is not a developmental marker unless observed

- **Problem:** repeated closed-eye juvenile poses can silently turn a presentation choice into an apparent stage claim.
- **Evidence:** #150 *Ninox variegata* had no species-specific juvenile eye-state or iris chronology; the v3 closed-eye pose was not source-backed.
- **Applied change:** v4 uses open but dark/non-diagnostic eyes, keeps the bird fully supported and explicitly age unknown, and makes no flight/nest claim.
- **Validation:** full plate and three role crops passed; no adult-like juvenile wing/tail or support defect was observed. This rule is validated for #150 v4 only and should be checked case by case.


## 2026-11-12 — Documented mature-pattern features in older juveniles
- **Problem:** an evidence-supported adult-like wing pattern can still cause a juvenile to read as a miniature adult.
- **Evidence:** #155 *Scotopelia ussheri*, Monticelli et al. 2015 pp.187–188: the juvenile flew and showed virtually adult-like barred wings, yet was smaller, stubbier, paler and loose-feathered.
- **Rule discovered:** do not delete a directly documented mature-pattern feature merely to look juvenile. Constrain proportions, contour-feather texture, tail length and supported posture instead.
- **Applied:** #155 v4 used a short/stubby body, loose feather texture, shorter wing/tail and two-level bilateral support while retaining barred remiges.
- **Validation:** full image plus three crops viewed; the juvenile remained recognizably older-juvenile rather than adult-proportioned. Validation applies only to #155 v4; later species need their own evidence.

## 2026-11-12 — Known-age mesoptile can retain patterned wings

- **Problem:** an older down-softened juvenile may be incorrectly rejected merely because its folded wing carries adult-like pattern.
- **Evidence:** Mikkola's Pel's Fishing Owl account (printed pp.304–306) describes mesoptile wings/tail as adult-like but paler/less reddish; Prague Zoo documents a light three-month bird with powder-down remnants.
- **Applied:** #156 v4 retains a compact paler-patterned folded wing while shortening the tail, preserving powder down and requiring bilateral branch support and no flight claim.
- **Validation:** full plate and three role crops were reopened after recovery; the bird remained visibly juvenile and evidence-bounded. This rule is verified only for #156 v4 and must not be generalized without species/stage evidence.


## 20261123T1640Z-cycle-1 Otus sulaensis

Problem: modern secondary phrase 'juvenile similaradult' would erase directly described barred down and dark juvenile eyes. Evidence: Hartert1898p126. Applied: primary-stage colour/barring and dark eyes in prompt; viewedresult preserves them. This validates visual application only. Adult#117/#141 relatedplates not automatically affected; their juvenile source mustbe checked independently. No globaltransfer of this species' iris chronology.



## 20261123T1640Z-cycle-2 Megascops hoyi

Problem: a researchedconcept cantravelwithoutsidecar andreadascalibratedbiologywhennoimagefooter. Evidence: actualv4lackedstatus; researchsayssciencefalseandyoungbarepartscalibrationunknown. Change: visiblependingfooter+specificunknownnote, preservingevidencedstage. Review: bothactuallyreadonv5, notablanketqualityclaim. Backcheckcontactsheetfound#215–218lackfooter; queueannotationrevisiononly, do not countasnewscienceornewspecies. #220/#221alreadyhavefooter—do notregenerateforit. Sourcebodyreuse isnotnewliteraturediscovery.


## 20261123T1640Z resumed annotation audit
Observed4exportedplates215–218 lackedvisiblepending-scientificstatus while sidecarswerefalse. Appliedfooteronly andviewedfull/nativecrop, retainedallunknownnotes/support/stages; toolslightlyrerenderstextures so checkallbirdsaftertextedit. Validatedreadabilityandinvariantsforthese4only, notbiologicalcalibration. #129existingarchive recovery avoidsduplicateimagegeneration. Rejected216darkclawhypothesisafterivoryclawview; nochangejustforchange. Do not turnsource-reusecounts into newdocuments; uploadedguide4pages=1book. Missing-speciesqueue remainsprimarydevelopmentresearchpriority afterboundedannotationqueueclosed.


## 20261123T1830Z #203 annotation audit
Problem: external juvenile observations can belong to another subspecies even when species synonyms match. ITIS686674 and Perez-Martinez2021 confirm CostaRica vermiculatus context; existing203 is nominate. Applied no colour transfer; explicit nominate/juvenile-colour uncertainty note plus scientific-pending footer. Actual full/youngcrop verified labels/support and no actionable morphology drift. Validated annotation readability on203 only; biology remains unknown. Earlier215–218 already labelled, not regenerated.


## 20261123T1830Z actual six-cycle audit
#204 primary1904p106 independently supports narrower/fewer juvenilebreastbars but sourceconflict remains. First edit introduced longhardyoungwing; correctiveedit/nativecrop verified boundedcompactwing. Do not call fieldrecord tentativeyoung or museum singleseries universalstage. ITISsynonym preventsnew-species doublecount. #207 ABSAolderjuvenileformedwing retained. Fiveannotation-only revisions improve exporteduncertainty labels, not biology. New missing-speciesproduction stillprimarygoal; closeboundedannotationqueue and do not repeat alreadylabelledplates. Primaryoldpapernewpage is not newdocument; indexdedupcorrected. Actual ruleefficacy limited to reviewed6plates; no globalclaim.


## 20261123T1933Z cycle1 #235 actual edit
Problem: Socotra style reference leaked its bold pale scapular stripe and hard young remiges into Arabian bird. Bates1936p19/1937p150 support earthy older juvenile with down remnants and weaker shafts; photographed Arabian adults support subdued scapular areas. Applied isolated identity/wing correction and viewed full plus youngcrop. Final softened short formed wing/fragmented buff scapularflecks passed bounded check. Reused style must explicitly exclude donor anatomy; validated only #235. An adjacent catalogue 'youngfemale' belonged another taxon and was rejected; correct pamelae holotype is adultfemale. No general sex-size/flight rule inferred.


## 20261123T1933Z cycle2 #236
Observed bright unsupportedyoungbill and crisp adult-hard lower wing panel. Primary2012 supports qualitative older-young irregular ventralstreaking, not barepartcolour/timeline. Targetededit used mutednon-diagnostic bill and soft contourveil over a retained formedwing. Full/nativecrop verified improvement only for236. A tempting nearby 'especially youngbirds' sentence belongs reyi, NOT spilonota; sectionboundary checked before selecting missingreyi. #235differentstage/reference mustnotinheritthisspecies' pattern. Unknowns remain explicit, not scientificpass.


## 20261123T1933Z cycle3 #137v6
Problem: v5young retained adultlikepale patternedbelly. Evidence FLO-WIDODO1999p21 andguide184 supportnearuniformpalerrufousresidualdown; Table2 specificallysupportsorangeyellowyoungbill. Editcorrectedventralpattern/downcoveragewhile retainingformedwing/tailbands andknownbill. Full/nativeyoungcropverified; notuniversalwingban. Backcheck#235/#236alreadyuseownprimaryyoungrecords and mutedunknownbill; do not transfer137knownbilloruniformrufous tothose taxa. Only137v6effectvalidated.


## 20261124T0332Z actual six-cycle outcomes
Freshmainmanifest perarchive merge verified6times, final916→922 andall6newIDs retained; priorstalesnapshotbugnotrepeated. #210adultbellyregionmaskvisiblypaler; #211/#214softcoveredwingtargetactuallyviewed, notgrowthmeasurement. Backcheck#208mesoptile/#210olderimmature/#213Kodminphoto demonstratesno universalshortwingrule: #213formedwing/tail preserved. #208/#212/#213exportuncertainty annotations actuallylegible, notscientificpass. Primary2018casePVCageestimated labelled; no genericnestclaim. Candidateaurantia/sororcula/castaneum juvenileundescribed → deferred, no inventedtrio. PDFprinted/PDFoffsetmustbechecked: wrong134–136AmericanScops excluded, correctballi100–102=PDF116–118 read. Nextprioritynew-speciesresearch and#201/#206unresolved; do notrepeatboundedannotationqueue as speciesproduction.
