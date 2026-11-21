# Run262 real browser source-gating diagnostic correction (post-run interpretation)

**2026-11-21, independently reviewed actual screenshots and the run's browser-visible page text. NO_RELEASE.** This is an additive research note; the original machine logs/screenshots remain immutable and their labels are not retroactively altered.

Run262 Actions: https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44871496985  
Artifact ID: 14694028743; ZIP bytes: 5,096,432; SHA256: `adef7e7a8c4c93e5096eeb31c1417c2da234655e31c3271cb7f3ce7d7cf4ce4c`. Independently downloaded ZIP, verified whole ZIP digest matched GitHub, 23/23 archive members passed CRC. Browser screenshots were opened in addition to machine JSON.

## image-to-3d.app: apparent free/anonymous source generation is *not* actually usable without login

Run262 machine label `FREE_QUOTA_OR_PAYMENT_OR_GENERATION_ERROR` is too broad and **does not establish quota exhaustion**. Screenshot `image_to_3d_app/source_uploaded_actual_browser.png` showed the site's overlay: **"Sign in to upload and generate"**. Its existing promotional page continued to display a sample futuristic soldier, not #172's uploaded chick. Although Playwright reported a file-input set and clicked a button, the service had not accepted an actual source-bound generation request. A nonspecific visible footer "Upgrade to Pro" can trigger the old detector. Corrected interpretation: **AUTH_REQUIRED / NO_ACCEPTED_IMAGE_TO_GLB_JOB / NO_NEW_GLB**. We did not register, log in or pay.

## supavoxel: legitimate input was visually uploaded; first run mistakenly skipped free generation control

Run262 machine label `POST_UPLOAD_ACCESS_GATE` is also **not evidence of a real credit-card gate**. The actual screenshot `supavoxel/source_uploaded_actual_browser.png` shows the white downy #172 chick in the input pane and a green enabled **"Start Creating"** button. The initial detector searched an overly broad phrase `card required` inside user-facing text such as **"No credit card required"**, which can incorrectly reject a free path. The proper interpretation is **UPLOAD_CONFIRMED / CLICK_NOT_ATTEMPTED_DUE_TO_FALSE_POSITIVE_GUARD / NO_NEW_GLB**.

Run262p on a new scope-limited branch restricts to SupaVoxel and corrects the false-positive guard, preserving the exact SHA256-pinned source. It will attempt only the real enabled free control and refuses account/payment/captcha bypass. Its runtime result must be inspected independently before anyone claims that a model was generated.

## Acceptance discipline

- The 512 x 512 rightmost-juvenile reference SHA256 remains `e439928a9ef08d3be266106cb5f2766b6f5a9f2c414d44e8da55ba81732153b8`.
- A successful GitHub Actions job or vendor "free" claim cannot establish the existence, visual quality, commercial rights, phone GPU performance or deployability of a GLB.
- This note is only in a separate research branch; no root vocabulary game, kitten WebGL prototype, 251-species production process, deployment or `main` modification. Extra paid external tools: **USD 0**.
- Both sites require fresh rights checks if a usable asset is eventually produced.

**Art verdict remains ART_UNREVIEWED / NO_RELEASE (zero valid new models).**
