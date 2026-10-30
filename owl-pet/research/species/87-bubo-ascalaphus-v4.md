# 87 *Bubo ascalaphus* v4 research and design boundary

Accessed 2026-10-31. Action SCIENCE_REVISION; v1-v3 preserved; unique increment0; science false.

## Sources actually read

- Reused `ASC-MIK2013-272`: Mikkola printed pp.272–273/PDF274–275, adult identity and mesoptile summary.
- Reused `ASC-ALSHEIKHLY2012-40D`: Sandgrouse34:72–74, c.40-day creamy-sandy juvenile with yellow iris, pale newly developed flight feathers and incomplete breast marks; exact flight ability/sex not reported.
- Reused `ASC-MOLDOVAN-SANDOR2009`: Sandgrouse31:73–78, staged nest series; prevents conflating downy, 30–33-day, 52–55-day and flying older young.
- New `ASC-DDCR2023`: Dubai Desert Conservation Reserve Annual Report 2022–2023, section4.3 “Monitoring of Pharaoh Eagle-Owl”, actually read online 2026-10-31. Three eggs were found inside a broom bush on 4March2022; chicks appeared on camera 23March and were active at the nest entrance. Supports arid shrub/ground support as possible habitat only; it gives no calibrated plumage, feather sequence or age for the visible chicks and is not used to redraw the documented c.40-day bird.

## Actual v3 recheck

The fixed v3 concept was reopened. Adult short tufts, eye/bill, breast-versus-belly zoning, feathered feet and near-equal height pass at concept level. The central c.40-day bird has an older juvenile body, creamy-sandy plumage, incomplete breast marks, short pale folded wing, short tail and bilateral rock support. No new evidence warrants changing biology. The only repository defect is the missing numeric prefix in the title.

## Design decision

V4 is a text-only correction: add repository number 87 while preserving every biological and scene feature. Exact feather count, juvenile sex, independent-flight ability, numeric adult RSD and regional fine plumage remain unknown. Archive integrity verification does not make science true.

## Complete imagegen prompt

```text
Use case: precise-object-edit
Asset type: owl-pet scientific species concept plate
Input image: #87 v3 is the edit target and authoritative visual baseline.
Primary request: change only the top title from “PHARAOH EAGLE-OWL” to exactly “87 PHARAOH EAGLE-OWL”.
Text (verbatim): “87 PHARAOH EAGLE-OWL”; italic scientific line “Bubo ascalaphus”; bottom labels “ADULT MALE”, “c.40-DAY JUVENILE”, “ADULT FEMALE”.
Constraints: preserve exactly three birds, all biological details, proportions, adult near-equal standing height, modestly fuller female, short adult tufts, orange-yellow eyes, black bills, feathered feet, zoned upper-breast drops/lower-belly fine bars, central creamy-sandy older juvenile with short pale developing folded wing, incomplete breast markings, short tail, two-foot rock support, desert wadi, lighting, crop and label positions. Change no bird, feather, foot, rock or habitat geometry.
Avoid: extra birds or text, altered plumage, mature juvenile remiges, flight pose, watermark, logo.
```

## Actual image review

Opened the generated 1536×1024 master and 520×700 juvenile crop. The top title is exactly `87 PHARAOH EAGLE-OWL`; scientific and three role labels are correct; exactly three birds remain. Adult short tufts, orange-yellow eyes, black bills, feathered feet, upper-breast drops/lower-belly bars and near-equal standing height remain coherent. The central c.40-day juvenile remains creamy-sandy with incomplete breast marks, compact pale developing folded wing, short tail and bilateral rock support; no flight pose or mature wing substitution. Desert wadi/shrub context is plausible. No post-generation edit was required. Result: `PASS_WITH_LIMITATIONS`, edit count 0, scientifically_verified=false. Unknowns remain exact flight ability, sex, feather count, adult numeric RSD and regional fine plumage.

## Archive checkpoint

At 2026-10-31T05:45:00+08:00 the concept, generated master, reviewed master, juvenile crop, three image manifests, STATUS, design README, knowledge note and run record were committed together. Fixed-commit byte/blob readback is still required before cycle credit.

## Fixed archive verification

At 2026-10-31T05:49:00+08:00, commit `e2e64d496ad9cb0bf37b1262950187cf04e86e10` was re-read. All four JPEG blobs and byte sizes exactly matched local Git object hashes; recursive tree had 2223 entries and was not truncated; manifest counts were 590/589/580; batch, run, research, STATUS, design README and knowledge records were present. This verifies archival integrity only; scientific verification remains false.
