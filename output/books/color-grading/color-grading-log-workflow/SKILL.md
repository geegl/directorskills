---
name: color-grading-log-workflow
description: |
  当用户处理Log编码素材（RED/ARRI/Sony RAW等）时调用。核心流程：先在Log状态下用Offset做整体调整，再用Shadow/Midtone/Highlight做影调分区，套用LUT正常化后做精细调整。Log状态适合大刀阔斧，正常化后适合精雕细琢。
source_book: 《调色师手册》第2版 Alexis Van Hurkman
source_chapter: 第3章
tags: [Log编码, LUT, 正常化, 动态范围, RAW素材, 高宽容度]
related_skills:
  - composes-with: color-grading-primary-workflow (f01) — 正常化后的一级校色
  - composes-with: color-grading-lift-gamma-gain (g01) — 精细调整的工具
  - depends-on: color-grading-waveform-monitor (g04) — 评估信号范围
---

# Log编码素材调色流程

## R — 原文 (Reading)
> 对已经正常化的素材使用Shadow、Midtone、Highlight工具，你会发现，每个影调之间的重叠比较轻微，不是很实用。这就是在套用LUT之前，调整这些控件的原因。
> — Van Hurkman, 第3章

## I — 方法论骨架 (Interpretation)
Log编码素材保留了摄影机传感器的高动态范围（13-14档），但画面看起来低对比度、低饱和度。其调色需要特殊的两阶段工作流：

**阶段一：Log状态下**
- 使用Offset/Exposure做整体信号定位
- 使用Shadow/Midtone/Highlight做影调分区——在Log状态下这些控件的影响范围更宽、过渡更平滑，因为影调区之间有广泛重叠
- Pivot/Range控件可自定义影调区边界

**阶段二：正常化后**
- 套用LUT或手动正常化到BT.709
- 使用Lift/Gamma/Gain做精细对比度调整
- 使用色彩平衡控件做精细色彩校正

核心逻辑：Log状态下控件的行为类似于胶片配光，适合大范围调整；正常化后控件的行为更像传统视频调色，适合精细操作。

## A1 — 书中的应用 (Past Application)
### 案例：ARRI Alexa Log-C素材调色 (第3章)
- **问题**: RAW/Log素材看起来灰蒙蒙，动态范围远超BT.709显示能力
- **方法论的使用**: 先在Log状态用Offset整体定位，再用Shadow/Midtone/Highlight做初步影调，最后套LUT正常化后用Lift/Gamma/Gain精调
- **结论**: Log状态下的Shadow控件向中间调区域延伸更多，提供更平滑的过渡

## A2 — 触发场景 (Future Trigger) ★
1. 拿到Log编码素材（RED Log3G10/ARRI Log-C/Sony S-Log3）需要调色
2. 客户提供LUT需要在调色流程中集成
3. RAW素材反拜耳后看起来严重过曝但需要找回高光细节

### 语言信号
- "这是Log素材/RAW素材"、"需要套LUT"
- "画面看起来灰灰的/低对比度"
- "摄影机动态范围很大"

## E — 可执行步骤 (Execution)
1. **在Log状态做整体调整**——用Offset/Exposure定位信号范围
2. **用Shadow/Midtone/Highlight做影调分区**——利用Log状态下的宽重叠做平滑过渡
3. **套用LUT或正常化**——转换到目标显示标准
4. **用Lift/Gamma/Gain做精细调整**——此时控件影响更精确
5. **做色彩平衡和饱和度微调**


   - 🔴 判停条件: 若以上步骤无法完成或产出质量不达标，回到步骤1重新评估

## B — 边界 (Boundary) ★
- **不要在正常化后再用Shadow/Midtone/Highlight**——过渡会变得尖锐不自然
- **不要在Log状态下做精细色彩校正**——控件影响范围太宽，精度不够
- **失败模式**: 忘记在套LUT前做初步调整，导致正常化后丢失高光/暗部细节
