# 数据复盘报告：GA + GSC

> 复盘日期：2026-08-25
> 数据周期：GA 过去 7 天（8/17-8/24）+ 28 天网页/事件（7/28-8/24）；GSC 过去 28 天（8/13-8/22）
> 工具：Google Analytics（G-6XQCHB1YYV）、Google Search Console（sc-domain:ds-guides.wiki）
> 上次复盘：2026-08-23（上线 8 天首次复盘）

---

## 1. 总览

上线 12 天，**7 天活跃用户 289 人（↑275%）**，自然搜索会话 262 次（↑1,915%），SEO 增长强劲。GSC 28 天累计 **208 次点击、4,332 次展示、CTR 4.8%、平均排名 7.8**。

本次复盘重点排查了四个问题：低 CTR 页面、美国机器人流量、deep_engagement 事件、未索引页面。已完成 3 个低 CTR 页面的 title/description 优化并推送部署。同时通过竞品对比发现重大内容缺口：**游戏有 19 个可玩角色，我们仅有 7 个角色页；Familiars（使魔/坐骑）系统完全空白。**

**评级：B** — SEO 增长趋势良好，内容缺口是当前最大瓶颈。

---

## 2. GA 数据分析

### 2.1 流量来源（过去 7 天，8/17-8/24）

| 渠道 | 会话数 | 环比变化 |
|------|--------|---------|
| 自然搜索（Organic Search） | 262 | ↑1,915% |
| 直接访问（Direct） | 116 | ↑66% |
| Bing | 16 | 新增 |
| Yahoo | 3 | 新增 |
| 引荐（Referral） | 0 | — |
| 社交（Social） | 0 | — |

**解读**：自然搜索爆发式增长，Bing/Yahoo 开始带来少量流量（Vercel 自动生成的 `og:image` meta 标签修复后 Bing 可以正常抓取）。引荐和社交仍为零。

### 2.2 热门页面（过去 28 天，7/28-8/24）

| 排名 | 页面 | 浏览量 | 用户数 | 人均页数 | 平均参与时间 | 解读 |
|------|------|--------|--------|---------|-------------|------|
| 1 | /（首页） | 113 | 101 | 1.12 | 10 秒 | 跳出率高，首屏需持续优化 |
| 2 | /en/characters.html | 28 | 22 | — | 13 秒 | 角色图鉴页 |
| 3 | /en/classes.html | 22 | 18 | — | 10 秒 | GSC 热门词落地页 |
| 4 | /en/lute.html | 21 | 17 | — | 20 秒 | GSC 展示最高（410），CTR 已优化 |
| 5 | /ru/build.html | 21 | 7 | 3.00 | 12 秒 | 俄文用户深度浏览 |
| 6 | /ko/gear.html | 20 | 8 | 2.50 | 1分34秒 | 全站最佳互动 |
| 7 | /en/build.html | 18 | 9 | 2.00 | 23 秒 | |
| 8 | /en/boss.html | 15 | 11 | — | 29 秒 | |
| 9 | /en/best-team.html | 13 | 7 | 1.86 | 1分51秒 | 高参与，CTR 已优化 |
| 10 | /en/endgame.html | 12 | 6 | — | 27 秒 | |
| 11 | /ko/karma.html | 9 | 6 | — | 43 秒 | 韩文 Karma 页 |
| 12 | /en/tier-list.html | 9 | 8 | — | 14 秒 | |
| 13 | /en/kalien.html | 7 | 5 | 1.40 | 21 秒 | 新角色页 |

**解读**：
- 韩文装备页（1分34秒）和 Best Team 页（1分51秒）互动最好，说明这些内容匹配用户需求
- 首页 10 秒仍是最大问题——8/23 已新增热门攻略板块，需观察后续数据
- 俄文用户人均浏览 3 页，说明俄文内容虽然量少但用户愿意深挖

### 2.3 国家/地区

**过去 7 天（8/17-8/24）：**

| 排名 | 国家 | 用户数 | 环比 | 解读 |
|------|------|--------|------|------|
| 1 | 美国 | 95 | ↑132% | 量大，含数据中心机器人流量 |
| 2 | 韩国 | 39 | ↑1,200% | 高质量市场 |
| 3 | 俄罗斯 | 27 | ↑1,250% | 高 CTR 市场 |
| 4 | 日本 | 26 | 新增 | 新兴市场 |
| 5 | 中国 | 10 | — | |
| 6 | 台湾 | 9 | — | |
| 7 | 德国 | 6 | — | |

**城市维度（疑似机器人）：**

| 城市 | 用户数 | 说明 |
|------|--------|------|
| Glenview, US | 24 | Google 数据中心所在地 |
| Council Bluffs, US | 16 | Google 数据中心所在地 |
| Boardman, US | 11 | Google 数据中心所在地 |
| Seoul, KR | 10 | 真实用户 |
| Shenzhen, CN | 6 | 真实用户 |

**解读**：美国前三大城市均为 Google 数据中心所在地，确认存在机器人/爬虫流量。GA4 默认已启用 IAB 机器人过滤，但数据中心流量不在过滤列表中。GA4 数据过滤器仅支持内部流量/开发者流量/主机名三种类型，无法直接按城市/IP 排除（需要 GTM）。随着真实流量增长，机器人占比会自然下降。

### 2.4 设备（GSC 数据，28 天）

| 设备 | 点击 | 展示 | CTR |
|------|------|------|-----|
| 桌面 | 140 | 3,205 | 4.4% |
| 移动 | 68 | 1,108 | 6.1% |

**解读**：移动 CTR 反而高于桌面，可能因为移动搜索结果中标题/描述展示更突出。桌面仍占 67% 点击。

### 2.5 事件与互动（过去 28 天）

| 事件 | 次数 | 用户数 | 用户占比 |
|------|------|--------|---------|
| page_view | 618 | 362 | 100% |
| session_start | 466 | 361 | 99.7% |
| first_visit | 366 | 361 | 99.7% |
| user_engagement | 384 | 193 | 53.3% |
| scroll | 114 | 78 | 21.5% |
| click（出站） | 6 | 5 | 1.4% |
| deep_engagement（关键事件） | 1 | 1 | 0.3% |

**解读**：
- 参与率 53.3%（上次 51.3%），略有提升
- 滚动率 21.5%（上次 20.9%），基本持平
- **deep_engagement 仅 1 次**：代码逻辑正确（sessionStorage 计数，第 3 页触发），但人均仅 1.70 页，大部分用户只看 1-2 页，达不到阈值。这是流量结构问题而非代码问题
- click 仅 6 次为出站点击（Steam/Discord 等），GA 增强衡量已确认开启全部 7 项，内部导航通过 page_view 跟踪

### 2.6 留存

| 指标 | 数值 |
|------|------|
| 新用户 | 361 |
| 回访用户 | 约 32（估算） |
| 回访率 | ~8.9% |

**解读**：与上次基本持平。攻略站回访率目标 >15%，需要持续更新内容和"最近更新"模块。

---

## 3. GSC 数据分析

### 3.1 搜索效果总览（28 天，8/13-8/22）

| 指标 | 本次（28天） | 上次（8天） | 变化 |
|------|-------------|------------|------|
| 点击次数 | 208 | 135 | +54% |
| 展示次数 | 4,332 | 2,870 | +51% |
| CTR | 4.8% | 4.7% | +0.1pp |
| 平均排名 | 7.8 | 7.8 | 持平 |

### 3.2 热门搜索词（28 天）

**高表现词：**

| 搜索词 | 点击 | 展示 | CTR | 落地页 |
|--------|------|------|-----|--------|
| dragonsword classes | 6 | 19 | 31.6% | /en/classes.html |
| dragonsword awakening classes | 3 | 31 | 9.7% | /en/classes.html |
| dragonsword awakening characters wiki | 3 | 10 | 30.0% | /en/characters.html |
| 드래곤소드 어웨이크닝 전용 카르마 | 2 | 33 | 6.1% | /ko/karma.html |
| kalien team | 2 | 6 | 33.3% | /en/best-team.html |
| dragonsword awakening roadmap | 1 | 36 | 2.8% | /en/roadmap.html |
| dragonsword awakening lute build | 1 | 28 | 3.6% | /en/lute.html |

**高展示低点击词（内容缺口/标题待优化）：**

| 搜索词 | 点击 | 展示 | CTR | 问题 |
|--------|------|------|-----|------|
| lute best karma | 0 | 14 | 0% | Lute 页缺少 Karma 推荐细节 |
| dragonsword awakening roxy build | 0 | 1+ | 0% | **无 Roxy 角色页** |
| ruinsbreaker | 0 | 有展示 | 0% | 装备套装名，Gear 页可能未覆盖 |
| lute ornette sion | 0 | 有展示 | 0% | 具体配队搜索，Best Team 页未按角色索引 |
| theresia best team | 0 | 1 | 0% | 配队需求 |
| kalien best team | 0 | 1 | 0% | 配队需求 |

### 3.3 热门页面（28 天）

| 页面 | 点击 | 展示 | CTR | 平均排名 | 状态 |
|------|------|------|-----|---------|------|
| /ru/gear.html | 16 | 102 | 15.7% | 5.8 | 优秀 |
| /en/classes.html | 15 | 124 | 12.1% | 4.1 | 优秀 |
| /en/lute.html | 13 | 410 | 3.2% | 5.3 | **已优化 title/description** |
| /en/boss.html | 10 | 137 | 7.3% | 9.4 | 良好 |
| /ko/endgame.html | 8 | 97 | 8.2% | 5.9 | 良好 |
| /ko/gear.html | 8 | 94 | 8.5% | 8.9 | 良好 |
| /ko/karma.html | 7 | 194 | 3.6% | 4.9 | **已优化 title/description** |
| /en/best-team.html | 7 | 169 | 4.1% | 8.2 | **已优化 title/description** |
| /en/characters.html | 7 | 87 | 8.0% | 9.0 | 良好 |
| /ru/build.html | 7 | 71 | 9.9% | 7.3 | 良好 |
| /en/roadmap.html | 4 | 132 | 3.0% | 10.8 | 排名靠后，CTR 低 |

### 3.4 国家/地区（GSC，28 天）

| 国家 | 点击 | 展示 | CTR |
|------|------|------|-----|
| 俄罗斯 | 49 | 347 | 14.1% |
| 韩国 | 44 | 806 | 5.5% |
| 美国 | 28 | 814 | 3.4% |
| 日本 | 23 | 204 | 11.3% |
| 中国 | 16 | 111 | 14.4% |
| 台湾 | 10 | 114 | 8.8% |
| 德国 | 8 | 103 | 7.8% |

**解读**：俄罗斯 CTR 最高（14.1%），韩国展示量最大（806）但 CTR 偏低（5.5%），美国展示量大但 CTR 仅 3.4%（含机器人流量影响）。

### 3.5 索引状态（截至 8/25）

| 状态 | 数量 | 说明 |
|------|------|------|
| 已编入索引 | 91 | |
| 未编入索引 | 41 | |
| — 网页会自动重定向 | 12 | www → 非 www 的 308，正常 |
| — 备用网页（有适当规范标记） | 4 | /index.html 形式 URL，canonical 正确，正常 |
| — 已发现-尚未编入索引 | 25 | Google 发现但未安排抓取，新站正常 |
| — 已抓取-尚未编入索引 | 0 | |

**已采取的行动**：
- 8/24 修复 sitemap.xml（语言首页 URL 从 `/zh/index.html` 改为 `/zh/`，与 canonical 一致）
- 8/24 重新提交非 www 版本 sitemap（状态：成功）
- 8/24 为 en/beginner-guide.html 请求索引（已加入优先队列）
- GSC 数据有 2-3 天延迟，8/24 的操作预计 8/27 后反映

---

## 4. 内容缺口分析（本次新增）

结合 GSC 搜索词、竞品对比（games.gg、Pro Game Guides、All Things How、Destructoid、dragon-sword-awakening.wiki 等）和项目素材搜集方法论，发现以下缺口：

### 4.1 缺失角色页（最高优先级）

游戏发售时有 **19 个可玩角色**，我们仅有 7 个角色页。竞品（allthings.how、Pro Game Guides、infernal-duck.com）均覆盖全部 19 个。

| 已有（7） | 缺失（12） | GSC 搜索信号 |
|-----------|-----------|-------------|
| Lute, Kalien, Ornette, Sion, Theresia, Charlotte, Reina | **Roxy**、Castella、Aria、Dana、Tarte、Cerese、Othello、Alex、Johnny、Astria、Kalsion（待确认是否=Kalien 异译）、第19人 | "dragonsword awakening roxy build" 已有展示 |

后续免费更新角色：Liza、Jerome、Veronica、Logan。

### 4.2 Familiars（使魔/坐骑）系统 — 完全空白

- 游戏有 29-30 个 Familiars，分 8 大类型，自带地形移动技能
- games.gg、Destructoid、Pro Game Guides、All Things How、VGTimes、九游都有专门的解锁指南
- 新 Wiki（dragon-sword-awakening.wiki）也有完整列表
- 应创建 `familiars.html` 系统页

### 4.3 竞品有但我们没有的长尾内容

| 内容 | 竞品来源 | 搜索潜力 |
|------|---------|---------|
| 如何解锁所有角色 | allthings.how, GladiatorBoost | "how to unlock characters" 类 |
| 资源刷取指南（Leaf of Vigor 等） | games.gg | 突破材料类 |
| 隐藏区域解锁（Shadowed Woods） | games.gg | 区域探索类 |
| 隐藏服装（Kalien's Secret Outfit） | games.gg | 收集类 |
| DLC/限时内容（Abyssal Direwolf，8/31 截止） | games.gg, allthings.how | 时效性流量 |
| Signal Skills / Switching Signals 机制 | dragon-sword-awakening.wiki | 战斗机制深度 |

### 4.4 现有页面需深化

| 页面 | 缺口 |
|------|------|
| lute.html | "best karma for lute" 14 展示 0 点击，需详细 Karma 推荐 |
| best-team.html | 需按角色索引配队（Kalien/Lute/Theresia 最佳队伍） |
| characters.html | 需补全 19 角色、解锁方式、阵营分类 |
| gear.html | "ruinsbreaker" 搜索词，需热门套装详细章节 |

### 4.5 素材文件缺口

`03-content-materials/` 缺少 4 个页面的素材文件：kalien、ornette、sion、tower-of-trials（关卡6新增页面未走素材搜集流程）。

---

## 5. 未查看的报告（及原因）

| 报告 | 工具 | 未看原因 | 何时需要看 |
|------|------|---------|-----------|
| 用户获取 | GA | 新站与会话渠道几乎一致 | 投放广告或 UTM 活动时 |
| 转化 | GA | deep_engagement 已配置但仅 1 次 | 数据积累后 |
| 广告 | GA | 没有投广告 | 接 AdSense/Adsterra 后 |
| 探索 | GA | 自定义分析，基础复盘不需要 | 漏斗/路径/分群分析时 |
| 落地页 | GA | 热门页面报告已覆盖 | 页面数 >50 时 |
| 电子商务 | GA | 纯内容站 | 永远不看 |
| 用户生命周期价值 | GA | 需长期数据 | 90 天后 |
| Core Web Vitals | GSC | 新站数据不足 | 30 天后月度检查 |
| 移动易用性 | GSC | 响应式 CSS 已适配 | 移动端异常时 |
| 链接报告 | GSC | 外链为零 | 开始反链建设后 |
| 安全问题/手动操作 | GSC | 正常应为空 | 每周扫一眼 |
| SimilarWeb | — | 站点太新（<10K 月访问） | 30 天后查竞品 |

---

## 6. 问题清单

### P0 — 紧急

1. **内容覆盖严重不足**：19 个角色仅 7 个有页面，Familiars 系统完全空白。GSC 已出现 "roxy build" 等搜索词但无落地页
2. **首页跳出率高**：101 用户、平均 10 秒，8/23 已优化首屏待验证效果

### P1 — 重要

3. **低 CTR 页面**：en/lute.html（3.2%）、ko/karma.html（3.6%）、en/best-team.html（4.1%）已优化 title/description（commit 2eb6de4），待观察效果
4. **美国机器人流量**：Glenview/Council Bluffs/Boardman 为数据中心城市。GA4 无法直接过滤，分析时手动排除，持续观察占比变化
5. **deep_engagement 仅 1 次**：代码正常，人均 1.70 页达不到 3 页阈值。需通过内链优化和内容关联提升人均页数
6. **25 个页面未索引**：已修复 sitemap 并重新提交，等待 Google 自然抓取

### P2 — 观察

7. **零引荐/社交流量**：游戏新站不急于外链（外链起效慢，热度窗口短）；确认长期价值后再启动，参考 `05-operation-guides/10-post-launch-seo-playbook.md`
8. **ja/ru/zh 新页面正文仍为英文**：元数据已翻译，正文待补充
9. **roadmap.html CTR 3.0%**：排名 10.8 偏后，标题可后续优化
10. **4 个页面缺素材文件**：kalien/ornette/sion/tower-of-trials 需补素材

---

## 7. 已完成的行动

| 日期 | 行动 | Commit |
|------|------|--------|
| 8/24 | 修复 sitemap.xml 语言首页 URL，重新提交 GSC | dfb32a3 |
| 8/24 | 为 en/beginner-guide.html 请求索引 | — |
| 8/25 | 优化 en/lute.html title/description（加入 Karma/Gear/Runes 关键词） | 2eb6de4 |
| 8/25 | 优化 ko/karma.html title/description（游戏名前置匹配搜索词） | 2eb6de4 |
| 8/25 | 优化 en/best-team.html title/description（加入具体英雄名） | 2eb6de4 |
| 8/25 | 确认 GA 增强衡量 7 项全部开启 | — |
| 8/25 | 确认 GA4 默认机器人过滤已启用，Internal Traffic 过滤器状态为"测试" | — |
| 8/25 | 确认 deep_engagement 代码逻辑正确（analytics.js sessionStorage 计数） | — |

---

## 8. 行动计划

### 本周（8/25-8/31）

- [ ] 创建 familiars.html（使魔系统页，5 语言）— 走素材搜集流程，五维来源检索
- [ ] 创建 roxy.html（Roxy 角色页，5 语言）— GSC 已有搜索信号
- [ ] 创建 castella.html（Castella 角色页，5 语言）— All Things How 评为 S 级
- [ ] 补充 kalien/ornette/sion/tower-of-trials 的素材文件
- [ ] 观察 3 个已优化页面的 CTR 变化（GSC 数据延迟 2-3 天）
- [ ] 检查 25 个未索引页面的最新状态（8/27 后）
- [ ] 用 Google Trends 确认游戏热度趋势，监控飙升词

### 两周内（9/1-9/14）

- [ ] 创建剩余缺失角色页：Aria、Dana、Tarte、Cerese、Othello、Alex、Johnny、Astria
- [ ] Lute 页增加详细 Karma 推荐章节（新增内容，不大改已有内容）
- [ ] Best Team 页按角色索引配队（新增章节）
- [ ] Characters 页补全 19 角色信息
- [ ] 从高流量页面（classes、gear、build）添加指向新页面的内链
- [ ] 补充 ja/ru/zh 新页面正文翻译（优先日文、俄文）
- [ ] 确认 Kalsion 是否为 Kalien 异译，统一命名
- [ ] 监控 Reddit/Discord/Steam 社区热门讨论，挖长尾词

### 30 天内（至 9/22）

- [ ] 第二次完整 GA+GSC 复盘（9/8）
- [ ] 用 SimilarWeb PRO 分析竞品流量和关键词差距
- [ ] 评估日访问是否达到 500+（Adsterra 门槛）
- [ ] 考虑 DLC/时效性内容（Abyssal Direwolf 8/31 截止后可做总结）
- [ ] 对数据好的页面新增多媒体内容（图片、图表）提升停留时长
- [ ] **外链暂不执行**：游戏新站热度窗口短，外链起效慢；确认网站有长期稳定流量后再启动（参考 `05-operation-guides/10-post-launch-seo-playbook.md`）

---

## 9. 下次复盘

- **GSC 快查**：2026-09-01（7 天后）
- **完整 GA+GSC 复盘**：2026-09-08（14 天后）
- **SimilarWeb 竞品分析**：2026-09-22（30 天后）
