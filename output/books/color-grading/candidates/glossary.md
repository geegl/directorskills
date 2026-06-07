# glossary.md — 调色专业术语

---

```yaml
id: g01
title: "Lift/Gamma/Gain（暗部/中间调/高光）"
type: glossary
source_chapter: 第3章
source_quote: "Lift工具可以提高或降低图像中最暗的部分。Gamma工具可以改变中间调的分布。Gain可以提高或降低白位。"
summary: 一级对比度调整的三大核心控件。Lift控制暗部（阴影），Gamma控制中间调分布，Gain控制高光（白位）。三者有交互性——大幅调整Lift会影响中间调甚至高光。通常先调Lift设定黑位，再调Gain设定白位，最后调Gamma平衡中间调。
tags: [核心工具, 对比度, 一级校色]
```

---

```yaml
id: g02
title: "HSL Qualifier（HSL选色/限定器）"
type: glossary
source_chapter: 第5章
source_quote: "二级调色的质量由键控的质量来决定。"
summary: 基于色相(Hue)、饱和度(Saturation)、亮度(Luminance)三个维度来选择图像中特定颜色区域的工具。通过调整三个维度的范围手柄和容差手柄来定义选区。是二级调色最常用的隔离工具。高质量素材（4:2:2以上）能产生更干净的键控边缘。
tags: [二级校色, 选色, 键控, HSL]
```

---

```yaml
id: g03
title: "Vectorscope（矢量示波器）"
type: glossary
source_chapter: 第4章、第8章
source_quote: "矢量示波器的色彩矢量校正设定为2倍放大率。"
summary: 显示图像色相（角度方向）和饱和度（离中心距离）的圆形示波器。中心代表无色彩（灰色），边缘代表完全饱和。标准靶位标示红(R)、黄(Yl)、绿(G)、青(Cy)、蓝(B)、品(Mg)六个方向。I-bar（肤色线）是判断肤色偏色的重要参考。
tags: [示波器, 色相, 饱和度, 色彩分析]
```

---

```yaml
id: g04
title: "Waveform Monitor（波形监视器）"
type: glossary
source_chapter: 第3章
source_quote: "当波形监视器设置成显示视频亮度，整体波形图的高度就是图像的反差。"
summary: 显示视频信号亮度分布的示波器。底部（0%）代表黑位，顶部（100%）代表白位。波形高度反映对比度范围。可设置为显示亮度(Luma)、RGB分量、色度(Chroma)等不同模式。是评估对比度、判断信号合法性的核心工具。
tags: [示波器, 亮度, 对比度, 广播安全]
```

---

```yaml
id: g05
title: "I-bar / 肤色线（Skin Tone Line）"
type: glossary
source_chapter: 第8章
source_quote: "矢量示波器的I-bar来协助判断，根据波形与I-bar的距离来修正肤色。"
summary: 矢量示波器上的一条参考线（同相轴线），约在33°位置（从品红向黄方向）。所有健康肤色的色相波形都会落在这条线附近。偏左（偏向黄/橙）通常表示亚洲或橄榄色肤色，偏右（偏向红）通常表示浅色或红润肤色。是快速判断肤色偏色的实用工具。
tags: [肤色, 矢量示波器, 参考线, 色彩平衡]
```

---

```yaml
id: g06
title: "Offset / Printer Points（通道偏移/光号）"
type: glossary
source_chapter: 第4章
source_quote: "Offset能马上重新平衡整个画面的影调。"
summary: Offset同时移动红绿蓝三个通道的值，整体提亮或压暗画面的同时改变色彩平衡。Printer Points允许单独调整每个通道。源自胶片时代配光机的光号概念。适用于处理严重偏色的素材，比分别调整暗部/中间调/高光更高效。
tags: [色彩平衡, 通道偏移, 配光, 一级校色]
```

---

```yaml
id: g07
title: "Log编码与正常化（Normalization）"
type: glossary
source_chapter: 第3章
source_quote: "Log编码素材的图像数据直接从图像传感器记录，不应用任何转换。"
summary: Log（对数）编码保留摄影机传感器的高动态范围数据（13-14档），但画面看起来低对比度、低饱和度。正常化是将Log数据转换到显示标准（如BT.709）的过程，通常通过LUT或手动调整实现。Log状态下做整体调整效果更平滑，正常化后做精细调整更有针对性。
tags: [Log编码, 正常化, 动态范围, LUT, 工作流]
```

---

```yaml
id: g08
title: "Broadcast Safe（广播安全/合法化）"
type: glossary
source_chapter: 第10章
source_quote: "如果被测量的信号的亮度和色度值在参考黑和参考白之间的规定范围内，那么，该视频信号就被认为是广播安全的。"
summary: 视频信号的亮度（0-100% IRE）和色度必须在规定范围内才能用于广播播出。超白（>100%）和超黑（<0%）信号需要被合法化。常用方法：降低Gain、使用广播安全滤镜、手动调整。10比特视频的合法范围通常是64-940码值。
tags: [质量控制, 信号标准, 合法化, IRE]
```

---

```yaml
id: g09
title: "Power Window / 形状遮罩（Shape Mask）"
type: glossary
source_chapter: 第6章
source_quote: "在需要调整的区域周围创建一个形状，通常是简单的椭圆或矩形。"
summary: 在画面上创建几何形状来限制调色影响范围的工具。基本形状包括椭圆、矩形、渐变。高级形状支持B样条和贝塞尔曲线绘制。可做羽化、运动跟踪、布尔运算组合。DaVinci Resolve中称为Power Window。用于暗角、补光、分区调色等。
tags: [二级校色, 遮罩, Power Window, 暗角]
```

---

```yaml
id: g10
title: "LUT（查找表/色彩映射表）"
type: glossary
source_chapter: 第2章、第3章
source_quote: "合并你正在使用的校准LUT文件和胶片模拟LUT文件。"
summary: Look-Up Table，将输入色彩值映射到输出色彩值的数学表格。用途：(1)校准LUT——使监视器符合显示标准；(2)创意LUT——模拟胶片或其他风格效果；(3)转换LUT——在不同色彩空间之间转换（如Log到BT.709）。是现代数字调色工作流的核心组件。
tags: [色彩管理, LUT, 色彩空间转换, 风格化]
```

---

```yaml
id: g11
title: "Contrast与Pivot工具"
type: glossary
source_chapter: 第3章
source_quote: "Pivot工具用于分配Contrast在黑位白位之间区域的权重。"
summary: Contrast同时线性改变黑位和白位扩展或压缩反差。Pivot控制Contrast的影响偏向——低Pivot值使高光更受影响，高Pivot值使暗部更受影响。比Lift/Gamma/Gain三件套更快实现整体反差调整，但可能裁切信号。适用于快速建立反差起点。
tags: [对比度, 快速工具, Pivot, 反差调整]
```

---

```yaml
id: g12
title: "色度采样（Chroma Subsampling）4:4:4/4:2:2/4:2:0"
type: glossary
source_chapter: 第5章
source_quote: "使用最高质量的视频素材，最好是未压缩的或具有最高色度采样的低压缩素材。"
summary: 描述视频信号中色度信息相对于亮度信息的采样比例。4:4:4=全色度（最佳）；4:2:2=半色度（专业标准）；4:2:0=四分之一色度（消费级）。色度采样越低，二级调色的键控边缘质量越差，越容易出现块状失真。
tags: [视频格式, 色度采样, 图像质量, 4:2:2]
```
