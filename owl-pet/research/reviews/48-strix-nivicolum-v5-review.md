# #48 Himalayan Owl v5 review — *Strix nivicolum*

- Reviewed: 2026-11-05T04:47:00+08:00
- Result: **PASS_WITH_LIMITATIONS**
- Scientifically verified: **false**
- Action: v4 → v5 high-resolution science/archive revision
- Master SHA-256: `c264cd723dd67e564e7bdd1c8f031ff550e25e2d38c071c789bccefd85ed7ea5`
- Master Git blob: `2e0f35ad63d6dd74020a033fcd235dae263f9985`
- Adult comparison crop: `owl-pet/production/review-crops/48-strix-nivicolum-v5-adults.png` (`54404a86d89745f3b4cea102a9e1447a85e2b843`)
- Juvenile crop: `owl-pet/production/review-crops/48-strix-nivicolum-v5-juvenile.png` (`87cc765aa4e26e308f036673124f9bed43aded6d`)

## Evidence-based check

- Identity: both adults are round-headed and untufted with dark brown eyes, yellowish bills, dark-edged tawny/brown facial discs, dark grey-brown upperparts, pale scapular marks, buff-barred folded wings/tails, crossed dark ventral pattern and feathered toes. This matches the National Taiwan Museum/TaiEOL descriptions.
- Sex treatment: adults are alike and near-equal in crown height. The female's slightly fuller presentation is not treated as a measured dimorphism.
- Juvenile: pale cream/light grey-brown rather than pure white; sparse white down wisps remain on crown/body; markings are diffuse. After edit, wings are short, rounded and embedded in fluff; no long tail, open wing or flight claim is visible. Both feet grip the cavity lip.
- Taxon gate: the sheet does not use the pure-white adjacent-species *S. newarensis* concept. Title uses current species name; historical Taiwanese combinations remain metadata only.
- Habitat/support: cool high-elevation conifer–broadleaf forest, mossy natural cavity and branch supports are visible; no human nest-box claim is inserted.
- Composition: exactly three birds, exact title, exact three labels; all feet/supports visible.

## Problem → evidence → modification → recheck

1. Initial render gave the juvenile a long, dark, layered viewer-left wing.
2. NTM supplies an age-unknown very-pale immature description but no adult-like remex authorization; the prompt explicitly bounded both wings as short and mesoptile-embedded.
3. One juvenile-only edit removed the long layering and hid both wings in fluffy mesoptile while preserving all text, adults and supports.
4. Full-frame and juvenile crop recheck found no adult-type juvenile wing or visible tail; adults/labels/supports remained unchanged.

## Remaining limitations / unknowns

Exact juvenile age, remex/tail measurements, climbing/flight threshold, sex-size ratio and population transfer remain unknown. The South Korean paper confirms fledging but its accessible abstract does not provide a developmental plate. This is concept-art review, not ornithologist sign-off.

## Iteration rule

A detailed negative prompt alone did not prevent the recurring long juvenile wing. For an age-unknown down-rich *Strix* juvenile, require an explicit post-generation crop gate: any long layered wing extending below mid-body triggers a juvenile-only edit. Applied and visually verified on #48 v5; v4 showed the same failure pattern, but broader archive validation remains pending.
