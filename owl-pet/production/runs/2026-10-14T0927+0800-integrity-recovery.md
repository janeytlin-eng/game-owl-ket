# Binary integrity recovery — 2026-10-14 09:27 +08:00

Result: PARTIAL production / VERIFIED archive repair.
Batch: 2026-10-14T0430+0800; next_cycle remains 5; no new cycle credit.

## Problem — evidence — correction — recheck
Previous #61 and #62 upload calls read base64 through a bounded shell output. The uploaded Git blob differed from the full original local git hash-object. Merely re-reading that same incorrect remote blob was circular validation.
- #61 old blob 3bc3bd2016fb2bfaf722cfd54b5fa65fd8de0544; correct full original df8c972aa06904bab4737179b0c3918d9c614570, 2895564 bytes.
- #62 old blob 477558057d4e40ac26cac4c3db91e451b7189523; correct full original 6ad2775f8a876b3ab7d4e3cf771a1ed1a7e5816a, 3014149 bytes.
Read local files in 90000-byte chunks (divisible by 3), assembled complete base64, uploaded blobs, required returned SHA to match independent local Git hash before tree/ref update.
Repair commit: 5efc1da49e062dc6e6b510ffeec20081c05c06ce.
Remote concepts-directory readback returned both exact hashes and full byte sizes. Original PNG pixels and manifest SHA-256 remain unchanged; old corrupt blobs remain recoverable in history.
The prior VERIFIED claims for binary transfer were incorrect and are superseded by this repair record.

## Research recheck
Re-read https://besgroup.org/2016/05/03/buffy-fish-owl-nesting-in-a-birds-nest-fern/ on 2026-10-14: body paragraphs/photo captions support down-covered resting nestling in Asplenium nidus; exact age unknown.
Re-read https://singaporebirds.com/species/barred-eagle-owl on 2026-10-14: Identification supports pitch-black adult eyes, yellow bill, outward tufts; juvenile white ground with dark bars. Exact juvenile wing-length inference remains unvalidated.
Reused source IDs BFOW-BESG-NEST-2016 and BEOW-SGBIRDS-2026; no duplicated sources.

## New verification rule
Require independent local Git blob hash == create_blob SHA == remote directory SHA, plus byte size; then PNG full decode. Never treat a returned remote SHA alone as evidence of an untruncated upload. Applied successfully to #61/#62 archive repair; not yet tested for new production.
No new image or scientific revision generated in this run. Cycle 5 research/generation/review is unfinished. No platform timeout telemetry observed; this record does not assert a platform limit.
