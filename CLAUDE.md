# DirectorSkills — 导演书籍蒸馏项目

> 用 book2skill 把 10 本影视制作全流程书籍蒸馏成可执行 skills，再用 darwin-skill 做质量优化。
> **全部 10 本书已完成蒸馏，97 个 skills，Darwin 质量审计通过（平均 8.9/10）。**

---

## 项目结构

```
DirectorSkills/
├── CLAUDE.md                          # 本文件（项目上下文）
├── .gitignore                         # 版权内容排除规则
└── output/books/                      # 蒸馏产出（10 本书，97 个 skills）
    ├── story-design/                  # ✅ 8 skills  — 剧本结构（救猫咪）
    ├── directing-masterclass/         # ✅ 15 skills — 导演思维
    ├── master-shots-v1/               # ✅ 6 skills  — 镜头技巧 Vol.1
    ├── master-shots-v2/               # ✅ 14 skills — 镜头技巧 Vol.2（对话戏）
    ├── master-shots-v3/               # ✅ 6 skills  — 镜头技巧 Vol.3（突破性场面）
    ├── shot-design/                   # ✅ 8 skills  — 分镜设计
    ├── cinematography-brown/          # ✅ 7 skills  — 灯光摄影
    ├── color-grading/                 # ✅ 11 skills — 色彩调色
    ├── scene-transitions/             # ✅ 9 skills  — 场景转场
    └── sound-design/                  # ✅ 13 skills — 声音设计
```

---

## 10 本书清单

覆盖从剧本到最终输出的完整影视制作链，每本书对应 AI 影视生成工作流的一个关键环节。

| # | 类别 | slug | 书名 | 作者 | Skills | Darwin 均分 |
|---|------|------|------|------|--------|------------|
| 1 | 剧本结构 | `story-design` | 《救猫咪》Save the Cat! | Blake Snyder | 8 | 9.2 |
| 2 | 导演思维 | `directing-masterclass` | 《电影导演大师课》On Film-making | Alexander Mackendrick | 15 | 9.2 |
| 3 | 镜头技巧 | `master-shots-v1` | 《大师镜头》第1卷 | Christopher Kenworthy | 6 | 9.2 |
| 4 | 镜头技巧 | `master-shots-v2` | 《大师镜头》第2卷 | Christopher Kenworthy | 14 | 8.9 |
| 5 | 镜头技巧 | `master-shots-v3` | 《大师镜头》第3卷 | Christopher Kenworthy | 6 | 8.7 |
| 6 | 分镜设计 | `shot-design` | 《电影镜头设计：从构思到银幕》Shot by Shot | Steven D. Katz | 8 | 9.2 |
| 7 | 灯光摄影 | `cinematography-brown` | 《电影摄影：理论与实践》 | Blain Brown | 7 | 9.1 |
| 8 | 色彩调色 | `color-grading` | 《调色师手册》第2版 | Alexis Van Hurkman | 11 | 8.8 |
| 9 | 场景转场 | `scene-transitions` | 《大师场景》Between the Scenes | Jeffrey Michael Bays | 9 | 8.9 |
| 10 | 声音设计 | `sound-design` | 《声音设计》Sound Design | David Sonnenschein | 13 | 8.1 |

---

## Darwin 质量审计

### 评分维度（10 维，每维 1.0 分，总分 10.0）

| 维度 | 检测内容 |
|------|----------|
| D1 前置信息 | frontmatter + name + tags |
| D2 章节完整 | R/I/A1/A2/E/B 六段齐全 |
| D3 失败模式 | 反模式/盲点/错误关键词 |
| D4 检查点 | 判停/验收标准 |
| D5 可执行性 | A1/A2 有编号步骤 |
| D6 原文质量 | R 段长度 + 引用标记 |
| D7 直觉迁移 | I 段深度 |
| D8 体验锚点 | E 段长度 + 视频/案例引用 |
| D9 B段深度 | 失败模式关键词密度 |
| D10 内容量 | 总长度 ≥ 2000 字符 |

### 审计结果

- **总 skill 数**: 97
- **平均分**: 8.9/10
- **最低分**: 7.9 (sound-design-expectation)
- **最高分**: 9.5 (directing-end-before-begin, shot-design-storyboard-rapid, scene-transition-caboose-diagnosis)
- **低于 8.0**: 0 个

---

## book2skill RIA-TV++ 方法论

### 核心理念
把书的方法论拆解成**原子化、可被 agent 在真实场景下调用**的 skills。

### 6 阶段流水线
```
阶段 0: Adler 整书理解     → BOOK_OVERVIEW.md
阶段 1: 5 个 agent 并行提取 → candidates/ (5 个文件)
阶段 1.5: 三重验证筛选       → verified.md + rejected/
阶段 2: RIA++ 构造 skill     → 每个 skill 的 SKILL.md
阶段 3: Zettelkasten 链接    → INDEX.md
阶段 4: 压力测试             → test-prompts.json
```

### SKILL.md 六段结构（RIA-TV++）
```
R — Reading (原文引用 ≤150 字)
I — Interpretation (用自己的话重写)
A1 — Immediate Action (立即可执行步骤)
A2 — Adaptive Application (适应性应用场景)
E — Execution (体验锚点 + 判停标准)
B — Boundary (检查点 + 失败模式 + 盲点)
```

### 输出目录结构
```
output/books/<slug>/
├── BOOK_OVERVIEW.md           # 阶段 0
├── INDEX.md                   # 阶段 3
├── verified.md                # 阶段 1.5 通过的
├── candidates/                # 阶段 1 (5 个文件)
│   ├── frameworks.md
│   ├── principles.md
│   ├── cases.md
│   ├── counter-examples.md
│   └── glossary.md
├── rejected/                  # 阶段 1.5 淘汰的
├── <skill-slug-1>/
│   ├── SKILL.md
│   └── test-prompts.json
└── <skill-slug-2>/
    └── ...
```

---

## 注意事项

- **PDF 和 OCR 全文不入仓库**（DMCA 合规），仅保留结构化 skills
- `full_text.md` 文件在本地生成但不提交到 git
- PDF 源文件存储在本地 `pdfs/` 目录（已加入 .gitignore）
