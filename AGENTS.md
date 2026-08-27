# AGENTS.md

AI 助手在本项目工作前必须读完此文件。兼容豆包、Codex、Claude、Cursor 等主流 AI 工具。

## 项目概述

AI 出海游戏热词站（DragonSword: Awakening），纯静态 HTML 多语言攻略站，部署于 Vercel。

## 项目结构

```
01-project-tutorials/   关卡教程原文（level0-6）
02-research-data/       调研产出（关键词、竞品分析）
03-content-materials/   素材库（27个页面素材 + 汇总表）
04-website/             网站代码（Git子模块，纯静态HTML，5语言）
05-operation-guides/    操作手册（14个文档，含工作流总览）
06-project-continuity/  项目延续手册（背景/方法/数据/AI交接/任务清单）
08-data-reviews/        数据复盘报告（按日期归档）
09-scripts/             Python工具脚本
.agents/skills/         AI技能文档（data-review/network-setup/playwright-cli/playwright-extension）
archive/                归档目录（07-homework/、09-screenshots/）
```

## 常用命令

```bash
# 本地预览网站
cd 04-website && python3 -m http.server 8000

# Git 操作（在 04-website/ 目录）
git add -A && git commit -m "描述" && git push origin main

# 连接用户 Chrome（需先读 .agents/skills/playwright-extension/SKILL.md）
PLAYWRIGHT_MCP_EXTENSION_TOKEN=<token> npx playwright cli -s=ga attach --extension=chrome
npx playwright cli -s=ga <command>   # 后续操作复用会话
npx playwright cli -s=ga detach      # 用完断开

# 页面 SEO 验证（在 04-website/ 目录）
python3 scripts/validate-pages.py           # 检查所有页面
python3 scripts/validate-pages.py en/kalien # 检查指定页面

# GitHub 推送（国内网络需走 ClashX 代理，SSH 已配置 443 端口代理）
git push origin main

# 飞书 API 遇 DNS 超时时设置代理（详见 .agents/skills/network-setup/SKILL.md）
export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890
```

## 浏览器自动化（Always）

- 用 `npx playwright cli -s=<session>` 连接用户 Chrome，用户可实时观察
- 操作前先读 `.agents/skills/playwright-extension/SKILL.md`
- 每步确认模式：highlight 目标 → 说明操作 → 等确认 → 执行
- 用完必须 `detach`；异常时 `kill-all`

## 浏览器自动化（Never）

- 禁止用 Python subprocess 直连 `@playwright/mcp`（会占满 sandbox 池）
- 禁止用 `npx playwright-cli`（正确是 `npx playwright cli`）
- 禁止在未 detach 的情况下长时间保持会话

## 教学方式（Always）

- 引导式教学：先讲概念（是什么、为什么），再讲操作（怎么做）
- 关键节点主动确认，接受用户实时纠错
- 事实性内容必须有真实来源，严禁编造

## 文件与目录（Always）

- 目录和文件用英文命名，命名要有意义
- 新文档放到对应目录，临时文件用完即删
- 运行时目录（`.playwright-cli/`、`.playwright-mcp/`、`node_modules/`）不提交 git

## 网站代码规范（Always）

- 纯静态 HTML/CSS/JS，无构建步骤，无框架
- GA 跟踪代码统一在 `js/analytics.js` 维护，所有 HTML 通过 `<script defer src=".../js/analytics.js"></script>` 引用
- canonical URL 统一为 `https://ds-guides.wiki/`（首页）；子页面必须包含语言目录，如 `https://ds-guides.wiki/en/beginner-guide.html`
- 多语言用子目录：`/en/`、`/zh/`、`/ko/`、`/ru/`、`/ja/`（英文首页在根目录 `/`，英文子页面在 `/en/`）
- 修改前先备份或确认 git 状态，避免覆盖用户工作

## SEO 红线与内容质量（Always）

- **TDH 红线**：页面拿到 Google 排名后，禁止修改 Title、Description、H1（"别改到大动脉上"）
- **已上线页面**：不频繁修改已有排名的页面；要补充内容就**新增内页**，不要动已有页面
- **素材采集深度**：采集同行页面时必须提取**完整正文**保存到本地，禁止只让 AI 总结摘要——摘要式输入必然导致摘要式输出（页面"看起来结构完整，实际一问一答两三句话，信息密度极低"）
- **内容厚度参考**：单页目标 600-800 英文单词（不设硬指标，作为信息密度参考）；不是所有页面都适合加表格/数据/步骤，不为凑字数强行添加
- **上线前质量检查**（4 项，独立 AI 检查而非建站 AI 自我评价）：
  1. 页面是不是只有一堆 H2 和摘要，没有把问题讲清楚？
  2. 有没有 AI 提示词、内部说明或测试内容泄漏到公开页面？
  3. 有没有提供正确的官方入口（Steam 链接、游戏官网等）？
  4. 网站有没有明显缺陷，页面是否真正解决搜索需求？
- **提取正文仅用于内部研究**：发布时仍需需求提炼 → 结构重组 → 事实核对 → 独立撰写 → 相似度检查，禁止换说法照抄同行原文

## 部署架构（Always）

- **Vercel**：托管网站（Hobby 免费计划），项目名 dragonsword-guides，push 到 main 自动部署
- **Cloudflare**：DNS 管理（Free 计划），代理状态为 DNS only（灰色云），不开启 Proxied
- **Spaceship**：域名注册商，nameserver 已指向 Cloudflare（celeste/thaddeus.ns.cloudflare.com）
- DNS 记录：A 记录 @ → 216.198.79.1；CNAME www → df9ecd0750052516.vercel-dns-017.com
- 域名：ds-guides.wiki（apex 为主域名直接服务；www 308 重定向到 ds-guides.wiki）
- **GA**：Measurement ID G-6XQCHB1YYV，代码在 `js/analytics.js`
- **GSC**：资源类型 sc-domain:ds-guides.wiki，通过 Cloudflare Domain Connect 验证，sitemap 已提交
- **内容补页节奏**：每 7-14 天查看 GSC 搜索词信号，对高 CTR/高展示但无落地页的词创建补页；下次复盘 2026-08-29
- **数据复盘节奏**：每周 GSC 快查，每两周 GA+GSC 完整复盘（读 `.agents/skills/data-review/SKILL.md`），每月加 SimilarWeb 竞品分析

## Git 提交规范（Always）

- Commit message 用英文，格式：`type: description`（如 `feat: add GA tracking`）
- 一个 commit 只做一件事
- 推送前确认 `.gitignore` 已排除临时文件

## 敏感操作（Ask First）

- 删除文件/目录、覆盖已有内容、强制推送（`git push -f`）
- 登录、支付、授权等需要用户账号的操作
- 修改域名 DNS、GA/GSC 设置
- 执行前必须说明影响范围，等用户确认

## 问题解决方法论（Always）

1. **先搜索再动手**：遇到不熟悉的问题，优先 Google 搜索官方文档/Stack Overflow/GitHub Issues，不要盲目试错
2. **结合 AI 判断**：将搜索结果与自身知识结合，分析根因而非表面修复
3. **查项目知识库**：搜索前先查本项目 `.agents/skills/` 和 `06-project-continuity/` 是否已有相关经验
4. **验证后再执行**：找到方案后先确认逻辑正确，再操作；操作后验证结果
5. **记录经验**：解决新问题后更新对应 skill 或文档，避免重复研究

## 网站迭代方法论（Always）

- **每轮只解决一类问题**：不要把内容、首页、埋点、语言和广告塞进同一次发布
- **迭代卡**：每轮开始前写五句话——只解决什么问题、做哪类修改、什么算有效、什么时候停、改坏了怎么恢复（详见 `05-operation-guides/12-网站迭代方法论.md`）
- **七轮迭代顺序**：质量基线 → 网址信号 → 玩家任务 → 首页入口 → 打开速度 → 测量校准 → 一次只改一类
- **GSC 数据分析**：效果→28天→查询→按展示排序→圈出高展示低点击词→对比前后28天确认持续需求→看Google拿哪页接→搜Google看前排形式→site:检查站内是否已有页面
- **GA4 首页分析**：探索→自由形式→着陆页+查询字符串→会话数+跳出率→过滤器会话数≥10→按跳出率排序
- **PageSpeed**：移动端优先，图片按实际尺寸输出，预告片点播放才加载，分析脚本不随意推迟（对照测试无收益就退回官方写法）

## 遇到问题时（Always）

- 工具报错时先读错误信息，定位根因而非绕过
- sandbox 异常时检查残留进程：`ps aux | grep playwright`
- 本文件未覆盖的事项，参考 `06-project-continuity/` 下的交接文档
