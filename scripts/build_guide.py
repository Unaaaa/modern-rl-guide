"""Build the reading index and collected guide from the chapter Markdown files."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PARTS = {
    1: '第一篇：强化学习的核心原理',
    5: '第二篇：大模型强化学习与现代算法',
    10: '第三篇：Agent 强化学习',
    14: '第四篇：多智能体强化学习',
    19: '第五篇：扩展能力与约束',
    22: '第六篇：训练、评估与工程落地',
    26: '第七篇：贯通案例与研究路线',
    29: '第八篇：银行为什么做、如何做强化学习',
}
CHAPTERS = sorted((ROOT / 'docs').glob('[0-9][0-9]-*.md'))
APPENDICES = sorted((ROOT / 'appendices').glob('*.md'))
NAV_MARKER = '\n<!-- navigation -->'


def content(path):
    return path.read_text().split(NAV_MARKER)[0].rstrip()


def title(path):
    return content(path).splitlines()[0].removeprefix('# ')


def relative(path):
    return path.relative_to(ROOT).as_posix()


anchors = {p.resolve(): ('introduction' if p.name.startswith('00-') else 'chapter-' + p.name[:2])
           for p in CHAPTERS}
anchors.update({p.resolve(): 'appendix-' + p.name[0] for p in APPENDICES})


def collected(path, heading_shift):
    text = content(path)
    def link(match):
        label, target = match.groups()
        if '://' in target or target.startswith('#'):
            return match[0]
        filename, _, fragment = target.partition('#')
        destination = (path.parent / filename).resolve()
        anchor = anchors.get(destination)
        if anchor:
            return f'[{label}](#{anchor})'
        return f'[{label}]({relative(destination)})'
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, text)
    lines = []
    fenced = False
    for line in text.splitlines():
        if line.startswith('```'):
            fenced = not fenced
        if not fenced and re.match(r'^#{1,6} ', line):
            line = '#' * heading_shift + line
        lines.append(line)
    return '\n'.join(lines)


# Chapter files are the editable source. Navigation is regenerated from file order.
for i, path in enumerate(CHAPTERS):
    links = ['[目录](../README.md)']
    if i:
        links.append(f'[上一章：{title(CHAPTERS[i-1])}]({CHAPTERS[i-1].name})')
    if i + 1 < len(CHAPTERS):
        links.append(f'[下一章：{title(CHAPTERS[i+1])}]({CHAPTERS[i+1].name})')
    path.write_text(content(path) + NAV_MARKER + '\n\n---\n\n' + ' · '.join(links) + '\n')
for i, path in enumerate(APPENDICES):
    links = ['[目录](../README.md)']
    if i:
        links.append(f'[上一附录]({APPENDICES[i-1].name})')
    if i + 1 < len(APPENDICES):
        links.append(f'[下一附录]({APPENDICES[i+1].name})')
    path.write_text(content(path) + NAV_MARKER + '\n\n---\n\n' + ' · '.join(links) + '\n')

readme = '''# 现代强化学习指南

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

每章从具体情境进入，先讲机制，再配必要公式、短例子和对照表。章末留一道“想一想”，可以先作答，再展开参考思路。PPO 裁剪、GRPO 组内优势、团队信用分配等关键机制，都有可逐步理解的例子；论文与官方资料链接放在相应内容旁边，方便继续深入。

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

'''
for p in CHAPTERS:
    n = int(p.name[:2])
    if n == 0:
        continue
    if n in PARTS:
        readme += '\n### ' + PARTS[n] + '\n\n'
    readme += f'- [{title(p)}]({relative(p)})\n'
readme += '\n## 附录\n\n'
for p in APPENDICES:
    readme += f'- [{title(p)}]({relative(p)})\n'
readme += '\n</details>\n'
(ROOT / 'README.md').write_text(readme)

book = '''# 现代强化学习指南

> 从核心原理到大模型与多智能体实践  
> 更新日期：2026-11-17  
> 面向具备机器学习基础的开发者、研究人员与技术负责人。

[分章目录与阅读路线](README.md)。全书共8篇31章与6类附录，章末配有思考题及参考思路。文中实验为设计方案，教学数值不代表训练结果。
'''
for p in CHAPTERS:
    n = int(p.name[:2])
    if n in PARTS:
        book += '\n## ' + PARTS[n] + '\n'
    book += f'\n<a id="{anchors[p.resolve()]}"></a>\n\n'
    book += collected(p, 1 if n == 0 else 2) + '\n'
for p in APPENDICES:
    book += f'\n<a id="{anchors[p.resolve()]}"></a>\n\n' + collected(p, 1) + '\n'
(ROOT / 'GUIDE.md').write_text(book)
print(f'Built {len(CHAPTERS)-1} chapters, introduction, {len(APPENDICES)} appendices, index and collected guide.')
