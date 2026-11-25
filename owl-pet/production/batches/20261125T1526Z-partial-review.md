# 2026-11-25 23:26接续生产 PARTIAL
开始2026-11-25T15:26:10Z。已完成3轮/6：#57v7证据边界图注、#58v7喙尖定性弱调整、#56v3幼鸟脸盘外缘。新增0种、已完成修订3；第4轮#55v6实际imagegen编辑/整图局部查看/原图检查点已入main，但概念归档提交推main失败，不算完成。批次20261125T1526Z保持3/6,next4，不新建批次、不重复出图。

|轮|版本|原图|真实验证/记账|
|---|---|---|---|
|1|57-bubo-nipalensis-v7|[原图](https://github.com/janeytlin-eng/game-owl-ket/blob/798a65e258586e82fdf4fca9a8c219ec1ca69747/owl-pet/production/generated/57-bubo-nipalensis-v7-original.png)|[VERIFIED](https://github.com/janeytlin-eng/game-owl-ket/commit/dcf6ffbc48c4a764d1883725577ba2a509915f36) · [ledger](https://github.com/janeytlin-eng/game-owl-ket/commit/ea9f180112b0996733a09af26e0875ca269cb515) · [run](https://github.com/janeytlin-eng/game-owl-ket/blob/main/owl-pet/production/runs/20261125T1526Z-cycle1.json)|
|2|58-ketupa-coromanda-v7|[原图](https://github.com/janeytlin-eng/game-owl-ket/blob/e4da6e5d8fe797cbc62de8a34ab228f03743fbee/owl-pet/production/generated/58-ketupa-coromanda-v7-original.png)|[VERIFIED](https://github.com/janeytlin-eng/game-owl-ket/commit/ab5143ed15b40463cc17681e6b22d3bdb51a6534) · [ledger](https://github.com/janeytlin-eng/game-owl-ket/commit/290621b56200fca8fe47c7c64d49d098db4129b9) · [run](https://github.com/janeytlin-eng/game-owl-ket/blob/main/owl-pet/production/runs/20261125T1526Z-cycle2.json)|
|3|56-bubo-virginianus-v3|[原图](https://github.com/janeytlin-eng/game-owl-ket/blob/77a9ebd36bd9a8e0e2db8cb385b2af2d221f1eef/owl-pet/production/generated/56-bubo-virginianus-v3-original.png)|[VERIFIED](https://github.com/janeytlin-eng/game-owl-ket/commit/f3a348cc3ba41f0ec2c8f27dea047d7b0871db80) · [ledger](https://github.com/janeytlin-eng/game-owl-ket/commit/11ceb03fd6bbf5d430a595a888711ba83a296b43) · [run](https://github.com/janeytlin-eng/game-owl-ket/blob/main/owl-pet/production/runs/20261125T1526Z-cycle3.json)|

第4轮原图检查点：[main原图](https://github.com/janeytlin-eng/game-owl-ket/blob/13b4eb5ca139ff2971fbecd5eb8c1763be75dd37/owl-pet/production/generated/55-bubo-lacteus-v6-original.png)，blob17f1c29b0364fad5b5ec84ed37a067f382e34a29；[检查点commit](https://github.com/janeytlin-eng/game-owl-ket/commit/13b4eb5ca139ff2971fbecd5eb8c1763be75dd37)。本地/workspace/scratch/180c531d917a/owl-1526/55-bubo-lacteus-v6.png，完整生成提示/新来源在[research](../../research/species/55-bubo-lacteus-v6.md)。原图不是只留scratch。

## 实际故障与恢复点
第4轮archive attempt1 connectorReadTimeout；attempt2github.create_blob内部MCP-32603。改用inlineGitTree创建了孤立archive提交fe581d4fc6ee5d113d1003a0082d31a93e0d5440，其parent13b4eb5；但update_ref未成功，main回读仍13b4eb5。首次helper未检查update_ref.isError，已发现纠正：**提交对象存在不等于main已更新**。显式expected_sha=13b4eb5,forcefalse重试返回GithubGraphQLAPIError，2026-11-25T15:47:10Z request95BE:1DC27D:A9C7115:FAA645D:6B0702FD；其间fetch一次Transportclosed，后续读恢复。此孤立commit不能作main归档/完成证据。REST update_file已成功保存第4轮REVIEWED/PARTIAL记录为7e1fc31c62aaeab0da0155ac17aba4bc22612d56；之后基于最新main重试完整GitTree归档仍返回ReadTimeout，main仍7e1fc31。现用REST保存汇总，不假称后台继续绘图。恢复应先核对最新main树、旧run和孤立commit内容，必要时重新base_tree合并既有图片blob；原图可复用，不重新生成#55。

## 研究与实查
SOURCE_INDEX.md新增2文档：GHO-IOC-AGECHART-2017（InternationalOwlCenter三圈养窝群已知年龄图表，PDF1/12–15正文及图注；有食物/圈养/亚种适用限制），VEO-PEREGRINE-FUND-CURRENT（机构二手综述，WhatTheyDo48–49支持成年奶油角色喙，不给幼鸟同色）。复用9次定位/去重6文档（Mikkola同书4轮只计1）。Reddy2023printed45/PDF2原图71–73本次真正下载渲染打开，影像可读状态升级1，不作新文献。Srinivasan截图服务只给文字占位，不称看过照片。Gutenberg本次只新读前文/巢址，发育后段检索503，已在3f79b0d更正为旧记录复用。Brown1965Zenodo400文件过大，未新读正文，既有幼羽事实明确复用。图鉴新读：#57p289/PDF291，#58p292/PDF294，#56p262–263/PDF264–265，#55p286/PDF288。

- #57v7：实际整图和图注crop读取通过，救护阶段与自然支撑艺术转译分开；幼鸟ruff仍未知。非形态新增科学通过。
- #58v7：实际整图/喙尖crop，颜色弱变淡但边界硬，不能说精确校准完成；照片成鸟远，不能量喙尖比例，保留优先核验。
- #56v3：实际整图/幼脸crop清晰羽缘黑褐脸盘界，已知日龄圈养证据支持阶段，野生精确日龄不确定；平衡翼仍实质发育且覆绒，双足支撑。
- #55v6：实际新图/成年喙crop证实奶油角色成年喙、幼鸟蓝灰喙保留；pinklids/幼鸟白腿细灰横纹/低伏旧枝巢支撑保留。归档未完成，不计完成轮。

全sciencefalse；新增用户确认0。归档覆盖仍206/251（当前下限口径；全251权威名录对齐未完成），剩45，版本不作物种。其他PARTIAL0；本批余第4–6轮保留。未修改任何其他任务/调度；连接错误视为暂时故障，不自动停用生产。

## 阶段计时
每run保留STARTED/RESEARCH_READY/IMAGE_GENERATED/REVIEWED/ARCHIVED/VERIFIED事件。纯研究/纯编辑CPU工时未测即未知，事件间隔含检索与等待，不能当纯工时。Builtin等待#57记录于run；#58记录于run；#56约50.2s；#55约49.6s。首图编辑超过120s正常返回，不是平台超时。第4轮经REST 7e1fc31c62aaeab0da0155ac17aba4bc22612d56补存实际REVIEWED（main），不能把孤立ARCHIVED算成功。错误发生时仍保留租约，后续账本释放需另行回读。归档helper已增加update_ref.isError检查及main分支SHA回读；此修复已应用于重试，但因ReadTimeout未取得成功归档验证，不声称已验证有效。

结束时间 2026-11-25T15:52:22.229Z（北京时间 2026-11-25 23:52）。中止原因是实际GitHub写入工具错误，并非已确认的固定平台时长限制。第5–6轮未开始。
