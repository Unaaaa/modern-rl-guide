# 现代强化学习指南

从核心原理到大模型与多智能体实践。面向具备机器学习基础、希望系统学习强化学习的读者。

**[从导读开始](docs/00-introduction.md)** · [合订版](GUIDE.md)

更新日期：2026-11-17。

从一个查询报错、小迷宫或协作任务出发，逐步理解背后的决策与学习机制。31章各自独立，前4章建立基础，随后进入大模型、Agent、多智能体及工程与银行实践；必要公式配合例子解释。

通用实验与银行案例目前为设计方案；文中教学数值与待运行结果均已注明。

## 如何学习

第一次阅读可以按章推进：先跟随情境和例子，再看概念怎样解释这些现象。到章末停下来想一想，尝试回答问题后，再展开参考思路。遇到术语查附录A，公式查附录B；前沿论文可在理解机制后选读。

各章提供“读前回顾”与前后导航，支持顺读或按专题选读。

## 按目标阅读

| 目标 | 阅读顺序 |
| --- | --- |
| 从零建立体系 | 导读 → 01—04 → 05—09 → 其他篇 |
| 大模型后训练 | 01—09 → 22—24 → 26 |
| Agent研发 | 01—07 → 10—13 → 21—25 |
| 多智能体学习 | 01—04 → 14—18 → 22—25 → 27 |
| 银行项目判断 | 导读 → 01—02 → 29—31 |
| 银行算法实施 | 01—04 → 14—18 → 21—25 → 29—31；语言策略另补05—13 |

## 章节目录

### 第一篇：强化学习的核心原理

- [第01章 强化学习解决什么问题](docs/01-why-rl.md)
- [第02章 一张图理解强化学习的基本体系](docs/02-rl-foundations.md)
- [第03章 经典算法的统一地图](docs/03-algorithm-map.md)
- [第04章 理解现代算法的桥梁：策略梯度、Actor–Critic 与 PPO](docs/04-policy-gradient-ppo.md)

### 第二篇：大模型强化学习与现代算法

- [第05章 大模型后训练的统一视角](docs/05-llm-post-training.md)
- [第06章 奖励与验证：训练信号从哪里来](docs/06-rewards-and-verifiers.md)
- [第07章 从 PPO 到 GRPO：大模型策略优化主线](docs/07-ppo-to-grpo.md)
- [第08章 GRPO 之后：现代策略优化改进](docs/08-modern-policy-optimization.md)
- [第09章 偏好直接优化、RLVR 与训练路径选择](docs/09-training-paths.md)

### 第三篇：Agent 强化学习

- [第10章 将工具调用与工作流建模为决策任务](docs/10-agent-task-modeling.md)
- [第11章 长任务中的奖励、探索与信用分配](docs/11-long-horizon-credit.md)
- [第12章 训练环境、轨迹与可复现交互](docs/12-agent-environments.md)
- [第13章 Agent 的学习闭环与持续改进](docs/13-agent-learning-loop.md)

### 第四篇：多智能体强化学习

- [第14章 多智能体问题建模与协作机制](docs/14-multi-agent-modeling.md)
- [第15章 多智能体训练架构与代表算法](docs/15-marl-algorithms.md)
- [第16章 团队奖励、个体贡献与信用分配](docs/16-team-credit-assignment.md)
- [第17章 通信、分工与 LLM 多角色联合训练](docs/17-llm-multi-agent-training.md)
- [第18章 自博弈、红蓝对抗与多主体评估](docs/18-self-play-evaluation.md)

### 第五篇：扩展能力与约束

- [第19章 离线强化学习与从示范中学习](docs/19-offline-rl.md)
- [第20章 世界模型、规划与层次化学习](docs/20-world-models.md)
- [第21章 安全、约束、多目标与鲁棒学习](docs/21-safe-and-robust-rl.md)

### 第六篇：训练、评估与工程落地

- [第22章 从任务需求到实验方案](docs/22-experiment-design.md)
- [第23章 训练系统、并行采样与框架选型](docs/23-training-systems.md)
- [第24章 评估、可观测性与训练排障](docs/24-evaluation-and-debugging.md)
- [第25章 部署与持续迭代](docs/25-deployment.md)

### 第七篇：贯通案例与研究路线

- [第26章 从小实验到现代算法对比](docs/26-algorithm-comparison-case.md)
- [第27章 实战：规划—执行—检查的多智能体协作](docs/27-collaboration-case.md)
- [第28章 方法选型、研究地图与学习路线](docs/28-research-roadmap.md)

### 第八篇：银行为什么做、如何做强化学习

- [第29章 银行为什么要做强化学习](docs/29-why-bank-rl.md)
- [第30章 银行如何开展强化学习：从试点到能力建设](docs/30-bank-implementation.md)
- [第31章 案例：反洗钱调查策略与红蓝对抗](docs/31-bank-aml-case.md)

## 附录

- [附录A：术语与最小符号表](appendices/a-glossary.md)
- [附录B：经典算法与核心公式速查](appendices/b-formulas.md)
- [附录C：现代优化与多主体训练伪代码](appendices/c-pseudocode.md)
- [附录D：环境与轨迹记录示例](appendices/d-trajectory-schema.md)
- [附录E：项目与实验报告模板](appendices/e-project-template.md)
- [附录F：原始资料与前沿阅读](appendices/f-references.md)
