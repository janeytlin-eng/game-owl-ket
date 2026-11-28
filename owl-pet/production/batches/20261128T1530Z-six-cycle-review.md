# 2026-11-28 本次6个完成子轮（含恢复1组）

新增物种0，修订6组，覆盖207/251不变；编号图1530→1536。不是6次新生成：恢复#10既有候选1张，其他5组共7次内置imagegen（含13/14返修各一次）。原1435Z批次由2/6跨触发补齐6/6；当前1530Z累计2/6,next3；其他PARTIAL0，lease空。科学通过/新增用户确认0；5局部PWL（其中15仅轻微色彩试作、12姿态设计），13仍NEEDS_REVISION。既有确认仅其历史范围，未覆盖。全251及集中整批科学验收未完。

|原图|批次/轮|真实VERIFIED提交|研究/完整提示|实际复查|运行记录|
|---|---|---|---|---|---|
|[10-surnia-ulula-v6](../../design/concepts/10-surnia-ulula-v6.png)|20261128T1435Z/3|[68fa546](https://github.com/janeytlin-eng/game-owl-ket/commit/68fa546f919e2878b838c302a6c9ce03bc69a02b)|[研究](../../research/species/10-surnia-ulula-v6.md)|[PASS_WITH_LIMITATIONS](../../research/reviews/10-surnia-ulula-v6-review.md)|[run](../runs/20261128T1435Z-cycle3-20261128T1435Z-10-surnia-ulula-v6.json)|
|[11-aegolius-funereus-v7](../../design/concepts/11-aegolius-funereus-v7.png)|20261128T1435Z/4|[6fbeb46](https://github.com/janeytlin-eng/game-owl-ket/commit/6fbeb46d82cd170b74e99e1c4c09f41673462c18)|[研究](../../research/species/11-aegolius-funereus-v7.md)|[PASS_WITH_LIMITATIONS](../../research/reviews/11-aegolius-funereus-v7-review.md)|[run](../runs/20261128T1435Z-cycle4-20261128T1530Z-11-aegolius-funereus-v7.json)|
|[13-micrathene-whitneyi-v9](../../design/concepts/13-micrathene-whitneyi-v9.png)|20261128T1435Z/5|[da17879](https://github.com/janeytlin-eng/game-owl-ket/commit/da17879996eb4c8c6402bc5c5faf09b427f6fe29)|[研究](../../research/species/13-micrathene-whitneyi-v9.md)|[NEEDS_REVISION](../../research/reviews/13-micrathene-whitneyi-v9-review.md)|[run](../runs/20261128T1435Z-cycle5-20261128T1530Z-13-micrathene-whitneyi-v9.json)|
|[14-bubo-virginianus-v7](../../design/concepts/14-bubo-virginianus-v7.png)|20261128T1435Z/6|[e3d6c95](https://github.com/janeytlin-eng/game-owl-ket/commit/e3d6c95b1e7fa2f13f7f73439b04e5296fde718a)|[研究](../../research/species/14-bubo-virginianus-v7.md)|[PASS_WITH_LIMITATIONS](../../research/reviews/14-bubo-virginianus-v7-review.md)|[run](../runs/20261128T1435Z-cycle6-20261128T1530Z-14-bubo-virginianus-v7.json)|
|[15-strix-varia-v8](../../design/concepts/15-strix-varia-v8.png)|20261128T1530Z/1|[dbe4ec5](https://github.com/janeytlin-eng/game-owl-ket/commit/dbe4ec548a8818b6e2e33702cd16fc2ac6f3f459)|[研究](../../research/species/15-strix-varia-v8.md)|[PASS_WITH_LIMITATIONS](../../research/reviews/15-strix-varia-v8-review.md)|[run](../runs/20261128T1530Z-cycle1-20261128T1530Z-15-strix-varia-v8.json)|
|[12-aegolius-acadicus-v7](../../design/concepts/12-aegolius-acadicus-v7.png)|20261128T1530Z/2|[91291e3](https://github.com/janeytlin-eng/game-owl-ket/commit/91291e3bb74723048ca8aa774357e5890470f93f)|[研究](../../research/species/12-aegolius-acadicus-v7.md)|[PASS_WITH_LIMITATIONS](../../research/reviews/12-aegolius-acadicus-v7-review.md)|[run](../runs/20261128T1530Z-cycle2-20261128T1530Z-12-aegolius-acadicus-v7.json)|

## 研究与迭代证据
新增2个已读来源：Mostafawi等2019 Sandgrouse41:95–97（#11实际读全文及Plate1/2）；Keegan2020 Arnold Arboretum亲历巢观察（#14实际读正文/图注，照片下载403未声称读像素）。复用13处来源定位引用，其中Ligon/Cornell两处仅复用历史，重新访问失败；同一本Mikkola各页、同一Duncan论文/补充材料不计多篇新文献。来源索引research/SOURCE_INDEX.md已逐轮增量提交。图鉴六处实际读页：360、440、418、262、346、444。全文提示和边界见各研究记录。

#11独立原始照片引导后，大圈绒丝显著减少、深褐较大幼鸟羽相更接近所选阶段；作者4–6周是估计，不变成此图已知日龄。#13两编后冠顶改善但颈胸曲丝残留，保留待修正；#14首编失败，第二编替换整片羽被后闭环显著减少，但叶片式重复/自然微结构仍未校准。#15蜡膜轻微冷色变化不能证明科学修复；#12闭眼休息为保守设计推断，保留完整幼鸟飞羽与双足握枝，不当作行为研究实证。先前进度中文误称#11珠颈鸮，纠正为学名Aegoliusfunereus，未改物种编号。

实际错误：13主文下载/检索403，误做后续本地解析缺失文件；Cornell403后转读ADW并在生成前纠正未读原文表述。14 Gutenberg503、图片403/web不可访问，尝试requests模块不存在；15补充PDF本地502，web正文可读、图像仅链接，未声称像素复核。均为局部来源访问失败，不是GitHub连接故障或平台强制超时。未取得平台超时遥测。研究/各阶段时间和生成等待/编辑等待见audit各run字段；恢复10旧生成等待未知，不伪造0秒。

## 历史恢复与保留
#25原图与concept各2864437bytes，完整GET/PNG解码/SHA256均729c187af12da587305c0c701c07440464896f5a6ada74431dfa3e7b19616ca1；已存在不重复生产。fd9d70d远端查422 No commit found，未声称可恢复该SHA。已保留原图版本与旧确认。全清单权威名录44种缺口仍需逐项核实，不以推测稀有种初生图凑数。

六个子轮每组original+concept/研究/复查均固定commit完整读取验证后计账；最终全树差异和元数据审计回执待本入口最后增量更新。

## 最终回读完成
2026-11-28T15:50:47.910Z 已在固定提交 `fe9502965d5dbf1cd13cdfbd7042d7a2c7232ad2` 对本次全部39个变更文件执行完整GET/Git blob SHA1校验，PNG完整解码、JSON解析；1530张原有编号图blob全部保留，现1536图/207规范物种，目录差异仅owl-pet/。回执：[逐文件验证](20261128T1530Z-readback.json)。

## 计时与瓶颈边界
五个新制组的首次生成实际工具等待合计188.514秒，13/14再次编辑等待合计77.338秒，共265.852秒；恢复10的旧生成等待未获取，记unknown。各run stages给出研究/生成/复查/归档/验证时间点。恢复10的started_at含此前中断间隔，不可当作本次持续工作耗时。blob上传发生在IMAGE_GENERATED之前，纯base64/blob时间未单独测量，阶段间隔不是各工具独占耗时，不能准确分摊研究/上传。已记录访问受限导致的额外检索、两次无效初编和恢复复用，未声称固定平台时长或API迁移提效。下一轮应单独采集blob传输start/end，尚未验证此测量规则。
