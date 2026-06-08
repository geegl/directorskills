E0608 05:23:19.474455 3657594 ev_epoll1_linux.cc:191] OrphanHandle: epoll_ctl failed: Bad file descriptor (9)
---
name: story-design-beat-sheet
description: |
  当用户需要从零构建故事结构、检查叙事是否完整、或诊断'故事写到一半不知道怎么继续'时调用。核心 trigger：用户提到'故事结构'、'节拍表'、'三幕结构'、'怎么写剧本'、'Beat Sheet'。不适用于：已有成熟结构只需微调细节，或用户讨论的是非叙事类内容。
source_book: 《救猫咪》Blake Snyder
source_chapter: 第6章 Structure
tags: [screenwriting, story-structure, beat-sheet, blake-snyder]
related_skills:
  - composes-with: story-design-genres — 类型决定BS2的具体节拍内容和时长分配
  - composes-with: story-design-midpoint — 中点是节拍表的核心转折，决定后半段走向
  - composes-with: story-design-five-step-finale — 终幕五步是节拍表高潮段的详细展开
---

## R — 原文 (Reading)

> 把一个新想法分解成布莱克·斯奈德节拍表的 15 个节拍，再在周末白板会议上把这 15 个节拍展开成一般故事中 40 个关键场景。在课堂上，我们总会找到那个"试金石场景"——它代表了整个故事的核心。

> — Blake Snyder, Save the Cat! Strikes Back

## I — 方法论骨架 (Interpretation)

BS2（Blake Snyder Beat Sheet）是一个15节拍的故事骨架工具，将任何故事分解为从'开场画面'到'终场画面'的15个结构节点。它的核心思想是：故事不是靠抽象的'三幕结构'搭建的，而是靠15个具体的功能性节拍来驱动。

每个节拍有明确的叙事功能：Opening Image 建立基调，Theme Stated 埋下主题，Set-Up 介绍世界，Catalyst 打破平衡，Debate 制造犹豫，Break into Two 进入新世界，B Story 讨论主题，Fun and Games 展示承诺，Midpoint 假胜利/假失败，Bad Guys Close In 压缩空间，All Is Lost 跌入谷底，Dark Night of the Soul 内心挣扎，Break into Three 找到出路，Finale 五步终局，Final Image 展示变化。

独特价值：这个系统比'三幕结构'具体15倍。每个节拍都是可操作的——你可以直接问自己'我的Midpoint是什么？'而不是模糊地问'第二幕怎么写'。

---

## A1 — 书中的应用 (Past Application)

### 案例 1
- **问题**: 如何在商业故事中应用此方法论
- **方法论的使用**: 《夺宝奇兵1》精准击中BS2的每一个节拍。开场 Indiana Jones 是不信仰黑魔法的科学家（Opening Image），他明确说'I don't believe in black magic'（Theme Stated），发现约柜下落同时发现 Karen Allen 还活着是经典 Midpoint 假胜利（'Sex at 60!'），最终他独自见证约柜的神圣力量，完成了从不信仰到信仰的弧线（Final Image）。
- **结论**: 节拍表不是公式——它是诊断工具。当故事卡住时，回到节拍表检查哪个节拍缺失或无力
- **结果**: 故事获得了清晰的结构和情感弧线

### 案例 2: 《蜘蛛侠：平行宇宙》的BS2分析
- **问题**: 如何用BS2框架分析一部非线性叙事的动画电影
- **方法论的使用**: Miles Morales 的故事精准击中BS2：Opening Image 是他对着镜子自拍不自信（基调），Catalyst 是被蜘蛛咬（打破平衡），Midpoint 是他以为能用 Uncle Aaron 的方式解决问题（假胜利——'I got this'），但紧接着 Aaron 死亡（假胜利被打碎），All Is Lost 是他把自己关在房间里拒绝成为蜘蛛侠，Final Image 是他从高楼跳下——自信地、主动地（与 Opening Image 的不自信形成完美对比）
- **结论**: BS2 适用于非线性叙事——节拍可以打乱顺序但功能不变
- **结果**: 故事在视觉创新的同时保持了经典的情感结构

---

## A2 — 触发场景 (Future Trigger) ★

### 用户会在什么情境下需要这个 skill?

1. 怎么构建故事结构
2. 故事写到一半不知道怎么继续
3. Beat Sheet怎么用

### 语言信号 (用户的话里出现这些就应激活)

- "故事结构"
- "节拍表"
- "三幕结构"
- "怎么写剧本"
- "Beat Sheet"
- "15个节拍"

### 与相邻 skill 的区分

- 与 `story-design-beat-sheet` 的区别: beat-sheet 是整体15节拍框架，本 skill 聚焦特定方法论
- 与 `story-design-genres` 的区别: genres 决定'是什么类型'，本 skill 决定'怎么操作'

---

## E — 可执行步骤 (Execution)

当 skill 被激活后, agent 应按以下步骤执行:

1. **确定 Opening Image 和 Final Image**
   - 完成标准: 两者必须是对比——主角的起点和终点状态要形成鲜明反差。完成标准：能用一句话说清'开场时主角是__，终场时变成了__'

2. **填入15个节拍**
   - 完成标准: 按顺序逐个填入：Theme Stated（第5-10分钟埋下主题），Catalyst（打破平衡的外部事件），Midpoint（假胜利或假失败），All Is Lost（跌入谷底）。完成标准：每个节拍都有具体的场景描述
   - 判停条件: 若核心条件不满足，则回到步骤1重新评估

3. **检查 Act 1 和 Act 3 的对称性**
   - 完成标准: Catalyst-Debate-Break into Two 的结构与 All Is Lost-Dark Night-Break into Three 完全对称——后者是前者的放大版，stakes 更高

---

## B — 边界 (Boundary) ★

### 不要在以下情况使用此 skill

- 不要在已有成熟结构只需微调时使用——BS2 是从零构建的工具
- 不要把 BS2 当成检查清单机械填写——每个节拍必须有机服务于整体故事

### 作者在书中警告的失败模式

- Fun and Games 缺乏'fun'导致故事沉闷——Evan Almighty 的 premise 本身不够有趣
- No Double Mumbo Jumbo 违反——Spider-Man 3 用了四重魔法（Quadruple Mumbo Jumbo），故事失控

### 作者的盲点

作者假设所有故事都遵循15节拍结构，但某些非线性叙事（如《记忆碎片》）或散文式叙事可能不适用。此外，BS2 偏好莱坞商业片，艺术电影可能需要更灵活的框架。
