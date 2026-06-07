# Counter-Example Extractor — 大师镜头 v1 (Master Shots Vol. 1)
# 阶段 1 产出：失败模式 / 反例 / 警告 / 陷阱

- id: ce01
  title: 选错镜头导致特效完全失效
  type: counter-example
  source_chapter: 第1章 §1.1
  source_quote: |
    "很多人选错了镜头。要是那样的话，结果就可笑了，本来借位产生的错觉也就完全没了效果。"
  failure_mode: |
    用广角镜头拍摄打斗借位——广角会放大空间距离，让拳头和头部之间的"空气"暴露无遗，观众一眼看穿是假打。
  mechanism: |
    广角镜头夸大空间感，物体间的距离被放大。长焦镜头压缩空间感，物体间的距离被缩短。选错焦距会逆转想要的视觉效果。
  warning_signs:
    - 拍摄时只关注构图不考虑焦距
    - 把镜头选择完全交给摄影导演
    - 没有在拍摄前用不同焦距试拍
  bound_to:
    - "长焦特效压缩空间框架"
    - "镜头选择决策框架（焦距→效果映射）"
  tags: [counter-example, lens-choice, long-lens-trick, failure]

- id: ce02
  title: 把两人当整体拍摄失去运动感
  type: counter-example
  source_chapter: 第1章 §1.3
  source_quote: |
    "很多人就会把两个人当做一个整体来处理——这就错了，因为把两个人作为整体拍摄，会失去运动的感觉。"
  failure_mode: |
    在打斗/扭打场景中，摄影机同时跟踪两个纠缠在一起的演员，结果画面看起来像一个整体在移动，失去了动感和力量对比。
  mechanism: |
    当两个运动速度不同的人被当作整体处理时，相对运动被抵消。只跟踪一个人才能保留运动差异和紧张感。
  warning_signs:
    - 画面中两个演员都清晰但缺乏动感
    - 观众无法分辨谁在追谁
    - 打斗看起来像"一起散步"
  bound_to:
    - "打斗中只跟踪一个演员"
  tags: [counter-example, fight-scene, tracking, loss-of-dynamism]

- id: ce03
  title: 摄影机离演员太近导致镜头被占满
  type: counter-example
  source_chapter: 第1章 §1.2
  source_quote: |
    "摄影机也不能离演员太近，如果靠得太近的话，受害者就会占了大部分镜头。"
  failure_mode: |
    拍摄"一记重拳"时摄影机离受害者太近，受害者占满镜头，观众觉得自己是受害者，无法感受到出拳者的畅快淋漓。
  mechanism: |
    摄影机距离影响观众认同的角色。离谁近，观众就认同谁。如果想让观众认同出拳者，摄影机就不能太靠近受害者。
  warning_signs:
    - 受害者占满画面
    - 观众视角被迫成为"挨打者"
    - 无法感受到英雄出拳的快感
  bound_to:
    - "视角高度→情感认同框架"
  tags: [counter-example, camera-distance, identification, fight-scene]

- id: ce04
  title: 为移动摄影机而乱动摄影机
  type: counter-example
  source_chapter: 前言
  source_quote: |
    "千万不要为了移动摄影机而乱动摄影机，但也不要因为懒得思考，就一直保持摄影机不动。"
  failure_mode: |
    两种极端：(1) 摄影机不停移动但没有叙事目的，观众感到眩晕和困惑；(2) 摄影机完全不动，画面沉闷无趣。
  mechanism: |
    移动本身不是目的，叙事才是。没有目的的移动分散观众注意力；缺乏移动则无法引导观众注意力。
  warning_signs:
    - 每个镜头都有摄影机运动
    - 运动没有配合演员的行动或情绪变化
    - 观众感到头晕而非沉浸
  bound_to:
    - "不要为移动而移动摄影机"
  tags: [counter-example, camera-movement, purposeless, excessive]

- id: ce05
  title: 迎着演员视线推近导致压迫感
  type: counter-example
  source_chapter: 第5章 §5.1
  source_quote: |
    "演员的视线要是太靠近镜头，反而会给人一种压迫感，而且摄影机推近的时候会挡住演员的视线。"
  failure_mode: |
    推近拍摄时让演员直视镜头，结果不是"进入角色内心"而是"被角色逼视"的压迫感。同时摄影机移动会挡住演员的视线方向。
  mechanism: |
    观众本能地将"直视"解读为"威胁"或"挑战"。适度的偏移才能产生亲密感，正对则产生对抗感。
  warning_signs:
    - 观众感到被角色"盯"着不舒服
    - 演员在推近过程中眼神游移
    - 情感效果从"亲密"变成了"对峙"
  bound_to:
    - "演员视线太靠近镜头会产生压迫感"
  tags: [counter-example, push-in, eye-line, oppressive]

- id: ce06
  title: 镜头还在移动时场景结束
  type: counter-example
  source_chapter: 第10章 §10.1
  source_quote: |
    "如果镜头还在向前推，场景却结束了，这时的效果就有点不了了之的感觉。"
  failure_mode: |
    推近拍摄对话场景时，摄影机还没停下场景就结束了，观众感觉"话没说完"或"戛然而止"。
  mechanism: |
    推近是一种"承诺"——告诉观众"重要的事情要来了"。如果承诺没有兑现（摄影机还在动但场景结束了），观众会感到失望。
  warning_signs:
    - 场景结尾感觉"不了了之"
    - 推近的速度和对话的节奏不匹配
    - 剪辑时发现推近结束后只能用一个角度
  bound_to:
    - "推近时保持演员一只眼睛在画面中位置不变"
  tags: [counter-example, push-in, timing, premature-ending]

- id: ce07
  title: 分散注意力的手段太生硬
  type: counter-example
  source_chapter: 第7章 §7.2
  source_quote: |
    "千万不要为了转移观众的注意力而生硬地设计一些情节。因为情节越是合理，最终吓人的效果就越强烈。"
  failure_mode: |
    为了让观众放松警惕，硬编一个不合理的理由让角色看向别处。观众会感到"这不对劲"，反而更警觉而非放松。
  mechanism: |
    观众对"为什么他突然看那边？"非常敏感。只有合理的、符合角色动机的注意力转移才能成功骗过观众。
  warning_signs:
    - 角色的行为不符合当前情境
    - 观众感到"导演在故意引导"
    - 最终的惊吓效果大打折扣
  bound_to:
    - "分散注意力-打破预期框架"
  tags: [counter-example, misdirection, forced-plot, audience-awareness]

- id: ce08
  title: 正反打对话的沉闷陷阱
  type: counter-example
  source_chapter: 第10章 §10.1
  source_quote: |
    "一般的对话场景中，取景时会让两名演员面对面坐着，后期剪辑时再把不同角度拍到的画面组合到一起。这样拍没什么大错，就是有些沉闷。"
  failure_mode: |
    所有对话场景都用标准的正反打（过肩镜头）拍摄，结果画面单调沉闷，对话的节奏完全由后期剪辑决定而非演员表演。
  mechanism: |
    正反打是"安全"但"无力"的选择。它把对话的节奏控制权从演员手中夺走，交给剪辑师，削弱了表演的自然感。
  warning_signs:
    - 每场对话都用相同的拍摄方式
    - 对话看起来像"乒乓球"——来回切换
    - 演员表演的细微节奏被剪辑打断
  bound_to:
    - "连贯镜头优于剪辑框架"
  tags: [counter-example, dialogue, over-the-shoulder, monotonous]

- id: ce09
  title: 肥皂剧式的分享镜头
  type: counter-example
  source_chapter: 第10章 §10.3
  source_quote: |
    "如果设计得不好，你也可能拍出肥皂剧的感觉：一名演员面对着镜头，另一名演员站在他身后对着他的后脑勺说话。"
  failure_mode: |
    试图让两个演员同时出现在画面中，但角度设计不当，结果一人正面一人背面，看起来像肥皂剧。
  mechanism: |
    肥皂剧常用这种角度是因为制作简单快速，但它很不自然——现实中很少有人对着别人的后脑勺说话。两个演员间必须有角度。
  warning_signs:
    - 一名演员完全背对镜头
    - 两人之间没有视线交流
    - 画面看起来像"前方播报"
  bound_to:
    - "连贯镜头优于剪辑框架"
  tags: [counter-example, dialogue, soap-opera, bad-staging]

- id: ce10
  title: 演员倒地太快显得滑稽
  type: counter-example
  source_chapter: 第12章 §12.4
  source_quote: |
    "先躺下的那名演员不能倒得太快，不然效果会很滑稽。"
  failure_mode: |
    拍摄激情场景中"浪漫躺下"时，演员倒得太快，看起来像"摔倒"而非"浪漫地倒下"。或者两人不是同时倒下，也显得滑稽。
  mechanism: |
    物理动作的速度与情感预期不匹配时，观众会产生"不协调"感，浪漫变成了喜剧。
  warning_signs:
    - 演员倒下的速度过快
    - 两名演员不是同时进入镜头
    - 观众感到"好笑"而非"浪漫"
  bound_to:
    - "不管思想多深刻，没行动再好的戏也出不来"
  tags: [counter-example, romance, timing, comical]

- id: ce11
  title: 背景太清晰破坏"拉开帷幕"效果
  type: counter-example
  source_chapter: 第6章 §6.2
  source_quote: |
    "如果你把背景拍得很清晰，最后他的现身就会显得很滑稽。"
  failure_mode: |
    在"拉开帷幕"技法中，隐藏角色在背景中过于清晰，观众提前发现，现身时失去惊喜效果，甚至显得滑稽。
  mechanism: |
    观众的注意力被清晰的背景吸引，提前发现了隐藏角色。当"帷幕拉开"时，观众已经知道了，效果大打折扣。
  warning_signs:
    - 背景中的隐藏角色过于明显
    - 观众在"帷幕拉开"前就发现了
    - 现身的时刻没有惊喜感
  bound_to:
    - "障碍物渐现登场框架"
  tags: [counter-example, reveal, background-focus, premature-discovery]

- id: ce12
  title: 演员看错反射方向
  type: counter-example
  source_chapter: 第8章 §8.4
  source_quote: |
    "如果演员看得不是地方，观众就能感觉出哪里不对劲。"
  failure_mode: |
    利用反射同时表现两个空间时，演员没有真正看着反射来源的方向，观众能本能地感觉到"眼神不对"。
  mechanism: |
    人眼对视线方向极其敏感。即使观众说不清哪里不对，错误的视线方向会产生"不真实"的直觉感受。
  warning_signs:
    - 演员的目光与反射面的角度不匹配
    - 观众感到"有什么不对劲但说不出来"
    - 反射的画面看起来"假"
  bound_to:
    - "反射面越大摄影机越好控制"
  tags: [counter-example, reflection, eye-line, uncanny]

- id: ce13
  title: 没有理由的演员移动
  type: counter-example
  source_chapter: 第8章 §8.2
  source_quote: |
    "千万不要让演员乱逛。"
  failure_mode: |
    为了让摄影机有理由移动，安排演员在场景中无目的地走来走去。观众会感到不自然，角色行为缺乏动机。
  mechanism: |
    每个演员的移动都必须有叙事理由（去拿文件、要去另一个房间等）。无理由的移动会让观众意识到"这是在拍电影"。
  warning_signs:
    - 演员在场景中走来走去但没有目的
    - 观众感到"他们在走位而非行动"
    - 摄影机的移动看起来是"为了移动而移动"
  bound_to:
    - "不要为移动而移动摄影机"
  tags: [counter-example, blocking, unmotivated-movement, artificial]

- id: ce14
  title: 窗外的脸被提前猜到
  type: counter-example
  source_chapter: 第7章 §7.9
  source_quote: |
    "只要我们看到空空的、黑洞洞的窗户，我们就条件反射般地知道那儿一定会出现一张脸。"
  failure_mode: |
    拍摄窗外惊现恐怖面孔时，如果窗户一开始就空荡荡地出现在画面中，观众立刻猜到"那里会出现脸"，惊吓效果全无。
  mechanism: |
    恐怖片的套路已经被观众内化。空窗户=即将出现脸，这个公式观众太熟悉了。必须分散注意力才能打破这个预期。
  warning_signs:
    - 画面中有空的、黑暗的窗户
    - 观众的目光一直在窗户上
    - 当脸出现时观众"早就知道了"
  bound_to:
    - "分散注意力-打破预期框架"
  tags: [counter-example, horror, window, predictable]

- id: ce15
  title: 演员动作太大抢镜（车内场景）
  type: counter-example
  source_chapter: 第9章 §9.4
  source_quote: |
    "记得要提醒演员动作不要太大，不然就会很容易拍到车门或是车底座。"
  failure_mode: |
    在车内静止场景中，演员动作幅度太大，拍到车门或车底座，分散观众注意力，破坏"和演员一起坐在车里"的沉浸感。
  mechanism: |
    车内空间狭小，任何多余动作都会暴露车辆结构细节。观众的注意力从对话转移到"车的构造"上。
  warning_signs:
    - 画面中出现车门、车底座等结构
    - 演员的动作显得不自然地大
    - 观众注意力从对话转移到环境
  bound_to:
    - "连贯镜头优于剪辑框架"
  tags: [counter-example, car-scene, movement, distracting]

- id: ce16
  title: 演员一看到信就停下来——效果全无
  type: counter-example
  source_chapter: 第8章 §8.5
  source_quote: |
    "如果她一看到信就停下来了，整个镜头就会效果全无。"
  failure_mode: |
    在"停下脚步"镜头中，演员收到物体后立即停下，缺乏延迟，镜头缺乏戏剧张力。
  mechanism: |
    延迟产生张力。演员忽视物体继续前行一段距离后再停下，产生"命运般的吸引力"效果。立即停下则只是"看到了东西"。
  warning_signs:
    - 演员看到物体后立刻停下
    - 镜头缺乏"神秘力量"的感觉
    - 观众没有感受到"注定要收到"的感觉
  bound_to:
    - "演员一开始需要忽视才能制造'停下脚步'的效果"
  tags: [counter-example, timing, delayed-reaction, flat]

- id: ce17
  title: 后期剪辑无法弥补拍摄失误
  type: counter-example
  source_chapter: 结语
  source_quote: |
    "不少的导演认为，后期的剪辑能弥补所有的错，所以拍摄的技能就无关紧要了。事实证明他们错了。"
  failure_mode: |
    拍摄时不够用心，认为"后期可以修"。结果后期发现镜头设计有根本问题（角度错误、运动不配合、焦点丢失），无法通过剪辑补救。
  mechanism: |
    剪辑只能重组已有素材，不能创造不存在的画面。如果拍摄阶段没有拍到正确的角度、运动和时机，后期无能为力。
  warning_signs:
    - 拍摄时"先拍了再说"
    - 没有事先设计镜头
    - 后期发现素材不够用或角度不对
  bound_to:
    - "后期剪辑不能弥补拍摄的失误"
  tags: [counter-example, post-production, insufficient-planning, anti-fix]

- id: ce18
  title: 空旷走廊里放外星人反而无效
  type: counter-example
  source_chapter: 第7章 §7.1
  source_quote: |
    "如果你真的在走廊里布置点什么奇怪的东西，反而就不会有效果了。"
  failure_mode: |
    为了制造恐怖，在走廊尽头放一个怪物。结果观众看到了但主角没看到，反而觉得"没劲"。
  mechanism: |
    恐惧来自"和主角一起不知道会发现什么"。如果观众先于角色知道威胁，恐惧变成了"等待主角发现"的无聊过程。
  warning_signs:
    - 走廊/空旷空间中有明确的威胁物
    - 观众先于角色看到威胁
    - 观众感到"快点发现啊"而非"害怕"
  bound_to:
    - "看不见的追踪者比看得见的更吓人"
  tags: [counter-example, horror, empty-space, premature-reveal]

- id: ce19
  title: 重复使用同一吓人手法导致观众免疫
  type: counter-example
  source_chapter: 第7章 §7.2
  source_quote: |
    "这种方法也已经用得太多了，观众早已有了免疫力，一看就能猜到后面会发生什么事。"
  failure_mode: |
    先让微不足道的东西吓观众一下（油漆桶倒了），然后杀人魔跳出。这个套路太老，观众早就知道"假吓之后必有真吓"。
  mechanism: |
    观众会学习模式。一旦他们识别出"假惊吓→真惊吓"的套路，后续使用同一模式就完全失效。
  warning_signs:
    - 使用了"经典"的吓人套路
    - 观众在假惊吓后就猜到真惊吓
    - 惊吓效果逐次递减
  bound_to:
    - "分散注意力-打破预期框架"
  tags: [counter-example, horror, cliché, audience-immunity]

- id: ce20
  title: 摄影机停止时演员还在动——暴露摄影机存在
  type: counter-example
  source_chapter: 第5章 §5.5
  source_quote: |
    "如果演员已经停下来了摄影机还在后退，观众就会发现摄影机的存在。"
  failure_mode: |
    摄影机和演员的运动不同步：演员停了但摄影机还在动，或者反过来。观众突然意识到"有台摄影机在拍"，从沉浸中醒来。
  mechanism: |
    摄影机运动的"隐形"依赖于与演员运动的完美同步。任何不同步都会打破"第四面墙"。
  warning_signs:
    - 演员停了摄影机还在动
    - 摄影机停了演员还在动
    - 观众突然意识到摄影机的存在
  bound_to:
    - "编舞式镜头设计框架"
  tags: [counter-example, camera-actor-sync, fourth-wall, desynchronization]
