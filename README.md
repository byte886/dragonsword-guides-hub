# Project Directory Guide

> AI出海游戏热词站项目（DragonSword: Awakening）完整工作目录。
> 最后整理：2026-08-27

---

## 快速接手（新AI会话必读）

**新开一个AI会话（豆包/Claude/ChatGPT/Cursor等），让它按以下顺序阅读，3分钟即可接手整个项目：**

1. 读 `README.md`（本文件）→ 了解目录结构
2. 读 `05-operation-guides/14-项目工作流总览.md` → 了解完整工作流和文档关系
3. 读 `06-project-continuity/05-AI上下文交接指南.md` → 了解项目全貌和当前状态
4. 读 `06-project-continuity/01-项目背景与决策日志.md` → 理解为什么这么做

> 本文档集设计为**AI无关（AI-agnostic）**，兼容豆包、Claude、ChatGPT、Cursor/CODEX等多种AI环境。

---

## Directory Structure

```
new-chat/
├── README.md                       # 本文件：目录总说明
├── AGENTS.md                       # AI助手项目规则（兼容主流AI工具）
├── .gitmodules                     # Git子模块配置
├── .gitignore                      # Git忽略规则
│
├── 01-project-tutorials/           # 项目官方教程原文（level0-6）
├── 02-research-data/               # 关卡1-2调研产出（关键词、竞品分析）
├── 03-content-materials/           # 关卡3素材库（27个页面素材 + 汇总表）
├── 04-website/                     # 网站代码（Git子模块，纯静态HTML，5语言）
├── 05-operation-guides/            # 操作手册（可复现的SOP + 工作流总览）
├── 06-project-continuity/          # 项目延续手册（背景/方法/数据/AI交接/任务清单）
├── 08-data-reviews/                # 数据复盘报告（按日期归档）
├── 09-scripts/                     # Python工具脚本
│
├── .agents/skills/                 # AI技能文档（项目专用Skills）
│   ├── data-review/                # 数据复盘方法论Skill
│   ├── network-setup/              # 网络配置Skill
│   ├── playwright-cli/             # Playwright CLI参考
│   └── playwright-extension/       # Playwright Extension连接指南
│
└── archive/                        # 归档目录（已完成/不再使用的内容）
    ├── 07-homework/                # 关卡作业提交文件（已完成，不再提交）
    └── 09-screenshots/             # 开发过程截图（临时参考，已归档）
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
关卡3为每个页面搜集的素材，共27个页面 + 汇总表。
- `00-homepage.md` ~ `26-roxy.md`：各页面素材
- `materials-summary.md`：所有素材的清单和信息源统计

### 04-website/
网站主体代码（Git子模块，独立仓库：byte886/dragonsword-guides）。
- 纯静态HTML/CSS/JS，无构建步骤
- 5种语言：英/中/韩/俄/日
- `css/style.css`：全局样式
- `js/main.js`：全局脚本
- `js/analytics.js`：GA跟踪代码（统一维护）
- `assets/`：图片资源
- `sitemap.xml`、`robots.txt`：SEO文件

### 05-operation-guides/
**可复现的操作指南**，不是结论报告。新会话的AI照着步骤可以从零操作。

| 文档 | 内容 |
|------|------|
| `00-项目总览.md` | 文档使用指南、项目背景、通用原则 |
| `01-关卡1-选词操作指南.md` | 5步选词法 + 手动SERP验证铁律 |
| `02-关卡2-关键词操作指南.md` | 关键词挖掘+清洗+分类+页面矩阵 |
| `03-关卡3-素材搜集指南.md` | 五维来源检索+交叉核验+搜索意图匹配 |
| `04-信息源使用手册.md` | 如何检索、核验、更新信息源 |
| `05-移交说明.md` | 项目当前状态、下一步、快速开始模板 |
| `06-deployment-guide.md` | Vercel+Cloudflare+Spaceship 部署操作手册 |
| `07-ga-gsc-guide.md` | GA/GSC 接入与指标查看指南 |
| `08-ga-gsc-practice-handbook.md` | GA/GSC 实践手册（看过/没看过的功能页面） |
| `09-astro-migration-plan.md` | Astro迁移技术方案（待执行） |
| `10-post-launch-seo-playbook.md` | 上线后SEO操作手册 |
| `11-队员实战经验汇总.md` | 4位队员实战经验、踩坑教训、有效方法 |
| `12-网站迭代方法论.md` | 七轮迭代法（每轮只改一类，用数据验证） |
| `13-AI协作提示词模板.md` | AI立规矩提示词模板 + 本项目AI使用规范 |
| `14-项目工作流总览.md` | 完整工作流 + 文档关系索引（统一入口） |

### 06-project-continuity/
**项目过程/知识延续手册**。当调研方法、数据、需求发生变化时，确保AI能理解项目历史背景。

| 文档 | 内容 |
|------|------|
| `00-项目延续总览.md` | 文档定位和使用方法 |
| `01-项目背景与决策日志.md` | 项目历史、关键决策、为什么这么做、踩过的坑 |
| `02-方法论演进管理.md` | 调研方法变化时怎么记录和更新 |
| `03-数据资产更新管理.md` | 关键词、素材等数据的更新机制 |
| `04-新需求接入与范围管理.md` | 新功能/新方向怎么评估和融入 |
| `05-AI上下文交接指南.md` | 新窗口AI快速接手的标准流程 |
| `06-PRD产品说明文档.md` | 产品需求文档 |
| `07-开发要求文档.md` | 开发规范和要求 |
| `08-审核报告.md` | 第一次审核报告 |
| `09-最终审核报告.md` | 最终审核报告 |
| `10-content-relationship-map.md` | 内容关联关系图（维护一个内容时知道哪些需要调整） |
| `11-项目任务清单.md` | 当前任务清单和优先级 |

### 08-data-reviews/
数据复盘报告，按日期归档。
- `README.md`：数据复盘说明
- `2026-08-23-data-review.md`：第一次数据复盘
- `2026-08-25-data-review.md`：第二次数据复盘

### 09-scripts/
开发过程中使用的Python脚本。
- `fix_all_anchors.py`：批量修复锚点
- `fix_anchors.py`：修复锚点
- `generate_table.py`：生成表格

### .agents/skills/
项目专用AI技能文档。每个Skill包含SKILL.md和相关参考文件。
- `data-review/`：数据复盘方法论Skill
- `network-setup/`：网络配置Skill（代理设置等）
- `playwright-cli/`：Playwright CLI命令参考
- `playwright-extension/`：Playwright Extension连接用户Chrome的操作指南

### archive/
归档目录，存放已完成或不再使用的内容。
- `07-homework/`：关卡作业提交文件（已完成，不再提交新作业）
- `09-screenshots/`：开发过程截图（临时参考，已归档）

---

## 快速开始

### 场景1：新开窗口继续项目
1. 读 `05-operation-guides/14-项目工作流总览.md`（了解完整工作流）
2. 读 `06-project-continuity/05-AI上下文交接指南.md`（3分钟了解全貌）
3. 读 `06-project-continuity/11-项目任务清单.md`（了解当前任务）
4. 根据任务读对应操作手册

### 场景2：重新走调研流程（学习/复盘）
1. 读 `05-operation-guides/00-项目总览.md`
2. 按 01→02→03 顺序阅读操作指南
3. 参考 `02-research-data/` 和 `03-content-materials/` 中的实际成果

### 场景3：继续开发/部署
1. 读 `05-operation-guides/05-移交说明.md` 了解当前状态
2. 网站代码在 `04-website/`（Git子模块）
3. 部署相关读 `06-deployment-guide.md`

### 场景4：数据复盘
1. 读 `08-data-reviews/` 下的历史报告
2. 读 `.agents/skills/data-review/SKILL.md` 了解复盘方法论
3. GA/GSC指标查看读 `08-ga-gsc-practice-handbook.md`

### 场景5：更新内容/数据
1. 读 `06-project-continuity/03-数据资产更新管理.md`
2. 素材在 `03-content-materials/`
3. 内容关联关系查 `10-content-relationship-map.md`

### 场景6：在新AI会话开始
复制以下内容到新窗口：
```
我正在做AI出海游戏热词站项目（DragonSword: Awakening）。
项目目录在 /Users/wenjiechen/Doubao/chats/2026-08-08/new-chat/

请按以下顺序了解项目：
1. 先读 README.md 了解目录结构
2. 再读 05-operation-guides/14-项目工作流总览.md 了解完整工作流
3. 然后读 06-project-continuity/05-AI上下文交接指南.md 了解项目全貌
4. 最后读 06-project-continuity/11-项目任务清单.md 了解当前任务

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
| 域名 | ds-guides.wiki |
| 主仓库 | github.com/byte886/dragonsword-guides-hub（本项目） |
| 网站仓库 | github.com/byte886/dragonsword-guides（04-website子模块） |
| 部署平台 | Vercel（Hobby免费计划） |
| DNS | Cloudflare（Free计划，DNS only） |
| 域名注册 | Spaceship |
| GA Measurement ID | G-6XQCHB1YYV |
| GSC资源 | sc-domain:ds-guides.wiki |
| 网站语言 | 英文/中文/韩文/俄文/日文 |
| 当前进度 | 关卡6进行中（数据复盘优化阶段） |
| 网站状态 | 已上线，已接入GA/GSC，持续迭代中 |

---

## 用户偏好（操作时遵守）

- **引导式教学**：拒绝直接结论，偏好详细操作流程和方法论
- **严格流程**：多步骤任务禁止跳步，关键节点主动确认
- **数据支撑**：调研要求可量化数据、多方案对比、来源标注
- **素材真实**：所有事实性内容必须有真实来源，严禁AI编造
- **结构化输出**：要求严格的结构化格式
- **敏感操作**：登录、密码、支付等由用户手动完成
- **先搜索再动手**：遇到不熟悉的问题，优先Google搜索官方文档，不要盲目试错
- **每轮只改一类**：网站迭代遵循七轮迭代法，每次发布只改一类内容
