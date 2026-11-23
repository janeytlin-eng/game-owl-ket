# #178 Otus insularis v5 — 科学校准状态标注修订

RESEARCH_READY 2026-11-23T23:42:42.899Z. 原图v4已实际全图查看，三鸟形态/支撑未发现本轮新错误；原图缺少概念图/科学校准待完成标注。仅修订标注，不覆盖v1–v4，不继承旧用户确认。未新增物种。

## 来源及实际读取
- **SSCO-CURRIE-ETAL-2004-P123-137**, Dave Currie, Rodney Fanchette, James Millett, Camille Hoareau & Nirmal J. Shah,2004, *The breeding biology of the Critically Endangered Seychelles Scops-owl Otus insularis: consequences for conservation and management*, Bird Conservation International14:123–137, DOI https://doi.org/10.1017/S0959270904000140 ; 实际重读出版社PDF pp124–126,128–130, Table1–2。https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E98F97E78DD111E5C95AE52C4D68D30B/S0959270904000140a.pdf/div-class-title-the-breeding-biology-of-the-critically-endangered-seychelles-scops-owl-span-class-italic-otus-insularis-span-consequences-for-conservation-and-management-div.pdf 。支持有绒羽/胸横斑的recent fledgling field category c8–12weeks；两巢幼鸟离巢时未会飞，后栖于巢上方枝条，一只约月后笨拙飞行；不能从此推定准确首飞日或逐羽生长。本文幼鸟观察用于保留既有阶段/支撑，不构造巢室或飞行动作。
- **SSCO-MIKKOLA-2013-P138**, Heimo Mikkola2013 *Owls of the World: A Photographic Guide*, 用户上传本printed138/PDF140本次实际读取。成人微小近隐耳簇、肩白斑、腹纵纹/横斑、裸跗跖与长趾；幼鸟描述笼统“似成鸟、不充分了解”，不能替代发育研究。支持保留物种轮廓，非新增幼鸟时序证据。
- **SSCO-CURRIE-ETAL-2002-P16-18**，沿用[v4研究](178-otus-insularis-v4.md)已核对的实测雌性平均质量方向及虹膜非性别/年龄规则。DOI https://doi.org/10.1080/03078698.2002.9674272 。本次出版社请求403，未冒称再次读到全文。保留近等高、雌略丰满与非普遍黄虹膜选项。
- 名称沿用现有名录 Otus insularis / protonym Gymnoscops insularis；无名录变更。

## 新增缺口来源（不用作#178形态）
**NBUR-INDRAWAN-SOMADIKARTA-2004-P160-170**. M.Indrawan & S.Somadikarta,2004,*A new hawk-owl from the Togian Islands, Gulf of Tomini, central Sulawesi, Indonesia*,Bull.B.O.C.124(3):160–171. 原始扫描 https://archive.org/download/bulletinofbriti124125brit/bulletinofbriti124125brit.pdf ; OCR https://archive.org/download/bulletinofbriti124125brit/bulletinofbriti124125brit_djvu.txt ; 原PDF镜像https://www.biologicaldiversity.org/campaigns/global_owl_project/descriptions/Ninox/Ninox%20burhani%20%28Indrawan%20%26%20Somadikarta%29%202004%2C%20Bulletin%20of%20the%20British%20Ornithologists%27%20Club%2C%20Vol.12.pdf 下载403后换IA实际读原文OCR pp160–170/type descriptions,Tables1–2,Observations。适用Ninox burhani成年雄标本/野外未定性别个体。两个标本均成年雄，支持成鸟白腹褐纵纹/细眉/裸跗跖等；野外3只并未定为幼鸟，不能以三鸟同现重建家庭/幼羽，未取得雌雄比例或巢/幼鸟发育依据。OCR未经逐字标本色表校准，正文身份与年龄边界可信，精确色号留待扫描。检索发现的泛站juvenile描述没有原始出处，未采用。DOI未取得。

## 问题—设计边界
v4没有印在画面上的科学状态，独立看图可能误以为校准图。加入清晰页脚；保留全部生物学设计及限制。新增规则：保存前检查画面状态而不只检查manifest字段。已回查#222v2页脚存在；#178v4缺失，故本轮实际应用；不声称全库已检查。
未知仍包括幼鸟准确年龄/虹膜频次/逐羽发育、巢材；PASS_WITH_LIMITATIONS,scientifically_verified=false。

## Full imagegen prompt
```text
Edit this exact existing #178 Seychelles Scops-Owl concept plate. Preserve all three owls' anatomy, face, iris colours, plumage, proportions, feet, supported perches, juvenile compact soft folded wing, labels, habitat, composition, lighting and tactile naturalistic maquette style. This is an annotation-only correction, NOT a biological repaint. Keep title "178 SEYCHELLES SCOPS-OWL" and italic "Otus insularis", roles "ADULT MALE", "ADULT FEMALE", "RECENT FLEDGLING (C. 8–12 WEEKS)". Add one elegant narrow dark brown/black footer with fine muted gold border at the bottom edge, below the three existing labels, readable exact text "CONCEPT · SCIENTIFIC CALIBRATION PENDING". Do not obscure feet, owls or labels. Footer status is essential: reviewed artwork is not a scientifically approved plate. Preserve 1536x1024 landscape, no new animals, no nest, no flight, no anatomical or age changes, no logo/watermark.
```
