# 2026-11-28 10:31起：本次6个生产子轮完成，整体任务PARTIAL
本次run/owner：20261128T0232Z；开始2026-11-28T02:31:59Z（上海10:31:59），记录截止2026-11-28T02:57:41.158Z。基线main 3628992f0ec48ead24ff95b092e60e717d94141f；逐轮均保存STARTED和15分钟lease，并按实际RESEARCH_READY、IMAGE_GENERATED、REVIEWED、ARCHIVED、VERIFIED持久化。先续最早0130Z批次5–6，之后新0232Z批次1–4；不是每次重置1/6。

## 实际数量
- 本次完成6轮；新增0物种、修订6版本/6种；实际imagegen7次，含#137标题纠错1次，全部实际看图。
- 归档按规范学名前两段、历史Pseudoscopsgrammicus→Asiogrammicus别名和亚种去重：207/251不变，尚差44；编号图1448→1454。所有1448基线编号图blob保留，修订不增加物种。
- 六图仅本次限定项目PASS_WITH_LIMITATIONS；科学通过0、新用户确认0。幼鸟精确年龄/飞行能力/雌雄比例及局部未解决项见各实际检查。全库待修正总数未知，既有108/130材料问题未在本次解决，112等限制继续保留；不能把6组局部通过说成251种科学通过。
- 当前批次20261128T0232Z累计4/6，下一子轮5；其他PARTIAL批次0、lease已释放。0130Z跨触发累计6/6，这次只补其5–6，不能称该批单次完成6。

## 按编号审查原图与真实VERIFIED提交

|本次轮|物种/版本|批次子轮|证据|VERIFIED commit|
|---|---|---|---|---|
|1|#134-megascops-sanctaecatarinae-v14|20261128T0130Z 5/6|[原图](../../production/originals/134-megascops-sanctaecatarinae-v14.png) · [研究/完整提示](../../research/species/134-megascops-sanctaecatarinae-v14.md) · [实际检查](../../research/reviews/134-megascops-sanctaecatarinae-v14-review.md)|[fca62629](https://github.com/janeytlin-eng/game-owl-ket/commit/fca62629f9e1afdbfda0bd8252999b8ad8012766)|
|2|#136-megascops-petersoni-v9|20261128T0130Z 6/6|[原图](../../production/originals/136-megascops-petersoni-v9.png) · [研究/完整提示](../../research/species/136-megascops-petersoni-v9.md) · [实际检查](../../research/reviews/136-megascops-petersoni-v9-review.md)|[704e849f](https://github.com/janeytlin-eng/game-owl-ket/commit/704e849ff7b0035cb446bb7518d73ede28f6542a)|
|3|#137-otus-alfredi-v9|20261128T0232Z 1/6|[原图](../../production/originals/137-otus-alfredi-v9.png) · [研究/完整提示](../../research/species/137-otus-alfredi-v9.md) · [实际检查](../../research/reviews/137-otus-alfredi-v9-review.md)|[6d8c1099](https://github.com/janeytlin-eng/game-owl-ket/commit/6d8c10998473021bf34dabaf7912a27241439a09)|
|4|#132-strix-davidi-v8|20261128T0232Z 2/6|[原图](../../production/originals/132-strix-davidi-v8.png) · [研究/完整提示](../../research/species/132-strix-davidi-v8.md) · [实际检查](../../research/reviews/132-strix-davidi-v8-review.md)|[f3cfbc4d](https://github.com/janeytlin-eng/game-owl-ket/commit/f3cfbc4d97aa38b221948ae7717e65e3316630c1)|
|5|#95-pulsatrix-melanota-v10|20261128T0232Z 3/6|[原图](../../production/originals/95-pulsatrix-melanota-v10.png) · [研究/完整提示](../../research/species/95-pulsatrix-melanota-v10.md) · [实际检查](../../research/reviews/95-pulsatrix-melanota-v10-review.md)|[d22546bc](https://github.com/janeytlin-eng/game-owl-ket/commit/d22546bc63c291e344ea4202721a1f31e38d0c59)|
|6|#85-otus-semitorques-v12|20261128T0232Z 4/6|[原图](../../production/originals/85-otus-semitorques-v12.png) · [研究/完整提示](../../research/species/85-otus-semitorques-v12.md) · [实际检查](../../research/reviews/85-otus-semitorques-v12-review.md)|[b2f565b2](https://github.com/janeytlin-eng/game-owl-ket/commit/b2f565b220d5bc9104ad2dc12a2249c23f85e785)|

## 本次研究与迭代
- #134：Pagano等2021印刷p55原文深色横叉末端上弯；将成鸟腹纹从长轴偏重改为有横叉的粗纹，保留幼鸟。MIKKOLA印刷239/PDF241；照片是已存实物图再次查看，元数据未在403时假称新读。
- #136：Fitzpatrick/O'Neill1986原始描述p4区分胸/胁显著轴纹与最下腹/crissum纯肉桂色，局部减少最下腹深轴；不抹除所有胸腹羽纹。MIKKOLA232/PDF234。
- #137：Widodo/Cox/Rasmussen1999原始描述15及Table2 pp18–19，成鸟额部细白蠕纹；幼鸟有成形翅尾，不降为初生阶段。首次图标题仍v8，实际发现并imagegen二编改v9，失败初稿[保留](../intermediates/20261128T0232Z-137-otus-alfredi-v9-first-attempt.png)。
- #132：**新增实际读原始资料1篇**，Scherzinger/Fang/Shi/Sun2021 Airo29:367–392，实际下载12960780字节、读367/370–372/376并看Fig5；约4½周、wooly mesoptile、深面盘/粉眼睑。只改幼鸟面色和近似4–5周标签；不把“所有羊毛状羽被都错”当通则。与2014同野外计划有重叠，不当独立队列重复验证。
- #95：Rivas-Fuenzalida/Burgos-Andrade2022 pp84–86原文，幼鸟开始生胸羽时头绒转白；将v9偏桃色头顶校为近白，保留黑面盘、深虹膜、肉桂色体绒和短翅。不是精确日龄证明。MIKKOLA314/PDF316。
- #85：Nohara/Honda2025原文75–76和Fig1实际下载/render查看，成鸟橙虹膜/趾羽不变；MIKKOLA158/PDF160灰褐面盘细小斑点，局部替换金色粗鳞片；幼鸟虹膜在原照片不可辨，不套图鉴年轻黄眼。腹部总体仍有风格化角状纹理，未称全身科学校准。
- 索引路径：[`SOURCE_INDEX.md`](../../research/SOURCE_INDEX.md)。新增1文献；复用10个既有ID（3个图鉴页域/拼写ID合并后为8个既有资料家族），13次既有生产引用；新增引用1次。#134临时p55别名合并既有LTSC-PAGANO-2021，规范映射更正1，不重复算新文献。图鉴实际页码、来源URL、证据局限及完整提示均在逐物种记录。
- [缺失物种实际补查与未核验线索](../../research/gaps/20261128T0232Z-missing-species.md)。资料不足未生成假幼鸟，未计子轮。

## 错误、计时及限制
7次imagegen有图，#137标题错误已二编修复；一次读源与多图组合输出超上下文，已分开重读，未以丢弃输出称实际查看。2021大PDFwebopen400改用实际PDF读取；2014源403仅历史复用。个别候选学名路径404已根据tree纠正，没有覆盖旧图。未发生GitHub写入/上传失败或审批拒绝。
每轮开始/阶段/结束时间、生成等待及编辑时间见[审计JSON](20261128T0232Z-audit.json)与run；阶段间隔含提交/上传/检查等待，不冒称纯研究或平台固定时长。瓶颈证据：实际生成等待与上传/分阶段Git提交并存；本次无平台超时遥测。外部API未部署，未修改其他任务。

## 恢复与下一步
fd9d70d本次connector实际返回422 No commit found；第25组v6原图与concept远端仍有相同blob10508841ef5f6184e8658664615302909765c1dd，完整字节/解码将在本次最终回读收据检查，不重新出图/计数。其他旧批次已核对账本，不新增重复待办。
下次从20261128T0232Z第5子轮接续；优先为108/130待修问题找到不同且有证据的方法，并继续44种缺口的分类和幼鸟资料补查。当前无有效生产lease，不宣称后台正在绘制；全251及整批集中科学审查未完成，不暂停生产任务，不修改调度。
最终完整回读收据：[`20261128T0232Z-final-readback-receipt.json`](20261128T0232Z-final-readback-receipt.json)。阶段计数不等于子轮；只有VERIFIED且读回才计入本次6轮。
