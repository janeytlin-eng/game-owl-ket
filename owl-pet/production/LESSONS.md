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


## 20261124T0432Z cycle1 219-otus-podarginus-v2
PASS_WITH_LIMITATIONS. Initialv1 feathercuffs nearly reached toes. Evidence Yamashina1938pp1–2 says bare tarsi except upperfront. Actualgenerated full plate and native feetcrop viewed: bothadultlowerlegs now visibly bare cream scales; feather retained upperfront, all6feet grip branch. Adultnear-equalscale/rufousbrownbarredplumage/dirtyivorybill/browneyes/reduceddisc/tuftlessheads and youngfluffy ageunknownformedclosedwing retained; no nest/flight. One imagegen edit of v1, no additional corrective edit needed. This validates localleg correction only, not taxonomy/juvenilegrowth or sciencecertification. Backcheck220has featheredtarsus species-specific; do not transferbareleg rule. Youngage/flight/sexmass remainunknown.


## 20261124T0432Z cycle2 221-ninox-meeki-v2
PASS_WITH_LIMITATIONS. Priorv1 juvenile had brown chin merging breast; guide printed496 explicitly almostwhite throat. Imagegenedited throat locally; fulloutput and nativeyoungcrop actuallyviewed: softnearwhite throat nowdistinct aboveplainbrown upperbreast, narrowrustylowerstreaks/whitecovertbars/compactformedwing retained. Adultsunchangednear-equalscale,yelloweyes,mutedslatehornbill,rufouslongventralstreaks; all6feet on mossybranch; featheredtarsi retained unlike219. Closedyoungeyes notagediagnosis. No adultwingban—olderyoungformedwingpattern directlyguide-supported. One imagegenedit,no correctiveedit needed. Actualrulevalidated localcolour boundary only; preciseage/iris/billchronology/flight/sexmass/nestunknown; scientificallyfalse. Primary1914fetch fresh403 recorded, no borrowedfacts. Backcheck219olderyoungbrownthroat is separatetaxon, do notwhiten it.


## 20261124T0432Z cycle3 225-otus-socotranus-v2
PASS_WITH_LIMITATIONS. NewPons2013 actualprimarymorphology/Table3 supports relativelybroadlargerbillversussunia; sexdirectionforbilllength remainsunreported. Editedadultbases are visiblybroader/compacthooked in fulloutput+nativebills crop, no forcedsexcontrast/heightpercentage; neutralbodysizeannotationlegible. Bodyplumage/yelloweyes/baretoes/featheredtarsi/shorttufts andphoto-supportedrecentfledglingformedwing/greyfluff/6supportedfeet retained. Billshape is boundeddesigninference, not measured calibration; no youngtimeline established. One imagegenedit, no correctiveedit needed. Newprimarysuccess supersedes prioraccess-failure as leadstatus only, olderrorhistory preserved. Backcheck235Arabianowl belongsdifferentlineage; no transferSocotrabill-shapeorjuvenilepattern. Sciencefalse.


## 20261124T0432Z cycle4 228-athene-granti-v2
PASS_WITH_LIMITATIONS. v1youngbodycrossbands overlyprominent relativeguide482 'onlyfaint'. Actualfulloutput+nativeyoungcrop: predominantlydarkbrownjuvenile, ventralbars nowfewthinlowcontrasts, whitefoldedwing/tailbars explicitlyretained. Adultbroadbrownonwhiteventrum/whitebrows/crownspots/yelloweyes preserved; all6feetgripbranch, juvenileclosedeyes/lowcrouch unchanged. Oneimagegenedit, no correctiveedit. This validates regionalcontrastcontrol only, notday-age orfeatherlength; guideonlyyoungphenotype, finebareparts/flight/sexmetricsunknown. Backcheck229hasdocumentedSTRONGERyoungcrossbars, so do notapply228faintbarsglobally. Sciencefalse.


## 20261124T0432Z cycle5 229-athene-malaitae-v2
PASS_WITH_LIMITATIONS. Actualfulloutput+nativejuvenilefacecrop viewed: rightyoung cheek/earcoverts nowcarryfineoffwhite transversebarscontinuingcrown/neck, ratherthanplaincheeks; notear-tufts/solidwhitemask. Existing strongerbodybars andadult-likecompactformedwing retained, exactageunknown. Adultsretain darkgreyeyes/palebill/neutralbodyscale; no Guadalcanalyelloweyes/whitebellytransfer. Sixfeet log-supported, billcolour remainsprovisionalforjuvenile, no flight/nestclaim. Oneimagegenedit,no additionalcorrectiveedit. Evidenceguidequalitativeonly; Callaghan2019foundyoungrecord doesnotverifythese markings. Localpatternapplicationvalidated only, scientificallyfalse. Backcheck228youngdarkbody/faintbars leftasdifferenttaxon, not affected.


## 20261124T0432Z cycle6 223-strix-butleri-v2
PASS_WITH_LIMITATIONS. Actualfulloutput andnativeyoungcrop viewedagainstactualKasravi2019referencecrop: a fewshortgreyforehead/crownmarks nowdistinct whilepaledownretained, orangeiris/greyhornbill anddarkfoldedformedwing retained; no genericshortwing/downballconversion. This isphoto-individualbasedcontrastrefinement, notuniversalnewbiologicalrule. Bothadultnear-equalscale/gingerbreast/whitebelly/featheredfeet/rocksupportretained; all6feet supported. NewstatusfooterandIranMay2019 exactageunknownnote legible andnotcoveringfeet; namecurrentbutleri nothadorami. Oneimagegenedit, no additionalcorrectiveeditneeded. Exactage/fulljuvenilefeatherchronology/sexmetrics/nestremainunknown; sciencefalse. Backcheck#164hadorami distinctspecies didnotreceivebutleriphototraits. #230toes hypothesisrejectedafteractualphotoinspection, no spuriousrevision.


## 20261124T0432Z six-cycle postflight
Actual219barelowerleg/221whitethroat/225broadbillbase/228faintventrum/229barredearcoverts/223photoheadmarks eachviewed, boundedapplicationonly. Mainfailurecycle6metadataenteredbeforelocalhashoutputinspection: must parseactualbytes/hash first, assertnonzero/hash64hex and reuse structuredvalues; do not handtype placeholders. No erroneousmetadataeligibleforcredit. Freshmanifestmerge928retainsall6IDs. C1verifierfilenamecheckfixedtoheadercheck. Actualleasevalidthroughallcycles but heartbeatnotrenewedaroundeachlongtool; nextbatchmustactualrenewbefore/after, no retroactivefake. See [complete evidence](batches/20261124T0432Z-completed-review.md). Missingyoungnotinvented and230unfoundedfootrevisioncancelled; don'tturnminorrefinementsinto6newspecies.


## 20261124T0532Z 已实际应用的后续检查规则
- 上传：单次工具输出可能静默截断；先分块≤500000base64字符，验4ceil(bytes/3)总长并把create_blob SHA与本地Git对象SHA比对，再更新tree。仍必须immutableGET长度/SHA256/PIL，不能把create_blob成功当图完好。237发现、220/172/234/232/226已实际应用，六张批次回读通过；不是未经验证提效口号。
- 来源：搜索结果邻接段落不能跨物种搬年龄。226Kakum所谓“幼鸟高哨音”实际属Fraser鹰鸮，已拒绝并保存原文定位。237单只subadult记录与species-only图题关联只算推断，不升级成年龄实证。
- 解剖：喙/cere/下颌分区且分年龄（234）；腿爪先放大，已有正确不重复修（226）。书中雌雄体重差不等于站高比（237/172）。
- 姿态：232调用图鉴明确成年鸣叫/白喉可见，是行为设计变体，不反称旧安静姿态错误。226三季度后侧静息只为显示背横斑/素腹，姿态为设计推断；初稿硬长翼局部编辑后软化，验证局部应用而非发育序列。
- 名录：明确authority+year，保留旧名/ID、从原始更正映射，不能把已并入的名录分量新增计物种，也不能未经全清单核对就改251合同总数。220/172实际应用，其他受影响组图待后续核对，不声称全库完成。
[六组实际检查/独立提交/原图](batches/20261124T0532Z-completed-review.md)。各物种具体unknown保持，科学通过0。


## 20261124T0632Z verified2/6 — narrow evidence recovery
#149v5实际查看后只修正OLDER阶段断言/待科学校准可见标识，不把尚无描述的幼羽说成已校准，不由单一雌雄翼长比推出体高。#201v5原照片403不等于所有一手影像均不可读：实际读取第一方PhotoArk YouTube oEmbed元数据，再打开其明确关联缩略图，恢复有限romblonis浅腹/formedwing视觉证据；原视频仍未看，不声称403已解除。图龄/虹膜/飞行/nominate对应仍未知。已实际应用在201提示/成图并查看复查，非普遍有效性声明。不能把临近段落鹦鹉幼鸟资料或romblonis棕榈巢搬进指名亚种/odiosa。150/152/153/155仅档案预读，未生图未计轮；后续先看原图和实际来源再决定，不凑修订。两图分块base64/GitblobSHA+remote长度/SHA256/PIL均通过。余4轮持久接续第3轮；预算为执行者自报，无固定超时遥测。
[证据与原图](batches/20261124T0632Z-partial-review.md)。

## 20261125T0640Z cycle6 #106v5
Actualfootcrops verify barecreamadultdigits/palehornclaws withfeatheredtarsi preserved. Do nottransferadultfeet toyoung. Correctguide338/PDF340 vswrongprinted340/huhula. Freshguideeyeconflict isrealtextconflict, notinaccessiblesnippet; eyesloweredinphoto cannotadjudicateopeniris. Modelrerenderedfeathers, allinvariantsrechecked. Scopevalidated#106only; #107basaltoefeathering different, noautomatictransfer. [Actualreview](../research/reviews/106-strix-albitarsis-v5-review.md).

## 20261125T0748Z cycle1 #100v6
Oneadultclawpaletteeditactuallyviewedfull/nativecrops: palehornbases/darktips retained, toe/tarsalboundaryalreadyrightnotre-edited. Stagepreserved andunknownage/flightnotinvented. Localapplicationverifiedonly; no universalclawpalette. [Review](../research/reviews/100-strix-huhula-v6-review.md).

## 20261125T0748Z-cycle2 103-tyto-longimembris-v6
# #103 v6 — actual generated full plate + native two adult-foot crops viewed. One imagegenedit. Adult claw shafts now darkblackishbrown with subduedhighlights, fleshpinktoes/longbarelowerlegs/sparsehairs remain; juvenileclawsunchanged. Exactly3birds/title/alllabels/whitefacemale/richerfemale/modestfullness/darkeyes/ivorybill/formedadultwings retained. Centralgoldpowderpuff/partialpinkface/emergingwhitefeathers/compactdowncoveredwing/shortconcealedtail/feetgroundsupport intact; captive55daylabel retained, no wildage/firstflight extrapolation. Tallgrass/unlinedsand supportsallfeet, no inventedtwignest. PASS_WITH_LIMITATIONS, sciencefalse, newuserapproval0, correctiveedit0. Issue→guideblackbrownclaws vs palev5→adult-onlyedit→nativecropsPASS. Contrast #100 needs PALE horn, #103 DARK horn; neveruniversalowlclawpalette. SourceFig1locatorcorrected171/PDF3; table3hasno57daywing/tail. DirectprimaryPDF502 twice; wwwwebbodyrecovered, nofreshphotopixelsclaim.
## 20261125T0748Z-cycle3 98-strix-chacoensis-v6
# #98v6 actual generated full plate and native adulttarsalcrop viewed. One imagegenedit. Sparse short rusty-brown crossmarks nowvisible on predominantlycreamadulttarsi, partial/irregularratherthan solidrufousorheavycontinuousrings. Adultproximaltoefeathers/distalbaretoes/reddishhornclaws/darktips/branchgrips preserved; juvenilelegsunchanged. Wholeplate: exactly3birds, title/currentname/rolelabels, malefrogapproach retainedfrompriorcase, palegreyconcentricfaces/darkeyes/yellowishbill/near-equalscale, whitebarredbodiesandmarkedwings pass. Juvenilefluffygreybuff/softfoldedwing/shorttail/fullfootgrip retained; age/flight/nestunknown. No newflyingornestingclaim. PASS_WITH_LIMITATIONS/sciencefalse, no newuserapproval. Localtarsalmarkcontrastappliedandrechecked, notuniversalpatternproved. Adultclawswerealreadycorrectandnotretouched. Nextbackcheck#99whitishfeatheredlegs belongdifferenttaxon; no automatictransfer. New0/reused2publications, no unnecessaryadditionaledit.
## 20261125T0748Z-cycle4 96-aegolius-ridgwayi-v6
# #96v6 actual generated fullplate and nativeyoungbreastcrop opened. Oneimagegenedit; darkv5shaftstreaks replaced byfewpale/faintbufffinewisps, warmbuffdown remainsdense/soft. Wingcoverts/headstreaks/face/yelloweyes/darkbill/shorttail/feet preserved; no uniformwhiteorplasticbody. Adultsfinecrownshaftstreaks/brownupperparts/plainbuffventra/fleshtoes/darkclaws/near-equalscale unchanged. All3birds/titles/roles/cavity/cloudforest/branchgrips pass; exactage,sex,firstflightandfeathergrowthunknown. PASS_WITH_LIMITATIONS,sciencefalse; no additionalcorrectiveedit. Targetvalidatedlocalcontrastonly, not independentphoto-agecalibration. Actualwebresearcherpage's other-speciesyoungimages NOT used; CAYAYAoriginal404(local)/webinaccessible,notfreshpixels. Bookexplicitpale/faintbreastconstraintactuallyapplied/reviewed. Backcheck#98juvenilefluffybodydiffers andadultbarstarsi NOT transferred. No scientific-pass/newconfirmation.
## 20261125T0748Z-cycle5 94-pulsatrix-koeniswaldiana-v6
Actual full1536×1024 image and both native adult-foot crops viewed 2026-11-25. PASS_WITH_LIMITATIONS: both adult claws now muted yellowish-grey horn with darker tips/contact shadows, matching Mikkola printed313/PDF315; bare grey toes, claw shape/grip/support unchanged. Adult dark brown irides, tawny brows, white throat, broken breast band, buff ventrum and wing/tail bars retained. Three-bird composition/labels and forest branch support remain. Juvenile dark face/iris, residual cream down, soft folded wing, hidden tail and two-foot perch retained; adult claw evidence NOT applied to young. No new age/flight or population size direction asserted. Menq2018 corroborates broad adult/young phenotype, not claw colour. Scientific verification remains false; no new user approval. One builtin edit, 38.129s waiting; no further correction indicated by actual image. The first image response exceeded available model-context output; file result recovered and separately viewed before review. New observation-to-rule: adult-only bare-part palette must leave juvenile feet untouched; applied to this image and visually checked, not generalized as species-stage validation.
## 20261125T0748Z-cycle6 92-ninox-japonica-v6
Actual generated full1536x1024 plate and both native adult-bill crops viewed2026-11-25. PASS_WITH_LIMITATIONS: left and center adult bills now predominantly dark neutral grey/brown horn, only small subdued paler terminal highlights, no large yellow wedge. Matches guide adult darkgrey and institutional darkbrown/paler-tip overlap. Juvenile open bill/gape unchanged; yellowadultiris/toesunchanged. Three individuals, exacttitle/name/labels, near-equal adults, darkhead, whitebetweeneye/scapularpatches, broadventralstreaks, barredtails, fluffier/lessstreakedyoung, compactsoftwing/shorttail/cavity/branchsupport retained. No adult palette imposed on immature, no day/flight/generalized sex sizeclaim. One builtin edit with measured generationwait recorded, zero furthercorrective edits indicated. Rule candidate applied and actualimagechecked: preserve smallpale-tip while avoiding warm light becoming a large yellow bill region; not a measured pigment/age calibration. Primary Table3 sexmeans vs discussion discrepancy retained, not used as geometry. Science=false; userapproval unchanged.
## 20261125T0904Z-cycle1
Fullplate plus both adultfootnativecrops actually viewed. PASS_WITH_LIMITATIONS: short grey-buff dorsal toefeathers now extendfromtarsi overadulttoes; barepinkexpanse removed, claws/distaltips visible andcoherentgrips retained. Threebirds/text/orangeadultirises/hornbills/mottledupperparts/herringboneventrum retained. Centerrecentfledgling unchangeddowny/shortsoftwings/hiddentail/shadowedeyes/twofootbranchsupport; no inventedcavity/age/flight. Primaryp76 featheredtoes is directadultobservation; bookpryeri baretoesexceptionmeansregionalbound, notallsubspecies rule. Onebuiltin edit; no furthercorrectionneededaftercrops. Sciencefalse/userconfirmationunchanged. Rule appliedandvisuallycheckedonthisimage: dorsalfeathersmustpreserveclawandtoecontours, no mittenfeet. Exactdensity/youngfeatheringchronologyunknown.
## 20261125T0904Z-cycle2
Fullplate andbothadultfootnativecropsactuallyviewed. PASS_WITH_LIMITATIONS: pale fine featheringextendsontoproximaldorsaltoes/middletoe, distal scalesandclaws remainvisible; extent shorter than#85, no fullmittenfeet. All3birds/title/labels/palecolours/fineshaftstreaks/near-equaladults retained; centerjuvenile transversebars/softshortwing/hiddentail/littletufts/begging/twofootpalmlipsupport unchanged. PrimaryoccurrencepaperTable1comparisonandguideadultdiagnosisagreebasalextent; exactdensityqualitative. No universalage/sex/flight orsubspeciesassignment. Onebuiltin edit, zeroadditionalcorrections after actualcropreview. Sciencefalse, newuserconfirmations0. Lesson: checkownspeciesproximalvsentiretoeextent, notcopyfeathered-foottemplate; appliedandverifiedonlythisplate.
## 20261125T0904Z-cycle3
Actualfullplate+bothlowerbellycropsviewed. PASS_WITH_LIMITATIONS: adultdensegridbarshavebecomefaintbrokenfinebrownlines, lightertowardsabdomen; faintshaftstracesremain, notblank. Upperbreaststreaks/blackruff/whitebrows/orangeeyes/wings/tails/feet/near-equaladultscale unchanged. Center c35dayyoung softfeathering/shortwings/cautiousgroundstance/twofootrocksupport unchanged, no newflightclaim. Guideprinted274/PDF276 andactualOwlPagesDescription supportqualitativefaintlowerbars; sourceindependencenotproven/contrastnotmeasured. OriginalyoungPDFopenedbutbodygarbled; HTMLretryinaccessible, onlypreviouslypersistedyoungstage reused, notnewphotoreview. Onebuiltin edit104s wait, noadditionalcorrectiveeditneededafteractualcrops. Sciencefalse/newuserapproval0. Reusablelesson: retain fainttraces instead oferasingallbellypattern, appliedandobservedthisversiononly.
## 20261125T0904Z-cycle4
Actualfullplateandbothnativeadultfootcropsviewed. PASS_WITH_LIMITATIONS: adultbaretoesnowduskygrey-brown withwarmhighlights, scales/claws/shapeandfeatherboundariesretained; youngtoesunchanged. Threebirds/text/woodbox/sill/branchsupport/yellowadultirises/darkbills/adultpale scapularband maintained. Studybounded22dayyoungstillsoftresidualdown/compactwing/shorttail/calling/leaningonsill; noextraage/flight/sexratioassertion. Mikkola130/PDF132 andOwlPagesactualDescriptionagreeadultpalette, correlatedsecondaryevidence notmeasuredcolourrange. PrimaryRiekertPDFopened4pagesbut0readablelines; screenshottoolonlyplaceholder, notnewreadphotopixels, historicalstudyrecord reusedandlimitationexplicit. Onebuiltin edit/noadditionalcorrection afteractualcropcheck. Sciencefalse/userconfirmations0. Lessonadultbarepartpalettecanbechangedwithoutextrapolatingyoungchronology, appliedandvisuallycheckedthisimage.
## 20261125T0904Z-cycle5
Full1536x1024plate+bothadultfootnativecropsactuallyviewed. PASS_WITH_LIMITATIONS: adultclawproximalhornnowpalegoldenbrown withdarkerhorn/distaltips/contactshadows, no uniformlyblackclaw; toe skin/featherextent/grip maintained. Detailregeneratedfrom680x453v8JPG to1536x1024, notrecoveredoldhighresolutionoriginal; oldversionspreserved. Exactly3birds/title/labels/continuousadultfacialdiscs/thinouterruff/darkhazelirises/greenishhornbills/tufts/near-equalheight/modestfemaleFullness retained. Youngbluegreyiris/greybill/bare nostrilmargin/noear tufts/finehorizontalbars/softshortwing/twofeetoncavityfloor retained. Naturalcavitytypicalconceptnotexactwoodboxobservation, noexactage/flight. Clawevidenceadults onlynotyoungchronology; colourqualitative. Onebuiltin edit/nofurthercorrectionneededafteractualcrops. Sciencefalse/newuserapproval0. LessonregenerateddetailfromsmallJPEGmustbelabelednewrendernotrestoredoriginal; appliedtocurrentrecord.
## 20261125T0904Z-cycle6
Actualfullplate+bothnativeadultfootcropsviewed. PASS_WITH_LIMITATIONS: adultbaretoesneutralgreyunderthedusklight, greyishbrownclawbases/darkerpointspreserved, footscales/grippingcontours/tarsalfeatherboundariesunchanged. No toe feathering importedfrom#85/#83. Threebirds/text/eyes/greybills/adultpattern/near-equalheight/modestfemaleFullnessretained. Centerrecentfledgling remainsbalancedonefootonbranch/otherjustlifting, softcompactfreshwing/residualdown/shorttail, notairborne; juvenilefeetnotrecoloured. Sourcebook122/PDF124 andOwlPagesactualDescription supportadultpalette; correlatedsecondaryevidence notpigmentmeasurement. BoanoauthorPDF403andpublisherfulltext403; priorsexmorphometricrecordonly, no freshfullPDFreadclaim. Grieco/Blasco locomotionrecordsonlyreused, exactage/flight/sexunknown. Onebuiltin edit/noadditionalcorrectiveeditneededafteractualcrops. Sciencefalse/newuserconfirmations0. Lessonstage-specificadultpaletteandbaretoeextentpreserved, actualapplicationverifiedonlythisimage.
## 20261125T1034Z-cycle1
Actualfull1536x1024plateandnativejuvenilechest/bellycropviewed. PASS_WITH_LIMITATIONS: softnarrowbrown-greytransversebarsnowvisibleunderresidualloosedown; notlongadultshaftstreaksorhardblackgrid, adultplates unchanged. Youngdarkeyes/shorttufts/downsoftenedfoldedwing/hiddentail/twofeetfirmbranchgrip retained. Exacttitle/name/labels/3birds/forest/cavitybackground maintained. Qualitativebarstrength/design notmeasuredagedfeatheratlas; age/sex/subspecies/flightunknown, photoML339711461recordonlynotfreshpixels. Mikkolaactualprinted156/PDF158 correctspriorwrong162/PDF164; BSSIdentificationactuallyread supportsfinebarredyoung. FreshDOIfailed/BioOnePDFreturnediframeonly; oldprimarychronology notcountednewread. Onebuiltin edit/noadditionalcorrection afteractualcrop. Sciencefalse/newuserapproval0. Lessonfinejuvenilebarsshouldremainvisiblewithinfluff, noteraseallmarksduetoyouth; ruleappliedandactualimagecheckedthisversiononly.
## 20261125T1034Z-cycle2
# #80 Otus sunia v6 actual review
Full generated1536×1024 and native juvenile crop actually viewed2026-11-25. PASS_WITH_LIMITATIONS, sciencefalse.
Problem→evidence→change: v5's young was inferred from two semitorques sources, wrongly labelled sunia. Those claims withdrawn in SOURCE_INDEX and v6 research. One builtin edit rebuilt center with WBSJ Kyoto's explicitly labelled コノハズク juvenile photograph; WBSJ current Otus sunia mapping and museum record cross-check the older Otus scops label.
Recheck: rounded head, subdued tufts, yellow iris, soft finely barred lowerbody, formed feathered folded wings and modest tail agree with this later photographed stage. No downy hatchling/adult remex mismatch because stage explicitly changed. Full and crop show both feet gripping same natural branch, no floating body or added limbs; upper adult yelloweyes/darkbills/mottling retained, toe hue subdued gray-brown. Near-equal adult display retained; labels correctly read ADULT MALE / AGE-UNKNOWN JUVENILE / ADULT FEMALE; woodland context not active nest claim.
One revision call, no second edit needed after actual inspection. Exact day, sex, subspecies, age-wide iris rule, wing-growth trajectory, flight ability and calibrated relative size remain unknown. No new user approval.
Lesson: resolve similar Japanese common names before transferring developmental observations. オオコノハズク=semitorques vs コノハズク=sunia. This rule was discovered, applied by invalidating two stable source IDs and rebuilding #80, and locally verified visually; not a retrospective pass of other plates. Audit adjacent Japanese-source Otus records before future reliance. Developed wings are permitted only for the photographed later juvenile, not copied to downy stages.
Source index:4new /3reused /2species-attribution corrections. User guide p152/PDF154 freshly read. Photocopyright originals not committed. See v6 research for all URLs, facts, limitations and full prompt.
## 20261125T1034Z-cycle3
# #78 Asio capensis v6 actual review
Full1536×1024 plus both adult chest/toe crops actually viewed2026-11-25. PASS_WITH_LIMITATIONS, sciencefalse. One builtin targeted revision, no extra edit after recheck.
Problem→evidence→change: inherited v5 prompt asked vertical black ventral streaks, visibly present on both adults. Fresh Mikkola printed518/PDF520 and fresh external MARSH-OWLPAGES-2020 Description support brown breast/fine buff vermiculation and plainer pale lower belly. v6 removes black longitudinal columns, retains fine irregular transverse/buff texture on brown chest and subtle lower belly texture. Mantles now earthbrown with subdued texture; wing/tail bars preserved. Pale toe plumes cover most adult toe surface to distal dark tips/claws; natural earth/grass contacts retained.
Central down-rich young unchanged: dark disc/eyes/black bill, small shoulder feather patches, compact soft wings/tail, low ground/grass support. No stage-specific action added. Near-equal adult height/subtle female fullness, no categorical sex color rule imposed. Title/scientific name/three stage labels retained.
Limits: qualitative pattern/coverage only, no exact age/flight/sex/subspecies/feather count; museum figure403 not inspected and not anatomy evidence; original Commons young page inaccessible this run, old actual-photo record reused. No new user confirmation.
Lesson: a correct species label does not validate inherited drawing prompt. Compare adult underpart pattern type with species account, not merely whether feathers look plausible. Applied and visually verified for #78 v6 only; check other archived Marsh Owl variants before scientific approval. Do not apply Striped Owl's ventral streaking to Marsh Owl. Source index new0/reused3; inherited adult prompt corrected.
## 20261125T1034Z-cycle4
# #76 Asio clamator v6 actual review
Full1536×1024 plus male/female foot crops actually viewed. PASS_WITH_LIMITATIONS, sciencefalse. One builtin edit, no second edit needed.
Problem→evidence→change: v5 adult toe tops largely scaly/unfeathered. Fresh Mikkola printed510/PDF512 explicitly covers tarsi and toes with cream plumage. v6 shows separate cream-feathered toes terminating before black claws, toes contacting same ground/root supports. Foot crops retain discrete digits, natural direction and no fused mitten. Rear digit visibility limited by frontal posture; do not claim all four digits measured.
Adult ventral stripes, dark cinnamon/brown iris, black bill/long tufts retained; unlike #78, longitudinal streaks are appropriate for clamator. Both adults retain comparable crown height, no mass-to-height ratio.
Center label now DEPENDENT JUVENILE; no exact hatch age certified. Fresh external primary2009 Results/Discussion supports young wing exercise before flight, and2025 Methods states age estimation. Low wing stretch, both feet/lower body ground-supported, cinnamon down/short tufts/growing wings remain, no takeoff. Sparse ground plant material at palm-base setting retained, not woven nest or cavity.
Limits: exact age, sex, subspecies, continuous pin/remex geometry, universal flight day and linear sex-size ratio unknown. External feet photo403 means no inspected photo claim. No user approval added.
Lesson applied/verified here: check distal feather coverage separately from feathered tarsus; label estimated development as stage unless the pictured individual is hatch-dated. This is qualitative local validation, not a global scientific pass. Sourceindex0new/3reused actual research sources, plus unverified photo lead.
## 20261125T1034Z-cycle5
# #77 Asio stygius v6 actual review
Full1536×1024 and both adult mantle/wing crops actually viewed. One builtin edit. PASS_WITH_LIMITATIONS, sciencefalse.
Problem→evidence→change: v5 adults carried conspicuous bright gold patches across upperparts/primary surfaces. Fresh guide p502/PDF504 plus fresh specialist Description constrain dark sooty wing, indistinct markings. v6 now has low-contrast feather edging/small sparse faint scapular markings with much darker mantles/primaries; secondary/tail barring and ventral dark shaft streak/crossbars retained. Texture remains, no blank black silhouette.
Center older young unchanged: black disc/yellow eyes, residual pale down, short tufts/barred belly and one low lateral wing extension, both feet on broad branch, no takeoff. Adult near-equal scale/support/text/habitat retained.
Attempted universal toe correction was NOT applied after actual primary Kelso1934 pp522–523 showed robustus-specific sparse coverage and explicit lack of Colombia/Ecuador specimens. Current regional toe coverage remains an open audit question; guide/general synthesis are not enough to force robustus anatomy into Nayón. Full old primary1936 link redirected to repository landing; search text is lead only.
New2/reused2 sources in actual index;2018 Fig2 locator corrected printed24/PDF5. Exact young age/sex/subspecies/flight and local adult toe coverage unknown; no new user confirmation.
Lesson: distinguish adult upperparts from underparts and taxon-specific foot evidence from generic species summaries. Discovery applied here by darkening only adults' upperparts and withholding unsubstantiated feet changes; crop inspection verifies the local appearance change, not regional morphology as a scientific pass. Adjacent #76 and#78 foot rules must not be copied wholesale to #77.
## 20261125T1034Z-cycle6
# #75 Ninox scutulata v6 actual review
Full1536×1024 plus male/female cere crops actually viewed2026-11-25. One builtin edit, no second edit needed; PASS_WITH_LIMITATIONS/sciencefalse.
Actual local recheck: adults have muted dull olive-brown cere above/around nostrils, still blue-black hard bill/small pale tip. No entire green beak, no juvenile soft-part extrapolation. Whiteforehead/yelloweyes/tuftlessheads and individual adult poses retained. Full scene preserves pale-down older dependent young, formed stretched brown remiges and developed barred tail, both feet grip connected mossy support, no takeoff. Adult bodies comparable, no conversion of contradictory unquantified sex evidence into height ratio. Three labels/title remain readable.
Unknown: exact youngage/sex/subspecies/flight/iris/cere chronology, calibrated adult skin color and sex size direction. Shoulder patch concealment not resolved, no gratuitous spot rows added. No new user approval.
Source use0new/4reused IDs; uploadedguide p464/PDF466 and two external source bodies freshly read, NParks prior context. Old fd9d70d422 and local/remote#25files checked; do not regenerate#25. One transient connector RemoteProtocolError recovered.
Lesson applied here: cere color and keratin bill color are separate gates; tiny soft-part correction requires native crops, and must not recolor juvenile without age-specific evidence. Full/crop visual improvement locally verified, no scientific color calibration or global rule success claim. Later-stage long wings from real-photo boundary must not be mechanically shortened just because young retains down.
## 20261125T1144Z-cycle1
# #70 Ninox strenua v6 actual review and iteration
Full initial1536×1024, crown crop and initial toe crop actually viewed; initial fine crown correction succeeded, toe bristles remained insufficiently visible. One additional builtin toe-only edit performed, full edited image and both native adult toe crops viewed. Edited thin individual sparse bristles are visible on proximal toe surfaces, skin/scales and individual digits/claws/branch grips remain; no dense fully feathered boots. Initial original preserved separately from edit1 original. Fine crown flecks retained, pale brow and coarse ventral V-marks/body-wing irregular bars retained.
Recentfledgling retainedwhitehead/darkeyepatches/finespeckles/lightstreaked whiteunderparts/paler barred formed wings and supportedtail, both feet anchored. No automatic erasure of its developed flight feathers; no takeoff. Adults comparableheight and restrained broader male, photographic mask ratio not quantitatively validated. Title unchanged.
Result PASS_WITH_LIMITATIONS/sciencefalse; exact age/sex/flight/feather-tract and sexratio/color calibration remain unknown. No new user approval.
Lesson actual loop: full-size appearance can hide omitted tiny toe bristles. Initial prompt failed that subcriterion; nativecrop identified it, toe-only edit locally improved visible short bristles, rechecked without toe fusion. This validates local correction only, not a reliable preventive prompt or scientific bristle-density reconstruction.
Index0new/5reused records; freshguide p450/PDF452, external MuseumsVictoria Description+Biology and OwlPages Description read. Prior Cooke2020/Mo2015 primary records reused only. Timings initialgeneration and extraedit waits instrumented in run; exact research/archive split not fully instrumented, do not infer fixed platform timeout.
## 20261125T1144Z-cycle2
# #71 Ninox connivens v6 actualreview
Full1536×1024 and both adult body/support crops actuallyviewed. Male-female crown-to-toe difference reduced compared v5, male remains modestly fuller/larger; supports more comparable. No numerical biological ratio certified, remaining pose/perspective difference explicit. Adult yelloweyes/blackbill/whitebrow, whitewing spots, longitudinal streaked pale underside and discrete footgrips preserved. Juvenile remains fluffy-collared older dependent with formed wingtail/white rectrix tips, onefoot securely gripsbranch while other holds loosebark nearbill; no unsupported takeoff or adult-pattern replacement.
Label POST-FLEDGING JUVENILE avoids ambiguous hatch-day claim. Exact depictedindividualage not known; sourcebehaviour was~30daysafterfledging, not fromhatch.
One builtin edit, no additional edit needed after full/crop check. PASS_WITH_LIMITATIONS/sciencefalse; new0/reused3sources. FreshABSAp1 and guide452/PDF454; Bullockabstractread/body403, prior fullreading reused only. No userconfirmation.
Lesson: sex-specific mass/rangeoverlap constrains direction, not exact drawn standingheight. Apply scale restraint and inspect crown-to-foot separately from branch elevations. Age labels must state clock origin or use a stage. Locally visually effective, no global proof or universal timing.
## 20261125T1144Z-cycle3
# #72 Ninox boobook v6 actualreview
Full1536×1024 and nativeyounglowerbody/feet crop actuallyviewed. Onebuiltin edit, no furthereditneeded. Recentfledglinglowerbreast/belly nowcreamy-white down; upperbreast retains localized tawnyband, darkface/powderblueiris/white dark-streaked crown retained. Formed folded wings/tail stayappropriate to selected olderstage, notneonatalwingbuds. Allfeet grey/pinkgrey withdarkclaws andseparate toegrips/scalecontact preserved.
Adultfootcolor is a reference OPTION, not correction of a universally wrong yellowfoot: freshMuseum expressly allows grey OR yellow, whereas ABSA specifies grey/pinkgrey. Conflict caught and recorded beforegeneration; no false consensus. Youngpalegrey/pink andbuff-whiteunderside have clearer stage support. Adultsnotrecoloredelsewhere, near-equalheight maintained.
PASS_WITH_LIMITATIONS/sciencefalse, no newuserconfirmation. Exact youngage/sex/subspecies/irischronology/flight andcolorcalibration unknown. Guidehazelmesoptileiris vsABSApowderblue retainedasstage/scopeconflict, nooverrule. Source0new/4reused, museumactual2026update notedunderstableID; VICPDFtooLarge priorreadingonly. Guide printed455/PDF457 refreshed.
Lesson: compare source agreement before calling an old trait wrong; preserve uncertainty if institution allows variation. Here body correction visually effective, greyfeet only boundedoption. Do not apply dull-yellowfeet from neighboringNinox toallboobooks or adultiris toyoung. No globalscientificpass.
## 20261125T1144Z-cycle4
# #73 Ninox rufa v7 actualreview
Full1536×1024 and nativeadultcrown/chest crop actuallyviewed. Onebuiltin edit, noextraeditneeded. Adulttopheads nowfine lightbrown transversebars onrufous, notlargewhitespots. Richrufous breastbelly creamyfinebars narrower/subdued vs v6 brightbrokenwhitebands. Whitebetweeneyes/goldeneyes/greyblackbill, restrainedmale-larger direction, v6proximalrufoustoeplumes+bare distal dirtyyellowtoegrips retained.
Centerrecentfledgling unchangedwhitehead/darkmask/unverifieddarkiris/whitishdown/formedbutsoftfoldedwing/shorttail andcarefulstep withonefootonbranchotheronconnectedrootlip; no takeoff/adultcrownpatterntransfer. No freshclaimsresolveiris oruniversalage.
PASS_WITH_LIMITATIONS/sciencefalse, userconfirmation0. New0/reused2evidencesources: freshguide448/PDF450 andfreshprimaryRiddell2021body p221–228; Bouglouan503 neverbodyread, explicitaccesscorrectionpersistedbeforegeneration. Patternwidth/color qualitative, exactscales andindividualsexratio unknown.
Lesson: adult crownpattern and bellypattern independentlychecked; thinning bars must noteraseallbars or substitute spots. Thislocalvisualchangeverified, notscientificcalibration orpreventivepromptsuccess acrosslibrary. Preserve prior localizedtoe correction whileeditingelsewhere.