# #55 Verreaux's Eagle-Owl — *Bubo lacteus* v5 research

- Run: `20261105T070800+0800-cycle-4`; batch `20261105T062700+0800`, cycle 4/6.
- Action: full-resolution science/archive revision; v1–v4 preserved.
- Checklist name retained: *Bubo lacteus*. IOC 15.1 / ITIS TSN 1244710 currently treats *Ketupa lactea* as valid and lists *Bubo lacteus* and original *Strix lactea* as synonyms; both systems are recorded rather than silently renaming the checklist.
- Research ready: 2026-11-05T07:12:00+08:00.
- Source delta: restored3 missing stable-index entries / reused2 / corrected2; science false.

## Evidence read/reused

- `VEO-BROWN-1965-P101-104`: L. H. Brown, 1965, *Observations on Verreaux's Eagle Owl Bubo lacteus (Temminck) in Kenya*, J. East Africa Natural History Society 25(2), printed pp.101–104; publisher scan opened 2026-11-05. Lines 32–49 document commandeered/abandoned stick nests of raptors and Hammerkop bases. Lines 51–61 directly describe young: pale grey down hidden by finely barred grey/white feathers; about six weeks barred overall except plain white thighs, black streak on each side of face, almost-black eyes with long black bristles, pale blue-grey bill, yellowish-white feet, paler orange-pink upper lids; day crouching/standing and night walking/wing-flapping; one young left at 50–60 days. This is the primary juvenile boundary.
- `VEO-ITIS-1244710`: ITIS/IOC v15.1 record re-read 2026-11-05, lines 42–58 and 67–98. Valid current name *Ketupa lactea*; synonyms *Bubo lacteus* and *Strix lactea*. Taxonomic authority, not plumage evidence.
- `VEO-BIRDLIFE-PILLANS-2019`: John Pillans field/photo account, BirdLife South Africa, pp.46–49; lines 19–35 re-read. Verreaux's Eagle-Owls used an abandoned Crowned Eagle nest in an Erythrina. Modern corroboration of old large stick-nest reuse; not an ageing atlas.
- `VEO-MIKKOLA-2013-P286`: page-specific repository extraction reused; uploaded file itself inaccessible this execution. Adult diagnostic dark eyes/pink lids and plate context. No claim of a new page read.
- `VEO-BIRDLIFE-PILLANS-2019` and prior v4 research were checked for conflicts; Brown 1965 remains the direct developmental source.

## Corrections and design boundary

1. Taxonomy: do not present repository *Bubo lacteus* as the only current placement; map it explicitly to current *Ketupa lactea* while preserving checklist numbering/title.
2. Juvenile: v5 uses Brown's approximately-six-week nestling, not a generic fledgling. It may crouch or stand/walk inside the nest and flap at night, but the plate shows a calm fully supported crouch—no branch departure or flight.
3. Plumage: fine grey/white barring is supported; crisp adult scapular spots, adult layered wing pattern and long exposed tail are not. Plain white thighs, black cheek streaks, almost-black eyes, pale blue-grey bill, yellowish-white feet and paler lids are positive constraints.
4. Sex direction: no species-specific quantified adult body ratio was found in the sources actually read. Adults remain near-equal crown height, female only subtly fuller; no universal “female larger” rule.

## Complete imagegen prompt

Create one polished 3:2 landscape scientific concept plate, 1536×1024, in the repository's warm painterly semi-realistic 3D animated-film maquette style. Exact title: “55 · VERREAUX'S EAGLE-OWL · Bubo lacteus”. Exactly three owls labeled left ADULT MALE, centre JUVENILE · APPROX. 6 WEEKS, right ADULT FEMALE.

Adults: very large pale grey-brown eagle-owls with small natural ear tufts, almost-black/dark-brown irises and highly diagnostic vivid rose-pink upper eyelids visible as a clean rim. Broad pale facial discs with darker border, black bill, finely vermiculated pale grey upperparts, large soft whitish scapular patches, pale underparts with fine grey barring, feathered tarsi/toes and dark claws. Male and female near-equal crown height; male only subtly slimmer, female only subtly fuller—no dramatic size claim. Both supported on thick stable branches beside the nest.

Juvenile: Brown 1965 approximately-six-week nestling in a broad old raptor stick nest. Smaller and low-crouched, both feet and belly fully supported by sticks and a shallow natural nest surface. Pale grey down partly hidden by fine grey-and-white juvenile barring; plain white thighs; a black streak on each side of the face; almost-black eyes with long dark periocular bristles; pale blue-grey bill; yellowish-white feet; paler orange-pink upper eyelids than adults. Weak short tufts. Folded wing compact and down-softened, fine juvenile barring but no crisp adult scapular spots/layered adult remiges; tail short/mostly hidden. Calm day posture; no walking, wing-flapping or flight in the still plate.

Environment: East African open woodland in a tall mature tree, large reused open stick nest originally built by a raptor; warm early light, distant woodland, no invented eggs/prey/lining.

Negatives: no yellow/orange adult irises; no missing pink lids; no huge ear tufts; no exaggerated female; no generic white fluff ball; no adult-spotted juvenile wings, long tail or flight; no extra bird/egg/prey; no unsupported chick; no title/label misspelling.

## Validation

Exact title/count/labels; adult almost-black eyes and vivid pink lids; pale huge eagle-owl structure and subtle sex direction only; juvenile approximately six weeks with Brown's fine barring/plain thighs/cheek streak/pale bill/feet/paler lids, compact soft wing, hidden tail and full stick-nest support. PASS_WITH_LIMITATIONS only; exact individual age, continuous feather sequence, flight threshold and adult sex ratio remain unknown.

## Actual image review

- Initial image was inspected at full available resolution; adult pink lids were too thick/cosmetic and the juvenile folded wing too crisp/adult-layered.
- Edit 1 softened the juvenile wing but overcorrected the adult lid rim to near-absence. Edit 2 restored a narrow natural rose upper-lid rim while preserving the juvenile correction.
- Final full master and adult/juvenile crops were actually inspected. Exactly three birds, stable supports, diagnostic dark eyes/lids, subtle adult scale direction, and a supported approximately-six-week juvenile passed the stated boundary.
- Result: `PASS_WITH_LIMITATIONS`; edit count 2; `scientifically_verified=false`. Review: `research/reviews/55-bubo-lacteus-v5-review.md`.
