# #172 Run218–219 independent native GroomLab feasibility audit — NO_RELEASE

**2026-11-19 UTC · #172 Tyto castanops v3 rightmost age-unknown cream mesoptile · added paid cost $0.** Research only; this is neither a newly accepted model nor the 251-species production workflow.

## Preflight and artwork boundary

Re-read the existing cat-only owl-pet prototype, `AGENTS.md`, `README.md`, `STATUS.md`, the species v3 research boundary, and Run216–217 trial records. Exact v3 concept plate hash from CI: `881dec86e0e66ab2ad0781db86a3b719b35e710d2be1a1606d761a9d0908483d`, 737545 bytes. The goal remains authentic cream down, natural heart-shaped facial disc, believable juvenile proportions and anatomical continuity around all sides, concealed wings and tail, and fully supported feet on a broad eucalyptus hollow lip. No exact-age assumption.

Prior attempts Run207–216 produced no aesthetically accepted owl juvenile; Run217's [real evidence](../172-tyto-castanops/run217-evidence/run217_report.json) shows upstream Apache-2.0 `GroomLab` cloned and CMake configured, but an overly broad CLI compilation timed out after 470s. The green CI job represented collection of failure evidence, not a compiled tool.

## Run218: genuinely successful native, zero-extra-fee tool compilation

[Actual GitHub Actions job](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44559916897) completed successfully. Changed the original full development build to a lean native CMake/Ninja Release compilation with tests, Alembic, Python, GUI/Blender helper and nonessential exporters disabled, checked out the exact upstream `5e81163e3520e14e99f001c41c441f85a186daf9`, and obtained **156/156 successful build steps in 145.62 seconds**. Verified actual binary `groomlab-cli 0.49.1 (TBB on, Alembic off)`, ran `--list-operators`; genuine operator registry includes `Plume`, `FeatherColor`, `Cards`, `Guides`, `Interpolate`, `Clump`, `ToMesh`, and others.

Remote actual [Run218 report](run218-evidence/run218_report.json) has all commands, exit codes, log lengths, cryptographic hashes, timestamps and complete source log files. 30-day [Actions evidence artifact #14548447254](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44559916897/artifacts/14548447254), 8667 compressed bytes, SHA256 `8357b3bd3d245422a5de3e84cb22c0044267d9708a2a0b65edb94c31eb116548`. **This artifact is logs only, not a character and not even a compiled executable.** Script [run218_lean_groomlab_cli.py](run218_lean_groomlab_cli.py) is independently reproducible.

## Run219 actual runtime evaluation submitted; no result implied yet

A separate isolated [Run219 Actions build and MCP runtime](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44561843568) was submitted and its queued/in-progress status checked. Source and workflow are committed on the isolated research branch: `run219_groomlab_actual_fur_mcp_trial.py`, `.github/workflows/owl172-run219-groomlab-native-fur-test.yml`. This experiment actually builds the same lean CLI, uses its own JSON-RPC MCP server to call `list_sample_meshes`, `list_presets`, `new_groom`, `evaluate`, `save_groom`, `render_preview` in five true spatial camera views and `export` to native USD curves, and checks source-byte sizes and hashes **if** it reaches those stages. The test subject is explicitly GroomLab's `wolf` example, separately credited to **Nick Rutlinh / GroomLab, CC BY 4.0**, **NOT a Tyto or pet model**. The native .groom, USD and preview (if any) are isolated in 30-day Actions evidence, while text diagnostics attempt persist only to research branch.

At this audit's writing, the Run219 report `run219-evidence/run219_report.json` was **not yet remotely accessible (404)**, and the workflow was in progress. Therefore **no claim** that actual groom generation, five-view fur preview, export, or any owl GLB succeeded.

## Quality and isolation gate

**Run218 NATIVE_OPEN_SOURCE_CLI_TECH_PASS / Run219 PENDING_VERIFIED_EXECUTION / NO_NEW_TYTO_GLB / NO_ART_PASS / NO_PHONE_HARDWARE_WEBGL / NO_RELEASE / NO_NOTIFICATION.**

Native grooming tooling is technically more promising than repeatedly using a programmatic sphere/needle hair pattern, but a CLI build is not a legitimate 360-degree young Tyto sculpt, high quality down or a mobile-ready electronic pet. No service charge or payment was made. The only repository changes are this experiment's dedicated research source, workflows, log/report files and audit on a research branch; production main, prior prototype, 251-species pipeline and deployment remain untouched.

Next art-critical need remains a real, lawful, reconstructable artist-grade juvenile masked-owl base mesh with natural heart facial structure; the separately tested groom system would only address finishing the feather material and LOD after that anatomical prerequisite.

## Run219 post-execution correction (verified from original artifact, 2026-11-19 16:09 UTC)

[Run219 workflow](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44561843568) did execute and finished its diagnostic/archival steps. **This is NOT a runtime groom success.** Its actual final script output was `{"status":"FAILED_NO_RELEASE","files":{}}`, logged in the original CI job. [Artifact #14549916838](https://github.com/janeytlin-eng/game-owl-ket/actions/runs/44561843568/artifacts/14549916838), 7224-byte compressed ZIP, GitHub SHA256 `419888a2a7d32ea9255cecf7e6ed01b6d95b3be701e33a3e9afa199f43d80c3d`, was downloaded, opened and inspected. The report says clone, CMake, CLI build and version checks all completed, but MCP `list_sample_meshes` and `list_presets` received invalid JSON. The immediate Python error was `RuntimeError('GroomLab own CC BY 4.0 sample wolf unavailable')`.

Root cause identified from upstream `engine/cli/CMakeLists.txt`: **MCP server and GroomScene sources are included only when `TARGET groomlab_alembic` exists**. Run219 copied Run218's lean `GROOMLAB_BUILD_ALEMBIC=OFF`, so the CLI binary could not possibly run a real MCP groom: it fell back to CLI usage text, which the Python client incorrectly attempted to parse as JSON. Thus no wolf 3D groom, PNG preview or USD export was made, and no Tyto model. The green GitHub job only signifies deliberate failure evidence collection.

The GitHub Actions job's own research-report push failed non-fast-forward because a separate audit commit advanced the branch concurrently; therefore its text diagnostics were **not persisted in the research branch**, only the correctly attributed original artifact and this corrective audit are durable evidence. Run220 independently tests the corrected `GROOMLAB_BUILD_ALEMBIC=ON` build on a new research branch. No payment and no production changes.
