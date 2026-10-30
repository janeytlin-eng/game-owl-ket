# #74 *Ninox novaeseelandiae* v4 research and design boundary

- Prepared: 2026-10-31T00:56:13+08:00
- Action: SCIENCE_REVISION; v2-v3 retained.
- Taxon: New Zealand nominate Morepork/Ruru, *Ninox novaeseelandiae*; not Australian Boobook #72 and not Norfolk hybrid populations.
- Uploaded Mikkola guide was not directly mounted this execution; no fresh claim from it.
- Active external search: three targeted queries returned empty payloads; new sources credited 0. Reused four sources actually reread from v3 record.

## Evidence actually read/reused

- **MOR-NZBO-HANZAB-2025** — New Zealand Birds Online 295_Morepork PDF, development section: pins/dorsal timing from day 8 onward; wing spotting by day 24; one-month dorsal feathering with downy head/underparts; fledging 38–40 days; recent fledglings have short tail, downy head/underparts and about 90% adult weight. Institutional synthesis, not a universal continuous series.
- **MOR-DOC-2026** — New Zealand Department of Conservation species account: chicks mainly attended until fully feathered and fledge around 37–42 days. Broad official synthesis.
- **MOR-STEPHENSON-MINOT-2006** — *Notornis* 53:308–315, printed pp.308–311: two measured chicks; white natal down darkens by day 15, pins/brown fluff around day 16, white spots/stronger claws by day 25, one fledged day 39; cavity leaf litter/wood dust. Small primary sample.
- **MOR-TEARA-2009** — institutional history/caption: white then brown down; forks/epiphytes/hollows; young leave 35–40 days and remain with adults.

## V3 inspection → correction

- V3 fixed original from commit `a77dcaa51fd78fb9942811ae10b59834adf6d683` was opened. Adult identity, habitat and juvenile fluff pass, but the recent fledgling reads much smaller than the source's approximately 90%-adult-weight boundary and its tail is not strongly distinguished from adult length.
- V4 keeps the well-supported recent-fledgling stage but gives it near-adult torso bulk while crouched lower, plus a clearly short juvenile tail. It remains fluffy on head/neck/underparts and does not become a sleek miniature adult.
- Exact body dimensions, individual age, tract chronology, sex ratio and island transfer remain unknown; `scientifically_verified=false`.

## Full imagegen prompt

```text
Use case: scientific-educational.
Asset type: owl-pet species concept plate.
Create a polished landscape 3:2 science-revision plate in the established realistic-cute natural-history game style for New Zealand Morepork / Ruru.
Show exactly three owls: adult male left, recent fledgling center, adult female right. Exact readable title “74 MOREPORK”, italic subtitle “Ninox novaeseelandiae”, and bottom labels “ADULT MALE”, “RECENT FLEDGLING”, “ADULT FEMALE”.
Habitat: humid New Zealand native podocarp/hardwood forest, a natural tree cavity/fork with leaf litter and wood dust, moss and one epiphyte; no Australian eucalypt-dominant setting and no water.
Adults: small compact Ninox, no ear tufts; dark chocolate-brown upperparts with sparse small off-white spots and broken bars; rufous-brown underparts with narrow cream crossbars/mottling; warm dark facial disc; yellow-green irises; dark hooked bill; feathered legs and yellow feet. Adults near-equal in standing height, female only subtly fuller; no fixed sex ratio.
Recent fledgling: source-selected about 38–40 days and approximately 90% adult body mass. It may crouch lower, but its torso bulk must be near adult rather than a half-sized chick. Developed folded juvenile wings; visibly short tail much shorter than adult tails; firm two-foot perch. Retain downy/fluffy head, neck and underparts, darker greyer-brown juvenile tone, soft pale fluffy tips on head, sparse irregular pale wing marks. Do not make it a sleek miniature adult.
Constraints: exactly three birds, all feet supported, functional wing surfaces, short juvenile tail, near-adult body bulk, fluffy juvenile head/underparts.
Avoid: early pinfeather chick, tiny body, long adult-length juvenile tail, dense adult white spotting on juvenile, flight pose, eggs, extra birds, extra text, logos, border, watermark.
```
