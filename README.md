# DirectorSkills

> 10 本影视制作全流程书籍 → 97 个可执行 AI skills

把经典电影教材的核心方法论蒸馏成结构化、可被 AI agent 直接调用的 skills。覆盖从剧本到成片的完整制作链路。

---

## Quick Start

```bash
# Clone（含 submodules）
git clone --recurse-submodules https://github.com/geegl/directorskills.git
cd directorskills

# 如果已经 clone 但没有 submodules
git submodule update --init --recursive
```

仓库的核心内容在 `output/books/` 下。每个 skill 是一个自包含的 `SKILL.md` 文件，可单独使用。

### 快速使用

1. 浏览 `output/books/` 找到你需要的领域（如 `color-grading/`）
2. 进入具体 skill 目录（如 `color-grading-contrast-before-color/`）
3. 读取 `SKILL.md` — 这就是完整的、可被 agent 调用的 skill

---

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
        # 解析 YAML frontmatter
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
    # 简单匹配（生产环境建议用 embedding）
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
├── BOOK_OVERVIEW.md       # 全书概览（阶段 0 产出）
├── INDEX.md               # skill 间链接索引（阶段 3 产出）
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

**审计结果：97/97 skills 全部通过，平均 8.9/10，无低于 8.0 的 skill。**

---

## Submodules

本仓库包含两个 git submodule：

| 路径 | 用途 |
|------|------|
| `.claude/skills/book2skill` | book2skill — 书籍蒸馏为 skills 的方法论技能 |
| `.hermes/skills/darwin-skill` | Darwin Skill — 质量进化优化技能 |

这些是蒸馏过程中使用的工具技能，不是本仓库的核心产出。核心产出在 `output/books/` 下。

---

## 许可证

[MIT License](LICENSE)

---

## 版权说明

本仓库仅包含蒸馏后的结构化 skills 和方法论文档，不包含任何原始书籍内容（PDF、OCR 全文等）。所有 skills 的 `source_book` 字段标注了原书信息，尊重原作者版权。
