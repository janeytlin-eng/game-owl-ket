# #149 *Ninox odiosa* v2 evidence and design boundary

- Current name: *Ninox odiosa* (Sclater, 1877); New Britain Boobook.
- Historical search names: Russet Hawk-Owl, New Britain Hawk-Owl, Spangled Boobook.
- Revision preserves v1 and does not change the 175/251 unique-species count.

## Archive integrity finding

The main-tree v1 blob is `055c79917fb2b4c30f43e8934f23354d20224d4f`, 786,445 bytes. The exported file has the same size but fails full PNG decode (`IDAT: invalid distance code`) and SHA-256 `d7925fd7…`, whereas the manifest records `475157b8…`. It cannot be visually inspected or safely used as an ImageGen target. v1 remains untouched; v2 is generated from a healthy adjacent owl-pet layout reference and is explicitly a reconstruction, not a recovered v1.

## Evidence actually read

- `NBBOO-IUCN-2018`: IUCN identification/range text (direct DOI open blocked) supports about 22 cm, fine-spotted chocolate-brown upperparts, paler mottled underparts, conspicuous white eyebrows/throat and New Britain forest distribution to c.1,200 m.
- `NBBOO-COMMONS-MALINOWSKI-2019`: CC BY 4.0 adult field photo metadata and pixels viewed. Compact earless russet/chocolate adult, orange-yellow eyes, short pale brows, pale throat, sparse white upperpart spots and branch support in dense vegetation.
- `NBBOO-GOULD-SHARPE-1884-PL5`: public-domain historic plate metadata/pixels read through Commons/BHL. Useful only as an adult pattern/history comparator.
- Original Sclater 1877 p.108 is retained as an unverified lead because the original page was not retrieved.
- Previously uploaded Mikkola guide was unavailable in this run; no unread page claim is used.

## Design boundary

- Adults near equal: no sexed visual series or measured sex-size direction was found.
- Use short separate pale brows, orange-yellow eyes, small pale throat, dark russet/chocolate upperparts with fine irregular white spangles, broad dark upper-breast zone and paler mottled lower underparts.
- No species-specific juvenile record was located. Use an age-unknown older juvenile, eyes closed, diffuse reduced markings, short soft wing/tail mostly hidden and two-foot branch support; no precise age, iris, flight or nest claim.
- Scientific verification remains false; only `PASS_WITH_LIMITATIONS` is available after pixel review.

## Full ImageGen prompt

```text
Use case: scientific-educational. Create a new 1536x1024 owl-pet triptych for #149 New Britain Boobook, Ninox odiosa, using Image 1 only as the established layout/style reference. Replace every bird and species-specific detail; do not retain Cebu Boobook anatomy. Exactly three birds on a mossy rainforest branch: ADULT MALE left, ADULT FEMALE centre, OLDER JUVENILE right. Keep the polished naturalistic 3D character-concept style, readable bottom labels, title “NEW BRITAIN BOOBOOK” and italic “Ninox odiosa”. Dense New Britain lowland/foothill forest, warm subdued dawn light.
Adults: compact small earless boobooks, near-equal visible scale because sex-size direction is unknown. Dark russet to chocolate-brown upperparts with fine irregular white spangles and small pale scapular marks; short separate white eyebrows, warm brown face, orange-yellow irides, small pale/white throat, broad darker warm-brown upper-breast zone and paler lower underparts mottled irregularly white and brown. Yellowish feet naturally gripping branch; no ear tufts; avoid long continuous V brows and avoid neat repeated rows.
Older juvenile: explicitly age unknown; eyes gently closed, low upright resting pose, both feet fully supported. Fluffier diffuse russet-brown body with reduced vague mottling, short rounded soft folded wing mostly buried in fluff, very short hidden tail, no crisp adult spangles or long remiges, no flight action.
Constraints: exactly three birds, whole bodies, natural support, no nest/eggs/cavity, no imposed dimorphism, no extra birds, no watermark, no misspelled text.
```

## Actual image review and iteration

- Reconstructed 1536×1024 master viewed. Adults show orange-yellow eyes, white brows/throat, dark russet upper breast, irregular pale spangles/mottling and supported feet.
- First-pass juvenile defect: crisp adult-like crown spangles and a long defined folded-wing edge. Edit1 changed only the juvenile to diffuse crown down and a shorter unspotted soft wing mostly buried in fluff.
- Full final plus 570×720 juvenile and 1020×600 adult crops were viewed. Both juvenile feet grip the branch, eyes are closed and no nest/flight claim appears. Result `PASS_WITH_LIMITATIONS`; adult spangle geometry and juvenile stage remain stylized, not specimen-exact. Science=false.

## Targeted edit prompt

```text
Targeted edit of Image 1. Preserve both adult New Britain Boobooks exactly, preserve all text, title, labels, forest, branch, composition, lighting and dimensions. Edit only the right-hand OLDER JUVENILE. Remove the crisp rows of adult-like pale crown spots and replace them with diffuse soft russet-brown down and only vague irregular mottling. Shorten and soften the visible folded wing so it is rounded, unspotted and mostly buried in body fluff, with no long parallel remiges or crisp coverts; keep the tail very short and mostly hidden. Keep the juvenile's eyes gently closed and both feet naturally gripping the same branch. Do not alter either adult, add birds, add a nest, or change any typography.
```
