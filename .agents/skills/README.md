# 项目技能文档索引

> 本目录包含项目专用的 AI 技能（Skills）文档。每个 Skill 是一个可复用的领域能力，包含操作指南、工具使用方法和最佳实践。
> 最后更新：2026-08-27

---

## 技能列表

| 技能目录 | 功能 | 何时使用 | 核心内容 |
|---------|------|---------|---------|
| `data-review/` | 数据复盘方法论 | 需要对 GA/GSC/SimilarWeb 数据进行系统性复盘时 | 复盘框架、指标解读、行动建议、报告模板 |
| `network-setup/` | 网络配置 | 遇到网络问题、需要配置代理、ClashX 设置时 | 代理配置、国内/国外网络切换、常见网络问题排查 |
| `playwright-cli/` | Playwright CLI 参考 | 需要通过命令行操作浏览器、连接用户 Chrome 时 | CLI 命令参考、会话管理、截图/点击/导航操作 |
| `playwright-extension/` | Playwright Extension 连接 | 需要连接用户已打开的 Chrome 进行实时操作时 | Extension 安装、Token 配置、attach/detach 流程、常见问题 |

---

## 技能使用规范

### 1. 使用前必须阅读 SKILL.md

每个技能目录下都有 `SKILL.md` 文件，使用前必须完整阅读，了解：
- 技能的功能范围和限制
- 前置条件和依赖
- 具体操作步骤
- 常见问题和排查方法

### 2. 技能不是工具

技能文档是操作指南，不是可直接调用的工具。需要按照文档中的步骤，使用对应的工具（如 Bash、computer_use_tool 等）来执行操作。

### 3. 遇到问题先查技能文档

遇到相关领域的问题时，先搜索本目录下是否有相关技能文档，避免重复研究。

### 4. 更新技能文档

解决新问题后，如果发现技能文档有不足，应及时更新对应技能的 `SKILL.md`，避免下次重复踩坑。

---

## 技能详细说明

### data-review（数据复盘方法论）

**文件：** `data-review/SKILL.md`

**核心内容：**
- GA4 数据解读框架（用户获取、行为、转化）
- GSC 数据解读框架（效果、索引、站点地图）
- SimilarWeb 竞品分析方法
- 数据复盘报告模板
- 行动建议生成方法

**使用场景：**
- 每周/每两周的数据复盘
- 网站流量异常排查
- 竞品流量分析
- 生成数据复盘报告

---

### network-setup（网络配置）

**文件：** `network-setup/SKILL.md`

**核心内容：**
- ClashX 代理配置
- 国内/国外网络切换方法
- 终端代理命令设置
- 常见网络问题排查（DNS 超时、连接被拒等）
- GitHub/飞书/Google 等平台的网络适配

**使用场景：**
- 命令行推送失败（GitHub/飞书 API）
- 需要访问国外网站但 VPN 未开启
- 网络连接异常排查

---

### playwright-cli（Playwright CLI 参考）

**文件：** `playwright-cli/SKILL.md`
**参考文件：** `playwright-cli/references/` 目录下的命令参考

**核心内容：**
- Playwright CLI 安装和配置
- 会话管理（attach/detach/kill-all）
- 浏览器操作命令（导航、截图、点击、输入、滚动）
- 元素定位方法
- 常见问题排查

**使用场景：**
- 需要通过命令行自动化操作浏览器
- 连接用户 Chrome 进行实时操作
- 批量网页操作（截图、数据采集等）

---

### playwright-extension（Playwright Extension 连接）

**文件：** `playwright-extension/SKILL.md`

**核心内容：**
- Chrome Extension 安装方法
- Token 配置和刷新
- attach 连接用户已打开的 Chrome
- detach 断开连接
- 实时观察操作的方法
- 常见问题排查（sandbox 异常、连接失败等）

**使用场景：**
- 需要连接用户已打开的 Chrome（用户已登录账号）
- 需要用户实时观察操作过程
- 登录态敏感操作（GA/GSC/Cloudflare 等）

---

## 待补充技能（未来规划）

以下技能可能在未来需要补充：

| 潜在技能 | 功能 | 优先级 |
|---------|------|--------|
| `seo-optimization/` | SEO 优化方法论 | 中 |
| `content-creation/` | 内容创作规范和提示词模板 | 中 |
| `translation-workflow/` | 多语言翻译工作流 | 低 |
| `deployment-troubleshooting/` | 部署问题排查手册 | 低 |

---

## 相关文档

- 项目操作手册：`../../05-operation-guides/`
- 项目延续手册：`../../06-project-continuity/`
- 数据复盘报告：`../../08-data-reviews/`
