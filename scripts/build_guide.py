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
