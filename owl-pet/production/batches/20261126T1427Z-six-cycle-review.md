# 2026-11-26 1427Z 六轮实际交付

本次完成6轮：旧1345Z第4–6轮跨次补齐6/6，新1445Z第1–3轮累计3/6,next4。其他有效PARTIAL0。新增0种/修订6种，其中4内容修订、2仅年龄归因标识；覆盖207/251不变，剩44。编号版本1148不作物种数。全部sciencefalse，新用户确认0。

|本次轮/批次轮|版本与实际改动|原图|真实归档/验证提交|
|---|---|---|---|
|1/4|49-strix-woodfordii-v7：成年肉粉眼睑|[原图](https://github.com/janeytlin-eng/game-owl-ket/blob/7e4e847733a68d001f1fb1f1e1fcc849b53e27cd/owl-pet/design/originals/49-strix-woodfordii-v7.png)|[归档](https://github.com/janeytlin-eng/game-owl-ket/commit/7e4e847733a68d001f1fb1f1e1fcc849b53e27cd) / [验证](https://github.com/janeytlin-eng/game-owl-ket/commit/effe5327564ca04081890feaa3d806f9cc20a4ba)|
|2/5|51-strix-rufipes-v7：成年冠部细横纹，仍有行列感待校准|[原图](https://github.com/janeytlin-eng/game-owl-ket/blob/033ea1d3f8f5fbdb40f7b34d2d9c3579783b909f/owl-pet/design/originals/51-strix-rufipes-v7.png)|[归档](https://github.com/janeytlin-eng/game-owl-ket/commit/033ea1d3f8f5fbdb40f7b34d2d9c3579783b909f) / [验证](https://github.com/janeytlin-eng/game-owl-ket/commit/74033479bcad56ded5bd8e85f997faaf01241ca4)|
|3/6|52-strix-hylophila-v8：成年窄尾带，保留v7较大幼鸟|[原图](https://github.com/janeytlin-eng/game-owl-ket/blob/989159469249c436506c03972bf85ceefbb5560c/owl-pet/design/originals/52-strix-hylophila-v8.png)|[归档](https://github.com/janeytlin-eng/game-owl-ket/commit/989159469249c436506c03972bf85ceefbb5560c) / [验证](https://github.com/janeytlin-eng/game-owl-ket/commit/9dbded24b35fd2ccfcc236e0d4ed62e11243d65c)|
|4/1|55-bubo-lacteus-v7：仅年龄归因标识|[原图](https://github.com/janeytlin-eng/game-owl-ket/blob/7e1f138ed207de46db36e6f53cfd923d44453470/owl-pet/design/originals/55-bubo-lacteus-v7.png)|[归档](https://github.com/janeytlin-eng/game-owl-ket/commit/7e1f138ed207de46db36e6f53cfd923d44453470) / [验证](https://github.com/janeytlin-eng/game-owl-ket/commit/2afd6eb563baade9412db0acc7257fe80748fff8)|
|5/2|57-bubo-nipalensis-v8：幼鸟面盘深环按原始照片柔化|[原图](https://github.com/janeytlin-eng/game-owl-ket/blob/9842079b2bd3f64a127f15c0abf52c67fbcbeace/owl-pet/design/originals/57-bubo-nipalensis-v8.png)|[归档](https://github.com/janeytlin-eng/game-owl-ket/commit/9842079b2bd3f64a127f15c0abf52c67fbcbeace) / [验证](https://github.com/janeytlin-eng/game-owl-ket/commit/681a8fc89d3160273dfffd6346bec6a01bcb2db4)|
|6/3|58-ketupa-coromanda-v8：仅野外估龄归因标识|[原图](https://github.com/janeytlin-eng/game-owl-ket/blob/4814bd4e8315174ad9ce957edd7da03a11626a79/owl-pet/design/originals/58-ketupa-coromanda-v8.png)|[归档](https://github.com/janeytlin-eng/game-owl-ket/commit/4814bd4e8315174ad9ce957edd7da03a11626a79) / [验证](https://github.com/janeytlin-eng/game-owl-ket/commit/3d140b98d93f402b71ddb5336a5e019d4ce002b3)|

[完整阶段、SHA256、来源事实/提示、审查、错误与计时审计](20261126T1427Z-audit.json)。每图research/species/版本.md含完整内置imagegen提示、来源ID/作者/年份/页码与事实边界；research/reviews/版本-review.md为实际看图结果。原图和concept精确字节双路径不可变GET、长度/SHA256/完整PNG解码通过；最新树与manifest单条ID核对通过，阶段与研究审查回读后才记账。

## 研究与实查

SOURCE_INDEX新增1（AWOO-OWLPAGES-2020），复用15次，16次引用去重11份资料；Mikkola同一本不重复计新来源。#57原始Srinivasan2013 pp106–107/图114实际本地PDF像素读取是已有来源访问范围升级1，不是新增论文。#51 Vukasovic2006p173实际重读保留啄壁与hualo顶腔；<=1周来自他种比较不是孵化日。#52 Menq正文新读、Verissimo既有照片检查历史复用，本次未重新看源照片；2024综述只历史复用。#55 Brown1965网络400Timeout，直接下载未抽出目标段，仍仅历史复用，不能把搜索摘要说成新读原文。#58原始Reddy/Ramachandran2023 pp44–45实际重读，8–10周为外观行为估计。每轮图鉴对应页实际读取。

## 错误、修订与未解决项

- #51首稿冠纹像网格，保存attempt1、再次imagegen编辑并看图，白纹断续和对比改善但仍有规则行列感，列后续校准，未称完全修好/科学通过。不要将#49冠白点换成该横纹规则。
- #52误用v6且漏查既有v7，duplicate guard在归档前触发；原图及研究曾被checkpoint触及，随后精确恢复并freshreadback核对。拒绝尝试另存design/originals/52-strix-hylophila-rejected1427-duplicate-attempt.png及research/species/52-strix-hylophila-rejected1427-duplicate.md，不计子轮。实际v8基于原v7保留已照片参照的较大幼鸟，仅尾纹调整。不能把无依据白雏重新覆盖较大阶段。
- #52/55/58立即ref回读不一致，最新提交和账本均确认真实已推送/记账后恢复，无重复生成/计数。需要用fresh branch/commit并immutable文件交叉核对，不能仅凭一次ref响应判断上传失败。
- #55/#58为注释修订，年龄参照不等于画中个体已测日龄；不计形态科学改善。#57实际照片纠正所选幼鸟粗黑面缘，不推断全年龄面缘/飞行时序，也不迁移至#55黑侧脸。

## 阶段时间与保存

|版本|研究墙钟STARTED→READY秒|生成等待秒|额外编辑等待秒|REVIEWED|ARCHIVED|VERIFIED|
|---|---:|---:|---:|---|---|---|
|49-strix-woodfordii-v7|91.7|41.7|0|2026-11-26T14:31:20.714Z|2026-11-26T14:31:24Z|2026-11-26T14:31:44.596Z|
|51-strix-rufipes-v7|53.3|40.5|39.096|2026-11-26T14:35:09.087Z|2026-11-26T14:35:13Z|2026-11-26T14:35:26.888Z|
|52-strix-hylophila-v8|238.8|103.7|0|2026-11-26T14:42:05.325Z|2026-11-26T14:42:09Z|2026-11-26T14:42:21.000Z|
|55-bubo-lacteus-v7|78.0|37.5|0|2026-11-26T14:45:03.846Z|2026-11-26T14:45:07Z|2026-11-26T14:45:20.537Z|
|57-bubo-nipalensis-v8|68.2|39.6|0|2026-11-26T14:47:52.925Z|2026-11-26T14:47:57Z|2026-11-26T14:48:10.977Z|
|58-ketupa-coromanda-v8|44.0|104.1|0|2026-11-26T14:51:24.271Z|2026-11-26T14:51:29Z|2026-11-26T14:51:41.735Z|

时间列为UTC，用户日期按北京时间2026-11-26；墙钟包含编排与检查，不是纯劳动。实际imagegen8次=六个最终结果＋#51一次再编辑＋#52一次拒绝尝试；不是8轮。未取得固定平台时长限制遥测。所有最终本地PNG在production1427/对应版本.png并已提交远端，完整提示在各研究档，内置工具没有切换API。

#25本地与远端完整PNG2864437字节/SHA256 729c187af12da587305c0c701c07440464896f5a6ada74431dfa3e7b19616ca1一致；fd9d70d远端422找不到提交，不重复出图。下一子轮1445Z第4/6，先选科学证据可推进的新物种/真实修正，优先保留#51残余冠纹待校准项。全251与整批科学集中审查未完成，未修改其他任务或调度。
