# 20261124T1535Z 完成与集中审查入口

本次实际完成6轮，当前批次6/6；新增物种0，修订6组（5处形态细节修订、1处证据边界注释修订），不把修订版本重复计物种。项目现用去重归档206/251，尚45；编号原图1028→1034，manifest982→988。251完整权威名录仍未导入/对齐，未据新证据调整约定总数。

| 子轮 | 编号版本 | 实际变更 | 原图 | 依据与实际检查 | 验证提交 |
|---|---|---|---|---|---|
| 1/6 | 209-glaucidium-minutissimum-v4 | 幼鸟后顶白点收敛；额前零星斑保留 | [原图](https://github.com/janeytlin-eng/game-owl-ket/blob/1da291ab2ac4d64022b01644f3f7641bc14f33cf/owl-pet/design/concepts/209-glaucidium-minutissimum-v4.png) | [研究](../../research/species/209-glaucidium-minutissimum-v4.md) / [复查](../../research/reviews/209-glaucidium-minutissimum-v4-review.md) | [3b24e64](https://github.com/janeytlin-eng/game-owl-ket/commit/3b24e64ee1f88f9756f4d44d373c539ef341f87d) |
| 2/6 | 202-ninox-theomacha-v4 | 成鸟跗跖羽被延至趾基，趾与爪保持裸露 | [原图](https://github.com/janeytlin-eng/game-owl-ket/blob/6058dba20d844e6f96ea18a6cf2c05fa13d9221d/owl-pet/design/concepts/202-ninox-theomacha-v4.png) | [研究](../../research/species/202-ninox-theomacha-v4.md) / [复查](../../research/reviews/202-ninox-theomacha-v4-review.md) | [eb8056b](https://github.com/janeytlin-eng/game-owl-ket/commit/eb8056b014535478d1d1561dc8ebda76033d72e5) |
| 3/6 | 207-tyto-multipunctata-v4 | 成鸟爪片加深为暗角质色，幼鸟爪色未推断 | [原图](https://github.com/janeytlin-eng/game-owl-ket/blob/43b5cfc3cc13cc5aa3d093f12c917481f578233f/owl-pet/design/concepts/207-tyto-multipunctata-v4.png) | [研究](../../research/species/207-tyto-multipunctata-v4.md) / [复查](../../research/reviews/207-tyto-multipunctata-v4-review.md) | [c3ca067](https://github.com/janeytlin-eng/game-owl-ket/commit/c3ca06708985d1af63f142d80f56492fe0e9dcc5) |
| 4/6 | 208-ninox-affinis-v4 | 幼鸟胸腹纵纹降低对比，保留弱纹 | [原图](https://github.com/janeytlin-eng/game-owl-ket/blob/e33501a29b076f0f0ee4052c7c32eddecc937637/owl-pet/design/concepts/208-ninox-affinis-v4.png) | [研究](../../research/species/208-ninox-affinis-v4.md) / [复查](../../research/reviews/208-ninox-affinis-v4-review.md) | [6f1f270](https://github.com/janeytlin-eng/game-owl-ket/commit/6f1f2706e8f4550b300022d8cd5546d342e6c950) |
| 5/6 | 206-glaucidium-castanopterum-v4 | 成鸟趾基稀疏刚毛可读性；首编辑不足后再次编辑 | [原图](https://github.com/janeytlin-eng/game-owl-ket/blob/9f5c31f95fb7e2728611a4207275a107500640fa/owl-pet/design/concepts/206-glaucidium-castanopterum-v4.png) | [研究](../../research/species/206-glaucidium-castanopterum-v4.md) / [复查](../../research/reviews/206-glaucidium-castanopterum-v4-review.md) | [59e0d00](https://github.com/janeytlin-eng/game-owl-ket/commit/59e0d002eeb0bb7af02a30b264b4e26c7c249dfd) |
| 6/6 | 210-athene-superciliaris-v3 | 仅证据边界说明：二手幼鸟描述、年龄/虹膜/喙/飞行未核实 | [原图](https://github.com/janeytlin-eng/game-owl-ket/blob/3f37e75b3c73f2c4aae9c7ae71f7da0a167f3484/owl-pet/design/concepts/210-athene-superciliaris-v3.png) | [研究](../../research/species/210-athene-superciliaris-v3.md) / [复查](../../research/reviews/210-athene-superciliaris-v3-review.md) | [5d838c4](https://github.com/janeytlin-eng/game-owl-ket/commit/5d838c42976d8b90281ed5e06c16cfa069934d8d) |

六图1536×1024完整PNG均实际查看，#206另查看足部放大裁图并追加一次imagegen修订；#210原图/翼尾裁图已具备相应特征，不重复修改解剖。六图各自完整远端GET、字节数、SHA256、PIL解码与Git blob/manifest对应通过；最新main非截断树逐项存在。各run有RESEARCH_READY、IMAGE_GENERATED、REVIEWED、ARCHIVED、VERIFIED阶段和完整提示/来源摘要；[账本](../BATCH_STATE.json)逐轮提交回读后已6/6，lease空，其他有效未完批次0（SUPERSEDED_DUPLICATE不是有效运行）。阶段数量不计轮数。

科学校准false：全部为PASS_WITH_LIMITATIONS，新增科学通过0、用户确认0。历史#01–16共16种已确认旧造型记录保留，不自动传递至当前版；全库当前版用户确认/待修正数量未知。当前可查科学通过0，206种概念仍待科学校准。全任务未完成，完整251集中审查入口/全批科学审查尚未完成，未暂停或改动其他任务。

## 研究索引与不确定性

[来源索引](../../research/SOURCE_INDEX.md)新增独立来源0、复用13次来源ID引用，按同书去重为8份文档；13条不是13篇新文献。实际外部查询并读取物种页面/MNHN、重读上传图鉴；检索未读线索明确排除。3处来源适用边界澄清（ML媒体类型、GMNI无幼鸟段、ASUP尾尖/初级飞羽端缘）及来源ID别名去重；历史来源保留。图鉴对应印刷页388、484、113、470、407、471（PDF各+2）。幼鸟精确日龄/虹膜/喙/飞行及个别成年喙色/性别线性比例仍未知；不据二手描述推断初生细节。#206刚毛密度/分布未精确复原，#208成年喙色冲突保留。

## 实际错误与恢复

- 初选#203误用v2、忽略已存在v3，生成重复尝试。归档检查挡住原图覆盖，未增加轮次/修订/物种数；自身重复图仅保留[拒计记录](../runs/20261124T1535Z-cycle1-duplicate-attempt.json)与[artifact](../artifacts/20261124T1535Z/203-duplicate-attempt.png)。中途误写历史v3研究/审查已在[dc4075fb](https://github.com/janeytlin-eng/game-owl-ket/commit/dc4075fb72fa823a8d1325ef91d8e5b0eabda029)恢复，最终树与初始48c2a6e1两份文本blob逐字节一致，历史PNG未改。
- 一次恢复提交参数content缺失：调用失败，核对后重试成功；一次图片查看早于下载完成，待文件就绪后实际查看；不当作生产成功。
- #208审查保存时RemoteProtocolError断连，核对main仍a15c994后重试成功，无重复生成。
- #208图像工具结果显示上下文输出截断；输出PNG仍存在，恢复该文件后持久化/实际查看/归档，无重新生成或虚构失败。
- #206首编辑刚毛不可辨，追加编辑后趾基可辨，未把两个尝试计两个修订。

## 时间与接续

批次实际开始2026-11-24T15:31:58.038Z，最后一轮VERIFIED 2026-11-24T16:00:31.690Z（北京时间23:31:58至次日00:00:31）；各阶段时间及等待见[机器证据](20261124T1535Z-evidence.json)。研究阶段间隔含阅读/设计/保存，归档阶段间隔含网络/上传/提交/校验，不是纯算力耗时。每次长imagegen前后实际续期15分钟lease；六轮结束已释放。本次没有平台固定超时遥测；不声称固定时长限制。外部API未接入、未切换。

问题自迭代：最高版本检查必须在生成前按最新树/manifest核对；稀疏细节须看放大图；具体羽区词须重读原文，已正确特征不重复修改。上述规则本次实际用于后续轮次，不声称全库均已验证。回看#202/#207不跨种套用#206趾毛；全库受影响回查仍待系统审查。

其他未完批次0。下一子轮：下一批次1/6，先对齐尚缺45种的名录/证据并选择可推进项目或仍有明确错误的修订；不能声称已经在后台执行。当前批次编号不重开。
