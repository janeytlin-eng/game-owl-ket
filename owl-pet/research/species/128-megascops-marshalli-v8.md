# #128 *Megascops marshalli* v8 research and design boundary

## Recovery finding

The latest v7 path is not a decodable complete PNG. The repository copy is 787,051 bytes, SHA-256 `ccc656d98a1f8e4496ba4a11b2c7c1d38b61697cc88a64b993b7f14feaf10853`, Git blob `a3317737c2a42efe57af302fad2ebd224f3839c4`; ImageMagick reports `IDAT: invalid distance code`. The v7 run instead records a 3,313,051-byte reviewed PNG with SHA-256 `413fa9e1cd9c189a24b478d6169d51fcf46066d4483ed44f8aa61e4df15e1d0b`. V7 and its record stay untouched as history. V8 is a fresh rebuild and must pass independent full decode, original-resolution viewing and commit-pinned path/blob readback.

## Evidence boundary

- Adult identity follows `MARS-WESKE-1981` and directly reread `MARS-MIK2013-P234`: very short ear tufts, dark-brown irides, rufous facial discs broadly rimmed black, rich chestnut dorsum with irregular blackish wavy bars/mottling, broken pale scapular band, irregular pale/dark ventral pattern, grayish-yellow bill, feathered tarsi ending at grayish-flesh bare toes.
- Pale hind-crown feathers must be a narrow broken posterior row with rufous/dusky-tipped individual feathers, not a broad smooth white forehead V, cap or halo.
- Female mass direction is modest and based on limited specimens/secondary synthesis. Keep adults near equal crown-to-foot display height; permit subtle fullness, not an imposed giant female.
- Downy chick is undescribed. Use an explicitly age-unknown older immature/mesoptile direction: adult-like species identity with softer, lower-contrast texture, a few lax buff-barred scapular feathers and formed but paler compact folded remiges. Hide most of the tail rather than inventing a precise ten-bar display. Flight ability remains unknown, so keep both feet naturally supported and wings folded.
- Habitat follows `MARS-HERZOG-2009` and `MARS-ARMONIA-2009-P29`: structurally complex wet montane cloud forest, dense understory, mosses/ferns/epiphytes. This is a roost composite, not a nest record.
- The plate remains concept art pending scientific calibration; `scientifically_verified=false`.

## Full imagegen prompt

Use case: scientific-educational natural-history concept plate for the owl electronic-pet project. Create a completely new 1536×1024 landscape plate for **#128 Cloud-forest Screech-Owl — *Megascops marshalli***, preserving the established refined softly realistic hand-painted/3D owl-pet style.

Show **exactly three birds**, evenly spaced on one thick, naturally horizontal moss-covered branch in humid Andean wet montane cloud forest with ferns, orchids and epiphytes: left **ADULT MALE**, center **OLDER IMMATURE — AGE UNKNOWN**, right **ADULT FEMALE**. All six feet must visibly and plausibly grip the branch; no floating bodies, no invented nest or cavity, no family-behaviour narrative. Adults should have near-equal crown-to-foot display height; female may be only subtly fuller, never automatically much larger.

Adult identity: compact small screech owls with very short subdued ear tufts; dark brown irides (never yellow/orange); rich rufous/chestnut facial discs with a broad black outer ruff; small grayish-yellow hooked bill; rich chestnut upperparts with fine irregular blackish wavy cross-bars and mottling, never repeated hard armor tiles; a broken pale scapular band; rufous throat/upper breast and whitish lower breast/belly with irregular black/rufous shaft streaks, broken bars and uneven pale spaces, never mechanical U-shaped scallops. Tarsi feathered only to the base of grayish-flesh slender bare toes with pale horn claws. At the posterior hind crown/nape only, show a narrow low-contrast broken row of individually pale-tipped feathers with dusky/rufous tips; do not paint a broad white forehead V, cap, halo or necklace.

Older immature: unmistakably the same species and mobile enough to perch, but age unknown. Dark brown eyes; softer lower-contrast buff/rufous body texture; a few lax buff-barred scapular feathers; compact naturally folded formed remiges that are paler and less crisply layered than adult wings. Wing tips stop well above the feet; tail mostly hidden behind the branch/body. Do not create a downy newborn, adult-length exaggerated wings, a long exposed perfectly ten-barred tail, or a miniature adult with perfectly regular coverts. Give a natural slight head turn distinct from adults; no flight pose.

Typography must be clean and exact: title **“#128 · CLOUD-FOREST SCREECH-OWL”**, scientific name **“Megascops marshalli”**, labels **“ADULT MALE”**, **“OLDER IMMATURE — AGE UNKNOWN”**, **“ADULT FEMALE”**. No extra birds, duplicated faces, malformed toes, watermark or extra text. Warm diffuse cloud-forest light must still leave dark eyes, black facial rims, bills, feet, wing edges and the narrow hind-crown row inspectable.

## Planned review gates

1. Exact count/text/species spelling and three life-stage/sex labels.
2. Dark-brown adult and immature eyes; grayish-yellow bills; short tufts; black-rimmed rufous discs.
3. No broad forehead band; hind-crown marking posterior, narrow, broken and low contrast.
4. Adult sizes near equal; no unsupported female-large formula.
5. Immature wing compact, softer and supported; tail mostly hidden; no newborn or flight claim.
6. Six plausible feet on one natural branch; cloud-forest habitat without invented nest.
7. Full PNG decode, dimensions, SHA-256/Git blob and immutable remote readback before cycle credit.
