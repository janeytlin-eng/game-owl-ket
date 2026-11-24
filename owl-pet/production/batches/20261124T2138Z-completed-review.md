# 20261124T2138Z 六轮接续审查入口

原批次已完成6/6，跨执行完成：前次5轮，本次恢复第6轮1轮。不得称本次单次六轮成功。新增物种0；原批次6物种修订，本次仅#19v6修订1。去重206/251，剩余45；全部科学校准false，用户确认未继承。

|轮次|编号原图|验证提交|审查|
|---|---|---|---|
|1|[04-athene-noctua-v6](https://github.com/janeytlin-eng/game-owl-ket/blob/a0d7aa11c2667cb7e5f1e851692546ad347fef32/owl-pet/design/concepts/04-athene-noctua-v6.png)|[ca028dbc](https://github.com/janeytlin-eng/game-owl-ket/commit/ca028dbc2cc9936d4bf51fe0b10238ed726c0272)|[研究](../../research/species/04-athene-noctua-v6.md) / [审查](../../research/reviews/04-athene-noctua-v6-review.md)|
|2|[06-asio-otus-v5](https://github.com/janeytlin-eng/game-owl-ket/blob/95072c7ecd74f445de44d2bc72ee5026a1d581fe/owl-pet/design/concepts/06-asio-otus-v5.png)|[289420f1](https://github.com/janeytlin-eng/game-owl-ket/commit/289420f13019e99896a1e0d1fe4655a8c95e1151)|[研究](../../research/species/06-asio-otus-v5.md) / [审查](../../research/reviews/06-asio-otus-v5-review.md)|
|3|[07-asio-flammeus-v5](https://github.com/janeytlin-eng/game-owl-ket/blob/ccd378ff4bdf4b21c4e9089969b7e81084938307/owl-pet/design/concepts/07-asio-flammeus-v5.png)|[50780c5e](https://github.com/janeytlin-eng/game-owl-ket/commit/50780c5e8cc63fe548bd43a57ff5d2c780f145be)|[研究](../../research/species/07-asio-flammeus-v5.md) / [审查](../../research/reviews/07-asio-flammeus-v5-review.md)|
|4|[11-aegolius-funereus-v5](https://github.com/janeytlin-eng/game-owl-ket/blob/844aad7fcda11d4b5ef072d0b970bc6ab2562185/owl-pet/design/concepts/11-aegolius-funereus-v5.png)|[79f7f973](https://github.com/janeytlin-eng/game-owl-ket/commit/79f7f973249810aee6a699857c37c55468cb6bbd)|[研究](../../research/species/11-aegolius-funereus-v5.md) / [审查](../../research/reviews/11-aegolius-funereus-v5-review.md)|
|5|[16-strix-occidentalis-v5](https://github.com/janeytlin-eng/game-owl-ket/blob/258a53373eae25f60245c02259ab8fbfbe7925dd/owl-pet/design/concepts/16-strix-occidentalis-v5.png)|[5a6efd5e](https://github.com/janeytlin-eng/game-owl-ket/commit/5a6efd5e0bcd7d92b078d9911fbd6643ca568ffd)|[研究](../../research/species/16-strix-occidentalis-v5.md) / [审查](../../research/reviews/16-strix-occidentalis-v5-review.md)|
|6|[19-megascops-trichopsis-v6](https://github.com/janeytlin-eng/game-owl-ket/blob/0a5313d645e600ece5bb060c410fdfbfbf932a48/owl-pet/design/concepts/19-megascops-trichopsis-v6.png)|[1e685737](https://github.com/janeytlin-eng/game-owl-ket/commit/1e6857375114d13937c0f81741e82d8fe74d5011)|[研究](../../research/species/19-megascops-trichopsis-v6.md) / [审查](../../research/reviews/19-megascops-trichopsis-v6-review.md)|

## 实际复查
2026-11-25恢复阶段实际查看六张最终图1200x1260合成审查图：每组3鸟，成年雌雄及幼鸟有自然支撑，未见额外肢体/悬空，幼鸟姿态包括洞口低伏、树枝站立、地面步行、巢室低攀、侧向树枝步行。阶段/年龄仍为各记录证据边界，不能因合成图清晰就科学通过。各原图独立GET/SHA256/解码证据见六run；本次实际新GET#19原图2911957bytes/1536x1024/SHA256351ff22b8c8f1476e3edb66fcb0a1243feaa5fc4e810f9101584323d6924eef1。

#19两次定向编辑：首版仍保留白长丝扇，实际脸部crop判需修；二版保留细须状羽并明显收敛长白丝。真实照片未标年龄性别，不能当性别/幼鸟模板；须长精确度仍未知。图鉴喙色冲突保留，无改色。#03原足羽已覆盖，原批次候选被否决，无重复出图/计数；#04看冠顶绝对高度造成雄大误判已按足位核查否决。#06/07/11足羽规则不能迁移到#16趾端刚毛或#19裸趾。

## 研究索引与瓶颈
原批次新增5来源，本次新增2（Arenas等2020康复原始论文、Hubick2008实物摄影），原批次共7；共享Mikkola图鉴复用6个物种页段，文献去重为同一本，非6部图鉴。第6轮生成等待38832ms、第二编辑40159ms；阶段时间与完整提示均在run。原租约过期前只STARTED，未丢图；恢复从研究继续。此前只读指令中断，非平台超时。其他source-specific失败如PDF403/HTML阻断并非GitHub连接失败。

下一子轮：新批次1/6，先读最新main/lease，优先有证据的缺失物种或实际待修项目。未完成全部251/集中科学审查，未暂停或修改其他自动化。此入口仅该批六版本审查，非全清单最终验收。
