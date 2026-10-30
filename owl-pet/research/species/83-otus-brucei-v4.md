# #83 *Otus brucei* v4 research and design boundary

- Run: `20261031T043000+0800-cycle-1`
- Accessed: 2026-10-31
- Action: SCIENCE_REVISION; v1–v3 preserved.
- Stage: RESEARCH_READY
- Source delta: new 1 / reused 2 / corrected 2.
- Scientific status: pending; `scientifically_verified=false`.

## Sources actually read

### BRU-BENDOV-KIAT2016 — reused, URL corrected

- Amir Ben Dov & Yosef Kiat, “Breeding Pallid Scops Owls in Rift valley, Israel, in spring 2015”, *Dutch Birding* 38:146–158 (2016).
- Official journal PDF actually opened: https://www.dutchbirding.nl/journal/pdf/DB_2016_38_3.pdf
- Author-uploaded full text actually read: https://www.researchgate.net/publication/305657832_Breeding_Pallid_Scops_Owls_in_Rift_valley_Israel_in_spring_2015
- Printed pp.151–152: all studied nests were cavities in mature date-palm trunks, generally 2–3 m below the canopy; fledging reported at about 26 days for the studied population. Plates 234–236 show the nest cavity, a fallen juvenile and nestlings.
- Printed pp.156–157 / plate 243: young pale sandy-grey, deep-yellow iris, pale eyebrow, fine horizontal bars on forehead/chest/belly and feathering on the upperside of the middle toe.
- Limits: small Israel sample; birds described as intermediate between named forms; exact individual age in the v3 plate cannot be inferred from appearance. “About 26 days” is a population/study statement, not an exact label for one generated bird.

### BRU-MIK2013-126 — reused, PDF pages directly read

- Heimo Mikkola, *Owls of the World: A Photographic Guide* (2013), printed pp.126–127 / uploaded PDF pp.128–129.
- Species/stage: *Otus brucei* adults and juvenile development.
- Facts: L 18–22 cm, mass 90–130 g; female stated at least 15 g heavier, but no standing-height ratio; pale yellow eyes, dark greyish-horn bill, fine blackish shaft-streaks, pale grey/ochre ground, subtle scapular row and tarsal feathering to basal toes. At two weeks mesoptile has adult-like feathers and ear tufts; at three weeks facial disc is forming and colour becomes transversely striped.
- Geographic limitation: named forms and their validity are uncertain; Israel birds combine pale exiguus-type colour and obsoletus-like size.
- Design use: adult identity and a feathered, forming-disc juvenile boundary. Mass cannot be converted into a visible crown-height ratio. The book does not assign the generated individual an exact age.

### BRU-CHANDRAN-2016 — new

- Abhinand Chandran, Pamela C. Rasmussen, Shah Jahan & Praveen J., “The Pallid Scops Owl *Otus brucei* in south-western India, with notes on its identification”, *Indian BIRDS* 12(2&3):56–63 (2016).
- Author-uploaded full text actually read: https://www.researchgate.net/publication/309011014_The_Pallid_Scops_Owl_Otus_brucei_in_south-western_India_with_notes_on_its_identification
- Printed pp.56–63; Table 1 and plates 69–76.
- Evidence base: 30 Pallid Scops specimens in UMMZ, 16 in NHMUK, comparative series, plus ~150 field photographs.
- Useful adult facts: uniformly pale grey with little/no rufous; plain pale facial disc; long thin upperpart streaks rather than broad blotches; weak narrow underpart crossbars; yellow-buff scapulars with narrow black tips; less-contrasting buff primary bands.
- Limits/conflicts: authors explicitly warn that underpart crossbars vary and that tarsal/toe feathering can be difficult or equivocal in the field; the paper is about adult identification, not daily juvenile feather chronology.

## v3 actual inspection

Fixed v3 `83-otus-brucei-v3.jpg` at commit `5c452e18d3858353f583ca6d9ac33f9b8a5623fc` was reopened at original resolution.

- Pass: exact title/name, three birds, pale sandy-grey adult identity, fine shaft streaking, date-palm cavity, juvenile horizontal bars, deep-yellow iris, bilateral support.
- Problem 1: the label `c. 26-DAY FRESH FLEDGLING` converts approximate population-level fledging into an exact individual age.
- Problem 2: the juvenile folded wing remains long and regularly layered enough to read as adult-like.
- Problem 3: adult support/perspective makes the male visibly larger, while the evidence only gives a mass direction and no standing-height ratio.
- Correction: use `RECENT FLEDGLING`; compact and soften the juvenile folded wing; align adult support/baselines and keep near-equal crown height, with at most subtle female fullness.
- Unknown: exact age, exact first-flight threshold, daily tract geometry, individual subspecies and sexed standing-height ratio.

## Full imagegen edit prompt

```text
Edit the supplied fixed v3 comparison plate into v4 while preserving the established warm, highly realistic photographic owl-pet concept style, 3:2 landscape composition, date-palm trunk cavity at sunset, exact species identity, and exactly three birds.

KEEP:
- Title at top: "PALLID SCOPS OWL" and italic scientific name "Otus brucei".
- Left adult male, center juvenile, right adult female; all birds fully visible, naturally supported, no extra birds or body parts.
- Pale sandy-grey Pallid Scops identity; pale yellow adult irises; dark grey-horn bills; fine long dark shaft-streaks rather than coarse blotches; small ear tufts; subtle buff-grey scapular line; barred remiges and tails.
- Center bird at the natural lip/floor of a mature date-palm trunk cavity, with both feet visibly and anatomically supported. Preserve the dark internal recess and fibrous palm context.
- High-resolution natural plumage detail and quiet desert/date-palm setting.

CHANGE ONLY THESE SCIENCE-CALIBRATION POINTS:
1. Replace the bottom center label "c. 26-DAY FRESH FLEDGLING" with exactly "RECENT FLEDGLING". Do not state an exact day.
2. Make the center fledgling clearly juvenile but not neonatal: pale sandy-grey and slightly woolly; forming facial disc; pale eyebrow; deep yellow iris; fine horizontal bars across forehead, chest and belly.
3. Correct the juvenile wing so it is a compact, fresh, softly edged folded wing: shorter and rounder than either adult wing, with irregular narrow juvenile bars; no long adult-like layered primary panel, no repeated bright white spot rows, and a visibly short tail. It must remain fully supported and not be flying.
4. Place adult male and adult female on support stumps at closely comparable baseline and perspective, with near-equal visible crown height. The female may look only subtly fuller-bodied, not conspicuously taller. Do not invent a fixed size ratio.
5. Keep tarsal feathering subtle; do not turn toe feathering into an exaggerated field mark.

DO NOT:
- change the number, sex labels, title, scientific name, cavity substrate, or overall lighting;
- add rufous body tones, bold white scapular patches, bark-like blotches, bare unsupported feet, human objects, graphic frames, or labels other than the specified title/name/three bottom labels;
- render mature adult wing geometry on the juvenile.

The result is a scientific-calibration concept, not a claim of subspecies, exact day, exact flight threshold, or confirmed sex-height ratio.
```

## Planned assets

- `owl-pet/design/concepts/83-otus-brucei-v4.jpg`
- `owl-pet/production/generated/83-otus-brucei-v4-generated-master.jpg`
- `owl-pet/production/reviewed/83-otus-brucei-v4-reviewed-master.jpg`
- `owl-pet/production/review-crops/83-otus-brucei-v4-juvenile.jpg`


## Actual generation, edit and review

- First v4 imagegen edit: 30.7 s. Full 1536×1024 original opened. Title/name/count, adult identity, date-palm cavity, corrected RECENT FLEDGLING label, adult support and near-equal crown height passed; the juvenile wing remained long with repeated pale rows.
- Targeted juvenile-wing edit: 52.4 s. Full edited master, 520×700 juvenile crop and 680×453 derivative opened.
- PASS: exactly three birds and exact labels; adults pale sandy-grey with fine long streaks; center fledgling has deep-yellow iris, pale eyebrow, fine horizontal bars, compact soft folded wing, short hidden tail and bilateral cavity-lip support; no flight pose.
- Result: PASS_WITH_LIMITATIONS; edit_count 1. Exact individual age, daily tract geometry, first-flight threshold, subspecies and sexed standing-height ratio remain unknown. Science false.
- Assets: concept SHA-256 `9ad1b557860591d62238ddb128aba6e62a70b0bf410f62051cf182a98c84235e`; generated `53903199acb19656c8a91071bc8df2fcf876c74d1a3da5fee73ae2336be6b52a`; reviewed `afa8a75a6e232ed529cba71be812f8764149a373777ededf01f47371ca95b38b`; crop `5503c744901b78a77e565b61aa67719249a67af202e99de9506aa2ca4ea7701c`.


## Fixed archive verification

At 2026-10-31T04:49:30+08:00, immutable commit `4d52a675ded909e923b8d2ce7e43bb0bb4971907` was reread. Concept, generated master, reviewed master and juvenile crop matched local base64 exactly; Git blobs and sizes matched; tree was non-truncated (2,201 entries); manifests were 587/586/577; support records matched. Result VERIFIED for archive integrity, not scientific verification.
