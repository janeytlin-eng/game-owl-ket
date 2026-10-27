# Production invocation summary — 2026-10-28T0629+0800

- Batch: 2026-10-28T0508+0800
- Batch before: 2/6
- This invocation completed: 1 verified cycle
- Batch after: 3/6
- Completed species: #201 Mantanani Scops Owl · *Otus mantananensis romblonis* v1
- Action: NEW +1
- Unique archived species: 183→184/251
- Archive commit: `adcd5aeeae03e80d1dd60a0954f0f0fed86ab760`
- Verification commit: `08707c9cf53c8d0a7b5daa781277e82884dbccab`
- Next cycle: 4/6
- Active lease: none
- Other incomplete batches: none recorded in current ledger
- Science status: false

## Stage evidence

| Stage | Time (+08:00) | Evidence |
|---|---|---|
| STARTED | 06:29:50 | lease and run record committed |
| RESEARCH_READY | 06:31:25 | 4 new source IDs; full prompt and design boundary saved |
| IMAGE_GENERATED | 06:33:31 | 1536×1024 source viewed; durable generated blob `40a45307…`; observed imagegen wait 44.9 s |
| REVIEWED | 06:36:20 | one targeted edit; master and derivative viewed; reviewed blob `f4393d38…`; observed edit wait 102.2 s |
| ARCHIVED | 06:37:38 | concept blob `7263eab1…`, manifest 439→440, research/card/run/status/knowledge/workflow committed |
| VERIFIED | 06:38:36 | commit-pinned readback passed; ledger advanced to 3/6 |

## Research/index delta

- New: 4 (MSO-EBIRD-ID-2026, MSO-AVIBASE-ROMBLONIS-2024, MSO-PHOTOARK-BIR070-00063, MSO-MACAULAY-615554542)
- Reused: 0
- Corrected source records: 0
- Metadata correction: one REVIEWED-stage source/JPEG SHA-256 transcription was replaced with actual local `sha256sum` values before archive; no image byte changed.
- Uploaded Mikkola guide was not accessible through the connected Library in this run; no page number or unread guide content was claimed.

## Review/iteration

- Initial failures: adult ear tufts too high; juvenile right folded wing too long, narrow and adult-like.
- Edit: shortened adult tufts and replaced only the juvenile side wing with a compact down-covered contour; preserved labels, adult identity, scale, feet/support and scene.
- Recheck: both 1536×1024 reviewed master and 680×453 concept passed with limitations.
- Remaining unknowns: exact juvenile age, flight ability, continuous feather sequence, nest geometry, quantified sex-size ratio, cross-population juvenile generality and captivity effects. Science remains false.
- Workflow update: a directly viewed frontal juvenile can constrain visible soft parts but does not prove lateral wing maturity; unseen feather sequence must not be invented.

## Stop reason / recovery point

No platform timeout telemetry or permission error occurred. This invocation did not claim 6/6 because the next project identity could not be assigned safely from repository facts: the tree contains no canonical roster entries for 170–200 and only #201 above that range; stale STATUS priority mentions are superseded by later manifest versions. The external guide sequence after Mantanani includes species already archived under canonical IDs (#23 and #18), so guessing #202 risks duplicate credit. The ledger remains recoverable at batch 2026-10-28T0508+0800, next_cycle 4, with no active lease.
