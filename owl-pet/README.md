# 猫头鹰3D电子宠物

本目录是独立电子宠物项目，原仓库根目录的猫头鹰词汇游戏保留。

## 项目入口

- [知识总纲（初始快照）](knowledge/OVERVIEW.md)
- [分类与命名](knowledge/TAXONOMY.md)
- [身体结构与姿态](knowledge/ANATOMY_AND_POSTURE.md)
- [研究与绘图流程](knowledge/DESIGN_WORKFLOW.md)
- 物种：[西方仓鸮](knowledge/species/01-tyto-alba.md)、[雪鸮](knowledge/species/02-bubo-scandiacus.md)、[雕鸮](knowledge/species/03-bubo-bubo.md)
- [概念图版本与状态](design/README.md)
- [项目状态与待办](STATUS.md)
- [更新记录](CHANGELOG.md)

## 开发现状

prototype/index.html 是此前的小猫WebGL养成原型，用户不满意其美术，保存仅用于保留交互和存档实现。尚未做成猫头鹰3D模型；角色概念图不能代替可旋转模型。原型可直接用静态服务器打开，浏览器需支持WebGL。

当前线上原型：https://mochi-pet-yiting.abloom-pin-2487.chatgpt.site

该原型原由Sites管理；本仓库是本次提交时的代码快照，不会自动与Sites双向同步。后续变更需要明确提交与部署流程。

## 维护约定

每次新物种或修订，更新相关物种档案、概念图版本、manifest、STATUS和CHANGELOG，一次提交后回读验证，报告真实SHA。以后以分专题档案为准，总纲用于导航和历史快照。
