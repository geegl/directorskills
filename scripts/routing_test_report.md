# Skill Routing Test Report

Generated: 2026-06-08 19:11

## Overall Summary

| Metric | Value |
|--------|-------|
| Total prompts tested | 659 |
| should_trigger | 323 total, **106 passed** (33%) |
| should_not_trigger | 204 total, **194 passed** (95%) |
| edge_case (reviewed) | 90 |
| **Overall pass rate** | **56.9%** |

## Per-Book Breakdown

| Book | Skills | Prompts | ST Pass | SNT Pass | Overall |
|------|--------|---------|---------|----------|---------|
| cinematography-brown | 7 | 42 | 20/21 (95%) | 20/20 (100%) | 98% |
| color-grading | 10 | 88 | 22/44 (50%) | 31/33 (94%) | 69% |
| directing-masterclass | 15 | 150 | 12/75 (16%) | 43/45 (96%) | 46% |
| master-shots-v1 | 6 | 38 | 8/20 (40%) | 10/12 (83%) | 56% |
| master-shots-v2 | 13 | 62 | 1/11 (9%) | 5/5 (100%) | 38% |
| master-shots-v3 | 6 | 30 | 16/30 (53%) | - | 53% |
| scene-transitions | 9 | 49 | 9/22 (41%) | 14/18 (78%) | 57% |
| shot-design | 8 | 48 | 8/24 (33%) | 16/16 (100%) | 60% |
| sound-design | 12 | 104 | 1/52 (2%) | 39/39 (100%) | 44% |
| story-design | 7 | 48 | 9/24 (38%) | 16/16 (100%) | 62% |

## Failed Tests Detail

### should_trigger failures (target skill NOT in top-5)

**[cinematography-brown/cinematography-master-scene] prompt #should-trigger-02**
> 对话场景怎么拍才能在剪辑时有足够素材

- Expected: `cinematography-master-scene` should be in top-5
- Got top-3: `scene-transition-caboose-diagnosis` (score=0.28), `dialogue-busy-hands-no-eye-contact` (score=0.27), `color-grading-shot-matching` (score=0.23)

**[color-grading/color-grading-color-temperature] prompt #should-trigger-01**
> 画面整体偏蓝偏冷，怎么用色温调整让它变暖？

- Expected: `color-grading-color-temperature` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[color-grading/color-grading-color-temperature] prompt #should-trigger-03**
> 日落效果怎么通过色温调出来但不过度？

- Expected: `color-grading-color-temperature` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[color-grading/color-grading-color-temperature] prompt #should-trigger-04**
> 色温和白平衡的关系是什么？校色时先调哪个？

- Expected: `color-grading-color-temperature` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[color-grading/color-grading-contrast-before-color] prompt #should-trigger-02**
> 调色应该先调什么再调什么？正确的顺序是什么？

- Expected: `color-grading-contrast-before-color` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[color-grading/color-grading-filter-nonlinear] prompt #should-trigger-01**
> 怎么在数字调色中模拟Pro-Mist柔光滤镜的效果？

- Expected: `color-grading-filter-nonlinear` should be in top-5
- Got top-3: `cinematography-hard-soft-light` (score=0.28), `sound-design-less-is-more` (score=0.19), `cinematography-180-degree-rule` (score=0.00)

**[color-grading/color-grading-filter-nonlinear] prompt #should-trigger-02**
> 光学滤镜的非线性特征和数字处理有什么区别？

- Expected: `color-grading-filter-nonlinear` should be in top-5
- Got top-3: `color-grading-contrast-saturation` (score=0.29), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[color-grading/color-grading-filter-nonlinear] prompt #should-trigger-03**
> 模拟电影胶片的halation（光晕）效果怎么做？

- Expected: `color-grading-filter-nonlinear` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[color-grading/color-grading-look-development] prompt #should-trigger-01**
> 导演想要一个像《银翼杀手2049》那样的调色风格，怎么建立？

- Expected: `color-grading-look-development` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[color-grading/color-grading-look-development] prompt #should-trigger-02**
> 同一部片子不同场景需要不同的情绪色调，但又要整体统一，怎么做？

- Expected: `color-grading-look-development` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[color-grading/color-grading-memory-colors] prompt #should-trigger-01**
> 肤色看起来不对偏黄了，怎么用记忆色彩校正？

- Expected: `color-grading-memory-colors` should be in top-5
- Got top-3: `color-grading-skin-tone-vectorscope` (score=0.25), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[color-grading/color-grading-memory-colors] prompt #should-trigger-02**
> 天空颜色太假了，怎么调回人脑认知中的'正确'蓝色？

- Expected: `color-grading-memory-colors` should be in top-5
- Got top-3: `directing-credible-impossible` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[color-grading/color-grading-memory-colors] prompt #should-trigger-03**
> 植物的绿色太荧光了，怎么让它看起来自然？

- Expected: `color-grading-memory-colors` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[color-grading/color-grading-memory-colors] prompt #should-trigger-04**
> 记忆色彩（memory colors）在调色中的参考价值是什么？

- Expected: `color-grading-memory-colors` should be in top-5
- Got top-3: `color-grading-overexposure-recovery` (score=0.32), `color-grading-color-temperature` (score=0.30), `color-grading-filter-nonlinear` (score=0.30)

**[color-grading/color-grading-overexposure-recovery] prompt #should-trigger-01**
> 高光区域过曝太严重了，传统调色拉不回来，还有什么办法？

- Expected: `color-grading-overexposure-recovery` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[color-grading/color-grading-overexposure-recovery] prompt #should-trigger-02**
> 红色通道被完全裁切了，能不能从绿色通道借数据恢复？

- Expected: `color-grading-overexposure-recovery` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[color-grading/color-grading-overexposure-recovery] prompt #should-trigger-03**
> 天空过曝成纯白了，怎么用其他通道的信息来恢复？

- Expected: `color-grading-overexposure-recovery` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[color-grading/color-grading-overexposure-recovery] prompt #should-trigger-04**
> 过曝的肤色怎么修复？单色过曝和全通道过曝处理方式一样吗？

- Expected: `color-grading-overexposure-recovery` should be in top-5
- Got top-3: `color-grading-contrast-saturation` (score=0.29), `color-grading-skin-tone-vectorscope` (score=0.25), `cinematography-180-degree-rule` (score=0.00)

**[color-grading/color-grading-primary-workflow] prompt #should-trigger-03**
> 调色的第一步应该是设定黑位和白位还是先校白平衡？

- Expected: `color-grading-primary-workflow` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[color-grading/color-grading-primary-workflow] prompt #should-trigger-04**
> 一级调色和二级调色的分工是什么？

- Expected: `color-grading-primary-workflow` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[color-grading/color-grading-shot-matching] prompt #should-trigger-01**
> 同一场景不同镜头色彩跳动严重，怎么匹配？

- Expected: `color-grading-shot-matching` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[color-grading/color-grading-shot-matching] prompt #should-trigger-02**
> 正反打镜头的天空颜色差很多，怎么让它们看起来一致？

- Expected: `color-grading-shot-matching` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[color-grading/color-grading-shot-matching] prompt #should-trigger-03**
> 多机位拍摄的素材颜色不统一，匹配的优先级是什么？

- Expected: `color-grading-shot-matching` should be in top-5
- Got top-3: `directing-reaction-over-action` (score=0.27), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[directing-masterclass/directing-activity-vs-action] prompt #1**
> 我写了一场主角回忆童年的闪回，但总觉得放进去之后节奏就慢了，这段闪回要不要删？

- Expected: `directing-activity-vs-action` should be in top-5
- Got top-3: `scene-transition-caboose-diagnosis` (score=0.28), `scene-transition-seamless-pause` (score=0.28), `scene-transition-low-point-no-plot` (score=0.26)

**[directing-masterclass/directing-activity-vs-action] prompt #2**
> 我有一个场景写完之后觉得特别无聊，但说不上来哪里有问题，能帮我诊断一下吗？

- Expected: `directing-activity-vs-action` should be in top-5
- Got top-3: `scene-transition-caboose-diagnosis` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[directing-masterclass/directing-activity-vs-action] prompt #3**
> 这段内容里角色一直在聊天和散步，看起来没什么事发生，观众会不会在这里走神？

- Expected: `directing-activity-vs-action` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[directing-masterclass/directing-activity-vs-action] prompt #4**
> 怎么让日常场景也有戏剧性？比如两个人吃饭聊天这种戏。

- Expected: `directing-activity-vs-action` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-activity-vs-action] prompt #5**
> 我剪辑的时候发现中间一大段过渡戏不知道该不该保留，看起来啥也没发生。

- Expected: `directing-activity-vs-action` should be in top-5
- Got top-3: `scene-transition-caboose-diagnosis` (score=0.28), `color-grading-shot-matching` (score=0.23), `cinematography-180-degree-rule` (score=0.00)

**[directing-masterclass/directing-ambiguity-diagnosis] prompt #3**
> 导演说我的剧本主题不够清晰，但我想要那种观众可以自己解读的感觉，这矛盾吗？

- Expected: `directing-ambiguity-diagnosis` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-ambiguity-diagnosis] prompt #4**
> 我写了一段很深的场景，不确定读者能不能get到我想表达的东西，怎么评估？

- Expected: `directing-ambiguity-diagnosis` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-ambiguity-diagnosis] prompt #5**
> 我写的东西说不清主题是什么，有人说是后现代，有人说是含糊不清，我怎么判断？

- Expected: `directing-ambiguity-diagnosis` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-coincidence-trouble] prompt #1**
> 我剧本里主角逃亡时偶然遇到一个好心人帮他过了关，但有人说这个转折太假了，怎么办？

- Expected: `directing-coincidence-trouble` should be in top-5
- Got top-3: `directing-credible-impossible` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[directing-masterclass/directing-coincidence-trouble] prompt #3**
> 我想设计一个意外事件来推动剧情，怎么判断它应该带来麻烦还是解决问题？

- Expected: `directing-coincidence-trouble` should be in top-5
- Got top-3: `msv3-unexpected-reveal` (score=0.32), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[directing-masterclass/directing-coincidence-trouble] prompt #4**
> 我的故事结局太巧了，读者觉得不真实，但我不知道具体是哪个环节出了问题。

- Expected: `directing-coincidence-trouble` should be in top-5
- Got top-3: `directing-protagonist-endangered` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[directing-masterclass/directing-contrast-emphasis] prompt #1**
> 我的PPT上放满了信息，观众完全不知道该看哪里，怎么突出重点？

- Expected: `directing-contrast-emphasis` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-contrast-emphasis] prompt #2**
> 我剪辑了一场两个人对话的戏，但视觉上看起来两人权重差不多，怎么让观众更关注主角？

- Expected: `directing-contrast-emphasis` should be in top-5
- Got top-3: `scene-transition-caboose-diagnosis` (score=0.28), `dialogue-busy-hands-no-eye-contact` (score=0.27), `shot-design-dialogue-staging` (score=0.26)

**[directing-masterclass/directing-contrast-emphasis] prompt #3**
> 我总觉得重要元素不够醒目，第一反应是把它放大或加粗，但效果还是不好，怎么回事？

- Expected: `directing-contrast-emphasis` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-contrast-emphasis] prompt #4**
> 这个仪表盘界面上有二十多个指标，用户不知道该先看哪个，怎么设计视觉层次？

- Expected: `directing-contrast-emphasis` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-contrast-emphasis] prompt #5**
> 我想让这个镜头里的某个角色特别突出，但不知道除了给他特写还有什么办法。

- Expected: `directing-contrast-emphasis` should be in top-5
- Got top-3: `dialogue-closeup-timing` (score=0.30), `dialogue-telephoto-claustrophobia` (score=0.30), `msv3-body-performance` (score=0.30)

**[directing-masterclass/directing-credible-impossible] prompt #2**
> 我的角色前半段是一个胆小的人，突然在高潮时变得无比勇敢，读者说太突兀了，怎么改？

- Expected: `directing-credible-impossible` should be in top-5
- Got top-3: `story-design-five-step-finale` (score=0.29), `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00)

**[directing-masterclass/directing-credible-impossible] prompt #3**
> 我之前设定这个世界没有魔法，但剧情需要角色突然获得超能力，世界观崩了怎么办？

- Expected: `directing-credible-impossible` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[directing-masterclass/directing-credible-impossible] prompt #4**
> 一部奇幻电影里龙会喷火但其他时候像普通蜥蜴一样行动，这种设定能站住脚吗？

- Expected: `directing-credible-impossible` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-credible-impossible] prompt #5**
> 现实中不可能发生的情节，在故事里能不能让观众接受？什么条件下可以？

- Expected: `directing-credible-impossible` should be in top-5
- Got top-3: `directing-protagonist-endangered` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[directing-masterclass/directing-dramatic-irony] prompt #1**
> 这个对话场景太平淡了，两个角色只是在聊天，怎么让观众紧张起来？

- Expected: `directing-dramatic-irony` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `dialogue-busy-hands-no-eye-contact` (score=0.27), `cinematography-180-degree-rule` (score=0.00)

**[directing-masterclass/directing-dramatic-irony] prompt #2**
> 我想让观众一直想知道接下来会发生什么，怎么设计这种悬念？

- Expected: `directing-dramatic-irony` should be in top-5
- Got top-3: `dialogue-delayed-reveal` (score=0.32), `msv3-unexpected-reveal` (score=0.32), `cinematography-180-degree-rule` (score=0.00)

**[directing-masterclass/directing-dramatic-irony] prompt #3**
> 希区柯克那个炸弹比喻具体是怎么操作的？我想在我的故事里用类似的手法。

- Expected: `directing-dramatic-irony` should be in top-5
- Got top-3: `directing-protagonist-endangered` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[directing-masterclass/directing-dramatic-irony] prompt #5**
> 我的播客节目想在叙事中制造紧张感，但不是视觉媒介，有什么办法？

- Expected: `directing-dramatic-irony` should be in top-5
- Got top-3: `scene-transition-binary-opposition` (score=0.29), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[directing-masterclass/directing-end-before-begin] prompt #1**
> 我写了一个故事开头，但写到一半发现不知道怎么收尾，结构越来越散了。

- Expected: `directing-end-before-begin` should be in top-5
- Got top-3: `directing-protagonist-endangered` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[directing-masterclass/directing-end-before-begin] prompt #2**
> 我的剧本开头改了四五版都不满意，总觉得哪里不对，能帮我看看吗？

- Expected: `directing-end-before-begin` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-end-before-begin] prompt #3**
> 我要准备一个商业演示，内容很多但不知道先讲什么后讲什么，结构很散。

- Expected: `directing-end-before-begin` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-end-before-begin] prompt #5**
> 有人告诉我'如果不知道结局就别开始写'，这话是什么意思？真的有道理吗？

- Expected: `directing-end-before-begin` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-idea-generation] prompt #1**
> 我脑子一片空白，完全想不出好的故事创意，有什么办法能帮我想点子？

- Expected: `directing-idea-generation` should be in top-5
- Got top-3: `directing-protagonist-endangered` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[directing-masterclass/directing-idea-generation] prompt #2**
> 我有一个大概的方向想写关于职场的故事，但具体怎么都想不到好的切入点。

- Expected: `directing-idea-generation` should be in top-5
- Got top-3: `directing-protagonist-endangered` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[directing-masterclass/directing-idea-generation] prompt #3**
> 最近写什么都觉得差点什么，灵感好像枯竭了，怎么才能找回创意？

- Expected: `directing-idea-generation` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-idea-generation] prompt #4**
> 我需要为一个品牌想一个有创意的广告概念，但怎么想都是老套的。

- Expected: `directing-idea-generation` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-idea-generation] prompt #5**
> 怎么才能想出别人没想到的角度？我的创意总是很平庸。

- Expected: `directing-idea-generation` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-invisible-witness] prompt #1**
> 这场戏有两个角色对峙，摄影机应该放在哪里？该拍谁的特写？

- Expected: `directing-invisible-witness` should be in top-5
- Got top-3: `dialogue-closeup-timing` (score=0.30), `dialogue-telephoto-claustrophobia` (score=0.30), `msv3-body-performance` (score=0.30)

**[directing-masterclass/directing-invisible-witness] prompt #2**
> 我拍了一场审讯戏，素材都有了但不知道该怎么剪辑，该切到谁？

- Expected: `directing-invisible-witness` should be in top-5
- Got top-3: `scene-transition-caboose-diagnosis` (score=0.28), `color-grading-shot-matching` (score=0.23), `cinematography-180-degree-rule` (score=0.00)

**[directing-masterclass/directing-invisible-witness] prompt #3**
> 为什么有些电影总能让观众认同某个角色？导演是怎么操控这种认同的？

- Expected: `directing-invisible-witness` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.55), `shot-design-pov-spectrum` (score=0.28), `cinematography-180-degree-rule` (score=0.00)

**[directing-masterclass/directing-invisible-witness] prompt #4**
> 这场戏里主角和反派都很重要，怎么通过景别让观众更关注主角？

- Expected: `directing-invisible-witness` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-invisible-witness] prompt #5**
> 分析一下这个导演的镜头设计，为什么这个时刻用远景而不是特写？

- Expected: `directing-invisible-witness` should be in top-5
- Got top-3: `dialogue-closeup-timing` (score=0.30), `dialogue-telephoto-claustrophobia` (score=0.30), `msv3-body-performance` (score=0.30)

**[directing-masterclass/directing-odets-rewrite] prompt #1**
> 我写了一场两个人对话的戏，但读起来像在聊天，完全没有交锋的感觉，怎么改？

- Expected: `directing-odets-rewrite` should be in top-5
- Got top-3: `dialogue-busy-hands-no-eye-contact` (score=0.27), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[directing-masterclass/directing-odets-rewrite] prompt #2**
> 角色A把所有背景信息直接讲给角色B听，感觉像是在'交代'，怎么让信息传递更有张力？

- Expected: `directing-odets-rewrite` should be in top-5
- Got top-3: `dialogue-deep-staging` (score=0.29), `scene-transition-loyalty-transfer` (score=0.28), `shot-dual-camera-tension` (score=0.27)

**[directing-masterclass/directing-odets-rewrite] prompt #3**
> 这场戏只有两个角色在对话，密度不够，怎么让它更丰富？

- Expected: `directing-odets-rewrite` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `dialogue-busy-hands-no-eye-contact` (score=0.27), `cinematography-180-degree-rule` (score=0.00)

**[directing-masterclass/directing-odets-rewrite] prompt #4**
> 我准备一场投资路演，想预判投资人可能的质疑并设计应对策略，有办法吗？

- Expected: `directing-odets-rewrite` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-odets-rewrite] prompt #5**
> 这场戏里角色好像在'为说而说'，没有真正的对抗，怎么增强冲突？

- Expected: `directing-odets-rewrite` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[directing-masterclass/directing-protagonist-endangered] prompt #2**
> 主角出场很多但观众好像不关心他的命运，为什么？

- Expected: `directing-protagonist-endangered` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-protagonist-endangered] prompt #4**
> 我拍纪录片需要在几个真实人物中选一个作为叙事中心，怎么决定？

- Expected: `directing-protagonist-endangered` should be in top-5
- Got top-3: `scene-transition-binary-opposition` (score=0.29), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[directing-masterclass/directing-protagonist-endangered] prompt #5**
> 大家都说我的主角太被动了，但我已经给他安排了很多事件，问题出在哪？

- Expected: `directing-protagonist-endangered` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-reaction-over-action] prompt #1**
> 这场戏发生了一个重大事件但观众反应很平淡，怎么才能更有感染力？

- Expected: `directing-reaction-over-action` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-reaction-over-action] prompt #2**
> 体育直播的关键得分后，我应该重播进球画面还是切到教练的反应？

- Expected: `directing-reaction-over-action` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-reaction-over-action] prompt #3**
> 我在剪辑一场对话戏，不知道在谁说话时该切到谁，有原则吗？

- Expected: `directing-reaction-over-action` should be in top-5
- Got top-3: `scene-transition-caboose-diagnosis` (score=0.28), `dialogue-busy-hands-no-eye-contact` (score=0.27), `color-grading-shot-matching` (score=0.23)

**[directing-masterclass/directing-reaction-over-action] prompt #4**
> 这个瞬间为什么没有力量？明明发生了一个很震撼的事情。

- Expected: `directing-reaction-over-action` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-scene-necessity] prompt #1**
> 我的剧本初稿有120页，感觉有些段落和主线关系不大但又不敢删，怎么判断哪些该留？

- Expected: `directing-scene-necessity` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-scene-necessity] prompt #3**
> 我做了一个培训课程，内容很多但感觉有些模块看起来都需要但好像也可以不要。

- Expected: `directing-scene-necessity` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-scene-necessity] prompt #4**
> 这段视频剪辑到一半发现有些镜头拍得不错但好像删掉也没影响，留还是不留？

- Expected: `directing-scene-necessity` should be in top-5
- Got top-3: `scene-transition-caboose-diagnosis` (score=0.28), `color-grading-shot-matching` (score=0.23), `cinematography-180-degree-rule` (score=0.00)

**[directing-masterclass/directing-scene-necessity] prompt #5**
> 观众说我的故事结构很散，我在修改时怎么知道哪些场景该保留？

- Expected: `directing-scene-necessity` should be in top-5
- Got top-3: `directing-story-framework` (score=0.29), `directing-protagonist-endangered` (score=0.28), `cinematography-180-degree-rule` (score=0.00)

**[directing-masterclass/directing-story-framework] prompt #1**
> 我有个故事创意，一个退役拳击手回到家乡想开拳馆，但不知道怎么展开成一个完整的故事，能帮我搭建结构吗？

- Expected: `directing-story-framework` should be in top-5
- Got top-3: `directing-protagonist-endangered` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[directing-masterclass/directing-story-framework] prompt #2**
> 我的剧本写到第二幕就散了，感觉角色在原地打转，不知道怎么继续推进，有什么办法？

- Expected: `directing-story-framework` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[directing-masterclass/directing-story-framework] prompt #3**
> 我想写一个关于小镇女教师发现秘密的小说，但只有一个模糊的感觉，不知道怎么从一个想法变成完整的故事。

- Expected: `directing-story-framework` should be in top-5
- Got top-3: `cinematography-hard-soft-light` (score=0.28), `directing-protagonist-endangered` (score=0.28), `directing-ambiguity-diagnosis` (score=0.26)

**[directing-masterclass/directing-story-framework] prompt #4**
> 游戏里每条支线任务都需要有完整的弧线吗？我想设计几条支线但不知道结构上该怎么处理。

- Expected: `directing-story-framework` should be in top-5
- Got top-3: `color-grading-contrast-saturation` (score=0.29), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[directing-masterclass/directing-tension-formula] prompt #1**
> 这场戏好像缺点什么，观众看到这里就不想看了，但我说不上来问题在哪。

- Expected: `directing-tension-formula` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-tension-formula] prompt #2**
> 我的剧本中段塌了，前面很好后面也很好，就是中间这段不知道为什么特别无聊。

- Expected: `directing-tension-formula` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[directing-masterclass/directing-tension-formula] prompt #3**
> 怎么让人一直想看下去？我想设计一个让读者停不下来的故事。

- Expected: `directing-tension-formula` should be in top-5
- Got top-3: `directing-protagonist-endangered` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[directing-masterclass/directing-tension-formula] prompt #4**
> 我设计了一个产品引导流程，但用户到了第三步就流失了，怎么让他们继续看下去？

- Expected: `directing-tension-formula` should be in top-5
- Got top-3: `color-grading-look-development` (score=0.22), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[directing-masterclass/directing-tension-formula] prompt #5**
> 我的游戏任务链中，玩家完成一个任务后就没有动力继续了，怎么解决？

- Expected: `directing-tension-formula` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[master-shots-v1/shot-camera-choreography] prompt #should-trigger-03**
> 我拍完发现摄影机运动太刻意了，观众老是注意到摄影机在动，怎么让它不被注意到？

- Expected: `shot-camera-choreography` should be in top-5
- Got top-3: `msv3-speed-conveyance` (score=0.32), `dialogue-distance-collapse-arc` (score=0.30), `shot-still-vs-motion-decision` (score=0.25)

**[master-shots-v1/shot-camera-choreography] prompt #should-trigger-04**
> 帮我设计一场戏的镜头方案，角色要穿过人群走到舞台中央发表演讲

- Expected: `shot-camera-choreography` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `dialogue-busy-hands-no-eye-contact` (score=0.27), `cinematography-180-degree-rule` (score=0.00)

**[master-shots-v1/shot-distract-and-scare] prompt #should-trigger-02**
> 观众都知道我角色身后会出现一个鬼，我怎么还能吓到他们？

- Expected: `shot-distract-and-scare` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[master-shots-v1/shot-distract-and-scare] prompt #should-trigger-03**
> 我想让两个人第一次对视的瞬间特别有张力，怎么拍才能让观众期待这个对视？

- Expected: `shot-distract-and-scare` should be in top-5
- Got top-3: `shot-dual-camera-tension` (score=0.27), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[master-shots-v1/shot-dual-camera-tension] prompt #should-trigger-02**
> 两人对峙的场景，不用台词怎么让观众一眼看出谁更强？

- Expected: `shot-dual-camera-tension` should be in top-5
- Got top-3: `shot-design-dialogue-staging` (score=0.26), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[master-shots-v1/shot-equal-length-rhythm] prompt #should-trigger-02**
> 观众都知道危险要来了，但我想让他们仍然被吓到，怎么通过镜头长度来控制节奏？

- Expected: `shot-equal-length-rhythm` should be in top-5
- Got top-3: `scene-transition-seamless-pause` (score=0.28), `scene-transition-low-point-no-plot` (score=0.26), `cinematography-180-degree-rule` (score=0.00)

**[master-shots-v1/shot-equal-length-rhythm] prompt #should-trigger-03**
> 这场戏的剪辑节奏不对，每个镜头长度都不一样，看起来很乱，怎么让它更有节奏感？

- Expected: `shot-equal-length-rhythm` should be in top-5
- Got top-3: `shot-design-continuity-composition` (score=0.29), `scene-transition-caboose-diagnosis` (score=0.28), `scene-transition-seamless-pause` (score=0.28)

**[master-shots-v1/shot-still-vs-motion-decision] prompt #should-trigger-02**
> 我想表现角色内心的挣扎，不用对白不用旁白，纯靠画面怎么让观众感受到？

- Expected: `shot-still-vs-motion-decision` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[master-shots-v1/shot-telephoto-compression] prompt #should-trigger-01**
> 我要拍一个打斗场景，但演员不能真的打到对方，怎么拍才能看起来像真的打中了？

- Expected: `shot-telephoto-compression` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[master-shots-v1/shot-telephoto-compression] prompt #should-trigger-02**
> 我拍一个追踪场景，追踪者和被追踪者实际距离很远，但我想让观众觉得快追上了，有什么办法？

- Expected: `shot-telephoto-compression` should be in top-5
- Got top-3: `msv3-power-distance` (score=0.30), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[master-shots-v1/shot-telephoto-compression] prompt #should-trigger-03**
> 我有一场走廊里的恐怖戏，角色慢慢走近，但走廊太宽了看起来不吓人，怎么增强威胁感？

- Expected: `shot-telephoto-compression` should be in top-5
- Got top-3: `dialogue-focal-progression` (score=0.35), `shot-distract-and-scare` (score=0.29), `scene-transition-loyalty-transfer` (score=0.28)

**[master-shots-v1/shot-telephoto-compression] prompt #should-trigger-04**
> 低成本动作片，没有武指也没有特效预算，打斗场面怎么拍得有冲击力？

- Expected: `shot-telephoto-compression` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[master-shots-v2/dialogue-camera-follow-identity] prompt #should-trigger-01**
> 追逐场景中，我该让摄影机跟着追人的还是被追的？

- Expected: `dialogue-camera-follow-identity` should be in top-5
- Got top-3: `msv3-speed-conveyance` (score=0.32), `shot-dual-camera-tension` (score=0.27), `cinematography-180-degree-rule` (score=0.00)

**[master-shots-v2/dialogue-camera-follow-identity] prompt #should-trigger-02**
> 老板在训话员工，怎么让观众站在老板这边？

- Expected: `dialogue-camera-follow-identity` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[master-shots-v2/dialogue-camera-follow-identity] prompt #should-trigger-03**
> 一个角色追着另一个角色在房间里走来走去说话，怎么拍出追赶感？

- Expected: `dialogue-camera-follow-identity` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[master-shots-v2/dialogue-closeup-timing] prompt #should-trigger-02**
> 两个人在吵架，越走越近最后面对面停下了，之前一直是运动镜头，这时候该用什么镜头？

- Expected: `dialogue-closeup-timing` should be in top-5
- Got top-3: `shot-still-vs-motion-decision` (score=0.25), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[master-shots-v2/dialogue-distance-collapse-arc] prompt #should-trigger-01**
> 角色在场景里情绪崩溃了，哭完了之后怎么自然地回到正常对话？

- Expected: `dialogue-distance-collapse-arc` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `dialogue-busy-hands-no-eye-contact` (score=0.27), `cinematography-180-degree-rule` (score=0.00)

**[master-shots-v2/dialogue-distance-collapse-arc] prompt #should-trigger-02**
> 我想用摄影机推近来表现两个角色越来越亲密，但不想切镜头

- Expected: `dialogue-distance-collapse-arc` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[master-shots-v2/dialogue-distance-collapse-arc] prompt #should-trigger-03**
> 两个角色在偷偷说话，我想在推近的过程中让观众感觉到他们之间有隔阂

- Expected: `dialogue-distance-collapse-arc` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[master-shots-v2/dialogue-gaze-mapping] prompt #should-trigger-01**
> 我在拍一个八个人围坐开会的对话场景，不想用全景镜头但观众分不清谁在跟谁说话，怎么办？

- Expected: `dialogue-gaze-mapping` should be in top-5
- Got top-3: `msv3-body-performance` (score=0.30), `dialogue-busy-hands-no-eye-contact` (score=0.27), `cinematography-180-degree-rule` (score=0.00)

**[master-shots-v2/dialogue-gaze-mapping] prompt #should-trigger-02**
> 场景里有个角色一直没说话，后来突然插了一句话，观众完全不知道他是谁、在哪里，怎么处理？

- Expected: `dialogue-gaze-mapping` should be in top-5
- Got top-3: `color-grading-contrast-saturation` (score=0.29), `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00)

**[master-shots-v2/dialogue-gaze-mapping] prompt #should-trigger-03**
> 群戏里演员的脸都在画面中央，但观众还是不知道他们分别在房间的什么位置，有什么办法？

- Expected: `dialogue-gaze-mapping` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[master-shots-v3/msv3-body-performance] prompt #bp-02**
> 我在拍一场两个角色在餐桌上进行无声对峙的戏。两人都有话想说但忍着。怎么用镜头捕捉这种张力？

- Expected: `msv3-body-performance` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `shot-dual-camera-tension` (score=0.27), `shot-design-dialogue-staging` (score=0.26)

**[master-shots-v3/msv3-body-performance] prompt #bp-04**
> 我在导一场角色偷偷观察心仪对象的戏。不用台词怎么表现这种吸引力？

- Expected: `msv3-body-performance` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[master-shots-v3/msv3-lens-emotion-mapping] prompt #lm-01**
> 我在拍一场两个角色在小房间里激烈争吵的对话戏。想让观众感受到窒息感和紧迫感。该用什么焦距的镜头？摄影机怎么动？

- Expected: `msv3-lens-emotion-mapping` should be in top-5
- Got top-3: `msv3-speed-conveyance` (score=0.32), `dialogue-focal-character-temperament` (score=0.30), `scene-transition-loyalty-transfer` (score=0.28)

**[master-shots-v3/msv3-lens-emotion-mapping] prompt #lm-02**
> 角色在一条拥挤的街道上意识到有人在远处盯着他。我想在镜头中让他在情感上与人群隔离开来。该选什么焦距？

- Expected: `msv3-lens-emotion-mapping` should be in top-5
- Got top-3: `dialogue-focal-character-temperament` (score=0.30), `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00)

**[master-shots-v3/msv3-lens-emotion-mapping] prompt #lm-03**
> 斯坦尼康操作员想用85mm镜头拍一场跟拍主角穿过走廊的戏。这个方案好不好？

- Expected: `msv3-lens-emotion-mapping` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[master-shots-v3/msv3-lens-emotion-mapping] prompt #lm-04**
> 我想拍一个斯皮尔伯格式的单镜头场景，两个演员在房间里走动，不切镜头就能看到多种构图。该怎么设置？

- Expected: `msv3-lens-emotion-mapping` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[master-shots-v3/msv3-lens-emotion-mapping] prompt #lm-05**
> 我在拍一场追逐戏，但广角镜头让主角的脸在特写中变形了。怎么解决？

- Expected: `msv3-lens-emotion-mapping` should be in top-5
- Got top-3: `msv3-speed-conveyance` (score=0.95), `dialogue-closeup-timing` (score=0.30), `dialogue-telephoto-claustrophobia` (score=0.30)

**[master-shots-v3/msv3-power-distance] prompt #pd-03**
> 我有一个俯拍镜头，反派走向摄影机。他应该是压倒性的，但俯角让他看起来很弱。我哪里做错了？

- Expected: `msv3-power-distance` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[master-shots-v3/msv3-power-distance] prompt #pd-04**
> 两个角色在谈判。想让观众感觉其中一个占上风，但他们坐在同一张桌子旁边。怎么用视觉来创造这种差距？

- Expected: `msv3-power-distance` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[master-shots-v3/msv3-power-distance] prompt #pd-05**
> 将军站在高台上对部队讲话。摄影机在下方仰拍，但他看起来还是没有威严感。为什么？

- Expected: `msv3-power-distance` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[master-shots-v3/msv3-speed-conveyance] prompt #sc-03**
> 我想拍一个单镜头的动作场面，要感觉快速且有冲击力。该用哪些摄影机技巧？

- Expected: `msv3-speed-conveyance` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[master-shots-v3/msv3-symbolic-staging] prompt #ss-01**
> 两个角色暗中互相吸引，但在聊很平常的工作话题。怎么在不改台词的情况下用镜头传达这种吸引力？

- Expected: `msv3-symbolic-staging` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[master-shots-v3/msv3-symbolic-staging] prompt #ss-04**
> 一对情侣正在亲密时刻，但我想表现有什么东西即将打断他们的连接。怎么用镜头语言来铺垫？

- Expected: `msv3-symbolic-staging` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[master-shots-v3/msv3-symbolic-staging] prompt #ss-05**
> 一个看起来很有压迫感的角色从俯角向摄影机走来。俯角应该让他看起来弱吗？

- Expected: `msv3-symbolic-staging` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[scene-transitions/scene-transition-binary-opposition] prompt #should-trigger-02**
> 我的电影有三条故事线，怎么让观众在切换时感受到每条线的不同氛围？

- Expected: `scene-transition-binary-opposition` should be in top-5
- Got top-3: `directing-protagonist-endangered` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[scene-transitions/scene-transition-binary-opposition] prompt #should-trigger-03**
> 怎么在一个房间里拍完一整场戏还能让观众感觉到场景在变化？

- Expected: `scene-transition-binary-opposition` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[scene-transitions/scene-transition-caboose-diagnosis] prompt #should-trigger-02**
> 电影太长了，怎么精简？

- Expected: `scene-transition-caboose-diagnosis` should be in top-5
- Got top-3: `directing-scene-necessity` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[scene-transitions/scene-transition-four-function-diagnosis] prompt #should-trigger-01**
> 我在剪辑一部短片，两个场景之间的转场不知道该用什么风格，音乐还是静默？

- Expected: `scene-transition-four-function-diagnosis` should be in top-5
- Got top-3: `scene-transition-music-quadrant` (score=0.55), `scene-transition-caboose-diagnosis` (score=0.28), `color-grading-shot-matching` (score=0.23)

**[scene-transitions/scene-transition-four-function-diagnosis] prompt #should-trigger-03**
> 我在设计一款叙事游戏的过场动画，每个过场应该让玩家做什么？

- Expected: `scene-transition-four-function-diagnosis` should be in top-5
- Got top-3: `scene-transition-binary-opposition` (score=0.29), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[scene-transitions/scene-transition-low-point-no-plot] prompt #should-trigger-01**
> 我的电影连续三个场景都是高强度动作戏，观众说看得太累了。怎么处理？

- Expected: `scene-transition-low-point-no-plot` should be in top-5
- Got top-3: `color-grading-contrast-saturation` (score=0.29), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[scene-transitions/scene-transition-low-point-no-plot] prompt #should-trigger-02**
> 两个紧张场景之间怎么过渡才不会让观众觉得太赶？

- Expected: `scene-transition-low-point-no-plot` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[scene-transitions/scene-transition-loyalty-transfer] prompt #should-trigger-01**
> 我的电影中途要换主角，怎么让观众接受？

- Expected: `scene-transition-loyalty-transfer` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[scene-transitions/scene-transition-music-quadrant] prompt #should-trigger-02**
> 我在剪辑一个短视频，两个片段之间要不要加BGM过渡？

- Expected: `scene-transition-music-quadrant` should be in top-5
- Got top-3: `scene-transition-caboose-diagnosis` (score=0.28), `color-grading-shot-matching` (score=0.23), `cinematography-180-degree-rule` (score=0.00)

**[scene-transitions/scene-transition-seamless-pause] prompt #should-trigger-01**
> 我的场景转换有8分钟长，怎么让观众不觉得拖沓？

- Expected: `scene-transition-seamless-pause` should be in top-5
- Got top-3: `scene-transition-binary-opposition` (score=0.29), `scene-transition-synch-node` (score=0.29), `scene-transition-caboose-diagnosis` (score=0.28)

**[scene-transitions/scene-transition-seamless-pause] prompt #should-trigger-02**
> 怎么让观众在不知不觉中休息？

- Expected: `scene-transition-seamless-pause` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[scene-transitions/scene-transition-synch-node] prompt #should-trigger-01**
> 我有三条故事线，怎么让观众知道它们是相关的？

- Expected: `scene-transition-synch-node` should be in top-5
- Got top-3: `directing-protagonist-endangered` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[scene-transitions/scene-transition-weather-contrast] prompt #should-trigger-01**
> 我的悬疑场景放在晴天会不会没有气氛？

- Expected: `scene-transition-weather-contrast` should be in top-5
- Got top-3: `shot-distract-and-scare` (score=0.29), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[shot-design/shot-design-angle-context] prompt #should-trigger-01**
> 低角度拍出来效果不对怎么办？

- Expected: `shot-design-angle-context` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[shot-design/shot-design-axis-of-action] prompt #should-trigger-02**
> 观众搞不清谁在看谁怎么办

- Expected: `shot-design-axis-of-action` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[shot-design/shot-design-axis-of-action] prompt #should-trigger-03**
> 怎么在对话场景中切换摄影机位置？

- Expected: `shot-design-axis-of-action` should be in top-5
- Got top-3: `msv3-power-distance` (score=0.30), `dialogue-busy-hands-no-eye-contact` (score=0.27), `cinematography-180-degree-rule` (score=0.00)

**[shot-design/shot-design-continuity-composition] prompt #should-trigger-01**
> 画面看起来不对劲，构图有问题

- Expected: `shot-design-continuity-composition` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[shot-design/shot-design-continuity-composition] prompt #should-trigger-03**
> 剪辑后画面节奏不对怎么办？

- Expected: `shot-design-continuity-composition` should be in top-5
- Got top-3: `scene-transition-caboose-diagnosis` (score=0.28), `scene-transition-seamless-pause` (score=0.28), `scene-transition-low-point-no-plot` (score=0.26)

**[shot-design/shot-design-dialogue-staging] prompt #should-trigger-01**
> 两个人对话怎么安排站位？

- Expected: `shot-design-dialogue-staging` should be in top-5
- Got top-3: `dialogue-busy-hands-no-eye-contact` (score=0.27), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[shot-design/shot-design-dialogue-staging] prompt #should-trigger-03**
> 对话场景看起来很单调怎么办？

- Expected: `shot-design-dialogue-staging` should be in top-5
- Got top-3: `dialogue-busy-hands-no-eye-contact` (score=0.27), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[shot-design/shot-design-dramatic-range] prompt #should-trigger-01**
> 摄影机放在哪里效果最好？

- Expected: `shot-design-dramatic-range` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[shot-design/shot-design-dramatic-range] prompt #should-trigger-02**
> 室内对话场景摄影机怎么放？

- Expected: `shot-design-dramatic-range` should be in top-5
- Got top-3: `dialogue-busy-hands-no-eye-contact` (score=0.27), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[shot-design/shot-design-dramatic-range] prompt #should-trigger-03**
> 怎么用空间来表现角色关系？

- Expected: `shot-design-dramatic-range` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[shot-design/shot-design-pov-spectrum] prompt #should-trigger-01**
> 怎么让观众站在主角的立场？

- Expected: `shot-design-pov-spectrum` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[shot-design/shot-design-pov-spectrum] prompt #should-trigger-03**
> 怎么控制观众对角色的认同程度？

- Expected: `shot-design-pov-spectrum` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.55), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[shot-design/shot-design-sightline-cut] prompt #should-trigger-01**
> 观众搞不清谁在看谁怎么办？

- Expected: `shot-design-sightline-cut` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[shot-design/shot-design-sightline-cut] prompt #should-trigger-03**
> 怎么从一个角色的视角切到另一个？

- Expected: `shot-design-sightline-cut` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[shot-design/shot-design-storyboard-rapid] prompt #should-trigger-01**
> 我不会画画，怎么快速画出分镜？

- Expected: `shot-design-storyboard-rapid` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[shot-design/shot-design-storyboard-rapid] prompt #should-trigger-03**
> 怎么把脑中的画面快速变成草图？

- Expected: `shot-design-storyboard-rapid` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-auditory-hierarchy] prompt #should-trigger-01**
> 混录的时候对白被音效盖住了，观众听不清台词，怎么处理层次？

- Expected: `sound-design-auditory-hierarchy` should be in top-5
- Got top-3: `color-grading-contrast-saturation` (score=0.29), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[sound-design/sound-design-auditory-hierarchy] prompt #should-trigger-02**
> 我在做一个战场场景，枪声、喊叫声、音乐同时响，怎么让观众知道该注意哪个？

- Expected: `sound-design-auditory-hierarchy` should be in top-5
- Got top-3: `scene-transition-music-quadrant` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[sound-design/sound-design-auditory-hierarchy] prompt #should-trigger-03**
> 环境声太突出抢了对白的注意力，怎么降低但又不能完全去掉？

- Expected: `sound-design-auditory-hierarchy` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-auditory-hierarchy] prompt #should-trigger-04**
> 声音设计中如何建立清晰的听觉层次，让观众的注意力跟着叙事走？

- Expected: `sound-design-auditory-hierarchy` should be in top-5
- Got top-3: `scene-transition-binary-opposition` (score=0.29), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[sound-design/sound-design-consistency] prompt #should-trigger-01**
> 上一集里这个角色的关门声是木门声，这一集换成了金属门声，观众会不会注意到？

- Expected: `sound-design-consistency` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[sound-design/sound-design-consistency] prompt #should-trigger-02**
> 系列片中同一辆车在不同集里引擎声不一样，怎么保持一致？

- Expected: `sound-design-consistency` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-consistency] prompt #should-trigger-03**
> 声音库里有好几个类似的爆炸声，选哪个作为我们片子的标准爆炸声？

- Expected: `sound-design-consistency` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-consistency] prompt #should-trigger-04**
> 需要替换一个已经建立的声音标识，但又不能让观众觉得突兀，怎么做？

- Expected: `sound-design-consistency` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-contrast-drama] prompt #should-trigger-01**
> 声音一直很响但没有感觉，观众已经麻木了，怎么通过对比重新制造冲击力？

- Expected: `sound-design-contrast-drama` should be in top-5
- Got top-3: `scene-transition-binary-opposition` (score=0.29), `scene-transition-weather-contrast` (score=0.28), `shot-still-vs-motion-decision` (score=0.25)

**[sound-design/sound-design-contrast-drama] prompt #should-trigger-02**
> 设计一个从极度安静到突然爆发的转场，铺垫怎么做？

- Expected: `sound-design-contrast-drama` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-contrast-drama] prompt #should-trigger-03**
> 动作场景的音效太吵了耳朵疼，能不能在高峰之间插入喘息空间？

- Expected: `sound-design-contrast-drama` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-contrast-drama] prompt #should-trigger-04**
> 恐怖场景中怎么用静默来最大化惊吓效果？

- Expected: `sound-design-contrast-drama` should be in top-5
- Got top-3: `shot-distract-and-scare` (score=0.58), `scene-transition-music-quadrant` (score=0.28), `cinematography-180-degree-rule` (score=0.00)

**[sound-design/sound-design-diegetic-taxonomy] prompt #should-trigger-01**
> 画面外有一个看不见的声源，怎么设计让观众好奇但不困惑？

- Expected: `sound-design-diegetic-taxonomy` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-diegetic-taxonomy] prompt #should-trigger-02**
> 角色戴着耳机听音乐，观众应该听到他听的内容还是环境声？

- Expected: `sound-design-diegetic-taxonomy` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `scene-transition-music-quadrant` (score=0.28), `cinematography-180-degree-rule` (score=0.00)

**[sound-design/sound-design-diegetic-taxonomy] prompt #should-trigger-03**
> 要不要在画面上展示声源？什么时候揭示比较有戏剧效果？

- Expected: `sound-design-diegetic-taxonomy` should be in top-5
- Got top-3: `msv3-unexpected-reveal` (score=0.32), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[sound-design/sound-design-energy-model] prompt #should-trigger-01**
> 纪录片的声音应该保持客观真实还是可以做主观化处理？

- Expected: `sound-design-energy-model` should be in top-5
- Got top-3: `color-grading-contrast-saturation` (score=0.29), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[sound-design/sound-design-energy-model] prompt #should-trigger-02**
> 混录中对白和音效冲突，怎么用能量模型判断优先级？

- Expected: `sound-design-energy-model` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-energy-model] prompt #should-trigger-03**
> 为一个有道德困境的角色设计声音主题，声音应该让人同情还是反感？

- Expected: `sound-design-energy-model` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[sound-design/sound-design-energy-model] prompt #should-trigger-04**
> 声音的能量高低怎么和叙事的情感弧线匹配？

- Expected: `sound-design-energy-model` should be in top-5
- Got top-3: `dialogue-distance-collapse-arc` (score=0.30), `scene-transition-binary-opposition` (score=0.29), `cinematography-180-degree-rule` (score=0.00)

**[sound-design/sound-design-entrainment] prompt #should-trigger-01**
> 需要让观众在这个场景中放松下来，BPM应该选多少？

- Expected: `sound-design-entrainment` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-entrainment] prompt #should-trigger-02**
> 冥想场景的声音设计，怎么通过节拍引导观众进入特定意识状态？

- Expected: `sound-design-entrainment` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-entrainment] prompt #should-trigger-03**
> 配乐节奏和画面剪辑不匹配，怎么调整BPM让它们同步？

- Expected: `sound-design-entrainment` should be in top-5
- Got top-3: `scene-transition-caboose-diagnosis` (score=0.28), `scene-transition-music-quadrant` (score=0.28), `scene-transition-seamless-pause` (score=0.28)

**[sound-design/sound-design-entrainment] prompt #should-trigger-04**
> 游戏沉浸式音频中怎么用声音频率引导玩家的生理状态？

- Expected: `sound-design-entrainment` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-expectation] prompt #should-trigger-01**
> 恐怖场景的惊吓点怎么用声音铺垫预期再打破？

- Expected: `sound-design-expectation` should be in top-5
- Got top-3: `shot-distract-and-scare` (score=0.58), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[sound-design/sound-design-expectation] prompt #should-trigger-02**
> 喜剧场景中怎么用声音打破严肃预期来制造笑点？

- Expected: `sound-design-expectation` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-expectation] prompt #should-trigger-03**
> 场景太可预测了，怎么用声音制造意外？

- Expected: `sound-design-expectation` should be in top-5
- Got top-3: `msv3-unexpected-reveal` (score=0.32), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[sound-design/sound-design-expectation] prompt #should-trigger-04**
> 反转揭示场景的声音怎么配合叙事转折？

- Expected: `sound-design-expectation` should be in top-5
- Got top-3: `msv3-unexpected-reveal` (score=0.32), `scene-transition-binary-opposition` (score=0.29), `cinematography-180-degree-rule` (score=0.00)

**[sound-design/sound-design-less-is-more] prompt #should-trigger-01**
> 场景声音设计感觉太满了，删掉哪些能反而更有力量？

- Expected: `sound-design-less-is-more` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-less-is-more] prompt #should-trigger-02**
> 设计一个反派角色的声音，是不是越少越神秘？

- Expected: `sound-design-less-is-more` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[sound-design/sound-design-less-is-more] prompt #should-trigger-03**
> 恐怖场景中怎么用极少的声音制造最大的恐惧感？

- Expected: `sound-design-less-is-more` should be in top-5
- Got top-3: `shot-distract-and-scare` (score=0.29), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[sound-design/sound-design-less-is-more] prompt #should-trigger-04**
> 主角独自在空房间里，只保留一个声音应该选什么？

- Expected: `sound-design-less-is-more` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-listening-modes] prompt #should-trigger-01**
> 观众听到这个声音会以为是什么发出的？怎么利用这种认知偏差？

- Expected: `sound-design-listening-modes` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-listening-modes] prompt #should-trigger-02**
> 外语角色说话时观众听不懂语言但需要感受到情绪，怎么设计？

- Expected: `sound-design-listening-modes` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[sound-design/sound-design-listening-modes] prompt #should-trigger-03**
> 评估一段声音设计是否有效，观众会以什么方式听？

- Expected: `sound-design-listening-modes` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-listening-modes] prompt #should-trigger-04**
> 恐怖场景中怎么利用'因果倾听'让观众自己脑补恐怖源？

- Expected: `sound-design-listening-modes` should be in top-5
- Got top-3: `shot-distract-and-scare` (score=0.29), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[sound-design/sound-design-music-story-parallel] prompt #should-trigger-01**
> 整部电影的声音'调性'应该是什么？怎么定义？

- Expected: `sound-design-music-story-parallel` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-music-story-parallel] prompt #should-trigger-02**
> 多个角色需要各自的声音标识，怎么设计不冲突？

- Expected: `sound-design-music-story-parallel` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[sound-design/sound-design-music-story-parallel] prompt #should-trigger-03**
> 音乐和音效在同一个场景中打架了，怎么协调？

- Expected: `sound-design-music-story-parallel` should be in top-5
- Got top-3: `scene-transition-music-quadrant` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[sound-design/sound-design-music-story-parallel] prompt #should-trigger-04**
> 声音弧线怎么和故事的三幕结构对应？

- Expected: `sound-design-music-story-parallel` should be in top-5
- Got top-3: `directing-protagonist-endangered` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[sound-design/sound-design-size-control] prompt #should-trigger-01**
> 一个巨大怪兽的吼叫声怎么设计才能听起来真的很大？

- Expected: `sound-design-size-control` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-size-control] prompt #should-trigger-02**
> 微小物体（比如昆虫）的声音怎么让它听起来小而不是普通？

- Expected: `sound-design-size-control` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-size-control] prompt #should-trigger-03**
> 降速处理后声音和画面不同步了，怎么保持大小感的同时修正同步？

- Expected: `sound-design-size-control` should be in top-5
- Got top-3: `color-grading-contrast-saturation` (score=0.29), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[sound-design/sound-design-size-control] prompt #should-trigger-04**
> 低频和高频的比例怎么影响观众对物体大小的感知？

- Expected: `sound-design-size-control` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-sonata-drama] prompt #should-trigger-01**
> 整部电影的声音弧线怎么设计？开头和结尾的声音应该有什么呼应？

- Expected: `sound-design-sonata-drama` should be in top-5
- Got top-3: `directing-story-framework` (score=0.29), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[sound-design/sound-design-sonata-drama] prompt #should-trigger-02**
> 角色的声音主题需要在影片中发生变化，怎么渐进式演变？

- Expected: `sound-design-sonata-drama` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[sound-design/sound-design-sonata-drama] prompt #should-trigger-03**
> 结尾需要'回家'的感觉，声音怎么实现这种奏鸣曲式的回归？

- Expected: `sound-design-sonata-drama` should be in top-5
- Got top-3: `directing-story-framework` (score=0.29), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[sound-design/sound-design-sonata-drama] prompt #should-trigger-04**
> 声音的'呈示-发展-再现'结构怎么对应故事的三幕？

- Expected: `sound-design-sonata-drama` should be in top-5
- Got top-3: `directing-protagonist-endangered` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[sound-design/sound-design-sync-illusion] prompt #should-trigger-01**
> 真实录制的拳头打击声效果不好，怎么用拟音创造更有冲击力的声音？

- Expected: `sound-design-sync-illusion` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-sync-illusion] prompt #should-trigger-02**
> 画面中一个不存在的物体需要有声音，怎么创造这种声音？

- Expected: `sound-design-sync-illusion` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-sync-illusion] prompt #should-trigger-03**
> 声音和画面差了一帧，观众能察觉到吗？怎么精确对齐？

- Expected: `sound-design-sync-illusion` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[sound-design/sound-design-sync-illusion] prompt #should-trigger-04**
> 拟音师怎么用不相关的物体创造出逼真的同步声音？

- Expected: `sound-design-sync-illusion` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[story-design/story-design-beat-sheet] prompt #should-trigger-01**
> 我想写一个关于时间旅行的故事，但不知道怎么构建结构

- Expected: `story-design-beat-sheet` should be in top-5
- Got top-3: `directing-protagonist-endangered` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[story-design/story-design-beat-sheet] prompt #should-trigger-02**
> 我的剧本第二幕总是写散了，有什么好的结构工具吗？

- Expected: `story-design-beat-sheet` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[story-design/story-design-beat-sheet] prompt #should-trigger-03**
> Beat Sheet怎么用？15个节拍每个都要写吗？

- Expected: `story-design-beat-sheet` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[story-design/story-design-five-step-finale] prompt #should-trigger-02**
> 结局怎么设计才能让观众感动？

- Expected: `story-design-five-step-finale` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[story-design/story-design-genres] prompt #should-trigger-01**
> 我的故事是关于一群人被困在一个房子里，有一个怪物追杀他们，这是什么类型？

- Expected: `story-design-genres` should be in top-5
- Got top-3: `directing-protagonist-endangered` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[story-design/story-design-genres] prompt #should-trigger-02**
> 爱情片的套路有哪些？怎么写出不一样的爱情故事？

- Expected: `story-design-genres` should be in top-5
- Got top-3: `story-design-theme-b-story` (score=0.32), `directing-protagonist-endangered` (score=0.28), `story-design-shard-of-glass` (score=0.27)

**[story-design/story-design-genres] prompt #should-trigger-03**
> 我的主角是一个普通人突然获得了超能力，这算什么类型？

- Expected: `story-design-genres` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[story-design/story-design-logline] prompt #should-trigger-01**
> 我有一个故事创意，能帮我用一句话说清楚吗？

- Expected: `story-design-logline` should be in top-5
- Got top-3: `directing-protagonist-endangered` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[story-design/story-design-logline] prompt #should-trigger-03**
> 怎么评估一个故事创意是否可行？

- Expected: `story-design-logline` should be in top-5
- Got top-3: `directing-protagonist-endangered` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[story-design/story-design-midpoint] prompt #should-trigger-03**
> 故事的节奏怎么控制？中间太平淡了

- Expected: `story-design-midpoint` should be in top-5
- Got top-3: `directing-protagonist-endangered` (score=0.28), `scene-transition-seamless-pause` (score=0.28), `scene-transition-low-point-no-plot` (score=0.26)

**[story-design/story-design-save-the-cat] prompt #should-trigger-01**
> 我的主角出场后观众不喜欢他，怎么改？

- Expected: `story-design-save-the-cat` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[story-design/story-design-save-the-cat] prompt #should-trigger-02**
> 怎么让观众一开始就关心主角？

- Expected: `story-design-save-the-cat` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

**[story-design/story-design-shard-of-glass] prompt #should-trigger-02**
> 角色弧线怎么设计才有深度？

- Expected: `story-design-shard-of-glass` should be in top-5
- Got top-3: `scene-transition-loyalty-transfer` (score=0.28), `directing-end-before-begin` (score=0.27), `cinematography-180-degree-rule` (score=0.00)

**[story-design/story-design-theme-b-story] prompt #should-trigger-01**
> 我的故事'不知道在说什么'，主题表达不清楚

- Expected: `story-design-theme-b-story` should be in top-5
- Got top-3: `directing-protagonist-endangered` (score=0.28), `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00)

**[story-design/story-design-theme-b-story] prompt #should-trigger-03**
> 主题表达太说教了怎么办？

- Expected: `story-design-theme-b-story` should be in top-5
- Got top-3: `cinematography-180-degree-rule` (score=0.00), `cinematography-back-lighting` (score=0.00), `cinematography-hard-soft-light` (score=0.00)

### should_not_trigger failures (target skill IS top-1)

**[color-grading/color-grading-log-workflow] prompt #should-not-trigger-03**
> 摄影机怎么设置Log模式？

- Expected: `color-grading-log-workflow` should NOT be top-1
- Got top-1: `color-grading-log-workflow` (score=0.18)

**[color-grading/color-grading-skin-tone-vectorscope] prompt #should-not-trigger-03**
> 肤色在PS中怎么修？

- Expected: `color-grading-skin-tone-vectorscope` should NOT be top-1
- Got top-1: `color-grading-skin-tone-vectorscope` (score=0.25)

**[directing-masterclass/directing-coincidence-trouble] prompt #6**
> 这个巧合设定在世界观里合理吗？会不会让观众觉得太假？

- Expected: `directing-coincidence-trouble` should NOT be top-1
- Got top-1: `directing-coincidence-trouble` (score=0.29)

**[directing-masterclass/directing-coincidence-trouble] prompt #8**
> 现实中真的会有这么多巧合吗？这个概率是不是太低了？

- Expected: `directing-coincidence-trouble` should NOT be top-1
- Got top-1: `directing-coincidence-trouble` (score=0.29)

**[master-shots-v1/shot-distract-and-scare] prompt #should-not-trigger-02**
> 怎么营造一种持续的悬疑氛围？整场戏都要让观众感到不安。

- Expected: `shot-distract-and-scare` should NOT be top-1
- Got top-1: `shot-distract-and-scare` (score=0.29)

**[master-shots-v1/shot-dual-camera-tension] prompt #should-not-trigger-02**
> 手持摄影和稳定器拍出来的画面质感有什么不同？我该买哪个？

- Expected: `shot-dual-camera-tension` should NOT be top-1
- Got top-1: `shot-dual-camera-tension` (score=0.27)

**[scene-transitions/scene-transition-loyalty-transfer] prompt #should-not-trigger-01**
> 这个角色的性格怎么塑造？

- Expected: `scene-transition-loyalty-transfer` should NOT be top-1
- Got top-1: `scene-transition-loyalty-transfer` (score=0.28)

**[scene-transitions/scene-transition-music-quadrant] prompt #should-not-trigger-01**
> 这段配乐的版权问题怎么解决？

- Expected: `scene-transition-music-quadrant` should NOT be top-1
- Got top-1: `scene-transition-music-quadrant` (score=0.28)

**[scene-transitions/scene-transition-seamless-pause] prompt #should-not-trigger-01**
> 电视剧的广告间歇怎么设计？

- Expected: `scene-transition-seamless-pause` should NOT be top-1
- Got top-1: `scene-transition-seamless-pause` (score=0.28)

**[scene-transitions/scene-transition-weather-contrast] prompt #should-not-trigger-01**
> 今天天气怎么样？

- Expected: `scene-transition-weather-contrast` should NOT be top-1
- Got top-1: `scene-transition-weather-contrast` (score=0.28)

## Edge Cases (reviewed)

| Book/Skill | Prompt (truncated) | Top-3 routed to |
|-----------|-------------------|-----------------|
| cinematography-brown/cinematography-180-degree-rule | 我想故意打破180度规则制造混乱感 | `shot-design-axis-of-action`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| color-grading/color-grading-color-temperature | 夜戏中混合了月光（蓝）和路灯（橙），色温怎么平衡才自然？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| color-grading/color-grading-contrast-before-color | 风格化调色（如漂白效果）中对比度和色彩的顺序还重要吗？ | `scene-transition-binary-opposition`, `color-grading-contrast-before-color`, `scene-transition-weather-contrast` |
| color-grading/color-grading-contrast-saturation | 黑白调色中饱和度为零，对比度策略需要调整吗？ | `color-grading-contrast-saturation`, `scene-transition-binary-opposition`, `color-grading-contrast-before-color` |
| color-grading/color-grading-filter-nonlinear | 虚拟制作（LED Volume）中还需要光学滤镜吗？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| color-grading/color-grading-log-workflow | 混合了Log和Rec.709素材的项目，调色工作流怎么统一？ | `color-grading-shot-matching`, `color-grading-primary-workflow`, `color-grading-log-workflow` |
| color-grading/color-grading-look-development | 广告项目中客户要求'电影感'但预算有限，Look怎么设计？ | `color-grading-look-development`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| color-grading/color-grading-memory-colors | 科幻片中外星球的植物颜色完全是想象的，没有记忆色彩参考怎么办？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| color-grading/color-grading-overexposure-recovery | RAW素材和ProRes素材的过曝恢复能力差多少？ | `color-grading-log-workflow`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| color-grading/color-grading-primary-workflow | 现场DIT的一级校色和后期调色师的一级校色有什么区别？ | `color-grading-primary-workflow`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| color-grading/color-grading-shot-matching | 日拍夜的素材和真实夜景素材怎么匹配？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| color-grading/color-grading-skin-tone-vectorscope | 非人类角色（如外星人、动画角色）的肤色还需要参考I-bar吗？ | `color-grading-skin-tone-vectorscope`, `scene-transition-loyalty-transfer`, `cinematography-180-degree-rule` |
| directing-masterclass/directing-activity-vs-action | 这场戏的背景交代很多，但都是通过角色对话讲出来的，算不算有戏剧结果？ | `dialogue-deep-staging`, `scene-transition-loyalty-transfer`, `dialogue-busy-hands-no-eye-contact` |
| directing-masterclass/directing-activity-vs-action | 我写了一段角色独自在房间里踱步的场景，氛围很好但没有对话，这算活动还是动作？ | `scene-transition-loyalty-transfer`, `dialogue-busy-hands-no-eye-contact`, `cinematography-180-degree-rule` |
| directing-masterclass/directing-ambiguity-diagnosis | 我写的这个场景有两种完全不同的解读，但每种都很有力，这样算成功还是失败？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| directing-masterclass/directing-ambiguity-diagnosis | 我的作品在西方观众看来是'好的多义'，但东方观众觉得'看不懂'，这是文化差异还是作品问题？ | `directing-ambiguity-diagnosis`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| directing-masterclass/directing-coincidence-trouble | 我的故事是喜剧，用巧合制造误会和笑料，需要遵守'巧合只能制造麻烦'的规则吗？ | `directing-coincidence-trouble`, `directing-protagonist-endangered`, `cinematography-180-degree-rule` |
| directing-masterclass/directing-coincidence-trouble | 故事早期我用了一个巧合让角色来到这个小镇，这个算'解决困难'吗？ | `directing-coincidence-trouble`, `directing-protagonist-endangered`, `scene-transition-loyalty-transfer` |
| directing-masterclass/directing-contrast-emphasis | 我设计了一个产品界面，所有功能对用户都同样重要，需要做对比强调吗？ | `scene-transition-binary-opposition`, `scene-transition-weather-contrast`, `shot-still-vs-motion-decision` |
| directing-masterclass/directing-contrast-emphasis | 我想让整个画面都很丰富很满，不想突出任何一个元素，这合理吗？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| directing-masterclass/directing-credible-impossible | 我写的是魔幻现实主义，故意让现实和超现实混在一起，也要遵守自洽性吗？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| directing-masterclass/directing-credible-impossible | 观众说我的故事逻辑自洽但还是觉得'假'，这和可信度是一回事吗？ | `directing-credible-impossible`, `directing-protagonist-endangered`, `cinematography-180-degree-rule` |
| directing-masterclass/directing-dramatic-irony | 我的故事的魅力在于让观众和主角一起发现真相，如果提前告诉观众信息会不会破坏这种乐趣？ | `directing-protagonist-endangered`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| directing-masterclass/directing-dramatic-irony | 我想在故事中用伏笔来暗示结局，这和戏剧反讽有什么区别？ | `directing-protagonist-endangered`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| directing-masterclass/directing-end-before-begin | 我想写一个系列小说，每一本都有独立的结尾，但整个系列有一个大结局，该怎么处理？ | `color-grading-contrast-saturation`, `directing-story-framework`, `cinematography-180-degree-rule` |
| directing-masterclass/directing-end-before-begin | 我已经确定了结尾但写着写着发现故事走向另一个方向了，该坚持原来的结尾还是跟着感觉走？ | `directing-story-framework`, `directing-protagonist-endangered`, `cinematography-180-degree-rule` |
| directing-masterclass/directing-idea-generation | 我想到了一个创意但不确定好不好，你能帮我评估一下吗？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| directing-masterclass/directing-idea-generation | 我团队的编剧室总是在一起头脑风暴，但产出的东西很平庸，有什么改进方法？ | `directing-story-framework`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| directing-masterclass/directing-invisible-witness | 我想在一场戏里让观众同时关注两个角色，而不是偏向其中一个，这怎么做？ | `scene-transition-loyalty-transfer`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| directing-masterclass/directing-invisible-witness | 我写的是一场纯对白的对手戏，没有动作，镜头设计上有什么要注意的？ | `directing-odets-rewrite`, `shot-camera-choreography`, `cinematography-180-degree-rule` |
| directing-masterclass/directing-odets-rewrite | 这场戏里反派和主角在对峙，但反派好像没什么筹码，感觉冲突不够强，怎么改？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| directing-masterclass/directing-odets-rewrite | 我把一个二人对话改成了三人场景，但感觉更乱了而不是更有层次，怎么回事？ | `dialogue-busy-hands-no-eye-contact`, `shot-design-dialogue-staging`, `cinematography-180-degree-rule` |
| directing-masterclass/directing-protagonist-endangered | 我的故事里主角和另一个角色都很濒危，但我想以主角为叙事中心，这样行吗？ | `scene-transition-binary-opposition`, `directing-protagonist-endangered`, `scene-transition-loyalty-transfer` |
| directing-masterclass/directing-protagonist-endangered | 我的主角面临的是内心困境而非外在威胁，这种'濒危'算不算？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| directing-masterclass/directing-reaction-over-action | 我在长镜头里完成了一场对话，没有剪辑点，怎么表现'反应'？ | `scene-transition-caboose-diagnosis`, `dialogue-busy-hands-no-eye-contact`, `color-grading-shot-matching` |
| directing-masterclass/directing-reaction-over-action | 这场戏的反应镜头拍了很多但剪在一起感觉拖沓，是不是反应太多也有问题？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| directing-masterclass/directing-scene-necessity | 这场戏的氛围营造得很好，删掉后故事也能理解但氛围会变差，该留吗？ | `directing-protagonist-endangered`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| directing-masterclass/directing-scene-necessity | 这场戏在因果链上可有可无但角色塑造很好，能丰富人物形象，该删吗？ | `dialogue-focal-character-temperament`, `directing-coincidence-trouble`, `directing-scene-necessity` |
| directing-masterclass/directing-story-framework | 我想分析一部已有电影的结构，看它的故事框架有没有缺失，你觉得该从哪入手？ | `directing-protagonist-endangered`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| directing-masterclass/directing-story-framework | 我写了一段散文，但感觉叙事不够有张力，能用故事框架帮我理一理吗？ | `scene-transition-binary-opposition`, `directing-protagonist-endangered`, `shot-dual-camera-tension` |
| directing-masterclass/directing-tension-formula | 这场戏里有期待也有不确定，但观众还是觉得无聊，是不是公式有问题？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| directing-masterclass/directing-tension-formula | 我的故事张力一直很强，但观众说看得太累了，是不是张力太密集了？ | `directing-protagonist-endangered`, `shot-dual-camera-tension`, `cinematography-180-degree-rule` |
| master-shots-v1/shot-camera-choreography | 我要拍一场打斗戏，演员要同时做动作摄影机也要动，但我不想事先设计得太死板，想保留一些即兴感，怎么平衡？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| master-shots-v1/shot-distract-and-scare | 我想在喜剧片里突然插入一个恐怖元素吓观众一跳，但不想破坏喜剧氛围，怎么平衡？ | `shot-distract-and-scare`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| master-shots-v1/shot-dual-camera-tension | 我要拍一个角色从强势变弱势的逆转过程，只有一台摄影机，能实现类似的运动对比效果吗？ | `shot-still-vs-motion-decision`, `scene-transition-binary-opposition`, `scene-transition-loyalty-transfer` |
| master-shots-v1/shot-equal-length-rhythm | 我想在爱情片中用等长镜头制造一种平静感，但不打算打破它，就让整场戏保持等长节奏，可以吗？ | `shot-equal-length-rhythm`, `scene-transition-seamless-pause`, `scene-transition-low-point-no-plot` |
| master-shots-v1/shot-still-vs-motion-decision | 角色决定不说出秘密，没有明显的动作，怎么用镜头表现这种消极决定？ | `scene-transition-loyalty-transfer`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| master-shots-v1/shot-telephoto-compression | 我想拍一场追逐戏，同时需要让追踪者显得更近，也需要让两个角色的运动状态形成对比，该怎么设计？ | `msv3-speed-conveyance`, `shot-still-vs-motion-decision`, `scene-transition-binary-opposition` |
| master-shots-v2/dialogue-camera-follow-identity | 反派电影里我想让观众害怕反派，该跟谁拍？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| master-shots-v2/dialogue-closeup-timing | 电话场景里角色接到了坏消息，要不要切到他的特写看反应？ | `dialogue-closeup-timing`, `dialogue-telephoto-claustrophobia`, `msv3-body-performance` |
| master-shots-v2/dialogue-distance-collapse-arc | 恐怖片里摄影机慢慢推近一个角色的脸，这是在制造恐惧还是情感深入？ | `shot-distract-and-scare`, `scene-transition-loyalty-transfer`, `cinematography-180-degree-rule` |
| master-shots-v2/dialogue-gaze-mapping | 悬疑片里一个杀手藏在房间里，主角不知道他在，这时候怎么安排其他角色的目光方向？ | `shot-distract-and-scare`, `scene-transition-loyalty-transfer`, `cinematography-180-degree-rule` |
| scene-transitions/scene-transition-binary-opposition | 我想拍一部只有一个场景的短片，全部在一个房间里完成，有没有办法制造场景转换的感觉？ | `scene-transition-binary-opposition`, `scene-transition-synch-node`, `scene-transition-caboose-diagnosis` |
| scene-transitions/scene-transition-caboose-diagnosis | 这个场景不推进情节但提供了很好的氛围，要不要删？ | `scene-transition-caboose-diagnosis`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| scene-transitions/scene-transition-four-function-diagnosis | 我在做一个商业广告，15秒内有5个场景切换，每个切换应该有什么功能？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| scene-transitions/scene-transition-low-point-no-plot | 我的恐怖片全程都需要保持紧张感，是不是就不需要低潮了？ | `shot-distract-and-scare`, `scene-transition-low-point-no-plot`, `cinematography-180-degree-rule` |
| scene-transitions/scene-transition-loyalty-transfer | 反派也能成为观众同情的对象吗？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| scene-transitions/scene-transition-music-quadrant | 我的电影全程没有配乐，只有环境音。这种情况下场景转换怎么处理音频？ | `scene-transition-music-quadrant`, `color-grading-contrast-saturation`, `scene-transition-binary-opposition` |
| scene-transitions/scene-transition-seamless-pause | 我的纪录片也需要这种无间歇欺骗吗？ | `scene-transition-seamless-pause`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| scene-transitions/scene-transition-synch-node | 我的多线叙事中故事线永远不交汇，还需要同步节点吗？ | `scene-transition-synch-node`, `scene-transition-binary-opposition`, `directing-protagonist-endangered` |
| scene-transitions/scene-transition-weather-contrast | 我的灾难片里天气就是主角，这个方法还适用吗？ | `scene-transition-weather-contrast`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| shot-design/shot-design-angle-context | 恐怖片的低角度有什么特殊效果？ | `shot-distract-and-scare`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| shot-design/shot-design-axis-of-action | 我想故意打破180度规则制造混乱感 | `shot-design-axis-of-action`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| shot-design/shot-design-continuity-composition | 韦斯·安德森的对称构图怎么做到的？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| shot-design/shot-design-dialogue-staging | 五个人在餐桌旁对话，怎么调度？ | `dialogue-busy-hands-no-eye-contact`, `shot-design-dialogue-staging`, `cinematography-180-degree-rule` |
| shot-design/shot-design-dramatic-range | 动作片的摄影机位置怎么选？ | `msv3-power-distance`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| shot-design/shot-design-pov-spectrum | 纪录片需要控制观众认同吗？ | `scene-transition-loyalty-transfer`, `shot-design-pov-spectrum`, `cinematography-180-degree-rule` |
| shot-design/shot-design-sightline-cut | 恐怖片怎么用视线制造不安？ | `shot-distract-and-scare`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| shot-design/shot-design-storyboard-rapid | 我需要给客户展示精美的分镜稿 | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| sound-design/sound-design-auditory-hierarchy | 纪录片中旁白和同期声冲突，优先级怎么判断？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| sound-design/sound-design-consistency | 续集电影要不要沿用前作的声音设计，还是重新设计？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| sound-design/sound-design-contrast-drama | 音乐录影带中全程高能量，还需要动态对比吗？ | `scene-transition-binary-opposition`, `scene-transition-music-quadrant`, `scene-transition-weather-contrast` |
| sound-design/sound-design-diegetic-taxonomy | 打破第四面墙的电影中，角色直接对观众说话算 diegetic 还是 non-diegetic？ | `sound-design-diegetic-taxonomy`, `scene-transition-loyalty-transfer`, `dialogue-busy-hands-no-eye-contact` |
| sound-design/sound-design-energy-model | 动画片中夸张的声音设计还需要遵循能量模型的真实性原则吗？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| sound-design/sound-design-entrainment | 恐怖片中用次声波（infrasound）引发不安感，这属于 entrainment 吗？ | `sound-design-entrainment`, `shot-distract-and-scare`, `sound-design-diegetic-taxonomy` |
| sound-design/sound-design-expectation | 观众已经习惯了jump scare套路，还有没有新的声音惊吓手法？ | `shot-distract-and-scare`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| sound-design/sound-design-less-is-more | 科幻大片的混录中怎么做到'少即是多'而不显得廉价？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| sound-design/sound-design-listening-modes | ASMR内容中观众的倾听模式和电影中有什么本质区别？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| sound-design/sound-design-music-story-parallel | 纪录片用现成音乐而不是原创配乐，怎么和叙事建立平行关系？ | `scene-transition-music-quadrant`, `scene-transition-binary-opposition`, `cinematography-180-degree-rule` |
| sound-design/sound-design-size-control | 微观纪录片中细菌的'声音'完全是想象的，大小感怎么建立？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| sound-design/sound-design-sonata-drama | 非线性叙事的电影中声音弧线怎么设计？还能用奏鸣曲式吗？ | `scene-transition-binary-opposition`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| sound-design/sound-design-sync-illusion | 动画片的声音同步和实拍有什么本质区别？ | `cinematography-180-degree-rule`, `cinematography-back-lighting`, `cinematography-hard-soft-light` |
| story-design/story-design-beat-sheet | 我想写一个非线性叙事的故事，BS2还适用吗？ | `scene-transition-binary-opposition`, `directing-protagonist-endangered`, `cinematography-180-degree-rule` |
| story-design/story-design-five-step-finale | 我想写一个开放式结局，五步法还适用吗？ | `directing-ambiguity-diagnosis`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| story-design/story-design-genres | 我的故事既有怪物追杀又有爱情线，应该怎么分类？ | `directing-protagonist-endangered`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| story-design/story-design-logline | 我的故事太复杂了，一句话说不清楚怎么办？ | `directing-protagonist-endangered`, `cinematography-180-degree-rule`, `cinematography-back-lighting` |
| story-design/story-design-midpoint | 散文式故事需要Midpoint吗？ | `story-design-midpoint`, `directing-protagonist-endangered`, `cinematography-three-point-lighting` |
| story-design/story-design-save-the-cat | 我的主角是反英雄，需要Save the Cat吗？ | `story-design-save-the-cat`, `sound-design-diegetic-taxonomy`, `sound-design-consistency` |
| story-design/story-design-shard-of-glass | 动作片也需要Shard of Glass吗？ | `story-design-shard-of-glass`, `cinematography-hard-soft-light`, `shot-design-axis-of-action` |
| story-design/story-design-theme-b-story | 我的故事没有B Story，主题怎么表达？ | `story-design-midpoint`, `story-design-theme-b-story`, `story-design-genres` |

## Per-Skill Pass Rate

| Book | Skill | ST | SNT | Status |
|------|-------|----|----|--------|
| cinematography-brown | cinematography-180-degree-rule | 3/3 | 2/2 | PASS |
| cinematography-brown | cinematography-back-lighting | 3/3 | 3/3 | PASS |
| cinematography-brown | cinematography-hard-soft-light | 3/3 | 3/3 | PASS |
| cinematography-brown | cinematography-light-direction-mood | 3/3 | 3/3 | PASS |
| cinematography-brown | cinematography-master-scene | 2/3 | 3/3 | **FAIL** |
| cinematography-brown | cinematography-three-point-lighting | 3/3 | 3/3 | PASS |
| cinematography-brown | cinematography-zone-system | 3/3 | 3/3 | PASS |
| color-grading | color-grading-color-temperature | 1/4 | 3/3 | **FAIL** |
| color-grading | color-grading-contrast-before-color | 3/4 | 3/3 | **FAIL** |
| color-grading | color-grading-contrast-saturation | 4/4 | 3/3 | PASS |
| color-grading | color-grading-filter-nonlinear | 1/4 | 3/3 | **FAIL** |
| color-grading | color-grading-log-workflow | 4/4 | 2/3 | **FAIL** |
| color-grading | color-grading-look-development | 2/4 | 3/3 | **FAIL** |
| color-grading | color-grading-memory-colors | 0/4 | 3/3 | **FAIL** |
| color-grading | color-grading-overexposure-recovery | 0/4 | 3/3 | **FAIL** |
| color-grading | color-grading-primary-workflow | 2/4 | 3/3 | **FAIL** |
| color-grading | color-grading-shot-matching | 1/4 | 3/3 | **FAIL** |
| color-grading | color-grading-skin-tone-vectorscope | 4/4 | 2/3 | **FAIL** |
| master-shots-v2 | dialogue-barrier-narrative | - | - | PASS |
| master-shots-v2 | dialogue-busy-hands-no-eye-contact | - | - | PASS |
| master-shots-v2 | dialogue-camera-follow-identity | 0/3 | 1/1 | **FAIL** |
| master-shots-v2 | dialogue-camera-height-stance | - | - | PASS |
| master-shots-v2 | dialogue-closeup-timing | 1/2 | 2/2 | **FAIL** |
| master-shots-v2 | dialogue-deep-staging | - | - | PASS |
| master-shots-v2 | dialogue-delayed-reveal | - | - | PASS |
| master-shots-v2 | dialogue-distance-collapse-arc | 0/3 | 1/1 | **FAIL** |
| master-shots-v2 | dialogue-focal-character-temperament | - | - | PASS |
| master-shots-v2 | dialogue-focal-progression | - | - | PASS |
| master-shots-v2 | dialogue-gaze-mapping | 0/3 | 1/1 | **FAIL** |
| master-shots-v2 | dialogue-position-swap | - | - | PASS |
| master-shots-v2 | dialogue-task-overload | - | - | PASS |
| master-shots-v2 | dialogue-telephoto-claustrophobia | - | - | PASS |
| directing-masterclass | directing-activity-vs-action | 0/5 | 3/3 | **FAIL** |
| directing-masterclass | directing-ambiguity-diagnosis | 2/5 | 3/3 | **FAIL** |
| directing-masterclass | directing-coincidence-trouble | 2/5 | 1/3 | **FAIL** |
| directing-masterclass | directing-contrast-emphasis | 0/5 | 3/3 | **FAIL** |
| directing-masterclass | directing-credible-impossible | 1/5 | 3/3 | **FAIL** |
| directing-masterclass | directing-dramatic-irony | 1/5 | 3/3 | **FAIL** |
| directing-masterclass | directing-end-before-begin | 1/5 | 3/3 | **FAIL** |
| directing-masterclass | directing-idea-generation | 0/5 | 3/3 | **FAIL** |
| directing-masterclass | directing-invisible-witness | 0/5 | 3/3 | **FAIL** |
| directing-masterclass | directing-odets-rewrite | 0/5 | 3/3 | **FAIL** |
| directing-masterclass | directing-protagonist-endangered | 2/5 | 3/3 | **FAIL** |
| directing-masterclass | directing-reaction-over-action | 1/5 | 3/3 | **FAIL** |
| directing-masterclass | directing-scene-necessity | 1/5 | 3/3 | **FAIL** |
| directing-masterclass | directing-story-framework | 1/5 | 3/3 | **FAIL** |
| directing-masterclass | directing-tension-formula | 0/5 | 3/3 | **FAIL** |
| master-shots-v3 | msv3-body-performance | 3/5 | - | **FAIL** |
| master-shots-v3 | msv3-lens-emotion-mapping | 0/5 | - | **FAIL** |
| master-shots-v3 | msv3-power-distance | 2/5 | - | **FAIL** |
| master-shots-v3 | msv3-speed-conveyance | 4/5 | - | **FAIL** |
| master-shots-v3 | msv3-symbolic-staging | 2/5 | - | **FAIL** |
| master-shots-v3 | msv3-unexpected-reveal | 5/5 | - | PASS |
| scene-transitions | scene-transition-binary-opposition | 1/3 | 2/2 | **FAIL** |
| scene-transitions | scene-transition-caboose-diagnosis | 1/2 | 2/2 | **FAIL** |
| scene-transitions | scene-transition-four-function-diagnosis | 1/3 | 2/2 | **FAIL** |
| scene-transitions | scene-transition-low-point-no-plot | 1/3 | 2/2 | **FAIL** |
| scene-transitions | scene-transition-loyalty-transfer | 1/2 | 1/2 | **FAIL** |
| scene-transitions | scene-transition-music-quadrant | 2/3 | 1/2 | **FAIL** |
| scene-transitions | scene-transition-seamless-pause | 0/2 | 1/2 | **FAIL** |
| scene-transitions | scene-transition-synch-node | 1/2 | 2/2 | **FAIL** |
| scene-transitions | scene-transition-weather-contrast | 1/2 | 1/2 | **FAIL** |
| master-shots-v1 | shot-camera-choreography | 2/4 | 2/2 | **FAIL** |
| shot-design | shot-design-angle-context | 2/3 | 2/2 | **FAIL** |
| shot-design | shot-design-axis-of-action | 1/3 | 2/2 | **FAIL** |
| shot-design | shot-design-continuity-composition | 1/3 | 2/2 | **FAIL** |
| shot-design | shot-design-dialogue-staging | 1/3 | 2/2 | **FAIL** |
| shot-design | shot-design-dramatic-range | 0/3 | 2/2 | **FAIL** |
| shot-design | shot-design-pov-spectrum | 1/3 | 2/2 | **FAIL** |
| shot-design | shot-design-sightline-cut | 1/3 | 2/2 | **FAIL** |
| shot-design | shot-design-storyboard-rapid | 1/3 | 2/2 | **FAIL** |
| master-shots-v1 | shot-distract-and-scare | 1/3 | 1/2 | **FAIL** |
| master-shots-v1 | shot-dual-camera-tension | 2/3 | 1/2 | **FAIL** |
| master-shots-v1 | shot-equal-length-rhythm | 1/3 | 2/2 | **FAIL** |
| master-shots-v1 | shot-still-vs-motion-decision | 2/3 | 2/2 | **FAIL** |
| master-shots-v1 | shot-telephoto-compression | 0/4 | 2/2 | **FAIL** |
| sound-design | sound-design-auditory-hierarchy | 0/4 | 3/3 | **FAIL** |
| sound-design | sound-design-consistency | 0/4 | 3/3 | **FAIL** |
| sound-design | sound-design-contrast-drama | 0/4 | 3/3 | **FAIL** |
| sound-design | sound-design-diegetic-taxonomy | 1/4 | 3/3 | **FAIL** |
| sound-design | sound-design-energy-model | 0/4 | 3/3 | **FAIL** |
| sound-design | sound-design-entrainment | 0/4 | 3/3 | **FAIL** |
| sound-design | sound-design-expectation | 0/4 | 3/3 | **FAIL** |
| sound-design | sound-design-less-is-more | 0/4 | 3/3 | **FAIL** |
| sound-design | sound-design-listening-modes | 0/4 | 3/3 | **FAIL** |
| sound-design | sound-design-music-story-parallel | 0/4 | 3/3 | **FAIL** |
| sound-design | sound-design-size-control | 0/4 | 3/3 | **FAIL** |
| sound-design | sound-design-sonata-drama | 0/4 | 3/3 | **FAIL** |
| sound-design | sound-design-sync-illusion | 0/4 | 3/3 | **FAIL** |
| story-design | story-design-beat-sheet | 0/3 | 2/2 | **FAIL** |
| story-design | story-design-five-step-finale | 2/3 | 2/2 | **FAIL** |
| story-design | story-design-genres | 0/3 | 2/2 | **FAIL** |
| story-design | story-design-logline | 1/3 | 2/2 | **FAIL** |
| story-design | story-design-midpoint | 2/3 | 2/2 | **FAIL** |
| story-design | story-design-save-the-cat | 1/3 | 2/2 | **FAIL** |
| story-design | story-design-shard-of-glass | 2/3 | 2/2 | **FAIL** |
| story-design | story-design-theme-b-story | 1/3 | 2/2 | **FAIL** |

## Root Cause Analysis

### Failure Pattern Summary

- **Total should_trigger failures**: 217
  - Prompts with <2 skill-specific keyword hits (possibly too generic): 217
  - Prompts routed to a different book's skill: 195
- **Total should_not_trigger failures**: 10

### Improvement Recommendations

1. **test-prompts quality**: Prompts with few skill-specific keywords need rewriting
   to include domain terms that uniquely identify the target skill.
2. **Skill description/tags**: Skills that frequently lose to neighbors need more
   distinctive tags or a clearer description boundary.
3. **Router algorithm**: Current keyword-overlap is a baseline. Consider adding
   negative keywords (from should_not_trigger patterns) and weighted tag matching.
