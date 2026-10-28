# 43 · 林斑小鸮 / Forest Owlet

- 现行学名：*Athene blewitti*；历史常用名：*Heteroglaux blewitti*。
- 阶段：RESEARCH_READY；科学验收仍为false。

## 证据与设计边界

- Mikkola印刷页421–423支持成年近乎无斑头背、实色胸带、下胸中央白块、胁部粗横斑、黄眼和无耳簇；明确无性别尺寸数据。
- 同页正文称juvenile未描述，但页423标注的未成年实物照片显示脸盘较不发达、腹面强红褐横纹。本轮只采用这些可见特征，不写完整幼羽序。
- Ishtiaq & Rahmani原始繁殖观察支持约40日离巢且随后继续依赖亲鸟；选刚离巢、洞口抓握阶段，不画成熟长飞羽或完全独立动作。
- Koparde et al. 2018支持从旧属 *Heteroglaux* 映射至现行 *Athene*。
- 成鸟雌雄保持近似尺度；开放落叶林而非密闭冠层。

## 完整ImageGen提示

Create a polished scientific-reference virtual-pet character sheet in the same warm storybook-naturalist style. Landscape 4:3, parchment lower margin, central Indian open deciduous forest with lower canopy, one real tree cavity and sunlit branch. Exactly three full-body Forest Owlets: adult male left, adult female center, recently fledged about-40-day-old juvenile right at the cavity lip. Current species Athene blewitti (historical Heteroglaux blewitti). Adults: compact stocky owl 20–23 cm, no ear tufts, yellow eyes, yellowish bill with dark-tinged cere, plain brownish-grey crown and mantle essentially unspotted except a few tiny pale speckles and sparse scapular/wing-coverts spots, very weak nape false-face, broad white throat patch, solid grey-brown upper breast band, plain white lower-breast center and belly, broad dark brown flank bars, white feathered tarsi and long dirty-yellow toes with heavy dark claws; dark brown tail with broad whitish bars and terminal band. Do not confuse with Athene brama: Forest Owlet must have far fewer crown/back spots, a solid pectoral band and plain white central lower breast. No sexual size-difference data: male and female same apparent height and volume, only natural pose differs. Juvenile: age-supported recently fledged individual, securely gripping the cavity rim; facial disc less developed than adult, softer shorter juvenile wing and tail, warm reddish-brown horizontal belly markings, head and back still mostly plain/unspotted, no mature long layered remiges; alert but dependent posture. Exactly three birds, all feet supported, no eggs, no prey, no fantasy accessories. Bottom labels only: "43 FOREST OWLET" and italic-style "Athene blewitti".

## 生成、检查与迭代

首稿成鸟识别与雌雄尺度通过；幼鸟翼面误生成人成鸟式白斑和完整层叠飞羽。定向编辑移除白斑、缩短并软化翼尾后复查通过。未解决：图鉴正文仍称juvenile未正式描述，当前只采用同页未成年实拍的较弱脸盘与红褐腹横纹，以及原始观察支持的约40日龄离巢动作阶段。

- 图片：`design/concepts/43-athene-blewitti-v1.png`
- blob：`5efc556a538c88a4b4a195b7a3bc7da1abe79b6b`
- SHA-256：`f3ab99c772c8e005ca045e2b74acc4b6ec1ca8a3246fefa0e21b785400ba03a8`
- 图片提交：`a31497b02ab1450c80c3b7456c07aae172583e07`


## 2026-10-26 v2 evidence-bounded revision

- Image: `design/concepts/43-athene-blewitti-v2.png`; archive commit `0add92a7742da2be5654d5060eb9ceb8e97e1eb0`; Git blob `392d29ec7bf7cf01413b72a83e72b7311811c876`.
- New habitat source `FOW-KHAN-2023-HABITAT` was read with four existing sources. Large-tree stands need not be closed-canopy and may adjoin agricultural cover.
- First render correctly separated Forest Owlet from Spotted Owlet but gave the fledgling adult-style white wing rows and mature layered remiges. One juvenile-only edit removed those rows, shortened and softened the wing, concealed the tail and retained both-foot/belly support.
- Remaining unknowns: complete juvenile feather sequence, population plumage variation, sex measurements and universal nest geometry. `scientifically_verified=false`.

## 2026-10-28 v3 research-ready correction

- New primary source `FOW-JATHAR-2004`, printed pp.53–55, supplies a multi-nest development sequence: 26–33 d nestling period (mean 30 d); at 28–30 d young perch near the nest, have stumpy tails and poorly developed primaries/secondaries, fly weakly/reluctantly, and show a highly blotched ventrum with central vertical streaks.
- Full text of `FOW-ISHTIAQ-2005` was read and its prior short-extract record corrected. Three mating-observed pairs suggested only slight female size difference; more belly barring occurred in two pairs and was explicitly not established as consistent.
- The 30 d versus 40 d fledging records are retained as study/sample variation. V3 selects the separately described 28–30 d weak-flight nearby-perch stage rather than claiming a universal fledging day.
- Reused `FOW-MIKKOLA-2013` (printed pp.421–423), `FOW-KOPARDE-2018`, `FOW-PEREGRINE-2026` and `FOW-KHAN-2023-HABITAT`.
- Unknown: exact feather-by-feather chronology, universal sex dimorphism and population variation. Science remains false.

## Complete ImageGen prompt for v3

Scientific-educational owl electronic-pet concept sheet in the established warm painterly semi-realistic style, horizontal 3:2 board. Title exactly “43 · FOREST OWLET · Athene blewitti”. Exactly three full-body Forest Owlets with exact labels “ADULT MALE”, “ADULT FEMALE”, and “JUVENILE”. Adults: compact stocky 20–23 cm owls, round untufted heads, yellow eyes, yellowish bill with dark cere, plain brownish-gray crown and mantle with almost no white spotting, only a few tiny pale scapular/wing-covert marks, weak nape false-face, white throat patch, solid gray-brown upper-breast band, white central lower breast and belly, broad dark-brown flank bars, short broadly barred tail, feathered tarsi and sturdy yellowish toes. Do not confuse with spotted owlet: no densely white-spotted crown/back and no all-over scaly underparts. Female may be only subtly larger and may have slightly more extensive belly barring than male, because this was reported in a few observed pairs but is not established as universal; avoid exaggerated size difference. Juvenile: evidence-bounded 28–30-day recently emerged bird, standing low on the natural cavity rim or immediately adjacent short rough branch with both feet fully supported; body darker than adults, still soft juvenile texture, yellow iris ring visible, shorter less-developed facial pattern, very stumpy tail, primaries and secondaries visibly short/ill-developed rather than mature layered adult wings, breast and belly highly blotched with a central field of vertical streaks; alert and capable only of weak reluctant short flight, but show it perched and dependent, not airborne. Habitat: central Indian open dry deciduous teak woodland with a real mature-tree cavity, sparse grasses and open agricultural edge light; natural cavity debris only. Three distinct calm poses, clean separation, no extra birds, no ear tufts, no eggs, no prey, no fantasy accessories, no watermark, and no text beyond the exact title and labels.

## v3 production result — 2026-10-28

- The full BNHS development sequence and complete Ibis text were applied; source change: new 1 / reused 4 / corrected 1.
- Initial 1536×1024 render passed adults, title, labels, count, support and habitat but failed juvenile-wing maturity.
- One targeted imagegen edit shortened and softened only the juvenile wing and removed/reduced the adult-like long layered remiges and spot rows.
- Full edited master and 680×453 derivative were opened and passed with limitations.
- Concept: `design/concepts/43-athene-blewitti-v3.png`; SHA-256 `107f434ab8f45df6b5d2527a094b677c7615034b3c80a6fe45805a86af302d75`; Git blob `43d3d2d67e79cae7bdab06088c79cdaabf9de468`.
- Reviewed master: `production/reviewed/43-athene-blewitti-v3-reviewed-master.jpg`; SHA-256 `53d9fc030ca72dc11ceea92b8afa5931f3a3b8b5b758bfd09cea2ef9595c48dc`; Git blob `fc85ee69eb4d33898b626fd5ce4d8218a840d795`.
- Scientific status remains false; exact feather chronology, population variation and universal sexual dimorphism remain unknown.
