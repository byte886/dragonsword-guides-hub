# Project Directory Guide

> AI出海游戏热词站项目（DragonSword: Awakening）完整工作目录。
> 最后整理：2026-08-15

---

## 快速接手（新AI会话必读）

**新开一个AI会话（豆包/Claude/ChatGPT/Cursor等），让它按以下顺序阅读，3分钟即可接手整个项目：**

1. 读 `README.md`（本文件）→ 了解目录结构
2. 读 `06-project-continuity/05-AI上下文交接指南.md` → 了解项目全貌和当前状态
3. 读 `06-project-continuity/01-项目背景与决策日志.md` → 理解为什么这么做

> 本文档集设计为**AI无关（AI-agnostic）**，兼容豆包、Claude、ChatGPT、Cursor/CODEX等多种AI环境。不同环境的文件访问方式可能不同，但文档内容和操作流程完全一致。

---

## Directory Structure

```
new-chat/
├── README.md                    # 本文件：目录总说明
├── 01-project-tutorials/        # 项目官方教程原文（level0-6）
├── 02-research-data/            # 关卡1-2调研产出（关键词、竞品分析）
├── 03-content-materials/        # 关卡3素材库（23个页面素材 + 汇总表）
├── 04-website/                  # 关卡4网站产物（137个HTML，5种语言）
├── 05-operation-guides/         # 关卡1-3操作指南（可复现的SOP）
├── 06-project-continuity/       # 项目延续手册（背景/方法/数据/需求/AI交接）
├── 07-homework/                 # 关卡作业提交文件
├── 08-scripts/                  # Python工具脚本
└── 09-screenshots/              # 所有截图按用途分类
    ├── google-trends/           # Google Trends截图
    ├── similarweb/              # SimilarWeb截图
    ├── site-data/               # 竞品站点数据截图
    ├── homework-reference/      # 作业参考截图
    └── dev-process/             # 开发过程BUG截图
```

---

## 各目录说明

### 01-project-tutorials/
项目官方教程原文，包含.docx原始文件和提取的_text.txt文本文件。
- level0：开船前置（工具准备）
- level1：选游戏热词
- level2：规划页面矩阵
- level3：调研素材储备
- level4：AI生成内容+建站
- level5：网站部署上线
- level6：数据复盘优化

### 02-research-data/
关卡1和关卡2的调研产出数据。
- `competitor_analysis.md`：竞品分析
- `keywords.json`：关键词结构化数据
- `keywords_google_trends.md`：Google Trends关键词原始数据
- `keywords_similarweb.md`：SimilarWeb关键词原始数据
- `keywords-cleaning.md`：关键词清洗过程和最终清单

### 03-content-materials/
关卡3为每个页面搜集的素材，共23个页面 + 汇总表。
- `00-homepage.md` ~ `23-roadmap.md`：各页面素材
- `materials-summary.md`：所有素材的清单和信息源统计

### 04-website/
关卡4开发的网站主体，纯静态HTML/CSS/JS。
- 137个HTML页面（5种语言：英/中/韩/俄/日）
- `css/style.css`：全局样式
- `js/main.js`：全局脚本（主题切换、语言切换、锚点导航等）
- `assets/`：图片资源
- `sitemap.xml`、`robots.txt`：SEO文件
- PRD、开发要求、审核报告等文档见 `06-project-continuity/06~09`

### 05-operation-guides/
**可复现的操作指南**，不是结论报告。新会话的AI照着步骤可以从零操作。
- `00-项目总览.md`：文档使用指南、项目背景、通用原则
- `01-关卡1-选词操作指南.md`：5步选词法
- `02-关卡2-关键词操作指南.md`：关键词挖掘+清洗+分类+页面矩阵
- `03-关卡3-素材搜集指南.md`：五维来源检索+交叉核验+结构化整理
- `04-信息源使用手册.md`：如何检索、核验、更新信息源
- `05-移交说明.md`：项目当前状态、下一步、快速开始模板

### 06-project-continuity/
**项目过程/知识延续手册**。当调研方法、数据、需求发生变化时，确保AI能理解项目历史背景、操作过程和关键要点。
- `00-项目延续总览.md`：文档定位和使用方法
- `01-项目背景与决策日志.md`：项目历史、关键决策、为什么这么做、踩过的坑
- `02-方法论演进管理.md`：调研方法变化时怎么记录和更新
- `03-数据资产更新管理.md`：关键词、素材等数据的更新机制
- `04-新需求接入与范围管理.md`：新功能/新方向怎么评估和融入
- `05-AI上下文交接指南.md`：新窗口AI快速接手的标准流程

### 07-homework/
各关卡作业提交文件。
- `level2-homework.md`
- `level3-homework.html`
- `homework_table.html`

### 08-scripts/
开发过程中使用的Python脚本。
- `fix_all_anchors.py`：批量修复锚点
- `fix_anchors.py`：修复锚点
- `generate_table.py`：生成表格

### 09-screenshots/
所有截图按用途分类归档。

---

## 快速开始

### 场景1：新开窗口继续项目
1. 读 `06-project-continuity/05-AI上下文交接指南.md`（3分钟了解全貌）
2. 读 `06-project-continuity/01-项目背景与决策日志.md`（理解为什么这么做）
3. 根据任务读对应操作手册

### 场景2：重新走调研流程（学习/复盘）
1. 读 `05-operation-guides/00-项目总览.md`
2. 按 01→02→03 顺序阅读操作指南
3. 参考 `02-research-data/` 和 `03-content-materials/` 中的实际成果

### 场景3：继续开发/部署
1. 读 `05-operation-guides/05-移交说明.md` 了解当前状态
2. 网站代码在 `04-website/`

### 场景4：更新内容/数据
1. 读 `06-project-continuity/03-数据资产更新管理.md`
2. 素材在 `03-content-materials/`

### 场景5：有新需求/新方向
1. 读 `06-project-continuity/04-新需求接入与范围管理.md`
2. 按5步评估法评估后再执行

### 场景6：在新AI会话开始
复制以下内容到新窗口：
```
我正在做AI出海游戏热词站项目（DragonSword: Awakening）。
项目目录在 /Users/wenjiechen/Doubao/chats/2026-08-08/new-chat/

请按以下顺序了解项目：
1. 先读 README.md 了解目录结构
2. 再读 06-project-continuity/05-AI上下文交接指南.md 了解项目全貌
3. 然后读 06-project-continuity/01-项目背景与决策日志.md 理解为什么这么做

我们的任务是：[在此描述你的具体任务]
```

---

## 项目核心信息

| 项目 | 内容 |
|------|------|
| 选定游戏 | DragonSword: Awakening（龙之剑：觉醒） |
| 开发商 | Hound13 Inc（韩国） |
| Steam App ID | 4570720 |
| 发布日期 | 2026年7月23日 |
| 域名规划 | ds-guides.wiki |
| GitHub仓库 | dragonsword-guides |
| 网站语言 | 英文/中文/韩文/俄文/日文 |
| 页面数量 | 137个HTML |
| 当前进度 | 关卡4完成，待部署 |

---

## 用户偏好（操作时遵守）

- **引导式教学**：拒绝直接结论，偏好详细操作流程和方法论
- **严格流程**：多步骤任务禁止跳步，关键节点主动确认
- **数据支撑**：调研要求可量化数据、多方案对比、来源标注
- **素材真实**：所有事实性内容必须有真实来源，严禁AI编造
- **结构化输出**：要求严格的结构化格式
- **敏感操作**：登录、密码、支付等由用户手动完成
