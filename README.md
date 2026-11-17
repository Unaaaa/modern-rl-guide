# 现代强化学习指南

> 从“会回答”走向“会决策”：理解模型如何从反馈中学习行动与协作。

模型能写出 SQL，却可能查错时间范围；Agent 能调用工具，却可能在报错后反复重试；多个智能体各有分工，却未必能一起把任务做好。

这些问题背后，都有一个共同的挑战：**面对不断变化的信息，下一步该做什么？**

强化学习研究如何利用行动的结果改进决策。这本中文指南从必要的基础出发，连接大模型后训练、工具型 Agent 与多智能体协作，再把方法放回实验、评估和具体业务中。希望帮你建立一套能读懂论文、分析系统、设计实验的知识体系。

**[开始阅读](docs/00-introduction.md)** · [从第01章学起](docs/01-why-rl.md) · [阅读合订版](GUIDE.md)

## 这本指南能帮你做什么

面对一个新任务，你需要判断：该改提示、补示范、优化流程，还是值得训练策略？面对一篇新论文，你需要看清：它到底改了什么，收益来自哪里，结论适用于哪些条件？

全书围绕这些实际判断展开：

| 你关心的问题 | 阅读后应能做到 | 从这里进入 |
| --- | --- | --- |
| RL 到底在学什么？ | 用观测、动作、奖励和策略描述任务，读懂价值与优势 | [核心原理](docs/01-why-rl.md) |
| PPO、GRPO、DPO 与 RLVR 是什么关系？ | 区分反馈与优化方法，追踪一次采样到参数更新 | [大模型后训练](docs/05-llm-post-training.md) |
| Agent 为什么总在长任务中失败？ | 分析工具选择、停止、求助，以及跨步骤的信用分配 | [Agent 任务建模](docs/10-agent-task-modeling.md) |
| 多个 Agent 怎样才算学会合作？ | 理解集中训练、团队奖励、通信与联合更新 | [多智能体学习](docs/14-multi-agent-modeling.md) |
| 奖励涨了，系统真的变好了吗？ | 设计基线、独立评估和消融，识别奖励捷径与过拟合 | [实验设计](docs/22-experiment-design.md) |
| 银行里有哪些值得尝试的场景？ | 从业务决策出发，形成有边界、可验证的试点方案 | [银行应用](docs/29-why-bank-rl.md) |

## 适合谁读

- **有机器学习基础，想系统学习 RL 的读者：** 从前4章建立共同语言，再进入现代方法。
- **正在做大模型或 Agent 的开发者：** 把奖励、轨迹、工具和训练串起来，找到系统值得改进的决策。
- **需要判断研究与项目价值的技术负责人：** 看清数据、环境、预算和证据要求，评估复杂训练是否值得投入。

默认你理解神经网络、损失函数和梯度下降。概率、价值和优化中的新概念会随例子解释。

## 跟着问题往前走

全书共 **8篇31章，另附6个附录**。从小迷宫中的一次移动，到语言模型的一条回答，再到多角色任务与合成调查案例，逐步扩展决策的复杂度。

每章从具体情境进入，逐步说明概念与机制，再用必要公式、完整算例和对照展开。章末留一道“想一想”，可以先作答，再展开参考思路。PPO 裁剪、GRPO 组内优势、团队信用分配等关键机制，都配有推理过程与适用条件；论文与官方资料链接放在相应内容旁边，方便继续深入。

想先感受内容，可以读三个片段：

- [一次偶然成功，应该让策略改变多少？](docs/04-policy-gradient-ppo.md)——用数字理解 PPO 裁剪。
- [同一道题答四次，怎样变成训练信号？](docs/07-ppo-to-grpo.md)——从相对奖励走到 GRPO 更新。
- [规划、执行、检查都参与了，奖励该给谁？](docs/16-team-credit-assignment.md)——理解团队信用分配。

## 选一条阅读路线

| 你的目标 | 建议路线 |
| --- | --- |
| 建立完整体系 | [导读](docs/00-introduction.md) → 01—04 → 05—09 → 其他各篇 |
| 学习大模型后训练 | 01—09 → 22—24 → 26 |
| 改进工具型 Agent | 01—07 → 10—13 → 21—25 |
| 研究多智能体协作 | 01—04 → 14—18 → 22—25 → 27 |
| 判断银行项目与试点 | [银行为什么做 RL](docs/29-why-bank-rl.md) → 30—31；按需回读基础与工程章节 |

各章均有“读前回顾”和前后导航。术语查[附录A](appendices/a-glossary.md)，公式查[附录B](appendices/b-formulas.md)，延伸阅读见[附录F](appendices/f-references.md)。

## 内容说明

当前提供正文、图表、思考题及实验设计。通用实验和银行案例尚不含训练代码与实测结果，示例数值用于教学。前沿方法的介绍保留任务条件与证据范围，便于读者判断如何使用。

更新日期：2026-11-17。

<details>
<summary>展开完整目录：8篇31章</summary>


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

</details>
