# 2026-11-27 本次串行完成6个生产子轮

状态：本次6轮VERIFIED（新增0种、修订6种），不同物种累计207/251，仍缺44种；图像版本1341，重复修订不计新物种。科学通过0、新用户确认0，本次6图均PASS_WITH_LIMITATIONS，不能等同科学通过。

先完成最早PARTIAL 20261127T0830Z第6轮，使该旧批次跨触发累计6/6；再开始20261127T0926Z并完成其1–5轮。当前批次累计5/6，其他未完批次0，下一子轮为20261127T0926Z第6轮。不是单个新批次在本次完成6/6。lease已释放，未改调度或任何其他任务；不声称后台生产或完成时间。

|本次轮次|编号/版本|实际批次子轮|修改与复查界限|不可变原图|提交证据|
|---|---|---|---|---|---|
|1|151-athene-jacquinoti-v6|20261127T0830Z 6/6|去掉缺乏物种巢位依据的显著树洞，仅调整环境呈现|[原图](https://github.com/janeytlin-eng/game-owl-ket/blob/a9410256f89aca7411c73896465064ad9d0eec67/owl-pet/design/originals/151-athene-jacquinoti-v6.png)|[VERIFIED 8c5eabc](https://github.com/janeytlin-eng/game-owl-ket/commit/8c5eabcfee89a009fef77931bdf0b87accb10d78) / [账本 c6974d2](https://github.com/janeytlin-eng/game-owl-ket/commit/c6974d25d77cb572dc4c4c0afc5e8099fbb3eb0d)|
|2|152-uroglaux-dimorpha-v6|20261127T0926Z 1/6|成年鸟黑色口须；首版过密如梳齿，二次编辑减稀，仍有平行化局限|[原图](https://github.com/janeytlin-eng/game-owl-ket/blob/508d595c60e65679b7a853e726dfb2abeeb10635/owl-pet/design/originals/152-uroglaux-dimorpha-v6.png)|[VERIFIED afd83a8](https://github.com/janeytlin-eng/game-owl-ket/commit/afd83a86f8bfb48ba77d56b6ac15ad1aef1c2e87) / [账本 0d3efeb](https://github.com/janeytlin-eng/game-owl-ket/commit/0d3efeb2d4bba829af55d5485861f47a0d0ff31b)|
|3|153-jubula-lettii-v6|20261127T0926Z 2/6|成年鸟趾背灰斑；局部被跗羽遮挡，精细边界仍待校对|[原图](https://github.com/janeytlin-eng/game-owl-ket/blob/e7bd80eedfe5c26a19611bd9f65a119c6fdc5398/owl-pet/design/originals/153-jubula-lettii-v6.png)|[VERIFIED 0384bce](https://github.com/janeytlin-eng/game-owl-ket/commit/0384bcedc10bdbb6d26958265de653f79bbf8a7d) / [账本 2ce95b5](https://github.com/janeytlin-eng/game-owl-ket/commit/2ce95b5c6ba1b520b287c8fe973385b02141c76c)|
|4|155-scotopelia-ussheri-v6|20261127T0926Z 3/6|成年鸟爪改淡角质色；保留有飞行观察依据的较晚幼鸟|[原图](https://github.com/janeytlin-eng/game-owl-ket/blob/ea2dfb1aa8a5f21724e81eafd1986bca9a2d5801/owl-pet/design/originals/155-scotopelia-ussheri-v6.png)|[VERIFIED d58e49f](https://github.com/janeytlin-eng/game-owl-ket/commit/d58e49fb66fe4a683203f0423ca6f941db05dad6) / [账本 627f5ac](https://github.com/janeytlin-eng/game-owl-ket/commit/627f5acf653e4cdc710a09e0a41eb721b0686120)|
|5|157-scotopelia-bouvieri-v6|20261127T0926Z 4/6|成年鸟暴露喙面由灰色改为淡黄角质色；肩斑冲突未擅改|[原图](https://github.com/janeytlin-eng/game-owl-ket/blob/433f472973c9cde798320a46cabba43f81b5ddb2/owl-pet/design/originals/157-scotopelia-bouvieri-v6.png)|[VERIFIED edf64c0](https://github.com/janeytlin-eng/game-owl-ket/commit/edf64c03b002abf36973c2c0b137c3b4f6c9330b) / [账本 d90115c](https://github.com/janeytlin-eng/game-owl-ket/commit/d90115c63767025e92a7f0bcfe24da21830397d2)|
|6|158-phodilus-badius-v6|20261127T0926Z 5/6|成年鸟爪改深棕角质色；保持已更正的Nias较晚幼鸟阶段|[原图](https://github.com/janeytlin-eng/game-owl-ket/blob/a01f79f3567dec4042d554897aba726080a1c57e/owl-pet/design/originals/158-phodilus-badius-v6.png)|[VERIFIED 992d749](https://github.com/janeytlin-eng/game-owl-ket/commit/992d749fdb81e78b0c55175d7399012990aadc8a) / [账本 b77bd7b](https://github.com/janeytlin-eng/game-owl-ket/commit/b77bd7ba73e3b8f7b702910ed6d629545629bf57)|

每个物种的[研究及完整提示](../../research/species/)和[实际审查](../../research/reviews/)按同编号文件可查；逐阶段运行记录、SHA256、字节数、来源及完整提示见[本次阶段审计](20261127T0926Z-stage-audit.json)。所有6张原图及concept分别从各自不可变归档commit完整下载，字节数/SHA256一致并PIL解码；研究/审查文件正文可读后才VERIFIED并推进账本。源文件/旧版本/既有确认记录保留。

## 资料索引与证据边界

[索引](../../research/SOURCE_INDEX.md)：新增1来源ID（VFO-BUTTIKOFER-1886-NLM-P247）；复用8个不同旧来源ID，共13次旧ID引用。合计9个不同来源ID、14次引用，不把同一本Mikkola图鉴的6次使用计为6条新出版物。实际图鉴页码481/PDF483、498/PDF500、357/PDF359、307/PDF309、308/PDF310、117–119/PDF119–121。图鉴本次可访问，并非仅搜索摘要。

新增来源完整书目补充（同ID元数据展开，不另计一条）：J.Büttikofer1886，Zoological researches in Liberia. A list of Birds, collected by Mr.F.X.Stampfli near Monrovia, on the Messurado River, and on the Junk River with its tributaries，Notes from the Leyden Museum8:243–268，原始URL https://repository.naturalis.nl/pub/508622/NLM1886008004014.pdf 。实际原文printed247/PDF5 §8；单一雌性标本、年龄未述、历史S.bouvieri鉴定存在地区疑问，不能作现代全物种或幼鸟普遍规则。黄色喙观察仅谨慎交叉参照，樱桃棕爪与图鉴黑爪冲突未据此修改。访问2026-11-27。

MNHN馆藏原文支持151历史名/标本，不支持幼鸟。Shany1995网站原始摘要本次读到，原始扫描本次不可达，历史读图事实有界复用。ML531449801本次Anubis拒绝访问，已保存访问状态更正，未谎称本次重读照片。155两篇原始野外/圈养记录实际读到；4–5月龄仅条件推算，不改写为已知出生日期。157Flickr原页元数据本次读取，未称本次重新看照片像素；Sharpe1875PDF因21,799,394bytes过大失败，其搜索摘录不作fresh验证。158Finsch1905printed26实际原文重读，Chasen跨页错误归属的旧纠正保留。全部仍未知项逐物种记录；没有因图片存在就标科学通过。

## 实际迭代与故障

152首图口须像平行梳齿，实际查看后拒收并保留attempt原图，二次内置imagegen编辑，视觉上减稀但残留平行化；未假称完全解决。共7次实际imagegen调用（6物种，152两次），其余5次均各1次编辑。151为避免无证据巢位暗示的设计调整，不声称发现确定巢位科学错误。153灰斑精细边界仍有遮挡。155/157/158爪喙色分别独立证据，禁止套用一条通用规则；155淡爪、157黑爪和158深角质爪不互相覆盖。

152归档首次遭GitHub RemoteProtocolError ServerDisconnected：核对最新main仍为REVIEWED后重试同一ARCHIVED，成功，未重复图或子轮。最终历史ledger并行批量回读遭Transport closed，改为公共不可变raw串行完整正文回读，不等同连接失效或CLI凭据故障。旧fd9d70d查询422无该commit；25组本地PNG2864437bytes Gitblob10508841ef5f6184e8658664615302909765c1dd，与远端既有blob核对后不重画。

发现JS阶段快照问题：save末尾旧快照回写导致前5个credit时运行记录阶段历史不全。不可变ARCHIVED提交仍保留实际全部归档阶段，原VERIFIED提交保留真实VERIFIED/exit0；从这些真实提交恢复完整历史，追加恢复说明并提交 b2a74dc796d88bbe9e2a3a57b05f88806b2fd6ce。没有篡改旧commit、重新生成或重计子轮。修正后第6轮最新运行记录保持完整VERIFIED。审计分别保存archive/verified/credit和阶段时间，不能用计划时间补造阶段。

## 可观测计时（秒）

|版本|STARTED→首RESEARCH_READY|本次最终生成/编辑等待|IMAGE_GENERATED→REVIEWED|REVIEWED→ARCHIVED|ARCHIVED→VERIFIED|
|---|---:|---:|---:|---:|---:|
|151-athene-jacquinoti-v6|25.7|38.516|5.6|5.4|22.8|
|152-uroglaux-dimorpha-v6|5.4|37.406|87.9|28.8|25.7|
|153-jubula-lettii-v6|5.2|39.347|5.2|6.5|22|
|155-scotopelia-ussheri-v6|4.7|39.632|5.2|5.2|24.6|
|157-scotopelia-bouvieri-v6|33.8|37.704|4.8|5.5|41.3|
|158-phodilus-badius-v6|24.5|102.481|5.2|6.1|43.7|

这些是实际阶段跨度，含工具/排队/复查，非纯CPU耗时；前置选题检索不全在STARTED内。152第二次编辑等待37.406秒，初次生成等待约41秒见原运行叙述；不把最终等待当两次总计。158等待102.481秒明显长于其他最终调用37–40秒，归档后完整验证跨度约22–44秒；样本仅本次，不推断固定平台上限。研究、完整提示、阶段增量已提交，scratch不被当持久归档。外部API未接入、未部署、未切换。

下一步：保留0926Z的next_cycle6，优先处理有新证据的缺失物种或已记录待修正问题。152残余口须平行化、153遮挡以及已登记110/130/134幼羽问题仍在校对范围；不能以细节修订冒充填补44个缺项。全251与集中整批科学审查未完成，不暂停任务。
