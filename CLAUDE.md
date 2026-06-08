# DirectorSkills — 项目上下文

> 10 本影视制作全流程书籍 → 97 个可执行 AI skills

## 项目结构

```
DirectorSkills/
├── README.md                          # 生产文档（使用指南、集成示例）
├── CLAUDE.md                          # 本文件（项目上下文）
├── LICENSE                            # MIT 许可证
├── docs/development.md                # 开发流程文档（方法论、Darwin 审计）
└── output/books/                      # 蒸馏产出（10 本书，97 个 skills）
    ├── story-design/                  # 8 skills  — 剧本结构
    ├── directing-masterclass/         # 15 skills — 导演思维
    ├── master-shots-v1/               # 6 skills  — 镜头技巧 Vol.1
    ├── master-shots-v2/               # 14 skills — 镜头技巧 Vol.2
    ├── master-shots-v3/               # 6 skills  — 镜头技巧 Vol.3
    ├── shot-design/                   # 8 skills  — 分镜设计
    ├── cinematography-brown/          # 7 skills  — 灯光摄影
    ├── color-grading/                 # 11 skills — 色彩调色
    ├── scene-transitions/             # 9 skills  — 场景转场
    └── sound-design/                  # 13 skills — 声音设计
```

## 10 本书清单

| # | 类别 | slug | 书名 | 作者 | Skills |
|---|------|------|------|------|--------|
| 1 | 剧本结构 | `story-design` | 《救猫咪》Save the Cat! | Blake Snyder | 8 |
| 2 | 导演思维 | `directing-masterclass` | 《电影导演大师课》On Film-making | Alexander Mackendrick | 15 |
| 3 | 镜头技巧 | `master-shots-v1` | 《大师镜头》第1卷 | Christopher Kenworthy | 6 |
| 4 | 镜头技巧 | `master-shots-v2` | 《大师镜头》第2卷 | Christopher Kenworthy | 14 |
| 5 | 镜头技巧 | `master-shots-v3` | 《大师镜头》第3卷 | Christopher Kenworthy | 6 |
| 6 | 分镜设计 | `shot-design` | 《电影镜头设计》Shot by Shot | Steven D. Katz | 8 |
| 7 | 灯光摄影 | `cinematography-brown` | 《电影摄影：理论与实践》 | Blain Brown | 7 |
| 8 | 色彩调色 | `color-grading` | 《调色师手册》第2版 | Alexis Van Hurkman | 11 |
| 9 | 场景转场 | `scene-transitions` | 《大师场景》Between the Scenes | Jeffrey Michael Bays | 9 |
| 10 | 声音设计 | `sound-design` | 《声音设计》Sound Design | David Sonnenschein | 13 |

## Submodules

- `.claude/skills/book2skill` — book2skill 蒸馏技能（kangarooking/cangjie-skill）
- `.hermes/skills/darwin-skill` — Darwin 质量进化技能（geegl/darwin-skill）

详细开发流程见 [docs/development.md](docs/development.md)。
