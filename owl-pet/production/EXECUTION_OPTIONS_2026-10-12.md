# 生产执行方案探索 · 2026-10-12

## 已核验的问题
最近两个批次各完成1/6，运行记录自报执行预算不足；未取得平台强制超时遥测。已建立BATCH_STATE.json，六轮按持久批次接续。当前账本尚未推进到2/6，不能声称修复已通过生产验收。

## 首选：分阶段持久化，沿用现有工具
每个子轮保存阶段：RESEARCH_READY -> IMAGE_GENERATED -> REVIEWED -> ARCHIVED -> VERIFIED。
保存物种、来源ID、实际读取摘要、设计边界、完整生成提示、图片路径/远端blob、审查问题、修订历史。只有VERIFIED推进批次完成数。
中断后从最后已证实阶段继续；研究就绪不重新研究，已生成且文件可恢复不重复生成。scratch路径不视为持久保存；图片无法恢复则明确记录，不声称可以直接续用。
研究准备队列最多预备2个资料明确物种，优先完成当前子轮；不得以预研代替完整生产。
每阶段记录开始/结束、工具等待、检索次数、生成/编辑次数、归档时间、实际错误。无平台超时事件不得把主动退出写成平台强制限制。
下一次生产验收：同一batch_id从1/6变为2/6；阶段记录与真实成果提交可回读。后续至少一次中断恢复验证；尚未执行这些测试。

## 提效实验
复用已核验资料索引和已确认风格，针对缺口增量检索；每种只更新必要物种档案、来源索引、图片清单和子轮记录，集中维护展示总览。
跟踪每个完成物种耗时、编辑次数、重复检索/重复生成、科学未解决项；以实际阶段日志比较，不降低研究/看图/复查质量。
更快文字模型不保证缩短图片生成等待；不据此直接换模型。

## 后备：GitHub Actions + 外部API执行器
官方支持Actions最短5分钟调度；外部程序可轮询Responses API background请求和使用web_search。调度程序仍需接入绘图、图像检查、持久队列、锁、重试与提交验证。
前提：用户授权API路径、有效API凭据、成本范围、单物种端到端验证。当前未接入、未部署、未证明可复现已确认图片风格。
现有ChatGPT内置imagegen不能仅靠Actions定时器从仓库调用；不得把增加cron说成完成迁移。
仅在当前阶段化方案测得吞吐不足后再评估迁移，保留现有生产。

## 官方资料
- https://learn.chatgpt.com/docs/automations （web任务不保留本地工作目录，需持久输入）
- https://developers.openai.com/api/docs/guides/background （异步请求与状态轮询，不是无限运行）
- https://developers.openai.com/api/docs/guides/tools-web-search （长研究background模式）
- https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax （schedule最短5分钟）
