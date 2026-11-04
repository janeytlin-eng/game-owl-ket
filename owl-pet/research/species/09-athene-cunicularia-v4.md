# #09 *Athene cunicularia* v4 — approximately 14-day emerging chick

- RESEARCH_READY: 2026-10-30T01:27:00+08:00
- Prior versions retained: v1–v3; v1 approval is historical and not transferred.
- Current roster name: *Athene cunicularia*; visual scope western North American *A. c. hypugaea*.
- Action: SCIENCE_REVISION; unique +0; science false.

## Evidence

- Reused **BUO-JOHNSON-AGING-2019** with a fresh read of introduction/methods and known-age day-13/14 images; PDF p.13 screenshot viewed. Mostly white down, open eyes, patchy brown crown/back/wing feather tracts; individual development varies.
- Reused **BUOW-SDZ-2017**: western chicks are brooded about 14 days, then begin emerging while feathers continue growing.
- Reused FWS species account: at two weeks juveniles stand/walk and appear at the entrance; flight starts much later.
- New **BUOW-SMITHSONIAN-2012**: juvenile plumage lacks adult white bars/spots; 3-week wing exercise and 4-week short flights are later than selected stage.
- Adult sex-size conflict between Mikkola and Cornell remains; near-equal display is retained.

## Boundary

Approximately 14-day chick is shown at first emergence, mostly white/cream down with patchy brown developing tracts and very short wing sheaths, both feet on packed soil and belly close to the burrow slope. It can stand/walk but is not flying, hopping or displaying wings. Exact age, individual condition, iris colour, feather count, local subspecies expression and burrow geometry remain unknown.

## Full built-in imagegen prompt

Use case: scientific-educational concept plate for the existing owl-pet collection.
Asset type: one landscape 3:2 tactile needle-felted-wool natural-history scene matching the confirmed owl-pet style.
Primary request: project #09 Burrowing Owl, Athene cunicularia, v4; exactly three western North American Burrowing Owls in one continuous shortgrass-prairie scene: adult male at left, adult female at right, and an approximately 14-day emerging chick at the natural mammal-burrow entrance in the center.
Adults: small compact tuftless owls with round heads, bright yellow eyes, white eyebrows and throat, sandy brown upperparts with rounded cream spots, pale barred underparts, short tail, long sparsely feathered tarsi and visible olive-gray toes. Keep male and female near-equal in displayed height and mass because sources conflict; do not encode a universal size difference.
Juvenile stage boundary: about 14 days, first emergence. It can stand and walk but cannot fly. Mostly white/cream fluffy down with patchy warm-brown developing feather tracts on crown, shoulder/back and very short wing sheaths; eyes open but do not force an exact iris colour; small hooked pale bill; no adult facial pattern, no regular white spot grid, no adult barring, no long layered remiges and no tail fan. Show it upright but low and steady at the burrow lip with both feet planted on packed soil and belly close enough to the slope for natural support; no hopping, wing display or unsupported pose.
Environment: natural prairie-dog or ground-squirrel burrow in dry shortgrass prairie, packed earth mound, sparse native grass and low warm morning light; no artificial pipe, cutaway chamber, prey, dung, trash or extra animals.
Composition: adults flank the central burrow entrance, all three fully visible; clear age contrast and physical support, no triptych/dividers.
Text, exact and legible: title "09 · BURROWING OWL · ATHENE CUNICULARIA"; labels "ADULT MALE", "ADULT FEMALE", and "APPROX. 14-DAY EMERGING CHICK".
Style: refined cinematic 3D with tactile needle-felted wool texture, documentary calm, realistic species markings.
Avoid: ear tufts, orange eyes on adults, feathered adult toes, exaggerated sex-size difference, adult-pattern juvenile, long juvenile flight feathers, flying/hopping juvenile, exposed unsupported chick, cavity/tree nest, artificial burrow pipe, extra birds, misspelled scientific name, watermark.


## Generated-image comparison checkpoint

At `2026-10-30T01:28:00+08:00`, the first render was checked at full resolution and with a dedicated juvenile crop. Adult morphology and support passed the prompt boundary. The chick's folded wing showed elongated spotted vanes inconsistent with the selected approximately 14-day first-emergence boundary documented above. The image therefore requires a localized wing edit and is not scientifically passed at this checkpoint. Generated evidence: `owl-pet/production/assets/09-athene-cunicularia-v4-generated.jpg`, `owl-pet/production/assets/09-athene-cunicularia-v4-generated-juvenile-crop.jpg`.


## Edit and recheck

A single localized edit removed the chick's elongated spotted wing vanes and replaced them with a compact down-softened wing bud bearing only short brown sheath nubs. Full-frame and juvenile-crop reinspection found no remaining adult spot grid, barring, long remiges or tail fan on the chick. Adults, text, burrow and physical support were preserved. Result: `PASS_WITH_LIMITATIONS`; exact iris colour and feather count remain deliberately non-diagnostic.


## Archive state

The reviewed v4 plate and both generated/reviewed evidence pairs were archived without replacing v1-v3. Scientific verification remains false: the design is evidence-bounded but not a specimen-level reconstruction. Fixed commit-pinned readback is pending at this stage.


## Fixed-commit verification

Fixed archive `1d6364b3eca882d2a9866480e7f5eeee79c363db` passed a non-truncated 1827-entry recursive-tree readback. All five formal image paths under `owl-pet/` matched their expected blobs and byte sizes; the initial root-path mistake was corrected and the erroneous paths were absent. Manifest, run, research/card and source-index blob matched. This verifies archive integrity, not specimen-level scientific certainty.
