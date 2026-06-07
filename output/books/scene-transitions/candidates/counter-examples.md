# Counter-Example Candidates — 大师场景

```yaml
- id: ce01
  title: 末节场景（无戏剧性结尾的过渡）
  type: counter-example
  source_chapter: 术语表
  source_quote: |
    末节场景（Caboose Scene）：不具任何戏剧性结尾的过渡场景，像火车末节车厢一样被拖着走。
  failure_mode: |
    场景没有明确的戏剧功能，只是被前一个场景"拖着走"。
    观众感到无聊但说不出为什么，因为场景本身缺乏目的。
  mechanism: |
    创作者认为"需要一个过渡"而添加了没有叙事目的的场景。
    缺乏场景转换四功能诊断，导致场景变成空洞的填充物。
  warning_signs:
    - 场景结束后观众无法说出其功能
    - 场景中没有情感、情节或节奏的变化
    - 场景可以被删除而不影响叙事
  bound_to:
    - "场景转换四功能诊断法"
    - "一旦目的完成就放手"
  tags: [counter-example, caboose-scene, purposeless, filler]

- id: ce02
  title: 重复使用同一技巧导致收益递减
  type: counter-example
  source_chapter: 第 4 章
  source_quote: |
    收益递减法则：重复使用同一技巧效果递减。
  failure_mode: |
    同一种场景转换手法反复使用，效果逐渐减弱直至失效。
    观众产生审美疲劳，原本有力的技巧变得可预测和无聊。
  mechanism: |
    大脑的适应机制：重复刺激导致神经反应减弱。
    观众会预测接下来的转换方式，失去惊喜感。
  warning_signs:
    - 同类转换手法出现第三次以上
    - 观众不再对转换产生情感反应
    - 转换变得"自动化"而非"有意图"
  bound_to:
    - "收益递减法则"
    - "场景DNA（长度×张力×情绪）"
  tags: [counter-example, diminishing-returns, repetition, fatigue]

- id: ce03
  title: 无目的地展示旅程
  type: counter-example
  source_chapter: 第 4 章
  source_quote: |
    只有在可以表现人物情感或能强调情节中的某些事物时，才表现人物的旅程。
  failure_mode: |
    无目的地展示主人公从A点到B点的移动过程。
    旅程本身没有情感内容或情节推动，变成纯粹的地理信息。
  mechanism: |
    创作者误认为"展示旅程=增加真实感"，
    但没有意识到旅程必须服务于情感或情节目的。
  warning_signs:
    - 旅程段落中没有情感变化
    - 旅程可以被一句话带过而不损失任何信息
    - 观众在旅程段落中开始走神
  bound_to:
    - "场景转换第二法则"
    - "投入公式"
  tags: [counter-example, aimless-journey, transport, purposeless]

- id: ce04
  title: 低潮时透露情节信息
  type: counter-example
  source_chapter: 第 5 章
  source_quote: |
    低潮时首先要做的：不再透露情节，不给观众重要信息。
  failure_mode: |
    在情感低潮（景物、舒缓段落）中继续释放新的情节信息。
    观众无法同时消化情感和处理新信息，导致混乱。
  mechanism: |
    低潮的功能是让观众消化已有信息，认知负荷已经达到。
    新信息的涌入会打破低潮的舒缓效果，同时新信息也得不到充分处理。
  warning_signs:
    - 低潮段落中有对话传递新信息
    - 景物镜头中出现新的叙事元素
    - 观众在"舒缓"段落中感到紧张
  bound_to:
    - "低潮时不再透露情节"
    - "景物的双重功能"
  tags: [counter-example, low-point-plot, cognitive-overload, rhythm]

- id: ce05
  title: 天气配合情绪的陈词滥调
  type: counter-example
  source_chapter: 第 5 章
  source_quote: |
    希区柯克打破类型片陈词滥调：在晴空万里平原上制造悬疑（《西北偏北》）。
  failure_mode: |
    机械地让天气配合人物情绪：悲伤下雨、开心天晴。
    这种做法让场景转换变得可预测且缺乏张力。
  mechanism: |
    观众已经学会了"天气=情绪"的对应关系，
    机械配合会强化这种预期而非打破它。
    对比（晴天+悲伤）反而能产生更强的戏剧效果。
  warning_signs:
    - 天气变化与情绪变化完全同步
    - 没有任何"意外"的天气-情绪组合
    - 观众能预测下一个场景的天气
  bound_to:
    - "天气不必配合情绪"
    - "二元对立场景并置工具"
  tags: [counter-example, weather-cliche, predictability, contrast]

- id: ce06
  title: 音乐的机械式使用
  type: counter-example
  source_chapter: 第 6 章
  source_quote: |
    音乐的机械式使用：作为润滑剂掩盖剪辑痕迹。
  failure_mode: |
    将音乐仅仅当作掩盖剪辑瑕疵的"润滑剂"，
    而非场景转换的有机组成部分。
    音乐变成了填充物而非表达工具。
  mechanism: |
    创作者用音乐填满所有场景转换的空白，
    导致音乐失去其情感标记功能。
    当音乐无处不在时，它就等于不存在。
  warning_signs:
    - 所有场景转换都有背景音乐
    - 音乐选择是"安全"的而非"有意图"的
    - 去掉音乐后场景转换完全没有情感变化
  bound_to:
    - "静默是深思熟虑的选择"
    - "转化策略四象限"
  tags: [counter-example, mechanical-music, filler, lubricant]

- id: ce07
  title: 抓住已完成目的的场景不放
  type: counter-example
  source_chapter: 第 4 章
  source_quote: |
    "一旦场景完成目的，再抓住这个场景不放就是犯罪。"——罗杰·克里腾登
  failure_mode: |
    场景已经完成了其叙事功能，但创作者因为"舍不得"而继续延展。
    结果是拖沓的节奏和观众的不耐烦。
  mechanism: |
    创作者对场景有情感依附，或者误认为"更多=更好"。
    没有意识到场景的力量恰恰在于适时结束。
  warning_signs:
    - 场景最后30秒没有新的情感或情节内容
    - 剪辑师觉得"可以在这里结束"但被否决
    - 观众在场景结束前已经开始期待下一个场景
  bound_to:
    - "一旦目的完成就放手"
    - "场景转换力度决策框架"
  tags: [counter-example, overstay, scene-length, pacing]

- id: ce08
  title: 电影"公式化"倾向的风险
  type: counter-example
  source_chapter: 批判（BOOK_OVERVIEW）
  source_quote: |
    投入公式（投入=情节张力+情绪化）和沉思公式过度简化了观众的情感反应。
  failure_mode: |
    机械地套用投入公式和沉思公式，认为"选对类型就能做好转换"。
    忽略了场景转换的"魔法"很大程度上来自直觉和经验。
  mechanism: |
    公式给出了两个变量的线性组合，但情感反应是非线性的、有交互效应的。
    最好的场景转换往往打破了所有"规则"——
    库布里克的"不展示时间流逝"之所以伟大，正因为它违反了所有预期。
  warning_signs:
    - 所有场景转换都按公式设计
    - 没有尝试"违规"的转换
    - 转换变得可预测
  bound_to:
    - "投入公式"
    - "沉思公式"
    - "从本能到技艺"
  tags: [counter-example, formulaic, over-simplification, rigidity]

- id: ce09
  title: 忽视配角旅程的展示时机
  type: counter-example
  source_chapter: 第 4 章
  source_quote: |
    除非要强调配角涉入，否则不展示配角旅程。
  failure_mode: |
    无差别地展示所有角色的移动过程，包括配角。
    稀释了主人公的情感焦点，分散观众注意力。
  mechanism: |
    创作者认为"展示所有人的行动=更真实"，
    但没有意识到场景转换的情感焦点应该集中在关键人物身上。
    配角的旅程通常应该被省略，只在需要强调时才展示。
  warning_signs:
    - 配角的移动过程占据了过多屏幕时间
    - 观众对配角旅程没有情感反应
    - 主人公的情感焦点被稀释
  bound_to:
    - "配角旅程的省略原则"
    - "场景转换第二法则"
  tags: [counter-example, supporting-cast-overuse, focus-dilution]

- id: ce10
  title: 场景数量过多导致转换失控
  type: counter-example
  source_chapter: 第 1 章
  source_quote: |
    场景数量：剧情电影的场景数量平均在40到200个之间。段落数量平均在10到30个之间。
  failure_mode: |
    场景数量过多，导致无法为每个转换投入足够的设计精力。
    大量场景转换变成硬切，整体节奏变得单调。
  mechanism: |
    创作者误认为"更多场景=更丰富"，
    但没有意识到场景数量与可经营的转换数量成反比。
    场景越多，每个转换可分配的注意力就越少。
  warning_signs:
    - 场景数量超过200个
    - 大部分转换都是无设计的硬切
    - 观众感到"跳跃"而非"流动"
  bound_to:
    - "剧情电影的场景数量参考"
    - "场景转换力度决策框架"
  tags: [counter-example, scene-proliferation, resource-scarcity, planning]
```
