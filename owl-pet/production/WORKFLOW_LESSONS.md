

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


## 2026-11-23 — #202 older-young formed-wing / crown isolation
Observed initial image: older immature acquired long hard remige tiers and adult crowns acquired many white shafts from the style reference. Primary1878p359 permits formed juvenile unbarred wing/tail with residual grey down; guide2013p484 says adult crown plain dark with some white forehead. Applied one edit to compact/soften the wing and confine white bristles to forehead, while matching adult standing scale to guide's slight female-fuller direction. Edited full and three crops actually opened and passed with limitations; this is visual verification for #202 only, not universal feather removal or sex-ratio science. Retrospective comparison limited to initial202 and previously viewed #179 style reference; other species not revalidated. Complete251 roster absent is now explicitly recorded; avoid endless revisions and prioritize deduplicated unarchived species. Historical scratch prune prevented local #25/fd9d70d recovery; existing main assets preserved.


## 2026-11-27 1734Z actual evidence update
78v7 adult inner periocular field corrected separately from outer disc rim;84v10 crown contrasted with mantle, visually effective local corrections, not universal scientific certification.79v7 two targeted edits retained looplike barbs: NEEDS_REVISION, no claimed rule success.81/82 stage labels distinguish source chronology from unmeasured individual age.80 clinical rescue injury cannot calibrate normal flight. Neighbor81/82 looptexture warrants later audit, not yet fixed. Largebase64 output silently truncated at1048607 chars: bounded chunks+expectedlength+immutablebytes/hash/fullPNGdecode resolved78; length must be checked beforeblob, not only header. Source/phase API transient errors recovered without duplicate credit. [Full evidence](batches/20261126T1734Z-six-cycle-review.md).


## 2026-11-27 1830Z actual iteration
79v8: same-species institutional realjuvenile pixels + entirecenterrebuild followedby lowerbellylocaledit substantially improved loops comparedwith surface-preserving negatives, but residualstylization notscientificpass.85v7: ownprimaryphoto/downstage/irisunknown kept, samegeneralstrategy still leavescurltexture => NEEDS_REVISION, no universalruleclaim.83v7: oldpalmstand fieldrecord doesnotauthenticate drawnactivecavity/sawnfloor; naturalsupport replacesinference.88v7: adultdorsaltoeplumes distinct frombarepads/distaltips/juveniletoes; localfull/cropchecked.86/87: population/studytime notmeasuredindividualage, sourceoperationalevents notinterchangeable.86textureflag retainedunmodified. Intermediates persistedlate thisrun; futureIMAGE_GENERATED checkpoint shouldretain attemptedsource beforelongedits too. [Sixoriginals/source/phase/error evidence](batches/20261126T1830Z-six-cycle-review.md).


## 85-otus-semitorques-v8 2026-11-26T19:34:43.009Z
Actualv7, attempt1, attempt2 and final3 full plates viewed plus final adult toe crop. Attempts1/2 retained loopy filaments; no texture success. Final3 selected from v7, only adult dorsaltoe shortfinepaleplumes added, hornclaws/naturalbilateralbranchcontact visible; crop confirms narrowfeatherstrands instead of former nakedscaled dorsa. Adult orangeiris/greyhornbill/tufts/herringbone/near-equalheight remain; young down/incompletewings/shadowiris/quiettwofoot support retained without unsupported olderstage transfer. Young looptexture remains NEEDS_REVISION; exactage/iris/flight/sexratio and precisiontoeextent unknown. Adult dorsalplumage issue improved visually; do not claim wholeimage sciencepass or totaltexturefix. No newuserconfirmation. Pattern: same-image textureprompt even wholecentershapechange remainslocked in unwantedsubstrate; three actual imagegen calls, firsttwo explicitlyfailed. New targeted anatomicaledit is successful bylocalview, texturestrategy notvalidated.


## 86-otus-elegans-v7 2026-11-26T19:38:15.203Z
Actual fullv6 and finalv7 viewed. Bothadults now neutralgrey baretoes/blackishhornclaws, tarsalfeathers stopnearbase; exact toegrips andbranchsupport maintained. Rightyoung toes unchanged (not agecolours extrapolated), compactfoldedwings/shorttail/begging/dualfootcontact retained. Adult yellowiris/darkbill/tufts/herringbone/near-equalheight preserved, Casuarina/cane context and creamgouache style/labels unchanged. Palettecorrection visiblyeffective; spectralprecision, picturedage/youngcontinuousplumage/flight/sexratio and residualcurltexture remainunverified. PASS_WITH_LIMITATIONS/sciencefalse; no newconfirmation. Ruleappliedandchecked: #85 featheredtoe evidence cannottransfer to#86 baretoes; adultcolours only when youngunknown. Prior indexprintedpage/iris/toepalette correction saved; MOE503/newpaperfindtimeout notclaimedread.


## 89-bubo-bengalensis-v7 2026-11-26T19:41:39.628Z
Actualfullv6/finalv7 and enlargedleftadultfootcrop viewed. Smallslategrey baresegments immediatelybehindblackclaws now distinguishable whilefulvoustarsal/proximaltoefeathers kept; highwarmilluminationmeansgreenhue subdued ratherthanmeasured. No whollybaretoe/mitten, stableallfootgroundcontact. Rightadultsamequalitativedistalboundary, youngunchanged; orangeeyes/darkbills/tufts/near-equaladultheight, faintbellybars/upperbreaststreaks androckscrubpreserved. Actualeditvisiblylocalized, exactjointlength/scalecount/colorimetryunverified; c35label is studyreferenced approximation notdatedindividual. PASS_WITH_LIMITATIONS/sciencefalse, newapproval0. Ruleapply: separate adult distalbarejoint exception from proximalfeathering; broadphotocaption'fullyfeathered' noteraseexplicitbodyexception. No transferredadulttoeextenttoyoung.


## 90-tyto-furcata-v6 2026-11-26T19:44:07.162Z
Actualinputv5/outputv6full viewed: STUDY-REFERENCEDNESTLING and science/individualage-flight-sexratiofooter readable. Centralwhite-downyoungstands twofeet onwoodfloor, shortemergingdarksidefeathers/noadulttail retained; notclaimsP20certification or flight. Adultwhiteheartfaces/darkeyes/creambills, palermale/darkerandmorespottedfemale/near-equalskeletalheight, allgrips/loft/background/layoutretained. Annotation-onlyPASS_WITH_LIMITATIONS/sciencefalse, notnewmorphologyvalidation. Handraisedcontainer-supportedstudy generalstandingcontextnotwildphaseclock; no newFig1photopixelinspection. Rulecandidateappliedandviewed: studycalendar inresearchdoesnotdateeachillustratedindividual; explicitimageboundarynowexportswithart.


## 91-tyto-javanica-delicatula-v6 2026-11-26T19:46:15.678Z
Actualv5/finalv6full viewed. Study-referencednestlinglabel/footer readable; current91taxonomy preserved. Threeowls, darkeyes/palebills/heartface/spots, adultnear-equalheight, supportedleaningyoungwithresidualdown/freshformedfoldedwings/shorttail andtwoseparatehollowfootgrips intact. NaturalMalleehollow/farmland retained; notuniformshortwingrule. Annotation-onlyPASS_WITH_LIMITATIONS/sciencefalse, no newuserapproval. FreshprimaryAssumptions/Definitionspp117–118 explicitlyageestimated/asynchronousandfledgingoperationalroostdefinitionnotmeasuredfirstflight; c40behaviorp120 supportsconceptnotexactindividualday. Ruleappliedandactualchecked: exportindividualunknown withouterasinglegitimateolderyoungwingdevelopment.


## 92-ninox-japonica-v7 2026-11-26T19:50:11.763Z
Actualinputv6/outputv7full viewed: AGE-UNKNOWNDEPENDENTYOUNG/scientificpendingfooterreadable, title/currentname92 unchanged. Adultsleftcenterretaincorrecteddarkgrey-brownbillswithsmallpaletips, yellowiris/yellowbristledbaretoes/creamfeatheredlegs/broadbreaststreaks/barredtails/noear-tufts/whiteshoulderpatches/near-equalheight. Rightyoungpalerbuff/sparserstreaks/fluff/openbegginggape/compactfoldedwing/shortconcealedtail/bilateralbranchgrip maintained, naturalcavity/orchardcontextstable. Annotation-onlyPASS_WITH_LIMITATIONS/sciencefalse, no newuserapproval. Primary25–28dnestperiod notpicturedindividualage/firstflight; adultpaletteandTaiwanmeasurementoverlap notyoungcolourseries/globalRSD. Ruleapplied/rechecked: preservepreviousvalidadultbillfixduringstageannotation.


## 85-otus-semitorques-v10 2026-11-26T20:37:45.047Z
Actual v8record/styleadultcrop/primaryFig3photo, v9failedtextedit, v10fullandyoungcrop viewed. V10 shows materiallylesslongoutlinedringlets thanv8/v9: densefinegrey tonaldown with shortirregularfuzz, distincttufts/incompletefoldedremiges/concealedtail, shadowiris/greyhornbill, lowbilateralbranchforksupport. Somefinerstylizedfilaments remain, exactfeatheratlasnotverified. All3rolelabels/current85title/footer nowinfirstimage, no furthertexteditdrift. Adultorangeiris/herringbone/greyhornbill/featheredtarsiandtoedorsa/hornclaws/near-equalscale preservedinnewcomposition. PASS_WITH_LIMITATIONS/sciencefalse, no newuserconfirmation. Texturedownimprovedinthisoutputonly, notuniversalnewrulevalidation; v9archivedfailure notcredited. Adult-onlystyleinputs+ownspeciesphotogivenfreshjuvenile substrateandfirst-renderlabelplacementhelpedthiscase; possibleage/iris/flight/sexratio/continuousfeatherunknown.

## 86-otus-elegans-v8 2026-11-26T20:41:46.030Z
Actualv7/firstedit/secondeditfull viewed: first horizontalnetworktooheavy/repetitive; secondnow muchfiner/fainterirregulartransversewisps whileverticalshaftstreakspresent. Finepatternstillstylizednotquantifiednaturalspacing; no scientificpass. Adultbaregreytoes/blackhornclaws/featheredlegbases/yelloweyes/darkbill/tufts/near-equalheight preserved. Rightyoung unchangedcurltexture/unknownphase notsolved, compactfoldedwing/shorttail/twofootgrips andshelterbelt/cane/creamgouache/textstable. PASS_WITH_LIMITATIONS/sciencefalse/no newconfirmation. Prompt'addfinecrossmarks' overshot todecorativemesh; explicitamplitudereduction workedvisuallyonthisimage, notuniversalpatternrule.

## 93-aegolius-harrisii-v6 2026-11-26T20:43:45.069Z
Actualv5/v6full viewed: centralSTUDYREFERENCEDNESTLING/footerreadable, current93taxon/locality/adultlabels retained. Youngdevelopingdisc/softshortfoldedwing/residualgreydown/shortconcealedtail/lowtwofootbellywoodchipsupport unchanged; noearlydownhatchlingorflightclaim. Adultplainorangebuffventrum/darkroundface/yelloweyes/palebill/wingpalespots/twotailbars/near-equalheight retained, schematicdeadgarapacutawaynotliteraldoorsize. Annotation-onlyPASS_WITH_LIMITATIONS/sciencefalse/no newconfirmation. Primaryp153–15424dspotdevelopmentstrongerthanoldguidep447unknown/unspottedbackgeneric; no unsupportedpatternerasure. Exactage/sex/firstflight/tracts/toegeometrystillunknown.

## 94-pulsatrix-koeniswaldiana-v7 2026-11-26T20:46:27.229Z
Actualv6/v7fullview: sciencepending/age-flight-sexratiofooter readable, ageunknownpostcavitylabelunchanged. Threeowls/stablefootcontacts, adultchestnutiris/tawnybrows/ivoryyellowbill/brokenbrownchestband/cinnamonventrum/narrowtailbars/near-equalheight/greybaretoes/yellowishgreyclaws remain. Centralcreamdown/darkbrownmask/darkeyes/compactwing/hiddentail retainedwithoutadultclawpalettetransfer. Branchhabitatnotliteralnest. Annotation-onlyPASS_WITH_LIMITATIONS/sciencefalse/no newconfirmation. Primarycalendarfiveweeksis inferredincubationnotyoungage; explicitunknownnotfullfeathercalibration.

## 95-pulsatrix-melanota-v7 2026-11-26T20:48:59.858Z
Actualv6/v7full viewed: AGEUNKNOWNDEPENDENTYOUNG/footerreadable, 95title/currentname/adultlabels preserved. Oldercentralwhitepatchycrown/cinnamondown/blackmask/darkiris/yellowbill/tinychestfeathers/shortsoftwing/concealedtail/belly+feetforksupport remain. Adultdarkeyes/paleyellowbills/whiteface/broadbrownchestband/rustybellybars/nearequalheight/feetstable, exposedorganicfork/shadecoffeeplantain unchanged. Annotation-onlyPASS_WITH_LIMITATIONS/sciencefalse, notcalibratedindividualfirstflight/nestoccupancy; no newconfirmation. Repeatedcurlyfeatheredges stillcandidateforphoto-boundedtextureaudit as#85family, notfixedhere; no scientificpass. Newprimaryfactonefemaleidentifiednotsexratioproof.

## 96-aegolius-ridgwayi-v7 2026-11-26T20:52:13.264Z
Actualv6full/sourcefirstpartyjuvenile878x700/v7full/nativeheadcrop viewed. Centralcrownlongbrightwhiteshaftsremoved, nowdensefinewarmgrey-brownshorttexturelikephoto; whiteeyebrows/lores preservedratherthanblankface. Adultfinecrownshaftstreaksunchanged, yelloweyes/darkbills/near-equalscale/fleshtoessparsebristles retained. Lastv6youngfaintbuffbreastwisps notrestoredtobolddarkshafts, bodyfluffy/compactwing/concealedtail/bilateralbranchgrip maintained. AGEUNKNOWNDEPENDENTYOUNG/footerreadable, 96taxon/title/adultlabels/cloudforest/cavitystable. Contentcrown+annotationPASS_WITH_LIMITATIONS/sciencefalse/no newconfirmation. Photoheadonlynoexactage/sex/flight/wingfootdata, notspecimen-general/universaljuvenilepattern. Ruleactualappliedandlocalviewverified: specificyoungcrownreference maydifferfrom legitimateadultshaftstreaks; preservevalidadultpattern andpriorbreastfix. CAYAYAoldinaccessible, alternatefirstpartydocument/newpixelsreadnotclaimedtwoindependentphotos.

## 95-pulsatrix-melanota-v8 2026-11-26T21:40:16.701Z
Actualv7record/adultstylecrop/uploadedguidep314wholephoto+upperbodycrop, newfirstdraft/finalfull/nativeyoungcrop viewed. Finalcinnamondown has directionalsofterfineflecks/irregularclumps and markedlylessrepeatedclosedringlets thanv7; creamcrown/darkmask/darkiris/yellowbill/tinychestfeathers/compactdevelopingfoldedwing/concealedtail/twofoot+bellyforksupport retained. Somefinefilamentstylization remainsnotliteralatlas. Primaryoldergroundyoungphase notnatalhatchlingandnotexactguideolderformedwingtail transfer. Adultsdarkeyes/whiteface/paleyellowbill/broadchestband/rustybellybars/featheredlegs/baretoes/nearequalheightcorrectinnewcomposition. Firstgoldboxes/rulesremovedinsecondcall; plainwhitelegibletitle95/roles/footer nowconsistent. PASS_WITH_LIMITATIONS/sciencefalse/no newconfirmation. Freshadult-onlystyling+photodownreferencehelpedinthisimageonly; graphicsre-edit didnotobviouslyrestorev7loops. No newFig3pixelsclaim/flight/sexratio.

## 86-otus-elegans-v9 2026-11-26T21:42:18.228Z
Actual institutional2011PDF printed4 Photo1 fullpage/head crop, v8 and v9 full images viewed. Right young crown/cheeks now shorter directional soft down, repeated closed loop filaments markedly reduced on head; some long fine wisps and body curls remain. Scope is head only; actual photo lowresolution and nest-cavity head cannot support body/age/flight. Adult fine faint crossmarks/shaftstreaks, yelloweyes/darkbills/greybaretoes/blackclaws/near-equalheight, Casuarina/cane, allsupport/labels/footer retained. Young existing folded wing/body/branch pose remains age/phase/firstflight unverified. PASS_WITH_LIMITATIONS, scientifically_verified=false, no new userconfirmation. Photo reference plus tightly scoped head correction visually worked here; not a validated universal down rule and not body correction.

## 97-lophostrix-cristata-v7 2026-11-26T21:45:51.849Z
Actualv6/firstedit/final fullimages and guide p358 text viewed; external Boliviabody read. Final adult lowerbreast/belly now palebrown with finer fainter irregularvermiculations, notoldboldblackzigzags. Firstedit incorrectly paledupperbreast; second restoreddarkchocolateneck/upperbreast and smalldullyellowthroat, mergingto palelowerbelly. Width/contrast qualitative, notmeasuredbiologicalthreshold. v6narrowtailbars/wingbars/whiteplumes/darkorangebrown eyes/yellowhornbills/baregrey-browntoes/darkclaws, near-equaladultheight retained; youngwhite/darkrufousface/shorttufts/foldedbrownwings/twofootlowforksupport unchanged andage/flightunknown. Labelsnowageunknownandsciencepending, legible. Some decorativefinefeathertexture remains. PASS_WITH_LIMITATIONS/sciencefalse/noapproval. Lesson: restrict faintpattern edit to LOWER underparts and explicitlypreservedark upperbreast; applied2ndprompt andviewvalidatedinthisplate only. Prior#86shaftstreakcrossmarks aredifferenttaxon, no transfer.

## 98-strix-chacoensis-v7 2026-11-26T21:47:35.707Z
Actualv6/v7 fullplates read against original NBO2013body+guidep336. Bothadultbills now muted horn-grey/brown nearbase gradingto yellowtip ratherthan solidyellow; samebeakshape/malefroggrip preserved. BroaderNBOyellowishbill and guidespecificbase/tip compatible qualitative descriptions, not calibratedcolourproven. Adultdarkiris/paleconcentricface/barredventrum/sparsecream-tarsalmarks/proximaltoefeathers/reddishhornclaws-darktips/twofootgrips/nearequalscale retained. Centralyoung unchangedveryfluffygreybuff/palegreyface/darkeyes/compactwing/shorttail/fullfootgrip, age/flight/barepartcolour/stage unresolved; curls not newclaim. Textnowageunknown/pendinglegible; no extraanimal/nest. PASS_WITH_LIMITATIONS/sciencefalse/noapproval. Lesson: narrowadultbase/tip colour edit can retain tip/shape in thisplate; do not import to young or#97bill.

## 99-bubo-magellanicus-v6 2026-11-26T21:50:09.345Z
Actual v5 and v6 fullplates viewed vs freshNovoaBlanco2020p32 body. Newbare continuous tiled/concrete balcony floor completelyreplaces fabricateddrygrass/leaves/twigrim, youngbellyandtuckedfeet supportedatfloor, nofloat; adultstableledges/footgrips retained. Younggreywhitedown/eyesopen/compactshortwingbud/no mature remiges/no tail unchanged, approx20daycasecaption retained butnotexacthatchorflightclaim. Threebirds remainillustrativecomposition not literalFig1two-young count. Adultnarrowtufts/yelloweyes/bluegreybill/whitethroat/finebars/dirtywhitetoefeathering/darkclaws/nearequalheight pass. Labelsrecordedcase/pending legible, no eggs/additional animals. PASS_WITH_LIMITATIONS/sciencefalse/noapproval. Historicalv5nestmaterialsourceassertioncorrectedandindexed, notsilentlyerased. Lesson: case-specific floor/lining sentence overrides genericowl-nest assumption or anothercasephoto; applied andviewedhere. Backcheckotherbalconycaseart should requirecaseID, not blanketremovealllining.

## 100-strix-huhula-v7 2026-11-26T21:52:22.573Z
Actualv6/v7 fullplates viewed plus freshHUH-BC2013p175body andguide340. Annotation-onlytargetcomplete: age-unknown nestyoung, S.h.albomarginata recordedstage and exactage/firstflight/sexratio-unverifiedscientificpendingfooterlegible. Threebirds/currentname/adultrolelabels maintained; rounduntuftedadultheads/darkbrowniris/yellowbill/finewhitishwavebars/featheredtarsi/bareochretoes/palehornclawbases-darktips retained. Centralpalegreyblackbarredyoung/heartmask-whiteborder/yellowbill/compactfoldedwing/concealedtail/active-supportedstanding unchanged; allfeet supportedonbroadangicoepiphyticfork, no cavityinvented. Primarywalkingobservationdoesnotproveflight orprecisehatchage; illustrationcompresses nestarchitecture and isnotmeasuredreconstruction. PASS_WITH_LIMITATIONS/sciencefalse/noapproval; notcountedasnewmorphologicaldiscovery. Lesson: afteractualcheckfindsnojustifiedmorphologyedit, preservevalidcontentandmakecase/unknownstatusvisible; annotationonlydistinctfromsciencecalibration. URLrecoveryupdatemustnotclaimredirectcollectionaspaper.

## 103-tyto-longimembris-v7 2026-11-26T22:30:46.370Z
Full v6/v7 plates actually viewed. Annotation-onlylabels captiveCASE and face/wing/firstflight scientificpending legible, exact3birds/title/adultroles retained. Adultwhitefacemale/richerbufffemale/modestfullness/darkiris/ivorybill/verylongfleshbaretarsi/toes anddarkblackbrownclaws unchangedatconceptlevel; juvenilegoldmesoptile/pinkpartialface/emergingfacialfeathers/compactconcealedwing/no longtail/allfeetgroundsupported/unlinedsand+tallgrass stable. Noactual55dayphotopixels recovered: pinkskinextent/featherage/flight remainunknown, notscientificpass. Primary alternateURLalso502 afterready; no biologicalpaintdonefromfailedphoto. PASS_WITH_LIMITATIONS/sciencefalse/no newconfirmation. Lesson: specificunverifiedfacialstage mustbevisible evenwhenapproximatecaptiveagehascaptionevidence; explicitmissingdetail notfalsepicturevalidation. #99barefloorcase not transferredtoothernests; thisgrasssandindependentlysource-supported.

## 101-otus-spilocephalus-v9 2026-11-26T22:32:41.076Z
Actualv8/v9 fullplates andfreshmuseumrecordbody/guidep148read. AnnotationonlyTaiwanrace/youngirisagefirstflightunverifiedclear; all3birds/title/adultroles consistent. Adultshortlowtufts/yellowiris/creambills/tea-brownvermiculation/featheredtarsi/barepink-browntoes/nearequalheight, youngyellowbrownvaguemarks/darkunverifiediris/compactsoftwing/concealedtail/bothfootlipgrip stable. Noeyecolourfactcreated, nofirstflight oractivebroodclaim. Hollow remainsillustrative. PASS_WITH_LIMITATIONS/sciencefalse/noapproval. Lesson: 'conservative darkiris' is designchoice, not measuredyoungstate; explicitannotationapplied/reviewedhere only. Museumonefemaleandoneunsexedskinsnotsexratio; bookcross-racephotoreferenceNOTimported.

## 104-asio-madagascariensis-v6 2026-11-26T22:35:57.849Z
Actualv5/v6 fullplates + uploadedp509twoadultphotos viewed. Bothadultperiocularfeathers nowdarkbrownsoftzones beyondthineyelidrims, blendedtotawnycheeks whilepalebrows/lores/outerrim/orangeiris/blackbills preserved. No allblackface andno youngmasktransfer. Qualitativeshade notcalibratedcolourmeasurement. Longnarrowflexibletufts/crown/upperpartpattern/sparsefinelowerbellyshafts/tarsitoebasefeathers/darkclaws/nearequaladultheight retained. Youngwhitecreamfluff/darkmask/shorttufts/formedsoftcompactbrownwing/concealedtail/bothfeetsteppingonbranch supported; exactage/iris/flightunknown. Labelsfooterpendingcorrect,3birds/env stable. PASS_WITH_LIMITATIONS/sciencefalse/noapproval. Lesson: adultperiocularfeathers aredistinctfromiris/eyelidring; boundedshadeeditvisuallyworkedhere, no universalmaskrule. Chapterfreshaccessfailed400/403, nofalseprimaryread or exactbroodage.

## 105-ptilopsis-granti-v9 2026-11-26T22:38:33.880Z
Actualv8/v9fullplates andnativev9adultventralcrop viewed againstfreshADWbody+guidep256. New sparse faintthinbrowntransversewisps visiblebetweenstrongshaftstreaks, mostobviousrightadultlowerbelly, notdarkclosedloopmesh; shaftsremainpredominant. Patternstillstylizedandcontrastqualitative; sourcehasnomeasuredspacing. Adultwhitepalegreyfaces/blackruff/orangeredeyes/creambill/longtufts/wingtail/toebasehalf-feathers/duskytoes-darkclaws/nearequalheight stable. Centralyoungcompletelyretainsyellowgreyeyes/shorttufts/softlessmarkedfluff/compactformeddown-fringedwing/concealedtail/twofootgrip; exactage/firstflightunknown. Threebirds/title/labels/newpendingfooter/savannasupportpass. PASS_WITH_LIMITATIONS/sciencefalse/noapproval. Prior86overshootrule(onefifthcontrast/thinbrokenirregularwisps) applied; thisfirstoutputdoesnotshowthickmesh, onecasevisualsupportnotuniversalvalidation. Do nottransferadultvermiculationintoyoung.

## 102-strix-nigrolineata-v6 2026-11-26T22:41:28.599Z
Actualv5/v6 fullplates andnativeadultfootcrop viewed. Adultclawshafts nowmutedtan/yellowishhornwithnaturaldarkertip/shadow vsoldcharcoal, samecurvature/toenumber/grip andorangebaretoes/barredfeatheredtarsi. Colourqualitative notcolourimetric. Youngclawsstaydark, noadultpaletteapplied. Adultdarkreddishiris/orangeyellowbill/blackbib/sootyupperparts/whiteblackventrum/fullerfemale-nearequalheight stable; youngpale-barredmesoptile/darkeyes/compactrounddown-softwing/concealedtail/lowtwofoot+bellyepiphytesupport retained. Threebirds/title/currentname/roles/Tikalregionalpendingfooterlegible. Image resynthesizedsomefeatheredges butno count/support/stagedriftobserved. PASS_WITH_LIMITATIONS/sciencefalse/noapproval. One measuredpairmassnotheightformula; noflightthreshold. Lesson: clawshaft colourtreatseparatelyfromtoe skin/tipshadow, specificyellowishhornhere differentfrom103darkhorn/106palehorn; applied/recheckedhereonly.

## 106-strix-albitarsis-v6 2026-11-26T22:44:36.949Z
Actualv5/v6 fullplates viewed againstfreshGreeney2003p67original/guidep338/PeruAvesIdentificationbody. AnnotationonlynewAGEUNKNOWNROOSTINGYOUNG/dayroostcontextandscientificpendingadultEYE/BILLconflict/firstflightunverifiedlegible. Noiris/billrepainting: adultdarkiris/greybillretainedpendingbookorange/yellowhorncontradiction; adultfeatheredtarsi/barecreamtoes/palehornclawsvalidv5fixpreserved. Adultsroundheads/rufousbandedplumage/nearequalheight, youngyellowcreamdown/darkeyes/compactwing/concealedtail/lowtwofoot+bellygrip stable. Fernleafbasesattachedtreefern/Chusquea-dayroost retained, no fabricatednestmaterial/eggs/flight. Exactly3birds/title/adultrolespass. PASS_WITH_LIMITATIONS/sciencefalse/noapproval, unresolvedcolourandpreciseyoungstage remain. Lesson: opposingtextsourcesdonotjustifyarbitrarycolourchoice; annotateconflict, retain priorvalideditandseparateroostfromnest. Actualfreshcross-sourcecheckdidnotsettleconflict; no claimofvalidatedcolour.

## 2026-11-27 2334Z 107-strix-fulvescens-v6
Problem: v5 adult toe skin had pink cast. Guide p345 and expert Description64–66 agree exposed toes are yellowish/yellow-grey; targeted edit corrected adult skin only and actual full-image review verified basal feathers and dark claws retained. Rule applied and visually checked once: toe-colour edits must specify feather-boundary and age scope, preventing adult-to-young transfer. No general biological validation claimed.
[Actual review](../research/reviews/107-strix-fulvescens-v6-review.md)


## 2026-11-27 2334Z 108-otus-rutilus-v6
Annotation gap→metadata provides photographed date but no hatch age/flighttest, and guidejuvenileunknown→caption AGE UNKNOWN / PERCH ONLY · FLIGHT UNVERIFIED added and actually read in final. Fresh sourcephoto403 prevents new morphology claims. Guide allows natural herringbone-like markings, so prompts should distinguish biological branching from rigid synthetic repetition; clarification discovered, not globally applied or verified. Prior #108v5 and #107v6 reviewed for scope; no blanket pattern removal.
[Actual review](../research/reviews/108-otus-rutilus-v6-review.md)


## 2026-11-27 2334Z 109-ptilopsis-leucotis-v10
Problem: juvenile iris imported adult orange. New Morita/Mikkola2025 p92 and guidep254 support juvenileyellow; local iris-only edit applied and actualoutput checked yellowyoung/orangeadults/titlev10 plus all support/text invariants. New primary captiveadult case must not normalize dark eyes in wild or supply juveniletiming. Prior#105/#109 age-role palette scope compared; no crossspecies iris inference. Residual regular feather texture/toe extent remains queue, no fullscience claim.
[Actual review](../research/reviews/109-ptilopsis-leucotis-v10-review.md)


## 2026-11-27 2334Z 110-megascops-barbarus-v7
Broadbright juvenile brows→guidep214 mesoptile narrow/indistinct→brows reduced only, ageunknownlabel added, actualfullresult verified. Adultpinktoecorrection fromv6 retained. CAYAYA researcher warns adult tuft lengths variable, so no false global tuft-shortening rule. Applied stage-specific brow distinction to110 only;107/108/109 priors rechecked visually and no transfer. Curl-like juvenile texture remains unresolved and prioritized, no claim fix from label.
[Actual review](../research/reviews/110-megascops-barbarus-v7-review.md)


## 2026-11-27 2334Z 111-otus-cyprius-v5
Bare fledged label→fieldsequence gives dependentfledgedyoung but no individualage/flighttest, publisherMethods intervalmidpoint→ageunknown/flightunverified added and actualread. SameDOI titlewrong inoldindex correctedwithhistoryretained, no newsourcecount. Prompt distinction applied to111 only,108 alreadyannotationchecked; no claim bothspecies share developmentalclock. No unchanged morphology declared newlycalibrated.
[Actual review](../research/reviews/111-otus-cyprius-v5-review.md)


## 2026-11-27 2334Z 112-asio-abyssinicus-v6
V5 juvenile closed loops recur despite prior anti-curlprompt. ActualMaton1989pixels showfineirregulardown and formedwing/tail, not yarn. Threepasses: firstfailed, second/third reduced longlightlooplines but residualfineclosedloops persist in actual690x960crop→NEEDS_REVISION and priority112v7, notscientificpass. Negativeprompts plus localidentitypreservation can lock unwantedtexture; material-rebuild wording tested but NOT proven effective. Recheck107/108/109/110/111 actualbaselines:109plasticregularity/110curls remain calibrationqueue, no retroactivefixclaim. Adulttoeaddition rejected aftercrop; preserve alreadyfeathereddorsa. Do not replaceolderjuvenileformedwing withgenericnewbornbuds.
[Actual review](../research/reviews/112-asio-abyssinicus-v6-review.md)


## 2026-11-27 0030Z 112-asio-abyssinicus-v7
Actualwholeplate rebuild changed olderjuvenilestagevisibility (formedwing/barredtail) but retained fineclosedcurltexture; hypothesisthatwhole-rebuildsolvesmaterial NOTverified. StatusNEEDS_REVISION retained. Prior109/110plastictexture also reviewed asaffectedcandidates; no scientificapproval. Renders should judge material independently from stage/softness. All sixfeet/text/adultnet checked; #25local/remoteidentical, fd9d70d422notvalidrecovery.


## 2026-11-27 0030Z 109-ptilopsis-leucotis-v11
Adultpatterntargetfinevermiculations successfullyvisible aftersubtleonefifthcontrastprompt, dominantshaftsnotheavygrid. This is oneplatevisualvalidation notquantitativebiologicalratio. Juvenileyellowiris/sixsupports checked; plasticfeathertexture remainsnotfixed. Earlier105finepattern/86overshoot rules reused with species-specific sources, nottransferred blindly.


## 2026-11-27 0030Z 113-ninox-natalis-v8
Adultwhiteplainshanks→guide494rufousochrebarredfeatheredtarsi→adultonlywarmbarredrepaint actualfullviewpassed. Institution2016generalyellowlegs notusedtoerasefeathers; baretoesremainyellow. GuidecaptionKiritimatiwrongregion flagged/excluded, nottaxonomychange. Youngunchanged/noadulttransfer; oneplatepromptapplication notuniversalrule.


## 2026-11-27 0030Z 115-otus-lempiji-v5
Image-onlyscopegap in115v4→primarySingaporecase printed38notuniversalJavajuvenileage/colour→scope+agecaption added andread. Allanatomyunchangedvisually; no newlycalibratedphenotype. Taxon/region/behaviour must be separated, nottransfergenericwhite Malaydown toJavayoung. Applied115only, notnewrulevalidatedacrossspecies.


## 2026-11-27 0030Z 116-margarobyas-lawrencii-v6
116genericjuvenile/cavityscene lackedimage-visiblelimits→oldguideunderGymnoglauxname correctlymappedITIS→olderunknownage/cavitynotactiveproof captionadded andread. Allbarelegfeaturesretained. PrimaryoldURLnowgenericredirectandhugeguide400arenotfreshread; nofalsepaperaccessclaim. No scientificapproval.


## 2026-11-27 0030Z 110-megascops-barbarus-v8
Actual brown-morph juvenile photo access upgraded the existing CAYAYA index entry. Replacing adult-like scales with diffuse mesoptile bars worked visibly in #110 v8, but two targeted attempts to remove fine curly fibers did not demonstrate a sufficient repair. Keep NEEDS_REVISION and science=false; preserve first attempt, both prompts, final original and immutable-byte verification. Do not count textual negative constraints as a validated loop-removal rule. #112 has the related unresolved texture problem; its current v7 was also actually reviewed this invocation, so both are priority candidates. Photo/print guide supports age-unknown mesoptile, not precise age, flight or nest occupancy. No morphology transferred from rufous photo to brown juvenile.


## 2026-11-27 0125Z 112-asio-abyssinicus-v8
Low microcontrast whole-down surface prompt tested in112v8; loops remain, NEEDS_REVISION. Targeted negative/curl prompts and this material rewrite not proven effective; do not reuse as successful rule. Actual Maton reference supports older formed-wing stage, no newborn assumptions. Cross-check110 next as related material defect. Bootstrap parser error occurred before main mutation; fixed by honoring structuredContent.sha.


## 2026-11-27 0125Z 110-megascops-barbarus-v9
Photo-first central rebuild improved110 head/pose/compactformedwing but inherited closedcurls persist; NEEDS_REVISION. Whole-subject reference swap not validated for material. 112 relatedfailed strategy already actuallyreviewed thisrun. Network reference downloads117/118 failed403 while110 archive fullreadback succeeded; connector fetch_blob PNG decoding failsUTF8, don't equate with GitHubconnection failure.


## 2026-11-27 0125Z 117-otus-manadensis-v10
117adulttoe pink→yellowgray corrected and visually checked, not juveniletraittransfer. Guide fresh194/PDF196. Marshall freshPDFopen redirects tohomepage, corrected READY beforeimagegen; newsecondary PoBsource indexed with dependencies/0data warning. Initialraw403 recovered bysameURLretry, not permanentblock.


## 2026-11-27 0125Z 118-megascops-cooperi-v6
118adultfinevermiculations actually added while shafts/openpaleground and supporteddefensivejuvenileremiges retained. Faintbrokenwaveletcontrol reused from109 pattern approach but visually validated hereonly; not universal plumagefrequency. Guide210/actualAvesCRbodyread; site'sAIillustrationexcluded. No flightgeneralization fromhistoricalonecase.


## 2026-11-27 0125Z 119-megascops-centralis-v6
119adulttoe paleyellow repair initiallyspilledonto tarsus; actualsecondedit restored originaltarsalskin while retaining yellowtoes, juvenilefeetunchanged. Both fulloutputs reviewed. Split toe vs tarsal scope should be checked separately; validated scopesrestore onlythisplate, source doesnotvalidate restoredtarsalcolour. AOS currentname freshbodyread; Reyes2017 historicalnotfreshfulltext.


## 2026-11-27 0125Z 120-megascops-ingens-v6
120adultclaws dark→palehorn corrected andactuallyviewed, no juveniletraittransfer. Existingyoungcurlydown remains separatecalibrationqueue similar110/112; current120 and earlier119/108 were actuallyviewed thisrun for potentialaffectedmaterial, do not call wholeplatesciencepassed. Primary2022fulltext download403/RGDisabled, metadataread only plus historicalprimaryreuse, no newnestmaterialclaim. #25 localv6 Gitblob equals currentmaintree10508841 size2864437; oldfd9d70d GitHub422unrecoverable, checkedlate thisrun rather than claiming pre-generationcheck.


## 2026-11-27 0231Z 112-asio-abyssinicus-v9
112 independent photo-only juvenile materialstudy→integration visually reduced repeatedoutlinedloops while keeping formedwing/tail and sourceolderstage. First successful one-plate materialexperiment, not universalscienceapproval. Studies saved beforeintegration, exact fulloutputsviewed. Crosscheck110 next to testtransfer, retainingunknownage/sex/flight and existingadultnet/feet.


## 2026-11-27 0231Z 110-megascops-barbarus-v10
Independentstudy→integration onlyvalidated112, NOT110: final110belly retainsclosedloops despite sourcefaithfulhead/pose/wing. MarkNEEDS_REVISION, avoiduniversalfixclaim. All originals/studies/prompts preserved. Crossaffected108checknext with itsownphoto, not brownmorph oradulttraitsborrowed.


## 2026-11-27 0231Z 108-otus-rutilus-v7
Recovered the actual Vassen Flickr photograph after Commons/thumbnail403 errors and re-viewed it before generation. A bounded edit reduced long bright wool-like locks to shorter denser brown down; fine curls remain uncertain. This supports the narrow long-lock correction only, not a transferable universal down-material rule or scientific approval. Keep #110 failed two-stage transfer and #119/#120 juvenile material in unresolved queue.


## 2026-11-27 0231Z 119-megascops-centralis-v7
Adult brow correction is distinct from juvenile down-material problem. Mikkola p242 explicitly distinguishes faint eyebrows/poorly defined outer disc from blackish orbital rings. Applied and visually verified in #119v7 while preserving previously repaired pale adult toes and pink lower tarsi. Juvenile curly material remains unresolved; do not claim wholeplate scientific pass.


## 2026-11-27 0231Z 120-megascops-ingens-v7
Pink eyelid descriptor alone produced oversaturated broad rings in first #120v7 attempt. Actual re-edit reduced prominence, evidence recorded, both attempts archived (initial undefined blob_sha corrected to git_blob before VERIFIED). Follow-up prompts should distinguish thin anatomical lid edge from decorative facial ring and avoid transferring prominent Colombian-species lids. This correction is locally observed; juvenile curl remains unresolved.


## 2026-11-27 0329Z 121-ninox-leucopsis-v6
Applied/reviewed smallwhiteadultthroat perguidep463. ABSA2019primaryinstitution lists pinkgreyadultfeet, so discarded gray-only correction despite guidepalette. Keep fact/individualvariation separate; patchrendering remainsdesign, youngage/flight unknown. No scienceapproval.


## 2026-11-27 0329Z 122-otus-megalotis-v6
Adulttoe-onlyneutralgreyedit observed; juvenilefeet/wingaction preserved. Hornpinkclawbase precise calibration remainsopen rather than claiming wholefoot scientificpass. Confounded rescue chronology used onlyforsupportedlaterstageaction. Keep sixcontacts and featheredboundary invariant.


## 2026-11-27 0329Z 123-otus-gurneyi-v6
Adultpalehornclawbase descriptor did not translate sufficiently: proximalareaslighter butmostclawstilldark; NEEDS_REVISION afteractualimagegenedit/review. Futurepromptneeds strongerlocalmaterialcontrast, notvalidatedyet. Historicguidep229misattribution correctedto174 viaactualuploadread, preservingoldrecord. No scientificsuccessclaimed.


## 2026-11-27 0329Z 124-ketupa-philippensis-v6
Adultlowerbellypattern taperedwhilebreaststreaksretained; visiblyeffectivein124v6only, notglobalpreventionrule. Firstpersonobservedflightsequence notusedtoassigncompositeexactage/sexorindependence. Adultclawbluecast remainsunknownandyoungirisprovisional; sciencefalse.


## 2026-11-27 0329Z 125-ninox-philippensis-v6
Undertailcoverts must be distinguished from rectrices. Targetedsmallwhitecoverts behindadultlegs retainedbrownbarredlongtail andventralstreaks, visuallyeffective125v6. No genericwhiteventruleforotherNinoxtaxa; paperexplicitlyseparatesspecies. Youngmuseumlocality/age/irisstillunknown.


## 2026-11-27 0329Z 126-strix-hadorami-v5
Oldbroadbutleri guide must be checked against2015split; primarydiagnosis37/description39 preserveswesternhadoramipalerufouscrossbars. Graphicregularitymodestlyreduced, exactwidthnotmeasuredscience. Primarytextread successful/localPDFpageattemptfailed explicitly, no freshphotopixelclaim. Keep126youngcurlmaterial and123clawpalette plus110priorcurl inunresolvedqueue.


## 2026-11-27 0426Z 123-otus-gurneyi-v7
Stronger explicit proximal palehorn/distal dark claw-sheath replacement finally visible in123v7, toe/clawboundaries preserved. Youngdown rerendering changedsurface slightly; avoidclaimingpixelinvariance. Locallyverifiedpalettefixonly, exacthornextentdesignnotratio. Priorweakeditfailurepreserved.


## 2026-11-27 0426Z 110-megascops-barbarus-v11
Directone-stagephotoreference/erasecoilpromptalsofailed110closedloopdown, aftertwostagefailure. Preservefailuresandstopassertingprompt-alonegeneralfix. Needgenuinelydifferentmaterialgenerationstrategy, notanothernearlyidenticalrephrasing. Anatomystage/supportpass doesnotimplymaterialpass.


## 2026-11-27 0426Z 127-megascops-albogularis-v7
Adultpalehornproximalclaw/darktip transferfrom123promptlocallyeffective127v7, notassumedforallspecies. InstitutionalBIOWEBbodyfound/readafterPDFsize/403andITIStimeout, supportsadultidentityonly; savefreshsourcewithoutclaimingnewjuvenilefacts. Comparewhitepairedthroat vswhitewingrow separately. Exactyoungiris/downmaterialstillunknown.


## 2026-11-27 0426Z 128-megascops-marshalli-v10
First128adultclawedit insufficient, secondeditpaleentiresheath succeededaftercheckingguidep234whichdoesNOTrequireblacktips. Do notgeneralize123darktipruleacrossspecies. Primary1981livebareparts listsiris/toes/bill butnotclaws; supportlevelremainsecondaryguideonly. Bothattempts preserved, youngformedwingsandpriorouterflightbarcorrectionretained.


## 2026-11-27 0426Z 129-megascops-hoyi-v6
129adulttoe skintone reducedochre to yellowishgray whiledarkhornclawsretained; no universalpaleclawrule. Youngyellowfeetandiris/billunverifiedlabels preserved. Primary1989fresh403doesnoterasehistoricalevidencebutcannotclaimfreshreading; SIBfreshsupportsnameonly. Checkstagecolourbeforecopyingadultpalette.


## 2026-11-27 0426Z 130-megascops-koepckeae-v7
130adultlegfeatherstargetbuffandbrownfleck locallyvisible, baretoe/clawandyoungwhitebrowstagespreserved. OriginalFjeldsa2012pages184/189downloadrecoveredafterwebfindredirect500, actualread supportsbuffmarkedlegs whilewarningregionalvariation; notautomaticLoja hockingiassignment. Youngclosedloopmaterialstillqueue. Keep legfeathers/toes/claws threeindependenttract/colorchecks.


## 20261127T0532Z 110v12
Actualinput/study/finaloutputfullimagesviewed. Mattepaintvolumeplate substantially suppresses highcontrastlongUclosedloops: paleventralsurface stillhasfinefaintwisps butnowappearsbroadblurredtone ratherthanoutlinedcoils. Tradeoff: youngmaterialover-soft/airbrushed andhead/barringlesscrispthanactualphoto; NOT photoaccuracy/fullscientificpass. Retainyellowiris/green-graybill/narrowbrows/notufts/compactwing/tailhidden/2feetnaturalbranch; adultpinkbaretoes/tufts/marks/yellowirises/greenbills/title/rolelabels/6feet/forestpreserved. PASS_WITH_LIMITATIONS localcoilvisibilityreductiononly, materialfidelitystillneedsrefinement. Exactage/flight/sex/nestunknown. Failedphoto-onlystudyretained. Rule: loweringmaterialdetailcanreducecoilcontrastinthiscase, notuniversalvalidatedfix; do notapplytoothersuntilcompared.


## 20261127T0532Z 132-strix-davidi-v7
Actualfullinput/outputviewed: bothadultclaws nowclearlypaleochre-grayproximally/darkergraytips; meetsprimary2014p62range qualitatively. Denselyfurredtoetopsandallgripsretained, centralyounggrayblackclaws unchanged. Adultdarkbrowniris/yellowbill/radialface, validtailbars/near-equalscale, fourweekgraybarredyoung/pinkishlids/concealedwing-tail/bareboxsill unchanged. Sixsupportedfeet/titlelabels/forestretained. LocalpalettePWL, exactshade/sexsize/individualageandmaterialfidelityunverified. Primaryadultandjuvenileclawparagraphsmustnotbeinterchanged. No newfullscientificpass.


## 20261127T0532Z 133-megascops-atricapilla-v7
Actualfullinput/outputviewed: adultinter-shaftareasnowhavefineirregularworm-likevermiculationswhileboldbranchingshafts/dirtybuffgroundretained. Fineoutlinesaregraphicallystrongerthanideal/naturalphotometricamountunverified; localpatternadditionPWLnotwholeplumageaccuracy. Centerphoto-boundedyoungyelloweyes/lowtufts/mixedbrokenbars/formedwings-tail/shortresidualwisps/feet retained, noadultwormpatterntransferred. Adultsblackcap/browneye/greenbill/scapulars/gray-fleshbaretoes/darkclaws andsixgrips/titlelabels/forest preserved. Exactyoungage/flight/sexratio unknown. Secondaryadultfinepatterncannotvalidateyoungdevelopment; primaryDantas warnsphenotype-aloneidentification.


## 20261127T0532Z 134-megascops-sanctaecatarinae-v7
Actualinput/outputfullviewed: allfouradultfeetnowclearbarering-scaledgray-browntoesfromdigitbase, featheredanklesendatbase; black/darkhornclawsandcurvature/branchcontactretained. No extrafoot/digitlossnoticed. Centralyoungupperbodybehindlip/darkeye/openhornbill/shortgraybrownfeathers andhiddenfeet-wing-tailretained; cannotverifyconcealedanatomy. Adultvariableiris/green-graybill/tufts/bodymarkings/near-equaldisplay/forest/cavity/alllabelsretained. PWL adultfeatherboundaryonly, exactskinshadeuncalibrated, speciesvoice/geographicIDandyoungage/flightunknown. Existingyoungloopwispsstillstylelimit, notcorrectedthiscycle. PaganoPDF403historicalonly. Lesson: distinguish tarsalanklefeathercoveragefromdigits, #132furredtoerulecannottransfer.

## 20261127T0633Z 135-otus-silvicola-v9
Recovery2026-11-27 0633Z: actual135v9fullPNGviewedagain andcomparedv8actualprior. ADULT IRIS RANGE: SOURCE CONFLICT andpendingfooter/v9readable. Physicaleyesnotforciblyorange; 3birds/6supportedfeet/formedtransitionalwing-tail/tuft/toefeathers/forest/ageunknownlabelretained. NewfreshwebMees2006p113 confirms sulphuryellownote; guide183actualreopened darkorangeyellow, disagreementretainednotresolved. Annotationonlynotnewmorphologycalibration. Exactirisrange/individualyoungage/flight/nestunknown. Reusepersistedactualimagegen/prompt33.788s from0532Z, no repeatedgeneration. PriorreportinterruptedbeforeREVIEWED, expiredleasecheckedmainnoadvance0967d44. Newsciencepass0.


## 20261127T0633Z 110-megascops-barbarus-v13
Actualinput/reference/outputfullviewed. Shortfeatheraccentrestorationaddsdetailtopreviousblur butreintroducesrepeatedscalloped/closedUunitsonhead-upperbodyandfaintlowerbelly. ThisdoesNOTmatchactualphotodenseshortirregularbarbtexture; no validatedbalancedmaterialsolution. Lowerbellystilldiffuse/airbrushed. NEEDS_REVISION material; geometry/yellowiris/graygreenbill/narrowbrows/notufts/compactwing/hidden tail/2feet-supportretained. Bothadultmarkings/pinkfeet/yelloweyes/greenbills/3birds6feet/titlelabels/forestpreserved. Age/flight/sexunknown. Preservev12matteandv13faileddetailattempt, comparebeforecallingimprovement. Repeatedsparse-fiberpromptbringsloopbiasback; cannotclaimuniversalfix orapplyunverifiedsuccesstoothers.


## 20261127T0633Z 133-megascops-atricapilla-v8
Actualinput/outputfullviewed. Adultfinevermiculationsnowlighter/moregraybrown, boldblackshaftbranchesretained. Reductionvisibleespeciallyinter-shaftareas, somefinepencillikeoutlinesstillpresent/qualitativeonly, notexactphotometriccalibration. Centralyoungyellowiris/smalltufts/mixedbars/formedwing-tail/feetunchangedoverall; adultsdarkcaps/browneyes/greenbills/graybaretoes/darkclaws/near-equaldisplay retained. Threebirds/sixgrips/titlelabels/forestpreserved. PASS_WITH_LIMITATIONS localcontrastonly, exactmarkgeometry/youngchronology/flight/sexratio unresolved. Do noteraseallfinepattern in future; source says finevermiculated, notplainbelly.


## 20261127T0633Z 134-megascops-sanctaecatarinae-v8
Actualtarget/reference/outputfullviewed: centralfeatherfieldsremainrepeatedshortcurved/closedU-wisps, stillmoregoldenandoutlinedthanactualphoto'sdensegrayirregularsurface. No convincingmaterialcorrection; NEEDS_REVISION. Somecontoursshorterbutnotprimaryreferencefidelitypass. Preserveactualphotoaccessandfailedattemptwithoutclaimingfix. Darkeye/openmutedgreenbill/roundedhead/upperbodybehindlip/noinventedhiddenfeetwingtail andadultnewbaregraytoes/darkclaws/variableiris/alllabels/forestcavityretained. Exactage/flightunknown, genericcavitynotphotocopiedimprovisednest. Sourcephotoheadandupperbodyonly, nofaithfulfullbodyclaim. Lesson: lowcontrastwordsalonefailedthiscase; nofurthernearlyidenticalpromptloopwithoutnewmaterialstrategy.


## 20261127T0633Z 119-megascops-centralis-v8
Actualinput/outputfullviewed: younglongoutlinedcurlcontours reducedsubstantially; gray-buffbarredmesoptile nowsofter/sparserwhisps, formedsideflightfeatherpanelsretainednotcoveredbynewdown. Materialstillstylizedsoftandunmeasured, notprimaryphotoreplica. PWL localcurlcontrastonly. Youngyellowiris/greenhornbill/no projectingtail/currentheadpose/twopinkfeetonsill retained. Adults faintbrows/orbitalrings/lemoniris/greenbill/pinklowerTARSIvsverypaleyellowTOES/hornclaws/near-equaldisplayunchanged. Exact3birds6supportedfeet/titlelabels/cavity/rainforest retained. Hatchage/flight/parasitegrowthgeneralizationunknown; DOInewaccessfailed/historicalprimaryonly. Loweringdownfibercontrastpreservedformedremigeboundaryinthisplateonly, notalljuvenilesrule.


## 20261127T0633Z 130-megascops-koepckeae-v8
Actualinput/outputfullplusfreshprimaryprinted95Fig1cpixelsviewed. Largestwhitewoolringletsreducedandbrown/grayfeathermassesmorecoherent, but repeatedcurvedfiberunitsstillpresentandmuchfluffier/outlinedthanprimaryphoto'scompactgraybarredsurface. NEEDS_REVISION materialfidelity, no fullscientificpass. JuvenileWHITEbrows/yellowiris/bluegraybill/brownchest/graywhitebars/formedcompactwing/twosupportedfeet/unknownagelabelretained; adultbuffyellowbrownflecktarsalFEATHERS/graybrownbareTOES/darkhornCLAWS/subduedbrows/blackruff/near-equaldisplay andtitleforestlabelsretained. Threebirds6feet/supports no newprey/nest/subspecies. FreshoriginalAlarcon2023actualbodyp104/PDF13 andFig1cp95/PDF4 confirmed afterpublisher403/webPDF400 recoveredlocalinstitutionPDF. Exactyoungage/flightandLoja subspeciesunknown. ExistingKOEP-ALARCON-2023 locator/pixelaccessupgrade1 notnewsource. Shorterfiberwordingnotvalidatedgeneralfix; retainthisboundedfailurefornextmaterialstrategy.


## 20261127T0730Z 138-otus-mentawi-v7
Actualinput/outputfullviewed: bothadultbreast/flankpaleocellispotsmorevisibleandlooselypairedwithherringboneunits; groundremainschestnutnotwhitened. Noexactringgeometry/numbervalidation, somepatchesstilllinear; PWL qualitativebook-supportedmarkingonly. Youngpalergreybrownthinstreaks/redbrownfaceeyes/grayhornbilltoes/formedwingfaintnarrowbars/wingpastshorttail/currentgrips retained. Adultbrowniris/yellowhornbill/shorttufts/scapularrow/fleshtoes/darkhornclaws/near-equaldisplay/3birds6feet/titlelabels/forestunchangedoverall. Noage/flight/sexsizeformula. Sourcefaintwingbarcueappliesyoungremigesnotallcoverts; adultocellinevertransferredtoyoung. No sciencepass.


## 20261127T0730Z 139-otus-jolandae-v8
Actual full PNG viewed 2026-11-27 after recovering generated file: initial imagegen display output was truncated by available context, generation itself completed in 38.31s. v8 adult feathered lower legs now show fine gray-brown crossbars/flecks over cream-buff ground; not a measured rendering of specimen colour intensity. Bare ochre toes/dark claws, supported grips, 3 birds, older immature female/formed wings/age-unknown label, adult sizes and forest retained. Primary Sangster2013 Underparts/Variation supports indistinct wavy adult tarsal markings; adult rule not transferred to immature. Local visual improvement only; sex-size ratio, juvenile exact age/iris chronology, nest and flight remain unverified. PASS_WITH_LIMITATIONS; scientifically_verified=false. Problem→evidence→edit→recheck: plain adult tarsi lacked described indistinct marks; adult-only edit applied; actual view shows marks. No global Otus rule inferred.


## 20261127T0730Z 140-otus-rufescens-v8
Actual full generated v8 viewed: narrow muted reddish-brown/pinkish lower eyelid edges on outer adults, rather than bright rings; improvement is subtle, quantitative hue not calibrated. Chestnut/amber irises/black pupils, horn-white bills, plain ochre sparse-dot bellies, near-toe pale feather boundaries, yellowish toes and supported feet retained. Central rich-rufescent mesoptile unchanged, no adult rim rule transferred; its exact age/iris/flight remain unknown. Titlev8/pending footer visible,3birds6feet and forestbranch preserved. Guide178 supportsadult rim only; Sangster2013 supports preserving corrected plain belly; original Warakagoda2004p102 was actually read later this cycle and supports mesoptile colours but not flight. Problem→evidence→edit→recheck: dark adult rim targeted, muted reddish rim visible at normal full view, all other characters retained qualitatively; no whole-species sciencepass. PASS_WITH_LIMITATIONS/scientifically_verified=false.


## 20261127T0730Z 142-asio-grammicus-v6
Full generated v6 actually viewed. Adult four feathered leg cuffs reddish-brown, greyish-brown bare toes and darker claws/grips retained; no new naked shanks. Young coolgreyback/cinnamonbuffbreast/down/feet unaltered qualitatively. Adult hazel eyes/bluegraybills/tufts/near equalbody size/no white shoulder spots maintained.3birds6supportedfeet, version and pendingfooter legible. Local colour correction supported by Mikkola printed500 (PDF502) identification text freshly read; sourceID covers500–501 but no claim freshly viewing501 photograph. Bouglouan104 agrees, secondary synthesis not independent growthresearch. Problem→evidence→edit→recheck: ivory adultleg feathers→speciesreddishbrown→adult-only recolour visibly applied. Exactcolourcalibration/juvenileageirisflight/sexratiostillunknown; scientifically_verified=false.


## 20261127T0730Z 143-asio-solomonensis-v6
Actual full v6 viewed: young distal hooked bill now black/darkcharcoal while nasal/cere basal patch remains bluegrey; boundaries clearly separated, minimal specular highlight. Orange-yellow eyes/darkmask/unbarredheadventraldown/emergingbarredwing retained, walkingyoungtwofeetcontactearth/root, adults unchanged qualitatively;3birds6feet/titlev6/pendingfooter visible. Actual primary LoynDebus2000p288 supports this individual age-unknown barepart combination; no matureflight/nestmaterial inference. Problem→evidence→edit→recheck: blue-grey spread overbill→primarydistinguishesblackbillfromcere→distalonlydarkening→visible distinction. Whole-sciencefalse; downcolour/precisefeatherlength/age/sexratio unresolved. Previousguide'juvenileundescribed' recorded as omission relative to2000paper, not supportforinventedyoung.


## Resume20261127T0830Z
Actual edited full PNG viewed2026-11-27: outeradult cheek filaments substantiallyshorter/softer, no long straight wires; featherlikeirregularfrayedendsremain. Exactlivefilamentlengthnotcalibrated; localdesignimprovementonly. Adultyelloweyes/oliveyellowbill/plaincrown/whitewingpatches/streakedbelly/yellowfeet/darkclaws/earlessoutline retainedqualitatively. Centerolderyoungdarkbrowniris/compactformedwing/shorttail/ageunknownlabel retained; smallrenderingdrift in featherdetails noted, notpixel-identical. Threebirdssixfeetnaturalbranchsupport, noflight/nestclaim; titlev5/pendingfooter readable. Sourceprimaryprinted12/PDF13actualreread anduploadedguide473/PDF475agreeauricularfilamenttrait; no transferadulttraittoyoung. Researchnew0/reused3IDs; exactage/juvenilemodernsplitlocality/iris chronology/sexquantitativeratio remainunknown. Problem→evidence→edit→recheck: promptlongfilamentproducedmammalianwires, reducedlengthandregularity, actualfullviewshowswireeffectremoved. Lesson actualappliedvisuallyeffectivehere, notvalidatedallNinox; #144candidate notchanged withoutfullcurrentreview. PASS_WITH_LIMITATIONS/scientifically_verified=false.
Complete actual edit prompt:
Use case precise-object-edit. Edit this recovered #145 Ninox philippensis v5 plate. ONLY correct the two ADULTS' exaggerated straight wire-like cheek whiskers: replace long naked strands extending far sideways with SHORTER, soft irregular tapering filamentous EAR-COVERT FEATHER tips lying mostly along the dark cheek plumage, a few delicate ends projecting slightly beyond cheek silhouette. They must look like feather extensions, gently curved/frayed, not mammalian vibrissae, fishing line, horns or ear tufts. Do not remove all auricular feather texture. Preserve rounded earless adult heads, yellow eyes, buffwhite brows, oliveyellow bills, plainbrown back/limitedwhitewingmarks/streakedventrum/yellowfeet/blackclaws, exactbodyproportions and allfootgrips. Central age-unknown YOUNG entirely unchanged, no adult trait transfer. Exact3 birds6supportedfeet, continuous mossy branch/Luzonforest/titlev5/labels/not-to-scale/sciencependingfooter unchanged. No new age/flight/nest/sex-ratio claim.


146-ninox-mindorensis-v5
Full generated v5 actually viewed: centerlabel explicitly JUVENILERECONSTRUCTION/AGEPLUMAGEUNVERIFIED; pendingfooterlegible. Threebirds/sixsupportedfeet, adultsfinebarring/eyes/bills/claws and unknownyoungclosedeyes/concealedwing-tail retainedqualitatively. No newscientificphenotype claim. Problem→evidence→change→recheck: AGEUNKNOWNnotadequateforunsupportedplumage; speciesprimarynojuvenilediagnosis+guideundescribed; explicitunverifiedlabelapplied; visuallyeffectiveevidencecommunicationonly. Stillunknownyoungage/iris/feathersequence/locomotion/nest/sexratio; notscientificallypassed. Ruleappliedonlythisplate; neighboring147alreadyhasunverifiedlabel, don'tduplicateeditthere. Sourceoriginalreadandpriorindexbibliographyreused; new0.

147-ninox-leventisi-v6
Actualfullv6viewed: adultscaledyellowtarsi nowwithsparsefinepalebristleedges, scalesshowthrough; notdenseboots. Mostlypaleclawsdarktips/yellowtoecontacts/paleadultirises/barredbody/whitethroatretained. Centerunknownyoungunchangedqualitatively and explicitPLUMAGEUNVERIFIEDlabelretained; 3birds6supportedfeet. Exactbristledensity/lengthnotmeasured, localtexturedesignrefinementonly. Primaryprinted15/PDF16supportsmostlythinbristles; no transfertojuvenile; juvenileage/iris/flight/nestunknown. Problem→smoothshanks→primarybristlecovered→sparseadult-onlyedit→finebristlesvisible; promptappliedeffectiveinthisplateonly. No new sciencepass.

148-ninox-rumseyi-v6
Actualfullv6view: adultsupperchestlongshaftsreplacedwithsmallweakshortdarkflecks/brokenbarfragments, lowerabdomenlargelyplainwarmfulvous. Whitethroat/eye/bill/crownwingpatterns/yellowlegs/mostlyblackclawsunchangedqualitatively; centerunverifiedyoung/shortdown-obscuredwing/step/uncertaintylabels preserved;3birds6contacts. Somefragmentrowsstillregular, exactpatternfrequencyunmeasured; PASS_WITH_LIMITATIONS notsciencepass. PrimaryCebudiagnosis supportsweakspeckles/shortbrokenbars, notLuzonlongshafts. Ruleappliedlocalonly; no newjuveniledevelopmentvalidation. Unknownyoungage/iris/flight/nestandsexratio. Source reusedpublicationnotnewresearchpaper.

149-ninox-odiosa-v7
Fullv7actuallyviewed: adultbaretoesnowochreyellowishbrown, clawsduskyhorn/darktipsunchangedqualitatively, featheredtarsiboundary/grips preserved. Younggrayishbaretoesunchanged/unverified, noadulttransfer. Diagnosticbrownband/whitethroat/palestreakedbelly/eyes/bill/sizecomposition/titlev7/alllabels/3birds6feet preserved. Colourqualitativeguide487only; no photometriccalibration. BirdForum403notnewread; Frenchleadbodynotyetfullyreviewed, notindependentscientificevidence. Source new0/bookreuse1, juvenilephenotypeunknown. Problem→grayadulttoes→guideyellowbrown→adultonlyrecolour→visiblewarmtone; no universalfeetcolourrule. PASS_WITH_LIMITATIONS/sciencefalse.

150-ninox-variegata-v7
Actualfullv7viewed: fewfinepaleadulttoebristlesvisibleespeciallylefttoeoutline, yellow-scaledskin remainsopen; changeverysubtle/rightfootpartlyobscured, notassertquantifiedbristledensityorcompleteanatomicalcalibration. Duskyhornclaws/legfeatherboundary/yelloweyes/hornbill/plainadultcrown/barredwing/scalyventrum preservedqualitatively. Centerunverifiedyoungunchanged anduncertaintyfooterretained,3birds6supportedfeet/titlev7legible. Guide497supportsadultbristledtoes, photometadatadoesnotsupportprecisebristlesorjuvenile. Problem→smoothadulttoeappearance→speciesbristledtoes→sparseadultonlyaddition→smallvisualchange; ruleappliedbutonlylimitedvisualeffectverified. PASS_WITH_LIMITATIONS/sciencefalse. Exactyoungage/iris/flight/nest/sexratio remainunknown. No crossspeciestransferfromwronginitialManuspage.

## 151-athene-jacquinoti-v6
Actualfullv6viewed: formerdarkholeinupperrighttrunkreplacedsolidbark/lichen, noreplacednest/eggs/cavity. Entirebirds/oliveadultbills/yellowishfeet/darkclaws/eye/plumage/support/juvenileunverifiedlabelsretainedqualitatively; exact3birds6footcontacts. Environmentaldesignrevisiononly, notnewnestknowledgeorbiologicalerrorclaim. Problem→unverifiednestlikecue→sourceshabitat/museumprovenancenotnest→neutralbarkbackground→actualviewconfirmsremoved. Juvenileage/plumage/iris/flight/sexmetricunknown, sciencefalse. No repeatoldbillfix. Ruleappliedvisuallyeffectiveforcompositiononly, notglobalecologicalvalidation.

## 152-uroglaux-dimorpha-v6
ActualinitialandsecondfullPNGsviewed: initialdenseblackcomb rejected/preserved, secondadultbristlefansfewer/lesssolidbutremainingleftshaftsarepartlyparallel. Localimprovementlimited, exactdensity/lengthunknown, notphotorealcalibrated. Greyblueadultbills/darktips/yelloweyesfeet/longtails/bodybars/3birds6branchcontacts preservedqualitatively. Evidence-supportedwhiteyoungface/ventrum/frostygreyupperparts/yellowiridesfeetunchanged, noage/flightclaim. Problem→missingblackrictalcontrast→guide498caption→initialoverdense→targetedthinning→visiblepartialimprovement. SourceShanyPDFunavailablecurrenttool/landingabstractonlyfresh, historicalscanreadretainednotinvented; bookactualread. No universalblackbristlesforotherowls. PASS_WITH_LIMITATIONS/sciencefalse, residualstylizationqueued.

## 153-jubula-lettii-v6
Actualfullv6view: subtle greyupperproximaladulttoe/anklepatchesnowvisible, mostbaretoesyellow; exacttoeversuscuffboundarypartlyobscured, no claimallpatchgeometrycalibrated. Hornclawsdarktips/grips unchangedqualitatively; centerimmatureyellowfeet/reducedmane/whiteface/formedwingstail preserved.3birds6feet/titlev6/footerreadable. Adultgreyuppersidepatchesfromguide357only, nottransferredyoung. MLcurrentbotwallrecorded, nofreshphoto/narrativeclaim. Problem→plainyellowadultdigits→speciespatches→smalllocalizedshade→limitedvisualeffectseen. PASS_WITH_LIMITATIONS/sciencefalse; age/sexratio/flightthreshold/nestunknown. No repeatedmaneedit.

## 155-scotopelia-ussheri-v6
Actualfullv6view: fouradultfeetvisibleclawcurvesnowmostlylightbeige-horn, softgreyshadingat tipsnotuniformblackhooks; yelloworangetoe skinunchanged, youngclawsremainuntoucheddark. Adultbluegreybill/yellowcere/darkeyes/plainrufousmantle/wingbars/6footcontacts andolderyoungformedbarredwing/stubbierpose retainedqualitatively. Conditional4–5monthlabelandunknownhatchdisclaimerretained. Paletteguide307only, original2015barepartsdoesnotstateclawcolour, limitationexplicit; notindependentprimaryvalidation. Problem→darkadultclaws→guidepalehorn→adultonlylightening→actualviewconfirmsmajoritycurvepale. No genericallfishowllightclawrule; nextspeciesmustownsource. Sciencefalse/exactage/sexheight/nestunknown. New0/reuse3.

## 157-scotopelia-bouvieri-v6
# 157 Scotopelia bouvieri v6 actual review
Actually viewed v5 full and built-in edited full1536x1024. Both adult exposed bills now read pale warm horn over their greater surface, with shaded lower edges, instead of former largely slate-grey; central immature unchanged. Improvement verified visually, not calibrated spectral colour measurement. Scapulars retained because historical fulvous vs book white descriptions conflict and no new fresh comparative photo establishes a correction. Dark eyes, bare yellow legs/blackish claws, plain off-white thighs, heavily streaked ventra, formed central wings/tail retained. Exactly3 owls and6 supported feet on branches, stable anatomy; labels/pendingfooter retained. Near-equal adult sizes are a conservative design choice, sex ratio unknown. Juvenile precise age/flight/nest and iris development remain unknown. PASS_WITH_LIMITATIONS; scientifically_verified false/user unconfirmed.
Iteration problem—evidence—change—recheck: yellow cere alone had obscured slate distal bill; Mikkola printed308 and cautiously read historical specimen support warm horn/yellow; target actual bill beyond cere; observed lighter horn now. Rule actually applied to157;155 intentionally remains bluegrey as independently supported, no genus-wide palette transfer. No extra species count.

## 158-phodilus-badius-v6
# 158 Phodilus badius v6 actual review
Fresh v5 full and edited full1536x1024 actually viewed. Both outer adults now have dark brown-horn hooked claws over most of their visible curves, with small reflected highlights; toe skin remains pale yellowish-brown and tarsi feathered. Centre older juvenile claws unchanged lighter, not an adult-trait transfer. Exactly3 owls/6 supported feet; juvenile seated body supported at cavityrim, formed short folded wing and residual loose down retained. Original vivid salmon/russet/buff developmental boundary, pale bills/dark eyes, near-equal adult sizes, forest/cavity composition/title/labels/pending footer retained. No extra edit needed for this narrow target. PASS_WITH_LIMITATIONS; scientifically_verified false, userunconfirmed. Adult facial-lid detail/precise iris chronology, juvenile exactage/flight/sex/Nias nest unknown. Primary Finsch1905 does not describe claw colour; book-only calibration for the claw decision, not independent scientific confirmation.
Iteration: pale claws were not equivalent to lighter toe skin. Adults-only mask instruction produced visually darker horn while leaving skin and young unaffected, verified here. Do not globalize:155 paleadultclaws/157blackishadultclaws have separate species evidence. Previously corrected Chasen misattribution remains withdrawn, older juvenile stage not redrawn to invented early down.

## 152v7 rictal comb repeat check
#152v7 actual review2026-11-27
Actualv6full andv7generatedfull viewed. Leftadult parallel comb-like strokes now lessconspicuous; rictalblackshafts also reduced so exactblacktraitvisibility/photographiccalibration still limited. Rightadult fineblackstreaks lessuniform; no claim exactshaftcount. Threebirds/sixsupportedfeet/titlev7/greybluebillsyelloweyesfeetblackclawslongadulttails/centerwhitefaceventrumgreyupperparts/forest preserved. Centerstage follows actualfreshreadShanyp74singleolderdownyfledgling, nothatchday/firstflight. Noeditneededforthe narrowly reduced comb rhythm, remainingdensity/contrast queued. PASS_WITH_LIMITATIONS/sciencefalse/userunconfirmed.
Problem→priorv6explicitparallelism→guide498trait/photo+newlyreachableprimaryyoungscan→targetirregular isolated fineadultshafts→actualrechecklessrhythm butreducedblackcontrast. Ruleapplied andpartialresult verified only152; no genuswidewhiskerrule. Uploadedguide andprimaryeachreused1; accessupgrades2, new0. Unknownage/sexratio/irisprogression/nest retained.

## 110-megascops-barbarus-v14
#110v14 actualreview NEEDS_REVISION/sciencefalse
Actualv13/reference/initialv14/secondv14full allviewed. Newphotographicmicrograinprioritythenstipplepatchworkedits BOTH stillproduceoutlinedclosedU/Vloops. Secondlowerbellyparticularlyclearcoils; nomaterialsuccess, notclaimbalancedshortavianfeathercalibration. Actual3birds6feet/youngyelloweyesgreengreybill/narrowbrownotufts/wingtailconcealed/branchsupportandadultpatterns maintained. Addedv14/pendingfooterlegible. Noage/flight/sex/nestclaim. Initialattemptpersisted separately, finalfailedmaterial preservedforreview, oldv13retained.
Problem→repeatededgepromptbias→freshguide214 andactualbrownjuvenilephoto→change semantic materialmethod/photopriority then tonalpatchwork→bothfailed. NewruleproposedbutNOT validated: erasingtexture mayneed a differentgenerationstrategy; do not apply asprovensolution to130/134. Those taxa require ownphoto/stageevidence, notuniversalshortwings. Twoactualimagegen calls, initial43.7s/second38.7s; statusNEEDS_REVISION, archivereadbackisnotart/sciencepass.

## 130-megascops-koepckeae-v9
#130v9 review NEEDS_REVISION/sciencefalse
Actuallyviewedv8/fullprimaryFig1c/initialv9/editedv9full. Entirejuvenile reconstructionproducedcompactgrayratherthanbrownwoolcoat andmorecoherentfinecrossbars/whitebrows/yellowiris/blackfaceedge, closeroriginal2019Loja case. Initialv9introducedbrightwhiteadultlikefoldedwingspots notestablishedinphoto; secondtargetededitremovedbrightspots andblendedcompactformedwingintograybody, actualrecheckconfirmsreduction. Keptformedwing appropriate documentedfledgling, didnotimposehatchlingwingbud.
ResidualoutlinedclosedU/scallopedunitsstillvisiblehead/belly, exactfeatherfidelityunresolved. ThereforeNEEDS_REVISION, partialshape/colour/wingcontrastimprovementonly; nofullmaterial/sciencepass. Bothadultstarsi/toes/claws/near-equaldisplay/3birds6supports/titlev9/footer retained; centralage/sex/flight/subspeciesunknown, nofrog/nestcopied. Sourceprinted104text/95Fig1c, adjacentgnateatermaterialnotowlnest. Newstrategyactualwholejuvenilerebuildimprovedcasepalette/compactness, notvalidatedgeneraltexturefix; backcheck134againstitsownphoto, don'ttransferLojaoutfit.

## 134-megascops-sanctaecatarinae-v9
#134v9 actualreview NEEDS_REVISION/sciencefalse
Actualv8/realWAphoto/initialv9/secondv9fullviewed. Wholevisibleyoungrebuildshiftedcoatgrayer andintroducedtoowhiteforeheadflecks. Secondeditedthese conspicuousflecksaway, actualrecheckconfirmsmoreevencrown, butmajorrepeatedclosedU/curvedwispsremainonheadandchest. Notconvincingmaterialfidelity, NEEDS_REVISION. Noentiregrayjuvenilephenotypepass, colourimprovementonlyrelativev8gold.
Bothadultindividualiriscolours/tarsalfeather-toebase/baregraybrowntoes/darkclaws/supports retained; centraldarkeye/openmutedgreenhornbill/upperbodyhiddenlip/wingtailfeetnotinvented. Titlev9andpendingfooterlegible. Referenceonlyupperbody; cavitygenericnotreconstructimprovisednest. Age/flight/juvenileirisdevelopmentunknown. Photorebuildstrategyfailedmaterialdespiteonefollowup; do notcall130partialpaletteimprovementgeneraltextureproof. Paganooriginalabstract/taxonomynowread supportsvoiceimportance/irisnotdiagnostic, notexactyoungage.
Twoactualimagegen calls ~38.6/38.7s, initialarchivedseparately; preserveoldv8andalluserconfirmation. New0/reuse4IDs, primarybodyaccessupgrade1. Actualscopeincludesunresolvedmaterial, so archiveverificationnotart/sciencepass.

## 165-ninox-punctulata-v7
#165v7 actualreview PASS_WITH_LIMITATIONS/sciencefalse
Actualv6/newv7fullviewed: bothadultbaretoe shaftswarmedfrompinkishcreamgray tosubduedyellowgray/ochregray, scales/darkhornclaws/featheredlegboundary/gripsretained. Notbrightyellow. Juveniletoes/eyes/bill/darkfluff/wing/currentposeunchanged, noclaimyoungbarepartssequence. Sixfootcontacts/3birds/forestroot/exactlabelsandpendingfooter intact, v7visible. Adulttoe decisionbook485only, noindependentprimaryadultcolourvalidation. Unknownsexratio/youngage/flight/nest/iris-billchronologyretained.
Youngsurfacelongcurltexturevisuallypresent, notsolvedbyadulttoeedit; queuephoto-basedmaterialreview withsourceFig3A beforeclaimingexactscientificproblem. Thisrunonlyverifiednarrowadultpalettechange, notoverallscientificfidelity. Ruleappliedadultskinmaskseparatefromfeatheredshank, visuallylimitedsuccess; nostepsshorteningformedyoungwings. PrimaryO'Connell2022p291actualmirrorbodyread notgenericNinoxyoungassumption.

## 166-bubo-cinerascens-v7
#166v7 actualreview PASS_WITH_LIMITATIONS/sciencefalse
Actuallyviewedv6/fullv7 andguide282page. Adultmid/lowerbreast-abdomen coarsetransverseherringbonebars replacedwithfinerdenserbroken darkbrownvermiculations, visuallylessladderlike. Patternstillstylized/precisegeometryunmeasured, notphotographiccolourcalibration. Adulthead/darkeyes/reddisheyerims/paletippedleadgreybill/wingstail/sizes/feet/grips unchangedqualitatively. Rightolderyoungnotedited, retainsformedfoldedwings/grayingplumage/root-supportedstance/estimated35–43days+unknownindividualage/firstflightnotestablished. Threebirds6feet/forest-savanna/labels/titlev7/footer preserved. Noextraeditneededforthisnarrowadultpatternscalechange.
Iteration: coarseventralbars→guidefinevermiculations→adultonlyfinerbrokenlinework→actualviewconfirmsqualitativechange. Do notuseTobiasp78followingB.lacteusunderpartsparagraphasGreyishfact; actualcontextreadingpreventedcross-taxonmisattribution. SameexistingpaperIDreused/expanded166mapping, correctedbibliographypages73–80, originaloldrecordretained. Barlow2022Table2/Fig6supportsolderrootstage/estimatedage, notfirstflightdate. New0/reuse3IDs, correction1, sciencefalse.

## 165-ninox-punctulata-v8
#165v8 actual review PASS_WITH_LIMITATIONS/scientifically_verified=false. Actual v7, original primary Fig3A and generated full1536x1024 viewed. Juvenile head/face now compact dark matte, long conspicuous looping highlights reduced; belly still carries some wispy curved filaments, not exact photograph texture match, queued residual material fidelity. Dark mask and tiny pale cheek traces follow primary photo direction, pupil/iris chronology unverified. Adults retain brown-white speckles/narrow breastband/dark irides/greenyellow bills/yellowgray adult toe skin/darkhornclaws/near-equal display; center two feet/root support, three owls/six contacts, background/labels/pendingfooter remain. Root is generic support not observed nest; photo handling pose not copied. No early-age/flight claim, no adult wing pattern added. Problem→actual primary pixels expose longhair mismatch→texture-only edit using same-species photo→partial compaction/darkening observed; residual belly wisps mean no full material or scientific pass. Apply only this species stage, compare 110/130/134 own reference rather than infer universal cure. Source new0/reuse2, existing primary Fig3A pixel access upgraded1; generationwait recorded. No extra edit necessary for narrow partial improvement; preserve residual as next-priority.

## 110-megascops-barbarus-v15
#110v15 actual review NEEDS_REVISION/sciencefalse. Actual oldv14/photo/initialv15/followupv15 full all viewed. Both texture-only and entire surface repaint prompts failed to erase closedU/V scallops, especially pale lowerbelly and crown. No demonstrated material improvement; v15 is an archived failed iteration, not scientific pass or new species. Adultspecies/eyes/bill/pinktoes/palehornclaws/near-equaldisplay, centralyelloweyes/greengraybill/narrowbrows/no tufts/concealedwingtail,3birds6grips/forest/title/footer retained qualitatively. Preciseage/flight/sex/nest stillunknown. Initialattempt separatelypersisted. Problem→samebrightedgebias→fresh same-speciesphoto+guide214→matte/stochasticgrain then complete surface repaint→failure verified. This strategy not validated; don't propagate as fix to130/134. Those require their own evidence. #165 partialheadcompaction didnot generalize. Twoactualimagegencalls/initial and edit prompts/waits persisted; archive validation means recoverability only.

## 130-megascops-koepckeae-v10
#130v10 actual review NEEDS_REVISION/sciencefalse. Actual v9/ownprimaryFig1c/initialv10/followupfull viewed. Two edits still retain repeated outlined curved/closedU featherunits on chest/belly, crown; no full texture cure. Followup subtle lowercontrast only, not scientific improvement. Supported graywhitefinebarreddirection/whitebrows/yelloweyes/blackdiscedge/bluegraybill/compactformedwing with reducedwhitecontrast retained, no frog/nest copied. Adults tarsalFEATHERSbuffyellowflecked/baregraybrowntoes/darkhornclaws/near-equaldisplay retained;3birds6footcontacts/branch/environment/titlev10/pendingfooter correct. Exactage/flight/subspecies/sex unknown. Initialattemptarchived. Problem→v9closedunitcoat→primaryshortfeatherphoto+text/guide222→diffusebar/grain then photographicshortfeatherrepaint→stillmaterialfailure, no universalfix claim. Photoreference alone didnot override image's existing edge bias; further strategy needs ownstageactualphoto and freshreview. Archive verification not visualpass.

## 134-megascops-sanctaecatarinae-v10
#134v10 actual review NEEDS_REVISION/sciencefalse. Actual v9/ownWAphoto/initialv10/followupfull viewed. Narrow pale orbitalfeatheraccent remains weak after specificfollowup, not demonstrably matched tophoto; long curved/scallopedunits still dominate crown/upperbody. No claim material or orbitalrim fixed. Dark juvenileeye/openmutedgreenhornbill/roundedhead/hiddenfeetwingtail/cavityrim/bodyextent retained. Two adults individualiriscolours/near-equaldisplay/featheredtarsitoebase/baregraybrowntoes/darkclaws/fourvisiblebranchgrips/environment/labels/v10/footer preserved. Onlyvisibleupperbody reference; age/flight/developmentunknown and improvisednest not copied. Initialattemptpersisted. Problem→actualgrayfinegrain/softpaleorbitreference versuscurlytarget→texture+rimedit then rim-only→insufficientchangeverified. More words didnot overcome existingrenderedges; this method not validated and cannottransferasfix. New0/reuse4IDs. Scientificfalse, archive recoverability only; nextcycle choose other source-backeddefect rather than third near-identicalattempt.

## 167-ketupa-poensis-v7
#167v7 actualreview PASS_WITH_LIMITATIONS/sciencefalse. Actualv6full andeditedfull viewed. Bothadultbaretoes nowcoolbluegray ratherthanwarmfleshygray, skin scales/shapes/grips/darkhornclaws and featheredtarsitoebase preserved. Rightyoung unchangedlightertoes/formedbarredwings/tail/weak tufts/blackbrow/darkeyes/slatebill/age-unknownlabel retained; no adultpalette transfer. Adultdarkeyes/paleblueedgelids/slatebills/rufousfeathers/whitescapulars/near-equaldisplay/3birds6branchcontacts/background/footer/v7title preserved. Noextraeditneededfornarrowtoe target. Exacttoe spectralcolour/sexheight/youngsoftpartchronology/flight/nestunknown, guide-onlycolourdecision notindependentprimaryvalidation. Problem→warmtoe bias→guide284bluegray→adultskin-onlycoolgrayedit→qualitativechangeactuallyviewed. Appliedandvisuallyeffectivehere, no automaticbluegrayfor168whoseadulttoesyellow. #165youngtexturepartialdidnotfix110/130/134; unresolved failuresretained inqueue. New0/reuse2ID. Archivereadbacknot scientificpass.

## 168-ketupa-leucosticta-v7
#168v7 actualreview PASS_WITH_LIMITATIONS/sciencefalse. Actualv6/editedfull1536x1024viewed. Bothadultlowestcentralwhiteabdomen nowlessconnectedbars/moresmallseparatedduskyflecks, retainssomebarsandregionalvariation, visuallymeets narrow documentedphenotypedirection. Upperbreast/flankstrongpattern/wingtailbars/headwhitebrow/tufttips/greenyelloweyesbills/barredtarsifeathers/paleyellowtoesblackclaws/near-equaldisplay unchangedqualitatively. ENTIRE rightyoungnearwhite/rufousbars/graybill/darkeyes/lowstep/formedwingboundary andtwofeet on connectedbranches retained; noadultsoftparttransfer. 3birds6footcontacts/forest/nonnest/labels/v7/footer intact. Noextraeditneededfornarrowadultzone. Exactpatternmap/scientificcalibrationpending, adultventraldecisionguide278only, Tobiascomparisonnotventralcorroboration. Age/iris/bill/wing/flightchronologyunknown; Perseeoriginalbodyfailed remains historicalonly, nofresh50dayclaim. Youngcurlmaterial remainspending ownphoto comparison, notsolvedbyadultedit. Problem→coarseconnectedlowbellybars→booksmallspotwhiteabdomen→adultlowestzoneflecks→qualitativechangeverified. Localruleappliedandviewed, notallAkunbarsinvalid andnotuniversalunmarkedowlbelly. #167toe bluegray contrast retainedonly167, hereyellowappropriate. New0/reuse2freshworks+1blockedhistoricalID.

## 169-ketupa-shelleyi-v7
#169v7 actualreview PASS_WITH_LIMITATIONS/sciencefalse. Actuallyviewedv6/initialv7/followupfull. Adultclawsproximalcurves nowlightgrayhorn withdarkhooktips, comparedv6allslate. Initialclawedit erased/diminishedadultposteriorcrownwhitepatch, detectedinwholeimagecomparison; followuprestoredsmallwhitepatchbehind/betweentuftbasesonbothadults, notscapular/foreheadV. Narrowclawfixretained. Youngwholemesoptile/darkbluegrayiris/guideonlynote/uncalibratedbill/formedwingtail/crouch retained,3birds6footcontacts/forestbranch/labels/v7/pendingfooter preserved. Exactgrayreflectance/clawlength/age/youngsoftparts/flight/sexratio/nestunknown. Adultclawdecisionguide288onlypluspriorhistoricalBouet record, nofreshindependentlivingphotocalibration. Problem→whole-darkclaws→lightbase/darktipedit→crownregression→targetedrestore→bothfixandpatchvisuallyverified. Thiscasevalidatesregressiongate, notgeneralmodelimprovement. Adultclawpalettecannottransfer170withoutownsource. Twoactualimagegencalls/initialarchived; new0/sourcefresh2+historical1.

## 170-glaucidium-sanchezi-v7
#170v7 actualreview PASS_WITH_LIMITATIONS/sciencefalse. Actualv6/fullv7viewed: adultbaretoe shafts nowmutedyellowishgray/warmgrayochre ratherthanbrightyellow; skin scales/grips/clawshapes/darktips/featherboundary retained. Sparsebristles requestedbut notclearlyresolvedinwholeplate, NOTvalidatedbristledensity; keeppendingfinefootcheck, do notaddlonghairjusttoforcevisibility. Rightimmaturetoesremainyellow, greyunspottedcrown/graycere/darkiris/shortformedwing/hidden tail retained. Adultmaleolivebrown/femalerufousplumage/yelloweyes/hornbills/near-equaldisplay and3birds6supportedfeet/forest/labels/footer/v7 preserved. Noextraeditneededfornarrowlargepaletteimprovement; completefootmicroanatomynotpassed. Book384toepaletteonly, primary2024cloudforestnottoecorroboration. Exactsexheight/youngage/flight/irisandfeathersequenceunknown. Problem→oversaturatedadulttoes→ownspeciesyellowgraybristleddescription→skin-onlysubdue→palettechangeobserved/bristlenotproven. Localpaletteapplicationvalid, cannotuniversalizeortransferadulttoyoung. New0/reuse2.

## 171-glaucidium-palmarum-v7
#171v7 actualreview PASS_WITH_LIMITATIONS/sciencefalse. Actualv6/fullv7viewed: adultclawproximalcurves nowwarmbeigehorn versusoldslate, darktipsretained; shape/grips/paleyellowskin/featheredtarsalboundaries preserved. Rightyoungbareparts unchanged, oldergrayplaincrown/fewforeheadflecks/shortformedwing/hidden tail. Adultmutedhornbillsv6fix/yelloweyes/whitecrowndots/cinnamonstreaks/tailbars/near-equaldisplay preserved.3birds6branchcontacts/drypalmcontext/labels/footer/v7retained. Exacthornreflectance stillartinterpretation, no independentlivingclawphotocalibration; bristledtoesnotfreshlyvalidated. Noextraeditneededfornarrowclawchange, youngage/iris/flight/sexheight/tailcountvariationunknown. Problem→darkclaws→speciesguide385horn-darktips→adultclawsheathonly→palettechangevisuallyverified. Sameoperation169neutralgraydifferent171warmhorn showsneedownspeciescolour, notglobalpaleclawsrule. OriginalNelson supportsadulttypepattern/palmforestnotclawcolourorjuvenilechronology; pendingretrievalstatuscorrectedinresearchifactualread. New0/reuse2sourceIDs.

## 172-tyto-castanops-v7
#172v7 actualreview PASS_WITH_LIMITATIONS/sciencefalse. Actualv6/fullv7viewed. Bothadultclaw maincurves nowdarkblackishbrownhorn insteadlightgray, highlightbounded; graybrownskin/scales/tarsalfeathers/grips/curvaturepreserved. Entiredownyyoungclaws/feet/face/darkiris/ivorybill/creamdown/compactwinghidden tail/lowtwofootstep unchanged. Female fuller/larger/darker andpalermale retained, quantitativeheightratiounknownnotmassdoubling. 3birds6footcontacts/eucalyptushollow/log/labels/Clementstaxonplaque/pendingunknownnotes/version7 retained. Only2D newversion; #172v3 and3Dtask untouched. Sourceguide110clawcolour, ABSAsexbiometrics notcolourproof; Debus185Tasmaniandownyemergence notQueenslandflightstage. Exactyoungday/iris/wingsequence/flight/nestmaterialunknown. Problem→paleadultclaws→speciesblackishbrown→adultclaws-onlydarken→actualview confirmsnarrowpalettechange, no youngtransfer. Contrast171warmhorn/169lightgray retainedasownsourceboundary, noglobalclawpalette. ABSArowmisreadtentativenumbercorrectedbeforegenerationtoactualmiddleclaw19.3–23.8m/21.7–33.5f; no numericalgeometryused. New0/reuse3.

## 110-megascops-barbarus-v16
#110v16 actualreview PASS_WITH_LIMITATIONS/sciencefalse. Actualadult-onlystylecrop/ownjuvenilephoto/freshwholeplate/youngclosecrop viewed. Clearmaterialimprovement comparedv15: juvenilefinegranularshortaviantexture/diffusegraybrownbands/palebelly, conspicuousclosedUloops notdominant; somewispyouterdown remains, exactfeathermapnotcalibrated. Noearpoints/yelloweyes/greengraybill/compactconcealedwinghidden tail/twofootgrips. Newwholeplateadultswerealsoaudited: brownrufousocellatedpattern/whitepatches/branchedshafts/yelloweyes/greenbills/pinkbaretoes/hornclaws/shorttail-longwings retaineddirections; ear tuftsvariableallowedbyfieldphotographs. Leftmaleperchslightlyhigher, crown-to-toebodyscalesnear-equal/femalefuller, notquantifiedsexratio.3birds6securefeet/Guatemalanpineoak/labels/v16/pendingunknownfootercorrect; nooccupiednest/flightclaim. Wholeboardnewlayoutnotpixelpreserveclaim. Noextraeditneededafterfull+cropreview. Problem→v9–15targetimageedge-lock→actualphoto+ADULTONLYstylecrop/newtriofromscratch→visibletextureimprovementverifiedhere. Rule discovered/applied/onecaseeffective, NOT universalcure; next130mustownphoto/stageandactualcheck. Exactage/sex/flight/irisandfeatherchronology/colourcalibrationunknown; scientificfalse/userunconfirmed. New0/reuse2, singleactualnewimagegen.

## 130-megascops-koepckeae-v11
# #130 Megascops koepckeae v11 — actual review, NEEDS_REVISION
Sources reused: KOEP-ALARCON-2023 (original printed104 text / printed95 Fig1c photo actually read/viewed), KOEP-MIK2013-222 (same MIKKOLA-2013 guide, printed222). New bibliography0. Full source limits and generation prompt in species record; edit prompt and both waits in run record.
Whole initial and edited 1536x1024 plates + separate juvenile close crops actually viewed. Adults independently checked after complete regeneration: yellow eyes, bluish/greenish horn bills, dark flecked crown/tufts, white scapular breaks, streaked/barred underparts, pale flecked tarsal feathers, graybrown bare toes and dark claws. Warm sunset orange is rendering, not measured taxon colour calibration. Adult near-equal crown-to-toe display is not a sex size finding. Three birds, two feet each, six branch contacts; no unsupported flight, nest, prey or frog. Title/roles/pending footer retained.
Problem→evidence→change→recheck: initial juvenile had conspicuous white oval wing spots, unlike Alarcon Fig1c; edit removed those spots while keeping a short formed folded wing. HOWEVER edited flank/belly developed conspicuous curled U/V filament loops, less consistent with actual fine transverse barred photo. Mark NEEDS_REVISION; do not declare texture solved or scientific pass. Both initial and edited retained; prior v1–v10 preserved. Juvenile white brows/black facial edge/yellow eyes/barred compact body broadly retained; exact age/sex/flight/feather chronology unverified.
Iteration lesson: adult-only style + actual juvenile photo improved #110 texture once but did not transfer successfully to #130 after this edit. 'Short fine down/filament' wording can still provoke curls. Actual application two imagegen calls, no universal validation. Next oldest batch cycle prioritizes this unresolved texture; use same actual Fig1c, preserve legal formed wing, avoid white adult wing marks and hair loops. Archive VERIFIED will mean exact recoverable PNG/research, not science approval.


## 130-megascops-koepckeae-v12
#130 v12 actual whole image viewed against original Alarcon Fig1c and v11. Horizontal lower bands more coherent but obvious curled filaments persist through chest/flank; NEEDS_REVISION, not solved. Adults yelloweyes/bluehornbills/graybrown toes/darkclaws/pale flecked tarsi, three birds/six branch contacts, labels/version/pending footer retained directions. Young legal formed wing/whitebrows/blackfaceedge/yelloweyes retained; exact age/flight/feather chronology/sex unknown. Problem curled Uloops→own-photo flat crossbands edit→some horizontal alignment, curl texture not eliminated. Negative loops wording alone ineffective here; do not claim model improvement. Source new0 reuse2, actual research/prompt in species record; prior versions untouched.

## 176-otus-pembaensis-v7
#176v7 wholeplate actually viewed: adulttoe skin now neutralgray instead beige, darkbrownblacktip claws retained, tarsalbase/grips intact. Young beige feet/unverifieddarkiris/bill/whitishcrossbarredmesoptile unchanged; existing young material still stylized and not calibrated. Adults yelloweyes/darkgreenbill/plaincrowns/narrowscapularline/near-equalscale preserved; all6 branchcontacts/titlev7/footer readable. Palette fix supported guide135 only, institution primarynestunknown remains. Problem warmadulttoe→speciesgraydescription→skinonlyedit→grayseen; local goal works here, no youngtransfer/universal rule. Scientificfalse/exactage/iris/flight/sexheightunknown; no newsource. PASS_WITH_LIMITATIONS.

## 177-otus-hartlaubi-v8
#177v8 actualwholeview: adultclawsnowdarkbrown/chocolatehorn versuscoolgray, darktipsremain. Yellowochretoes/featherboundary/6branchcontacts retained, young entirely retainedincludingunverifieddarkeyes/bill/claws/formeddevelopingwing/nonflyingstance. Adultyelloweyes/yellowgraytippedbills/localbristles/whitescapulars/near-equaldisplay unchanged directions. v8placedonfooter nottitlenextasasked butlegiblecorrectversion. Noextraeditneedednarrowpalette; brownreflectanceguide-only notphotometric. Exactyoungage/bareparts/tarsalfeathermapunknown. Problemcoolgrayclaws→ownbookbrown→adultonlyedit→brownseen, notuniversalpalette. Nauroisfresh403andhistoricalfactsdistinguished; no freshPDFread claim. PASS_WITH_LIMITATIONS sciencefalse.

## 178-otus-insularis-v7
#178v7 bothinitialandtextcorrectedwholeplates viewed: leftmale baretarsi/toes now subduedpalegrayyellow, femalevariation andyoungfeetunchanged; no feathersadded, darkclaws/grips retained. Initialimage added 'Precise-Object-Edit' undertitle; actualdetected and imagegenedited again, finalonlyv7, allotherlabels intact. Bothadultbilldarktips/yelloweyes/bodypatterns, youngbarredfluff/formedwings/twofeet/fieldagecategory preserved; exactyoungage/iris/flightthreshold notvalidated. 3birds6contacts/forestcorrect. Paletteownbook138only, Currie2004 actualprimary supportsbarelegs andfieldfledglingcategory, nottoephotometry. Problemoversaturatedmaleleg→palegrayyellowedit→correctcolourplusunwantedtext→textonlyedit→bothvisuallyconfirmed. New0/reuse2; sciencefalse, PASS_WITH_LIMITATIONS. Lesson alwayscheckalltext afterlocaledit; don't leak implementationwords.

## 175-otus-ireneae-v8
#175v8 wholeplate actualview: bothadultclawsmuchdarkerbrownwithblackishhooks, palegraypinkbrown baretoe shafts broadly retained; exactskin/clawjunction darktransition uncalibrated/pendingmicrocheck, not pixelunchangedclaim. Youngpaleclaws/eyes/bill/body retained. Adults paleeyes/greenhornbill/pinkgraycere/morph/tarsalocclusion preserved. Threebirds6branchcontacts/threeunknownfooterlines/titlev8legible. Ownsourcebook134+OwlPagessecondaryagreepalette butnotindependentmeasurement. Problempaleclaws→darkbrownblacktipadults-only→qualitativedarkeningconfirmed; no youngtransfer. Exactage/iris/flight/tarsalboundary unknown, PASS_WITH_LIMITATIONS sciencefalse. 178textpollutionbackcheckednonehere.

## 134-megascops-sanctaecatarinae-v11
#134v11 initial/finalwholeplates andactualWikiAves RIGHTyoung photo viewed. Replacingvisibleyoungfromownphoto did NOT suppress long outlinedU/Vloops, now evenmorecrisp; orbitalpaleedgevisiblebutnotfaithfullycalibrated. NEEDS_REVISION, notmaterialsuccess. Initialretainedv10title incorrectly, secondimagegen fixedv11actualview; initialalsoarchived. Youngdarkeye/greenhornopenbill/roundedhead/bodyextentbehindcavitylip/hiddenwingtailfeet retained, no inventedhiddenanatomy. Adultindividualirides/greenishgraybills/lightgraybrowntoes/darkclaws/fouradultbranchgrips/near-equalbody/Araucaria/cavity/roles/pendingfooter preserved directions. Cavitydesigninference notreconstructionofimprovisedphoto nest. Exactyoungage/flight/wingfeetunknown; book239 explicitlyyoungunknown. Problemcurledtexture/weakrim→photo-referencedvisibleyoungreplacement→loopsstilldominant→textversionfix→failurehonestlyretained. Repeatingwording/localeditsnotvalidated; queue134and130 for a genuinelydifferent reconstruction approach nexttime. New0/reuse3; sciencefalse.

## 179-otus-mayottensis-v6
#179v6 actualv5/fieldadultphoto/generatedwholeviewed. Smalladultthroatwhitishgroundnowvisiblebeneathbothbills withdarklines/barring retained; becomes narrowVcollar, preciseextentnotcalibrated. Bauerphoto headtilted/shadedthroat doesnotindependentlymeasurewhiteextent; colourgoalguide139only, notpopulationproof. Brownventrum/reducedshoulderflecks/yelloweyes/grayhornbills/near-equaladultbody/shortbaretarsus/graybrowntoes/darkclaws retained, threebirds6footcontacts/evergreenbranch/labels/v6/footer intact. Youngunchangedclosedeyes/unknownplumage, museumimmatureidentityNOTphenotypeevidence; no youngscientificpass. Problemuncontrastedbrownthroat→bookwhitethroatwithdarkmarks→localedit→whitishbasevisuallyseen, actualfeatherextentstillpending. New0/reuse2/sciencefalse/PASS_WITH_LIMITATIONS. Needindependentproperlylitadultthroatphoto beforecalibration.

## 195-otus-brookii-v6
#195v6 actualwholeplatevs v5: bothadultclawsmaincurves nowdarkhornbrown/gray ratherthanverylightgray; paleallowedtoes/featheredtarsalboundary/clawshapes/sixgrips retained. Youngpaleclaws/whitishrufousbelly/rufoushead/mesoptilebars/formedwing/shorttail unchanged, uncalibratedcurlmaterialnotclaimedfixed. Adultlongwhiteinnertufts/brows/paleyellowbills/eyevariations/near-equaldisplay, emptycavityforest/rolelabels/pendingfooter/v6 intact. Problemlightclaws→ownbookdarkish→adultonlydarken→qualitativelyseen; hue/tractmicroboundary notmeasured. Gooddie74actualread supportsadult/nestcontext notclawpaletteorjuvenilechronology. Commonsmisidentifiedyoungstillnotborrowed. New0/reuse2/sciencefalse/PASS_WITH_LIMITATIONS.

## 202-ninox-theomacha-v6
#202v6 actualwholeview adultclawsnowblackcharcoal/limitedhighlights, dullyellowbrowntoes/reddishtarsalfeathers/gripsunchanged; youngclawsremainoldpalehorn notadulttransfer. Adultsplainbrowndorsum/chestnutbelly/goldeneyes/yellowbill/greencere preserved. Younggraychocolateupperchest/rufousabdomen/residualgrey/unbarredformedwing/unknowniris-bill/stance retained. 3birds6branchcontacts/titlev6/nominateplaque/unknownfooterintact. Problemgrayclaws→ownbookblack→adultonlyedit→blackvisuallyseen. Sourceowlpagesfreshbodyonlyidentity/distributionnotcolourproof, wrongs580excluded. Exactcolourreflectance/youngage/flight/sexheightunknown; historicalskinnotnewlyread. New0/reuse2/PASS_WITH_LIMITATIONS/sciencefalse.

## 204-glaucidium-sjostedti-v4
#204v4 actualwholeview: adultscalytoe skin now paleyellow ratherthandeeporangegold, cinnamontarsalfeathers retained; hornclawsdarktips/gripsunchanged. Sparsebristlesnotclearlyresolved thusnotvalidated, don'taddhairtoforce. Youngownbareparts/underbarpatternunchanged, Efulenhistoricalvsbookyoungbarconflictstillunknown. Adultwhiteplainthroat/yelloweyesbills/chestnutmantle/whiteheadbars/palelowerbelly retained; 3birds6contacts/titlev4/footerreadable. Problemoversaturatedtoe→guide410paleyellow→adultskinonlyedit→palettequalitativelyconfirmed. Ownbookonlypalette, OwlPagesidentityrange notindependentcolour. New0/reuse2/PASS_WITH_LIMITATIONS/sciencefalse; preciseage/flight/youngiris/billunknown.

## 203-megascops-guatemalae-v4
#203v4 actualwholeandprioradultthroatcropviewed. Smallgraywhite throatground belowadultbills nowclearer, fine darkruf/facialpatternretained; no giantblankwhitebib/lowerbellybarringregression. Adults yelloweyes/greenbills/duskyfleshtoes/hornclaws/featherboundaries/near-equalsizes andsix naturalfootcontacts maintained. Youngunchangedunverifieddarkeyes/greenbill/ageunknownmesoptile/curltexture notclaimedcorrected. Titlev4/nominateplaque/rolelabels/footer/forestintact. Problembrownthroat→freshOwlPagesexplicitwhitish→localonlyedit→palerthroatactuallyseen. Exactpatchshape/hueguide-secondarynotindependentfieldcalibration. MGUAbook supportsotheridentity/stagefacts, notnewmeasuredwhitepatch. New0/reuse2/PASS_WITH_LIMITATIONS/sciencefalse. Neither source validatesyoungday/flight/iris; sourcefactvsdesignwhiteboundary distinguished.

## 201-otus-mantananensis-v10
#201v10 actualv9/primarypublicpreview/finalwholeviewed. Adultclawsmaincurvesnowdarkhornratherthanpalegray, tipsremainblack, palegraybrowntoes/narrowbarezone/tarsalfeathers/gripsretained. Youngpaleclaws/restingclosedeyes/buffhead/mottledupperchest/formedwings/tailconcealment/twofootgrips unchanged, notvalidatednominateyoung. Adultpatterns/yelloweyes/graybills/near-equaldisplay/title#201v10/forest/mixedpopulationplaque/unknownfooter intact. Problempaleadultclaws→ownbook199darkhorn→adultsheathonly→qualitativedarkeningseen, reflectance/skinclawboundaryunmeasured. CurrentoEmbedactuallyreturned exactjuvenileromblonisSemirara title andPhotoArkauthor, 7282byte480x360previewactuallyviewed; notfullvideo/time/preciseyoungiris orfirstflight. Sourcecaptionidentityandcoarsemottlingonly. New0/reuse2/PASS_WITH_LIMITATIONS/sciencefalse, no thirdpartyimagearchived.

## 20261127T1429Z 216-otus-thilohoffmanni-v4
Actual complete output viewed. All three hard bill surfaces are paler low-saturation ivory-yellow; pink ceres and role eye colours remain distinct. Adult heights/plumage/feet/contact and juvenile incomplete disc/pseudo-crown corners/formed wings remain qualitatively stable. Local palette adjustment realized; source conflict primary whitish vs book yellowish retained, no asserted biological error resolved. Whole plate scientific false, exact colour calibration and young age/flight/nest unknown. No immediate further edit indicated for chosen bounded palette. Rule: read actual source wording before declaring colour defect; initial research misstatement corrected before generation. PASS_WITH_LIMITATIONS.
Research boundary and full actual prompt: ../research/species/216-otus-thilohoffmanni-v4.md . Applied in this image only, not a universal biological validation.


## 20261127T1429Z 217-otus-longicornis-v4
Actual complete final image viewed: juvenile repeated bold pale U/crescent rims substantially removed, grey soft down field and irregular brown transverse chest bands visible, head/back darker. Adult colour/size/eyes/bills/long tufts, three-role labels/footer and branch contact retained. Juvenile closed eyes, small compact wing/no long adult remiges/hidden tail and both grips retain stage-conservative supported resting pose. Fine head loops/individual band geometry still artistic, no measured stage chronology. PASS_WITH_LIMITATIONS/scientific false; texture reconstruction effective locally, not retroactive validation of unresolved #130/#134. Next check compare crop before applying elsewhere.
Research boundary and full actual prompt: ../research/species/217-otus-longicornis-v4.md . Applied in this image only, not a universal biological validation.


## 20261127T1429Z 219-otus-podarginus-v4
Actual final complete plate viewed: juvenile pale repeated loops substantially reduced; loose fine reddishbrown filaments, darker crown and subdued transverse brown colour stripes now read as soft plumage. Older compact formed folded wing retained, not replaced with hatchling appendage; existing headtilt/iris/provisional bill, both supported feet stable. Adults/creamy bare lower tarsi/blackishclaws, rainforest and all labels remain. Fine filament scale/stage and wing sequence still unverified. PASS_WITH_LIMITATIONS/sciencefalse. Problem model outlines every feather; actual material-specific rebuild reduced loops here, cannot declare success on #130/#134 or all oldgroups.
Research boundary and full actual prompt: ../research/species/219-otus-podarginus-v4.md . Applied in this image only, not a universal biological validation.


## 20261127T1429Z 218-otus-nigrorum-v4
Actual final complete image viewed. Young flank/compact wing sharp bright scales greatly reduced, feather edges diffuse; buffwhite ventrum retains dusky transverse pigment bands. Young rufousbuff crown/fine bars and closed eyes persist. Wing separation is now less distinct under soft feathers, not pixel-identical; no extended remiges or new flight claim. Adults' individual patterns/iris/pinklids/sex bellycontrast/tarsus and all three paired grips/text retained. Material correction effective locally but precise immature feather edge, chronology, iris/bill remain uncalibrated. PASS_WITH_LIMITATIONS/sciencefalse. Avoid describing mere lowered wing contrast as proof of delayed wing development.
Research boundary and full actual prompt: ../research/species/218-otus-nigrorum-v4.md . Applied in this image only, not a universal biological validation.


## 20261127T1429Z 215-otus-angelinae-v4
Both actual initial and second full originals viewed. Initial body wire loops lower but crown retained connected wirelike crossgrid; second targeted crown edit broke some raised filaments and loosened top contour, yet connected artificial ridges remain. Crown material target NOT fully achieved; NEEDS_REVISION/scientificfalse, not claimed solved. Body material improvement and existing faint transverse pigment/broadbackbands retained, oldercompactwing/pairedgrips/eyeunverifiedlabel remain; adults and text qualitativelystable with slight rerender drift. No age/iris/flight facts added. Record initial and edit prompt/waits, preserve both assets. Repeated prompt-only local edits are not proven to solve crown lattice; next round should use actual juvenile reference/full-region reconstruction, while unresolved #130/#134 also remain unpassed.
Research boundary and full actual prompt: ../research/species/215-otus-angelinae-v4.md . Applied in this image only, not a universal biological validation.


## 20261127T1429Z 220-tyto-rosenbergii-v4
Actual final complete output viewed. Right chick white/cream down noticeably finer, less long coiled-loop texture, greyfacialarea/incompletedisc/provisional bill remain; short downveiled wings/no mature flightblades/tail, both feet on flatwoodfloor supported. Adults' spotting/eyes/creamy bills/feathered tarsi and bare toes stable; sizeunknown label retained, not claiming equal height. Clementsplaque now reads Tyto javanica rosenbergii doublei, corrected against actual Cornell list. All labels/footer intact. Local material+orthography change effective; sourcephoto pixels unavailable fresh, exact downmicrostructure/age/iris/bill/flight stillunverified. PWL/sciencefalse, no assertion originalphoto independently rechecked. Historical primary photograph used by preserved earlier actualrecord, not a freshview substitute.
Research boundary and full actual prompt: ../research/species/220-tyto-rosenbergii-v4.md . Applied in this image only, not a universal biological validation.


## 20261127T1429Z cross-check and failure boundary
217/219/218/220 actual output soften overly repeated feather-edge patterns while retaining evidenced colour bands. 215 second crown edit still artificial lattice: NOT validated; avoid claiming universal prompt success.130v12/134v11 prior records reviewed only, no fresh image inspection or correction credited.216 original colour wording conflict explicitly read before generation;220 publisher screenshot text placeholder is not actual photo viewing. Full fact/prompt/review links in batches/20261127T1429Z-six-cycle-review.md .


## 20261127T1529Z 215-otus-angelinae-v5
Initial and follow-up full originals actually viewed. New specific observed fledgling stage: whitishbrow/russetface, paler largely plain cream lowerabdomen/sparse rufous chest bands, no visible longtufts, formed compact folded wing/short concealedtail and two supportedfeet. Second material edit removes prominent crown coil lattice into fine short wisps; pale belly filament loops reduced. Fine strand scale still artistic/coarsemonochrome reference cannot validate it. Both adults/labels and environment retained qualitatively with small rerender drift, not pixelidentity. PWL/scientificfalse; improved material locally and source-specific stagechange is explicit, not alljuvenile claim. General book darkjuvenile description retained in record; exact stage variation/age/iris/flight remains unresolved. Firstflight age estimated from other species in Becking not adopted.
Research/fullactualprompt: ../research/species/215-otus-angelinae-v5.md . Applied in this image only, not universal biological validation.


## 20261127T1529Z 130-megascops-koepckeae-v13
Bothactual full initial and followup viewed. Wholejuvenile reconstruction straightened head and changed bodyorientation/support, retains primarywhitebrows/yelloweye/blackdisc/bluegreybill and moreevidentcompactformedwing, adults/tarsi/feet/text remain. Initial retained finecrossbars but strongbrightUloops persist and smallwing paleoutlinedscale rows. Followup lowerededgecontrast but weakened primarybarpattern and stilllooped. Select initialv13 clearerbarphenotype, rejectededit preserved separately. NEEDS_REVISION/scientificfalse; do not assert newmethod validated. Exactage/flight/feathermicrogeometry unknown, no prey/nest inferred. Further work requires material strategy distinct from repeatedconditionalnegativeprompts; 215successfullocalmaterialchange not universal.
Research/fullactualprompt: ../research/species/130-megascops-koepckeae-v13.md . Applied in this image only, not universal biological validation.


## 20261127T1529Z 134-megascops-sanctaecatarinae-v12
Actual complete newtrio original viewed. Wholetrio fromadult-onlystyle+realjuvenile reference yields substantially finer granular shortfeather young surface, no continuous raisedwirelattice or adulttufts; darkeye/featheryorbit/smallpalebrows/greenhornopenbill/faintbrowncrossbands realized. Young whitefeatherface distribution remains stylized and moreconspicuous than photo, microgeometry notcalibrated. Juvenile wings/feet/tail concealed behindlip, body support plausible; cavity is design, notphoto-specificnest. Fouradultfeet stronggrips, toebasesfeathered/lightgrey-browntoes/darkclaws, individualyellowvsbrowneyes explicitnotsexmarker, no fixedsexheight assertion. Adultbushyshorttips improved relativev11 needlepoints; adultpattern coarsegenreference lacksregion-specificcalibration. PWL/sciencefalse; newwholeplate+adult-onlystyle strategy visually effective once, notuniversalvalidatedrule; oldoriginals retained.
Research/fullactualprompt: ../research/species/134-megascops-sanctaecatarinae-v12.md . Applied in this image only, not universal biological validation.


## 20261127T1529Z 221-ninox-meeki-v4
Actual final full image viewed: juvenile crown/brownupperbreast now finer short edged feathers, raised curledloops reduced, white throat and heavycreamwhite wingcovertbars preserved. Narrow rusty lowerstreaks, compactformedwing/hidden tail/sleepingneck and bothfootgrips stable. Adults and originalsexdisplay/eyes/bills/crownpatterns unchanged qualitatively, allrolelabels/footer visible. Localmaterial improvement PWL/sciencefalse; noprimaryfinefeathergeometry, age/iris/flight/nest stillunknown; not a developmental finding. Sourceprimary1914 accessfailure retained, noadultcrowncorrection inferred.
Research/fullactualprompt: ../research/species/221-ninox-meeki-v4.md . Applied in this image only, not universal biological validation.


## 20261127T1529Z 222-ninox-sumbaensis-v3
Actual final fulloriginal viewed. Youngbrownrufous crown and body repeatedbright curls reduced, softer finewisps; plain reddishunmarkedventrum preserved, noVbars/whitepatches. Supported headwinding-inspired tiltedhead/insectwatching eyeline remains, not depictionofhunting; compactformedwing/hidden tail/pairedtoegrips intact. Adultbarredcaps/finechevrons/whitebrows/eyes/near-equaldisplay and originaltitle/roles/footer stable. Somefinecurved strands persist, texture stillartistic/unmeasured; localPWL/scientificfalse, exactage/billiris/toe/growth/flight/nestunknown. Must not transfer rudolfi size statements tosumbaensis.
Research/fullactualprompt: ../research/species/222-ninox-sumbaensis-v3.md . Applied in this image only, not universal biological validation.


## 20261127T1529Z 223-strix-butleri-v4
Actual complete output viewed. Bothadult upperdisc aboveeyes now greybrown with softtransition to palegrey lowerface, centraldarkcrownstripe/pairedwhiteclusters preserved; nofullblackmask/tufts. Orange-yelloweyes/green-greybills/thinventralshafts/whitefeatheredtoes/horn-greyclaws/sixrockcontacts intact. Juvenile olderformedwing/graycrownpatches and alltext/sourcefooter preserved, no age/flightassertion. Adultfacialtone localPWL/scientificfalse; exactdiscfield/photometriccolour/sexratio unvalidated. Young finecurlrender remains historicaldisplay, no new juvenilematerial/sciencepass transferred; futurephoto-specificrecheck needed before any new texture claim. Existing2013broadbutleri book excludedfromcurrentyoungtaxonomy.
Research/fullactualprompt: ../research/species/223-strix-butleri-v4.md . Applied in this image only, not universal biological validation.


## 20261127T1529Z cross-image evidence/strategy limits
Actual primary215 fieldstage differs from generalizedguideyoung; explicitstagechoice/citation resolved designscope but cause of difference notproven. Materialfollowup improved215/221/222 locally; notuniversal.134 wholetrio from adult-onlystyle+realjuvenile reference removes previousmesh largely, oneinstance only.130 newbodypose plus followup stillfailedUoutline, and secondedit weakened actualbarfact: keepinitialnewv13/NEEDS_REVISION and bothattempts.223adultfacialdisc only; youngcolour/material notnewlycalibrated. These are applied+visuallychecked findings, no scientificpass. Each fullprompt/review linked in batches/20261127T1529Z-six-cycle-review.md .


## 20261127T1629Z 130-megascops-koepckeae-v14
Actual initial and edited full plates viewed against primary Fig1c. Problem—evidence—change—recheck: initial juvenile too warm brown and pronounced pale U/scallop rims; edit cooled chest to smoky grey, reduced rim contrast and retained yellow eyes/white brows/black ruff, supported perching, real formed wing. Recheck: repeated curved pale feather margins still visible, bars less distinct than field image; unresolved material issue NEEDS_REVISION. New whole-trio conditioning improved upright stance relative v13 but did not eliminate looped texture; do not claim method validated. Adults near-equal display, broad shaft streaks/short tufts/bare toes rendered; adult warm light strong, not a calibrated subspecies colour claim. No nest invented/no prey/no flight action. Sex-size data, juvenile precise age/subspecies and match between reference adults and Ecuador young remain unknown. Scientific verification false; old originals/user decisions unchanged. Next material revision should test simplified continuous grey down with separate narrow bars, not repeatedly re-edit same texture at this invocation.
Fullresearch/prompt: ../research/species/130-megascops-koepckeae-v14.md . Applied/visuallychecked here only, not universal biological validation.


## 20261127T1629Z 108-otus-rutilus-v8
Actual full first edit and whole-trio reconstruction viewed against FrankVassen2013 photo. Direct old-plate edit failed (archived initial). New adult-only+own-photo generation visibly replaces long coil network with shorter dense brown granular down, source-like side head angle/darkmask/yellowbrown eye/pinklowerlid/darkbill/concealedwingtail and supported twofeet. Fine curl granules remain stylized; no exact feather geometry or age calibration. Whole-trio adults rechecked: yellowirises/graybrownbill/smalltufts/herringbone shaft marks/white scapular stripe/graybrown toes-darkclaws/featheredtarsi; near-equaldisplay rather than ratio. Threebirds/sixfeet, branch support, humidforest and ageunknown/flightunverified/sciencepending labels correct. Source-like juvenile smaller than oldplate is design choice not measured age scaling. PASS_WITH_LIMITATIONS for long-lock reduction, sciencefalse, exactyoungage/sex/flightunknown. Strategy effective in this one case, #130 earlier failure retained and prevents universal-rule claim.
Fullresearch/prompt: ../research/species/108-otus-rutilus-v8.md . Applied/visuallychecked here only, not universal biological validation.


## 20261127T1629Z 120-megascops-ingens-v8
Actual v7, first edit, final second edit full originals viewed. Initial retained long pale curls; final material edit substantially lowered individual strand contrast and changed belly/throat to continuous soft beige masses with fine pale residual down. Subtle fine fiber traces remain; PASS_WITH_LIMITATIONS for visible longcoil reduction only, not literal feather density/map. Real developed folded barred remiges intact, no wingbud regression. Browniris/darkface/graybill/smallpaleeggtooth/openbill supportedpose retained; movement interpretation billclap not flight. Adults honeybrown iris/subduedpinkbrownlid/oliveyellowbill/palehornclaw/yellowgraytoe/near-equaldisplay retained; exactly3birds/sixfeet/natural deadstump. Title v8/new variation preserved. Primary author fulltext actually read; originalfigureattachment403/RGimage404, no photographpixel claim. Body110cm vs abstract2.5m and estimated age20–30/discussion25–30 recorded as conflict, notresolvedbyrender. Scientificfalse. Lesson lowcontrasttonalfields effective inthisonecase afterfirststrandeditfailed, formedwings separatelyprotected; no universal all-downrule.
Fullresearch/prompt: ../research/species/120-megascops-ingens-v8.md . Applied/visuallychecked here only, not universal biological validation.


## 20261127T1629Z 119-megascops-centralis-v9
Actual full input/output viewed: adult pale white V-brows now subdued brownish and integrated with crown; facialdisc edges softly blended, black orbitalring/yellowiris/greenyellowbill retained. Direction matches directguide hardlyvisiblebrows, exact shade is designjudgement. Adultpattern/shorttufts/whitewingpatches/pinklowertarsi-vs-paleyellowtoes/hornclaws and near-equaldisplay retained. Juvenile graybuffcrossbars/formedwing/hidden-tail/ageunknown/yelloweyes/twopinkfeetonsill retained; no newyoungmaterialclaim. Exactly3birds/sixsupportcontacts/lowlandrainforest/cavity/text with119v9sciencepending retained. No extraedit needed for selectedadultbrowtarget. PASS_WITH_LIMITATIONS, scientificfalse; exact juvenile age/flight/parasite growth unknown. FreshAOSmappingbodyread, DOI/publisherbodyfailed; historicalpaper evidence not labelledfresh. Lesson: separately specify orbital skin ring and feathered outerdisc edge, successfully applied visibly here, not generalblackrimremoval acrossowls.
Fullresearch/prompt: ../research/species/119-megascops-centralis-v9.md . Applied/visuallychecked here only, not universal biological validation.


## 20261127T1629Z 123-otus-gurneyi-v8
Actual originalshankar2013pixels/cropadultstyle/v7/newfulltrio viewed. Newjuvenile markedly shorter dense granular graybrown feather/down replacesoldlongcurlmesh; source-like darkcrossmottling/softuprighttufts/darkiris-pinkpurplelids/darkbill/narrowformedsidewings/concealedtail retained. Some finefuzz atlowerbelly remains asphoto, not novelhatchage. Wholeplateadultsaudited: rufousunmarkedfaces/brownirises/graywhitebills/longspottedtufts/darkshaftstreaks/palescapularspots/featheredtarsi/graybrowntoes/palehornclawsdarktips recentfixretained. Maleupperperchbody tallerdisplay, no adultsexheightratio validated, femalefullerbody notinventedsexmark. All3birds/sixcontacts/grippingbranch/Philippinegenericforest/titlev8/ageunknown/flightunverified/sciencepending correct. PASS_WITH_LIMITATIONS for materialimprovement and preserveddiagnostics, no whole-sciencepass. Exactage/sex/morphstage/flight and wildnestunknown; captivephotocontext notwildbiology. No furthereditrequired selectedtarget. Strategyadult-only+same-speciesphoto/newwholetrio successfulvisuallyhere+#108, not #130universalrule. Access initial403 correctedthroughFlickrogimage, fullbodyphoto actuallyviewed beforegeneration.
Fullresearch/prompt: ../research/species/123-otus-gurneyi-v8.md . Applied/visuallychecked here only, not universal biological validation.


## 20261127T1730Z 138-otus-mentawi-v8
Actual input and full v8 output viewed: juvenile underparts now noticeably paler cooler graybrown with finer thin dark longitudinal streaks, compared v7 broad warm shaft marks. Young darker reddishbrown face/brown iris/palegrayhornbilltoes/formedfoldedwing beyond shortdarktail/faintnarrowflightbars retained. No all-downregression/noflightclaim. Adultocelli/chestnutground/browniris/yellowhornbill/shorttufts/featheredtarsi/fleshtoes/darkhornclaws/near-equaldisplay maintained. Exactly3birds/sixfootgrips/branchsupport/forest/ageunknown andv8sciencependinglabels. No furthereditneeded for selectedcolour/streaktarget. PASS_WITH_LIMITATIONS qualitative primarytext match only; feathergeometry/stageexactage/sexsize/flight unknown. Priorbookpages reused historically; notfreshavailable. Problem–evidence–change–recheck: v7heavywarmstreaks versus2018p31–32 thin/pale→narrow juvenile-onlyedit→visiblefinegraystreak improvement. No newnest/growthclaim, no blanketjuvenilerule. Recovery: oldleaseexpired, reusedpersistentRESEARCH_READY notnewcycle; oldscratchunavailable/currentv7downloaded. Sciencefalse.
Applied and visually checked here only; not universal scientific validation.


## 20261127T1730Z 130-megascops-koepckeae-v15
Actualphoto/isolatedstudy/integratedfullplate viewed. Study had diffusegraydown/faintbars; integration reintroduced prominentlyoutlinedpaleU/scallopedmargins onyoungthroat/breast and morestructuredlongfoldedwing. Materialgoal NOT achieved, NEEDS_REVISION/sciencefalse. Face yellowiris/whitebrows/blackdiscedges/bluegraybill supported; bodychangedfrontstance stilltwofeetsecureperch, no age/flight proof. Wingboundaryneedscomparison tofieldphoto nextrevision; do notcallscientificallycalibrated. Adults near-equaldisplay/shorttufts/shaftstreaks/featheredtarsi/baregraybrowntoes and3birds/sixsupportfeet/titlev15/pendingfooter retained. Methodphoto-onlystudy→integration visuallyfailed onthisplate, despite successelsewhere; do notextendpipelineclaim. Preservestudy/fullprompt/failedintegration/oldv14. Nextpriority: avoidoldyoungconditioningentirely or simplifywholejuveniletonalvolume; don'trepeatsameintegration. Sourceactualoriginalread p104/Fig1c, Mikkolahistoricalonly. No newpublication/sexsize/earlystageclaim.
Applied and visually checked here only; not universal scientific validation.


## 20261127T1730Z 79-otus-lettia-v9
Actualv8/institutionalphoto/v9fullviewed: juvenile breastbelly finegraybuff surface morecontinuous and lesslarge paleoutlinedflakes thanv8; faint narrow diffusebars retained. Some smallcurvedmargins remain, exactfeathergeometry notvalidated; PASS_WITH_LIMITATIONS for reducedoutlinecontrast only. Headsmalltufts/darkbrowniris/warmrim/palehornbill/compactformedwing/hidden-tail/twofeetbranch kept; sourcefeetpartlyhidden so contactgeometry designednotinferred. Bothadultfeaturepalette/near-equaldisplay/3birds6grips/forestcavity/titleandunknownage-flight-sexratiofooter retained, notliteralnestreconstruction. No additionaleditneededselectedtarget; scientificfalse. Photoactualpixelread andregionalaccountbodyfresh, bookhistorical only. Lesson reduceoutlinecontrastindowninterior withshortfinebarbends andseparatepigmentbars fromedgegeometry, visiblyeffectivehereonly; #130failedintegrationnotuniversalrule.
Applied and visually checked here only; not universal scientific validation.


## 20261127T1730Z 86-otus-elegans-v10
Actualinput/sourcePhoto1head/outputfullviewed. Unsupportedfullydepictedjuvenilewingstretch andbodyreplacedbyone nestyounghead/upperchestatnaturalcavitylip, wings/tail/feetoccludedinside; nofloatingshowntoes ornewremexsequence. PWL for reducingunsupportedanatomy, NOT verificationofhiddenfeet/bodystage/exactage. Headsoftgrey-buffdown/roundface/greyhornbill/yellowisheyes qualitativesourcephoto only; exactiris/tuftlengthunverified. Twoadults sameyellowiris/darkbill/graybaretoes/darkclaws/finebellycrossmarks/near-equaldisplay preserved. Threebirds exactly, source-speciesinterpositus explicittitle/v10/correctNESTYOUNGageunknown/footer. Casuarinacavityandshelterbelt-cane supported regionalrecord, openinggeometry/sill artisticnotliteralnestreconstruction; noegg/prey/liningadded. Noextraeditneededselectedsupport/wing-evidenceboundarytarget. Oldv9kept; bookhistorical-only. Lesson useobservablebodyregioninstead ofinventedcompletewing/footphase whenprimaryphotoonlyshowshead, appliedandviewedhere, notalljuvenilesshouldbehidden. Sciencefalse.
Applied and visually checked here only; not universal scientific validation.


## 20261127T1730Z 85-otus-semitorques-v11
Actualfullinput/sourceFig3/outputviewed. Young visibleamberirisring substantiallydarkenedundernaturalbrowshadow; tinyreflectiveeyeopen/stillthere, notblackirisphenotypeclaim/closedeye. PASS_WITH_LIMITATIONS for reducedunverifiedcolourspecificity. Lowcrouch/down/tufts/shortincompletewing/concealedtail/bilateralfeetbellysupport retained. Adults orangeirises/grayhornbills/grey-brownpattern/featheredtarsi andtoebacks/hornclaws/near-equaldisplay retained;3birds/sixcontacts/Cryptomeria/titlev11/rolelabels/age-iris-firstflight-sexratioUNVERIFIED footer. No wingredrawbecauseexistingwingcompatiblequalitativeFig3, no unnecessarychange. Exacthatchage/sex/firstflight/sourceirisunknown, nestnotfound. Evidenceoriginalsaysirisundiscernible→shadeeyesratherthanassigncolour→actualviewvisibilityreduced, notbiologicalcorrectiontonewknowncolour. Scientificfalse and fulloriginalpaperreadthiscycle, bookhistoricalnotfresh.
Applied and visually checked here only; not universal scientific validation.


## 20261127T1730Z 95-pulsatrix-melanota-v9
Actualv8/initialmaterialedit/textcorrectedfulloutput viewed. Longhangingcinnamonlocks visuallyshortened/lowercontrast and bodymorecontinuoussoftdown; finerstrandtracesstillstylized/unmeasured. PWL localmaterialtarget only, notwholefeatherchronologycalibration. Initialwrongliteralv9by95 preserved; texteditremovedit and addedcorrecttopv9, rolelabels/footer/plainwhite typography retained. Youngcinnamonbody/creamwhitecrown/blackface/darkbrowniris/yellowbill/smalldevelopingwing/concealedtail/lowforktwofeetbellysupport retained. Adultdarkiris/paleyellowbill/greycere/whitespectacles/brownchestband/rustybellybars/featheredtarsi/baregraybrowntoes/hornclawsblacktips/near-equaldisplay/3birds6grips maintained. No newnestreconstruction; originalpaperphase distinctearlywhiteperiocularchickvsolderblackface, noexactday/flight/sexratioproof. Actualprimaryfullbodyread, freshphotoaccessnotclaimed andbookunavailablehere historicalonly. Lesson exactlabelplacementavoidliteralinstructiontext, actualedit+recheckcorrectedhere; strongestremainingmaterialproblem130stayspriority. Sciencefalse.
Applied and visually checked here only; not universal scientific validation.


## 20261127T1826Z 130-megascops-koepckeae-v16
Actualv15/photo/newfirst/finalfullplatesviewed. Photo-only biologicalconditioning (nooldgeneratedyoung/adultstyleimage) substantiallyreduceslargebrightUoutlines comparedv15, graywhitebars nowfiner/darker/dense andnearersource. Finecurvedbarbmarginsstillremain; PWL forreducedcontrast/scale only, notperfectfeathergeometry/scientificapproval. Firstfreshyoungwingbrightadult-likewhitecovertrow identified; actualwing-onlyeditmutedrowtograybrown/faintbars whilekeepingformedcompactwing, noall-downregression. Adultsfullrebuildaudited: shorttufts/darkfleckedcrown/blackruff/yellowiris/bluegreenbill/broadbranchedshaftmarks/paleochrebreast/brokenwhitescapularline/featheredlightyellow-brownspeckledtarsi/baregraybrowntoes-darkclaws; near-equalbodydisplay notvalidatedsexheightrelation. Threebirds/sixsecuregrips/Andeanshrub/titlev16/age-sex-flightunknownfooter. AdultsregionalcolourandEcuadoryoungnotsubspeciesmatchedfamily, nooccupiednest/prey. Sourcebookactuallyrecovered/rereadp222thisrun; cachedprimaryfullbody/Fig1cactuallyreopened. Methodvisuallyimprovedhereafterv15failedintegration, notuniversalvalidation. Wingcolourcorrectionappliedandverified, oldversionsandfailedinitialretained. Scientificfalse.
Applied and visually checked here only; not universal scientific validation.


## 20261127T1826Z 206-glaucidium-castanopterum-v5
Actual full generated PNG viewed after generation. Adult brown/ochre barred upperchests and muted lateralchestnut feathers now distinct from mostlywhite centralbelly; overlongbrightorangestreaks reduced bothadults. Notexactphotocolortransfer; someillustrative feathergeometry remains. Yellowadultiris,green-yellowbills/olivecere,white scapularmarks, near-equaladultsizes(no sexdata),seven visible male tailbars,featheredtarsi/sparse toe bristles/darkclaws/branchcontacts rechecked. Rightyoung retains dulladultlike fullyfeathered age-unknown stage rather than invented neonate; youngiris/bill/flightunknown label retained; no nest reconstructed, denseJavaBali forestplausible. PASS_WITH_LIMITATIONS, scientifically_verified=false. Problem-evidence-change-review: v4 allfrontorange longitudinalpattern obscured lateralchestfield; Mikkola407actualtext/photocaption plus independently viewed Veronesi2016photo support regionalpatterndifference; targeted adultchestedit applied and checked. Young unresolved not upgraded; rule use feather-tract region rather than uniform wholefront streak substitution. New1 photo/reuse2 IDs; no userconfirmation.
Applied and visually checked here only; not universal scientific validation.


## 20261127T1826Z 170-glaucidium-sanchezi-v8
Initial and corrected fullPNGs actuallyviewed. Rightyoung crown nowgrey-brown withoutdiscrete pale adultlike crownspots, feather shaft/highlights retainednotcountedspots; smallfacebrowflecks outsidecrown retained. Firstoutputwrongversionv7 fixedsecondimagegen nowv8; bothprompts/initialsaved. Adults olivebrownmale/rufousfemale spottedcrowns, nearequalsize(youthsizeillustrative), adultyellowiris/hornyellowbill/graycere,bristledyellowgraytoes/hornclawsdarktips rechecked; rightyounggreycere/closedformedwing/shortpalecinnamontail and supportedfeet retained. Densehumidforestplausible, nooccupiednest. Mesoptile sourcebook-only; exactage/iris/flight unknown, scientifically_verifiedfalse. PASS_WITH_LIMITATIONS. Lesson: juvenilecrown mask separate fromface and adultspotting; prompts do not guaranteeversiontext, actualsecondreviewrequired. External PDF download502 logged; actualwebpaperbodyread supportsenvironmentonly. New0/reuse2stableIDs.
Applied and visually checked here only; not universal scientific validation.


## 20261127T1826Z 171-glaucidium-palmarum-v8
Actualfullv8viewed. Greyjuveniletop/backcap now unspotted; fewpale foreheadflecks remain bounded abovebrow, contrastingbrownupperparts. Adultwhitecrowndots/yellowiris/yellowhornbillcere/cinnamonstreaks/visible3–4tailbars/bristledyellowtoes/hornclawsdarktips retained; adultstandingheights nearequal no5gtoheightclaim. Youngcompactformedfoldedwings/shorttail/eachfoot supported, noairbornepose/nest added. Rightyoungiris/bill/age/flight unknown, existingpendingfooterretained; sciencefalse. PASS_WITH_LIMITATIONS. Rulefoundandapplied: palmarum foreheaddescription permitsfewflecks whiletop/backunspotted, distinctfromsanchezi noforeheadspotrule; actualeditcheckedhereonly. Primaryfulltext403/oldSORAredirectlogged, notcountedasverifiednewsource. New0/reuse2actualIDs.
Applied and visually checked here only; not universal scientific validation.


## 20261127T1826Z 195-otus-brookii-v7
Actualfulloutput plus enlargedcenterbirdcrop viewed. RepeatedbrightU loops reduced to finer tapering wisps; darkfinefreckles and shortstreaksnow read on warmwhitishrufousunderbody, finebrowncrossbarredupperparts retained. Residual longpaleshaftlikefineedges stylized, notmicroscopicplumagevalidation. Bothadults' longwhiteinnertufts/darkcrown/rufousface/orangeyelloweyes/palebills/darkclaws/featheredtarsi/near-equalbodydirection and allbranchcontacts preserved. Youngshortformedfoldedwing unchangednoadultwhitecovertstripe, shorttail/naturalgrips; noage/iris/flightupgrade. Emptycavitynotdocumentedoccupiednest. PASS_WITH_LIMITATIONS/sciencefalse. Lesson130 texturehypothesis applied195 and reducedcoarseUmesh visually, twoexamples notuniversal; biologicalexactbarbmap remainsunverified. Targetedexternaldiscovery repeatedexcludedJavalead, actualmetadata recheckedwithoutadoptingyoungtraits; primaryGooddie printed74 actualbodyread supportsadultnest/environmentonly. New0/reuse2IDs.
Applied and visually checked here only; not universal scientific validation.


## 20261127T1826Z 201-otus-mantananensis-v11
Actualfulloutput and adultbreast/bellycrop viewed. Bothadultslongthickteardropstreaks replaced by finerblackpeppering/broken crosslines, darkerupperbreast retains thinshaftstreaks and palerbellycontrast. Crosslinearrangement remains somewhatregularized/illustrative; notscientificplatepass. Crown/tufts/greyhornbill/yellowiris/darkruff/white scapulars/wingtailbars/near-equalsize/featheredtarsinarrowbarezone/lightgraybrowntoes/darkhornclaws and allfootcontacts preserved. Centralyoungunchanged: buffrestingclosedeyes/formedfoldedwings supported, mixedpopulationadultnominate/youngromblonis plaque and exactunknownfooter retained. Nojuveniletraitsfromadultphototransfer/noinventednest. PASS_WITH_LIMITATIONS, sciencefalse. Evidence book199–200actualpairphoto/text plus independent2023adultphoto actualpixels; latter sex/subspeciesunknown, localitynotautonominateproof. New1/reuse1ID. Lesson feathertract/morph/populationboundariesexplicit; improveadultpepperingonly, youngcurlsnotdeclaredverified. 174 investigatedthenDEFERRED noimage/noextra cyclecredit, no fabricatedtoefeatherdefect.
Applied and visually checked here only; not universal scientific validation.


## 20261127T1931Z 134-megascops-sanctaecatarinae-v13
Fullv12/refphoto/finalv13 actualviewed. Youngbroadwhiteface reduced; brows mutedgray, narrowpaleorbitalfeatherededge arounddarkeye and graybrowncheeksnowcloserprimaryphoto. Finewhitefeatherstips onneckremainillustrative, no microscopiccalibrationclaim. Greenhornopenbill/compacttuftlesshead/faintcrossbars/cavitybody support/concealedwingsfeet maintained. Adultbushyshorttiptufts/coarsebranchedstreaks/whitescapularspots/yellowvsbrowneyes declaredindividualvariation/greenishgraybills/tarsalfeatherstotoebase/lightgraybrowntoes/darkclaws/4securegrips/nearequalscale preserved. ForestAraucaria/cavitydesign notexactnest. PASS_WITH_LIMITATIONS/sciencefalse. Problem overbroadyoungpalemask→actualWA1527488rightyoung narrowfeatherorbit→limitedfacepaletteedit→fullrechecksuccessfulhere. Don'tmerge paleorbit/bareeyelid oryoung/sexattributes; no exactage/flight/nestdetailinvention. New0/reuse3IDs. FreshWikiAvespage403butoriginalphotoaccessible; uploadedguideactual239read.
Applied and visually checked here only; not universal scientific validation.


## 20261127T1931Z 108-otus-rutilus-v9
Actualv8/sourcephoto/newwholetrio/editedfinal allviewed. Initialwholetrio retainedlongtangledcurls despite excludingoldgeneratedyoung. Secondedit reduces strandlength/contrast BUTintroducesexcessivelybroadregular darkhorizontalbellybands compared source'sfine diffusemottle; remainingthinclosedcurl outlines also visible. NEEDS_REVISION, no successfulmaterialorpatterncalibrationclaim. Existingyoungdarkmask/yellowbrowniris/pinklowerlid/darkbill/tuftlesscrown/compactconcealedwinghidden tail/2supportedfeet retained. Adultsnewwholetrio audited ownbrownmorphherringbones/whiteblackedgedscapularline/yelloweyes/graybrownbills/featheredtarsi/graybrowntoes/blackbrownclaws/shorttufts/nearequaldisplay, sixgrips/humidAndasibe forest/nooccupiednest. Unknownage/sex/flightremain. Problem longloops→adult-onlystyle+realphoto/newtriofailed→secondedit shortenedfibers butpatternregressed→recordunresolved notsciencepass. Lesson materialedit can strengthen unsupportedbandcontrast; subsequentprompts must lock lowcontrast/mottledsourcebands; notyetvalidated. New0/reuse2, originalfirstattemptandallpromptsretained.
Applied and visually checked here only; not universal scientific validation.


## 20261127T1931Z 112-asio-abyssinicus-v10
Actualv9/bookpageincludingNoakesphoto/2018Lannelucphoto/outputv10 fullviewed. Adulttoe feathering nowextendsalongtoe tops toclawbases ratherthanlongbarescalysegments, darkhornclawsexposedandallgripsretained. Finefeatherdensitystylized notfieldmeasured. Prominentwhiteadultscapularbuttons muted to irregularbuffflecks; flightbarsremain. Bookwithoutdistinctwhite vsOwlPagesindistinctwhiterow resolvedlowcontrastnotabsence; sourcephotoangle/shadecannotexactcolorcalibrate. Orangeyellowiris/blackbill/longtufts/bodycheckering/barredlongwings/tails/near-equalscale preserved. Centralolderyoungunchangedformedwing/barredtail/2grips/exactageflightunknown. Forestnaturalperch/nooccupiednest. Footerpendingandv10present. PASS_WITH_LIMITATIONS/sciencefalse. Lesson: distinguishscapularpatchcontrastfrombarredflightfeathers, and toeFEATHERSfromclawSHEATH; onlyadultscope appliedverified. No juvenilematerialsuccessclaim thiscycle. New0/reuse3directIDs, additionalMatoncaptionrefreshcontextonly.
Applied and visually checked here only; not universal scientific validation.


## 20261127T1931Z 120-megascops-ingens-v9
Actualv8/book229textphoto/finalv9 fullviewed. Adultbelly coarseblackbranches substantiallythinned, fewer narrowshafts andfinecrossvermiculations read onwarmlighterground; paleedgecrossmarks still stylized notexactphotomapping. Upperbreaststrongermottle/wingtailbars/scapularsmallmarks/shorttufts/honeybrowneyes/subtlepinkrim/oliveyellowbill/featheredtarsi-yellowgraytoes-palehornclaws/nearequalscale/grips preserved. Youngunchanged residualwhitedown/formedbarredremiges/darkface/graybill/eggtooth/supportedfeet; finecurlyyoungmaterialremainsunresolvednotvalidatedthiscycle. Footernowstatesestimatedyoungage/flightunverified/sciencepending, v9correct. PASS_WITH_LIMITATIONS foradultpatternonly/sciencefalse. Lesson: reducecoarseadultshaftwidth withouterasingcontrastrelativecolombianus; no youngmaterialclaimfromadultedit. New2actualreadsourceIDs and2reused; IkiamFig1403 preservedasfailure, nofreshyoungphotopixels.
Applied and visually checked here only; not universal scientific validation.


## 20261127T1931Z 119-megascops-centralis-v10
Actualv9/book242–243text/PiaObergadultphotopage/Jordan2012photopixels/finalv10fullviewed. Bothadultmidlowerfront nowgreyishoffwhitewithfinerirregulardarkvermiculations andsomeunevenshaftmarks; sourcegraybrownmorphdirectionclearer thanoldwarmcoarsestreaks. Warmforestlightstillstylistic/notRGBcalibration; finefeatheredges remainillustrative. Adultweakbrows/plainouterface/blackorbitalring/lemoneyes/greenyellowbill/shorttufts/whitewingcovertpatches/shorttail/pinklowerlegs-paleyellowtoes-hornclaws/nearequalscale/allfeet unchanged. Youngfullformedfoldedwing/graybuffbarreddown/novisibletail/pinkfeet/cavitysillsupport retained, no age/flightupgrade. PASS_WITH_LIMITATIONS adulttractcolorpatternonly/sciencefalse. Lesson applyspeciesmorph-specificgreywhiteground ratherthangenus-wideorangeherringbone, distinguishfinevermiculationsfromheadbrow/eyering; externalAOSoldnamecurrenttaxonomyactualread. New0/reuse3IDs.
Applied and visually checked here only; not universal scientific validation.


## 20261127T1931Z 109-ptilopsis-leucotis-v12
Actualv11/book254textphoto/Helsens2005adultphotopixels/finalv12wholeviewed. Strong clippedorange rimlight/glitterdots removed, barkmatte and featherareas finewispy/subduedgrey-buff, whitishfaceblackruffmorelegible; visuallysubstantialmaterial/readabilityimprovement, notphysicalreflectancescience. Threebirds/ear-tuftshape/faceoutlines/longwingtailpatterns/mainshafts/orangeadultvs yellowyoungirises/hornbills/nearequalscale/sixfeet/perchpositions retained. Fine adultvermiculations nowlowcontrast/unmeasured; exactproximaltoe-featherextent stillnotnewlyvalidated, footernote retained. Youngformedwing/ageunknownstage unchanged, no firstflightchronology. Dryopenwoodlandnotdensewetforest/nooccupiednest. PASS_WITH_LIMITATIONS forlighting/materialONLY, entirebiology sciencefalse. Lesson: lightingandmattefeatherrequest canreduceglossycarvedtilelook for109, independentcase notuniversal featherplumagefix; don'tclaimv12finepattern/agepassed. New1same-speciesadultphotorecord/reuse2; originalphoto notrepublished, titlev12correct.
Applied and visually checked here only; not universal scientific validation.


## 20261127T2003Z 108-otus-rutilus-v10
Actual full image viewed against v9 and Vassen field photo. Broad repetitive dark belly rings visibly removed; surface now fine irregular brown shading. Adult IDs/yellow eyes/scapular white-black marks/gray-brown bare toes/dark claws retained, male/female near equal height. Juvenile dark mask/pink lower lid/closed concealed wings/no tufts, both feet grip continuous branch; no nest/mature flight pose. However numerous small looping hairlike filaments persist and exceed photo's short granular feather texture; this defect remains NEEDS_REVISION. The bounded tonal edit worked but did not solve material identity, so no scientific pass or completed-species increment. Header v10 correct. Lesson: target color-pattern separately from fiber geometry, don't claim successful biological calibration when only stripe contrast fixed.
Applied and visually checked here only; not universal scientific validation.


## 20261127T2003Z 47-strix-leptogrammica-v9
Actually viewed initial enlarged corrected detail, final wholeplate and enlarged final left adult toe crop. Both adult distal shafts now bluishgrey rather than pink; dull lead-grey curved claws remain bare, feet retain branch contact. Basal feather fringes visible but final wholeplate softens microbarbs; no quantitative phalanx proportion verified. Original diagnosis refined: v8 already had basal barbs, so this is chiefly shaft-colour correction, not first addition of feathering. Two-stage imagegen workflow applied and colour improvement visually confirmed for this plate only. Dark adult eyes/greenhorn bills/bluegrey cere/white throat/rufous pectorals/barred belly retained; young source-stage34-day cavity support remains, not claimed exact reconstruction or measured age. Female display on different perch remains uncalibrated despite guide female larger; no science pass. No novel nest construction assertion. v9 title correct, prior versions/confirmations retained. PWL for bounded colour fix; fine anatomical boundary/sex-size/juvenile exact stage still pending.
Applied and visually checked here only; not universal scientific validation.


## 20261127T2003Z 130-megascops-koepckeae-v17
Actually viewed v16 whole/croppedyoung/primaryFig1c/corrected enlarged detail and final fullv17. Large bright U/scallop edges reduced substantially at wholeplate scale, but fine filaments still curl and dark pigment stripes regularized; NOT full biological material repair. Reclassify latest as NEEDS_REVISION rather than imply PWL means material calibrated. Young compact formed dark foldedwing/no white adultshoulderline/whitebrow/darkruff/yelloweyes/bluegraybill/twofirmbranchgrips retained. Adults shorttufts/shaftstreaks/scapularline/graybrowntoes/darkclaws/near-equalscale preserved; exact regionalfamily/subspecies notasserted, no nest/prey/new age. v17correct. Crop→imagegenintegration does carry coarse texture change into wholeplate here, but does not solve fine feathergeometry; method notuniversallyvalidated. This is a documented negative/partial production experiment, not new species nor scientificpass.
Applied and visually checked here only; not universal scientific validation.


## 20261127T2003Z 112-asio-abyssinicus-v11
Actual first/finalfullimages compared with v10 and actualMatonfieldphoto. Firstedit increased woolcurls; secondedit reduced obvious heavyfibercontrast but thin closedcurl/loop patterns persist and source has finer irregular diffuse down. NEEDS_REVISION; no verified successfulmaterialrepair or sciencepass. Developed long foldedwing and barredtail belowbranch retained, pale crownpatch/darkmask/orangeiris/blackbill/olderstage kept. Adults fullyfeatheredtoes/darkhornclaws/tufts/barredlongwingtail/mutedscapulars/yelloworangeeyes and sixbranchcontacts unchanged in scope. No newbornregression, no occupiednest or exactage/flightinference. Titlev11/footerunverified retained. Lesson direct wholeplate 'shorter no curls' instruction stillfailsfinegeometry after2calls; stop calling thisvalidatedtexturestrategy. Preserve negativefirstattempt and bothfullprompts. This is reviewed experiment archival only, notnew completedspecies.
Applied and visually checked here only; not universal scientific validation.


## 20261127T2003Z 206-glaucidium-castanopterum-v6
Actually viewed v5wholeplate/Veronesirealphoto/newv6wholeplate. Bothadult crowns now fine horizontal slightlywavy ochre/darkbrown lines; tall pointed chevron-shingle units reduced. Lines stillregularillustrative and browedges remain raised; not exactcolor/densitycalibration. White scapularlines/chestnutupperparts+sidechest/whitecentralbelly/finebarredthroat/yellowiris/greenyellowbill/olivecere/olivebristledtoes/darkclaws and visiblemale tailbars retained. Adultnear-equalheight retained since nosexsize data, no genericfemaleenlargement. Threebirds/allfeetstableonbranch, roundno-tuftheads; rightdullfledgling unchanged nojuvenilepatterntransfer/newbornregression. Age/iris/bill/sexsizeunknown notices and scientificpendingfooter/v6clear. PASS_WITH_LIMITATIONS for bounded adultcrown correction only; younggeometry and allbiology stillpending. Lesson distinguish pigmentbars fromraised featheredge geometry; actualappliedvisuallyusefulhere notspecieswide rule.
Applied and visually checked here only; not universal scientific validation.


## 20261127T2003Z 201-otus-mantananensis-v12
Actually viewed v11 full/enlargedyoung/actualPhotoArk7282bytepreview and generatedv12full. Thickbright V/U ribbonedges visibly reduced to softer finerdown/brownmottle, but numerous fineclosedcurlthreads persist onhead/body. NEEDS_REVISION for material identity; no full repair or scientificpass claimed. Lowrespreview cannot validate fineplumage geometry, exactbill/iris/flightstage; sourcestillcoarseonly. Sleepingclosedeyes retained as illustrative restingpose, notobservedbehaviour. Bothadults finepepperedbelly/darkerupperbreast/whitescapulars/yelloweyes/greyhornbill/narrowbaretarsalzone/lightgraybrowntoes/darkclaws andnear-equalscale retained. Centralformedfoldedwings andsupportedtwofeet unchanged, allsixcontactscontinueonbranch, no nest. Mixednominateadult/romblonisyoungwarning andpendingfooter/titlev12clear. Lesson grossedgecontrastcanreducewhilefinecurlgeometryremains; do not repeat same prompts calling itvalidatedaviansanddown. Priorv9/v11 andallconfirmationrecords remain. New0/reuse2/no independentsecondyoung evidence.
Applied and visually checked here only; not universal scientific validation.


## 20261127T2003Z 108-otus-rutilus-v11
Actualv10/photo/isolatedstudy/finalv11 viewed. Juvenile-only photo-conditioning followed by integration gives muchfiner lessoutlinedbrownfuzzyvolume thanv10; repeatedlargeclosedcurlunits diminished and no broadregularbellyrings. Finefilaments remain somewhatcurled/longerthanfieldphoto, no exactmicrostructurecalibration. PASS_WITH_LIMITATIONS for reducedcoarseloopscale only, not scientificallyverified. Compactovalyoung/darkmask/pinklowerlid/yellowbrowniris/darkbill/noeartufts/concealedfoldedwings/hiddentail/twofootbranchgrip kept; originalphoto age/sex/flightunknown. Bothadults retain brownmorphherringbone/scapularline/yellowiris/graybrownbills/tarsifeathers/baregraybrowntoes/darkclaws/near-equalscale; sixfootcontacts onsolidbranch, humidAndasibeforest/nooccupiednest. v11/unknownfooter present. Lesson only-sourcejuvenilestudy+integration visually reducescoarseunitartifacts here, finegeometrystillunresolved; not universalvalidatedmethod. Preflight enumeratedALL108versions numerically, v11new. Replaces invalidated47cycle, notextra duplicate credit.
Applied and visually checked here only; not universal scientific validation.


## 20261127T2003Z final versioncollision audit
Actual failure: selected47v8 without enumeratingv9–v13; restoredoldv9exactbaselineandrevokedcredit. Implementedcorrectivecheck: ALLnumericversionsenumeratedfor108replacement; fullbaselineimageblobdiff finaloldchanged0. MustapplyALLversionpreflightbefore EVERY target; do not claim preventativefutureefficacy fromthissinglecheck. Invalid47experiment isnot newmorphologicalcorrection. Do notinterpret materialnegativearchive as sciencepass.


## 20261127T2127Z 130-megascops-koepckeae-v18
Actualv17/photo/initialv18/finalv18wholeplates viewed. Bothfirst andsecondedit retain manyfineclosedcurl/U-shaped threads; secondeditsoftenssomecontrast but no defensible microgeometryrepair, NEEDS_REVISION. Adults slightdetailsoftening occurred; keyshorttufts/yelloweyes/bluegreenbill/broadbranchedshaftstreaks/scapularline/baregraybrowntoes/darkclaws remain. Younggraywhitebars/brownchest/whitebrows/blackfaceedge/compactformedfoldedwing/hidden shorttail/twofeetbranchsupport retained. No newbornregression, nest/prey/newage/subspeciesmatch inferred. v18/footer pendinglegible. Primaryphoto/downpattern supportsstillpending; no sciencepass/newspeciescredit. Repeatedfailurecause model converts downinstruction tocurledhair evenwhennegativeprompt explicitlyforbidsit; shortening/softeningwording notvalidatedsolution. Keep bothattempts andcompleteprompts, nextrepair should require differentvisuallydemonstratedmaterialstrategy ratherthanrelabelling. Comparison limited to morphology visible, exactsexheight/age/flightunknown.
Method applied and checked here only, no universal scientific validation.


## 20261127T2127Z 136-megascops-petersoni-v8
Actualv7/newv8wholeplate viewed. Newscientificpending/firstyearreference/exactage-flight-sexratiounverifiedfooterlegible withinparchment, v8visible; no overlapwithfeet. Threebirds/roles FIRST-YEARpreserved, formedfirstyearwings/tail/palehornclaws/pinktoes/darkeyes/warmbuffbrows/cinnamonbody/nearequaladults/6supportedgrips/cloudforest remainqualitatively. No claimpixelidentity or morphologyimprovement. AnnotationonlyPWL/sciencefalse. Sourceprimaryfirstyearnearlyadultplumage notnataldown; new2022nest/eggfactsindexed but NOT depicted orusedtovalidateyoung. Unknownpreciseage/irisdevelopment/flight/sexratio andfinecolourcontrastremain. Lesson exportedimage mustcarrysciencependingstatus; actuallyapplied/readablehere, notnewscientificvalidation.
Method applied and checked here only, no universal scientific validation.
