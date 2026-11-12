# #179 *Otus mayottensis* v4 image review

- **Reviewed:** 2026-11-13T05:51:09.417+08:00
- **Run:** 20261113T054310+0800-cycle-6
- **Result:** PASS_WITH_LIMITATIONS
- **scientifically_verified:** false
- **Edit count:** 0; no image defect required a second ImageGen invocation.

## Files actually opened

- 1536×1024 full generated/final plate.
- 512×768 adult-male crop.
- 512×768 adult-female crop.
- 512×768 age-unknown older-immature crop.

## Evidence-by-feature review

| Check | Evidence boundary | Observed result |
|---|---|---|
| Count/text | Saved prompt | Exactly three birds; title “179 MAYOTTE SCOPS-OWL”, italic binomial and three role labels are correct. |
| Adult morphology | Marshall 1978 printed p.19; living-bird photos; Mikkola p.139 repository transcription | Blackish-/rufous-brown adults with dark shaft streaks, short tufts, yellow eyes and compact short-tailed outline. |
| Sex treatment | No quantified sex direction found | Adults are near-equal; female only subtly fuller; no sex-coded morph. |
| Tarsi/feet | Marshall 1978 printed p.19 | Feathering stops above a short visible distal bare segment; not feathered to the toe and not a broadly naked leg. All feet grip the branch. |
| Immature | Voisin et al. 2011 printed pp.15–16 only identifies one immature | Rendered as an age-unknown older immature: dark/indeterminate iris, softer irregular body feather, fewer-layer compact wing, mostly hidden short tail, bilateral support. No exact age or flight claim. |
| Habitat/nest | Mayotte secondary-forest setting; nest evidence absent | Humid open branch; no cavity, lining, eggs, prey or invented breeding action. |

## Problem → evidence → modification → recheck

- Prior v3 problem: tarsi were described/rendered as feathered to the toes. Marshall's examined-specimen text says the distal c.5 mm is bare. The v4 prompt and plate expose only that short terminal segment. Crop recheck passed.
- Prior v3 problem: adult pattern was too muted for the blackish-brown back/brownish-red belly and conspicuous shaft streaks. The v4 plate strengthens these shared traits without assigning morph by sex. Both adult crops passed.
- Generation check found no new visual defect needing an edit. This is a validated no-edit outcome, not a claim of scientific completeness.

## Remaining limitations

Exact immature age, iris development, flight ability, complete feather sequence, population morph frequency, and represented nest details remain unknown. Therefore the plate is a reviewed concept, not a scientifically verified reconstruction.


## Archive transport correction — 2026-11-13T05:57:27.852+08:00

The first archive transport truncated the full plate and adult-male crop because a Base64 command-output cap was hit. Those two Git blobs are superseded and are not evidence. Canonical full image blob is `e047a4014b006e4d462f9b50fea08f21a1c965a3` (3,042,459 bytes, SHA-256 `891f8879695a7ff9d7f215d899e94973c2fb99a1e8ffef2c20802f63d41dee16`); canonical male crop blob is `d222f130e37a654cbf118dd35eab9b7c925609b6` (799,117 bytes, SHA-256 `95d2fe6231bb7f6ffd9403e18a60cc6ca3ee2edc24b6b37ca5a69dc48b8476b7`). Visual conclusions are unchanged; immutable readback still pending.
