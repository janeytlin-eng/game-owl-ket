# 2026-11-28 本次6生产子轮完成，整体PARTIAL
run 20261128T0329Z；首个持久化子轮开始2026-11-28T03:31:50.266Z，结束记录2026-11-28T03:50:49.329Z；前置回读未单独计时。基线main 6329ea470cc3c9bac20af0273ca02089a148c518。先续最早0304Z第5–6轮，跨次补齐6/6；再做0329Z第1–4轮。每轮STARTED/15分钟lease和RESEARCH_READY/IMAGE_GENERATED/REVIEWED/ARCHIVED/VERIFIED均独立提交，原图双路径全字节SHA256/PNG解码、研究审查回读成立后计账。

新增物种0/修订6版本6种；207/251不变，尚差44；编号图1460→1466，1460既有图blob保留。8次实际imagegen与实际查看，2次必要二编，2初稿保留。5局部PWL、108仍NEEDS_REVISION；130成人冠顶局部通过但幼鸟卷纹仍未解决，112幼鸟纹理同样未知/未解。科学通过/新用户确认0。

|本次轮|物种/版本|批次轮|实际结果|证据|VERIFIED提交|
|---|---|---|---|---|---|
|1|108-otus-rutilus-v17|20261128T0304Z 5/6|NEEDS_REVISION|[原图](../originals/108-otus-rutilus-v17.png) · [研究/完整提示](../../research/species/108-otus-rutilus-v17.md) · [实际检查](../../research/reviews/108-otus-rutilus-v17-review.md)|[4a3cb9cd](https://github.com/janeytlin-eng/game-owl-ket/commit/4a3cb9cd4d61a6668c412f504b01b4b4da0aa888)|
|2|130-megascops-koepckeae-v23|20261128T0304Z 6/6|PASS_WITH_LIMITATIONS|[原图](../originals/130-megascops-koepckeae-v23.png) · [研究/完整提示](../../research/species/130-megascops-koepckeae-v23.md) · [实际检查](../../research/reviews/130-megascops-koepckeae-v23-review.md)|[e1d88eb8](https://github.com/janeytlin-eng/game-owl-ket/commit/e1d88eb865024c49d3ad4d49743fe00a1be6ec4c)|
|3|129-megascops-hoyi-v8|20261128T0329Z 1/6|PASS_WITH_LIMITATIONS|[原图](../originals/129-megascops-hoyi-v8.png) · [研究/完整提示](../../research/species/129-megascops-hoyi-v8.md) · [实际检查](../../research/reviews/129-megascops-hoyi-v8-review.md)|[3b833ef9](https://github.com/janeytlin-eng/game-owl-ket/commit/3b833ef919816913c87835fa06d0708a777dfd10)|
|4|131-megascops-watsonii-v9|20261128T0329Z 2/6|PASS_WITH_LIMITATIONS|[原图](../originals/131-megascops-watsonii-v9.png) · [研究/完整提示](../../research/species/131-megascops-watsonii-v9.md) · [实际检查](../../research/reviews/131-megascops-watsonii-v9-review.md)|[c26ba4c7](https://github.com/janeytlin-eng/game-owl-ket/commit/c26ba4c78ff33a2a860e60417da1a5600a2fcdde)|
|5|133-megascops-atricapilla-v10|20261128T0329Z 3/6|PASS_WITH_LIMITATIONS|[原图](../originals/133-megascops-atricapilla-v10.png) · [研究/完整提示](../../research/species/133-megascops-atricapilla-v10.md) · [实际检查](../../research/reviews/133-megascops-atricapilla-v10-review.md)|[feb380e6](https://github.com/janeytlin-eng/game-owl-ket/commit/feb380e6ab70fdad1277b2b9fe28b392f86555b4)|
|6|112-asio-abyssinicus-v16|20261128T0329Z 4/6|PASS_WITH_LIMITATIONS|[原图](../originals/112-asio-abyssinicus-v16.png) · [研究/完整提示](../../research/species/112-asio-abyssinicus-v16.md) · [实际检查](../../research/reviews/112-asio-abyssinicus-v16-review.md)|[2178f3f4](https://github.com/janeytlin-eng/game-owl-ket/commit/2178f3f4b7b4f29ee0a5c38a4cc07fc32a536a86)|

## 逐轮研究与迭代
- 108：Vassen2013Andasibe照片页面实际新读、缓存原图和v16实际看，图鉴143/PDF145实际读。新试验将照片放第一参考，整只幼鸟以三分之四侧身重建，再针对羽面二编；姿态改变，卷丝仍在。记负结果，不能把换姿态称材质修复，不再把同方法当已验证规则。
- 130：图鉴222/PDF224成年冠顶黑褐细浅斑；Alarcon2023原文104/PDF13实际读，保留幼鸟既有离巢阶段。首次新冠顶太平，实际二编恢复柔和羽面起伏，局部PWL；整个幼鸟及其未解纹理保持不变，绝不说已解决。
- 129：图鉴228/PDF230成年灰褐面盘细暗蠕纹实际读，SIB机构页名称/旧名实际读（不是形态来源）；面盘细纹局部PWL，幼鸟虹膜/喙/趾色仍只保留明确未核验标签。雌鸟20g质量差不推导身高。
- 131：图鉴236–237/PDF238–239成年黑褐中等耳羽实际读；Menq2018正文、Dantas2021原文401摘要实际读，区域usta与当前Mwatsonii概念边界保持。成鸟耳羽色局部PWL；不由二手“两日龄至四周”描述重画本组未定龄幼鸟。预检页码偏移曾读到Marshalli，编辑前已改正，未采用其特征。
- 133：图鉴238/PDF240、Lewis2020正文67–72实际读；Dantas2021原文427/PDF27明确M.atricapilla红色型也有褐眼，相邻alagoensis正模不借用。成年面盘细暗蠕纹局部PWL，幼鸟保留，无新年龄或色型性别关联。
- 112：图鉴508/PDF510及Lewis2020正文58–62实际读；保留先前面盘校正与耳羽位置，仅使成年耳羽更暗，局部PWL。全幼鸟成形翼尾、日龄未知和未解材质不变，不把图鉴“可能像Asiootus”当本种确证。

## 来源与新增访问
[`SOURCE_INDEX.md`](../../research/SOURCE_INDEX.md)：新增可读机构元数据资源1（**不是幼鸟生物学资料**），生物学新源0，复用13ID/14引用合并8既有资料家族，访问边界更新1。图鉴别名和Dantas两ID不重复计文献。逐物种记录含URL/页码/适用阶段/局限/完整提示。
[缺口研究与机构项目包的实际读取范围](../../research/gaps/20261128T0329Z-access-frontier.md)：AQAR2023链接可读部分仅多项目封面、证书前部；后段未读及下载503，不能称安达曼仓鸮学位论文全文已读，也不能据此绘制幼鸟。Otusmirus检索中的成鸟图不转为幼鸟，未生成资料不足新种，未分配新编号。

## 真实错误、计时与限制
[审计JSON](20261128T0329Z-audit.json)记录所有阶段起止、生成/编辑等待与阶段间隔；间隔含归档网络/提交/检查，不伪称纯研究时间。一次中间图提交的HEAD_CHANGED保护拒绝发生于本任务自身112 RESEARCH_READY提交推进期间；等待长工具完成、读回提交信息确认后，按最新main非force重试成功，没有覆盖并发成果。所有最终图已逐轮全字节解码读回。
#25v6原图/概念图保留相同Gitblob10508841ef5f6184e8658664615302909765c1dd；fd9d70d仍connector422 No commit found，不重复计数。最终完整回读再次检查这两路径。
全库科学校准/待修正总数未知。108整鸟重建未验证有效，130和112幼鸟材质仍待不同方法；成年羽区局部有效不推广为全物种科学通过。251权威名录逐项对照及44种缺口仍未完成，未取得平台超时遥测，未切换外部API或改其他任务。

当前批次20261128T0329Z累计4/6；其他PARTIAL0，下一子轮5，lease已释放。旧0304Z是跨次6/6，本次仅补其5–6，不冒称旧批本次六轮。全清单/整批集中科学审查未完，不暂停生产任务，不宣称后台绘图或预计结束。
[最终回读收据](20261128T0329Z-final-readback-receipt.json)待实际完整检查后写入。
