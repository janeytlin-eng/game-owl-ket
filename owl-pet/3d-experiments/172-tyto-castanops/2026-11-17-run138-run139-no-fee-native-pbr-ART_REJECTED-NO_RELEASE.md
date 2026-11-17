# #172 Tyto castanops v3 — actual Run138–Run139 free texture-aware image-to-3D results
**Research recorded 2026-11-17 18:40 Asia/Shanghai. Final art decision: ART_REJECTED / NO_RELEASE. Not a user-facing pet sample.**

## Required preflight, source lock and scope
Re-read `owl-pet/AGENTS.md`, `owl-pet/README.md`, `owl-pet/prototype/index.html`, `owl-pet/research/species/172-tyto-castanops-v3.md`, Run137–137C actual prior GLB four-angle rejection, and known rejected asset SHA registry. The old pet prototype is a cat, not a finished owl. Source is unchanged original **rightmost** v3 cream-fluffy age-unknown mesoptile RGBA, 512×512 SHA256 `e439928a9ef08d3be266106cb5f2766b6f5a9f2c414d44e8da55ba81732153b8`. Reference target is open dark eyes, rounded heart disc integrated into fluffy head, cream down, short buried wings, concealed tail, squat body and both feet supported on eucalypt hollow lip. Exact age and unseen sides remain unverified.

## Run138 — actual free browser attempts; no GLB
Independent branch `research/owl172-run138-alternate-no-fee-web-3d`; [real workflow 44065902475](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44065902475).
- Upsampler's no-signup converter received genuine pinned input via Chromium Playwright, and the visible `Convert to 3D` button was clicked. After asynchronous browser wait, neither a valid downloadable GLB nor matching binary response was obtained: `PUBLIC_UI_REQUEST_FINISHED_NO_VALID_GLB`. Initial/post-upload/final UI text and screenshots archived.
- image-to-3d.app opened, but Playwright screenshot timed out. A `preview.glb` HTTP 200 response was observed but response body was already evicted from inspector cache; it is not a verified generated model, and no generation button was clicked there. Status `ACTUAL_PUBLIC_BROWSER_ERROR`.
- No Blender models/renders invented; `run138_native_skipped.txt` documents the strict stop. Source PIN, browser result JSON, screenshots/errors, SHA256SUMS and successful checksum verification archived; no payment or login bypass.

## Run139 / 139B — genuinely obtained a new textured 3D GLB
Independent branch `research/owl172-run139-3dvalley-actual-free-trellis2`. Early workflow YAML job-name/branch errors were fixed before a runnable job. [Run139 actual source upload but no click 44066200630](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44066200630) verified the normal free 3DValley public UI after source upload, revealing exact button text `Make 3D model`. This was patched; [Run139B successful real generation / Blender 44066390229](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44066390229).

Via standard public, no-signup **free TRELLIS.2 Standard UI**, clicked `Make 3D model` once and captured a real `application/octet-stream` GLB response. Real source PBR mesh:
- Binary SHA256 `9a154c9e3aeebb34ebcd6f209760e1d9e21e2f544f2b690dae406d9c8bf878e8`
- **9,983,448 bytes, 192,765 triangles, 1 mesh, 2 texture images, 2 textures, 1 material, 0 animations**; different from all already rejected GLBs (including Run137 SHA `b65fe7ca...`).
- Blender **4.0.2** actually imported the exact binary and produced **four actual Cycles renders at front/45°/side/back** and a full four-view JPG. JSON mesh inspection and screenshots/checksums persisted, original binary quarantined in Actions artifact **14321440568**, with 30-day retention. Do not redistribute the unreviewed GLB from public repository.
- No money was paid; the site offers daily free generation, then 5 credits paid; this run used only the free public action. The site claims free-model output ownership on page, but no full independent IP/commercial-use audit was done, hence license/release remains UNVERIFIED.

## Actual visual review against the real rightmost chick: **REJECTED**
I actually inspected the 4-view Blender contact sheet and original pinned source crop. Run139B is materially improved compared to Run137's blank rough greyscale neural shell: an identifiable rounded white owl, an actual broad heart-shaped face and some plausible volumetric feathers, with valid front-to-back geometry and embedded texture. **That is not enough for this demanding juvenile quality gate:**
1. **Front / eyes:** generated dark eyes are half-shut/narrow and irregular, while original has large, clean, dark **open** eyes. The mask is heavily outlined and too rigid. Facial proportions and beak are no longer source faithful.
2. **45° and full side:** long conspicuous adult-like wing flight-feather projection and a visibly **long tapered tail** replace down-buried stub wings and a concealed tail; silhouette is adult rather than a compact fluffy crouched juvenile.
3. **Back:** mottled nearly white surface is covered with noisy black specks and rigid flecks rather than soft cream second-down; no credible fluffy contour across all angles.
4. **Pose/support:** both paws/claws are distinctly exposed, appear unsupported by any broad old eucalypt hollow lip; no actual tree hollow geometry. Not a correct juvenile pet assembly.
5. **Product readiness:** raw 192,765 triangles/10MB, no rig or animation. True physical phone GPU performance, consistent mobile touch interaction, LOD, and complete rights still not proven.

**Decision ART_REJECTED / NO_RELEASE** for raw Run139 result. It is a **genuine textured GLB technical asset to iterate on**, not an accepted final 3D electronic pet. Light-colored surface / 3D loadability must not be misrepresented as natural cream fluff art approval; no user-facing image/sample/3D website deployment. A separate Run140 isolated experiment performs real Blender mesh reduction and simulated mobile Chromium WebGL QA; its results must be audited separately and cannot override this art gate.

## Isolation and evidence
Run138 base comparison to Run137C: 4 commits ahead, 0 behind, all changed paths under only `owl-pet/3d-experiments/172-tyto-castanops/**` and a single dedicated `.github/workflows/owl-pet-172-run138-*.yml`. Run139 comparison before this audit: 7 commits ahead, 0 behind, only #172 experiment paths and one dedicated `.github/workflows/owl-pet-172-run139-*.yml`. No `main`, original owl concept file, 251-species prototype automation, legacy cat pet or deployment modification. Both completed audit jobs ran SHA256 checksum verification and published quarantined 30-day evidence bundles. **Extra spend: zero.**

### Next discriminating art iteration
Do not retry these identical sources blindly. Priority: improve eye openness/face proportions, intrinsically down-buried short wings, invisible tail, backside down coat, genuine supported crouch. Only after true four-view human art acceptance and permitted asset rights, validate mobile WebGL on a real phone and share an actual working viewer.