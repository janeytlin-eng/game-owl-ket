# Manifest integrity repair — #165 Speckled Boobook

- Time: 2026-10-27T16:35:30.000+08:00
- Scope: metadata integrity only; not a production cycle and not a new species count.
- Finding: `design/concepts/165-ninox-punctulata-v1.png`, Git blob `87ac0f12f1843c6703f890d8b3241c9804e649fa`, archive commit `3210c304fbc4690dbf747f81e25eef1e3fccf3c7`, and verification commit `ea63f1a7a1ace898e244cffc21299d4e6830b0de` existed, while `design/manifest.json` omitted the corresponding entry.
- Repair: added the #165 manifest record and appended an audit note to the batch ledger and original run record.
- Count effect: none; #165 was already a unique archived species. Multiple versions are still de-duplicated by species.
- Scientific status: unchanged; `scientifically_verified=false`.
