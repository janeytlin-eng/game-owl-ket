# #79 Collared Scops Owl — *Otus lettia* — v4 research/design record

- Batch/cycle: `2026-10-31T0134+0800` · 3/6
- Action: SCIENCE_REVISION; unique-species increment 0.
- Started: 2026-10-31T02:36:48+08:00
- RESEARCH_READY: 2026-10-31T02:37:06+08:00
- Previous v1-v3 and user-confirmation records preserved.

## Evidence reused and checked

1. **LET-LEADPRATHOM-2009** — Leadprathom et al., “Breeding Biology of the Collared Scops Owl *Otus lettia*”, *Ardea* 97, DOI 10.5253/078.097.0409, printed p.459 development subsection. Repository's prior actual-read record: remiges/semiplumes begin at 6–10 d; bill bristles begin at 11–15 d; rectrices begin at 16–20 d; fully feathered/fledged 21–25 d. Applied to the same 11–15 d stage already selected for v3.
2. **SUN-BSS-CURRENT** — Bird Society of Singapore current species account. Repository's prior actual-read record supports current name *Otus lettia*, dark eyes/reddish orbital rim, short conspicuous tufts, bark-brown vermiculation, pale hind collar, sandy-buff finely streaked underparts and paler fine-barred juvenile. Sex-size direction is not established.
3. **LET-HKBWS-2023** — Hong Kong Bird Watching Society regional account/checklist material previously read for current identity, cavity/nest context and polytypic treatment. Does not establish an exact individual feather geometry or sex ratio.
4. **WHSO-MIKKOLA-2013** — Mikkola photographic guide, repository actual-read record at printed p.162 / PDF p.164. Sexed measurements unavailable and female-greater marked uncertain; therefore no exaggerated sex-size direction. The uploaded guide itself was not directly exposed in this runtime; this cycle reused the page-pinned repository record rather than claiming a fresh page view.

## Active external search this cycle

- System-1 queries: Leadprathom 2009 nestling development; juvenile plumage/sex size; current taxonomy. The connected search service returned an empty result payload.
- System-2 retry with title/DOI, BirdLife wording and museum-measurement terms also returned an empty result payload.
- Therefore: **new sources 0, reused 4, corrected design boundary 1**. No search hit is treated as verified evidence. Existing page-pinned primary chronology remains the strongest usable source.

## Problem → evidence → change → check plan

- **Problem:** v3's 11–15 d central nestling has a row of relatively long, neatly separated dark wing feathers that reads more mature/regular than the dated development boundary warrants.
- **Evidence:** remiges only begin at 6–10 d, while rectrices do not begin until 16–20 d; at 11–15 d use short sparse growing remige tips/pins under soft down and no visible tail.
- **Change:** preserve the exact supported stage and adult plate; shorten/soften only the juvenile wing and make the emerging dark tips sparse/irregular.
- **Required review:** exact text and three-bird count; adult identity/near-equal scale; juvenile open eyes, supported belly, no tail, no standing/flight, no mature layered wing; both adults naturally supported.

## Known limits

Exact individual eye-opening day, pin count/geometry, subspecies transfer, sex-size direction and the relationship between dark pin sheaths and visible vane length remain unknown. This concept cannot be scientifically verified from the available evidence.

## Full imagegen prompt

Use the attached #79 Otus lettia v3 plate as the layout/style reference. Create one scientifically cautious photorealistic prototype group plate with exactly three Collared Scops Owls: adult male on the left, one 11–15-day cavity nestling in the center, adult female on the right. Preserve exact title “COLLARED SCOPS OWL”, italic scientific name “Otus lettia”, and labels “ADULT MALE”, “11–15-DAY CAVITY NESTLING”, “ADULT FEMALE”. Preserve the warm natural daylight, tropical broadleaf cavity, photographic depth and near-equal adult scale; do not make the female generically much larger. Adults: compact scops-owl bodies, conspicuous but natural ear tufts, dark brown irides with subdued reddish orbital rims, greenish-yellow bill, mottled bark-brown upperparts, pale hind-collar cue and sandy-buff finely black-streaked underparts, both feet naturally supported. Juvenile: retain open eyes, pale natal/early semiplume down, just-beginning bill bristles, no visible tail/rectrices, belly/sternum supported on dry cavity substrate. Correct the v3 juvenile wing treatment: depict only very short growing dark remige tips/pins under soft down, irregular and sparse, not long neat layered adult-like feathers or repeated pale bars. No standing, climbing, wing spreading or flight. Exactly three owls, no extra birds, no labels changed, no fantasy features, no mature juvenile tail or adult wing fan.

## Actual image review

- The v4 imagegen result was opened at 1536×1024. Title/name/labels and three-bird count are exact; adults retain dark eyes, reddish orbital rims, greenish-yellow bills, bark-brown plumage, near-equal scale and natural support.
- Juvenile crop reopened at 520×700: open eyes, pale down, belly/sternum support, visible small feet, short sparse dark growing wing tips and no visible tail. No standing, climbing or flight.
- 680×453 concept derivative reopened: composition and text remain legible; no new issue found.
- Result: PASS_WITH_LIMITATIONS; one direct imagegen revision of v3; no additional edit. Science false.

## Archive checkpoint

- 2026-10-31T02:40:20+08:00: exact concept/generated/reviewed/crop JPEG objects and three manifest rows persisted; immutable commit readback pending.

## Fixed archive verification

- 2026-10-31T02:41:05+08:00: immutable archive `20419a0cd19aec7ecffa739e3b319fc3f61a95ea` returned exact complete concept/generated/reviewed/crop JPEG payloads, blob IDs and byte sizes. Manifests 583/582/573 and linked records matched. Production VERIFIED; scientific status false.

