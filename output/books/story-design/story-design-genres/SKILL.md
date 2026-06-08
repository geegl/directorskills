---
name: story-design-genres
description: |
  当用户需要确定自己的故事属于什么类型、检查类型片必有元素、或诊断'故事类型不清晰'时调用。核心 trigger：用户提到'这是什么类型的故事'、'恐怖片怎么写'、'爱情片套路'、'故事类型'。不适用于：用户已在分析具体场景结构（用 beat-sheet）。
source_book: 《救猫咪》Blake Snyder
source_chapter: 第4章 Genres
tags: [screenwriting, story-structure, beat-sheet, blake-snyder]
related_skills:
  - composes-with: story-design-beat-sheet — 类型决定节拍表的具体内容和节奏
  - composes-with: story-design-theme-b-story — 类型惯例为B Story提供框架
  - depends-on: story-design-logline — logline帮助验证概念是否符合类型期待
---

## R — 原文 (Reading)

> 就像节拍表和它那些好用的"把手"（比如"游戏时间"和"跌入谷底"），这 10 种类型让我们可以按类型来引用故事。当你说"哦，这基本上是金色旅程加一点伙伴爱"，我就完全明白你的意思了。

> — Blake Snyder, Save the Cat! Strikes Back

## I — 方法论骨架 (Interpretation)

Blake Snyder 将所有故事分为10种原始冲突类型，每种类型有其必有的核心元素。这不是传统的'恐怖/喜剧/剧情'分类，而是基于'主角面对什么类型的冲突'来分类。

10种类型：Monster in the House（怪物+封闭空间+角色的过错），Golden Fleece（公路旅行+团队+沿途变化），Out of the Bottle（魔法/愿望+教训），Dude with a Problem（普通人+极端困境），Rites of Passage（人生转折+痛苦），Buddy Love（不完整的人+另一半），Whydunit（侦探+黑暗秘密），Fool Triumphant（被低估的人+体制），Institutionalized（个人vs群体），Superhero（非凡能力+巨大责任）。

独特价值：类型决定了观众的预期——每种类型都有其'必有元素'，缺失任何一个都会让观众感到不对劲。

---

## A1 — 书中的应用 (Past Application)

### 案例 1
- **问题**: 如何在商业故事中应用此方法论
- **方法论的使用**: 《Michael Clayton》让华纳兄弟的市场部困惑不已——它是喜剧？惊悚片？精神戏剧？但Blake Snyder一眼看出它是'Institutionalized'类型：关于'群体'的故事，核心问题是'谁更疯狂——他们还是我？'George Clooney 面对的是一个腐败的法律机构，他必须决定是融入还是反抗。
- **结论**: 类型不是标签——它是合同。观众选择看超级英雄电影时，你必须交付该类型的必有元素，否则就是违约
- **结果**: 故事获得了清晰的结构和情感弧线

### 案例 2: 《异形》的Monster in the House分析
- **问题**: 如何用STC!类型法分析经典科幻恐怖片
- **方法论的使用**: 《异形》是完美的'Monster in the House'类型：怪物（异形）+封闭空间（太空船）+角色的过错（公司故意带回异形、船员违反隔离协议）。Blake Snyder指出，缺失'角色的过错'会让恐怖片变成单纯的猎杀——《异形》之所以经典，正是因为'错在人类自己'这个元素
- **结论**: 类型分析能揭示故事为何有效——不是因为怪物可怕，而是因为人类犯了错
- **结果**: 类型框架帮助理解了'必有元素'如何共同创造观众体验

---

## A2 — 触发场景 (Future Trigger) ★

### 用户会在什么情境下需要这个 skill?

1. 这是什么类型的故事
2. 恐怖片怎么写
3. 爱情片套路

### 语言信号 (用户的话里出现这些就应激活)

- "故事类型"
- "属于什么类型"
- "类型片"
- "套路"
- "必有元素"

### 与相邻 skill 的区分

- 与 `story-design-beat-sheet` 的区别: beat-sheet 是整体15节拍框架，本 skill 聚焦特定方法论
- 与 `story-design-genres` 的区别: genres 决定'是什么类型'，本 skill 决定'怎么操作'

---

## E — 可执行步骤 (Execution)

当 skill 被激活后, agent 应按以下步骤执行:

1. **识别核心冲突**
   - 完成标准: 问自己：主角面对的是什么？怪物？旅程？魔法？普通人面对极端困境？确定原始冲突类型

2. **检查该类型的必有元素**
   - 完成标准: 每种类型都有3-4个必有元素。如 Monster in the House 必须有：怪物+封闭空间+角色的过错。缺失任何一个都会让故事失败
   - 判停条件: 若核心条件不满足，则回到步骤1重新评估

3. **在必有元素内创新**
   - 完成标准: 类型模板是骨架，创新是在必有元素内的新鲜 twist，而非抛弃必有元素

---

## B — 边界 (Boundary) ★

### 不要在以下情况使用此 skill

- 不要用传统类型标签（恐怖/喜剧）——STC!类型基于原始冲突，更精确
- 不要在类型确定前就开始写——类型决定了所有后续决策

### 作者在书中警告的失败模式

- Quadruple Mumbo Jumbo——Spider-Man 3 用了四重魔法，违反了 Out of the Bottle 的'一种魔法'规则
- Empowerment vs Comeuppance 混淆——Evan Almighty 是 comeuppance tale 而非 empowerment tale，不够'fun'

### 作者的盲点

作者的10种类型基于好莱坞商业片分析，可能不完全适用于非西方叙事传统或实验性作品。此外，某些跨类型故事（如 Buddy Love + Dude with a Problem）的分类可能模糊。
