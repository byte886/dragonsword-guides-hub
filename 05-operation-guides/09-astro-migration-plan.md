# Astro 迁移技术方案

> 创建日期：2026-08-23
> 状态：待执行
> 目标：将纯 HTML 静态站迁移到 Astro 框架，解决公共代码维护问题，同时保持 SEO 和 URL 不变

## 一、选型决策

**选定框架：Astro（静态输出 + MDX 内容集合）**

### 选型依据

| 功能需求 | Astro 实现方式 | 需要 SSR |
|---------|--------------|---------|
| 站内搜索 | Pagefind（构建时索引，客户端搜索，零后端） | 否 |
| 玩家评论 | Giscus（基于 GitHub Discussions，免费） | 否 |
| 多语言内容增加 | Content Collections + MDX，构建快 | 否 |
| 广告变现 | BaseLayout 加 script，和现在一样 | 否 |
| 外部 API 游戏数据 | 构建时 fetch 生成静态页 + 客户端 island 实时刷新 | 否 |

### 为什么不选 Next.js

- Next.js SSG 即使无交互也发送约 60-115KB React 运行时 JS，影响 Core Web Vitals
- Astro 默认零 JS，Lighthouse 性能分 98-100（Next.js 需调优到 85-96）
- 所有功能需求均不需要 SSR/ISR/鉴权/数据库，Next.js 的全栈能力用不上
- Astro 构建 100+ 页面约 1-2 秒，Next.js 约 10-30 秒
- Astro 不绑定 Vercel，可部署到任何静态主机

### 为什么不选 SSR

- SSR 适合实时数据、个性化内容、鉴权页面——本项目均不需要
- SSR 每次请求实时渲染，TTFB 100-500ms，有服务器超时/报错风险
- SSG 预构建文件 CDN 毫秒级返回，无服务器宕机风险
- 攻略内容更新方式是"改代码 → push → 部署"，不需要实时渲染

## 二、项目结构

```
04-website/
├── astro.config.mjs          # Astro 配置（build.format: 'file' 保持 .html URL）
├── package.json
├── tsconfig.json
├── .gitignore                # 排除 node_modules、dist
├── public/
│   ├── robots.txt            # 直接复制现有
│   ├── images/               # 图片资源
│   └── js/
│       └── analytics.js      # GA 代码（保持独立文件）
├── src/
│   ├── layouts/
│   │   └── BaseLayout.astro  # 统一 head（title/description/canonical/hreflang/
│   │                         #   OG/JSON-LD/GA）+ navbar + footer
│   ├── components/
│   │   ├── Navbar.astro      # 导航栏（改一处全站生效）
│   │   ├── Footer.astro      # 页脚
│   │   ├── Sidebar.astro     # 侧边栏
│   │   ├── TableOfContents.astro
│   │   ├── CtaSection.astro  # CTA 卡片
│   │   ├── Callout.astro     # 提示框（MDX 中使用）
│   │   ├── AdSlot.astro      # 广告位组件
│   │   ├── CommentSection.astro  # Giscus 评论
│   │   └── Search.astro      # Pagefind 搜索框
│   ├── content/              # 内容集合（Markdown/MDX，AI 编写）
│   │   ├── config.ts         # 内容 schema 定义
│   │   ├── en/
│   │   │   ├── karma.mdx
│   │   │   ├── gear.mdx
│   │   │   └── ...
│   │   ├── ko/
│   │   ├── ja/
│   │   ├── ru/
│   │   └── zh/
│   ├── pages/
│   │   ├── index.astro       # 英文首页（保持 / URL）
│   │   └── [lang]/
│   │       └── [...slug].astro  # 动态路由：/en/karma.html 等
│   ├── styles/
│   │   └── global.css        # 现有 CSS 迁移
│   └── consts.ts             # 站点配置（导航、语言列表、GA ID）
```

## 三、URL 保持策略

关键配置 `astro.config.mjs`：

```js
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://ds-guides.wiki',
  output: 'static',
  build: {
    format: 'file',           // 生成 /en/karma.html 而不是 /en/karma/
  },
  integrations: [mdx(), sitemap()],
});
```

| 现有 URL | 迁移后 URL | 变化 |
|---------|-----------|------|
| `/` | `/` | 无 |
| `/en/karma.html` | `/en/karma.html` | 无 |
| `/ko/gear.html` | `/ko/gear.html` | 无 |
| `/sitemap.xml` | `/sitemap.xml` | 自动生成，内容一致 |
| `/robots.txt` | `/robots.txt` | 无 |

## 四、SEO 迁移方案

| 项目 | 方案 |
|------|------|
| title/description | BaseLayout 从 MDX frontmatter 读取，每个页面独立设置 |
| canonical | BaseLayout 自动生成：`https://ds-guides.wiki/{lang}/{slug}.html` |
| hreflang | BaseLayout 根据同 slug 的其他语言版本自动生成 `<link rel="alternate">` |
| Open Graph / Twitter Card | BaseLayout 统一模板，frontmatter 可覆盖 |
| JSON-LD 结构化数据 | BaseLayout 生成 Article/BreadcrumbList，frontmatter 传字段 |
| sitemap.xml | `@astrojs/sitemap` 自动生成，包含所有语言页面 |
| robots.txt | 放 public/ 直接复制 |
| GA 跟踪 | BaseLayout 引用 `/js/analytics.js`，和现在完全一致 |
| 内部链接 | 保持 `href="/en/karma.html"` 格式，无需修改 |
| 308 重定向 | 保持现有 Cloudflare/Vercel 配置不变 |

## 五、内容编写方式（给 AI 的 Markdown）

每个页面一个 MDX 文件，frontmatter 定义 SEO 元数据，正文用 Markdown 编写：

```mdx
---
title: "Best Karma & Ascension Guide"
description: "Learn how to farm, upgrade..."
language: "en"
slug: "karma"
updated: "2026-08-23"
---

## ⚡ Quick Answer

Karma is unlocked after...

## 📋 Character Overview

| Name | Kalien |
|------|--------|
| Faction | Red Fox |

<Callout type="tip">
  Prioritize ATK Power Up first.
</Callout>

<CtaSection />
```

AI 只需要写 Markdown 正文，不需要碰 HTML 结构、导航、footer。

## 六、功能实现方案

### 站内搜索（Pagefind）

- 构建后自动索引所有页面内容
- 零后端、零成本、支持多语言
- 添加一个搜索框组件，约 200KB JS（仅搜索时加载）

### 玩家评论（Giscus）

- 基于 GitHub Discussions，免费
- 评论数据存在 GitHub 仓库（byte886/dragonsword-guides）
- 支持多语言（跟随页面语言）
- 只需在内容页底部加一个组件

### 广告位（AdSlot 组件）

- BaseLayout 或内容页中预留广告位
- Adsterra/AdSense 代码集中管理
- 一个组件控制全站广告位置

### 外部 API 游戏数据

- 构建时获取：`astro build` 时 fetch API 数据生成静态表格（适合更新不频繁的数据）
- 客户端实时：用 `<script client:visible>` 在页面加载后 fetch（适合需要实时刷新的数据）
- 不需要 SSR 服务器

## 七、部署运维变化

| 项目 | 现在 | 迁移后 |
|------|------|--------|
| 构建 | 无（直接上传 HTML） | `astro build`（Vercel 自动执行） |
| Vercel 配置 | 静态文件 | 自动检测 Astro，零配置 |
| Node.js | 不需要 | Vercel 构建环境自带（18+） |
| DNS/Cloudflare | 不变 | 不变 |
| 域名 | 不变 | 不变 |
| GA/GSC | 不变 | 不变 |
| Git push 部署 | 不变 | 不变（push main 自动构建部署） |
| 本地预览 | `python3 -m http.server 8000` | `npm run dev`（支持热更新） |

### Vercel 免费额度对本项目的影响

| 限制项 | 免费额度 | 本项目用量 |
|--------|---------|-----------|
| 带宽 | 100 GB/月 | 约 500 MB/月，远低于限制 |
| 部署次数 | 100 次/天 | 个人使用足够 |
| 构建时间 | 45 分钟/次 | Astro 构建约 1-2 分钟 |
| 项目数 | 200 | 1 |
| 源文件数 | 15,000 | 约 100+ MDX + 组件 |

## 八、迁移步骤

| 步骤 | 内容 | 验证方式 |
|------|------|---------|
| 1 | 在 `astro-migration` 分支初始化 Astro 项目 | `npm run dev` 能看到默认页 |
| 2 | 迁移 CSS 到 src/styles/global.css | 页面样式一致 |
| 3 | 创建 BaseLayout（head + navbar + footer + GA） | 首页 HTML 结构正确 |
| 4 | 迁移首页为 index.astro | 本地访问 `/` 正常 |
| 5 | 配置 Content Collections + MDX | 能渲染 MDX 内容 |
| 6 | 创建动态路由 `[lang]/[...slug].astro` | `/en/karma.html` 可访问 |
| 7 | 批量转换 HTML 页面为 MDX（先转 5 个英文页验证） | 内容、表格、链接完整 |
| 8 | 验证 URL 格式（.html）和 SEO 标签 | curl 检查 head 标签 |
| 9 | 转换剩余所有页面（en/ko/ja/ru/zh） | 逐页对比 |
| 10 | 添加 sitemap 集成，对比新旧 sitemap | URL 数量和路径一致 |
| 11 | 推送到 Vercel 预览部署 | 预览 URL 全面检查 |
| 12 | 合并到 main，生产部署 | 线上验证 |
| 13 | GSC 重新提交 sitemap | GSC 无抓取错误 |

## 九、风险控制

| 风险 | 应对 |
|------|------|
| URL 变化导致 SEO 损失 | `build.format: 'file'` 保证 URL 不变；合并前用脚本对比新旧 sitemap |
| 页面内容遗漏 | 逐页对比迁移前后的 HTML 文本内容 |
| GA 数据中断 | BaseLayout 引用同一个 analytics.js，Measurement ID 不变 |
| CSS 样式丢失 | 先整体迁移 CSS，不做重构，视觉一致后再优化 |
| 迁移期间线上不受影响 | 在分支上操作，Vercel 预览部署验证通过后才合并 main |
| 回滚 | git revert 合并提交即可，Vercel 自动回滚部署 |

## 十、不做的事

- 不引入 React/Vue 等 UI 框架（除非搜索/评论组件需要，且仅作为 island 按需加载）
- 不使用 SSR 或 Vercel Functions（纯静态输出）
- 不重构 CSS（先迁移，后续优化）
- 不改变域名、DNS、Cloudflare 配置
- 不改变 GA/GSC 配置

## 参考资料

- Astro 官方文档：https://docs.astro.build/
- Astro on Vercel：https://examples.vercel.com/docs/frameworks/frontend/astro
- Content Collections：https://docs.astro.build/en/guides/content-collections/
- Pagefind：https://pagefind.app/
- Giscus：https://giscus.app/
- @astrojs/sitemap：https://docs.astro.build/en/guides/integrations-guide/sitemap/
