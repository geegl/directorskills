# DirectorSkills

> 10 本影视制作全流程书籍 + 1 个跨书参考库 → 98 个可执行 AI skills

---

## 为什么做这个项目

AI 正在重塑影视制作流程——从剧本生成到镜头设计、从调色到声音，每个环节都可以被 AI agent 辅助甚至独立完成。但目前的 AI 影视工具缺乏**结构化的专业知识库**：它们能执行指令，却不懂"为什么这样拍更好"、"什么情况下不该用这个技巧"。

DirectorSkills 把经典电影教材的核心方法论蒸馏成**结构化、可被 AI agent 直接调用**的 skills。每个 skill 包含：

- **原文引用** — 来自权威教材的具体引文，可溯源
- **方法论解读** — 从"知道"到"会用"的关键转化
- **实战案例** — 真实电影场景中的应用
- **触发条件** — 什么时候该用，什么时候不该用
- **可执行步骤** — agent 拿到就能执行的 1-2-3 步
- **失败模式** — 常见错误和作者盲点，避免踩坑

**目标用户**：影视 AI agent 开发者、prompt 工程师、影视教育工作者。

---

## 为什么选这 10 本书

选书标准：**每一本都是该领域公认的方法论标杆**，而非泛泛的入门读物。10 本书覆盖从剧本到成片的完整制作链路，每本书对应 AI 影视生成工作流的一个关键环节。

| 环节 | 为什么需要 | 选的书 | 为什么选这本 |
|------|-----------|--------|------------|
| **剧本结构** | AI 生成的故事需要结构骨架 | 《救猫咪》Blake Snyder | 好莱坞最广泛使用的 15 节拍模板，可操作性最强 |
| **导演思维** | AI 需要理解"为什么这样调度" | 《电影导演大师课》Alexander Mackendrick | 苏格兰动画之父的 USC 讲义，从故事到画面的完整方法论 |
| **镜头技巧** | AI 需要具体的镜头语言库 | 《大师镜头》Vol.1-3 Christopher Kenworthy | 100+ 个具体镜头技法，每个配真实电影案例 |
| **分镜设计** | AI 需要把文字转化为视觉 | 《电影镜头设计》Steven D. Katz | 分镜行业的"圣经"，从轴线到景别的完整系统 |
| **灯光摄影** | AI 生成的画面需要光影逻辑 | 《电影摄影》Blain Brown | 覆盖 Zone System 到三点布光的完整摄影理论 |
| **色彩调色** | AI 调色需要专业判断依据 | 《调色师手册》第 2 版 Alexis Van Hurkman | DaVinci Resolve 官方教材，从技术校正到创意风格 |
| **场景转场** | AI 需要场景间的叙事连接 | 《大师场景》Jeffrey Michael Bays | 唯一专注场景转换的专著，9 种转场技法 |
| **声音设计** | AI 需要声音叙事能力 | 《声音设计》David Sonnenschein | 声音设计领域的理论框架，从感知心理到实际操作 |

---

## 为什么用这些 skills

### vs 直接问 ChatGPT

| 维度 | 直接问 LLM | 用 DirectorSkills |
|------|-----------|-------------------|
| 知识来源 | 混合网络文章、可能过时 | 指定权威教材，可溯源到章节 |
| 结构 | 自由发挥，每次不同 | RIA-TV++ 六段结构，一致可预期 |
| 边界 | 不知道什么时候不该用 | B 段包含失败模式和作者盲点 |
| 可测试 | 无法验证 | 每个 skill 配套 test-prompts |

### vs 手动 prompt engineering

- **98 个 skill 覆盖全链路**，不需要为每个场景重新写 prompt
- **related_skills 交叉引用**，agent 可以自动发现关联方法论
- **已通过 Darwin 质量审计**（平均 8.9/10），经过结构化验证

---

## Quick Start

```bash
git clone https://github.com/geegl/directorskills.git
cd directorskills
```

核心内容在 `output/books/` 下。每个 skill 是一个自包含的 `SKILL.md` 文件，可单独使用。

### 使用方式

1. 浏览 `output/books/` 找到你需要的领域（如 `color-grading/`）
2. 进入具体 skill 目录（如 `color-grading-contrast-before-color/`）
3. 读取 `SKILL.md` — 这就是完整的、可被 agent 调用的 skill

---

## 覆盖范围

| # | 类别 | 书名 | 作者 | Skills |
|---|------|------|------|--------|
| 1 | 剧本结构 | 《救猫咪》Save the Cat! | Blake Snyder | 8 |
| 2 | 导演思维 | 《电影导演大师课》On Film-making | Alexander Mackendrick | 15 |
| 3 | 镜头技巧 | 《大师镜头》Vol.1-3 | Christopher Kenworthy | 26 |
| 4 | 分镜设计 | 《电影镜头设计》Shot by Shot | Steven D. Katz | 8 |
| 5 | 灯光摄影 | 《电影摄影：理论与实践》 | Blain Brown | 7 |
| 6 | 色彩调色 | 《调色师手册》第 2 版 | Alexis Van Hurkman | 11 |
| 7 | 场景转场 | 《大师场景》Between the Scenes | Jeffrey Michael Bays | 9 |
| 8 | 声音设计 | 《声音设计》Sound Design | David Sonnenschein | 13 |

> **附录：** [camera-lens-anchoring](output/books/camera-reference/camera-lens-anchoring/SKILL.md) — 专业影视摄影机镜头锚定库（跨书综合 + 行业实践，1 skill）

**总计 98 个 skills（97 书蒸馏 + 1 跨书参考）**

---

## Skill 格式参考

每个 skill 遵循 **RIA-TV++** 六段格式，存储在 `SKILL.md` 中。

### YAML Frontmatter

```yaml
---
name: scene-transition-binary-opposition
description: |
  当用户需要通过场景对比制造戏剧张力时调用。核心 trigger：场景对比、二元对立。
source_book: 《大师场景：顶级场景转换术》 Jeffrey Michael Bays
source_chapter: 第2章, 第5章
tags: [场景转换, 二元对立, 场所选择, 对比, 叙事]
related_skills:
  - composes-with: scene-transition-four-function-diagnosis — 四功能诊断确定转换目的
  - contrasts-with: scene-transition-weather-contrast — 二元对立是通用工具
---
```

| 字段 | 说明 |
|------|------|
| `name` | 唯一标识符，格式 `{book-slug}-{technique-slug}` |
| `description` | 触发条件和适用场景，供 agent 判断是否激活 |
| `source_book` | 原书信息 |
| `source_chapter` | 对应章节 |
| `tags` | 分类标签 |
| `related_skills` | 与其他 skill 的关系（composes-with / depends-on / contrasts-with） |

### 六段结构

| 段 | 名称 | 内容 |
|----|------|------|
| **R** | Reading | 原文引用（≤150 字），带来源标注 |
| **I** | Interpretation | 用自己的话重写核心方法论 |
| **A1** | Immediate Action | 书中的具体应用案例（≥2 个） |
| **A2** | Adaptive Application | 触发场景、语言信号、与相邻 skill 的区分 |
| **E** | Execution | 可执行步骤 + 判停条件 |
| **B** | Boundary | 边界条件 + 失败模式 + 作者盲点 |

### test-prompts.json

每个 skill 配套一个 `test-prompts.json`，包含 should-trigger 和 should-not-trigger 测试用例：

```json
[
  {
    "id": "should-trigger-01",
    "type": "should_trigger",
    "prompt": "两个场景怎么对比才有张力？",
    "expected_behavior": "激活，解释二元对立方法"
  },
  {
    "id": "should-not-trigger-01",
    "type": "should_not_trigger",
    "prompt": "场景内部的灯光怎么布置？",
    "expected_behavior": "不激活，这是灯光问题"
  }
]
```

---

## 集成示例

### 导入 AI Agent 系统

每个 `SKILL.md` 是自包含的，可以直接作为 agent 的知识库使用：

```python
import yaml
from pathlib import Path

def load_skills(books_dir="output/books"):
    skills = {}
    for skill_file in Path(books_dir).rglob("SKILL.md"):
        content = skill_file.read_text()
        parts = content.split("---", 2)
        if len(parts) >= 3:
            meta = yaml.safe_load(parts[1])
            skills[meta["name"]] = {
                "metadata": meta,
                "content": content,
                "path": str(skill_file),
            }
    return skills

# 使用
skills = load_skills()
# 根据用户输入匹配 skill
user_input = "怎么用灯光营造神秘感？"
for name, skill in skills.items():
    desc = skill["metadata"].get("description", "")
    tags = skill["metadata"].get("tags", [])
    if any(t in user_input for t in tags):
        print(f"匹配: {name}")
        print(skill["content"])
        break
```

### 作为 Prompt 模板

直接将 SKILL.md 的内容注入 agent 的 system prompt，或在用户请求时动态加载对应 skill 的 R/I/A1/A2/E/B 各段。

---

## 目录结构

```
output/books/<slug>/
├── BOOK_OVERVIEW.md       # 全书概览
├── INDEX.md               # skill 间链接索引
├── verified.md            # 通过验证的候选列表
├── candidates/            # 提取的候选 skills
├── rejected/              # 淘汰的候选（含淘汰理由）
└── <skill-slug>/
    ├── SKILL.md           # 核心：结构化 skill
    └── test-prompts.json  # 测试用例
```

---

## 质量保证

所有 skills 经过 Darwin Skill 质量进化优化，采用 10 维评分体系（每维 1.0 分，总分 10.0）：

| 维度 | 检测内容 |
|------|----------|
| D1 前置信息 | frontmatter + name + tags |
| D2 章节完整 | R/I/A1/A2/E/B 六段齐全 |
| D3 失败模式 | 反模式/盲点/错误关键词 |
| D4 检查点 | 判停/验收标准 |
| D5 可执行性 | A1/A2 有编号步骤 |
| D6 原文质量 | R 段长度 + 引用标记 |
| D7 直觉迁移 | I 段深度 |
| D8 体验锚点 | E 段长度 + 案例引用 |
| D9 B段深度 | 失败模式关键词密度 |
| D10 内容量 | 总长度 ≥ 2000 字符 |

**审计结果：98/98 skills 全部通过，路由测试 659/659 (100%)。**

---

## 开发工具

蒸馏过程使用了两个开源 skill 作为工具：

| 工具 | 用途 | 仓库 |
|------|------|------|
| book2skill | 书籍 → skills 的 6 阶段蒸馏方法论 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) |
| Darwin Skill | 质量进化优化，9 维度评估 + 自动修复 | [alchaincyf/darwin-skill](https://github.com/alchaincyf/darwin-skill) |

这些是开发过程中的工具，不包含在本仓库中。

---

## 许可证

[MIT License](LICENSE)

---

## 版权说明

本仓库仅包含蒸馏后的结构化 skills 和方法论文档，不包含任何原始书籍内容（PDF、OCR 全文等）。所有 skills 的 `source_book` 字段标注了原书信息，尊重原作者版权。
