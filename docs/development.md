# DirectorSkills 开发文档

> 内部开发流程记录。对外部用户请参考 [README.md](../README.md)。

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

## 注意事项

- **PDF 和 OCR 全文不入仓库**（DMCA 合规），仅保留结构化 skills
- `full_text.md` 文件在本地生成但不提交到 git
- PDF 源文件存储在本地 `pdfs/` 目录（已加入 .gitignore）

---

## Submodules

| 路径 | 用途 | 仓库 |
|------|------|------|
| `.claude/skills/book2skill` | book2skill 蒸馏技能 | kangarooking/cangjie-skill |
| `.hermes/skills/darwin-skill` | Darwin 质量进化技能 | geegl/darwin-skill |
