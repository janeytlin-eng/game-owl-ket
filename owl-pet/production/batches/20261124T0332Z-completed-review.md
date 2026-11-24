# 20261124T0332Z — 六轮完成及按编号审查入口

2026-11-24北京时间11:31:33–11:49:12完成本次六个串行子轮，随后最终审查归档。每轮均实际研究/增量索引、imagegen编辑、查看/复查、分阶段提交、原图回读/PIL解码/SHA256核验、账本提交回读。本次完成6轮，当前批次6/6；其他未完批次0，lease释放，下一子轮未来新批次1/6。不把旧0232Z批次重计。

新增物种0、修订6组，205/251不变（剩余46）。962→968个编号原图版本，manifest916→922，最终六条各恰好一次；保留旧版本和用户确认范围。三组形态修订、三组说明修订，不是6个新物种。均PASS_WITH_LIMITATIONS/scientifically_verified=false；新增用户确认0。251仍为约定范围，完整固定251名录映射缺口未解决，不宣布分类学总数获验证。

|子轮|原图|修订|归档提交|验证提交|阶段记录|
|---|---|---|---|---|---|
|1|[208-ninox-affinis-v3](../../design/concepts/208-ninox-affinis-v3.png)|喙色冲突/幼鸟未知/科学状态说明|[362c874e](https://github.com/janeytlin-eng/game-owl-ket/commit/362c874ef40c2c78cd8bef3d099f7028ce49ce42)|[e9756f97](https://github.com/janeytlin-eng/game-owl-ket/commit/e9756f9703e50f433bf5e50d8a9470e818d13451)|[run](../runs/20261124T0332Z-cycle1.md)|
|2|[210-athene-superciliaris-v2](../../design/concepts/210-athene-superciliaris-v2.png)|成年中央下腹白色及横纹渐淡|[b417a957](https://github.com/janeytlin-eng/game-owl-ket/commit/b417a9572652945304fd02f6ac13451ca5f7f103)|[bafd294c](https://github.com/janeytlin-eng/game-owl-ket/commit/bafd294c8e28933ae37d4954dc80757ad26a1c16)|[run](../runs/20261124T0332Z-cycle2.md)|
|3|[211-megascops-roboratus-v2](../../design/concepts/211-megascops-roboratus-v2.png)|幼鸟过熟折翼改为短软体羽遮盖|[edbf8252](https://github.com/janeytlin-eng/game-owl-ket/commit/edbf8252d9896615618e815ccbbea6e3f8ec4551)|[4c40240b](https://github.com/janeytlin-eng/game-owl-ket/commit/4c40240b910a04e8eb9222128e81e94eec723dd2)|[run](../runs/20261124T0332Z-cycle3.md)|
|4|[212-megascops-seductus-v2](../../design/concepts/212-megascops-seductus-v2.png)|Xochicalco人工管巢个案/估计年龄说明|[239c7003](https://github.com/janeytlin-eng/game-owl-ket/commit/239c7003fe85953ae89556e50696fd099e82f20d)|[a1af6d17](https://github.com/janeytlin-eng/game-owl-ket/commit/a1af6d17ebe2e1bdee0281b0017aa74a4d2f001a)|[run](../runs/20261124T0332Z-cycle4.md)|
|5|[213-glaucidium-tephronotum-v2](../../design/concepts/213-glaucidium-tephronotum-v2.png)|Cameroon幼鸟参考/未知年龄飞行说明；保留已见形成翼尾|[756f4ca0](https://github.com/janeytlin-eng/game-owl-ket/commit/756f4ca0c147f9c682a51a0bebd9c706145336af)|[5ecef115](https://github.com/janeytlin-eng/game-owl-ket/commit/5ecef115db751a7522855fb17d4105512643cb95)|[run](../runs/20261124T0332Z-cycle5.md)|
|6|[214-otus-balli-v2](../../design/concepts/214-otus-balli-v2.png)|幼鸟过熟折翼改为短软细横纹覆盖|[bb30b198](https://github.com/janeytlin-eng/game-owl-ket/commit/bb30b198439eaa05f6fc70103691ba081c927c37)|[00699c31](https://github.com/janeytlin-eng/game-owl-ket/commit/00699c3196d367b3c83c4458dd2d5da5493cb06d)|[run](../runs/20261124T0332Z-cycle6.md)|

## 来源与未知边界
[研究索引](../../research/SOURCE_INDEX.md)新增5条有用来源/页码定位：同一本Mikkola图鉴3条新页码定位（100、106、415），OwlPages两物种网页条目；不是5篇新论文。复用15条已有页码/来源记录实际重读（按文档去重10份，Mikkola六物种页计1本；另有两份原始文本/直接观察资料及机构/目录/物种网页）。更正已有来源事实0；新增Fishpool2023元数据线索1仍标原文未核验，不计已读论文。新条目ID已与本次开始索引去重。[缺口记录及完整元数据/URL/页码/限制](../../research/runs/20261124T0332Z-gaps.md)。

T.aurantia、T.sororcula、G.castaneum的图鉴幼鸟均明确未描述；补查未获得可验证幼羽新依据，因此未生成、不计完成。Castaneum与capense的名录冲突保留，不擅自增加唯一物种。Fishpool2023 PDF点击失败，仅实际读取元数据/目录；2015Demey/Borrow全文BHL本次403，仍未读；2014Borrow p24幼鸟照片实际查看，不伪称2015全文已读。

#210幼鸟依据为有限次级“较晚幼鸟”描述，与2013图鉴未描述并列保存；#211/#214柔软遮盖折翼为保守设计边界，不是实测羽长/羽龄；#213照片支持已形成折翼/尾，不能一概短翼化。#212原始2018 pp111–113/图3实际读取/查看，约两周是估计，PVC人工管巢是Xochicalco个案，不是普遍巢型。所有未知眼/喙颜色时序、精确羽龄/飞行能力、未证实雌雄比例继续标未知。

## 阶段时间与瓶颈（秒）
下表研究为子轮开始→RESEARCH_READY的墙钟间隔，部分资料在上一子轮增量查阅，不能当互斥纯研究CPU时长。生成等待是实际imagegen await；生成→检查间隔从生成checkpoint开始，尚包含其GitHub存储工作；归档→VERIFIED包含上传/下载/回读，不能当独立网络传输耗时。每轮一次imagegen编辑，共6次；没有把阶段数当子轮数。

|子轮|开始→研究就绪|imagegen等待|生成checkpoint→检查|归档开始→验证|
|---|---:|---:|---:|---:|
|1|186|45.473|6|23|
|2|47|55.611|6|32|
|3|8|51.665|7|31|
|4|42|46.594|6|22|
|5|33|45.751|6|21|
|6|33|47.821|6|30|

## 问题—证据—修改—复查与回查
- #210中央下腹黄褐且横纹延伸：图鉴471/次级描述支持奶白中央区域；局部编辑后实际全图/细节检查为较白渐淡，胸侧横纹保留。色彩精确标定仍未通过。
- #211/#214幼鸟外露翼片过长、成人式锐利：自身mesoptile证据不足以支持该成熟外观；改为较短软羽遮盖，分别放大查看翼末端/落脚支撑。只验证视觉约束改善，没有验证真实羽长序列。
- 回查#208软mesoptile与#210较晚羽衣、#213直接照片，后两者成熟一些的翼尾有其阶段依据，因此不迁移“所有幼鸟缩翼”规则。#213保留形成翼尾是本轮实际应用的反例，不是泛称改进。
- #208/#212/#213的科学状态和不确定性从侧车记录带入图面，实际复查可读；它们是说明修订，不虚报形态修正或科学通过。
- 每次归档从最新main重读manifest后合并，最终922条保留全部本批六条，上一批stale快照累积错误未重现。此运行内六次实际检验有效，不保证未经检验的外部并发。

## 实际错误与恢复点
一次JS解析错误发生于执行前，改正后才写研究；一次误用不存在的poll会话ID，实际下载文件均已完整本地恢复。#214先读错PDF134–136（印刷118–120，其他Scops）后改为PDF116–118/印刷100–102，不采用错页事实；书p101争议modestus的完整翼尾不能转作balli幼鸟证据。Sharpe1875 webPDF21799394字节限制由既有完整PDF正文重读接续。没有图片生成/归档/权限失败，没有平台超时遥测或固定运行时长结论。

## 最终核验与下一步
最新未截断GitHub tree5666路径，968编号原图/205规范物种；两个已归档亚种与旧名按原有映射合并。六张正式原图全部按各自不可变archive SHA重新下载、解码1536×1024、字节和SHA256匹配；研究/审查/索引/各run在对应归档commit读取成功后才推进账本，最后全部6条VERIFIED回读通过。无后台生产或预计完成时间声明。

未解决优先队列：#201幼鸟直接视觉证据（前次403/限流是历史错误，不伪称本次新尝试）；#206近端尾带受遮挡的总数/细纹校准；46种未归档及251规范名录映射；本次三种资料缺口的原始论文/确证幼羽再查。全清单及集中全批科学审查尚未完成，不暂停或修改生产/其他自动化。下一子轮新批次1/6须重新读取main/lease并优先选择能补充新物种或解决具体待修正证据的项目，不反复制作已标注的图片。
