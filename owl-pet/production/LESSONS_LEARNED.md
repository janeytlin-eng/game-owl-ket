## 2026-11-07 — #148 *Ninox rumseyi* v3: sex direction and brow length must be independently constrained

## 2026-11-07 — behaviour evidence is not an age clock

- **Problem:** a source can document a juvenile flying or begging without supplying hatch date, molt sequence or first-flight threshold.
- **Evidence:** Lok et al. (2009) directly record mobile, begging Hillview juveniles but explicitly do not establish exact age; Mees (2006) gives only a population-level marginal adult sex-size comparison outside Singapore.
- **Applied:** #190 v2 labels the bird AGE-UNKNOWN JUVENILE, gives full branch support, and keeps adults near-equal.
- **Validated:** full plate and both crops passed the targeted checks; this validates the prompt constraint for this plate only, not a universal species-development rule.


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


## 2026-11-07 — #174 *Strix sartorii* v3 — toe feathering must reach the claw base
- **Problem found:** the first render preserved feathered tarsi but left most toe surfaces visually bare.
- **Evidence:** the directly read 2015 field account describes toe feathering extending to the bases of the claws; the edited crop makes that feature checkable without hiding grip or claws.
- **Rule derived:** when a source specifies feathered toes, prompt the full toe-to-claw-base extent separately from tarsal feathering, while requiring exposed claws and explicit branch support.
- **Applied:** one targeted edit to all three #174 birds.
- **Verified:** the reopened adult and fledgling crops show short dense toe feathering reaching the claw bases, visible dark claws and firm bilateral support. Verified for #174 v3 only; other Strix plates require source-specific recheck.

## 2026-11-07 — Separate stage evidence from nest-location evidence

- **Discovery:** a reliable fledgling record does not by itself establish nest location, cavity form, substrate or clutch details; Cameron (2002) records Sokoke Scops Owl fledglings while the dedicated 2001 search still failed to locate a nest.
- **Rule:** treat life-stage evidence and nest-site evidence as independent gates. A fledgling may be shown when its observable stage is supported, but nest/cavity/egg details require separate direct evidence.
- **Applied:** #175 *Otus ireneae* v3 uses an age-unknown supported fledgling and omits nest, cavity and eggs.
- **Verified:** visually effective for #175 v3; not yet validated across earlier plates.


## 2026-11-07 — #188 *Otus semitorques* v3 — recent-fledgling evidence does not license mature remiges
- **Problem found:** the first image matched the down-rich fledgling body but exposed a long, layered wing that read as adult flight plumage.
- **Evidence:** Nohara & Honda (2025) describe/figure a recently fledged juvenile with the entire body covered in down, little movement, and incomplete flight and tail feathers; exact day-age, iris, first-flight ability and feather sequence remain unknown.
- **Rule derived:** when direct evidence says incomplete flight feathers, require a compact wing mostly buried in down with only short developing feather tips; forbid a long layered remex fan even if the face and ear tufts look developed.
- **Applied:** one localized edit to #188 v3; adults, text, forest and support were locked.
- **Verified effect:** the reopened full plate and juvenile crop show a shorter soft wing, down-dominant contour and complete branch support. Verified for #188 v3 only; earlier recent-fledgling plates need source-specific recheck.


## 2026-11-24 — 0112Z六轮实证增量与优先队列

- **成鸟腹纹不是通用长黑纵纹模板。** #184台湾机构/图鉴148与#190NParks分别支持细横纹/小斑、淡短纵纹；两图实际imagegen修订并放大复查已应用。它们的目标纹理不同；#195仍保留其图鉴168支持的较粗不规则暗纹，不全库自动淡化。两例有局部修正证据，不代表全物种规则已验证。
- **虹膜按种/地域/阶段核对。** #188本州直接论文p76橙眼，定向修正后已放大复查；#184台湾黄眼保留；两种均未把成年虹膜套给幼鸟。不能从一次配色修订推断全局科学准确。
- **已观察飞行与首飞日龄是两件事。** #190 Lok2009行为段是p38/PDF8，明确一幼鸟飞到亲鸟枝上；旧p37/仅移动说法已在新记录纠正。已有完整飞羽的较大幼鸟不可因'young'标签被强制改成无羽绒球。此图保留支持充分的站枝/乞食，未新画飞行动作。
- **幼鸟羽色必须分区。** #197图鉴170明确下腹/腿羽比头胸浅，实际改图并放大复查；回看#195图鉴168为另一种红褐中间羽期，不自动套浅腹模板。#197具体羽序/虹膜仍未知。
- **跨亚种参考要直接可见；未知不因归档消失。** #201原v3藏在文档中的nominate成人/romblonis幼鸟参考现在写进原图；成年窄裸跗蹠带依图鉴199修正并看图。幼鸟羽被仍PRIORITY_UNRESOLVED，PhotoArk原始caption可读但图片403，当前不得据此科学通过。下一生产优先查可实际看清并定位年龄/地域的幼鸟实物资料；如无证据，保留未知并处理其它资料明确项目。
- #195本轮仅改年龄未知中间羽期/校准标识，明确不是形态发现。#201版权页2025不作拍摄年份。原始文献页码/引文不足以补出幼鸟的腿/翅/巢结构。
- 缺失种Palawan O.fuliginosus：原始Sharpe1888p197诊断OCR实际读到，未写年龄；类型为幼鸟的搜索说法未核验。保持研究待办，[缺口记录](../research/species/otus-fuliginosus-20261124-evidence-gap.md)，不计物种完成。
- **归档运行恢复已实际应用。** 第6轮functions临时store丢失，保留在磁盘的同一PNG通过分块读取恢复，检查截断/完整长度后上传；不可把重建临时变量算作重画/新图。远端不可变提交原图解码+SHA256验证通过，未取得平台超时遥测。原图checkpoint/最终版均在GitHub，不把scratch当持久保存。
- 复查和局限逐物种见[本批六轮入口](batches/20261124T0112Z-completed-review.md)。这不是全251种整批最终科学审查。


## 2026-11-25 — actual cycles5–6 resumed / local morphology and source traps
- #73v6: guidep448 proximaltoe feather boundary omitted from oldprompt. Fine adult proximaltoe feathers added; distalbare scales/claws remain; full+footcrop actually viewed. Applied/visually verified for oneplate, primary-photo corroboration stillunknown. No globalNinox rule. #63fullviewbaretarsi/toesalreadycorrect, #96guidep446 sparsebristlescorrect, #93fullviewbaretoescorrect; do not generalize by genus.
- #97v6: genericbarredtail caused wide brightregularbands. Wetmorep158–159 specifies narrowbars, lesscentral/tip; guidep358 fine mottling not permission to remove ventralbars. V6thin/subduedbars full+comparisoncrop actuallychecked. Width remainsqualitativedesignchoice; no broadsciencepass.
- Existing sourceURLs must be title/pagechecked: HAR-UBAID-ETAL-2012-BHL /40855939 actuallyresolves1931–34SouthAfricanMuseum, not2012BBOC. QuarantinecitationURL pendingcorrectcopy, preservehistory. A searchhit/audiolabel/thumbnail/placeholder is not readphoto. M.Dahlem205bytecaptcha rejected; RiddelllocalPDF403 althoughwebbodyread works. No screenshot-pixel claim.
- Screening Otusbeccarii actual2023account+guidep193 stillgave noyoungappearance, existing#224hasaudioonly/unresolvedtaxonomy; no new species manufactured. Unverified searchleads not sourcecounts. Researchnoimage doesnotcreditcycle. Related actual [#73](../research/reviews/73-ninox-rufa-v6-review.md) / [#97](../research/reviews/97-lophostrix-cristata-v6-review.md).


## 2026-11-25 #112v5 — validate requested net morphology in output
Priorv4netpromptdidnotproduce primarysupportedwidecrossbars, fullbeforecrop longshafts. CollarBoesman2019p158 actualread; v5adultbellyonly edit explicitlybroadtransversecomponents, cropvisuallyvalidated. No universalAsionet/sexratio. JuvenileNOTinferredfromguide'sspeculativeAsiootuscomparison; retainedpriorphoto-derivedageunknownstage. Sourceaswritten and source-to-output checking are separategates. Onecaseappliednotglobalvalidation. [Review](../research/reviews/112-asio-abyssinicus-v5-review.md).

## 2026-11-25 #110v6 — separate adult toe hue from juvenile unknowns
Actualv5 fullview grey adultnakedtoes. Guidep214+freshobserverDescription both pink, adult-only edit andfull/cropview confirm change withsupportretained. Do not tintjuveniletoes byadultaccount, or turn+9gmass intoheight. Audit found several apparentissues alreadyvalid (#104featheredfeet,#103latefluff,#120youngremiges); rejected fixes. Recovered#93Ubaidpaper correcttitle/URL/fullPDFandFigure2, notjuvenileageproof. Onecaseapplied; not allMegascopscalibrated.

##2026-11-25 #132v6 — actual bytes, not repeated success claims
Latestv5 anditsoriginalcopies786444bytes repeatedlyfailedPILdecode; preservehistory/quarantine, cannotcallvalidjustbecauseoldreviewPASS. Validv4+fresh2014originalFig11 allowednewv6 reconstruction. FullnewPNGmustdownload/hash/decodebeforecredit. Tailcentralupperversusventralbars distinguished, blanketbarremovalrejected. Requestedminorheadturnsubtleonly, notpromotedtoscientificcorrection. Stage4weekboxversus5weekbranchphotoexplicitlyseparate. Onecasearchivevalidation, entirelibrarynotyetdecodedaudited.

##2026-11-25 95-pulsatrix-melanota-v6
Corrupt oldv5 pluscopies notvaliddespitehistoricalPASS. Prefixscan foundno recoverableoriginal. Rebuildfromvalidpriorversionwith actualprimarydevelopmentboundary; explicitcrownwhite+firstchestfeathersandsoftshortwingcheckedonoutput. Do notlabelgroundfoundolderyoungasactualnestchick. Adultfemale-heightnotassumedfromunsexedweights. Oneappliedcase, notglobalvalidation.

##2026-11-25 139-otus-jolandae-v6
Comparison-specific absence of broadsidebars/diamonds doesnotmean removeshafts. Firstpromptpriorv5 insufficienteffect checkedactualcrop; v6narrowedlateralcomponentsvisually. Repetitionremainsnotclaimscientificpass. Originalolderimmaturetype supportsfeatherremnants nothatchage, preservevalidformedwings. #138textaloneinsufficienttodenycoverts, rejected speculativeedit.

##2026-11-25 140-otus-rufescens-v7
Do not normalize every Otus into streakedgenericowl: rufescens explicitventralspotsversusjolandaeshafts+finebars. Zoneboundarymatters: adultflightfeatherbars remainlegitimate, andv7didnoterasewingpattern. Guidebodyyellowishtoes/captionwhitish variation not groundsfornewrecolour; rejectedfalsefix. Youngvalidmesoptile retained noadultpatterntransfer. Outputfull+cropverifyshowsdirectionimproved, literalspotmapnotvalidated.

##2026-11-25 128-megascops-marshalli-v9
Tract-specificcolourchangeavoidsblanketerasinglegitimatewhiteshoulder. Observedv8irisalreadydarkbrownandprimarybellyvariationrejectedtwofalsefixes. Do notimposeeighttailbarsonolderjuvenile ornewbornbuds. v9lowerwingdirection visuallycheckedonecase, notglobalcalibration.

##2026-11-25 201-otus-mantananensis-v7
Finepatternnotwholesaleabsenceofwhite: sourcecaptionveryfinepatternandactualboundedphotoreference. Editreducedflecksizebutlightenedcrownbackground, remainingtonalcalibrationexplicit; don'tcallsciencepass. Preservewhiteeyebrows/scapularband. #201bellyand#206bristlesalreadycorrectedso avoidrepeatfixes; preserveexistingyoungpopulationwarning.

##2026-11-25 137-otus-alfredi-v7
Generic darktalonprior leakeddespiteyellowfeet. Checkclawsasindependentbarepart; sourceTable2explicitlycoversbothadultandyoungratherthanguessingagecolour. Validpalevermiculationforeheadandfineventralrufousbarsremain, no falseplain-crownfix. Actualfeetstripconfirmscolourdirectiononecase.

##2026-11-25 130-megascops-koepckeae-v6
#130: apply adult eyebrow criterion only to adults. Primary juvenile white brows are independently documented. Preserve legitimate pale face margins and do not transfer hockingi painting palette to unassigned Loja birds. This edit visibly reduces adult white-band contrast; broad scientific validity unverified.

##2026-11-25 136-megascops-petersoni-v7
#136 species-specific pale details: distinguish warm buff eyebrow from white, and pale horn claw from #137 orange-yellow claw. Both primary and guide checked independently. Actual revision visually achieved warm brows/pale claws; do not extrapolate to other owl species or erase valid variable belly shaft/crossbar pattern.

##2026-11-25 #201v8 recovery
Preservedoriginal bytes/hash afterinterruption; reviewedfull/crop beforecredit. Modestcrownrebalance retainedfinepattern, validwhitebrows andmixedpopulationwarning. Greyishmorphvariationmeansnevercallqualitativetoneapprovalscientificcolourvalidation. Actualappliedviewpasswithlimits; no additionalimagegen necessary forrecoverable IMAGE_GENERATED.

##2026-11-25 135-otus-silvicola-v7
Guidecriterion limitedtoeartract; retainedvalidwhitefacebrows. Actualtarget achievedwhileprotectingprimarysupported fullyfeatheredimmature. Don'trepaintallpaleplumageorborrowthisrestrictionforotherowls.

##2026-11-25 134-megascops-sanctaecatarinae-v6
#134 actualphysicalphoto accessedagain: densefinefeathers notgenericlongcurlywool. Correction visiblyshortenedtexture andremovedunsupportedOLDERlabel. Keepunknownhiddenanatomyconcealed andrecordimprovisednestcontext; futurecavityscenesmustnotclaimliteralnaturalnestreconstruction.

##2026-11-25 131-megascops-watsonii-v6
#131 annotation makesgeographicscopevisible. Actualtextpass; modelcollateralminorpostureandtonechangesneedexplicitdisclosure, notclaimpixelpreservation. Supportedanatomyretainedqualitatively, noextra biologicalclaim. SACCfreshfindtimeoutdoesnoteraseearliersuccessfulread; logbothoutcomes.
