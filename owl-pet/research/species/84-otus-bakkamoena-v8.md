# #84 *Otus bakkamoena* v8 research, archive repair and design boundary

- Run: `20261031T045100+0800-cycle-2`
- Accessed: 2026-10-31
- Action: SCIENCE_REVISION / archive-integrity repair; v1–v7 preserved.
- Stage: RESEARCH_READY
- Source delta: new 0 / reused 2 / corrected 2.
- Scientific status: `scientifically_verified=false`.

## Sources actually read

### BAK-BRRAICH-SINGH2021 — reused, publisher PDF freshly opened

- Onkar Singh Brraich & Jagdeep Singh, “An Indian Scops Owl *Otus bakkamoena* breeding in an artificial wooden nest box”, *Indian BIRDS* 17(2):55–56 (published 28 May 2021).
- Publisher PDF: https://indianbirds.in/pdfs/IB_17_2_Brraich_Singh_IndianScopsOwl.pdf
- Printed p.55: the box was occupied on 23 April; two juveniles seen on 2 July were grey with dark-brown horizontal belly bars, lacked plumage around the eyes and ear tufts, had grey bills/exposed nostrils, blue eyes and underdeveloped wings.
- Printed p.56: one chick fell on 13 July and survived rehabilitation; the other was seen flying near the nest on 8 September.
- Limits: single nest and brood; no hatch dates, daily tract sequence, universal iris transition or exact individual age. The artificial box is an observed nest substrate but does not require the concept to depict manufactured hardware.

### BAK-MIK2013-150 — reused, uploaded PDF pages directly read

- Heimo Mikkola, *Owls of the World: A Photographic Guide* (2013), printed pp.150–151 / uploaded PDF pp.152–153.
- Facts: adults 20–22 cm, 125–152 g; female described as clearly larger and slightly heavier, but no standing-height ratio; long dark-edged tufts, two nuchal collars, hazel/dark-brown eyes, greenish horn-brown bill/dusky-green cere, pale grey-brown facial disc with blackish ruff, tarsal feathering to toe bases. Juvenile mesoptile pale grey or warm reddish-yellow with fine dusky-brown bars also across face/chin.
- Limits: named forms and taxonomy; no individual juvenile age, first-flight threshold or eye-colour transition.

## Active research exclusion

Searches also surfaced developmental dates under older broad Russian usage of `Otus bakkamoena`. Those records refer to the northern collared/Japanese complex under historical taxonomy and are not transferred to current Indian *O. bakkamoena*. They are a lead only, not a verified design source for v8.

## Prior-image and archive inspection

- Current manifest preferred v7 points to fixed commit `7f6f352543a09a100106f1fa395cb30d000323ba` / blob `92a18d2ab3fa2ef4d91dd9b3a9cbf92bbb5133a8`.
- The v7 PNG bytes were fetched from the immutable raw URL. Header/dimensions read as 1536×1024, but full decode failed with `IDAT: invalid distance code`; it cannot serve as a recoverable visual master. The prior scientific status remains false and the historical file is preserved.
- Complete v6 at fixed commit `23efe6f2787571e8e4ac106072eb01abe63b3956` was fetched, decoded and opened at 1536×1024.
- V6 pass: exact number/title, three supported birds, dark-eyed tufted adults, blue-grey-eyed grey-billed untufted juvenile, natural cavity and horizontal juvenile bars.
- V6 problems to correct in rebuild: adult faces still read as concentric eye rings rather than one continuous disc; juvenile underdeveloped wing should be explicit; female direction should be modest and not a fixed ratio.
- V8 is a full rebuild from complete v6, not an edit of the corrupted v7 payload.

## Full imagegen prompt

```text
Rebuild the supplied complete #84 Indian Scops Owl v6 plate into a clean, complete, scientifically bounded v8 master in the same established photorealistic owl-pet comparison style, 3:2 landscape. Preserve the warm woodland, natural mature-tree cavity, exact three-bird comparison, and repository numbering.

TEXT — exact:
- Top title: "84 INDIAN SCOPS OWL · Otus bakkamoena"
- Bottom labels: left "ADULT MALE", center "JUVENILE", right "ADULT FEMALE"
No other words.

ADULTS:
- Indian Scops Owl adults, grey-brown morph: conspicuous long ear tufts with dark outer margins; hazel-brown to dark-brown irises; greenish horn-brown bill and dusky green cere; long fine dark shaft streaks; subdued wavy crossbars; barred flight/tail feathers; pale forehead/eyebrows; distinct nuchal collar.
- Each adult face must read as one continuous pale grey-buff facial disc with a thin dark outer ruff. No separate white circular goggles or thick bright rings immediately around the eyes.
- Both adults fully visible and naturally gripping stable branches. The female may be modestly fuller and marginally larger, but do not create a dramatic height ratio or distort support/perspective.

CENTER JUVENILE — evidence-bounded single brood stage:
- A greyish, chubby, well-supported juvenile inside the natural cavity lip/floor.
- Bluish-grey irises, grey bill, exposed nostrils not covered by feathers, a narrow naturally bare grey periocular margin, and no ear tufts.
- Pale grey mesoptile/down with fine dark-brown horizontal bars over belly, face and chin.
- Short, soft, visibly underdeveloped folded wings, down-fringed and without adult remige layering; short concealed tail; not flying.
- Both feet clearly visible and planted on natural bark flakes/wood floor. Natural cavity is a design setting; do not reproduce the artificial nest box.

COMPOSITION:
- exactly three owls; adult male left, juvenile center, adult female right;
- no extra birds, legs, feet, eyes, labels, frames, nest-box hardware, woven basket, human objects or manufactured boards;
- maintain high-resolution natural feather detail, anatomically correct feet, believable cavity depth, and uncluttered readable labels.

This is a science-calibration rebuild and archive-integrity repair. Do not claim exact juvenile age, universal juvenile eye colour, exact flight threshold, subspecies, a fixed sex-size ratio, or transfer developmental timing from older broad Otus bakkamoena taxonomy.
```

## Planned assets

- `owl-pet/design/concepts/84-otus-bakkamoena-v8.jpg`
- `owl-pet/production/generated/84-otus-bakkamoena-v8-generated-master.jpg`
- `owl-pet/production/reviewed/84-otus-bakkamoena-v8-reviewed-master.jpg`
- `owl-pet/production/review-crops/84-otus-bakkamoena-v8-juvenile.jpg`
