# #71 *Ninox connivens* v4 research and design boundary

- Prepared: 2026-10-31T00:50:41+08:00
- Action: SCIENCE_REVISION; v1-v3 retained.
- Current name: *Ninox connivens* (Latham, 1801). Opened repository sources use the current genus; no unsupported old-genus remapping is added.
- Uploaded Heimo Mikkola guide: not directly mounted; repository-verified extract at printed pp.452–453/PDF pp.454–455 reused only for black bill/yellow eye, restrained sex direction and fluffy mesoptile direction.
- Active external search: two batches / six queries attempted; returned empty payloads. New sources credited: 0. Reused sources actually reread from v3 record: 6.

## Evidence actually read/reused

- **BARK-BARNES-ROSE-DEBUS-2005** — Barnes, Rose & Debus, Australian Field Ornithology 22:182–195. Printed pp.182–183, 185–186, 192–195 / PDF pp.1–2, 4–5, 9–14: nestling period about 36 days; a post-fledging day-2 owlet roosted 5 m high; day-3 owlets 10–12 m; dependence continued. Strong for supported mobility and developed flight surfaces, not exact feather geometry.
- **BARK-VIC-WILDLIFE-2023** — Victorian Wildlife Rehabilitation Guidelines, printed pp.80–81/PDF pp.4–5: adult yellow eyes, minimal facial mask, brownish-grey upperparts, white spotted wings, vertically streaked white underparts; juvenile incomplete collar, flanks/breast approaching adults; adult measurements overlap.
- **BARK-BULLOCK-2026** — primary abstract reused: one NSW family had 37–41 day nestling period and 5–6 month post-fledging dependence.
- **BARK-ABSA-2020** — HANZAB synthesis p.1: juvenile plumage at fledging, adult-like immature moult around three months, female marginally smaller with overlap.
- **BARK-AM-2022** — Australian Museum: adults grey-brown with white wing spots and streaked white underside; young less streaked with white-grey mottled nape; open tree hollow with wood debris.
- **WHSO-MIKKOLA-2013** — printed pp.452–453/PDF pp.454–455; reused only within stated limits.

## V3 inspection → correction

- V3 fixed original was opened from commit `12cfd6ef6f30d480b1f9bc5f328db338675ab775`. Adults and support pass, but the recent fledgling carries dense crisp adult-like white crown flecks and repeated white wing spots, weakening the source-supported incomplete-collar/mottled-nape juvenile distinction.
- V4 keeps the evidence-supported flight-capable stage and developed wing/tail, but removes dense adult crown speckles and converts juvenile wing markings to sparse diffuse bars/patches. Adult spots stay irregular and non-rowed. Sex direction remains subtle.
- Unknown: exact day-specific feather-tract geometry, subspecies transfer, universal sex ratio and first-flight mechanics. `scientifically_verified=false`.

## Full imagegen prompt

```text
Use case: scientific-educational.
Asset type: owl-pet species concept plate.
Primary request: Create a polished landscape 3:2 science-revision plate in the established realistic-cute natural-history game concept style for Barking Owl.
Scene/backdrop: dry open south-eastern Australian eucalypt woodland beside a shaded creekline; one very large old living eucalypt with a deep vertical hollow and loose decayed wood debris on its lip; warm natural dawn light; no decorative waterfall.
Subject: exactly three Barking Owls: adult male left, recent fledgling center, adult female right.
Composition/framing: full bodies, all feet visible and naturally supported; adults on separate branches flanking the hollow; recent fledgling alert on the firm hollow lip. Exact readable title “71 BARKING OWL”, italic subtitle “Ninox connivens”, bottom labels “ADULT MALE”, “RECENT FLEDGLING”, “ADULT FEMALE”.
Adults: medium hawk-owls, no ear tufts, almost no facial disc, broad white eyebrows, large bright yellow eyes, dark horn/blackish bill; brownish-grey upperparts with irregular non-rowed white wing spots; white underparts with strong brownish-grey vertical streaks, never V chevrons. Sexes similar with strong overlap; male only subtly fuller/longer-bodied and crown/support heights comparable.
Recent fledgling: selected day-2/day-3 post-fledging mobility stage from primary field observations at 5–12 m roost height. Developed folded wings and visible developed tail, firm two-foot grip and mobile posture. Clear juvenile identity: incomplete off-white collar, pale grey-white mottled nape, softer/plainer brown crown without dense adult white speckles, paler face, fewer softer vertical underpart streaks. Wing marks broad, diffuse and sparse, not crisp adult white spot rows. No neonatal wing buds and no hidden tail.
Constraints: juvenile must not be a miniature adult; adult spots irregular; adult underparts vertical streaks only; exact three birds and specified text only; stable support.
Avoid: extra birds, prey, eggs, ear tufts, Powerful-Owl chevrons, adult-spotted juvenile crown/wing, exaggerated sex gap, impossible feet, logos, borders, watermark, extra text.
```


## Review and archive evidence — 2026-10-31T00:53:50+08:00

- Full 1536×1024 master, 520×700 juvenile crop and 680×453 derivative opened. Adult vertical streaks/irregular spots; juvenile plainer crown, incomplete collar/mottled nape, diffuse wing marks, developed wing/tail and support passed first render.
- Result: PASS_WITH_LIMITATIONS; edit count 0. Exact day-specific feather geometry and subspecies transfer remain unknown. Science false.
- Archive prepared with concept blob `4830cefdc8d051d8d6fd703eda05ea6cf4b47f14`; fixed readback pending.
