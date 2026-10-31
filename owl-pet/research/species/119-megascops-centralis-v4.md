# #119 *Megascops centralis* v4 — juvenile folded-wing correction

- Batch / cycle: `2026-10-31T1130+0800` · 5/6
- Prepared: 2026-10-31T14:43:00+08:00
- Action: `SCIENCE_REVISION`; v1–v3 preserved; unique increment 0
- New sources: `CHSO-MIK2013-P242-243`, `CHSO-ITIS-1063250`
- Reused: `CHSO-REYES-ASTUDILLO-2017-PARTIAL`, `CHSO-JORDAN-2012`, `CHSO-AVIBASE-MAPPING`
- Corrected: `CHSO-REYES-ASTUDILLO-2017-PARTIAL` access/evidence boundary; full author-uploaded primary text pp.377–381 read
- Index: [SOURCE_INDEX.md](../SOURCE_INDEX.md)

## Source facts versus design inference

**Source facts.** The two 2015 owlets were explicitly “at an advanced stage of development”; most plumage was gray mesoptile with fine black bars, while facial disc, rictal bristles, primaries and secondaries were pennaceous. Primaries/secondaries were light brown with black transverse bars and differed from adult pattern. Tail measured 0 mm on both visits. Both fledged before 21 March, but hatch dates and exact ages were not known. The paper records possible parasite effects on growth. Mikkola printed pp.242–243 supports small short-tufted adults and states sex-size differences unknown; its 2013 “juvenile undescribed” is superseded for this exact nest by the 2017 study.

**Design inference.** A folded wing can visibly contain formed remiges, but the current v3 wing cannot be treated as a literal feather map: its long, crisp, evenly layered panel reaches close to the feet and reads like an adult wing. V4 therefore keeps a compact light-brown/dark-barred remige group embedded in gray mesoptile, ends it clearly above the feet/cavity sill and hides the tail. This is a conservative visual correction, not a claim about exact feather length or flight competence.

## Preserved boundaries

- Exactly three labeled birds and the existing composition.
- Adults remain near-equal in apparent scale because sex-size difference is unknown; no “female larger” template.
- Juvenile remains age unknown, cavity-supported on both feet, gray mesoptile, no projecting tail.
- Do not add nestlings, eggs, exposed parasites, flight, unsupported feet or adult-perfect juvenile coverts.
- Exact age, normal development, flight ability, juvenile sex, iris chronology and literal feather geometry remain unknown; `scientifically_verified=false`.

## Complete imagegen edit prompt

```text
Use case: scientific-educational image edit.

Edit the provided #119 Chocó Screech-Owl / Megascops centralis v3 concept plate into a new non-destructive v4 master. Preserve the established polished natural-history electronic-pet illustration style, 1536×1024 landscape layout, the exact three-bird composition, all existing text, adult birds, tree-cavity setting, moss, lighting, palette and overall framing.

Preserve verbatim:
- title: “CHOCO SCREECH-OWL”
- subtitle: “Megascops centralis”
- labels: “ADULT MALE”, “OLDER JUVENILE — AGE UNKNOWN”, “ADULT FEMALE”
- exactly three birds: adult male left, older juvenile center, adult female right

Change ONLY the center juvenile’s visible folded wing and immediately adjacent mesoptile transition:
- retain evidence-supported formed primaries and secondaries: light brown with irregular dark transverse bars;
- make the folded wing compact and shorter in silhouette, ending clearly above both feet and above the cavity sill, never descending as a long adult-length panel toward the toes;
- use a small irregular group of fresh, soft-edged remiges partly embedded in fluffy gray mesoptile, with varied spacing and softened tips;
- eliminate adult-perfect long layering, crisp repeated feather tiers, broad adult coverts, tidy scalloped rows, chevrons, fish scales, loops and mechanically aligned bands;
- keep the gray mesoptile with fine irregular black bars, gray bill with small pale-yellow tip, yellow iris as the documented A-like individual choice, no projecting tail, and both feet visibly supported on the cavity sill;
- no claim of flight and no wing spreading.

Do not change the adults: preserve near-equal apparent scale, small lowered ear tufts, yellow eyes, pale greenish bills, gray-brown cryptic pattern, bare pinkish lower tarsi/toes and secure branch grip. Do not invent sexual dimorphism.

Hard constraints: no extra birds, chicks or eggs; no flying bird; no unsupported foot; no watermark; no misspelled or duplicated text; do not crop any bird or label. The result is a scientific concept with explicit age/flight uncertainty, not a scientific pass.
```

## Review plan

Open the complete v4 image at original resolution, then inspect a center-juvenile crop and feet/sill crop. Pass only if the juvenile wing visibly terminates above the feet and sill, remains formed but non-adult-layered, tail remains nonprojecting, two-foot support is clear, and adults/text/count are preserved. If not, perform a juvenile-only imagegen edit and repeat both checks.
