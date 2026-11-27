

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
