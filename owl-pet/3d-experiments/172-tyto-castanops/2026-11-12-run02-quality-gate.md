# 棉棉 #172 — 3D自主打样 Run 02 (2026-11-12)
## Boundary
独立实验，不改 owl-pet 251 物种原型图、manifest 或生产工作流。来源为 `owl-pet/design/concepts/172-tyto-castanops-v3.png` 右侧的 age-unknown cream mesoptile（Git blob `5126b4bbc2d637aad4848b6c8a3825e7ef9bd05b`），已回读 `research/species/172-tyto-castanops-v3.md`、`research/reviews/172-tyto-castanops-v3-review.md` 与现存 Run01 审查。
## Actual experiment
独立使用 Python trimesh、skimage SDF marching cubes、VTK offscreen，完成三次**真正多边形三维网格**修订；采用连续一体头颈躯体表面、面盘渐变与面部浮雕、眼眶、角质喙、短绒羽包裹翅、3D弯曲绒羽缎带、脚趾与爪。导出 GLB、再导入校验，四机位（正、斜前、侧、背）实渲并检查。不是 SVG/平面形象。
|版本|bytes|部件|三角形|SHA256|
|---|---:|---:|---:|---|
|v03|7,027,304|27|239,964|`441d412aa34a47ca0efe9d76356e36c02093915b8b24d9ce4ce28d516baf4f27`|
|v04|5,862,244|27|205,164|`6f626415ad7e6f0f5eb6d62e683384ff598685129e58e2d16fd4cc8de694ce9b`|
|v05|6,606,852|23|224,340|`2040b270de4562e2c5ee443381fdcc5f6a06862e6df1179ad539eb862e24f435`|

v05 主体水密，46,688 面。离线 WebGL2 查看器 HTML 构建完成（单文件约 8.8MB，内嵌 GLB）。已尝试 Chromium 验证，但环境屏蔽 file:// 与 localhost，均报 `ERR_BLOCKED_BY_ADMINISTRATOR`，所以**绝不声称手机端运行通过**。
## Quality gate: FAIL — 不通知用户
正面脸盘虽从浮贴式图案改为连续主体凹面、减小眼睛喙尺寸，**仍像梨形毛线玩偶**；缺失原图真实羽缘、深刻脸盘和柔软二期绒羽。绒丝偏锯齿/针状，侧视豆形，翼部体量不足，双足的支撑与树洞边缘关系未实现，背面明暗失真。尚不达到用户“有点看得过去”的门槛。**用户不应收到验收通知**。二维原型 v3 不变。
## Tools and next iteration
fal Hunyuan 3D Pro 账号无余额，未付费；Anatomy Skill 实为等轴技术 SVG/WebGL 图解，不是动物绒羽建模；本机无 Blender/bpy 和训练权重，trimesh+VTK 可用。下一轮优先解决原型参考图的多机位重建、PBR 绒羽材质、真实心形脸盘结构、短翼和站姿；建立可重复视觉评分后再做互动。

本轮源代码、v03–v05 GLB、渲染审查格与证据包另作为独立本地 `mianmian_172_3d_run02_rejected_experiments.zip`（失败实验，不进入正式生产素材）。