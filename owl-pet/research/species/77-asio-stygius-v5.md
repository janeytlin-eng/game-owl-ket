# #77 *Asio stygius* v5 research and design boundary

- Run: `20261105T233209+0800-cycle-1`; batch `20261105T233209+0800`, cycle 1/6.
- Action: `SCIENCE_REVISION`; v1–v4 preserved.
- Current name: *Asio stygius* (Wagler, 1832). No alternate combination is substituted in the repository title; older literature may contain the typographic spelling *A. styigius*.
- Selected stage: older branch-active juvenile, estimated by the primary authors as older than one month; not an exact individual age and not transferred to the dated 26–27-day Brazilian ground stage.
- Scientific status: false.

## Sources actually opened and read on 2026-11-05

### STY-CADENA-ORTIZ-2018-P23-25-F2-T3 — new to current source index

Cadena-Ortiz, Bedoya, Pozo-Zamora, Watson & Brito, “Notas sobre la dieta, desarrollo de jóvenes y distribución del Búho Estigio *Asio stygius* … en Ecuador,” *Revista Ecuatoriana de Ornitología* 3:20–31, DOI `10.18272/reo.v0i3.773`. Direct journal PDF opened. Printed pp.23–25, Table 3 and Figure 2 were read and the printed-p.23 figure page was rendered.

Facts: two young at Nayón were observed for 35 days. They retained scattered down, black facial discs, small ear tufts, yellow irides, barred bellies and pale hind-crown feathers; later the belly darkened and the breast began adult-like parallel/herringbone lines. On 20 May they moved rapidly between branches in the same tree, and one extended its wings, interpreted as intimidation. The authors infer the birds were already older than one month at first observation because the Lopes birds at 27 days were still ground-bound.

Limits: two juveniles at one Ecuador locality; the age is an inference, not hatch-dated. The photographs do not provide a continuous measured feather sequence or flight threshold, and the defensive interpretation is observational. The article does not sex the young.

### STY-LOPES-ETAL-2004-P423-425-F1 — re-read and boundary correction

Lopes, Goes, Souza & de Melo Ferreira, “Observations on a nest of the Stygian Owl (*Asio stygius*) in the central Brazilian cerrado,” *Ornitología Neotropical* 15:423–427. Direct SORA PDF opened and printed pp.423–425/Fig.1 read.

Facts: the ground nest was a 17 cm × 3 cm shallow depression under a shrub below 70 cm. One day before predation, the hatch-dated 26–27-day young were a little over two-thirds adult body size; remiges and rectrices were still poorly developed and entirely prevented flight attempts.

Boundary: this dated Brazilian stage validates v4's short down-dominated wing, but it does **not** validate branch movement or wing extension. V5 therefore changes stage rather than adding action to the v4 ground nestling.

### WHSO-MIKKOLA-2013 — repository extraction reused, guide not freshly mounted

The repository's earlier extraction records printed pp.502–503 / PDF pp.504–505 for adult and mesoptile appearance. The user-uploaded guide itself was not mounted in this run, so no new page transcription is claimed. It is used only as a previously read morphology cross-check.

## Design decision

- Adults remain near-equal in crown height; female may be subtly fuller only. No quantified linear sex-size ratio was found, so size is not encoded as a large height difference.
- Both adults: long erect ear tufts, deep black facial masks, yellow-orange irides, black bill/claws, very dark sooty-brown upperparts, warm buff-gold streaking below.
- Juvenile: older branch-active stage with black disc, yellow iris, small tufts, scattered residual pale down (especially hind-crown/body), barred belly and formed but still juvenile-soft wing/tail. One wing may extend sideways in a low intimidation posture; both feet grip one broad branch continuously. No flight pose or exact-age label.
- Scene: Nayón rural-tree setting, muted highland orchard/remnant-native vegetation. It is a documented observation setting, not a nest claim.

## Full imagegen prompt

```text
Use case: scientific-educational
Asset type: owl-pet species concept plate, horizontal 3:2
Input image: Image 1 is the v4 style and adult-identity reference; preserve its painterly-realistic, gently rounded owl-pet finish but do not copy the static juvenile stage.
Primary request: exactly three full-body Stygian Owls, left adult male, center older branch-active juvenile, right adult female.
Scene/backdrop: a muted rural highland tree setting in Nayón, Ecuador, with one broad natural branch spanning the lower frame, soft olive remnant vegetation and distant slopes; no nest, eggs or prey.
Text (verbatim): top line “77 STYGIAN OWL”; second italic serif line “Asio stygius”; bottom labels “ADULT MALE”, “OLDER JUVENILE”, “ADULT FEMALE”. No other text.
Adults: near-black sooty-brown, long upright ear tufts, deep black facial masks/discs, yellow-orange irises, black bills and claws, dark upperparts and warm buff-golden streaking/barring below. Keep crown heights comparable; female only subtly fuller. Give the adults distinct calm head/stance directions while both feet remain visibly supported.
Central juvenile: later than the 26–27-day ground stage and estimated older than one month, but do not print an exact age. Black facial disc, yellow irises, small developing ear tufts, pale hind-crown feathers and scattered residual pale down over a partly formed juvenile plumage; barred belly with only beginning chest herringbone. It is active on the branch: both feet firmly grip the same broad branch while one wing extends sideways and slightly downward in a low defensive/intimidation gesture; the other wing stays folded. Formed remiges and tail are allowed but must be softer, shorter and less perfectly layered than the adults, without adult-regular pale rows. This is not takeoff or flight.
Constraints: exact number/title/order; exactly three owls; coherent feet and continuous branch support; no generic female-much-larger rule; no ground-nestling body, no newborn fluff, no adult-perfect juvenile wing pattern, no hovering or airborne pose, no extra birds, no prey, no eggs, no logo, border or watermark.
```

## Review gates and unknowns

- Verify exact three birds/text/order; adult identity; comparable adult crown height; juvenile yellow iris, black disc, small tufts, residual down, formed-but-nonadult wings/tail; both feet gripping a branch; wing gesture reads as supported intimidation rather than flight.
- Unknown: exact age, juvenile sex, exact feather geometry and branch-to-flight threshold; cross-population transfer; adult linear sex-size ratio; bill/iris chronology. These prevent scientific approval.

## Production result

- Initial generation passed identity/action/support but its extended juvenile wing was too long and perfectly graduated. One targeted edit shortened and softened only that wing; final full image and two crops passed with limitations.
- Concept/reviewed master: 1536×1024 PNG, 2,840,596 bytes; SHA-256 `310a22ffa328c88539a874fe27a2a533433c0568e1ec3efadd28cb2a98e51fdd`; Git blob `d61c329a97937b85020f93ce1e099c807eaa62db`.
- Initial generated master remains preserved separately; edit count 1; unique coverage unchanged at 176/251; revision +1; immutable archive readback pending; science false.

### Immutable archive verification

Archive commit `71a6ddf87b71ffebe5ae864713bac53b6d43abc3`, tree `4095e921a692ba61c7fe3023aa54915c85449873`, returned all required paths and exact image blob/size tuples in a non-truncated 3,153-entry tree. Manifests parsed at 700/701/691 with this entry last. `PASS_WITH_LIMITATIONS`; scientific status remains false.
