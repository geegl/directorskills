# 新 Session 启动 Prompt

把以下内容完整复制粘贴到新 session：

---

读取当前目录下的 CLAUDE.md 了解项目全貌。

我需要你继续蒸馏导演书籍。当前进度：《电影导演大师课》已完成（15 个 skill），还剩 6 本待蒸馏。

**你的任务：**
1. 读取 CLAUDE.md 了解 book2skill 方法论、文件结构、上下文管理规则
2. 按照 CLAUDE.md 中的蒸馏顺序，从镜头域开始蒸馏（shot-design → master-shots-v1/v2/v3），然后视觉域（color-grading + scene-transitions）
3. 每本书严格按 book2skill 6 阶段执行（阶段 0-4）
4. 蒸馏完所有书后，做跨书 Zettelkasten 链接，生成总 INDEX.md
5. 最后用 darwin-skill 做质量优化

**关键文件：**
- 项目上下文: `CLAUDE.md`
- 完整计划: `.claude/plans/book2skill-deep-thunder.md`
- book2skill 方法论: `~/.claude/skills/book2skill/`
- darwin-skill: `~/.hermes/skills/darwin-skill/`

**上下文管理：**
- 一次蒸馏一本，sub-agent 做重活，主 session 只编排
- Haiku 读取/提取，Opus 写 skill
- 结果全部写入文件，不积累在上下文里
