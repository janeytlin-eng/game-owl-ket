# 2026-11-27 05:30 起生产 — 本次完成6轮
截至 2026-11-26T21:54:32.441Z（UTC；用户时区Asia/Shanghai+08）。
本次新增0种、修订6种，按规范学名去重已归档207/251，缺44种。1191张编号版本图≠1191种；219个历史编号≠219个不同学名。所有6最终图科学核准false、新用户确认0；概念图通过有限范围检查不等于科学通过。当前总用户确认数未知，不迁移旧版本确认。
本次执行旧批次20261126T2030Z-B2第4–6子轮，跨触发累计6/6；随后新批次20261126T2130Z-B2第1–3子轮，累计3/6、下一4。其他PARTIAL批次0，lease释放。不是声称单个旧批次本次做了6轮。未完成全部251及整批科学审查，不停用任务、不改其他自动化。

## 六最终组图、实际SHA与审查入口
|本次轮|批次/子轮|物种/版本|修订|不可变原图|VERIFIED提交|
|---|---|---|---|---|---|
|1|20261126T2030Z-B2/4|95-pulsatrix-melanota-v8|幼鸟定向绒羽重建；另一次去金框|[PNG](https://raw.githubusercontent.com/janeytlin-eng/game-owl-ket/f6a98334923c2fdb0c59be07430f872b1ea6ed62/owl-pet/design/originals/95-pulsatrix-melanota-v8.png)|[7bc2b827](https://github.com/janeytlin-eng/game-owl-ket/commit/7bc2b827f6fc5bfa79bf9f9599dd08c7a865e5e8)|
|2|20261126T2030Z-B2/5|86-otus-elegans-v9|幼鸟头脸短绒纹限定修正|[PNG](https://raw.githubusercontent.com/janeytlin-eng/game-owl-ket/b31cf4b1687753df932c3695034ce7c470f532b6/owl-pet/design/originals/86-otus-elegans-v9.png)|[9f7d2977](https://github.com/janeytlin-eng/game-owl-ket/commit/9f7d2977a4e7a2d69a449845f0bd3fcb2be08323)|
|3|20261126T2030Z-B2/6|97-lophostrix-cristata-v7|成年下腹细淡虫纹；二次恢复深色上胸|[PNG](https://raw.githubusercontent.com/janeytlin-eng/game-owl-ket/cef3122b6674568e6bb1956fc5c1aeffb07e6ab4/owl-pet/design/originals/97-lophostrix-cristata-v7.png)|[5db73b4a](https://github.com/janeytlin-eng/game-owl-ket/commit/5db73b4ac2309a553c93b178d6896a021585934c)|
|4|20261126T2130Z-B2/1|98-strix-chacoensis-v7|成年喙基角灰色/黄尖|[PNG](https://raw.githubusercontent.com/janeytlin-eng/game-owl-ket/f64cb41bfd07aa9dbd7782ec125444caeb22f98c/owl-pet/design/originals/98-strix-chacoensis-v7.png)|[0dd62c87](https://github.com/janeytlin-eng/game-owl-ket/commit/0dd62c87cb51ebd9eb02594472a3a4ce92b18270)|
|5|20261126T2130Z-B2/2|99-bubo-magellanicus-v6|撤销虚构干草垫，裸阳台地面|[PNG](https://raw.githubusercontent.com/janeytlin-eng/game-owl-ket/20310c6ee99fcfa9dc1390965f26cd673231360f/owl-pet/design/originals/99-bubo-magellanicus-v6.png)|[cb776060](https://github.com/janeytlin-eng/game-owl-ket/commit/cb77606021fa7439f4c2893d0ac292e1c5873c82)|
|6|20261126T2130Z-B2/3|100-strix-huhula-v7|仅案例/亚种/未知阶段标识|[PNG](https://raw.githubusercontent.com/janeytlin-eng/game-owl-ket/e828cec765363b181aa255a65f65c724abf0b6d6/owl-pet/design/originals/100-strix-huhula-v7.png)|[612a2043](https://github.com/janeytlin-eng/game-owl-ket/commit/612a2043034c2f5a7109732fc68e6810ae31a6fc)|

5轮图像内容修订+1轮标识修订；8次实际内置imagegen（95、97各2次，其余各1次），首稿保留于production/attempts，不额外计轮。每图整图已实际查看，95/86另有本物种实拍局部依据，必要局部检查见各run；没有科学签字。六图originals/concepts两不可变路径实际GET，完整bytes/SHA256/PIL全图解码通过；研究/审查/账本回读验证。实际完整prompt、来源事实与推断边界均按轮保存。

- **95-pulsatrix-melanota-v8**：[研究](../../research/species/95-pulsatrix-melanota-v8.md)、[实际复查](../../research/reviews/95-pulsatrix-melanota-v8-review.md)、[阶段运行记录](https://github.com/janeytlin-eng/game-owl-ket/blob/main/owl-pet/production/runs/20261126T2030Z-B2-cycle4-resume2130Z-95-pulsatrix-melanota-v8.json)、[归档提交](https://github.com/janeytlin-eng/game-owl-ket/commit/f6a98334923c2fdb0c59be07430f872b1ea6ed62)、[计账提交](https://github.com/janeytlin-eng/game-owl-ket/commit/5a41078db83464b042675543c4f3c4707092980f)。
- **86-otus-elegans-v9**：[研究](../../research/species/86-otus-elegans-v9.md)、[实际复查](../../research/reviews/86-otus-elegans-v9-review.md)、[阶段运行记录](https://github.com/janeytlin-eng/game-owl-ket/blob/main/owl-pet/production/runs/20261126T2030Z-B2-cycle5-resume2130Z-86-otus-elegans-v9.json)、[归档提交](https://github.com/janeytlin-eng/game-owl-ket/commit/b31cf4b1687753df932c3695034ce7c470f532b6)、[计账提交](https://github.com/janeytlin-eng/game-owl-ket/commit/64d90d9f7448140193a34a63604353efdc262dd2)。
- **97-lophostrix-cristata-v7**：[研究](../../research/species/97-lophostrix-cristata-v7.md)、[实际复查](../../research/reviews/97-lophostrix-cristata-v7-review.md)、[阶段运行记录](https://github.com/janeytlin-eng/game-owl-ket/blob/main/owl-pet/production/runs/20261126T2030Z-B2-cycle6-resume2130Z-97-lophostrix-cristata-v7.json)、[归档提交](https://github.com/janeytlin-eng/game-owl-ket/commit/cef3122b6674568e6bb1956fc5c1aeffb07e6ab4)、[计账提交](https://github.com/janeytlin-eng/game-owl-ket/commit/fe967e0793fa2680fb9ccc43f7e1ff1353582ae9)。
- **98-strix-chacoensis-v7**：[研究](../../research/species/98-strix-chacoensis-v7.md)、[实际复查](../../research/reviews/98-strix-chacoensis-v7-review.md)、[阶段运行记录](https://github.com/janeytlin-eng/game-owl-ket/blob/main/owl-pet/production/runs/20261126T2130Z-B2-cycle1-resume2130Z-98-strix-chacoensis-v7.json)、[归档提交](https://github.com/janeytlin-eng/game-owl-ket/commit/f64cb41bfd07aa9dbd7782ec125444caeb22f98c)、[计账提交](https://github.com/janeytlin-eng/game-owl-ket/commit/dd1b4dc7dd4b6a1e2d48f7b8ec960d89f40ba350)。
- **99-bubo-magellanicus-v6**：[研究](../../research/species/99-bubo-magellanicus-v6.md)、[实际复查](../../research/reviews/99-bubo-magellanicus-v6-review.md)、[阶段运行记录](https://github.com/janeytlin-eng/game-owl-ket/blob/main/owl-pet/production/runs/20261126T2130Z-B2-cycle2-resume2130Z-99-bubo-magellanicus-v6.json)、[归档提交](https://github.com/janeytlin-eng/game-owl-ket/commit/20310c6ee99fcfa9dc1390965f26cd673231360f)、[计账提交](https://github.com/janeytlin-eng/game-owl-ket/commit/3db39f1f29c41741aa1854113f961723317e9bc0)。
- **100-strix-huhula-v7**：[研究](../../research/species/100-strix-huhula-v7.md)、[实际复查](../../research/reviews/100-strix-huhula-v7-review.md)、[阶段运行记录](https://github.com/janeytlin-eng/game-owl-ket/blob/main/owl-pet/production/runs/20261126T2130Z-B2-cycle3-resume2130Z-100-strix-huhula-v7.json)、[归档提交](https://github.com/janeytlin-eng/game-owl-ket/commit/e828cec765363b181aa255a65f65c724abf0b6d6)、[计账提交](https://github.com/janeytlin-eng/game-owl-ket/commit/b6aee941f0897bc88e9d74a1e132cea89c348b12)。

## 主动研究和知识库
[来源索引](../../research/SOURCE_INDEX.md)已增量提交。新增来源ID/出版物0；复用12次定位引用，书籍别名归并后7份独立旧文档；实际照片访问升级2（95图鉴p314上身、86机构PDFp4 Photo1），不是新出版物。
- #95：MEL-RIVAS-FUENZALIDA-BURGOS-2022-84-88原文p84–86实际读；原图Fig3的404/403以及原PDF403/出版社503未解决，不声称看过该图像。可访问上传Mikkola2013 printed314/PDF316实际图文：较老幼鸟只借上身绒羽，绝不借成熟翼尾；2022文字支持肉桂绒/白冠变化但无精确年龄。
- #86：ELE-BIRD-RESEARCH-NEWS-2011-P1-2旧ID沿用，实际printed4–5/PDF1–2，p4 Photo1实际打开，为南大东interpositus巢口头部，只校头脸不外推隐藏身体。图鉴printed160/PDF162复用。
- #97：CRI-MIK2013-358和CRI-BIRDS-BOLIVIA-2026实际正文，后者页面更新2021-08-20，ID年份非出版年；图鉴p358暗上胸/淡下腹/细虫纹限定。Wetmore尾纹既有校正保留，没有冒称本轮重读。
- #98：CHAO-NBO-2013原作者正文DetailedDescription/BareParts/Measurements/Reproduction实际阅读，图鉴p336/PDF338；喙基/尖分区为定性设计，幼鸟裸部不套成年配色，圈养出巢记录不当野外首飞年龄。
- #99：MAG-NOVOA-BLANCO-2020-P31-33实际原文p32明确裸阳台地面、无巢材，纠正v5反向误读1条；MAG-MIK2013-266实际上传书p266/PDF268。不同阳台案例材料不得混用。
- #100：HUH-BC2013旧SORA链接现跳集合，新增恢复访问URL（不是新论文）1条：机构文章页及作者上传全文p175实际读；HUH-MIK2013-340实际图鉴p340/PDF342。18Nov观察时点不等于精确孵化日龄；旧Ciccaba huhula albomarginata对应现Strix，不新增分类范围。
共2条索引纠错：99事实、100URL；原文历史保留。来源ID、原始URL/作者/年份/页章/阶段/限制/设计决策见6研究卡与中央索引。未读新检索线索不算核验。

## 问题—证据—修改—复查及限度
95新稿绒圈减少但生成器加金框：保留首稿、第二次仅去装饰，复查羽被未明显回退。86照片约束头部短绒，身体卷纹仍未校准，不宣称全幼鸟解决。97初次淡化越界上胸，依据p358恢复暗上胸，保留下腹细纹；经验只在该图验证。98成年喙分区有效，未转用幼鸟。99纠正源头误读并撤销干草垫；不能因其它猫头鹰画草巢而否定此原文。100仅标识修订，没有虚报形态发现或新科学结论。所有固定性别高度/幼鸟首飞等仍未知。
回查影响边界：86不同于85趾羽，97下腹不同于86成年轴纹，98不传成年喙色给幼鸟，99需按案例查阳台而非全局删巢材，100保留已校爪色；没有进行未记录的批量改图。上述规则及应用/单图有效性已写WORKFLOW_LESSONS.md。

## 阶段时长与实际错误
[阶段审计JSON](20261126T2130Z-stage-audit.json)保留每轮真实阶段时标、等待与SHA。研究开始至RESEARCH_READY是事件窗口，部分材料在上一子轮预取；不冒充独立研究CPU时间。imagegen等待精准围绕调用计时，检查/提示编辑/上传独立用时未单独埋点则标未知。
|物种|研究事件窗口秒|首生成等待秒|二次编辑等待秒|REVIEWED→ARCHIVED秒|ARCHIVED→记录复核秒|
|---|---:|---:|---:|---:|---:|
|95-pulsatrix-melanota-v8|147.270|30.015|37.441|3.066|171.638|
|86-otus-elegans-v9|27.936|37.648|0.000|3.383|17.756|
|97-lophostrix-cristata-v7|26.835|41.520|35.431|3.209|27.835|
|98-strix-chacoensis-v7|4.006|34.952|0.000|2.963|77.945|
|99-bubo-magellanicus-v6|4.321|38.855|0.000|3.090|20.680|
|100-strix-huhula-v7|32.688|30.589|0.000|3.128|20.554|

8次等待合计286.451秒，95/97返修增加两次等待与归档步骤。95照片访问失败和后续恢复检查、原图上传/回读也占事件间隔，不能仅以生成等待推算完成速率。
实际错误完整记录：95外部图404/403/PDF403/出版社503；95首稿金框；97上胸越界已返修；异步下载100尚未完成即view返回文件不存在，下载结束后已重开真实图；98首次校验poll仍运行时提前计账，随后实际双路径exit0通过后才进入下一轮，后续审计曾从旧对象覆盖阶段为ARCHIVED，已从原始验证提交恢复VERIFIED并保留纠错。98最终验证依据提交为0dd62c87cb51ebd9eb02594472a3a4ce92b18270，原过早验证SHA历史保留，不重复计数。今后必须先观察exit0再计账；不把调用开始当成功。不虚构固定平台超时/后台生产或完成预计。
#25本地2864437bytes保留，当前远端相同blob10508841ef5f6184e8658664615302909765c1dd，未重复画；fd9d70d当前连接回404，不当真实远端恢复提交。

## 下一接续
当前20261126T2130Z-B2 next_cycle4；优先核对最新main/lease并筛查下一待修正项或证据充分的缺图种，尚未为下一物种占坑/生成。207/251未改变，44缺图仍需可靠幼鸟资料；现图全部科学未核准，当前总用户确认未知。未完批次仅本批次，其他0，lease空。
