# 20261127T1106Z 本次六轮实际生产审查

本次6轮：新增0种、修订6组，唯一归档207/251，219编号资产、1353个编号版本（不同版本不重复计物种），44种尚未归档。9次实际内置imagegen（110/130/134各2次），三次首稿均独立保存，非额外物种或子轮。启动2026-11-27 19:05:32 +0800，生产第1轮started_at 2026-11-27T11:08:00.436Z，第6轮verified_at 2026-11-27T11:27:48.722Z；本汇总整理至2026-11-27T11:29:37.480Z。先补旧1030Zcycle6，关闭旧批次；再新1106Zcycles1–5，当前5/6,next_cycle6，其他PARTIAL0，无有效lease。当前批次未满6/6，不称本次将新批次六轮完成。

| 本次子轮 | 批次／子轮 | 编号版本／原图 | 实际检查结果 | VERIFIED提交 | 运行记录 |
|---|---|---|---|---|---|
| 1/6 | 20261127T1030Z / 6 | [165-ninox-punctulata-v8](../../design/originals/165-ninox-punctulata-v8.png) | PASS_WITH_LIMITATIONS；science=false | [ad2f39c159](https://github.com/janeytlin-eng/game-owl-ket/commit/ad2f39c1596cc7ae36bc690223c5c33598291c22) | [run](../runs/20261127T1030Z-cycle6-20261127T1106Z-165-ninox-punctulata-v8.json) |
| 2/6 | 20261127T1106Z / 1 | [110-megascops-barbarus-v15](../../design/originals/110-megascops-barbarus-v15.png) | NEEDS_REVISION；science=false | [94bfaa9195](https://github.com/janeytlin-eng/game-owl-ket/commit/94bfaa9195fe5217956a2bd7e26895928839d45b) | [run](../runs/20261127T1106Z-cycle1-20261127T1106Z-110-megascops-barbarus-v15.json) |
| 3/6 | 20261127T1106Z / 2 | [130-megascops-koepckeae-v10](../../design/originals/130-megascops-koepckeae-v10.png) | NEEDS_REVISION；science=false | [8e8effb28c](https://github.com/janeytlin-eng/game-owl-ket/commit/8e8effb28ce4a7255c1d0bcf0f8959ae75524151) | [run](../runs/20261127T1106Z-cycle2-20261127T1106Z-130-megascops-koepckeae-v10.json) |
| 4/6 | 20261127T1106Z / 3 | [134-megascops-sanctaecatarinae-v10](../../design/originals/134-megascops-sanctaecatarinae-v10.png) | NEEDS_REVISION；science=false | [3a6c9e80ff](https://github.com/janeytlin-eng/game-owl-ket/commit/3a6c9e80ff921fbf2925549004113383f7885ba9) | [run](../runs/20261127T1106Z-cycle3-20261127T1106Z-134-megascops-sanctaecatarinae-v10.json) |
| 5/6 | 20261127T1106Z / 4 | [167-ketupa-poensis-v7](../../design/originals/167-ketupa-poensis-v7.png) | PASS_WITH_LIMITATIONS；science=false | [aa94af3345](https://github.com/janeytlin-eng/game-owl-ket/commit/aa94af3345574b88b7bb7765ac61f4a2d741cc6f) | [run](../runs/20261127T1106Z-cycle4-20261127T1106Z-167-ketupa-poensis-v7.json) |
| 6/6 | 20261127T1106Z / 5 | [168-ketupa-leucosticta-v7](../../design/originals/168-ketupa-leucosticta-v7.png) | PASS_WITH_LIMITATIONS；science=false | [55fb7bdd52](https://github.com/janeytlin-eng/game-owl-ket/commit/55fb7bdd52d0c5fbb1d5c08f5ca1d1bf5721fb52) | [run](../runs/20261127T1106Z-cycle5-20261127T1106Z-168-ketupa-leucosticta-v7.json) |

全部研究、来源ID、对应页码、完整首图及编辑提示、各阶段实际UTC时间、字节/SHA256及PNG解码结果位于逐轮run；审查在 research/reviews 对应编号。归档验证通过并不等于生物学或艺术校准通过。

## 来源与科学边界

知识库 [SOURCE_INDEX.md](../../research/SOURCE_INDEX.md) 已逐轮增量提交：新增来源0；复用15次稳定ID引用，去重11ID；其中Brosset1986一项仅历史复用且本次原文访问失败，14次引用为本次实际正文／照片读取支持。图鉴KOEP别名归入同一本书、Tobias两个定位ID归入同一论文，9个来源家族中8个本次实际读到，1个历史未恢复。实际新增访问证据1（165原论文Fig3A像素），无新增书目纠错。上传Mikkola2013本次实际printed485/214/222/239/284/278页；图鉴不独立替代发展研究。

165暗色幼头更紧凑但腹部残余曲线仍待校准；167成年裸趾由暖灰转蓝灰；168成年最低白腹转少量独立小斑为局部PWL。110/130/134各两次实质编辑后闭合卷纹仍未解决，134浅眼周羽缘不足，均NEEDS_REVISION，保留初稿及失败过程。全部scientifically_verified=false，新用户确认0，保留旧版本及其特定确认范围。幼鸟日龄、飞行、虹膜／喙／翼羽时序及精确性别体差不补猜。168幼绒材质未解决，待其自身照片校对；不能用165部分改善宣称已解决其他种。

## 阶段时间（实际UTC，可加8小时）

| 编号 | STARTED | RESEARCH_READY | IMAGE_GENERATED末次 | REVIEWED | ARCHIVED | VERIFIED | 实际生成等待秒（含编辑） |
|---|---|---|---|---|---|---|---|
| 165-ninox-punctulata-v8 | 2026-11-27T11:08:00.481Z | 2026-11-27T11:08:13.112Z | 2026-11-27T11:10:07.814Z | 2026-11-27T11:10:12.912Z | 2026-11-27T11:10:17.782Z | 2026-11-27T11:10:46.275Z | 37.982 |
| 110-megascops-barbarus-v15 | 2026-11-27T11:11:16.244Z | 2026-11-27T11:11:20.896Z | 2026-11-27T11:13:49.537Z | 2026-11-27T11:13:56.216Z | 2026-11-27T11:14:01.369Z | 2026-11-27T11:14:32.608Z | 80.968 |
| 130-megascops-koepckeae-v10 | 2026-11-27T11:14:45.615Z | 2026-11-27T11:14:50.607Z | 2026-11-27T11:17:18.433Z | 2026-11-27T11:17:24.969Z | 2026-11-27T11:17:30.625Z | 2026-11-27T11:18:08.652Z | 82.362 |
| 134-megascops-sanctaecatarinae-v10 | 2026-11-27T11:18:20.234Z | 2026-11-27T11:18:27.055Z | 2026-11-27T11:20:58.154Z | 2026-11-27T11:21:04.208Z | 2026-11-27T11:21:09.677Z | 2026-11-27T11:21:37.677Z | 78.441 |
| 167-ketupa-poensis-v7 | 2026-11-27T11:22:35.352Z | 2026-11-27T11:22:41.475Z | 2026-11-27T11:23:52.445Z | 2026-11-27T11:23:57.549Z | 2026-11-27T11:24:03.072Z | 2026-11-27T11:24:35.505Z | 39.763 |
| 168-ketupa-leucosticta-v7 | 2026-11-27T11:25:40.097Z | 2026-11-27T11:25:45.535Z | 2026-11-27T11:27:12.533Z | 2026-11-27T11:27:17.691Z | 2026-11-27T11:27:22.461Z | 2026-11-27T11:27:48.745Z | 42.743 |

生成工具等待总计362.259秒。阶段间隔包含工具、上传及人工实际阅图，不能等同纯计算时间；研究部分在STARTED前已有实际阅读，故STARTED→RESEARCH_READY不代表全部研究耗时。完整时间戳保存在run，阶段次数不算子轮。重复材质失败是本次主要质量瓶颈（3种×2次仍未解决），继续相同边缘否定词未验证有效；成年局部皮肤或斑纹变化较明确，但未据此推断通用性能。后续优先换证据明确的待修／未归档项目，材料问题需要不同构图重建或局部策略且仍须实际生成检验，未声称部署API或模型训练。

## 实际错误与恢复

- Preflight connected GitHub contents ledger returned Transport closed (4MB); immutable raw full read recovered. Root AGENTS.md404 is absent, owl-pet/AGENTS.md read. Incomplete crop165 initially included adjacent panels, correctly clipped panelA only beforeimagegen.
- PublisherPDF web400 too large for OConnell36705500bytes/Alarcon34951163bytes; actual fulloriginal localPDF texts/renders read. Persee only viewerchrome/no leucostictus body; blockedhistorynotfreshsource.
- 167/168 initial originals path404 because previous master underproduction/generated &concepts; exactconceptpathsfound tree thenfullbytesdownloaded/viewed. No connectionfailure.
- 167 VERIFIED immediate refreadback mismatched; subsequentfreshref+commit+immutableVERIFIEDrunexit0provedaa94af3345574b88b7bb7765ac61f4a2d741cc6f. Refinedhelperrepeatcheck; freshledgerloaded/credit exactlyonce4f258632e92d69fb0eda9cb874d83cb9de1decb3. No repeatedgeneration/cycle.
- 110/130/134 eachtwoactualedits failedmaterialfix; initialattempts preserved. Noartsciencepassclaim.
- fd9d70d422NoCommitFound; #25localfilepresent and correspondingremotepriorblobalreadyarchived, no duplicateproduction.

第25组本地可恢复，远端原有正确blob10508841ef5f6184e8658664615302909765c1dd保留；未重新制作。上次六轮仅补[汇总恢复入口](20261127T1030Z-six-cycle-review.md)，不计本次成果。

## 下一步

接续1106Z第6轮；有效lease则避重，过期时核对已归档run再续。110/130/134待修，165余留材质及168幼羽需来源限定校对，剩余44种按既有研究缺口选可证实阶段，不能拿成人标本充幼鸟。固定251全名录仍有权威对照待办，当前207为仓库学名去重覆盖审计，不宣布全球分类更改。全清单、集中整批科学审查尚未完成，不暂停其他任务／本生产安排；没有后台执行或ETA声明。
