# DirectorSkills — 导演书籍蒸馏项目

> 用 book2skill 把 7 本导演/电影制作书籍蒸馏成可执行 skills，再用 darwin-skill 做质量优化。

---

## 项目结构

```
DirectorSkills/
├── CLAUDE.md                          # 本文件（项目上下文）
├── .claude/plans/book2skill-deep-thunder.md  # 完整蒸馏计划
├── output/books/                      # 蒸馏产出
│   ├── directing-masterclass/         # ✅ 已完成
│   ├── shot-design/                   # ⏳ 待开始
│   ├── master-shots-v1/               # ⏳ 待开始
│   ├── master-shots-v2/               # ⏳ 待开始
│   ├── master-shots-v3/               # ⏳ 待开始
│   ├── color-grading/                 # ⏳ 待开始
│   └── scene-transitions/             # ⏳ 待开始
└── *.pdf                              # 源书 PDF（存于 Google Drive，见下方链接）
```

---

## 7 本书清单与分组

### 主题域分组
- **镜头域** (Shot): 4 本，共享镜头语言，skill 间有交叉
- **导演域** (Directing): 1 本，基础方法论总纲
- **视觉域** (Visual): 2 本，后期/视觉叙事

| # | slug | 书名 | 作者 | 主题 | 状态 | PDF 链接 |
|---|------|------|------|------|------|----------|
| 1 | `directing-masterclass` | 电影导演大师课 | Alexander Mackendrick | 导演方法论 | ✅ 完成 | [下载](https://drive.google.com/file/d/1IKPyDhJwXAA5_I8eFTjJvZP5Et4GVoWi/view?usp=drive_link) |
| 2 | `shot-design` | 从构思到银幕电影镜头设计 | Steven Katz | 镜头设计 | ⏳ 待蒸馏 | [下载](https://drive.google.com/file/d/1AGX52El5v_5nbaAQ2ZuwWqTW9d_u9HZj/view?usp=drive_link) |
| 3 | `master-shots-v1` | 大师镜头 | Sean Tian | 镜头技法 | ⏳ 待蒸馏 | [下载](https://drive.google.com/file/d/1B4rrvbxpvDiAn_eJ2uOtj4NZz-LD04vf/view?usp=drive_link) |
| 4 | `master-shots-v2` | 大师镜头·第2卷 | Christopher Kenworthy | 对话镜头 | ⏳ 待蒸馏 | [下载](https://drive.google.com/file/d/1A10sOYuPl78A7GaLVxYSUIvwh33MdHOB/view?usp=drive_link) |
| 5 | `master-shots-v3` | 大师镜头·第3卷 | Christopher Kenworthy | 镜头调度 | ⏳ 待蒸馏 | [下载](https://drive.google.com/file/d/1zGhQcHEVICXMaJJfNtysrVsTP3DXvxJ7/view?usp=drive_link) |
| 6 | `color-grading` | 调色师手册·第2版 | Alexis Van Hurkman | 调色技法 | ⏳ 待蒸馏 | [下载](https://drive.google.com/file/d/1BKYNgVFVc-JYQc3Vm4lD4u0I847JyWAK/view?usp=drive_link) |
| 7 | `scene-transitions` | 大师场景：顶级场景转换术 | Jeffrey Michael Bays | 场景转换 | ⏳ 待蒸馏 | [下载](https://drive.google.com/file/d/1FtIPf8T_AuY6VJsXSU1lOgS3Oa7-34sM/view?usp=drive_link) |

### 蒸馏顺序
```
批次 1: 导演域 (directing-masterclass) ✅
批次 2: 镜头域 (shot-design → v1 → v2 → v3) ⏳
批次 3: 视觉域 (color-grading + scene-transitions) ⏳
```

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

### 三重验证标准（阶段 1.5）
- **V1 跨域**: 书中至少 2 个独立段落有佐证？
- **V2 预测力**: 能推导出书里没明说的新问题的答案？
- **V3 独特性**: 不是任何聪明人都会说的常识？
- 通过率预期：30-50%（V3 是最大淘汰关）

### SKILL.md 六段结构
```
R — Reading (原文引用 ≤150 字)
I — Interpretation (用自己的话重写)
A1 — Past Application (书中案例)
A2 — Future Trigger ★ (触发场景 + 语言信号)
E — Execution (1-2-3 可执行步骤)
B — Boundary ★ (边界 + 反例 + 作者盲点)
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

## 已完成工作

### directing-masterclass (15 个 skills)

| ID | slug | 标题 |
|----|------|------|
| f01 | directing-story-framework | "很久很久以前"故事构建框架 |
| f02 | directing-activity-vs-action | 活动vs动作区分判断 |
| f03 | directing-idea-generation | 获得创意的四步法 |
| f04 | directing-dramatic-irony | 戏剧反讽操控法 |
| f05 | directing-invisible-witness | 隐身见证人视点操控 |
| f07 | directing-tension-formula | 期待与不确定的张力公式 |
| f14 | directing-contrast-emphasis | 通过对比强调（排版师思维） |
| f18 | directing-odets-rewrite | 编剧修改的奥德兹法则 |
| f19 | directing-protagonist-endangered | 主角濒危判断法 |
| f22 | directing-reaction-over-action | 反应重于动作的剪辑原则 |
| f29 | directing-scene-necessity | 场景必要性检验法 |
| p06 | directing-credible-impossible | 可信的不可能优于不可信的可能 |
| p15 | directing-coincidence-trouble | 巧合制造麻烦而非解决困难 |
| p21 | directing-end-before-begin | 想好结尾再写开头 |
| g18 | directing-ambiguity-diagnosis | 模棱两可的精确区分 |

---

## 关键文件引用

### book2skill 方法论
- 主流程: `~/.claude/skills/book2skill/SKILL.md`
- 阶段 0: `~/.claude/skills/book2skill/methodology/01-stage0-adler.md`
- 阶段 1: `~/.claude/skills/book2skill/methodology/02-stage1-parallel-extract.md`
- 阶段 1.5: `~/.claude/skills/book2skill/methodology/03-stage1.5-triple-verify.md`
- 阶段 2: `~/.claude/skills/book2skill/methodology/04-stage2-ria-plus.md`
- 阶段 3: `~/.claude/skills/book2skill/methodology/05-stage3-zettelkasten.md`
- 阶段 4: `~/.claude/skills/book2skill/methodology/06-stage4-pressure-test.md`
- 模板: `~/.claude/skills/book2skill/templates/`
- 提取器: `~/.claude/skills/book2skill/extractors/`

### darwin-skill 优化
- 主流程: `~/.hermes/skills/darwin-skill/SKILL.md`
- 成果卡片: `~/.hermes/skills/darwin-skill/templates/result-card.html`

---

## 上下文管理规则

1. **一次蒸馏一本** — 不要贪多，一本做完再开下一本
2. **sub-agent 做重活** — 每个阶段用独立 agent，结果写入文件
3. **主 session 只做编排** — 不直接读 PDF 大文件
4. **自适应模型** — Haiku 做批量读取/提取，Sonnet 编排，Opus 写 skill

---

## 云端 Agent 启动指南

### 初始化
```bash
git clone --recursive https://github.com/geegl/directorskills.git
cd directorskills
# 如果 clone 时没带 --recursive：
git submodule update --init --recursive
```

### PDF 获取
源书 PDF 存放于 Google Drive（见上方表格的 PDF 链接列），需要下载到本地供蒸馏流程读取。

### 建议的工作流（仅供参考，可自行优化）

> ⚠️ 以下是原作者的建议方案，非硬性要求。执行 Agent 可根据自身环境和偏好选择更优方案。

**建议流程：**
1. 从 Google Drive 下载 PDF 到本地（可用 `gdown`、`wget` 或浏览器手动下载）
2. 按 book2skill 的 6 阶段流水线逐本蒸馏（参见 `CLAUDE.md` 中的 `RIA-TV++ 方法论`）
3. 蒸馏完成后用 darwin-skill 做质量优化

**关于 OCR 的建议：**
- Claude 原生支持读取 PDF（包括扫描版图片 PDF），大多数情况下可直接处理，无需额外 OCR
- 如果遇到图片质量差、识别率低的情况，可考虑以下 fallback：
  - Apify Actor: [`cspnair/pdf-ocr-api`](https://apify.com/cspnair/pdf-ocr-api)（$0.01/PDF，支持多种 OCR 引擎）
  - Python 库: `pytesseract` + `pdf2image`（本地部署，免费）
  - Google Cloud Vision API（高精度，按量计费）

**关于并行策略的建议：**
- 镜头域 4 本书（shot-design、master-shots-v1/v2/v3）有交叉内容，建议串行蒸馏以便跨书链接
- 导演域和视觉域可并行处理

---

## darwin-skill 优化阶段（全部蒸馏完后）

按 darwin-skill Phase 0-3 执行：
1. Phase 0: 扫描所有 SKILL.md，git 分支
2. Phase 0.5: 验证/补充 test-prompts
3. Phase 1: 9 维度基线评估，生成评分卡
4. Phase 2: 按分数从低到高优化，每 skill 最多 3 轮
5. Phase 3: 汇总报告 + 成果卡片
