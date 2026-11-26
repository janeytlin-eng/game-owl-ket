# 2026-11-26 六轮证据标识修订交付

北京时间约16:33开始；各轮起止UTC见下表。实际完成6个串行生产子轮：旧20261126T0540Z的3–6轮和新20261126T0845Z的1–2轮。旧批次跨触发补齐6/6，本次贡献4轮；当前新批次2/6，next_cycle=3，其他有效未完批次0。不是本次完成两个六轮批次。

新增物种0，实际imagegen编辑/查看/归档修订6组。均是图面的年龄、证据范围和科学待校准标识修订；没有新的形态科学通过，也没有新增用户确认。覆盖依现行物种名归一口径207/251不变、剩44；修订版本不重复计物种。所有旧图/编号/确认均保留。全清单和集中整批科学审查未完成，未暂停/改动其他任务或自动化。

每轮RESEARCH_READY研究/完整提示和来源索引先提交；IMAGE_GENERATED原始工具输出持久提交；实际整图/页脚crop查看后REVIEWED，展示图/审查/manifest提交ARCHIVED；不可变originals及concepts两路径逐一GET、准确字节/SHA256、完整PNG解码和Gitblob一致、研究审查回读后VERIFIED，才登记账本。表中验证SHA不是GitHub签名认证；是生产检查记录提交。

|本次轮|批次/子轮|版本/原图|研究与完整提示|实际审查|验证提交|
|---|---|---|---|---|---|
|1/6|20261126T0540Z/3|[08-strix-nebulosa-v7](https://github.com/janeytlin-eng/game-owl-ket/blob/0150d00d2d2ab7b9e84b165bb91bfa7734e59176/owl-pet/design/originals/08-strix-nebulosa-v7.png)|[研究](../../research/species/08-strix-nebulosa-v7.md)|[审查](../../research/reviews/08-strix-nebulosa-v7-review.md)|[623e8202d6](https://github.com/janeytlin-eng/game-owl-ket/commit/623e8202d6ca0029642d9f6eb777a421fa6d72e7)|
|2/6|20261126T0540Z/4|[11-aegolius-funereus-v6](https://github.com/janeytlin-eng/game-owl-ket/blob/5c9db3b14900285e5bfea01970ef2993beb8e54e/owl-pet/design/originals/11-aegolius-funereus-v6.png)|[研究](../../research/species/11-aegolius-funereus-v6.md)|[审查](../../research/reviews/11-aegolius-funereus-v6-review.md)|[c282c7adcb](https://github.com/janeytlin-eng/game-owl-ket/commit/c282c7adcbdaa216eae997bf65aae7e8fa662f15)|
|3/6|20261126T0540Z/5|[12-aegolius-acadicus-v6](https://github.com/janeytlin-eng/game-owl-ket/blob/20b96afb1526c4c9a441ef1c62d2981827b1ec28/owl-pet/design/originals/12-aegolius-acadicus-v6.png)|[研究](../../research/species/12-aegolius-acadicus-v6.md)|[审查](../../research/reviews/12-aegolius-acadicus-v6-review.md)|[729e9b12ea](https://github.com/janeytlin-eng/game-owl-ket/commit/729e9b12ea1f211dfb506376c07496734f29ceaa)|
|4/6|20261126T0540Z/6|[14-bubo-virginianus-v6](https://github.com/janeytlin-eng/game-owl-ket/blob/4d297af2ddbdeb7052c6f8f0cf076f5067cce167/owl-pet/design/originals/14-bubo-virginianus-v6.png)|[研究](../../research/species/14-bubo-virginianus-v6.md)|[审查](../../research/reviews/14-bubo-virginianus-v6-review.md)|[62d9d49179](https://github.com/janeytlin-eng/game-owl-ket/commit/62d9d4917982797606c1baead783e7a20d537028)|
|5/6|20261126T0845Z/1|[15-strix-varia-v7](https://github.com/janeytlin-eng/game-owl-ket/blob/e05cf3e40cb898048961a25137f80d67414d469b/owl-pet/design/originals/15-strix-varia-v7.png)|[研究](../../research/species/15-strix-varia-v7.md)|[审查](../../research/reviews/15-strix-varia-v7-review.md)|[a190dad974](https://github.com/janeytlin-eng/game-owl-ket/commit/a190dad974f1771320692f546a23dee428fb1f77)|
|6/6|20261126T0845Z/2|[16-strix-occidentalis-v7](https://github.com/janeytlin-eng/game-owl-ket/blob/66a89059493eb6d65be2e86d2963e16de2700f60/owl-pet/design/originals/16-strix-occidentalis-v7.png)|[研究](../../research/species/16-strix-occidentalis-v7.md)|[审查](../../research/reviews/16-strix-occidentalis-v7-review.md)|[7ce90fc5a9](https://github.com/janeytlin-eng/game-owl-ket/commit/7ce90fc5a92951b9ff9295bff361e1623c6f9a0a)|

具体问题—修改—复查：#08v7补年龄未知/科学待校准标识，保留v6羽趾和攀爬幼鸟；#11v6撤销未经个体校准的约21–23日龄；#12v6撤销物种一般4–5周区间到图中个体的映射，保留有资料支持的成形幼羽；#14v6撤销约21日龄并标明巢几何/区域羽纹未知；#15v7把论文估计入口年龄与生成个体分开，保留洞口支撑；#16v7明确年龄未知。Forsman确实有离巢10天个体参考，并非文献没有此阶段；图像与个体羽区未逐项校准，故不把参考日龄当作成图日龄。六张整图和页脚实际检查可读，未见明显新落脚漂浮；细微羽区/色彩/性别尺度仍未知，不将视觉检查当科学通过。

研究索引：新增来源0；六轮sources数组共15次定位引用/13个稳定ID，按同一本Mikkola和CFN正文+补充去重为9份资料。7份外部资料原文/正文或文字图注本次实际读取，Mikkola图鉴及Hoffmeister1947仅复用历史已读记录。不是本次重新阅读上传图鉴。新观察范围与限制已增量落入[来源索引](../../research/SOURCE_INDEX.md)并回读含六个版本；各版本记录具体URL/作者/章节/页码/适用阶段。图鉴不同页码不是新出版物，CFN补充不是第二篇论文。#16额外新读Forsman印刷78–79/Fig8及82/Table15，原引用范围升级；#14原始Gutenberg/cache503、镜像不可访问，保留历史读，不把搜索摘要当新验证。#16截图调用未提供可供本次独立检查的图片块，只声称正文/图注读取。

|版本|开始UTC|VERIFIED UTC|imagegen等待秒|RESEARCH_READY到持久IMAGE_GENERATED秒|REVIEWED到验证秒|
|---|---|---|---:|---:|---:|
|08-strix-nebulosa-v7|2026-11-26T08:33:59.853Z|2026-11-26T08:36:41.007Z|37.587|93.3|40.9|
|11-aegolius-funereus-v6|2026-11-26T08:36:47.849Z|2026-11-26T08:38:51.522Z|35.414|66.2|21.6|
|12-aegolius-acadicus-v6|2026-11-26T08:38:57.458Z|2026-11-26T08:40:56.229Z|37.302|66.6|20.9|
|14-bubo-virginianus-v6|2026-11-26T08:41:01.483Z|2026-11-26T08:43:21.195Z|35.528|67.7|21.1|
|15-strix-varia-v7|2026-11-26T08:43:26.876Z|2026-11-26T08:47:31.248Z|34.352|64.8|135.9|
|16-strix-occidentalis-v7|2026-11-26T08:47:36.251Z|2026-11-26T08:50:04.055Z|36.597|56.5|19.8|

这些阶段差值包括编排/上传/回读，不能当作纯研究或纯归档工时。精确纯研究时间、图像编辑服务内部时间、网络上传独立时间未分别测量，未知。生成等待为调用墙钟，6次合计216.780秒。#15归档后至VERIFIED较长包括输出截断/上下文续接，不声称平台固定超时或持续后台生产。所有阶段戳为记录时间；ARCHIVED阶段在验证记录时追加，实际归档commit时间应以GitHub为准。

实际错误与恢复：#14源文503如上。#15工具输出因可用上下文被截断，先检查持久阶段/既有原图再恢复，无重复生成。#16完成双路径二进制验证并提交7ce90fc5a92951b9ff9295bff361e1623c6f9a0a后，commits/main回读触发ref mismatch；git/ref/heads/main与不可变验证提交回读确认该提交真实在main，随后恢复一次计数，未重复出图。修正发布 helper使用git/ref/heads/main读最新指针及其git/commits树，保留expected_sha/force=false；后续账本更新和报告提交回读通过，不能据此断言所有缓存故障根除。

复用/迭代规则：参考照片或论文年龄只限定设计阶段，不能自动证明生成个体精确日龄；保留合理的成形幼鸟飞羽；雌鸟体重方向不推出固定站高比；局部标识编辑仍须检查三鸟/支撑/文本，科学未知必须在图上和档案同时可见。当前实际应用与可读复查范围只限这六张，非全251已校准。上传前检查base64长度/Gitblob，远端完整解码后计数的修复链本次6张12个原图/展示路径通过；未对全历史库声称回查完毕。

下一子轮：20261126T0845Z cycle3。先读最新main/有效lease/未完成阶段，优先实际待修正队列或尚无图且资料明确的物种；不固定重复这六张或把已保存图当新产出。当前无活动lease。全部251与最终集中审查未完成，不暂停生产。

原图精确证据：

- 08-strix-nebulosa-v7: 3173802 bytes; SHA256 829cc74603a2a780e370b82f6329f5384df645665d0092c2d4548e9e00167642; Gitblob 9ba2c57e538de7d313cdca33dca1dca3f1692b87; archive [0150d00d2d2ab7b9e84b165bb91bfa7734e59176](https://github.com/janeytlin-eng/game-owl-ket/commit/0150d00d2d2ab7b9e84b165bb91bfa7734e59176); [run](https://github.com/janeytlin-eng/game-owl-ket/blob/623e8202d6ca0029642d9f6eb777a421fa6d72e7/owl-pet/production/runs/20261126T0540Z-cycle3-resume0833Z.json).

- 11-aegolius-funereus-v6: 2687593 bytes; SHA256 aaa971fc9330b1a8842a61a7b60eba177e6b703090f69bbfb287b79de8e1d159; Gitblob ca9401beafec3ff82698fc5e4751c10e60c0dae8; archive [5c9db3b14900285e5bfea01970ef2993beb8e54e](https://github.com/janeytlin-eng/game-owl-ket/commit/5c9db3b14900285e5bfea01970ef2993beb8e54e); [run](https://github.com/janeytlin-eng/game-owl-ket/blob/c282c7adcbdaa216eae997bf65aae7e8fa662f15/owl-pet/production/runs/20261126T0540Z-cycle4-resume0833Z.json).

- 12-aegolius-acadicus-v6: 3222302 bytes; SHA256 4c9e53bfae7cca434141f0651f69e4203d961f455c72665910ecfd3628749434; Gitblob e5e0da1d7dbba34b18eb9e0cec5a326582c4a220; archive [20b96afb1526c4c9a441ef1c62d2981827b1ec28](https://github.com/janeytlin-eng/game-owl-ket/commit/20b96afb1526c4c9a441ef1c62d2981827b1ec28); [run](https://github.com/janeytlin-eng/game-owl-ket/blob/729e9b12ea1f211dfb506376c07496734f29ceaa/owl-pet/production/runs/20261126T0540Z-cycle5-resume0833Z.json).

- 14-bubo-virginianus-v6: 2671966 bytes; SHA256 8aa6f5170a00b2447416cdf4ac4b3e03e40cf2325510af09c206be314ede5c8b; Gitblob e88eb2dc355881a40e05415070b081f21820354a; archive [4d297af2ddbdeb7052c6f8f0cf076f5067cce167](https://github.com/janeytlin-eng/game-owl-ket/commit/4d297af2ddbdeb7052c6f8f0cf076f5067cce167); [run](https://github.com/janeytlin-eng/game-owl-ket/blob/62d9d4917982797606c1baead783e7a20d537028/owl-pet/production/runs/20261126T0540Z-cycle6-resume0833Z.json).

- 15-strix-varia-v7: 3067505 bytes; SHA256 4c594e77e4591775fa9019ee826a76a1bf5acebde654e1e25a2ffaa4dae94737; Gitblob 989ce35f9b54157594494f6fa34e7a50a40988ef; archive [e05cf3e40cb898048961a25137f80d67414d469b](https://github.com/janeytlin-eng/game-owl-ket/commit/e05cf3e40cb898048961a25137f80d67414d469b); [run](https://github.com/janeytlin-eng/game-owl-ket/blob/a190dad974f1771320692f546a23dee428fb1f77/owl-pet/production/runs/20261126T0845Z-cycle1-resume0833Z.json).

- 16-strix-occidentalis-v7: 2678872 bytes; SHA256 8f9aba34ca4f33ec676f2bc0c547842c788cce9f0c112438465cb7adf6a4da2b; Gitblob bd734c41eb7bd9b7b5b896c100da9dfb2d6425d9; archive [66a89059493eb6d65be2e86d2963e16de2700f60](https://github.com/janeytlin-eng/game-owl-ket/commit/66a89059493eb6d65be2e86d2963e16de2700f60); [run](https://github.com/janeytlin-eng/game-owl-ket/blob/7ce90fc5a92951b9ff9295bff361e1623c6f9a0a/owl-pet/production/runs/20261126T0845Z-cycle2-resume0833Z.json).
