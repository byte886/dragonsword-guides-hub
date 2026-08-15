# AGENTS.md

AI 助手在本项目工作前必须读完此文件。兼容豆包、Codex、Claude、Cursor 等主流 AI 工具。

## 项目概述

AI 出海游戏热词站（DragonSword: Awakening），纯静态 HTML 多语言攻略站，部署于 Vercel。

## 项目结构

```
01-project-tutorials/   关卡教程文本
04-website/             网站代码（纯静态 HTML，5 语言，115 个文件）
06-project-continuity/  AI 上下文交接指南
07-homework/            关卡作业复盘
.agents/skills/         AI 技能文档（playwright-cli、playwright-extension）
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
- canonical URL 统一为 `https://ds-guides.wiki/`
- 多语言用子目录：`/en/`、`/zh/`、`/ko/`、`/ru/`、`/ja/`
- 修改前先备份或确认 git 状态，避免覆盖用户工作

## 部署架构（Always）

- **Vercel**：托管网站（Hobby 免费计划），项目名 dragonsword-guides，push 到 main 自动部署
- **Cloudflare**：DNS 管理（Free 计划），代理状态为 DNS only（灰色云），不开启 Proxied
- **Spaceship**：域名注册商，nameserver 已指向 Cloudflare（celeste/thaddeus.ns.cloudflare.com）
- DNS 记录：A 记录 @ → 216.198.79.1；CNAME www → cname.vercel-dns.com
- 域名：ds-guides.wiki（Vercel 中 ds-guides.wiki 308 重定向到 www.ds-guides.wiki）

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

## 遇到问题时（Always）

- 工具报错时先读错误信息，定位根因而非绕过
- sandbox 异常时检查残留进程：`ps aux | grep playwright`
- 本文件未覆盖的事项，参考 `06-project-continuity/` 下的交接文档
