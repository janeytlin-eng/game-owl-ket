# 2026-11-27 本次六轮生产与实际复查

本次完成6个完整生产子轮（研究、实际imagegen/查看、必要复修、原图/资料归档、回读验证），新增物种0，修订6组；其中2组局部形态修订有效（78眼周/84冠部）、3组仅证据边界标识（80/81/82）、1组纹理修订未解决（79），NEEDS_REVISION保留，不能称六组科学校准通过。总覆盖207/251不变，剩44。编号PNG版本1160→1166，非物种数；名录完整对应及整批科学审查尚未完成。

原20261126T1630Z-B2本次贡献cycle4–6，跨次补齐6/6；当前20261126T1734Z-B2累计3/6,next4；其他有效PARTIAL0。本次实际6轮跨两个批次，不声称任一批次全部本次完成。全部sciencefalse，新用户确认0。旧版本/旧确认未删除。

|本次轮|版本|原图|归档commit|验证commit|
|---|---|---|---|---|
|1/6|78-asio-capensis-v7|[原图](../../design/originals/78-asio-capensis-v7.png)|[af993981](https://github.com/janeytlin-eng/game-owl-ket/commit/af9939810697c6a99584f6696326675b177981e7)|[86ee0639](https://github.com/janeytlin-eng/game-owl-ket/commit/86ee06398c6701bfb1389ee3b79a1133f93677f3)|
|2/6|79-otus-lettia-v7|[原图](../../design/originals/79-otus-lettia-v7.png)|[bdf04101](https://github.com/janeytlin-eng/game-owl-ket/commit/bdf04101f8f57ba41c2f2a88d815790f912148ae)|[b8ae1658](https://github.com/janeytlin-eng/game-owl-ket/commit/b8ae16587616a425410ece98c0b0412bf45dec3d)|
|3/6|80-otus-sunia-v7|[原图](../../design/originals/80-otus-sunia-v7.png)|[c459a32f](https://github.com/janeytlin-eng/game-owl-ket/commit/c459a32f19b538bc2d39318f2636be030e8ddb87)|[507c5cd9](https://github.com/janeytlin-eng/game-owl-ket/commit/507c5cd94e5257bfddcc8aeae7a2224cc464391c)|
|4/6|81-otus-scops-v7|[原图](../../design/originals/81-otus-scops-v7.png)|[43b275ab](https://github.com/janeytlin-eng/game-owl-ket/commit/43b275abac17b9d4759a855f7169a1ef80a9fbce)|[8270843b](https://github.com/janeytlin-eng/game-owl-ket/commit/8270843bdc5d34ad0381d9c18b1d270e2e543e19)|
|5/6|82-otus-senegalensis-v7|[原图](../../design/originals/82-otus-senegalensis-v7.png)|[30298650](https://github.com/janeytlin-eng/game-owl-ket/commit/30298650ac7f35c7b68582173209cb155b7c5605)|[ce573e3e](https://github.com/janeytlin-eng/game-owl-ket/commit/ce573e3e0174fef4cbbc02a45c0336c938644e04)|
|6/6|84-otus-bakkamoena-v10|[原图](../../design/originals/84-otus-bakkamoena-v10.png)|[27106da6](https://github.com/janeytlin-eng/game-owl-ket/commit/27106da6b207f7db8270638f9f149bd9e35e8c13)|[014e0b48](https://github.com/janeytlin-eng/game-owl-ket/commit/014e0b48b4692a40e8f949e808fa1165dc4420ed)|

## 研究和索引
[SOURCE_INDEX](../../research/SOURCE_INDEX.md)实际增量提交。新1 SUNIA-IRBJ-603-CURRENT；复用15次来源引用，16次引用去重12份文献/网页（图鉴同一本书只计1），其中82 Riekert1986仅复用历史已读记录，不是本次重新阅读全文。78/79/81/82/84实际重读上传图鉴印刷518/156/122/130/150页（PDF+2）；80使用机构身体/名称映射与临床记录，不声称新读图鉴或照片像素。当前外部网络检索逐轮实际执行，搜索命中与正文读取分开。来源定位/局限/旧名、事实与设计推断及完整一/二次提示见[物种研究](../../research/species/)，逐轮实际审查见[reviews](../../research/reviews/)。本次未把任何新照片像素作为已检视依据。

- 78：guide518/OWLpages3610 Description64–68支持成年眼周暗褐；Ansara2008出版社摘要只支持质量/尾长方向，不是高度倍率。成年内眼区不同于外盘缘，局部修改实际有效。
- 79：guide156/BSS Identification支持幼鸟窄而不规则横斑；实际v6反复闭环羽丝，连续两次编辑仍存在。保留[首尝试](../attempts/79-otus-lettia-v7-first1734Z.png)、最终v7/两完整提示及失败复查，优先修订队列；不把增加footer当解决羽纹。
- 80：新IRBJ临床幼鸟尺骨骨折记录是病理个案，不能推导正常首飞；BIRDFAN名称与Kyoto机构正文重读，保留先前纠正semitorques误归因。仅图上补科学状态/年龄首飞比例未知，不改已照片支持的较晚幼鸟翼。
- 81：Grieco2025出版社摘要反映研究中离巢后移动，不测定图中个体日龄；把RECENTFLEDGLING改AGE-UNKNOWN JUVENILE，支持的自然一步姿势保留。
- 82：原22-DAY STUDY NESTLING让源文个案年龄看似赋给生成羽翼；改STUDY-REFERENCED NESTLING+illustratedageunknown。1986PDF新访问无可读字/screenshotplaceholder、localGET403且找不到本地渲染，1987publisher403，未当已读。保留历史研究依据，不改变幼鸟发育形态。
- 84：guide150成年冠深于背与新读BrraichSingh2021原始55–56页单窝记录共同界定设计。成年冠暗底/浅斑减少有效，幼鸟蓝灰眼/无角/弱翼不改；未把观察日期当孵化日期，木箱案例与天然洞概念场景区分。

## 实际阶段、工时、错误
六run均实际含STARTED/RESEARCH_READY/IMAGE_GENERATED/REVIEWED/ARCHIVED/VERIFIED，阶段数不当子轮数。各图不可变归档SHA的原图与concept两路径GET，完整字节长度/SHA256/PIL解码通过，研究/审查回读。最后完整tree未截断，六双路径一致，全部最新sciencefalse。精确总研究耗时未知（部分预读在STARTED前），下表为实际记录可测值，归档至验证包含检查/编排，不假装纯上传耗时。

|版本|首次imagegen等待秒|第二编辑等待秒|ARCHIVED→VERIFIED秒|
|---|---:|---:|---:|
|78-asio-capensis-v7|68.444|0|31.45|
|79-otus-lettia-v7|39.322|38.922|22.33|
|80-otus-sunia-v7|34.999|0|37.39|
|81-otus-scops-v7|35.921|0|13.62|
|82-otus-senegalensis-v7|36.349|0|14.34|
|84-otus-bakkamoena-v10|42.345|0|25.22|

错误与恢复：78单次exec stdout静默截断base641048607字符，第一中间blob无效；在任何ARCHIVED/信用前，用500000字符有界分块拼合完整3709188字符、重传后双路径2781891字节/SHA256/全解码通过，保留实际错误。3.96MB账本contents两次Transportclosed，fetch_file空内容，改用不可变raw下载+8有界片段核对；不当连接永久不可用。执行存储load返回副本导致78后写run遗漏中间阶段，按真实阶段commit重建日志，未伪造时间；重建证据在run。82 RESEARCH_READY提交GraphQL临时错误（17:51:09Z request0565:3268F:721602:1640EC9:6B08718C），核对main只有STARTED后重试成功，无重复出图。无审批拒绝，无平台超时遥测。生成总7次（79两次），不是6个新物种。

#25本地production1030/25-glaucidium-brasilianum-cactorum-v6.png2864437字节/SHA256729c187af12da587305c0c701c07440464896f5a6ada74431dfa3e7b19616ca1，gitblob10508841ef5f6184e8658664615302909765c1dd与当前远端concept一致，可恢复但已归档，不重复制作；fd9d70d远端git/commits本次404，不能声称真实远端成功。

## 自我迭代与接续
实证有效：78内眼区与外面盘缘拆开检查；84冠与背分区比对。应用未有效：79两次只改纹理提示仍保留闭环羽丝，后续需更强实物纹理参照/局部策略，禁止声称规则验证成功。81/82重新区分研究时间与图中个体年龄，仅证据标识有效；回查80/84年轻阶段不因未知年龄统统回滚为短翼绒球。79近邻旧81/82也可见若干卷曲羽丝，列后续候选纹理核查，未执行修改，不宣称通过。当前下一子轮20261126T1734Z-B2第4轮，应优先79未解纹理或可靠缺种资料；保留批次，不重新1/6。交付后释放lease，不声称后台绘图。全251/集中科学审查未完成，未修改调度或其他任务。
