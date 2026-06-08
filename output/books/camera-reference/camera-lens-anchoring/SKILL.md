---
name: camera-lens-anchoring
description: |
  当用户需要为特定情绪/风格/场景选择专业影视摄影机+镜头组合、或需要在AI视频prompt中添加具体摄影机锚点时调用。
  核心 trigger：用户提到"用什么摄影机"、"什么镜头"、"电影感"、"摄影机型号"、"镜头选择"、"画质风格"、"胶片感"、"数字感"。
  不适用于：纯剪辑问题（用 shot-design）、纯调色问题（用 color-grading）、纯叙事问题（用 directing）。
source_book: 跨书综合 — cinematography-brown + color-grading + ai-shortfilm-prompts 方法论 + 行业实践
source_chapter: 综合
tags: [摄影机, 镜头, 画质, 电影感, 胶片, 数字, 拍摄设备, AI视频prompt, 好莱坞, 专业设备]
related_skills:
  - composes-with: color-grading-log-workflow — 不同摄影机的Log编码需要不同的调色流程
  - composes-with: color-grading-look-development — Look开发需要先确定摄影机色彩科学
  - composes-with: cinematography-back-lighting — 灯光风格与摄影机宽容度直接相关
  - composes-with: msv3-lens-emotion-mapping — 焦距选择与镜头情绪映射
  - composes-with: shot-design-angle-context — 角度选择需要考虑镜头特性
---

# 专业影视摄影机镜头锚定库 (Camera-Lens Anchoring)

## R — 原文 (Reading)

> AI训练数据绑定了大量真实电影画面到具体摄影机元数据。写"IMAX胶片 + Panavision C系列 35mm f/4"比写"电影质感、史诗级"有效10倍。具体型号是审美锚点，空泛形容词不是。
> — ai-shortfilm-prompts 方法论, methodology.zh.md
>
> 摄影机的选择不仅是技术决策，更是美学决策。ARRI Alexa的肤色渲染、RED的高分辨率裁切空间、Kodak胶片的颗粒感——每种媒介都有自己的"签名"。
> — Blain Brown, 《电影摄影》, p.42
>
> "Shot on [camera]" phrasing works best. Combining camera + lens + film stock in a triple-anchor gives the strongest control across all major AI video models.
> — AI 视频 prompt 实践报告, 2025-2026

## I — 方法论骨架 (Interpretation)

**核心原则：具体摄影机/镜头型号 > 空泛美学形容词。**

AI模型（无论是语言模型还是视频生成模型）的训练数据中，真实电影画面与摄影机元数据高度绑定。当你说"Panavision C系列"时，AI调用的是《星球大战》《银翼杀手2049》的画面记忆；当你说"电影质感"时，AI调用的是随机的高清素材。

**三层锚定体系：**
1. **摄影机** → 决定色彩科学、宽容度、噪点特征（数字 vs 胶片）
2. **镜头** → 决定焦外质感、色散、畸变风格
3. **设置** → 光圈、ISO/ASA、胶片感光度 → 决定景深、噪点、动态范围

**AI 视频模型响应差异（2025-2026 实测）：**
- **Sora / Veo 2**：对摄影机名称响应最强，"shot on ARRI Alexa" 能可靠产出电影感肤色和自然高光衰减
- **Seedance / Kling**：摄影机名称更多作为风格锚点，焦距描述（"35mm" vs "85mm"）比具体型号更有效
- **所有模型通用**：镜头焦距 > 摄影机型号 > 泛泛形容词。"Shot on Cooke S4 50mm" 比 "shot on ARRI" 更精准

## A1 — 过去案例 (Past Application)

### 案例 1: 史诗/大场面 — IMAX 胶片路线

**场景：** 末日战场，陨石划过天空，主角站在废墟上。
```
摄影机：IMAX 胶片摄影机 (15/70 格式)
镜头：Panavision C 系列变形宽银幕，35mm，f/4
胶片：Kodak Vision3 500T，低饱和灰蓝主调
参考影片：《敦刻尔克》《星际穿越》《沙丘》《奥本海默》
```
**为什么管用：** IMAX + Panavision C 系列是诺兰的标志性组合。AI训练数据中有大量诺兰电影画面，这个组合直接锚定到那种"真实的宏大感"。

### 案例 2: 赛博/硬科幻 — 高感光数字路线

**场景：** 霓虹街道，改造人主角在雨中行走。
```
摄影机：Sony Venice 2 (8.6K)，Rialto 分体
镜头：Canon K-35 改装定焦，35mm，f/2.8
色彩科学：S-Gamut3.Cine，后期偏青绿冷调
参考影片：《银翼杀手2049》《攻壳机动队》《曼达洛人》(部分场景)
```
**为什么管用：** Venice 双原生 ISO 2500 在霓虹灯下噪点极低。K-35 的柔和色散让霓虹光晕自然扩散，不会太"数码锐利"。

### 案例 3: 港风/武侠 — 胶片漂白路线

**场景：** 雨中小巷，刀客对决，慢动作水滴。
```
摄影机：Panaflex Millennium XL2 (35mm 胶片)
镜头：Cooke S4 定焦组，50mm，f/2
胶片：Kodak Vision3 500T，漂白旁路 (Bleach Bypass)
参考影片：《英雄》《花样年华》《一代宗师》《卧虎藏龙》
```
**为什么管用：** 漂白旁路是港片武侠的标志性后期工艺。Cooke 镜头的暖色调渲染 + 低饱和 + 胶片颗粒 = 王家卫/张艺谋的画面记忆。

### 案例 4: 纪录片/战地 — 手持数字路线

**场景：** 战地记者视角，混乱的街道，尘土飞扬。
```
摄影机：ARRI Alexa Mini，手持肩扛
镜头：Angenieux Optimo 24-290mm T2.8 变焦，偏广角端
设置：EI 1600，自然光为主，不做灯光修饰
参考影片：《拆弹部队》《93航班》《荒野猎人》(手持段落)
```
**为什么管用：** Alexa Mini 是好莱坞手持拍摄的主力机。变焦镜头的"新闻摄影机"画面记忆 + Alexa 的肤色渲染 = 纪实但不失电影感。

### 案例 5: 商业/奢侈品 — 大画幅浅景深路线

**场景：** 产品特写，模特面部，柔光环境。
```
摄影机：ARRI Alexa 65 (65mm 大画幅)
镜头：ARRI DNA 75mm，全开 T2.8
色彩科学：ARRI Wide Gamut / Log-C，后期偏暖
参考影片：Apple 产品视频、奢侈品广告、《荒野猎人》(自然光段落)
```
**为什么管用：** Alexa 65 的 65mm 传感器提供比全画幅更浅的景深和更柔和的焦外。这是好莱坞高端广告的终极武器。

### 案例 6: 恐怖/惊悚 — 16mm 粗粝路线

**场景：** 废弃医院，手电筒光束，角落里的影子。
```
摄影机：Aaton XTR Prod (Super 16mm 胶片)
镜头：Angenieux 12-240mm T3 变焦，偏广角端
胶片：Kodak Vision3 500T，高对比度，暗部偏绿
参考影片：《女巫布莱尔》《28天后》《遗传厄运》
```
**为什么管用：** 16mm 的粗粝颗粒 + 变焦镜头的"业余感" = 恐怖片的标志性质感。比写"阴森恐怖"有效10倍。

### 案例 7: 复古/怀旧 — 经典胶片路线

**场景：** 60 年代美国小镇，秋天，暖色调。
```
摄影机：Panavision Panaflex Gold II (35mm 胶片)
镜头：Cooke Speed Panchro 改装定焦，50mm
胶片：Kodak Vision3 200T，暖橙+海盐蓝
参考影片：《爱乐之城》《月光男孩》《水形物语》
```
**为什么管用：** Speed Panchro 是50-60年代好莱坞的标配镜头，改装后保留了经典的柔和焦外和微妙色散。配合 200T 的细腻颗粒 = 复古但不粗糙。

### 案例 8: 硬核动作 — 高分辨率数字路线

**场景：** 追车爆炸，碎片飞溅，高速摄影。
```
摄影机：RED V-Raptor [X] 8K VV
镜头：Leitz THALIA 定焦组，24mm，f/4
设置：8K 全画幅，后期可大幅裁切重构图
参考影片：《疯狂麦克斯：狂暴之路》《碟中谍7》《壮志凌云2》
```
**为什么管用：** RED 8K 的超高分辨率给后期重构图极大自由度——追车场景可以在后期重新选择画面重心。THALIA 的温暖有机质感中和了 RED 的"数码锐利"。

### 案例 9: 文艺/诗意 — 柔和肤色路线

**场景：** 沉默的角色特写，自然光从窗户洒入。
```
摄影机：ARRI Alexa 35 (ALEV 4 传感器)
镜头：Cooke Panchro/i 75mm，f/2
色彩科学：ARRI REVEAL Color Science，柔和肤色渲染
参考影片：《月光男孩》《罗马》《游牧人生》
```
**为什么管用：** Alexa 35 的 REVEAL 色彩科学是 ARRI 迄今最好的肤色渲染。Panchro/i 的经典 Cooke 暖调 + 75mm 的亲密压缩感 = 文艺片的视觉签名。

### 案例 10: 惊悚/悬疑 — 冷调高对比路线

**场景：** 空旷的豪宅，角色在走廊里缓慢行走。
```
摄影机：ARRI Alexa Mini LF
镜头：Zeiss Supreme Prime 27mm，f/1.4
色彩科学：Log-C，后期冷调去饱和，暗部细节保留
参考影片：《消失的爱人》《遗传厄运》《仲夏夜惊魂》
```
**为什么管用：** Supreme Prime 的临床锐利 + Alexa LF 的大画幅浅景深 = 一种"美丽但不安"的感觉。广角端轻微畸变增强了空间的压迫感。

### 案例 11: 虚拟制作/LED Volume

**场景：** LED 墙前拍摄，需要与虚拟背景无缝融合。
```
摄影机：Sony Venice 2 (8.6K) 或 ARRI Alexa 35
镜头：Zeiss Nano Prime (极低呼吸效应) 或 Cooke SP3
设置：匹配 LED 墙刷新率，避免摩尔纹
参考影片：《曼达洛人》《新蝙蝠侠》(部分场景)
```
**为什么管用：** LED Volume 要求镜头呼吸效应极低 + 摄影机与 LED 刷新率同步。Zeiss Nano Prime 专为此设计。

## A2 — 触发场景 (Future Trigger) ★

### 用户会在什么情境下需要这个 skill?

1. 用户在写 AI 视频 prompt，需要添加具体摄影机锚点
2. 用户问"用什么摄影机/镜头拍这个场景"
3. 用户描述了一个视觉风格但不知道用什么设备实现
4. 用户在做 Look 开发，需要先确定摄影机和镜头组合
5. 用户想模仿某部电影的画面质感
6. 用户在做虚拟制作/LED Volume 的设备选型

### 语言信号
- "用什么摄影机/镜头"
- "怎么拍出XX的感觉"
- "电影感/胶片感/数字感"
- "像XX电影那样的画面"
- "画质风格/视觉风格"
- "摄影机型号/镜头型号"
- "怎么写AI视频prompt才能出好画面"
- "好莱坞用什么设备"

## E — 可执行步骤 (Execution)

### 步骤 1: 确定美学目标

问用户（或从上下文推断）：
- 目标情绪？（史诗/亲密/恐怖/纪实/商业/文艺/惊悚）
- 参考影片？（如果有，直接查表）
- 媒介偏好？（胶片感 vs 数字感 vs 不在意）
- 预算级别？（好莱坞级 vs 独立制作）

### 步骤 2: 查表选择摄影机 + 镜头

从下方 **速查表** 中选择匹配的组合。优先级：
1. 有参考影片 → 直接查"按美学风格索引"
2. 有情绪关键词 → 查"适用场景"列
3. 都没有 → 用最通用的组合（ARRI Alexa 35 + Cooke S4/i）

### 步骤 3: 输出结构化锚定

按以下格式输出：
```
摄影机：[具体型号] + [传感器/胶片格式]
镜头：[品牌 + 系列 + 焦段 + 光圈]
色彩科学：[色彩空间 + 后期方向]
参考影片：[1-3 部电影]
```

### 步骤 4: 如用于 AI 视频 prompt，追加运镜和氛围

```
氛围画质：模拟[摄影机型号] + [镜头]（[焦段]，[光圈]）。[色彩描述]。
运镜：手持/斯坦尼康/固定，全程保持极其轻微的、如呼吸般的镜头浮动。
```

**AI prompt 黄金公式：** `shot on [摄影机], [镜头品牌+焦段], [胶片/色彩]`
例：`shot on ARRI Alexa 35, Cooke S4 50mm, Kodak Vision3 500T`

## B — 边界与盲点 (Boundary)

### 边界 1: AI 视频生成模型 ≠ 真实摄影机

Sora/Seedance/Kling 不是真的摄影机。写"ARRI Alexa"不会真的用 Alexa 拍摄——它只是给 AI 一个审美锚点。但这个锚点非常有效，因为 AI 训练数据中"ARRI Alexa"和"高质量肤色渲染"高度共现。

### 边界 2: 型号不是万能的

同一台摄影机在不同人手里出片天差地别。型号只决定了"底子"，灯光、构图、运动才是灵魂。不要让用户以为"买了 RED 就能拍出诺兰"。

### 边界 3: 胶片模拟 ≠ 胶片

写"模拟 Kodak 500T"和真的用胶片拍摄是两回事。数字后期模拟的胶片颗粒和真实胶片的化学颗粒在微观结构上不同。对于普通观众看不出区别，但对于专业调色师很重要。

### 边界 4: 经典设备的现代改装

很多经典镜头（如 Cooke Speed Panchro、Canon K-35、Zeiss Super Speed）原厂已停产，但通过 TLS、Zero Optik、Iron Glass 等改装厂重新上壳后可以用于现代 PL 卡口机身。改装后的光学特性保留原味，机械性能现代化。

### 作者盲点

本 skill 的知识来源是跨书综合 + ai-shortfilm-prompts 方法论 + 行业实践。推荐的设备组合以好莱坞主流实践为基准，对独立制作和亚洲市场的特殊需求覆盖有限。此外，AI视频生成模型的技术迭代极快，某些在2026年有效的锚定技巧可能在6个月后就过时了。

---

## 速查表

### 按美学风格索引（11 种风格 × 专业设备）

| 美学风格 | 摄影机 | 镜头 | 色彩/胶片 | 标志性参考 |
|----------|--------|------|-----------|-----------|
| 史诗/宏大 | IMAX 15/70 胶片机 | Panavision C 系列变形宽银幕 35mm f/4 | Kodak Vision3 500T，低饱和灰蓝 | 《敦刻尔克》《沙丘》《奥本海默》 |
| 赛博/硬科幻 | Sony Venice 2 8.6K | Canon K-35 改装 35mm f/2.8 | S-Gamut3.Cine 青绿冷调 | 《银翼杀手2049》《攻壳机动队》 |
| 港风/武侠 | Panaflex XL2 (35mm胶片) | Cooke S4 50mm f/2 | 漂白旁路，低饱和 | 《英雄》《花样年华》《一代宗师》 |
| 纪录/战地 | ARRI Alexa Mini | Angenieux Optimo 24-290mm T2.8 | Log-C，自然光 | 《拆弹部队》《93航班》 |
| 商业/奢侈品 | ARRI Alexa 65 (65mm) | ARRI DNA 75mm T2.8 | Log-C 暖调 | Apple 广告，奢侈品视频 |
| 恐怖/粗粝 | Aaton XTR Prod (S16mm) | Angenieux 12-240mm T3 | Kodak 500T 高对比偏绿 | 《女巫布莱尔》《遗传厄运》 |
| 复古/怀旧 | Panaflex Gold II (35mm胶片) | Cooke Speed Panchro 50mm | Kodak Vision3 200T 暖橙 | 《爱乐之城》《月光男孩》 |
| 硬核动作 | RED V-Raptor [X] 8K VV | Leitz THALIA 24mm f/4 | REDWideGamutRGB 高分辨率 | 《疯狂麦克斯》《碟中谍7》 |
| 文艺/诗意 | ARRI Alexa 35 | Cooke Panchro/i 75mm f/2 | REVEAL 柔和肤色 | 《月光男孩》《罗马》 |
| 惊悚/悬疑 | ARRI Alexa Mini LF | Zeiss Supreme Prime 27mm f/1.4 | Log-C 冷调去饱和 | 《消失的爱人》《仲夏夜惊魂》 |
| 虚拟制作/VP | Sony Venice 2 / Alexa 35 | Zeiss Nano Prime / Cooke SP3 | 匹配 LED 墙 | 《曼达洛人》《新蝙蝠侠》 |

### 按摄影机型号索引（好莱坞主力设备）

| 摄影机 | 传感器 | 分辨率 | 宽容度 | 原生ISO | 核心特征 | 最佳搭配镜头 | 典型用途 |
|--------|--------|--------|--------|---------|----------|-------------|----------|
| **ARRI Alexa 35** | Super 35 (ALEV 4) | 4.6K | 17档 | 800 | REVEAL色彩科学，肤色渲染最佳 | Cooke S4/i, Zeiss Supreme Prime | 剧情片，广告，流媒体 |
| **ARRI Alexa Mini LF** | 大画幅 | 4.5K | 14.5档 | 800 | 大画幅浅景深，好莱坞主力 | Cooke Panchro/i, Leitz THALIA | 商业，人像，剧情片 |
| **ARRI Alexa 65** | 65mm 大画幅 | 6.5K | 14+档 | 800 | 最大数字传感器，极致浅景深 | ARRI DNA, Hasselblad HC | 高端广告，大片 |
| **ARRI Alexa Mini** | Super 35 | 3.4K | 14+档 | 800 | 小巧轻便，手持/Steadicam 主力 | Angenieux Optimo, Zeiss Master Prime | 手持，纪录片，动作 |
| **RED V-Raptor [X] 8K** | VV 全画幅 | 8K | 17+档 | 800 | 超高分辨率，后期裁切自由 | Leitz THALIA, Angenieux EZ | 动作片，需要后期重构图 |
| **RED Komodo-X** | Super 35 | 6K | 16+档 | 800 | 全局快门，紧凑，防抖 | Sigma Cine, Tokina Vista | 车载，无人机，紧凑场景 |
| **Sony Venice 2** | 全画幅 | 8.6K/6K | 16+档 | 500/2500 或 800/3200 | 双原生ISO，高感光最强 | Canon K-35, Zeiss Supreme | 夜景，低光，科幻 |
| **Sony BURANO** | 全画幅 | 8.6K | 16档 | 800/3200 | 紧凑型CineAlta，IBIS+内置ND | Sony G Master, Cooke SP3 | 纪录片，紧凑制作 |
| **Canon EOS C400** | 全画幅 | 6K | 16+档 | 800/3200/12800 | 三原生ISO，RF卡口 | Canon CN-E RF, Flex Zoom | 纪录片，商业 |
| **Blackmagic URSA Cine 12K LF** | 大画幅 | 12K | 16档 | 800/3200 | 超高分辨率，BRAW内录 | Sigma Cine, Tokina Vista | 广告，MV，独立 |
| **Panaflex Millennium XL2** | 35mm 胶片 | — | ~14档 | ASA 50-500 | 好莱坞胶片时代主力 | Cooke S4, Panavision Primo | 胶片质感需求 |
| **Panavision Millennium DXL2** | 大画幅 (RED Monstro) | 8K | 16+档 | 800 | Panavision 色彩科学 | Primo 70 系列 | 大片，高端广告 |
| **IMAX MSM 9802** | 15/70 胶片 | ~18K等效 | ~15档 | ASA 500 | 最大胶片格式，极致分辨率 | Panavision C 系列 | IMAX 大片 |

### 按镜头品牌/系列索引（好莱坞常用）

| 镜头系列 | 卡口 | 覆盖 | 特征 | 色散/焦外 | 适合场景 | 典型用户 |
|----------|------|------|------|-----------|----------|----------|
| **Panavision C 系列** | PV (仅租赁) | 变形宽银幕 | 经典变形宽银幕，水平色散 | 椭圆焦外，水平光晕 | 史诗，科幻 | 诺兰、J.J. Abrams |
| **Panavision Primo 70** | PV (仅租赁) | 65mm 大画幅 | 极致锐利，大画幅覆盖 | 极低色散 | 高端广告，Alexa 65 | Roger Deakins |
| **Cooke S4/i** | PL | Super 35 | 温暖，柔和，"Cooke Look" | 低色散，奶油焦外 | 剧情片，文艺 | Emmanuel Lubezki |
| **Cooke Panchro/i** | PL | 全画幅 | Speed Panchro 的现代重生 | 经典柔和，微色散 | 复古，怀旧 | Bruno Delbonnel |
| **Cooke SP3** | RF/PL | 全画幅 | 新一代 Cooke，紧凑 | 低呼吸效应 | VP，紧凑制作 | 流媒体，VP |
| **Cooke Anamorphic/i FF** | PL | 变形宽银幕全画幅 | 现代变形宽银幕 | 2x 压缩，经典光晕 | 史诗，MV | Denis Villeneuve |
| **Zeiss Master Prime** | PL | Super 35 | 锐利，中性，T1.3 | 极低色散 | 惊悚，现代剧情 | David Fincher |
| **Zeiss Supreme Prime** | PL | 全画幅 | 锐利，高对比 | 极低色散 | VP，现代大片 | 《曼达洛人》 |
| **Zeiss Nano Prime** | PL/LPL | 全画幅 | 极紧凑，轻量 | 低呼吸效应 | VP，手持，Steadicam | VP 制作 |
| **Leitz THALIA** | PL | 全画幅 | 温暖，有机，微晕影 | 低色散，复古感 | 硬核动作，纪实 | Greig Fraser |
| **Leitz HUGO** | PL | 全画幅 | 紧凑，复古现代混合 | 中等色散 | 文艺，独立 | 新锐 DP |
| **Canon K-35** | PL (改装) | Super 35 | 柔和，微暖，复古 | 中等色散，复古光晕 | 赛博，夜景 | Hoyte van Hoytema |
| **Canon CN-E Primo** | PL/EF | 全画幅 | 锐利，可靠 | 低色散 | 纪录片，商业 | 纪录片 DP |
| **ARRI DNA** | PL (仅ARRI) | 65mm | 专为 Alexa 65 设计 | 柔和，自然 | 高端广告 | 高端广告 |
| **Angenieux Optimo** | PL | Super 35/全画幅 | 顶级变焦，灵活 | 中等色散 | 手持，纪录片 | 纪录片，动作 |
| **Angenieux EZ** | PL | 全画幅 | 性价比变焦 | 中等色散 | 独立，商业 | 独立制作 |
| **Sigma Cine High Speed** | PL/EF | 全画幅 | 锐利，性价比高 | 低色散 | 独立，A24 系 | 独立制作 |
| **Tokina Vista** | PL | 全画幅 | T1.5 大光圈，锐利 | 低色散 | 独立，商业 | 独立制作 |

### 按经典胶片/色彩锚定索引

| 胶片/色彩 | 特征 | 参考影片 | AI prompt 关键词 |
|-----------|------|----------|----------------|
| **Kodak Vision3 500T** | 高感光，颗粒明显，偏冷 | 《敦刻尔克》《黑暗骑士》 | `Kodak 500T film grain, cool tones` |
| **Kodak Vision3 250D** | 日光型，颗粒细腻，色彩饱和 | 《水形物语》《爱乐之城》 | `Kodak 250D, warm saturated daylight` |
| **Kodak Vision3 200T** | 颗粒极细腻，色彩丰富 | 《月光男孩》《爱乐之城》 | `Kodak 200T, fine grain, rich color` |
| **Kodak Ektachrome** | 反转片，高饱和，高对比 | 《荒野生存》 | `Ektachrome slide film, vivid saturated` |
| **Kodak Portra 400** | 肤色优化，柔和，低对比 | 人像摄影，文艺片 | `Portra 400, soft skin tones` |
| **Fujifilm Pro 400H** | 柔和，偏冷，低对比 | 日系文艺 | `Pro 400H, soft cool pastel` |
| **漂白旁路 (Bleach Bypass)** | 保留银粒子，低饱和，高对比 | 《拯救大兵瑞恩》《英雄》 | `bleach bypass, desaturated high contrast` |
| **交叉冲洗 (Cross Process)** | 色彩偏移，复古感 | MV，时尚摄影 | `cross processed, color shift` |
| **ARRI REVEAL** | Alexa 35 新色彩科学，肤色极佳 | 最新流媒体大片 | `ARRI REVEAL color science` |
| **ARRI Log-C4** | Alexa 35 新 Log 编码 | 2024-2026 大片 | `Log-C4, ARRI Wide Gamut 4` |

## 使用示例

### 示例 1: 写末日战场 AI 视频 prompt

```
用户：帮我写一个 15 秒的末日战场 prompt，要有史诗感。

→ 调用 camera-lens-anchoring

输出：
核心主题：写实末日战场 | 磅礴史诗 | 真人实景 | 杜绝CG感
氛围画质：变形宽荧幕电影质感。模拟 IMAX 胶片摄影机 + Panavision C 系列
        （焦段 35mm，光圈 f/4）。Kodak Vision3 500T 胶片颗粒，
        低饱和灰蓝主调，暗部信息压缩保留细节。
运镜：手持拍摄，全程保持极其轻微的、如呼吸般的镜头浮动。
参考：《敦刻尔克》开场海滩段落
```

### 示例 2: 夜景霓虹设备选型

```
用户：我在拍一个雨夜霓虹街道的场景，角色是改造人，想拍出赛博朋克的感觉。

→ 调用 camera-lens-anchoring

输出：
摄影机：Sony Venice 2 (8.6K)，Rialto 分体，方便手持
镜头：Canon K-35 改装定焦，35mm，f/2.8
色彩科学：Venice S-Gamut3.Cine，后期偏青绿冷调，暗部压低
参考影片：《银翼杀手2049》洛杉矶夜景段落

为什么选这个组合：
- Venice 双原生 ISO 2500 在霓虹灯下噪点极低
- K-35 的柔和色散让霓虹光晕自然扩散，不会太"数码锐利"
- 35mm 焦段在街头手持不抖，又能保留环境信息

AI prompt 版本：
shot on Sony Venice 2, Canon K-35 35mm, teal-and-orange color grade,
rain-soaked neon street, handheld with subtle breathing movement
```
