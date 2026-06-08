# DirectorSkills

> 10 本影视制作全流程书籍 → 97 个可执行 AI skills

把经典电影教材的核心方法论蒸馏成结构化、可被 AI agent 直接调用的 skills。覆盖从剧本到成片的完整制作链路。

## 覆盖范围

| # | 类别 | 书名 | Skills |
|---|------|------|--------|
| 1 | 剧本结构 | 《救猫咪》Save the Cat! | 8 |
| 2 | 导演思维 | 《电影导演大师课》On Film-making | 15 |
| 3 | 镜头技巧 | 《大师镜头》Vol.1-3 | 26 |
| 4 | 分镜设计 | 《电影镜头设计》Shot by Shot | 8 |
| 5 | 灯光摄影 | 《电影摄影：理论与实践》 | 7 |
| 6 | 色彩调色 | 《调色师手册》第2版 | 11 |
| 7 | 场景转场 | 《大师场景》Between the Scenes | 9 |
| 8 | 声音设计 | 《声音设计》Sound Design | 13 |

**总计 97 个 skills，Darwin 质量审计平均分 8.9/10**

## Skill 结构

每个 skill 遵循 RIA-TV++ 六段格式：

```
R — Reading        原文引用（≤150 字）
I — Interpretation 用自己的话重写核心洞察
A1 — Immediate     立即可执行的步骤
A2 — Adaptive      适应不同场景的应用方式
E — Execution      体验锚点 + 判停标准
B — Boundary       检查点 + 失败模式 + 盲点
```

## 蒸馏方法

采用 book2skill 6 阶段流水线：

1. **Stage 0** — Adler 整书理解
2. **Stage 1** — 5 个 agent 并行提取候选 skills
3. **Stage 1.5** — 三重验证筛选（跨域佐证 / 预测力 / 独特性）
4. **Stage 2** — RIA-TV++ 格式构造 SKILL.md
5. **Stage 3** — Zettelkasten 链接索引
6. **Stage 4** — 压力测试

蒸馏完成后通过 Darwin Skill 做质量进化优化，确保每个 skill 达到生产标准。

## 目录结构

```
output/books/<slug>/
├── BOOK_OVERVIEW.md       # 阶段 0：全书概览
├── INDEX.md               # 阶段 3：skill 索引
├── verified.md            # 阶段 1.5：通过验证的候选
├── candidates/            # 阶段 1：提取结果
├── rejected/              # 阶段 1.5：淘汰的候选
└── <skill-slug>/
    ├── SKILL.md           # 核心：结构化 skill
    └── test_prompts.json  # 阶段 4：测试用例
```

## 使用方式

Skills 可直接导入 AI agent 系统作为知识库，也可作为 prompt engineering 的参考模板。每个 SKILL.md 是自包含的，可单独使用。

## 版权说明

本仓库仅包含蒸馏后的结构化 skills 和方法论文档，不包含任何原始书籍内容（PDF、OCR 全文等）。
